"""Deterministic complete S5-based delivery, never edits frozen/candidate originals."""
from __future__ import annotations
import argparse,ast,base64,hashlib,io,json,stat,zipfile,zlib
from pathlib import Path
R=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
OVERRIDES={'py/analyst.py':'kaggle/step18/analyst.py','py/worker.py':'kaggle/step18/worker_s4.py','web/app.js':'kaggle/step18/web/app.js'}
HELPERS=['step18_profile_inputs','step18_calibration_state','step18_calibration_metrics','step18_audio_rt','step18_trimmer']
MEMO='''# 当前完整源码候选：从可核验S5接线，非正式18发布
默认ICL/6dB上限仍为继承值；不预填用户文本或声音，不拼参考PCM。
分析/校准/S4 worker/S5播放器实际接线；DSP使用numpy-causal-v1，Rust不启用。
真实训练、双T4模型、音质、DeepSeek、实体首声/RTF均未签；建档不等于训练。
S6–S8-C文件当前缺失，未冒称恢复；详见README.zh-CN.md。
'''
def sha(raw):return hashlib.sha256(raw).hexdigest()
def capture():
 baseline=json.loads((R/'kaggle/source_manifest_step17.json').read_text());frozen=(R/'kaggle/kaggle-fixed-step17.py').read_bytes();assert sha(frozen)==baseline['launcher_sha256']
 tree=ast.parse(frozen);literal=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets));data={};origin={}
 for row in baseline['assets']:
  n=row['path'];raw=(R/'kaggle/source'/n).read_bytes();assert sha(raw)==row['sha256'] and zlib.decompress(base64.b64decode(literal[n][1]))==raw
  data[n]=raw;origin[n]={'source':'kaggle/source/'+n,'transformation':'unchanged'}
 assert len(data)==53
 for n,p in OVERRIDES.items():data[n]=(R/p).read_bytes();origin[n]={'source':p,'transformation':'candidate-entry-replacement'}
 for name in HELPERS:
  n='py/'+name+'.py';p='kaggle/step18/'+name+'.py';data[n]=(R/p).read_bytes();origin[n]={'source':p,'transformation':'candidate-dependency-added'}
 raw=data['py/bootstrap.py'].decode();node=next(n for n in ast.parse(raw).body if isinstance(n,ast.FunctionDef) and n.name=='build_rust');lines=raw.splitlines(keepends=True)
 data['py/bootstrap.py']=(''.join(lines[:node.lineno-1])+"def build_rust() -> bool:\n    print('Candidate uses numpy-causal-v1; Rust install/build deliberately disabled.')\n    return False\n"+''.join(lines[node.end_lineno:])).encode();origin['py/bootstrap.py']['transformation']='only-build_rust-function-disabled'
 data['MEMO.md']=MEMO.encode();origin['MEMO.md']['transformation']='replace-stale-historical-homepage-with-candidate-scope'
 return data,origin

def build_bytes():
 data,origin=capture();records={p:{'sha256':sha(raw),'bytes':len(raw),'data':base64.b64encode(zlib.compress(raw,9)).decode()} for p,raw in sorted(data.items())}
 template=(HERE/'launcher_template.py').read_text();marker='FILES = {}  # BUILDER_REPLACES_THIS_ASSIGNMENT';assert template.count(marker)==1
 script=template.replace(marker,'FILES = '+repr(records)).encode();ast.parse(script)
 readme=(HERE/'README.zh-CN.md').read_bytes();meta={'schema':'complete-s5-based-kaggle-candidate-v1','release':False,'real_model_verified':False,'missing_later_stages_reconstructed':False,'source_assets':{p:{'sha256':sha(raw),'bytes':len(raw),**origin[p]} for p,raw in sorted(data.items())},'launcher_sha256':sha(script),'readme_sha256':sha(readme)}
 contents={**{'source/'+p:raw for p,raw in data.items()},'kaggle-step18-candidate.py':script,'README.zh-CN.md':readme,'MANIFEST.json':json.dumps(meta,ensure_ascii=False,sort_keys=True,indent=2).encode()+b'\n'}
 out=io.BytesIO()
 with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for name,raw in sorted(contents.items()):
   info=zipfile.ZipInfo(name,(1980,1,1,0,0,0));info.create_system=3;info.external_attr=(stat.S_IFREG|0o600)<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,raw,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
 assert capture()==(data,origin),'source_changed_during_build'
 return script,out.getvalue(),meta

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);a=ap.parse_args();script,archive,meta=build_bytes();a.output_dir.mkdir(mode=0o700)
 for name,raw in [('kaggle-step18-candidate.py',script),('kaggle-step18-full-source.zip',archive)]:
  with (a.output_dir/name).open('xb') as f:f.write(raw)
 summary={'source_assets':len(meta['source_assets']),'launcher_bytes':len(script),'launcher_sha256':sha(script),'zip_bytes':len(archive),'zip_sha256':sha(archive),'release':False,'real_gpu_or_quality_verified':False};(a.output_dir/'BUILD.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
if __name__=='__main__':main()
