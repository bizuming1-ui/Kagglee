"""Read-only G0 tool tests: diagnostic false-accept witnesses are NOT fixes/GPU proof."""
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import io
import itertools
import json
import os
from pathlib import Path
import signal
import struct
import subprocess
import sys
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch
import test_reliability
import gpu_ownership as gpu

ROOT=Path(__file__).resolve().parents[1]/'source'
OBSERVATIONS=[]

def load(name):
    spec=importlib.util.spec_from_file_location('g0_tool_'+name,ROOT/'tools'/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def worker_frame(kind,payload):return struct.pack('<BI',kind,len(payload))+payload
def gateway_frame(kind,payload,seg=0):return struct.pack('<BII',kind,seg,len(payload))+payload

def encoded(value):return json.dumps(value,ensure_ascii=False).encode()

@contextmanager
def http_fixture(body,status=200):
    received=[]
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*_):pass
        def do_POST(self):
            received.append(self.path)
            self.rfile.read(int(self.headers.get('Content-Length',0)))
            self.send_response(status);self.send_header('Content-Length',str(len(body)))
            self.send_header('X-Session-Id','fixture-session');self.end_headers()
            self.wfile.write(body)
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
    thread=threading.Thread(target=lambda:server.serve_forever(poll_interval=.01));thread.start()
    try:yield f'http://127.0.0.1:{server.server_port}',received
    finally:
        server.shutdown();thread.join(3);server.server_close()
        if thread.is_alive():raise AssertionError('HTTP fixture did not stop')


def gateway_body(stats=None,end=None,pcm=b'\x00\x00',trailing=b''):
    return (gateway_frame(2,encoded({'text':'fixture'})) + gateway_frame(1,pcm)
        + gateway_frame(4,encoded({'gpu':0} if stats is None else stats))
        + gateway_frame(5,encoded({} if end is None else end)) + trailing)


def e2e_main(module,url):
    output=io.StringIO()
    with patch.object(sys,'argv',['e2e_check.py','--url',url]),patch.dict(os.environ,{'QTTS_ACCESS_TOKEN':'synthetic-local-fixture'}),redirect_stdout(output):
        try:module.main()
        except SystemExit as result:return result.code,output.getvalue()
    raise AssertionError('expected CLI exit')


class ToolBoundaryTests(unittest.TestCase):
    def test_observed_e2e_false_accepts_missing_gpu_failed_end_and_bad_pcm(self):
        module=load('e2e_check');rows=[]
        cases=[('missing-gpu',gateway_body(stats={})),
               ('failed-end',gateway_body(end={'failed':True,'cancelled':True})),
               ('odd-pcm',gateway_body(pcm=b'\x00\x01\x02')),
               ('partial-next-header',gateway_body(trailing=b'\x01\x00'))]
        for name,body in cases:
            with self.subTest(case=name),http_fixture(body) as (url,received):
                code,out=e2e_main(module,url)
                self.assertEqual(code,0,out);self.assertIn('RESULT: PASS',out)
                self.assertEqual(received,['/api/speak'])
                rows.append({'case':name,'exit_code':code,'reported_pass':True})
        OBSERVATIONS.append({'id':'F13','cases':rows,'actual_local_http':True,
                             'actual_gpu_or_gateway_executed':False,'fixed':False})

    def test_observed_watermark_passes_empty_http_failure_and_error_stream(self):
        module=load('watermark_check');rows=[]
        for name,status,body in [('empty-503',503,b''),('error-frame',200,gateway_frame(6,encoded({'error':'fixture failure'}))),
                                 ('partial-header',200,b'\x01\x00')]:
            threads=[]
            def make_thread(*args,**kwargs):
                thread=threading.Thread(*args,**kwargs);threads.append(thread);return thread
            output=io.StringIO()
            with self.subTest(case=name),http_fixture(body,status) as (url,received),patch.object(sys,'argv',['watermark_check.py','--url',url]),patch('access_control.load_access_token',return_value='synthetic-local-fixture'),patch.object(module,'threading',NS(Thread=make_thread,Lock=threading.Lock)),redirect_stdout(output):
                try:
                    with self.assertRaises(SystemExit) as raised:module.main()
                    self.assertEqual(raised.exception.code,0)
                finally:
                    for thread in threads:
                        thread.join(3);self.assertFalse(thread.is_alive(),'tool daemon outlived fixture')
            self.assertIn('audio=0.0s',output.getvalue());self.assertIn('RESULT: PASS',output.getvalue())
            self.assertIn('/api/speak',received)
            rows.append({'case':name,'http_status':status,'audio_seconds':0.,'exit_code':0,'reported_pass':True})
        OBSERVATIONS.append({'id':'F14','cases':rows,'actual_local_http':True,
                             'player_is_tool_simulator_not_browser':True,'fixed':False})

    def test_observed_selftest_accepts_explicitly_failed_mock_stream(self):
        module=load('selftest');module.RESULTS.clear()
        body=worker_frame(1,bytes(12000*2))*3 + worker_frame(2,encoded({'failed':True,'cancelled':True,'engine':'mock','gpu':0}))
        # Deterministic diagnostic timestamps, not measured speed/first sound.
        clock=itertools.count();output=io.StringIO()
        with http_fixture(body) as (url,received),patch.object(module,'PORTS',[int(url.rsplit(':',1)[1])]),patch.object(module,'time',NS(time=lambda:next(clock)*.01)),redirect_stdout(output):
            result=module.t_stream('fixture-profile')
        self.assertIs(result,True);self.assertEqual(received,['/synth'])
        self.assertEqual(module.RESULTS[-1]['status'],'passed')
        OBSERVATIONS.append({'id':'F15','failed_stats':True,'cancelled_stats':True,'engine':'mock',
                             'tool_check_returned':True,'actual_local_http':True,
                             'timing_is_deterministic_fixture':True,'actual_model_executed':False,'fixed':False})

    def test_protect_benchmark_default_cli_blocked_private_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            out=Path(temporary)/'report.json'
            command=[sys.executable,str(ROOT/'tools/voice_benchmark.py'),'--output',str(out)]
            first=subprocess.run(command,capture_output=True,text=True,timeout=10)
            self.assertEqual(first.returncode,2,first.stderr)
            report=json.loads(out.read_text());self.assertEqual(report['status'],'blocked')
            self.assertFalse(report['real_gpu_verified']);self.assertFalse(report['voice_quality_verified'])
            self.assertEqual(report['measurements'],[]);self.assertEqual(out.stat().st_mode&0o777,0o600)
            saved=out.read_bytes()
            second=subprocess.run(command,capture_output=True,text=True,timeout=10)
            self.assertNotEqual(second.returncode,0);self.assertEqual(out.read_bytes(),saved)

    def test_protect_benchmark_valid_fixture_parses_exact_padding_not_gpu_proof(self):
        module=load('voice_benchmark')
        stats={'engine':'faster-qwen3-tts','voice_binding':'fixture-pin','speech_samples':240,
               'gen_ms':10.,'rtf':1.,'gpu':0}
        body=worker_frame(1,bytes((240+192)*2))+worker_frame(2,encoded(stats))
        with http_fixture(body) as (url,_):pcm,row=module.measure(url,{'voice_binding':'fixture-pin'})
        self.assertEqual(len(pcm),(240+192)*2)
        self.assertEqual(row['speech_seconds'],.01);self.assertEqual(row['worker_rtf'],1.)
        self.assertGreater(row['wall_seconds'],0.)
        # Injected worker statistics/zero PCM validate parser only, never RTF achievement.

    def test_protect_benchmark_rejects_failure_bounds_protocol_and_metric_mismatch(self):
        module=load('voice_benchmark')
        stats={'engine':'faster-qwen3-tts','voice_binding':'fixture-pin','speech_samples':240,'gen_ms':10.,'rtf':1.}
        pcm=worker_frame(1,bytes((240+192)*2));terminal=worker_frame(2,encoded(stats))
        cases=[pcm,pcm+terminal+b'\x01',pcm+terminal+pcm,
               worker_frame(9,b'x'),struct.pack('<BI',1,16*1024*1024+1),worker_frame(3,b'private-error')]
        for mutation in ({'failed':True},{'cancelled':True},{'engine':'mock'},{'voice_binding':'old'},
                         {'anomalies':['bad']},{'speech_samples':True},{'speech_samples':432},{'rtf':.5},{'gen_ms':float('nan')}):
            cases.append(pcm+worker_frame(2,encoded(dict(stats,**mutation))))
        for index,body in enumerate(cases):
            with self.subTest(case=index),http_fixture(body) as (url,_):
                with self.assertRaises(RuntimeError):module.measure(url,{'voice_binding':'fixture-pin'})
        with http_fixture(pcm+terminal,503) as (url,_):
            import requests
            with self.assertRaises(requests.HTTPError):module.measure(url,{'voice_binding':'fixture-pin'})

    def test_protect_backend_actual_isolated_runtime_stays_blocked_without_models(self):
        with tempfile.TemporaryDirectory() as temporary:
            out=Path(temporary)/'probe.json'
            cp=subprocess.run([sys.executable,str(ROOT/'tools/backend_probe.py'),'--runtime','--timeout','10','--output',str(out)],capture_output=True,text=True,timeout=15)
            self.assertEqual(cp.returncode,2,cp.stderr)
            report=json.loads(out.read_text());self.assertEqual(report['status'],'blocked')
            self.assertEqual(json.loads(cp.stdout),report)
            for key in ('model_loaded','inference_verified','training_verified','performance_verified'):
                self.assertIs(report[key],False)
            self.assertEqual(out.stat().st_mode&0o777,0o600)

    def test_protect_resource_status_and_invalid_duration_do_not_create_lock(self):
        module=load('resource_control')
        with tempfile.TemporaryDirectory() as temporary,patch.object(gpu,'default_root',return_value=Path(temporary)/'ownership'):
            output=io.StringIO()
            with redirect_stdout(output):self.assertEqual(module.main(['status']),0)
            row=json.loads(output.getvalue());self.assertFalse(row['busy']);self.assertFalse(row['gpu_verified'])
            for seconds in ('0','3601'):
                with redirect_stderr(io.StringIO()),self.assertRaises(SystemExit) as raised:
                    module.main(['reserve','--seconds',seconds])
                self.assertEqual(raised.exception.code,2)
            self.assertFalse((Path(temporary)/'ownership').exists())

    def test_protect_resource_rejection_restores_signal_handlers_and_holder(self):
        module=load('resource_control')
        handlers={sig:signal.getsignal(sig) for sig in (signal.SIGINT,signal.SIGTERM)}
        with tempfile.TemporaryDirectory() as temporary,patch.object(gpu,'default_root',return_value=Path(temporary)/'ownership'):
            with gpu.GpuLease.acquire('inference'):
                output=io.StringIO()
                with redirect_stdout(output):code=module.main(['reserve','--seconds','1'])
                self.assertEqual(code,2);self.assertEqual(json.loads(output.getvalue())['status'],'rejected')
                self.assertTrue(gpu.status()['busy'])
            self.assertFalse(gpu.status()['busy'])
        self.assertEqual({sig:signal.getsignal(sig) for sig in handlers},handlers)

    def test_protect_e2e_http_and_explicit_error_do_fail(self):
        module=load('e2e_check')
        with http_fixture(b'fixture unavailable',503) as (url,_):
            code,_=e2e_main(module,url);self.assertEqual(code,2)
        with http_fixture(gateway_body()+gateway_frame(6,encoded({'error':'fixture failure'}))) as (url,_):
            code,out=e2e_main(module,url);self.assertEqual(code,1);self.assertIn('[FAIL] no error frames',out)

    def test_protect_selftest_wrapper_distinguishes_skip_fail_and_pass(self):
        module=load('selftest');module.RESULTS.clear()
        with redirect_stdout(io.StringIO()):
            for value in (None,False,True):
                fn=module.check('fixture check')(lambda value=value:(value,'fixture only'))
                self.assertIs(fn(),value)
        self.assertEqual([r['status'] for r in module.RESULTS],['skipped','failed','passed'])

    def test_protect_simulated_player_drains_completed_short_tail(self):
        module=load('e2e_check')
        under,gap,total,first=module.simulate_player([(1.,1,0,480)],2.,4.)
        self.assertEqual((under,gap,total,first),(0,0.,0.,1.))
        self.assertEqual(module.simulate_player([],2.,4.),(0,0,0,None))
        under,_,_,first=module.simulate_player([(0.,1,0,24000),(3.,1,1,24000)],.1,.1)
        self.assertEqual(under,1);self.assertIsNotNone(first)

if __name__=='__main__':unittest.main()
