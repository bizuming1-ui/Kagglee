"""Actual CPU process/FD/flock lifecycle. NO GPU reservation hardware evidence."""
import io
import json
import multiprocessing
import os
from pathlib import Path
import select
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock,patch

ROOT=Path(__file__).resolve().parents[1]/'source'
TEMP=tempfile.TemporaryDirectory(prefix='qtts-ownership-env-')
os.environ.setdefault('QTTS_STATE',TEMP.name);os.environ.setdefault('QTTS_MOCK','1')
sys.path.insert(0,str(ROOT/'py'))
import gpu_ownership as gpu
import supervisor
from resource_limits import UploadRejected
TOOL=ROOT/'tools/resource_control.py'


def wait_line(process):
    if not select.select([process.stdout],[],[],8)[0]:raise AssertionError('child readiness deadline')
    line=process.stdout.readline()
    if not line:raise AssertionError('child exited before readiness')
    return line


def stop(process):
    if process.poll() is None:
        process.terminate()
        try:process.wait(5)
        except subprocess.TimeoutExpired:process.kill();process.wait(5)
    if process.stdout is not None:process.stdout.close()
    if process.stdin is not None:process.stdin.close()


class OwnershipTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.base=Path(self.temp.name);self.root=self.base/'ownership'
        supervisor.STOP.clear();self.addCleanup(supervisor.STOP.clear)

    def reject(self,fn,*args,**kwargs):
        with self.assertRaises(UploadRejected):fn(*args,**kwargs)

    def test_default_namespace_ignores_state_and_cuda_aliases(self):
        first=gpu.default_root()
        with patch.dict(os.environ,{'QTTS_STATE':'/unrelated','CUDA_VISIBLE_DEVICES':'GPU-alias','QTTS_GPU_LOCK_DIR':'/ignored'}):
            self.assertEqual(gpu.default_root(),first)

    def test_exclusive_modes_permissions_and_idempotent_close(self):
        with gpu.GpuLease.acquire('inference',root=self.root) as lease:
            self.assertTrue(gpu.status(root=self.root)['busy'])
            for mode in ('inference','offline-reservation'):self.reject(gpu.GpuLease.acquire,mode,root=self.root)
            self.assertEqual(self.root.stat().st_mode&0o777,0o700);self.assertEqual((self.root/'fleet.lock').stat().st_mode&0o777,0o600)
        lease.close();self.assertFalse(gpu.status(root=self.root)['busy'])
        with gpu.GpuLease.acquire('offline-reservation',root=self.root):pass

    def test_fresh_status_does_not_create_files(self):
        self.assertFalse(gpu.status(root=self.root)['busy']);self.assertFalse(self.root.exists())

    def test_dead_pid_expired_record_never_overrides_lock(self):
        with gpu.GpuLease.acquire('inference',root=self.root) as lease:
            record={**lease.record,'pid':999999999,'created':1}
            os.ftruncate(lease.fd,0);os.pwrite(lease.fd,json.dumps(record).encode(),0)
            result=gpu.status(root=self.root);self.assertTrue(result['busy']);self.assertFalse(result['record_is_authoritative']);self.assertFalse(result['gpu_verified'])
            self.reject(gpu.GpuLease.acquire,'offline-reservation',root=self.root)

    def test_broken_diagnostic_does_not_unlock_owner(self):
        with gpu.GpuLease.acquire('inference',root=self.root) as lease:
            os.ftruncate(lease.fd,0);os.pwrite(lease.fd,b'not json',0)
            result=gpu.status(root=self.root);self.assertTrue(result['busy']);self.assertIsNone(result['last_record'])
            self.reject(gpu.GpuLease.acquire,'offline-reservation',root=self.root)
        with gpu.GpuLease.acquire('inference',root=self.root):pass

    def test_bad_kind_and_descriptor_fields(self):
        self.reject(gpu.GpuLease.acquire,'training',root=self.root)
        for fd,nonce in [(True,'a'*32),(0,'a'*32),(-1,'a'*32),(1<<25,'a'*32),(3,'wrong')]:self.reject(gpu.GpuLease.adopt,fd,nonce,root=self.root)

    def test_symlink_root_file_hardlink_and_fifo_rejected(self):
        target=self.base/'target';target.mkdir();self.root.symlink_to(target)
        self.reject(gpu.GpuLease.acquire,'inference',root=self.root);self.root.unlink();self.root.mkdir(mode=0o700)
        lock=self.root/'fleet.lock';outside=self.base/'outside';outside.write_bytes(b'x');lock.symlink_to(outside)
        self.reject(gpu.GpuLease.acquire,'inference',root=self.root);lock.unlink();lock.hardlink_to(outside)
        self.reject(gpu.GpuLease.acquire,'inference',root=self.root);lock.unlink();os.mkfifo(lock)
        self.reject(gpu.GpuLease.acquire,'inference',root=self.root)

    def test_status_rejects_changed_permissions(self):
        with gpu.GpuLease.acquire('inference',root=self.root):
            (self.root/'fleet.lock').chmod(0o644);self.reject(gpu.status,root=self.root)

    def test_adopt_shared_description_parent_close_not_unlock(self):
        owner=gpu.GpuLease.acquire('inference',root=self.root)
        adopted=gpu.GpuLease.adopt(owner.fd,owner.record['nonce'],root=self.root)
        try:
            owner.close();self.assertTrue(gpu.status(root=self.root)['busy'])
            self.reject(gpu.GpuLease.acquire,'offline-reservation',root=self.root)
        finally:adopted.close();owner.close()
        self.assertFalse(gpu.status(root=self.root)['busy'])

    def test_bad_nonce_or_inode_does_not_release_parent(self):
        with gpu.GpuLease.acquire('inference',root=self.root) as owner:
            self.reject(gpu.GpuLease.adopt,owner.fd,'f'*32,root=self.root)
            other=os.open(self.base/'other',os.O_RDWR|os.O_CREAT,0o600)
            try:self.reject(gpu.GpuLease.adopt,other,owner.record['nonce'],root=self.root)
            finally:os.close(other)
            self.assertTrue(gpu.status(root=self.root)['busy'])

    def test_unlocked_fresh_descriptor_cannot_adopt_stale_record(self):
        owner=gpu.GpuLease.acquire('inference',root=self.root);nonce=owner.record['nonce'];owner.close()
        fd=os.open(self.root/'fleet.lock',os.O_RDWR)
        try:self.reject(gpu.GpuLease.adopt,fd,nonce,root=self.root)
        finally:os.close(fd)

    def test_offline_lease_cannot_be_adopted_for_inference(self):
        with gpu.GpuLease.acquire('offline-reservation',root=self.root) as owner:
            self.reject(gpu.GpuLease.adopt,owner.fd,owner.record['nonce'],root=self.root)
            self.assertTrue(gpu.status(root=self.root)['busy'])

    def test_mock_guard_skips_without_gpu_claim(self):
        with patch.object(gpu.GpuLease,'acquire') as acquire:
            self.assertIsNone(gpu.inference_guard(mock=True));acquire.assert_not_called()

    def test_invalid_environment_does_not_fallback_to_acquire(self):
        for env in ({gpu.FD_ENV:'1'},{gpu.NONCE_ENV:'a'*32},{gpu.FD_ENV:'-3',gpu.NONCE_ENV:'a'*32},{gpu.FD_ENV:'１２',gpu.NONCE_ENV:'a'*32}):
            with patch.dict(os.environ,env,clear=True),patch.object(gpu.GpuLease,'acquire') as acquire:
                self.reject(gpu.inference_guard);acquire.assert_not_called()

    def test_exec_child_holds_after_parent_closes(self):
        owner=gpu.GpuLease.acquire('inference',root=self.root)
        code="import os,sys;sys.path.insert(0,sys.argv[1]);import gpu_ownership as g;l=g.GpuLease.adopt(int(os.environ[g.FD_ENV]),os.environ[g.NONCE_ENV],root=sys.argv[2]);os.close(int(os.environ[g.FD_ENV]));print('ready',flush=True);sys.stdin.readline();l.close()"
        process=subprocess.Popen([sys.executable,'-c',code,str(ROOT/'py'),str(self.root)],env={**os.environ,**owner.export()},pass_fds=(owner.fd,),stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
        try:
            self.assertEqual(wait_line(process).strip(),'ready');owner.close();self.assertTrue(gpu.status(root=self.root)['busy'])
            process.stdin.write('stop\n');process.stdin.flush();process.wait(5)
            self.assertFalse(gpu.status(root=self.root)['busy'])
        finally:owner.close();stop(process)

    def test_sigkill_parent_does_not_unlock_live_exec_child(self):
        childcode="import os,sys,time;sys.path.insert(0,sys.argv[1]);import gpu_ownership as g;l=g.GpuLease.adopt(int(os.environ[g.FD_ENV]),os.environ[g.NONCE_ENV],root=sys.argv[2]);os.close(int(os.environ[g.FD_ENV]));print('child-ready',flush=True);time.sleep(60)"
        parentcode="import os,sys,subprocess,time;sys.path.insert(0,sys.argv[1]);import gpu_ownership as g;l=g.GpuLease.acquire('inference',root=sys.argv[2]);p=subprocess.Popen([sys.executable,'-c',sys.argv[3],sys.argv[1],sys.argv[2]],env={**os.environ,**l.export()},pass_fds=(l.fd,),stdout=subprocess.PIPE,text=True);assert p.stdout.readline().strip()=='child-ready';print(p.pid,flush=True);time.sleep(60)"
        parent=subprocess.Popen([sys.executable,'-c',parentcode,str(ROOT/'py'),str(self.root),childcode],stdout=subprocess.PIPE,text=True,start_new_session=True)
        childpid=None;pidfd=None
        try:
            childpid=int(wait_line(parent));pidfd=os.pidfd_open(childpid);parent.kill();parent.wait(5)
            self.assertTrue(gpu.status(root=self.root)['busy']);self.reject(gpu.GpuLease.acquire,'offline-reservation',root=self.root)
            os.kill(childpid,signal.SIGTERM);self.assertTrue(select.select([pidfd],[],[],5)[0]);self.assertFalse(gpu.status(root=self.root)['busy'])
        finally:
            if childpid is not None:
                try:os.kill(childpid,signal.SIGKILL)
                except ProcessLookupError:pass
            if pidfd is not None:os.close(pidfd)
            stop(parent)

    def test_proc_passes_fd_only_to_model_roles_and_closes_log(self):
        with gpu.GpuLease.acquire('inference',root=self.root) as lease,patch.object(supervisor,'LOG_DIR',self.base):
            for name in ('worker0','analyst','gateway'):
                pr=supervisor.Proc(name,['unused'],{});pr.resource_lease=lease
                with patch.object(supervisor.subprocess,'Popen',return_value=Mock(pid=123)) as popen:
                    pr.start();kwargs=popen.call_args.kwargs
                    self.assertTrue(kwargs['stdout'].closed)
                    self.assertEqual(kwargs['pass_fds'],() if name=='gateway' else (lease.fd,))
                    self.assertEqual(gpu.FD_ENV in kwargs['env'],name!='gateway')

    def test_child_env_scrubs_stale_inherited_capabilities(self):
        with patch.dict(os.environ,{gpu.FD_ENV:'42',gpu.NONCE_ENV:'a'*32}):
            for name in ('gateway','analyst','worker0'):
                env=supervisor.child_environment(name,{})
                self.assertNotIn(gpu.FD_ENV,env);self.assertNotIn(gpu.NONCE_ENV,env)

    def test_stop_prevents_new_start_and_restart(self):
        supervisor.STOP.set();pr=supervisor.Proc('worker0',['unused'],{})
        with patch.object(supervisor.subprocess,'Popen') as popen,patch.object(pr,'kill') as kill:
            pr.start();pr.restart('test-stop');popen.assert_not_called();kill.assert_called_once()

    def test_main_busy_does_not_overwrite_pid_or_start_children(self):
        pid=self.base/'supervisor.pid';pid.write_text('old-pid')
        with patch.object(supervisor,'STATE',self.base),patch.object(supervisor,'MOCK',False),patch.object(supervisor.GpuLease,'acquire',side_effect=UploadRejected('busy',409)),patch.object(supervisor,'build_procs') as build:
            self.assertEqual(supervisor.main(),2);build.assert_not_called();self.assertEqual(pid.read_text(),'old-pid')

    def test_main_installs_handlers_before_start_and_releases_on_stop(self):
        old=signal.getsignal(signal.SIGTERM);pr=Mock(name='controlled-process');pr.name='worker0'
        observed=[]
        def start():observed.append(signal.getsignal(signal.SIGTERM)!=old);supervisor.STOP.set()
        pr.start.side_effect=start
        lease=gpu.GpuLease.acquire('inference',root=self.root)
        with patch.object(supervisor,'STATE',self.base),patch.object(supervisor,'MOCK',False),patch.object(supervisor.GpuLease,'acquire',return_value=lease),patch.object(supervisor,'build_procs',return_value=[pr]),patch.object(supervisor,'ensure_access_token',return_value='synthetic-not-real-token'),patch.object(supervisor,'auth_directory',return_value=self.base):
            self.assertEqual(supervisor.main(),0)
        self.assertEqual(observed,[True]);pr.kill.assert_called_once();self.assertIsNone(lease.fd);self.assertEqual(signal.getsignal(signal.SIGTERM),old);self.assertFalse((self.base/'supervisor.pid').exists())

    def test_partial_start_failure_releases_parent_lease(self):
        pr=Mock();pr.name='worker0';pr.start.side_effect=RuntimeError('injected start failure')
        lease=gpu.GpuLease.acquire('inference',root=self.root)
        with patch.object(supervisor,'STATE',self.base),patch.object(supervisor,'MOCK',False),patch.object(supervisor.GpuLease,'acquire',return_value=lease),patch.object(supervisor,'build_procs',return_value=[pr]),patch.object(supervisor,'ensure_access_token',return_value='synthetic-token'),patch.object(supervisor,'auth_directory',return_value=self.base):
            with self.assertRaises(RuntimeError):supervisor.main()
        pr.kill.assert_called_once();self.assertIsNone(lease.fd);self.assertFalse((self.base/'supervisor.pid').exists())

    def test_proc_kill_reaps_leader_and_kills_surviving_descendant(self):
        code="import subprocess,sys,time;p=subprocess.Popen([sys.executable,'-c','import signal,time;signal.signal(signal.SIGTERM,signal.SIG_IGN);print(1,flush=True);time.sleep(60)'],stdout=subprocess.PIPE);p.stdout.readline();print(p.pid,flush=True);time.sleep(60)"
        process=subprocess.Popen([sys.executable,'-c',code],stdout=subprocess.PIPE,text=True,start_new_session=True)
        pr=supervisor.Proc('test',['unused'],{});pr.p=process;pidfd=None
        try:
            childpid=int(wait_line(process));pidfd=os.pidfd_open(childpid);pr.kill()
            self.assertIsNone(pr.p);self.assertIsNotNone(process.returncode);self.assertTrue(select.select([pidfd],[],[],5)[0])
        finally:
            if pidfd is not None:os.close(pidfd)
            stop(process)

    def test_bootstrap_precheck_never_kills_by_stale_pid_or_name(self):
        import bootstrap
        (self.base/'supervisor.pid').write_text(str(os.getpid()))
        with patch.object(bootstrap,'STATE',self.base),patch.object(bootstrap,'ownership_status',return_value={'busy':False}),patch.object(bootstrap.os,'kill') as kill,patch.object(bootstrap.subprocess,'run') as run:
            self.reject(bootstrap.stop_old);kill.assert_not_called();run.assert_not_called()
            self.assertTrue((self.base/'supervisor.pid').exists())

    def test_bootstrap_busy_stops_before_install_or_gpu_probe(self):
        import bootstrap
        from contextlib import redirect_stdout
        with patch.object(bootstrap,'ownership_status',return_value={'busy':True}),patch.object(bootstrap,'detect_gpus') as detect,patch.object(bootstrap,'pip') as install,redirect_stdout(io.StringIO()):
            self.assertEqual(bootstrap.main(),2);detect.assert_not_called();install.assert_not_called()

    def test_bootstrap_old_health_cannot_mask_new_supervisor_exit(self):
        import bootstrap
        for sequence in ([2],[None,2]):
            process=Mock();process.poll.side_effect=sequence
            with patch.object(bootstrap,'http_json',return_value={'workers_healthy':2}) as health:
                self.assertFalse(bootstrap.wait_ready(2,timeout_s=1,supervisor_process=process))
                if len(sequence)==1:health.assert_not_called()
        process=Mock();process.poll.return_value=None
        with patch.object(bootstrap,'http_json',return_value={'workers_healthy':2}):self.assertTrue(bootstrap.wait_ready(2,timeout_s=1,supervisor_process=process))


class ProductionEntryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.state=Path(self.temp.name)
        self.env={**os.environ,'QTTS_STATE':str(self.state),'QTTS_ROOT':str(ROOT),'QTTS_MOCK':'0'}
        self.env.pop(gpu.FD_ENV,None);self.env.pop(gpu.NONCE_ENV,None)

    def test_real_worker_and_analyst_refuse_offline_holder_before_torch(self):
        modules=self.state/'modules';modules.mkdir();marker=self.state/'unexpected-torch'
        (modules/'torch.py').write_text('from pathlib import Path\nPath('+repr(str(marker))+').touch()\nraise RuntimeError("must not reach torch")')
        with gpu.GpuLease.acquire('offline-reservation'):
            for name in ('worker.py','analyst.py'):
                result=subprocess.run([sys.executable,str(ROOT/'py'/name)],env={**self.env,'PYTHONPATH':str(modules)},capture_output=True,text=True,timeout=10)
                self.assertNotEqual(result.returncode,0);self.assertIn('GPU fleet ownership is busy',result.stderr);self.assertFalse(marker.exists())

    def test_real_second_supervisor_preserves_existing_pid(self):
        path=self.state/'supervisor.pid';path.write_text('12345')
        with gpu.GpuLease.acquire('offline-reservation'):
            result=subprocess.run([sys.executable,str(ROOT/'py/supervisor.py')],env=self.env,capture_output=True,text=True,timeout=10)
            self.assertEqual(result.returncode,2,result.stdout+result.stderr);self.assertEqual(path.read_text(),'12345')

    def test_resource_cli_busy_and_observation(self):
        with gpu.GpuLease.acquire('inference'):
            result=subprocess.run([sys.executable,str(TOOL),'reserve','--seconds','1'],capture_output=True,text=True,timeout=5)
            self.assertEqual(result.returncode,2);self.assertEqual(json.loads(result.stdout)['status'],'rejected')
            result=subprocess.run([sys.executable,str(TOOL),'status'],capture_output=True,text=True,timeout=5)
            self.assertTrue(json.loads(result.stdout)['busy']);self.assertFalse(json.loads(result.stdout)['gpu_verified'])

    def test_resource_cli_timed_reservation_releases(self):
        result=subprocess.run([sys.executable,str(TOOL),'reserve','--seconds','1'],capture_output=True,text=True,timeout=5)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr);rows=[json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([r['status'] for r in rows],['offline_reserved','released']);self.assertFalse(gpu.status()['busy'])

    def test_resource_cli_sigterm_and_sigkill_release(self):
        for sig in (signal.SIGTERM,signal.SIGKILL):
            process=subprocess.Popen([sys.executable,str(TOOL),'reserve','--seconds','30'],stdout=subprocess.PIPE,text=True)
            try:
                self.assertEqual(json.loads(wait_line(process))['status'],'offline_reserved');self.assertTrue(gpu.status()['busy'])
                process.send_signal(sig);process.wait(5);self.assertFalse(gpu.status()['busy'])
                self.assertEqual(process.returncode,130 if sig==signal.SIGTERM else -signal.SIGKILL)
            finally:stop(process)

    def test_resource_cli_rejects_invalid_deadlines_and_arbitrary_commands(self):
        for args in (['reserve','--seconds','0'],['reserve','--seconds','3601'],['reserve','--seconds','1','--command','arbitrary'],['status','--root','/tmp/other']):
            result=subprocess.run([sys.executable,str(TOOL),*args],capture_output=True,text=True,timeout=5);self.assertEqual(result.returncode,2)


if __name__=='__main__':unittest.main()
