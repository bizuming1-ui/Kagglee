"""Schema2 provenance and real read-lease lifecycles. Fixture codes ONLY."""
import ast
import base64
import json
import multiprocessing
import os
from pathlib import Path
import select
import shutil
import signal
import subprocess
import sys
import time
import types
import unittest
from unittest.mock import patch
import zlib

import test_training_codes as helpers
import training_codes as tc
from training_data import digest,encode
from resource_limits import UploadRejected

REPO=Path(__file__).resolve().parents[2]
TOOL=REPO/'kaggle/source/tools/encode_training.py'


def frozen_store():
    # Static asset extraction only; do not execute the frozen installer.
    tree=ast.parse((REPO/'kaggle/kaggle-fixed-step8.py').read_text())
    value=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets))
    files=ast.literal_eval(value);sha,data=files['py/training_codes.py'];raw=zlib.decompress(base64.b64decode(data))
    assert digest(raw)==sha
    module=types.ModuleType('frozen_step8_codes');exec(compile(raw,'frozen-step8-training_codes.py','exec'),module.__dict__)
    return module.TrainingCodesStore


def hold(root,limits,did,sha,ready):
    store=tc.TrainingCodesStore(root,limits,free_bytes=0)
    with store.lease(did,sha):ready.set();signal.pause()


def wait_for_cli_lease(process,lock):
    # Non-mutating readiness: probing LOCK_EX ourselves could race the reader.
    deadline=time.monotonic()+6
    while time.monotonic()<deadline and process.poll() is None:
        if lock.exists():
            info=lock.stat();expected=(os.major(info.st_dev),os.minor(info.st_dev),info.st_ino)
            for line in Path('/proc/locks').read_text().splitlines():
                parts=line.split()
                if len(parts)>5 and parts[1]=='FLOCK' and parts[3]=='WRITE':
                    fields=parts[5].split(':')
                    if len(fields)==3 and (int(fields[0],16),int(fields[1],16),int(fields[2]))==expected:return
        time.sleep(.02)
    raise AssertionError('CLI did not hold the pinned code lease before deadline')


class ProvenanceTests(helpers.Fixture,unittest.TestCase):
    def setUp(self):helpers.CodeTests.setUp(self)
    run_codes=helpers.CodeTests.run_codes

    def prepared(self):
        result=self.run_codes();return result,self.codes.root/result['id']

    def repin(self,directory,manifest):
        raw=encode(manifest);(directory/'manifest.json').write_bytes(raw);return digest(raw)

    def test_exact_source_seal_survives_library_and_input_deletion(self):
        origin=self.data.root/self.did;manifest=(origin/'manifest.json').read_bytes();jsonl=(origin/'train_raw.jsonl').read_bytes()
        result,directory=self.prepared()
        self.assertEqual(result['schema'],2);self.assertTrue(result['provenance_verified_now'])
        self.assertEqual((directory/'source/manifest.json').read_bytes(),manifest)
        self.assertEqual((directory/'source/train_raw.jsonl').read_bytes(),jsonl)
        source=json.loads(manifest);self.assertEqual(source['declarations'],{'voice_rights_confirmed':True,'single_speaker_confirmed':True})
        self.assertEqual(source['library_name'],self.library['name']);self.assertEqual(source['source_revision'],self.library['revision'])
        self.lib.remove(self.library['id'],self.library['revision']);self.data.delete(self.did,self.sha)
        verified=self.codes.verify(result['id'],result['manifest_sha256']);self.assertTrue(verified['provenance_verified_now'])
        self.assertEqual(verified['state'],'test_only_codes');self.assertFalse(verified['checks']['training_verified'])

    def test_list_does_not_claim_fresh_provenance_or_disclose_text(self):
        self.prepared();row=self.codes.list()[0]
        self.assertEqual(row['source_provenance_policy'],'sealed-source-v1');self.assertFalse(row['provenance_verified_now'])
        self.assertNotIn('对应第',json.dumps(row,ensure_ascii=False));self.assertNotIn('declarations',row)

    def test_tampered_source_hashes_declarations_and_revision_rejected(self):
        for kind in ('declarations','library','revision','raw','sample_hash','reference'):
            result,directory=self.prepared();source=directory/'source/manifest.json';meta=json.loads(source.read_bytes())
            if kind=='declarations':meta['declarations']['voice_rights_confirmed']=False
            elif kind=='library':meta['library_name']='another source'
            elif kind=='revision':meta['source_revision']+=1
            elif kind=='sample_hash':meta['samples'][0]['source_sha256']='f'*64
            elif kind=='reference':meta['reference_sample_id']=meta['samples'][1]['id']
            else:(directory/'source/train_raw.jsonl').write_bytes(b'{}\n')
            if kind!='raw':source.write_bytes(encode(meta))
            self.reject(409,self.codes.verify,result['id'],result['manifest_sha256'])
            self.codes.delete(result['id'],result['manifest_sha256'])

    def test_missing_or_extra_seal_members_fail_closed(self):
        for member in ('manifest.json','train_raw.jsonl','extra','source-dir'):
            result,directory=self.prepared()
            if member=='extra':(directory/'source/extra').write_bytes(b'bad')
            elif member=='source-dir':shutil.rmtree(directory/'source')
            else:(directory/'source'/member).unlink()
            self.reject(409,self.codes.verify,result['id'],result['manifest_sha256'])
            self.codes.delete(result['id'],result['manifest_sha256'])

    def test_seal_links_and_nested_directories_rejected(self):
        for kind in ('symlink','hardlink','directory'):
            result,directory=self.prepared();path=directory/'source/train_raw.jsonl';outside=self.state/('outside-'+kind)
            path.rename(outside)
            if kind=='symlink':path.symlink_to(outside)
            elif kind=='hardlink':path.hardlink_to(outside)
            else:path.mkdir()
            self.reject(409,self.codes.verify,result['id'],result['manifest_sha256'])
            self.codes.delete(result['id'],result['manifest_sha256'])

    def test_valid_but_unrelated_source_rebinding_rejected(self):
        result,directory=self.prepared();self.lib.remove(self.library['id'],self.library['revision'])
        library,body=self.source();other=self.data.prepare(self.lib,body)
        otherdir=self.data.root/other['id']
        for name in ('manifest.json','train_raw.jsonl'):(directory/'source'/name).write_bytes((otherdir/name).read_bytes())
        m=json.loads((directory/'manifest.json').read_bytes());m['source_id']=other['id'];m['source_manifest_sha256']=other['manifest_sha256']
        pinned=self.repin(directory,m)
        self.reject(409,self.codes.verify,result['id'],pinned)

    def test_rehashed_code_text_cannot_disagree_with_sealed_input(self):
        result,directory=self.prepared();m=json.loads((directory/'manifest.json').read_bytes())
        rows=[json.loads(line) for line in (directory/'train_with_codes.jsonl').read_bytes().split(b'\n') if line]
        rows[0]['text']='替换过的文本';m['samples'][0]['text_sha256']=digest(rows[0]['text'].encode());m['samples'][0]['row_sha256']=digest(encode(rows[0]))
        raw=b''.join(encode(row) for row in rows);(directory/'train_with_codes.jsonl').write_bytes(raw);m['jsonl_sha256']=digest(raw)
        self.reject(409,self.codes.verify,result['id'],self.repin(directory,m))

    def test_rehashed_reference_cannot_disagree_with_source(self):
        result,directory=self.prepared();m=json.loads((directory/'manifest.json').read_bytes())
        rows=[json.loads(line) for line in (directory/'train_with_codes.jsonl').read_bytes().split(b'\n') if line]
        reference=rows[1]['audio']
        for row,sample in zip(rows,m['samples']):row['ref_audio']=reference;sample['row_sha256']=digest(encode(row))
        raw=b''.join(encode(row) for row in rows);(directory/'train_with_codes.jsonl').write_bytes(raw);m['jsonl_sha256']=digest(raw)
        self.reject(409,self.codes.verify,result['id'],self.repin(directory,m))

    def test_frozen_step8_schema1_remains_unchanged_and_unsealed(self):
        old=frozen_store()(self.codes.root,self.limits,free_bytes=0)
        result=old.prepare(self.data,self.did,self.sha,lambda:helpers.fixture_encoder)
        root=self.codes.root/result['id'];before=(root/'manifest.json').read_bytes()
        verified=self.codes.verify(result['id'],result['manifest_sha256'])
        self.assertEqual(verified['schema'],1);self.assertEqual(verified['source_provenance_policy'],'legacy-unsealed')
        self.assertFalse(verified['provenance_verified_now']);self.assertFalse((root/'source').exists())
        self.data.delete(self.did,self.sha)
        with self.codes.lease(result['id'],result['manifest_sha256']) as (_,meta,rows):
            self.assertEqual(meta['schema'],1);self.assertEqual(len(rows),3);self.assertFalse(meta['checks']['training_verified'])
        self.assertEqual((root/'manifest.json').read_bytes(),before)
        self.codes.delete(result['id'],result['manifest_sha256'])

    def test_schema2_cannot_silently_fall_back_when_seal_missing(self):
        result,directory=self.prepared();shutil.rmtree(directory/'source')
        self.reject(409,lambda:self.codes.lease(result['id'],result['manifest_sha256']).__enter__())
        self.codes.delete(result['id'],result['manifest_sha256'])

    def test_seal_size_permissions_and_budget(self):
        result,directory=self.prepared();size=sum(p.stat().st_size for p in directory.rglob('*') if p.is_file())
        self.assertEqual(size,self.codes._size(directory))
        for path in (directory/'source',*(directory/'source').iterdir()):self.assertEqual(path.stat().st_mode&0o777,0o700 if path.is_dir() else 0o600)
        seal=sum(p.stat().st_size for p in (directory/'source').iterdir());self.assertGreater(seal,0)
        self.codes.per_bytes=size-seal;self.reject(409,self.codes.verify,result['id'],result['manifest_sha256'])

    def test_source_write_failure_rolls_back_and_keeps_input(self):
        original=self.codes._write
        def write(path,raw):
            if path.parent.name=='source':raise OSError('injected source archive failure')
            return original(path,raw)
        with patch.object(self.codes,'_write',side_effect=write):
            with self.assertRaises(OSError):self.run_codes()
        self.assertEqual(self.codes.list(),[]);self.assertFalse(list(self.codes.root.glob('.pending-*')))
        self.assertTrue(self.data.verify(self.did,self.sha)['integrity_verified_now'])

    def test_cancel_after_sealing_never_publishes(self):
        original=self.codes._write;stop=[]
        def write(path,raw):
            original(path,raw)
            if path.parent.name=='source' and path.name=='train_raw.jsonl':stop.append(True)
        with patch.object(self.codes,'_write',side_effect=write):self.reject(409,lambda:self.run_codes(cancelled=lambda:bool(stop)))
        self.assertEqual(self.codes.list(),[]);self.assertFalse(list(self.codes.root.glob('.pending-*')))

    def test_read_lease_protects_only_selected_version_and_not_global_list(self):
        a,root=self.prepared();b,_=self.prepared();before=(root/'manifest.json').read_bytes()
        with self.codes.lease(a['id'],a['manifest_sha256']) as (directory,meta,rows):
            self.assertEqual(directory,root);self.assertEqual(len(rows),3);self.assertEqual(meta['state'],'test_only_codes')
            self.reject(409,self.codes.delete,a['id'],a['manifest_sha256'])
            self.reject(409,lambda:self.codes.lease(a['id'],a['manifest_sha256']).__enter__())
            self.assertEqual(len(self.codes.list()),2);self.assertTrue(self.codes.verify(a['id'],a['manifest_sha256'])['provenance_verified_now'])
            self.codes.delete(b['id'],b['manifest_sha256'])
        self.assertEqual((root/'manifest.json').read_bytes(),before);self.assertFalse((root/'.use').exists())
        self.codes.delete(a['id'],a['manifest_sha256'])

    def test_bad_pin_or_bad_files_cannot_leave_a_stuck_lease(self):
        result,root=self.prepared()
        self.reject(409,lambda:self.codes.lease(result['id'],'f'*64).__enter__())
        (root/'source/train_raw.jsonl').unlink()
        self.reject(409,lambda:self.codes.lease(result['id'],result['manifest_sha256']).__enter__())
        self.codes.delete(result['id'],result['manifest_sha256'])

    def test_exception_inside_reader_releases_lease(self):
        result,_=self.prepared()
        with self.assertRaises(RuntimeError):
            with self.codes.lease(result['id'],result['manifest_sha256']):raise RuntimeError('reader failed')
        self.codes.delete(result['id'],result['manifest_sha256'])

    def test_real_process_death_releases_code_read_lease(self):
        result,_=self.prepared();ctx=multiprocessing.get_context('fork');ready=ctx.Event()
        p=ctx.Process(target=hold,args=(self.codes.root,self.limits,result['id'],result['manifest_sha256'],ready));p.start()
        try:
            self.assertTrue(ready.wait(5));self.reject(409,self.codes.delete,result['id'],result['manifest_sha256'])
            self.assertEqual(len(self.codes.list()),1)
        finally:p.kill();p.join(5)
        self.assertFalse(p.is_alive());self.codes.delete(result['id'],result['manifest_sha256'])

    def test_fork_inherited_reader_keeps_lock_after_parent_context_exit(self):
        result,_=self.prepared();ctx=multiprocessing.get_context('fork');ready=ctx.Event()
        def child():ready.set();signal.pause()
        process=None
        try:
            with self.codes.lease(result['id'],result['manifest_sha256']):
                process=ctx.Process(target=child);process.start();self.assertTrue(ready.wait(5))
            self.reject(409,self.codes.delete,result['id'],result['manifest_sha256'])
        finally:
            if process is not None:process.kill();process.join(5)
        self.codes.delete(result['id'],result['manifest_sha256'])

    def cli(self,result,*args):
        return [sys.executable,str(TOOL),'hold-read','--state',str(self.state),'--id',result['id'],'--manifest-sha256',result['manifest_sha256'],*args]

    def test_cli_hold_read_only_receipt_preserves_fixture_state(self):
        result,root=self.prepared();before=(root/'manifest.json').read_bytes()
        done=subprocess.run(self.cli(result,'--seconds','1','--timeout','10'),capture_output=True,text=True,timeout=15)
        self.assertEqual(done.returncode,0,done.stdout+done.stderr);row=json.loads(done.stdout)['result']
        self.assertTrue(row['read_lease_completed']);self.assertEqual(row['state'],'test_only_codes');self.assertFalse(row['training_verified'])
        self.assertNotIn('对应第',done.stdout+done.stderr);self.assertEqual((root/'manifest.json').read_bytes(),before)

    def test_cli_cancel_and_timeout_release_real_reader(self):
        for action in ('cancel','timeout','parent-kill'):
            result,_=self.prepared();p=subprocess.Popen(self.cli(result,'--seconds','30','--timeout','2' if action=='timeout' else '15'),stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            pidfd=None
            try:
                wait_for_cli_lease(p,self.codes.root/('.use-'+result['id']))
                self.reject(409,self.codes.delete,result['id'],result['manifest_sha256'])
                if action=='cancel':p.terminate()
                elif action=='parent-kill':
                    children=Path(f'/proc/{p.pid}/task/{p.pid}/children').read_text().split();self.assertEqual(len(children),1)
                    pidfd=os.pidfd_open(int(children[0]));p.kill()
                stdout,stderr=p.communicate(timeout=10)
                if action=='parent-kill':self.assertTrue(select.select([pidfd],[],[],5)[0])
                else:self.assertEqual(json.loads(stdout)['status'],'cancelled' if action=='cancel' else 'timeout',stdout+stderr)
                self.codes.delete(result['id'],result['manifest_sha256'])
            finally:
                if p.poll() is None:p.kill();p.wait(5)
                if pidfd is not None:os.close(pidfd)
                p.stdout.close();p.stderr.close()

    def test_cli_rejects_unbounded_hold_or_arbitrary_commands(self):
        result,_=self.prepared()
        for extra in (['--seconds','0'],['--seconds','3601'],['--seconds','1','--command','anything']):
            done=subprocess.run(self.cli(result,*extra),capture_output=True,text=True,timeout=5);self.assertEqual(done.returncode,2)


if __name__=='__main__':unittest.main()
