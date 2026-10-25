package main

// Copied beside hash-matched original Go sources ONLY in an ignored test tree.
// Observed tests intentionally assert old defects, not successful product fixes.
import (
	"context"
	"encoding/binary"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func g0Frame(kind byte, payload []byte) []byte {
	frame := make([]byte, 5+len(payload))
	frame[0] = kind
	binary.LittleEndian.PutUint32(frame[1:], uint32(len(payload)))
	copy(frame[5:], payload)
	return frame
}
func g0Stats() []byte { return g0Frame(fStats, []byte(`{"audio_s":0.01,"rtf_x":1,"failed":false}`)) }
func g0Run(t *testing.T, payload []byte) (*Job, *WorkerRef) {
	t.Helper()
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { io.Copy(io.Discard, r.Body); w.Write(payload) }))
	t.Cleanup(server.Close)
	scheduler := NewScheduler([]string{server.URL})
	session := (&App{sched: scheduler}).newSession(context.Background(), SpeakReq{Mode: "read"}, &ProfileInfo{ID: "fixture"})
	t.Cleanup(session.cancel)
	job := &Job{sess: session, seg: Segment{Index: 0, Text: "fixture"}, buf: &SegBuf{wake: session.wake}, attempts: 2, enq: time.Now()}
	scheduler.run(scheduler.workers[0], job)
	return job, scheduler.workers[0]
}
func TestG0ObservedOddPCMIsAccepted(t *testing.T) {
	job, worker := g0Run(t, append(g0Frame(fPCM, []byte{1, 2, 3}), g0Stats()...))
	frames, done, err, _ := job.buf.take()
	if !done || err != "" || worker.served != 1 || len(frames) != 1 || len(frames[0]) != 3 || job.buf.samples != 1 {
		t.Fatal("baseline changed")
	}
	t.Log("OBSERVED_NOT_FIXED: odd PCM16 payload forwarded; samples rounded down")
}
func TestG0ObservedStatsWithoutPCMIsAccepted(t *testing.T) {
	job, worker := g0Run(t, g0Stats())
	frames, done, err, _ := job.buf.take()
	if !done || err != "" || worker.served != 1 || len(frames) != 0 {
		t.Fatal("baseline changed")
	}
	t.Log("OBSERVED_NOT_FIXED: positive audio_s stats with no PCM marked served")
}
func TestG0ObservedMalformedErrorFrameIsIgnored(t *testing.T) {
	job, worker := g0Run(t, append(g0Frame(fErr, []byte("{")), g0Stats()...))
	_, done, err, _ := job.buf.take()
	if !done || err != "" || worker.served != 1 {
		t.Fatal("baseline changed")
	}
	t.Log("OBSERVED_NOT_FIXED: malformed error JSON ignored before valid stats")
}
func TestG0ObservedPartialHeaderAfterStatsIsIgnored(t *testing.T) {
	job, worker := g0Run(t, append(g0Stats(), fPCM, 1))
	_, done, err, _ := job.buf.take()
	if !done || err != "" || worker.served != 1 {
		t.Fatal("baseline changed")
	}
	t.Log("OBSERVED_NOT_FIXED: truncated final header after stats ignored")
}
func TestG0ObservedMetricsSnapshotAliasesRunMap(t *testing.T) {
	metrics := NewMetrics()
	metrics.record(map[string]any{"session": "fixture"})
	snapshot := metrics.snapshot()
	runs := snapshot["runs"].([]map[string]any)
	if _, ok := runs[0]["client"]; ok {
		t.Fatal("unexpected initial client")
	}
	if !metrics.mergeClient("fixture", map[string]any{"synthetic": true}) {
		t.Fatal("merge failed")
	}
	if _, ok := runs[0]["client"]; !ok {
		t.Fatal("baseline alias changed")
	}
	t.Log("OBSERVED_NOT_FIXED: previously returned snapshot changed after mergeClient")
}
func TestG0ProtectConsumedAudioCannotResetForRetry(t *testing.T) {
	buffer := &SegBuf{wake: make(chan struct{}, 1)}
	buffer.push([]byte{1, 2}, 1)
	buffer.take()
	ok, dropped := buffer.resetIfUnconsumed()
	if ok || dropped != 0 {
		t.Fatal("consumed audio retry permitted")
	}
}
func TestG0ProtectUnconsumedRetryAccounting(t *testing.T) {
	buffer := &SegBuf{wake: make(chan struct{}, 1)}
	buffer.push([]byte{1, 2, 3, 4}, 2)
	ok, dropped := buffer.resetIfUnconsumed()
	if !ok || dropped != 2 || buffer.samples != 0 || len(buffer.frames) != 0 {
		t.Fatal("retry reset accounting failed")
	}
}
func TestG0ProtectCancellationReachesWorkerRequest(t *testing.T) {
	ready := make(chan struct{})
	release := make(chan struct{})
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		io.Copy(io.Discard, r.Body)
		w.WriteHeader(200)
		w.(http.Flusher).Flush()
		close(ready)
		select {
		case <-r.Context().Done():
		case <-release:
		}
	}))
	defer server.Close()
	defer close(release)
	scheduler := NewScheduler([]string{server.URL})
	session := (&App{sched: scheduler}).newSession(context.Background(), SpeakReq{Mode: "read"}, &ProfileInfo{ID: "fixture"})
	defer session.cancel()
	job := &Job{sess: session, seg: Segment{Text: "fixture"}, buf: &SegBuf{wake: session.wake}, enq: time.Now()}
	done := make(chan struct{})
	go func() { scheduler.run(scheduler.workers[0], job); close(done) }()
	select {
	case <-ready:
	case <-time.After(3 * time.Second):
		t.Fatal("request not received")
	}
	session.cancel()
	select {
	case <-done:
	case <-time.After(3 * time.Second):
		t.Fatal("scheduler did not cancel")
	}
	_, finished, err, _ := job.buf.take()
	if !finished || err != "cancelled" || scheduler.workers[0].busy {
		t.Fatal("cancel contract failed")
	}
}
func TestG0ProtectSameSeedAndVoicePinsAcrossWorkers(t *testing.T) {
	received := make(chan synthReq, 2)
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		var body synthReq
		if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
			t.Error(err)
		}
		received <- body
		w.Write(append(g0Frame(fPCM, []byte{1, 2}), g0Stats()...))
	}))
	defer server.Close()
	scheduler := NewScheduler([]string{server.URL, server.URL})
	profile := &ProfileInfo{ID: "fixture", VoiceBinding: strings.Repeat("a", 64), VoiceConditioning: "icl-generated-only-codec"}
	session := (&App{sched: scheduler}).newSession(context.Background(), SpeakReq{Mode: "read"}, profile)
	defer session.cancel()
	session.seed = 42
	for _, worker := range scheduler.workers {
		job := &Job{sess: session, seg: Segment{Text: "same target"}, buf: &SegBuf{wake: session.wake}, enq: time.Now()}
		scheduler.run(worker, job)
	}
	first, second := <-received, <-received
	if first.Seed != 42 || second.Seed != 42 || first.VoiceBinding != profile.VoiceBinding || second.VoiceBinding != first.VoiceBinding || second.VoiceConditioning != first.VoiceConditioning {
		t.Fatal("effective request conditions differ")
	}
}
func TestG0ProtectOversizedFrameRejected(t *testing.T) {
	header := make([]byte, 5)
	header[0] = fPCM
	binary.LittleEndian.PutUint32(header[1:], (32<<20)+1)
	job, worker := g0Run(t, header)
	_, done, err, _ := job.buf.take()
	if !done || err != "oversized frame" || worker.served != 0 {
		t.Fatal("oversized frame accepted")
	}
}
