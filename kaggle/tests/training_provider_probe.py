"""HF wheel metadata + original constructor with explicit heavy-loader fixtures.
No installed Qwen, Torch, weights, encoding or training; metadata is not fabricated.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import importlib.metadata as metadata
import json
import os
import sys
import tempfile
from types import SimpleNamespace as NS
from unittest.mock import Mock, patch

R=Path(__file__).resolve().parents[2]
H=R/'docs/validation/step18'

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--round',type=int,choices=(1,2,3),required=True)
    args=parser.parse_args()
    provenance=json.loads((H/'chain-provider-provenance.json').read_text())
    path=R/provenance['metadata_path']
    assert hashlib.sha256(path.read_bytes()).hexdigest()==provenance['metadata_sha256']
    sys.path[:0]=[str(R/'kaggle/source/py'),str(path.parent.parent)]
    import training_codes as tc
    import qwen_compat as compat
    from resource_limits import UploadRejected
    assert metadata.version('qwen-tts-hf')=='0.1.1.post1'
    try:
        metadata.version('qwen-tts')
    except metadata.PackageNotFoundError:
        pass
    else:
        raise AssertionError('Probe requires no old qwen-tts metadata; never install both namespaces')
    cases=[{'id':'CHAIN-P01','case':'hash-pinned-real-HF-wheel-metadata',
            'HF_version':metadata.version('qwen-tts-hf'),'legacy_metadata_present':False,
            'metadata_path_scoped_not_installed':True}]
    with tempfile.TemporaryDirectory(prefix='qtts-provider-') as temp:
        directory=Path(temp)
        (directory/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (directory/'model.safetensors').write_bytes(b'NOT REAL WEIGHTS; local hash fixture only')
        pin=tc.model_fingerprint(directory)
        cfg=NS(model_type='qwen3_tts_tokenizer_12hz',input_sample_rate=24000,output_sample_rate=24000,
               encode_downsample_rate=1920,decode_upsample_rate=1920,encoder_valid_num_quantizers=16,
               encoder_config=NS(codebook_size=2048),decoder_config=NS(codebook_size=2048,num_quantizers=16))
        loaded=NS(config=cfg,device='cpu',model=NS(dtype='float32',eval=Mock()),feature_extractor=NS(sampling_rate=24000))
        loader=Mock(return_value=loaded)
        modules={'torch':NS(float32='float32',set_num_threads=Mock()),
                 'qwen_tts':NS(Qwen3TTSTokenizer=NS(from_pretrained=loader))}
        with patch.dict(sys.modules,modules), patch.object(compat,'install_qwen_rope_bridge',return_value={'status':'fixture-bypass'}),patch.dict(os.environ,{}):
            try:
                tc.QwenCPUEncoder(directory,pin)
            except metadata.PackageNotFoundError as error:
                assert error.name=='qwen-tts'
            else:
                raise AssertionError('Expected original constructor to query absent legacy distribution')
            assert loader.call_count==1
            cases.append({'id':'CHAIN-P02','case':'original-encoder-provider-mismatch',
                          'observed':'PackageNotFoundError: qwen-tts','heavy_loader_fixture_called':True,
                          'real_model_loaded':False,'condition':'after successful prior loader/contract steps',
                          'classification':'confirmed-provider-metadata-contract-defect'})
            # Precisely show the older broad stub can conceal this defect.
            with patch.object(tc.importlib.metadata,'version',return_value='stub-only'):
                encoder=tc.QwenCPUEncoder(directory,pin)
                assert encoder.version=='stub-only'
            cases.append({'id':'CHAIN-P03','case':'broad-metadata-stub-conceals-missing-provider',
                          'stubbed_version':'stub-only','constructor_completed_with_fixtures':True})
            before=loader.call_count
            try:
                tc.QwenCPUEncoder(directory,'f'*64)
            except UploadRejected as error:
                assert error.code==409
            else:
                raise AssertionError('Wrong model pin accepted')
            assert loader.call_count==before
            cases.append({'id':'CHAIN-P04','case':'wrong-model-pin-rejected-before-loader','code':409})
    # Execute only the existing provider_version body, avoiding module-level Torch.
    training=R/'kaggle/source/py/tts_training.py'
    node=next(node for node in ast.parse(training.read_bytes()).body if isinstance(node,ast.FunctionDef) and node.name=='provider_version')
    namespace={}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[])),str(training),'exec'),namespace)
    assert namespace['provider_version']()=='0.1.1.post1'
    cases.append({'id':'CHAIN-P05','case':'existing-training-provider-helper-recognizes-HF',
                  'version':'0.1.1.post1','method':'actual AST function, no Torch import'})
    try:
        compat.install_qwen_rope_bridge()
    except compat.BackendCompatibilityError:
        pass
    else:
        raise AssertionError('Metadata-only environment must not claim full reviewed runtime')
    cases.append({'id':'CHAIN-P06','case':'metadata-alone-not-a-compatible-runtime',
                  'runtime_admission_blocked':True,'Qwen_imported':False})
    names=('training_codes.py','tts_training.py','qwen_compat.py')
    receipt={'round':args.round,'experiment_completed':True,'cases':cases,
             'source_hashes':{f'kaggle/source/py/{name}':hashlib.sha256((R/'kaggle/source/py'/name).read_bytes()).hexdigest() for name in names},
             'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'wheel_sha256':provenance['wheel_sha256'],'metadata_sha256':provenance['metadata_sha256'],
             'heavy_loader_and_bridge_are_fixtures':True,'actual_qwen_encoder_executed':False,
             'torch_executed':False,'weights_loaded':False,'actual_training_executed':False,
             'gpu_executed':False,'real_voice_executed':False,'product_modified':False}
    print(json.dumps(receipt,ensure_ascii=False,indent=2))
