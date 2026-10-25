"""S2-A real TCP calibration snapshot contracts; no real models or voice-quality proof."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import sys
import threading
import unittest
from unittest.mock import patch
import numpy as np
import test_step18_profile_inputs as s1
from qtts_common import read_json, write_json_atomic
import step18_calibration_state as state

ROOT = Path(__file__).resolve().parents[2]
TARGET_NAME = os.environ.get('QTTS_S2_TARGET', 'candidate18')
assert TARGET_NAME in ('candidate18', 's1-before')
if TARGET_NAME == 's1-before':
    spec=importlib.util.spec_from_file_location('s1_before_calibration_analyst', ROOT/'docs/validation/step18/s2-before/kaggle/step18/analyst.py')
    TARGET=importlib.util.module_from_spec(spec);sys.modules[spec.name]=TARGET;spec.loader.exec_module(TARGET)
else: TARGET=s1.CANDIDATE
HTTP_CASES=[]

@contextmanager
def serve(f):
    with patch.object(s1,'TARGET',TARGET):
        with s1.serve(f):yield f

class Step18CalibrationState(unittest.TestCase):
    def setUp(self):
        import tempfile
        t=tempfile.TemporaryDirectory(prefix='s2-snapshot-http-');self.addCleanup(t.cleanup);self.root=Path(t.name);self.fixtures=[]
    def fixture(self):
        f=s1.version.VersionFixture(self.root/str(len(self.fixtures)));p,prof=f.profile();np.save(p/'centroid.npy',np.array([1.,0.],np.float32));self.fixtures.append(f);return f,p,prof
    def snapshot(self,p):
        return {str(x.relative_to(p)):hashlib.sha256(x.read_bytes()).hexdigest() for x in p.rglob('*') if x.is_file() and not x.is_symlink()}
    def post(self,f,route,body=None,pid='voice'):
        return f.post('/profiles/'+pid+'/'+route,json.dumps(body or {}))
    def tearDown(self):
        for f in self.fixtures:
            HTTP_CASES.extend({'test_id':self.id(),'target':TARGET_NAME,**r} for r in f.rows)
            self.assertFalse(list(f.profiles.glob('_cal_*')))
            self.assertTrue(f.heavy.slots.acquire(False));self.assertTrue(f.heavy.slots.acquire(False));self.assertFalse(f.heavy.slots.acquire(False));f.heavy.slots.release();f.heavy.slots.release()
        self.assertFalse(state._ACTIVE)
    def paused(self,f):
        ready=threading.Event();release=threading.Event();calls=[]
        def hook():
            calls.append(1)
            if len(calls)==1:
                ready.set()
                if not release.wait(6):raise AssertionError('owned ASR release barrier timeout')
        f.release_hook=hook;return ready,release
    def conflict(self,action,check=None):
        f,p,prof=self.fixture();ready,release=self.paused(f)
        with serve(f),ThreadPoolExecutor(max_workers=1) as pool:
            future=pool.submit(self.post,f,'calibrate')
            try:
                self.assertTrue(ready.wait(4));action(f,p,prof);after=self.snapshot(p)
            finally:release.set()
            r=future.result(timeout=6)
        self.assertEqual(r.status_code,409);self.assertEqual(self.snapshot(p),after)
        if p.exists():self.assertNotIn('calibration',read_json(p/'profile.json'))
        if check:check(f,p)
    def test_stable_calibration_commits_receipt_for_assessed_bytes(self):
        f,p,_=self.fixture()
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,200);self.assertEqual(r.json()['chosen'],1)
        self.assertRegex(r.json().get('input_version',''),r'^[a-f0-9]{64}$')
        prof=read_json(p/'profile.json');self.assertEqual(prof['calibration'],r.json());self.assertEqual(prof['ref_text'],'fixture one')
        self.assertEqual((p/prof['anchor']).read_bytes(),(p/'cand1.wav').read_bytes());self.assertEqual(len(f.synth_calls),4)
    def test_real_candidate_and_text_edits_reject_old_scores(self):
        def action(f,p,prof):
            self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200)
            self.assertEqual(self.post(f,'text',{'ref_text':'new unassessed text'}).status_code,200)
        self.conflict(action,lambda f,p:self.assertEqual(read_json(p/'profile.json')['ref_text'],'new unassessed text'))
    def test_real_candidate_edit_rejects_old_scores(self):
        self.conflict(lambda f,p,prof:self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200))
    def test_real_text_edit_rejects_old_scores(self):
        self.conflict(lambda f,p,prof:self.assertEqual(self.post(f,'text',{'ref_text':'new zero'}).status_code,200))
    def test_real_text_aba_is_still_a_version_conflict(self):
        def action(f,p,prof):
            for text in ('intermediate','fixture zero'):self.assertEqual(self.post(f,'text',{'ref_text':text}).status_code,200)
        self.conflict(action)
    def test_real_candidate_aba_is_still_a_version_conflict(self):
        f,p,_=self.fixture()
        with serve(f):
            self.assertEqual(self.post(f,'candidate',{'index':0}).status_code,200)
            start=read_json(p/'profile.json');ready,release=self.paused(f)
            with ThreadPoolExecutor(max_workers=1) as pool:
                future=pool.submit(self.post,f,'calibrate')
                try:
                    self.assertTrue(ready.wait(4))
                    for k in (1,0):self.assertEqual(self.post(f,'candidate',{'index':k}).status_code,200)
                    now=read_json(p/'profile.json');self.assertEqual(now['anchor'],start['anchor']);self.assertEqual(now['ref_text'],start['ref_text'])
                finally:release.set()
                r=future.result(timeout=6)
        self.assertEqual(r.status_code,409);self.assertNotIn('calibration',read_json(p/'profile.json'))
    def test_same_filename_new_candidate_bytes_are_rejected(self):
        self.conflict(lambda f,p,prof:(p/'cand1.wav').write_bytes((p/'cand0.wav').read_bytes()))
    def test_generation_metadata_change_is_rejected(self):
        def action(f,p,prof):prof['gen']={'temperature':.7};write_json_atomic(p/'profile.json',prof)
        self.conflict(action)
    def test_centroid_byte_change_is_rejected(self):
        self.conflict(lambda f,p,prof:np.save(p/'centroid.npy',np.array([0.,1.],np.float32)))
    def test_real_delete_returns_conflict_without_profile_resurrection(self):
        def action(f,p,prof):
            r=f.client.delete('/profiles/voice');f.rows.append({'path':'/profiles/voice','method':'DELETE','request_utf8':'','status':r.status_code,'response_text':r.text});self.assertEqual(r.status_code,200)
        self.conflict(action,lambda f,p:self.assertFalse(p.exists()))
    def test_changed_trained_state_is_rejected(self):
        def action(f,p,prof):prof['trained_adapter']={'owned_fixture':True};write_json_atomic(p/'profile.json',prof)
        self.conflict(action)
    def test_second_calibration_same_profile_returns_409(self):
        f,p,_=self.fixture();ready,release=self.paused(f)
        with serve(f),ThreadPoolExecutor(max_workers=1) as pool:
            a=pool.submit(self.post,f,'calibrate')
            try:
                self.assertTrue(ready.wait(4));b=self.post(f,'calibrate');self.assertEqual(b.status_code,409)
            finally:release.set()
            self.assertEqual(a.result(timeout=6).status_code,200)
        self.assertEqual(len(f.synth_calls),4)
    def test_serial_runs_have_unique_safe_temporary_ids(self):
        f,p,_=self.fixture()
        with serve(f):
            for _ in range(2):self.assertEqual(self.post(f,'calibrate').status_code,200)
        ids=[row['profile'] for row in f.worker_calls if row['profile'].startswith('_cal_')]
        self.assertEqual(len(ids),4);self.assertEqual(len(set(ids)),4)
        self.assertTrue(all(re.fullmatch(r'[a-zA-Z0-9_-]{1,64}',pid) for pid in ids))
    def test_evaluation_uses_captured_bytes_not_later_live_file(self):
        f,p,_=self.fixture();old=hashlib.sha256((p/'cand1.wav').read_bytes()).hexdigest();synth=f.synth;calls=[]
        def change_during_evaluation(*args,**kwargs):
            if not calls:(p/'cand1.wav').write_bytes((p/'cand0.wav').read_bytes())
            calls.append(1);return synth(*args,**kwargs)
        with serve(f),patch.object(TARGET,'synth_full',side_effect=change_during_evaluation):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,409);self.assertEqual([r['anchor_sha256'] for r in f.synth_calls[2:]],[old,old]);self.assertNotIn('calibration',read_json(p/'profile.json'))
    def test_json_commit_failure_preserves_old_state_and_releases_guard(self):
        f,p,_=self.fixture();before=self.snapshot(p);writer=TARGET.write_json_atomic
        def failed_commit(path,value):
            if Path(path)==p/'profile.json':raise OSError('owned final calibration commit failure')
            return writer(path,value)
        with serve(f):
            with patch.object(TARGET,'write_json_atomic',side_effect=failed_commit):r=self.post(f,'calibrate')
            self.assertEqual(r.status_code,500);self.assertEqual(self.snapshot(p),before);self.assertFalse(state._ACTIVE)
            self.assertEqual(self.post(f,'calibrate').status_code,200)
    def test_temp_setup_errors_cleanup_without_claiming_valid_choice(self):
        f,p,_=self.fixture();writer=TARGET.write_json_atomic;released=[];f.release_hook=lambda:released.append(True)
        def fail_temp(path,value):
            if Path(path).parent.name.startswith('_cal_'):raise OSError('owned temporary profile failure')
            return writer(path,value)
        with serve(f),patch.object(TARGET,'write_json_atomic',side_effect=fail_temp):r=self.post(f,'calibrate')
        self.assertEqual(released,[True]);self.assertFalse(list(f.profiles.glob('_cal_*')))
        # Metric/all-failed semantics are intentionally NOT signed off by this cleanup contract.
        if r.status_code==200:self.assertTrue(all('error' in row for row in r.json()['results']))
    def test_asr_release_error_cannot_commit_and_guard_is_reusable(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        def fail_release():raise RuntimeError('owned ASR release failure')
        f.release_hook=fail_release
        with serve(f):
            r=self.post(f,'calibrate');self.assertEqual(r.status_code,500);self.assertEqual(self.snapshot(p),before);self.assertFalse(state._ACTIVE)
            f.release_hook=lambda:None;self.assertEqual(self.post(f,'calibrate').status_code,200)
    def test_snapshot_byte_budget_rejects_before_model_fixture_calls(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        with serve(f),patch.object(state,'MAX_SNAPSHOT_BYTES',8):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,413);self.assertEqual(f.worker_calls,[]);self.assertEqual(f.synth_calls,[]);self.assertEqual(self.snapshot(p),before)
    def test_snapshot_candidate_count_budget_rejects_before_evaluation(self):
        f,p,prof=self.fixture();prof['candidates']=[dict(prof['candidates'][0]) for _ in range(25)];write_json_atomic(p/'profile.json',prof);before=self.snapshot(p)
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,413);self.assertEqual(f.worker_calls,[]);self.assertEqual(self.snapshot(p),before)
    def test_calibration_rejects_unsafe_candidate_path_before_evaluation(self):
        f,p,prof=self.fixture();(f.root/'owned.wav').write_bytes((p/'cand0.wav').read_bytes());prof['candidates'][1]['file']='../owned.wav';write_json_atomic(p/'profile.json',prof);before=self.snapshot(p)
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,400);self.assertEqual(f.worker_calls,[]);self.assertEqual(self.snapshot(p),before)
    def test_identical_selection_is_idempotent_not_a_false_conflict(self):
        f,p,_=self.fixture()
        with serve(f):
            self.assertEqual(self.post(f,'candidate',{'index':0}).status_code,200);start=read_json(p/'profile.json');ready,release=self.paused(f)
            with ThreadPoolExecutor(max_workers=1) as pool:
                a=pool.submit(self.post,f,'calibrate')
                try:
                    self.assertTrue(ready.wait(4));self.assertEqual(self.post(f,'candidate',{'index':0}).status_code,200)
                    self.assertEqual(read_json(p/'profile.json'),start)
                finally:release.set()
                self.assertEqual(a.result(timeout=6).status_code,200)
    def test_distinct_profiles_can_progress_while_one_calibration_is_paused(self):
        f,p,prof=self.fixture();other=f.profiles/'other';shutil.copytree(p,other);prof['id']='other';write_json_atomic(other/'profile.json',prof);ready,release=self.paused(f)
        with serve(f),ThreadPoolExecutor(max_workers=1) as pool:
            a=pool.submit(self.post,f,'calibrate')
            try:
                self.assertTrue(ready.wait(4));b=self.post(f,'calibrate',pid='other');self.assertEqual(b.status_code,200)
            finally:release.set()
            self.assertEqual(a.result(timeout=6).status_code,200)
        self.assertIn('calibration',read_json(other/'profile.json'));self.assertIn('calibration',read_json(p/'profile.json'))

if __name__=='__main__':unittest.main(verbosity=2)
