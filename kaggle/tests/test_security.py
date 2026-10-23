"""CPU-only access control and resource-budget regressions (no real model/API)."""
import asyncio
import concurrent.futures
from dataclasses import replace
import io
import os
from pathlib import Path
import stat
import sys
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]/'source'
TEMP=tempfile.TemporaryDirectory(prefix='qtts-security-')
os.environ.setdefault('QTTS_MOCK','1')
os.environ.setdefault('QTTS_STATE',TEMP.name)
sys.path.insert(0,str(ROOT/'py'))
import access_control as access
import analyst
import bootstrap
import numpy as np
import resource_limits as limits
import supervisor
from fastapi import FastAPI,Request
from fastapi.testclient import TestClient

class AccessTests(unittest.TestCase):
    def test_generated_token_permissions_reuse_and_concurrent_provisioning(self):
        with tempfile.TemporaryDirectory() as d, patch.dict(os.environ,{},clear=True):
            state=Path(d)
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
                tokens=list(pool.map(lambda _:access.ensure_access_token(state),range(16)))
            self.assertEqual(len(set(tokens)),1)
            self.assertGreaterEqual(len(tokens[0]),32)
            self.assertEqual(stat.S_IMODE((state/access.TOKEN_FILE).stat().st_mode),0o600)
            self.assertEqual(access.load_access_token(state),tokens[0])

    def test_invalid_explicit_token_and_symlink_fail_closed(self):
        with tempfile.TemporaryDirectory() as d:
            for value in ['','short','a'*257,'含中文'*20,' '*40]:
                with patch.dict(os.environ,{'QTTS_ACCESS_TOKEN':value}):
                    with self.assertRaises(ValueError):access.ensure_access_token(Path(d))
            with patch.dict(os.environ,{},clear=True):
                (Path(d)/'outside').write_text('x'*40)
                (Path(d)/access.TOKEN_FILE).symlink_to(Path(d)/'outside')
                with self.assertRaises(OSError):access.ensure_access_token(Path(d))

    def test_default_auth_directory_is_outside_exported_voice_state(self):
        with patch.dict(os.environ,{},clear=True):
            state=Path('/kaggle/working/qtts/state')
            folder=access.auth_directory(state)
            self.assertTrue(str(folder).startswith(tempfile.gettempdir()))
            self.assertFalse(folder.is_relative_to(state))
            self.assertNotEqual(folder,access.auth_directory(Path('/different/state')))

    def test_local_probe_headers_never_go_to_workers_or_remote_hosts(self):
        with patch.dict(os.environ,{'QTTS_ACCESS_TOKEN':'test-token-not-real-012345678901234567890123'}):
            self.assertIn('Authorization',access.gateway_headers('http://127.0.0.1:7860/api/health',Path(TEMP.name),7860))
            for url in ['http://127.0.0.1:7001/health','https://evil.example:7860/api/health','http://evil.example:7860','http://localhost:7010/health']:
                self.assertEqual(access.gateway_headers(url,Path(TEMP.name),7860),{})

    def test_child_processes_only_receive_required_credentials(self):
        credentials={name:'synthetic-not-real' for name in ['QTTS_ACCESS_TOKEN','DEEPSEEK_API_KEY','HF_TOKEN','KAGGLE_USERNAME','KAGGLE_KEY']}
        with patch.dict(os.environ,credentials):
            for name in ['worker0','analyst']:
                child=supervisor.child_environment(name,{})
                self.assertIn('HF_TOKEN',child)
                for secret in ['QTTS_ACCESS_TOKEN','DEEPSEEK_API_KEY','KAGGLE_USERNAME','KAGGLE_KEY']:self.assertNotIn(secret,child)
            gateway=supervisor.child_environment('gateway',{})
            self.assertIn('QTTS_ACCESS_TOKEN',gateway);self.assertIn('DEEPSEEK_API_KEY',gateway)
            for secret in ['HF_TOKEN','KAGGLE_USERNAME','KAGGLE_KEY']:self.assertNotIn(secret,gateway)

    def test_bootstrap_has_the_safe_archive_extractor_import(self):
        self.assertTrue(callable(bootstrap.extract_tar_safely))


class ResourceTests(unittest.TestCase):
    def test_unknown_length_body_is_rejected_before_application_or_parser(self):
        async def scenario(chunks, maximum, expect):
            called=[];sent=[]
            async def app(scope,receive,send):
                called.append(True);data=b''
                while True:
                    event=await receive();data+=event.get('body',b'')
                    if not event.get('more_body',False):break
                self.assertEqual(data,b''.join(chunks))
                await send({'type':'http.response.start','status':204,'headers':[]})
                await send({'type':'http.response.body','body':b''})
            events=[{'type':'http.request','body':chunk,'more_body':i<len(chunks)-1} for i,chunk in enumerate(chunks)]
            async def receive():return events.pop(0)
            async def send(event):sent.append(event)
            middleware=limits.BodyBudgetMiddleware(app,maximum,maximum)
            await middleware({'type':'http','method':'POST','headers':[(b'content-type',b'multipart/form-data')]},receive,send)
            self.assertEqual(sent[0]['status'],expect)
            self.assertEqual(bool(called),expect==204)
        asyncio.run(scenario([b'123456',b'abcdef'],8,413))
        asyncio.run(scenario([b'1234',b'abcd'],8,204))

    def test_known_body_limits_and_malformed_length(self):
        async def app(scope,receive,send):self.fail('oversized body reached application')
        for length,expected in [(b'100',413),(b'-1',400),(b'broken',400)]:
            async def run():
                sent=[]
                async def receive():self.fail('declared oversized body was read')
                async def send(event):sent.append(event)
                await limits.BodyBudgetMiddleware(app,8)({'type':'http','method':'POST','headers':[(b'content-type',b'multipart/form-data'),(b'content-length',length)]},receive,send)
                self.assertEqual(sent[0]['status'],expected)
            asyncio.run(run())

    def test_read_upload_empty_per_file_and_aggregate_limits(self):
        class File:
            def __init__(self,data):self.file=io.BytesIO(data)
            async def read(self,n):return self.file.read(n)
        async def run():
            budget=replace(limits.UploadLimits(),file_bytes=8)
            self.assertEqual(await limits.read_upload(File(b'12345678'),budget,8),b'12345678')
            for data,remaining,code in [(b'',8,400),(b'123456789',100,413),(b'12345',4,413)]:
                with self.assertRaises(limits.UploadRejected) as caught:await limits.read_upload(File(data),budget,remaining)
                self.assertEqual(caught.exception.code,code)
        asyncio.run(run())

    def test_heavy_slot_remains_reserved_after_http_waiter_cancels(self):
        admission=limits.HeavyAdmission(1);started=threading.Event();release=threading.Event()
        def work():started.set();release.wait(2);return 'finished'
        async def run():
            task=asyncio.create_task(admission.run(work))
            await asyncio.to_thread(started.wait,1)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):await task
            try:
                with self.assertRaises(limits.UploadRejected) as caught:await admission.run(lambda:'unsafe')
                self.assertEqual(caught.exception.code,429)
            finally:release.set()
            for _ in range(100):
                try:
                    result=await admission.run(lambda:'recovered');break
                except limits.UploadRejected:await asyncio.sleep(.005)
            else:self.fail('heavy slot was not released')
            self.assertEqual(result,'recovered')
        asyncio.run(run())

    def test_retained_build_records_are_bounded_and_terminal_jobs_pruned(self):
        admission=limits.BuildAdmission();jobs={'old':{'state':'done'}};done=threading.Event();job={'id':'new','state':'running'}
        self.assertTrue(admission.slot.acquire(blocking=False))
        admission.start(jobs,job,1,lambda:(job.update(state='done'),done.set()))
        self.assertTrue(done.wait(1));self.assertEqual(set(jobs),{'new'})

    def test_build_start_failure_does_not_leave_a_record(self):
        admission=limits.BuildAdmission();jobs={};job={'id':'new','state':'running'}
        with patch('threading.Thread.start',side_effect=RuntimeError('simulated start failure')):
            with self.assertRaises(RuntimeError):admission.start(jobs,job,1,lambda:None)
        self.assertEqual(jobs,{})

    def test_resource_environment_validation(self):
        for value in ['0','-1','invalid','999999']:
            with patch.dict(os.environ,{'QTTS_MAX_UPLOAD_FILES':value}):
                with self.assertRaises(ValueError):limits.UploadLimits.from_env()


class AnalystUploadTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory(prefix='qtts-upload-')
        self.addCleanup(self.directory.cleanup)
        self.budget=replace(limits.UploadLimits(),files=2,file_bytes=8,request_bytes=1024)
        self.patches=[patch.object(analyst,'PROFILES_DIR',Path(self.directory.name)),patch.object(analyst,'LIMITS',self.budget),
                      patch.object(analyst,'ADMISSION',limits.BuildAdmission()),patch.dict(analyst.JOBS,{},clear=True)]
        for p in self.patches:p.start();self.addCleanup(p.stop)
        self.client=TestClient(analyst.app)
        self.addCleanup(self.client.close)

    def test_too_many_files_empty_oversized_and_empty_name_rejected(self):
        cases=[([('files',('a.wav',b'a'))]*3,{'name':'test'},413),
               ([('files',('a.wav',b''))],{'name':'test'},400),
               ([('files',('a.wav',b'123456789'))],{'name':'test'},413),
               ([('files',('a.wav',b'a'))],{'name':'   '},400)]
        with patch.object(analyst,'build_profile') as build:
            for files,data,code in cases:
                response=self.client.post('/profiles',files=files,data=data)
                self.assertEqual(response.status_code,code,response.text)
            build.assert_not_called()
        self.assertEqual(analyst.JOBS,{})

    def test_busy_build_rejected_without_waiting_and_failure_releases(self):
        started=threading.Event();release=threading.Event()
        def build(job,*args):started.set();release.wait(2);job['state']='done'
        with patch.object(analyst,'build_profile',side_effect=build):
            try:
                first=self.client.post('/profiles',files={'files':('a.wav',b'1234')},data={'name':'test','calibrate':'0'})
                self.assertEqual(first.status_code,200,first.text);self.assertTrue(started.wait(1))
                second=self.client.post('/profiles',files={'files':('a.wav',b'1234')},data={'name':'test'})
                self.assertEqual(second.status_code,429,second.text)
                self.assertEqual(len(analyst.JOBS),1)
            finally:release.set()
            deadline=time.monotonic()+1
            while time.monotonic()<deadline:
                if analyst.ADMISSION.slot.acquire(blocking=False):
                    analyst.ADMISSION.slot.release();break
                time.sleep(.005)
            else:self.fail('build slot leaked')
        # An invalid upload also returns the slot immediately.
        response=self.client.post('/profiles',files={'files':('empty.wav',b'')},data={'name':'test'})
        self.assertEqual(response.status_code,400,response.text)

    def test_profile_count_and_disk_budget_reject_before_job(self):
        with patch.object(analyst,'LIMITS',replace(self.budget,profiles=1)):
            (Path(self.directory.name)/'existing').mkdir()
            response=self.client.post('/profiles',files={'files':('a.wav',b'a')},data={'name':'test'})
            self.assertEqual(response.status_code,409)
        with patch.object(analyst.shutil,'disk_usage',return_value=SimpleNamespace(free=1)):
            response=self.client.post('/profiles',files={'files':('a.wav',b'a')},data={'name':'test'})
            self.assertEqual(response.status_code,507)
        self.assertEqual(analyst.JOBS,{})

    def test_decode_oversize_is_rejected_not_silently_truncated_or_fallback(self):
        budget=replace(self.budget,seconds=1)
        output=np.zeros(analyst.SR+1,np.float32).tobytes()
        with patch.object(analyst,'LIMITS',budget),patch.object(analyst.subprocess,'run',return_value=SimpleNamespace(returncode=0,stdout=output,stderr=b'')) as run:
            with self.assertRaises(limits.UploadRejected):analyst.decode_audio(b'compressed','a.wav')
            args=run.call_args.args[0]
            self.assertIn('-protocol_whitelist',args);self.assertEqual(args[args.index('-protocol_whitelist')+1],'pipe')
            self.assertIn('-t',args)

    def test_total_decoded_duration_is_not_silently_truncated(self):
        budget=replace(self.budget,seconds=2,total_seconds=3)
        job={'id':'duration','state':'running','pct':0,'log':[]}
        with patch.object(analyst,'LIMITS',budget),patch.object(analyst.SPK,'load'),patch.object(analyst,'decode_audio',return_value=np.zeros(analyst.SR*2,np.float32)),patch.object(analyst,'highpass',side_effect=lambda y,sr:y),patch.object(analyst,'estimate_snr',return_value=50),patch.object(analyst,'normalize_speech',side_effect=lambda y,sr:y),patch.object(analyst,'profile_dir',side_effect=lambda pid:Path(self.directory.name)/pid),patch.object(analyst.ASR,'transcribe') as transcribe:
            analyst.build_profile(job,'test',[('a.wav',b'a'),('b.wav',b'b')],'auto','',False)
            self.assertEqual(job['state'],'error')
            self.assertIn('total decoded audio duration',job['error'])
            transcribe.assert_not_called()

    def test_thread_start_failure_releases_endpoint_admission(self):
        with patch.object(analyst.ADMISSION,'start',side_effect=RuntimeError('simulated failure')):
            response=self.client.post('/profiles',files={'files':('a.wav',b'a')},data={'name':'test'})
        self.assertEqual(response.status_code,503,response.text)
        self.assertEqual(analyst.JOBS,{})
        self.assertTrue(analyst.ADMISSION.slot.acquire(blocking=False))
        analyst.ADMISSION.slot.release()

    def test_soundfile_fallback_still_decodes_valid_short_audio(self):
        import soundfile as sf
        data=io.BytesIO();source=np.sin(np.arange(analyst.SR*2)*.04).astype(np.float32)*.1
        sf.write(data,source,analyst.SR,format='WAV')
        with patch.object(analyst.subprocess,'run',side_effect=FileNotFoundError()):
            decoded=analyst.decode_audio(data.getvalue(),'valid.wav')
        self.assertEqual(decoded.shape,source.shape)
        self.assertEqual(decoded.dtype,np.float32)
        self.assertLess(float(np.max(np.abs(decoded-source))),.0001)

    def test_soundfile_fallback_checks_duration_before_allocating(self):
        import soundfile as sf
        data=io.BytesIO();sf.write(data,np.zeros(16001,np.float32),16000,format='WAV')
        with patch.object(analyst,'LIMITS',replace(self.budget,seconds=1)),patch.object(analyst.subprocess,'run',side_effect=FileNotFoundError()):
            with self.assertRaises(limits.UploadRejected):analyst.decode_audio(data.getvalue(),'long.wav')

    def test_consistency_text_count_is_bounded_before_expensive_work(self):
        with patch.object(analyst,'load_profile',return_value={'id':'test'}),patch.object(analyst,'consistency') as work:
            for texts in [['x']*7,['x'*201],['x'*200]*6,'wrong-type']:
                response=self.client.post('/consistency',json={'profile':'test','texts':texts})
                self.assertEqual(response.status_code,400,response.text)
            work.assert_not_called()

if __name__=='__main__':unittest.main()
