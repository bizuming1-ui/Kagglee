"""Actual CPU tensors/optimizer + two-process Gloo. NOT Qwen/CUDA/T4 evidence."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]/'source'
sys.path.insert(0,str(ROOT/'py'))
from resource_limits import UploadRejected
import training_job as job
import test_training_codes as helpers

TORCH=importlib.util.find_spec('torch') is not None
if TORCH:
    import torch
    from torch import nn
    import torch.distributed as dist
    import torch.multiprocessing as mp
    from torch.nn.parallel import DistributedDataParallel as DDP
    from lora_adapter import LoRALinear,inject_lora,adapter_state,adapter_digest,restore_adapter
    from tts_training import JointLoss,epoch_indices,optimize_epoch,load_adapter
    from tts_dataset import TTSDataset


if TORCH:
    class Attention(nn.Module):
        def __init__(self):
            super().__init__();self.q_proj=nn.Linear(4,4);self.v_proj=nn.Linear(4,4)
        def forward(self,x):return self.q_proj(x).tanh()+self.v_proj(x)

    class SubTalker(nn.Module):
        def __init__(self):
            super().__init__();self.embeddings=nn.ModuleList([nn.Embedding(8,4) for _ in range(15)]);self.self_attn=Attention()
        def get_input_embeddings(self):return self.embeddings

    class Talker(nn.Module):
        def __init__(self):
            super().__init__();self.text=nn.Embedding(64,6);self.codec=nn.Embedding(32,4)
            self.text_projection=nn.Linear(6,4);self.self_attn=Attention();self.code_predictor=SubTalker()
        def get_text_embeddings(self):return self.text
        def get_input_embeddings(self):return self.codec
        def forward(self,inputs_embeds,labels,**kwargs):
            hidden=self.self_attn(inputs_embeds);target=labels.clamp(min=0).float();mask=labels!=-100
            loss=((hidden.sum(-1)-target).square()*mask).sum()/mask.sum()
            return NS(loss=loss,hidden_states=([hidden],None))
        def forward_sub_talker_finetune(self,ids,hidden):
            logits=self.code_predictor.self_attn(hidden);return logits,(logits.sum(-1)-ids.float().mean(-1)).square().mean()

    class TinyCore(nn.Module):
        def __init__(self):
            super().__init__();self.talker=Talker();self.speaker_encoder=nn.Linear(4,4)
            self.config=NS(talker_config=NS(hidden_size=4))

    def tiny_data(count=3,max_sequence=128):
        cfg=NS(tts_pad_token_id=0,tts_bos_token_id=1,tts_eos_token_id=2,
               talker_config=NS(codec_nothink_id=3,codec_think_bos_id=4,codec_think_eos_id=5,codec_pad_id=6,codec_bos_id=7,codec_eos_token_id=8))
        def processor(**_):return {'input_ids':torch.tensor([[1,2,3,4,5,6,7,8,9,10,11,12,13,14]])}
        rows=[{'audio':f'a{i}.wav','ref_audio':'a0.wav','text':f'not private real speech {i}','audio_codes':[[i%7]*16 for _ in range(3)]} for i in range(count)]
        return TTSDataset(rows,processor,cfg,torch.zeros(1,3,128),max_sequence)

    def gloo_worker(rank,rendezvous,output):
        torch.set_num_threads(1);torch.manual_seed(11)
        dist.init_process_group('gloo',init_method=rendezvous,rank=rank,world_size=2)
        try:
            core=TinyCore();inject_lora(core,2,4);before=adapter_digest(core)
            task=JointLoss(core,torch.zeros(1,4));model=DDP(task,find_unused_parameters=True,broadcast_buffers=False)
            optimizer=torch.optim.AdamW([p for p in task.parameters() if p.requires_grad],lr=.01)
            reports=[]
            for epoch in range(2):
                reports.append(optimize_epoch(model,tiny_data(),epoch_indices(3,epoch)[rank],optimizer,torch.amp.GradScaler('cpu',enabled=False),torch.device('cpu'),accumulation=3,amp=False))
            after=adapter_digest(core)
            Path(output,f'{rank}.json').write_text(json.dumps({'rank':rank,'before':before,'after':after,'reports':reports}))
        finally:dist.destroy_process_group()


def base_tree(root):
    root.mkdir();(root/'speech_tokenizer').mkdir()
    for name,data in {'config.json':{'model_type':'qwen3_tts','tts_model_type':'base','tts_model_size':'1b7','talker_config':{'num_code_groups':16}},'generation_config.json':{},'tokenizer_config.json':{},'speech_tokenizer/config.json':{'model_type':'qwen3_tts_tokenizer_12hz'}}.items():
        (root/name).write_text(json.dumps(data))
    (root/'model.safetensors').write_bytes(b'NOT REAL WEIGHTS, fingerprint tests only')
    (root/'speech_tokenizer/model.safetensors').write_bytes(b'NOT REAL TOKENIZER WEIGHTS')
    return root


class AdmissionTests(helpers.Fixture,unittest.TestCase):
    def setUp(self):helpers.CodeTests.setUp(self)
    run_codes=helpers.CodeTests.run_codes

    def test_fixture_training_rejected_before_import_or_gpu(self):
        out=self.run_codes()
        args=NS(state=str(self.state),id=out['id'],manifest_sha256=out['manifest_sha256'],model_dir='/not-used',model_sha256='a'*64,
                epochs=1,accumulation=4,max_sequence=1024,lora_rank=8,seed=42,timeout=10,lr=2e-5,lora_alpha=16.,confirm_data_reviewed=True,ack_experimental_training=True)
        with patch.object(job,'base_fingerprint',side_effect=AssertionError('must not inspect model')):
            self.reject(409,job.run_controller,args,ROOT/'tools/train_tts.py')
        self.assertFalse((self.state/'training_runs').exists());self.codes.delete(out['id'],out['manifest_sha256'])

    def test_explicit_review_and_legacy_gate(self):
        out=self.run_codes();meta,_=self.codes._manifest(self.codes.root/out['id'],out['id'])
        self.reject(400,job.admit,meta,[{},{}],False,True)
        self.reject(400,job.admit,meta,[{},{}],True,False)
        meta['schema']=1;meta['state']='audio_codes_prepared';meta['engine']['kind']='qwen3_tts_tokenizer_12hz';meta['checks']['tokenization_executed']=True
        self.reject(409,job.admit,meta,[{},{}],True,True)

    def test_controller_has_no_fake_training_cli_switch(self):
        out=self.run_codes()
        done=subprocess.run([sys.executable,str(ROOT/'tools/train_tts.py'),'train','--state',str(self.state),'--id',out['id'],'--manifest-sha256',out['manifest_sha256'],
                             '--model-dir','/not-used','--model-sha256','a'*64,'--confirm-data-reviewed','--ack-experimental-training'],capture_output=True,text=True,timeout=10)
        self.assertEqual(done.returncode,2);self.assertEqual(json.loads(done.stdout)['code'],409)
        self.assertNotIn('not private',done.stdout);self.assertFalse((self.state/'training_runs').exists())

    def test_code_lease_fd_adoption_checks_owner_and_last_reference(self):
        out=self.run_codes();cid,pin=out['id'],out['manifest_sha256']
        with self.codes.lease_with_fd(cid,pin) as (_,_,_,fd):
            with self.codes.adopt_lease(cid,pin,fd):self.reject(409,self.codes.delete,cid,pin)
            with self.codes.fs._open(self.codes.root/('.use-'+cid)) as wrong:
                self.reject(409,lambda:self.codes.adopt_lease(cid,pin,wrong.fileno()).__enter__())
            with open(self.state/'unrelated','wb') as wrong:
                self.reject(409,lambda:self.codes.adopt_lease(cid,pin,wrong.fileno()).__enter__())
        with self.codes.fs._open(self.codes.root/('.use-'+cid)) as unlocked:
            self.reject(409,lambda:self.codes.adopt_lease(cid,pin,unlocked.fileno()).__enter__())
        self.codes.delete(cid,pin)

    def test_base_fingerprint_and_weight_mutation(self):
        root=base_tree(self.state/'base');before=job.base_fingerprint(root)
        (root/'model.safetensors').write_bytes(b'other fixture weights');self.assertNotEqual(before,job.base_fingerprint(root))
        (root/'evil.py').write_text('raise AssertionError()');self.reject(400,job.base_fingerprint,root)

    def test_model_links_pickle_remote_code_and_missing_assets(self):
        for kind in ('symlink','hardlink','pickle','remote','missing','shard'):
            root=base_tree(self.state/kind)
            if kind=='symlink':(root/'link.json').symlink_to(root/'config.json')
            elif kind=='hardlink':(root/'hard.json').hardlink_to(root/'config.json')
            elif kind=='pickle':(root/'pytorch_model.bin').write_bytes(b'pickle rejected')
            elif kind=='remote':(root/'tokenizer_config.json').write_text('{"auto_map":{}}')
            elif kind=='missing':(root/'generation_config.json').unlink()
            else:(root/'model.safetensors.index.json').write_text('{"weight_map":{"x":"../escape.safetensors"}}')
            self.reject(400,job.base_fingerprint,root)

    def test_option_budgets_and_no_nan(self):
        args=NS(epochs=1,accumulation=4,max_sequence=1024,lora_rank=8,seed=42,timeout=10,lr=2e-5,lora_alpha=16.,model_sha256='a'*64)
        job.validate_options(args)
        for key,bad in [('epochs',0),('accumulation',0),('max_sequence',2049),('lora_rank',64),('timeout',999999),('lr',float('nan')),('lora_alpha',float('inf')),('model_sha256','bad')]:
            changed=copy.copy(args);setattr(changed,key,bad);self.reject(400,job.validate_options,changed)

    def test_child_environment_scrubs_keys_not_gpu_visibility(self):
        with patch.dict(os.environ,{'DEEPSEEK_API_KEY':'private','HF_TOKEN':'private','QTTS_ACCESS_TOKEN':'private','CUDA_VISIBLE_DEVICES':'2,3'}):
            gpu=NS(export=lambda:{'QTTS_GPU_LEASE_FD':'30','QTTS_GPU_LEASE_NONCE':'n'})
            env=job.child_environment(gpu,31)
        for key in ('DEEPSEEK_API_KEY','HF_TOKEN','QTTS_ACCESS_TOKEN'):self.assertNotIn(key,env)
        self.assertEqual(env['CUDA_VISIBLE_DEVICES'],'2,3');self.assertEqual(env[job.CODE_FD],'31');self.assertEqual(env['HF_HUB_OFFLINE'],'1')


CPU_HOLDER=r"""import json,os,sys,time,signal
from pathlib import Path
root,request_path,rank,parent,mode=sys.argv[1:]
sys.path[:0]=[root+'/py',root+'/tools']
from encode_training import arm_parent_death
arm_parent_death(int(parent))
signal.pthread_sigmask(signal.SIG_UNBLOCK,{signal.SIGINT,signal.SIGTERM})
from training_codes import TrainingCodesStore
from resource_limits import UploadLimits
from gpu_ownership import GpuLease,FD_ENV,NONCE_ENV
from training_job import CODE_FD
request=json.loads(Path(request_path).read_text())
store=TrainingCodesStore.configured(request['state'],UploadLimits())
with GpuLease.adopt(int(os.environ[FD_ENV]),os.environ[NONCE_ENV],root=request['test_gpu_root'],expected_kind='offline-reservation'):
 with store.adopt_lease(request['codes_id'],request['codes_sha256'],int(os.environ[CODE_FD])):
  os.close(int(os.environ[FD_ENV]));os.close(int(os.environ[CODE_FD]))
  ready=Path(request['run_dir'],'ready-'+rank)
  temporary=Path(request['run_dir'],'.ready-'+rank+'.tmp')
  temporary.write_text(str(os.getpid()));temporary.replace(ready)
  if mode=='exit0':time.sleep(.1)
  elif mode=='fail' and rank=='0':raise SystemExit(2)
  else:time.sleep(30)
"""


def controlled_fixture(args,mode):
    # INTERNAL TEST INJECTION ONLY. Production CLI has no such bypass/switch.
    real_popen=subprocess.Popen;real_acquire=job.GpuLease.acquire
    gpu_root=Path(args.state)/'test-gpu'
    def spawn(command,**kwargs):
        req=Path(command[command.index('--_request')+1]);data=json.loads(req.read_text());data['test_gpu_root']=str(gpu_root);job.write_json(req,data)
        rank=command[command.index('--_rank')+1];parent=command[command.index('--_parent-pid')+1]
        if mode=='spawn-error' and rank=='1':raise OSError('injected Popen failure')
        return real_popen([sys.executable,'-c',CPU_HOLDER,str(ROOT),str(req),rank,parent,mode],**kwargs)
    with patch.object(job,'admit'),patch.object(job,'model_fingerprint',return_value=None),patch.object(job.importlib.util,'find_spec',return_value=object()),patch.object(job.GpuLease,'acquire',side_effect=lambda kind:real_acquire(kind,root=gpu_root)),patch.object(job.subprocess,'Popen',side_effect=spawn):
        return job.run_controller(args,ROOT/'tools/train_tts.py')


class ControllerLifetimeTests(helpers.Fixture,unittest.TestCase):
    def setUp(self):helpers.CodeTests.setUp(self)
    run_codes=helpers.CodeTests.run_codes

    def arguments(self,timeout):
        out=self.run_codes();base=base_tree(self.state/'base')
        return NS(state=str(self.state),id=out['id'],manifest_sha256=out['manifest_sha256'],model_dir=str(base),model_sha256=job.base_fingerprint(base),epochs=1,accumulation=4,max_sequence=1024,lora_rank=8,seed=42,timeout=timeout,lr=2e-5,lora_alpha=16.,confirm_data_reviewed=True,ack_experimental_training=True)

    def test_zero_exit_without_checkpoint_cannot_claim_optimizer_success(self):
        args=self.arguments(10);result=controlled_fixture(args,'exit0')
        self.assertEqual(result['status'],'failed');self.assertFalse(result['optimizer_execution_observed'])
        self.codes.delete(args.id,args.manifest_sha256)

    def test_timeout_stops_both_fd_holders_before_release(self):
        args=self.arguments(2);result=controlled_fixture(args,'hang')
        self.assertEqual(result['status'],'timeout');self.assertTrue(all(code is not None for code in result['rank_exit_codes']))
        self.codes.delete(args.id,args.manifest_sha256)
        with job.GpuLease.acquire('offline-reservation',root=self.state/'test-gpu'):pass

    def test_one_failed_rank_terminates_other_and_never_publishes(self):
        args=self.arguments(10);result=controlled_fixture(args,'fail')
        self.assertEqual(result['status'],'failed');self.assertIsNone(result['checkpoint_relative_directory'])
        self.assertTrue(all(code is not None for code in result['rank_exit_codes']));self.codes.delete(args.id,args.manifest_sha256)

    def test_second_spawn_failure_stops_first_and_releases_locks(self):
        args=self.arguments(10);result=controlled_fixture(args,'spawn-error')
        self.assertEqual(result['status'],'failed');self.assertEqual(len(result['rank_exit_codes']),1)
        self.assertIsNotNone(result['rank_exit_codes'][0]);self.codes.delete(args.id,args.manifest_sha256)

    def test_offline_gpu_adoption_is_explicit_not_worker_default(self):
        root=self.state/'gpu-adopt'
        with job.GpuLease.acquire('offline-reservation',root=root) as owned:
            self.reject(409,lambda:job.GpuLease.adopt(owned.fd,owned.record['nonce'],root=root))
            with job.GpuLease.adopt(owned.fd,owned.record['nonce'],root=root,expected_kind='offline-reservation'):pass
            self.reject(409,lambda:job.GpuLease.acquire('inference',root=root))
        with job.GpuLease.acquire('inference',root=root):pass

    def test_controller_sigterm_and_sigkill_real_children_release(self):
        import select,time
        for action in ('sigterm','sigkill'):
            state=self.state/action;state.mkdir()
            # Use the already-created immutable dataset; separate run dir across actions.
            if action=='sigterm':args=self.arguments(30)
            request_file=self.state/'controller-args.json';request_file.write_text(json.dumps(vars(args)))
            program="import sys,json;from types import SimpleNamespace;sys.path[:0]=sys.argv[1:3];from test_tts_training import controlled_fixture;print(controlled_fixture(SimpleNamespace(**json.load(open(sys.argv[3]))),'hang'),flush=True)"
            previous=set(p.name for p in (self.state/'training_runs').iterdir()) if (self.state/'training_runs').exists() else set()
            process=subprocess.Popen([sys.executable,'-c',program,str(ROOT/'py'),str(Path(__file__).parent),str(request_file)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            pidfds=[]
            try:
                deadline=time.monotonic()+10;ready=[]
                while time.monotonic()<deadline and process.poll() is None:
                    ready=[p for p in (self.state/'training_runs').glob('*/ready-*') if p.parent.name not in previous]
                    if len(ready)==2:break
                    time.sleep(.03)
                self.assertEqual(len(ready),2)
                for path in ready:pidfds.append(os.pidfd_open(int(path.read_text())))
                self.reject(409,self.codes.delete,args.id,args.manifest_sha256)
                if action=='sigterm':process.terminate()
                else:process.kill()
                process.wait(10)
                for fd in pidfds:self.assertTrue(select.select([fd],[],[],5)[0])
                # Do not delete between the two actions: verify lock closure instead.
                with self.codes.lease(args.id,args.manifest_sha256):pass
                with job.GpuLease.acquire('offline-reservation',root=self.state/'test-gpu'):pass
            finally:
                if process.poll() is None:process.kill();process.wait(5)
                for fd in pidfds:os.close(fd)
        self.codes.delete(args.id,args.manifest_sha256)


@unittest.skipUnless(TORCH,'optional torch tensor tests unavailable; not GPU proof')
class TensorTests(unittest.TestCase):
    def setUp(self):torch.set_num_threads(1);torch.manual_seed(7)

    def test_lora_zero_init_freeze_fp32_and_backward(self):
        base=nn.Linear(4,3);layer=LoRALinear(base,2,4);x=torch.randn(2,4)
        self.assertTrue(torch.equal(base(x),layer(x)));self.assertFalse(base.weight.requires_grad)
        layer(x).square().mean().backward();self.assertIsNone(base.weight.grad)
        self.assertGreater(layer.lora_B.grad.abs().sum().item(),0);self.assertEqual(layer.lora_A.dtype,torch.float32)

    def test_fp16_frozen_base_keeps_float32_trainable_gradients(self):
        layer=LoRALinear(nn.Linear(4,3).half(),2,4)
        output=layer(torch.randn(2,4).half())
        output.float().square().mean().backward()
        self.assertEqual(output.dtype,torch.float16);self.assertEqual(layer.lora_B.grad.dtype,torch.float32)
        self.assertIsNone(layer.base.weight.grad)

    def test_targets_include_subtalker_not_speaker_and_no_guess(self):
        core=TinyCore();targets=inject_lora(core,2,4)
        self.assertEqual(len(targets),4);self.assertTrue(any('code_predictor' in name for name in targets))
        self.assertTrue(all('speaker' not in name for name in targets));self.assertEqual(sum(p.requires_grad for p in core.parameters()),8)
        with self.assertRaises(ValueError):inject_lora(nn.Linear(4,4))

    def test_real_joint_loss_projection_and_optimizer_updates(self):
        core=TinyCore();inject_lora(core,2,4);initial=adapter_digest(core);frozen=core.talker.text.weight.clone()
        task=JointLoss(core,torch.zeros(1,4));optimizer=torch.optim.AdamW([p for p in task.parameters() if p.requires_grad],lr=.01)
        stats=optimize_epoch(task,tiny_data(),[0,1,2],optimizer,torch.amp.GradScaler('cpu',enabled=False),torch.device('cpu'),accumulation=2,amp=False)
        self.assertEqual(stats['optimizer_steps'],2);self.assertNotEqual(initial,adapter_digest(core));self.assertTrue(torch.equal(frozen,core.talker.text.weight))
        self.assertTrue(torch.isfinite(torch.tensor(stats['loss_mean'])))

    def test_nonfinite_loss_rejected_without_update(self):
        core=TinyCore();inject_lora(core,2,4);initial=adapter_digest(core);task=JointLoss(core,torch.full((1,4),float('nan')))
        optimizer=torch.optim.AdamW([p for p in task.parameters() if p.requires_grad],lr=.01)
        with self.assertRaisesRegex(ValueError,'non-finite'):
            optimize_epoch(task,tiny_data(),[0],optimizer,torch.amp.GradScaler('cpu',enabled=False),torch.device('cpu'),amp=False)
        self.assertEqual(initial,adapter_digest(core))

    def test_nonfinite_gradient_skips_update_not_fake_success(self):
        core=TinyCore();inject_lora(core,2,4);before=adapter_digest(core)
        task=JointLoss(core,torch.zeros(1,4));p=next(p for p in task.parameters() if p.requires_grad)
        handle=p.register_hook(lambda gradient:torch.full_like(gradient,float('inf')))
        optimizer=torch.optim.AdamW([p for p in task.parameters() if p.requires_grad],lr=.01)
        try:stats=optimize_epoch(task,tiny_data(),[0],optimizer,torch.amp.GradScaler('cpu',enabled=False),torch.device('cpu'),amp=False)
        finally:handle.remove()
        self.assertEqual(stats['optimizer_steps'],0);self.assertEqual(stats['overflow_steps'],1);self.assertEqual(before,adapter_digest(core))

    def test_sampler_full_coverage_padding_epoch_and_tail(self):
        for count in range(2,17):
            ranks=epoch_indices(count,0)
            self.assertEqual(len(ranks[0]),len(ranks[1]));self.assertEqual(set(sum(ranks,[])),set(range(count)))
            self.assertEqual(len(sum(ranks,[])),count+count%2)
        with self.assertRaises(ValueError):epoch_indices(1,0)
        self.assertNotEqual(epoch_indices(16,0),epoch_indices(16,1))

    def test_dataset_masks_and_no_truncation(self):
        dataset=tiny_data();batch=dataset.collate_fn([dataset[0]])
        self.assertEqual(batch['codec_ids'].shape[-1],16);self.assertEqual(batch['codec_mask'].sum().item(),3)
        self.assertFalse(batch['codec_embedding_mask'][0,6,0]);self.assertEqual((batch['codec_0_labels']!=-100).sum().item(),4)
        with self.assertRaisesRegex(ValueError,'no truncation'):tiny_data(max_sequence=16)[0]

    def test_restore_adapter_strict_members_shapes_and_finite(self):
        core=TinyCore();inject_lora(core,2,4);state=adapter_state(core);restore_adapter(core,state)
        wrong=dict(state);wrong.pop(next(iter(wrong)))
        with self.assertRaises(ValueError):restore_adapter(core,wrong)
        wrong=dict(state);first=next(iter(wrong));wrong[first]=torch.full_like(wrong[first],float('nan'))
        with self.assertRaises(ValueError):restore_adapter(core,wrong)

    def test_actual_two_process_gloo_optimizer_sync(self):
        with tempfile.TemporaryDirectory() as temporary:
            rendezvous=(Path(temporary)/'gloo').as_uri()
            mp.spawn(gloo_worker,args=(rendezvous,temporary),nprocs=2,join=True)
            a,b=[json.loads((Path(temporary)/f'{r}.json').read_text()) for r in (0,1)]
            self.assertEqual(a['after'],b['after']);self.assertNotEqual(a['before'],a['after'])
            self.assertEqual(a['before'],b['before'])
            for epoch in range(2):
                self.assertEqual(a['reports'][epoch]['optimizer_steps'],1)
                self.assertEqual(set(a['reports'][epoch]['seen_indices']+b['reports'][epoch]['seen_indices']),{0,1,2})

    @unittest.skipUnless(importlib.util.find_spec('safetensors'),'optional safetensors unavailable')
    def test_atomic_adapter_checkpoint_and_reload_not_full_model(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);base=base_tree(root/'base');core=TinyCore();targets=inject_lora(core,2,4)
            state=adapter_state(core);request={'run_dir':str(root),'sample_ids':['a','b'],'model_sha256':job.base_fingerprint(base),'codes_id':'a'*32,
                                            'codes_sha256':'b'*64,'lora_rank':2,'lora_alpha':4}
            reports=[{'rank':i,'parameters_changed':True,'epochs':[{'seen_ids':[sid]}]} for i,sid in enumerate(('a','b'))]
            job.save_checkpoint(request,core,torch.zeros(1,4),targets,reports)
            self.assertFalse((root/'.checkpoint-pending').exists());meta=json.loads((root/'adapter/manifest.json').read_text())
            self.assertFalse(meta['published_to_inference']);self.assertFalse(meta['inference_reload_verified']);self.assertFalse(meta['training_quality_verified'])
            fresh=TinyCore();speaker=load_adapter(fresh,root/'adapter',base);self.assertEqual(speaker.shape,(1,4))
            for name,value in adapter_state(fresh).items():self.assertTrue(torch.equal(value,state[name]))
            (root/'adapter/adapter.safetensors').write_bytes(b'bad')
            with self.assertRaises(ValueError):load_adapter(TinyCore(),root/'adapter',base)


if __name__=='__main__':unittest.main()
