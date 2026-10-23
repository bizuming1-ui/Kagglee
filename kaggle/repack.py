#!/usr/bin/env python3
"""Reproducibly repack decoded assets without importing/running the original launcher."""
from __future__ import annotations

import argparse
import ast
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import textwrap
import zlib

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "kaggle/source"
OUTPUT = REPO / "kaggle/kaggle-fixed-step17.py"
MANIFEST = REPO / "kaggle/source_manifest_step17.json"
ORIGINAL_SHA256 = "26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461"
EXTRA_ASSETS = ["go/gateway/reliability_test.go", "go/gateway/security.go", "go/gateway/security_test.go", "py/access_control.py", "py/resource_limits.py", "tools/backend_probe.py", "web/recorder.js", "go/gateway/preflight_test.go", "py/voice_library.py", "py/library_api.py", "py/training_data.py", "py/training_codes.py", "tools/encode_training.py", "py/gpu_ownership.py", "tools/resource_control.py", "py/lora_adapter.py", "py/tts_dataset.py", "py/tts_training.py", "py/training_job.py", "tools/train_tts.py", "LICENSE-QWEN-DERIVED.txt", "py/trained_profiles.py", "py/adapter_engine.py", "tools/trained_voice.py", "py/qwen_compat.py", "py/clone_stream.py", "py/reference_segments.py", "py/voice_binding.py", "tools/voice_benchmark.py", "go/gateway/voice_binding_test.go", "go/gateway/fidelity_test.go"]


def source_assignment(text: str):
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "FILES" for t in node.targets):
            return node, ast.literal_eval(node.value)
    raise ValueError("launcher FILES literal not found")


def safe_name(name: str) -> bool:
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts and "\\" not in name


def render(original: bytes) -> tuple[bytes, bytes]:
    if hashlib.sha256(original).hexdigest() != ORIGINAL_SHA256:
        raise ValueError("unexpected original launcher: refusing to package another revision")
    text = original.decode("utf-8")
    assignment, files = source_assignment(text)
    original_files = {}
    for name, (expected, data) in files.items():
        if not safe_name(name):
            raise ValueError(f"unsafe source path: {name}")
        raw = zlib.decompress(base64.b64decode(data, validate=True))
        digest = hashlib.sha256(raw).hexdigest()
        if not digest.startswith(expected):
            raise ValueError(f"original asset hash mismatch: {name}")
        original_files[name] = digest
    assets = {}
    records = []
    root = SOURCE.resolve()
    for name in sorted(set(files) | set(EXTRA_ASSETS)):
        path = (SOURCE / name).resolve()
        path.relative_to(root)
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assets[name] = (digest, base64.b64encode(zlib.compress(raw, 9)).decode("ascii"))
        records.append({"path": name, "bytes": len(raw), "sha256": digest,
                        "original_sha256": original_files.get(name),
                        "changed": original_files.get(name) != digest})
    lines = ["FILES = {"]
    for name, (digest, data) in assets.items():
        lines.append(f"    {json.dumps(name)}: ({json.dumps(digest)}, (")
        lines.extend("        " + json.dumps(chunk) for chunk in textwrap.wrap(data, 112))
        lines.append("    )),")
    lines.append("}\n")
    source_lines = text.splitlines(keepends=True)
    text = "".join(source_lines[:assignment.lineno-1]) + "\n".join(lines) + "".join(source_lines[assignment.end_lineno:])
    text = "# 第十七阶段增量版；长参考时间戳切分与窗口重识别/16或24秒参考/生成参数绑定/朗读聚合；真实音色零噪声与T4性能待验。原始至step16冻结。\n" + text
    text = text.replace(
        'ROOT = Path("/kaggle/working/qtts") if Path("/kaggle/working").exists() else Path.cwd() / "qtts"',
        'ROOT = Path(os.environ.get("QTTS_ROOT") or (str(Path("/kaggle/working/qtts")) if Path("/kaggle/working").exists() else str(Path.cwd() / "qtts")))',
        1,
    )
    text = text.replace('hashlib.sha256(raw).hexdigest()[:12] != h', 'hashlib.sha256(raw).hexdigest() != h', 1)
    text = text.replace('        p = ROOT / rel',
                        '        if Path(rel).is_absolute() or ".." in Path(rel).parts:\n'
                        '            raise SystemExit("unsafe embedded asset path")\n'
                        '        p = ROOT / rel', 1)
    text = text.replace('\n_unpack()\n', '\n_unpack()\n\nif os.environ.get("QTTS_UNPACK_ONLY") == "1":\n'
                        '    print("仅解包完成；未安装依赖、读取Secrets或启动服务。")\n'
                        '    raise SystemExit(0)\n', 1)
    text = text.replace('"DEEPSEEK_API_KEY", "HF_TOKEN", "KAGGLE_USERNAME", "KAGGLE_KEY"', '"DEEPSEEK_API_KEY", "HF_TOKEN", "KAGGLE_USERNAME", "KAGGLE_KEY", "QTTS_ACCESS_TOKEN"', 1)
    text += '\n# Propagate bootstrap failure instead of merely printing it.\nraise SystemExit(_rc)\n'
    ast.parse(text)
    _, embedded = source_assignment(text)
    for name, (digest, data) in embedded.items():
        raw = zlib.decompress(base64.b64decode(data, validate=True))
        if hashlib.sha256(raw).hexdigest() != digest or raw != (SOURCE / name).read_bytes():
            raise ValueError(f"repacked asset verification failed: {name}")
    output = text.encode("utf-8")
    manifest = {"stage": "step17-long-reference-alignment-context-generation-binding-read-grouping-partial-scope", "original_sha256": ORIGINAL_SHA256,
                "original_assets_verified": len(files), "asset_count": len(records),
                "launcher_sha256": hashlib.sha256(output).hexdigest(), "assets": records}
    return output, (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", type=Path, help="original saved kaggle file; never executed")
    parser.add_argument("--check", action="store_true", help="verify outputs are up to date without writing")
    args = parser.parse_args()
    original = args.original
    if original is None:
        head = json.loads((REPO / "workspace/HEAD.json").read_text())
        original = REPO / "workspace/revisions" / head["revision"] / "kaggle"
    launcher, manifest = render(original.read_bytes())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != launcher or not MANIFEST.exists() or MANIFEST.read_bytes() != manifest:
            raise SystemExit("repacked launcher/manifest is stale; run python kaggle/repack.py")
        print(f"REPACK CHECK OK: original 22 hashes + current {len(json.loads(manifest)['assets'])} assets; deterministic outputs match")
    else:
        OUTPUT.write_bytes(launcher)
        MANIFEST.write_bytes(manifest)
        print(f"wrote {OUTPUT.relative_to(REPO)} ({len(launcher)} bytes), verified {len(json.loads(manifest)['assets'])} assets")


if __name__ == "__main__":
    main()
