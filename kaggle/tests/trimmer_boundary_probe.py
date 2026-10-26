"""Read-only EdgeTrimmer baseline. Synthetic PCM; no codec/ASR/model/GPU proof."""
from pathlib import Path
import argparse,ast,copy,hashlib,json
import numpy as np
R=Path(__file__).resolve().parents[2]
path=R/'kaggle/source/py/worker.py'
node=copy.deepcopy(next(n for n in ast.parse(path.read_bytes()).body if isinstance(n,ast.ClassDef) and n.name=='EdgeTrimmer'))
module=ast.Module(body=[node],type_ignores=[]);ns={'np':np,'SAMPLE_RATE':24000}
exec(compile(ast.fix_missing_locations(module),str(path),'exec'),ns)
Trimmer=ns['EdgeTrimmer']

def run(parts):
    trimmer=Trimmer();outputs=[trimmer.push(part) for part in parts]
    output=np.concatenate(outputs)
    return {'input_samples':sum(map(len,parts)),'output_samples':len(output),'held_samples':len(trimmer.held),
        'held_nonzero_samples':int(np.count_nonzero(trimmer.held)),'started':trimmer.started,'lead_dropped':trimmer.lead_dropped,
        'output_sha256':hashlib.sha256(output.tobytes()).hexdigest()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--round',type=int,required=True);args=p.parse_args()
    y=np.full(12000,.02,np.float32);cases=[]
    for size in [64,119,120,1920,12000]:
        result=run([y[i:i+size] for i in range(0,len(y),size)])
        if size<120:assert result['output_samples']==0 and not result['started']
        else:assert result['output_samples']==len(y)
        cases.append({'case':'voiced-input-partition','partition_samples':size,**result,
            'production_codec_note':'Generated codec contract emits multiples of1920; arbitrary tiny blocks are helper-contract tests, not proof this occurs in current Faster production.'})
    quiet=np.full(960,.0025,np.float32);voice=np.full(2400,.02,np.float32)
    whole=run([np.concatenate([quiet,voice])]);split=run([quiet,voice])
    assert whole['output_samples']-split['output_samples']==840
    cases.append({'case':'cross-chunk-35ms-preroll','whole':whole,'split':split,'kept_context_difference_samples':840,
        'interpretation':'Quiet pre-roll may include unvoiced speech; synthetic signal does not prove a real phoneme was lost.'})
    tail=run([np.full(120,.02,np.float32),np.zeros(120,np.float32),np.full(60,.02,np.float32)])
    assert tail['held_nonzero_samples']==60 and not hasattr(Trimmer,'finish')
    cases.append({'case':'short-terminal-voiced-remainder',**tail,'finish_api_present':False})
    silence=run([np.zeros(480,np.float32)]*60)
    assert silence['lead_dropped']>21600 and silence['started'] and silence['held_samples']<=43200
    cases.append({'case':'long-silence-bounded-hold',**silence,'noise_free_success_claimed':False})
    print(json.dumps({'round':args.round,'experiment_completed':True,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases,'method':'AST-extracted actual EdgeTrimmer with NumPy synthetic PCM',
        'product_modified':False,'full_model_executed':False,'gpu_executed':False,'real_phoneme_loss_proven':False,'user_hiss_root_cause_proven':False},indent=2))
if __name__=='__main__':main()
