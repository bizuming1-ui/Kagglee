"""Pass2 DSP/tools: 10 protections + 2 OBSERVED_NOT_FIXED witnesses.
Actual NumPy/files/local HTTP. Rust ABI, GPU health, clocks, install/model roles
are explicit fixtures. No Rust binary, model, GPU, training or acoustic signoff.
"""
from contextlib import contextmanager,ExitStack,redirect_stdout
import ctypes
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import io
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import Mock,patch
import wave
import numpy as np
import test_reliability
import audio_rt
import qtts_common as common
from resource_limits import UploadRejected
from test_tool_boundaries import load,encoded,worker_frame

OBSERVATIONS=[]

@contextmanager
def bench_fixture(root,*,wrong_gpu=False):
    """Original benchmark run/measure; hardware declarations and time are fixtures."""
    module=load('voice_benchmark');profiles=root/'state/profiles';directory=profiles/'voice';directory.mkdir(parents=True)
    profile={'id':'voice','anchor':'anchor.wav','ref_text':'fixture reference','language':'Chinese','gen':{}}
    (directory/'profile.json').write_text(json.dumps(profile))
    with wave.open(str(directory/'anchor.wav'),'wb') as wav:
        wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(24000);wav.writeframes(bytes(38400*2))
    pin=module.reference_binding(directory,profile)
    tone=(np.sin(2*np.pi*220*np.arange(24000)/24000)*1000).astype('<i2').tobytes()+bytes(192*2)
    requests=[];servers=[];threads=[]
    def handler(index):
        class Handler(BaseHTTPRequestHandler):
            def log_message(self,*_):pass
            def send(self,raw):
                self.send_response(200);self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
            def do_GET(self):
                requests.append((index,self.path,None))
                self.send(encoded({'ready':True,'busy':False,'model_loaded':True,'engine':'faster-qwen3-tts',
                    'voice_conditioning':'icl-generated-only-codec','gpu':index,'cuda_visible_devices':str(index),'dtype':'fp16'}))
            def do_POST(self):
                body=json.loads(self.rfile.read(int(self.headers['Content-Length'])));requests.append((index,self.path,body))
                if self.path=='/profile/load':self.send(encoded({'ok':True,'voice_binding':pin}));return
                stats={'engine':'faster-qwen3-tts','voice_binding':pin,'speech_samples':24000,
                       'gen_ms':10.,'rtf':.01,'gpu':0 if wrong_gpu else index,'anomalies':[]}
                self.send(worker_frame(1,tone)+worker_frame(2,encoded(stats)))
        return Handler
    try:
        for index in range(2):
            server=ThreadingHTTPServer(('127.0.0.1',0),handler(index));servers.append(server)
            thread=threading.Thread(target=lambda s=server:s.serve_forever(poll_interval=.01));threads.append(thread);thread.start()
        args=NS(run=True,profile='voice',rounds=3,chunk_size=8,output=str(root/'experiment/report.json'))
        counter=itertools.count()
        with patch.object(common,'PROFILES_DIR',profiles),patch.object(module,'WORKER_PORTS',[s.server_port for s in servers]),patch.object(module,'time',NS(perf_counter=lambda:next(counter)*.001)):
            yield module,args,pin,tone,requests
    finally:
        for server in servers:server.shutdown()
        for thread in threads:thread.join(3)
        for server in servers:server.server_close()
        assert all(not thread.is_alive() for thread in threads),'owned HTTP fixture outlived context'


class DSPToolBoundaries(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)

    def test_protect_nonfinite_sanitization_matches_zero_replacement_without_mutation(self):
        dirty=np.tile([np.nan,np.inf,-np.inf,.02,-.03],200).astype(np.float32);original=dirty.copy()
        clean=np.nan_to_num(dirty,nan=0.,posinf=0.,neginf=0.)
        with patch.object(audio_rt,'_LIB',None):
            a,b=audio_rt.Leveler(24000),audio_rt.Leveler(24000)
            try:
                a.start_segment();b.start_segment()
                np.testing.assert_array_equal(a.process(dirty),b.process(clean))
                self.assertEqual((a.gain_db,a.env_dbfs),(b.gain_db,b.env_dbfs))
                np.testing.assert_array_equal(dirty,original)
            finally:a.close();b.close()

    def test_protect_dc_only_processing_retains_state_across_calls_before_flush(self):
        samples=np.linspace(-.2,.2,1703,dtype=np.float32)
        with patch.object(audio_rt,'_LIB',None):
            a,b=audio_rt.Leveler(24000,max_gain_db=0,min_gain_db=0),audio_rt.Leveler(24000,max_gain_db=0,min_gain_db=0)
            try:
                full=a.process(samples);parts=np.concatenate([b.process(samples[:17]),b.process(samples[17:453]),b.process(samples[453:])])
                np.testing.assert_array_equal(parts,full)
            finally:a.close();b.close()
        # No start_segment fade or adaptive gain; NOT general partition invariance.

    def test_protect_subgate_signal_does_not_learn_speech_or_change_gain(self):
        with patch.object(audio_rt,'_LIB',None):
            leveler=audio_rt.Leveler(24000,-21,6,-9)
            try:
                before=leveler.env_dbfs;out=leveler.process(np.full(2400,.0001,np.float32))
                self.assertEqual(leveler._seen,0);self.assertEqual(leveler.env_dbfs,before);self.assertEqual(leveler.gain_db,0.)
                self.assertEqual(out.size,2400)
            finally:leveler.close()

    def test_protect_no_rust_flag_avoids_all_library_loading(self):
        with patch.dict(os.environ,{'QTTS_NO_RUST':'1'}),patch.object(audio_rt.ctypes,'CDLL') as load_library:
            self.assertIsNone(audio_rt._load());load_library.assert_not_called()

    def test_protect_loader_skips_legacy_abi_and_sets_reviewed_ctypes_signatures(self):
        paths=[self.root/'old.so',self.root/'v3.so']
        for path in paths:path.touch()
        names=('rt_version','rt_leveler_new','rt_leveler_free','rt_leveler_start_segment','rt_leveler_process',
               'rt_leveler_flush','rt_leveler_gain_db','rt_leveler_env_dbfs','rt_breath_synth','rt_rms_dbfs','rt_peak')
        good=NS(**{name:Mock(return_value=3) for name in names});old=NS(rt_version=Mock(return_value=2))
        with patch.dict(os.environ,{'QTTS_NO_RUST':'0'}),patch.object(audio_rt,'_candidates',return_value=iter(paths)),patch.object(audio_rt.ctypes,'CDLL',side_effect=[old,good]) as cdll:
            self.assertIs(audio_rt._load(),good);self.assertEqual(cdll.call_count,2)
        self.assertIs(good.rt_leveler_process.restype,ctypes.c_int32)
        self.assertEqual(good.rt_leveler_process.argtypes,[ctypes.c_void_p,ctypes.c_void_p,ctypes.c_size_t,ctypes.c_void_p])
        self.assertEqual(good.rt_leveler_new.argtypes,[ctypes.c_uint32,ctypes.c_float,ctypes.c_float,ctypes.c_float])
        # Symbol objects are fixtures: no dlopen or Rust execution occurred.

    def test_protect_benchmark_request_equivalence_and_private_generated_artifacts(self):
        with bench_fixture(self.root) as (module,args,pin,tone,received):report=module.run(args)
        self.assertEqual(report['status'],'measured-speed-only') # synthetic metrics, NOT achieved RTF
        self.assertFalse(report['voice_quality_verified']);self.assertFalse(report['all_user_requirements_completed'])
        rows=report['measurements'];self.assertEqual(len(rows),18);self.assertEqual(len(report['prompt_warmup']),2)
        synth=[(i,b) for i,path,b in received if path=='/synth'];self.assertEqual(len(synth),18)
        left=[b for i,b in synth if i==0];right=[b for i,b in synth if i==1];self.assertEqual(left,right)
        for body in left:
            self.assertEqual((body['seed'],body['voice_binding'],body['lead_pause_ms'],body['tail_pause_ms'],body['breath']),(17,pin,0,0,False))
        ledger=self.root/'experiment/measurements.jsonl';self.assertEqual(ledger.stat().st_mode&0o777,0o600)
        self.assertEqual(len(ledger.read_text().splitlines()),18)
        for row in rows:
            path=self.root/'experiment'/row['wav'];self.assertEqual(path.stat().st_mode&0o777,0o600)
            with wave.open(str(path),'rb') as wav:
                self.assertEqual((wav.getframerate(),wav.getnchannels(),wav.getsampwidth(),wav.getnframes()),(24000,1,2,24192))
                self.assertEqual(wav.readframes(24192),tone)
        self.assertTrue(all(r['separate_from_hot_rtf'] for r in report['prompt_warmup']))

    def test_protect_incomplete_benchmark_keeps_slow_row_private_wav_and_ledger(self):
        with bench_fixture(self.root) as (module,args,pin,tone,_):
            row={'worker_rtf':.8,'wall_rtf':.9,'speech_samples':24000,'speech_seconds':1.,'wall_seconds':.9,'voice_binding':pin,'gpu':0}
            argv=['voice_benchmark.py','--run','--profile','voice','--output',args.output]
            with patch.object(sys,'argv',argv),patch.object(module,'measure',side_effect=[(tone,row),RuntimeError('private failure marker')]),redirect_stdout(io.StringIO()):
                self.assertEqual(module.main(),2)
        report=json.loads(Path(args.output).read_text());self.assertEqual(report['status'],'blocked')
        self.assertNotIn('private failure marker',json.dumps(report));self.assertFalse(report['voice_quality_verified'])
        ledger=Path(args.output).parent/'measurements.jsonl';rows=[json.loads(line) for line in ledger.read_text().splitlines()]
        self.assertEqual(len(rows),1);self.assertFalse(rows[0]['target_passed'])
        self.assertEqual(len(list(Path(args.output).parent.glob('*.wav'))),1)
        for path in Path(args.output).parent.iterdir():self.assertEqual(path.stat().st_mode&0o777,0o600)

    def test_protect_encoder_controller_scrubs_credentials_offline_cpu_env_and_restores_handler(self):
        module=load('encode_training');captured=[];previous=signal.getsignal(signal.SIGTERM)
        def spawn(cmd,**kwargs):
            captured.append((cmd,kwargs));Path(cmd[cmd.index('--_report')+1]).write_text(encoded({'status':'ok','result':{'model_loaded':False}}).decode())
            return NS(wait=lambda timeout:0,poll=lambda:0)
        names=('QTTS_GPU_LEASE_FD','QTTS_GPU_LEASE_NONCE','QTTS_ACCESS_TOKEN','DEEPSEEK_API_KEY','HF_TOKEN','HUGGING_FACE_HUB_TOKEN','KAGGLE_USERNAME','KAGGLE_KEY')
        with patch.dict(os.environ,{name:'synthetic-secret' for name in names}),patch.object(module.subprocess,'Popen',side_effect=spawn),redirect_stdout(io.StringIO()) as out:
            self.assertEqual(module.main(['fingerprint','--model-dir',str(self.root)]),0)
        self.assertIs(signal.getsignal(signal.SIGTERM),previous);env=captured[0][1]['env']
        self.assertTrue(all(name not in env for name in names));self.assertEqual(env['CUDA_VISIBLE_DEVICES'],'')
        for key in ('HF_HUB_OFFLINE','TRANSFORMERS_OFFLINE'):self.assertEqual(env[key],'1')
        for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):self.assertEqual(env[key],'2')
        self.assertTrue(captured[0][1]['start_new_session']);self.assertNotIn('synthetic-secret',out.getvalue())

    def test_protect_encoder_missing_or_oversize_receipt_blocks_before_printing_contents(self):
        module=load('encode_training');previous=signal.getsignal(signal.SIGTERM)
        for oversize in (False,True):
            def spawn(cmd,**kwargs):
                if oversize:Path(cmd[cmd.index('--_report')+1]).write_bytes(b'x'*((1<<20)+1))
                return NS(wait=lambda timeout:0,poll=lambda:0)
            with self.subTest(oversize=oversize),patch.object(module.subprocess,'Popen',side_effect=spawn),redirect_stdout(io.StringIO()) as out:
                self.assertEqual(module.main(['fingerprint','--model-dir',str(self.root)]),2)
            self.assertEqual(json.loads(out.getvalue())['status'],'failed');self.assertLess(len(out.getvalue()),200)
            self.assertIs(signal.getsignal(signal.SIGTERM),previous)

    def test_protect_trained_voice_cli_redacts_unexpected_error_and_preserves_blocked_status(self):
        module=load('trained_voice')
        for error,expected,code in ((RuntimeError('private exception marker'),'rejected',409),(UploadRejected('local admission blocked',503),'blocked',503)):
            with self.subTest(status=expected),patch('trained_profiles.TrainedArtifacts',side_effect=error),redirect_stdout(io.StringIO()) as out:
                self.assertEqual(module.main(['describe','--state',str(self.root),'--run-id','fixture']),2)
            receipt=json.loads(out.getvalue());self.assertEqual((receipt['status'],receipt['code']),(expected,code))
            self.assertNotIn('private exception marker',out.getvalue())

    def test_observed_numpy_flush_leaves_dc_memory_for_next_process_call(self):
        with patch.object(audio_rt,'_LIB',None):
            leveler=audio_rt.Leveler(24000,-21,0,0);fresh=audio_rt.Leveler(24000,-21,0,0)
            try:
                leveler.process(np.full(480,.2,np.float32));tail=leveler.flush(192)
                self.assertEqual(int(tail[-1]),0);self.assertEqual(leveler._last,0.)
                self.assertNotEqual(leveler._prev_x,0.);self.assertNotEqual(leveler._prev_y,0.)
                residue=leveler.process(np.zeros(240,np.float32));baseline=fresh.process(np.zeros(240,np.float32))
                np.testing.assert_array_equal(baseline,np.zeros(240,np.int16))
                self.assertEqual(np.count_nonzero(residue),240);self.assertEqual(int(np.abs(residue.astype(np.int32)).max()),6026)
            finally:leveler.close();fresh.close()
        OBSERVATIONS.append({'id':'F27','fixed':False,'actual_numpy_executed':True,'flush_ended_at_zero':True,
            'dc_memory_retained_after_flush':True,'zero_input_after_flush_nonzero_samples':240,
            'zero_input_after_flush_peak_i16':6026,'fresh_zero_input_nonzero_samples':0,
            'rust_binary_executed':False,'normal_worker_same_leveler_reuse_proven':False,'user_hiss_root_cause_proven':False})

    def test_observed_benchmark_accepts_duplicate_synthesis_gpu_identity_across_workers(self):
        with bench_fixture(self.root,wrong_gpu=True) as (module,args,_,_,received):report=module.run(args)
        self.assertEqual(report['status'],'measured-speed-only');self.assertTrue(report['real_gpu_verified']);self.assertTrue(report['speed_target_passed'])
        self.assertEqual({row['gpu'] for row in report['measurements']},{0});self.assertEqual({row['worker'] for row in report['measurements']},{0,1})
        self.assertEqual(len(report['measurements']),18);self.assertEqual(len([r for r in received if r[1]=='/synth']),18)
        self.assertFalse(report['voice_quality_verified']);self.assertFalse(report['all_user_requirements_completed'])
        OBSERVATIONS.append({'id':'F28','fixed':False,'actual_original_benchmark_run_and_measure':True,
            'actual_local_http_two_endpoints':True,'health_gpu_identities':[0,1],'measurement_gpu_identities':[0],
            'measurement_rows':18,'status':'measured-speed-only','report_real_gpu_verified':True,
            'health_stats_pcm_and_clock_are_fixtures':True,'actual_model_or_gpu_executed':False,'performance_improvement_measured':False})


if __name__=='__main__':unittest.main()
