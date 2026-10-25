"""S4 real array/state tests, archived S3 AST red control. Not acoustic evidence."""
import ast
import importlib.util
import math
import os
from pathlib import Path
import unittest
import numpy as np
R=Path(__file__).resolve().parents[2]
TARGET=os.environ.get('QTTS_S4_TARGET','candidate')
if TARGET=='s3-before':
    SOURCE=R/'docs/validation/step18/s4-before/kaggle/step18/worker.py'
    node=next(n for n in ast.parse(SOURCE.read_bytes()).body if isinstance(n,ast.ClassDef) and n.name=='EdgeTrimmer')
    ns={'np':np,'SAMPLE_RATE':24000};exec(compile(ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[])),str(SOURCE),'exec'),ns);Trimmer=ns['EdgeTrimmer']
else:
    SOURCE=R/'kaggle/step18/step18_trimmer.py';spec=importlib.util.spec_from_file_location('s4_trimmer_contract',SOURCE);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);Trimmer=module.EdgeTrimmer


def fixture():
    return np.concatenate([np.full(960,.0025,np.float32),np.full(2400,.02,np.float32),np.zeros(1700,np.float32),np.full(60,.03,np.float32),np.full(1500,.0001,np.float32),np.zeros(2000,np.float32)])


def batch_reference(x,keep=840,max_lead=21600,max_held=43200,thr=10**(-46/20)):
    """Offline index/cropping oracle; no queues or candidate methods."""
    x=np.asarray(x,np.float32);frames=[(i,min(i+120,len(x))) for i in range(0,len(x),120)]
    voices=[float(np.sqrt(np.mean(x[a:b].astype(np.float64)**2)))>thr for a,b in frames]
    first=next((i for i,((a,b),v) in enumerate(zip(frames,voices)) if v or b>max_lead),None)
    if first is None:
        tail=x[max(0,len(x)-keep):];return tail.copy() if np.any(tail!=0) else np.empty(0,np.float32)
    start=max(0,frames[first][0]-keep)
    last=next((frames[i][1] for i in range(len(frames)-1,first-1,-1) if voices[i]),frames[first][0])
    end=max(min(len(x),last+keep),len(x)-max_held)
    nz=np.flatnonzero(x)
    if nz.size and nz[-1]>=end:end=max(end,min(len(x),int(nz[-1])+1+keep))
    return x[start:end].copy()


class TrimmerContracts(unittest.TestCase):
    def finish(self,t,**kwargs):
        self.assertTrue(callable(getattr(t,'finish',None)),'explicit finish API required')
        return t.finish(**kwargs)
    def state(self,t):
        self.assertTrue(callable(getattr(t,'snapshot',None)),'accounting snapshot required')
        d=t.snapshot();self.assertTrue(d['sample_accounting_ok']);self.assertLess(d['pending_samples'],120)
        self.assertLessEqual(d['preroll_samples'],t.keep);self.assertLessEqual(d['held_samples'],t.max_held);return d
    def run_parts(self,x,sizes,**kw):
        t=Trimmer(**kw);out=[];at=i=0
        while at<len(x):
            end=min(len(x),at+sizes[i%len(sizes)]);out.append(t.push(x[at:end]));at=end;i+=1
        out.append(self.finish(t));self.state(t)
        return np.concatenate(out),t
    def same(self,sizes,x=None,**kw):
        x=fixture() if x is None else x;a,_=self.run_parts(x,[len(x) or 1],**kw);b,t=self.run_parts(x,sizes,**kw)
        np.testing.assert_array_equal(a,b);return b,t
    def test_01_one_sample_partition(self):self.same([1])
    def test_02_sixty_four_samples_partition(self):self.same([64])
    def test_03_119_samples_partition(self):self.same([119])
    def test_04_exact_grid_partition(self):self.same([120])
    def test_05_grid_plus_one_partition(self):self.same([121])
    def test_06_codec_frame_partition(self):self.same([1920])
    def test_07_irregular_partition(self):self.same([7,119,1,240,1920,53])
    def test_08_random_partition(self):self.same(np.random.default_rng(31).integers(1,2000,50))
    def test_09_cross_chunk_preroll_is_840(self):
        x=np.concatenate([np.full(960,.0025,np.float32),np.full(2400,.02,np.float32)])
        out,_=self.run_parts(x,[960,2400]);np.testing.assert_array_equal(out,x[120:])
    def test_10_terminal_sixty_voiced_samples(self):
        x=np.concatenate([np.full(120,.02,np.float32),np.zeros(120,np.float32),np.full(60,.02,np.float32)])
        out,_=self.run_parts(x,[120,120,60]);np.testing.assert_array_equal(out,x)
    def test_11_entire_short_voiced_segment(self):
        for n in (1,7,60,119):
            with self.subTest(n=n):
                x=np.full(n,.02,np.float32);out,_=self.run_parts(x,[1]);np.testing.assert_array_equal(out,x)
    def test_12_subthreshold_nonzero_tail_retained(self):
        x=np.concatenate([np.full(240,.02,np.float32),np.zeros(2000,np.float32),np.full(60,.00001,np.float32)])
        out,_=self.run_parts(x,[240,2000,60]);np.testing.assert_array_equal(out,x)
    def test_13_only_exact_zero_tail_removed(self):
        x=np.concatenate([np.full(240,.02,np.float32),np.zeros(4000,np.float32)])
        out,t=self.run_parts(x,[1920]);np.testing.assert_array_equal(out,x[:1080]);self.assertEqual(t.snapshot()['trailing_zero_dropped_samples'],3160)
    def test_14_middle_pause_is_not_shortened(self):
        x=np.concatenate([np.full(240,.02,np.float32),np.zeros(9000,np.float32),np.full(360,.02,np.float32)])
        out,_=self.run_parts(x,[137]);np.testing.assert_array_equal(out,x)
    def test_15_held_budget_spills_not_deletes(self):
        x=np.concatenate([np.full(240,.02,np.float32),np.zeros(5000,np.float32),np.full(120,.02,np.float32)])
        out,t=self.run_parts(x,[119],max_held_ms=10);np.testing.assert_array_equal(out,x);self.assertEqual(t.snapshot()['trailing_zero_dropped_samples'],0)
    def test_16_long_leading_silence_is_bounded(self):
        t=Trimmer();returned=0
        for _ in range(150):returned+=len(t.push(np.zeros(480,np.float32)));self.state(t)
        d=self.state(t);self.assertTrue(d['lead_limit_reached']);self.assertGreater(returned,0);self.finish(t);self.state(t)
    def test_17_finish_idempotent(self):
        t=Trimmer();t.push(np.full(60,.02,np.float32));self.finish(t);before=self.state(t);self.assertEqual(self.finish(t).size,0);self.assertEqual(self.state(t),before)
    def test_18_cancel_drops_all_caches(self):
        t=Trimmer();t.push(np.full(240,.02,np.float32));t.push(np.zeros(2003,np.float32));d=self.state(t)
        self.assertGreater(d['buffered_samples'],0);self.assertEqual(self.finish(t,cancelled=True).size,0);after=self.state(t)
        self.assertEqual(after['buffered_samples'],0);self.assertEqual(after['cancel_discarded_samples'],d['buffered_samples'])
    def test_19_push_after_finish_rejected(self):
        t=Trimmer();self.finish(t)
        with self.assertRaises(RuntimeError):t.push(np.ones(1,np.float32))
    def test_20_empty_push_no_state_change(self):
        t=Trimmer();t.push(np.full(47,.02,np.float32));before=self.state(t);self.assertEqual(t.push([]).size,0);self.assertEqual(self.state(t),before)
    def test_21_empty_stream_finish(self):
        t=Trimmer();self.assertEqual(self.finish(t).size,0);self.assertEqual(self.state(t)['input_samples'],0)
    def test_22_readonly_strided_input_not_mutated(self):
        a=fixture();x=a[::2];copy=x.copy();x.flags.writeable=False
        out,_=self.run_parts(x,[137]);expected,_=self.run_parts(copy,[137]);np.testing.assert_array_equal(out,expected);np.testing.assert_array_equal(x,copy)
    def test_23_independent_batch_oracle(self):
        for keep,held in ((0,0),(35,1800),(5,10)):
            with self.subTest(keep=keep,held=held):
                x=fixture();out,_=self.run_parts(x,[17,1920,1],keep_ms=keep,max_held_ms=held)
                np.testing.assert_array_equal(out,batch_reference(x,keep=int(keep*24),max_held=int(held*24)))
    def test_24_long_quiet_batch_oracle(self):
        for value in (0.,.0001):
            with self.subTest(value=value):
                x=np.full(72037,value,np.float32);out,_=self.run_parts(x,[1920]);np.testing.assert_array_equal(out,batch_reference(x))
    def test_25_grid_and_actual_partial_rms(self):
        t=Trimmer();self.assertEqual(t.push(np.full(119,.006,np.float32)).size,0);out=self.finish(t);self.assertEqual(out.size,119)
    def test_26_low_level_unstarted_history_preserved(self):
        x=np.full(60,.0001,np.float32);out,_=self.run_parts(x,[17]);np.testing.assert_array_equal(out,x)
    def test_27_invalid_configurations_rejected(self):
        for kw in ({'sr':True},{'sr':7999},{'sr':24000.5},{'keep_ms':-1},{'keep_ms':float('inf')},{'max_held_ms':-1},{'max_lead_ms':float('nan')},{'thr_db':1}):
            with self.subTest(kw=kw),self.assertRaises(ValueError):
                try:Trimmer(**kw)
                except OverflowError:self.fail('configuration must reject with controlled ValueError, not overflow')
    def test_28_nonfinite_equals_zero_and_extremes_finite(self):
        x=np.tile(np.array([np.nan,np.inf,-np.inf,.02],np.float32),121);clean=np.nan_to_num(x,nan=0.,posinf=0.,neginf=0.)
        a,_=self.run_parts(x,[17]);b,_=self.run_parts(clean,[17]);np.testing.assert_array_equal(a,b)
        extreme=np.full(121,np.finfo(np.float32).max,np.float32);out,_=self.run_parts(extreme,[17]);np.testing.assert_array_equal(out,extreme)
    def test_29_zero_keep_and_zero_hold_defined(self):
        x=np.concatenate([np.zeros(120,np.float32),np.full(240,.02,np.float32),np.zeros(240,np.float32)])
        out,t=self.run_parts(x,[1],keep_ms=0,max_held_ms=0);np.testing.assert_array_equal(out,x[120:]);self.assertEqual(t.snapshot()['buffered_samples'],0)
    def test_30_all_state_counters_conserve_during_stream(self):
        t=Trimmer();x=fixture()
        for at in range(0,len(x),73):t.push(x[at:at+73]);self.state(t)
        self.finish(t);d=self.state(t);self.assertEqual(d['input_samples'],len(x));self.assertEqual(d['buffered_samples'],0)

if __name__=='__main__':unittest.main(verbosity=2)
