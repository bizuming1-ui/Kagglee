"""S2-B real TCP metric/selection/readiness contracts; all model roles are fixtures."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import numpy as np
import test_step18_calibration_state as s2
from qtts_common import read_json, write_json_atomic

ROOT=Path(__file__).resolve().parents[2]
TARGET_NAME=os.environ.get('QTTS_S2B_TARGET','candidate18')
assert TARGET_NAME in ('candidate18','s2a-before')
if TARGET_NAME=='s2a-before':
    spec=importlib.util.spec_from_file_location('s2a_before_validity_analyst',ROOT/'docs/validation/step18/s2b-before/kaggle/step18/analyst.py')
    TARGET=importlib.util.module_from_spec(spec);sys.modules[spec.name]=TARGET;spec.loader.exec_module(TARGET)
else:TARGET=s2.s1.CANDIDATE
HTTP_CASES=[]
@contextmanager
def serve(f):
    with patch.object(s2.s1,'TARGET',TARGET):
        with s2.s1.serve(f):yield f

class Step18CalibrationValidity(unittest.TestCase):
    setUp=s2.Step18CalibrationState.setUp
    fixture=s2.Step18CalibrationState.fixture
    snapshot=s2.Step18CalibrationState.snapshot
    post=s2.Step18CalibrationState.post
    def tearDown(self):
        for f in self.fixtures:
            HTTP_CASES.extend({'test_id':self.id(),'target':TARGET_NAME,**row} for row in f.rows)
            self.assertFalse(list(f.profiles.glob('_cal_*')))
            self.assertTrue(f.heavy.slots.acquire(False));self.assertTrue(f.heavy.slots.acquire(False));self.assertFalse(f.heavy.slots.acquire(False));f.heavy.slots.release();f.heavy.slots.release()
        self.assertFalse(s2.state._ACTIVE)
    def rejected(self,f,p,response,before):
        self.assertEqual(response.status_code,422);body=response.json()
        self.assertIsNone(body['chosen']);self.assertFalse(body['reference_saved']);self.assertFalse(body['ready']);self.assertFalse(body['quality_verified'])
        self.assertEqual(self.snapshot(p),before)
        for row in body['results']:self.assertIsNone(row['score']);self.assertFalse(row['eligible'])
        return body
    def test_complete_trials_choose_valid_candidate_without_quality_claim(self):
        f,p,_=self.fixture()
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,200);body=r.json();self.assertEqual(body['chosen'],1)
        self.assertIn('selection_valid',body)
        self.assertTrue(body['selection_valid']);self.assertFalse(body['quality_verified']);self.assertEqual(body['valid_candidates'],2)
        self.assertEqual(read_json(p/'profile.json')['calibration'],body)
        for row in body['results']:
            self.assertEqual(row['expected_trials'],2);self.assertEqual(row['valid_trials'],2);self.assertEqual(row['coverage'],1)
            self.assertTrue(row['eligible']);self.assertEqual([t['seed'] for t in row['trials']],[11,12])
            self.assertTrue(all(t['sample_count']==4800 and t['duration_s']==.2 for t in row['trials']))
    def test_asr_all_failure_has_null_cer_no_choice_no_save(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        def unavailable(*args):raise RuntimeError('OWNED_PRIVATE_ASR_SECRET')
        f.transcribe=unavailable
        with serve(f):r=self.post(f,'calibrate')
        body=self.rejected(f,p,r,before);self.assertNotIn('OWNED_PRIVATE',r.text)
        for row in body['results']:
            self.assertIsNone(row['cer']);self.assertEqual(row['asr_trials'],0)
            self.assertTrue(all(t['cer'] is None for t in row['trials']))
    def test_partial_asr_coverage_never_becomes_complete_score(self):
        f,p,_=self.fixture();before=self.snapshot(p);calls=[]
        def partial(*args):
            calls.append(1)
            if len(calls)%2:raise RuntimeError('owned missing trial')
            return 'zh',[{'text':TARGET.CAL_TEXTS[1]}]
        f.transcribe=partial
        with serve(f):r=self.post(f,'calibrate')
        body=self.rejected(f,p,r,before)
        for row in body['results']:
            self.assertEqual(row['expected_trials'],2);self.assertEqual(row['valid_trials'],1);self.assertEqual(row['coverage'],.5)
            self.assertEqual(row['asr_trials'],1);self.assertEqual(row['cer'],0)
    def test_incomplete_high_similarity_cannot_beat_complete_candidate(self):
        f,p,_=self.fixture();calls=[]
        def partial(*args):
            calls.append(1)
            if len(calls)==1:raise RuntimeError('owned missing first trial')
            return 'zh',[{'text':TARGET.CAL_TEXTS[(len(calls)-1)%2]}]
        f.transcribe=partial;values=iter((.99,.99,.2,.2));f.similarity=lambda *a:next(values)
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,200);self.assertEqual(r.json()['chosen'],1);self.assertIsNone(r.json()['results'][0]['score']);self.assertFalse(r.json()['results'][0]['eligible'])
    def test_empty_asr_hypothesis_is_missing_not_measured_success(self):
        for segments in ([],[{'text':'  '}],[{'text':None}]):
            with self.subTest(segments=segments):
                f,p,_=self.fixture();before=self.snapshot(p);f.transcribe=lambda *a,segments=segments:('zh',segments)
                with serve(f):r=self.post(f,'calibrate')
                body=self.rejected(f,p,r,before);self.assertTrue(all(row['cer'] is None for row in body['results']))
    def test_all_synthesis_failure_preserves_existing_calibration_and_anchor(self):
        f,p,prof=self.fixture();prof['calibration']={'chosen':0,'owned_prior_receipt':True};write_json_atomic(p/'profile.json',prof);before=self.snapshot(p)
        with serve(f),patch.object(TARGET,'synth_full',side_effect=RuntimeError('OWNED_PRIVATE_SYNTH_SECRET')):r=self.post(f,'calibrate')
        self.rejected(f,p,r,before);self.assertEqual(read_json(p/'profile.json')['calibration'],prof['calibration']);self.assertNotIn('OWNED_PRIVATE',r.text)
    def test_one_failed_candidate_does_not_prevent_valid_selection(self):
        f,p,_=self.fixture();original=f.synth
        def synth(index,pid,text,**kw):
            if read_json(f.profiles/pid/'profile.json')['ref_text']=='fixture zero':raise RuntimeError('owned failed candidate0')
            return original(index,pid,text,**kw)
        with serve(f),patch.object(TARGET,'synth_full',side_effect=synth):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,200);self.assertEqual(r.json()['chosen'],1);self.assertIsNone(r.json()['results'][0]['score']);self.assertEqual(r.json()['results'][0]['valid_trials'],0)
    def test_nonfinite_similarity_cannot_enter_ranking(self):
        for value in (float('nan'),float('inf'),-float('inf')):
            with self.subTest(value=str(value)):
                f,p,_=self.fixture();before=self.snapshot(p);f.similarity=lambda *a,value=value:value
                with serve(f):r=self.post(f,'calibrate')
                body=self.rejected(f,p,r,before);self.assertTrue(all(row['sim'] is None for row in body['results']))
    def test_nonfinite_cer_cannot_enter_ranking(self):
        for value in (float('nan'),float('inf')):
            with self.subTest(value=str(value)):
                f,p,_=self.fixture();before=self.snapshot(p)
                with serve(f),patch.object(TARGET,'cer',return_value=value):r=self.post(f,'calibrate')
                body=self.rejected(f,p,r,before);self.assertTrue(all(row['cer'] is None for row in body['results']))
    def test_unverified_speaker_backend_is_not_a_reliable_metric(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        with serve(f),patch.object(TARGET.SPK,'method','mfcc-proxy'):r=self.post(f,'calibrate')
        body=self.rejected(f,p,r,before);self.assertTrue(all(row['sim'] is None for row in body['results']))
    def test_missing_centroid_is_not_a_measured_zero_similarity(self):
        f,p,_=self.fixture();(p/'centroid.npy').unlink();before=self.snapshot(p)
        with serve(f):r=self.post(f,'calibrate')
        body=self.rejected(f,p,r,before);self.assertTrue(all(row['sim'] is None for row in body['results']))
    def test_invalid_centroid_is_reported_unavailable_without_saving(self):
        for kind in ('nan','malformed'):
            with self.subTest(kind=kind):
                f,p,_=self.fixture()
                if kind=='nan':np.save(p/'centroid.npy',np.array([np.nan,0.]))
                else:(p/'centroid.npy').write_bytes(b'owned invalid numpy')
                before=self.snapshot(p)
                with serve(f):r=self.post(f,'calibrate')
                self.rejected(f,p,r,before)
    def test_invalid_pcm_is_rejected_before_fake_asr(self):
        waves=[np.array([],np.float32),np.array([np.nan]),np.array([np.inf]),np.zeros((2,100)),np.zeros(4800),np.full(4800,1.5),np.array([1j]),np.array([-32768],np.int16)]
        for index,wave in enumerate(waves):
            with self.subTest(wave=index):
                f,p,_=self.fixture();before=self.snapshot(p)
                with serve(f),patch.object(TARGET,'synth_full',return_value=(wave,{})):r=self.post(f,'calibrate')
                self.rejected(f,p,r,before);self.assertEqual(f.asr_calls,[])
    def test_bad_temporary_worker_pin_never_runs_synthesis(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        f.worker_hook=lambda *a:NS(status_code=200,json=lambda:{'ok':True,'voice_binding':'0'*64})
        with serve(f):r=self.post(f,'calibrate')
        self.rejected(f,p,r,before);self.assertEqual(f.synth_calls,[])
    def test_bad_temporary_worker_http_status_never_runs_synthesis(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        f.worker_hook=lambda i,path,body,pin:NS(status_code=503,json=lambda:{'ok':True,'voice_binding':pin})
        with serve(f):r=self.post(f,'calibrate')
        self.rejected(f,p,r,before);self.assertEqual(f.synth_calls,[])
    def test_final_worker_failure_returns_saved_but_not_ready(self):
        f,p,_=self.fixture()
        def worker(i,path,body,pin):
            if body['profile']=='voice' and i==1:raise RuntimeError('OWNED_PRIVATE_WORKER_SECRET')
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        f.worker_hook=worker
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,503);body=r.json();self.assertTrue(body['reference_saved']);self.assertFalse(body['ready']);self.assertNotIn('OWNED_PRIVATE',r.text)
        self.assertEqual(body['chosen'],1);self.assertEqual(read_json(p/'profile.json')['anchor_candidate'],1)
        self.assertEqual([w['ok'] for w in body['workers']],[True,False])
    def test_empty_final_worker_receipt_is_not_ready(self):
        f,p,_=self.fixture()
        with serve(f),patch.object(TARGET,'load_on_workers',return_value=[]):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,503);self.assertTrue(r.json()['reference_saved']);self.assertFalse(r.json()['ready']);self.assertEqual(len(r.json()['workers']),2)
    def test_final_reload_exception_is_sanitized_partial_failure(self):
        f,p,_=self.fixture()
        with serve(f),patch.object(TARGET,'load_on_workers',side_effect=RuntimeError('OWNED_PRIVATE_RELOAD_SECRET')):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,503);self.assertTrue(r.json()['reference_saved']);self.assertFalse(r.json()['ready']);self.assertNotIn('OWNED_PRIVATE',r.text)
    def final_reload_mutation(self,delete=False):
        f,p,_=self.fixture();ready=threading.Event();release=threading.Event();owner=[]
        def worker(i,path,body,pin):
            if body['profile']=='voice' and i==0:
                if not owner:owner.append(threading.get_ident())
                if threading.get_ident()==owner[0]:
                    ready.set()
                    if not release.wait(6):raise AssertionError('owned reload barrier timeout')
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        f.worker_hook=worker
        with serve(f),ThreadPoolExecutor(max_workers=1) as pool:
            a=pool.submit(self.post,f,'calibrate')
            try:
                self.assertTrue(ready.wait(4))
                if delete:
                    b=f.client.delete('/profiles/voice');f.rows.append({'path':'/profiles/voice','method':'DELETE','request_utf8':'','status':b.status_code,'response_text':b.text})
                else:b=self.post(f,'text',{'ref_text':'new text during final reload'})
                self.assertEqual(b.status_code,200)
            finally:release.set()
            r=a.result(timeout=6)
        self.assertEqual(r.status_code,503);self.assertTrue(r.json()['reference_saved']);self.assertFalse(r.json()['ready'])
        if delete:self.assertFalse(p.exists())
        else:self.assertEqual(read_json(p/'profile.json')['ref_text'],'new text during final reload')
    def test_real_edit_during_final_reload_is_not_ready(self):self.final_reload_mutation()
    def test_real_delete_during_final_reload_is_not_ready(self):self.final_reload_mutation(True)
    def test_generic_calibration_error_does_not_echo_private_exception(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        def secret():raise RuntimeError('OWNED_PRIVATE_RELEASE_SECRET')
        f.release_hook=secret
        with serve(f):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,500);self.assertNotIn('OWNED_PRIVATE',r.text);self.assertEqual(self.snapshot(p),before)
    def test_serial_failure_can_retry_and_then_choose_valid_candidate(self):
        f,p,_=self.fixture();original=f.transcribe
        def fail(*a):raise RuntimeError('owned temporary ASR outage')
        with serve(f):
            with patch.object(TARGET.ASR,'transcribe',side_effect=fail):r=self.post(f,'calibrate')
            self.assertEqual(r.status_code,422);self.assertNotIn('calibration',read_json(p/'profile.json'))
            self.assertEqual(self.post(f,'calibrate').status_code,200)
    def test_json_commit_failure_still_keeps_prior_files(self):
        f,p,_=self.fixture();before=self.snapshot(p);writer=TARGET.write_json_atomic
        def fail(path,value):
            if Path(path)==p/'profile.json':raise OSError('OWNED_PRIVATE_COMMIT_SECRET')
            return writer(path,value)
        with serve(f),patch.object(TARGET,'write_json_atomic',side_effect=fail):r=self.post(f,'calibrate')
        self.assertEqual(r.status_code,500);self.assertEqual(self.snapshot(p),before);self.assertNotIn('OWNED_PRIVATE',r.text)

if __name__=='__main__':unittest.main(verbosity=2)
