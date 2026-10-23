#!/usr/bin/env python3
"""Three CPU/mock pipeline rounds; no real GPU, model, voice or paid API involved."""
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import requests

ROOT = Path(__file__).resolve().parents[1] / 'source'
REPO = ROOT.parents[1]
spec = importlib.util.spec_from_file_location('e2e', ROOT/'tools/e2e_check.py')
e2e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e2e)

def free_ports(n):
    sockets = [socket.socket() for _ in range(n)]
    try:
        for s in sockets: s.bind(('127.0.0.1',0))
        return [s.getsockname()[1] for s in sockets]
    finally:
        for s in sockets:s.close()

def wait_for(fn, timeout=12):
    deadline = time.monotonic()+timeout
    while time.monotonic()<deadline:
        try:
            if fn():return
        except (requests.RequestException, ValueError, KeyError):pass
        time.sleep(.05)
    raise AssertionError('timed out waiting for local mock services')

def main():
    results=[]
    token='mock-pipeline-access-token-012345678901234567890123'
    client=requests.Session();client.headers['Authorization']='Bearer '+token
    with tempfile.TemporaryDirectory(prefix='qtts-pipeline-') as d:
        state=Path(d)/'state';voice=state/'profiles/voice';voice.mkdir(parents=True)
        (voice/'profile.json').write_text(json.dumps({'id':'voice','name':'Mock only','language':'Chinese','ref_text':'参考文本','anchor':'unused.wav','units_per_sec':4.5,'breath_files':[],'pause_clause_ms':100,'pause_sentence_ms':200}))
        binary=Path(d)/'gateway'
        go=os.environ.get('QTTS_TEST_GO', str(REPO/'.venv/bin/go'))
        subprocess.run([go,'build','-o',str(binary),'.'],cwd=ROOT/'go/gateway',check=True)
        ports=free_ports(3);base=f'http://127.0.0.1:{ports[2]}'
        env={**os.environ,'QTTS_ROOT':str(ROOT),'QTTS_STATE':str(state),'QTTS_MOCK':'1',
             'QTTS_WORKER_PORTS':','.join(map(str,ports[:2])),'QTTS_GATEWAY_PORT':str(ports[2]),
             'QTTS_WEB':str(ROOT/'web'),'QTTS_MOCK_SPEED':'8','QTTS_BIND':'127.0.0.1','QTTS_ACCESS_TOKEN':token}
        processes=[];logs=[]
        try:
            for i,p in enumerate(ports[:2]):
                log=open(Path(d)/f'worker{i}.log','w+');logs.append(log)
                processes.append(subprocess.Popen([sys.executable,str(ROOT/'py/worker.py'),'--gpu',str(i),'--port',str(p),'--host','127.0.0.1'],env=env,stdout=log,stderr=subprocess.STDOUT))
                wait_for(lambda p=p:requests.get(f'http://127.0.0.1:{p}/health',timeout=1).json()['ready'])
            log=open(Path(d)/'gateway.log','w+');logs.append(log)
            processes.append(subprocess.Popen([str(binary)],cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT))
            wait_for(lambda:len([x for x in client.get(base+'/api/workers',timeout=1).json() if x['ready']])==2)
            assert requests.get(base+'/api/profiles',timeout=1).status_code==401
            response=client.post(base+'/api/profiles/activate',json={'id':'voice'},timeout=5)
            assert response.status_code==200,response.text
            for round_id in range(1,4):
                text='你好，我们正在核对双工作进程的有序调度。每一段文字都应得到对应的音频，不能丢失，也不能重复。接下来核对连续播放的缓冲和结束汇总，然后验证中断后能够继续发起新请求。'
                result=e2e.run(base,'read',text,'voice',access_token=token)
                assert result is not None
                assert not result['errors'],result['errors']
                assert result['end'] is not None
                assert result['ev'] and result['segs']
                order=[x[2] for x in result['ev']];assert order==sorted(order)
                assert all(any(x[2]==i for x in result['ev']) for i in result['segs'])
                assert ''.join(x['text'] for _,x in sorted(result['segs'].items()))==text
                assert {x['gpu'] for x in result['stats'].values()}=={0,1}
                assert all(x.get('rtf') is not None for x in result['stats'].values())
                policy=result['policy'];u,*_=e2e.simulate_player(result['ev'],policy['start_s'],max(policy['low_s'],policy['start_s']))
                assert u==0, f'mock simulated underruns: {u}'
                # Abruptly close a live HTTP stream, then require both workers to go idle.
                interrupted=client.post(base+'/api/speak',json={'mode':'read','profile':'voice','text':text*3},stream=True,timeout=5)
                next(interrupted.iter_content(64));interrupted.close()
                wait_for(lambda:all(not requests.get(f'http://127.0.0.1:{p}/health',timeout=1).json()['busy'] for p in ports[:2]),timeout=8)
                short=e2e.run(base,'read','中断后的新请求可以继续正常合成。','voice',access_token=token)
                assert short and short['end'] is not None and short['ev'] and not short['errors']
                results.append({'round':round_id,'passed':True,'mode':'CPU mock, not real T4', 'segments':len(result['segs']), 'worker_ids':[0,1], 'simulated_underruns':u, 'cancel_then_resume':True})
                print(json.dumps(results[-1],ensure_ascii=False),flush=True)
        except Exception:
            for log in logs:
                log.flush();log.seek(0);print(log.read()[-4000:],file=sys.stderr)
            raise
        finally:
            for p in processes:p.terminate()
            for p in processes:
                try:p.wait(timeout=5)
                except subprocess.TimeoutExpired:p.kill();p.wait()
            for log in logs:log.close()
    print('MOCK PIPELINE: 3/3 passed. This is not GPU/voice-quality evidence.')

if __name__=='__main__':main()
