"""Read-only final release/evidence verification, not a GPU/model acceptance test."""
from pathlib import Path
import ast,base64,hashlib,json,re,subprocess,sys,zlib
from urllib.request import urlopen
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda name:(H/name).read_text()

def main():
 assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='arena/041344f2-kagglee'
 raw=(R/'kaggle/kaggle-fixed-step15.py').read_bytes()
 assert len(raw)==291325 and sha(raw)=='61c063f0b2053321bfeafc8509bbbc1c91be183da72739186f7e5c4bf1899d43'
 manifest=json.loads((R/'kaggle/source_manifest_step15.json').read_text())
 assert manifest['launcher_sha256']==sha(raw) and manifest['asset_count']==48 and manifest['stage'].startswith('step15-')
 tree=ast.parse(raw);files=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
 for row in manifest['assets']:
  name=row['path'];b=zlib.decompress(base64.b64decode(files[name][1],validate=True))
  assert b==(R/'kaggle/source'/name).read_bytes() and sha(b)==files[name][0]==row['sha256']
 for name,digest in json.loads(read('frozen-before.json')).items():assert sha((R/name).read_bytes())==digest,name
 handoff=(R/'docs/KAGGLE_HANDOFF_PROMPT.md').read_text();names=re.findall(r'^## 内嵌备忘录：(\S+)$',handoff,re.M)
 assert len(names)==len(set(names))==45
 for name in names:
  body=re.search(r'^## 内嵌备忘录：'+re.escape(name)+r'\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',handoff,re.M|re.S)
  assert body and body.group(1).strip()==(R/'docs'/name).read_text().strip(),name
 questions=re.split(r'^## 问题\d+：',(R/'docs/KAGGLE_DECISIONS.md').read_text(),flags=re.M)[1:]
 assert len(questions)==18 and all(len(re.findall(r'^\d+\. ',q,re.M))==50 for q in questions)
 checklist=re.findall(r'^- \[([ x])\] R[123]-\d{3}：',(R/'docs/KAGGLE_REVIEW_CHECKLIST.md').read_text(),re.M)
 assert len(checklist)==300 and checklist.count('x')==22
 reviews=json.loads(read('review-disposition.json'));assert len({x['recommendation'] for g in reviews['rounds'] for x in g['items']})==300
 for r in (1,2,3):
  assert re.search(r'Ran 301 tests in [\d.]+s\n\nOK\s*$',read(f'python-round{r}.txt'))
  node=read(f'node-round{r}.txt');assert '# pass 30' in node and '# fail 0' in node
  cache=json.loads(read(f'training-cache-round{r}.json'));assert cache['passed'] and cache['same_loss_reports'] and cache['all_adapter_tensors_bitwise_equal'] and cache['same_optimizer_steps']==6
  for prefix in ['real-import','reference-isolation']:
   result=json.loads(read(f'{prefix}-round{r}.json'));assert result['passed'] and not result['full_qwen_model_loaded'] and not result['gpu_executed']
  result=json.loads(read(f'real-preflight-cpu-round{r}.json'));assert result['status']=='blocked'
  c=next(x for x in result['checks'] if x['name']=='qwen_mimi_rope_cpu');assert c['required'] and c['status']=='pass'
  for case in json.loads(read(f'reference-isolation-round{r}.json'))['round_cases']:
   assert case['reference_codes_decoded']==0 and case['samples']==76800 and case['prompt_extractions']==1
 assert re.search(r'360 passed \(',read('browser-repeat3.txt'))
 assert '3 passed (' in read('final-copy-repeat3.txt')
 assert 'ok  ' in read('go-final-race3.txt') and 'WARNING: DATA RACE' not in read('go-final-race3.txt')
 scripts=[('ownership_process_check','real_supervisor_fd_lifecycle_passed'),('training_gateway_check','training_input_http_passed'),('codes_cli_check','local_cli_storage_passed'),('mock_pipeline','passed'),('adapter_gateway_check','passed'),('fatal_startup_check','passed')]
 for prefix,key in scripts:
  rows=[json.loads(line) for line in read(prefix+'.txt').splitlines() if line.startswith('{')]
  selected=[row for row in rows if key in row and 'round' in row]
  assert len(selected)==3 and [row['round'] for row in selected]==[1,2,3] and all(row[key] for row in selected),prefix
  if prefix=='training_gateway_check':assert len([row for row in rows if row.get('real_go_analyst_http') and row.get('passed')])==3
  if prefix=='adapter_gateway_check':assert any(row.get('corrupt_adapter_refused') and row.get('no_pcm_fallback') and row.get('active_retained') for row in rows)
 cp=json.loads(read('copy-page.json'));assert cp['passed'] and len(cp['rounds'])==3 and cp['formal_project_unchanged']
 assert all(x['sha256']==sha(raw) and x['bytes']==len(raw) for x in cp['rounds'])
 for name in ['tools/kaggle-copy-server.mjs','public/kaggle-copy.js']:assert sha(raw) in (R/name).read_text()
 formal=json.loads(urlopen('http://127.0.0.1:3000/api/project').read());old=json.loads(read('formal-api-readonly.json'))
 assert formal['revision']==old['revision'] and {name:sha(body.encode()) for name,body in formal['files'].items()}==old['hashes']
 live=json.loads(urlopen('http://127.0.0.1:3001/api/code').read());assert live['sha256']==sha(raw) and live['code'].encode()==raw
 subprocess.run([sys.executable,str(R/'kaggle/repack.py'),'--check'],check=True,cwd=R)
 result={'passed':True,'stage':15,'artifact_bytes':len(raw),'artifact_sha256':sha(raw),'assets':48,
  'implemented_scope_regressions_passed':True,'all_user_requirements_completed':False,'requirement_status':'PARTIAL/BLOCKED',
  'python':{'per_round':301,'rounds':3,'total':903},'node':{'per_round':30,'rounds':3,'total':90},
  'browser':{'per_round':120,'rounds':3,'total':360,'final_exact_copy_extra':3},'go_race_count':3,
  'protocol_scripts_each_rounds':3,'protocol_script_count':6,'actual_faster_control_flow_with_injected_cpu_model_fixtures_rounds':3,
  'actual_complete_qwen_import_tiny_mimi_reload_rounds':3,'unchanged_training_cpu_adapter_bitwise_ab_rounds':3,'required_real_hf_rope_cpu_smoke_rounds':3,
  'independent_clipboard_download_mobile_rounds':3,'full_qwen_model_executed':False,'gpu_executed':False,
  'actual_qwen_t4_reference_replay_listening_verified':False,'speaker_similarity_or_prosody_preserved_verified':False,
  'actual_first_audible_latency_gain_verified':False,'actual_profile_build_speedup_measured':False,
  'single_t4_two_model_memory_throughput_tested':False,'acoustic_exact_text_rejection_implemented':False,
  'web_training_execution_closed_loop_implemented':False,'long_training_all_samples_sharding_implemented':False,
  'review_recommendations':300,'complete_target_checklist':'22/300','decision_questions':18,'decision_suggestions':900,
  'complete_embedded_memos':45,'frozen_original_through_14_unchanged':True,'formal15_files_head_unchanged':True}
 (H/'final-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
