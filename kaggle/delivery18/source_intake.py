"""Read-only launcher intake; never imports or executes the supplied launcher.

Default gate checks known chat observations, not complete source authenticity.
Extraction, when requested, only creates a new private directory after ALL checks.
No dependency installation, runtime startup, process management, or network calls.
"""
from __future__ import annotations

import argparse
import ast
import base64
import binascii
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import zlib

MAX_INPUT = 4 * 1024 * 1024
MAX_FILE = 2 * 1024 * 1024
MAX_TOTAL = 16 * 1024 * 1024
MAX_ASSETS = 256
# Observations retained from the pasted code, NOT an independently verified manifest.
OBSERVED = {
    'py/clone_stream.py': (9390, '4d25171cbbfab62b081ccad2cbf1ba807d7c711b1518c91be50deb02eec0efb2'),
    'py/worker.py': (36438, '31e9c1a2aa9e2aa9c7599957a8f8f00ac87891630688122569e019e2887d569e'),
    'web/app.js': (81601, '102caae740a19aeeb5d6ad80005d89e75d1456d39c2fca9097f55226e6d2539d'),
    'py/step18_audio_rt.py': (9167, 'ca134b0788025b48c00ff8441fa9e2b227960bb2ae98c8e23b322f9f92c399d9'),
    'py/step18_trimmer.py': (7013, '762b797128a584e40d3557c2a776b9812770f5e2d94fd8e9468e566830ae9c7e'),
}
REQUIRED = {
    'py/diagnostic_audio.py', 'py/diagnostic_pair.py',
    'py/diagnostic_store.py', 'py/diagnostic_training.py',
    'py/notebook_monitor.py', 'py/private_entry.py',
}
HISTORICAL_LAUNCHER_SHA = '0129f9e683ae5764e9c6863b8086fe95c9d14e10960b6a5ea9ac1d417966e297'


class IntakeError(ValueError):
    """Rejected before execution or extraction."""


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _literal_dict(node):
    if not isinstance(node, ast.Dict):
        raise IntakeError('FILES and its records must be literal dictionaries')
    names = []
    for key in node.keys:
        if not isinstance(key, ast.Constant) or type(key.value) is not str:
            raise IntakeError('nonliteral/dynamic dictionary key')
        names.append(key.value)
    if len(names) != len(set(names)):
        raise IntakeError('duplicate dictionary key')
    return names


def _path(name):
    p = PurePosixPath(name)
    if (not name or not name.isascii() or '\\' in name or ':' in name
            or any(ord(c) < 32 or ord(c) == 127 for c in name)
            or p.is_absolute() or any(s in ('', '.', '..') for s in name.split('/'))
            or len(name) > 240):
        raise IntakeError('unsafe asset path')
    return p


def _decode(record):
    if type(record) is not dict or set(record) != {'bytes', 'sha256', 'data'}:
        raise IntakeError('invalid asset record schema')
    n, digest, payload = record['bytes'], record['sha256'], record['data']
    if type(n) is not int or not 0 <= n <= MAX_FILE:
        raise IntakeError('invalid asset byte budget')
    if type(digest) is not str or not re.fullmatch(r'[0-9a-f]{64}', digest):
        raise IntakeError('invalid asset SHA256')
    if type(payload) is not str or len(payload) > MAX_INPUT:
        raise IntakeError('invalid base64 payload')
    try:
        compressed = base64.b64decode(payload, validate=True)
        decoder = zlib.decompressobj()
        # Limit output BEFORE materializing a potentially compressed bomb.
        raw = decoder.decompress(compressed, n + 1)
        if (len(raw) != n or not decoder.eof or decoder.unused_data
                or decoder.unconsumed_tail):
            raise IntakeError('size mismatch, incomplete zlib, or trailing data')
    except (ValueError, binascii.Error, zlib.error) as exc:
        if isinstance(exc, IntakeError):
            raise
        raise IntakeError('invalid compressed payload') from None
    if sha(raw) != digest:
        raise IntakeError('asset SHA256 mismatch')
    return raw


def inspect_bytes(source):
    if not source or len(source) > MAX_INPUT:
        raise IntakeError('launcher input budget exceeded or empty')
    try:
        tree = ast.parse(source)
    except (SyntaxError, ValueError, RecursionError):
        raise IntakeError('launcher does not parse') from None
    assignments = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id == 'FILES' for t in node.targets):
                if len(node.targets) != 1:
                    raise IntakeError('ambiguous FILES assignment')
                assignments.append(node.value)
        elif (isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
              and node.target.id == 'FILES'):
            assignments.append(node.value)
    if len(assignments) != 1:
        raise IntakeError('expected one top-level literal FILES assignment')
    literal = assignments[0]
    names = _literal_dict(literal)
    if not 1 <= len(names) <= MAX_ASSETS:
        raise IntakeError('asset count budget exceeded or empty')
    for name in names:
        p = _path(name)
        if any(str(parent) in names for parent in p.parents if str(parent) != '.'):
            raise IntakeError('asset file/directory collision')
    for record_node in literal.values:
        _literal_dict(record_node)
    try:
        records = ast.literal_eval(literal)
    except (ValueError, TypeError, RecursionError):
        raise IntakeError('FILES is not a safe literal') from None
    # Reject aggregate claimed sizes before decompression.
    sizes = [r.get('bytes') for r in records.values()]
    if any(type(n) is not int or not 0 <= n <= MAX_FILE for n in sizes):
        raise IntakeError('invalid asset byte budget')
    if sum(sizes) > MAX_TOTAL:
        raise IntakeError('aggregate asset budget exceeded')
    data = {name: _decode(record) for name, record in records.items()}
    manifest = {name: {'bytes': len(raw), 'sha256': sha(raw)}
                for name, raw in sorted(data.items())}
    issues = []
    if len(data) != 67:
        issues.append('asset_count_does_not_match_chat_observation_67')
    for name, (size, digest) in OBSERVED.items():
        if manifest.get(name) != {'bytes': size, 'sha256': digest}:
            issues.append('observed_asset_missing_or_different:' + name)
    for name in sorted(REQUIRED - data.keys()):
        issues.append('observed_feature_module_missing:' + name)
    report = {
        'schema': 'source-intake-v1',
        'launcher_sha256': sha(source), 'launcher_bytes': len(source),
        'historical_0129_launcher_match': sha(source) == HISTORICAL_LAUNCHER_SHA,
        'asset_count': len(data), 'decoded_bytes': sum(map(len, data.values())),
        'asset_manifest_sha256': sha(json.dumps(manifest, sort_keys=True,
                                              separators=(',', ':')).encode()),
        'asset_integrity_passed': True,
        'matches_known_chat_observations': not issues,
        'observation_mismatches': issues,
        'assets': manifest,
        'scope': 'literal FILES snapshot only; launcher is not executed',
        'complete_source_authenticity_verified': False,
        'full_system_tested': False, 'real_model_tested': False,
        'physical_dual_gpu_verified': False, 'audio_quality_verified': False,
        'release': False,
    }
    return data, report


def read_source(path):
    # Avoid an unbounded read even if an unexpected large file is supplied.
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_INPUT + 1)
    if len(raw) > MAX_INPUT:
        raise IntakeError('launcher input budget exceeded')
    return raw


def extract_new(data, report, output):
    """New private directory only; preserve input source asset bytes exactly."""
    if not report['matches_known_chat_observations']:
        raise IntakeError('not extracting a candidate that mismatches known observations')
    # Recheck the report/data contract before touching disk.
    expected = report['assets']
    if set(data) != set(expected):
        raise IntakeError('extraction asset set mismatch')
    for name, raw in data.items():
        _path(name)
        if expected[name] != {'bytes': len(raw), 'sha256': sha(raw)}:
            raise IntakeError('extraction data changed after inspection')
    target = Path(output).absolute()
    # Refuse symlink parents rather than accidentally writing into another tree.
    for parent in [target.parent, *target.parent.parents]:
        if parent.is_symlink():
            raise IntakeError('symlink output parent')
    if not target.parent.is_dir():
        raise IntakeError('output parent must already exist')
    try:
        target.mkdir(mode=0o700)  # no exist_ok: existing dir/files/symlinks fail
    except FileExistsError:
        raise IntakeError('output already exists; refusing overwrite') from None
    source_root = target / 'source'
    source_root.mkdir(mode=0o700)
    for name, raw in sorted(data.items()):
        p = source_root / name
        p.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        with p.open('xb') as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(raw)
    with (target / 'INTAKE.json').open('x', encoding='utf-8') as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump(report, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('launcher', type=Path)
    parser.add_argument('--extract-new', type=Path)
    args = parser.parse_args(argv)
    try:
        data, report = inspect_bytes(read_source(args.launcher))
        if args.extract_new:
            extract_new(data, report, args.extract_new)
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
        return 0 if report['matches_known_chat_observations'] else 2
    except (IntakeError, OSError) as exc:
        # Do not echo exception text: paths/payload fragments may contain secrets.
        message = str(exc) if isinstance(exc, IntakeError) else 'file operation failed'
        print(json.dumps({'error': message, 'release': False}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
