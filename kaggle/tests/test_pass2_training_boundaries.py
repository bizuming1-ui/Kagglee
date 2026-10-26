"""Second semantic-pass contracts. CPU/OFD/process/AST only, no tensor training.
The stop_ranks witness asserts an unfixed helper gap with an extra descendant;
production ranks currently use no DataLoader subprocesses. Do not infer GPU failure.
"""
import ast
import copy
import io
from contextlib import redirect_stdout
import os
from pathlib import Path
import random
import select
import signal
import subprocess
import sys
import tempfile
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import test_reliability
import training_job as job
import gpu_ownership as gpu
from resource_limits import UploadRejected

ROOT=Path(__file__).resolve().parents[1]/'source'
OBSERVATIONS=[]


def extract(file,name,namespace):
    tree=ast.parse((ROOT/'py'/file).read_bytes())
    node=copy.deepcopy(next(n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name==name))
    module=ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0),node],type_ignores=[])
    exec(compile(ast.fix_missing_locations(module),str(ROOT/'py'/file),'exec'),namespace)
    return namespace[name]


def ready_line(process):
    if not select.select([process.stdout],[],[],5)[0]:raise AssertionError('fixture readiness deadline')
    line=process.stdout.readline()
    if not line:raise AssertionError('fixture exited before readiness')
    return line


class Pass2TrainingBoundaryTests(unittest.TestCase):
    def test_observed_stop_ranks_leaves_term_ignoring_descendant_holding_ofd(self):
        # All PIDs/groups are created here. Never signal a saved PID or unrelated group.
        child_code="import signal,time;signal.signal(signal.SIGTERM,signal.SIG_IGN);print('ready',flush=True);time.sleep(60)"
        leader_code="import subprocess,sys,time;p=subprocess.Popen([sys.executable,'-c',sys.argv[2]],stdout=subprocess.PIPE,text=True,pass_fds=(int(sys.argv[1]),));p.stdout.readline();print(p.pid,flush=True);time.sleep(60)"
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)/'gpu';lease=gpu.GpuLease.acquire('offline-reservation',root=root)
            leader=None;pidfd=None
            try:
                leader=subprocess.Popen([sys.executable,'-c',leader_code,str(lease.fd),child_code],
                    pass_fds=(lease.fd,),stdout=subprocess.PIPE,text=True,start_new_session=True)
                pidfd=os.pidfd_open(int(ready_line(leader)))
                job.stop_ranks([leader])
                self.assertIsNotNone(leader.returncode)
                self.assertFalse(select.select([pidfd],[],[],0)[0])
                lease.close()
                self.assertTrue(gpu.status(root=root)['busy'])
                OBSERVATIONS.append({'id':'F16','leader_reaped':True,'extra_descendant_alive_after_stop':True,
                    'fleet_lock_busy_after_parent_reference_closed':True,'actual_cpu_process_and_flock':True,
                    'production_rank_or_dataloader_executed':False,'extra_descendant_is_explicit_fixture':True,'fixed':False})
            finally:
                if leader is not None:
                    try:os.killpg(leader.pid,signal.SIGKILL)
                    except ProcessLookupError:pass
                    leader.wait(timeout=5)
                    if leader.stdout is not None:leader.stdout.close()
                if pidfd is not None:
                    exited=bool(select.select([pidfd],[],[],5)[0]);os.close(pidfd)
                    self.assertTrue(exited,'fixture descendant cleanup failed')
                lease.close()
            self.assertFalse(gpu.status(root=root)['busy'])

    def test_protect_epoch_partition_complete_equal_and_prefix_padding(self):
        indices=extract('tts_training.py','epoch_indices',{'random':random})
        for world in (2,3,4):
            for count in range(world,33):
                ranks=indices(count,0,17,world)
                self.assertEqual(len(set(map(len,ranks))),1)
                flat=[v for rank in ranks for v in rank]
                self.assertEqual(set(flat),set(range(count)))
                self.assertEqual(len(flat),count+(-count)%world)
                self.assertEqual(len(flat)-len(set(flat)),(-count)%world)

    def test_protect_epoch_order_deterministic_and_too_few_rejected(self):
        indices=extract('tts_training.py','epoch_indices',{'random':random})
        self.assertEqual(indices(17,2,7),indices(17,2,7))
        self.assertNotEqual(indices(17,2,7),indices(17,3,7))
        with self.assertRaises(ValueError):indices(1,0)

    def test_protect_option_integer_types_limits_and_finite_values(self):
        defaults=dict(epochs=1,accumulation=4,max_sequence=1024,lora_rank=8,seed=42,timeout=10,lr=2e-5,lora_alpha=16.,model_sha256='a'*64)
        job.validate_options(NS(**defaults))
        for name,low,high in (('epochs',1,100),('accumulation',1,64),('max_sequence',64,2048),('lora_rank',1,32),('seed',0,2147483647),('timeout',1,21600)):
            for value in (True,False,1.5,low-1,high+1):
                with self.subTest(name=name,value=value),self.assertRaises(UploadRejected):
                    job.validate_options(NS(**dict(defaults,**{name:value})))
            for value in (low,high):job.validate_options(NS(**dict(defaults,**{name:value})))
        for name in ('lr','lora_alpha'):
            for value in (0.,-1.,float('nan'),float('inf')):
                with self.assertRaises(UploadRejected):job.validate_options(NS(**dict(defaults,**{name:value})))

    def test_protect_cli_help_and_missing_required_inputs_do_not_train(self):
        tool=ROOT/'tools/train_tts.py'
        for arguments,expected in ((['--help'],0),(['train'],2),(['fingerprint'],2)):
            cp=subprocess.run([sys.executable,str(tool)]+arguments,capture_output=True,text=True,timeout=10)
            self.assertEqual(cp.returncode,expected)
            self.assertNotIn('Traceback',cp.stderr)

    def test_protect_child_environment_scrubs_enumerated_keys_and_keeps_offline_pin(self):
        names=('QTTS_ACCESS_TOKEN','DEEPSEEK_API_KEY','HF_TOKEN','HUGGING_FACE_HUB_TOKEN','KAGGLE_USERNAME','KAGGLE_KEY','PYTHONPATH')
        with tempfile.TemporaryDirectory() as temporary,gpu.GpuLease.acquire('offline-reservation',root=Path(temporary)/'gpu') as lease:
            with patch.dict(os.environ,{**{name:'synthetic-fixture-value' for name in names},'CUDA_VISIBLE_DEVICES':'2,3',job.CODE_FD:'999'}):
                env=job.child_environment(lease,31)
            self.assertFalse(set(names)&set(env))
            self.assertEqual(env['CUDA_VISIBLE_DEVICES'],'2,3')
            self.assertEqual(env[job.CODE_FD],'31');self.assertEqual(env[gpu.FD_ENV],str(lease.fd))
            self.assertEqual(env[gpu.NONCE_ENV],lease.record['nonce'])
            self.assertEqual((env['HF_HUB_OFFLINE'],env['TRANSFORMERS_OFFLINE'],env['QTTS_MOCK']),('1','1','0'))

    def test_protect_inference_guard_rejects_offline_ofd_without_releasing_holder(self):
        with tempfile.TemporaryDirectory() as temporary,patch.object(gpu,'default_root',return_value=Path(temporary)/'gpu'):
            with gpu.GpuLease.acquire('offline-reservation') as lease,patch.dict(os.environ,lease.export()):
                with self.assertRaises(UploadRejected):gpu.inference_guard()
                self.assertTrue(gpu.status()['busy'])
                os.fstat(lease.fd)
            self.assertFalse(gpu.status()['busy'])

    def test_protect_gpu_adopt_rejects_fresh_same_inode_description(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)/'gpu'
            with gpu.GpuLease.acquire('inference',root=root) as lease:
                fd=os.open(root/'fleet.lock',os.O_RDWR)
                try:
                    with self.assertRaises(UploadRejected):gpu.GpuLease.adopt(fd,lease.record['nonce'],root=root)
                    self.assertTrue(gpu.status(root=root)['busy'])
                finally:os.close(fd)
            self.assertFalse(gpu.status(root=root)['busy'])

    def test_protect_failed_atomic_request_write_preserves_old_and_removes_temp(self):
        with tempfile.TemporaryDirectory() as temporary:
            path=Path(temporary)/'request.json';job.write_json(path,{'old':True})
            before=path.read_bytes()
            with patch.object(job.os,'replace',side_effect=OSError('injected local failure')):
                with self.assertRaises(OSError):job.write_json(path,{'new':True})
            self.assertEqual(path.read_bytes(),before)
            self.assertEqual(list(Path(temporary).iterdir()),[path])
            self.assertEqual(path.stat().st_mode&0o777,0o600)

    def test_protect_stop_ranks_reaps_direct_live_child(self):
        process=subprocess.Popen([sys.executable,'-c',"import time;print('ready',flush=True);time.sleep(60)"],stdout=subprocess.PIPE,text=True,start_new_session=True)
        try:
            ready_line(process);job.stop_ranks([process]);self.assertIsNotNone(process.returncode)
        finally:
            if process.poll() is None:
                os.killpg(process.pid,signal.SIGKILL);process.wait(5)
            process.stdout.close()

    def test_protect_commit_adapter_rolls_back_baseexception_without_tensor_emulation(self):
        commit=extract('lora_adapter.py','commit_adapter',{})
        class Parent:
            def __init__(self):self.a='old-a';self.b='old-b'
            def __setattr__(self,name,value):
                if name=='b' and value=='reject':raise KeyboardInterrupt('fixture setter interruption')
                object.__setattr__(self,name,value)
        parent=Parent()
        with self.assertRaises(KeyboardInterrupt):commit(None,[(parent,'a','new-a'),(parent,'b','reject')])
        self.assertEqual((parent.a,parent.b),('old-a','old-b'))
        commit(None,[(parent,'a','new-a'),(parent,'b','new-b')])
        self.assertEqual((parent.a,parent.b),('new-a','new-b'))

    def test_protect_dataset_constructor_copies_rows_and_bounds_cache_no_tensor_claim(self):
        Dataset=extract('tts_dataset.py','TTSDataset',{'copy':copy})
        rows=[{'text':'original','audio_codes':[[1]*16]}];mel=object()
        data=Dataset(rows,None,None,mel,cache_bytes=0)
        rows[0]['text']='changed';rows[0]['audio_codes'][0][0]=9
        self.assertEqual(data.rows[0]['text'],'original');self.assertEqual(data.rows[0]['audio_codes'][0][0],1)
        self.assertEqual((len(data),data.cache_used,data.tokenizer_calls),(1,0,0))
        self.assertIs(data.reference_mel,mel)
        for budget in (True,-1,(256<<20)+1):
            with self.assertRaises(ValueError):Dataset(rows,None,None,mel,cache_bytes=budget)

if __name__=='__main__':unittest.main()
