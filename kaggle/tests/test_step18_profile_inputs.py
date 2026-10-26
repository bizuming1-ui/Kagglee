"""Same HTTP contracts against frozen17 (red control) or isolated18 (green candidate).
Workers/models are explicit fixtures; only real analyst routes/IO/admission are under test.
"""
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import input_http_fixture as tcp
import test_version_http_boundaries as version
from qtts_common import read_json, write_json_atomic

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('step18_candidate_analyst', ROOT/'kaggle/step18/analyst.py')
CANDIDATE = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = CANDIDATE
spec.loader.exec_module(CANDIDATE)
TARGET_NAME = os.environ.get('QTTS_S1_TARGET', 'candidate18')
assert TARGET_NAME in ('candidate18', 'frozen17')
TARGET = CANDIDATE if TARGET_NAME == 'candidate18' else tcp.analyst
HTTP_CASES = []

@contextmanager
def serve(fixture):
    # Only the harness module target changes; no frozen production function is modified.
    with patch.object(tcp, 'analyst', TARGET), patch.object(version, 'analyst', TARGET), \
            patch.object(version, 'REAL_RELOAD', TARGET.load_on_workers):
        with fixture.serve_original(): yield fixture

class Step18ProfileInputs(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix='s1-candidate-http-')
        self.addCleanup(tmp.cleanup); self.root = Path(tmp.name); self.fixtures = []
    def fixture(self, trained=False):
        f = version.VersionFixture(self.root/str(len(self.fixtures)))
        directory, prof = f.profile(trained)
        self.fixtures.append(f)
        return f, directory, prof
    def snapshot(self, directory):
        return {str(p.relative_to(directory)): {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in directory.rglob('*') if p.is_file() and not p.is_symlink()}
    def post(self, f, route, body):
        return f.post('/profiles/voice/'+route, json.dumps(body))
    def tearDown(self):
        for f in self.fixtures:
            HTTP_CASES.extend({'test_id':self.id(), 'target':TARGET_NAME, **row} for row in f.rows)
            self.assertFalse(list(f.profiles.glob('_cal_*')))
            self.assertTrue(f.heavy.slots.acquire(False)); self.assertTrue(f.heavy.slots.acquire(False))
            self.assertFalse(f.heavy.slots.acquire(False)); f.heavy.slots.release(); f.heavy.slots.release()
    def invalid(self, route, raws, status=400):
        f, directory, _ = self.fixture(); before = self.snapshot(directory)
        with serve(f):
            for raw in raws:
                with self.subTest(raw=repr(raw)[:120]):
                    response = f.post('/profiles/voice/'+route, raw)
                    self.assertEqual(response.status_code, status)
                    self.assertEqual(self.snapshot(directory), before)
                    self.assertEqual(f.worker_calls, [])
    def test_reject_boolean_index(self): self.invalid('candidate', ['{"index":true}', '{"index":false}'])
    def test_reject_float_index(self): self.invalid('candidate', ['{"index":1.0}', '{"index":1.9}'])
    def test_reject_string_index(self): self.invalid('candidate', ['{"index":"1"}'])
    def test_reject_null_and_container_index(self): self.invalid('candidate', ['{"index":null}', '{"index":[]}', '{"index":{}}'])
    def test_reject_missing_index(self): self.invalid('candidate', ['{}'])
    def test_reject_negative_and_out_of_range_index(self): self.invalid('candidate', ['{"index":-1}', '{"index":2}', '{"index":9999999999999999999999999}'])
    def test_reject_nonfinite_numbers(self):
        self.invalid('candidate', ['{"index":'+x+'}' for x in ('NaN', 'Infinity', '-Infinity', '1e309')])
    def test_reject_duplicate_keys(self):
        self.invalid('candidate', ['{"index":0,"index":1}'])
        self.invalid('text', ['{"ref_text":"first","ref_text":"last"}'])
    def test_reject_unknown_keys(self):
        self.invalid('candidate', ['{"index":1,"typo":1}'])
        self.invalid('text', ['{"ref_text":"new","typo":1}'])
    def test_reject_nonobject_json(self):
        self.invalid('candidate', ['null', '[]', 'true', '0', '"x"', 'NaN', '1e309'])
    def test_reject_malformed_and_invalid_utf8_json(self):
        # Bytes are sent directly rather than round-tripped through the harness UTF-8 recorder.
        f, directory, _ = self.fixture(); before = self.snapshot(directory)
        with serve(f):
            for raw in (b'{', b'{"ref_text":"\xff"}', b'\xff'):
                with self.subTest(raw=raw):
                    r = f.client.post('/profiles/voice/text', content=raw, headers={'Content-Type':'application/json'})
                    f.rows.append({'path':'/profiles/voice/text','request_hex':raw.hex(),'status':r.status_code,'response_text':r.text})
                    self.assertEqual(r.status_code,400); self.assertEqual(self.snapshot(directory),before)
        self.assertEqual(f.worker_calls,[])
    def test_reject_nonstring_text(self):
        self.invalid('text', [json.dumps({'ref_text':v}) for v in (None, True, 2, [], {'x':1})])
    def test_reject_empty_oversized_and_surrogate_text(self):
        self.invalid('text', [json.dumps({'ref_text':v}) for v in ('', '  \n ', 'x'*20001, '\ud800')])
    def test_accept_unicode_and_exact_text_limit(self):
        f,directory,_ = self.fixture()
        with serve(f):
            for value in ('  你好，world！🙂  ', '文'*20000):
                r=self.post(f,'text',{'ref_text':value}); self.assertEqual(r.status_code,200)
                p=read_json(directory/'profile.json'); self.assertEqual(p['ref_text'],value.strip())
                self.assertEqual(p['candidates'][0]['text'],value.strip())
    def test_reject_profile_body_over_byte_budget(self):
        self.invalid('text', [json.dumps({'ref_text':'x'*(128*1024)})], 413)
    def test_accept_candidate_bytes_and_original_worker_pin_guard(self):
        f,directory,_=self.fixture()
        with serve(f): r=self.post(f,'candidate',{'index':1})
        self.assertEqual(r.status_code,200); self.assertTrue(r.json()['reference_saved'])
        p=read_json(directory/'profile.json');self.assertEqual(p['anchor_candidate'],1)
        self.assertEqual((directory/p['anchor']).read_bytes(),(directory/'cand1.wav').read_bytes())
        self.assertEqual(p['ref_text'],'fixture one');self.assertEqual(len(f.worker_calls),2)
    def test_candidate_normalization_updates_both_text_fields(self):
        f,directory,p=self.fixture();p['candidates'][1]['text']='  fixture one  ';write_json_atomic(directory/'profile.json',p)
        with serve(f):r=self.post(f,'candidate',{'index':1})
        self.assertEqual(r.status_code,200);p=read_json(directory/'profile.json')
        self.assertEqual(p['ref_text'],'fixture one');self.assertEqual(p['ref_text'],p['candidates'][1]['text'])
    def test_delete_waits_for_executor_commit_without_resurrecting_profile(self):
        if TARGET_NAME=='frozen17':self.skipTest('new executor/delete coordination contract; frozen writes occur on the event loop')
        f,directory,_=self.fixture();ready=threading.Event();release=threading.Event();delete_entered=threading.Event()
        original_write=TARGET.write_json_atomic;original_delete=TARGET.commit_delete
        def held_write(path,value):
            if Path(path).name=='profile.json' and value.get('anchor_candidate')==1:
                ready.set()
                if not release.wait(5):raise AssertionError('owned commit barrier timeout')
            return original_write(path,value)
        def marked_delete(pid):delete_entered.set();return original_delete(pid)
        with serve(f),patch.object(TARGET,'write_json_atomic',side_effect=held_write),patch.object(TARGET,'commit_delete',side_effect=marked_delete),ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(self.post,f,'candidate',{'index':1})
            try:
                self.assertTrue(ready.wait(4));b=pool.submit(f.client.delete,'/profiles/voice');self.assertTrue(delete_entered.wait(4))
            finally:release.set()
            ar=a.result(timeout=6);br=b.result(timeout=6)
            f.rows.append({'path':'/profiles/voice','method':'DELETE','request_utf8':'','status':br.status_code,'response_text':br.text})
            self.assertIn(ar.status_code,(200,503));self.assertEqual(br.status_code,200)
        self.assertFalse(directory.exists())
    def test_serial_edits_keep_candidate_text_alignment(self):
        for order in ('text-first','candidate-first'):
            with self.subTest(order=order):
                f,directory,_=self.fixture()
                with serve(f):
                    edits=[('text',{'ref_text':'edited'}),('candidate',{'index':1})]
                    if order=='candidate-first':edits.reverse()
                    for route,body in edits:self.assertEqual(self.post(f,route,body).status_code,200)
                p=read_json(directory/'profile.json');self.assertEqual(p['anchor_candidate'],1)
                self.assertEqual(p['ref_text'],p['candidates'][1]['text'])
                self.assertEqual(p['ref_text'],'fixture one' if order=='text-first' else 'edited')
    def test_full_heavy_returns_429_without_any_disk_write(self):
        f,directory,_=self.fixture();before=self.snapshot(directory)
        f.heavy.slots.acquire();f.heavy.slots.acquire()
        try:
            with serve(f):
                for route,body in (('text',{'ref_text':'must not save'}),('candidate',{'index':1})):
                    r=self.post(f,route,body);self.assertEqual(r.status_code,429)
                    self.assertEqual(r.headers['retry-after'],'5');self.assertEqual(self.snapshot(directory),before)
                    self.assertEqual(f.worker_calls,[])
        finally:f.heavy.slots.release();f.heavy.slots.release()
    def test_two_real_inflight_edits_then_429_cannot_write(self):
        f,directory,_=self.fixture();first=threading.Event();two=threading.Event();release=threading.Event();lock=threading.Lock();threads=set()
        def worker(index,path,body,pin):
            if index==0:
                with lock:
                    threads.add(threading.get_ident());first.set()
                    if len(threads)==2:two.set()
                if not release.wait(5):raise AssertionError('owned worker barrier timeout')
            return NS(status_code=200,json=lambda:{'ok':True,'voice_binding':pin})
        f.worker_hook=worker
        with serve(f),ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(self.post,f,'candidate',{'index':1})
            try:
                self.assertTrue(first.wait(4));b=pool.submit(self.post,f,'text',{'ref_text':'accepted second'})
                self.assertTrue(two.wait(4));before=self.snapshot(directory)
                for route,body in (('text',{'ref_text':'rejected third'}),('candidate',{'index':0})):
                    self.assertEqual(self.post(f,route,body).status_code,429)
                    self.assertEqual(self.snapshot(directory),before)
            finally:release.set()
            self.assertEqual(a.result(timeout=6).status_code,503);self.assertEqual(b.result(timeout=6).status_code,200)
        p=read_json(directory/'profile.json');self.assertEqual(p['anchor_candidate'],1);self.assertEqual(p['ref_text'],'accepted second')
    def test_bad_worker_ack_remains_503_reference_saved(self):
        f,directory,_=self.fixture();f.worker_hook=lambda *args:NS(status_code=200,json=lambda:{'ok':True,'voice_binding':'0'*64})
        with serve(f):r=self.post(f,'candidate',{'index':1})
        self.assertEqual(r.status_code,503);self.assertTrue(r.json()['reference_saved']);self.assertFalse(r.json()['ok'])
        self.assertEqual(read_json(directory/'profile.json')['anchor_candidate'],1)
    def test_trained_and_missing_profile_guards(self):
        f,directory,_=self.fixture(trained=True);before=self.snapshot(directory)
        with serve(f):
            for route,body in (('text',{'ref_text':'x'}),('candidate',{'index':1}),('calibrate',{})):
                self.assertEqual(self.post(f,route,body).status_code,409)
            self.assertEqual(f.post('/profiles/missing/text','{"ref_text":"x"}').status_code,404)
            self.assertEqual(f.post('/profiles/missing/candidate','{"index":0}').status_code,404)
        self.assertEqual(self.snapshot(directory),before);self.assertFalse((f.profiles/'missing').exists());self.assertEqual(f.worker_calls,[])
    def test_reject_unsafe_candidate_paths_and_nonregular_files(self):
        for kind in ('parent','symlink','directory'):
            with self.subTest(kind=kind):
                f,directory,p=self.fixture();outside=f.root/'owned.wav';outside.write_bytes((directory/'cand0.wav').read_bytes())
                if kind=='parent':name='../owned.wav'
                else:
                    name='unsafe.wav';path=directory/name
                    if kind=='symlink':path.symlink_to(outside)
                    elif kind=='fifo':os.mkfifo(path)
                    else:path.mkdir()
                p['candidates'][1]['file']=name;write_json_atomic(directory/'profile.json',p);before=self.snapshot(directory)
                with serve(f):r=self.post(f,'candidate',{'index':1})
                self.assertEqual(r.status_code,400);self.assertEqual(self.snapshot(directory),before);self.assertEqual(f.worker_calls,[])
    def test_reject_fifo_candidate_without_blocking(self):
        if TARGET_NAME == 'frozen17':
            self.skipTest('frozen FIFO copy could block the event loop; not executed in red control')
        f,directory,p=self.fixture();os.mkfifo(directory/'pipe.wav')
        p['candidates'][1]['file']='pipe.wav';write_json_atomic(directory/'profile.json',p);before=self.snapshot(directory)
        with serve(f):r=self.post(f,'candidate',{'index':1})
        self.assertEqual(r.status_code,400);self.assertEqual(self.snapshot(directory),before);self.assertEqual(f.worker_calls,[])
    def test_reject_malformed_candidate_metadata(self):
        for rows in (None, {}, [None], [{'file':'cand0.wav','text':None}], [{'file':None,'text':'x'}]):
            with self.subTest(rows=rows):
                f,directory,p=self.fixture();p['candidates']=rows;write_json_atomic(directory/'profile.json',p);before=self.snapshot(directory)
                with serve(f):r=self.post(f,'candidate',{'index':0})
                self.assertEqual(r.status_code,400);self.assertEqual(self.snapshot(directory),before);self.assertEqual(f.worker_calls,[])
    def test_json_commit_failure_preserves_old_files_and_cleans_new_anchor(self):
        f,directory,_=self.fixture();(directory/'anchor_1.wav').write_bytes((directory/'cand0.wav').read_bytes());before=self.snapshot(directory)
        with serve(f),patch.object(TARGET,'write_json_atomic',side_effect=OSError('owned injected commit failure')):
            r=self.post(f,'candidate',{'index':1})
        self.assertEqual(r.status_code,500);self.assertEqual(self.snapshot(directory),before);self.assertEqual(f.worker_calls,[])
    def test_identical_candidate_selection_reuses_immutable_anchor(self):
        f,directory,_=self.fixture()
        with serve(f):
            self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200);before=self.snapshot(directory)
            self.assertEqual(self.post(f,'candidate',{'index':1}).status_code,200)
        self.assertEqual(self.snapshot(directory),before)
        p=read_json(directory/'profile.json');self.assertEqual((directory/p['anchor']).read_bytes(),(directory/'cand1.wav').read_bytes())

if __name__=='__main__':unittest.main(verbosity=2)
