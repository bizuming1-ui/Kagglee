"""S4 real worker/trimmer/DSP/framing, only engine and reference pin are fixtures."""
import ast
import importlib.util
import json
from pathlib import Path
import sys
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import numpy as np
from test_step18_dsp_worker import frames,worker as s3worker
from test_step18_trimmer import batch_reference,fixture
R=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('s4_worker_contract',R/'kaggle/step18/worker_s4.py');worker=importlib.util.module_from_spec(spec);sys.modules[spec.name]=worker;spec.loader.exec_module(worker)
import step18_trimmer as trimmer
import step18_audio_rt as dsp

class WorkerTrimmerContracts(unittest.TestCase):
    def run_job(self,x,sizes=(1920,),cancel_in_engine=False,fail=False,cancel_on_drain=False):
        w=worker.Worker();w.ready=True;w.profiles['voice']={'id':'voice'};w.voice_bindings['voice']='fixturepin'
        cancel=threading.Event();emitted=[];instances=[];processed=[];flushes=[]
        class CapturingTrimmer(trimmer.EdgeTrimmer):
            def __init__(self):super().__init__();instances.append(self)
            def finish(self,cancelled=False):
                was_open=not self.closed;result=super().finish(cancelled)
                if cancel_on_drain and was_open and not cancelled:cancel.set()
                return result
        class CaptureDSP(dsp.Leveler):
            def process(self,a):processed.append(a.copy());return super().process(a)
            def flush(self,n=192):flushes.append(n);return super().flush(n)
        def stream(*args):
            at=i=0
            while at<len(x):
                end=min(len(x),at+sizes[i%len(sizes)]);yield x[at:end];at=end;i+=1
                if fail:raise RuntimeError('S4 fixture engine failure')
                if cancel_in_engine:cancel.set()
        w.engine=SimpleNamespace(name='synthetic-engine',dtype_name='cpu-fixture',supports_trained=False,stream=stream)
        with patch.object(worker,'load_profile',return_value=None),patch.object(worker,'reference_binding',return_value='fixturepin'),patch.object(worker,'EdgeTrimmer',CapturingTrimmer),patch.object(worker.audio_rt,'Leveler',CaptureDSP):
            w.run_job({'profile':'voice','text':'合成数值合同','seed':7,'breath':True,'tail_pause_ms':0},emitted.append,cancel,worker.now_ms())
        packets=frames(emitted);stats=json.loads([p for k,p in packets if k==worker.F_STATS][-1]);pcm=[np.frombuffer(p,dtype='<i2') for k,p in packets if k==worker.F_PCM]
        self.assertIsNone(emitted[-1]);self.assertFalse(w.lock.locked());self.assertFalse(w.busy)
        self.assertTrue(stats['trim']['closed']);self.assertTrue(stats['trim']['sample_accounting_ok']);self.assertEqual(stats['trim']['buffered_samples'],0)
        self.addCleanup(w.levelers['voice'].close)
        return np.concatenate(pcm) if pcm else np.empty(0,np.int16),stats,processed,flushes,packets
    def direct(self,x):
        lev=dsp.Leveler(24000,worker.output_target_dbfs(),worker.output_max_gain_db());self.addCleanup(lev.close);lev.start_segment()
        return np.concatenate([lev.process(x),lev.flush(192)])
    def test_01_unique_binding_and_s3_preservation(self):
        self.assertIs(worker.EdgeTrimmer,trimmer.EdgeTrimmer);self.assertIsNot(worker.EdgeTrimmer,s3worker.EdgeTrimmer);self.assertIs(worker.audio_rt,s3worker.audio_rt)
    def test_02_short_segment_emitted_at_finish(self):
        x=np.full(60,.02,np.float32);pcm,st,inputs,flushes,_=self.run_job(x,[17]);np.testing.assert_array_equal(pcm,self.direct(x))
        self.assertEqual(st['speech_samples'],60);self.assertEqual(st['chunks'],1);self.assertEqual(flushes,[192]);self.assertEqual(st['trim']['input_samples'],60)
    def test_03_whole_and_split_worker_pcm_identical(self):
        x=fixture();a,st,_,_,_=self.run_job(x,[len(x)]);b,bst,inputs,_,_=self.run_job(x,[1,119,7,1920,240])
        np.testing.assert_array_equal(a,b);np.testing.assert_array_equal(a,self.direct(batch_reference(x)))
        self.assertEqual(st['speech_samples'],bst['speech_samples']);self.assertFalse(bst['quality_verified']);self.assertFalse(bst['reference_pcm_splicing'])
    def test_04_cross_chunk_preroll_preserved(self):
        x=np.concatenate([np.full(960,.0025,np.float32),np.full(2400,.02,np.float32)]);pcm,st,_,_,_=self.run_job(x,[960,2400])
        self.assertEqual(st['speech_samples'],3240);self.assertEqual(st['trim']['leading_dropped_samples'],120);np.testing.assert_array_equal(pcm,self.direct(x[120:]))
    def test_05_subthreshold_terminal_tail_reaches_dsp(self):
        x=np.concatenate([np.full(240,.02,np.float32),np.zeros(2000,np.float32),np.full(60,.00001,np.float32)])
        pcm,st,inputs,_,_=self.run_job(x,[240,2000,60]);np.testing.assert_array_equal(np.concatenate(inputs),x);np.testing.assert_array_equal(pcm,self.direct(x));self.assertEqual(st['speech_samples'],len(x))
    def test_06_cancelled_pending_not_drained(self):
        pcm,st,inputs,flushes,packets=self.run_job(np.full(180,.02,np.float32),[60],cancel_in_engine=True)
        self.assertTrue(st['cancelled']);self.assertEqual(pcm.size,0);self.assertEqual(inputs,[]);self.assertEqual(flushes,[]);self.assertEqual(st['trim']['cancel_discarded_samples'],60)
    def test_07_failure_cleans_pending_without_fake_success(self):
        pcm,st,inputs,flushes,packets=self.run_job(np.full(60,.02,np.float32),[60],fail=True)
        self.assertTrue(st['failed']);self.assertEqual(pcm.size,0);self.assertEqual(flushes,[]);self.assertEqual(sum(k==worker.F_ERR for k,_ in packets),1);self.assertEqual(st['trim']['cancel_discarded_samples'],60)
    def test_08_cancel_after_finish_before_pcm_emission(self):
        pcm,st,inputs,flushes,_=self.run_job(np.full(60,.02,np.float32),[60],cancel_on_drain=True)
        self.assertTrue(st['cancelled']);self.assertEqual(pcm.size,0);self.assertEqual(flushes,[]);self.assertEqual(inputs,[]);self.assertEqual(st['cancelled_after_trim_samples'],60);self.assertEqual(st['trim']['returned_samples'],60)
    def test_09_exact_zero_trim_accounting_wire_and_dsp(self):
        x=np.concatenate([np.full(240,.02,np.float32),np.zeros(4000,np.float32)]);pcm,st,inputs,_,_=self.run_job(x,[47,1920,120])
        self.assertEqual(st['trim']['trailing_zero_dropped_samples'],3160);self.assertEqual(st['speech_samples'],1080);self.assertEqual(len(pcm),1080+192)
        self.assertEqual(st['trim']['returned_samples'],st['speech_samples']);self.assertFalse(st['trim']['quality_verified']);np.testing.assert_array_equal(pcm,self.direct(x[:1080]))
    def test_10_worker_scope_only_run_job_and_trimmer_alias(self):
        def defs(path):return {n.name:n for n in ast.parse(path.read_bytes()).body if isinstance(n,(ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef))}
        old=defs(R/'kaggle/step18/worker.py');new=defs(R/'kaggle/step18/worker_s4.py')
        self.assertEqual(set(old)-set(new),{'EdgeTrimmer'});self.assertEqual(set(new)-set(old),set())
        self.assertEqual({k for k in new if ast.dump(new[k])!=ast.dump(old[k])},{'Worker'})
        def methods(node):return {n.name:ast.dump(n) for n in node.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
        a,b=methods(old['Worker']),methods(new['Worker']);self.assertEqual(set(a),set(b));self.assertEqual({k for k in a if a[k]!=b[k]},{'run_job'})

if __name__=='__main__':unittest.main(verbosity=2)
