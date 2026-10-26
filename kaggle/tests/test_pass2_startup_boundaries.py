"""Pass2 startup/ownership: 10 protections + 2 OBSERVED_NOT_FIXED cases.
Only CPU subprocesses/files/signals and explicit health/metadata/IO fixtures.
Never runs the complete bootstrap installer, model download, GPU or compiler.
"""
from contextlib import ExitStack,redirect_stdout
import io
import json
import os
from pathlib import Path
import select
import signal
import subprocess
import sys
import tempfile
import threading
import time
from types import SimpleNamespace as NS
import unittest
from unittest.mock import Mock,patch
import test_reliability
import bootstrap
import supervisor
import gpu_ownership as gpu
import test_probe
from resource_limits import UploadRejected

probe=test_probe.probe
OBSERVATIONS=[]
ROOT=Path(__file__).resolve().parents[1]/'source'


class StartupBoundaries(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)

    def test_protect_bootstrap_checks_every_reviewed_pin_before_runtime_probe(self):
        class StopAtProbe(Exception):pass
        for mismatch in (None,*bootstrap.PINS):
            versions=dict(bootstrap.PINS)
            if mismatch:versions[mismatch]='unreviewed-fixture'
            def sh(cmd,**kwargs):
                self.assertEqual(Path(cmd[1]).name,'backend_probe.py');self.assertIn('--runtime',cmd)
                self.assertEqual(kwargs['timeout'],150);raise StopAtProbe()
            with self.subTest(mismatch=mismatch),ExitStack() as stack:
                stack.enter_context(patch.object(bootstrap,'STATE',self.root))
                stack.enter_context(patch.object(bootstrap,'stop_old'))
                stack.enter_context(patch.object(bootstrap,'print_memo'))
                stack.enter_context(patch.object(bootstrap,'detect_gpus',return_value=2))
                stack.enter_context(patch.object(bootstrap,'installed_version',side_effect=versions.get))
                install=stack.enter_context(patch.object(bootstrap,'install_reviewed_faster'))
                stack.enter_context(patch.object(bootstrap,'can_import',return_value=True))
                stack.enter_context(patch.object(bootstrap,'pip'))
                stack.enter_context(patch.object(bootstrap,'cuda_lib_paths',return_value=''))
                stack.enter_context(patch.object(bootstrap,'ensure_access_token',return_value='x'*40))
                stack.enter_context(patch.object(bootstrap,'sh',side_effect=sh))
                downloads=stack.enter_context(patch.object(bootstrap,'preload_models'))
                stack.enter_context(patch.dict(os.environ,{'QTTS_TTS_ENGINE':'faster','QTTS_ALLOW_SINGLE_GPU':'0'}))
                stack.enter_context(redirect_stdout(io.StringIO()))
                with self.assertRaises(StopAtProbe):bootstrap.main()
                self.assertEqual(install.call_count,int(mismatch is not None));downloads.assert_not_called()
        # Metadata and dependency installation are fixtures, not a real pinned GPU runtime.

    def test_protect_reviewed_install_exact_pins_platform_constraints_and_cleanup(self):
        versions={'torch':'2.fixture','torchaudio':'audio.fixture','torchvision':'vision.fixture'};captured=[]
        def pip(*args):
            path=Path(args[args.index('--constraint')+1]);captured.append((args,path,path.read_text()))
            self.assertEqual(path.stat().st_mode&0o777,0o600)
            self.assertEqual(path.parent.parent,self.root)
        with patch.object(bootstrap,'STATE',self.root),patch.object(bootstrap,'installed_version',side_effect=versions.get),patch.object(bootstrap,'pip',side_effect=pip):
            bootstrap.install_reviewed_faster()
        args,path,raw=captured[0]
        self.assertEqual(args[:3],tuple(k+'=='+v for k,v in bootstrap.PINS.items()))
        self.assertEqual(raw,'torch==2.fixture\ntorchaudio==audio.fixture\ntorchvision==vision.fixture\n')
        self.assertFalse(path.parent.exists())

    def test_protect_reviewed_install_detects_torch_change_and_removes_constraints(self):
        versions=iter(['2.fixture','changed.fixture']);paths=[]
        def version(name):return next(versions) if name=='torch' else None
        def pip(*args):paths.append(Path(args[args.index('--constraint')+1]))
        with patch.object(bootstrap,'STATE',self.root),patch.object(bootstrap,'installed_version',side_effect=version),patch.object(bootstrap,'pip',side_effect=pip):
            with self.assertRaisesRegex(RuntimeError,'platform Torch changed unexpectedly'):bootstrap.install_reviewed_faster()
        self.assertEqual(len(paths),1);self.assertFalse(paths[0].parent.exists())

    def test_protect_probe_atomic_failure_keeps_previous_report_and_removes_temp(self):
        output=self.root/'report.json';probe.write_report(output,{'fixture':'previous'});before=output.read_bytes()
        with patch.object(probe.os,'replace',side_effect=OSError('fixture publish failure')),self.assertRaisesRegex(OSError,'fixture publish failure'):
            probe.write_report(output,{'fixture':'new'})
        self.assertEqual(output.read_bytes(),before);self.assertEqual(list(self.root.iterdir()),[output])
        self.assertEqual(output.stat().st_mode&0o777,0o600)

    def test_protect_probe_oversize_and_malformed_child_reports_fail_closed(self):
        for raw in (b' '*((256<<10)+1),b'{',b'{"schema":1,"status":"surface_preflight_passed","checks":"bad"}'):
            def spawn(cmd,**kwargs):
                Path(cmd[cmd.index('--output')+1]).write_bytes(raw)
                self.assertIs(kwargs['stdout'],subprocess.DEVNULL);self.assertIs(kwargs['stderr'],subprocess.DEVNULL)
                return NS(wait=lambda timeout:0)
            with self.subTest(size=len(raw)),patch.object(probe.subprocess,'Popen',side_effect=spawn):
                result=probe.isolated_runtime(2,'fp16',1)
            self.assertEqual(result['status'],'blocked')
            self.assertTrue(any(c['name']=='runtime_child' for c in result['checks']))
            self.assertFalse(result['model_loaded'])

    def test_protect_stale_failure_nonce_does_not_block_current_healthy_receipt(self):
        (self.root/'startup-failure.json').write_text(json.dumps({'startup_id':'different-startup','kind':'fixture'}))
        with patch.object(bootstrap,'STATE',self.root),patch.object(bootstrap,'http_json',return_value={'workers_healthy':2}) as health:
            self.assertTrue(bootstrap.wait_ready(2,timeout_s=1,supervisor_process=NS(poll=lambda:None)))
        health.assert_called_once()

    def test_protect_closed_gpu_lease_cannot_start_model_role(self):
        lease=gpu.GpuLease.acquire('inference',root=self.root/'gpu');lease.close()
        proc=supervisor.Proc('worker0',['unused'],{});proc.resource_lease=lease
        with patch.object(supervisor,'STOP',threading.Event()),patch.object(supervisor.subprocess,'Popen') as spawn:
            with self.assertRaisesRegex(UploadRejected,'lease already closed'):proc.start()
        spawn.assert_not_called();self.assertIsNone(proc.p);self.assertFalse(gpu.status(root=self.root/'gpu')['busy'])

    def test_protect_start_oserror_closes_log_without_releasing_supervisor_lease(self):
        with gpu.GpuLease.acquire('inference',root=self.root/'gpu') as lease:
            proc=supervisor.Proc('worker0',['unused'],{});proc.resource_lease=lease;logs=[]
            def fail(cmd,**kwargs):logs.append(kwargs['stdout']);raise OSError('fixture spawn failure')
            with patch.object(supervisor,'STOP',threading.Event()),patch.object(supervisor,'LOG_DIR',self.root),patch.object(supervisor.subprocess,'Popen',side_effect=fail):proc.start()
            self.assertTrue(proc.gave_up);self.assertIsNone(proc.p);self.assertTrue(logs[0].closed)
            self.assertTrue(gpu.status(root=self.root/'gpu')['busy'])
        self.assertFalse(gpu.status(root=self.root/'gpu')['busy'])

    def test_protect_restart_budget_discards_old_entries_and_stops_at_seventh_recent(self):
        proc=supervisor.Proc('fixture',['unused'],{});now=time.time()
        proc.restarts=[now-700]+[now-10]*6
        with patch.object(supervisor,'STOP',threading.Event()),patch.object(proc,'kill') as kill,patch.object(proc,'start') as start:
            proc.restart('fixture budget')
        self.assertTrue(proc.gave_up);self.assertEqual(len(proc.restarts),7)
        self.assertTrue(all(now-t<600 for t in proc.restarts));kill.assert_called_once();start.assert_not_called()

    def test_protect_watch_uses_distinct_streaming_and_buffered_stall_thresholds(self):
        for mode,stalled,restarts in (('streaming',90,0),('streaming',91,1),('sentence-buffered',180,0),('sentence-buffered',181,1)):
            stop=threading.Event();proc=supervisor.Proc('worker0',['unused'],{},'http://fixture/health');proc.p=NS(poll=lambda:None)
            health={'ready':False,'busy':True,'stalled_s':stalled,'model_output_mode':mode}
            with self.subTest(mode=mode,stalled=stalled),patch.object(supervisor,'STOP',stop),patch.object(stop,'wait',side_effect=lambda *_:stop.set()),patch.object(supervisor,'STATE',self.root),patch.object(supervisor,'http_json',return_value=health),patch.object(proc,'restart') as restart:
                supervisor.watch([proc]);self.assertEqual(restart.call_count,restarts)

    def test_observed_shell_timeout_skips_exited_leader_descendant_holding_stdout(self):
        child="import os,json,sys,time;from pathlib import Path;Path(sys.argv[1]).write_text(json.dumps({'pid':os.getpid(),'pgid':os.getpgrp()}));time.sleep(30)"
        leader="import subprocess,sys,time;from pathlib import Path;p=subprocess.Popen([sys.executable,'-c',sys.argv[1],sys.argv[2]]);end=time.monotonic()+3\nwhile not Path(sys.argv[2]).exists():\n assert time.monotonic()<end;time.sleep(.01)"
        wrapper=r'''
import os,json,sys,signal,subprocess
from pathlib import Path
import bootstrap
original=subprocess.Popen
fd=None
signal.signal(signal.SIGTERM,lambda *_:(_ for _ in ()).throw(SystemExit(99)))
def observe(*args,**kwargs):
 global fd
 p=original(*args,**kwargs)
 p.wait(timeout=5) # controlled schedule: leader is reaped before timer arming
 row=json.loads((Path(sys.argv[3])/'child.json').read_text())
 assert row['pgid']==p.pid
 fd=os.pidfd_open(row['pid'])
 print(json.dumps({'leader':p.pid,'child':row['pid'],'leader_reaped':p.returncode==0}),flush=True)
 return p
bootstrap.subprocess.Popen=observe
try:
 rc=bootstrap.sh([sys.executable,'-c',sys.argv[1],sys.argv[2],str(Path(sys.argv[3])/'child.json')],timeout=.1,quiet=True)
 print(json.dumps({'shell_returned':True,'rc':rc}),flush=True)
finally:
 if fd is not None:
  try:signal.pidfd_send_signal(fd,signal.SIGKILL)
  except ProcessLookupError:pass
  os.close(fd)
'''
        env={**os.environ,'PYTHONPATH':str(ROOT/'py'),'QTTS_STATE':str(self.root/'state')}
        process=subprocess.Popen([sys.executable,'-c',wrapper,leader,child,str(self.root)],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=True)
        fd=None;rest='';stderr=''
        try:
            self.assertTrue(select.select([process.stdout],[],[],6)[0],'wrapper readiness deadline')
            row=json.loads(process.stdout.readline());self.assertTrue(row['leader_reaped'])
            fd=os.pidfd_open(row['child'])
            with self.assertRaises(subprocess.TimeoutExpired):process.communicate(timeout=.35)
            self.assertIsNone(process.poll());self.assertFalse(select.select([fd],[],[],0)[0])
            signal.pidfd_send_signal(fd,signal.SIGKILL)
            self.assertTrue(select.select([fd],[],[],5)[0])
            rest,stderr=process.communicate(timeout=5)
            self.assertEqual(process.returncode,0,stderr)
            self.assertEqual(json.loads(rest.strip()),{'shell_returned':True,'rc':0})
        finally:
            if fd is not None:
                try:signal.pidfd_send_signal(fd,signal.SIGKILL)
                except ProcessLookupError:pass
                self.assertTrue(select.select([fd],[],[],5)[0]);os.close(fd)
            if process.poll() is None:process.terminate()
            try:process.communicate(timeout=6)
            except subprocess.TimeoutExpired:process.kill();process.communicate(timeout=3)
        OBSERVATIONS.append({'id':'F21','fixed':False,'actual_cpu_process_pipe_timer_and_pidfd':True,
            'controlled_leader_reaped_before_timer':True,'requested_deadline_did_not_finish_shell':True,
            'descendant_held_stdout_after_leader_exit':True,'external_descendant_cleanup_required':True,
            'shell_returned_zero_after_external_cleanup':True,'fixture_descendant_exit_verified':True,
            'actual_bootstrap_install_download_or_model_executed':False})

    def test_observed_fatal_receipt_io_failure_prevents_worker_stop_and_counter_accumulation(self):
        stop=threading.Event();passes=[]
        def advance(*_):
            passes.append(True)
            if len(passes)>=8:stop.set()
        proc=supervisor.Proc('worker0',['unused'],{},'http://fixture/health');proc.p=NS(poll=lambda:None);proc.started_at=time.time()-2000
        with patch.object(supervisor,'STOP',stop),patch.object(stop,'wait',side_effect=advance),patch.object(supervisor,'STATE',self.root),patch.object(supervisor,'http_json',return_value={'fatal_error':True,'error':'fixture fatal config'}),patch.object(supervisor,'write_json_atomic',side_effect=OSError('fixture receipt IO')) as write,patch.object(proc,'kill') as kill,patch.object(proc,'restart') as restart:
            supervisor.watch([proc]);self.assertEqual(write.call_count,8)
            kill.assert_not_called();restart.assert_not_called()
        self.assertEqual(len(passes),8);self.assertEqual(proc.fail_count,1);self.assertFalse(proc.gave_up)
        self.assertFalse((self.root/'startup-failure.json').exists())
        OBSERVATIONS.append({'id':'F22','fixed':False,'original_watch_executed':True,
            'fatal_health_and_receipt_io_are_fixtures':True,'watch_iterations':8,'fatal_receipt_attempts':8,
            'worker_kill_calls':0,'restart_calls':0,'final_health_fail_count':1,'gave_up':False,
            'actual_worker_process_or_gpu_executed':False})


if __name__=='__main__':unittest.main()
