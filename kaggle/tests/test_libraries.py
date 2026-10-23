"""Real local filesystem/FastAPI regressions; build function is explicitly mocked."""
import asyncio
import concurrent.futures
import httpx
from dataclasses import replace
import hashlib
import json
import os
from pathlib import Path
import select
import stat
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]/'source'
TEMP=tempfile.TemporaryDirectory(prefix='qtts-libraries-env-')
os.environ.setdefault('QTTS_STATE',TEMP.name);os.environ.setdefault('QTTS_MOCK','1')
sys.path.insert(0,str(ROOT/'py'))
import voice_library as lib
from resource_limits import UploadRejected, BuildAdmission, HeavyAdmission
import analyst
import persist
from fastapi.testclient import TestClient


class LibraryStorageTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'libraries'
        self.store=lib.LibraryStore(self.root,maximum=2,files=2,file_bytes=8,library_bytes=12,total_bytes=16,free_bytes=0)

    def create(self,name='自己的库'):
        return self.store.create(name)

    def sample(self,name='自己的库'):
        row=self.create(name);return self.store.add(row['id'],row['revision'],[('ref.wav',b'1234')])

    def reject(self,code,fn,*args):
        with self.assertRaises(UploadRejected) as raised:fn(*args)
        self.assertEqual(raised.exception.code,code)

    def test_empty_named_library_survives_new_process_without_profile(self):
        row=self.create();self.assertEqual((row['state'],row['samples'],row['training_verified']),('empty',[],False))
        code='import json,sys;from voice_library import LibraryStore;print(json.dumps(LibraryStore(sys.argv[1]).get(sys.argv[2]),ensure_ascii=False))'
        result=subprocess.run([sys.executable,'-c',code,str(self.root),row['id']],env={**os.environ,'PYTHONPATH':str(ROOT/'py')},capture_output=True,text=True,timeout=3,check=True)
        self.assertEqual(json.loads(result.stdout)['name'],'自己的库')
        self.assertFalse((Path(self.temp.name)/'profiles').exists())
        self.assertEqual(stat.S_IMODE(self.root.stat().st_mode),0o700)
        self.assertEqual(stat.S_IMODE((self.root/row['id']/'library.json').stat().st_mode),0o600)

    def test_name_validation_normalization_and_unique_casefold(self):
        for value in ('','  ','x'*65,'x\nname','\ud800',None,True):self.reject(400,self.store.create,value)
        row=self.create(' Cafe\u0301 ');self.assertEqual(row['name'],'Café')
        self.reject(409,self.store.create,'CAFÉ')

    def test_count_and_disk_budgets(self):
        self.create('a');self.create('b');self.reject(409,self.store.create,'c')
        with patch.object(lib.shutil,'disk_usage',return_value=type('Disk',(),{'free':0})()):
            self.store.free_bytes=1;self.reject(507,self.store.add,self.store.list()[0]['id'],1,[('a',b'a')])

    def test_dedup_filename_sanitization_and_hash(self):
        row=self.create();row=self.store.add(row['id'],1,[('../../a.wav',b'abc'),('same.wav',b'abc')])
        self.assertEqual(len(row['samples']),1);sample=row['samples'][0]
        self.assertEqual(sample['name'],'a.wav');self.assertEqual(sample['sha256'],hashlib.sha256(b'abc').hexdigest())
        same=self.store.add(row['id'],2,[('renamed',b'abc')]);self.assertEqual(same['revision'],2)
        self.assertEqual((self.root/row['id']/(sample['id']+'.audio')).read_bytes(),b'abc')

    def test_stale_revision_and_bool_rejected_without_changes(self):
        row=self.sample()
        for revision,code in ((1,409),(True,400),('2',400)):
            self.reject(code,self.store.add,row['id'],revision,[('b',b'b')])
        self.assertEqual(self.store.get(row['id'])['samples'],row['samples'])

    def test_count_file_library_and_global_byte_budgets_are_transactional(self):
        row=self.sample()
        for files in ([('a',b'a')]*3,[('a',b'123456789')],[('a',b'12345678'),('b',b'b')]):
            self.reject(413,self.store.add,row['id'],2,files)
        self.assertEqual(len(self.store.get(row['id'])['samples']),1)
        self.store.add(row['id'],2,[('four',b'5678')])
        second=self.create('other');second=self.store.add(second['id'],1,[('a',b'abcdefgh')])
        self.reject(413,self.store.add,second['id'],2,[('b',b'1234')])
        self.assertEqual(len(list(self.root.rglob('*.audio'))),3)

    def test_metadata_failure_rolls_back_all_new_files(self):
        row=self.sample();directory=self.root/row['id'];before=(directory/'library.json').read_bytes()
        with patch.object(lib,'atomic_json',side_effect=OSError('injected')):
            with self.assertRaises(OSError):self.store.add(row['id'],2,[('b',b'b')])
        self.assertEqual((directory/'library.json').read_bytes(),before);self.assertEqual(len(list(directory.glob('*.audio'))),1)

    def test_sample_write_failure_rolls_back_partial_file(self):
        row=self.create()
        with patch.object(lib.os,'fsync',side_effect=OSError('injected')):
            with self.assertRaises(OSError):self.store.add(row['id'],1,[('b',b'b')])
        self.assertFalse(list((self.root/row['id']).glob('*.audio')))
        self.assertEqual(self.store.get(row['id'])['revision'],1)

    def test_uuid_validation_and_symlink_library_metadata_and_sample(self):
        for value in ('../x','X'*32,'f'*31,{},True):self.reject(400,self.store.get,value)
        external=Path(self.temp.name)/'external';external.mkdir();(external/'secret').write_text('retained')
        (self.root/('f'*32)).symlink_to(external,target_is_directory=True)
        self.reject(409,self.store.get,'f'*32);(self.root/('f'*32)).unlink()
        row=self.sample();directory=self.root/row['id'];sample=directory/(row['samples'][0]['id']+'.audio')
        sample.unlink();sample.symlink_to(external/'secret')
        with self.assertRaises(OSError):self.store.begin(row['id'],2,[row['samples'][0]['id']],'a'*12)
        self.assertEqual((external/'secret').read_text(),'retained')
        metadata=directory/'library.json';metadata.unlink();metadata.symlink_to(external/'secret')
        self.reject(409,self.store.get,row['id'])

    def test_hardlink_and_modified_sample_integrity_fail_closed(self):
        row=self.sample();path=self.root/row['id']/(row['samples'][0]['id']+'.audio')
        path.write_bytes(b'4321');self.reject(409,self.store.begin,row['id'],2,[row['samples'][0]['id']],'a'*12)
        self.assertFalse(self.store.get(row['id'])['busy'])
        os.link(path,path.with_suffix('.link'));self.reject(409,self.store.begin,row['id'],2,[row['samples'][0]['id']],'a'*12)

    def test_invalid_empty_duplicate_and_foreign_selections(self):
        row=self.sample();sid=row['samples'][0]['id']
        for selected in ([],[sid,sid],['f'*32],['../x']):self.reject(400,self.store.begin,row['id'],2,selected,'a'*12)
        self.assertIsNone(self.store.get(row['id'])['last_build']);self.assertFalse(self.store.get(row['id'])['busy'])

    def test_build_lease_blocks_mutation_and_second_store_until_released(self):
        row=self.sample();sid=row['samples'][0]['id'];lease=self.store.begin(row['id'],2,[sid],'a'*12)
        try:
            self.assertEqual(self.store.get(row['id'])['state'],'processing')
            self.reject(409,self.store.add,row['id'],2,[('b',b'b')]);self.reject(409,self.store.remove_sample,row['id'],sid,2)
            self.reject(409,self.store.remove,row['id'],2)
            other=lib.LibraryStore(self.root,free_bytes=0);self.reject(409,other.begin,row['id'],2,[sid],'b'*12)
        finally:self.store.finish(lease,{'state':'error'})
        self.assertEqual(self.store.get(row['id'])['state'],'processing_failed')

    def test_success_then_failed_reprocessing_retains_previous_profile(self):
        row=self.sample();sid=row['samples'][0]['id']
        lease=self.store.begin(row['id'],2,[sid],'a'*12);self.store.finish(lease,{'state':'done','profile':'voice-123'})
        result=self.store.get(row['id']);self.assertEqual(result['state'],'reference_prepared');self.assertFalse(result['inference_verified'])
        lease=self.store.begin(row['id'],2,[sid],'b'*12);self.store.finish(lease,{'state':'error','profile':'partial'})
        self.assertEqual(self.store.get(row['id'])['prepared_profile'],'voice-123')
        changed=self.store.add(row['id'],2,[('b',b'b')]);self.assertEqual(changed['state'],'samples_unverified')

    def test_finish_commit_failure_releases_lease_and_reports_interruption(self):
        row=self.sample();lease=self.store.begin(row['id'],2,[row['samples'][0]['id']],'a'*12)
        with patch.object(lib,'atomic_json',side_effect=OSError('injected')):
            with self.assertRaises(OSError):self.store.finish(lease,{'state':'done','profile':'voice-123'})
        result=self.store.get(row['id']);self.assertEqual(result['state'],'interrupted');self.assertFalse(result['busy'])

    def test_crashed_process_releases_advisory_lease_without_fake_completion(self):
        row=self.sample();sid=row['samples'][0]['id']
        code='import sys;from voice_library import LibraryStore;s=LibraryStore(sys.argv[1]);lease=s.begin(sys.argv[2],2,[sys.argv[3]],"a"*12);print("ready",flush=True);sys.stdin.read()'
        process=subprocess.Popen([sys.executable,'-c',code,str(self.root),row['id'],sid],env={**os.environ,'PYTHONPATH':str(ROOT/'py')},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            self.assertTrue(select.select([process.stdout],[],[],3)[0]);self.assertEqual(process.stdout.readline().strip(),'ready')
            self.reject(409,self.store.remove,row['id'],2)
        finally:
            process.kill();process.communicate(timeout=3)
        result=self.store.get(row['id']);self.assertEqual(result['state'],'interrupted');self.assertFalse(result['busy'])

    def test_same_revision_concurrent_mutations_do_not_lose_updates(self):
        row=self.create();barrier=threading.Barrier(2)
        def add(value):
            barrier.wait()
            try:return self.store.add(row['id'],1,[(value,value.encode())])['revision']
            except UploadRejected as error:return error.code
        with concurrent.futures.ThreadPoolExecutor(2) as pool:results=list(pool.map(add,['a','b']))
        self.assertEqual(sorted(results),[2,409]);self.assertEqual(len(self.store.get(row['id'])['samples']),1)

    def test_removing_samples_and_library_never_removes_independent_profiles(self):
        profile=Path(self.temp.name)/'profiles/ready';profile.mkdir(parents=True);(profile/'profile.json').write_text('{}')
        row=self.sample();row=self.store.remove_sample(row['id'],row['samples'][0]['id'],2)
        self.assertEqual(row['state'],'empty');self.assertFalse(list((self.root/row['id']).glob('*.audio')))
        self.store.remove(row['id'],3);self.assertTrue(profile.exists());self.assertEqual(self.store.list(),[])

    def test_orphan_recovery_and_metadata_corruption_fail_closed(self):
        row=self.create();directory=self.root/row['id'];(directory/('f'*32+'.audio')).write_bytes(b'orphan');(directory/'.pending-old').write_bytes(b'partial')
        self.store.add(row['id'],1,[('a',b'a')]);self.assertFalse((directory/'.pending-old').exists());self.assertFalse((directory/('f'*32+'.audio')).exists())
        meta=json.loads((directory/'library.json').read_text());meta['last_build']={'state':'trained'};(directory/'library.json').write_text(json.dumps(meta))
        self.reject(409,self.store.get,row['id'])

    def test_dataset_pack_does_not_silently_include_raw_library(self):
        self.sample();state=Path(self.temp.name);profile=state/'profiles/ready';profile.mkdir(parents=True);(profile/'profile.json').write_text('{}')
        with patch.object(persist,'STATE',state),patch.object(persist,'PROFILES_DIR',state/'profiles'):
            archive=persist._pack(state/'archive.tar.gz')
        with tarfile.open(archive) as stream:
            self.assertIn('profiles/ready/profile.json',stream.getnames())
            self.assertFalse(any('libraries' in name or name.endswith('.audio') for name in stream.getnames()))


class LibraryAPITests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.state=Path(self.temp.name);self.profiles=self.state/'profiles';self.profiles.mkdir()
        self.store=lib.LibraryStore(self.state/'libraries',files=2,file_bytes=8,library_bytes=12,total_bytes=32,free_bytes=0)
        limits=replace(analyst.LIMITS,files=2,file_bytes=8,request_bytes=2048)
        for p in (patch.object(analyst,'LIBRARIES',self.store),patch.object(analyst,'LIMITS',limits),patch.object(analyst,'PROFILES_DIR',self.profiles),patch.object(analyst,'ADMISSION',BuildAdmission()),patch.object(analyst,'HEAVY',HeavyAdmission()),patch.dict(analyst.JOBS,{},clear=True)):
            p.start();self.addCleanup(p.stop)
        self.client=TestClient(analyst.app);self.addCleanup(self.client.close)
        self.addCleanup(self.wait_idle)

    def wait_idle(self):
        deadline=time.monotonic()+3
        while time.monotonic()<deadline:
            if analyst.ADMISSION.slot.acquire(blocking=False):analyst.ADMISSION.slot.release();return
            time.sleep(.005)
        self.fail('background admission leaked')

    def create(self):
        response=self.client.post('/libraries',json={'name':'先建的空库','language':'Chinese'})
        self.assertEqual(response.status_code,200,response.text);return response.json()['library']

    def uploaded(self):
        row=self.create();return self.client.post('/libraries/'+row['id']+'/samples',data={'revision':1},files={'files':('a.wav',b'1234')}).json()['library']

    def process(self,row,**extra):
        return self.client.post('/libraries/'+row['id']+'/process',content=json.dumps({'revision':row['revision'],'sample_ids':[s['id'] for s in row['samples']],**extra}),headers={'Content-Type':'application/json'})

    def test_real_http_create_empty_then_upload_select_and_process(self):
        row=self.create();self.assertEqual(self.client.get('/profiles').json()['profiles'],[])
        row=self.client.post('/libraries/'+row['id']+'/samples',data={'revision':1},files={'files':('a.wav',b'1234')}).json()['library']
        def build(job,name,files,language,text,calibrate):
            self.assertEqual((name,files,language,text,calibrate),('先建的空库',[('a.wav',b'1234')],'Chinese','参考',False))
            job.update(state='done',profile='voice-123',pct=100)
        with patch.object(analyst,'build_profile',side_effect=build):
            response=self.process(row,ref_text='参考',calibrate=False);self.assertEqual(response.status_code,200,response.text);self.wait_idle()
        result=self.client.get('/libraries/'+row['id']).json()['library'];self.assertEqual(result['state'],'reference_prepared');self.assertFalse(result['training_verified'])
        job=self.client.get('/jobs/'+response.json()['job']).json();self.assertEqual((job['state'],job['profile']),('done','voice-123'))

    def test_strict_json_duplicate_unknown_fields_nonfinite_and_types(self):
        for content in (json.dumps({'name':'\ud800'}),'[]','{"name":"a","unexpected":1}','{"name":"a","name":"b"}','{"name":NaN}','{"name":true}','{bad'):
            response=self.client.post('/libraries',content=content,headers={'Content-Type':'application/json'});self.assertEqual(response.status_code,400,response.text)
        self.assertEqual(self.store.list(),[])

    def test_upload_empty_oversize_count_fields_and_stale_revision(self):
        row=self.create();url='/libraries/'+row['id']+'/samples'
        for files,data,code in (([('files',('x',b''))],{'revision':1},400),([('files',('x',b'123456789'))],{'revision':1},413),([('files',('x',b'a'))]*3,{'revision':1},413),([('files',('x',b'a'))],{'revision':0},400),([('files',('x',b'a'))],{'revision':1,'extra':'x'},413)):
            response=self.client.post(url,data=data,files=files);self.assertEqual(response.status_code,code,response.text)
        self.assertEqual(self.store.get(row['id'])['samples'],[])

    def test_empty_or_foreign_selection_and_bad_calibrate_never_start_job(self):
        row=self.create()
        with patch.object(analyst,'build_profile') as build:
            for extra in ({},{'sample_ids':['f'*32]},{'calibrate':'false'},{'ref_text':'x'*20001},{'ref_text':'\ud800'},{'revision':True}):
                response=self.process(row,**extra);self.assertEqual(response.status_code,400,response.text)
            build.assert_not_called()
        self.assertEqual(analyst.JOBS,{})

    def test_build_failure_sanitizes_error_preserves_raw_and_releases(self):
        row=self.uploaded()
        with patch.object(analyst,'build_profile',side_effect=RuntimeError('/private/secret-path')):
            response=self.process(row);self.assertEqual(response.status_code,200);self.wait_idle()
        job=self.client.get('/jobs/'+response.json()['job']).json();self.assertEqual(job['state'],'error');self.assertNotIn('secret-path',job['error'])
        result=self.store.get(row['id']);self.assertEqual(result['state'],'processing_failed');self.assertEqual(result['samples'],row['samples'])

    def test_no_final_success_before_metadata_commit(self):
        row=self.uploaded();entered=threading.Event();release=threading.Event();original=self.store.finish
        def finish(lease,job):entered.set();release.wait(2);return original(lease,job)
        with patch.object(analyst,'build_profile',side_effect=lambda job,*args:job.update(state='done',profile='voice-123',pct=100)),patch.object(self.store,'finish',side_effect=finish):
            try:
                response=self.process(row);self.assertEqual(response.status_code,200);self.assertTrue(entered.wait(1))
                self.assertEqual(self.client.get('/jobs/'+response.json()['job']).json()['state'],'running')
                self.assertTrue(self.store.get(row['id'])['busy'])
            finally:release.set();self.wait_idle()
        self.assertEqual(self.store.get(row['id'])['state'],'reference_prepared')

    def test_library_and_legacy_share_busy_admission_and_mutations_are_blocked(self):
        row=self.uploaded();entered=threading.Event();release=threading.Event()
        def build(job,*args):entered.set();release.wait(2);job.update(state='done',profile='voice-123')
        with patch.object(analyst,'build_profile',side_effect=build):
            try:
                response=self.process(row);self.assertEqual(response.status_code,200);self.assertTrue(entered.wait(1))
                self.assertEqual(self.process(row).status_code,429)
                self.assertEqual(self.client.post('/profiles',data={'name':'legacy'},files={'files':('a',b'a')}).status_code,429)
                self.assertEqual(self.client.request('DELETE','/libraries/'+row['id'],json={'revision':2}).status_code,409)
                self.assertEqual(self.client.post('/libraries/'+row['id']+'/samples',data={'revision':2},files={'files':('b',b'b')}).status_code,409)
            finally:release.set();self.wait_idle()

    def test_thread_start_failure_rolls_back_lease_and_admission(self):
        row=self.uploaded()
        original_start=threading.Thread.start
        def start(thread,*args,**kwargs):
            if thread.name.startswith('build-'):raise RuntimeError('injected build thread start failure')
            return original_start(thread,*args,**kwargs)
        with patch('threading.Thread.start',new=start):response=self.process(row)
        self.assertEqual(response.status_code,503,response.text);self.wait_idle();self.assertFalse(self.store.get(row['id'])['busy'])
        self.assertEqual(self.store.get(row['id'])['state'],'processing_failed');self.assertEqual(analyst.JOBS,{})

    def test_cancelled_http_wait_does_not_strand_reservation_handoff(self):
        row=self.uploaded();entered=threading.Event();release=threading.Event();original=self.store.begin
        def begin(*args):entered.set();release.wait(2);return original(*args)
        async def run():
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=analyst.app),base_url='http://test') as client:
                task=asyncio.create_task(client.post('/libraries/'+row['id']+'/process',json={'revision':2,'sample_ids':[row['samples'][0]['id']]}))
                self.assertTrue(await asyncio.to_thread(entered.wait,1));task.cancel()
                with self.assertRaises(asyncio.CancelledError):await task
                release.set();await asyncio.to_thread(self.wait_idle)
        with patch.object(self.store,'begin',side_effect=begin),patch.object(analyst,'build_profile',side_effect=lambda job,*args:job.update(state='done',profile='voice-123')):
            try:asyncio.run(run())
            finally:release.set();self.wait_idle()
        self.assertEqual(self.store.get(row['id'])['state'],'reference_prepared');self.assertFalse(self.store.get(row['id'])['busy'])
        self.assertEqual(len(analyst.JOBS),1)

    def test_profile_count_and_free_disk_admission_preserve_raw(self):
        row=self.uploaded()
        with patch.object(analyst,'LIMITS',replace(analyst.LIMITS,profiles=1)):
            (self.profiles/'existing').mkdir();self.assertEqual(self.process(row).status_code,409)
        with patch.object(analyst.shutil,'disk_usage',return_value=type('Disk',(),{'free':1})()):
            self.assertEqual(self.process(row).status_code,507)
        self.assertFalse(self.store.get(row['id'])['busy']);self.assertEqual(analyst.JOBS,{})

    def test_failed_executor_submit_cannot_execute_its_queued_mutation_later(self):
        async def run():
            loop=asyncio.get_running_loop()
            loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=1))
            called=[];heavy=HeavyAdmission(1)
            with patch('threading.Thread.start',side_effect=RuntimeError('worker start rejected')):
                with self.assertRaises(RuntimeError):await heavy.run(lambda:called.append('must not run'))
            # Starting a later worker drains the earlier queued work item too.
            self.assertEqual(await loop.run_in_executor(None,lambda:7),7)
            self.assertEqual(called,[])
            self.assertTrue(heavy.slots.acquire(blocking=False));self.assertFalse(heavy.slots.acquire(blocking=False));heavy.slots.release()
        asyncio.run(run())

    def test_store_io_error_does_not_expose_private_path(self):
        with patch.object(self.store,'create',side_effect=OSError('/secret/raw-library')):
            response=self.client.post('/libraries',json={'name':'name'})
        self.assertEqual(response.status_code,503);self.assertNotIn('/secret',response.text)

    def test_cas_delete_and_get_and_no_audio_download(self):
        row=self.uploaded();sid=row['samples'][0]['id'];url='/libraries/'+row['id']
        self.assertEqual(self.client.request('DELETE',url+'/samples/'+sid,json={'revision':1}).status_code,409)
        response=self.client.request('DELETE',url+'/samples/'+sid,json={'revision':2});self.assertEqual(response.status_code,200,response.text)
        self.assertEqual(self.client.get(url+'/samples/'+sid).status_code,405)
        self.assertEqual(self.client.request('DELETE',url,json={'revision':3}).status_code,200)
        self.assertEqual(self.client.get(url).status_code,404)


if __name__=='__main__':unittest.main()
