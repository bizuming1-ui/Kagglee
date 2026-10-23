"""Verify current review2 progress, not product/voice completion. Requires extracted reviewed wheels."""
from pathlib import Path
import ast,hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent;D=R/'docs'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
b=json.loads((H/'baseline.json').read_text())
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='arena/03d65d8e-kagglee'
assert all(sha(R/name)==value for name,value in b['frozen_hashes'].items())
assert all(sha(R/row['path'])==row['sha256'] for row in b['source_inventory'])
assert sha(D/'KAGGLE_HANDOFF_PROMPT.md')==b['historical_handoff_sha256']
for r in (1,2):
    rows=json.loads((H/f'review{r}.json').read_text())['recommendations']
    assert len(rows)==len({row['id'] for row in rows})==100
    assert len(re.findall(r'^\d+\. \[S18-R'+str(r)+r'-\d{3}\]',(D/f'KAGGLE_STEP18_REVIEW{r}.md').read_text(),re.M))==100
assert not (D/'KAGGLE_STEP18_REVIEW3.md').exists()
upstream=json.loads((H/'upstream-round2-provenance.json').read_text())
for row in upstream['inspected_wheels']:
    p=R/'.cache/step18/wheels'/row['wheel_url'].rsplit('/',1)[-1]
    assert sha(p)==row['wheel_sha256']
assert upstream['reviewed_runtime_provider']=='qwen-tts-hf==0.1.1.post1'
assert not upstream['full_models_executed']
dsp=[];reference=[]
for r in (1,2,3):
    d=json.loads((H/f'dsp-partition-baseline-round{r}.json').read_text());assert d['experiment_completed'] and len(d['cases'])==12 and not d['model_executed'];dsp.append(d['cases'])
    j=json.loads((H/f'reference-state-baseline-round{r}.json').read_text())
    assert j['experiment_completed'] and not j['full_model_executed'] and not j['gpu_executed']
    assert len(j['prompt_contract_cases'])==6 and len(j['calibration_cases'])==4 and len(j['candidate_payload_cases'])==9
    assert j['probe_sha256']==sha(R/'kaggle/tests/reference_state_probe.py')
    assert all(sha(R/p)==value for p,value in j['source_hashes'].items())
    assert all(c['rejected'] for c in j['prompt_contract_cases'][:2])
    concurrent=next(c for c in j['calibration_cases'] if c['case']=='concurrent-candidate-edit')
    assert concurrent['assessed_reference_texts'][1]['ref_text']=='old-text-1' and concurrent['final_ref_text']=='new-unassessed-text'
    failed_reload=next(c for c in j['calibration_cases'] if c['case']=='reload-failed');assert failed_reload['function_returned_normally'] and not any(x['ok'] for x in failed_reload['reload_receipts'])
    assert [x['seed'] for x in j['consistency_case']['calls']]==[100,101]
    reference.append({k:j[k] for k in ('prompt_contract_cases','calibration_cases','candidate_payload_cases','consistency_case')})
assert dsp[0]==dsp[1]==dsp[2] and reference[0]==reference[1]==reference[2]
assert '# pass 30' in (H/'round2-node.txt').read_text() and '# fail 0' in (H/'round2-node.txt').read_text()
hand=(D/'KAGGLE_STEP18_HANDOFF_PROMPT.md').read_text();names=re.findall(r'^## 内嵌备忘录：(\S+)$',hand,re.M)
assert len(names)==len(set(names))==60
for name in names:
    body=re.search(r'^## 内嵌备忘录：'+re.escape(name)+r'\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',hand,re.M|re.S)
    assert body and body.group(1).strip()==(D/name).read_text().strip(),name
for p in [R/'kaggle/tests/reference_state_probe.py',H/'fetch_reviewed_upstream.py',H/'prepare_round2.py',H/'refresh_handoff.py']:ast.parse(p.read_bytes())
result={'step':'second-topical-review-only','passed':True,'branch':b['branch'],'stage17_assets_unchanged':53,
    'frozen_hashes_verified':len(b['frozen_hashes']),'formal_15_files_unchanged':True,'review_rounds_recorded':2,'recommendations_each_round':100,
    'review3_completed':False,'full_source_three_semantic_reviews_complete':False,'stage18_self_qa_completed':False,
    'node_tests_passed_this_step':30,'reference_state_control_cases_per_round':20,'reference_state_rounds':3,
    'dsp_synthetic_cases_per_round':12,'dsp_rounds':3,'upstream_wheels_sha256_verified':3,
    'handoff_complete_memos':60,'handoff_bytes':len(hand.encode()),'handoff_sha256':sha(D/'KAGGLE_STEP18_HANDOFF_PROMPT.md'),
    'product_source_modified':False,'stage18_release_created':False,'full_functional_validation_completed':False,
    'full_model_executed':False,'gpu_executed':False,'user_hiss_root_cause_proven':False,'all_user_requirements_completed':False}
(H/'progress-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
