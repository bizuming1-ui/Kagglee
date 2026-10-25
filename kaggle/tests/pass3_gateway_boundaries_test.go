package main

// Audit only. Compiled beside SHA-matched copies, never edited product Go files.
// Real local HTTP/Go state; provider, PCM and stats are explicit synthetic fixtures.
import (
	"context"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestP3GProtectChatPayloadRoleOrderCustomSystemAndTextRetention(t *testing.T) {
	type capture struct {
		Model     string    `json:"model"`
		Messages  []ChatMsg `json:"messages"`
		Stream    bool      `json:"stream"`
		MaxTokens int       `json:"max_tokens"`
	}
	received := make(chan capture, 1)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != "POST" || r.URL.Path != "/chat/completions" || r.Header.Get("Authorization") != "Bearer synthetic-only" {
			t.Error("request shape changed")
		}
		var captured capture
		if err := json.NewDecoder(r.Body).Decode(&captured); err != nil {
			t.Error(err)
		}
		received <- captured
		io.WriteString(w, "data: {\"choices\":[{\"delta\":{\"content\":\"你好。\"}}]}\n\ndata: [DONE]\n")
	}))
	defer server.Close()
	scheduler := NewScheduler(nil)
	session := p2Session(t, scheduler)
	req := SpeakReq{Mode: "chat", Text: "当前问题", System: "保留自定义系统说明", History: []ChatMsg{{Role: "user", Content: "先前问题"}, {Role: "assistant", Content: "先前答复"}}}
	session.produce(&Config{LLMBase: server.URL, LLMModel: "fixture-model", LLMMaxTokens: 8192}, req, "synthetic-only")
	var captured capture
	select {
	case captured = <-received:
	case <-time.After(5 * time.Second):
		t.Fatal("owned HTTP deadline")
	}
	expected := []ChatMsg{{Role: "system", Content: req.System}, req.History[0], req.History[1], {Role: "user", Content: req.Text}}
	if captured.Model != "fixture-model" || !captured.Stream || captured.MaxTokens != 8192 || len(captured.Messages) != len(expected) {
		t.Fatal("payload incomplete")
	}
	for i, m := range expected {
		if captured.Messages[i] != m {
			t.Fatal("history/system reordered", i)
		}
	}
	if session.llmErr != "" || !session.allSubmitted || len(session.jobs) != 1 || session.jobs[0].seg.Text != "你好。" {
		t.Fatal("producer lost prefix")
	}
}

func TestP3GProtectMissingLLMKeyFailsBeforeHTTPAndDelta(t *testing.T) {
	calls := 0
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { calls++; w.WriteHeader(500) }))
	defer server.Close()
	err := StreamLLM(context.Background(), &Config{LLMBase: server.URL}, "", nil, func(string) { t.Error("unexpected delta") })
	if err == nil || calls != 0 {
		t.Fatal("missing key reached HTTP")
	}
}

func TestP3GProtectSSECommentsCRLFAndFinalLineWithoutNewline(t *testing.T) {
	for _, ending := range []string{"data: [DONE]", "data: {\"choices\":[{\"delta\":{},\"finish_reason\":\"stop\"}]}"} {
		server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			io.Copy(io.Discard, r.Body)
			io.WriteString(w, ": heartbeat\r\nevent: message\r\ndata: {\"choices\":[{\"delta\":{\"role\":\"assistant\"}}]}\r\n\r\ndata: {\"choices\":[{\"delta\":{\"content\":\"你好 café🧠\"}}]}\r\n\r\n"+ending)
		}))
		var got strings.Builder
		err := StreamLLM(context.Background(), &Config{LLMBase: server.URL}, "synthetic-only", nil, func(v string) { got.WriteString(v) })
		server.Close()
		if err != nil || got.String() != "你好 café🧠" {
			t.Fatal("SSE terminal/Unicode changed", err, got.String())
		}
	}
}

func TestP3GProtectSSEErrorJSONRedactsProviderMessageAndKeepsPriorDelta(t *testing.T) {
	secret := "synthetic-provider-secret-not-real"
	for _, bad := range []string{`{"error":{"message":"` + secret + `"}}`, `{broken-` + secret} {
		server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			io.Copy(io.Discard, r.Body)
			io.WriteString(w, "data: {\"choices\":[{\"delta\":{\"content\":\"原始前缀\"}}]}\n\ndata: "+bad+"\n")
		}))
		var got strings.Builder
		err := StreamLLM(context.Background(), &Config{LLMBase: server.URL}, "synthetic-only", nil, func(v string) { got.WriteString(v) })
		server.Close()
		if err == nil || strings.Contains(err.Error(), secret) || got.String() != "原始前缀" {
			t.Fatal("SSE error leaked or rewrote prefix")
		}
	}
	// Only in-stream error JSON/malformed JSON. F30 non-200 body leak remains NOT FIXED.
}

func TestP3GProtectExactReadMultiscriptChunkingAndFlushIdempotence(t *testing.T) {
	text := "开始 café é 🧠 https://example.invalid/a_b?q=1\n保留  空格、括号（测试）与数字12.50，最后结束"
	for _, step := range []int{1, 2, 7, 4096} {
		segmenter := NewSegmenter(ReadSegCfg(nil), 17)
		segments := feedAll(segmenter, text, step)
		var joined strings.Builder
		for i, seg := range segments {
			if seg.Index != i {
				t.Fatal("index gap")
			}
			joined.WriteString(seg.Text)
		}
		if joined.String() != text || len(segmenter.Flush()) != 0 {
			t.Fatal("read source changed", step, joined.String())
		}
	}
	// Word-bearing input with no isolated punctuation-only tail; F39 below is separate.
}

func TestP3GProtectPauseClampsAndReadSeedReproducibility(t *testing.T) {
	cfg := ReadSegCfg(&ProfileInfo{PauseClauseMs: 9999, PauseSentenceMs: 1, PauseParaMs: 9999})
	if cfg.PauseClause != 400 || cfg.PauseSent != 160 || cfg.PausePara != 1200 || cfg.PauseEllipsis != 260 || !cfg.PreserveText || cfg.ImmediateFirst {
		t.Fatal("pause/config clamp changed")
	}
	text := strings.Repeat("这是一段保留原字的连续朗读。接下来继续说清楚。\n\n", 8) + "自然结束"
	a, b := feedAll(NewSegmenter(cfg, 17), text, 1), feedAll(NewSegmenter(cfg, 17), text, 4096)
	if len(a) != len(b) || len(a) < 2 {
		t.Fatal("seed/chunk count changed")
	}
	for i := range a {
		if a[i] != b[i] {
			t.Fatal("read partition changed", i)
		}
	}
	// Deterministic synthetic grouping, not natural prosody/audio evidence.
}

func TestP3GProtectSchedulerRetryBudgetTerminatesWithoutRequeue(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		w.WriteHeader(429)
		io.WriteString(w, strings.Repeat("x", 1000))
	}))
	defer server.Close()
	scheduler := NewScheduler([]string{server.URL})
	session := p2Session(t, scheduler)
	job := p2Job(session, 0)
	job.attempts = 2
	scheduler.workers[0].healthy = true
	scheduler.run(scheduler.workers[0], job)
	_, done, err, _ := job.buf.take()
	worker := scheduler.workers[0]
	if !done || !strings.HasPrefix(err, "worker http 429 ") || len(err) > 450 || len(scheduler.jobs) != 0 || job.attempts != 2 || worker.failed != 1 || worker.served != 0 || worker.busy || !worker.healthy {
		t.Fatal("retry cap or bounded error changed")
	}
}

func TestP3GProtectSchedulerUrgencyThenStableFIFOAcrossSessions(t *testing.T) {
	scheduler := NewScheduler([]string{"http://fixture.invalid"})
	worker := scheduler.workers[0]
	ordinary, urgent, first := p2Session(t, scheduler), p2Session(t, scheduler), p2Session(t, scheduler)
	urgent.urgency = .9
	a, b, c := p2Job(ordinary, 3), p2Job(urgent, 4), p2Job(first, 0)
	scheduler.Submit(a)
	scheduler.Submit(b)
	scheduler.Submit(c)
	for _, want := range []*Job{b, c, a} {
		scheduler.mu.Lock()
		got := scheduler.pickLocked(worker)
		scheduler.mu.Unlock()
		if got != want {
			t.Fatal("priority/FIFO changed")
		}
	}
	if len(scheduler.jobs) != 0 {
		t.Fatal("queue not drained")
	}
	// No Start/healthLoop goroutines; manual original queue selection, no GPU throughput claim.
}

func TestP3GProtectSchedulerPositiveStatsEMAAndQueueMetadata(t *testing.T) {
	raw := append(g0Frame(fPCM, []byte{1, 0, 2, 0}), g0Frame(fStats, []byte(`{"failed":false,"rtf_x":4,"first_chunk_ms":200,"audio_s":2}`))...)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { io.Copy(io.Discard, r.Body); w.Write(raw) }))
	defer server.Close()
	scheduler := NewScheduler([]string{server.URL})
	session := p2Session(t, scheduler)
	job := p2Job(session, 0)
	worker := scheduler.workers[0]
	worker.rtf = 2
	worker.firstMs = 100
	worker.audioSec = 3
	scheduler.run(worker, job)
	frames, done, err, stats := job.buf.take()
	if !done || err != "" || len(frames) != 1 || worker.rtf != 2.6 || worker.firstMs != 130 || worker.audioSec != 5 || worker.served != 1 || worker.failed != 0 || worker.busy {
		t.Fatal("stats accumulation changed")
	}
	if stats["attempts"] != 1 || stats["queue_wait_ms"].(float64) < 0 || session.produced != 2 {
		t.Fatal("queue/sample metadata changed")
	}
	// Stats audio_s=2 with two PCM samples is intentionally a fixture; no consistency/RTF signoff.
}

func TestP3GProtectSchedulerForwardsOptInChunkAndProsodyWithoutChangingSeedPin(t *testing.T) {
	t.Setenv("QTTS_FIRST_CHUNK_SIZE", "2")
	received := make(chan synthReq, 2)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		var body synthReq
		if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
			t.Error(err)
		}
		received <- body
		w.Write(append(g0Frame(fPCM, []byte{1, 0}), g0Stats()...))
	}))
	defer server.Close()
	scheduler := NewScheduler([]string{server.URL})
	session := p2Session(t, scheduler)
	session.seed = 91
	session.lang = "Chinese"
	for _, index := range []int{0, 2} {
		job := p2Job(session, index)
		job.seg.Text = "原字保留"
		job.seg.Breath = true
		job.seg.PauseBeforeMs = 280
		scheduler.run(scheduler.workers[0], job)
	}
	captured := []synthReq{<-received, <-received}
	if len(captured) != 2 || captured[0].ChunkSize != 2 || captured[1].ChunkSize != 6 {
		t.Fatal("chunk forwarding changed")
	}
	for _, r := range captured {
		if r.Seed != 91 || r.Language != "Chinese" || r.Text != "原字保留" || r.VoiceBinding != session.profile.VoiceBinding || r.VoiceConditioning != session.profile.VoiceConditioning || !r.Breath || r.LeadPauseMs != 280 {
			t.Fatal("synth request changed")
		}
	}
	// Forwarded breath flag is not reference PCM playback or acoustic acceptance.
}

func TestP3GObservedPreserveTextDropsStandalonePunctuationAndWhitespaceTail(t *testing.T) {
	for _, text := range []string{"你好。!?", "你好。\n\n", "\t\n", "!?"} {
		segmenter := NewSegmenter(LiveSegCfg(nil), 17)
		segments := feedAll(segmenter, text, 1)
		var joined strings.Builder
		for _, seg := range segments {
			joined.WriteString(seg.Text)
		}
		if joined.String() == text {
			t.Fatal("F39 witness changed", text)
		}
		t.Logf("OBSERVED_NOT_FIXED F39 source=%q joined=%q", text, joined.String())
	}
	// Punctuation/whitespace-only final group is discarded by finish despite PreserveText.
	// Real segmenter + synthetic text, not a missing spoken-word or audio-root-cause proof.
}

func TestP3GObservedCancelledWorkerStatsCountAsServedWithLiveSessionContext(t *testing.T) {
	job, worker := g0Run(t, append(g0Frame(fPCM, []byte{1, 0, 2, 0}), g0Frame(fStats, []byte(`{"failed":false,"cancelled":true,"audio_s":0.0000833333333333,"rtf_x":1}`))...))
	frames, done, err, stats := job.buf.take()
	if job.sess.ctx.Err() != nil || !done || err != "" || len(frames) != 1 || stats["cancelled"] != true || worker.served != 1 || worker.failed != 0 || worker.busy {
		t.Fatal("F40 witness changed")
	}
	t.Log("OBSERVED_NOT_FIXED F40 original Scheduler.run accepted synthetic cancelled=true stats, live session ctx, served=1 failed=0; worker HTTP/PCM/stats fixtures, no actual production cancellation/GPU/audio proof")
}
