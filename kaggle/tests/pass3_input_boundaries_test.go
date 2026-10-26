package main

// Audit-only: real Go/Python pin implementations in owned filesystem/CPU children.
// Profiles/worker acks are fixtures, reference bytes are NOT audio/model evidence.
import (
	"bytes"
	"context"
	"encoding/hex"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

type p3PinResult struct {
	OK         bool   `json:"ok"`
	Pin        string `json:"pin"`
	Generation string `json:"generation"`
	Error      string `json:"error"`
}

func p3PythonPins(t *testing.T, directory string, profiles []json.RawMessage) []p3PinResult {
	t.Helper()
	root, python := os.Getenv("QTTS_AUDIT_ROOT"), os.Getenv("QTTS_AUDIT_PYTHON")
	if root == "" || python == "" {
		t.Fatal("audit runner must supply explicit repository/interpreter paths")
	}
	script := `import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(sys.argv[1])/'kaggle/source/py'))
from voice_binding import reference_binding,generation_bytes
out=[]
for profile in json.load(sys.stdin):
 try:out.append({'ok':True,'pin':reference_binding(Path(sys.argv[2]),profile),'generation':generation_bytes(profile).hex()})
 except Exception as error:out.append({'ok':False,'error':type(error).__name__})
print(json.dumps(out))
`
	ctx, cancel := context.WithTimeout(context.Background(), 8*time.Second)
	defer cancel()
	cmd := exec.CommandContext(ctx, python, "-c", script, root, directory)
	cmd.Env = []string{"PATH=" + os.Getenv("PATH"), "PYTHONDONTWRITEBYTECODE=1"}
	raw, err := json.Marshal(profiles)
	if err != nil {
		t.Fatal(err)
	}
	cmd.Stdin = bytes.NewReader(raw)
	output, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatal("owned Python pin child failed", err)
	}
	var rows []p3PinResult
	if err = json.Unmarshal(output, &rows); err != nil || len(rows) != len(profiles) {
		t.Fatal("invalid pin child receipt", err)
	}
	return rows
}
func p3PinDirectory(t *testing.T) string {
	t.Helper()
	dir := t.TempDir()
	if err := os.WriteFile(filepath.Join(dir, "ref.bin"), []byte{'R', 0, 255, 'F', 1, 2}, 0600); err != nil {
		t.Fatal(err)
	}
	return dir
}

func TestP3ProtectGoPythonUnicodeAndGenerationPinEquivalence(t *testing.T) {
	dir := p3PinDirectory(t)
	profiles := []json.RawMessage{
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"你好 café\u0000🧠","language":"Chinese"}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"你好 café\u0000🧠","language":"Chinese","gen":null}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"你好 café\u0000🧠","language":"Chinese","gen":{"temperature":0.8,"top_k":50,"top_p":1,"repetition_penalty":1.05}}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"你好 café\u0000🧠","language":"Chinese","name":"excluded metadata","gen":{"unrecognized_metadata":123}}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"a","language":"bc","gen":{"top_k":-0.0}}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"ab","language":"c","gen":{"top_k":0}}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"é","language":"English","gen":{"temperature":2,"top_k":4096,"top_p":1,"repetition_penalty":4}}`),
		json.RawMessage(`{"anchor":"ref.bin","ref_text":"é","language":"English","gen":{"temperature":0.01,"top_k":0,"top_p":0.01,"repetition_penalty":0.01}}`),
	}
	py := p3PythonPins(t, dir, profiles)
	for i, raw := range profiles {
		var p ProfileInfo
		if err := json.Unmarshal(raw, &p); err != nil {
			t.Fatal(err)
		}
		pin, err := referenceBinding(dir, &p)
		generation, gerr := generationBytes(p.Gen)
		if err != nil || gerr != nil || !py[i].OK || pin != py[i].Pin || hex.EncodeToString(generation) != py[i].Generation {
			t.Fatal("Go/Python pin mismatch", i, err, gerr, py[i].Error)
		}
	}
	for _, i := range []int{1, 2, 3} {
		if py[i].Pin != py[0].Pin {
			t.Fatal("effective defaults/metadata changed pin")
		}
	}
	if py[4].Pin == py[5].Pin {
		t.Fatal("length framing collision")
	}
	t.Log("cross_language_valid_vectors=8; actual Go+Python, raw bytes not WAV/model conditioning")
}

func TestP3ProtectGoPythonNumericTypeAndRangeRejection(t *testing.T) {
	dir := p3PinDirectory(t)
	var profiles []json.RawMessage
	for _, gen := range []string{`{"temperature":true}`, `{"top_k":"0"}`, `{"top_p":false}`, `{"repetition_penalty":"1"}`, `{"temperature":0}`, `{"temperature":2.01}`, `{"top_k":1.5}`, `{"top_k":4097}`, `{"top_p":0}`, `{"top_p":1.01}`, `{"repetition_penalty":0}`, `{"repetition_penalty":4.01}`} {
		profiles = append(profiles, json.RawMessage(`{"anchor":"ref.bin","gen":`+gen+`}`))
	}
	py := p3PythonPins(t, dir, profiles)
	for i, raw := range profiles {
		var p ProfileInfo
		err := json.Unmarshal(raw, &p)
		if err == nil {
			_, err = referenceBinding(dir, &p)
		}
		if err == nil || py[i].OK {
			t.Fatal("invalid generation accepted", i)
		}
	}
	t.Log("cross_language_rejected_vectors=12")
}

func TestP3ProtectGenerationRevisionDuringActivationKeepsPreviousActive(t *testing.T) {
	root, initial := p2Profile(t)
	var once sync.Once
	var calls atomic.Int32
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls.Add(1)
		io.Copy(io.Discard, r.Body)
		once.Do(func() {
			path := filepath.Join(root, "profiles/fixture/profile.json")
			raw, err := os.ReadFile(path)
			if err != nil {
				t.Error(err)
				return
			}
			var p map[string]any
			json.Unmarshal(raw, &p)
			p["gen"] = map[string]float64{"temperature": .65}
			raw, _ = json.Marshal(p)
			if err = os.WriteFile(path, raw, 0600); err != nil {
				t.Error(err)
			}
		})
		writeJSON(w, 200, map[string]any{"ok": true, "voice_binding": initial.VoiceBinding, "voice_conditioning": initial.VoiceConditioning})
	})
	aWorker, bWorker := httptest.NewServer(handler), httptest.NewServer(handler)
	defer aWorker.Close()
	defer bWorker.Close()
	a := &App{cfg: &Config{StateDir: root, WebDir: root, AnalystURL: "http://127.0.0.1:1", WorkerURLs: []string{aWorker.URL, bWorker.URL}}, guard: testGuard(t)}
	rr := httptest.NewRecorder()
	a.routes().ServeHTTP(rr, authed("POST", "/api/profiles/activate", `{"id":"fixture"}`))
	if rr.Code != 503 || activeProfileID(root) != "previous" || calls.Load() != 2 {
		t.Fatal("activation mixed revisions", rr.Code, calls.Load())
	}
	current, err := loadProfileInfo(root, "fixture")
	if err != nil || current.VoiceBinding == initial.VoiceBinding {
		t.Fatal("revision not reflected", err)
	}
}

func TestP3ProtectMalformedOrEmptySpeakNeverCallsConfiguredWorker(t *testing.T) {
	var calls atomic.Int32
	worker := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { calls.Add(1); w.WriteHeader(500) }))
	defer worker.Close()
	root := t.TempDir()
	a := &App{cfg: &Config{StateDir: root, WebDir: root, AnalystURL: worker.URL, WorkerURLs: []string{worker.URL}}, guard: testGuard(t), sched: NewScheduler([]string{worker.URL}), metrics: NewMetrics()}
	for _, raw := range []string{`null`, `{}`, `{"text":null}`, `{"text":123}`, `{"text":false}`, `{"text":" \n\t "}`, `{} {}`, `{"text":`} {
		rr := httptest.NewRecorder()
		a.routes().ServeHTTP(rr, authed("POST", "/api/speak", raw))
		if rr.Code != 400 || rr.Header().Get("X-Session-Id") != "" || len(a.guard.speakSlots) != 0 {
			t.Fatal("invalid request entered session", rr.Code)
		}
	}
	if calls.Load() != 0 {
		t.Fatal("worker called for rejected input")
	}
}

func TestP3ProtectProfileIdentityNotConfusedWithContentPin(t *testing.T) {
	t.Setenv("QTTS_MOCK", "0")
	root := t.TempDir()
	var pins []string
	for _, id := range []string{"voice-a", "voice-b"} {
		dir := filepath.Join(root, "profiles", id)
		os.MkdirAll(dir, 0700)
		os.WriteFile(filepath.Join(dir, "ref.bin"), []byte("same synthetic reference bytes"), 0600)
		raw := json.RawMessage(`{"id":"` + id + `","name":"` + id + `","anchor":"ref.bin","ref_text":"same","language":"English"}`)
		os.WriteFile(filepath.Join(dir, "profile.json"), raw, 0600)
		p, err := loadProfileInfo(root, id)
		if err != nil {
			t.Fatal(err)
		}
		py := p3PythonPins(t, dir, []json.RawMessage{raw})
		if p.ID != id || !py[0].OK || p.VoiceBinding != py[0].Pin {
			t.Fatal("identity/pin crossed")
		}
		pins = append(pins, p.VoiceBinding)
	}
	if pins[0] != pins[1] || strings.TrimSpace(pins[0]) == "" {
		t.Fatal("content pin unexpectedly identity-dependent")
	}
	// Equal content hashes do NOT establish speaker identity, authorization or quality.
}

func TestP3ObservedNullTopKAcceptedByGoButRejectedByPythonBinding(t *testing.T) {
	t.Setenv("QTTS_MOCK", "0")
	root := t.TempDir()
	dir := filepath.Join(root, "profiles/fixture")
	os.MkdirAll(dir, 0700)
	os.WriteFile(filepath.Join(dir, "ref.bin"), []byte("synthetic reference hash fixture"), 0600)
	raw := json.RawMessage(`{"id":"fixture","anchor":"ref.bin","ref_text":"fixture","language":"English","gen":{"top_k":null}}`)
	os.WriteFile(filepath.Join(dir, "profile.json"), raw, 0600)
	p, err := loadProfileInfo(root, "fixture")
	if err != nil || p.Gen["top_k"] != 0 || p.VoiceBinding == "" {
		t.Fatal("Go null-coercion witness changed", err)
	}
	py := p3PythonPins(t, dir, []json.RawMessage{raw})
	if py[0].OK || py[0].Error != "ValueError" {
		t.Fatal("Python witness changed")
	}
	t.Log("OBSERVED_NOT_FIXED F31: identical disk profile gen.top_k=null becomes Go float64 zero with valid pin; actual Python reference_binding rejects ValueError; no model, activation success or wrong-voice proof")
}
