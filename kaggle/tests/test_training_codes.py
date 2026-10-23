"""Real local transactions/leases + explicit fixture encoder. No Qwen execution."""
import importlib.util
import io
import json
import math
import multiprocessing
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_training_data import Fixture,wav
import training_codes as tc
import training_data as td
from resource_limits import UploadRejected

TOOL=Path(__file__).resolve().parents[1]/'source/tools/encode_training.py'
spec=importlib.util.spec_from_file_location('encode_training_tool',TOOL)
tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)


def fixture_encoder(waveform):
    return [[i%2048 for i in range(16)] for _ in range(math.ceil(len(waveform)/1920))]


def hold_lease(root,limits,did,sha,ready):
    store=td.TrainingDataStore(root,limits,free_bytes=0)
    with store.lease(did,sha):
        ready.set();signal.pause()


class CodeTests(Fixture,unittest.TestCase):
    def setUp(self):
        Fixture.setUp(self)
        self.codes=tc.TrainingCodesStore(self.state/'training_codes',self.limits,free_bytes=0)
        self.library,self.body=self.source();self.input=self.data.prepare(self.lib,self.body)
        self.did=self.input['id'];self.sha=self.input['manifest_sha256']

    def run_codes(self,**kwargs):return self.codes.prepare(self.data,self.did,self.sha,lambda:fixture_encoder,**kwargs)

    def test_transaction_full_coverage_and_independent_copies(self):
        before=self.data.verify(self.did,self.sha);result=self.run_codes();directory=self.codes.root/result['id']
        self.assertEqual(result['state'],'test_only_codes');self.assertFalse(result['checks']['tokenization_executed'])
        rows=[json.loads(line) for line in (directory/'train_with_codes.jsonl').read_bytes().split(b'\n') if line]
        original=[json.loads(line) for line in (self.data.root/self.did/'train_raw.jsonl').read_bytes().split(b'\n') if line]
        self.assertEqual(len(rows),3)
        for row,raw in zip(rows,original):
            self.assertEqual({k:v for k,v in row.items() if k!='audio_codes'},raw)
            self.assertEqual((directory/row['audio']).read_bytes(),(self.data.root/self.did/raw['audio']).read_bytes())
            self.assertEqual(len(row['audio_codes']),19)
        self.assertEqual(self.data.verify(self.did,self.sha),before)
        self.data.delete(self.did,self.sha)
        self.assertTrue(self.codes.verify(result['id'],result['manifest_sha256'])['integrity_verified_now'])
        self.codes.delete(result['id'],result['manifest_sha256']);self.assertEqual(self.codes.list(),[])

    def test_source_lease_blocks_delete_but_not_other_dataset_list(self):
        with self.data.lease(self.did,self.sha):
            self.reject(409,self.data.delete,self.did,self.sha)
            self.assertEqual(len(self.data.list()),1)
            self.reject(409,lambda:list(self.data.lease(self.did,self.sha).__enter__()))
        self.data.delete(self.did,self.sha)

    def test_process_death_releases_input_lease(self):
        ctx=multiprocessing.get_context('fork');ready=ctx.Event()
        process=ctx.Process(target=hold_lease,args=(self.data.root,self.limits,self.did,self.sha,ready));process.start()
        try:
            self.assertTrue(ready.wait(5));self.reject(409,self.data.delete,self.did,self.sha)
        finally:process.terminate();process.join(5)
        self.assertFalse(process.is_alive());self.data.delete(self.did,self.sha)

    def test_factory_is_under_verified_lease(self):
        def factory():
            self.reject(409,self.data.delete,self.did,self.sha)
            return fixture_encoder
        result=self.codes.prepare(self.data,self.did,self.sha,factory)
        self.assertEqual(result['sample_count'],3)

    def test_bad_pin_does_not_load_model_or_leave_lease(self):
        called=[]
        self.reject(409,self.codes.prepare,self.data,self.did,'f'*64,lambda:called.append(True))
        self.assertEqual(called,[]);self.data.delete(self.did,self.sha)

    def test_cancellation_before_model(self):
        called=[]
        self.reject(409,lambda:self.codes.prepare(self.data,self.did,self.sha,lambda:called.append(True),cancelled=lambda:True))
        self.assertEqual(called,[]);self.assertEqual(self.codes.list(),[])

    def test_cancel_after_encode_rolls_back_and_releases(self):
        stop=[]
        def encoder(waveform):stop.append(True);return fixture_encoder(waveform)
        self.reject(409,lambda:self.codes.prepare(self.data,self.did,self.sha,lambda:encoder,cancelled=lambda:bool(stop)))
        self.assertFalse(list(self.codes.root.glob('.pending-*')));self.data.delete(self.did,self.sha)

    def test_bad_codes_never_publish(self):
        good=fixture_encoder([0]*36000)
        cases=[[],good[:-1],good+[good[0]],[[0]*15]*19,[[0]*17]*19,
               [[True]*16]*19,[[1.0]*16]*19,[[-1]*16]*19,[[2048]*16]*19,[[None]*16]*19,tuple(good)]
        for bad in cases:
            with self.subTest(value=str(bad)[:30]):
                self.reject(409,self.codes.prepare,self.data,self.did,self.sha,lambda:lambda _:bad)
                self.assertEqual(self.codes.list(),[]);self.assertFalse(list(self.codes.root.glob('.pending-*')))

    def test_encoder_failure_and_write_failure_rollback(self):
        def bad(_):raise RuntimeError('private transcript must never escape CLI')
        with self.assertRaises(RuntimeError):self.codes.prepare(self.data,self.did,self.sha,lambda:bad)
        with patch.object(self.codes,'_write',side_effect=OSError('disk full')):
            with self.assertRaises(OSError):self.run_codes()
        self.assertEqual(self.codes.list(),[]);self.assertFalse(list(self.codes.root.glob('.pending-*')))

    def test_rename_failure_preserves_input(self):
        with patch.object(tc.os,'rename',side_effect=OSError('publish failure')):
            with self.assertRaises(OSError):self.run_codes()
        self.assertEqual(self.codes.list(),[]);self.assertTrue(self.data.verify(self.did,self.sha)['integrity_verified_now'])

    def test_quotas_and_orphan_cleanup(self):
        orphan=self.codes.root/('.pending-'+'a'*32);orphan.mkdir();(orphan/'partial').write_bytes(b'x')
        self.codes.per_bytes=100
        self.reject(413,self.run_codes);self.assertFalse(orphan.exists())
        self.codes.per_bytes=64<<20;self.codes.total_bytes=10
        self.reject(413,self.run_codes)
        self.codes.total_bytes=256<<20;self.codes.maximum=1
        result=self.run_codes();self.reject(409,self.run_codes)
        self.codes.delete(result['id'],result['manifest_sha256'])
        self.codes.free_bytes=1<<60;self.reject(507,self.run_codes)

    def test_pinned_output_verify_list_and_delete(self):
        result=self.run_codes();row=self.codes.list()[0]
        self.assertFalse(row['integrity_verified_now']);self.assertNotIn('text',json.dumps(row))
        self.reject(409,self.codes.verify,result['id'],'f'*64)
        self.reject(409,self.codes.delete,result['id'],'f'*64)
        self.assertTrue(self.codes.verify(result['id'],result['manifest_sha256'])['integrity_verified_now'])

    def test_tamper_audio_index_and_membership(self):
        for kind in ('audio','index','extra'):
            result=self.run_codes();root=self.codes.root/result['id']
            if kind=='audio':next((root/'audio').iterdir()).write_bytes(b'changed')
            elif kind=='index':(root/'train_with_codes.jsonl').write_bytes(b'{}\n')
            else:(root/'unexpected').write_bytes(b'x')
            self.reject(409,self.codes.verify,result['id'],result['manifest_sha256'])
            self.codes.delete(result['id'],result['manifest_sha256'])

    def test_source_change_during_encoding_prevents_publication(self):
        def encoder(waveform):
            with open(self.data.root/self.did/'train_raw.jsonl','ab') as out:out.write(b' ')
            return fixture_encoder(waveform)
        self.reject(409,self.codes.prepare,self.data,self.did,self.sha,lambda:encoder)
        self.assertEqual(self.codes.list(),[])

    def test_permissions_and_backup_exclusion(self):
        result=self.run_codes();directory=self.codes.root/result['id']
        for path in [directory,*directory.rglob('*')]:self.assertEqual(path.stat().st_mode&0o777,0o700 if path.is_dir() else 0o600)
        import persist,tarfile
        profile=self.state/'profiles'/'fixture';profile.mkdir(parents=True)
        (profile/'profile.json').write_text('{"fixture":true}')
        (self.state/'active.json').write_text('{"id":"fixture"}')
        with patch.object(persist,'STATE',self.state),patch.object(persist,'PROFILES_DIR',self.state/'profiles'):
            with tarfile.open(persist._pack(self.state/'archive.tar.gz')) as archive:
                members=archive.getnames()
                self.assertIn('profiles/fixture/profile.json',members);self.assertIn('active.json',members)
                self.assertFalse(any('training_codes' in name or 'training_data' in name or 'libraries' in name for name in members))

    def test_symlink_and_hardlink_codes_rejected(self):
        result=self.run_codes();root=self.codes.root/result['id'];path=next((root/'audio').iterdir());copy=root/'outside.wav';path.rename(copy);path.symlink_to(copy)
        self.reject(409,self.codes.verify,result['id'],result['manifest_sha256']);path.unlink();path.hardlink_to(copy)
        self.reject(409,self.codes.verify,result['id'],result['manifest_sha256'])

    def test_cli_list_verify_and_delete_fixture_only(self):
        result=self.run_codes()
        for command in ('list','verify','delete'):
            args=[sys.executable,str(TOOL),command,'--state',str(self.state),'--timeout','15']
            if command!='list':args+=['--id',result['id'],'--manifest-sha256',result['manifest_sha256']]
            completed=subprocess.run(args,capture_output=True,text=True,timeout=20)
            self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr)
            self.assertEqual(json.loads(completed.stdout)['status'],'ok')
            self.assertNotIn('对应第',completed.stdout)

    def test_real_cli_missing_dependencies_blocked_without_output(self):
        if importlib.util.find_spec('torch') is not None and importlib.util.find_spec('qwen_tts') is not None:
            self.skipTest('this negative test requires missing tokenizer dependencies')
        model=self.state/'model';model.mkdir()
        (model/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (model/'model.safetensors').write_bytes(b'fixture-not-real-weights')
        completed=subprocess.run([sys.executable,str(TOOL),'encode','--state',str(self.state),'--id',self.did,
                  '--manifest-sha256',self.sha,'--model-dir',str(model),'--model-sha256',tc.model_fingerprint(model)],capture_output=True,text=True,timeout=15)
        self.assertEqual(completed.returncode,2,completed.stdout+completed.stderr)
        self.assertEqual(json.loads(completed.stdout)['status'],'blocked')
        self.assertEqual(self.codes.list(),[]);self.data.delete(self.did,self.sha)

    def test_real_cli_deadline_kills_worker_and_releases_lease(self):
        # Stall dependency IMPORT, never pretend to encode using a fake model.
        model=self.state/'model';model.mkdir()
        (model/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (model/'model.safetensors').write_bytes(b'fixture-not-real-weights')
        modules=self.state/'modules';modules.mkdir();marker=self.state/'import-entered'
        (modules/'torch.py').write_text('from pathlib import Path\nimport time\nPath('+repr(str(marker))+').touch()\ntime.sleep(60)\n')
        env={**os.environ,'PYTHONPATH':str(modules)}
        completed=subprocess.run([sys.executable,str(TOOL),'encode','--state',str(self.state),'--id',self.did,
                  '--manifest-sha256',self.sha,'--model-dir',str(model),'--model-sha256',tc.model_fingerprint(model),'--timeout','3'],env=env,capture_output=True,text=True,timeout=10)
        self.assertTrue(marker.exists());self.assertEqual(completed.returncode,2,completed.stdout+completed.stderr)
        self.assertEqual(json.loads(completed.stdout)['status'],'timeout')
        self.assertEqual(self.codes.list(),[]);self.data.delete(self.did,self.sha)

    def test_real_cli_sigterm_cancel_releases_lease(self):
        import time
        model=self.state/'model';model.mkdir()
        (model/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (model/'model.safetensors').write_bytes(b'fixture-not-real-weights')
        modules=self.state/'modules';modules.mkdir();marker=self.state/'import-entered'
        (modules/'torch.py').write_text('from pathlib import Path\nimport time\nPath('+repr(str(marker))+').touch()\ntime.sleep(60)\n')
        process=subprocess.Popen([sys.executable,str(TOOL),'encode','--state',str(self.state),'--id',self.did,
                  '--manifest-sha256',self.sha,'--model-dir',str(model),'--model-sha256',tc.model_fingerprint(model),'--timeout','15'],
                  env={**os.environ,'PYTHONPATH':str(modules)},stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            deadline=time.monotonic()+5
            while not marker.exists() and time.monotonic()<deadline:time.sleep(.02)
            self.assertTrue(marker.exists());process.terminate();stdout,stderr=process.communicate(timeout=10)
            self.assertEqual(process.returncode,130,stdout+stderr);self.assertEqual(json.loads(stdout)['status'],'cancelled')
            self.data.delete(self.did,self.sha);self.assertEqual(self.codes.list(),[])
        finally:
            if process.poll() is None:process.kill();process.wait(5)
            process.stdout.close();process.stderr.close()

    def test_sigkill_controller_kills_encoder_and_releases_input(self):
        import select,time
        model=self.state/'model';model.mkdir()
        (model/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (model/'model.safetensors').write_bytes(b'fixture-not-real-weights')
        modules=self.state/'modules';modules.mkdir();marker=self.state/'encoder-pid'
        (modules/'torch.py').write_text('from pathlib import Path\nimport time,os\nPath('+repr(str(marker))+').write_text(str(os.getpid()))\ntime.sleep(60)\n')
        process=subprocess.Popen([sys.executable,str(TOOL),'encode','--state',str(self.state),'--id',self.did,
                  '--manifest-sha256',self.sha,'--model-dir',str(model),'--model-sha256',tc.model_fingerprint(model),'--timeout','15'],
                  env={**os.environ,'PYTHONPATH':str(modules)},stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        pidfd=None
        try:
            deadline=time.monotonic()+5
            while not marker.exists() and time.monotonic()<deadline:time.sleep(.02)
            self.assertTrue(marker.exists());pid=int(marker.read_text());pidfd=os.pidfd_open(pid)
            self.reject(409,self.data.delete,self.did,self.sha)
            process.kill();process.wait(5)
            self.assertTrue(select.select([pidfd],[],[],5)[0],'orphan encoder must die with controller')
            self.data.delete(self.did,self.sha);self.assertEqual(self.codes.list(),[])
        finally:
            if process.poll() is None:process.kill();process.wait(5)
            if pidfd is not None:os.close(pidfd)


class ModelTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        (self.root/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (self.root/'model.safetensors').write_bytes(b'test-only-not-real-weights')

    def test_fingerprint_deterministic_and_changes(self):
        first=tc.model_fingerprint(self.root);self.assertEqual(first,tc.model_fingerprint(self.root))
        (self.root/'model.safetensors').write_bytes(b'changed');self.assertNotEqual(first,tc.model_fingerprint(self.root))

    def test_wrong_model_shapes_and_remote_code_rejected(self):
        for update in ({'model_type':'qwen3_tts_tokenizer_25hz'},{'input_sample_rate':48000},{'encoder_valid_num_quantizers':8},
                       {'encoder_config':{'codebook_size':1024}},{'decode_upsample_rate':True},{'auto_map':{}}):
            (self.root/'config.json').write_text(json.dumps({'model_type':'qwen3_tts_tokenizer_12hz',**update}))
            with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root)

    def test_pickle_links_and_index_escape_rejected(self):
        extra=self.root/'pytorch_model.bin';extra.write_bytes(b'pickle')
        with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root)
        extra.unlink();extra=self.root/'linked.safetensors';extra.symlink_to(self.root/'model.safetensors')
        with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root)
        extra.unlink();extra.hardlink_to(self.root/'model.safetensors')
        with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root)
        extra.unlink();index=self.root/'model.safetensors.index.json';index.write_text('{"weight_map":{"x":"../outside.safetensors"}}')
        with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root)

    def test_missing_model_and_bad_pin_no_dependency_load(self):
        with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root/'missing')
        with self.assertRaises(UploadRejected) as e:tc.QwenCPUEncoder(self.root,'f'*64)
        self.assertEqual(e.exception.code,409)

    def test_adapter_refuses_missing_or_multiple_sample_results(self):
        from types import SimpleNamespace
        obj=object.__new__(tc.QwenCPUEncoder)
        for codes in ([],[object(),object()],None):
            obj.tokenizer=SimpleNamespace(encode=lambda *a,**k:SimpleNamespace(audio_codes=codes))
            with self.assertRaises(UploadRejected):obj([0])

    def test_adapter_loader_contract_with_stub_imports_no_real_model(self):
        from types import SimpleNamespace as NS
        from unittest.mock import Mock
        cfg=NS(model_type='qwen3_tts_tokenizer_12hz',input_sample_rate=24000,output_sample_rate=24000,
               encode_downsample_rate=1920,decode_upsample_rate=1920,encoder_valid_num_quantizers=16,
               encoder_config=NS(codebook_size=2048),decoder_config=NS(codebook_size=2048,num_quantizers=16))
        model=NS(dtype='float32',eval=Mock())
        loaded=NS(config=cfg,device='cpu',model=model,feature_extractor=NS(sampling_rate=24000))
        loader=Mock(return_value=loaded);threads=Mock()
        modules={'torch':NS(float32='float32',set_num_threads=threads),'qwen_tts':NS(Qwen3TTSTokenizer=NS(from_pretrained=loader))}
        with patch.dict(sys.modules,modules),patch.object(tc.importlib.metadata,'version',return_value='stub-only'),patch('qwen_compat.installed_version',return_value=None),patch.dict(os.environ,{}):
            encoder=tc.QwenCPUEncoder(self.root,tc.model_fingerprint(self.root))
            kwargs=loader.call_args.kwargs
            self.assertEqual(kwargs,dict(device_map='cpu',dtype='float32',attn_implementation='eager',local_files_only=True,trust_remote_code=False,use_safetensors=True))
            threads.assert_called_once_with(2);model.eval.assert_called_once()
            cfg.encoder_valid_num_quantizers=8
            with self.assertRaises(UploadRejected):tc.QwenCPUEncoder(self.root,tc.model_fingerprint(self.root))
            (self.root/'model.safetensors').write_bytes(b'changed')
            with self.assertRaises(UploadRejected):encoder.finish()

    def test_sharded_index_only_references_fingerprinted_files(self):
        (self.root/'model.safetensors.index.json').write_text('{"weight_map":{"x":"model.safetensors"}}')
        self.assertEqual(len(tc.model_fingerprint(self.root)),64)
        (self.root/'model.safetensors.index.json').write_text('{"weight_map":{"x":"not-present.safetensors"}}')
        with self.assertRaises(UploadRejected):tc.model_fingerprint(self.root)

    def test_cli_fingerprint_no_model_load(self):
        result=subprocess.run([sys.executable,str(TOOL),'fingerprint','--model-dir',str(self.root)],capture_output=True,text=True,timeout=15)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        value=json.loads(result.stdout)['result'];self.assertFalse(value['model_loaded']);self.assertEqual(value['model_tree_sha256'],tc.model_fingerprint(self.root))

    def test_cli_rejects_missing_directory_without_path_leak(self):
        result=subprocess.run([sys.executable,str(TOOL),'fingerprint','--model-dir',str(self.root/'private-name')],capture_output=True,text=True,timeout=15)
        self.assertEqual(result.returncode,2);self.assertNotIn('private-name',result.stdout+result.stderr)


class ProcessTests(unittest.TestCase):
    def test_timeout_and_cancel_stop_worker_group(self):
        for error,expected in ((subprocess.TimeoutExpired('test',1),2),(KeyboardInterrupt(),130)):
            from unittest.mock import Mock
            process=Mock(pid=123456);process.wait.side_effect=[error,0,0];process.poll.side_effect=[None,0]
            with patch.object(tool.subprocess,'Popen',return_value=process),patch.object(tool.os,'killpg') as kill,context_stdout():
                self.assertEqual(tool.main(['list','--state','unused','--timeout','1']),expected)
                self.assertEqual([c.args[1] for c in kill.call_args_list],[signal.SIGTERM,signal.SIGKILL])

    def test_real_group_termination_kills_descendant_after_leader_exits(self):
        import select
        code="import subprocess,sys,time; p=subprocess.Popen([sys.executable,'-c','import signal,time;signal.signal(signal.SIGTERM,signal.SIG_IGN);print(1,flush=True);time.sleep(60)'],stdout=subprocess.PIPE);p.stdout.readline();print(p.pid,flush=True);time.sleep(60)"
        process=subprocess.Popen([sys.executable,'-c',code],stdout=subprocess.PIPE,text=True,start_new_session=True)
        try:
            self.assertTrue(select.select([process.stdout],[],[],5)[0]);pid=int(process.stdout.readline())
            pidfd=os.pidfd_open(pid)
            try:
                tool.terminate(process);self.assertIsNotNone(process.poll())
                self.assertTrue(select.select([pidfd],[],[],5)[0])
            finally:os.close(pidfd)
            status=Path('/proc')/str(pid)/'stat'
            # Zombie is dead and cannot continue encoding; PID1 reaps orphans.
            try:state=status.read_text().split()[2]
            except (FileNotFoundError,ProcessLookupError):state='gone'
            self.assertIn(state,('Z','X','gone'))
        finally:
            tool.terminate(process);process.stdout.close()

    def test_scrubbed_cpu_offline_environment(self):
        from unittest.mock import Mock
        process=Mock();process.wait.return_value=1;process.poll.return_value=1
        with patch.dict(os.environ,{'QTTS_ACCESS_TOKEN':'private','HF_TOKEN':'private','DEEPSEEK_API_KEY':'private','QTTS_GPU_LEASE_FD':'42','QTTS_GPU_LEASE_NONCE':'test-only'}),patch.object(tool.subprocess,'Popen',return_value=process) as popen,context_stdout():
            self.assertEqual(tool.main(['list','--state','unused']),2)
        env=popen.call_args.kwargs['env'];self.assertEqual(env['CUDA_VISIBLE_DEVICES'],'');self.assertEqual(env['HF_HUB_OFFLINE'],'1')
        for key in ('QTTS_ACCESS_TOKEN','HF_TOKEN','DEEPSEEK_API_KEY','QTTS_GPU_LEASE_FD','QTTS_GPU_LEASE_NONCE'):self.assertNotIn(key,env)


def context_stdout():
    from contextlib import redirect_stdout
    return redirect_stdout(io.StringIO())


if __name__=='__main__':unittest.main()
