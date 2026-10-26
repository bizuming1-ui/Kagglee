"""CPU-only source intake tests; no Qwen/ASR/browser/GPU claims."""
import base64
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch
import zlib

SPEC = importlib.util.spec_from_file_location('source_intake', Path(__file__).with_name('source_intake.py'))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def record(raw=b'print("asset is not executed")\n'):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'data': base64.b64encode(zlib.compress(raw)).decode()}


def launcher(records=None, prefix=''):
    return (prefix + '\nFILES = ' + repr(records if records is not None else {'py/a.py': record()}) + '\n').encode()


class IntakeTests(unittest.TestCase):
    def test_literal_only(self):
        data, report = m.inspect_bytes(launcher(prefix='raise RuntimeError("must not execute")'))
        self.assertIn('py/a.py', data)
        self.assertTrue(report['asset_integrity_passed'])
        self.assertFalse(report['release'])
        self.assertFalse(report['complete_source_authenticity_verified'])

    def test_side_effect_not_executed(self):
        with tempfile.TemporaryDirectory() as td:
            marker = Path(td) / 'must-not-exist'
            m.inspect_bytes(launcher(prefix=f'from pathlib import Path\nPath({str(marker)!r}).touch()'))
            self.assertFalse(marker.exists())

    def test_duplicate_files_assignment(self):
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher() + launcher())

    def test_missing_files(self):
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(b'print("hello")')

    def test_files_call_rejected(self):
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(b'FILES = dict()')

    def test_annotation_supported(self):
        source = launcher().replace(b'FILES = ', b'FILES: dict = ')
        self.assertEqual(len(m.inspect_bytes(source)[0]), 1)

    def test_alias_assignment_rejected(self):
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher().replace(b'FILES = ', b'x = FILES = '))

    def test_duplicate_asset_key(self):
        rec = repr(record())
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(f'FILES = {{"a": {rec}, "a": {rec}}}'.encode())

    def test_duplicate_record_field(self):
        rec = repr(record()).replace("'bytes': ", "'bytes': 0, 'bytes': ")
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(f'FILES = {{"a": {rec}}}'.encode())

    def test_unpack_rejected(self):
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(b'FILES = {**{}}')

    def test_unsafe_paths(self):
        for name in ('../escape', '/tmp/escape', 'x/../y', './x', 'a//b', 'a/',
                     'a\\b', 'C:/x', 'a\x00b', 'a\nb', '', '声音.py'):
            with self.subTest(name=name), self.assertRaises(m.IntakeError):
                m.inspect_bytes(launcher({name: record()}))

    def test_file_directory_collision(self):
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': record(), 'a/b': record()}))

    def test_invalid_base64(self):
        rec = record(); rec['data'] = '!!!'
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': rec}))

    def test_wrong_digest(self):
        rec = record(); rec['sha256'] = '0' * 64
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': rec}))

    def test_invalid_digest(self):
        for digest in ('abcd', 'A' * 64, 42):
            rec = record(); rec['sha256'] = digest
            with self.subTest(digest=digest), self.assertRaises(m.IntakeError):
                m.inspect_bytes(launcher({'a': rec}))

    def test_bool_and_negative_sizes(self):
        for size in (True, -1, 1.0, m.MAX_FILE + 1):
            rec = record(); rec['bytes'] = size
            with self.subTest(size=size), self.assertRaises(m.IntakeError):
                m.inspect_bytes(launcher({'a': rec}))

    def test_truncated_compressed_stream(self):
        rec = record(); rec['data'] = base64.b64encode(zlib.compress(b'hello')[:-1]).decode()
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': rec}))

    def test_trailing_compressed_stream(self):
        for suffix in (b'extra', zlib.compress(b'second')):
            rec = record(); rec['data'] = base64.b64encode(zlib.compress(b'hello') + suffix).decode()
            with self.subTest(suffix=suffix), self.assertRaises(m.IntakeError):
                m.inspect_bytes(launcher({'a': rec}))

    def test_decompression_bomb_bound(self):
        rec = record(b'a' * 1000000); rec['bytes'] = 32
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': rec}))

    def test_aggregate_budget(self):
        with patch.object(m, 'MAX_TOTAL', 2), self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': record(b'aa'), 'b': record(b'bb')}))

    def test_asset_count_budget(self):
        with patch.object(m, 'MAX_ASSETS', 1), self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': record(), 'b': record()}))

    def test_input_budget(self):
        with patch.object(m, 'MAX_INPUT', 10), self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher())

    def test_empty_file_asset_valid(self):
        self.assertEqual(m.inspect_bytes(launcher({'a': record(b'')}))[0], {'a': b''})

    def test_extra_record_field(self):
        rec = record(); rec['extra'] = 'not allowed'
        with self.assertRaises(m.IntakeError):
            m.inspect_bytes(launcher({'a': rec}))

    def test_report_deterministic(self):
        self.assertEqual(m.inspect_bytes(launcher()), m.inspect_bytes(launcher()))

    def test_legacy_58_does_not_pass_current_gate(self):
        records = {f'py/a{i}.py': record() for i in range(58)}
        _, report = m.inspect_bytes(launcher(records))
        self.assertFalse(report['matches_known_chat_observations'])
        self.assertIn('asset_count_does_not_match_chat_observation_67', report['observation_mismatches'])

    def test_real_old_bundle_rejected_without_execution(self):
        old = Path(__file__).parent / 'artifacts-startup-return-fix/kaggle-step18-candidate.py'
        _, report = m.inspect_bytes(m.read_source(old))
        self.assertEqual(report['asset_count'], 58)
        self.assertFalse(report['matches_known_chat_observations'])

    def _fixture(self):
        # Synthetic positive contract test: replace observations ONLY inside this
        # context. This does not recreate or authenticate the user's 67 assets.
        records = {f'py/fixture{i}.py': record() for i in range(67)}
        raw = b'print("asset is not executed")\n'
        observed = {'py/fixture0.py': (len(raw), m.sha(raw))}
        return launcher(records), patch.multiple(m, OBSERVED=observed, REQUIRED=set())

    def test_new_extract_and_permissions(self):
        source, observations = self._fixture()
        with observations, tempfile.TemporaryDirectory() as td:
            data, report = m.inspect_bytes(source)
            output = Path(td) / 'new'
            m.extract_new(data, report, output)
            self.assertEqual(len(list((output / 'source/py').glob('*.py'))), 67)
            self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o700)
            self.assertEqual(stat.S_IMODE((output / 'INTAKE.json').stat().st_mode), 0o600)
            for name, raw in data.items():
                self.assertEqual((output / 'source' / name).read_bytes(), raw)
                self.assertEqual(stat.S_IMODE((output / 'source' / name).stat().st_mode), 0o600)

    def test_existing_directory_preserved(self):
        source, observations = self._fixture()
        with observations, tempfile.TemporaryDirectory() as td:
            data, report = m.inspect_bytes(source)
            sentinel = Path(td) / 'old'; sentinel.write_bytes(b'unchanged')
            with self.assertRaises(m.IntakeError):
                m.extract_new(data, report, Path(td))
            self.assertEqual(sentinel.read_bytes(), b'unchanged')

    def test_symlink_parent_rejected(self):
        source, observations = self._fixture()
        with observations, tempfile.TemporaryDirectory() as td:
            data, report = m.inspect_bytes(source)
            link = Path(td) / 'link'; link.symlink_to(td, target_is_directory=True)
            with self.assertRaises(m.IntakeError):
                m.extract_new(data, report, link / 'new')
            self.assertFalse((Path(td) / 'new').exists())

    def test_changed_data_rejected_before_mkdir(self):
        source, observations = self._fixture()
        with observations, tempfile.TemporaryDirectory() as td:
            data, report = m.inspect_bytes(source)
            data['py/fixture0.py'] = b'changed'
            output = Path(td) / 'new'
            with self.assertRaises(m.IntakeError):
                m.extract_new(data, report, output)
            self.assertFalse(output.exists())

    def test_mismatch_rejected_before_mkdir(self):
        with tempfile.TemporaryDirectory() as td:
            data, report = m.inspect_bytes(launcher())
            output = Path(td) / 'new'
            with self.assertRaises(m.IntakeError):
                m.extract_new(data, report, output)
            self.assertFalse(output.exists())

    def test_cli_legacy_exit_two_and_no_extraction(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / 'source.py'; source.write_bytes(launcher())
            with contextlib.redirect_stdout(io.StringIO()) as output:
                code = m.main([str(source)])
            self.assertEqual(code, 2)
            self.assertFalse(json.loads(output.getvalue())['matches_known_chat_observations'])
            self.assertEqual(sorted(p.name for p in Path(td).iterdir()), ['source.py'])

    def test_cli_error_does_not_echo_sensitive_path(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code = m.main(['/missing/private-name-token.py'])
        self.assertEqual(code, 2)
        self.assertNotIn('private-name-token', output.getvalue())

    def test_read_budget(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / 'source.py'; source.write_bytes(b'x' * 11)
            with patch.object(m, 'MAX_INPUT', 10), self.assertRaises(m.IntakeError):
                m.read_source(source)


if __name__ == '__main__':
    unittest.main(verbosity=2)
