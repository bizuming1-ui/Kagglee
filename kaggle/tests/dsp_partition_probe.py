"""Read-only stage17 NumPy DSP partition experiment. Synthetic signal, no model/GPU/audio claim."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, os
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
os.environ['QTTS_NO_RUST']='1'
spec=importlib.util.spec_from_file_location('stage18_baseline_audio_rt',ROOT/'kaggle/source/py/audio_rt.py')
audio=importlib.util.module_from_spec(spec);spec.loader.exec_module(audio)

def run(y,pattern,target,gain):
    lev=audio.Leveler(24000,target,max_gain_db=gain);lev.start_segment()
    chunks=[];i=0;k=0
    try:
        while i<len(y):
            n=pattern[k%len(pattern)];chunks.append(lev.process(y[i:i+n]));i+=n;k+=1
        result=np.concatenate(chunks)
        return result,{'gain_db':lev.gain_db,'env_dbfs':lev.env_dbfs}
    finally:lev.close()

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--round',type=int,required=True);args=parser.parse_args()
    sr=24000;t=np.arange(sr//2,dtype=np.float64)/sr
    y=(0.12*np.sin(2*np.pi*220*t)+0.035*np.sin(2*np.pi*510*t)).astype(np.float32)
    cases=[]
    for name,target,gain in [('fade-and-dc-isolated',-6.,0.),('normal-agc',-18.,6.)]:
        full,full_state=run(y,[len(y)],target,gain)
        for pattern in ([48],[64],[96],[240],[1920],[31,127,513,9,2048]):
            split,state=run(y,pattern,target,gain)
            assert len(split)==len(full)==len(y) and np.isfinite(split).all()
            diff=split.astype(np.int32)-full.astype(np.int32)
            cases.append({'experiment':name,'partition_samples':pattern,'output_samples':len(split),'different_samples':int(np.count_nonzero(diff)),
                'max_abs_i16_difference':int(np.max(np.abs(diff))),'rms_i16_difference':float(np.sqrt(np.mean(diff.astype(np.float64)**2))),
                'whole_state':full_state,'split_state':state})
    assert any(c['experiment']=='fade-and-dc-isolated' and c['partition_samples']==[48] and c['different_samples']>0 for c in cases)
    assert any(c['experiment']=='normal-agc' and c['partition_samples']==[1920] and c['different_samples']>0 for c in cases)
    print(json.dumps({'round':args.round,'experiment_completed':True,'backend':audio.BACKEND,'source_sha256':hashlib.sha256((ROOT/'kaggle/source/py/audio_rt.py').read_bytes()).hexdigest(),
        'source_modified':False,'numpy_version':np.__version__,'signal':'synthetic half-second two-tone, 24000 Hz','cases':cases,
        'partition_dependence_reproduced':True,'model_executed':False,'gpu_executed':False,'user_hiss_root_cause_proven':False,'voice_quality_verified':False},indent=2))
if __name__=='__main__':main()
