"""CPU real LoRA math + explicitly injected native API fixtures, NOT Qwen/NCCL evidence."""
from contextlib import contextmanager
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
import types
import unittest
from unittest.mock import patch
import numpy as np
import test_training_codes as helpers
from test_tts_training import TORCH
from trained_profiles import TrainedArtifacts,guard_profile,binding_of
from resource_limits import UploadRejected
if TORCH:
    import torch
    from test_tts_training import TinyCore
    from lora_adapter import inject_lora,adapter_state,adapter_digest,prepare_adapter,commit_adapter
    from training_job import save_checkpoint
    from adapter_engine import AdapterEngine

ROOT=Path(__file__).resolve().parents[1]/'source'


@unittest.skipUnless(TORCH,'optional torch tests')
class AdapterTests(helpers.Fixture,unittest.TestCase):
    def setUp(self):
        helpers.Fixture.setUp(self);self.store=TrainedArtifacts(self.state);torch.manual_seed(17)
        self.core=TinyCore();self.core.device=torch.device('cpu');self.core.dtype=torch.float32
        self.base=copy.deepcopy(self.core);self.x=torch.tensor([[.2,-.4,.8,1.]])
        self.ids=['1'*32,'2'*32,'3'*32];self.profile_id='4'*32
        self.make_run('a'*32,.1,2)

    def make_run(self,rid,value,rank):
        core=copy.deepcopy(self.base);targets=inject_lora(core,rank,4)
        with torch.no_grad():
            for name,weight in core.named_parameters():
                if name.endswith(('.lora_A','.lora_B')):weight.fill_(value)
        run=self.state/'training_runs'/rid;run.mkdir()
        req={'run_dir':str(run),'model_sha256':'b'*64,'codes_id':'c'*32,'codes_sha256':'d'*64,
             'sample_ids':self.ids,'lora_rank':rank,'lora_alpha':4,'epochs':1,'confirm_data_reviewed':True,'ack_experimental_training':True}
        # These NCCL-shaped records are hand-built fixtures. NO NCCL was executed.
        reports=[{'rank':r,'world_size':2,'backend':'nccl','parameters_changed':True,'adapter_sha256':adapter_digest(core),
                  'epochs':[{'epoch':0,'optimizer_steps':1,'loss_mean':1.,'seen_ids':self.ids[r::2]}]} for r in (0,1)]
        save_checkpoint(req,core,torch.ones(1,4)*value,targets,reports)
        (run/'request.json').write_text(json.dumps(req));(run/'result.json').write_text(json.dumps({'status':'completed','job_id':rid,'rank_exit_codes':[0,0],
             'optimizer_execution_observed':True,'checkpoint_relative_directory':f'training_runs/{rid}/adapter'}))
        pin=hashlib.sha256((run/'adapter/manifest.json').read_bytes()).hexdigest()
        binding={'run_id':rid,'manifest_sha256':pin,'base_model_sha256':'b'*64,'codes_id':'c'*32,'codes_manifest_sha256':'d'*64}
        return binding

    def profile(self,rid='a'*32,pid=None):
        record=self.store.inspect(rid);pid=pid or self.profile_id
        profile={'id':pid,'trained_adapter':{'run_id':rid,'manifest_sha256':record['manifest_sha256'],
                 'base_model_sha256':'b'*64,'codes_id':'c'*32,'codes_manifest_sha256':'d'*64},'gen':{}}
        directory=self.state/'profiles'/pid;directory.mkdir(parents=True,exist_ok=True)
        (directory/'profile.json').write_text(json.dumps(profile));return profile

    def engine(self):
        engine=AdapterEngine(0,self.state,self.state/'base','b'*64)
        engine.model=types.SimpleNamespace(model=self.core);return engine

    @contextmanager
    def native_api(self):
        class Prompt:
            def __init__(self,**kwargs):self.__dict__.update(kwargs)
        class Stop:pass
        modules={'qwen_tts':types.ModuleType('qwen_tts'),'qwen_tts.inference':types.ModuleType('qwen_tts.inference'),
                 'qwen_tts.inference.qwen3_tts_model':types.SimpleNamespace(VoiceClonePromptItem=Prompt),
                 'transformers':types.SimpleNamespace(StoppingCriteria=Stop,StoppingCriteriaList=list)}
        with patch.dict(sys.modules,modules):yield

    def test_pinned_manifest_and_rank_weight_digest(self):
        rec=self.store.inspect('a'*32);self.assertEqual(rec['speaker'].shape,(1,4))
        self.assertEqual(set(rec['weights']),set(adapter_state(self._mounted(rec))));self.assertFalse(self.store.describe('a'*32)['quality_verified'])
        self.reject(409,self.store.inspect,'a'*32,'e'*64)

    def _mounted(self,rec):
        core=copy.deepcopy(self.base);m=rec['manifest'];commit_adapter(core,prepare_adapter(core,rec['weights'],m['target_modules'],m['lora_rank'],m['lora_alpha']));return core

    def test_real_tensor_switch_two_ranks_and_restore_prior_version(self):
        first=self.profile();self.make_run('e'*32,.4,3);second=self.profile('e'*32,'5'*32);engine=self.engine()
        base=self.core.talker.self_attn(self.x).detach().clone()
        with self.native_api():
            engine.load_profile(first);a=self.core.talker.self_attn(self.x).detach().clone()
            engine.load_profile(second);b=self.core.talker.self_attn(self.x).detach().clone()
            engine.load_profile(first);again=self.core.talker.self_attn(self.x).detach().clone()
        self.assertFalse(torch.equal(base,a));self.assertFalse(torch.equal(a,b));torch.testing.assert_close(a,again,rtol=0,atol=0)
        self.assertEqual(engine.prompt[0].ref_spk_embedding.tolist(),[float(np.float32(.1))]*4)
        self.assertIsNone(engine.prompt[0].ref_code);self.assertTrue(engine.prompt[0].x_vector_only_mode);self.assertFalse(engine.prompt[0].icl_mode)

    def test_corrupt_second_tensor_does_not_partially_replace_modules(self):
        rec=self.store.inspect('a'*32);m=rec['manifest'];before=self.core.talker.self_attn(self.x).detach().clone()
        rec['weights'][m['target_modules'][-1]+'.lora_B']=np.zeros((1,1),np.float32)
        with self.assertRaises(ValueError):prepare_adapter(self.core,rec['weights'],m['target_modules'],2,4)
        torch.testing.assert_close(before,self.core.talker.self_attn(self.x),rtol=0,atol=0)
        self.assertFalse(any(name.endswith('lora_A') for name,_ in self.core.named_parameters()))

    def test_target_mismatch_rejected_without_base_fallback(self):
        rec=self.store.inspect('a'*32)
        with self.assertRaises(ValueError):prepare_adapter(self.core,rec['weights'],list(reversed(rec['manifest']['target_modules'])),2,4)

    def test_hash_damage_after_cached_load_rejected_previous_adapter_unchanged(self):
        profile=self.profile();engine=self.engine()
        with self.native_api():
            engine.load_profile(profile);before=adapter_digest(self.core)
            path=self.state/'training_runs'/('a'*32)/'adapter/adapter.safetensors';path.write_bytes(path.read_bytes()+b'damage')
            self.reject(409,engine.load_profile,profile)
        self.assertEqual(adapter_digest(self.core),before)

    def test_deleted_or_rebound_cached_profile_never_used(self):
        profile=self.profile();engine=self.engine();path=self.state/'profiles'/self.profile_id/'profile.json'
        with self.native_api():
            engine.load_profile(profile);path.unlink()
            with self.assertRaises(FileNotFoundError):engine.load_profile(profile)
            newer=copy.deepcopy(profile);newer['trained_adapter']['manifest_sha256']='f'*64;path.write_text(json.dumps(newer))
            self.reject(409,engine.load_profile,profile)

    def test_mock_and_faster_both_reject_trained_presence_even_empty(self):
        for value in ({},None,{'run_id':'a'*32}):
            self.reject(409,guard_profile,{'trained_adapter':value})
        guard_profile({'id':'ordinary'})
        for value in ({},None):self.reject(409,binding_of,{'trained_adapter':value})

    def test_wrong_base_and_speaker_dimension_rejected_before_switch(self):
        profile=self.profile();engine=self.engine();engine.base_hash='f'*64
        with self.native_api():self.reject(409,engine.load_profile,profile)
        engine.base_hash='b'*64;self.core.config.talker_config.hidden_size=5
        with self.native_api():self.reject(409,engine.load_profile,profile)
        self.assertIsNone(engine.key)

    def test_uncompleted_or_missing_rank_updates_refused(self):
        run=self.state/'training_runs'/('a'*32);original=(run/'result.json').read_text()
        for status in ('failed','timeout','cancelled'):
            result=json.loads(original);result['status']=status;(run/'result.json').write_text(json.dumps(result));self.reject(409,self.store.inspect,'a'*32)
        (run/'result.json').write_text(original)
        path=run/'adapter/manifest.json';m=json.loads(path.read_text());m['rank_reports'][1]['parameters_changed']=False;path.write_text(json.dumps(m))
        self.reject(409,self.store.inspect,'a'*32)

    def test_unsafe_links_and_extra_members_rejected(self):
        path=self.state/'training_runs'/('a'*32)/'adapter/speaker.safetensors';data=path.read_bytes();path.unlink()
        outside=self.state/'outside';outside.write_bytes(data);path.symlink_to(outside)
        with self.assertRaises((UploadRejected,OSError)):self.store.inspect('a'*32)
        path.unlink();path.hardlink_to(outside);self.reject(409,self.store.inspect,'a'*32)
        path.unlink();path.write_bytes(data);(path.parent/'unexpected').write_bytes(b'x');self.reject(409,self.store.inspect,'a'*32)

    def test_publishing_requires_ack_no_activation_and_uniform_transcript(self):
        profile=self.profile();pin=profile['trained_adapter']['manifest_sha256'];self.reject(400,self.store.publish,'a'*32,pin,'名字')
        @contextmanager
        def lease(*args):yield self.state,{'schema':2,'state':'audio_codes_prepared','checks':{'tokenization_executed':True},'samples':[{'id':sid} for sid in self.ids]},[{'audio':'reference.wav','ref_audio':'reference.wav','text':'训练统一参考对应文本'}]
        from training_codes import TrainingCodesStore
        from test_training_data import wav
        (self.state/'reference.wav').write_bytes(wav())
        with patch.object(TrainingCodesStore,'lease',lease):
            out=self.store.publish('a'*32,pin,'自己的训练版本',True)
        saved=json.loads((self.state/'profiles'/out['profile_id']/'profile.json').read_text())
        self.assertEqual(saved['ref_text'],'训练统一参考对应文本');self.assertEqual(saved['name'],'自己的训练版本');self.assertFalse(out['active_changed'])
        self.assertFalse((self.state/'active.json').exists());self.assertEqual(saved['trained_adapter'],profile['trained_adapter'])
        self.assertFalse(saved['quality_verified']);self.assertFalse(saved['inference_reload_verified'])

    def test_fixture_codes_still_cannot_publish(self):
        @contextmanager
        def lease(*args):yield self.state,{'schema':2,'state':'test_only_codes','checks':{'tokenization_executed':False}},[]
        from training_codes import TrainingCodesStore
        pin=self.store.inspect('a'*32)['manifest_sha256']
        with patch.object(TrainingCodesStore,'lease',lease):self.reject(409,self.store.publish,'a'*32,pin,'不能发布fixture',True)

    def test_buffered_single_yield_saved_prompt_and_cooperative_cancel(self):
        profile=self.profile();engine=self.engine();cancel=threading.Event();calls=[]
        def generate(**kw):
            calls.append(kw);self.assertFalse(kw['stopping_criteria'][0](torch.zeros(1,1,dtype=torch.long),None).item())
            return [np.ones(2400,np.float32)*.1],24000
        engine.model.generate_voice_clone=generate
        with self.native_api():
            values=list(engine.stream(profile,'真实文本接口替身','Chinese',2,80,7,cancel))
        self.assertEqual(len(values),1);self.assertEqual(len(values[0]),2400);self.assertTrue(calls[0]['non_streaming_mode'])
        self.assertIs(calls[0]['voice_clone_prompt'],engine.prompt);self.assertNotIn('ref_audio',calls[0]);self.assertEqual(engine.output_mode,'sentence-buffered')
        cancel.set()
        with self.native_api():self.assertEqual(list(engine.stream(profile,'x','Auto',2,80,7,cancel)),[])
        self.assertEqual(len(calls),1)

    def test_mid_generation_cancel_discards_late_pcm(self):
        profile=self.profile();engine=self.engine();cancel=threading.Event()
        def generate(**kw):
            cancel.set();self.assertTrue(kw['stopping_criteria'][0](torch.zeros(1,1,dtype=torch.long),None).item())
            return [np.ones(2400,np.float32)],24000
        engine.model.generate_voice_clone=generate
        with self.native_api():self.assertEqual(list(engine.stream(profile,'x','Auto',2,80,7,cancel)),[])

    def test_invalid_native_pcm_contract_never_yields(self):
        profile=self.profile();engine=self.engine()
        for wave,sr in [(np.ones(4),16000),(np.ones((4,2)),24000),(np.array([np.nan]),24000),(np.zeros(0),24000)]:
            engine.model.generate_voice_clone=lambda **kw:([wave],sr)
            with self.native_api(),self.assertRaises(RuntimeError):list(engine.stream(profile,'x','Auto',2,80,7,threading.Event()))

    def test_cli_errors_redact_private_paths_and_are_not_success(self):
        done=subprocess.run([sys.executable,str(ROOT/'tools/trained_voice.py'),'describe','--state',str(self.state),'--run-id','../private'],capture_output=True,text=True,timeout=10)
        self.assertEqual(done.returncode,2);out=json.loads(done.stdout);self.assertEqual(out['status'],'rejected');self.assertNotIn(str(self.state),done.stdout)

    def test_existing_worker_wire_has_pcm_then_buffered_stats_and_mock_rejects(self):
        import worker
        import struct
        import time
        profile=self.profile();engine=self.engine()
        engine.model.generate_voice_clone=lambda **kw:([np.sin(np.arange(24000)*.1).astype(np.float32)*.1],24000)
        instance=worker.Worker();instance.engine=engine;instance.ready=True;frames=[]
        with self.native_api(),patch.object(worker,'load_profile',return_value=profile):
            instance.run_job({'profile':profile['id'],'text':'接入现有PCM和聊天链路','lead_pause_ms':100},frames.append,threading.Event(),time.time()*1000)
        self.addCleanup(instance.levelers[profile['id']].close)
        parsed=[(raw[0],raw[5:]) for raw in frames if raw is not None]
        self.assertTrue(any(t==worker.F_PCM for t,_ in parsed));self.assertFalse(any(t==worker.F_ERR for t,_ in parsed))
        stats=json.loads(parsed[-1][1]);self.assertEqual(stats['model_output_mode'],'sentence-buffered');self.assertEqual(stats['engine'],'qwen-adapter-buffered')
        self.assertEqual(stats['chunks'],1);self.assertIsNone(frames[-1])
        mock=worker.Worker();mock.ready=True;frames=[]
        with patch.object(worker,'load_profile',return_value=profile),patch.object(mock.engine,'stream',side_effect=AssertionError('never synthesize fallback')):
            mock.run_job({'profile':profile['id'],'text':'不得回退原声'},frames.append,threading.Event(),time.time()*1000)
        types_seen=[raw[0] for raw in frames if raw is not None]
        self.assertNotIn(worker.F_PCM,types_seen);self.assertIn(worker.F_ERR,types_seen)

    def test_fixed_profile_http_edits_rejected_and_consistency_failure_not_pass(self):
        import analyst
        from fastapi.testclient import TestClient
        profile=self.profile()
        with patch.object(analyst,'load_profile',return_value=profile):
            client=TestClient(analyst.app)
            for route,body in [('text',{'ref_text':'不能改'}),('candidate',{'index':0}),('calibrate',{})]:
                response=client.post('/profiles/'+profile['id']+'/'+route,json=body);self.assertEqual(response.status_code,409)
        with patch.object(analyst,'load_ref_stats',return_value={'prof':profile}),patch.object(analyst,'synth_full',side_effect=RuntimeError('trained backend refuses')):
            result=analyst.consistency(profile['id'],['测试文本'])
        self.assertFalse(result['consistent']);self.assertFalse(result['quality_verified'])

    def test_engine_selection_unknown_and_mock_native_cannot_start(self):
        import worker
        for kind in ('unknown','qwen-adapter-buffered'):
            with patch.dict(os.environ,{'QTTS_TTS_ENGINE':kind}),self.assertRaises(RuntimeError):worker.Worker()

    def test_native_probe_checks_official_api_not_faster_and_stays_surface_only(self):
        import test_probe
        class Native:
            @classmethod
            def from_pretrained(cls,name,**kwargs):raise AssertionError('no load')
            def generate_voice_clone(self,text,**kwargs):raise AssertionError('no generation')
        def imports(name):
            if name=='torch':return test_probe.fake_import()(name)
            self.assertEqual(name,'qwen_tts');return types.SimpleNamespace(Qwen3TTSModel=Native)
        with patch('qwen_compat.configuration_smoke',return_value={'status':'installed','configuration_smoke_passed':True}),patch.dict(os.environ,{'QTTS_TTS_ENGINE':'qwen-adapter-buffered'}),patch.object(test_probe.probe.metadata,'version',return_value='fixture'),patch.object(test_probe.probe.importlib,'import_module',side_effect=imports):
            report=test_probe.probe.collect(True)
        self.assertEqual(report['status'],'surface_preflight_passed');self.assertEqual(report['model_output_mode'],'sentence-buffered');self.assertFalse(report['inference_verified'])
        packages={c['name']:c['required'] for c in report['checks']};self.assertTrue(packages['package.qwen-provider']);self.assertFalse(packages['package.faster-qwen3-tts'])

    def test_native_http_pcm_frames_and_health_without_real_qwen(self):
        import worker
        import struct
        from fastapi.testclient import TestClient
        profile=self.profile();engine=self.engine();engine.model.generate_voice_clone=lambda **kw:([np.sin(np.arange(24000)*.1).astype(np.float32)*.1],24000)
        instance=worker.Worker();instance.engine=engine;instance.ready=True
        with self.native_api(),patch.object(worker,'W',instance),patch.object(worker,'load_profile',return_value=profile):
            client=TestClient(worker.app)
            health=client.get('/health').json();self.assertEqual(health['model_output_mode'],'sentence-buffered');self.assertFalse(health['quality_verified'])
            response=client.post('/synth',json={'profile':profile['id'],'text':'实际HTTP帧测试，仍是CPU接口替身'})
        self.addCleanup(instance.levelers[profile['id']].close)
        self.assertEqual(response.status_code,200);raw=response.content;frames=[]
        while raw:
            kind,size=struct.unpack('<BI',raw[:5]);frames.append((kind,raw[5:5+size]));raw=raw[5+size:]
        self.assertTrue(any(kind==worker.F_PCM for kind,_ in frames));self.assertEqual(frames[-1][0],worker.F_STATS)
        self.assertEqual(json.loads(frames[-1][1])['model_output_mode'],'sentence-buffered')

    def test_two_worker_models_are_isolated_not_shared_adapter_state(self):
        profile=self.profile();first=self.engine();second=self.engine();second.model=types.SimpleNamespace(model=copy.deepcopy(self.base))
        with self.native_api():first.load_profile(profile)
        self.assertTrue(any(name.endswith('lora_A') for name,_ in first.model.model.named_parameters()))
        self.assertFalse(any(name.endswith('lora_A') for name,_ in second.model.model.named_parameters()))
        self.assertIsNone(second.key)

    def test_bounded_manifest_and_nonfinite_saved_speaker_rejected(self):
        from safetensors.numpy import save
        run=self.state/'training_runs'/('a'*32)/'adapter';path=run/'manifest.json';original=path.read_bytes()
        path.write_bytes(b' '*(1<<20)+b'{}');self.reject(409,self.store.inspect,'a'*32);path.write_bytes(original)
        data=save({'speaker_embedding':np.full((1,4),np.nan,np.float32)});(run/'speaker.safetensors').write_bytes(data)
        m=json.loads(original);m['files']['speaker.safetensors']=hashlib.sha256(data).hexdigest();path.write_text(json.dumps(m))
        self.reject(409,self.store.inspect,'a'*32)

    def test_production_load_never_accepts_unpinned_or_wrong_local_base(self):
        engine=self.engine()
        with patch('training_job.base_fingerprint',return_value='e'*64):self.reject(409,engine.load)
        engine.base_hash=''
        with patch('training_job.base_fingerprint',side_effect=AssertionError('pin checked first')):self.reject(409,engine.load)


if __name__=='__main__':unittest.main()
