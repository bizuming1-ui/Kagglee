"""Bounded long recording/unchanged training maths; no acoustic quality claims."""
import copy
import io
import json
import threading
import os
import sys
import time
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from unittest.mock import patch
import wave
import numpy as np
import test_reliability
import worker
import analyst
from resource_limits import UploadLimits,UploadRejected
import test_tts_training as train

class RecordingTests(unittest.TestCase):
    def test_long_recording_default_limits_are_bounded(self):
        with patch.dict(os.environ,{},clear=True):limits=UploadLimits.from_env()
        self.assertEqual(limits.seconds,1200);self.assertEqual(limits.total_seconds,1800)
        self.assertEqual(limits.request_bytes,128<<20);self.assertEqual(limits.file_bytes,64<<20)

    def test_eleven_minute_complete_pcm_decodes_without_truncation(self):
        # Deliberately synthetic, NOT microphone/voice quality evidence.
        data=np.tile(np.array([100,-100],dtype='<i2'),24000*660//2)
        stream=io.BytesIO()
        with wave.open(stream,'wb') as wav:
            wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(24000);wav.writeframes(data.tobytes())
        with patch.object(analyst,'LIMITS',UploadLimits()),patch.object(analyst.subprocess,'run',side_effect=FileNotFoundError()):
            decoded=analyst.decode_audio(stream.getvalue())
        self.assertEqual(len(decoded),24000*660)
        self.assertAlmostEqual(float(decoded[0]),100/32768)

    def test_long_capture_does_not_silently_expand_training_sequence_gate(self):
        from training_data import canonical_wav
        # Existing training clip budget is intentional; recording != training segmentation.
        from inspect import getsource
        self.assertIn('min(240,self.limits.seconds)',getsource(__import__('training_data').TrainingDataStore.prepare))

    def test_default_lead_never_injects_breath_even_if_requested(self):
        w=worker.Worker();w.breath_banks['v']=[np.ones(4000,np.float32)*.1]
        with patch.dict(os.environ,{'QTTS_BREATH_MODE':'off'}),patch.object(worker.audio_rt,'breath',side_effect=AssertionError('synthetic breath forbidden')):
            a=w.lead_audio({'id':'v'},500,True,42)
        self.assertEqual(np.count_nonzero(a),0)

    def test_legacy_reference_breath_setting_cannot_enable_playback(self):
        w=worker.Worker()
        with patch.dict(os.environ,{'QTTS_BREATH_MODE':'reference'}),patch.object(worker.audio_rt,'breath',side_effect=AssertionError('no noise fallback')):
            self.assertEqual(np.count_nonzero(w.lead_audio({'id':'v'},500,True,42)),0)
            w.breath_banks['v']=[np.ones(65,np.float32)*.01]
            self.assertEqual(np.count_nonzero(w.lead_audio({'id':'v'},500,True,42)),0)

    def test_first_speech_time_excludes_trimmed_initial_empty_chunk(self):
        w=worker.Worker();w.ready=True;w.profiles['v']={'id':'v'}
        w.levelers['v']=worker.audio_rt.Leveler(24000)
        w.engine.stream=lambda *args:iter([np.zeros(1000,np.float32),(.1*np.sin(np.arange(9600)*.09)).astype(np.float32)])
        emitted=[];clock=iter(range(0,10000,10))
        with patch.object(worker,'now_ms',side_effect=lambda:next(clock)):
            w.run_job({'profile':'v','text':'测试声音','language':'Chinese'},emitted.append,threading.Event(),0)
        stats=json.loads(next(f[5:] for f in emitted if f and f[0]==worker.F_STATS))
        self.assertFalse(stats.get('failed',False))
        self.assertGreater(stats['first_chunk_ms'],stats['model_first_chunk_ms'])
        self.assertFalse(stats['acoustic_text_verified'])

@unittest.skipUnless(train.TORCH,'Torch required, not fake training success')
class CacheTests(unittest.TestCase):
    def test_cached_inputs_and_batches_are_exactly_equal_and_private(self):
        import torch
        d=train.tiny_data();uncached=train.tiny_data();uncached.cache_budget=0
        for _ in range(3):
            for i in range(3):
                a=d.collate_fn([d[i]]);b=uncached.collate_fn([uncached[i]])
                self.assertEqual(set(a),set(b))
                for key in a:self.assertTrue(torch.equal(a[key],b[key]),key)
        self.assertEqual(d.tokenizer_calls,3);self.assertEqual(uncached.tokenizer_calls,9)
        d[0]['text_ids'].fill_(0);self.assertTrue(torch.equal(d[0]['text_ids'],uncached[0]['text_ids']))

    def test_cache_byte_budget_fallback_does_not_evict_or_truncate(self):
        d=train.tiny_data();d.cache_budget=1
        for _ in range(2):d[0]
        self.assertEqual(d.cache_used,0);self.assertEqual(d.tokenizer_calls,2)
        self.assertEqual(d.cache_hits,0)

    def test_source_mutation_cannot_poison_frozen_dataset(self):
        seed=train.tiny_data();source=seed.rows
        d=train.TTSDataset(source,seed.processor,seed.config,seed.reference_mel)
        source[0]['text']='externally changed';source[0]['audio_codes'][0][0]=1999
        self.assertNotEqual(d.rows[0]['text'],source[0]['text'])
        self.assertLess(int(d[0]['audio_codes'].max()),8)
        first=d[0]['text_ids'].clone()
        self.assertEqual(d[0]['text_ids'].tolist(),first.tolist())
        # Cache copies returned tensors, never returns its writable backing store.
        value=d[0];value['audio_codes'].fill_(2000)
        self.assertLess(int(d[0]['audio_codes'].max()),8)

    def test_cache_and_uncached_optimizer_updates_bitwise_equal(self):
        import torch
        from lora_adapter import inject_lora,adapter_state
        from tts_training import JointLoss,optimize_epoch
        torch.set_num_threads(1);torch.manual_seed(14)
        base=train.TinyCore();a=copy.deepcopy(base);b=copy.deepcopy(base)
        for core in (a,b):inject_lora(core,2,4)
        # Same initial adapters as well as same base.
        b.load_state_dict(a.state_dict());d=train.tiny_data();e=train.tiny_data();e.cache_budget=0
        stats=[]
        for core,dataset in ((a,d),(b,e)):
            task=JointLoss(core,torch.zeros(1,4));opt=torch.optim.AdamW([p for p in task.parameters() if p.requires_grad],lr=.01)
            reports=[]
            for epoch in range(3):reports.append(optimize_epoch(task,dataset,[0,1,2],opt,torch.amp.GradScaler('cpu',enabled=False),torch.device('cpu'),2,False))
            stats.append(reports)
        self.assertEqual(stats[0],stats[1])
        for key in adapter_state(a):self.assertTrue(torch.equal(adapter_state(a)[key],adapter_state(b)[key]),key)
        self.assertEqual(d.tokenizer_calls,3);self.assertEqual(e.tokenizer_calls,9)

    def test_bad_cache_budget_is_not_unbounded_allocation(self):
        d=train.tiny_data()
        for budget in (-1,True,257<<20):
            with self.subTest(budget=budget),self.assertRaises(ValueError):train.TTSDataset(d.rows,d.processor,d.config,d.reference_mel,cache_bytes=budget)

    def test_aggregated_finite_gradients_and_provider_metadata(self):
        import torch
        from tts_training import gradients_finite,provider_version
        p=torch.nn.Parameter(torch.ones(2));self.assertTrue(gradients_finite([p]))
        p.grad=torch.ones(2);self.assertTrue(gradients_finite([p]))
        p.grad[0]=float('inf');self.assertFalse(gradients_finite([p]))
        with patch('qwen_compat.installed_version',side_effect=lambda name:'0.1.1.post1' if name=='qwen-tts-hf' else None):self.assertEqual(provider_version(),'0.1.1.post1')

if __name__=='__main__':unittest.main()
