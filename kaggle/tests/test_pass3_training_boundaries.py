"""Third reread: original files/OFD/controller and CLI. No torch/training.
Synthetic completed adapters and production-shaped code lease metadata are fixtures.
F35 is an original controller receipt gap under controlled CPU rank substitution;
original artifact inspection rejects it. No claim that real rank_worker emits it.
"""
from contextlib import contextmanager
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

import test_reliability  # Isolated mock runtime, not a tensor implementation.
import test_training_codes as code_helpers
import test_training_artifact_boundaries as artifact_helpers
import test_tts_training as controller
import training_data as td
import training_codes as tc
import training_job as job
from trained_profiles import TrainedArtifacts, binding_of, guard_profile
from resource_limits import UploadRejected
import numpy as np

ROOT=Path(__file__).resolve().parents[1]/'source'
OBSERVATIONS=[]


class TrainingBoundaries(unittest.TestCase):
    def setUp(self):
        # Compose existing fixtures, do not inherit their tests or manufacture codes
        # with production tokenization_executed=true.
        code_helpers.CodeTests.setUp(self)

    def reject(self,code,fn,*args,**kwargs):
        with self.assertRaises(UploadRejected) as caught:fn(*args,**kwargs)
        self.assertEqual(caught.exception.code,code)

    # Fixture setup uses these methods; it is not unittest inheritance.
    from test_training_data import Fixture as _Fixture
    source=_Fixture.source

    def run_codes(self,**kwargs):
        return self.codes.prepare(self.data,self.did,self.sha,lambda:code_helpers.fixture_encoder,**kwargs)

    def artifact(self):
        fixture=artifact_helpers.ArtifactBoundaryTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        return fixture

    def arguments(self):
        out=self.run_codes();base=controller.base_tree(self.state/'base')
        return NS(state=str(self.state),id=out['id'],manifest_sha256=out['manifest_sha256'],model_dir=str(base),
                  model_sha256=job.base_fingerprint(base),epochs=1,accumulation=4,max_sequence=1024,lora_rank=8,
                  seed=42,timeout=10,lr=2e-5,lora_alpha=16.,confirm_data_reviewed=True,ack_experimental_training=True)

    def synthetic_code_lease(self,artifact):
        # Deliberately not a real TrainingCodesStore snapshot or tokenizer result.
        # Used ONLY to reach original publish's file transaction and final recheck.
        from test_training_data import wav
        directory=artifact.state/'lease-fixture';directory.mkdir(mode=0o700)
        (directory/'audio').mkdir(mode=0o700)
        rows=[];payloads=[]
        for index,sid in enumerate(artifact.ids):
            raw=wav(hz=440+index*110);path=directory/'audio'/(sid+'.wav');path.write_bytes(raw);path.chmod(0o600)
            rows.append({'audio':'audio/'+sid+'.wav','ref_audio':'audio/'+artifact.ids[1]+'.wav','text':f'fixture transcript {index}'})
            payloads.append(raw)
        @contextmanager
        def lease(*args,**kwargs):
            self.assertEqual(args,('c'*32,'d'*64))
            yield directory,{'schema':2,'state':'audio_codes_prepared','checks':{'tokenization_executed':True},
                             'samples':[{'id':sid} for sid in artifact.ids]},rows
        return patch.object(tc.TrainingCodesStore,'lease',side_effect=lease),rows,payloads

    def test_protect_raw_prepare_keyboardinterrupt_rolls_back_and_library_remains_unchanged(self):
        before=self.lib.get(self.library['id']);original=self.data._write;calls=[]
        def write(path,raw):
            original(path,raw);calls.append(path.name)
            if path.name=='train_raw.jsonl':raise KeyboardInterrupt('owned fixture interruption')
        with patch.object(self.data,'_write',side_effect=write),self.assertRaises(KeyboardInterrupt):
            self.data.prepare(self.lib,self.body)
        self.assertGreaterEqual(len(calls),4)
        self.assertEqual(self.lib.get(self.library['id']),before)
        self.assertFalse(list(self.data.root.glob('.pending-*')))
        self.assertEqual([row['id'] for row in self.data.list()],[self.did])
        result=self.data.prepare(self.lib,self.body)
        self.assertTrue(self.data.verify(result['id'],result['manifest_sha256'])['integrity_verified_now'])

    def test_protect_canonical_pcm_extrema_odd_frame_count_and_metadata_removal(self):
        import io,struct,wave
        values=np.resize(np.array([-32768,32767,0,123],dtype='<i2'),36001)
        out=io.BytesIO()
        with wave.open(out,'wb') as stream:
            stream.setnchannels(1);stream.setsampwidth(2);stream.setframerate(24000);stream.writeframes(values.tobytes())
        original=out.getvalue();junk=b'JUNK'+struct.pack('<I',3)+b'xyz'+b'\x00'
        raw=original[:12]+junk+original[12:];raw=raw[:4]+struct.pack('<I',len(raw)-8)+raw[8:]
        canonical,stats=td.canonical_wav(raw,240,36001)
        self.assertEqual(canonical,original);self.assertEqual(stats['frames'],36001)
        self.assertEqual(stats['peak'],1.);self.assertTrue(math.isfinite(stats['rms']))
        self.reject(413,td.canonical_wav,raw,240,36000)
        self.assertEqual(np.frombuffer(canonical,offset=44,dtype='<i2').tolist(),values.tolist())

    def test_protect_final_cancel_after_full_codes_verification_never_renames(self):
        cancelled=[];verified=[];original=self.codes._verify
        def verify(*args,**kwargs):
            result=original(*args,**kwargs);verified.append(result);cancelled.append(True);return result
        with patch.object(self.codes,'_verify',side_effect=verify):
            self.reject(409,self.run_codes,cancelled=lambda:bool(cancelled))
        self.assertEqual(len(verified),1);self.assertTrue(verified[0]['integrity_verified_now'])
        self.assertEqual(verified[0]['state'],'test_only_codes')
        self.assertFalse(list(self.codes.root.glob('.pending-*')));self.assertEqual(self.codes.list(),[])
        self.assertTrue(self.data.verify(self.did,self.sha)['integrity_verified_now'])
        self.assertEqual(self.run_codes()['state'],'test_only_codes')

    def test_protect_encoder_baseexception_after_first_sample_cleans_and_releases_source(self):
        calls=[]
        def encoder(waveform):
            calls.append(len(waveform))
            if len(calls)==2:raise KeyboardInterrupt('owned encoder interruption')
            return code_helpers.fixture_encoder(waveform)
        with self.assertRaises(KeyboardInterrupt):self.codes.prepare(self.data,self.did,self.sha,lambda:encoder)
        self.assertEqual(calls,[36000,36000]);self.assertEqual(self.codes.list(),[])
        self.assertFalse(list(self.codes.root.glob('.pending-*')))
        with self.data.lease(self.did,self.sha):pass
        self.assertEqual(self.run_codes()['sample_count'],3)

    def test_protect_qwen_finish_only_checks_materialized_pin_without_loading_tokenizer(self):
        model=self.state/'tokenizer';model.mkdir();(model/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        weights=model/'model.safetensors';weights.write_bytes(b'fixture bytes, not weights')
        encoder=object.__new__(tc.QwenCPUEncoder)
        encoder.directory=model;encoder.expected_hash=tc.model_fingerprint(model)
        encoder.finish()  # NO __init__, import torch, tokenizer or encoding.
        weights.write_bytes(b'changed fixture bytes, still not weights')
        self.reject(409,encoder.finish)
        self.assertFalse(hasattr(encoder,'tokenizer'))

    def test_protect_adopted_codes_ofd_keeps_delete_blocked_after_parent_context_closes(self):
        out=self.run_codes();cid,pin=out['id'],out['manifest_sha256']
        parent=self.codes.lease_with_fd(cid,pin);_,_,_,fd=parent.__enter__()
        child=self.codes.adopt_lease(cid,pin,fd);child.__enter__()
        try:
            parent.__exit__(None,None,None)
            self.reject(409,self.codes.delete,cid,pin)
        finally:child.__exit__(None,None,None);parent.__exit__(None,None,None)
        self.assertTrue(self.codes.verify(cid,pin)['provenance_verified_now'])
        self.codes.delete(cid,pin)

    def test_protect_cancelled_result_with_completed_adapter_is_not_inspectable(self):
        artifact=self.artifact();self.assertEqual(artifact.store.inspect(artifact.rid,artifact.pin)['run_id'],artifact.rid)
        path=artifact.run/'result.json';result=json.loads(path.read_text());result['status']='cancelled';path.write_text(json.dumps(result))
        self.reject(409,artifact.store.inspect,artifact.rid,artifact.pin)
        self.reject(409,artifact.store.publish,artifact.rid,artifact.pin,'fixture',True)
        self.assertFalse((artifact.state/'profiles').exists())

    def test_protect_epoch_loss_and_request_membership_reject_before_profile_publish(self):
        artifact=self.artifact();path=artifact.run/'request.json';before=path.read_bytes()
        request=json.loads(before);request['sample_ids']=list(reversed(request['sample_ids']));path.write_text(json.dumps(request))
        self.reject(409,artifact.store.inspect,artifact.rid,artifact.pin);path.write_bytes(before)
        mpath=artifact.checkpoint/'manifest.json';manifest=json.loads(mpath.read_text())
        manifest['rank_reports'][1]['epochs'][0]['loss_mean']=float('nan');mpath.write_text(json.dumps(manifest))
        self.reject(409,artifact.store.inspect,artifact.rid)
        self.assertFalse((artifact.state/'profiles').exists())

    def test_protect_second_artifact_inspection_cleans_pending_profile_on_tensor_change(self):
        artifact=self.artifact();context,_,_=self.synthetic_code_lease(artifact)
        active=artifact.state/'active.json';active.write_text('{"id":"old-fixture"}');before=active.read_bytes()
        original=tc.TrainingCodesStore._write
        def write(owner,path,raw):
            original(owner,path,raw)
            if path.name=='profile.json':
                tensor=artifact.checkpoint/'speaker.safetensors';tensor.write_bytes(tensor.read_bytes()+b'changed')
        with context,patch.object(tc.TrainingCodesStore,'_write',new=write):
            self.reject(409,artifact.store.publish,artifact.rid,artifact.pin,'fixture',True)
        self.assertEqual({p.name for p in (artifact.state/'profiles').iterdir()},{'.lock'})
        self.assertFalse(list(artifact.state.glob('.trained-profile-*')));self.assertEqual(active.read_bytes(),before)

    def test_protect_publish_selects_matching_reference_text_without_activation_or_quality_claim(self):
        artifact=self.artifact();context,rows,payloads=self.synthetic_code_lease(artifact)
        active=artifact.state/'active.json';active.write_text('{"id":"old-fixture"}');before=active.read_bytes()
        with context:result=artifact.store.publish(artifact.rid,artifact.pin,'fixture',True)
        directory=artifact.state/'profiles'/result['profile_id'];profile=json.loads((directory/'profile.json').read_text())
        self.assertEqual((directory/'anchor.wav').read_bytes(),payloads[1]);self.assertEqual(profile['ref_text'],rows[1]['text'])
        self.assertEqual(binding_of(profile)['manifest_sha256'],artifact.pin)
        for key in ('quality_verified','inference_reload_verified','active_changed'):self.assertFalse(result[key])
        self.assertEqual(active.read_bytes(),before);self.reject(409,guard_profile,profile,False)
        self.assertEqual(profile['model_output_mode'],'sentence-buffered')

    def test_protect_trained_voice_cli_rejects_bad_pin_without_loading_or_raw_trace(self):
        artifact=self.artifact()
        cp=subprocess.run([sys.executable,str(ROOT/'tools/trained_voice.py'),'publish','--state',str(artifact.state),
            '--run-id',artifact.rid,'--adapter-sha256','f'*64,'--name','fixture','--ack-unverified-adapter'],capture_output=True,text=True,timeout=10)
        self.assertEqual(cp.returncode,2);response=json.loads(cp.stdout)
        self.assertEqual(response['status'],'rejected');self.assertEqual(response['code'],409)
        self.assertNotIn('Traceback',cp.stdout+cp.stderr);self.assertNotIn(str(artifact.state),cp.stdout)
        self.assertFalse((artifact.state/'profiles').exists())

    def test_observed_controller_zero_cpu_ranks_and_empty_manifest_claim_optimizer_execution(self):
        args=self.arguments();needle="if mode=='exit0':time.sleep(.1)"
        replacement="if mode=='exit0':\n   if rank=='0':\n    adapter=Path(request['run_dir'],'adapter');adapter.mkdir(mode=0o700);(adapter/'manifest.json').write_text('{}')\n   time.sleep(.1)"
        self.assertIn(needle,controller.CPU_HOLDER)
        before={sig:signal.getsignal(sig) for sig in (signal.SIGINT,signal.SIGTERM)}
        with patch.object(controller,'CPU_HOLDER',controller.CPU_HOLDER.replace(needle,replacement)):
            result=controller.controlled_fixture(args,'exit0')
        self.assertEqual(result['status'],'completed');self.assertTrue(result['optimizer_execution_observed'])
        self.assertEqual(result['rank_exit_codes'],[0,0]);run=self.state/'training_runs'/result['job_id']
        self.assertEqual(json.loads((run/'result.json').read_text()),result)
        self.assertEqual({p.name for p in (run/'adapter').iterdir()},{'manifest.json'})
        self.assertEqual((run/'adapter/manifest.json').read_text(),'{}')
        self.reject(409,TrainedArtifacts(self.state).inspect,result['job_id'])
        self.assertEqual({sig:signal.getsignal(sig) for sig in before},before)
        self.codes.delete(args.id,args.manifest_sha256)
        with job.GpuLease.acquire('offline-reservation',root=self.state/'test-gpu'):pass
        self.assertFalse(result['quality_verified']);self.assertFalse(result['inference_reload_verified'])
        OBSERVATIONS.append({'id':'F35','fixed':False,'original_controller_executed':True,
            'two_real_owned_cpu_rank_processes':True,'real_codes_and_gpu_ofd_adoption':True,
            'admission_dependency_and_tokenizer_gates_are_fixture_substitutions':True,
            'rank_training_implementation_is_cpu_fixture':True,'rank_exit_codes':[0,0],
            'checkpoint_contains_only_empty_json_manifest':True,'controller_status':'completed',
            'controller_optimizer_execution_observed':True,'original_artifact_inspect_rejects':True,
            'signals_and_leases_restored':True,'actual_optimizer_or_model_executed':False,
            'production_rank_emits_malformed_checkpoint_proven':False,'invalid_voice_published':False})


if __name__=='__main__':unittest.main()
