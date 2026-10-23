#!/usr/bin/env python3
"""Actual HF Qwen12Hz tiny random decoder CPU: frame contract/causality/windows.
NOT pretrained speech, full Qwen TTS, GPU throughput, noise or similarity proof.
"""
import hashlib
import inspect
import json
import os
from pathlib import Path
import sys
from types import SimpleNamespace as NS
os.environ['HF_HUB_OFFLINE']='1'
original_stdout=sys.stdout
sys.stdout=sys.stderr
def no_network(event,args):
    if event=='socket.connect':raise AssertionError('offline experiment')
sys.addaudithook(no_network)
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'source/py'))
import numpy as np
import torch
from qwen_compat import install_qwen_rope_bridge
install_qwen_rope_bridge()
from qwen_tts.core.tokenizer_12hz.configuration_qwen3_tts_tokenizer_v2 import Qwen3TTSTokenizerV2DecoderConfig
from qwen_tts.core.tokenizer_12hz.modeling_qwen3_tts_tokenizer_v2 import Qwen3TTSTokenizerV2Decoder
from clone_stream import GeneratedCodecWindow
assert not torch.cuda.is_available()
torch.set_num_threads(1);torch.manual_seed(17)
c=Qwen3TTSTokenizerV2DecoderConfig(codebook_size=8,codebook_dim=8,hidden_size=8,latent_dim=8,
    num_attention_heads=2,num_key_value_heads=2,intermediate_size=16,num_hidden_layers=1,
    decoder_dim=32,num_quantizers=16,upsample_rates=[8,5,4,3],upsampling_ratios=[2,2],
    max_position_embeddings=128,sliding_window=72)
m=Qwen3TTSTokenizerV2Decoder._from_config(c).eval();cases=[]
with torch.inference_mode():
    codes=torch.randint(0,8,(40,16))
    full=m(codes.T[None])[0,0].numpy()
    prefix=m(codes[:8].T[None])[0,0].numpy()
    extended=m(codes[:12].T[None])[0,0].numpy()
    causal_error=float(np.max(np.abs(prefix-extended[:len(prefix)])))
    assert causal_error <= 1e-6
    assert full.size==40*1920 and np.isfinite(full).all()
    # Adapter only wraps actual tiny decoder; no synthetic waveform fixture here.
    def decode(body):return [m(body['audio_codes'].transpose(1,2))[0,0]],24000
    for lookahead in (0,2):
        for chunk in (2,4,8,12):
            w=GeneratedCodecWindow(NS(decode=decode),lookahead=lookahead);waves=[]
            for start in range(0,40,chunk):waves.append(w.push(codes[start:start+chunk]))
            waves.append(w.finish());audio=np.concatenate(waves)
            assert audio.size==40*1920 and np.isfinite(audio).all() and w.peak_frames<=25+lookahead+chunk
            cases.append({'chunk':chunk,'lookahead':lookahead,'samples':audio.size,'window_peak_frames':w.peak_frames,
                          'random_model_window_vs_full_max_abs':float(np.max(np.abs(audio-full)))})
print(json.dumps({'passed':True,'actual_qwen12hz_decoder_executed':True,'random_tiny_parameters':sum(p.numel() for p in m.parameters()),
 'codec_modeling_py_sha256':hashlib.sha256(Path(inspect.getfile(Qwen3TTSTokenizerV2Decoder)).read_bytes()).hexdigest(),
 'sample_rate':24000,'samples_per_frame':1920,'causal_prefix_max_abs':causal_error,'round_cases':cases,
 'full_qwen_model_loaded':False,'trained_codec_loaded':False,'gpu_executed':False,'voice_quality_verified':False}),file=original_stdout)
