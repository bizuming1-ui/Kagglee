#!/usr/bin/env python3
"""Frozen16 vs17 real build control flow, synthetic PCM + explicit ASR/speaker fixtures.
No actual Whisper/Qwen weights/GPU; proves screenshot-shaped structural repair only.
"""
import ast,base64,hashlib,json,sys,tempfile,zlib
from pathlib import Path
from unittest.mock import patch
original_stdout=sys.stdout
sys.stdout=sys.stderr
import numpy as np
import test_reliability
import analyst
from test_step15 import BuildCostTests
from test_step17 import transcript
from reference_segments import prepare_segments
R=Path(__file__).resolve().parents[2]
raw=(R/'kaggle/kaggle-fixed-step16.py').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429'
files=ast.literal_eval(next(n.value for n in ast.parse(raw).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
source=zlib.decompress(base64.b64decode(files['py/analyst.py'][1]))
node=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='build_profile')
node.name='_step16_baseline_build';exec(compile(ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[])),'frozen16-build','exec'),vars(analyst))
fixture=BuildCostTests();cases=[]
with tempfile.TemporaryDirectory() as d:
 with patch.object(analyst,'build_profile',side_effect=analyst._step16_baseline_build):
  baseline=fixture.run_profile(d,duration=29,manual='',segments=[transcript(28.7)])
 assert baseline['state']=='error' and 'no aligned' in baseline['error']
 current=fixture.run_profile(d,duration=29,manual='',segments=[transcript(28.7)])
 assert current['state']=='done'
 p=json.loads((Path(d)/current['profile']/'profile.json').read_text())
 import soundfile as sf
 for c in p['candidates']:
  info=sf.info(Path(d)/current['profile']/c['file']);assert info.samplerate==24000 and info.frames<=16*24000
  cases.append({'file_frames':info.frames,'sample_rate':info.samplerate,'transcript_characters':len(c['text'])})
 report=p['quality']['asr'][0]['alignment']
assert report['word_split_segments']>1 and report['asr_windows']==0
seen=[]
def window_asr(audio,language):
 seen.append(len(audio));return 'zh',[dict(start=0.,end=len(audio)/16000,text='实际窗口的合成转写替身',words=[],logprob=-.1)]
_,recovered,receipt=prepare_segments(np.ones(round(28.7*16000),np.float32)*.03,[dict(start=0.,end=28.7,text='未对齐全文',words=[])],'zh',window_asr)
assert receipt['asr_windows']==2 and sum(seen)==round(28.7*16000) and recovered[-1]['end']==28.7
print(json.dumps({'passed':True,'baseline_frozen16_reproduced_no_aligned_error':True,'current17_same_fixture_build_succeeded':True,
 'source_seconds':29,'long_asr_segment_seconds':28.7,'alignment':report,'saved_candidate_wavs':cases,
 'window_retranscription_fixture':receipt,'all_window_samples_consumed':sum(seen),'asr_speaker_injected_fixtures':True,
 'real_whisper_weights_loaded':False,'full_qwen_model_loaded':False,'gpu_executed':False,'voice_quality_verified':False}),file=original_stdout)
