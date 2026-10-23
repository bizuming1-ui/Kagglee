#!/usr/bin/env python3
"""Read-only release/evidence verification; does NOT run a model or trainer.

Requires the existing Node workbench on port 3000. Run from this checkout.
Only the two JSON receipts in this evidence directory are rewritten.
"""
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

REPO=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sha=lambda raw:hashlib.sha256(raw).hexdigest()
read=lambda name:(HERE/name).read_text()


def main():
    assert subprocess.check_output(['git','branch','--show-current'],cwd=REPO,text=True).strip()=='arena/041344f2-kagglee'
    artifact=REPO/'kaggle/kaggle-fixed-step9.py';raw=artifact.read_bytes()
    expected='8ec892dcc5ca10daf20c8de84dd2be08d9a3de8807872c2051ddf52bd5882a9b'
    assert len(raw)==233074 and sha(raw)==expected
    manifest=json.loads((REPO/'kaggle/source_manifest_step9.json').read_text())
    assert manifest['launcher_sha256']==expected and manifest['asset_count']==37
    tree=ast.parse(raw)
    value=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets))
    files=ast.literal_eval(value);assert len(files)==37
    for record in manifest['assets']:
        name=record['path'];decoded=zlib.decompress(base64.b64decode(files[name][1],validate=True))
        assert decoded==(REPO/'kaggle/source'/name).read_bytes()
        assert sha(decoded)==record['sha256']==files[name][0] and len(decoded)==record['bytes']
    frozen=['02e9bb45a14f1e168badc8f897cead0ddd7e70c884d7fd26382c9a5b49778007',
            'a628d1bf3f320a330d9206b5f1864e4b38a04f0bc04b26028af2e94368f111d0',
            '4b69f9adec43487c731c53e7ae65f91534626e71660f1b50b109bfe0c8cb973b',
            '069421e5f0d4112148211e1289f91ec7a1b184105e5431fde0c3d72e8c744e27',
            'acfa5639324e16aa7dcfe314caef09bee8eb277d59bdd71a5f1f4cffa0a7aaf1',
            '781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256',
            '3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0',
            '777c1d523559c9c734cd5e99841810524284e91269ced23963e8e5ab3f3cc1e1']
    for i,expected_frozen in enumerate(frozen,1):assert sha((REPO/f'kaggle/kaggle-fixed-step{i}.py').read_bytes())==expected_frozen
    head=json.loads((REPO/'workspace/HEAD.json').read_text())
    assert sha((REPO/'workspace/revisions'/head['revision']/'kaggle').read_bytes())=='26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461'
    handoff=(REPO/'docs/KAGGLE_HANDOFF_PROMPT.md').read_text()
    memo_names=re.findall(r'^## 内嵌备忘录：(\S+)$',handoff,re.M)
    assert len(memo_names)==21 and len(set(memo_names))==21
    for name in memo_names:
        match=re.search(r'^## 内嵌备忘录：'+re.escape(name)+r'\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',handoff,re.M|re.S)
        assert match and match.group(1).strip()==(REPO/'docs'/name).read_text().strip(),name
    blocks=re.split(r'^## 问题\d+：',(REPO/'docs/KAGGLE_DECISIONS.md').read_text(),flags=re.M)[1:]
    assert len(blocks)==8 and all(len(re.findall(r'^\d+\. ',block,re.M))==50 for block in blocks)
    rows=re.findall(r'^- \[([ x])\] R[123]-\d{3}：',(REPO/'docs/KAGGLE_REVIEW_CHECKLIST.md').read_text(),re.M)
    assert len(rows)==300 and rows.count('x')==22
    review=json.loads(read('review-map.json'));assert [len(g['items']) for g in review['rounds']]==[100,100,100]
    assert sum(row['checked_preserved'] for g in review['rounds'] for row in g['items'])==22
    for i in range(1,4):
        text=read(f'python-round{i}.txt');assert 'Ran 201 tests' in text and text.rstrip().endswith('OK')
        text=read(f'node-round{i}.txt');assert '# pass 30' in text and '# fail 0' in text
    assert '327 passed (10.3m)' in read('browser-repeat3.txt')
    assert '3 passed (9.2s)' in read('final-copy-repeat3.txt')
    assert len(re.findall(r'^=== RUN   TestPreflightReportIsAuthenticatedBoundedAndReadOnly$',read('go-race3.txt'),re.M))==3
    assert '\nPASS\nok' in read('go-race3.txt')
    for name,key in [('ownership-process3.txt','real_supervisor_fd_lifecycle_passed'),('training-http3.txt','passed'),('training-http3.txt','training_input_http_passed'),('codes-cli3.txt','local_cli_storage_passed'),('mock-pipeline3.txt','passed')]:
        records=[json.loads(line) for line in read(name).splitlines() if line.startswith('{')]
        records=[row for row in records if key in row]
        assert len(records)==3 and {row['round'] for row in records}=={1,2,3} and all(row[key] for row in records),name
    runtime=json.loads(read('runtime-probe.json'))
    assert runtime['status']=='blocked' and all(runtime[k] is False for k in ('model_loaded','inference_verified','training_verified','performance_verified'))
    assert 'found 0 vulnerabilities' in read('npm-audit.txt')
    old=json.loads((REPO/'docs/validation/step8/formal-api-readonly.json').read_text())
    with urlopen('http://127.0.0.1:3000/api/project',timeout=5) as response:current=json.load(response)
    hashes={name:sha(value.encode()) for name,value in current['files'].items()}
    assert current['revision']==old['revision']==head['revision'] and hashes==old['hashes']
    total=sum(len(value.encode()) for value in current['files'].values());assert total==1043155 and len(hashes)==15
    for name,hashed in hashes.items():assert sha((REPO/'workspace/revisions'/head['revision']/name).read_bytes())==hashed
    formal={**old,'all15HashesMatchStage8Receipt':True,'hashes':hashes}
    (HERE/'formal-api-readonly.json').write_text(json.dumps(formal,ensure_ascii=False,indent=2)+'\n')
    sys.path.insert(0,str(REPO/'kaggle/source/py'))
    from gpu_ownership import status
    resource=status()
    assert resource['busy'] is False # Observation only, NOT hardware measurement or reservation.
    results={'artifact_bytes':len(raw),'artifact_sha256':sha(raw),'assets':37,'frozen_1_through_8_hashes_match':True,
             'original_hash_matches':True,'complete_embedded_memos':21,'professional_questions':8,'suggestions':400,
             'checklist_checked':22,'checklist_total':300,'python':{'unique':201,'rounds':3,'passed':603},
             'browser':{'unique':109,'rounds':3,'passed':327},'copy_special_passed':3,
             'ownership_process_rounds':3,'ownership_process_models':'CPU stand-ins, not real GPU models',
             'formal_all15_hashes_and_head_unchanged':True,'protocol_lock_busy_at_finish':resource['busy'],
             'gpu_verified':False,'training_verified':False}
    (HERE/'final-checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(results,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
