# Mechanism: mechanism-shape
"""A noticed failure survives preparation of its remedy without changing its evidence."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "capture.py"
sys.path.insert(0, str(SCRIPT.parent))
import amendment


def failure():
    return {
        "session": "observing-session",
        "message": {"role": "user", "content": "Tell me what the study found."},
        "context": [{"role": "assistant", "content": "I am reading the study."},
                    {"role": "tool", "content": "The study found eight families."}],
        "loaded": [{"path": ".agents/skills/discover/SKILL.md", "text": "An uncommitted loaded instruction.\nTell the findings."}],
        "observed": "Here is my decision.",
        "expected": "Report the findings before proposing a decision.",
        "rules": ["discover: report the returned material"],
        "register": "docs/rule-failures.md#the-findings-were-omitted",
        "limitations": [],
    }


class CaptureCLI(unittest.TestCase):
    def run_capture(self, source, output):
        return subprocess.run([sys.executable, str(SCRIPT), "--capture", str(source), "--output", str(output)],
                              capture_output=True, text=True, encoding="utf-8")

    def test_the_loaded_text_and_ordered_context_survive_without_an_amendment(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = failure()
            instruction = root / "loaded.md"
            instruction.write_text(draft["loaded"][0]["text"], encoding="utf-8")
            draft["loaded"][0]["path"] = str(instruction)
            instruction.write_text("Changed after the failing turn.", encoding="utf-8")
            source = root / "draft.json"
            source.write_text(json.dumps(draft), encoding="utf-8")
            output = root / "case" / "failure.json"
            result = self.run_capture(source, output)
            self.assertEqual(0, result.returncode, result.stderr)
            saved = json.loads(output.read_text(encoding="utf-8"))
            for key, value in draft.items():
                self.assertEqual(value, saved[key])
            self.assertEqual("failure-capture-1", saved["format"])
            self.assertEqual(64, len(saved["sha256"]))
            self.assertNotIn("amended", saved)
            self.assertNotIn("verdict", saved)
            checked = subprocess.run([sys.executable, str(SCRIPT), "--check", str(root)],
                                     capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(0, checked.returncode, checked.stderr)
            self.assertEqual({"checked": 1, "diagnostics": []}, json.loads(checked.stdout))

    def test_missing_instruction_contents_and_unlabelled_messages_are_refused_before_writing(self):
        for field in ("snapshot", "role", "empty_expected", "future_verdict"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                draft = failure()
                if field == "snapshot":
                    draft["loaded"][0].pop("text")
                elif field == "role":
                    draft["context"][0].pop("role")
                elif field == "empty_expected":
                    draft["expected"] = " "
                else:
                    draft["verdict"] = "helped"
                source = root / "draft.json"
                source.write_text(json.dumps(draft), encoding="utf-8")
                output = root / "new-folder" / "failure.json"
                result = self.run_capture(source, output)
                self.assertNotEqual(0, result.returncode)
                self.assertFalse(output.parent.exists())

    def test_unavailable_or_reconstructed_evidence_is_explicitly_labelled(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = failure()
            draft["loaded"][0]["text"] = None
            draft["limitations"] = [
                {"field": "/loaded/0/text", "kind": "missing", "reason": "The earlier loaded text is unavailable."},
                {"field": "/message/content", "kind": "reconstructed", "reason": "Only a contemporary summary survived."},
            ]
            source = root / "draft.json"
            source.write_text(json.dumps(draft), encoding="utf-8")
            output = root / "failure.json"
            result = self.run_capture(source, output)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIsNone(json.loads(output.read_text(encoding="utf-8"))["loaded"][0]["text"])
            for labels in ([], [{"field": "/loaded/0/text", "kind": "missing", "reason": " "}],
                           [{"field": "/not-a-field", "kind": "missing", "reason": "Unavailable."}]):
                draft["limitations"] = labels
                source.write_text(json.dumps(draft), encoding="utf-8")
                refused = root / "refused.json"
                result = self.run_capture(source, refused)
                self.assertNotEqual(0, result.returncode)
                self.assertFalse(refused.exists())

    def test_ambiguous_json_is_refused_instead_of_silently_replacing_evidence(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "draft.json"
            raw = json.dumps(failure())
            source.write_text(raw[:-1] + ', "observed":"a replacement"}', encoding="utf-8")
            output = root / "failure.json"
            result = self.run_capture(source, output)
            self.assertNotEqual(0, result.returncode)
            self.assertIn("duplicate", result.stderr)
            self.assertFalse(output.exists())

    def test_existing_evidence_is_not_overwritten_and_corruption_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "draft.json"
            source.write_text(json.dumps(failure()), encoding="utf-8")
            output = root / "case" / "failure.json"
            self.assertEqual(0, self.run_capture(source, output).returncode)
            before = output.read_bytes()
            self.assertNotEqual(0, self.run_capture(source, output).returncode)
            self.assertEqual(before, output.read_bytes())
            changed = json.loads(before)
            changed["observed"] = "A different answer."
            output.write_text(json.dumps(changed), encoding="utf-8")
            checked = subprocess.run([sys.executable, str(SCRIPT), "--check", str(root)],
                                     capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(0, checked.returncode)
            self.assertIn("digest", json.loads(checked.stdout)["diagnostics"][0]["error"])

    def test_an_observation_cannot_be_mistaken_for_a_prepared_experiment(self):
        class NoModelCall:
            def run(self, directory):
                raise AssertionError("an observation must not start a model call")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = root / "draft.json"
            draft.write_text(json.dumps(failure()), encoding="utf-8")
            observed = root / "failure.json"
            self.assertEqual(0, self.run_capture(draft, observed).returncode)
            with self.assertRaisesRegex(ValueError, "prepare.*experiment"):
                amendment.run_case(observed, root / "output", NoModelCall())
            self.assertFalse((root / "output").exists())

    def test_a_valid_digest_does_not_make_an_invalid_capture_time_admissible(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            draft = root / "draft.json"
            draft.write_text(json.dumps(failure()), encoding="utf-8")
            output = root / "failure.json"
            self.assertEqual(0, self.run_capture(draft, output).returncode)
            record = json.loads(output.read_text(encoding="utf-8"))
            for invalid in (123, "not a time", "2026-10-26T12:00:00", "2026-10-26T12:00:00+03:00"):
                record["captured_at"] = invalid
                record.pop("sha256")
                record["sha256"] = hashlib.sha256(json.dumps(record, ensure_ascii=False, sort_keys=True,
                                                           separators=(",", ":")).encode("utf-8")).hexdigest()
                output.write_text(json.dumps(record), encoding="utf-8")
                checked = subprocess.run([sys.executable, str(SCRIPT), "--check", str(root)],
                                         capture_output=True, text=True, encoding="utf-8")
                self.assertNotEqual(0, checked.returncode, invalid)
                self.assertIn("UTC", json.loads(checked.stdout)["diagnostics"][0]["error"])


if __name__ == "__main__":
    unittest.main()
