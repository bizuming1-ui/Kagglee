"""New named outputs only: never overwrites historical successful receipts."""
import argparse,ast,gzip,json,os,subprocess,sys,tempfile,unittest
from pathlib import Path
import build as b
R=b.R;H=R/'docs/validation/step18/delivery';PY=sys.executable

def cpu(n):
 sys.path[:0]=[str(R/'docs/validation/step18'),str(R/'kaggle/tests')]
 from run_s5_final_cpu import TARGETS,ReceiptResult
 with tempfile.TemporaryDirectory(prefix='delivery-cpu-',dir=R/'.cache') as td:
  os.environ.update(QTTS_STATE=td,QTTS_MOCK='1',QTTS_NO_RUST='1')
  suite=unittest.defaultTestLoader.loadTestsFromNames(TARGETS)
  with (H/f'cpu-round{n}.txt').open('w') as stream:result=unittest.TextTestRunner(stream=stream,verbosity=2,resultclass=ReceiptResult).run(suite)
  d={'round':n,'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),'passed':result.wasSuccessful() and result.testsRun==610 and not result.skipped,'records':result.records,'actual_gpu_training_or_quality_verified':False,'test_targets':TARGETS}
  (H/f'cpu-round{n}.json.gz').write_bytes(gzip.compress(json.dumps(d,ensure_ascii=False).encode(),mtime=0));assert d['passed'];print(json.dumps({k:v for k,v in d.items() if k not in ('records','test_targets')}))

def run(n):
 commands=[('unit',[PY,str(b.HERE/'test_delivery.py')]),('smoke',[PY,str(b.HERE/'smoke.py'),'--round',str(n)]),('cpu',[PY,str(Path(__file__)),'--cpu-round',str(n)]),('node',['node','--test','tests/server.test.js']),('vm',['node','kaggle/tests/test_step18_playback.mjs',f'--round={n}'])]
 for name,argv in commands:
  out=subprocess.run(argv,cwd=R,capture_output=True,timeout=180);(H/f'{name}-console-round{n}.txt').write_bytes(out.stdout+out.stderr);assert out.returncode==0,(name,out.returncode);print(f'round={n} {name}=PASS',flush=True)
  if name=='vm':
   data=json.loads(out.stdout);assert data['tests']==37 and data['failures']==0
  if name=='node':assert b'# pass 30\n' in out.stdout and b'# fail 0\n' in out.stdout
 script=b.HERE/'artifacts/kaggle-step18-candidate.py'
 with tempfile.TemporaryDirectory(prefix='delivery-gates-',dir=R/'.cache') as td:
  commands=[['--doctor'],['--run','--destination',str(Path(td)/'must-not-exist')]]
  gates=[]
  for args in commands:
   out=subprocess.run([PY,str(script),*args],capture_output=True,timeout=25);need=out.returncode==2 and not (Path(td)/'must-not-exist').exists();assert need;gates.append({'args':args[:1],'exit_code':out.returncode,'report':json.loads(out.stdout),'no_runtime_created':True})
 data,origin=b.capture();parsed=[]
 for p,raw in data.items():
  if p.endswith('.py'):ast.parse(raw);parsed.append(p)
 for p in ('web/app.js','web/recorder.js'):
  out=subprocess.run(['node','--check'],input=data[p],capture_output=True,timeout=20);assert out.returncode==0
 with tempfile.TemporaryDirectory(prefix='delivery-go-',dir=R/'.cache') as td:
  from test_delivery import module
  tree=module().extract_new(Path(td)/'source');go=R/'.venv/lib/python3.11/site-packages/go/bin/go';out=subprocess.run([str(go),'test','-json','-count=1','./...'],cwd=tree/'go/gateway',env={**os.environ,'GOTOOLCHAIN':'local','GOPROXY':'off','GOSUMDB':'off','CGO_ENABLED':'0'},capture_output=True,timeout=120)
  (H/f'go-round{n}.jsonl.gz').write_bytes(gzip.compress(out.stdout+out.stderr,mtime=0));assert out.returncode==0
  events=[json.loads(line) for line in out.stdout.splitlines()];passes=[e['Test'] for e in events if e.get('Action')=='pass' and 'Test' in e];assert passes and not any(e.get('Action')=='fail' for e in events)
 assert subprocess.run(['git','diff','--check'],cwd=R,capture_output=True).returncode==0
 result={'round':n,'passed':True,'new_unit_tests':36,'cpu_inherited_tests':610,'node_tests':30,'vm_tests':37,'vm_not_added_to_cpu_count':True,'go_top_level_passes':len([p for p in passes if '/' not in p]),'go_all_pass_events':len(passes),'go_race_not_run':True,'ast_assets':parsed,'gates':gates,'real_gpu_or_model_executed':False,'source_hashes':{str(p.relative_to(R)):b.sha(p.read_bytes()) for p in sorted(b.HERE.glob('*.py'))},'launcher_sha256':b.sha(script.read_bytes()),'zip_sha256':b.sha((b.HERE/'artifacts/kaggle-step18-full-source.zip').read_bytes())}
 (H/f'round{n}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'round':n,'passed':True,'go_top_level':result['go_top_level_passes'],'ast':len(parsed)}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--cpu-round',type=int);a=ap.parse_args()
 if a.cpu_round:cpu(a.cpu_round)
 else:
  for n in (1,2,3):run(n)
