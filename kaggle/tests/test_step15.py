"""Reference isolation / output level / build cost tests. NOT Qwen/T4 listening evidence."""
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from types import SimpleNamespace as NS
from unittest.mock import patch
import numpy as np
import test_reliability
import worker
import analyst
import audio_rt
from fastapi.testclient import TestClient

class ReferenceIsolationTests(unittest.TestCase):
    def test_explicit_xvector_never_conditions_on_reference_text_or_codes(self):
        captured=[];closed=[]
        def generate(**kwargs):
            captured.append(kwargs)
            try:yield np.ones(4800,np.float32)*.1,24000,{}
            finally:closed.append(True)
        engine=worker.RealEngine(0);engine._prompts['v']={};engine.model=NS(generate_voice_clone_streaming=generate)
        with patch.dict(sys.modules,{'torch':NS(manual_seed=lambda seed:None)}),patch.dict(os.environ,{'QTTS_CLONE_MODE':'xvector'}),patch.object(worker,'generated_only_stream',side_effect=lambda model,**kw:generate(**kw)):
            result=list(engine.stream({'id':'v','anchor':'anchor.wav','ref_text':'REFERENCE MUST NOT BE SPOKEN'},'目标文字','Chinese',4,100,7,threading.Event()))
        self.assertEqual(len(result),1);self.assertEqual(len(closed),1)
        args=captured[0]
        self.assertEqual(args['text'],'目标文字');self.assertEqual(args['ref_text'],'')
        self.assertIs(args['xvec_only'],True);self.assertIs(args['append_silence'],False)

    def test_profile_warmup_uses_same_isolated_prompt(self):
        captured=[];engine=worker.RealEngine(0);engine.sane=True
        engine.model=NS(_resolve_voice_clone_prompt_from_reference=lambda **kw:(captured.append(kw) or ({},[],False)))
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'xvector'}):
            info=engine.load_profile({'id':'v','anchor':'ref.wav','ref_text':'secret reference'})
        self.assertEqual(captured[0]['ref_text'],'');self.assertTrue(captured[0]['xvec_only'])
        self.assertFalse(captured[0]['append_silence']);self.assertFalse(info['reference_pcm_splicing'])

    def test_old_reference_environment_cannot_splice_nonzero_pcm(self):
        w=worker.Worker();w.breath_banks['v']=[np.ones(50000,np.float32)*.7]
        with patch.dict(os.environ,{'QTTS_BREATH_MODE':'reference'}):
            for pause in (-1,0,150,500,1500,9999):
                y=w.lead_audio({'id':'v'},pause,True,42)
                self.assertEqual(y.size,int(max(0,min(pause,1500))*24));self.assertFalse(y.any())

    def test_loading_old_profile_never_opens_breath_wav(self):
        w=worker.Worker();w.ready=True
        prof={'id':'v','anchor':'ref.wav','ref_text':'x','breath_files':['secret.wav'],'target_rms_dbfs':-21}
        with patch.object(worker,'load_profile',return_value=prof),patch.dict(os.environ,{'QTTS_OUTPUT_DBFS':'-18'}),patch('soundfile.read',side_effect=AssertionError('reference breath read forbidden')):
            info=w.load_profile('v')
        self.assertEqual(w.breath_banks['v'],[]);self.assertEqual(info['breath_clips'],0)
        self.assertEqual(w.levelers['v'].target_dbfs,-18)

    def test_complete_worker_stream_only_has_silent_lead_and_generated_signal(self):
        w=worker.Worker();w.ready=True;w.profiles['v']={'id':'v'}
        w.levelers['v']=audio_rt.Leveler(24000,-18)
        w.breath_banks['v']=[np.ones(12000,np.float32)*.7]
        generated=(.05*np.sin(np.arange(12000)*2*np.pi*440/24000)).astype(np.float32)
        w.engine.stream=lambda *args:iter([generated])
        frames=[]
        with patch.dict(os.environ,{'QTTS_BREATH_MODE':'reference'}):
            w.run_job({'profile':'v','text':'测试声音','lead_pause_ms':500,'breath':True},frames.append,threading.Event(),0)
        pcm=[np.frombuffer(f[5:],dtype='<i2') for f in frames if f and f[0]==worker.F_PCM]
        self.assertEqual(pcm[0].size,12000);self.assertFalse(pcm[0].any())
        self.assertGreater(np.max(np.abs(pcm[1])),100)
        stats=json.loads(next(f[5:] for f in frames if f and f[0]==worker.F_STATS))
        self.assertFalse(stats['reference_pcm_splicing']);self.assertFalse(stats['acoustic_text_verified'])

class LoudnessTests(unittest.TestCase):
    def test_output_target_has_safe_finite_bounds_and_fallback(self):
        for value,want in [('-18',-18),('-14',-14),('-24',-24),('-13',-18),('-25',-18),('nan',-18),('inf',-18),('no',-18)]:
            with self.subTest(value=value),patch.dict(os.environ,{'QTTS_OUTPUT_DBFS':value}):self.assertEqual(worker.output_target_dbfs(),want)
        with patch.dict(os.environ,{},clear=True):self.assertEqual(worker.output_target_dbfs(),-18)

    def test_new_target_is_louder_on_low_level_signal_without_overflow(self):
        y=(.035*np.sin(2*np.pi*440*np.arange(24000*6)/24000)).astype(np.float32)
        old,new=audio_rt.Leveler(24000,-21),audio_rt.Leveler(24000,-18,max_gain_db=12)
        a=old.process(y);b=new.process(y)
        old_rms=np.sqrt(np.mean(a[-24000:].astype(float)**2))
        new_rms=np.sqrt(np.mean(b[-24000:].astype(float)**2))
        gain=20*np.log10(new_rms/old_rms)
        self.assertGreater(gain,2);self.assertLess(gain,4)
        self.assertLess(np.max(np.abs(b.astype(float))),32767)

    def test_hot_input_is_limited_not_wrapped(self):
        y=(3*np.sin(np.arange(24000)*.1)).astype(np.float32)
        b=audio_rt.Leveler(24000,-18).process(y)
        self.assertEqual(b.dtype,np.int16);self.assertLess(np.max(np.abs(b.astype(float))),32767)

class BuildCostTests(unittest.TestCase):
    def test_embeddings_cached_by_samples_not_name_and_private_per_build(self):
        calls=[];spk=NS(embed=lambda y:(calls.append(y.copy()) or np.array([.1,.2])))
        cache=analyst.BuildEmbeddingCache(spk);y=np.arange(16000,dtype=np.float32)
        cache.embed(y)[0]=99
        self.assertEqual(cache.embed(y.copy())[0],.1)
        cache.embed(y+1)
        self.assertEqual(cache.report()['calls'],2);self.assertEqual(cache.report()['hits'],1)
        analyst.BuildEmbeddingCache(spk).embed(y);self.assertEqual(len(calls),3)

    def test_embeddings_entry_budget_is_bounded(self):
        cache=analyst.BuildEmbeddingCache(NS(embed=lambda y:np.array([.1,.2])))
        for i in range(80):cache.embed(np.array([i],np.float32))
        self.assertEqual(cache.report()['entries'],64)
        self.assertEqual(cache.report()['calls'],80)

    def test_cpu_asr_reuse_does_not_keep_cuda_model(self):
        for name,flag,unloaded in [('large-v3/cpu-int8','1',False),('cpu-int8','1',False),('large-v3/cuda-float16','1',True),('large-v3/cpu-int8','0',True)]:
            model=analyst.ASRModel();model.model=object();model.name=name
            with self.subTest(name=name,flag=flag),patch.dict(os.environ,{'QTTS_ASR_KEEP_CPU':flag}),patch.object(model,'unload') as unload:
                self.assertEqual(model.release_after_use(),unloaded);self.assertEqual(unload.called,unloaded)

    def test_release_waits_for_entire_lazy_transcription_not_just_model_load(self):
        model=analyst.ASRModel();model.name='large-v3/cpu-int8'
        entered=threading.Event();finish=threading.Event();release_attempted=threading.Event();released=threading.Event()
        answers=[];errors=[]
        def segments():
            entered.set()
            if not finish.wait(5):raise AssertionError('fixture transcription release deadline')
            yield NS(start=0.,end=1.,text='测试',avg_logprob=0.,words=[])
        model.model=NS(transcribe=lambda *a,**k:(segments(),NS(language='zh')))
        def transcribe():
            try:answers.append(model.transcribe(np.ones(16000,np.float32),'zh'))
            except Exception as e:errors.append(e)
        def release():
            release_attempted.set();model.release_after_use();released.set()
        with patch.object(analyst,'MOCK',False),patch.dict(os.environ,{'QTTS_ASR_KEEP_CPU':'0'}):
            a=threading.Thread(target=transcribe);a.start()
            try:
                self.assertTrue(entered.wait(2))
                b=threading.Thread(target=release);b.start();self.assertTrue(release_attempted.wait(2))
                self.assertFalse(released.wait(.05),'model released while lazy ASR still uses it')
                self.assertIsNotNone(model.model)
            finally:
                finish.set();a.join(3)
                if 'b' in locals():b.join(3)
        self.assertFalse(errors,errors);self.assertTrue(released.is_set());self.assertIsNone(model.model)
        self.assertEqual(answers[0][1][0]['text'],'测试')

    def test_direct_api_default_does_not_request_gpu_calibration(self):
        observed=[]
        def capture(jobs,job,budget,run):
            with patch.object(analyst,'build_profile',side_effect=lambda *a:observed.append(a[-1])):run()
        with TestClient(analyst.app) as client,patch.object(analyst.ADMISSION,'start',side_effect=capture):
            response=client.post('/profiles',data={'name':'named'},files={'files':('a.wav',b'1234')})
        # capture replaces the normal admission finally, so release the test-acquired slot.
        analyst.ADMISSION.slot.release()
        self.assertEqual(response.status_code,200,response.text);self.assertEqual(observed,[False])

    def run_profile(self,root,duration=6,manual='对应的短参考文字',segments=None,calibrate=False):
        y=(.1*np.sin(np.arange(24000*duration)*.05)).astype(np.float32)
        job={'id':'test','state':'running','pct':0,'log':[]}
        spk=NS(method='fixture-not-ecapa',load=lambda:None,embed=lambda y:np.array([1.,0.]),sim=lambda a,b:1.)
        kwargs={}
        if segments is not None:kwargs['transcribe']=lambda *a:('zh',segments)
        asr=NS(name='fixture-not-whisper',release_after_use=lambda:None,**kwargs)
        with patch.object(analyst,'SPK',spk),patch.object(analyst,'ASR',asr),patch.object(analyst,'decode_audio',return_value=y),patch.object(analyst,'highpass',side_effect=lambda y,sr:y),patch.object(analyst,'estimate_snr',return_value=40),patch.object(analyst,'to16k',side_effect=lambda y:np.interp(np.arange(round(len(y)*2/3))*1.5,np.arange(len(y)),y).astype(np.float32)),patch.object(analyst,'f0_track',return_value=np.ones(duration*100)*100),patch.object(analyst,'find_breaths',return_value=[]),patch.object(analyst,'profile_dir',side_effect=lambda pid:Path(root)/pid),patch.object(analyst,'load_profile',side_effect=lambda pid:json.loads((Path(root)/pid/'profile.json').read_text())),patch.object(analyst,'load_on_workers',return_value=[{'ok':True},{'ok':True}]),patch.object(analyst,'MOCK',False):
            analyst.build_profile(job,'test',[('a.wav',b'fixture')],'Chinese',manual,calibrate)
        return job

    def test_final_build_receipt_is_persisted_not_lost_after_calibration(self):
        with tempfile.TemporaryDirectory() as root:
            job=self.run_profile(root)
            self.assertEqual(job['state'],'done',job)
            profile=json.loads((Path(root)/job['profile']/'profile.json').read_text())
            q=profile['quality'];self.assertIn('build_s',q)
            self.assertEqual(set(q['stage_ms']),{'speaker_load','decode_denoise','asr','candidate_scoring','prosody_analysis','worker_load','optional_calibration'})
            self.assertFalse(q['calibration_requested']);self.assertEqual(q['asr'][0]['engine'],'manual-aligned-short-clip')
            self.assertEqual(profile['reference_normalize_dbfs'],-21)
            self.assertEqual(q['embedding_cache']['calls'],1)
            self.assertTrue(all(ms>=0 for ms in q['stage_ms'].values()))

    def test_full_aligned_sixteen_second_manual_clip_is_not_truncated_to_fourteen(self):
        with tempfile.TemporaryDirectory() as root:
            job=self.run_profile(root,duration=16)
            self.assertEqual(job['state'],'done',job)
            profile=json.loads((Path(root)/job['profile']/'profile.json').read_text())
            self.assertEqual(profile['candidates'][0]['end'],16)
            import soundfile as sf
            self.assertEqual(sf.info(str(Path(root)/job['profile']/profile['anchor'])).frames,24000*16)

    def test_invalid_window_timestamps_never_pair_truncated_audio_with_full_text(self):
        with tempfile.TemporaryDirectory() as root:
            segments=[{'start':0.,'end':20.,'text':'全文不能套到前十四秒','logprob':0.,'words':[]}]
            job=self.run_profile(root,duration=20,manual='',segments=segments)
            self.assertEqual(job['state'],'error');self.assertIn('no speech',job['error'])
            self.assertEqual(list(Path(root).iterdir()),[])

if __name__=='__main__':unittest.main()
