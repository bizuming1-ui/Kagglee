"""Packaging checks never run bootstrap installers or import the generated launcher."""
import ast
import base64
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zlib

REPO=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('repack', REPO/'kaggle/repack.py')
repack=importlib.util.module_from_spec(spec);spec.loader.exec_module(repack)

class PackagingTests(unittest.TestCase):
    def test_repack_is_deterministic_and_current(self):
        subprocess.run([sys.executable,str(REPO/'kaggle/repack.py'),'--check'],check=True)

    def test_launcher_roundtrip_extract_only_without_bootstrap(self):
        with tempfile.TemporaryDirectory() as d:
            env={**os.environ,'QTTS_UNPACK_ONLY':'1','QTTS_ROOT':str(Path(d)/'extracted')}
            result=subprocess.run([sys.executable,str(repack.OUTPUT)],cwd=d,env=env,capture_output=True,text=True,timeout=10)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('未安装依赖',result.stdout)
            _,files=repack.source_assignment(repack.OUTPUT.read_text())
            for name,(digest,data) in files.items():
                expected=zlib.decompress(base64.b64decode(data,validate=True))
                actual=(Path(env['QTTS_ROOT'])/name).read_bytes()
                self.assertEqual(actual,expected,name)
                self.assertEqual(actual,(repack.SOURCE/name).read_bytes(),name)
                self.assertEqual(hashlib.sha256(actual).hexdigest(),digest)
            self.assertFalse((Path(env['QTTS_ROOT'])/'state').exists())

    def test_step1_launcher_is_frozen(self):
        manifest=json.loads((REPO/'kaggle/source_manifest.json').read_text())
        raw=(REPO/'kaggle/kaggle-fixed-step1.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),manifest['launcher_sha256'])

    def test_step2_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step2.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'a628d1bf3f320a330d9206b5f1864e4b38a04f0bc04b26028af2e94368f111d0')

    def test_step3_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step3.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'4b69f9adec43487c731c53e7ae65f91534626e71660f1b50b109bfe0c8cb973b')

    def test_step4_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step4.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'069421e5f0d4112148211e1289f91ec7a1b184105e5431fde0c3d72e8c744e27')

    def test_step5_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step5.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'acfa5639324e16aa7dcfe314caef09bee8eb277d59bdd71a5f1f4cffa0a7aaf1')

    def test_step6_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step6.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256')

    def test_step7_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step7.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0')

    def test_step8_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step8.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'777c1d523559c9c734cd5e99841810524284e91269ced23963e8e5ab3f3cc1e1')

    def test_step9_launcher_is_frozen(self):
        raw=(REPO/'kaggle/kaggle-fixed-step9.py').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'8ec892dcc5ca10daf20c8de84dd2be08d9a3de8807872c2051ddf52bd5882a9b')

    def test_step10_launcher_is_frozen(self):
        raw=(REPO/"kaggle/kaggle-fixed-step10.py").read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),"2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4")

    def test_step11_launcher_is_frozen(self):
        self.assertEqual(hashlib.sha256((REPO/"kaggle/kaggle-fixed-step11.py").read_bytes()).hexdigest(),"cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e")

    def test_original_saved_source_still_matches_evidence(self):
        head=json.loads((REPO/'workspace/HEAD.json').read_text())
        original=REPO/'workspace/revisions'/head['revision']/'kaggle'
        self.assertEqual(hashlib.sha256(original.read_bytes()).hexdigest(),repack.ORIGINAL_SHA256)

if __name__=='__main__':unittest.main()
