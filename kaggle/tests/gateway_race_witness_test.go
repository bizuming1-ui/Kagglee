package main

// ISOLATED EXPECTED-FAIL witness, never part of the passing regression suite.
// Local synthetic map only. Run with -race; no production traffic or private data.
import (
	"encoding/json"
	"sync"
	"testing"
)

func TestObservedMetricsSnapshotEncodingRace(t *testing.T) {
	metrics := NewMetrics()
	metrics.record(map[string]any{"session": "synthetic-only", "payload": "not private"})
	snapshot := metrics.snapshot()
	start := make(chan struct{})
	var group sync.WaitGroup
	group.Add(2)
	go func() {
		defer group.Done()
		<-start
		for i := 0; i < 20000; i++ {
			metrics.mergeClient("synthetic-only", map[string]any{"counter": i})
		}
	}()
	go func() {
		defer group.Done()
		<-start
		for i := 0; i < 20000; i++ {
			_, _ = json.Marshal(snapshot)
		}
	}()
	close(start)
	group.Wait()
}
