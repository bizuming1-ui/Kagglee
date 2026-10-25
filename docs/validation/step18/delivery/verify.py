"""Independent read-only complete-delivery seal, not GPU/model acceptance."""
from pathlib import Path
import ast,gzip,hashlib,importlib.util,io,json,re,subprocess,sys,zipfile
R=Path(__file__).resolve().parents[4];H=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'kaggle/delivery18'));import build as b
sha=lambda raw:hashlib.sha256(raw).hexdigest()
def read(n):return json.loads((H/n).read_text())
def packed(n):return json.loads(gzip.decompress((H/n).read_bytes()))
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='arena/1160bd87-kagglee'
m=read('manifest.json');assert m['schema']=='complete-source-delivery-evidence-v1'
for p,v in m['files'].items():assert sha((R/p).read_bytes())==v,p
assert m['files_count']==len(m['files'])
base=read('baseline.json');old=packed('before-files.json.gz');assert len(old)==base['protected_live_files']==3071
for p,v in old.items():assert sha((R/p).read_bytes())==v,p
for p in base['historical_dialogue_artifacts_currently_absent']:assert not (R/p).exists(),p
assert base['not_reconstructed_or_claimed_present'] and base['available_baseline']=='S5'
s5=subprocess.run([sys.executable,str(R/'docs/validation/step18/verify_s5.py')],cwd=R,capture_output=True,timeout=30);assert s5.returncode==0 and s5.stdout==(R/'docs/validation/step18/s5-verification-first.txt').read_bytes()
script=R/'kaggle/delivery18/artifacts/kaggle-step18-candidate.py';zip_path=script.with_name('kaggle-step18-full-source.zip');built_script,built_zip,meta=b.build_bytes();assert script.read_bytes()==built_script and zip_path.read_bytes()==built_zip
build=json.loads(script.with_name('BUILD.json').read_text());assert build['source_assets']==58 and build['launcher_bytes']==286135 and build['zip_bytes']==432569 and build['launcher_sha256']==sha(built_script) and build['zip_sha256']==sha(built_zip)
assert sha(built_script)=='f54346e232b44750f77c506bc9cefd155edd809c0f7444092621fc7b0bb4fab7' and sha(built_zip)=='1559b70d7451736fef4d288539dadf465d15e8a266864167612e0fd628970243'
spec=importlib.util.spec_from_file_location('delivered_entry',script);candidate=importlib.util.module_from_spec(spec);spec.loader.exec_module(candidate);data=candidate.decode_files();assert len(data)==58 and sum(map(len,data.values()))==611276
with zipfile.ZipFile(io.BytesIO(built_zip)) as z:
 assert len(z.infolist())==61 and len(set(z.namelist()))==61
 for p,raw in data.items():assert z.read('source/'+p)==raw and meta['source_assets'][p]['sha256']==sha(raw)
 assert z.read('kaggle-step18-candidate.py')==built_script and json.loads(z.read('MANIFEST.json'))==meta and z.read('README.zh-CN.md')==(R/'kaggle/delivery18/README.zh-CN.md').read_bytes()
for n,p in b.OVERRIDES.items():assert data[n]==(R/p).read_bytes()
for name in b.HELPERS:assert data['py/'+name+'.py']==(R/'kaggle/step18'/(name+'.py')).read_bytes()
for n in (1,2,3):
 d=read(f'round{n}.json');assert d['round']==n and d['passed'] and d['new_unit_tests']==36 and d['cpu_inherited_tests']==610 and d['node_tests']==30 and d['vm_tests']==37 and d['vm_not_added_to_cpu_count'] and d['go_top_level_passes']==40 and d['go_all_pass_events']==56 and d['go_race_not_run'] and len(d['ast_assets'])==38 and not d['real_gpu_or_model_executed']
 assert d['launcher_sha256']==sha(built_script) and d['zip_sha256']==sha(built_zip)
 for p,v in d['source_hashes'].items():assert sha((R/p).read_bytes())==v,p
 for p in d['ast_assets']:ast.parse(data[p])
 for gate in d['gates']:assert gate['exit_code']==2 and gate['no_runtime_created'] and gate['report']['status']=='blocked' and not gate['report']['real_model_executed'] and not gate['report']['training_verified'] and not gate['report']['quality_or_speed_verified']
 cpu=packed(f'cpu-round{n}.json.gz');assert cpu['round']==n and cpu['tests']==610 and cpu['passed'] and not any(cpu[k] for k in ('failures','errors','skipped','actual_gpu_training_or_quality_verified')) and len(cpu['records'])==610 and all(r['status']=='pass' for r in cpu['records'])
 unit=(H/f'unit-console-round{n}.txt').read_text();assert re.search(r'Ran 36 tests in .*\n\nOK\n$',unit) and len(re.findall(r'^test_.* \.\.\. ok$',unit,re.M))==36
 node=(H/f'node-console-round{n}.txt').read_text();assert '# pass 30\n' in node and '# fail 0\n' in node
 vm=json.loads((H/f'vm-console-round{n}.txt').read_text());assert vm['tests']==37 and vm['failures']==0
 go=[json.loads(line) for line in gzip.decompress((H/f'go-round{n}.jsonl.gz').read_bytes()).splitlines()];assert not any(e.get('Action')=='fail' for e in go) and len([e for e in go if e.get('Action')=='pass' and e.get('Test') and '/' not in e['Test']])==40
 smoke=read(f'smoke-round{n}.json');assert smoke['round']==n and smoke['passed'] and smoke['launcher_sha256']==sha(built_script) and smoke['zip_sha256']==sha(built_zip)
 for key in ('fresh_complete_source_extraction','actual_go_offline_build','four_actual_programs','complete_s5_app_served_byte_exact','initial_profiles_empty','gateway_end_present','explicit_synthetic_profile_fixture','all_four_waited_and_pidfd_exit_observed'):assert smoke[key]
 assert smoke['mock_worker_count']==2 and smoke['unauthorized_status']==401 and all(x>0 and x%2==0 for x in smoke['worker_pcm_bytes']) and smoke['gateway_pcm_bytes']>0 and not smoke['physical_gpu_or_model_executed'] and not smoke['physical_audio_quality_or_speed_verified']
 assert len(smoke['processes'])==len({x['pid'] for x in smoke['processes']})==4 and all(x['waited'] and x['pidfd_exit_observed'] for x in smoke['processes'])
assert len(re.findall(r'^\d+\. ',(R/'docs/KAGGLE_STEP18_Q42_COMPLETE_DELIVERY.md').read_text(),re.M))==50
for n in (1,2,3):assert len(set(re.findall(fr'D18-R{n}-\d{{3}}',(R/f'docs/KAGGLE_STEP18_DELIVERY_REVIEW_R{n}.md').read_text())))==100
handoff=(R/'docs/KAGGLE_STEP18_DELIVERY_HANDOFF.md').read_bytes();blocks=re.findall(r'^## 内嵌备忘录：(\S+)\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',handoff.decode(),re.M|re.S);assert len(blocks)==len({p for p,body in blocks})==116
for p,body in blocks:assert body.strip()==(R/'docs'/p).read_text().strip(),p
assert (R/'docs/KAGGLE_STEP18_HANDOFF_PROMPT.md').read_text().rstrip() in handoff.decode()
hr=read('handoff.json');assert hr['completed_memos']==116 and hr['bytes']==len(handoff) and hr['sha256']==sha(handoff) and hr['all_embedded_sources_match'] and not hr['missing_later_stages_reconstructed']
assert subprocess.run(['git','diff','--check'],cwd=R,capture_output=True).returncode==0
result={'step':'complete-kaggle-source-delivery-from-available-S5-not-release','audit_seal_checks_passed':True,'delivery_scope_complete':True,'requirement_status':'PARTIAL/BLOCKED','source_assets':58,'zip_members':61,'launcher_bytes':len(built_script),'launcher_sha256':sha(built_script),'zip_bytes':len(built_zip),'zip_sha256':sha(built_zip),'packaging_unit_passes':[36]*3,'inherited_cpu_passes':[610]*3,'player_vm_passes':[37]*3,'vm_not_added_to_cpu_total':True,'node_passes':[30]*3,'go_top_level_passes':[40]*3,'go_all_pass_events_per_round':56,'go_race_rerun':False,'ast_assets_per_round':38,'fresh_actual_go_four_program_mock_smokes':3,'all_four_owned_programs_waited_each_round':True,'actual_real_run_gate_exit_codes':[2]*3,'real_gpu_models_training_quality_speed_verified':False,'old_173_browser_rerun_this_step':False,'protected_live_paths_unchanged':3071,'available_baseline':'S5','historical_later_artifacts_absent':base['historical_dialogue_artifacts_currently_absent'],'absent_later_artifacts_reconstructed':False,'previous_successful_files_overwritten':False,'formal17_or_workbench_changed':False,'q42_actions':50,'review_recommendations':[100]*3,'complete_handoff_memos':116,'complete_handoff_bytes':len(handoff),'complete_handoff_sha256':sha(handoff),'stage18_production_released':False,'remote_kaggle_deployed':False,'original_300_final_signed_off':0,'overall_completion_percentage':None,'completion_date_estimate':None,'manifest_files':len(m['files'])}
print(json.dumps(result,ensure_ascii=False,indent=2))
