"""Probe contracts; fake GPU objects are never real device/quality evidence."""
import ast
import importlib.util
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, patch

ROOT=Path(__file__).resolve().parents[1]/'source'
spec=importlib.util.spec_from_file_location('backend_probe',ROOT/'tools/backend_probe.py')
probe=importlib.util.module_from_spec(spec);spec.loader.exec_module(probe)

class Backend:
    @classmethod
    def from_pretrained(cls, name, **kwargs):raise AssertionError('model loading is forbidden')
    def warmup(self, prefill_len=100):raise AssertionError('warmup forbidden')
    def _prepare_generation(self,text,**kwargs):raise AssertionError('generation forbidden')


def fake_import(count=2,available=True,cls=Backend):
    cuda=SimpleNamespace(is_available=lambda:available,device_count=lambda:count,
        get_device_properties=lambda index:SimpleNamespace(name='FAKE T4',total_memory=16<<30),
        get_device_capability=lambda index:(7,5))
    return lambda name:SimpleNamespace(cuda=cuda) if name=='torch' else (SimpleNamespace(fast_generate_streaming=lambda **kw:None) if name=='faster_qwen3_tts.streaming' else SimpleNamespace(FasterQwen3TTS=cls))


class ProbeTests(unittest.TestCase):
    def setUp(self):
        # API/GPU surface unit fixtures must not pretend to import a real Qwen package.
        smoke=patch('qwen_compat.configuration_smoke',return_value={'status':'installed','configuration_smoke_passed':True})
        smoke.start();self.addCleanup(smoke.stop)

    def test_static_inspection_never_imports_cuda_backend_or_loads_a_model(self):
        with patch.object(probe.metadata,'version',return_value='test-version'),patch.object(probe.importlib,'import_module',side_effect=AssertionError('no imports')):
            report=probe.collect(False)
        self.assertEqual(report['status'],'inspection_only')
        self.assertFalse(report['model_loaded'])

    def test_runtime_surface_pass_is_not_model_training_or_performance_success(self):
        with patch.object(probe.metadata,'version',return_value='test-version'),patch.object(probe.importlib,'import_module',side_effect=fake_import()):
            report=probe.collect(True)
        self.assertEqual(report['status'],'surface_preflight_passed')
        self.assertEqual(len(report['devices']),2)
        for key in ['model_loaded','inference_verified','training_verified','performance_verified']:self.assertIs(report[key],False)
        self.assertTrue(any('forwarding/semantics unverified' in c['detail'] for c in report['checks']))

    def test_missing_cuda_or_gpu_count_blocks_instead_of_using_mock_success(self):
        for available,count in [(False,0),(True,1)]:
            with patch.object(probe.metadata,'version',return_value='test-version'),patch.object(probe.importlib,'import_module',side_effect=fake_import(count,available)):
                self.assertEqual(probe.collect(True)['status'],'blocked')

    def test_t4_bf16_and_unapproved_fp32_are_blocked(self):
        with patch.object(probe.metadata,'version',return_value='test-version'),patch.object(probe.importlib,'import_module',side_effect=fake_import()),patch.dict(os.environ,{'QTTS_ALLOW_FP32':'0'}):
            for dtype in ['bf16','fp32']:self.assertEqual(probe.collect(True,dtype=dtype)['status'],'blocked')

    def test_incompatible_keyword_signature_is_blocked(self):
        class Wrong(Backend):
            def _prepare_generation(self, text):pass
        with patch.object(probe.metadata,'version',return_value='test-version'),patch.object(probe.importlib,'import_module',side_effect=fake_import(cls=Wrong)):
            self.assertEqual(probe.collect(True)['status'],'blocked')

    def test_positional_only_required_keyword_is_blocked(self):
        class Wrong:
            def warmup(self,prefill_len,/):pass
        report={'checks':[]}
        probe.signature_check(report,Wrong,'warmup',['prefill_len'])
        self.assertEqual(report['checks'][0]['status'],'blocked')

    def test_new_required_parameter_and_keyword_only_model_id_are_blocked(self):
        class Wrong:
            def warmup(self,prefill_len,new_required):pass
            @classmethod
            def from_pretrained(cls,*,model_id,**kwargs):pass
        for method,parameters in [('warmup',['prefill_len']),('from_pretrained',['device','dtype','attn_implementation','max_seq_len'])]:
            report={'checks':[]}
            probe.signature_check(report,Wrong,method,parameters)
            self.assertEqual(report['checks'][0]['status'],'blocked')

    def test_import_error_message_cannot_leak_secrets_into_report(self):
        with patch.object(probe.metadata,'version',return_value='test-version'),patch.object(probe.importlib,'import_module',side_effect=RuntimeError('sk-sensitive-value')):
            report=probe.collect(True)
        self.assertEqual(report['status'],'blocked')
        self.assertNotIn('sk-sensitive-value',json.dumps(report))

    def test_runtime_timeout_kills_group_and_does_not_claim_ready(self):
        process=MagicMock(pid=123456)
        process.wait.side_effect=[subprocess.TimeoutExpired('fake',1),None]
        with patch.object(probe.subprocess,'Popen',return_value=process),patch.object(probe.os,'killpg') as kill:
            report=probe.isolated_runtime(2,'fp16',1)
        self.assertEqual(report['status'],'blocked');kill.assert_called_once()
        self.assertTrue(any(c['name']=='runtime_timeout' for c in report['checks']))

    def test_child_exit_without_report_is_a_structured_failure(self):
        with patch.object(probe.subprocess,'Popen',return_value=MagicMock(pid=123456)):
            report=probe.isolated_runtime(2,'fp16',1)
        self.assertEqual(report['status'],'blocked')
        self.assertTrue(any(c['name']=='runtime_child' for c in report['checks']))

    def test_atomic_report_permissions_and_cli_static_exit_are_honest(self):
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)/'report.json'
            result=subprocess.run([sys.executable,str(ROOT/'tools/backend_probe.py'),'--output',str(output)],capture_output=True,text=True,timeout=10)
            report=json.loads(output.read_text())
            self.assertEqual(result.returncode,2)
            self.assertIn(report['status'],['blocked','inspection_only'])
            self.assertFalse(report['model_loaded'])
            self.assertEqual(stat.S_IMODE(output.stat().st_mode),0o600)

    def test_probed_keywords_match_actual_worker_calls(self):
        methods=['from_pretrained','warmup','_prepare_generation','generate_voice_clone','fast_generate_streaming']
        actual=[]
        for file in ('py/worker.py','py/adapter_engine.py','py/clone_stream.py'):
            actual += [(node.func.attr if isinstance(node.func,ast.Attribute) else node.func.id,{kw.arg for kw in node.keywords}) for node in ast.walk(ast.parse((ROOT/file).read_text()))
                if isinstance(node,ast.Call) and ((isinstance(node.func,ast.Attribute) and node.func.attr in methods) or (isinstance(node.func,ast.Name) and node.func.id in methods))]
        checked=[(ast.literal_eval(node.args[2]),set(ast.literal_eval(node.args[3]))) for node in ast.walk(ast.parse((ROOT/'tools/backend_probe.py').read_text()))
            if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='signature_check']
        self.assertEqual(len(actual),len(checked))
        for call in actual:self.assertIn(call,checked)

    def test_bootstrap_probes_before_starting_downloads(self):
        source=(ROOT/'py/bootstrap.py').read_text().split('def main()',1)[1]
        self.assertLess(source.index('runtime compatibility preflight'),source.index('3/9 start model download'))
        self.assertIn('"--expected-gpus",str(n_workers)',source)

if __name__=='__main__':unittest.main()
