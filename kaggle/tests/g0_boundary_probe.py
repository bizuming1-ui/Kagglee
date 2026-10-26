"""G0 malformed local Base/restore counterexamples. CPU/local synthetic files only.
Captures existing defects, NOT a post-fix regression or model/training experiment.
"""
from pathlib import Path
import argparse
import hashlib
import io
import json
import os
import sys
import tarfile
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]

def archive(entries):
    body = io.BytesIO()
    with tarfile.open(fileobj=body, mode='w') as output:
        for name, content in entries:
            member = tarfile.TarInfo(name)
            member.size = len(content)
            output.addfile(member, io.BytesIO(content))
    body.seek(0)
    return tarfile.open(fileobj=body)

def base_tree(path, talker):
    path.mkdir()
    (path / 'speech_tokenizer').mkdir()
    files = {
        'config.json': {'model_type': 'qwen3_tts', 'tts_model_type': 'base',
                        'tts_model_size': '1b7', 'talker_config': talker},
        'generation_config.json': {}, 'tokenizer_config.json': {},
        'speech_tokenizer/config.json': {},
    }
    for name, content in files.items():
        (path / name).write_text(json.dumps(content))
    (path / 'model.safetensors').write_bytes(b'NOT REAL WEIGHTS; only file-tree fingerprint fixture')
    return path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--round', type=int, choices=(1, 2, 3), required=True)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='qtts-g0-boundary-') as temporary:
        state = Path(temporary)
        os.environ.update(QTTS_STATE=str(state / 'state'), QTTS_MOCK='1')
        sys.path.insert(0, str(ROOT / 'kaggle/source/py'))
        import persist
        import training_job as job
        from resource_limits import UploadRejected
        cases = []
        good = base_tree(state / 'good', {'num_code_groups': 16})
        digest = job.base_fingerprint(good)
        assert digest == job.base_fingerprint(good) and len(digest) == 64
        cases.append({'id': 'G0-B01', 'case': 'valid-synthetic-base-fingerprint', 'weights_loaded': False})
        for number, shape in enumerate((None, [], 'invalid'), 2):
            directory = base_tree(state / f'malformed-{number}', shape)
            try:
                job.base_fingerprint(directory)
            except AttributeError:
                cases.append({'id': f'G0-B{number:02}', 'case': 'malformed-talker-config',
                              'shape': type(shape).__name__, 'observed': 'uncaught AttributeError',
                              'controlled_rejection': False, 'classification': 'confirmed-local-input-error-contract'})
            else:
                raise AssertionError('baseline malformed-config behavior changed')
        bad = base_tree(state / 'remote', {'num_code_groups': 16})
        (bad / 'tokenizer_config.json').write_text('{"auto_map":{}}')
        try:
            job.base_fingerprint(bad)
        except UploadRejected as error:
            assert error.code == 400
        else:
            raise AssertionError('remote-code metadata accepted')
        cases.append({'id': 'G0-B05', 'case': 'remote-code-metadata-rejected', 'code': 400})
        target = state / 'atomic.json'
        target.write_text('{"old":true}')
        try:
            job.write_json(target, {'bad': float('nan')})
        except ValueError:
            pass
        else:
            raise AssertionError('NaN accepted')
        assert target.read_text() == '{"old":true}'
        cases.append({'id': 'G0-B06', 'case': 'nan-write-preserves-old-json'})
        destination = state / 'reject-scope'
        destination.mkdir()
        with archive([('active.json', b'new'), ('unexpected.py', b'unsafe')]) as stream:
            try:
                persist.extract_state_members(stream, destination)
            except ValueError:
                pass
            else:
                raise AssertionError('archive scope accepted')
        assert not list(destination.iterdir())
        cases.append({'id': 'G0-B07', 'case': 'bad-archive-member-prevalidates-before-writes'})
        destination = state / 'partial-restore'
        profile = destination / 'profiles/voice/profile.json'
        profile.parent.mkdir(parents=True)
        profile.write_bytes(b'old-profile')
        active = destination / 'active.json'
        active.write_bytes(b'old-active')
        real_replace = os.replace
        def fail_active(source, target):
            if Path(target) == active:
                raise OSError('injected local I/O failure on second member')
            return real_replace(source, target)
        with archive([('profiles/voice/profile.json', b'new-profile'), ('active.json', b'new-active')]) as stream:
            with patch.object(os, 'replace', side_effect=fail_active):
                try:
                    persist.extract_state_members(stream, destination)
                except OSError:
                    pass
                else:
                    raise AssertionError('fault injection did not execute')
        assert profile.read_bytes() == b'new-profile' and active.read_bytes() == b'old-active'
        assert set(p.name for p in profile.parent.iterdir()) == {'profile.json'}
        cases.append({'id': 'G0-B08', 'case': 'restore-second-member-io-failure',
                      'fault_injected': True, 'first_member_changed': True, 'second_member_unchanged': True,
                      'archive_wide_transactional': False, 'classification': 'restore-consistency-design-gap',
                      'note': 'Single-file atomic replace is not archive-wide rollback; no production I/O failure or audible impact proved.'})
        profiles = state / 'pack-profiles'
        (profiles / 'voice').mkdir(parents=True)
        (profiles / 'voice/anchor.wav').write_bytes(b'synthetic-not-real-wave')
        (profiles / '_cal_voice').mkdir()
        (profiles / '_cal_voice/private').write_bytes(b'excluded')
        pack_state = state / 'pack-state'
        for name in ('training_data', 'training_codes', 'training_runs', 'libraries'):
            (pack_state / name).mkdir(parents=True)
            (pack_state / name / 'private').write_bytes(b'excluded')
        with patch.object(persist, 'PROFILES_DIR', profiles), patch.object(persist, 'STATE', pack_state):
            packed = persist._pack(state / 'snapshot.tar.gz')
        with tarfile.open(packed) as stream:
            names = stream.getnames()
        assert 'profiles/voice/anchor.wav' in names
        assert not any('_cal_' in name or name.split('/')[0] in ('training_data', 'training_codes', 'training_runs', 'libraries') for name in names)
        cases.append({'id': 'G0-B09', 'case': 'snapshot-excludes-unrelated-private-training-and-library-directories',
                      'network_called': False, 'note': 'Profile anchors intentionally remain in the explicitly configured state snapshot.'})
        known_secrets = ('QTTS_ACCESS_TOKEN', 'DEEPSEEK_API_KEY', 'HF_TOKEN',
                         'HUGGING_FACE_HUB_TOKEN', 'KAGGLE_USERNAME', 'KAGGLE_KEY', 'PYTHONPATH')
        with patch.dict(os.environ, {**{name: 'synthetic-only' for name in known_secrets}, 'CUDA_VISIBLE_DEVICES': '2,3'}):
            env = job.child_environment(SimpleNamespace(export=lambda: {'QTTS_GPU_LEASE_FD': '30', 'QTTS_GPU_LEASE_NONCE': 'synthetic'}), 31)
        assert not any(name in env for name in known_secrets)
        assert env['CUDA_VISIBLE_DEVICES'] == '2,3' and env[job.CODE_FD] == '31'
        assert env['HF_HUB_OFFLINE'] == env['TRANSFORMERS_OFFLINE'] == '1'
        cases.append({'id': 'G0-B10', 'case': 'training-child-known-secret-scrub-and-offline-policy',
                      'scope': 'enumerated keys only; not proof that every possible credential alias is scrubbed'})
        assert len(cases) == 10
        source_names = ('training_job.py', 'gpu_ownership.py', 'persist.py', 'access_control.py', 'resource_limits.py', 'qtts_common.py')
        receipt = {
            'round': args.round, 'experiment_completed': True, 'cases': cases,
            'source_hashes': {f'kaggle/source/py/{name}': hashlib.sha256((ROOT / 'kaggle/source/py' / name).read_bytes()).hexdigest() for name in source_names},
            'probe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'gpu_executed': False, 'actual_training_executed': False, 'weights_loaded': False,
            'network_called': False, 'real_voice_executed': False, 'product_modified': False,
        }
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
