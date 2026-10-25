"""Third semantic pass input batch: five protections and one unfixed FIFO witness.
Real bounded I/O/CPU children; no real credentials, model, GPU or acoustic proof.
"""
import asyncio
import hashlib
import io
import json
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import test_reliability
import access_control as auth
import qtts_common as common
import resource_limits as limits
import voice_binding as binding

ROOT=Path(__file__).resolve().parents[2]
OBSERVATIONS=[]

class InputBoundaryTests(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)

    def test_protect_read_upload_reads_at_most_budget_plus_one_and_preserves_exact_bytes(self):
        class Upload:
            def __init__(self,data):self.source=io.BytesIO(data);self.requests=[]
            async def read(self,n):self.requests.append(n);return self.source.read(n)
        budget=limits.UploadLimits(file_bytes=100000)
        data=bytes(range(256))*300
        exact=Upload(data);self.assertEqual(asyncio.run(limits.read_upload(exact,budget,len(data))),data)
        self.assertTrue(all(1<=n<=65536 for n in exact.requests))
        excess=Upload(data)
        with self.assertRaises(limits.UploadRejected):asyncio.run(limits.read_upload(excess,budget,32))
        self.assertEqual(excess.source.tell(),33);self.assertEqual(excess.requests,[33])

    def test_protect_spooled_body_closes_on_overflow_disconnect_and_downstream_error(self):
        real=limits.tempfile.SpooledTemporaryFile
        for scenario in ('overflow','disconnect','downstream-error'):
            opened=[];called=[];sent=[]
            def spool(*args,**kwargs):
                handle=real(*args,**kwargs);opened.append(handle);return handle
            async def downstream(scope,receive,send):
                called.append(True);await receive();raise RuntimeError('synthetic downstream failure')
            events=iter([{'type':'http.request','body':b'abcd','more_body':True},
                {'type':'http.disconnect'} if scenario=='disconnect' else {'type':'http.request','body':b'e' if scenario=='overflow' else b'','more_body':False}])
            async def receive():return next(events)
            async def send(message):sent.append(message)
            middleware=limits.BodyBudgetMiddleware(downstream,4,json_maximum=4)
            scope={'type':'http','method':'POST','headers':[]}
            with self.subTest(scenario=scenario),patch.object(limits.tempfile,'SpooledTemporaryFile',side_effect=spool):
                if scenario=='downstream-error':
                    with self.assertRaises(RuntimeError):asyncio.run(middleware(scope,receive,send))
                else:asyncio.run(middleware(scope,receive,send))
            self.assertEqual(len(opened),1);self.assertTrue(opened[0].closed)
            if scenario=='overflow':self.assertEqual(sent[0]['status'],413);self.assertEqual(called,[])
            elif scenario=='disconnect':self.assertEqual(sent,[]);self.assertEqual(called,[])
            else:self.assertEqual(called,[True])

    def test_protect_atomic_json_replace_failure_retains_old_private_file_and_cleans_temp(self):
        path=self.root/'profile.json';common.write_json_atomic(path,{'revision':1})
        with patch.object(common.os,'replace',side_effect=OSError('synthetic publication failure')):
            with self.assertRaises(OSError):common.write_json_atomic(path,{'revision':2})
        self.assertEqual(json.loads(path.read_text()),{'revision':1});self.assertEqual(list(self.root.iterdir()),[path])
        common.write_json_atomic(path,{'revision':3});self.assertEqual(json.loads(path.read_text()),{'revision':3})
        self.assertEqual(path.stat().st_mode&0o777,0o600)

    def test_protect_reference_growth_between_fstat_and_read_fails_closed(self):
        path=self.root/'ref.bin';path.write_bytes(b'initial fixture bytes');profile={'anchor':'ref.bin'}
        before=binding.reference_binding(self.root,profile);real=binding.os.fstat
        def fstat(fd):
            result=real(fd)
            with path.open('ab') as stream:stream.write(b'grown')
            return result
        with patch.object(binding.os,'fstat',side_effect=fstat):
            with self.assertRaisesRegex(ValueError,'changed while reading'):binding.reference_binding(self.root,profile)
        self.assertNotEqual(before,binding.reference_binding(self.root,profile))
        # Same-sized concurrent rewrite and malicious same-UID isolation NOT proven.

    def test_protect_two_auth_processes_publish_one_private_token_without_logging_it(self):
        script="import sys,hashlib;from pathlib import Path;sys.path.insert(0,sys.argv[1]);import access_control as a;print(hashlib.sha256(a.ensure_access_token(Path(sys.argv[2])).encode()).hexdigest())"
        command=[sys.executable,'-c',script,str(ROOT/'kaggle/source/py'),str(self.root/'auth')]
        processes=[]
        try:
            for _ in range(2):processes.append(subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env={'PATH':os.environ.get('PATH',''),'PYTHONDONTWRITEBYTECODE':'1'},start_new_session=True))
            hashes=[]
            for process in processes:
                out,err=process.communicate(timeout=5);self.assertEqual(process.returncode,0);self.assertEqual(err,'');self.assertRegex(out.strip(),r'^[a-f0-9]{64}$');hashes.append(out.strip())
            self.assertEqual(hashes[0],hashes[1]);directory=self.root/'auth'
            self.assertEqual(directory.stat().st_mode&0o777,0o700);self.assertEqual((directory/auth.TOKEN_FILE).stat().st_mode&0o777,0o600)
            self.assertEqual(hashlib.sha256((directory/auth.TOKEN_FILE).read_bytes()).hexdigest(),hashes[0])
        finally:
            for process in processes:
                if process.poll() is None:os.killpg(process.pid,signal.SIGKILL)
                process.communicate(timeout=5)
        # Tokens are generated only in owned temporary private directories and removed.

    def test_observed_auth_fifo_blocks_before_file_type_validation(self):
        script="import sys;from pathlib import Path;sys.path.insert(0,sys.argv[1]);import access_control as a;print('calling-token-read',flush=True);a.ensure_access_token(Path(sys.argv[2]));print('returned',flush=True)"
        env={'PATH':os.environ.get('PATH',''),'PYTHONDONTWRITEBYTECODE':'1'}
        control=self.root/'control';control.mkdir(mode=0o700);(control/auth.TOKEN_FILE).write_text('x'*40)
        command=[sys.executable,'-c',script,str(ROOT/'kaggle/source/py')]
        normal=subprocess.run(command+[str(control)],capture_output=True,text=True,env=env,timeout=5)
        self.assertEqual(normal.returncode,0);self.assertEqual(normal.stdout,'calling-token-read\nreturned\n')
        directory=self.root/'fifo-auth';directory.mkdir(mode=0o700);os.mkfifo(directory/auth.TOKEN_FILE,0o600)
        process=subprocess.Popen(command+[str(directory)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env,start_new_session=True)
        try:
            with selectors.DefaultSelector() as selector:
                selector.register(process.stdout,selectors.EVENT_READ)
                self.assertTrue(selector.select(timeout=5),'owned child failed to reach read handshake')
                self.assertEqual(process.stdout.readline(),'calling-token-read\n')
            with self.assertRaises(subprocess.TimeoutExpired):process.wait(timeout=.25)
        finally:
            if process.poll() is None:os.killpg(process.pid,signal.SIGKILL)
            out,err=process.communicate(timeout=5)
        self.assertLess(process.returncode,0);self.assertNotIn('returned',out);self.assertEqual(err,'')
        OBSERVATIONS.append({'id':'F32','fixed':False,'actual_ensure_access_token_in_owned_child':True,
            'regular_file_control_returned':True,'fifo_has_no_writer':True,'fifo_call_did_not_return_before_external_cleanup':True,
            'owned_child_killed_and_reaped':True,'real_credentials_used':False,'unauthorized_remote_exploit_proven':False,
            'full_bootstrap_executed':False,'deadline_is_test_containment_not_performance_measurement':True})


if __name__=='__main__':unittest.main()
