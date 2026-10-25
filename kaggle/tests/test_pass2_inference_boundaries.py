"""Pass2 inference lifecycle. CPU files/threads/ASGI; NO Torch/model/codec run.
One observation deliberately confirms an unfixed early-disconnect cancellation gap.
Minimal manual_seed and replay iterators are explicit fixtures, not Torch emulation.
"""
import asyncio
import copy
import json
import os
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

import test_reliability
import numpy as np
import worker
import qwen_compat as qc
from adapter_engine import AdapterEngine
from voice_binding import reference_binding,generation_bytes,MAX_REFERENCE_BYTES
from qtts_common import write_json_atomic
from resource_limits import UploadRejected
from starlette.requests import ClientDisconnect

OBSERVATIONS=[]
SOURCE=Path(__file__).resolve().parents[1]/'source/py'


class Replay:
    def __init__(self,rows):self.rows=iter(rows);self.closed=0
    def __iter__(self):return self
    def __next__(self):return next(self.rows)
    def close(self):self.closed+=1


class InferenceBoundaries(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)

    def test_protect_binding_equivalent_generation_defaults_and_metadata_exclusion(self):
        (self.root/'a.wav').write_bytes(b'synthetic reference bytes')
        prof={'anchor':'a.wav','ref_text':'合成转写','language':'Chinese'}
        explicit={**prof,'gen':{'temperature':.8,'top_k':50.,'top_p':1,'repetition_penalty':1.05}}
        self.assertEqual(generation_bytes(prof),generation_bytes(explicit))
        self.assertEqual(reference_binding(self.root,prof),reference_binding(self.root,{**explicit,'quality':.99,'name':'display only','candidates':[{'text':'unused'}]}))
        for key,value in [('temperature',0),('temperature',2.01),('top_k',4097),('top_k',False),('top_p',0),('repetition_penalty',4.01)]:
            with self.subTest(key=key,value=value),self.assertRaises(ValueError):generation_bytes({'gen':{key:value}})
        self.assertEqual(struct.unpack('<4d',generation_bytes({'gen':{'top_k':-0.0}}))[1],0.)

    def test_protect_reference_sparse_oversize_and_empty_rejected_before_read(self):
        path=self.root/'a.wav'
        for size in (0,MAX_REFERENCE_BYTES+1):
            with path.open('wb') as f:f.truncate(size)
            with self.assertRaisesRegex(ValueError,'size/type'):reference_binding(self.root,{'anchor':'a.wav'})

    def test_protect_reference_fifo_rejected_without_waiting_for_writer(self):
        path=self.root/'a.wav';os.mkfifo(path)
        code="from pathlib import Path;from voice_binding import reference_binding;import sys\ntry:reference_binding(Path(sys.argv[1]),{'anchor':'a.wav'})\nexcept ValueError:print('fifo-rejected')\nelse:raise AssertionError('FIFO accepted')"
        env={**os.environ,'PYTHONPATH':str(SOURCE)}
        result=subprocess.run([sys.executable,'-c',code,str(self.root)],env=env,capture_output=True,text=True,timeout=3)
        self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(result.stdout.strip(),'fifo-rejected')

    def test_protect_queued_cancel_never_reads_profile_or_releases_other_owner_lock(self):
        lock=threading.Lock();entered=threading.Event();lock.acquire();released=[]
        class ProbeLock:
            def acquire(self,**kw):entered.set();return lock.acquire(**kw)
            def release(self):released.append(True);lock.release()
        runtime=worker.Worker();runtime.ready=True;runtime.lock=ProbeLock();cancel=threading.Event();frames=[]
        thread=threading.Thread(target=runtime.run_job,args=({'profile':'v','text':'合成文本'},frames.append,cancel,worker.now_ms()))
        with patch.object(worker,'load_profile') as load,patch.object(runtime.engine,'stream') as stream:
            try:
                thread.start();self.assertTrue(entered.wait(3));cancel.set();thread.join(3)
                self.assertFalse(thread.is_alive());self.assertTrue(lock.locked());self.assertEqual(released,[])
                load.assert_not_called();stream.assert_not_called()
            finally:
                cancel.set()
                if lock.locked():lock.release()
                thread.join(3)
        self.assertEqual(sum(f is None for f in frames),1)
        self.assertEqual(sum(bool(f) and f[0]==worker.F_STATS for f in frames),1)
        self.assertFalse(any(f and f[0]==worker.F_PCM for f in frames))
        self.assertEqual((runtime.served,runtime.failed),(0,0))
        # Existing early-cancel stats lack cancelled:true. This protection is
        # admission/ownership only, not terminal-status semantic signoff.

    def test_protect_first_load_reference_change_does_not_commit_worker_binding(self):
        anchor=self.root/'a.wav';anchor.write_bytes(b'original synthetic reference')
        prof={'id':'v','anchor':'a.wav','ref_text':'合成转写'}
        runtime=worker.Worker();runtime.ready=True
        def load(p):anchor.write_bytes(b'changed synthetic reference');return {'fixture':True}
        with patch.object(worker,'profile_dir',return_value=self.root),patch.object(worker,'load_profile',return_value=prof),patch.object(runtime.engine,'load_profile',side_effect=load):
            with self.assertRaisesRegex(RuntimeError,'reference changed during prompt extraction'):runtime.load_profile('v')
        self.assertNotIn('v',runtime.profiles);self.assertNotIn('v',runtime.voice_bindings)
        self.assertTrue(runtime.lock.acquire(blocking=False));runtime.lock.release()
        # Does not assert engine-internal prompt rollback: existing F08 is unfixed.

    def engine(self):
        engine=worker.RealEngine(0);engine._prompts['v']={'fixture':True};engine.model=NS()
        return engine,{'id':'v','anchor':'a.wav','ref_text':'合成转写'}

    def test_protect_realengine_rate_failure_closes_replay_iterator_once(self):
        engine,prof=self.engine();replay=Replay([(np.ones(4800,np.float32),22050,{})])
        with patch.dict(sys.modules,{'torch':NS(manual_seed=lambda seed:None)}),patch.object(worker,'generated_only_stream',return_value=replay):
            with self.assertRaisesRegex(RuntimeError,'22050Hz'):list(engine.stream(prof,'目标','Chinese',4,80,7,threading.Event()))
        self.assertEqual(replay.closed,1)

    def test_protect_realengine_consumer_close_closes_replay_and_masks_seed(self):
        engine,prof=self.engine();seeds=[]
        replay=Replay([(np.ones(4800,np.float32),24000,{'codec_ms':2,'codec_window_frames':4})]*2)
        with patch.dict(sys.modules,{'torch':NS(manual_seed=seeds.append)}),patch.object(worker,'generated_only_stream',return_value=replay):
            stream=engine.stream(prof,'目标','Chinese',4,80,2**40+3,threading.Event())
            try:self.assertEqual(next(stream).size,4800)
            finally:stream.close()
        self.assertEqual(replay.closed,1);self.assertEqual(seeds,[3])
        self.assertEqual(engine.last_stream_metrics['codec_ms'],2)

    def test_protect_realengine_no_prompt_never_opens_generation_iterator(self):
        engine,prof=self.engine();engine._prompts.clear()
        with patch.dict(sys.modules,{'torch':NS(manual_seed=lambda seed:None)}),patch.object(worker,'generated_only_stream') as generate:
            with self.assertRaisesRegex(RuntimeError,'prompt must be loaded'):list(engine.stream(prof,'目标','Chinese',4,80,7,threading.Event()))
        generate.assert_not_called()

    def test_protect_rope_bridge_preserves_other_registry_entries_and_original_error(self):
        cfg=NS(rope_parameters={'rope_type':'default','rope_theta':12345.});before=copy.deepcopy(cfg.__dict__);calls=[]
        def original(config,**kwargs):
            calls.append((config,kwargs));raise RuntimeError('upstream fixture failure')
        original.__module__='qwen_tts._transformers_compat';original.__name__='_default_rope_parameters'
        other=object();module=NS(_default_rope_parameters=original);registry={'default':original,'other':other}
        qc.bridge_registry(module,registry)
        with self.assertRaisesRegex(RuntimeError,'upstream fixture failure'):registry['default'](cfg,device='cpu',seq_len=17)
        self.assertEqual(cfg.__dict__,before);self.assertIs(registry['other'],other)
        self.assertIsNot(calls[0][0],cfg);self.assertEqual(calls[0][0].rope_theta,12345.)
        self.assertEqual(calls[0][1],{'device':'cpu','seq_len':17,'layer_type':None})

    def adapter(self):
        pid='a'*32;directory=self.root/'profiles'/pid;directory.mkdir(parents=True)
        prof={'id':pid,'anchor':'a.wav','ref_text':'合成转写','trained_adapter':{'run_id':'1'*32,'manifest_sha256':'2'*64,'base_model_sha256':'3'*64,'codes_id':'4'*32,'codes_manifest_sha256':'5'*64}}
        path=directory/'profile.json';write_json_atomic(path,prof)
        return AdapterEngine(0,self.root,self.root/'unused-base','3'*64),prof,path

    def test_protect_adapter_profile_disk_rebind_and_deletion_fail_closed(self):
        engine,prof,path=self.adapter();self.assertEqual(engine._profile_now(prof),prof)
        changed=copy.deepcopy(prof);changed['trained_adapter']['manifest_sha256']='6'*64
        write_json_atomic(path,changed)
        with self.assertRaisesRegex(UploadRejected,'trained profile changed'):engine._profile_now(prof)
        write_json_atomic(path,prof);self.assertEqual(engine._profile_now(prof),prof)
        path.unlink()
        with self.assertRaises(FileNotFoundError):engine._profile_now(prof)
        self.assertIsNone(engine.key);self.assertIsNone(engine.model)

    def test_protect_adapter_profile_symlink_and_read_budget_fail_closed(self):
        engine,prof,path=self.adapter();outside=self.root/'outside.json';path.rename(outside);path.symlink_to(outside)
        with self.assertRaises((UploadRejected,OSError)):engine._profile_now(prof)
        path.unlink();path.write_bytes(b' ' *((256<<10)+1))
        with self.assertRaisesRegex(UploadRejected,'profile byte budget'):engine._profile_now(prof)
        write_json_atomic(path,prof);self.assertEqual(engine._profile_now(prof),prof)
        self.assertIsNone(engine.key);self.assertIsNone(engine.prompt)

    def test_observed_asgi_header_disconnect_before_first_iteration_loses_cancel(self):
        started=threading.Event();finished=threading.Event();captured=[];threads=[];sent=[]
        def produce(body,emit,cancel,t_req):
            captured.append(cancel);threads.append(threading.current_thread());started.set()
            cancel.wait(10);finished.set()
        async def request_body():return {'profile':'fixture','text':'合成文本'}
        async def receive():raise AssertionError('ASGI 2.4 path must fail on send first')
        async def send(message):
            sent.append(message['type']);raise OSError('fixture disconnect before body starts')
        async def experiment():
            with patch.object(worker,'W',NS(run_job=produce)):
                response=await worker.synth(NS(json=request_body))
                try:
                    self.assertTrue(await asyncio.to_thread(started.wait,3))
                    with self.assertRaises(ClientDisconnect):await response({'type':'http','asgi':{'spec_version':'2.4'}},receive,send)
                    await response.body_iterator.aclose()  # unstarted async generator: finally is not entered
                    self.assertEqual(sent,['http.response.start'])
                    self.assertFalse(captured[0].is_set());self.assertFalse(finished.is_set())
                finally:
                    if captured:captured[0].set()
                    for thread in threads:thread.join(3);self.assertFalse(thread.is_alive())
                    await response.body_iterator.aclose()
        asyncio.run(experiment());self.assertTrue(finished.is_set())
        OBSERVATIONS.append({'id':'F18','fixed':False,'original_synth_and_real_streaming_response_executed':True,
            'asgi_spec_version':'2.4','send_disconnect_before_body_is_fixture':True,'body_iteration_started':False,
            'producer_cancel_set_by_response':False,'producer_still_waiting_after_disconnect':True,
            'fixture_thread_cleanup_verified':True,'actual_model_executed':False,'tcp_or_browser_executed':False})


if __name__=='__main__':unittest.main()
