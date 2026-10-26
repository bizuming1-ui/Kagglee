"""Fresh complete delivered tree + real Go/HTTP + explicit CPU MOCK, never GPU proof."""
import gzip,hashlib,http.client,importlib.util,json,os,secrets,selectors,signal,socket,struct,subprocess,sys,tempfile,time,wave
from pathlib import Path
import build as b
R=b.R;H=R/'docs/validation/step18/delivery';GO=R/'.venv/lib/python3.11/site-packages/go/bin/go'
def need(v,code):
 if not v:raise AssertionError(code)
def port():
 with socket.socket() as s:s.bind(('127.0.0.1',0));return s.getsockname()[1]
def call(p,path,body=None,token=None):
 c=http.client.HTTPConnection('127.0.0.1',p,timeout=30)
 try:
  headers={'Authorization':'Bearer '+token} if token else {}
  if body is not None:headers['Content-Type']='application/json'
  c.request('POST' if body is not None else 'GET',path,json.dumps(body).encode() if body is not None else None,headers);r=c.getresponse();return r.status,r.read(8*1024*1024)
 finally:c.close()
def wait_health(p,children,token=None):
 deadline=time.monotonic()+30
 while time.monotonic()<deadline:
  need(all(c.poll() is None for c in children),'owned_service_early_exit')
  try:
   status,raw=call(p,'/api/health' if token else '/health',token=token);d=json.loads(raw)
   if status==200 and d.get('ready',d.get('ok',False)):return d
  except (OSError,ValueError):pass
  time.sleep(.03)
 raise AssertionError('readiness_deadline')
def frames(raw,header):
 out=[];size=struct.calcsize(header)
 while raw:
  need(len(raw)>=size,'truncated_frame_header');fields=struct.unpack(header,raw[:size]);n=fields[-1];need(n<=len(raw)-size,'truncated_frame_body');out.append((fields,raw[size:size+n]));raw=raw[size+n:]
 return out

def run(number):
 script=b.HERE/'artifacts/kaggle-step18-candidate.py';spec=importlib.util.spec_from_file_location('complete_candidate',script);candidate=importlib.util.module_from_spec(spec);spec.loader.exec_module(candidate)
 processes=[];fds=[];logs=[];observations=[];result={}
 with tempfile.TemporaryDirectory(prefix='delivery-smoke-',dir=R/'.cache') as temp:
  private=Path(temp);tree=candidate.extract_new(private/'source');state=private/'state';state.mkdir(mode=0o700);ports=[port() for _ in range(4)];need(len(set(ports))==4,'port_reservation_collision');token=secrets.token_urlsafe(32)
  env={k:v for k,v in os.environ.items() if k in ('HOME','PATH','LANG','LD_LIBRARY_PATH')};env.update(QTTS_ROOT=str(tree),QTTS_STATE=str(state),QTTS_AUTH_DIR=str(private/'auth'),QTTS_MOCK='1',QTTS_NO_RUST='1',QTTS_TTS_ENGINE='faster',QTTS_CLONE_MODE='icl',QTTS_WORKER_PORTS=','.join(map(str,ports[:2])),QTTS_ANALYST_PORT=str(ports[2]),QTTS_GATEWAY_PORT=str(ports[3]),QTTS_ACCESS_TOKEN=token,QTTS_WEB=str(tree/'web'),QTTS_BIND='127.0.0.1',QTTS_MOCK_SPEED='3',DEEPSEEK_API_KEY='',PYTHONUNBUFFERED='1')
  binary=private/'gateway';compiled=subprocess.run([str(GO),'build','-trimpath','-buildvcs=false','-o',str(binary),'.'],cwd=tree/'go/gateway',env={**env,'GOTOOLCHAIN':'local','GOPROXY':'off','GOSUMDB':'off','CGO_ENABLED':'0'},capture_output=True,timeout=120);need(compiled.returncode==0,'actual_offline_go_build_failed')
  roles=[('worker0',[sys.executable,str(tree/'py/worker.py'),'--gpu','0','--port',str(ports[0])]),('worker1',[sys.executable,str(tree/'py/worker.py'),'--gpu','1','--port',str(ports[1])]),('analyst',[sys.executable,str(tree/'py/analyst.py')]),('gateway',[str(binary)])]
  try:
   for role,argv in roles:
    log=(private/(role+'.txt')).open('wb');logs.append(log);p=subprocess.Popen(argv,cwd=tree,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True);processes.append(p);fds.append(os.pidfd_open(p.pid));observations.append({'role':role,'pid':p.pid})
   health=[wait_health(p,processes) for p in ports[:3]];wait_health(ports[3],processes,token)
   need(all(d['engine']=='mock' and not d['model_loaded'] and d['rt']=='numpy-causal-v1' for d in health[:2]),'worker_not_explicit_causal_mock');need(health[2]['mock'] is True,'analyst_not_mock')
   unauthorized,_=call(ports[3],'/api/profiles');need(unauthorized==401,'auth_weakened')
   status,raw=call(ports[3],'/app.js');need(status==200 and raw==(tree/'web/app.js').read_bytes(),'complete_frontend_not_served')
   status,raw=call(ports[3],'/api/profiles',token=token);need(status==200 and json.loads(raw)['profiles']==[],'profiles_prefilled')
   profile=state/'profiles/audit-fixture';profile.mkdir(parents=True)
   with wave.open(str(profile/'anchor.wav'),'wb') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(24000);f.writeframes(b'\0'*4800)
   (profile/'profile.json').write_text(json.dumps({'id':'audit-fixture','anchor':'anchor.wav','ref_text':'explicit synthetic fixture','language':'Chinese','units_per_sec':4.5}))
   status,raw=call(ports[3],'/api/profiles/activate',{'id':'audit-fixture'},token);activation=json.loads(raw);need(status==200 and all(w['ok'] for w in activation['workers']) and len(activation['workers'])==2,'two_mock_workers_not_activated')
   worker_pcm=[]
   for p in ports[:2]:
    status,raw=call(p,'/synth',{'profile':'audit-fixture','text':'明确的模拟测试。','seed':42});rows=frames(raw,'<BI');pcm=sum(len(v) for f,v in rows if f[0]==1);need(status==200 and pcm>0 and pcm%2==0 and any(f[0]==2 for f,v in rows) and not any(f[0]==3 for f,v in rows),'mock_worker_stream_failed');worker_pcm.append(pcm)
   status,raw=call(ports[3],'/api/speak',{'profile':'audit-fixture','mode':'read','text':'这是明确的模拟联通测试，不是真实模型。'},token);rows=frames(raw,'<BII');pcm=sum(len(v) for f,v in rows if f[0]==1)
   need(status==200 and pcm>0 and any(f[0]==5 for f,v in rows) and not any(f[0]==6 for f,v in rows),'gateway_framed_stream_failed')
   result={'round':number,'passed':True,'fresh_complete_source_extraction':True,'actual_go_offline_build':True,'gateway_binary_sha256':b.sha(binary.read_bytes()),'four_actual_programs':True,'unauthorized_status':unauthorized,'complete_s5_app_served_byte_exact':True,'initial_profiles_empty':True,'mock_worker_count':2,'worker_pcm_bytes':worker_pcm,'gateway_pcm_bytes':pcm,'gateway_end_present':True,'explicit_synthetic_profile_fixture':True,'physical_gpu_or_model_executed':False,'physical_audio_quality_or_speed_verified':False,'processes':observations,'launcher_sha256':b.sha(script.read_bytes()),'zip_sha256':b.sha((b.HERE/'artifacts/kaggle-step18-full-source.zip').read_bytes())}
  finally:
   for p in processes:
    if p.poll() is None:
     try:os.killpg(p.pid,signal.SIGTERM)
     except ProcessLookupError:pass
   for p in processes:
    try:p.wait(timeout=10)
    except subprocess.TimeoutExpired:
     os.killpg(p.pid,signal.SIGKILL);p.wait(timeout=5)
   for row,p,fd in zip(observations,processes,fds):
    with selectors.DefaultSelector() as sel:sel.register(fd,selectors.EVENT_READ);row.update(waited=True,exit_code=p.returncode,pidfd_exit_observed=bool(sel.select(3)));need(row['pidfd_exit_observed'],'owned_pid_survived')
    os.close(fd)
   for log in logs:log.close()
   for path in private.glob('*.txt'):need(token.encode() not in path.read_bytes(),'token_leaked_in_child_log')
  need(len(observations)==4 and len({r['pid'] for r in observations})==4,'four_unique_owned_programs_required')
  result['all_four_waited_and_pidfd_exit_observed']=True
 return result
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--round',type=int,required=True);n=ap.parse_args().round;d=run(n);(H/f'smoke-round{n}.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
