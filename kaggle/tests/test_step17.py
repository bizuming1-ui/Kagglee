"""Long-reference alignment/build tests. Synthetic ASR fixtures are NOT voice quality."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
import test_reliability
import analyst
from reference_segments import prepare_segments, split_words, context_seconds
from voice_binding import reference_binding, generation_bytes
import test_step15
from fastapi.testclient import TestClient


def transcript(seconds):
    words=[(.1+i*.4,.45+i*.4,f'第{i}词，') for i in range(int((seconds-.5)/.4))]
    return {'start':0.,'end':seconds,'text':''.join(w[2] for w in words),'words':words,'logprob':-.1}


class LongReferenceTests(unittest.TestCase):
    def test_28_7_and_60_seconds_word_segments_preserve_complete_text(self):
        for seconds in (28.7,60):
            source=transcript(seconds);audio=np.zeros(round(seconds*16000),np.float32)
            with self.subTest(seconds=seconds):
                lg,segs,r=prepare_segments(audio,[source],'zh',lambda *a:self.fail('unnecessary ASR'),16)
                self.assertEqual(''.join(s['text'] for s in segs),source['text'])
                self.assertGreater(len(segs),1);self.assertEqual(r['asr_windows'],0)
                self.assertTrue(all(0<=s['start']<s['end']<=seconds and s['end']-s['start']<=16 for s in segs))

    def test_twenty_minutes_timestamp_planning_without_truncating_transcript(self):
        source=transcript(1200);audio=np.zeros(1200*16000,np.float32)
        _,segs,r=prepare_segments(audio,[source],'zh',lambda *a:self.fail('ASR retry not needed'),24)
        self.assertEqual(''.join(s['text'] for s in segs),source['text'])
        self.assertGreater(len(segs),40);self.assertLess(len(segs),60)
        self.assertTrue(all(s['end']-s['start']<=24 for s in segs))

    def test_missing_word_times_retranscribes_actual_audio_windows(self):
        y=np.ones(round(28.7*16000),np.float32)*.03;seen=[]
        def asr(part,language):
            seen.append(part.copy());d=len(part)/16000
            return 'zh',[{'start':0.,'end':d,'text':f'窗口{len(seen)}的真实识别替身','words':[],'logprob':-.1}]
        _,out,r=prepare_segments(y,[{'start':0.,'end':28.7,'text':'不能按比例分的全文','words':[]}],'zh',asr)
        self.assertEqual(len(seen),2);self.assertEqual(sum(len(x) for x in seen),len(y))
        self.assertEqual([s['start'] for s in out],[0.,16.]);self.assertAlmostEqual(out[-1]['end'],28.7)
        self.assertNotIn('不能按比例分的全文',''.join(s['text'] for s in out));self.assertEqual(r['asr_windows'],2)

    def test_bad_words_or_mismatched_text_cannot_be_used_as_alignment(self):
        s=transcript(28.7)
        for bad in [dict(s,text='另外的全文'),dict(s,words=[(0,29,'全文')]),dict(s,words=[(float('nan'),1,'坏')]),dict(s,words=[(2,3,'x'),(1,2,'y')])]:
            self.assertIsNone(split_words(bad,16))

    def test_nonfinite_or_outside_segments_do_not_become_candidates(self):
        invalid=[{'start':0,'end':float('inf'),'text':'x'},{'start':-1,'end':2,'text':'x'},{'start':0,'end':5,'text':'x'}]
        _,out,r=prepare_segments(np.zeros(16000,np.float32),invalid,'zh',lambda *a:self.fail('bad segment ASR'))
        self.assertEqual(out,[]);self.assertEqual(r['invalid_segments'],3)

    def test_context_allowlist(self):
        for v in (16,'16',24,'24'):self.assertEqual(context_seconds(v),int(v))
        for v in (15,30,True,16.0,None,'0016','inf'):
            with self.assertRaises(ValueError):context_seconds(v)

    def test_screenshot_shape_long_recording_builds_without_shortening_whole_transcript(self):
        fixture=test_step15.BuildCostTests()
        with tempfile.TemporaryDirectory() as root:
            job=fixture.run_profile(root,duration=29,manual='',segments=[transcript(28.7)])
            self.assertEqual(job['state'],'done',job)
            p=json.loads((Path(root)/job['profile']/'profile.json').read_text())
            self.assertGreater(p['quality']['asr'][0]['alignment']['word_split_segments'],1)
            self.assertEqual(p['quality']['reference_context']['source_total_s'],29)
            self.assertTrue(all(v<=16 for v in p['quality']['reference_context']['candidate_durations_s']))

    def test_explicit24_second_matching_manual_anchor_is_not_cut_to16(self):
        fixture=test_step15.BuildCostTests();original=analyst.build_profile
        with tempfile.TemporaryDirectory() as root,patch.object(analyst,'build_profile',side_effect=lambda *a,**kw:original(*a,**kw,anchor_seconds=24)):
            job=fixture.run_profile(root,duration=24,manual='这是整段二十四秒录音的已知匹配文字')
            self.assertEqual(job['state'],'done',job)
            p=json.loads((Path(root)/job['profile']/'profile.json').read_text())
            self.assertEqual(p['quality']['reference_context']['anchor_limit_s'],24)
            self.assertEqual(p['quality']['reference_context']['candidate_durations_s'][0],24)
            self.assertEqual(p['ref_text'],'这是整段二十四秒录音的已知匹配文字')

    def test_low_input_warning_reaches_existing_profile_decision_display(self):
        original=np.sin
        with tempfile.TemporaryDirectory() as root,patch.object(np,'sin',side_effect=lambda x:original(x)*.01):
            job=test_step15.BuildCostTests().run_profile(root,duration=6)
            self.assertEqual(job['state'],'done',job)
            p=json.loads((Path(root)/job['profile']/'profile.json').read_text())
            f=p['quality']['files'][0]
            self.assertLess(f['source_rms_dbfs'],-40);self.assertTrue(f['warnings'])
            self.assertIn('输入电平很低',f['decision'])

    def test_invalid_context_form_is_rejected_before_background_build(self):
        with TestClient(analyst.app) as c:
            r=c.post('/profiles',data={'name':'test','anchor_seconds':'99'},files={'files':('a.wav',b'123')})
        self.assertEqual(r.status_code,400)


class GenerationBindingTests(unittest.TestCase):
    def test_effective_defaults_are_identical_and_each_parameter_is_bound(self):
        p={'anchor':'a.wav','ref_text':'你好','language':'Chinese'}
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'a.wav').write_bytes(b'wave')
            pin=reference_binding(root,p)
            self.assertEqual(pin,reference_binding(root,dict(p,gen={'temperature':.8,'top_k':50,'top_p':1.,'repetition_penalty':1.05})))
            for k,v in [('temperature',.65),('top_k',40),('top_p',.9),('repetition_penalty',1.1)]:
                self.assertNotEqual(pin,reference_binding(root,dict(p,gen={k:v})))

    def test_invalid_or_nonfinite_sampling_is_refused(self):
        for g in [{'temperature':float('nan')},{'top_p':float('inf')},{'top_k':1.5},{'temperature':True},{'top_k':'50'},{'top_p':0},{'repetition_penalty':-1}]:
            with self.assertRaises(ValueError):generation_bytes({'gen':g})


if __name__=='__main__':unittest.main()
