"""CPU-only regression tests. These are not T4 performance or voice-quality tests."""
import concurrent.futures
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import subprocess
import tarfile
import tempfile
import time
import unittest
from types import SimpleNamespace
from unittest.mock import patch, MagicMock

ROOT = Path(__file__).resolve().parents[1] / 'source'
STATE = tempfile.TemporaryDirectory(prefix='qtts-unit-')
os.environ['QTTS_STATE'] = STATE.name
os.environ['QTTS_MOCK'] = '1'
sys.path.insert(0, str(ROOT / 'py'))
import numpy as np
import audio_rt
import bootstrap
import persist
import qtts_common as common
import worker

class ReliabilityTests(unittest.TestCase):
    def test_t4_never_automatically_falls_back_to_bf16(self):
        self.assertIsNone(worker.next_fallback_dtype('fp16', False, False))
        self.assertEqual(worker.next_fallback_dtype('fp16', False, True), 'fp32')
        self.assertEqual(worker.next_fallback_dtype('fp16', True, False), 'bf16')
        self.assertIsNone(worker.next_fallback_dtype('fp32', True, True))

    def test_emulated_bf16_does_not_count_as_native_t4_support(self):
        cuda = SimpleNamespace(get_device_capability=lambda:(7,5), is_bf16_supported=lambda:True)
        self.assertFalse(worker.native_bf16_supported(SimpleNamespace(cuda=cuda)))
        cuda.get_device_capability=lambda:(8,0)
        self.assertTrue(worker.native_bf16_supported(SimpleNamespace(cuda=cuda)))

    def test_stream_rejects_wrong_sample_rate(self):
        engine=worker.RealEngine(0);engine._prompts['voice']={}
        engine.model=SimpleNamespace(generate_voice_clone_streaming=lambda **kw:iter([(np.zeros(32),22050,None)]))
        fake_torch=SimpleNamespace(manual_seed=lambda seed:None)
        import threading
        with patch.dict(sys.modules, {'torch':fake_torch}), patch.object(worker,'generated_only_stream',return_value=iter([(np.zeros(32),22050,{})])):
            with self.assertRaisesRegex(RuntimeError, '22050Hz'):
                list(engine.stream({'id':'voice','anchor':'unused.wav','ref_text':'text'},'你好','Chinese',4,64,1,threading.Event()))

    def test_silent_subprocess_timeout_is_enforced(self):
        t = time.monotonic()
        with self.assertRaises(TimeoutError):
            bootstrap.sh([sys.executable, '-c', 'import time;time.sleep(10)'], timeout=.2)
        self.assertLess(time.monotonic()-t, 2)

    def test_subprocess_exit_status_is_not_hidden(self):
        self.assertEqual(bootstrap.sh([sys.executable, '-c', 'raise SystemExit(7)'], check=False), 7)
        with self.assertRaises(RuntimeError):
            bootstrap.sh([sys.executable, '-c', 'raise SystemExit(7)'])

    def test_bootstrap_dependency_import_has_timeout_and_discards_library_logs(self):
        process=MagicMock(pid=123456)
        process.wait.side_effect=[subprocess.TimeoutExpired('fake',60),None]
        with patch.object(bootstrap.subprocess,'Popen',return_value=process) as spawn,patch.object(bootstrap.os,'killpg') as kill:
            self.assertFalse(bootstrap.can_import('faster_qwen3_tts'))
            self.assertEqual(spawn.call_args.kwargs['stdout'],subprocess.DEVNULL)
            self.assertEqual(spawn.call_args.kwargs['stderr'],subprocess.DEVNULL)
            kill.assert_called_once()

    def test_two_gpus_are_required_by_default(self):
        for count in (0,1):
            with tempfile.TemporaryDirectory() as directory, patch.object(bootstrap,'STATE',Path(directory)), patch.object(bootstrap,'sh') as shell, patch.object(bootstrap, 'detect_gpus', return_value=count), patch.dict(os.environ, {'QTTS_ALLOW_SINGLE_GPU':'0'}):
                self.assertEqual(bootstrap.main(), 2)
                report=json.loads((Path(directory)/'backend_probe.json').read_text())
                self.assertEqual(report['status'],'blocked');self.assertFalse(report['model_loaded'])
                shell.assert_not_called()

    def test_cancel_arriving_at_lock_acquisition_never_starts_synthesis(self):
        import threading
        cancel=threading.Event()
        class CancelAtAcquisition:
            released=False
            def acquire(self, **kw):cancel.set();return True
            def release(self):self.released=True
        w=worker.Worker();w.ready=True;w.profiles['voice']={'id':'voice'}
        w.lock=CancelAtAcquisition();emitted=[]
        w.run_job({'profile':'voice','text':'已取消'},emitted.append,cancel,common.now_ms())
        self.assertEqual(w.failed,0)
        self.assertEqual(w.served,0)
        self.assertTrue(w.lock.released)
        self.assertIsNone(emitted[-1])
        self.assertEqual(len(emitted),2)
        self.assertEqual(emitted[0][0],worker.F_STATS)

    def test_empty_e2e_run_is_a_clean_failure_not_a_pass_or_format_crash(self):
        spec=importlib.util.spec_from_file_location('qtts_e2e',ROOT/'tools/e2e_check.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        empty={'ev':[], 'segs':{}, 'stats':{}, 'sid':'empty','wall':.1,'end':None,'errors':[],'policy':{}}
        output=io.StringIO()
        with patch.object(module,'run',return_value=empty), patch.object(sys,'argv',['e2e_check.py']), contextlib.redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:module.main()
        self.assertEqual(raised.exception.code,1)
        self.assertIn('[FAIL] every segment has audio',output.getvalue())

    def test_concurrent_atomic_json_writes(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'value.json'
            def write(n): common.write_json_atomic(target, {'n':n,'text':'你好'*100})
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
                list(pool.map(write, range(80)))
            self.assertIn(json.loads(target.read_text())['n'], range(80))
            self.assertEqual(list(Path(d).glob('*.tmp')), [])

    def test_numpy_audio_fallback_accepts_all_short_chunks(self):
        with patch.object(audio_rt, '_LIB', None):
            lv=audio_rt.Leveler(24000)
            for n in [0,1,32,64,65,96,120,239,400,479,480,481,24000]:
                x=(np.sin(np.arange(n)*.08)*.1).astype(np.float32)
                lv.start_segment();y=lv.process(x)
                self.assertEqual(y.shape,x.shape, f'length={n}')
                self.assertEqual(y.dtype,np.int16)
                self.assertTrue(np.isfinite(y).all())

    def test_short_recorded_breath_does_not_broadcast_fail(self):
        w=worker.Worker();w.breath_banks['voice']=[np.ones(65,np.float32)*.01]
        a=w.lead_audio({'id':'voice'},300,True,1)
        self.assertEqual(a.shape,(7200,))
        self.assertTrue(np.isfinite(a).all())

    def archive(self, members):
        f=io.BytesIO()
        with tarfile.open(fileobj=f,mode='w') as tf:
            for name,typ,link in members:
                m=tarfile.TarInfo(name);m.type=typ;m.linkname=link
                if typ==tarfile.REGTYPE:
                    data=b'{}';m.size=len(data);tf.addfile(m,io.BytesIO(data))
                else:tf.addfile(m)
        f.seek(0);return tarfile.open(fileobj=f)

    def test_tar_rejects_traversal_symlinks_and_unexpected_files(self):
        for name,typ,link in [('profiles/../escape',tarfile.REGTYPE,''),('/absolute',tarfile.REGTYPE,''),('profiles/link',tarfile.SYMTYPE,'/tmp'),('profiles/hard',tarfile.LNKTYPE,'active.json'),('unexpected.py',tarfile.REGTYPE,'')]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as d:
                with self.archive([('active.json',tarfile.REGTYPE,''),(name,typ,link)]) as tf:
                    with self.assertRaises(ValueError): persist.extract_state_members(tf,Path(d))
                self.assertEqual(list(Path(d).iterdir()),[])

    def test_tar_does_not_follow_existing_destination_escape_link(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as outside:
            (Path(d)/'profiles').symlink_to(outside,target_is_directory=True)
            with self.archive([('profiles/escape.json',tarfile.REGTYPE,'')]) as tf:
                with self.assertRaises(ValueError):persist.extract_state_members(tf,Path(d))
            self.assertEqual(list(Path(outside).iterdir()),[])

    def test_tar_restores_valid_voice_assets(self):
        with tempfile.TemporaryDirectory() as d:
            with self.archive([('profiles/voice/profile.json',tarfile.REGTYPE,''),('active.json',tarfile.REGTYPE,'')]) as tf:
                persist.extract_state_members(tf,Path(d))
            self.assertEqual((Path(d)/'profiles/voice/profile.json').read_text(),'{}')

    def test_selftest_missing_profile_is_not_a_pass(self):
        spec=importlib.util.spec_from_file_location('qtts_selftest',ROOT/'tools/selftest.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        self.assertIsNone(module.t_stream(None))
        self.assertEqual(module.RESULTS[-1]['status'],'skipped')
        self.assertIsNone(module.RESULTS[-1]['ok'])

if __name__=='__main__':unittest.main()
