#!/usr/bin/env python3
"""Real complete Faster/Qwen imports + tiny TF Mimi load, CPU/offline only.

No fake imports, no downloaded model weights, no Qwen model construction.
--baseline loads the frozen step12 compatibility source and expects the user's
Mimi AttributeError after Faster's lazy import. Default exercises current code.
"""
import argparse
import ast
import base64
from contextlib import redirect_stdout
import hashlib
import importlib.util
from importlib import metadata
import json
import os
from pathlib import Path
import sys
import tempfile
import traceback
import zlib

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--baseline',action='store_true');args=parser.parse_args()
os.environ.update(HF_HUB_OFFLINE='1',TRANSFORMERS_OFFLINE='1')
def no_network(event,values):
    if event=='socket.connect':raise AssertionError('network forbidden in real-import CPU check')
sys.addaudithook(no_network)
result={'baseline_step12':args.baseline,'full_qwen_model_loaded':False,'gpu_executed':False,'network_forbidden':True}
with tempfile.TemporaryDirectory(prefix='qtts-lazy-rope-') as directory,redirect_stdout(sys.stderr):
    import torch
    assert not torch.cuda.is_available(),'CPU-only evidence must not be mislabeled'
    torch.set_num_threads(1)
    for package,version in {'faster-qwen3-tts':'0.5.4','qwen-tts-hf':'0.1.1.post1','transformers':'5.20.2'}.items():assert metadata.version(package)==version
    # Exact top-level import used by Worker and preflight; it does NOT import Qwen.
    import faster_qwen3_tts
    absent='qwen_tts._transformers_compat' not in sys.modules
    assert absent,'reviewed Faster lazy-import contract changed'
    result['actual_faster_import_leaves_qwen_unloaded']=absent
    if args.baseline:
        tree=ast.parse((ROOT/'kaggle/kaggle-fixed-step12.py').read_bytes())
        files=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
        digest,data=files['py/qwen_compat.py'];source=zlib.decompress(base64.b64decode(data));assert hashlib.sha256(source).hexdigest()==digest
        path=Path(directory)/'step12_compat.py';path.write_bytes(source)
        spec=importlib.util.spec_from_file_location('step12_compat',path);qc=importlib.util.module_from_spec(spec);spec.loader.exec_module(qc)
    else:
        sys.path.insert(0,str(ROOT/'kaggle/source/py'))
        import qwen_compat as qc
    status=qc.install_qwen_rope_bridge();result['install_status']=status['status']
    # What Faster.from_pretrained does next (without downloading a full model).
    from qwen_tts import Qwen3TTSModel
    from transformers import MimiConfig,MimiModel
    from transformers.modeling_rope_utils import ROPE_INIT_FUNCTIONS
    def config(theta):
        return MimiConfig(hidden_size=8,num_filters=2,upsampling_ratios=[2,2],codebook_size=8,codebook_dim=4,
            num_quantizers=2,vector_quantization_hidden_dimension=4,upsample_groups=8,num_hidden_layers=1,
            intermediate_size=16,num_attention_heads=2,num_key_value_heads=2,sliding_window=4,
            rope_parameters={'rope_type':'default','rope_theta':theta})
    if args.baseline:
        assert status['status']=='not_applicable'
        try:MimiModel(config(12345.))
        except AttributeError as error:
            assert 'rope_theta' in str(error)
            trace=traceback.format_exc();assert 'modeling_mimi.py' in trace and '_transformers_compat.py' in trace
            result.update(passed=True,original_error_reproduced=str(error),real_mimi_initialization_failed=True)
        else:raise AssertionError('step12 baseline unexpectedly constructed modern Mimi')
    else:
        assert status['status']=='installed' and ROPE_INIT_FUNCTIONS['default']._qtts_rope_bridge
        assert qc.configuration_smoke()['configuration_smoke_passed']
        first=ROPE_INIT_FUNCTIONS['default'];qc.install_qwen_rope_bridge();assert first is ROPE_INIT_FUNCTIONS['default']
        bridge_calls=[]
        def trace_bridge(frame,event,arg):
            if event=='call' and frame.f_code is first.__code__:bridge_calls.append(1)
        sys.setprofile(trace_bridge)
        for theta in (10000.,12345.,1000000.):
            cfg=config(theta);before=cfg.to_dict();model=MimiModel(cfg).eval()
            assert cfg.to_dict()==before
            path=Path(directory)/str(int(theta));model.save_pretrained(path)
            # Exercise actual TF from_pretrained/_init_weights, not only function math.
            loaded=MimiModel.from_pretrained(path,local_files_only=True).eval()
            assert loaded.config.rope_parameters['rope_theta']==theta
            rotary=[m for m in loaded.modules() if hasattr(m,'inv_freq') and hasattr(m,'original_inv_freq')]
            assert rotary and ROPE_INIT_FUNCTIONS['default'] is first
            expected=1./(theta**(torch.arange(0,4,2,dtype=torch.float32)/4))
            for m in rotary:torch.testing.assert_close(m.inv_freq,expected,rtol=0,atol=0)
            assert all(torch.isfinite(p).all() for p in loaded.parameters())
            result['tiny_mimi_parameters']=sum(p.numel() for p in loaded.parameters())
        sys.setprofile(None);assert bridge_calls
        result['bridge_calls_from_actual_mimi_initialization']=len(bridge_calls)
        result.update(passed=True,complete_qwen_package_imported=True,configuration_smoke_passed=True,
            actual_tiny_mimi_construct_save_reload=True,theta_values=[10000.,12345.,1000000.],
            model_config_unchanged=True,bridge_idempotent=True)
print(json.dumps(result))
