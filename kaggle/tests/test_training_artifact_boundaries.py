"""Real NumPy/safetensors/local file checks; rank reports are HAND-BUILT FIXTURES.
No optimizer, NCCL, Base model or voice generation occurs in this test module.
"""
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from safetensors.numpy import save

ROOT=Path(__file__).resolve().parents[1]/'source'
sys.path.insert(0,str(ROOT/'py'))
from resource_limits import UploadRejected
from trained_profiles import TrainedArtifacts,binding_of,guard_profile
from training_codes import TrainingCodesStore

class ArtifactBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='qtts-artifact-fixture-')
        self.addCleanup(self.temp.cleanup)
        self.state=Path(self.temp.name)
        self.store=TrainedArtifacts(self.state)
        self.rid='a'*32
        self.ids=['1'*32,'2'*32]
        self.target='talker.self_attn.q_proj'
        self.run=self.state/'training_runs'/self.rid
        self.checkpoint=self.run/'adapter'
        self.checkpoint.mkdir(parents=True)
        self.build()

    def build(self,dtype=np.float32,nonfinite=False,incomplete=False):
        a=np.ones((2,4),dtype=dtype)
        if nonfinite:a[0,0]=np.nan
        weights={self.target+'.lora_A':a,self.target+'.lora_B':np.zeros((4,2),dtype=dtype)}
        digest=hashlib.sha256()
        for name,value in sorted(weights.items()):
            digest.update(name.encode());digest.update(value.tobytes(order='C'))
        reports=[{'rank':rank,'world_size':2,'backend':'nccl','parameters_changed':True,
                  'adapter_sha256':digest.hexdigest(),'epochs':[{'epoch':0,'loss_mean':1.,'optimizer_steps':1,
                  'seen_ids':self.ids[:1] if incomplete else [self.ids[rank]]}]} for rank in (0,1)]
        # This is intentionally synthetic metadata, NOT evidence NCCL ran.
        request={'model_sha256':'b'*64,'codes_id':'c'*32,'codes_sha256':'d'*64,
                 'sample_ids':self.ids,'lora_rank':2,'lora_alpha':4.,'epochs':1,
                 'confirm_data_reviewed':True,'ack_experimental_training':True}
        result={'status':'completed','job_id':self.rid,'rank_exit_codes':[0,0],
                'optimizer_execution_observed':True,'checkpoint_relative_directory':f'training_runs/{self.rid}/adapter'}
        payloads={'adapter.safetensors':save(weights),
                  'speaker.safetensors':save({'speaker_embedding':np.ones((1,4),np.float32)})}
        for name,data in payloads.items():(self.checkpoint/name).write_bytes(data)
        manifest={'schema':1,'kind':'qtts_lora_adapter','two_rank_execution_observed':True,
                  'optimizer_updates_observed':True,'base_model_sha256':'b'*64,'codes_id':'c'*32,
                  'codes_manifest_sha256':'d'*64,'sample_ids':self.ids,'lora_rank':2,'lora_alpha':4.,
                  'target_modules':[self.target],'rank_reports':reports,
                  'files':{name:hashlib.sha256(data).hexdigest() for name,data in payloads.items()}}
        for path,value in ((self.run/'request.json',request),(self.run/'result.json',result),(self.checkpoint/'manifest.json',manifest)):
            path.write_text(json.dumps(value))
        self.pin=hashlib.sha256((self.checkpoint/'manifest.json').read_bytes()).hexdigest()

    def rejects(self,code,function,*args,**kwargs):
        with self.assertRaises(UploadRejected) as caught:function(*args,**kwargs)
        self.assertEqual(caught.exception.code,code)

    def test_actual_safetensors_parse_of_synthetic_artifact_not_training(self):
        record=self.store.inspect(self.rid,self.pin)
        self.assertEqual(record['weights'][self.target+'.lora_A'].shape,(2,4))
        self.assertEqual(record['speaker'].shape,(1,4))
        description=self.store.describe(self.rid)
        self.assertFalse(description['quality_verified'])
        self.assertFalse(description['inference_reload_verified'])

    def test_wrong_manifest_pin_rejected(self):
        self.rejects(409,self.store.inspect,self.rid,'f'*64)

    def test_tensor_mutation_rejected(self):
        path=self.checkpoint/'adapter.safetensors'
        path.write_bytes(path.read_bytes()+b'changed')
        self.rejects(409,self.store.inspect,self.rid,self.pin)

    def test_nonfinite_tensor_rejected_even_with_updated_hashes(self):
        self.build(nonfinite=True)
        self.rejects(409,self.store.inspect,self.rid,self.pin)

    def test_float64_tensor_rejected(self):
        self.build(dtype=np.float64)
        self.rejects(409,self.store.inspect,self.rid,self.pin)

    def test_incomplete_epoch_membership_rejected(self):
        self.build(incomplete=True)
        self.rejects(409,self.store.inspect,self.rid,self.pin)

    def test_publish_requires_explicit_ack_before_inspect(self):
        with patch.object(self.store,'inspect',side_effect=AssertionError('must not inspect')):
            self.rejects(400,self.store.publish,self.rid,self.pin,'synthetic',False)

    def test_fixture_codes_cannot_publish_profile(self):
        @contextmanager
        def fixture_lease(*args,**kwargs):
            yield self.state,{'schema':2,'state':'test_only_codes','checks':{'tokenization_executed':False}},[]
        with patch.object(TrainingCodesStore,'lease',side_effect=fixture_lease):
            self.rejects(409,self.store.publish,self.rid,self.pin,'synthetic',True)
        self.assertEqual(list((self.state/'profiles').iterdir()),[])

    def test_trained_profile_has_no_untrained_backend_fallback(self):
        self.rejects(409,guard_profile,{'trained_adapter':{}},False)
        guard_profile({},False)

    def test_binding_rejects_bad_pin_and_id(self):
        binding={'run_id':self.rid,'codes_id':'c'*32,'manifest_sha256':self.pin,
                 'base_model_sha256':'b'*64,'codes_manifest_sha256':'d'*64}
        self.assertEqual(binding_of({'trained_adapter':binding}),binding)
        for key,value in (('run_id',True),('manifest_sha256',None),('codes_id','../escape')):
            self.rejects(409,binding_of,{'trained_adapter':{**binding,key:value}})

if __name__=='__main__':unittest.main()
