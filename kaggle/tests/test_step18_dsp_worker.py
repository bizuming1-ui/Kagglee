"""S3 candidate worker integration. Real run_job/trimmer/DSP/frame, synthetic engine/pin.
No HTTP, model weights, training, GPU, real reference audio or acoustic signoff.
"""
import ast
import importlib.util
import json
import os
from pathlib import Path
import struct
import sys
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import numpy as np
import test_reliability  # import frozen worker/audio_rt first: deliberate module-cache collision
from test_step18_dsp_causality import signal

R=Path(__file__).resolve().parents[2]
os.environ.setdefault('QTTS_MOCK','1')
spec=importlib.util.spec_from_file_location('s3_candidate_worker',R/'kaggle/step18/worker.py')
worker=importlib.util.module_from_spec(spec);sys.modules[spec.name]=worker;spec.loader.exec_module(worker)
import step18_audio_rt as dsp


def frames(emitted):
    decoded=[]
    for packet in emitted:
        if packet is None:continue
        kind,size=struct.unpack('<BI',packet[:5]);assert size==len(packet)-5
        decoded.append((kind,packet[5:]))
    return decoded


class CandidateDSPWorkerContracts(unittest.TestCase):
    def run_fixture(self, sizes=(47,400,1920,307), cancel_after_first=False, fail=False, existing=None):
        w=existing or worker.Worker();w.ready=True;w.profiles['voice']={'id':'voice'};w.voice_bindings['voice']='fixturepin'
        samples=signal(13007);cancel=threading.Event();emitted=[];processed=[];tails=[]
        class Capturing(dsp.Leveler):
            def process(self,x):
                result=super().process(x);processed.append((np.array(x,copy=True),result.copy()));return result
            def flush(self,n=192):
                result=super().flush(n);tails.append(result.copy());return result
        def stream(*args):
            at=0;idx=0
            while at<len(samples):
                end=min(len(samples),at+sizes[idx%len(sizes)]);yield samples[at:end];at=end;idx+=1
                if fail:raise RuntimeError('fixture engine failure')
                if cancel_after_first:cancel.set()
        w.engine=SimpleNamespace(name='synthetic-engine',dtype_name='cpu-fixture',supports_trained=False,stream=stream)
        with patch.object(worker,'load_profile',return_value=None),patch.object(worker,'reference_binding',return_value='fixturepin'),patch.object(worker.audio_rt,'Leveler',Capturing):
            w.run_job({'profile':'voice','text':'合成合同，不是声音验收','seed':77,'breath':True},emitted.append,cancel,worker.now_ms())
        packets=frames(emitted);stats=json.loads([payload for kind,payload in packets if kind==worker.F_STATS][-1])
        self.assertIsNone(emitted[-1]);self.assertFalse(w.lock.locked());self.assertFalse(w.busy)
        return w,packets,stats,processed,tails

    def test_01_unique_dsp_binding_survives_frozen_import(self):
        self.assertIs(worker.audio_rt,dsp);self.assertIsNot(worker.audio_rt,test_reliability.audio_rt)
        self.assertEqual(dsp.BACKEND,'numpy-causal-v1')
        self.assertEqual(Path(worker.audio_rt.__file__).resolve(),R/'kaggle/step18/step18_audio_rt.py')
    def test_02_actual_run_job_pcm_matches_direct_causal_processing(self):
        w,packets,stats,processed,tails=self.run_fixture()
        self.addCleanup(w.levelers['voice'].close)
        self.assertTrue(processed);self.assertEqual(len(tails),1)
        input=np.concatenate([x for x,_ in processed]);actual=np.concatenate([x for _,x in processed])
        direct=dsp.Leveler(worker.SAMPLE_RATE,worker.output_target_dbfs(),worker.output_max_gain_db());self.addCleanup(direct.close);direct.start_segment()
        np.testing.assert_array_equal(actual,direct.process(input));np.testing.assert_array_equal(tails[0],direct.flush(192))
        wire=np.concatenate([np.frombuffer(payload,dtype='<i2') for kind,payload in packets if kind==worker.F_PCM])
        np.testing.assert_array_equal(wire,np.concatenate([actual,tails[0]]))
        self.assertEqual(stats['speech_samples'],len(input));self.assertEqual(stats['chunks'],len(processed));self.assertFalse(stats['quality_verified'])
        self.assertEqual(stats['rt'],'numpy-causal-v1');self.assertFalse(stats['reference_pcm_splicing']);self.assertFalse(stats['acoustic_text_verified'])
        self.assertFalse(any(kind==worker.F_ERR for kind,_ in packets));self.assertEqual(w.served,1);self.assertEqual(w.failed,0)
    def test_03_reset_installs_causal_leveler(self):
        w=worker.Worker();lev=w._reset_leveler('voice');self.addCleanup(lev.close)
        self.assertIs(type(lev),dsp.Leveler);lev.start_segment()
        output=[lev.process(signal(17)) for _ in range(30)]
        self.assertEqual(sum(map(len,output)),510);self.assertEqual(lev._blk_n,30);self.assertGreater(lev._seen,0)
    def test_04_reset_closes_old_leveler(self):
        w=worker.Worker();old=w._reset_leveler('voice');new=w._reset_leveler('voice');self.addCleanup(new.close)
        self.assertIsNot(old,new)
        with self.assertRaises(RuntimeError):old.process([.1])
    def test_05_repeated_jobs_start_with_fresh_dsp(self):
        w,packets,stats,_,_=self.run_fixture();old=w.levelers['voice']
        w,second,_,_,_=self.run_fixture(existing=w);self.addCleanup(w.levelers['voice'].close)
        self.assertTrue(old._closed)
        self.assertEqual([p for k,p in packets if k==worker.F_PCM],[p for k,p in second if k==worker.F_PCM])
    def test_06_cancel_does_not_emit_tail(self):
        w,packets,stats,processed,tails=self.run_fixture((1920,),cancel_after_first=True);self.addCleanup(w.levelers['voice'].close)
        self.assertTrue(stats['cancelled']);self.assertEqual(tails,[]);self.assertEqual(stats['speech_samples'],sum(len(out) for _,out in processed))
        self.assertFalse(any(k==worker.F_ERR for k,_ in packets))
    def test_07_engine_failure_remains_visible_without_tail(self):
        w,packets,stats,processed,tails=self.run_fixture((1920,),fail=True);self.addCleanup(w.levelers['voice'].close)
        self.assertTrue(stats['failed']);self.assertEqual(w.failed,1);self.assertEqual(tails,[])
        self.assertEqual(sum(k==worker.F_ERR for k,_ in packets),1)
    def test_08_worker_named_definitions_ast_preserved(self):
        def defs(path):
            tree=ast.parse(path.read_bytes())
            return {node.name:ast.dump(node,include_attributes=False) for node in tree.body if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))}
        self.assertEqual(defs(R/'kaggle/source/py/worker.py'),defs(R/'kaggle/step18/worker.py'))
    def test_09_reference_playback_stays_disabled(self):
        w=worker.Worker()
        for want in (True,False):
            out=w.lead_audio({'id':'voice','anchor':'DO_NOT_READ.wav'},35,want,1)
            self.assertEqual(len(out),840);self.assertFalse(out.any())

if __name__=='__main__':unittest.main(verbosity=2)
