"""7 protections +5 unfixed observation groups through actual loopback TCP, not TestClient.
Original analyst.app, FastAPI/JSON/middleware/routes/files/admission execute.
Profile bytes are owned synthetic fixtures, worker acknowledgments explicit fixtures.
No authenticated Go chain, remote exploit, Qwen/GPU/audio quality or fix signoff.
"""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from input_http_fixture import TCPFixture,analyst,read_json,write_json_atomic,reference_binding
HTTP_CASES=[];OBSERVATIONS=[]
class InputHTTPBoundaries(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory(prefix='input-http-test-');self.addCleanup(t.cleanup);self.root=Path(t.name);self.fixtures=[]
    def fixture(self,trained=False):
        f=TCPFixture(self.root/str(len(self.fixtures)));p,prof=f.profile(trained);self.fixtures.append(f);return f,p,prof
    def tearDown(self):
        for f in self.fixtures:
            HTTP_CASES.extend({'test_id':self.id(),**r} for r in f.rows)
    def snapshot(self,p):return {x.name:x.read_bytes() for x in p.iterdir()}
    def observe(self,key,facts):
        OBSERVATIONS.append({'id':key,'fixed':False,'actual_tcp_http':True,'original_analyst_app':True,'worker_reload_ack_is_fixture':True,'actual_model_executed':False,'actual_go_auth_chain':False,**facts})
    def test_protect_legal_integer_selection_exact_bytes_text_and_binding(self):
        f,p,_=self.fixture()
        with f.serve():
            for k in (1,0):
                response=f.post('/profiles/voice/candidate',json.dumps({'index':k}));self.assertEqual(response.status_code,200)
                row=read_json(p/'profile.json');self.assertEqual(row['anchor_candidate'],k);self.assertEqual(row['ref_text'],f'fixture {"one" if k else "zero"}')
                self.assertEqual((p/row['anchor']).read_bytes(),(p/f'cand{k}.wav').read_bytes());self.assertRegex(reference_binding(p,row),r'^[a-f0-9]{64}$')
        self.assertEqual(f.reloads,['voice','voice'])
    def test_protect_range_and_missing_profile_reject_without_mutation(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        with f.serve():
            for raw in ('{"index":-1}','{"index":2}','{"index":999}'):
                self.assertEqual(f.post('/profiles/voice/candidate',raw).status_code,400)
            self.assertEqual(f.post('/profiles/missing/candidate','{"index":1}').status_code,404)
        self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
    def test_protect_finite_top_level_nonobjects_and_broken_json_are_422(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        with f.serve():
            for raw in ('null','[]','true','17','"text"','{'):
                self.assertEqual(f.post('/profiles/voice/candidate',raw).status_code,422,raw)
        self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
    def test_protect_trained_routes_reject_before_malformed_reference_mutation(self):
        f,p,_=self.fixture(trained=True);before=self.snapshot(p)
        with patch.object(analyst,'calibrate_profile') as cal,f.serve():
            for route,raw in (('candidate','{"index":1.9}'),('text','{"ref_text":{"wrong":"type"}}'),('calibrate','{}')):
                self.assertEqual(f.post('/profiles/voice/'+route,raw).status_code,409)
        self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[]);cal.assert_not_called()
    def test_protect_library_strict_body_rejects_ambiguous_nonfinite_and_fields(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        with patch.object(analyst.LIBRARIES,'create') as create,f.serve():
            for raw in ('{"name":NaN}','{"name":Infinity}','{"name":-Infinity}','NaN','{"name":"x","name":"y"}','{"name":"x","unknown":1}','{}','[]','{'):
                self.assertEqual(f.post('/libraries',raw).status_code,400,raw)
        create.assert_not_called();self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
    def test_protect_legal_unicode_text_and_empty_rejection(self):
        f,p,_=self.fixture();text='合法中文 α 😀'
        with f.serve():
            self.assertEqual(f.post('/profiles/voice/text',json.dumps({'ref_text':' '+text+' '},ensure_ascii=False)).status_code,200)
            row=read_json(p/'profile.json');self.assertEqual(row['ref_text'],text);self.assertEqual(row['candidates'][0]['text'],text)
            before=self.snapshot(p)
            for raw in ('{}','{"ref_text":"   "}'):
                self.assertEqual(f.post('/profiles/voice/text',raw).status_code,400)
            self.assertEqual(self.snapshot(p),before)
        self.assertEqual(f.reloads,['voice'])
    def test_observed_bool_float_and_string_index_are_coerced(self):
        results=[]
        for raw,selected in (('{"index":true}',1),('{"index":false}',0),('{"index":1.9}',1),('{"index":"1"}',1),('{"index":1.0}',1)):
            f,p,_=self.fixture()
            with f.serve():r=f.post('/profiles/voice/candidate',raw)
            self.assertEqual(r.status_code,200);self.assertEqual(read_json(p/'profile.json')['anchor_candidate'],selected);self.assertEqual(f.reloads,['voice'])
            results.append({'raw':raw,'status':r.status_code,'selected':selected})
        self.observe('S1-HTTP-I01',{'cases':results,'strict_integer_validation_not_implemented':True})
    def test_observed_containers_nonfinite_and_nonfinite_top_level_return_500(self):
        results=[]
        for raw in ('{"index":null}','{"index":[]}','{"index":{}}','{"index":"bad"}','{"index":NaN}','{"index":Infinity}','{"index":-Infinity}','{"index":1e309}','NaN','Infinity','-Infinity'):
            f,p,_=self.fixture();before=self.snapshot(p)
            with f.serve():r=f.post('/profiles/voice/candidate',raw)
            self.assertEqual(r.status_code,500,raw);self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
            results.append({'raw':raw,'status':r.status_code,'disk_unchanged':True,'reload_calls':0})
        self.observe('S1-HTTP-I02',{'cases':results,'top_level_nonfinite_not_same_as_nested_int_conversion':True,'uvicorn_real_error_response_not_testclient_raise':True})
    def test_observed_missing_duplicate_and_unknown_fields_have_legacy_policies(self):
        results=[]
        for raw,selected in (('{}',0),('{"index":0,"index":1}',1),('{"index":1,"index":0}',0),('{"index":1,"extra":1}',1)):
            f,p,prof=self.fixture();shutil.copy(p/'cand1.wav',p/'anchor_1.wav');prof.update(anchor='anchor_1.wav',anchor_candidate=1,ref_text='fixture one');write_json_atomic(p/'profile.json',prof)
            with f.serve():r=f.post('/profiles/voice/candidate',raw)
            self.assertEqual(r.status_code,200);self.assertEqual(read_json(p/'profile.json')['anchor_candidate'],selected)
            results.append({'raw':raw,'initial_selected':1,'status':200,'selected':selected})
        self.observe('S1-HTTP-I03',{'cases':results,'missing_defaults_zero_duplicate_last_wins_unknown_ignored':True,'compatibility_policy_not_changed':True})
    def test_observed_nonstring_text_is_stringified_and_surrogate_errors_before_publish(self):
        results=[]
        for value in ({'x':1},[],None,True,1.9):
            f,p,_=self.fixture();raw=json.dumps({'ref_text':value})
            with f.serve():r=f.post('/profiles/voice/text',raw)
            expected=str(value).strip();self.assertEqual(r.status_code,200);self.assertEqual(read_json(p/'profile.json')['ref_text'],expected)
            results.append({'raw':raw,'status':200,'saved_text':expected})
        f,p,_=self.fixture();before=self.snapshot(p)
        with f.serve():r=f.post('/profiles/voice/text','{"ref_text":"\\ud800"}')
        self.assertEqual(r.status_code,500);self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
        self.observe('S1-HTTP-I04',{'cases':results,'surrogate_status':500,'surrogate_keeps_old_file_and_removes_temp':True})
    def test_observed_corrupt_candidate_shape_and_owned_unsafe_file(self):
        results=[]
        for kind,expected in (('empty',400),('null',500),('dict',500),('null-entry',500),('parent-file',200),('symlink-file',200)):
            f,p,prof=self.fixture();external=f.profiles/'owned-outside.wav';external.write_bytes((p/'cand1.wav').read_bytes())
            if kind=='empty':prof['candidates']=[]
            elif kind=='null':prof['candidates']=None
            elif kind=='dict':prof['candidates']={'0':{'file':'cand0.wav','text':'fixture'}}
            elif kind=='null-entry':prof['candidates']=[None]
            elif kind=='parent-file':prof['candidates'][0]['file']='../owned-outside.wav'
            else:
                (p/'owned-link.wav').symlink_to(external);prof['candidates'][0]['file']='owned-link.wav'
            write_json_atomic(p/'profile.json',prof);before=self.snapshot(p)
            with f.serve():r=f.post('/profiles/voice/candidate','{"index":0}')
            self.assertEqual(r.status_code,expected,kind)
            if expected==200:self.assertEqual((p/'anchor_0.wav').read_bytes(),external.read_bytes());self.assertEqual(f.reloads,['voice'])
            else:self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
            results.append({'corrupt_profile_fixture':kind,'status':expected,'copied_owned_external_bytes':expected==200})
        self.observe('S1-HTTP-I05',{'cases':results,'all_files_inside_owned_temporary_fixture':True,'profile_metadata_corruption_preinstalled_not_request_body':True,'public_remote_exploit_or_arbitrary_private_file_read_proven':False,'actual_model_acceptance_of_wav_not_tested':True})
    def test_protect_rejected_indices_do_not_enter_heavy_or_leak_slots(self):
        f,p,_=self.fixture();before=self.snapshot(p)
        self.assertTrue(f.heavy.slots.acquire(False));self.assertTrue(f.heavy.slots.acquire(False))
        try:
            with f.serve():
                for raw,code in (('{"index":2}',400),('{"index":null}',500)):
                    self.assertEqual(f.post('/profiles/voice/candidate',raw).status_code,code)
        finally:f.heavy.slots.release();f.heavy.slots.release()
        self.assertEqual(self.snapshot(p),before);self.assertEqual(f.reloads,[])
        self.assertTrue(f.heavy.slots.acquire(False));self.assertTrue(f.heavy.slots.acquire(False));self.assertFalse(f.heavy.slots.acquire(False));f.heavy.slots.release();f.heavy.slots.release()
if __name__=='__main__':unittest.main(verbosity=2)
