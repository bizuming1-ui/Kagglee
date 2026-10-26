"""Third pass reference/API/backup: 10 protections + 2 unfixed witnesses.
Original ASGI routes/HeavyAdmission, CPU threads, files, flock and tar execute.
Model, ASR, speaker, worker-ack roles are explicit fixtures; no Qwen/GPU/voice proof.
"""
import asyncio
from contextlib import contextmanager,ExitStack
import copy
import io
import json
from pathlib import Path
import shutil
import tarfile
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import httpx
import numpy as np
import test_reliability
import test_libraries
import analyst
import persist
import voice_library as library
from qtts_common import read_json,write_json_atomic
from reference_segments import prepare_segments
from resource_limits import HeavyAdmission,UploadRejected
from voice_binding import reference_binding
from fastapi.testclient import TestClient

OBSERVATIONS=[]

class ReferenceBoundaries(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)
        self.profiles=self.root/'profiles';self.profiles.mkdir()

    def profile(self,*,trained=False):
        directory=self.profiles/'voice';directory.mkdir(exist_ok=True)
        for index in (0,1):analyst.write_wav(directory/f'cand{index}.wav',(.05*np.sin(np.arange(36000)*(.05+.01*index))).astype(np.float32))
        shutil.copy(directory/'cand0.wav',directory/'anchor_0.wav')
        np.save(directory/'centroid.npy',np.array([1.,0.],np.float32))
        prof={'id':'voice','anchor':'anchor_0.wav','anchor_candidate':0,'ref_text':'旧候选零转写','language':'Chinese',
              'candidates':[{'file':'cand0.wav','text':'旧候选零转写'},{'file':'cand1.wav','text':'旧候选一转写'}]}
        if trained:prof['trained_adapter']={'fixture':True}
        write_json_atomic(directory/'profile.json',prof);return directory,prof

    @contextmanager
    def runtime(self,heavy=None):
        with ExitStack() as stack:
            stack.enter_context(patch.object(analyst,'PROFILES_DIR',self.profiles))
            stack.enter_context(patch.object(analyst,'profile_dir',side_effect=lambda pid:self.profiles/pid))
            stack.enter_context(patch.object(analyst,'load_profile',side_effect=lambda pid:read_json(self.profiles/pid/'profile.json')))
            stack.enter_context(patch.object(analyst,'HEAVY',heavy or HeavyAdmission(2)))
            yield

    def store(self):return library.LibraryStore(self.root/'libraries',maximum=4,files=4,file_bytes=32,library_bytes=128,total_bytes=512,free_bytes=0)

    def populated(self,store):
        row=store.create('有序原始库');return store.add(row['id'],1,[('a.raw',b'first'),('b.raw',b'second')])

    def test_protect_candidate_copy_failure_does_not_publish_profile_or_reload(self):
        directory,prof=self.profile();before=(directory/'profile.json').read_bytes();pin=reference_binding(directory,prof)
        with self.runtime(),patch.object(analyst.shutil,'copy',side_effect=PermissionError('synthetic copy failure')),patch.object(analyst,'load_on_workers') as reload,TestClient(analyst.app,raise_server_exceptions=False) as client:
            response=client.post('/profiles/voice/candidate',json={'index':1})
        self.assertEqual(response.status_code,500);reload.assert_not_called()
        self.assertEqual((directory/'profile.json').read_bytes(),before);self.assertFalse((directory/'anchor_1.wav').exists())
        self.assertEqual(reference_binding(directory,prof),pin)

    def test_protect_candidate_json_failure_retains_selected_pin_without_claiming_orphan_rollback(self):
        directory,prof=self.profile();before=(directory/'profile.json').read_bytes();pin=reference_binding(directory,prof)
        with self.runtime(),patch.object(analyst,'write_json_atomic',side_effect=OSError('synthetic JSON failure')),patch.object(analyst,'load_on_workers') as reload,TestClient(analyst.app,raise_server_exceptions=False) as client:
            response=client.post('/profiles/voice/candidate',json={'index':1})
        self.assertEqual(response.status_code,500);reload.assert_not_called();self.assertEqual((directory/'profile.json').read_bytes(),before)
        self.assertEqual(reference_binding(directory,prof),pin)
        self.assertEqual((directory/'anchor_1.wav').read_bytes(),(directory/'cand1.wav').read_bytes())
        # Old selection intact, but new orphan is NOT rolled back; not a transaction signoff.

    def test_protect_trained_reference_mutation_routes_reject_before_disk_or_workers(self):
        directory,_=self.profile(trained=True);before={p.name:p.read_bytes() for p in directory.iterdir()}
        with self.runtime(),patch.object(analyst,'load_on_workers') as reload,patch.object(analyst,'calibrate_profile') as calibrate,TestClient(analyst.app) as client:
            for route,body in (('text',{'ref_text':{'wrong':'type'}}),('candidate',{'index':1.9}),('calibrate',{})):
                response=client.post(f'/profiles/voice/{route}',json=body);self.assertEqual(response.status_code,409)
        reload.assert_not_called();calibrate.assert_not_called();self.assertEqual({p.name:p.read_bytes() for p in directory.iterdir()},before)
        # Metadata fixture only; no actual trained model/artifact validation.

    def test_protect_snapshot_baseexception_releases_fd_and_clears_owned_blobs(self):
        store=self.store();row=self.populated(store);held=[]
        with self.assertRaises(KeyboardInterrupt):
            with store.snapshot(row['id'],row['revision'],[row['samples'][0]['id']]) as lease:
                held.append(lease);raise KeyboardInterrupt()
        self.assertIsNone(held[0].file);self.assertEqual(held[0].files,[])
        after=store.add(row['id'],row['revision'],[('c.raw',b'third')]);self.assertEqual(after['revision'],row['revision']+1)

    def test_protect_snapshot_preserves_selection_order_and_foreign_failure_releases(self):
        store=self.store();row=self.populated(store);ids=[s['id'] for s in row['samples']]
        with store.snapshot(row['id'],row['revision'],ids[::-1]) as lease:self.assertEqual(lease.files,[('b.raw',b'second'),('a.raw',b'first')])
        with self.assertRaises(UploadRejected):
            with store.snapshot(row['id'],row['revision'],[ids[0],'f'*32]):self.fail('foreign sample accepted')
        with store.snapshot(row['id'],row['revision'],ids) as lease:self.assertEqual(len(lease.files),2)
        self.assertEqual(store.get(row['id']),row)

    def test_protect_readonly_snapshot_leaves_prepared_result_and_revision_unchanged(self):
        store=self.store();row=self.populated(store);ids=[s['id'] for s in row['samples']]
        lease=store.begin(row['id'],row['revision'],ids,'a'*12);store.finish(lease,{'state':'done','profile':'fixture-profile'})
        directory=store.root/row['id'];before=(directory/'library.json').read_bytes();ready=store.get(row['id'])
        self.assertEqual(ready['state'],'reference_prepared')
        with store.snapshot(row['id'],row['revision'],ids):self.assertTrue(store.get(row['id'])['busy'])
        self.assertEqual((directory/'library.json').read_bytes(),before);self.assertEqual(store.get(row['id']),ready)
        self.assertFalse(ready['training_verified']);self.assertFalse(ready['inference_verified'])

    def test_protect_pack_extract_roundtrip_preserves_reference_binding_and_bytes(self):
        directory,prof=self.profile();pin=reference_binding(directory,prof);(self.root/'active.json').write_text('{"id":"voice"}')
        (self.profiles/'_cal_hidden').mkdir();(self.profiles/'_cal_hidden/secret').write_bytes(b'not backup')
        store=self.store();self.populated(store);archive=self.root/'backup.tar.gz';destination=self.root/'restored'
        with patch.object(persist,'PROFILES_DIR',self.profiles),patch.object(persist,'STATE',self.root):persist._pack(archive)
        with tarfile.open(archive) as tf:
            names=tf.getnames();self.assertFalse(any('_cal_hidden' in n or 'libraries' in n for n in names));persist.extract_state_members(tf,destination)
        restored=destination/'profiles/voice';self.assertEqual(reference_binding(restored,read_json(restored/'profile.json')),pin)
        for p in directory.iterdir():self.assertEqual((restored/p.name).read_bytes(),p.read_bytes())
        self.assertEqual((destination/'active.json').read_bytes(),(self.root/'active.json').read_bytes())
        # Single stable local snapshot only; no remote Kaggle upload or concurrent commit proof.

    def test_protect_archive_late_unsafe_member_cannot_overwrite_existing_active(self):
        for kind in (tarfile.SYMTYPE,tarfile.LNKTYPE,tarfile.FIFOTYPE,tarfile.CHRTYPE):
            destination=self.root/f'out-{kind.decode()}';destination.mkdir();active=destination/'active.json';active.write_bytes(b'old fixture active')
            raw=io.BytesIO()
            with tarfile.open(fileobj=raw,mode='w') as tf:
                first=tarfile.TarInfo('active.json');first.size=3;tf.addfile(first,io.BytesIO(b'new'))
                bad=tarfile.TarInfo('profiles/voice/unsafe');bad.type=kind;bad.linkname='active.json';tf.addfile(bad)
            raw.seek(0)
            with tarfile.open(fileobj=raw) as tf,self.assertRaises(ValueError):persist.extract_state_members(tf,destination)
            self.assertEqual(active.read_bytes(),b'old fixture active');self.assertFalse((destination/'profiles').exists())

    def test_protect_duplicate_delete_revision_is_rejected_before_store_mutation(self):
        with patch.object(analyst.LIBRARIES,'remove_sample') as remove,TestClient(analyst.app) as client:
            response=client.request('DELETE','/libraries/'+'a'*32+'/samples/'+'b'*32,content='{"revision":1,"revision":1}',headers={'Content-Type':'application/json'})
        self.assertEqual(response.status_code,400);remove.assert_not_called()

    def test_protect_24second_word_partition_preserves_coherent_text_and_times_without_asr(self):
        audio=np.zeros(60*16000,np.float32)
        words=[(5.,17.,'第一句'),(17.,29.,'Second '),(29.,41.,'third '),(41.,53.,'第四句')]
        segments=[{'start':5.,'end':53.,'text':''.join(w[2] for w in words),'words':words}];before=copy.deepcopy(segments)
        language,out,report=prepare_segments(audio,segments,'zh',lambda *_:self.fail('unnecessary window ASR'),24)
        self.assertEqual(language,'zh');self.assertEqual([(p['start'],p['end']) for p in out],[(5.,29.),(29.,53.)])
        self.assertEqual([p['text'] for p in out],['第一句Second','third 第四句']);self.assertEqual(report['word_split_segments'],2);self.assertEqual(report['asr_windows'],0)
        self.assertEqual(segments,before);self.assertEqual(sum(len(p['words']) for p in out),4)

    def test_observed_rejected_heavy_admission_already_saved_text_and_candidate(self):
        directory,_=self.profile();heavy=HeavyAdmission(2);entered=[threading.Event(),threading.Event()];release=threading.Event();results=[]
        async def experiment():
            def occupied(index):
                entered[index].set()
                if not release.wait(5):raise AssertionError('owned heavy fixture cleanup deadline')
            tasks=[asyncio.create_task(heavy.run(occupied,i)) for i in range(2)]
            try:
                for event in entered:self.assertTrue(await asyncio.to_thread(event.wait,3))
                async with httpx.AsyncClient(transport=httpx.ASGITransport(app=analyst.app),base_url='http://fixture') as client:
                    for route,body in (('text',{'ref_text':'拒绝请求却保存的新转写'}),('candidate',{'index':1})):
                        _,initial=self.profile();before=reference_binding(directory,initial)
                        response=await client.post(f'/profiles/voice/{route}',json=body)
                        current=read_json(directory/'profile.json');after=reference_binding(directory,current)
                        self.assertEqual(response.status_code,429);self.assertNotIn('reference_saved',response.json());self.assertNotEqual(before,after)
                        if route=='text':self.assertEqual(current['ref_text'],body['ref_text'])
                        else:self.assertEqual((current['anchor_candidate'],current['anchor'],current['ref_text']),(1,'anchor_1.wav','旧候选一转写'));self.assertEqual((directory/'anchor_1.wav').read_bytes(),(directory/'cand1.wav').read_bytes())
                        results.append({'route':route,'status':429,'disk_reference_changed':True,'reference_saved_reported':False})
            finally:
                release.set();await asyncio.wait_for(asyncio.gather(*tasks,return_exceptions=False),5)
        with self.runtime(heavy),patch.object(analyst,'load_on_workers') as reload:asyncio.run(experiment())
        reload.assert_not_called()
        for _ in range(2):self.assertTrue(heavy.slots.acquire(blocking=False))
        for _ in range(2):heavy.slots.release()
        OBSERVATIONS.append({'id':'F33','fixed':False,'actual_original_asgi_and_heavy_admission':True,'occupied_by_two_owned_cpu_threads':True,
            'cases':results,'worker_reload_called':False,'threads_and_slots_released':True,'actual_model_or_wrong_voice_proven':False})

    def test_observed_calibration_commits_old_scores_after_actual_text_edit(self):
        directory,initial=self.profile();before=reference_binding(directory,initial);seen=[];edits=[];asr_calls=[]
        def post(index,path,body,**kwargs):
            prof=analyst.load_profile(body['profile']);pin=reference_binding(analyst.profile_dir(body['profile']),prof)
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        def synth(index,pid,text,**kwargs):
            prof=analyst.load_profile(pid);seen.append({'pid':pid,'ref_text':prof['ref_text'],'pin':reference_binding(analyst.profile_dir(pid),prof)})
            return np.full(4800,.03,np.float32),{'fixture_not_model':True}
        def transcribe(*args):
            text=analyst.CAL_TEXTS[len(asr_calls)%len(analyst.CAL_TEXTS)];asr_calls.append(text);return 'zh',[{'text':text}]
        with self.runtime(),patch.object(analyst,'MOCK',False),patch.object(analyst,'worker_post',side_effect=post),patch.object(analyst,'synth_full',side_effect=synth),patch.object(analyst,'to16k',side_effect=lambda a:a),patch.object(analyst,'SPK',NS(method='fixture-no-model',embed=lambda y:np.array([1.,0.]),sim=lambda *a:.9)),TestClient(analyst.app) as client:
            def edit():
                response=client.post('/profiles/voice/text',json={'ref_text':'评分后提交前修改的转写'})
                self.assertEqual(response.status_code,200);edits.append(response.json())
            with patch.object(analyst,'ASR',NS(transcribe=transcribe,release_after_use=edit)):
                response=client.post('/profiles/voice/calibrate')
        self.assertEqual(response.status_code,200);self.assertEqual(len(edits),1);self.assertEqual(len(seen),4);self.assertEqual(len(asr_calls),4)
        self.assertEqual([r['ref_text'] for r in seen],['旧候选零转写']*2+['旧候选一转写']*2)
        self.assertTrue(all(row['pin']==before for row in seen[:2]))
        final=read_json(directory/'profile.json');self.assertNotEqual(reference_binding(directory,final),before)
        self.assertEqual(final['ref_text'],'评分后提交前修改的转写');self.assertEqual(final['candidates'][0]['text'],final['ref_text'])
        self.assertEqual(final['calibration'],response.json());self.assertEqual(final['calibration']['chosen'],0)
        self.assertFalse(list(self.profiles.glob('_cal_*')))
        OBSERVATIONS.append({'id':'F34','fixed':False,'actual_original_calibrate_and_text_asgi':True,'text_edit_http_status':200,'calibration_http_status':200,
            'candidate_reference_changed_before_score_commit':True,'all_four_evaluation_calls_used_old_candidate_texts':True,
            'chosen_candidate':0,'stale_calibration_saved_on_changed_profile':True,'temporary_profiles_removed':True,
            'model_asr_speaker_and_worker_ack_are_fixtures':True,'actual_voice_quality_or_wrong_voice_proven':False})


if __name__=='__main__':unittest.main()
