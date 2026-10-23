#!/usr/bin/env python3
"""Real Go/analyst synthetic WAV snapshots, 3 rounds. NO training/model run."""
import hashlib
import io
import json
import wave
import sys
from pathlib import Path
import numpy as np
import requests
from library_gateway_check import main


def audio(hz):
    output=io.BytesIO();pcm=(np.sin(np.arange(36000)*2*np.pi*hz/24000)*10000).astype('<i2')
    with wave.open(output,'wb') as stream:
        stream.setnchannels(1);stream.setsampwidth(2);stream.setframerate(24000);stream.writeframes(pcm.tobytes())
    return output.getvalue()


def check(client,base,state,round_id):
    endpoint=base+'/api/prep/training-data'
    assert requests.get(endpoint,timeout=2).status_code==401
    oversize=client.post(endpoint,data=b'{"unknown":"'+b'x'*(1<<20)+b'"}',headers={'Content-Type':'application/json'},timeout=3)
    assert oversize.status_code==413,oversize.text
    row=client.post(base+'/api/prep/libraries',json={'name':f'训练输入合成WAV实验{round_id}'},timeout=3).json()['library']
    library_url=base+'/api/prep/libraries/'+row['id'];raws=[audio(440),audio(660)]
    response=client.post(library_url+'/samples',data={'revision':1},files=[('files',('first.wav',raws[0])),('files',('second.wav',raws[1]))],timeout=3)
    assert response.status_code==200,response.text
    row=response.json()['library']
    body={'library_id':row['id'],'revision':2,'samples':[{'id':s['id'],'text':f'人工合成WAV的格式实验条目{i}，非真人语音训练证明。'} for i,s in enumerate(row['samples'])],
          'reference_sample_id':row['samples'][0]['id'],'voice_rights_confirmed':True,'single_speaker_confirmed':True}
    jobs=client.get(base+'/api/prep/health',timeout=2).json()['jobs']
    assert client.post(endpoint,json={**body,'voice_rights_confirmed':False},timeout=3).status_code==400
    response=client.post(endpoint,json=body,timeout=5);assert response.status_code==200,response.text
    dataset=response.json()['dataset'];directory=state/'training_data'/dataset['id']
    meta=json.loads((directory/'manifest.json').read_text());assert dataset['checks']['training_verified'] is False and dataset['checks']['two_rank_execution_verified'] is False
    assert meta['samples'][0]['source_sha256']==hashlib.sha256(raws[0]).hexdigest()
    assert client.get(base+'/api/prep/health',timeout=2).json()['jobs']==jobs
    verify=endpoint+'/'+dataset['id']+'/verify';pin={'manifest_sha256':dataset['manifest_sha256']}
    assert client.post(verify,json=pin,timeout=3).status_code==200
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'source/py'))
    from training_data import TrainingDataStore
    from resource_limits import UploadLimits
    inputs=TrainingDataStore(state/'training_data',UploadLimits(),free_bytes=0)
    with inputs.lease(dataset['id'],dataset['manifest_sha256']):
        busy=client.delete(endpoint+'/'+dataset['id'],json=pin,timeout=3)
        assert busy.status_code==409,busy.text
        assert client.get(endpoint,timeout=3).status_code==200
    path=directory/'audio'/(row['samples'][0]['id']+'.wav');original=path.read_bytes();path.write_bytes(original+b'!')
    assert client.post(verify,json=pin,timeout=3).status_code==409
    path.write_bytes(original)
    assert client.delete(library_url,json={'revision':2},timeout=3).status_code==200
    assert client.post(verify,json=pin,timeout=3).status_code==200
    assert client.delete(endpoint+'/'+dataset['id'],json=pin,timeout=3).status_code==200
    assert client.get(endpoint,timeout=3).json()['datasets']==[]
    print(json.dumps({'round':round_id,'training_input_http_passed':True,'encoding_read_lease_blocks_http_delete':True,'synthetic_pcm16_wav_only':True,'transcripts_per_sample':2,'fixed_hash_tamper_rejected':True,'source_deletion_does_not_remove_copy':True,'no_new_model_job':True,'training_verified':False}),flush=True)


if __name__=='__main__':
    main(extra_check=check)
    print('TRAINING INPUT HTTP: 3/3 passed. No tokenizer, model, optimizer or actual rank execution.')
