"""CPU-only contracts for the complete ASR transcript shown in the simple voice card."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import test_step18_profile_inputs as harness

TARGET = harness.CANDIDATE

class Step18FullTranscriptTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="step18-full-transcript-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.fixtures = []

    def fixture(self, trained=False):
        f = harness.version.VersionFixture(self.root / str(len(self.fixtures)))
        directory, profile = f.profile(trained)
        self.fixtures.append((f, directory, profile))
        return f, directory, profile

    def post(self, f, value, *, raw=None):
        body = raw if raw is not None else json.dumps(value, ensure_ascii=True)
        return f.post("/profiles/voice/transcript", body)

    def test_joins_all_segments_in_source_order_without_inventing_punctuation(self):
        rows = [
            {"f": 1, "start": 0.0, "end": 1.0, "text": "Next file."},
            {"f": 0, "start": 2.0, "end": 3.0, "text": "world!"},
            {"f": 0, "start": 0.0, "end": 1.0, "text": "Hello"},
            {"f": 0, "start": 1.0, "end": 1.5, "text": "again"},
        ]
        self.assertEqual(TARGET.assemble_full_transcript(rows), "Hello again world!\nNext file.")

    def test_assembly_rejects_over_limit_instead_of_silently_truncating(self):
        with self.assertRaisesRegex(ValueError, "未保存，也未截断"):
            TARGET.assemble_full_transcript([{"f": 0, "start": 0, "end": 1, "text": "文" * 100_001}])

    def test_transcript_exact_limit_preserves_unicode_and_does_not_touch_anchor(self):
        f, directory, before = self.fixture()
        text = "😀" * 100_000
        anchor_before = (directory / before["anchor"]).read_bytes()
        payload = json.dumps({"full_transcript": text}, ensure_ascii=False)
        with harness.serve(f):
            response = self.post(f, {}, raw=payload)
            visible = f.client.get("/profiles").json()["profiles"][0]
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json(), {
            "ok": True, "transcript_saved": True, "characters": 100_000,
            "anchor_unchanged": True, "model_prompt_unchanged": True, "worker_reload": False,
        })
        self.assertEqual(visible["full_transcript"], text)
        self.assertEqual(visible["full_transcript_source"], "user_edited_unverified")
        self.assertEqual(visible["ref_text"], before["ref_text"])
        self.assertEqual((directory / before["anchor"]).read_bytes(), anchor_before)
        self.assertEqual(f.worker_calls, [])

    def test_over_limit_and_invalid_transcripts_are_rejected_without_writes(self):
        cases = [
            ({"full_transcript": "😀" * 100_001}, 413),
            ({"full_transcript": "  \n  "}, 400),
            ({"full_transcript": 7}, 400),
            ({"full_transcript": "\ud800"}, 400),
            ({"full_transcript": "text", "extra": True}, 400),
        ]
        for payload, expected in cases:
            with self.subTest(length=len(str(payload))):
                f, directory, _ = self.fixture()
                before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in directory.iterdir() if p.is_file()}
                with harness.serve(f):
                    response = self.post(f, payload)
                self.assertEqual(response.status_code, expected, response.text)
                after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in directory.iterdir() if p.is_file()}
                self.assertEqual(after, before)
                self.assertEqual(f.worker_calls, [])

    def test_duplicate_json_key_is_rejected(self):
        f, directory, _ = self.fixture()
        before = (directory / "profile.json").read_bytes()
        with harness.serve(f):
            response = self.post(f, {}, raw='{"full_transcript":"first","full_transcript":"last"}')
        self.assertEqual(response.status_code, 400)
        self.assertEqual((directory / "profile.json").read_bytes(), before)
        self.assertEqual(f.worker_calls, [])

    def test_trained_profile_can_save_transcript_without_changing_training_reference(self):
        f, directory, before = self.fixture(trained=True)
        with harness.serve(f):
            response = self.post(f, {"full_transcript": "完整源转写。"})
        self.assertEqual(response.status_code, 200, response.text)
        saved = harness.read_json(directory / "profile.json")
        self.assertEqual(saved["full_transcript"], "完整源转写。")
        self.assertEqual(saved["ref_text"], before["ref_text"])
        self.assertEqual(saved["anchor"], before["anchor"])
        self.assertEqual(f.worker_calls, [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
