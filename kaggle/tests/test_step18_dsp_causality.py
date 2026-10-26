"""S3 real NumPy contracts; selectable frozen17 red control. Not acoustic/Rust tests."""
import importlib.util
import inspect
import math
import os
from pathlib import Path
import sys
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TARGET = os.environ.get('QTTS_S3_TARGET', 'candidate')
PATH = ROOT / ('source/py/audio_rt.py' if TARGET == 'frozen17' else 'step18/step18_audio_rt.py')
spec = importlib.util.spec_from_file_location('s3_contract_dsp_' + TARGET, PATH)
dsp = importlib.util.module_from_spec(spec); spec.loader.exec_module(dsp)
# The red control must execute NumPy even if a native library is installed later.
if TARGET == 'frozen17': dsp._LIB = None


def signal(n=12037, sr=24000):
    t = np.arange(n) / sr
    return ((.013 + .19 * (np.arange(n) % 3000 > 1300)) *
            (np.sin(2*np.pi*211*t) + .2*np.sin(2*np.pi*977*t)) + .003).astype(np.float32)


def split_process(level, x, sizes):
    result=[]; at=0; i=0
    while at<len(x):
        end=min(len(x),at+sizes[i % len(sizes)])
        result.append(level.process(x[at:end]));at=end;i+=1
    return np.concatenate(result) if result else level.process([])


def reference(x, sr=24000, target=-21, max_db=9, min_db=-9, fade=None):
    """Independent, deliberately unoptimized scalar specification (float64 state)."""
    wanted=gain=1.; envelope=10**(target/20); gain_min=10**(min_db/20);gain_max=10**(max_db/20)
    previous_input=previous_output=0.; squared=[]; learned=0; output=[]
    length=max(32,int(sr/100+.5)); fade=max(8,int(sr*.004)) if fade is None else fade
    for index,s in enumerate(np.asarray(x,dtype=np.float32)):
        current=float(s) if math.isfinite(float(s)) else 0.
        filtered=current-previous_input+(1-40*math.pi/sr)*previous_output
        previous_input,previous_output=current,filtered
        squared.append(filtered**2)
        if len(squared)==length:
            rms=math.sqrt(sum(squared)/length);squared=[]
            if rms>10**(-46/20):
                envelope=(1-(.08 if learned<60 else .012))*envelope + (.08 if learned<60 else .012)*rms
                learned+=1
                wanted=min(gain_max,max(gain_min,10**(target/20)/max(envelope,.0001)))
        seconds=.03 if wanted<gain else .6
        gain=gain+(wanted-gain)*(1-math.exp(-1/(sr*seconds)))
        value=filtered*gain
        if index<fade:value*=.5-.5*math.cos(math.pi*index/fade)
        value=math.copysign(.89+.1*math.tanh((abs(value)-.89)/.1),value) if abs(value)>.89 else value
        output.append(round(32767*value))
    return np.array(output,np.int16),gain,envelope


class CausalDSPContracts(unittest.TestCase):
    def level(self, sr=24000, **kwargs):
        lev=dsp.Leveler(sr,**kwargs);self.addCleanup(lev.close);return lev

    def same_partition(self, sizes, n=12037, sr=24000, **kwargs):
        a,b=self.level(sr,**kwargs),self.level(sr,**kwargs);a.start_segment();b.start_segment()
        x=signal(n,sr);expected=a.process(x);actual=split_process(b,x,sizes)
        np.testing.assert_array_equal(actual,expected)
        self.assertEqual((b.gain_db,b.env_dbfs),(a.gain_db,a.env_dbfs))
        return a,b

    def custom_fade(self, lev, n):
        self.assertIn('fade_samples',inspect.signature(lev.start_segment).parameters)
        lev.start_segment(fade_samples=n)

    def test_01_fade_split_at_half(self):self.same_partition([48],1500,max_gain_db=0,min_gain_db=0)
    def test_02_fade_one_sample_calls(self):self.same_partition([1],1500,max_gain_db=0,min_gain_db=0)
    def test_03_subwindow_calls_learn_identically(self):self.same_partition([17])
    def test_04_complete_window_grid(self):self.same_partition([240])
    def test_05_window_minus_one(self):self.same_partition([239])
    def test_06_window_plus_one(self):self.same_partition([241])
    def test_07_irregular_remainders(self):self.same_partition([13,97,239,1,1920,7,400])
    def test_08_random_partition_grid(self):self.same_partition(np.random.default_rng(781).integers(1,2900,40))
    def test_09_multirate_partition(self):
        for sr in (8000,22050,44100,48000):
            with self.subTest(sr=sr):self.same_partition([1,79,241,1920,7],4097,sr)
    def test_10_empty_blocks_no_side_effect(self):
        a,b=self.level(),self.level();a.start_segment();b.start_segment();x=signal(3001)
        expected=a.process(x);head=b.process(x[:47]);before=b.__dict__.copy()
        self.assertEqual(b.process([]).size,0);self.assertEqual(before,b.__dict__)
        np.testing.assert_array_equal(np.concatenate([head,b.process(x[47:])]),expected)
    def test_11_prefix_has_no_lookahead(self):
        prefix=signal(120);a,b=self.level(),self.level()
        aa=a.process(np.concatenate([prefix,signal(3000)]));bb=b.process(np.concatenate([prefix,np.ones(3000,np.float32)*.8]))
        np.testing.assert_array_equal(aa[:len(prefix)],bb[:len(prefix)])
    def test_12_reference_recurrence(self):
        x=signal(19007);lev=self.level();lev.start_segment();out=lev.process(x)
        expected,gain,env=reference(x)
        np.testing.assert_array_equal(out,expected)
        self.assertAlmostEqual(lev.gain_db,20*math.log10(gain),places=10)
        self.assertAlmostEqual(lev.env_dbfs,20*math.log10(env),places=10)
    def test_13_nonfinite_equals_zero(self):
        x=signal(3701);x[::31]=np.nan;x[::53]=np.inf;x[::71]=-np.inf;original=x.copy()
        a,b=self.level(),self.level();a.start_segment();b.start_segment()
        np.testing.assert_array_equal(a.process(x),b.process(np.nan_to_num(x,nan=0.,posinf=0.,neginf=0.)))
        np.testing.assert_array_equal(x,original)
    def test_14_strided_input_not_mutated(self):
        x=signal(7011);view=x[::3];view.flags.writeable=False;copy=view.copy()
        a,b=self.level(),self.level();np.testing.assert_array_equal(a.process(view),b.process(copy));np.testing.assert_array_equal(view,copy)
    def test_15_all_silence_preserves_gain(self):
        lev=self.level();out=split_process(lev,np.zeros(5003,np.float32),[7,19]);self.assertFalse(out.any());self.assertEqual(lev.gain_db,0.)
    def test_16_gate_does_not_learn_subthreshold_noise(self):
        lev=self.level();before=lev.env_dbfs;lev.process(signal(7000)*.0001);self.assertEqual(lev.env_dbfs,before);self.assertEqual(lev.gain_db,0.)
    def test_17_process_length_dtype_extremes(self):
        lev=self.level();x=np.array([np.finfo(np.float32).max,-np.finfo(np.float32).max,1,-1,0]*501,np.float32)
        out=lev.process(x);self.assertEqual(out.dtype,np.int16);self.assertEqual(out.size,x.size)
        self.assertLessEqual(int(np.max(np.abs(out.astype(np.int32)))),round(.99*32767))
        self.assertTrue(math.isfinite(lev.gain_db));self.assertTrue(math.isfinite(lev.env_dbfs))
    def test_18_gain_budget_during_steps(self):
        lev=self.level(max_gain_db=6,min_gain_db=-9)
        for amplitude in (.025,.9,.008,1.,.02):
            lev.process(signal(12000)*amplitude)
            self.assertGreaterEqual(lev.gain_db,-9.-1e-10);self.assertLessEqual(lev.gain_db,6.+1e-10)
    def test_19_positive_flush_resets_dc_and_last(self):
        lev=self.level();lev.process(np.full(301,.3,np.float32));tail=lev.flush(192)
        self.assertEqual(tail.size,192);self.assertEqual(tail[-1],0)
        self.assertFalse(lev.flush(192).any());self.assertFalse(lev.process(np.zeros(500,np.float32)).any())
    def test_20_zero_flush_has_no_side_effect(self):
        a,b=self.level(),self.level();x=signal(3001);a.process(x[:301]);b.process(x[:301]);before=b.__dict__.copy()
        self.assertEqual(b.flush(0).size,0);self.assertEqual(b.__dict__,before)
        np.testing.assert_array_equal(a.flush(192),b.flush(192))
    def test_21_negative_and_fractional_flush_rejected(self):
        lev=self.level()
        for n in (-1,1.2,True):
            with self.subTest(n=n),self.assertRaises(ValueError):lev.flush(n)
    def test_22_flush_preserves_partial_rms_and_fade(self):
        lev=self.level();lev.start_segment();lev.process(signal(47));keys=('_blk_n','_blk_sum','_fade_left','_gain','_want','_env','_seen')
        for k in keys:self.assertIn(k,lev.__dict__)
        before={k:getattr(lev,k) for k in keys};lev.flush(17);self.assertEqual(before,{k:getattr(lev,k) for k in keys})
    def test_23_close_is_idempotent_and_terminal(self):
        lev=self.level();lev.close();lev.close()
        for operation in (lambda:lev.process([.1]),lambda:lev.flush(),lambda:lev.start_segment(),lambda:lev.gain_db,lambda:lev.env_dbfs):
            with self.subTest(operation=operation),self.assertRaises(RuntimeError):operation()
    def test_24_invalid_parameters_rejected(self):
        cases=[{'sr':0},{'sr':-24000},{'sr':True},{'sr':24000.5},{'sr':7999},{'sr':384001},{'target_dbfs':float('nan')},{'target_dbfs':float('inf')},{'target_dbfs':-41},{'max_gain_db':19},{'max_gain_db':-1},{'min_gain_db':1},{'min_gain_db':-25}]
        for params in cases:
            with self.subTest(params=params),self.assertRaises(ValueError):
                lev=dsp.Leveler(**{'sr':24000,**params});lev.close()
    def test_25_zero_and_one_sample_fades(self):
        a,b=self.level(),self.level();self.custom_fade(a,0);np.testing.assert_array_equal(a.process(signal(50)),b.process(signal(50)))
        c=self.level();self.custom_fade(c,1);expected=b=self.level();wanted=expected.process(signal(50));wanted[0]=0
        np.testing.assert_array_equal(c.process(signal(50)),wanted)
    def test_26_invalid_fade_does_not_mutate(self):
        lev=self.level();self.custom_fade(lev,11);before=lev.__dict__.copy()
        for n in (-1,True,1.2):
            with self.subTest(n=n),self.assertRaises(ValueError):lev.start_segment(fade_samples=n)
            self.assertEqual(lev.__dict__,before)
    def test_27_restarted_segment_preserves_learning(self):
        lev=self.level();lev.process(signal(5013));keys=('_prev_x','_prev_y','_blk_n','_blk_sum','_env','_gain','_want','_seen')
        for k in keys:self.assertIn(k,lev.__dict__)
        before={k:getattr(lev,k) for k in keys};lev.start_segment();self.assertEqual(before,{k:getattr(lev,k) for k in keys});self.assertEqual(lev.process([.3])[0],0)
    def test_28_final_internal_state_partition_exact(self):
        a,b=self.same_partition([73,7,901,1,240]);self.assertEqual(a.__dict__,b.__dict__)
    def test_29_long_rms_learning_after_sixty_windows(self):self.same_partition([23,417,1,79],19007)
    def test_30_attack_and_release_follow_reference(self):
        x=np.concatenate([signal(16000)*4,signal(24000)*.12]);lev=self.level();lev.start_segment();out=lev.process(x)
        expected,gain,env=reference(x);np.testing.assert_array_equal(out,expected);self.assertAlmostEqual(lev.gain_db,20*math.log10(gain),places=10)

if __name__=='__main__':unittest.main(verbosity=2)
