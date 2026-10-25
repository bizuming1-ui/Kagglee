"""Single-event-loop real TCP combinations, with controlled worker/ASR/model roles.
8 limited protections +4 unfixed observations. No real inference, remote exploit or fix.
"""
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager,ExitStack
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import numpy as np
from input_http_fixture import TCPFixture,analyst,read_json,write_json_atomic,reference_binding
REAL_RELOAD=analyst.load_on_workers
HTTP_CASES=[];OBSERVATIONS=[]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class VersionFixture(TCPFixture):
    def __init__(self,root):
        super().__init__(root);self.worker_calls=[];self.synth_calls=[];self.asr_calls=[];self.release_hook=lambda:None;self.worker_hook=None;self.sim_index=0
    def transport(self,index,path,body,**kwargs):
        prof=analyst.load_profile(body['profile']);pin=reference_binding(analyst.profile_dir(body['profile']),prof) if prof else ''
        self.worker_calls.append({'index':index,'profile':body['profile'],'pin':pin})
        if self.worker_hook:return self.worker_hook(index,path,body,pin)
        return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
    def synth(self,index,pid,text,**kwargs):
        prof=analyst.load_profile(pid);directory=analyst.profile_dir(pid)
        self.synth_calls.append({'profile':pid,'ref_text':prof['ref_text'],'anchor_sha256':digest(directory/prof['anchor'])})
        return np.full(4800,.03,np.float32),{'explicit_fixture_not_model':True}
    def similarity(self,*args):
        value=(.2,.2,.9,.9)[self.sim_index%4];self.sim_index+=1;return value
    def transcribe(self,*args):
        text=analyst.CAL_TEXTS[len(self.asr_calls)%len(analyst.CAL_TEXTS)];self.asr_calls.append(text);return 'zh',[{'text':text}]
    @contextmanager
    def serve_original(self):
        with super().serve():
            with ExitStack() as stack:
                stack.enter_context(patch.object(analyst,'load_on_workers',REAL_RELOAD))
                stack.enter_context(patch.object(analyst,'worker_post',side_effect=self.transport))
                stack.enter_context(patch.object(analyst,'synth_full',side_effect=self.synth))
                stack.enter_context(patch.object(analyst,'to16k',side_effect=lambda a:a))
                stack.enter_context(patch.object(analyst,'SPK',NS(method='ecapa',embed=lambda y:np.array([1.,0.]),sim=self.similarity)))
                stack.enter_context(patch.object(analyst,'ASR',NS(transcribe=self.transcribe,release_after_use=lambda:self.release_hook())))
                yield self
class VersionHTTPBoundaries(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory(prefix='version-http-');self.addCleanup(t.cleanup);self.root=Path(t.name);self.fixtures=[]
    def fixture(self,trained=False):
        f=VersionFixture(self.root/str(len(self.fixtures)));p,prof=f.profile(trained);np.save(p/'centroid.npy',np.array([1.,0.],np.float32));self.fixtures.append(f);return f,p,prof
    def tearDown(self):
        for f in self.fixtures:HTTP_CASES.extend({'test_id':self.id(),**r} for r in f.rows)
    def post(self,f,route,body):return f.post('/profiles/voice/'+route,json.dumps(body))
    def observe(self,key,**facts):OBSERVATIONS.append({'id':key,'fixed':False,'actual_tcp_http':True,'single_uvicorn_event_loop':True,'controlled_interleaving_not_thread_stress':True,'worker_asr_speaker_synth_are_fixtures':True,'actual_model_or_wrong_voice_proven':False,**facts})
    def clean(self,f):
        self.assertFalse(list(f.profiles.glob('_cal_*')))
        self.assertTrue(f.heavy.slots.acquire(False));self.assertTrue(f.heavy.slots.acquire(False));self.assertFalse(f.heavy.slots.acquire(False));f.heavy.slots.release();f.heavy.slots.release()
    def test_protect_serial_candidate_then_text_commits_matching_selected_reference(self):
        f,p,_=self.fixture()
        with f.serve_original():
            self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200)
            self.assertEqual(self.post(f,'text',{'ref_text':'new selected one'}).status_code,200)
        prof=read_json(p/'profile.json');self.assertEqual(prof['anchor_candidate'],1);self.assertEqual(prof['ref_text'],prof['candidates'][1]['text']);self.assertEqual(prof['ref_text'],'new selected one');self.assertEqual(prof['candidates'][0]['text'],'fixture zero');self.assertEqual((p/prof['anchor']).read_bytes(),(p/'cand1.wav').read_bytes());self.clean(f)
    def test_protect_serial_text_then_candidate_keeps_old_candidate_edit_not_mismatched_text(self):
        f,p,_=self.fixture()
        with f.serve_original():
            self.assertEqual(self.post(f,'text',{'ref_text':'edited zero'}).status_code,200)
            self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200)
        prof=read_json(p/'profile.json');self.assertEqual(prof['anchor_candidate'],1);self.assertEqual(prof['ref_text'],'fixture one');self.assertEqual(prof['candidates'][0]['text'],'edited zero');self.clean(f)
    def overlap_guard(self,first,second):
        f,p,_=self.fixture();entered=threading.Event();release=threading.Event();first_thread=[]
        def worker(index,path,body,pin):
            if not first_thread:first_thread.append(threading.get_ident())
            if threading.get_ident()==first_thread[0] and index==0:
                entered.set();self.assertTrue(release.wait(4))
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        f.worker_hook=worker
        with f.serve_original(),ThreadPoolExecutor(max_workers=1) as pool:
            future=pool.submit(self.post,f,*first)
            try:
                self.assertTrue(entered.wait(3));b=self.post(f,*second);self.assertEqual(b.status_code,200)
            finally:release.set()
            a=future.result(timeout=5);self.assertEqual(a.status_code,503);self.assertTrue(a.json()['reference_saved']);self.assertFalse(a.json()['ok'])
        prof=read_json(p/'profile.json');self.assertEqual(prof['anchor_candidate'],1)
        if second[0]=='text':self.assertEqual(prof['ref_text'],'second text');self.assertEqual(prof['candidates'][1]['text'],'second text')
        else:self.assertEqual(prof['ref_text'],'fixture one');self.assertEqual(prof['candidates'][0]['text'],'first text')
        self.clean(f)
    def test_protect_overlapping_candidate_then_text_old_reload_is_503(self):self.overlap_guard(('candidate',{'index':1}),('text',{'ref_text':'second text'}))
    def test_protect_overlapping_text_then_candidate_old_reload_is_503(self):self.overlap_guard(('text',{'ref_text':'first text'}),('candidate',{'index':1}))
    def test_protect_trained_mutations_never_start_calibration_or_worker_reload(self):
        f,p,_=self.fixture(trained=True);before={x.name:x.read_bytes() for x in p.iterdir()}
        with f.serve_original():
            for route,body in (('candidate',{'index':1}),('text',{'ref_text':'x'}),('calibrate',{})):self.assertEqual(self.post(f,route,body).status_code,409)
        self.assertEqual(f.worker_calls,[]);self.assertEqual(f.synth_calls,[]);self.assertEqual({x.name:x.read_bytes() for x in p.iterdir()},before);self.clean(f)
    def test_protect_bad_worker_pin_returns_503_saved_without_claiming_rollback(self):
        f,p,_=self.fixture();f.worker_hook=lambda *a:NS(status_code=200,json=lambda:{'ok':True,'voice_binding':'0'*64})
        with f.serve_original():r=self.post(f,'candidate',{'index':1})
        self.assertEqual(r.status_code,503);self.assertTrue(r.json()['reference_saved']);self.assertFalse(r.json()['ok']);self.assertEqual(read_json(p/'profile.json')['anchor_candidate'],1);self.clean(f)
    def test_protect_stable_calibration_commits_selected_candidate_and_cleans_temps(self):
        f,p,_=self.fixture()
        with f.serve_original():r=self.post(f,'calibrate',{})
        self.assertEqual(r.status_code,200);self.assertEqual(r.json()['chosen'],1);prof=read_json(p/'profile.json');self.assertEqual(prof['calibration'],r.json());self.assertEqual(prof['anchor_candidate'],1);self.assertEqual(prof['ref_text'],'fixture one');self.assertEqual(len(f.synth_calls),4);self.clean(f)
    def test_protect_calibration_evaluation_errors_clean_temp_without_claiming_valid_choice(self):
        f,p,_=self.fixture()
        with f.serve_original(),patch.object(analyst,'synth_full',side_effect=RuntimeError('owned synthetic evaluation error')):r=self.post(f,'calibrate',{})
        self.assertEqual(r.status_code,200);self.assertTrue(all('error' in row for row in r.json()['results']));self.clean(f)
        # Existing all-failed calibration may return chosen0; this contract ONLY protects cleanup.
    def test_observed_two_inflight_mutations_then_429_still_changes_disk(self):
        f,p,_=self.fixture();two=threading.Event();release=threading.Event();lock=threading.Lock();threads=set()
        def worker(index,path,body,pin):
            if index==0:
                with lock:
                    threads.add(threading.get_ident())
                    if len(threads)==2:two.set()
                self.assertTrue(release.wait(4))
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        f.worker_hook=worker;first=threading.Event()
        original=f.worker_hook
        def marked(*args):first.set();return original(*args)
        f.worker_hook=marked
        with f.serve_original(),ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(self.post,f,'candidate',{'index':1})
            try:
                self.assertTrue(first.wait(3));b=pool.submit(self.post,f,'text',{'ref_text':'inflight text'});self.assertTrue(two.wait(3))
                c=self.post(f,'text',{'ref_text':'text despite429'});self.assertEqual(c.status_code,429)
                self.assertEqual(read_json(p/'profile.json')['ref_text'],'text despite429')
                d=self.post(f,'candidate',{'index':0});self.assertEqual(d.status_code,429);self.assertEqual(read_json(p/'profile.json')['anchor_candidate'],0)
            finally:release.set()
            self.assertEqual(a.result(timeout=5).status_code,503);self.assertEqual(b.result(timeout=5).status_code,503)
        self.clean(f);self.observe('S2-TCP-O01',third_text_status=429,fourth_candidate_status=429,final_selected=0,earlier_requests_503=True,disk_mutations_precede_admission_rejection=True)
    def calibration_pause(self,f):
        ready=threading.Event();release=threading.Event()
        def pause():ready.set();self.assertTrue(release.wait(4))
        f.release_hook=pause;return ready,release
    def test_observed_old_calibration_scores_survive_real_candidate_and_text_edits(self):
        f,p,_=self.fixture();ready,release=self.calibration_pause(f)
        with f.serve_original(),ThreadPoolExecutor(max_workers=1) as pool:
            future=pool.submit(self.post,f,'calibrate',{})
            try:
                self.assertTrue(ready.wait(3));self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200);self.assertEqual(self.post(f,'text',{'ref_text':'unassessed new one'}).status_code,200)
            finally:release.set()
            r=future.result(timeout=5);self.assertEqual(r.status_code,200)
        prof=read_json(p/'profile.json');self.assertEqual(prof['ref_text'],'unassessed new one');self.assertEqual(prof['calibration'],r.json());self.assertEqual(r.json()['chosen'],1);self.assertEqual([v['ref_text'] for v in f.synth_calls],['fixture zero']*2+['fixture one']*2);self.clean(f)
        self.observe('S2-TCP-O02',calibration_status=200,candidate_edit_status=200,text_edit_status=200,chosen=1,final_text='unassessed new one',all_assessments_use_old_text=True,old_scores_saved_after_two_real_http_mutations=True)
    def test_observed_same_filename_candidate_bytes_changed_before_calibration_commit(self):
        f,p,_=self.fixture();ready,release=self.calibration_pause(f);old=digest(p/'cand1.wav')
        with f.serve_original(),ThreadPoolExecutor(max_workers=1) as pool:
            future=pool.submit(self.post,f,'calibrate',{})
            try:
                self.assertTrue(ready.wait(3));(p/'cand1.wav').write_bytes((p/'cand0.wav').read_bytes());new=digest(p/'cand1.wav');self.assertNotEqual(old,new)
            finally:release.set()
            r=future.result(timeout=5);self.assertEqual(r.status_code,200)
        prof=read_json(p/'profile.json');self.assertEqual(prof['anchor_candidate'],1);self.assertEqual(digest(p/prof['anchor']),new);self.assertEqual([v['anchor_sha256'] for v in f.synth_calls[2:]],[old,old]);self.clean(f)
        self.observe('S2-TCP-O03',calibration_status=200,chosen=1,assessed_candidate_sha256=old,committed_anchor_sha256=new,filename_unchanged=True,byte_change_is_owned_filesystem_fixture_not_http_upload=True)
    def test_observed_profile_deleted_before_calibration_commit_returns_500_not_conflict(self):
        f,p,_=self.fixture();ready,release=self.calibration_pause(f)
        with f.serve_original(),ThreadPoolExecutor(max_workers=1) as pool:
            future=pool.submit(self.post,f,'calibrate',{})
            try:
                self.assertTrue(ready.wait(3));r=f.client.delete('/profiles/voice');f.rows.append({'path':'/profiles/voice','request_utf8':'','status':r.status_code,'response_text':r.text,'method':'DELETE'});self.assertEqual(r.status_code,200)
            finally:release.set()
            result=future.result(timeout=5);self.assertEqual(result.status_code,500)
        self.assertFalse(p.exists());self.clean(f)
        self.observe('S2-TCP-O04',delete_status=200,calibration_status=500,profile_resurrected=False,temporary_profiles_removed=True,controlled_missing_profile_failure_not_4xx_conflict=True)
if __name__=='__main__':unittest.main(verbosity=2)
