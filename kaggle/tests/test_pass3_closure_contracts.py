"""Read-only source/audit contracts. Not the 426-test CPU suite or legal/voice acceptance."""
import ast
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import unittest
from unittest.mock import patch
R=Path(__file__).resolve().parents[2];H=R/'docs/validation/step18'
def read(n):return json.loads((H/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def extracted(path,name,namespace):
    node=next(n for n in ast.parse((R/path).read_text()).body if isinstance(n,ast.FunctionDef) and n.name==name)
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),namespace)
    return namespace[name]
class ClosureContracts(unittest.TestCase):
    def test_01_three_pass_coverage_and_exact_delta(self):
        old=read('g0-pass3-frontend-coverage.json');new=read('g0-pass3-closure-coverage.json');before={r['path']:r for r in old['modules']};changed=[]
        self.assertEqual(len(new['modules']),53);self.assertEqual(new['cumulative_pass3_lines'],13668)
        self.assertTrue(new['all_source_three_semantic_reviews_complete']);self.assertEqual(new['remaining_assets_without_full_pass3'],0)
        for row in new['modules']:
            p=row['path'];self.assertEqual(sha(R/p),row['sha256']);self.assertEqual(len((R/p).read_text().splitlines()),row['lines'])
            self.assertEqual(row['pass1'],before[p]['pass1']);self.assertEqual(row['pass2'],before[p]['pass2'])
            for n in (1,2,3):self.assertTrue(row[f'pass{n}']['full_file_semantic_read'])
            if row['pass3']!=before[p]['pass3']:changed.append(row)
        self.assertEqual({r['path'] for r in changed},{'kaggle/source/LICENSE-QWEN-DERIVED.txt','kaggle/source/MEMO.md'})
        self.assertEqual(sum(r['lines'] for r in changed),421)
        self.assertEqual(sum(r['lines'] for r in new['modules']),13668)
    def test_02_branch_frozen_assets_and_formal_workbench(self):
        self.assertEqual(subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip(),'arena/1160bd87-kagglee')
        b=read('baseline.json');self.assertEqual(len(b['frozen_hashes']),94)
        for p,d in b['frozen_hashes'].items():self.assertEqual(sha(R/p),d,p)
        self.assertEqual(json.loads((R/'workspace/HEAD.json').read_text())['revision'],b['formal_revision'])
        self.assertEqual(len(list((R/'workspace/revisions'/b['formal_revision']).iterdir())),15)
        self.assertFalse((R/'kaggle/kaggle-fixed-step18.py').exists())
    def test_03_original_300_identity_preserved(self):
        old=read('g0-recommendation-disposition.json')['recommendations'];new=read('g0-pass3-closure-recommendation-gaps.json')['recommendations']
        original={r['id']:r for n in (1,2,3) for r in read(f'review{n}.json')['recommendations']}
        self.assertEqual(len(new),300);self.assertEqual(len({r['id'] for r in new}),300)
        for a,b in zip(old,new):
            for key,value in a.items():self.assertEqual(b[key],value,(a['id'],key))
            self.assertEqual(b['recommendation'],original[b['id']]['recommendation'])
    def test_04_classifications_and_partial_link_counts(self):
        d=read('g0-pass3-closure-recommendation-gaps.json');rows=d['recommendations']
        self.assertEqual(dict(Counter(r['disposition'] for r in rows)),d['counts']);self.assertEqual(d['counts'],read('g0-recommendation-disposition.json')['counts'])
        linked={r['id'] for r in rows if r['partial_third_pass_links']}
        self.assertEqual(linked,set(read('pass3-frontend-recommendation-links.json')['cumulative_unique_tentative_ids']))
        self.assertEqual(len(linked),45);self.assertEqual(sum(len(r['partial_third_pass_links']) for r in rows),53)
        self.assertEqual(d['rows_without_partial_third_pass_links'],255)
    def test_05_partial_link_provenance_exact(self):
        d=read('g0-pass3-closure-recommendation-gaps.json')
        for p,v in d['partial_link_files'].items():self.assertEqual(sha(R/p),v)
        for row in d['recommendations']:
            for link in row['partial_third_pass_links']:
                old=json.loads((R/link['path']).read_text())['rows'][link['row_index']]
                self.assertEqual(old['id'],row['id']);self.assertEqual(old['recommendation'],row['recommendation'])
                self.assertEqual(old['current_contract'],link['current_contract']);self.assertEqual(old['coverage_boundary'],link['coverage_boundary'])
                self.assertFalse(old['specific_row_test_signoff']);self.assertFalse(old['final_disposition_signed_off'])
    def test_06_next_actions_and_no_automatic_signoff(self):
        d=read('g0-pass3-closure-recommendation-gaps.json')
        self.assertEqual(d['unclosed_rows'],300);self.assertFalse(d['g0_complete'])
        for row in d['recommendations']:
            self.assertEqual(row['next_action']['required_review'],row['recommendation'])
            self.assertEqual(row['next_action']['required_contract'],row['planned_test_contract'])
            for k in ('specific_row_test_signoff','product_fix_implemented','final_disposition_signed_off','row_evidence_revalidated_as_functional_this_batch'):self.assertFalse(row[k])
        self.assertTrue(all(not v for v in read('g0-pass3-closure-boundaries.json')['gate'].values()))
    def test_07_license_text_and_legal_boundary(self):
        text=(R/'kaggle/source/LICENSE-QWEN-DERIVED.txt').read_text();d=read('g0-pass3-closure-boundaries.json')['license']
        for token in ('Version 2.0, January 2004','3. Grant of Patent License.','4. Redistribution.','6. Trademarks.','7. Disclaimer of Warranty.','Copyright 2026 Alibaba Cloud','NOTICE'):self.assertIn(token,text)
        self.assertEqual(len(text.splitlines()),201);self.assertFalse(d['legal_release_signed_off']);self.assertFalse(d['all_dependencies_weights_voice_consent_verified'])
        self.assertTrue(d['absence_in_inventory_does_not_prove_no_upstream_NOTICE_obligation']);self.assertEqual(len(d['conditions_to_check']),10)
    def test_08_memo_drift_actual_conditioning_ast(self):
        fn=extracted('kaggle/source/py/clone_stream.py','conditioning',{'os':os})
        with patch.dict(os.environ,{},clear=True):self.assertEqual(fn({'ref_text':'verified text'}),('verified text',False))
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'xvector'},clear=True):self.assertEqual(fn({'ref_text':'unused'}),('',True))
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'invalid'},clear=True):
            with self.assertRaises(ValueError):fn({'ref_text':'text'})
        self.assertIn('xvec_only=True',(R/'kaggle/source/MEMO.md').read_text());self.assertEqual(read('g0-pass3-closure-boundaries.json')['memo']['existing_observation'],'D01')
    def test_09_memo_drift_actual_gain_ast(self):
        fn=extracted('kaggle/source/py/worker.py','output_max_gain_db',{'os':os,'math':math})
        for env,expected in (({},6.),({'QTTS_MAX_GAIN_DB':'12'},12.),({'QTTS_MAX_GAIN_DB':'13'},6.),({'QTTS_MAX_GAIN_DB':'nan'},6.)):
            with patch.dict(os.environ,env,clear=True):self.assertEqual(fn(),expected)
        self.assertIn('最大增益12dB',(R/'kaggle/source/MEMO.md').read_text())
    def test_10_history_absence_reported_not_fabricated(self):
        hashes=read('pass3-closure-preserved.json');availability=read('pass3-closure-history-availability.json');missing=[];available=0
        for p,v in hashes.items():
            if (R/p).is_file():self.assertEqual(sha(R/p),v,p);available+=1
            else:missing.append(p)
        self.assertEqual(len(hashes),1139);self.assertEqual(available,1136);self.assertEqual(sorted(missing),sorted(availability['missing']));self.assertEqual(len(missing),3)
        self.assertTrue(all(p.endswith('.log') for p in missing));self.assertFalse(availability['full_history_integrity_passed']);self.assertFalse(availability['missing_history_reconstructed'])
        self.assertEqual(availability['missing_expected_sha256'],{p:hashes[p] for p in missing})
    def test_11_prior_browser_raw_receipts_not_new_execution(self):
        for n in (1,2,3):
            receipt=read(f'pass3-frontend-audit-round{n}.json');p=R/receipt['browser_report'];self.assertEqual(sha(p),receipt['browser_report_sha256']);data=json.loads(p.read_text());tests=[]
            def walk(s):
                for spec in s.get('specs',[]):tests.extend(spec.get('tests',[]))
                for child in s.get('suites',[]):walk(child)
            for suite in data['suites']:walk(suite)
            self.assertEqual(len(tests),158);self.assertEqual(data['stats']['expected'],158)
            self.assertTrue(all(t['status']=='expected' and len(t['results'])==1 and t['results'][0]['status']=='passed' for t in tests))
        self.assertFalse(read('pass3-closure-environment.json')['browser_cpu426_go_model_rerun_this_batch'])
    def test_12_saved_decisions_and_50_actions_each(self):
        text=(R/'docs/KAGGLE_STEP18_DECISIONS.md').read_text();self.assertEqual(sha(R/'docs/KAGGLE_STEP18_DECISIONS.md'),read('g0-decisions-preserved.json')['sha256'])
        heads=list(re.finditer(r'^## 问题(\d+)：',text,re.M));self.assertEqual([m.group(1) for m in heads],['25','26','27'])
        for i,m in enumerate(heads):
            part=text[m.end():heads[i+1].start() if i+1<len(heads) else len(text)];start=re.search(r'^### .*50项实施建议$',part,re.M);self.assertIsNotNone(start)
            self.assertEqual(re.findall(r'^(\d+)\. ',part[start.end():].split('\n### ',1)[0],re.M),[str(j) for j in range(1,51)])
if __name__=='__main__':unittest.main(verbosity=2)
