"""Pass2 analysis API contracts: real files/ASGI/admission, explicit model fixtures.
10 protections + 2 OBSERVED_NOT_FIXED cases. No voice/ASR/GPU acceptance.
"""
import asyncio
import copy
import json
from pathlib import Path
import shutil
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import httpx
import numpy as np
import test_reliability
import test_libraries as libraries
import test_step15
import analyst
import worker
from qtts_common import read_json,write_json_atomic
from reference_segments import prepare_segments
from resource_limits import HeavyAdmission
from voice_binding import reference_binding
from fastapi.testclient import TestClient

OBSERVATIONS=[]


class AnalysisBoundaries(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)

    def profile(self):
        directory=self.root/'voice';directory.mkdir()
        analyst.write_wav(directory/'cand0.wav',(.05*np.sin(np.arange(36000)*.05)).astype(np.float32))
        shutil.copy(directory/'cand0.wav',directory/'anchor_0.wav')
        np.save(directory/'centroid.npy',np.array([1.,0.],np.float32))
        prof={'id':'voice','anchor':'anchor_0.wav','anchor_candidate':0,'ref_text':'合成候选转写','language':'Chinese',
              'candidates':[{'file':'cand0.wav','text':'合成候选转写'}]}
        write_json_atomic(directory/'profile.json',prof)
        return directory,prof

    def load(self,pid):return read_json(self.root/pid/'profile.json')

    def test_protect_reload_rejects_http_bad_flags_shapes_and_wrong_pin(self):
        directory,prof=self.profile();pin=reference_binding(directory,prof)
        for code,body in ((503,{'ok':True,'voice_binding':pin}),(200,{'ok':1,'voice_binding':pin}),
                          (200,{'ok':True,'voice_binding':'wrong'}),(200,[]),(200,None)):
            with self.subTest(code=code,body=body),patch.object(analyst,'profile_dir',side_effect=lambda p:self.root/p),patch.object(analyst,'load_profile',side_effect=self.load),patch.object(analyst,'worker_post',return_value=NS(status_code=code,json=lambda:body)):
                result=analyst.load_on_workers('voice')
            self.assertEqual(len(result),len(analyst.WORKERS));self.assertTrue(all(r['ok'] is False for r in result))

    def test_protect_reload_final_reference_change_rejects_all_receipts(self):
        directory,prof=self.profile();pin=reference_binding(directory,prof);calls=[]
        def post(*args,**kwargs):
            calls.append(True)
            changed=dict(prof,ref_text='另一版转写');write_json_atomic(directory/'profile.json',changed)
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        with patch.object(analyst,'profile_dir',side_effect=lambda p:self.root/p),patch.object(analyst,'load_profile',side_effect=self.load),patch.object(analyst,'worker_post',side_effect=post):
            result=analyst.load_on_workers('voice')
        self.assertEqual(len(calls),len(analyst.WORKERS))
        self.assertTrue(all(r=={'ok':False,'error':'reference changed during worker reload'} for r in result))

    def test_protect_nested_duplicate_json_rejected_before_training_preparation(self):
        raw='{"library_id":"x","revision":1,"samples":[{"id":"x","text":"a","text":"b"}],"reference_sample_id":"x","voice_rights_confirmed":true,"single_speaker_confirmed":true}'
        with TestClient(analyst.app) as client,patch.object(analyst.TRAINING_DATA,'prepare') as prepare:
            response=client.post('/training-data',content=raw,headers={'Content-Type':'application/json'})
        self.assertEqual(response.status_code,400);prepare.assert_not_called()

    def test_protect_process_bad_unicode_flag_and_context_never_reserve_library(self):
        with TestClient(analyst.app) as client,patch.object(analyst.LIBRARIES,'begin') as begin:
            for extra in ({'ref_text':'\ud800'},{'calibrate':1},{'anchor_seconds':16.0}):
                raw=json.dumps({'revision':1,'sample_ids':['a'*32],**extra})
                response=client.post('/libraries/'+'b'*32+'/process',content=raw,headers={'Content-Type':'application/json'})
                self.assertEqual(response.status_code,400)
        begin.assert_not_called()

    def test_protect_cpu_lazy_asr_failure_is_not_silently_converted_to_success(self):
        model=analyst.ASRModel();model.name='fixture/cpu-int8';calls=[]
        def segments():
            calls.append('iterator-entered');raise RuntimeError('fixture lazy CPU failure')
            yield  # lazy generator, not a load-time exception
        original=NS(transcribe=lambda *a,**kw:(segments(),NS(language='zh')));model.model=original
        with patch.object(analyst,'MOCK',False),self.assertRaisesRegex(RuntimeError,'fixture lazy CPU failure'):
            model.transcribe(np.ones(16000,np.float32),'zh')
        self.assertEqual(calls,['iterator-entered']);self.assertIs(model.model,original)

    def test_protect_embedding_oversize_result_not_retained_or_reported_as_hit(self):
        calls=[]
        cache=analyst.BuildEmbeddingCache(NS(embed=lambda y:(calls.append(len(y)) or np.ones(4097,np.float32))))
        source=np.arange(60,dtype=np.float64).reshape(10,6)[:,::2]
        first=cache.embed(source);second=cache.embed(source.copy())
        self.assertEqual(calls,[30,30]);self.assertEqual(first.nbytes,16388)
        self.assertIsNot(first,second);self.assertEqual(cache.report()['entries'],0)
        self.assertEqual((cache.report()['calls'],cache.report()['hits']),(2,0))

    def test_protect_quiet_boundary_windows_cover_actual_samples_without_overlap(self):
        audio=np.full(20*16000,.04,np.float32);audio[int(15.2*16000):int(15.3*16000)]=0
        seen=[];progress=[]
        def transcribe(part,language):
            seen.append((part.copy(),language));duration=len(part)/16000
            return 'en',[{'start':0.,'end':duration,'text':f'window {len(seen)}','words':[]}]
        language,out,report=prepare_segments(audio,[{'start':0.,'end':20.,'text':'DO NOT SLICE THIS TEXT','words':[]}],None,transcribe,16,lambda *a:progress.append(a))
        self.assertEqual(language,'en');self.assertEqual([len(a) for a,_ in seen],[244800,75200])
        np.testing.assert_array_equal(np.concatenate([a for a,_ in seen]),audio)
        self.assertEqual([lang for _,lang in seen],[None,'en'])
        self.assertEqual([s['text'] for s in out],['window 1','window 2'])
        self.assertEqual((report['asr_windows'],report['output_segments']),(2,2))
        self.assertEqual(progress,[(1,0.,15.3),(2,15.3,20.)])

    def test_protect_progress_failure_stops_before_window_asr_and_preserves_inputs(self):
        audio=np.ones(20*16000,np.float32)*.02
        segments=[{'start':0.,'end':20.,'text':'原始全文','words':[]}];before=copy.deepcopy(segments)
        with patch.object(analyst.ASR,'transcribe') as transcribe:
            with self.assertRaisesRegex(RuntimeError,'fixture progress stop'):
                prepare_segments(audio,segments,'zh',transcribe,16,progress=lambda *a:(_ for _ in ()).throw(RuntimeError('fixture progress stop')))
        transcribe.assert_not_called();self.assertEqual(segments,before)
        self.assertTrue(np.all(audio==np.float32(.02)))

    def test_protect_long_manual_text_not_forced_onto_asr_candidate_windows(self):
        segments=[{'start':0.,'end':8.,'text':'第一段ASR替身转写','words':[],'logprob':-.1},
                  {'start':8.5,'end':17.,'text':'第二段ASR替身转写','words':[],'logprob':-.1}]
        manual='人工整段文本不能强行配给短候选'
        job=test_step15.BuildCostTests().run_profile(self.root,duration=17,manual=manual,segments=segments)
        self.assertEqual(job['state'],'done',job)
        prof=read_json(self.root/job['profile']/'profile.json');quality=prof['quality']
        self.assertEqual(quality['asr'][0]['manual_text_policy'],'long-manual-not-forced-ASR-timestamps')
        self.assertTrue(all(c['text'] in {s['text'] for s in segments} for c in prof['candidates']))
        self.assertNotEqual(prof['ref_text'],manual);self.assertEqual(quality['reference_context']['source_total_s'],17.)
        self.assertFalse(quality['reference_context']['model_trained'])

    def test_observed_concurrent_calibrations_share_temp_and_clobber_success_receipt(self):
        directory,prof=self.profile();runtime=worker.Worker();runtime.ready=True
        a_synth=threading.Event();b_load=threading.Event();a_done=threading.Event()
        a_ident=[];missing=[];synth_calls=[];tasks=[]
        def worker_post(index,path,body,**kwargs):
            pid=body['profile']
            if pid.startswith('_cal_'):
                if not a_ident:a_ident.append(threading.get_ident())
                elif threading.get_ident()!=a_ident[0]:
                    b_load.set()
                    if not a_done.wait(5):raise AssertionError('first calibration completion deadline')
            try:
                receipt={'ok':True,**runtime.load_profile(pid)}
                return NS(status_code=200,json=lambda:receipt)
            except FileNotFoundError as error:
                missing.append(pid);receipt={'ok':False,'error':str(error)}
                return NS(status_code=500,json=lambda:receipt)
        def synth(*args,**kwargs):
            synth_calls.append(threading.get_ident());a_synth.set()
            if not b_load.wait(5):raise AssertionError('second calibration reload deadline')
            return np.full(4800,.03,np.float32),{'fixture':True}
        spk=NS(method='fixture-not-ecapa',embed=lambda y:np.array([1.,0.]),sim=lambda *a:.9)
        async def experiment():
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=analyst.app),base_url='http://fixture') as client:
                async def first():
                    try:return await client.post('/profiles/voice/calibrate')
                    finally:a_done.set()
                tasks.append(asyncio.create_task(first()))
                try:
                    self.assertTrue(await asyncio.to_thread(a_synth.wait,3))
                    tasks.append(asyncio.create_task(client.post('/profiles/voice/calibrate')))
                    responses=await asyncio.wait_for(asyncio.gather(*tasks),8)
                    return [(r.status_code,r.json()) for r in responses]
                finally:
                    a_done.set();b_load.set()
                    await asyncio.gather(*tasks,return_exceptions=True)
        patches=[patch.object(analyst,'profile_dir',side_effect=lambda p:self.root/p),patch.object(analyst,'load_profile',side_effect=self.load),
            patch.object(worker,'profile_dir',side_effect=lambda p:self.root/p),patch.object(worker,'load_profile',side_effect=self.load),
            patch.object(analyst,'HEAVY',HeavyAdmission(2)),patch.object(analyst,'WORKERS',['fixture-worker']),
            patch.object(analyst,'worker_post',side_effect=worker_post),patch.object(analyst,'synth_full',side_effect=synth),
            patch.object(analyst,'SPK',spk),patch.object(analyst,'ASR',NS(release_after_use=lambda:None)),
            patch.object(analyst,'to16k',side_effect=lambda y:y),patch.object(analyst,'CAL_TEXTS',['合成目标'])]
        for p in patches:p.start()
        try:
            responses=asyncio.run(experiment())
            self.assertEqual([r[0] for r in responses],[200,200])
            first,second=[r[1] for r in responses]
            self.assertGreater(first['results'][0]['score'],-9)
            self.assertEqual(second['results'][0]['score'],-9)
            self.assertIn('not found',second['results'][0]['error'])
            self.assertEqual(missing,['_cal_voice_0']);self.assertEqual(len(synth_calls),1)
            self.assertEqual(self.load('voice')['calibration'],second)
            self.assertFalse(list(self.root.glob('_cal_*')))
            self.assertTrue(analyst.HEAVY.slots.acquire(blocking=False));self.assertTrue(analyst.HEAVY.slots.acquire(blocking=False))
            self.assertFalse(analyst.HEAVY.slots.acquire(blocking=False));analyst.HEAVY.slots.release();analyst.HEAVY.slots.release()
        finally:
            for p in reversed(patches):p.stop()
            for leveler in runtime.levelers.values():leveler.close()
        OBSERVATIONS.append({'id':'F19','fixed':False,'actual_two_asgi_requests_and_heavy_admission':True,
            'original_calibrate_and_mock_worker_load_executed':True,'shared_temp_deleted_by_first_calibration':True,
            'second_reload_missing_profile':True,'successful_receipt_overwritten_by_error_receipt':True,
            'both_http_statuses': [200,200],'model_synthesis_asr_speaker_are_fixtures':True,
            'admission_slots_released':True,'temporary_directories_cleaned':True,'actual_model_or_gpu_executed':False})

    def test_observed_profile_deleted_during_reload_still_reports_success(self):
        directory,prof=self.profile();pin=reference_binding(directory,prof);calls=[]
        def post(*args,**kwargs):
            calls.append(True)
            if directory.exists():shutil.rmtree(directory)
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        with patch.object(analyst,'profile_dir',side_effect=lambda p:self.root/p),patch.object(analyst,'load_profile',side_effect=self.load),patch.object(analyst,'worker_post',side_effect=post):
            result=analyst.load_on_workers('voice');response=analyst.reload_response(result)
        self.assertEqual(len(calls),len(analyst.WORKERS));self.assertFalse(directory.exists())
        self.assertTrue(all(r['ok'] is True for r in result));self.assertEqual(response.status_code,200)
        body=json.loads(response.body);self.assertTrue(body['ok']);self.assertTrue(body['reference_saved'])
        OBSERVATIONS.append({'id':'F20','fixed':False,'original_load_and_reload_response_executed':True,
            'live_profile_deleted_before_final_check':True,'all_reload_receipts_ok':True,'response_http_status':200,
            'response_reference_saved':True,'worker_receipts_are_fixtures':True,'post_delete_synthesis_executed':False,
            'actual_model_or_gpu_executed':False})


class LibraryProcessBoundary(unittest.TestCase):
    setUp=libraries.LibraryAPITests.setUp
    wait_idle=libraries.LibraryAPITests.wait_idle
    create=libraries.LibraryAPITests.create
    uploaded=libraries.LibraryAPITests.uploaded
    process=libraries.LibraryAPITests.process

    def test_protect_invalid_done_profile_cannot_commit_library_success(self):
        row=self.uploaded();before=copy.deepcopy(row['samples'])
        def invalid(job,*args,**kwargs):job.update(state='done',profile='../escape')
        with patch.object(analyst,'build_profile',side_effect=invalid):
            response=self.process(row);self.assertEqual(response.status_code,200,response.text);self.wait_idle()
        job=analyst.JOBS[response.json()['job']]
        self.assertEqual(job['state'],'error');self.assertIn('raw samples retained',job['error'])
        self.assertEqual(self.store.get(row['id'])['samples'],before)
        updated=self.store.add(row['id'],row['revision'],[('extra.wav',b'ab')])
        self.assertEqual(len(updated['samples']),2)  # no leaked library build lease


if __name__=='__main__':unittest.main()
