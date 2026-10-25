"""Pass2 local state contracts. Synthetic WAV/fixture codes; no model or remote upload.

The observed test intentionally confirms an UNFIXED original behavior. Its PASS
means reproducibility, NOT snapshot correctness. Candidate function is the original
AST body with explicit worker-reload/admission fixtures; real filesystem/tar IO.
"""
import ast
import asyncio
import copy
import io
import json
import os
from pathlib import Path
import shutil
import struct
import tarfile
import types
import unittest
from unittest.mock import patch

import test_training_codes as helpers
import training_codes as tc
import training_data as td
import access_control as auth
import persist
import qtts_common as common
from resource_limits import UploadRejected

REPO=Path(__file__).resolve().parents[2]
OBSERVATIONS=[]


class StateBoundaries(helpers.Fixture,unittest.TestCase):
    def setUp(self):helpers.CodeTests.setUp(self)
    run_codes=helpers.CodeTests.run_codes

    def unchanged_and_released(self):
        self.assertTrue(self.data.verify(self.did,self.sha)['integrity_verified_now'])
        self.assertEqual(self.lib.get(self.library['id']),self.library)
        self.assertEqual(self.codes.list(),[])
        self.assertFalse(list(self.codes.root.glob('.pending-*')))
        with self.data.lease(self.did,self.sha):pass

    def test_protect_seal_write_failure_cleans_staging_and_source_lease(self):
        original=self.codes._write
        def write(path,raw):
            if path.parent.name=='source' and path.name=='train_raw.jsonl':raise OSError('injected seal IO')
            return original(path,raw)
        with patch.object(self.codes,'_write',side_effect=write),self.assertRaisesRegex(OSError,'injected seal IO'):
            self.run_codes()
        self.unchanged_and_released()
        self.assertTrue(self.run_codes()['provenance_verified_now'])

    def test_protect_publish_rename_failure_keeps_source_and_allows_retry(self):
        with patch.object(tc.os,'rename',side_effect=OSError('injected publish IO')),self.assertRaisesRegex(OSError,'injected publish IO'):
            self.run_codes()
        self.unchanged_and_released()
        self.assertEqual(self.run_codes()['state'],'test_only_codes')

    def test_protect_cancel_after_encoder_return_never_publishes(self):
        stopped=False;calls=[]
        def encoder(x):
            nonlocal stopped
            calls.append(len(x));stopped=True
            return helpers.fixture_encoder(x)
        with self.assertRaises(UploadRejected) as raised:
            self.codes.prepare(self.data,self.did,self.sha,lambda:encoder,cancelled=lambda:stopped)
        self.assertEqual(raised.exception.code,409);self.assertEqual(calls,[36000])
        self.unchanged_and_released()

    def test_protect_adopt_verify_failure_closes_duplicate_not_parent_ofd(self):
        result=self.run_codes();cid=result['id'];pin=result['manifest_sha256']
        with self.codes.lease_with_fd(cid,pin) as (directory,meta,rows,fd):
            source=directory/'source/train_raw.jsonl';before=source.read_bytes()
            source.write_bytes(b'{}\n')
            try:
                self.reject(409,lambda:self.codes.adopt_lease(cid,pin,fd).__enter__())
                os.fstat(fd)  # failure must not close the caller-owned descriptor
            finally:source.write_bytes(before)
            self.reject(409,self.codes.delete,cid,pin)
        self.codes.delete(cid,pin)  # leaked duplicate OFD would still block deletion
        self.assertEqual(self.codes.list(),[])

    def test_protect_detached_codes_remain_fixture_not_permission_to_train(self):
        result=self.run_codes();cid=result['id'];pin=result['manifest_sha256']
        self.lib.remove(self.library['id'],self.library['revision']);self.data.delete(self.did,self.sha)
        with self.codes.lease(cid,pin) as (directory,meta,rows):
            self.assertEqual(meta['engine']['kind'],'test_fixture');self.assertEqual(len(rows),3)
            self.assertEqual(meta['state'],'test_only_codes')
            for key in ('tokenization_executed','tokenization_verified','training_verified','two_rank_execution_verified','inference_verified'):
                self.assertIs(meta['checks'][key],False)
        self.assertTrue(self.codes.verify(cid,pin)['provenance_verified_now'])

    def test_protect_code_frame_rounding_and_strict_plain_integer_bounds(self):
        for frames,count in ((38400,20),(38401,21)):
            good=[[0,2047]+[7]*14 for _ in range(count)]
            self.assertIs(tc.validate_codes(good,frames),good)
            for value in (True,False,-1,2048,1.0,'1'):
                bad=copy.deepcopy(good);bad[0][0]=value
                self.reject(409,tc.validate_codes,bad,frames)
            self.reject(409,tc.validate_codes,good[:-1],frames)

    def test_protect_wav_unknown_odd_chunk_preserves_every_pcm_sample(self):
        original=helpers.wav();body=b'JUNK'+struct.pack('<I',1)+b'X\0'+original[12:]
        raw=b'RIFF'+struct.pack('<I',len(body)+4)+b'WAVE'+body
        canonical,info=td.canonical_wav(raw,240,24000*900)
        self.assertEqual(canonical,original);self.assertEqual(info['frames'],36000)
        self.assertNotEqual(td.digest(raw),td.digest(canonical))
        self.assertEqual(canonical[44:],original[44:])

    def profile(self):
        directory=self.state/'profiles/voice';directory.mkdir(parents=True)
        (directory/'cand0.wav').write_bytes(helpers.wav(hz=440))
        (directory/'cand1.wav').write_bytes(helpers.wav(hz=660))
        shutil.copy(directory/'cand0.wav',directory/'anchor_0.wav')
        meta={'id':'voice','anchor':'anchor_0.wav','anchor_candidate':0,'ref_text':'合成文本零',
              'candidates':[{'file':'cand0.wav','text':'合成文本零'},{'file':'cand1.wav','text':'合成文本一'}]}
        common.write_json_atomic(directory/'profile.json',meta)
        return directory

    def test_protect_pack_scope_excludes_raw_training_and_auth_state(self):
        self.profile()
        for name in ('training_runs','auth'):
            (self.state/name).mkdir();(self.state/name/'excluded').write_text('fixture-only')
        calibration=self.state/'profiles/_cal_fixture';calibration.mkdir();(calibration/'excluded').touch()
        common.write_json_atomic(self.state/'active.json',{'id':'voice'})
        archive=self.state/'out/state.tar.gz'
        with patch.multiple(persist,STATE=self.state,PROFILES_DIR=self.state/'profiles'),patch.object(persist.subprocess,'run',side_effect=AssertionError('remote command forbidden')):
            persist._pack(archive)
        with tarfile.open(archive) as tf:
            names=tf.getnames()
        self.assertIn('active.json',names);self.assertIn('profiles/voice/profile.json',names)
        self.assertTrue(all(n=='active.json' or n=='profiles/voice' or n.startswith('profiles/voice/') for n in names))

    def test_protect_restore_prevalidates_external_existing_symlink_before_any_write(self):
        target=self.state/'restored';outside=self.state/'outside';outside.mkdir()
        (target/'profiles').mkdir(parents=True);(target/'profiles/escape').symlink_to(outside,target_is_directory=True)
        buf=io.BytesIO()
        with tarfile.open(fileobj=buf,mode='w') as tf:
            for name in ('profiles/good/file','profiles/escape/file'):
                row=tarfile.TarInfo(name);row.size=4;tf.addfile(row,io.BytesIO(b'test'))
        buf.seek(0)
        with tarfile.open(fileobj=buf) as tf,self.assertRaises(ValueError):persist.extract_state_members(tf,target)
        self.assertFalse((target/'profiles/good').exists());self.assertFalse((outside/'file').exists())

    def test_protect_default_auth_is_state_scoped_private_and_outside_state(self):
        with patch.dict(os.environ,{},clear=True),patch.object(auth.tempfile,'gettempdir',return_value=str(self.state/'temporary')):
            a=auth.auth_directory(self.state/'state-a');b=auth.auth_directory(self.state/'state-b')
            self.assertNotEqual(a,b);self.assertFalse(a.is_relative_to(self.state/'state-a'))
            token=auth.ensure_access_token(a)
            self.assertEqual(token,auth.ensure_access_token(a));self.assertNotEqual(token,auth.ensure_access_token(b))
            self.assertEqual(a.stat().st_mode&0o777,0o700)
            self.assertEqual((a/auth.TOKEN_FILE).stat().st_mode&0o777,0o600)
            self.assertFalse((self.state/'state-a'/auth.TOKEN_FILE).exists())

    def test_protect_auth_forwarding_exact_local_gateway_only(self):
        # Explicit synthetic token; no provisioning, networking, or secret logging.
        with patch.dict(os.environ,{'QTTS_ACCESS_TOKEN':'x'*40}):
            for url in ('http://localhost:7860/x','http://127.0.0.1:7860/x'):
                self.assertEqual(auth.gateway_headers(url,self.state,7860),{'Authorization':'Bearer '+'x'*40})
            for url in ('http://localhost:7001/x','https://localhost:7860/x','http://localhost:7860@evil.invalid/x','http://evil.invalid:7860/x'):
                self.assertEqual(auth.gateway_headers(url,self.state,7860),{})

    def test_observed_pack_candidate_interleaving_yields_missing_restored_anchor(self):
        directory=self.profile();archive=self.state/'out/state.tar.gz';events=[]
        tree=ast.parse((REPO/'kaggle/source/py/analyst.py').read_bytes())
        node=next(n for n in tree.body if isinstance(n,ast.AsyncFunctionDef) and n.name=='set_candidate')
        node.decorator_list=[]  # registration excluded; original function body unchanged
        async def run(fn,*args):return fn(*args)
        ns={'asyncio':asyncio,'shutil':shutil,'write_json_atomic':common.write_json_atomic,
            'profile_dir':lambda pid:directory,'load_profile':lambda pid:json.loads((directory/'profile.json').read_text()),
            'HEAVY':types.SimpleNamespace(run=run),'load_on_workers':lambda pid:[{'ok':True,'fixture':True}],
            'reload_response':lambda result:{'ok':True,'workers':result}}
        exec(compile(ast.Module(body=[node],type_ignores=[]),'original-set-candidate','exec'),ns)
        original=tarfile.TarFile.addfile
        def addfile(tf,member,stream=None):
            original(tf,member,stream)
            if member.name=='profiles/voice/anchor_0.wav' and not events:
                # tarfile.add already enumerated this directory. Run the actual
                # candidate-switch body before its later profile.json is read.
                response=asyncio.run(ns['set_candidate']('voice',{'index':1}))
                self.assertTrue(response['ok']);events.append('candidate_changed_after_directory_enumeration')
        with patch.multiple(persist,STATE=self.state,PROFILES_DIR=self.state/'profiles'),patch.object(tarfile.TarFile,'addfile',new=addfile):
            persist._pack(archive)
        live=json.loads((directory/'profile.json').read_text())
        self.assertTrue((directory/live['anchor']).exists())
        self.assertEqual((directory/live['anchor']).read_bytes(),(directory/'cand1.wav').read_bytes())
        restored=self.state/'restored'
        with tarfile.open(archive) as tf:
            names=tf.getnames();persist.extract_state_members(tf,restored)
        saved=json.loads((restored/'profiles/voice/profile.json').read_text())
        self.assertEqual(saved,live);self.assertEqual(saved['anchor'],'anchor_1.wav')
        self.assertEqual(len(events),1);self.assertNotIn('profiles/voice/anchor_1.wav',names)
        self.assertFalse((restored/'profiles/voice'/saved['anchor']).exists())
        OBSERVATIONS.append({'id':'F17','fixed':False,'local_pack_and_extract_executed':True,
            'original_candidate_function_ast_executed':True,'worker_reload_is_fixture':True,
            'deterministic_interleaving_not_thread_stress':True,'live_selected_anchor_present':True,
            'restored_profile_references_missing_anchor':True,'remote_kaggle_executed':False,
            'actual_model_executed':False})


if __name__=='__main__':unittest.main()
