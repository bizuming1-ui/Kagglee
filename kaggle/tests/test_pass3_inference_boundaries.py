"""Third inference pass: original methods + real files/OFD/NumPy/safetensors.
Torch, Transformers, native generation, decoder/predictor and module replacement
are explicit control-flow stubs. NO tensor emulation/model/GPU/acoustic proof.
F36 witnesses cleanup ordering when the upstream iterator's close itself fails.
"""
from contextlib import contextmanager, nullcontext
import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace as NS, ModuleType
import unittest
from unittest.mock import patch, Mock

import test_reliability
import test_training_artifact_boundaries as artifacts
import numpy as np
import worker
import clone_stream as cs
import qwen_compat as qc
import gpu_ownership as gpu
from adapter_engine import AdapterEngine
from qtts_common import write_json_atomic
from resource_limits import UploadRejected
from voice_binding import reference_binding

OBSERVATIONS=[]


def last_stats(frames):
    return json.loads(next(f[5:] for f in reversed(frames) if f and f[0]==worker.F_STATS))


class InferenceBoundaries(unittest.TestCase):
    def setUp(self):
        temporary=tempfile.TemporaryDirectory(prefix='pass3-inference-')
        self.addCleanup(temporary.cleanup);self.root=Path(temporary.name)

    def artifact_adapter(self):
        fixture=artifacts.ArtifactBoundaryTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        profile={'id':'9'*32,'anchor':'anchor.wav','ref_text':'synthetic fixed text',
                 'trained_adapter':{'run_id':fixture.rid,'manifest_sha256':fixture.pin,
                 'base_model_sha256':'b'*64,'codes_id':'c'*32,'codes_manifest_sha256':'d'*64}}
        path=fixture.state/'profiles'/profile['id']/'profile.json';path.parent.mkdir(parents=True,mode=0o700)
        write_json_atomic(path,profile)
        engine=AdapterEngine(0,fixture.state,fixture.state/'unused-base','b'*64)
        return fixture,engine,profile,path

    @contextmanager
    def adapter_imports(self):
        # _select's cache/rejection branches need imports, but no tensor operation.
        lora=ModuleType('lora_adapter');lora.prepare_adapter=Mock(side_effect=AssertionError('tensor path must not run'))
        lora.commit_adapter=Mock(side_effect=AssertionError('module commit must not run'))
        prompt=ModuleType('qwen_tts.inference.qwen3_tts_model');prompt.VoiceClonePromptItem=object
        torch=ModuleType('torch')
        with patch.dict(sys.modules,{'torch':torch,'lora_adapter':lora,'qwen_tts.inference.qwen3_tts_model':prompt}):yield lora

    @contextmanager
    def stream_imports(self):
        seeds=[];torch=ModuleType('torch');torch.manual_seed=seeds.append;torch.inference_mode=nullcontext
        tf=ModuleType('transformers');tf.StoppingCriteria=type('StoppingCriteria',(),{});tf.StoppingCriteriaList=list
        # Cancel.__call__ is not invoked: no torch.full/tensor/device fake.
        with patch.dict(sys.modules,{'torch':torch,'transformers':tf}):yield seeds

    def test_protect_adapter_base_binding_rejects_before_inspection_or_cached_mutation(self):
        _,engine,profile,path=self.artifact_adapter();profile['trained_adapter']['base_model_sha256']='f'*64
        write_json_atomic(path,profile);engine.key=('old','old-pin');engine.prompt=['old-prompt']
        with self.adapter_imports() as lora,patch.object(engine.artifacts,'inspect') as inspect:
            with self.assertRaisesRegex(UploadRejected,'another Base'):engine._select(profile)
        inspect.assert_not_called();lora.prepare_adapter.assert_not_called();lora.commit_adapter.assert_not_called()
        self.assertEqual((engine.key,engine.prompt),(('old','old-pin'),['old-prompt']))

    def test_protect_cached_adapter_reinspects_actual_tensor_hash_before_reuse(self):
        artifact,engine,profile,_=self.artifact_adapter();engine.key=(profile['id'],artifact.pin);engine.prompt=['cached-prompt']
        with self.adapter_imports() as lora,patch.object(engine.artifacts,'inspect',wraps=engine.artifacts.inspect) as inspect:
            self.assertEqual(engine._select(profile),profile)
            tensor=artifact.checkpoint/'adapter.safetensors';tensor.write_bytes(tensor.read_bytes()+b'changed')
            with self.assertRaisesRegex(UploadRejected,'tensor file hash changed'):engine._select(profile)
            self.assertEqual(inspect.call_count,2)
        self.assertEqual(engine.prompt,['cached-prompt']);lora.prepare_adapter.assert_not_called();lora.commit_adapter.assert_not_called()

    def test_protect_adapter_codes_binding_mismatch_rejects_without_tensor_prepare(self):
        artifact,engine,profile,path=self.artifact_adapter();profile['trained_adapter']['codes_id']='e'*32
        write_json_atomic(path,profile)
        with self.adapter_imports() as lora:
            with self.assertRaisesRegex(UploadRejected,'binding mismatch'):engine._select(profile)
        lora.prepare_adapter.assert_not_called();lora.commit_adapter.assert_not_called()
        self.assertIsNone(engine.key);self.assertIsNone(engine.prompt)

    def test_protect_adapter_cancel_before_selection_never_generates_or_seeds(self):
        _,engine,profile,_=self.artifact_adapter();cancel=threading.Event();cancel.set()
        engine.model=NS(generate_voice_clone=Mock(side_effect=AssertionError('must not generate')))
        with self.stream_imports() as seeds,patch.object(engine,'_select') as select:
            self.assertEqual(list(engine.stream(profile,'fixture','Auto',4,10,7,cancel)),[])
        select.assert_not_called();engine.model.generate_voice_clone.assert_not_called();self.assertEqual(seeds,[])

    def test_protect_adapter_cancel_after_buffered_generation_discards_all_returned_pcm(self):
        _,engine,profile,_=self.artifact_adapter();engine.prompt=['fixture-prompt'];cancel=threading.Event();calls=[]
        def generate(**kwargs):calls.append(kwargs);cancel.set();return [np.full(4800,.02,np.float32)],24000
        engine.model=NS(generate_voice_clone=generate)
        with self.stream_imports() as seeds,patch.object(engine,'_select',return_value=profile):
            self.assertEqual(list(engine.stream(profile,'目标','Chinese',4,20,2**40+3,cancel)),[])
        self.assertEqual(seeds,[3]);self.assertEqual(len(calls),1)
        self.assertTrue(calls[0]['non_streaming_mode']);self.assertIs(calls[0]['voice_clone_prompt'],engine.prompt)
        self.assertEqual(len(calls[0]['stopping_criteria']),1)

    def test_protect_adapter_rejects_bad_native_pcm_and_emits_one_valid_sentence(self):
        _,engine,profile,_=self.artifact_adapter();cancel=threading.Event()
        cases=[([],24000),([np.ones(4)],16000),(np.ones(4),24000),([np.ones((1,4))],24000),
               ([np.zeros(4)],24000),([np.array([float('nan')])],24000),([np.ones(43201)],24000)]
        with self.stream_imports(),patch.object(engine,'_select',return_value=profile):
            for waves,sr in cases:
                engine.model=NS(generate_voice_clone=lambda waves=waves,sr=sr,**kwargs:(waves,sr))
                with self.subTest(sr=sr),self.assertRaises(RuntimeError):list(engine.stream(profile,'目标','Auto',4,10,7,cancel))
            engine.model=NS(generate_voice_clone=lambda **kwargs:([np.full(4800,.03,np.float64)],24000))
            output=list(engine.stream(profile,'目标','Auto',4,10,7,cancel))
        self.assertEqual(len(output),1);self.assertEqual(output[0].dtype,np.float32);self.assertEqual(output[0].shape,(4800,))

    def test_protect_realengine_metrics_accumulate_and_replay_closes_on_exhaustion(self):
        engine=worker.RealEngine(0);engine._prompts['v']={'fixture':True};engine.model=NS();seeds=[]
        class Replay:
            def __init__(self):self.rows=iter([(np.ones(1920,np.float32),24000,{'prepare_ms':5,'codec_ms':2,'decode_ms':3,'codec_window_frames':4}),
                (np.ones(3840,np.float32),24000,{'prepare_ms':4,'codec_ms':7,'decode_ms':11,'codec_window_frames':6})]);self.closed=0
            def __iter__(self):return self
            def __next__(self):return next(self.rows)
            def close(self):self.closed+=1
        replay=Replay();prof={'id':'v','anchor':'a.wav','ref_text':'fixture'}
        with patch.dict(sys.modules,{'torch':NS(manual_seed=seeds.append)}),patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}),patch.object(worker,'generated_only_stream',return_value=replay):
            output=list(engine.stream(prof,'目标','Auto',4,10,7,threading.Event()))
        self.assertEqual([len(a) for a in output],[1920,3840]);self.assertEqual(replay.closed,1);self.assertEqual(seeds,[7])
        self.assertEqual(engine.last_stream_metrics,{'prepare_ms':5.,'codec_ms':9.,'token_decode_ms':14.,'codec_window_frames':6,'reference_codes_decoded':0})

    def runtime(self):
        (self.root/'a.wav').write_bytes(b'synthetic reference, not playback')
        profile={'id':'v','anchor':'a.wav','ref_text':'fixture','units_per_sec':4.5}
        runtime=worker.Worker();runtime.ready=True
        def close():
            for leveler in runtime.levelers.values():leveler.close()
        self.addCleanup(close)
        return runtime,profile

    def test_protect_worker_partial_generation_error_releases_lock_and_next_job_runs(self):
        runtime,profile=self.runtime();first=[];second=[]
        def broken(*args):yield np.full(4800,.05,np.float32);raise RuntimeError('synthetic generation failure')
        with patch.object(worker,'profile_dir',return_value=self.root),patch.object(worker,'load_profile',return_value=profile),patch.object(runtime,'after_job') as after:
            with patch.object(runtime.engine,'stream',side_effect=broken):runtime.run_job({'profile':'v','text':'你好'},first.append,threading.Event(),worker.now_ms())
            self.assertTrue(last_stats(first)['failed']);self.assertFalse(runtime.busy)
            self.assertTrue(runtime.lock.acquire(blocking=False));runtime.lock.release()
            with patch.object(runtime.engine,'stream',return_value=iter([np.full(4800,.05,np.float32)])):
                runtime.run_job({'profile':'v','text':'你好'},second.append,threading.Event(),worker.now_ms())
            self.assertEqual(after.call_count,2)
        self.assertEqual(sum(bool(f) and f[0]==worker.F_ERR for f in first),1)
        self.assertEqual(sum(bool(f) and f[0]==worker.F_STATS for f in first),1);self.assertIsNone(first[-1])
        self.assertIsNone(second[-1]);self.assertNotIn('failed',last_stats(second));self.assertEqual((runtime.failed,runtime.served),(1,1))

    def test_protect_worker_missing_prompt_reloads_even_with_same_disk_pin(self):
        runtime,profile=self.runtime();engine=worker.RealEngine(0);engine.sane=True;resolver=Mock(return_value=({'fixture':True},[],True))
        engine.model=NS(_voice_prompt_cache={},_resolve_voice_clone_prompt_from_reference=resolver);runtime.engine=engine
        pin=reference_binding(self.root,profile);runtime.profiles['v']=profile;runtime.voice_bindings['v']=pin;frames=[]
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}),patch.object(worker,'profile_dir',return_value=self.root),patch.object(worker,'load_profile',return_value=profile),patch.object(engine,'stream',return_value=iter([np.full(4800,.05,np.float32)])),patch.object(runtime,'after_job'):
            runtime.run_job({'profile':'v','text':'你好','voice_binding':pin},frames.append,threading.Event(),worker.now_ms())
        resolver.assert_called_once();self.assertIn('v',engine._prompts);self.assertNotIn('failed',last_stats(frames))
        self.assertEqual(last_stats(frames)['voice_binding'],pin)

    def test_protect_rope_failed_import_retains_cause_and_retry_installs_single_bridge(self):
        def original(config,**kwargs):return config.rope_theta
        original.__module__='qwen_tts._transformers_compat';original.__name__='_default_rope_parameters'
        module=NS(_default_rope_parameters=original);other=object();registry={'default':original,'other':other}
        cause=ImportError('synthetic dependency error')
        with patch.object(qc,'installed_version',side_effect=qc.PINS.get),patch.object(qc.importlib,'import_module',side_effect=[cause,module]),patch.dict(sys.modules,{'transformers.modeling_rope_utils':NS(ROPE_INIT_FUNCTIONS=registry)}):
            with self.assertRaises(qc.BackendCompatibilityError) as caught:qc.install_qwen_rope_bridge()
            self.assertIs(caught.exception.__cause__,cause);self.assertIs(registry['default'],original)
            self.assertEqual(qc.install_qwen_rope_bridge()['status'],'installed')
            bridged=registry['default'];qc.bridge_registry(module,registry);self.assertIs(registry['default'],bridged)
        self.assertIs(registry['other'],other);self.assertEqual(bridged(NS(rope_parameters={'rope_type':'default','rope_theta':123.})),123.)

    def test_protect_gpu_short_record_write_closes_lock_and_new_owner_can_acquire(self):
        root=self.root/'gpu';write=os.pwrite
        with patch.object(gpu.os,'pwrite',side_effect=lambda fd,raw,offset:write(fd,raw[:-2],offset)):
            with self.assertRaisesRegex(OSError,'short GPU lease record write'):gpu.GpuLease.acquire('inference',root=root)
        status=gpu.status(root=root);self.assertFalse(status['busy']);self.assertIsNone(status['last_record'])
        self.assertTrue((root/'fleet.lock').exists());self.assertEqual((root/'fleet.lock').stat().st_mode&0o777,0o600)
        with gpu.GpuLease.acquire('offline-reservation',root=root):self.assertTrue(gpu.status(root=root)['busy'])
        self.assertFalse(gpu.status(root=root)['busy'])

    def test_observed_upstream_close_failure_skips_codec_window_final_cleanup(self):
        window=cs.GeneratedCodecWindow(object());cancel=threading.Event();closes=[]
        class Replay:
            def __iter__(self):return self
            def __next__(self):return object(),{}
            def close(self):closes.append(True);raise RuntimeError('synthetic upstream close failure')
        def push(chunk):
            window.codes='synthetic retained marker, not tensor';window.pending=np.ones(1920,np.float32)
            return np.ones(1920,np.float32)
        torch=ModuleType('torch');torch.inference_mode=nullcontext
        upstream=ModuleType('faster_qwen3_tts.streaming');upstream.fast_generate_streaming=lambda **kwargs:Replay()
        model=NS(_prepare_generation=lambda **kwargs:(NS(speech_tokenizer=object()),None,None,None,None,None,None,'reference conditioning marker'),predictor_graph=None,talker_graph=None)
        with patch.dict(sys.modules,{'torch':torch,'faster_qwen3_tts.streaming':upstream}),patch.object(cs,'GeneratedCodecWindow',return_value=window),patch.object(window,'push',side_effect=push):
            stream=cs.generated_only_stream(model,text='目标',language='Auto',ref_audio='not opened',ref_text='fixture',xvec_only=False,
                chunk_size=4,max_new_tokens=10,temperature=.8,top_k=50,top_p=1.,repetition_penalty=1.05,cancel=cancel)
            try:
                self.assertEqual(next(stream)[0].size,1920)
                with self.assertRaisesRegex(RuntimeError,'upstream close failure'):stream.close()
                self.assertEqual(len(closes),1);self.assertFalse(window.closed)
                self.assertIsNotNone(window.codes);self.assertEqual(window.pending.size,1920)
                self.assertIsNone(stream.gi_frame)
            finally:window.finish(cancelled=True);stream.close()
        self.assertTrue(window.closed);self.assertIsNone(window.codes);self.assertEqual(window.pending.size,0)
        OBSERVATIONS.append({'id':'F36','fixed':False,'original_generated_only_stream_finally_executed':True,
            'consumer_closed_started_generator':True,'upstream_close_calls':1,'upstream_close_raises_fixture_error':True,
            'codec_window_closed_before_explicit_test_cleanup':False,'pending_samples_before_explicit_cleanup':1920,
            'code_marker_retained_before_explicit_cleanup':True,'explicit_test_cleanup_completed':True,
            'prepare_predictor_decoder_and_torch_context_are_control_fixtures':True,'actual_tensor_model_or_gpu_executed':False,
            'production_upstream_close_raises_or_gpu_memory_leak_proven':False})


if __name__=='__main__':unittest.main()
