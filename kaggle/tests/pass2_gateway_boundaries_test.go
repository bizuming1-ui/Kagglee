package main

// Compile only beside SHA-matched copied product sources and old G0 contracts.
// CPU/HTTP/files/protocol fixtures; never real DeepSeek, Qwen, GPU or audio playback.
import (
	"bytes"
	"context"
	"encoding/binary"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"sync/atomic"
	"testing"
	"time"
)

func p2Session(t *testing.T, s *Scheduler) *Session {
	t.Helper()
	session := (&App{sched: s}).newSession(context.Background(), SpeakReq{Mode: "read"}, &ProfileInfo{ID: "fixture", VoiceBinding: strings.Repeat("a", 64), VoiceConditioning: "icl-generated-only-codec"})
	t.Cleanup(session.cancel)
	return session
}
func p2Job(session *Session, index int) *Job {
	return &Job{sess: session, seg: Segment{Index: index, Text: "fixture"}, buf: &SegBuf{wake: session.wake}, tried: map[int]bool{}, enq: time.Now()}
}
func p2Ready(t *testing.T, ch <-chan struct{}) {
	t.Helper()
	select {
	case <-ch:
	case <-time.After(5 * time.Second):
		t.Fatal("owned fixture deadline")
	}
}

type p2Wire struct {
	kind  byte
	index uint32
	raw   []byte
}

func p2Decode(t *testing.T, raw []byte) []p2Wire {
	t.Helper()
	var frames []p2Wire
	for len(raw) > 0 {
		if len(raw) < 9 {
			t.Fatal("partial client header")
		}
		n := int(binary.LittleEndian.Uint32(raw[5:9]))
		if n > len(raw)-9 {
			t.Fatal("partial client payload")
		}
		frames = append(frames, p2Wire{raw[0], binary.LittleEndian.Uint32(raw[1:5]), append([]byte(nil), raw[9:9+n]...)})
		raw = raw[9+n:]
	}
	return frames
}
func p2Profile(t *testing.T) (string, *ProfileInfo) {
	t.Helper()
	t.Setenv("QTTS_MOCK", "0")
	t.Setenv("QTTS_TTS_ENGINE", "faster")
	t.Setenv("QTTS_CLONE_MODE", "icl")
	root := t.TempDir()
	dir := filepath.Join(root, "profiles", "fixture")
	if err := os.MkdirAll(dir, 0700); err != nil {
		t.Fatal(err)
	}
	p := &ProfileInfo{ID: "fixture", Anchor: "ref.wav", RefText: "fixture reference", Language: "English"}
	raw, _ := json.Marshal(p)
	if err := os.WriteFile(filepath.Join(dir, "profile.json"), raw, 0600); err != nil {
		t.Fatal(err)
	}
	// Hash fixture only: deliberately not a decodable WAV/model reference.
	if err := os.WriteFile(filepath.Join(dir, "ref.wav"), []byte("synthetic hash input, not audio"), 0600); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(root, "active.json"), []byte(`{"id":"previous"}`), 0600); err != nil {
		t.Fatal(err)
	}
	initial, err := loadProfileInfo(root, "fixture")
	if err != nil {
		t.Fatal(err)
	}
	return root, initial
}

func TestP2ProtectRetryDropsUnconsumedPCMAndSelectsOtherWorker(t *testing.T) {
	first := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		w.Write(append(g0Frame(fPCM, []byte{1, 0, 2, 0}), g0Frame(fStats, []byte(`{"failed":true}`))...))
	}))
	defer first.Close()
	second := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		w.Write(append(g0Frame(fPCM, []byte{3, 0}), g0Stats()...))
	}))
	defer second.Close()
	s := NewScheduler([]string{first.URL, second.URL})
	session := p2Session(t, s)
	job := p2Job(session, 0)
	for _, w := range s.workers {
		w.healthy = true
	}
	s.run(s.workers[0], job)
	if job.attempts != 1 || !job.tried[0] || session.produced != 0 || job.buf.samples != 0 || len(s.jobs) != 1 {
		t.Fatal("retry accounting")
	}
	s.mu.Lock()
	wrong := s.pickLocked(s.workers[0])
	next := s.pickLocked(s.workers[1])
	s.mu.Unlock()
	if wrong != nil || next != job {
		t.Fatal("other worker preference")
	}
	s.run(s.workers[1], next)
	frames, done, err, stats := job.buf.take()
	if !done || err != "" || len(frames) != 1 || !bytes.Equal(frames[0], []byte{3, 0}) || session.produced != 1 || stats["attempts"] != 2 || s.workers[0].busy || s.workers[1].busy {
		t.Fatal("retry result")
	}
}

func TestP2ProtectConsumedPCMFailureCannotReplayOrRetry(t *testing.T) {
	release := make(chan struct{})
	var released atomic.Bool
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		w.Write(g0Frame(fPCM, []byte{1, 0}))
		w.(http.Flusher).Flush()
		select {
		case <-release:
		case <-r.Context().Done():
			return
		}
		w.Write(g0Frame(fErr, []byte(`{"error":"fixture failed after PCM"}`)))
	}))
	defer server.Close()
	defer func() {
		if released.CompareAndSwap(false, true) {
			close(release)
		}
	}()
	s := NewScheduler([]string{server.URL})
	session := p2Session(t, s)
	job := p2Job(session, 0)
	done := make(chan struct{})
	go func() { s.run(s.workers[0], job); close(done) }()
	defer func() { session.cancel(); p2Ready(t, done) }()
	p2Ready(t, session.wake)
	frames, finished, _, _ := job.buf.take()
	if finished || len(frames) != 1 {
		t.Fatal("fixture consumption schedule")
	}
	if released.CompareAndSwap(false, true) {
		close(release)
	}
	p2Ready(t, done)
	frames, finished, err, _ := job.buf.take()
	if !finished || err != "fixture failed after PCM" || len(frames) != 0 || job.attempts != 0 || len(s.jobs) != 0 || session.produced != 1 {
		t.Fatal("consumed audio retried")
	}
}

func TestP2ProtectCancelledQueuedJobRemovedBeforeHealthyDispatch(t *testing.T) {
	s := NewScheduler([]string{"http://unused"})
	cancelled := p2Session(t, s)
	live := p2Session(t, s)
	stale, current := p2Job(cancelled, 0), p2Job(live, 1)
	s.Submit(stale)
	s.Submit(current)
	cancelled.cancel()
	s.mu.Lock()
	picked := s.pickLocked(s.workers[0])
	s.mu.Unlock()
	_, done, err, _ := stale.buf.take()
	if picked != current || !done || err != "cancelled" || len(s.jobs) != 0 {
		t.Fatal("cancelled queue dispatch")
	}
}

func TestP2ProtectOrderedForwarderKeepsSegmentPCMAndEndAccounting(t *testing.T) {
	s := NewScheduler(nil)
	session := p2Session(t, s)
	first, second := p2Job(session, 0), p2Job(session, 1)
	// Later segment completes first, without ever running the scheduler or a model.
	second.buf.push([]byte{2, 0}, 1)
	second.buf.finish("", map[string]any{"gpu": float64(1)})
	first.buf.push([]byte{1, 0}, 1)
	first.buf.push([]byte{3, 0}, 1)
	first.buf.finish("", map[string]any{"gpu": float64(0)})
	session.jobs = []*Job{first, second}
	session.allSubmitted = true
	recorder := httptest.NewRecorder()
	metrics := NewMetrics()
	session.serve(recorder, recorder, metrics)
	var pcm []byte
	var indices []uint32
	ends := 0
	for _, frame := range p2Decode(t, recorder.Body.Bytes()) {
		if frame.kind == cPCM {
			pcm = append(pcm, frame.raw...)
			indices = append(indices, frame.index)
		}
		if frame.kind == cEnd {
			ends++
		}
	}
	if !bytes.Equal(pcm, []byte{1, 0, 3, 0, 2, 0}) || fmt.Sprint(indices) != "[0 0 1]" || ends != 1 || metrics.total != 1 || len(session.segStats) != 2 || session.ctx.Err() == nil {
		t.Fatal("ordered output/accounting")
	}
}

type p2FailWriter struct {
	*httptest.ResponseRecorder
	failed bool
}

func (w *p2FailWriter) Write(raw []byte) (int, error) {
	if len(raw) > 0 && raw[0] == cPCM {
		w.failed = true
		return 0, io.ErrClosedPipe
	}
	return w.ResponseRecorder.Write(raw)
}
func TestP2ProtectForwarderWriteFailureCancelsWithoutSuccessEnd(t *testing.T) {
	s := NewScheduler(nil)
	session := p2Session(t, s)
	job := p2Job(session, 0)
	job.buf.push([]byte{1, 0}, 1)
	job.buf.finish("", nil)
	session.jobs = []*Job{job}
	session.allSubmitted = true
	writer := &p2FailWriter{ResponseRecorder: httptest.NewRecorder()}
	metrics := NewMetrics()
	session.serve(writer, writer, metrics)
	if !writer.failed || !errors.Is(session.ctx.Err(), context.Canceled) || metrics.total != 0 {
		t.Fatal("write error not cancelled")
	}
	for _, frame := range p2Decode(t, writer.Body.Bytes()) {
		if frame.kind == cEnd {
			t.Fatal("success END after write failure")
		}
	}
}

func TestP2ProtectLLMReadCancellationReachesLocalHTTPHandler(t *testing.T) {
	ready, handlerDone, release := make(chan struct{}), make(chan struct{}), make(chan struct{})
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		w.WriteHeader(200)
		w.(http.Flusher).Flush()
		close(ready)
		select {
		case <-r.Context().Done():
			close(handlerDone)
		case <-release:
		}
	}))
	defer server.Close()
	defer close(release)
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	done := make(chan error, 1)
	go func() {
		done <- StreamLLM(ctx, &Config{LLMBase: server.URL}, "fixture-key", nil, func(string) { t.Error("unexpected delta") })
	}()
	p2Ready(t, ready)
	cancel()
	select {
	case err := <-done:
		if !errors.Is(err, context.Canceled) {
			t.Fatal(err)
		}
	case <-time.After(5 * time.Second):
		t.Fatal("LLM request cancellation deadline")
	}
	p2Ready(t, handlerDone)
}

func TestP2ProtectLLMIncompleteOutputReportedWhileOriginalPrefixPreserved(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		fmt.Fprint(w, "data: {\"choices\":[{\"delta\":{\"content\":\"尚未完成的原文\"},\"finish_reason\":\"length\"}]}\n")
	}))
	defer server.Close()
	s := NewScheduler(nil)
	session := (&App{sched: s}).newSession(context.Background(), SpeakReq{Mode: "chat"}, &ProfileInfo{ID: "fixture"})
	defer session.cancel()
	session.produce(&Config{LLMBase: server.URL}, SpeakReq{Mode: "chat", Text: "input"}, "fixture-key")
	if !session.allSubmitted || !strings.Contains(session.llmErr, "incomplete") || len(session.jobs) != 1 || session.jobs[0].seg.Text != "尚未完成的原文" {
		t.Fatal("LLM truncation swallowed or prefix rewritten")
	}
	session.jobs[0].buf.finish("fixture no model", nil)
	rr := httptest.NewRecorder()
	session.serve(rr, rr, NewMetrics())
	errorsSeen, ends := 0, 0
	for _, frame := range p2Decode(t, rr.Body.Bytes()) {
		if frame.kind == cError {
			errorsSeen++
		}
		if frame.kind == cEnd {
			var end map[string]any
			if json.Unmarshal(frame.raw, &end) != nil || len(end["errors"].([]any)) == 0 {
				t.Fatal("END lost errors")
			}
			ends++
		}
	}
	if errorsSeen != 2 || ends != 1 {
		t.Fatal("failed stages not reported")
	}
}

func TestP2ProtectReadProducerNeverCallsLLMAndPreservesLongMultiscriptText(t *testing.T) {
	var requests atomic.Int32
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { requests.Add(1); w.WriteHeader(500) }))
	defer server.Close()
	s := NewScheduler(nil)
	session := p2Session(t, s)
	text := strings.Repeat("你好，Hello 3.14 **原文**「こんにちは」 한국어。\n", 100)
	session.produce(&Config{LLMBase: server.URL}, SpeakReq{Mode: "read", Text: text}, "fixture-key")
	var joined strings.Builder
	for _, job := range session.jobs {
		joined.WriteString(job.seg.Text)
	}
	if requests.Load() != 0 || !session.allSubmitted || joined.String() != text || len(session.jobs) < 2 {
		t.Fatal("read mode changed source or called LLM")
	}
}

func TestP2ProtectWatermarkHysteresisResumeAndStaleTelemetryFallback(t *testing.T) {
	s := NewScheduler(nil)
	session := p2Session(t, s)
	session.produced = sampleRate * 61
	job := p2Job(session, 2)
	session.telemetry(Telemetry{State: "paused", PlayedS: 0})
	if session.allowDispatch(job) || !session.throttled {
		t.Fatal("high watermark")
	}
	session.telemetry(Telemetry{State: "paused", PlayedS: 10})
	if session.allowDispatch(job) {
		t.Fatal("hysteresis chatter")
	}
	session.telemetry(Telemetry{State: "paused", PlayedS: 30})
	if !session.allowDispatch(job) || session.throttled {
		t.Fatal("hysteresis resume")
	}
	session.telemetry(Telemetry{State: "paused", PlayedS: 0})
	if session.allowDispatch(job) {
		t.Fatal("rearm gate")
	}
	session.lastTelem = time.Now().Add(-3 * time.Second)
	if !session.allowDispatch(job) || !session.allowDispatch(p2Job(session, 0)) {
		t.Fatal("stale fallback / head exemption")
	}
	// Existing fail-open stale telemetry is preserved, NOT a bounded-memory proof.
}

func TestP2ProtectTruncatedPayloadAndPreStatsHeaderCannotCountAsServed(t *testing.T) {
	partial := make([]byte, 7)
	partial[0] = fPCM
	binary.LittleEndian.PutUint32(partial[1:], 10)
	for _, raw := range [][]byte{nil, {fPCM, 1}, partial} {
		job, worker := g0Run(t, raw)
		_, done, err, _ := job.buf.take()
		if !done || err == "" || worker.served != 0 || worker.failed != 1 {
			t.Fatal("invalid stream accepted before stats")
		}
	}
}

func TestP2ProtectActivationDeletionRejectsAndKeepsPreviousActive(t *testing.T) {
	root, initial := p2Profile(t)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if err := os.Remove(filepath.Join(root, "profiles", "fixture", "profile.json")); err != nil {
			t.Error(err)
			w.WriteHeader(500)
			return
		}
		json.NewEncoder(w).Encode(map[string]any{"ok": true, "voice_binding": initial.VoiceBinding, "voice_conditioning": initial.VoiceConditioning})
	}))
	defer server.Close()
	app := &App{cfg: &Config{StateDir: root, WorkerURLs: []string{server.URL}}}
	rr := httptest.NewRecorder()
	app.activate(rr, httptest.NewRequest("POST", "/api/profiles/activate", strings.NewReader(`{"id":"fixture"}`)))
	temps, _ := filepath.Glob(filepath.Join(root, ".active-*.tmp"))
	if rr.Code != 503 || activeProfileID(root) != "previous" || len(temps) != 0 {
		t.Fatal("deleted profile activated")
	}
}

func TestP2ObservedHealthHTTP503JSONStillCountsAsHealthy(t *testing.T) {
	if os.Getenv("QTTS_PASS2_HEALTH_CHILD") != "1" {
		ctx, cancel := context.WithTimeout(context.Background(), 15*time.Second)
		defer cancel()
		cmd := exec.CommandContext(ctx, os.Args[0], "-test.run=^TestP2ObservedHealthHTTP503JSONStillCountsAsHealthy$", "-test.v")
		cmd.Env = append(os.Environ(), "QTTS_PASS2_HEALTH_CHILD=1")
		output, err := cmd.CombinedOutput()
		if err != nil || !bytes.Contains(output, []byte("OBSERVED_NOT_FIXED_F23")) {
			t.Fatalf("owned child: %v %s", err, output)
		}
		t.Log("OBSERVED_NOT_FIXED_F23: owned child exited; original healthLoop accepted HTTP503; gateway reported two healthy fixture workers")
		return
	}
	// healthLoop has no stop hook. Isolate it in an owned test child, which exits
	// after assertions; do NOT leave its perpetual goroutine in the outer suite.
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(503)
		fmt.Fprint(w, `{"ready":true,"stalled_s":0}`)
	}))
	defer server.Close()
	s := NewScheduler([]string{server.URL, server.URL})
	go s.healthLoop()
	deadline := time.NewTimer(5 * time.Second)
	defer deadline.Stop()
	ticker := time.NewTicker(time.Millisecond)
	defer ticker.Stop()
	for !(s.workers[0].isHealthy() && s.workers[1].isHealthy()) {
		select {
		case <-ticker.C:
		case <-deadline.C:
			t.Fatal("health observation deadline")
		}
	}
	rr := httptest.NewRecorder()
	(&App{sched: s, cfg: &Config{StateDir: t.TempDir()}}).health(rr, httptest.NewRequest("GET", "/api/health", nil))
	var body map[string]any
	if json.Unmarshal(rr.Body.Bytes(), &body) != nil || body["workers_healthy"] != float64(2) || body["ok"] != true {
		t.Fatal(rr.Body.String())
	}
	t.Log("OBSERVED_NOT_FIXED_F23: original HTTP503 counted as two healthy workers")
}

func TestP2ObservedActivationConditioningChangesButBindingFinalCheckPasses(t *testing.T) {
	root, initial := p2Profile(t)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		raw, err := os.ReadFile(filepath.Join(root, "profiles", "fixture", "profile.json"))
		if err != nil {
			t.Error(err)
			w.WriteHeader(500)
			return
		}
		var p map[string]any
		if err = json.Unmarshal(raw, &p); err != nil {
			t.Error(err)
			w.WriteHeader(500)
			return
		}
		p["model_output_mode"] = "sentence-buffered"
		raw, _ = json.Marshal(p)
		if err = os.WriteFile(filepath.Join(root, "profiles", "fixture", "profile.json"), raw, 0600); err != nil {
			t.Error(err)
			w.WriteHeader(500)
			return
		}
		json.NewEncoder(w).Encode(map[string]any{"ok": true, "voice_binding": initial.VoiceBinding, "voice_conditioning": initial.VoiceConditioning})
	}))
	defer server.Close()
	rr := httptest.NewRecorder()
	(&App{cfg: &Config{StateDir: root, WorkerURLs: []string{server.URL}}}).activate(rr, httptest.NewRequest("POST", "/api/profiles/activate", strings.NewReader(`{"id":"fixture"}`)))
	current, err := loadProfileInfo(root, "fixture")
	if err != nil {
		t.Fatal(err)
	}
	var receipt struct {
		Workers []struct {
			Conditioning string `json:"voice_conditioning"`
		}
	}
	if err = json.Unmarshal(rr.Body.Bytes(), &receipt); err != nil {
		t.Fatal(err)
	}
	if rr.Code != 200 || activeProfileID(root) != "fixture" || initial.VoiceBinding != current.VoiceBinding || current.VoiceConditioning != "trained-speaker-vector" || len(receipt.Workers) != 1 || receipt.Workers[0].Conditioning != initial.VoiceConditioning || current.VoiceConditioning == initial.VoiceConditioning {
		t.Fatal("observation changed", rr.Body.String())
	}
	t.Log("OBSERVED_NOT_FIXED_F24: original activation publishes 200 after actual metadata mutation; acknowledged ICL but final profile requests trained-speaker-vector; reference pin unchanged; no model or subsequent playback executed")
}
