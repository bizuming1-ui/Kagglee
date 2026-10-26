import ast,base64,contextlib,copy,importlib.util,io,json,os,subprocess,sys,tempfile,unittest,zipfile,zlib
from pathlib import Path
from unittest.mock import patch
import build as b
SCRIPT=b.HERE/'artifacts/kaggle-step18-candidate.py'
def module():
 spec=importlib.util.spec_from_file_location('delivery_candidate',SCRIPT);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class Delivery(unittest.TestCase):
 def setUp(self):self.c=module();self.t=tempfile.TemporaryDirectory();self.p=Path(self.t.name)
 def tearDown(self):self.t.cleanup()
 def bad(self,record):
  self.c.FILES={'py/a.py':record}
  with self.assertRaises((ValueError,TypeError,zlib.error)):self.c.decode_files()
 def record(self,raw=b'a'):return {'sha256':b.sha(raw),'bytes':len(raw),'data':base64.b64encode(zlib.compress(raw)).decode()}
 def test_01_all_assets(self):self.assertEqual(len(self.c.decode_files()),58)
 def test_02_exact_single_file(self):self.assertEqual(b.build_bytes()[0],SCRIPT.read_bytes())
 def test_03_zip_deterministic(self):self.assertEqual(b.build_bytes()[1],(b.HERE/'artifacts/kaggle-step18-full-source.zip').read_bytes())
 def test_04_zip_full_source(self):
  with zipfile.ZipFile(b.HERE/'artifacts/kaggle-step18-full-source.zip') as z:
   for n,raw in self.c.decode_files().items():self.assertEqual(z.read('source/'+n),raw)
   self.assertEqual(z.read('kaggle-step18-candidate.py'),SCRIPT.read_bytes())
 def test_05_bad_path(self):
  for n in ('../a','/a','a//b','a\\b','a:evil','a/./b'):
   with self.assertRaises(ValueError):self.c.safe_name(n)
 def test_06_bad_hash(self):d=self.record();d['sha256']='0'*64;self.bad(d)
 def test_07_bad_base64(self):d=self.record();d['data']='not-base64!';self.bad(d)
 def test_08_bool_length(self):d=self.record();d['bytes']=True;self.bad(d)
 def test_09_big_length(self):d=self.record();d['bytes']=self.c.MAX_FILE+1;self.bad(d)
 def test_10_wrong_length(self):d=self.record();d['bytes']=2;self.bad(d)
 def test_11_trailing_compressed(self):d=self.record();d['data']=base64.b64encode(zlib.compress(b'a')+b'junk').decode();self.bad(d)
 def test_12_truncated_compressed(self):d=self.record();d['data']=base64.b64encode(zlib.compress(b'a')[:-2]).decode();self.bad(d)
 def test_13_bounded_expansion(self):d=self.record(b'a'*(3*1024*1024));d['bytes']=1;self.bad(d)
 def test_14_empty_members(self):
  self.c.FILES={}
  with self.assertRaises(ValueError):self.c.decode_files()
 def test_15_member_count(self):
  self.c.FILES={f'f{i}':self.record() for i in range(257)}
  with self.assertRaises(ValueError):self.c.decode_files()
 def test_16_extra_record_key(self):d=self.record();d['secret']='not-public';self.bad(d)
 def test_17_new_tree_exact(self):
  dest=self.c.extract_new(self.p/'new')
  for n,raw in self.c.decode_files().items():self.assertEqual((dest/n).read_bytes(),raw)
 def test_18_existing_preserved(self):
  target=self.p/'existing';target.mkdir();(target/'keep').write_bytes(b'keep')
  with self.assertRaises(FileExistsError):self.c.extract_new(target)
  self.assertEqual((target/'keep').read_bytes(),b'keep')
 def test_19_symlink_target(self):
  (self.p/'link').symlink_to(self.p,target_is_directory=True)
  with self.assertRaises(ValueError):self.c.extract_new(self.p/'link')
 def test_20_symlink_parent(self):
  (self.p/'link').symlink_to(self.p,target_is_directory=True)
  with self.assertRaises(ValueError):self.c.extract_new(self.p/'link'/'new')
 def test_21_missing_parent(self):
  with self.assertRaises(ValueError):self.c.extract_new(self.p/'missing'/'new')
 def test_22_permissions(self):
  root=self.c.extract_new(self.p/'new');self.assertEqual(root.stat().st_mode&0o777,0o700)
  for n in self.c.FILES:self.assertEqual((root/n).stat().st_mode&0o777,0o600)
 def test_23_check_no_side_effects(self):
  with patch.object(self.c,'load_secrets',side_effect=AssertionError),patch.object(self.c.runpy,'run_path',side_effect=AssertionError),contextlib.redirect_stdout(io.StringIO()) as out:self.assertEqual(self.c.main(['--check']),0)
  self.assertEqual(json.loads(out.getvalue())['status'],'source_verified_not_started');self.assertEqual(list(self.p.iterdir()),[])
 def test_24_run_blocked_before_extract(self):
  report={'status':'blocked'}
  with patch.object(self.c,'doctor',return_value=report),patch.object(self.c,'extract_new',side_effect=AssertionError),patch.object(self.c,'load_secrets',side_effect=AssertionError),contextlib.redirect_stdout(io.StringIO()):self.assertEqual(self.c.main(['--run','--destination',str(self.p/'new')]),2)
  self.assertFalse((self.p/'new').exists())
 def inventory(self,text,code=0):
  with patch.dict(os.environ,{'QTTS_MOCK':'0','QTTS_ALLOW_SINGLE_GPU':'0'}),patch.object(self.c.subprocess,'run',return_value=subprocess.CompletedProcess([],code,text,'')):return self.c.doctor()
 def test_25_missing_gpu(self):self.assertEqual(self.inventory('')['status'],'blocked')
 def test_26_one_gpu(self):self.assertEqual(self.inventory('GPU-a, Tesla T4\n')['status'],'blocked')
 def test_27_duplicate_uuid(self):self.assertEqual(self.inventory('GPU-a, Tesla T4\nGPU-a, Tesla T4\n')['status'],'blocked')
 def test_28_wrong_gpu(self):self.assertEqual(self.inventory('GPU-a, NVIDIA A100\nGPU-b, NVIDIA A100\n')['status'],'blocked')
 def test_29_simulated_inventory_not_model_proof(self):
  v=self.inventory('GPU-a, Tesla T4\nGPU-b, Tesla T4\n');self.assertEqual(v['status'],'hardware_visible_runtime_still_unverified');self.assertFalse(v['real_model_executed']);self.assertFalse(v['quality_or_speed_verified'])
 def test_30_mock_real_refused(self):
  with patch.dict(os.environ,{'QTTS_MOCK':'1'}),patch.object(self.c.subprocess,'run',side_effect=FileNotFoundError):self.assertIn('mock_environment_not_allowed',self.c.doctor()['reasons'])
 def test_31_entry_actual_bytes(self):
  data=self.c.decode_files()
  for n,p in b.OVERRIDES.items():self.assertEqual(data[n],(b.R/p).read_bytes())
 def test_32_helpers_actual_bytes(self):
  data=self.c.decode_files()
  for n in b.HELPERS:self.assertEqual(data['py/'+n+'.py'],(b.R/'kaggle/step18'/(n+'.py')).read_bytes())
 def test_33_only_rust_function_changed(self):
  old=ast.parse((b.R/'kaggle/source/py/bootstrap.py').read_bytes());new=ast.parse(self.c.decode_files()['py/bootstrap.py'])
  for tree in (old,new):tree.body=[n for n in tree.body if not (isinstance(n,ast.FunctionDef) and n.name=='build_rust')]
  self.assertEqual(ast.dump(old),ast.dump(new))
 def test_34_training_included(self):
  data=self.c.decode_files()
  for n in ('py/tts_training.py','py/training_job.py','tools/train_tts.py','py/persist.py','web/recorder.js'):self.assertIn(n,data)
 def test_35_no_private_assets(self):
  for p in self.c.FILES:self.assertFalse(any(s in p for s in ('.access-token','state/','training_data/','training_codes/','.env')))
 def test_36_sources_parse(self):
  for n,raw in self.c.decode_files().items():
   if n.endswith('.py'):ast.parse(raw)
if __name__=='__main__':unittest.main(verbosity=2)
