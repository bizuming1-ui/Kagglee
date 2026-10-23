"""CPU schema/controller regressions. Real package check is rope_wheel_check.py."""
import copy
import os
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch,MagicMock
import test_reliability
import worker
import bootstrap
import supervisor
import qwen_compat as qc


def original(config,device=None,seq_len=None,layer_type=None):
    return (config.rope_theta,getattr(config,'partial_rotary_factor',1.),device,seq_len,layer_type)
original.__module__='qwen_tts._transformers_compat';original.__name__='_default_rope_parameters'


class CompatibilityTests(unittest.TestCase):
    def test_modern_schema_uses_actual_theta_not_a_hardcoded_default(self):
        for theta in (10000.,12345.,1000000.):
            cfg=NS(rope_parameters={'rope_type':'default','rope_theta':theta});before=copy.deepcopy(cfg.__dict__)
            self.assertEqual(qc.legacy_default_call(original,cfg,'cpu',7), (theta,1.,'cpu',7,None));self.assertEqual(before,cfg.__dict__)

    def test_legacy_schema_and_device_are_unchanged(self):
        cfg=NS(rope_theta=999.,partial_rotary_factor=.5)
        self.assertEqual(qc.legacy_default_call(original,cfg,'cuda:0',8,'layer'),(999.,.5,'cuda:0',8,'layer'))

    def test_scaled_missing_nested_invalid_modern_schema_refused(self):
        for params in (None,{}, {'rope_type':'linear','rope_theta':10000.},{'layer':{'rope_theta':10000.}},
                       {'rope_type':'default','rope_theta':float('nan')},{'rope_type':'default','rope_theta':-1},
                       {'rope_type':'default','rope_theta':True},{'rope_type':'default','rope_theta':100.,'partial_rotary_factor':2}):
            with self.subTest(params=params),self.assertRaises(qc.BackendCompatibilityError):qc.legacy_default_call(original,NS(rope_parameters=params))

    def test_partial_factor_propagates_without_mutating_modern_dict(self):
        cfg=NS(rope_parameters={'rope_type':'default','rope_theta':111.,'partial_rotary_factor':.5})
        self.assertEqual(qc.legacy_default_call(original,cfg)[:2],(111.,.5));self.assertFalse(hasattr(cfg,'rope_theta'))

    def test_registry_install_idempotent_and_unknown_override_refused(self):
        module=NS(_default_rope_parameters=original);registry={'default':original};qc.bridge_registry(module,registry)
        first=registry['default'];qc.bridge_registry(module,registry);self.assertIs(first,registry['default'])
        registry['default']=lambda:None
        with self.assertRaises(qc.BackendCompatibilityError):qc.bridge_registry(module,registry)
        with self.assertRaises(qc.BackendCompatibilityError):qc.bridge_registry(NS(_default_rope_parameters=original),{})

    def test_legacy_official_namespace_does_not_import_or_patch_hf5(self):
        with patch.dict(sys.modules,{'qwen_tts._transformers_compat':None}),patch.object(qc,'installed_version',return_value=None),patch.object(qc.importlib,'import_module',side_effect=AssertionError('legacy must not import HF')):
            self.assertEqual(qc.install_qwen_rope_bridge()['status'],'not_applicable')

    def test_unreviewed_or_colliding_hf_distribution_rejected(self):
        with patch.dict(sys.modules,{'qwen_tts._transformers_compat':NS(_default_rope_parameters=original)}):
            with patch.object(qc,'installed_version',return_value='unknown'),self.assertRaises(qc.BackendCompatibilityError):qc.install_qwen_rope_bridge()
            def versions(name):return '0.1.1' if name=='qwen-tts' else qc.PINS.get(name)
            with patch.object(qc,'installed_version',side_effect=versions),self.assertRaises(qc.BackendCompatibilityError):qc.install_qwen_rope_bridge()

    def test_installed_hf_is_imported_even_when_faster_has_not_imported_qwen(self):
        module=NS(_default_rope_parameters=original);registry={'default':original}
        with patch.dict(sys.modules,{'qwen_tts._transformers_compat':None}),patch.object(qc,'installed_version',side_effect=qc.PINS.get),patch.object(qc.importlib,'import_module',return_value=module) as importer,patch.dict(sys.modules,{'transformers.modeling_rope_utils':NS(ROPE_INIT_FUNCTIONS=registry)}):
            self.assertEqual(qc.install_qwen_rope_bridge()['status'],'installed')
            importer.assert_called_once_with('qwen_tts._transformers_compat')
            first=registry['default'];self.assertTrue(first._qtts_rope_bridge)
            self.assertEqual(qc.install_qwen_rope_bridge()['status'],'installed');self.assertIs(first,registry['default'])

    def test_installed_hf_import_failure_blocks_instead_of_not_applicable(self):
        with patch.object(qc,'installed_version',side_effect=qc.PINS.get),patch.object(qc.importlib,'import_module',side_effect=ImportError('missing CPU dependency')),self.assertRaises(qc.BackendCompatibilityError):qc.install_qwen_rope_bridge()

    def test_hf_bad_versions_and_namespace_conflicts_are_rejected_before_import(self):
        cases=[{**qc.PINS,'qwen-tts-hf':'unreviewed'}, {**qc.PINS,'transformers':'unreviewed'}, {**qc.PINS,'qwen-tts':'0.1.1'}]
        for versions in cases:
            with self.subTest(versions=versions),patch.object(qc,'installed_version',side_effect=versions.get),patch.object(qc.importlib,'import_module',side_effect=AssertionError('must reject before import')),self.assertRaises(qc.BackendCompatibilityError):qc.install_qwen_rope_bridge()

    def test_loaded_hf_module_without_distribution_metadata_is_not_legacy(self):
        with patch.dict(sys.modules,{'qwen_tts._transformers_compat':NS()}),patch.object(qc,'installed_version',return_value=None),self.assertRaises(qc.BackendCompatibilityError):qc.install_qwen_rope_bridge()

    def test_preflight_refuses_skipped_or_incomplete_hf_smoke(self):
        import test_probe
        for result in ({'status':'not_applicable'},{'status':'installed','configuration_smoke_passed':False},{'status':'installed'}):
            report={'checks':[]}
            with patch.object(qc,'configuration_smoke',return_value=result),patch.object(qc,'installed_version',side_effect=qc.PINS.get):test_probe.probe.qwen_configuration_check(report)
            self.assertEqual(report['checks'][0]['status'],'blocked');self.assertTrue(report['checks'][0]['required'])

    def test_preflight_still_allows_official_legacy_without_hf_smoke(self):
        import test_probe
        report={'checks':[]}
        with patch.object(qc,'configuration_smoke',return_value={'status':'not_applicable'}),patch.object(qc,'installed_version',return_value=None):test_probe.probe.qwen_configuration_check(report)
        self.assertEqual(report['checks'][0]['status'],'warning');self.assertFalse(report['checks'][0]['required'])

    def test_worker_fatal_boot_is_distinguished_from_transient_failure(self):
        for error,fatal in [(AttributeError("'MimiConfig' object has no attribute 'rope_theta'"),True),(qc.BackendCompatibilityError('bad config'),True),(RuntimeError('temporary IO'),False)]:
            instance=worker.Worker();instance.engine.load=MagicMock(side_effect=error)
            instance.boot();self.assertFalse(instance.ready);self.assertEqual(instance.fatal_error,fatal)

    def test_wait_ready_exits_on_fatal_health_and_on_current_nonce_receipt(self):
        with tempfile.TemporaryDirectory() as directory,patch.object(bootstrap,'STATE',Path(directory)):
            process=MagicMock();process.poll.return_value=None
            with patch.object(bootstrap,'http_json',return_value={'workers':[{'worker':{'fatal_error':True}}]}):self.assertFalse(bootstrap.wait_ready(2,supervisor_process=process))
            import json
            (Path(directory)/'startup-failure.json').write_text(json.dumps({'startup_id':bootstrap.STARTUP_ID}))
            with patch.object(bootstrap,'http_json',side_effect=AssertionError('must fail before gateway call')):self.assertFalse(bootstrap.wait_ready(2,supervisor_process=process))

    def test_owned_supervisor_cleanup_uses_only_supplied_popen(self):
        process=MagicMock();process.poll.return_value=None;bootstrap.stop_created_supervisor(process)
        process.terminate.assert_called_once();process.wait.assert_called_once_with(timeout=45)
        process=MagicMock();process.poll.return_value=0;bootstrap.stop_created_supervisor(process);process.terminate.assert_not_called()

    def test_supervisor_stops_fatal_worker_without_retry(self):
        supervisor.STOP.clear();self.addCleanup(supervisor.STOP.clear)
        process=MagicMock();process.p.poll.return_value=None;process.gave_up=False;process.name='worker0';process.health_url='http://127.0.0.1:7001/health'
        process.kill.side_effect=supervisor.STOP.set
        with patch.object(supervisor,'http_json',return_value={'fatal_error':True,'error':'MimiConfig rope_theta'}),patch.object(supervisor,'write_json_atomic') as receipt:
            supervisor.watch([process])
        process.kill.assert_called_once();process.restart.assert_not_called();self.assertTrue(process.gave_up);receipt.assert_called_once()

    def test_two_worker_gpu_mapping_is_distinct(self):
        procs=[p for p in supervisor.build_procs() if p.name.startswith('worker')]
        self.assertEqual([p.env['CUDA_VISIBLE_DEVICES'] for p in procs],['0','1'])

    def test_session_resident_does_not_restart_at_600_or_old_memory_limit(self):
        instance=worker.Worker();instance.served=700;instance.engine.vram=lambda:{'alloc_mb':14000}
        fake=NS(cuda=NS(empty_cache=lambda:None))
        with patch.object(worker,'MOCK',False),patch.dict(sys.modules,{'torch':fake}),patch.dict(os.environ,{'QTTS_RESIDENT':'1'}):instance.after_job()
        self.assertFalse(instance.restart_requested)
        with patch.object(worker,'MOCK',False),patch.dict(sys.modules,{'torch':fake}),patch.dict(os.environ,{'QTTS_RESIDENT':'0'}):instance.after_job()
        self.assertTrue(instance.restart_requested)

    def test_install_constraints_preserve_platform_torch_cuda_and_audio(self):
        versions={'torch':'2.10.0+cu128','torchaudio':'2.10.0+cu128','torchvision':None}
        def run_pip(*args):
            self.assertIn('--constraint',args)
            constraints=Path(args[-1]).read_text();self.assertIn('torch==2.10.0+cu128',constraints);self.assertIn('torchaudio==2.10.0+cu128',constraints)
            self.assertIn('transformers==5.20.2',args);self.assertNotIn('--upgrade',args)
        with tempfile.TemporaryDirectory() as directory,patch.object(bootstrap,'STATE',Path(directory)),patch.object(bootstrap,'installed_version',side_effect=versions.get),patch.object(bootstrap,'pip',side_effect=run_pip):bootstrap.install_reviewed_faster()
        with patch.object(bootstrap,'installed_version',return_value=None),patch.object(bootstrap,'pip') as pip_call,self.assertRaises(RuntimeError):bootstrap.install_reviewed_faster()
        pip_call.assert_not_called()


if __name__=='__main__':unittest.main()
