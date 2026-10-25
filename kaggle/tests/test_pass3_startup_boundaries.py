"""Third-pass startup/tools/DSP: 10 protections + 2 observed NOT FIXED.
Real owned CPU processes/OFDs and C-ABI fault fixture; NOT Rust/model/GPU proof.
"""
from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import select
import signal
import struct
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch
import numpy as np
import test_reliability
import test_tool_boundaries as tools
import bootstrap
import supervisor
import audio_rt
import gpu_ownership as gpu
from resource_limits import UploadRejected

ROOT = Path(__file__).resolve().parents[1] / 'source'
OBSERVATIONS = []


class StartupBoundaries(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='pass3-startup-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def test_protect_bootstrap_direct_live_child_timeout_reaps_and_closes_pipe(self):
        popen = subprocess.Popen
        owned = []
        def spawn(*args, **kwargs):
            self.assertTrue(kwargs['start_new_session'])
            p = popen(*args, **kwargs); owned.append(p); return p
        try:
            with patch.object(bootstrap.subprocess, 'Popen', side_effect=spawn):
                with self.assertRaises(TimeoutError):
                    bootstrap.sh([sys.executable, '-c', 'import time; print("ready",flush=True); time.sleep(60)'], quiet=True, timeout=.3)
            self.assertEqual(len(owned), 1)
            self.assertEqual(owned[0].returncode, -signal.SIGKILL)
            self.assertTrue(owned[0].stdout.closed)
        finally:
            for p in owned:
                if p.poll() is None: os.killpg(p.pid, signal.SIGKILL); p.wait(timeout=5)
                if p.stdout: p.stdout.close()
        # Direct live leader only: F21 descendant-held stdout remains unfixed.

    def test_protect_bootstrap_busy_and_stale_marker_refuse_without_pid_kill(self):
        root = self.root / 'fleet'
        lease = gpu.GpuLease.acquire('inference', root=root)
        try:
            with patch.object(bootstrap, 'STATE', self.root), patch.object(bootstrap, 'ownership_status', side_effect=lambda: gpu.status(root=root)), patch.object(bootstrap.os, 'killpg') as kill:
                with self.assertRaises(UploadRejected) as error: bootstrap.stop_old()
                self.assertEqual(error.exception.code, 409)
                lease.close()
                marker = self.root / 'supervisor.pid'; marker.write_text('0\n')
                with self.assertRaises(UploadRejected) as error: bootstrap.stop_old()
                self.assertEqual(error.exception.code, 409); self.assertEqual(marker.read_text(), '0\n')
                marker.unlink(); bootstrap.stop_old(); kill.assert_not_called()
        finally: lease.close()

    def test_protect_supervisor_kills_owned_descendant_after_leader_exit_and_releases_ofd(self):
        root = self.root / 'fleet'
        lease = gpu.GpuLease.acquire('inference', root=root)
        child_code = 'import signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); print("ready",flush=True); time.sleep(60)'
        leader_code = ('import subprocess,sys; p=subprocess.Popen([sys.executable,"-c",sys.argv[1]],pass_fds=(int(sys.argv[2]),),stdout=subprocess.PIPE,text=True); '
                       'assert p.stdout.readline().strip()=="ready"; print(p.pid,flush=True)')
        p = subprocess.Popen([sys.executable, '-c', leader_code, child_code, str(lease.fd)], pass_fds=(lease.fd,), stdout=subprocess.PIPE, text=True, start_new_session=True)
        pidfd = None
        proc = supervisor.Proc('worker-fixture', [], {})
        try:
            self.assertTrue(select.select([p.stdout], [], [], 5)[0])
            descendant = int(p.stdout.readline()); pidfd = os.pidfd_open(descendant)
            self.assertEqual(p.wait(timeout=5), 0)
            lease.close(); self.assertTrue(gpu.status(root=root)['busy'])
            proc.p = p; proc.kill(); self.assertIsNone(proc.p)
            self.assertTrue(select.select([pidfd], [], [], 5)[0])
            self.assertFalse(gpu.status(root=root)['busy'])
        finally:
            lease.close()
            if pidfd is None or not select.select([pidfd], [], [], 0)[0]:
                try: os.killpg(p.pid, signal.SIGKILL)
                except ProcessLookupError: pass
            p.wait(timeout=5); p.stdout.close()
            if pidfd is not None: os.close(pidfd)

    def test_protect_supervisor_stop_interrupts_actual_backoff_before_new_start(self):
        stop = threading.Event(); killed = threading.Event()
        proc = supervisor.Proc('worker-fixture', [], {})
        with patch.object(supervisor, 'STOP', stop), patch.object(proc, 'kill', side_effect=killed.set), patch.object(proc, 'start') as start:
            thread = threading.Thread(target=proc.restart, args=('synthetic CPU backoff',))
            thread.start()
            try:
                self.assertTrue(killed.wait(3)); stop.set(); thread.join(3)
                self.assertFalse(thread.is_alive()); start.assert_not_called()
                self.assertEqual(len(proc.restarts), 1)
            finally: stop.set(); thread.join(3)

    def test_protect_supervisor_auth_admission_failure_releases_lease_pid_and_handlers(self):
        root = self.root / 'fleet'; acquired = []
        original = gpu.GpuLease.acquire
        def acquire(kind):
            lease = original(kind, root=root); acquired.append(lease); return lease
        handlers = {s: signal.getsignal(s) for s in (signal.SIGTERM, signal.SIGINT)}
        stop = threading.Event()
        with patch.object(supervisor, 'STATE', self.root), patch.object(supervisor, 'MOCK', False), patch.object(supervisor, 'STOP', stop), patch.object(supervisor.GpuLease, 'acquire', side_effect=acquire), patch.object(supervisor, 'ensure_access_token', side_effect=UploadRejected('synthetic credential admission', 503)), patch.object(supervisor, 'build_procs') as build:
            self.assertEqual(supervisor.main(), 2); build.assert_not_called()
        self.assertEqual(len(acquired), 1)
        self.assertFalse((self.root / 'supervisor.pid').exists())
        self.assertFalse(gpu.status(root=root)['busy'])
        self.assertEqual(handlers, {s: signal.getsignal(s) for s in handlers})

    def test_protect_probe_timeout_reaps_real_owned_child_and_reports_blocked(self):
        probe = tools.load('backend_probe'); popen = subprocess.Popen; owned = []
        def spawn(command, **kwargs):
            self.assertIn('--child-runtime', command); self.assertTrue(kwargs['start_new_session'])
            p = popen([sys.executable, '-c', 'import time; time.sleep(60)'], **kwargs)
            owned.append(p); return p
        try:
            with patch.object(probe.subprocess, 'Popen', side_effect=spawn): report = probe.isolated_runtime(2, 'fp16', .15)
            self.assertEqual(report['status'], 'blocked')
            self.assertTrue(any(c['name'] == 'runtime_timeout' and c['status'] == 'blocked' for c in report['checks']))
            for key in ('model_loaded', 'inference_verified', 'training_verified', 'performance_verified'): self.assertIs(report[key], False)
            self.assertEqual(len(owned), 1); self.assertEqual(owned[0].returncode, -signal.SIGKILL)
        finally:
            for p in owned:
                if p.poll() is None: os.killpg(p.pid, signal.SIGKILL); p.wait(timeout=5)

    def test_protect_probe_callshape_inspection_never_invokes_backend_or_proves_behavior(self):
        probe = tools.load('backend_probe')
        class Backend:
            @classmethod
            def from_pretrained(cls, model_id, *, device, dtype, attn_implementation, max_seq_len): raise AssertionError('must not execute')
            def warmup(self, *, prefill_len): raise AssertionError('must not execute')
        report = {'checks': [], 'mode': 'runtime_surface'}
        probe.signature_check(report, Backend, 'from_pretrained', ['device', 'dtype', 'attn_implementation', 'max_seq_len'])
        probe.signature_check(report, Backend, 'warmup', ['prefill_len'])
        self.assertTrue(all(c['status'] == 'pass' and 'behavior untested' in c['detail'] for c in report['checks']))
        class Extra:
            def warmup(self, required_other, *, prefill_len): raise AssertionError('must not execute')
        probe.signature_check(report, Extra, 'warmup', ['prefill_len'])
        self.assertEqual(probe.finalize(report)['status'], 'blocked')

    def test_protect_benchmark_fragmented_stream_terminal_and_sample_rtf_contracts(self):
        bench = tools.load('voice_benchmark'); frame = tools.worker_frame
        stats = {'engine': 'faster-qwen3-tts', 'voice_binding': 'fixture-pin', 'speech_samples': 24000, 'rtf': .1, 'gen_ms': 100, 'gpu': 0}
        pcm = b'\x00\x00' * (24000 + 192)
        good = frame(1, pcm) + frame(2, json.dumps(stats).encode())
        cases = [('valid', good)]
        for key, value in [('speech_samples', True), ('speech_samples', 23999), ('rtf', .11), ('gen_ms', float('nan')), ('cancelled', True), ('failed', True), ('voice_binding', 'changed'), ('engine', 'mock'), ('anomalies', ['fixture'])]:
            cases.append((key + repr(value), frame(1, pcm) + frame(2, json.dumps({**stats, key: value}).encode())))
        cases += [('after-terminal', good + frame(1, b'\x00\x00')), ('duplicate-terminal', good + frame(2, b'{}')), ('partial-header', good + b'\x01'), ('oversize', struct.pack('<BI', 1, (16 << 20) + 1)), ('missing-terminal', frame(1, pcm))]
        class Response:
            closed = False
            def __enter__(self): return self
            def __exit__(self, *_): self.closed = True
            def raise_for_status(self): pass
            def iter_content(self, _): return iter([raw[:2], raw[2:7], raw[7:31], raw[31:]])
        for name, raw in cases:
            with self.subTest(name=name):
                response = Response()
                with patch('requests.post', return_value=response), patch.object(bench.time, 'perf_counter', side_effect=[10, 10.2]):
                    if name == 'valid':
                        actual, row = bench.measure('http://fixture.invalid', {'voice_binding': 'fixture-pin'})
                        self.assertEqual(actual, pcm); self.assertEqual(row['speech_seconds'], 1)
                        self.assertAlmostEqual(row['wall_rtf'], .2); self.assertEqual(row['worker_rtf'], .1)
                    else:
                        with self.assertRaises(RuntimeError): bench.measure('http://fixture.invalid', {'voice_binding': 'fixture-pin'})
                self.assertTrue(response.closed)
        # All PCM, stats, HTTP response and clocks here are explicit fixtures, not an RTF measurement.

    def test_protect_benchmark_default_output_collision_preserves_existing_private_report(self):
        bench = tools.load('voice_benchmark'); path = self.root / 'report.json'
        path.write_bytes(b'{"historical":"synthetic"}\n'); path.chmod(0o600)
        with patch.object(sys, 'argv', ['voice_benchmark.py', '--output', str(path)]), patch('requests.post') as post, patch('requests.get') as get:
            with self.assertRaises(FileExistsError): bench.main()
            post.assert_not_called(); get.assert_not_called()
        self.assertEqual(path.read_bytes(), b'{"historical":"synthetic"}\n')
        self.assertEqual(path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ['report.json'])

    def test_protect_numpy_leveler_strided_nonfinite_and_extreme_input_is_bounded_int16(self):
        self.assertEqual(audio_rt.BACKEND, 'numpy')
        x = np.tile(np.array([np.nan, 0, np.inf, 0, -np.inf, 0, 1e6, 0, -1e6, 0], dtype=np.float64), 192)[::2]
        self.assertFalse(x.flags.c_contiguous)
        level = audio_rt.Leveler(48000, max_gain_db=0, min_gain_db=0)
        try:
            level.start_segment(); out = level.process(x)
            self.assertEqual(out.dtype, np.int16); self.assertEqual(out.size, x.size)
            self.assertLessEqual(int(np.max(np.abs(out.astype(np.int32)))), 32440)
            self.assertTrue(np.isfinite(level.env_dbfs)); self.assertTrue(np.isfinite(level.gain_db))
            self.assertEqual(level.process([]).size, 0)
            tail = level.flush(); self.assertEqual(tail.size, 192); self.assertEqual(int(tail[-1]), 0)
            self.assertFalse(level.flush().any())
        finally: level.close(); level.close()
        # No chunk-invariance or F27 DC-state reset claim; no acoustic quality claim.

    def test_observed_probe_accepts_valid_shaped_receipt_after_real_child_exit23(self):
        probe = tools.load('backend_probe'); popen = subprocess.Popen; outcomes = []
        fixture = {'schema': 1, 'status': 'surface_preflight_passed', 'mode': 'runtime_surface', 'checks': [], 'model_loaded': False, 'inference_verified': False, 'training_verified': False, 'performance_verified': False, 'synthetic_producer': True}
        for exit_code in (0, 23):
            owned = []
            def spawn(command, **kwargs):
                output = command[command.index('--output') + 1]
                script = 'import json,sys; from pathlib import Path; Path(sys.argv[1]).write_text(sys.argv[2]); sys.exit(int(sys.argv[3]))'
                p = popen([sys.executable, '-c', script, output, json.dumps(fixture), str(exit_code)], **kwargs)
                owned.append(p); return p
            try:
                with patch.object(probe.subprocess, 'Popen', side_effect=spawn): report = probe.isolated_runtime(2, 'fp16', 5)
                self.assertEqual(len(owned), 1); self.assertEqual(owned[0].returncode, exit_code)
                self.assertEqual(report, fixture); outcomes.append({'child_exit': exit_code, 'accepted_status': report['status']})
            finally:
                for p in owned:
                    if p.poll() is None: os.killpg(p.pid, signal.SIGKILL); p.wait(timeout=5)
        OBSERVATIONS.append({'id': 'F37', 'fixed': False, 'original_parent_isolated_runtime_executed': True, 'real_owned_cpu_children_reaped': True, 'receipt_producer_is_synthetic': True, 'outcomes': outcomes, 'actual_gpu_preflight_false_pass_proven': False, 'model_or_gpu_executed': False})

    def test_observed_real_ctypes_abi3_missing_symbol_aborts_import_instead_of_fallback(self):
        c = self.root / 'abi_fixture.c'
        source = 'unsigned int rt_version(void) { return ABI_VERSION; }\n'
        c.write_text(source)
        compiler = subprocess.run(['/usr/bin/cc', '--version'], capture_output=True, text=True, timeout=10, check=True).stdout.splitlines()[0]
        outcomes = []
        for version, disabled in [(2, False), (3, False), (3, True)]:
            lib = self.root / ('libabi' + str(version) + '.so')
            subprocess.run(['/usr/bin/cc', '-shared', '-fPIC', '-DABI_VERSION=' + str(version), str(c), '-o', str(lib)], capture_output=True, text=True, timeout=20, check=True)
            env = {**os.environ, 'QTTS_RT_LIB': str(lib), 'QTTS_NO_RUST': '1' if disabled else '0', 'PYTHONPATH': str(ROOT / 'py'), 'OPENBLAS_NUM_THREADS': '2', 'OMP_NUM_THREADS': '2'}
            cp = subprocess.run([sys.executable, '-c', 'import audio_rt; print(audio_rt.BACKEND)'], env=env, capture_output=True, text=True, timeout=20)
            if version == 3 and not disabled:
                self.assertNotEqual(cp.returncode, 0); self.assertIn('AttributeError', cp.stderr); self.assertIn('rt_leveler_new', cp.stderr)
                result = 'AttributeError:rt_leveler_new'
            else:
                self.assertEqual(cp.returncode, 0, cp.stderr); self.assertEqual(cp.stdout.strip(), 'numpy'); result = 'numpy'
            outcomes.append({'c_fixture_abi_version': version, 'QTTS_NO_RUST': disabled, 'child_exit': cp.returncode, 'result': result})
        OBSERVATIONS.append({'id': 'F38', 'fixed': False, 'actual_ctypes_and_original_audio_rt_import_executed': True, 'c_fault_fixture_compiled_and_loaded': True, 'c_source_sha256': hashlib.sha256(source.encode()).hexdigest(), 'compiler': compiler, 'outcomes': outcomes, 'rust_compiled': False, 'rust_executed': False, 'production_rust_library_corruption_proven': False, 'model_or_gpu_executed': False})


if __name__ == '__main__': unittest.main()
