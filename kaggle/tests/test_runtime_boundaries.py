"""CPU runtime audit: 7 protection contracts + 3 OBSERVED_NOT_FIXED cases.
Heavy model/device/codec paths are explicit fixtures. Original methods are not edited.
"""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import struct
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

import test_reliability  # isolated mock runtime initialization, no CUDA/weights
import numpy as np
import worker
import clone_stream
from voice_binding import reference_binding, generation_bytes

OBSERVATIONS=[]


def last_stats(frames):
    return json.loads(next(row[5:] for row in reversed(frames) if row and row[0]==worker.F_STATS))


class RuntimeBoundaryTests(unittest.TestCase):
    def test_observed_unconsumed_response_queue_has_no_bound(self):
        captured=[];finished=threading.Event()
        original_queue=asyncio.Queue
        class RecordingQueue(original_queue):
            def __init__(self,*args,**kwargs):
                super().__init__(*args,**kwargs);captured.append(self)
        def produce(body,emit,cancel,t_req):
            for _ in range(512):emit(worker.frame(worker.F_PCM,b'\0\0'))
            emit(None);finished.set()
        async def experiment():
            request=NS(json=self._request_body)
            with patch.object(worker,'W',NS(run_job=produce)),patch.object(worker.asyncio,'Queue',RecordingQueue):
                response=await worker.synth(request)
                self.assertTrue(await asyncio.to_thread(finished.wait,3))
                await asyncio.sleep(0)
                observed={'maxsize':captured[0].maxsize,'queued_before_consumption':captured[0].qsize()}
                consumed=[row async for row in response.body_iterator]
                self.assertEqual(len(consumed),512)
                self.assertEqual(captured[0].qsize(),0)
                return observed
        observed=asyncio.run(experiment())
        self.assertEqual(observed,{'maxsize':0,'queued_before_consumption':513})
        OBSERVATIONS.append(dict(id='S18-G0-RUNTIME-F07',**observed,producer_frames=512,fixed=False,
                                 method='original async synth; bounded CPU producer fixture; no TCP/client memory pressure measurement'))

    @staticmethod
    async def _request_body():return {'profile':'synthetic','text':'fixture'}

    def test_observed_failed_reload_leaves_prompt_not_matching_accepted_pin(self):
        with tempfile.TemporaryDirectory(prefix='runtime-prompt-') as temporary:
            directory=Path(temporary);anchor=directory/'anchor.wav'
            first=b'SYNTHETIC REFERENCE A';second=b'SYNTHETIC REFERENCE B'
            anchor.write_bytes(first)
            profile={'id':'synthetic','anchor':'anchor.wav','ref_text':'fixture transcript','language':'Chinese'}
            first_pin=reference_binding(directory,profile)
            engine=worker.RealEngine(0);engine.sane=True
            resolved=[];used=[];change_during_resolution=[False]
            def resolve(**kwargs):
                digest=hashlib.sha256(anchor.read_bytes()).hexdigest();resolved.append(digest)
                if change_during_resolution[0]:anchor.write_bytes(first)
                return {'synthetic_reference_sha256':digest},[],True
            engine.model=NS(_voice_prompt_cache={},_resolve_voice_clone_prompt_from_reference=resolve)
            def stream(*args):
                used.append(engine._prompts['synthetic']['synthetic_reference_sha256'])
                yield np.full(4800,.05,np.float32)
            runtime=worker.Worker();runtime.engine=engine;runtime.ready=True
            frames=[]
            with patch.object(worker,'profile_dir',return_value=directory),patch.object(worker,'load_profile',return_value=profile),\
                 patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}),patch.object(runtime,'after_job'):
                runtime.load_profile('synthetic')
                anchor.write_bytes(second);change_during_resolution[0]=True
                with self.assertRaisesRegex(RuntimeError,'reference changed during prompt extraction'):
                    runtime.load_profile('synthetic')
                self.assertEqual(runtime.voice_bindings['synthetic'],first_pin)
                self.assertEqual(reference_binding(directory,profile),first_pin)
                with patch.object(engine,'stream',side_effect=stream):
                    runtime.run_job({'profile':'synthetic','text':'你好','voice_binding':first_pin,
                                     'voice_conditioning':'icl-generated-only-codec'},frames.append,threading.Event(),worker.now_ms())
            stats=last_stats(frames)
            self.assertNotIn('failed',stats)
            self.assertEqual(stats['voice_binding'],first_pin)
            self.assertEqual(len(resolved),2)  # next job did not rebuild the failed prompt
            self.assertEqual(used,[hashlib.sha256(second).hexdigest()])
            self.assertNotEqual(used[0],hashlib.sha256(anchor.read_bytes()).hexdigest())
            for leveler in runtime.levelers.values():leveler.close()
            OBSERVATIONS.append({'id':'S18-G0-RUNTIME-F08','failed_reload_rejected':True,
                'current_file_and_accepted_pin_match':True,'cached_prompt_matches_current_file':False,
                'resolver_calls_including_initial_and_failed_reload':len(resolved),'next_job_rebuilt_prompt':False,
                'next_job_failed':bool(stats.get('failed')),'fixed':False,
                'method':'original Worker + RealEngine.load_profile; synthetic resolver/prompt/stream, real file hashes; not acoustic proof'})

    def test_observed_conditioning_normalization_disagrees_with_reported_mode(self):
        engine=NS(name='faster-qwen3-tts')
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':' XVECTOR '}):
            text,xvector=clone_stream.conditioning({'ref_text':'fixture'})
            reported=worker.voice_conditioning(engine)
        self.assertEqual((text,xvector),('',True))
        self.assertEqual(reported,'icl-generated-only-codec')
        OBSERVATIONS.append({'id':'S18-G0-RUNTIME-F09','environment':' XVECTOR ',
            'actual_conditioning_helper_xvector':xvector,'reported_conditioning':reported,
            'fixed':False,'model_executed':False})

    def test_protect_response_iterator_close_signals_producer_cancellation(self):
        finished=threading.Event();captured=[]
        def produce(body,emit,cancel,t_req):
            captured.append(cancel);emit(worker.frame(worker.F_PCM,b'\0\0'))
            cancel.wait(3);finished.set()
        async def experiment():
            with patch.object(worker,'W',NS(run_job=produce)):
                response=await worker.synth(NS(json=self._request_body))
                try:
                    first=await asyncio.wait_for(anext(response.body_iterator),2)
                    self.assertEqual(first,worker.frame(worker.F_PCM,b'\0\0'))
                    await response.body_iterator.aclose()
                    self.assertTrue(captured[0].is_set())
                    self.assertTrue(await asyncio.to_thread(finished.wait,2))
                finally:
                    if captured:captured[0].set()
        asyncio.run(experiment())

    def test_protect_pin_mismatch_fails_before_silent_or_generated_pcm(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory=Path(temporary);(directory/'a.wav').write_bytes(b'synthetic')
            profile={'id':'synthetic','anchor':'a.wav','ref_text':'fixture'}
            runtime=worker.Worker();runtime.ready=True;frames=[]
            with patch.object(worker,'profile_dir',return_value=directory),patch.object(worker,'load_profile',return_value=profile),patch.object(runtime.engine,'stream') as stream:
                runtime.run_job({'profile':'synthetic','text':'fixture','voice_binding':'wrong','lead_pause_ms':500},frames.append,threading.Event(),worker.now_ms())
            stream.assert_not_called()
            self.assertFalse(any(row and row[0]==worker.F_PCM for row in frames))
            self.assertTrue(last_stats(frames)['failed']);self.assertFalse(runtime.busy)
            self.assertTrue(runtime.lock.acquire(blocking=False));runtime.lock.release()

    def test_protect_realengine_reload_evicts_same_path_cache_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            engine=worker.RealEngine(0);engine.sane=True
            directory=Path(temporary);anchor=str(directory/'a.wav')
            cache={(anchor,'old',False,False):'stale',('other.wav','old',False,False):'keep'}
            def resolve(**kwargs):
                self.assertNotIn((anchor,'old',False,False),cache)
                self.assertFalse(kwargs['xvec_only']);self.assertFalse(kwargs['append_silence'])
                return {'synthetic':True},[],True
            engine.model=NS(_voice_prompt_cache=cache,_resolve_voice_clone_prompt_from_reference=resolve)
            with patch.object(worker,'profile_dir',return_value=directory),patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}):
                info=engine.load_profile({'id':'synthetic','anchor':'a.wav','ref_text':'matching fixture'})
            self.assertEqual(len(cache),1);self.assertEqual(next(iter(cache))[0],'other.wav')
            self.assertFalse(info['reference_pcm_splicing'])

    def test_protect_binding_literal_and_strict_generation_contract(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory=Path(temporary);(directory/'a.wav').write_bytes(b'RIFF\x00\xffTEST')
            profile={'anchor':'a.wav','ref_text':'你好 café\x00声音','language':'Chinese'}
            pin=reference_binding(directory,profile)
            self.assertEqual(pin,'17f55c974517bf2cfa3cde3f0c3b207952acb89b174595fde9b25920c59625ab')
            self.assertNotEqual(pin,reference_binding(directory,dict(profile,gen={'temperature':.9})))
            for bad in ({'temperature':True},{'top_k':1.5},{'top_p':float('nan')}):
                with self.assertRaises(ValueError):generation_bytes({'gen':bad})
            (directory/'link.wav').symlink_to(directory/'a.wav')
            with self.assertRaises(OSError):reference_binding(directory,dict(profile,anchor='link.wav'))

    def test_protect_reference_breath_is_never_spliced_into_planner_pause(self):
        runtime=worker.Worker();runtime.breath_banks['synthetic']=[np.full(24000,.8,np.float32)]
        pause=runtime.lead_audio({'id':'synthetic'},500,True,42)
        self.assertEqual(len(pause),12000);self.assertTrue(np.all(pause==0))
        self.assertEqual(runtime.lead_audio({},9000,False,42).size,36000)

    def test_protect_invalid_clone_mode_rejected_instead_of_implicit_fallback(self):
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'unexpected'}):
            with self.assertRaisesRegex(ValueError,'icl or xvector'):clone_stream.conditioning({'ref_text':'fixture'})
        with patch.dict(os.environ,{'QTTS_CLONE_MODE':'icl'}):
            with self.assertRaisesRegex(ValueError,'transcript matching'):clone_stream.conditioning({})

    def test_protect_worker_frame_length_and_unicode_stats(self):
        raw=worker.jframe(worker.F_STATS,{'error':'合成fixture','failed':True})
        kind,length=struct.unpack('<BI',raw[:5])
        self.assertEqual(kind,worker.F_STATS);self.assertEqual(length,len(raw)-5)
        self.assertEqual(json.loads(raw[5:]),{'error':'合成fixture','failed':True})
