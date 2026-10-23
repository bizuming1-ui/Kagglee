#!/usr/bin/env python3
"""Read-only formal workbench + release evidence checks; never runs a model."""
import ast
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.request import urlopen
import zlib
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent
sha=lambda raw:hashlib.sha256(raw).hexdigest()
read=lambda name:(H/name).read_text()


def main():
    assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='arena/041344f2-kagglee'
    artifact=R/'kaggle/kaggle-fixed-step12.py';raw=artifact.read_bytes()
    assert len(raw)==282031 and sha(raw)=='2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08'
    manifest=json.loads((R/'kaggle/source_manifest_step12.json').read_text());assert manifest['launcher_sha256']==sha(raw) and manifest['asset_count']==47
    tree=ast.parse(raw);files=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
    assert len(files)==47
    for row in manifest['assets']:
        decoded=zlib.decompress(base64.b64decode(files[row['path']][1],validate=True))
        assert decoded==(R/'kaggle/source'/row['path']).read_bytes()
        assert sha(decoded)==files[row['path']][0]==row['sha256'] and len(decoded)==row['bytes']
    for stage in range(1,12):
        filename='source_manifest.json' if stage==1 else f'source_manifest_step{stage}.json'
        old=json.loads((R/'kaggle'/filename).read_text());assert sha((R/f'kaggle/kaggle-fixed-step{stage}.py').read_bytes())==old['launcher_sha256']
    assert sha((R/'kaggle/kaggle-fixed-step10.py').read_bytes())=='2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4'
    assert sha((R/'kaggle/kaggle-fixed-step11.py').read_bytes())=='cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e'
    head=json.loads((R/'workspace/HEAD.json').read_text())
    assert sha((R/'workspace/revisions'/head['revision']/'kaggle').read_bytes())=='26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461'
    handoff=(R/'docs/KAGGLE_HANDOFF_PROMPT.md').read_text();names=re.findall(r'^## 内嵌备忘录：(\S+)$',handoff,re.M)
    assert len(names)==len(set(names))==30
    for name in names:
        body=re.search(r'^## 内嵌备忘录：'+re.escape(name)+r'\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',handoff,re.M|re.S)
        assert body and body.group(1).strip()==(R/'docs'/name).read_text().strip(),name
    questions=re.split(r'^## 问题\d+：',(R/'docs/KAGGLE_DECISIONS.md').read_text(),flags=re.M)[1:]
    assert len(questions)==11 and all(len(re.findall(r'^\d+\. ',q,re.M))==50 for q in questions)
    checklist=re.findall(r'^- \[([ x])\] R[123]-\d{3}：',(R/'docs/KAGGLE_REVIEW_CHECKLIST.md').read_text(),re.M)
    assert len(checklist)==300 and checklist.count('x')==22
    review=json.loads(read('review-map.json'));assert [len(g['items']) for g in review['rounds']]==[100,100,100]
    for i in (1,2,3):
        log=read(f'python-round{i}.txt');assert re.search(r'Ran 267 tests in [\d.]+s\n\nOK\s*$',log)
        node=read(f'node-round{i}.txt');assert '# pass 30' in node and '# fail 0' in node
    for prefix,key in [('ownership_process_check','real_supervisor_fd_lifecycle_passed'),('training_gateway_check','training_input_http_passed'),('codes_cli_check','local_cli_storage_passed'),('mock_pipeline','passed')]:
        records=[json.loads(line) for line in read(f'{prefix}.txt').splitlines() if line.startswith('{')]
        records=[r for r in records if key in r];assert len(records)==3 and all(r[key] for r in records),(prefix,key)

    assert re.search(r'^ok\s+qtts/gateway',read('go-race3.txt'),re.M)
    assert re.search(r'339 passed',read('browser-repeat3.txt')) and not re.search(r'\d+ failed',read('browser-repeat3.txt'))
    assert '3 passed' in read('final-copy-repeat3.txt')
    records=[json.loads(line) for line in read('adapter_gateway_check.txt').splitlines() if line.startswith('{')]
    assert len(records)==4 and all(r['passed'] and r['adapter_A_B_A'] and not r['qwen_executed'] and not r['gpu_executed'] for r in records[:3])
    assert all(records[-1][key] for key in ('corrupt_adapter_refused','no_pcm_fallback','active_retained'))
    for name in ('real-wheel-cpu.json','real-wheel-cpu-repeat2.json','real-wheel-cpu-repeat3.json'):
        cpu=json.loads(read(name));assert cpu['passed'] and cpu['transformers_version']=='5.20.2' and not cpu['full_qwen_model_loaded'] and not cpu['gpu_executed']
        assert 'rope_theta' in cpu['reported_attribute_error_reproduced'] and cpu['configuration_unchanged']
    fatal=[json.loads(line) for line in read('fatal-startup-process3.txt').splitlines() if line.startswith('{')]
    assert len(fatal)==3 and all(r['passed'] and r['worker_exited'] and r['owned_supervisor_shutdown'] and not r['gpu_executed'] for r in fatal)
    copies=json.loads(read('copy-page.json'));assert copies['passed'] and copies['formal_project_unchanged'] and len(copies['rounds'])==3
    old=json.loads((R/'docs/validation/step11/formal-api-readonly.json').read_text())
    with urlopen('http://127.0.0.1:3000/api/project',timeout=5) as response:project=json.load(response)
    hashes={n:sha(v.encode()) for n,v in project['files'].items()}
    assert hashes==old['hashes'] and project['revision']==old['revision']==head['revision']
    total=sum(len(v.encode()) for v in project['files'].values());assert len(hashes)==15 and total==1043155
    for name,hashed in hashes.items():assert sha((R/'workspace/revisions'/head['revision']/name).read_bytes())==hashed
    (H/'formal-api-readonly.json').write_text(json.dumps({**old,'all15HashesMatchStage11Receipt':True,'readOnly':True},ensure_ascii=False,indent=2)+'\n')
    sys.path.insert(0,str(R/'kaggle/source/py'))
    from gpu_ownership import status
    lock=status();assert lock['busy'] is False
    result={'artifact_bytes':len(raw),'artifact_sha256':sha(raw),'assets':47,'original_through_step11_frozen':True,
            'complete_embedded_memos':30,'questions':11,'suggestions':550,'checklist_checked':22,'checklist_total':300,
            'python':{'unique':267,'rounds':3,'passed':801},'browser':{'unique':113,'rounds':3,'passed':339},
            'final_copy_passed':3,'go_race_count':3,'node_passed':90,'protocol_scripts_each_rounds':3,
            'adapter_real_local_go_http_sse_rounds':3,'adapter_model':'real CPU tiny LoRA + injected native API; local SSE fixture',
            'no_pcm_fallback_on_corrupt_adapter':True,'formal_head_and_all15_hashes_unchanged':True,
            'explicit_adapter_chat_code_implemented':True,'mimi_rope_config_bug_reproduced_and_bridged':True,'real_wheel_cpu_rounds':3,'fatal_controller_process_rounds':3,'session_resident_policy_implemented':True,'permanent_kaggle_gpu_guaranteed':False,'native_model_output_mode':'sentence-buffered',
            'real_dual_t4_detected_in_user_prior_run':True,'fresh_step12_gpu_model_load_verified':False,'browser_copy_page_real_clipboard_rounds':3,'browser_copy_page_download_exact':True,'all_non_gpu_release_checks_passed':True,'qwen_training_executed':False,'qwen_inference_executed':False,'gpu_verified':False,'quality_verified':False,
            'lock_observational_busy':lock['busy']}
    (H/'final-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
