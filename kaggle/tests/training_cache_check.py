#!/usr/bin/env python3
"""Real CPU tiny-LoRA A/B against frozen step13 code; no Qwen/GPU quality claim."""
import ast
import base64
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import time
import zlib

REPO=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(REPO/'kaggle/tests'),str(REPO/'kaggle/source/py')]
import test_tts_training as fixture
import torch
from lora_adapter import inject_lora,adapter_state
from tts_dataset import TTSDataset
import tts_training

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

raw=(REPO/'kaggle/kaggle-fixed-step13.py').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60'
tree=ast.parse(raw);files=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
torch.set_num_threads(1);torch.manual_seed(140)
with tempfile.TemporaryDirectory() as temporary:
 root=Path(temporary)
 for asset in ('py/tts_dataset.py','py/tts_training.py'):
  digest,blob=files[asset];source=zlib.decompress(base64.b64decode(blob));assert hashlib.sha256(source).hexdigest()==digest
  (root/Path(asset).name).write_bytes(source)
 old_data=module('baseline_data',root/'tts_dataset.py');old_train=module('baseline_train',root/'tts_training.py')
 a=fixture.TinyCore();inject_lora(a,2,4);b=copy.deepcopy(a)
 source=fixture.tiny_data();counts=[0,0];reports=[]
 for i,(core,dataset_class,train) in enumerate(((a,old_data.TTSDataset,old_train),(b,TTSDataset,tts_training))):
  def processor(**args):
   counts[i]+=1
   return source.processor(**args)
  data=dataset_class(source.rows,processor,source.config,source.reference_mel)
  started=time.perf_counter()
  for index in range(len(data)):data[index]  # Actual run_rank pre-admission.
  task=train.JointLoss(core,torch.zeros(1,4));opt=torch.optim.AdamW([p for p in task.parameters() if p.requires_grad],lr=.01)
  epochs=[]
  for epoch in range(3):epochs.append(train.optimize_epoch(task,data,[0,1,2],opt,torch.amp.GradScaler('cpu',enabled=False),torch.device('cpu'),2,False))
  reports.append({'epochs':epochs,'elapsed_seconds':time.perf_counter()-started,'tokenizer_calls':counts[i],
    'cache_bytes':getattr(data,'cache_used',0)})
 assert reports[0]['epochs']==reports[1]['epochs']
 assert all(torch.equal(adapter_state(a)[key],adapter_state(b)[key]) for key in adapter_state(a))
 assert counts==[12,3],counts
 assert sum(e['optimizer_steps'] for e in reports[0]['epochs'])==6
 print(json.dumps({'passed':True,'baseline':'frozen step13 source','model':'real CPU tiny LoRA; synthetic inputs, not Qwen',
  'gpu_executed':False,'qwen_training_executed':False,'training_quality_verified':False,
  'same_loss_reports':True,'all_adapter_tensors_bitwise_equal':True,'same_optimizer_steps':6,
  'samples_per_epoch':3,'epochs':3,'before':reports[0],'after':reports[1],
  'timing_scope':'CPU tiny fixture incl cold optimizer startup; NOT a GPU speed benchmark or quality result'}))
