"""Reference revision / generated-only windows / bounded gain, not T4 listening."""
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from types import SimpleNamespace as NS
from unittest.mock import patch
import numpy as np
import torch
import test_reliability
import worker
import clone_stream
from voice_binding import reference_binding


class BindingTests(unittest.TestCase):
    def test_cross_language_unicode_nul_and_mutations(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'a.wav').write_bytes(b'RIFF\x00\xffTEST')
            prof={'anchor':'a.wav','ref_text':'你好 café\x00声音','language':'Chinese'}
            pin=reference_binding(p,prof)
            self.assertEqual(pin,'17f55c974517bf2cfa3cde3f0c3b207952acb89b174595fde9b25920c59625ab')
            for k,v in [('ref_text','new'),('language','English')]:
                self.assertNotEqual(reference_binding(p,dict(prof,**{k:v})),pin)
            self.assertEqual(reference_binding(p,dict(prof,quality=.9)),pin)
            (p/'a.wav').write_bytes(b'new');self.assertNotEqual(reference_binding(p,prof),pin)

    def test_path_and_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'a.wav').write_bytes(b'wave');(p/'link.wav').symlink_to(p/'a.wav')
            for anchor in ('../a.wav','a\\b.wav','/tmp/a.wav','.','..','link.wav'):
                with self.subTest(anchor=anchor),self.assertRaises((ValueError,OSError)):
                    reference_binding(p,{'anchor':anchor})
            self.assertEqual(reference_binding(p,{},allow_missing=True),'')
            with self.assertRaises(ValueError):reference_binding(p,{})

    def test_mismatch_refused_before_even_lead_pcm(self):
        w=worker.Worker();w.ready=True;w.profiles['v']={'id':'v'}
        frames=[];w.run_job({'profile':'v','text':'hello','lead_pause_ms':500,'voice_binding':'old'},frames.append,threading.Event(),0)
        self.assertFalse(any(f and f[0]==worker.F_PCM for f in frames))
        self.assertTrue(any(f and f[0]==worker.F_ERR for f in frames))

    def test_revision_changed_while_waiting_is_rechecked_under_lock(self):
        w=worker.Worker();w.ready=True;w.profiles['v']={'id':'v'};frames=[];read=threading.Event()
        def load(pid):read.set();return {'id':'v'}
        w.lock.acquire()
        with patch.object(worker,'load_profile',side_effect=load):
            t=threading.Thread(target=w.run_job,args=({'profile':'v','text':'hello','voice_binding':'old'},frames.append,threading.Event(),0));t.start()
            self.assertFalse(read.wait(.15),'read profile happened before synthesis lock')
            w.lock.release();t.join(5)
        self.assertFalse(t.is_alive());self.assertTrue(read.is_set())
        self.assertFalse(any(f and f[0]==worker.F_PCM for f in frames))

    def test_profile_read_after_load_lock_and_extraction_change_rejected(self):
        w=worker.Worker();w.ready=True;prof={'id':'v'}
        with patch.object(worker,'load_profile',return_value=prof) as reader,patch.object(worker,'reference_binding',side_effect=['old','new']):
            with self.assertRaisesRegex(RuntimeError,'during prompt extraction'):w.load_profile('v')
        self.assertNotIn('v',w.profiles)


class ConditioningTests(unittest.TestCase):
    def test_default_icl_preserves_matching_reference_text_as_condition(self):
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}):
            self.assertEqual(clone_stream.conditioning({'ref_text':'准确转写'}),('准确转写',False))
            with self.assertRaisesRegex(ValueError,'matching'):clone_stream.conditioning({})
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'xvector'}):
            self.assertEqual(clone_stream.conditioning({'ref_text':'ignored'}),('',True))
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'guess'}):
            with self.assertRaises(ValueError):clone_stream.conditioning({})

    def test_reload_evicts_same_path_prompt_only(self):
        e=worker.RealEngine(0);e.sane=True;prof={'id':'v','anchor':'a.wav','ref_text':'准确转写'}
        anchor=str(worker.profile_dir('v')/'a.wav');seen=[]
        cache={(anchor,'old',True,False):'STALE',('other.wav','x',False,False):'KEEP'}
        def resolve(**kw):
            seen.append(kw);self.assertFalse(any(k[0]==anchor for k in cache));return {},[],True
        e.model=NS(_voice_prompt_cache=cache,_resolve_voice_clone_prompt_from_reference=resolve)
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}):info=e.load_profile(prof)
        self.assertEqual(seen[0]['ref_text'],'准确转写');self.assertFalse(seen[0]['xvec_only'])
        self.assertEqual(len(cache),1);self.assertEqual(info['voice_conditioning'],'icl-generated-only-codec')

    def test_engine_passes_icl_target_separately_and_closes_generator(self):
        e=worker.RealEngine(0);e._prompts['v']={};e.model=NS();seen=[];closed=[]
        def stream(model,**kw):
            seen.append(kw)
            try:yield np.ones(4800,np.float32)*.1,24000,{'codec_ms':2,'codec_window_frames':8}
            finally:closed.append(True)
        with patch.object(worker,'generated_only_stream',side_effect=stream),patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}):
            out=list(e.stream({'id':'v','anchor':'a.wav','ref_text':'参考内容'},'只生成目标','Chinese',4,100,7,threading.Event()))
        self.assertEqual(len(out),1);self.assertTrue(closed)
        self.assertEqual(seen[0]['text'],'只生成目标');self.assertEqual(seen[0]['ref_text'],'参考内容')
        self.assertFalse(seen[0]['xvec_only']);self.assertFalse(seen[0]['append_silence'])
        self.assertEqual(e.last_stream_metrics['codec_ms'],2)


class CodecWindowTests(unittest.TestCase):
    @staticmethod
    def codec(calls,unstable=False):
        def decode(body):
            codes=body['audio_codes'];calls.append(codes.shape[1]);assert torch.all(codes<999)
            audio=np.repeat(codes[0,:,0].numpy().astype(np.float32)*.001,1920)
            if unstable:audio[-min(len(audio),2*1920):]+=.5
            return [audio],24000
        return NS(decode=decode)

    def test_all_chunk_sizes_complete_exact_bounded_generated_samples(self):
        for chunk in (2,4,8,12,16):
            calls=[];w=clone_stream.GeneratedCodecWindow(self.codec(calls));out=[]
            for i in range(0,211,chunk):
                codes=torch.arange(i,min(i+chunk,211))[:,None].repeat(1,16)
                out.append(w.push(codes))
            out.append(w.finish());y=np.concatenate(out)
            self.assertEqual(len(y),211*1920)
            np.testing.assert_array_equal(y,np.repeat(np.arange(211,dtype=np.float32)*.001,1920))
            self.assertLessEqual(max(calls),25+2+chunk)
            self.assertEqual(w.finish().size,0)

    def test_lookahead_prevents_committing_unstable_right_edges(self):
        w=clone_stream.GeneratedCodecWindow(self.codec([],True),lookahead=2);out=[]
        for i in range(0,32,4):out.append(w.push(torch.arange(i,i+4)[:,None].repeat(1,16)))
        y=np.concatenate(out)
        np.testing.assert_array_equal(y,np.repeat(np.arange(30,dtype=np.float32)*.001,1920))
        self.assertEqual(w.finish().size,2*1920)

    def test_short_tail_flush_and_cancel_no_late_pcm(self):
        w=clone_stream.GeneratedCodecWindow(self.codec([]),lookahead=2);self.assertEqual(w.push(torch.ones(1,16,dtype=torch.long)).size,0)
        self.assertEqual(w.finish().size,1920)
        w=clone_stream.GeneratedCodecWindow(self.codec([]),lookahead=2);w.push(torch.ones(2,16,dtype=torch.long))
        self.assertEqual(w.finish(cancelled=True).size,0);self.assertEqual(w.finish().size,0)

    def test_wrong_codec_contract_fails_closed(self):
        for length,sr,val in [(1921,24000,.1),(1920,22050,.1),(1920,24000,float('nan'))]:
            w=clone_stream.GeneratedCodecWindow(NS(decode=lambda body:([np.full(length,val)],sr)))
            with self.assertRaises(RuntimeError):w.push(torch.ones(1,16,dtype=torch.long))
        for shape in ((2,15),(17,16),(0,16)):
            w=clone_stream.GeneratedCodecWindow(self.codec([]))
            with self.assertRaises(RuntimeError):w.push(torch.ones(shape,dtype=torch.long))


class NoiseAndGainTests(unittest.TestCase):
    def test_max_gain_safe_bounds_and_invalid_config(self):
        for value,want in [('6',6),('12',12),('0',0),('-1',6),('13',6),('nan',6),('inf',6),('bad',6)]:
            with patch.dict(os.environ,{'QTTS_MAX_GAIN_DB':value}):self.assertEqual(worker.output_max_gain_db(),want)

    def test_leveler_reset_removes_history_and_limits_upward_gain(self):
        w=worker.Worker();y=(.001*np.sin(np.arange(48000)*.1)).astype(np.float32)
        with patch.dict(os.environ,{'QTTS_MAX_GAIN_DB':'6'}):
            a=w._reset_leveler('v');first=a.process(y);a.process(np.ones(48000,np.float32)*.8)
            b=w._reset_leveler('v');second=b.process(y)
        np.testing.assert_array_equal(first,second);self.assertLessEqual(b.gain_db,6.0001)
        self.assertEqual(b.target_dbfs,-18)

    def test_empty_second_job_cannot_flush_prior_voice(self):
        w=worker.Worker();w.ready=True;w.profiles['v']={'id':'v'}
        signal=(.1*np.sin(np.arange(12000)*.1)).astype(np.float32)
        w.engine.stream=lambda *a:iter([signal]);w.run_job({'profile':'v','text':'hello'},lambda f:None,threading.Event(),0)
        w.engine.stream=lambda *a:iter([]);frames=[]
        w.run_job({'profile':'v','text':'hello'},frames.append,threading.Event(),0)
        self.assertFalse(any(f and f[0]==worker.F_PCM for f in frames))


if __name__=='__main__':unittest.main()

class ReloadAndBenchmarkTests(unittest.TestCase):
    def test_partial_reload_is_not_reported_as_success(self):
        import analyst
        self.assertEqual(analyst.reload_response([{'ok':True},{'ok':False}]).status_code,503)
        self.assertEqual(analyst.reload_response([{'ok':True},{'ok':True}]).status_code,200)

    def benchmark_module(self):
        import importlib.util
        p=Path(__file__).resolve().parents[1]/'source/tools/voice_benchmark.py'
        spec=importlib.util.spec_from_file_location('voice_benchmark_unit',p)
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

    def test_real_benchmark_is_explicit_and_blocked_without_run(self):
        m=self.benchmark_module();r=m.run(NS(run=False))
        self.assertEqual(r['status'],'blocked');self.assertFalse(r['voice_quality_verified'])
        self.assertFalse(r['real_gpu_verified']);self.assertFalse(r['all_user_requirements_completed'])

    def test_benchmark_excludes_padding_and_refuses_mock_or_anomalies(self):
        from unittest.mock import MagicMock
        import requests
        m=self.benchmark_module()
        base={'engine':'faster-qwen3-tts','voice_binding':'pin','speech_samples':24000,'rtf':.03,'gen_ms':30,'anomalies':[]}
        for mutate,passed in [({},True),({'engine':'mock'},False),({'anomalies':['too_long']},False),({'speech_samples':24192},False),({'rtf':0},False),({'cancelled':True},False),({'voice_binding':'old'},False)]:
            stats=dict(base,**mutate);data=worker.frame(1,bytes((24000+192)*2))+worker.jframe(2,stats)
            response=MagicMock();response.__enter__.return_value=response;response.iter_content.return_value=iter([data])
            with patch.object(requests,'post',return_value=response),patch.object(m.time,'perf_counter',side_effect=[10,10.04]):
                if passed:
                    pcm,row=m.measure('http://127.0.0.1',{'voice_binding':'pin'});self.assertEqual(row['speech_seconds'],1)
                    self.assertAlmostEqual(row['wall_rtf'],.04);self.assertEqual(row['worker_rtf'],.03)
                else:
                    with self.assertRaises(RuntimeError):m.measure('http://127.0.0.1',{'voice_binding':'pin'})

class FinalPolicyTests(unittest.TestCase):
    def test_default_zero_lookahead_and_explicit_experiment_bounds(self):
        with patch.dict(os.environ,{},clear=True):self.assertEqual(clone_stream.codec_lookahead_frames(),0)
        with patch.dict(os.environ,{'QTTS_CODEC_LOOKAHEAD_FRAMES':'2'}):self.assertEqual(clone_stream.codec_lookahead_frames(),2)
        for value in ('3','-1','nan','bad'):
            with patch.dict(os.environ,{'QTTS_CODEC_LOOKAHEAD_FRAMES':value}),self.assertRaises(ValueError):clone_stream.codec_lookahead_frames()

    def test_different_worker_mode_fails_before_pcm(self):
        w=worker.Worker();w.ready=True;w.profiles['v']={'id':'v'};frames=[]
        w.run_job({'profile':'v','text':'hello','voice_conditioning':'other','lead_pause_ms':100},frames.append,threading.Event(),0)
        self.assertTrue(any(f and f[0]==worker.F_ERR for f in frames))
        self.assertFalse(any(f and f[0]==worker.F_PCM for f in frames))

    def test_synthesis_requires_an_in_memory_prompt_snapshot(self):
        e=worker.RealEngine(0)
        with self.assertRaisesRegex(RuntimeError,'version-checked'):
            list(e.stream({'id':'v','anchor':'a.wav','ref_text':'hello'},'target','English',4,100,17,threading.Event()))
