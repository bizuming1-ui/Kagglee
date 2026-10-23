#!/usr/bin/env python3
"""Actual TF5.20.2 Mimi + Qwen-HF wheel initializer, CPU only, no full model."""
import hashlib
import json
from pathlib import Path
import sys
import types
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'source/py'))
import torch
from transformers import MimiConfig
from transformers.modeling_rope_utils import ROPE_INIT_FUNCTIONS
from qwen_compat import bridge_registry
wheel=Path(sys.argv[1]);member='qwen_tts/_transformers_compat.py'
with zipfile.ZipFile(wheel) as archive:source=archive.read(member)
module=types.ModuleType('qwen_tts._transformers_compat');exec(compile(source,member,'exec'),module.__dict__)
module.patch_transformers_rope_registry()
config=MimiConfig(hidden_size=32,num_attention_heads=4,rope_parameters={'rope_type':'default','rope_theta':12345.})
before=config.to_dict();error=None
try:module._default_rope_parameters(config,device=torch.device('cpu'))
except AttributeError as e:error=str(e)
assert error and 'rope_theta' in error,error
bridge_registry(module,ROPE_INIT_FUNCTIONS)
for theta in (10000.,12345.,1000000.):
 config=MimiConfig(hidden_size=32,num_attention_heads=4,rope_parameters={'rope_type':'default','rope_theta':theta})
 before=config.to_dict();freq,scale=ROPE_INIT_FUNCTIONS['default'](config,device=torch.device('cpu'))
 expected=1./(theta**(torch.arange(0,8,2,dtype=torch.float32)/8))
 torch.testing.assert_close(freq,expected,rtol=0,atol=0)
 assert scale==1. and before==config.to_dict()
bridge_registry(module,ROPE_INIT_FUNCTIONS)
print(json.dumps({'passed':True,'transformers_version':__import__('transformers').__version__,
 'qwen_wheel_sha256':hashlib.sha256(wheel.read_bytes()).hexdigest(),'qwen_member':member,'member_sha256':hashlib.sha256(source).hexdigest(),
 'reported_attribute_error_reproduced':error,'modern_theta_values_checked':[10000.,12345.,1000000.],
 'configuration_unchanged':True,'full_qwen_model_loaded':False,'gpu_executed':False,'cuda_available':torch.cuda.is_available()}))
