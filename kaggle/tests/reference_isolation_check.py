#!/usr/bin/env python3
"""Actual Faster0.5.4 resolver/prepare + production generated-only decoder.
Explicit CPU prompt/talker/kernel/codec fixtures, NOT Qwen weights/listening/RTF.
Both ICL and explicit xvector tested; reference markers must never reach codec.
"""
import hashlib
from importlib import metadata
import inspect
import json
import os
from pathlib import Path
import sys
import threading
from types import SimpleNamespace as NS
from unittest.mock import patch
os.environ['QTTS_MOCK']='1';os.environ['HF_HUB_OFFLINE']='1'
def no_network(event,args):
    if event=='socket.connect':raise AssertionError('network forbidden')
sys.addaudithook(no_network)
import numpy as np
import torch
torch.set_num_threads(1)
assert not torch.cuda.is_available()
from faster_qwen3_tts import FasterQwen3TTS
import faster_qwen3_tts.streaming as streaming
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'source/py'))
from worker import RealEngine
assert metadata.version('faster-qwen3-tts')=='0.5.4'
results=[]
for mode in ('icl','xvector'):
 for chunk_size in (2,4,8,12):
    os.environ['QTTS_CLONE_MODE']=mode
    extracted=[];decoded=[];prompts=[];built_text=[];marker=[999]
    def create_prompt(**kw):
        extracted.append(kw)
        if mode=='xvector':assert kw['x_vector_only_mode'] is True and kw['ref_text']==''
        else:assert kw['ref_text']=='THIS IS MATCHING REFERENCE TEXT' and 'x_vector_only_mode' not in kw
        return [NS(ref_spk_embedding=torch.tensor([.3,.4,.5]),ref_code=torch.full((9,16),marker[0]),ref_text=kw['ref_text'])]
    def prompt_dict(items):
        return {'ref_spk_embedding':[items[0].ref_spk_embedding],'ref_code':[items[0].ref_code],
                'x_vector_only_mode':[False],'icl_mode':[True]}
    class CodecFixture:
        sample_rate=24000
        def decode(self,body):
            codes=body['audio_codes'];assert codes.ndim==3 and torch.all(codes==7),'REFERENCE code reached decoder'
            n=codes.shape[1];decoded.append(n)
            return [torch.sin(torch.arange(n*1920)*.1)*.1],24000
    model=NS(model=NS(talker=NS(),config=NS(talker_config=NS()),speech_tokenizer=CodecFixture()),
             create_voice_clone_prompt=create_prompt,_prompt_items_to_voice_clone_prompt=prompt_dict,
             _build_assistant_text=lambda text:(built_text.append(text) or text),
             _build_ref_text=lambda text:text,_tokenize_texts=lambda texts:[torch.tensor([[1,2]]) for text in texts])
    faster=FasterQwen3TTS(model,None,None,device='cpu',dtype=torch.float32);faster._warmed_up=True
    # Audio I/O and talker embeddings deliberately explicit fixtures, resolver and prepare remain actual library code.
    faster._load_ref_audio_with_silence=lambda *a,**kw:(np.zeros(24000,np.float32),24000)
    def inputs(**kw):
        vcp=kw['voice_clone_prompt'];prompts.append(vcp)
        if mode=='icl':
            assert torch.all(vcp['ref_code'][0]==marker[0]) and vcp['icl_mode']==[True]
            assert vcp['x_vector_only_mode']==[False] and kw['ref_ids'][0] is not None
        else:
            assert vcp['ref_code']==[None] and vcp['icl_mode']==[False]
            assert vcp['x_vector_only_mode']==[True] and kw['ref_ids']==[None]
        return (torch.zeros(1,2,4),)*4
    faster._build_talker_inputs_local=inputs
    def kernel(**kw):
        assert kw['chunk_size']==chunk_size
        for start in range(0,80,chunk_size):
            yield torch.full((min(chunk_size,80-start),16),7,dtype=torch.long),{'fixture':True}
    engine=RealEngine(0);engine.model=faster;engine.sane=True
    profile={'id':'fixture','anchor':'never-read-reference.wav','ref_text':'THIS IS MATCHING REFERENCE TEXT'}
    engine.load_profile(profile)
    with patch.object(streaming,'fast_generate_streaming',kernel):
        audio=list(engine.stream(profile,'只读这段目标文字。','Chinese',chunk_size,100,7,threading.Event()))
    assert len(extracted)==1 and built_text==['只读这段目标文字。'],'warm cache not reused / reference appended to target'
    assert sum(len(a) for a in audio)==80*1920 and all(np.isfinite(a).all() for a in audio)
    assert max(decoded)<=25+2+chunk_size
    primary_decoded=decoded.copy()
    # Same path/text replaced: without eviction this ICL assertion fails on old reference marker.
    marker[0]=1001;engine.load_profile(profile)
    with patch.object(streaming,'fast_generate_streaming',kernel):
        replaced=list(engine.stream(profile,'新参考仍只生成目标。','Chinese',chunk_size,100,7,threading.Event()))
    assert len(extracted)==2 and sum(len(a) for a in replaced)==80*1920
    results.append({'mode':mode,'chunk_size':chunk_size,'chunks':len(audio),'generated_frames':80,
                    'decoded_window_frames':primary_decoded,'samples':sum(len(a) for a in audio),
                    'reference_codes_decoded':0,'prompt_extractions_before_reload':1,'after_same_path_reload':len(extracted)})
source=Path(inspect.getfile(FasterQwen3TTS)).read_bytes()
print(json.dumps({'passed':True,'actual_faster_version':metadata.version('faster-qwen3-tts'),
 'faster_model_py_sha256':hashlib.sha256(source).hexdigest(),'actual_faster_resolver_prepare_control_flow':True,
 'production_generated_only_decoder':True,'injected_cpu_prompt_talker_kernel_codec_fixtures':True,
 'full_qwen_model_loaded':False,'gpu_executed':False,'voice_quality_verified':False,'round_cases':results}))
