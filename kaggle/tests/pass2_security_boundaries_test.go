package main

// Audit-only contracts beside SHA-matched source copies. Loopback HTTP, synthetic
// credentials and hash inputs. No provider/model/GPU/physical playback evidence.
import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
	"unicode/utf8"
)

func TestS2ProtectFailedAuthCannotConsumeOwnerOperationBudgets(t *testing.T) {
	g := testGuard(t)
	g.failed = newBucket(2, 0)
	g.all = newBucket(1, 0)
	g.speech = newBucket(1, 0)
	calls := 0
	h := g.middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { calls++; w.WriteHeader(204) }))
	for i, want := range []int{401, 401, 429, 429} {
		rr := httptest.NewRecorder()
		h.ServeHTTP(rr, httptest.NewRequest("POST", "/api/speak", strings.NewReader("{}")))
		if rr.Code != want || rr.Header().Get("Cache-Control") != "no-store" {
			t.Fatal(i, rr.Code)
		}
	}
	rr := httptest.NewRecorder()
	h.ServeHTTP(rr, authed("POST", "/api/speak", "{}"))
	if rr.Code != 204 || calls != 1 || len(g.speakSlots) != 0 || len(g.heavySlots) != 0 {
		t.Fatal("owner budget/slot affected")
	}
}

func TestS2ProtectTokenBucketConcurrentCapacityIsExact(t *testing.T) {
	b := newBucket(7, 0)
	var allowed atomic.Int32
	var wg sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			if b.allow() {
				allowed.Add(1)
			}
		}()
	}
	wg.Wait()
	if allowed.Load() != 7 || b.tokens != 0 {
		t.Fatal("capacity/race", allowed.Load(), b.tokens)
	}
}

func TestS2ProtectAllConfiguredBudgetEdgesFailClosed(t *testing.T) {
	for _, row := range []struct {
		name     string
		min, max int
	}{
		{"QTTS_MAX_TEXT_CHARS", 1, 200000}, {"QTTS_MAX_HISTORY_CHARS", 1, 200000},
		{"QTTS_MAX_SPEAK_CONCURRENT", 1, 8}, {"QTTS_MAX_HEAVY_CONCURRENT", 1, 8},
		{"QTTS_SPEAK_PER_MINUTE", 1, 120}, {"QTTS_REQUEST_TIMEOUT_S", 1, 7200},
		{"QTTS_MAX_JSON_BYTES", 1024, 4 << 20}, {"QTTS_MAX_UPLOAD_BYTES", 1024, 512 << 20},
	} {
		for _, n := range []int{row.min, row.max} {
			t.Setenv(row.name, fmt.Sprint(n))
			if _, err := loadLimits(); err != nil {
				t.Fatal(row.name, n, err)
			}
		}
		for _, raw := range []string{fmt.Sprint(row.min - 1), fmt.Sprint(row.max + 1), "1.5", "NaN", "99999999999999999999999999"} {
			t.Setenv(row.name, raw)
			if _, err := loadLimits(); err == nil {
				t.Fatal("accepted invalid limit", row.name, raw)
			}
		}
		t.Setenv(row.name, "")
	}
}

func TestS2ProtectHeavyAdmissionIndependentOfSpeechAndCancelReleases(t *testing.T) {
	g := testGuard(t)
	g.heavySlots = make(chan struct{}, 1)
	entered := make(chan struct{})
	done := make(chan struct{})
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	h := g.middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if strings.HasPrefix(r.URL.Path, "/api/prep/") {
			close(entered)
			<-r.Context().Done()
			w.WriteHeader(408)
			return
		}
		w.WriteHeader(204)
	}))
	go func() {
		defer close(done)
		h.ServeHTTP(httptest.NewRecorder(), authed("POST", "/api/prep/profiles", "{}").WithContext(ctx))
	}()
	t.Cleanup(func() { cancel(); p2Ready(t, done) })
	p2Ready(t, entered)
	rr := httptest.NewRecorder()
	h.ServeHTTP(rr, authed("DELETE", "/api/prep/profiles/x", "{}"))
	if rr.Code != 429 || rr.Header().Get("Retry-After") != "5" {
		t.Fatal("heavy admission", rr.Code)
	}
	rr = httptest.NewRecorder()
	h.ServeHTTP(rr, authed("POST", "/api/speak", "{}"))
	if rr.Code != 204 {
		t.Fatal("speech unnecessarily blocked", rr.Code)
	}
	cancel()
	p2Ready(t, done)
	if len(g.heavySlots) != 0 || len(g.speakSlots) != 0 {
		t.Fatal("slot retained after handler exit")
	}
}

func TestS2ProtectAdmissionDeferReleasesOnHandlerPanic(t *testing.T) {
	g := testGuard(t)
	g.speakSlots = make(chan struct{}, 1)
	first := true
	h := g.middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if first {
			first = false
			panic("synthetic handler panic")
		}
		w.WriteHeader(204)
	}))
	recovered := false
	func() {
		defer func() { recovered = recover() != nil }()
		h.ServeHTTP(httptest.NewRecorder(), authed("POST", "/api/speak", "{}"))
	}()
	if !recovered || len(g.speakSlots) != 0 {
		t.Fatal("panic did not unwind slot")
	}
	rr := httptest.NewRecorder()
	h.ServeHTTP(rr, authed("POST", "/api/speak", "{}"))
	if rr.Code != 204 {
		t.Fatal(rr.Code)
	}
}

func TestS2ProtectJSONBudgetExactBoundaryKnownAndUnknownLength(t *testing.T) {
	body := `{"text":"你a🧠"}`
	for _, unknown := range []bool{false, true} {
		for _, delta := range []int{0, -1} {
			g := testGuard(t)
			g.limits.JSONBytes = int64(len(body) + delta)
			h := g.middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
				var req SpeakReq
				if decodeJSON(w, r, &req) {
					if req.Text != "你a🧠" {
						t.Error("valid unicode changed")
					}
					w.WriteHeader(204)
				}
			}))
			req := authed("POST", "/api/speak", body)
			if unknown {
				req.ContentLength = -1
			}
			rr := httptest.NewRecorder()
			h.ServeHTTP(rr, req)
			want := 204
			if delta < 0 {
				want = 413
			}
			if rr.Code != want || len(g.speakSlots) != 0 {
				t.Fatal(unknown, delta, rr.Code)
			}
		}
	}
}

func TestS2ProtectCORSPreflightIsNotAnAPIAuthenticationBypass(t *testing.T) {
	g := testGuard(t)
	calls := 0
	h := cors(g.middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { calls++; w.WriteHeader(204) })))
	for _, row := range []struct {
		method, origin string
		want           int
	}{
		{"OPTIONS", "https://owner.example", 204}, {"OPTIONS", "https://other.example", 403},
		{"POST", "https://owner.example", 401}, {"POST", "https://other.example", 403}, {"POST", "", 401},
	} {
		req := httptest.NewRequest(row.method, "https://owner.example/api/report", nil)
		req.Header.Set("Origin", row.origin)
		rr := httptest.NewRecorder()
		h.ServeHTTP(rr, req)
		if rr.Code != row.want || rr.Header().Get("X-Content-Type-Options") != "nosniff" || rr.Header().Get("Access-Control-Allow-Origin") == "*" {
			t.Fatal(row, rr.Code)
		}
	}
	if calls != 0 {
		t.Fatal("unauthorized API handler invoked")
	}
	req := authed("POST", "https://owner.example/api/report", "{}")
	req.Header.Set("Origin", "https://owner.example")
	rr := httptest.NewRecorder()
	h.ServeHTTP(rr, req)
	if rr.Code != 204 || calls != 1 {
		t.Fatal("owner denied")
	}
}

func TestS2ProtectProxyRemovesAllCredentialHeaderValues(t *testing.T) {
	var calls atomic.Int32
	upstream := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls.Add(1)
		for _, name := range []string{"Authorization", "Proxy-Authorization", "Cookie", "X-DeepSeek-Key"} {
			if len(r.Header.Values(name)) != 0 {
				t.Error("credential values forwarded", name)
			}
		}
		raw, err := io.ReadAll(r.Body)
		if err != nil || string(raw) != "bounded-fixture" || r.URL.Path != "/libraries/"+strings.Repeat("a", 32)+"/samples" {
			t.Error("proxy request changed")
		}
		w.Write([]byte(`{"ok":true}`))
	}))
	defer upstream.Close()
	g := testGuard(t)
	a := &App{cfg: &Config{AnalystURL: upstream.URL}, guard: g}
	req := authed("POST", "/api/prep/libraries/"+strings.Repeat("a", 32)+"/samples", "bounded-fixture")
	for _, name := range []string{"Proxy-Authorization", "Cookie", "X-DeepSeek-Key"} {
		req.Header.Add(name, "synthetic-private-1")
		req.Header.Add(name, "synthetic-private-2")
	}
	rr := httptest.NewRecorder()
	g.middleware(a.proxy()).ServeHTTP(rr, req)
	if rr.Code != 200 || calls.Load() != 1 || strings.Contains(rr.Body.String(), "synthetic-private") {
		t.Fatal("proxy/redaction")
	}
}

func TestS2ProtectProxyCancellationReachesOwnedUpstreamAndRedactsError(t *testing.T) {
	entered, exited := make(chan struct{}), make(chan struct{})
	upstream := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		defer close(exited)
		io.Copy(io.Discard, r.Body)
		close(entered)
		<-r.Context().Done()
	}))
	defer upstream.Close()
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	a := &App{cfg: &Config{AnalystURL: upstream.URL}, guard: testGuard(t)}
	done := make(chan struct{})
	rr := httptest.NewRecorder()
	go func() {
		defer close(done)
		a.guard.middleware(a.proxy()).ServeHTTP(rr, authed("POST", "/api/prep/profiles", "bounded").WithContext(ctx))
	}()
	t.Cleanup(func() { cancel(); p2Ready(t, done); p2Ready(t, exited) })
	p2Ready(t, entered)
	cancel()
	p2Ready(t, done)
	p2Ready(t, exited)
	if rr.Code != 502 || strings.Contains(rr.Body.String(), upstream.URL) || len(a.guard.heavySlots) != 0 {
		t.Fatal("cancellation/error privacy", rr.Code)
	}
}

func TestS2ProtectSpeakRuneHistoryAndSystemEdges(t *testing.T) {
	l := defaultLimits()
	l.TextChars = 3
	l.HistoryChars = 3
	valid := SpeakReq{Text: "你a🧠", History: []ChatMsg{{Role: "user", Content: "你a🧠"}}, System: strings.Repeat("🧠", 4096)}
	if err := validateSpeak(valid, l); err != nil {
		t.Fatal(err)
	}
	for _, kind := range []string{"text", "history", "system", "roles", "count", "invalid-utf8"} {
		req := valid
		req.History = append([]ChatMsg(nil), valid.History...)
		switch kind {
		case "text":
			req.Text += "x"
		case "history":
			req.History[0].Content += "x"
		case "system":
			req.System += "x"
		case "roles":
			req.History[0].Role = "system"
		case "count":
			req.History = make([]ChatMsg, 17)
		case "invalid-utf8":
			req.Text = string([]byte{0xff})
		}
		if err := validateSpeak(req, l); err == nil {
			t.Fatal("accepted invalid budget/role/text", kind)
		}
	}
}

func TestS2ObservedMalformedUnicodeBecomesAcceptedReplacementText(t *testing.T) {
	g := testGuard(t)
	g.limits.TextChars = 3
	h := g.middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		var req SpeakReq
		if !decodeJSON(w, r, &req) {
			return
		}
		if err := validateSpeak(req, g.limits); err != nil {
			writeJSON(w, 400, map[string]string{"error": err.Error()})
			return
		}
		writeJSON(w, 200, map[string]any{"text": req.Text, "valid_utf8_after_decode": utf8.ValidString(req.Text)})
	}))
	server := httptest.NewServer(h)
	defer server.Close()
	client := &http.Client{Timeout: 5 * time.Second}
	bodies := [][]byte{[]byte(`{"text":"a\ud800b"}`), []byte(`{"text":"a\udc00b"}`), append(append([]byte(`{"text":"a`), 0xff), []byte(`b"}`)...)}
	for _, body := range bodies {
		req, err := http.NewRequest("POST", server.URL+"/api/speak", bytes.NewReader(body))
		if err != nil {
			t.Fatal(err)
		}
		req.Header.Set("Authorization", "Bearer "+testAccessToken)
		res, err := client.Do(req)
		if err != nil {
			t.Fatal(err)
		}
		var row struct {
			Text  string `json:"text"`
			Valid bool   `json:"valid_utf8_after_decode"`
		}
		err = json.NewDecoder(res.Body).Decode(&row)
		res.Body.Close()
		if err != nil || res.StatusCode != 200 || row.Text != "a�b" || !row.Valid {
			t.Fatal("Unicode witness changed", res.StatusCode, row, err)
		}
	}
	t.Log(`OBSERVED_NOT_FIXED F29: original guard/decodeJSON/validateSpeak accepts isolated high/low surrogate and invalid UTF8 wire as replacement text; actual local HTTP, composite validation handler only, no synthesis`)
}

func TestS2ObservedProviderHTTPErrorExposesSyntheticServerKeyInClientFrames(t *testing.T) {
	const key = "synthetic-server-only-key-not-a-real-credential"
	var calls atomic.Int32
	provider := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls.Add(1)
		if r.Header.Get("Authorization") != "Bearer "+key {
			t.Error("server key not selected")
		}
		io.Copy(io.Discard, r.Body)
		w.WriteHeader(401)
		fmt.Fprint(w, "synthetic-private-provider-detail Authorization=", r.Header.Get("Authorization"), strings.Repeat("Z", 1000))
	}))
	defer provider.Close()
	root, _ := p2Profile(t)
	a := &App{cfg: &Config{StateDir: root, WebDir: root, AnalystURL: "http://127.0.0.1:1", LLMBase: provider.URL, LLMModel: "fixture", LLMKey: key, LLMMaxTokens: 8192}, guard: testGuard(t), sched: NewScheduler(nil), metrics: NewMetrics()}
	server := httptest.NewServer(a.routes())
	defer server.Close()
	client := &http.Client{Timeout: 5 * time.Second}
	req, err := http.NewRequest("POST", server.URL+"/api/speak", strings.NewReader(`{"mode":"chat","profile":"fixture","text":"fixture"}`))
	if err != nil {
		t.Fatal(err)
	}
	req.Header.Set("Authorization", "Bearer "+testAccessToken) // no X-DeepSeek-Key; use configured server key
	res, err := client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	raw, err := io.ReadAll(io.LimitReader(res.Body, 16<<10))
	res.Body.Close()
	if err != nil || res.StatusCode != 200 {
		t.Fatal(res.StatusCode, err)
	}
	errors, ends := 0, 0
	for _, frame := range p2Decode(t, raw) {
		if frame.kind == cPCM || frame.kind == cText {
			t.Fatal("unexpected generated text/PCM")
		}
		if frame.kind == cError {
			errors++
			if !bytes.Contains(frame.raw, []byte(key)) || !bytes.Contains(frame.raw, []byte("synthetic-private-provider-detail")) {
				t.Fatal("expected exposure absent")
			}
		}
		if frame.kind == cEnd {
			ends++
			if !bytes.Contains(frame.raw, []byte(key)) {
				t.Fatal("END did not retain raw error")
			}
		}
	}
	snapshot, _ := json.Marshal(a.metrics.snapshot())
	if calls.Load() != 1 || errors != 1 || ends != 1 || !bytes.Contains(snapshot, []byte(key)) || len(a.guard.speakSlots) != 0 {
		t.Fatal("exposure/accounting changed", calls.Load(), errors, ends)
	}
	t.Log(`OBSERVED_NOT_FIXED F30: provider HTTP401 raw body echoed synthetic configured key into client ERROR/END and metrics; real authenticated gateway/local HTTP, malicious/error provider fixture, no real secret/provider/model/GPU`)
}
