#!/usr/bin/env python3
"""Three real HTTP Go -> analyst -> filesystem rounds; invalid-audio failure only.

No stub build function, no GPUs/model/DeepSeek. Raw ingestion is deliberately
non-decoding. A later corrupt-audio processing request must FAIL and retain data.
"""
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import requests

ROOT=Path(__file__).resolve().parents[1]/'source'
REPO=ROOT.parents[1]


def ports():
    sockets=[socket.socket() for _ in range(2)]
    try:
        for stream in sockets:stream.bind(('127.0.0.1',0))
        return [stream.getsockname()[1] for stream in sockets]
    finally:
        for stream in sockets:stream.close()


def wait(function):
    deadline=time.monotonic()+12
    while time.monotonic()<deadline:
        try:
            value=function()
            if value:return value
        except requests.RequestException:pass
        time.sleep(.04)
    raise AssertionError('local library service did not reach expected state')


def stop(process):
    process.terminate()
    try:process.wait(3)
    except subprocess.TimeoutExpired:process.kill();process.wait(3)


def main(extra_check=None):
    token='library-gateway-test-only-token-01234567890123456789'
    with tempfile.TemporaryDirectory(prefix='qtts-library-http-') as temporary:
        directory=Path(temporary);state=directory/'state';binary=directory/'gateway'
        subprocess.run([str(REPO/'.venv/bin/go'),'build','-o',str(binary),'.'],cwd=ROOT/'go/gateway',check=True)
        analyst_port,gateway_port=ports();base=f'http://127.0.0.1:{gateway_port}'
        env={**os.environ,'QTTS_ROOT':str(ROOT),'QTTS_STATE':str(state),'QTTS_MOCK':'1',
             'QTTS_ANALYST_PORT':str(analyst_port),'QTTS_GATEWAY_PORT':str(gateway_port),'QTTS_WEB':str(ROOT/'web'),
             'QTTS_BIND':'127.0.0.1','QTTS_ACCESS_TOKEN':token,'DEEPSEEK_API_KEY':'','HF_TOKEN':''}
        processes=[]
        with open(directory/'services.log','w+') as output:
            def start_analyst():
                process=subprocess.Popen([sys.executable,str(ROOT/'py/analyst.py')],env=env,stdout=output,stderr=subprocess.STDOUT)
                processes.append(process)
                wait(lambda:requests.get(f'http://127.0.0.1:{analyst_port}/health',timeout=1).status_code==200)
                return process
            try:
                analyst=start_analyst()
                gateway=subprocess.Popen([str(binary)],cwd=ROOT,env=env,stdout=output,stderr=subprocess.STDOUT);processes.append(gateway)
                client=requests.Session();client.headers['Authorization']='Bearer '+token
                wait(lambda:client.get(base+'/api/prep/libraries',timeout=1).status_code==200)
                for round_id in range(1,4):
                    assert requests.get(base+'/api/prep/libraries',timeout=2).status_code==401
                    response=client.post(base+'/api/prep/libraries',json={'name':f'自己命名的空库{round_id}'},timeout=3)
                    assert response.status_code==200,response.text
                    row=response.json()['library'];url=base+'/api/prep/libraries/'+row['id']
                    assert row['samples']==[] and row['state']=='empty'
                    assert client.get(base+'/api/profiles',timeout=2).json()['profiles']==[]
                    payload=b'A'*((1<<20)+512)  # bigger than Go JSON budget; must use upload budget
                    response=client.post(url+'/samples',data={'revision':1},files=[('files',('large-reference.bin',payload)),('files',('broken.wav',b'bad'))],timeout=5)
                    assert response.status_code==200,response.text
                    row=response.json()['library'];assert len(row['samples'])==2 and row['revision']==2
                    assert row['decoded_duration_verified'] is False and row['training_verified'] is False
                    original={sample['id']:hashlib.sha256((state/'libraries'/row['id']/(sample['id']+'.audio')).read_bytes()).hexdigest() for sample in row['samples']}
                    stop(analyst);analyst=start_analyst()
                    restored=client.get(url,timeout=3).json()['library'];assert restored['samples']==row['samples']
                    response=client.post(url+'/process',json={'revision':2,'sample_ids':[row['samples'][1]['id']],'calibrate':False},timeout=3)
                    assert response.status_code==200,response.text
                    job_id=response.json()['job']
                    def terminal():
                        job=client.get(base+'/api/prep/jobs/'+job_id,timeout=2).json()
                        return job if job['state']!='running' else None
                    job=wait(terminal);assert job['state']=='error',job
                    result=client.get(url,timeout=3).json()['library']
                    assert result['state']=='processing_failed' and not result['busy'] and not result['training_verified']
                    assert result['samples']==row['samples']
                    assert client.get(base+'/api/profiles',timeout=2).json()['profiles']==[]
                    for sid,digest in original.items():assert hashlib.sha256((state/'libraries'/row['id']/(sid+'.audio')).read_bytes()).hexdigest()==digest
                    assert client.delete(url,json={'revision':1},timeout=3).status_code==409
                    assert client.delete(url+'/samples/'+row['samples'][0]['id'],json={'revision':2},timeout=3).status_code==200
                    assert client.delete(url,json={'revision':3},timeout=3).status_code==200
                    assert client.get(url,timeout=3).status_code==404
                    if extra_check is not None:extra_check(client,base,state,round_id)
                    print(json.dumps({'round':round_id,'passed':True,'real_go_analyst_http':True,'upload_above_json_budget':len(payload),'process_restart_restored':True,'corrupt_audio_processing':'expected_error','raw_hashes_unchanged':True,'training_verified':False},ensure_ascii=False),flush=True)
                print('LIBRARY HTTP: 3/3 passed; corrupt processing correctly failed, NOT model/decoder success or training.')
            except Exception:
                output.flush();output.seek(0);print(output.read()[-6000:],file=sys.stderr);raise
            finally:
                for process in reversed(processes):
                    if process.poll() is None:stop(process)


if __name__=='__main__':main()
