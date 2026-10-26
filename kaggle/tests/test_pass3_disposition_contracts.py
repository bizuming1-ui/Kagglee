"""Review-provenance checks, not new execution of the historical failure witnesses."""
import hashlib
import json
from pathlib import Path
import re
import unittest
R=Path(__file__).resolve().parents[2];H=R/'docs/validation/step18'
def read(n):return json.loads((H/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pointer(d,p):
    for part in p.strip('/').split('/'):
        part=part.replace('~1','/').replace('~0','~');d=d[int(part)] if isinstance(d,list) else d[part]
    return d
class DispositionContracts(unittest.TestCase):
    def test_01_exact_300_original_identity(self):
        old={r['id']:r for r in read('g0-pass3-closure-recommendation-gaps.json')['recommendations']};new=read('g0-disposition-review.json')['rows']
        self.assertEqual(len(new),300);self.assertEqual({r['id'] for r in new},set(old))
        for r in new:
            a=old[r['id']]
            for field in ('recommendation','source','work_package'):self.assertEqual(r[field],a[field])
            self.assertEqual(r['initial_disposition'],a['disposition']);self.assertEqual(r['test_contract'],a['planned_test_contract'])
    def test_02_three_review_notes_exactly_100_each(self):
        d=read('g0-disposition-review.json');notes={}
        for n in (1,2,3):
            p=H/f'disposition-review{n}.tsv';self.assertEqual(sha(p),d['note_files'][str(p.relative_to(R))]);lines=p.read_text().splitlines()
            self.assertEqual(len(lines),100)
            for i,line in enumerate(lines,1):
                index,note=line.split('\t');self.assertEqual(index,f'{i:03d}');self.assertGreater(len(note),12);notes[f'S18-R{n}-{index}']=note
        for row in d['rows']:self.assertEqual(row['review_note'],notes[row['id']])
        self.assertEqual(len(set(notes.values())),300)
    def test_03_review_routes_not_new_bug_counts(self):
        d=read('g0-disposition-review.json');counts={'repair-in-stated-scope':23,'retain-invariant':96,'implement-contract-or-documentation':89,'defer-until-real-evidence':55,'investigate-before-design':37}
        self.assertEqual(d['action_counts'],counts);self.assertEqual(d['review_dispositions_recorded'],300)
        self.assertTrue(all(r['review_disposition_recorded'] for r in d['rows']))
        self.assertFalse(d['original_300_modified']);self.assertFalse(d['g0_complete'])
    def test_04_partial_links_and_failure_union(self):
        d=read('g0-disposition-review.json');linked={r['id'] for r in d['rows'] if r['partial_third_pass_links']};bound={r['id'] for r in d['rows'] if r['failure_observation_binding']}
        self.assertEqual(len(linked),45);self.assertEqual(len(bound),23);self.assertEqual(len(linked|bound),65)
        self.assertEqual(d['union_rows_with_either_limited_reference'],65);self.assertEqual(d['rows_without_either_limited_reference'],235)
        self.assertEqual(linked&bound,{'S18-R1-016','S18-R2-031','S18-R2-032'})
    def test_05_23_explicit_failure_row_bindings(self):
        old={r['id'] for r in read('g0-recommendation-disposition.json')['recommendations'] if r['disposition']=='confirmed-defect-in-stated-scope'}
        d=read('disposition-failure-bindings.json');self.assertEqual({r['recommendation_id'] for r in d['rows']},old);self.assertEqual(len(d['rows']),23)
        self.assertEqual(d['historical_round_bindings'],69)
        for r in d['rows']:
            self.assertFalse(r['fresh_execution']);self.assertFalse(r['complete_recommendation_test_signoff']);self.assertFalse(r['product_fixed']);self.assertTrue(r['boundary'])
    def test_06_resolve_every_pointer_and_hash(self):
        for row in read('disposition-failure-bindings.json')['rows']:
            self.assertEqual([r['round'] for r in row['historical_observations']],[1,2,3])
            for ref in row['historical_observations']:
                p=R/ref['path'];self.assertEqual(sha(p),ref['sha256']);raw=json.loads(p.read_text());self.assertEqual(raw['round'],ref['round'])
                self.assertEqual(sha(R/ref['source']),ref['source_sha256']);self.assertEqual(sha(R/ref['current_related_probe']),ref['current_related_probe_sha256'])
                if row['family']=='dsp':self.assertIsNone(ref['probe_identity_matches_recorded_sha']);self.assertNotIn('probe_sha256',raw)
                else:self.assertTrue(ref['probe_identity_matches_recorded_sha']);self.assertEqual(raw['probe_sha256'],ref['current_related_probe_sha256'])
                for part in ref['pointers']:self.assertEqual(pointer(raw,part['pointer']),part['observed_fragment'])
    def test_07_payload_witness_limits(self):
        for n in (1,2,3):
            d=read(f'reference-state-baseline-round{n}.json')['candidate_payload_cases']
            self.assertIs(d[0]['input'],True);self.assertEqual(d[0]['selected'],1)
            self.assertIs(d[1]['input'],False);self.assertEqual(d[1]['selected'],0)
            self.assertEqual(d[2]['input'],1.9);self.assertEqual(d[2]['selected'],1)
            for i in (4,5,6):self.assertEqual(d[i]['uncaught_exception_type'],'TypeError')
        row=next(r for r in read('disposition-failure-bindings.json')['rows'] if r['recommendation_id']=='S18-R2-024');self.assertIn('NaN is not present',row['boundary'])
    def test_08_calibration_and_diagnostic_observed_facts(self):
        for n in (1,2,3):
            d=read(f'reference-state-baseline-round{n}.json');a,b,c,e=d['calibration_cases']
            self.assertTrue(a['missing_asr_reported_as_cer_0_05']);self.assertEqual(b['final_ref_text'],'new-unassessed-text');self.assertTrue(b['stale_candidate_assessment_reproduced'])
            self.assertTrue(c['function_returned_normally']);self.assertTrue(all(not r['ok'] for r in c['reload_receipts']))
            self.assertEqual(e['calibration']['chosen'],0);self.assertTrue(all('error' in r for r in e['calibration']['results']))
            self.assertEqual([r['seed'] for r in d['consistency_case']['calls']],[100,101]);self.assertFalse(d['full_model_executed'])
    def test_09_dsp_observations_not_acoustic_proof(self):
        for n in (1,2,3):
            d=read(f'dsp-partition-baseline-round{n}.json');self.assertEqual(d['cases'][0]['max_abs_i16_difference'],1424);self.assertEqual(d['cases'][10]['max_abs_i16_difference'],8)
            self.assertTrue(d['partition_dependence_reproduced']);self.assertFalse(d['voice_quality_verified']);self.assertFalse(d['user_hiss_root_cause_proven'])
    def test_10_short_tail_and_trimmer_boundaries(self):
        for n in (1,2,3):
            d=read(f'pass3-frontend-latency_contract_probe-round{n}.json')['cases']
            for i in (2,3,8,9):self.assertTrue(d[i]['stranded_finished_tail']);self.assertFalse(d[i]['play_command'])
            self.assertEqual(d[3]['buffer_ms'],50);self.assertEqual(d[4]['buffer_ms'],51);self.assertTrue(d[4]['play_command'])
            t=read(f'trimmer-boundary-round{n}.json');self.assertEqual(t['cases'][0]['output_samples'],0);self.assertEqual(t['cases'][5]['kept_context_difference_samples'],840);self.assertEqual(t['cases'][6]['held_nonzero_samples'],60);self.assertFalse(t['real_phoneme_loss_proven'])
    def test_11_no_automatic_final_or_functional_signoff(self):
        d=read('g0-disposition-review.json');self.assertEqual(d['rows_functionally_accepted'],0);self.assertEqual(d['rows_finally_signed_off'],0)
        for r in d['rows']:
            for k in ('specific_row_test_signoff','final_disposition_signed_off','product_fix_implemented','functional_acceptance'):self.assertFalse(r[k])
        note=next(r['review_note'] for r in d['rows'] if r['id']=='S18-R1-041');self.assertIn('2..8',note)
        self.assertRegex((R/'kaggle/source/go/gateway/session.go').read_text(),r'n >= 2 && n <= 8')
    def test_12_d02_not_recovered_by_renaming_new_runs(self):
        d=read('disposition-history-recovery.json');self.assertFalse(d['history_gap_resolved']);self.assertFalse(d['old_content_reconstructed']);self.assertFalse(d['full_historical_integrity_passed'])
        self.assertEqual(d['same_hash_candidates'],[]);self.assertEqual(d['restored_files'],[])
        self.assertEqual(d['expected_missing_hashes'],read('pass3-closure-history-availability.json')['missing_expected_sha256'])
        for r in d['git_history_queries']:self.assertEqual(r['available_commit_ids'],[]);self.assertFalse((R/r['path']).exists())
if __name__=='__main__':unittest.main(verbosity=2)
