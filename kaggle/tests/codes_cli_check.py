#!/usr/bin/env python3
"""Three real local CLI/storage rounds; codes are TEST FIXTURE, not real Qwen."""
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]/'source'
sys.path.insert(0,str(ROOT/'py'));sys.path.insert(0,str(Path(__file__).resolve().parent))
from test_training_data import wav
from voice_library import LibraryStore
from training_data import TrainingDataStore
from training_codes import TrainingCodesStore,model_fingerprint
from resource_limits import UploadLimits


def cli(*args):
    result=subprocess.run([sys.executable,str(ROOT/'tools/encode_training.py'),*args],capture_output=True,text=True,timeout=20)
    return result.returncode,json.loads(result.stdout)


def main():
    missing=importlib.util.find_spec('torch') is None or importlib.util.find_spec('qwen_tts') is None
    with tempfile.TemporaryDirectory(prefix='qtts-codes-check-') as temporary:
        state=Path(temporary);limits=UploadLimits()
        libraries=LibraryStore(state/'libraries',free_bytes=0)
        inputs=TrainingDataStore(state/'training_data',limits,free_bytes=0)
        codes=TrainingCodesStore(state/'training_codes',limits,free_bytes=0)
        model=state/'fixture-model';model.mkdir()
        (model/'config.json').write_text('{"model_type":"qwen3_tts_tokenizer_12hz"}')
        (model/'model.safetensors').write_bytes(b'NOT REAL WEIGHTS; missing-dependency gate only')
        for index in range(1,4):
            lib=libraries.create('编码链路实验'+str(index))
            lib=libraries.add(lib['id'],lib['revision'],[('a.wav',wav()),('b.wav',wav(hz=550))])
            data=inputs.prepare(libraries,{'library_id':lib['id'],'revision':lib['revision'],
                'samples':[{'id':s['id'],'text':'人工合成音频格式实验，不是真实人声。'} for s in lib['samples']],
                'reference_sample_id':lib['samples'][0]['id'],'voice_rights_confirmed':True,'single_speaker_confirmed':True})
            def fixture(waveform):return [[0]*16 for _ in range(math.ceil(len(waveform)/1920))]
            out=codes.prepare(inputs,data['id'],data['manifest_sha256'],lambda:fixture)
            assert out['state']=='test_only_codes' and out['checks']['tokenization_executed'] is False
            assert out['schema']==2 and out['provenance_verified_now']
            for name in ('manifest.json','train_raw.jsonl'):
                assert (codes.root/out['id']/'source'/name).read_bytes()==(inputs.root/data['id']/name).read_bytes()
            common=['--state',str(state),'--id',out['id'],'--manifest-sha256',out['manifest_sha256']]
            code,response=cli('verify',*common);assert code==0 and response['result']['integrity_verified_now']
            inputs.delete(data['id'],data['manifest_sha256'])
            code,response=cli('verify',*common);assert code==0
            # A second input is used only for the real CLI dependency gate.
            second=inputs.prepare(libraries,{'library_id':lib['id'],'revision':lib['revision'],
                'samples':[{'id':s['id'],'text':'依赖门禁实验。'} for s in lib['samples']],
                'reference_sample_id':lib['samples'][0]['id'],'voice_rights_confirmed':True,'single_speaker_confirmed':True})
            gate='not_run_dependencies_present'
            if missing:
                code,response=cli('encode','--state',str(state),'--id',second['id'],'--manifest-sha256',second['manifest_sha256'],
                                  '--model-dir',str(model),'--model-sha256',model_fingerprint(model))
                assert code==2 and response['status']=='blocked',response
                gate='blocked_missing_dependencies'
            inputs.delete(second['id'],second['manifest_sha256']);libraries.remove(lib['id'],lib['revision'])
            code,response=cli('verify',*common);assert code==0 and response['result']['provenance_verified_now']
            with codes.lease(out['id'],out['manifest_sha256']):
                code,response=cli('delete',*common);assert code==2 and response['code']==409
                code,response=cli('list','--state',str(state));assert code==0 and not response['result'][0]['provenance_verified_now']
            code,response=cli('hold-read',*common,'--seconds','1','--timeout','10')
            assert code==0 and response['result']['read_lease_completed'] and not response['result']['training_allowed']
            code,response=cli('delete',*common);assert code==0
            code,response=cli('list','--state',str(state));assert code==0 and response['result']==[]
            print(json.dumps({'round':index,'local_cli_storage_passed':True,'fixture_only':True,
                 'independent_after_source_deleted':True,'sealed_provenance':True,'read_lease_delete409':True,'hold_read_completed':True,'real_encode_dependency_gate':gate,
                 'gate_weights_are_fixture_not_real':True,'model_loaded':False,'training_verified':False}),flush=True)
    print('CODES CLI: 3/3 local storage/protocol rounds. Fixture codes ONLY; real Qwen encoding NOT accepted.')


if __name__=='__main__':main()
