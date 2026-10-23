"""Real synthetic PCM16 WAV/file/API tests; NO Qwen, rank or optimizer run."""
from dataclasses import replace
import io
import json
import os
from pathlib import Path
import shutil
import struct
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
import wave

ROOT=Path(__file__).resolve().parents[1]/'source'
TEMP=tempfile.TemporaryDirectory(prefix='qtts-training-env-')
os.environ.setdefault('QTTS_STATE',TEMP.name);os.environ.setdefault('QTTS_MOCK','1')
sys.path.insert(0,str(ROOT/'py'))
import numpy as np
import persist
import analyst
import training_data as td
from voice_library import LibraryStore
from resource_limits import UploadLimits, UploadRejected, HeavyAdmission
from fastapi.testclient import TestClient


def wav(seconds=1.5,hz=440,sr=24000,channels=1,constant=False):
    x=np.zeros(int(sr*seconds),dtype='<i2') if constant else (np.sin(np.arange(int(sr*seconds))*2*np.pi*hz/sr)*10000).astype('<i2')
    if channels>1:x=np.repeat(x[:,None],channels,axis=1)
    out=io.BytesIO()
    with wave.open(out,'wb') as stream:
        stream.setnchannels(channels);stream.setsampwidth(2);stream.setframerate(sr);stream.writeframes(x.tobytes())
    return out.getvalue()


class Fixture:
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.state=Path(self.temp.name);self.limits=UploadLimits()
        self.lib=LibraryStore(self.state/'libraries',free_bytes=0)
        self.data=td.TrainingDataStore(self.state/'training_data',self.limits,free_bytes=0)

    def source(self,payloads=None):
        payloads=payloads or [wav(hz=440),wav(hz=550),wav(hz=660)]
        row=self.lib.create('自己的训练素材')
        row=self.lib.add(row['id'],row['revision'],[(f'{index}.wav',raw) for index,raw in enumerate(payloads)])
        body={'library_id':row['id'],'revision':row['revision'],'samples':[{'id':s['id'],'text':f'对应第{index}段的文本。'} for index,s in enumerate(row['samples'])],
              'reference_sample_id':row['samples'][0]['id'],'voice_rights_confirmed':True,'single_speaker_confirmed':True}
        return row,body

    def reject(self,code,fn,*args):
        with self.assertRaises(UploadRejected) as raised:fn(*args)
        self.assertEqual(raised.exception.code,code)


class TrainingStorageTests(Fixture,unittest.TestCase):
    def test_real_wav_export_jsonl_provenance_and_pinned_verification(self):
        source,body=self.source();body['samples'][0]['text']='准确的第一段\n含\u2028分隔符。'
        result=self.data.prepare(self.lib,body);directory=self.data.root/result['id']
        meta=json.loads((directory/'manifest.json').read_text());rows=[json.loads(line) for line in (directory/'train_raw.jsonl').read_bytes().split(b'\n') if line]
        self.assertEqual(result['state'],'input_snapshot_ready');self.assertEqual(result['sample_count'],3)
        self.assertTrue(result['integrity_verified_now']);self.assertFalse(result['checks']['training_verified'])
        self.assertEqual(meta['source_revision'],source['revision']);self.assertEqual([r['text'] for r in rows],[r['text'] for r in body['samples']])
        self.assertEqual(len({r['ref_audio'] for r in rows}),1)
        for sample,raw in zip(meta['samples'],[wav(hz=440),wav(hz=550),wav(hz=660)]):
            self.assertEqual(sample['source_sha256'],td.digest(raw));self.assertEqual(sample['frames'],36000)
            self.assertEqual((directory/'audio'/(sample['id']+'.wav')).read_bytes(),raw)
        self.assertTrue(self.data.verify(result['id'],result['manifest_sha256'])['integrity_verified_now'])
        self.assertFalse(self.data.list()[0]['integrity_verified_now'])
        for path in directory.rglob('*'):self.assertEqual(path.stat().st_mode&0o777,0o700 if path.is_dir() else 0o600)

    def test_snapshot_does_not_change_profile_job_and_survives_source_deletion(self):
        source,body=self.source();sid=source['samples'][0]['id'];lease=self.lib.begin(source['id'],2,[sid],'a'*12);self.lib.finish(lease,{'state':'done','profile':'previous-ready'})
        before=self.lib.get(source['id']);result=self.data.prepare(self.lib,body)
        self.assertEqual(self.lib.get(source['id']),before)
        self.lib.remove(source['id'],2)
        self.assertTrue(self.data.verify(result['id'],result['manifest_sha256'])['integrity_verified_now'])
        self.data.delete(result['id'],result['manifest_sha256']);self.assertEqual(self.data.list(),[])

    def test_authorization_and_single_speaker_are_explicit_booleans(self):
        _,body=self.source()
        for key in ('voice_rights_confirmed','single_speaker_confirmed'):
            for value in (False,1,'true',None):self.reject(400,self.data.prepare,self.lib,{**body,key:value})
        self.assertEqual(self.data.list(),[])

    def test_per_sample_text_duplicate_foreign_reference_and_stale_revision(self):
        _,body=self.source()
        for text in ('','x'*2001,'\ud800',True):
            changed={**body,'samples':[{'id':body['samples'][0]['id'],'text':text}]}
            self.reject(400,self.data.prepare,self.lib,changed)
        self.reject(400,self.data.prepare,self.lib,{**body,'samples':[body['samples'][0]]*2})
        self.reject(400,self.data.prepare,self.lib,{**body,'reference_sample_id':'f'*32})
        self.reject(400,self.data.prepare,self.lib,{**body,'samples':[{'id':'f'*32,'text':'外来'}],'reference_sample_id':'f'*32})
        self.reject(409,self.data.prepare,self.lib,{**body,'revision':1})
        self.assertEqual(self.data.list(),[])

    def test_container_gate_rejects_corrupt_wrong_rate_stereo_constant_and_truncation(self):
        valid=wav()
        for raw in (b'not WAV',valid[:-2],wav(sr=22050),wav(channels=2),wav(constant=True)):
            with self.subTest(size=len(raw)):
                with self.assertRaises(UploadRejected):td.canonical_wav(raw,240,900*td.SR)
        chunk=b'data'+struct.pack('<I',4)+b'\x01\x00\x02\x00'
        duplicate=valid+chunk;duplicate=duplicate[:4]+struct.pack('<I',len(duplicate)-8)+duplicate[8:]
        self.reject(400,td.canonical_wav,duplicate,240,900*td.SR)

    def test_extra_metadata_is_removed_but_all_pcm_frames_preserved(self):
        original=wav();junk=b'JUNK'+struct.pack('<I',6)+b'privat'
        raw=original[:12]+junk+original[12:];raw=raw[:4]+struct.pack('<I',len(raw)-8)+raw[8:]
        canonical,stats=td.canonical_wav(raw,240,900*td.SR)
        self.assertEqual(canonical,original);self.assertEqual(stats['frames'],36000);self.assertNotEqual(td.digest(raw),td.digest(canonical))

    def test_short_long_reference_and_total_duration_never_truncated(self):
        self.reject(413,td.canonical_wav,wav(.5),240,900*td.SR)
        self.reject(413,td.canonical_wav,wav(2),1,900*td.SR)
        self.reject(413,td.canonical_wav,wav(2),240,td.SR)
        source,body=self.source([wav(17)]);self.reject(413,self.data.prepare,self.lib,body)
        self.assertEqual(self.lib.get(source['id'])['samples'],source['samples']);self.assertEqual(self.data.list(),[])

    def test_rank_plan_covers_all_has_equal_steps_and_explicit_odd_padding(self):
        for count in (1,2,3,15,16):
            ids=[f'{index:032x}' for index in range(1,count+1)];plan=td.rank_plan(ids)
            rows=plan['ranks'][0]+plan['ranks'][1]
            self.assertEqual({r['sample_id'] for r in rows if not r['padding']},set(ids));self.assertEqual(sum(r['padding'] for r in rows),count%2)
            self.assertEqual(len(plan['ranks'][0]),len(plan['ranks'][1]));self.assertFalse(plan['training_verified'])
            self.assertEqual(plan,td.rank_plan(list(reversed(ids))))
        ids=[f'{i:032x}' for i in range(3)];self.assertNotEqual(td.rank_plan(ids,epoch=0)['ranks'],td.rank_plan(ids,epoch=1)['ranks'])

    def test_write_and_publish_failures_roll_back_without_altering_raw(self):
        source,body=self.source()
        for target in ('_write','rename'):
            context=patch.object(self.data,'_write',side_effect=OSError('injected')) if target=='_write' else patch.object(td.os,'rename',side_effect=OSError('injected'))
            with context:
                with self.assertRaises(OSError):self.data.prepare(self.lib,body)
            self.assertFalse(list(self.data.root.glob('.pending-*')));self.assertEqual(self.data.list(),[])
        self.assertEqual(self.lib.get(source['id'])['samples'],source['samples']);self.assertFalse(self.lib.get(source['id'])['busy'])

    def test_snapshot_lease_and_global_preparation_are_nonblocking(self):
        source,body=self.source();entered=threading.Event();release=threading.Event();original=td.canonical_wav;results=[]
        def decode(*args):entered.set();release.wait(3);return original(*args)
        def prepare():results.append(self.data.prepare(self.lib,body))
        with patch.object(td,'canonical_wav',side_effect=decode):
            thread=threading.Thread(target=prepare);thread.start()
            try:
                self.assertTrue(entered.wait(1));self.reject(409,self.lib.remove,source['id'],2);self.reject(409,self.data.prepare,self.lib,body)
            finally:release.set();thread.join(3)
        self.assertEqual(len(results),1);self.assertFalse(self.lib.get(source['id'])['busy'])

    def test_count_per_snapshot_global_byte_and_disk_budgets(self):
        _,body=self.source()
        self.data.per_bytes=10;self.reject(413,self.data.prepare,self.lib,body);self.assertEqual(self.data.list(),[])
        self.data.per_bytes=64<<20;self.data.total_bytes=1;self.reject(413,self.data.prepare,self.lib,body)
        self.data.total_bytes=256<<20
        with patch.object(td.shutil,'disk_usage',return_value=type('D',(),{'free':1})()):self.reject(507,self.data.prepare,self.lib,body)
        result=self.data.prepare(self.lib,body);self.data.maximum=1;self.reject(409,self.data.prepare,self.lib,body)
        self.assertEqual(self.data.list()[0]['id'],result['id'])

    def test_audio_index_and_plan_tampering_fail_fixed_hash_verification(self):
        _,body=self.source();result=self.data.prepare(self.lib,body);directory=self.data.root/result['id']
        for path in (directory/'train_raw.jsonl',directory/'rank_plan.json',next((directory/'audio').iterdir())):
            before=path.read_bytes();path.write_bytes(before+b'!');self.reject(409,self.data.verify,result['id'],result['manifest_sha256']);path.write_bytes(before)
        self.reject(409,self.data.verify,result['id'],'f'*64);self.reject(400,self.data.verify,result['id'],'bad')
        self.assertTrue(self.data.verify(result['id'],result['manifest_sha256'])['integrity_verified_now'])

    def test_symlink_hardlink_and_path_traversal_fail_closed(self):
        _,body=self.source();result=self.data.prepare(self.lib,body);directory=self.data.root/result['id'];path=next((directory/'audio').iterdir())
        external=self.state/'secret';external.write_bytes(b'not exported');before=path.read_bytes();path.unlink();path.symlink_to(external)
        self.reject(409,self.data.verify,result['id'],result['manifest_sha256']);self.assertEqual(external.read_bytes(),b'not exported')
        path.unlink();path.write_bytes(before);os.link(path,self.state/'hardlink');self.reject(409,self.data.verify,result['id'],result['manifest_sha256'])
        self.reject(400,self.data.verify,'../escape',result['manifest_sha256'])

    def test_failed_hash_delete_retains_snapshot_and_deletion_does_not_touch_library(self):
        source,body=self.source();result=self.data.prepare(self.lib,body)
        self.reject(409,self.data.delete,result['id'],'f'*64)
        self.data.delete(result['id'],result['manifest_sha256']);self.assertEqual(self.lib.get(source['id'])['samples'],source['samples'])

    def test_dataset_backup_does_not_include_training_input_copies(self):
        _,body=self.source();self.data.prepare(self.lib,body)
        profile=self.state/'profiles/ready';profile.mkdir(parents=True);(profile/'profile.json').write_text('{}')
        import tarfile
        with patch.object(persist,'STATE',self.state),patch.object(persist,'PROFILES_DIR',self.state/'profiles'):
            archive=persist._pack(self.state/'snapshot.tar.gz')
        with tarfile.open(archive) as stream:
            self.assertIn('profiles/ready/profile.json',stream.getnames())
            self.assertFalse(any(name.startswith(('libraries/','training_data/')) for name in stream.getnames()))

    def test_interrupted_staging_is_reaped_without_removing_published_snapshot(self):
        _,body=self.source();result=self.data.prepare(self.lib,body);orphan=self.data.root/'.pending-old';orphan.mkdir();(orphan/'partial').write_bytes(b'partial')
        self.data.prepare(self.lib,body);self.assertFalse(orphan.exists());self.assertTrue((self.data.root/result['id']).exists())


class TrainingAPITests(Fixture,unittest.TestCase):
    def setUp(self):
        super().setUp()
        for p in (patch.object(analyst,'LIBRARIES',self.lib),patch.object(analyst,'TRAINING_DATA',self.data),patch.object(analyst,'HEAVY',HeavyAdmission())):
            p.start();self.addCleanup(p.stop)
        self.client=TestClient(analyst.app);self.addCleanup(self.client.close)

    def test_real_prepare_verify_delete_without_model_or_job_creation(self):
        source,body=self.source();before=dict(analyst.JOBS)
        response=self.client.post('/training-data',json=body);self.assertEqual(response.status_code,200,response.text);row=response.json()['dataset']
        self.assertFalse(row['checks']['training_verified']);self.assertEqual(row['sample_count'],3);self.assertNotIn('对应第',response.text)
        response=self.client.post('/training-data/'+row['id']+'/verify',json={'manifest_sha256':row['manifest_sha256']});self.assertEqual(response.status_code,200,response.text)
        self.assertTrue(response.json()['dataset']['integrity_verified_now']);self.assertEqual(dict(analyst.JOBS),before)
        self.assertEqual(self.client.get('/training-data').json()['datasets'][0]['id'],row['id'])
        self.assertEqual(self.client.request('DELETE','/training-data/'+row['id'],json={'manifest_sha256':row['manifest_sha256']}).status_code,200)
        self.assertEqual(self.lib.get(source['id'])['samples'],source['samples'])

    def test_unknown_duplicate_fields_wrong_booleans_and_missing_transcript_rejected(self):
        _,body=self.source()
        for extra in ({'training_verified':True},{'voice_rights_confirmed':'true'},{'samples':[]},{'samples':[{'id':body['samples'][0]['id']}]}):
            response=self.client.post('/training-data',json={**body,**extra});self.assertEqual(response.status_code,400,response.text)
        response=self.client.post('/training-data',content='{"library_id":"a","library_id":"b"}',headers={'Content-Type':'application/json'});self.assertEqual(response.status_code,400)
        self.assertEqual(self.data.list(),[])

    def test_failed_storage_response_sanitized_and_no_raw_download_routes(self):
        _,body=self.source()
        with patch.object(self.data,'prepare',side_effect=OSError('/private/source/transcript')):
            response=self.client.post('/training-data',json=body)
        self.assertEqual(response.status_code,503);self.assertNotIn('/private',response.text)
        self.assertEqual(self.client.get('/training-data/'+'a'*32+'/audio/file.wav').status_code,404)


if __name__=='__main__':unittest.main()
