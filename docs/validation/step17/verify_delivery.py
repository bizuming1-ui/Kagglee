"""Read-only release evidence verification. No GPU/acoustic target inference."""
from pathlib import Path
import ast,base64,hashlib,json,re,subprocess,sys,zlib
from urllib.request import urlopen
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda name:(H/name).read_text()
def main():
 assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='arena/041344f2-kagglee'
 raw=(R/'kaggle/kaggle-fixed-step17.py').read_bytes()
 assert len(raw)==313504 and sha(raw)=='6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea'
 m=json.loads((R/'kaggle/source_manifest_step17.json').read_text())
 assert m['launcher_sha256']==sha(raw) and m['asset_count']==53
 files=ast.literal_eval(next(n.value for n in ast.parse(raw).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
 for row in m['assets']:
  name=row['path'];b=zlib.decompress(base64.b64decode(files[name][1],validate=True))
  assert b==(R/'kaggle/source'/name).read_bytes() and sha(b)==files[name][0]==row['sha256']
 for name,digest in json.loads(read('frozen-before.json')).items():assert sha((R/name).read_bytes())==digest,name
 assert sha((R/'kaggle/kaggle-fixed-step16.py').read_bytes())=='c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429'
 handoff=(R/'docs/KAGGLE_HANDOFF_PROMPT.md').read_text();names=re.findall(r'^## 内嵌备忘录：(\S+)$',handoff,re.M)
 assert len(names)==len(set(names))==57
 for name in names:
  body=re.search(r'^## 内嵌备忘录：'+re.escape(name)+r'\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',handoff,re.M|re.S)
  assert body and body.group(1).strip()==(R/'docs'/name).read_text().strip(),name
 qs=re.split(r'^## 问题\d+：',(R/'docs/KAGGLE_DECISIONS.md').read_text(),flags=re.M)[1:]
 assert len(qs)==24 and all(len(re.findall(r'^\d+\. ',q,re.M))==50 for q in qs)
 checks=re.findall(r'^- \[([ x])\] R[123]-\d{3}：',(R/'docs/KAGGLE_REVIEW_CHECKLIST.md').read_text(),re.M)
 assert len(checks)==300 and checks.count('x')==22
 d=json.loads(read('review-disposition.json'));assert len({i['recommendation'] for g in d['rounds'] for i in g['items']})==300
 assert len(d['rounds'])==3 and all(len(g['items'])==100 for g in d['rounds'])
 for r in (1,2,3):
  assert re.search(r'Ran 334 tests in [\d.]+s\n\nOK\s*$',read(f'python-round{r}.txt'))
  assert '# pass 30' in read(f'node-round{r}.txt') and '# fail 0' in read(f'node-round{r}.txt')
  for label in ['long-reference','reference-isolation','actual-codec','real-import','training-cache']:
   data=json.loads(read(f'{label}-round{r}.json'));assert data['passed']
   if label!='training-cache':assert not data['full_qwen_model_loaded'] and not data['gpu_executed']
   if label=='long-reference':
    assert data['baseline_frozen16_reproduced_no_aligned_error'] and data['current17_same_fixture_build_succeeded']
    assert data['alignment']['word_split_segments']>1 and data['window_retranscription_fixture']['asr_windows']==2
    assert data['all_window_samples_consumed']==round(28.7*16000) and all(c['file_frames']<=16*24000 for c in data['saved_candidate_wavs'])
   if label=='reference-isolation':
    assert len(data['round_cases'])==8
    for c in data['round_cases']:assert c['samples']==153600 and c['reference_codes_decoded']==0 and c['after_same_path_reload']==2
   if label=='actual-codec':
    assert data['random_tiny_parameters']==23813 and data['causal_prefix_max_abs']<=1e-6
    assert len(data['round_cases'])==8 and all(c['samples']==76800 for c in data['round_cases'])
   if label=='training-cache':assert data['same_loss_reports'] and data['all_adapter_tensors_bitwise_equal'] and data['same_optimizer_steps']==6
  p=json.loads(read(f'real-preflight-cpu-round{r}.json'));assert p['status']=='blocked'
  c=next(c for c in p['checks'] if c['name']=='qwen_mimi_rope_cpu');assert c['required'] and c['status']=='pass'
  assert all(c['status']=='pass' for c in p['checks'] if c['name'].startswith('api.'))
 assert '369 passed (' in read('browser-repeat3.txt')
 assert '3 passed (' in read('final-copy-repeat3.txt')
 assert 'ok  ' in read('go-final-race3.txt') and 'WARNING: DATA RACE' not in read('go-final-race3.txt')
 scripts=[('ownership_process_check','real_supervisor_fd_lifecycle_passed'),('training_gateway_check','training_input_http_passed'),('codes_cli_check','local_cli_storage_passed'),('mock_pipeline','passed'),('adapter_gateway_check','passed'),('fatal_startup_check','passed')]
 for script,key in scripts:
  rows=[json.loads(line) for line in read(script+'.txt').splitlines() if line.startswith('{')]
  selected=[row for row in rows if key in row and 'round' in row]
  assert len(selected)==3 and [row['round'] for row in selected]==[1,2,3] and all(row[key] for row in selected),script
  if script=='training_gateway_check':assert len([row for row in rows if row.get('real_go_analyst_http') and row.get('passed')])==3
  if script=='adapter_gateway_check':assert any(row.get('corrupt_adapter_refused') and row.get('no_pcm_fallback') and row.get('active_retained') for row in rows)
 cp=json.loads(read('copy-page.json'));assert cp['passed'] and len(cp['rounds'])==3 and cp['formal_project_unchanged']
 assert all(c['sha256']==sha(raw) and c['bytes']==len(raw) for c in cp['rounds'])
 for name in ['tools/kaggle-copy-server.mjs','public/kaggle-copy.js']:assert sha(raw) in (R/name).read_text()
 live=json.loads(urlopen('http://127.0.0.1:3001/api/code').read());assert live['code'].encode()==raw
 p=json.loads(urlopen('http://127.0.0.1:3000/api/project').read());old=json.loads(read('formal-api-readonly.json'))
 assert p['revision']==old['revision'] and {n:sha(t.encode()) for n,t in p['files'].items()}==old['hashes']
 blocked=json.loads(read('target-rtf-not-run.json'));assert blocked['status']=='blocked' and blocked['measurements']==[] and not blocked['real_gpu_verified']
 subprocess.run([sys.executable,str(R/'kaggle/repack.py'),'--check'],check=True,cwd=R)
 result={'passed':True,'stage':17,'artifact_bytes':len(raw),'artifact_sha256':sha(raw),'assets':53,
 'implemented_scope_regressions_passed':True,'all_user_requirements_completed':False,'requirement_status':'PARTIAL/BLOCKED',
 'python':{'per_round':334,'rounds':3,'total':1002},'node':{'per_round':30,'rounds':3,'total':90},
 'browser':{'per_round':123,'rounds':3,'total':369,'final_exact_copy_extra':3},'go_race_count':3,
 'protocol_scripts_each_rounds':3,'protocol_script_count':6,'actual_faster_cpu_control_rounds':3,'frozen16_vs17_long_reference_fixture_rounds':3,
 'actual_random_tiny_qwen_codec_rounds':3,'actual_complete_import_tiny_mimi_rounds':3,'cpu_training_bitwise_ab_rounds':3,
 'full_qwen_model_executed':False,'gpu_executed':False,'speaker_similarity_verified':False,
 'single_speaker_listening_verified':False,'no_hiss_listening_verified':False,'genuine_t4_rtf_0_3_verified':False,
 'seamless_reading_listening_verified':False,'dual_gpu_timbre_equivalence_verified':False,'real_whisper_reference_test_executed':False,
 'rtf_benchmark_measurements_in_this_sandbox':0,'formal_workbench_unchanged':True,'handoff_complete_memos':57,
 'handoff_bytes':len(handoff.encode()),'handoff_sha256':sha(handoff.encode()),'frozen_file_hashes_verified':len(json.loads(read('frozen-before.json'))),
 'question_count':24,'question_suggestions':1200,'target_checklist_completed':22,'target_checklist_total':300,
 'review_dispositions':d['counts']}
 (H/'final-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
