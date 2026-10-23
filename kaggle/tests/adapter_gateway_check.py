#!/usr/bin/env python3
"""REAL local Go/2-worker HTTP+SSE, CPU LoRA + injected Qwen generator ONLY.

No production mock flag for trained inference. This test explicitly substitutes
model objects in test processes; does NOT attest real Qwen, NCCL, GPU or voice.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import types
import numpy as np

REPO=Path(__file__).resolve().parents[2];ROOT=REPO/'kaggle/source'
sys.path[:0]=[str(ROOT/'py'),str(REPO/'kaggle/tests')]


def fixture_worker():
    # Parse worker's own --gpu/--port while injecting only in this TEST executable.
    import worker
    import torch
    from test_tts_training import TinyCore
    from test_adapter_inference import AdapterTests
    from adapter_engine import AdapterEngine
    torch.set_num_threads(1);torch.manual_seed(17)
    core=TinyCore();core.device=torch.device('cpu');core.dtype=torch.float32
    engine=AdapterEngine(worker.ARGS.gpu,os.environ['QTTS_STATE'],Path(os.environ['QTTS_STATE'])/'unused-base','b'*64)
    def generate(**kw):
        x=torch.tensor([[.2,-.4,.8,1.]])
        value=float(core.talker.self_attn(x).sum())+float(kw['voice_clone_prompt'][0].ref_spk_embedding.sum())
        hz=350+int(abs(value)*100)
        return [np.sin(np.arange(24000)*2*np.pi*hz/24000).astype(np.float32)*.1],24000
    engine.model=types.SimpleNamespace(model=core,generate_voice_clone=generate)
    engine.load=lambda:None # test object was constructed above; no real model load.
    worker.W.engine=engine
    # Keep modules injected for this isolated process lifetime, not production.
    context=AdapterTests().native_api();context.__enter__()
    import uvicorn
    uvicorn.run(worker.app,host='127.0.0.1',port=worker.ARGS.port,log_level='error',access_log=False)


def main():
    import requests
    from test_adapter_inference import AdapterTests
    from mock_pipeline import free_ports,wait_for,e2e
    from library_gateway_check import stop
    fixture=AdapterTests();fixture.setUp();state=fixture.state
    first=fixture.profile();fixture.make_run('e'*32,.4,3);second=fixture.profile('e'*32,'5'*32)
    for profile in (first,second):
        profile.update(name='CPU integration fixture only',model_output_mode='sentence-buffered',units_per_sec=4.5)
        (state/'profiles'/profile['id']/'profile.json').write_text(json.dumps(profile))
    binary=state/'gateway';subprocess.run([str(REPO/'.venv/bin/go'),'build','-o',str(binary),'.'],cwd=ROOT/'go/gateway',check=True)
    ports=free_ports(3);token='adapter-http-fixture-only-token-01234567890123456789'
    class SSE(BaseHTTPRequestHandler):
        def log_message(self,*_):pass
        def do_GET(self):self.send_response(200);self.end_headers()
        def do_POST(self):
            self.rfile.read(int(self.headers.get('Content-Length','0')))
            self.send_response(200);self.send_header('Content-Type','text/event-stream');self.end_headers()
            for text in ('本机SSE替身。','核对选择的训练版本。','不是真实DeepSeek或Qwen语音。'):
                self.wfile.write(('data: '+json.dumps({'choices':[{'delta':{'content':text}}]})+'\n\n').encode());self.wfile.flush()
            self.wfile.write(b'data: [DONE]\n\n')
    llm=ThreadingHTTPServer(('127.0.0.1',0),SSE);thread=threading.Thread(target=llm.serve_forever,daemon=True);thread.start()
    env={**os.environ,'QTTS_ROOT':str(ROOT),'QTTS_STATE':str(state),'QTTS_MOCK':'1','QTTS_TTS_ENGINE':'faster',
         'QTTS_BIND':'127.0.0.1','QTTS_GATEWAY_PORT':str(ports[2]),'QTTS_WORKER_PORTS':','.join(map(str,ports[:2])),
         'QTTS_WEB':str(ROOT/'web'),'QTTS_ACCESS_TOKEN':token,'DEEPSEEK_API_KEY':'local-test-only',
         'DEEPSEEK_BASE_URL':f'http://127.0.0.1:{llm.server_port}'}
    processes=[];base=f'http://127.0.0.1:{ports[2]}';client=requests.Session();client.headers['Authorization']='Bearer '+token
    try:
        with open(state/'services.txt','w+') as output:
            for gpu,port in enumerate(ports[:2]):
                processes.append(subprocess.Popen([sys.executable,__file__,'--fixture-worker','--gpu',str(gpu),'--port',str(port)],env=env,stdout=output,stderr=subprocess.STDOUT))
            for port in ports[:2]:wait_for(lambda port=port:requests.get(f'http://127.0.0.1:{port}/health',timeout=1).json()['ready'],timeout=30)
            processes.append(subprocess.Popen([str(binary)],cwd=ROOT,env=env,stdout=output,stderr=subprocess.STDOUT))
            wait_for(lambda:client.get(base+'/api/health',timeout=1).json()['workers_healthy']==2)
            for round_id in range(1,4):
                for profile in (first,second,first):
                    response=client.post(base+'/api/profiles/activate',json={'id':profile['id']},timeout=10)
                    assert response.status_code==200,response.text
                    result=e2e.run(base,'chat','用已选训练版本回答。',profile['id'],access_token=token)
                    assert result and not result['errors'] and result['end'] and result['ev']
                    assert ''.join(result['texts'])=='本机SSE替身。核对选择的训练版本。不是真实DeepSeek或Qwen语音。'
                    assert [event[2] for event in result['ev']]==sorted(event[2] for event in result['ev'])
                    assert all(s['engine']=='qwen-adapter-buffered' and s['model_output_mode']=='sentence-buffered' and s['chunks']==1 for s in result['stats'].values())
                print(json.dumps({'round':round_id,'passed':True,'real_local_go_http_sse':True,'adapter_A_B_A':True,'qwen_executed':False,'gpu_executed':False,'llm':'local SSE fixture','model':'CPU tiny LoRA; injected native API'}),flush=True)
            # A corrupted pinned adapter must not become active or emit PCM.
            path=state/'training_runs'/('e'*32)/'adapter/speaker.safetensors';path.write_bytes(path.read_bytes()+b'corrupt')
            assert client.post(base+'/api/profiles/activate',json={'id':second['id']},timeout=10).status_code==503
            assert client.get(base+'/api/profiles',timeout=2).json()['active']==first['id']
            for port in ports[:2]:
                raw=requests.post(f'http://127.0.0.1:{port}/synth',json={'profile':second['id'],'text':'错误版本不得输出声音','lead_pause_ms':100},timeout=5).content
                kinds=[]
                while raw:
                    import struct
                    kind,size=struct.unpack('<BI',raw[:5]);kinds.append(kind);raw=raw[5+size:]
                assert 1 not in kinds and 3 in kinds,kinds
            print(json.dumps({'corrupt_adapter_refused':True,'no_pcm_fallback':True,'active_retained':True}),flush=True)
    finally:
        for process in reversed(processes):stop(process)
        llm.shutdown();llm.server_close();thread.join(3);fixture.doCleanups()


if __name__=='__main__':
    if '--fixture-worker' in sys.argv:fixture_worker()
    else:main()
