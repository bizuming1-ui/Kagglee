"""完整 Kaggle 源码候选：基于当前可核验 S5，不是 S8-C 恢复包或正式发布。
默认只校验；显式 --run 才安装依赖、下载模型并启动。
Kaggle: %run /path/to/kaggle-step18-candidate.py --run --destination /kaggle/working/qtts18-new
解包目录必须全新；GPU T4 x2 / Internet On。真实训练、音质、首声、RTF未验收。
"""
from __future__ import annotations
import argparse,base64,hashlib,json,os,re,runpy,subprocess,sys,zlib
from pathlib import Path,PurePosixPath

FILES = {}  # BUILDER_REPLACES_THIS_ASSIGNMENT
MAX_FILE=2*1024*1024
MAX_TOTAL=16*1024*1024

def need(value,code):
 if not value:raise ValueError(code)
def sha(raw):return hashlib.sha256(raw).hexdigest()
def safe_name(name):
 need(isinstance(name,str) and name and '\\' not in name and ':' not in name and all(p not in ('','.','..') for p in name.split('/')) and not PurePosixPath(name).is_absolute(),'unsafe_asset_path')
 return name

def decode_files():
 need(isinstance(FILES,dict) and 0<len(FILES)<=256,'asset_count');out={};total=0
 for name,entry in FILES.items():
  safe_name(name);need(isinstance(entry,dict) and set(entry)=={'sha256','bytes','data'},'asset_record')
  need(type(entry['bytes']) is int and 0<=entry['bytes']<=MAX_FILE,'asset_byte_budget')
  need(isinstance(entry['data'],str) and len(entry['data'])<=4*MAX_FILE,'compressed_byte_budget')
  compressed=base64.b64decode(entry['data'],validate=True);decoder=zlib.decompressobj();raw=decoder.decompress(compressed,entry['bytes']+1)
  need(decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail and len(raw)==entry['bytes'],'asset_decompression_or_length')
  need(sha(raw)==entry['sha256'],'asset_sha256');total+=len(raw);need(total<=MAX_TOTAL,'aggregate_byte_budget');out[name]=raw
 return out

def extract_new(destination):
 data=decode_files();target=Path(os.path.abspath(destination))
 need(all(not p.is_symlink() for p in (target,*target.parents)),'symlink_destination')
 need(target.parent.is_dir(),'destination_parent_required');target.mkdir(mode=0o700);os.chmod(target,0o700)
 for name,raw in sorted(data.items()):
  p=target/name;p.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
  fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
  with os.fdopen(fd,'wb') as f:os.fchmod(f.fileno(),0o600);f.write(raw)
 return target

def doctor():
 report={'status':'blocked','mode':'REAL_OPT_IN','release':False,'real_model_executed':False,'training_verified':False,'quality_or_speed_verified':False,'reasons':[],'physical_gpu_count':0}
 if os.environ.get('QTTS_MOCK','0')!='0':report['reasons'].append('mock_environment_not_allowed')
 if os.environ.get('QTTS_ALLOW_SINGLE_GPU','0')!='0':report['reasons'].append('single_gpu_override_not_allowed')
 try:
  cp=subprocess.run(['nvidia-smi','--query-gpu=uuid,name','--format=csv,noheader'],capture_output=True,text=True,timeout=20)
  rows=[line.split(',',1) for line in cp.stdout.splitlines() if line.strip()];report['physical_gpu_count']=len(rows)
  if cp.returncode!=0 or len(rows)!=2 or any(len(row)!=2 or not row[0].strip().startswith('GPU-') or not re.fullmatch(r'(?:Tesla |NVIDIA )?T4',row[1].strip()) for row in rows) or len({row[0].strip() for row in rows})!=2:report['reasons'].append('two_distinct_physical_t4_required')
 except (OSError,subprocess.TimeoutExpired):report['reasons'].append('nvidia_inventory_unavailable')
 if not report['reasons']:report['status']='hardware_visible_runtime_still_unverified'
 return report

def load_secrets():
 # Called only after explicit real opt-in and hardware gate; no values printed.
 try:
  from kaggle_secrets import UserSecretsClient
  client=UserSecretsClient()
  for key in ('DEEPSEEK_API_KEY','HF_TOKEN','KAGGLE_USERNAME','KAGGLE_KEY','QTTS_ACCESS_TOKEN'):
   if not os.environ.get(key):
    try:os.environ[key]=client.get_secret(key)
    except Exception:pass
 except Exception:pass

def main(argv=None):
 parser=argparse.ArgumentParser(description=__doc__);mode=parser.add_mutually_exclusive_group();mode.add_argument('--check',action='store_true');mode.add_argument('--extract-only',action='store_true');mode.add_argument('--doctor',action='store_true');mode.add_argument('--run',action='store_true');parser.add_argument('--destination',type=Path);args=parser.parse_args(argv)
 try:
  data=decode_files()
  if args.doctor or args.run:
   report=doctor();print(json.dumps(report),flush=True)
   if report['status']=='blocked':return 2
   if args.doctor:return 0
  if args.run or args.extract_only:
   need(args.destination is not None,'new_destination_required');root=extract_new(args.destination)
   print(json.dumps({'status':'extracted_only','root':str(root),'assets':len(data),'release':False}),flush=True)
   if args.extract_only:return 0
   os.environ.update(QTTS_ROOT=str(root),QTTS_STATE=str(root/'state'),QTTS_MOCK='0',QTTS_NO_RUST='1',PYTHONUNBUFFERED='1')
   load_secrets()
   # Retains reviewed bootstrap's install/download/readiness/ownership policy.
   # Its return means startup returned, NOT training/quality or final child shutdown.
   runpy.run_path(str(root/'py/bootstrap.py'),run_name='__main__');return 0
  print(json.dumps({'status':'source_verified_not_started','assets':len(data),'source_bytes':sum(map(len,data.values())),'baseline':'available-S5','release':False,'missing_S6_to_S8C_not_reconstructed':True,'real_model_executed':False}));return 0
 except (OSError,ValueError,KeyError,TypeError,zlib.error) as exc:
  print(json.dumps({'status':'rejected','error_type':type(exc).__name__,'release':False}),flush=True);return 1

if __name__=='__main__':
 # Pasting the whole file in a notebook defaults to check, ignoring kernel -f.
 # IPython %run supplies the script argv normally and therefore supports --run.
 notebook_kernel=Path(sys.argv[0]).name in ('ipykernel_launcher.py','ipykernel_launcher')
 code=main([] if notebook_kernel else None)
 if notebook_kernel:
  if code:raise RuntimeError('candidate check failed; see controlled report')
 else:raise SystemExit(code)
