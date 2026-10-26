# Mechanism: mechanism-shape
"""Public-CLI tests of evidence validation, separate from reader accuracy."""

import json
from copy import deepcopy
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("replay.py")


class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.dataset = {
            "rule": "Register a recognised rule failure and prepare a repair.",
            "cases": [{"id": "case-a", "conversation": "The rule was not followed.",
                       "work": "No registration or repair was prepared.",
                       "stop_hook_active": False}],
        }

    def run_cli(self, command, reviews=None):
        cases_path = self.root / "cases.json"
        cases_path.write_text(json.dumps(self.dataset), encoding="utf-8")
        arguments = [sys.executable, str(SCRIPT), command, str(cases_path)]
        if reviews is not None:
            reviews_path = self.root / "reviews.json"
            reviews_path.write_text(reviews if isinstance(reviews, str) else json.dumps(reviews),
                                    encoding="utf-8")
            arguments.append(str(reviews_path))
        return subprocess.run(arguments, capture_output=True, text=True, encoding="utf-8")

    def review(self, verdict="return"):
        packet = self.run_cli("packet")
        self.assertEqual(packet.returncode, 0, packet.stderr)
        case = json.loads(packet.stdout)["cases"][0]
        return {"case_id": case["id"], "case_sha256": case["sha256"],
                "verdict": verdict, "reason": "A required repair remains unfinished.",
                "evidence": [{"source": source, "quote": text}
                             for source, text in case["sources"].items()]}

    def test_supported_return_previews_a_stop_block(self):
        result = self.run_cli("evaluate", [self.review()])
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)[0]
        self.assertEqual(report["status"], "return")
        self.assertEqual(report["stop_preview"]["decision"], "block")
        self.assertEqual(report["stop_preview"]["reason"], "A required repair remains unfinished.")

    def test_legitimate_stop_has_empty_preview(self):
        result = self.run_cli("evaluate", [self.review("allow")])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)[0]["stop_preview"], {})

    def test_unknown_has_no_hook_preview(self):
        result = self.run_cli("evaluate", [self.review("unknown")])
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)[0]
        self.assertEqual(report["status"], "unknown")
        self.assertIsNone(report["stop_preview"])

    def test_already_continued_turn_cannot_request_another_retry(self):
        self.dataset["cases"][0]["stop_hook_active"] = True
        result = self.run_cli("evaluate", [self.review()])
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)[0]
        self.assertEqual(report["status"], "limit_reached")
        self.assertIsNone(report["stop_preview"])

    def test_invalid_readings_produce_no_decision(self):
        original = self.review()
        variants = []
        for key, value in (("case_sha256", "0" * 64), ("case_id", "other"),
                           ("verdict", "probably"), ("reason", " ")):
            review = deepcopy(original)
            review[key] = value
            variants.append([review])
        fabricated = deepcopy(original)
        fabricated["evidence"][0]["quote"] = "This source never said this."
        variants.append([fabricated])
        incomplete = deepcopy(original)
        incomplete["evidence"] = [item for item in incomplete["evidence"]
                                  if item["source"] != "work"]
        variants.extend(([incomplete], [], [original, original]))
        for reviews in variants:
            with self.subTest(reviews=reviews):
                result = self.run_cli("evaluate", reviews)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("replay:", result.stderr)

    def test_changed_case_invalidates_a_saved_reading(self):
        review = self.review()
        self.dataset["cases"][0]["work"] += " Registration has now been completed."
        result = self.run_cli("evaluate", [review])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("different case version", result.stderr)

    def test_reviews_match_by_identity_and_validate_before_any_output(self):
        second = deepcopy(self.dataset["cases"][0])
        second["id"] = "case-b"
        self.dataset["cases"].append(second)
        packet = json.loads(self.run_cli("packet").stdout)
        first_review = self.review()
        second_review = deepcopy(first_review)
        second_review.update(case_id="case-b", case_sha256=packet["cases"][1]["sha256"],
                             verdict="allow")
        result = self.run_cli("evaluate", [second_review, first_review])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([(item["case_id"], item["status"]) for item in json.loads(result.stdout)],
                         [("case-a", "return"), ("case-b", "allow")])
        second_review["reason"] = ""
        result = self.run_cli("evaluate", [first_review, second_review])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_empty_duplicate_or_untyped_cases_produce_no_packet(self):
        original = deepcopy(self.dataset)
        variants = []
        empty = deepcopy(original)
        empty["cases"] = []
        variants.append(empty)
        duplicate = deepcopy(original)
        duplicate["cases"].append(deepcopy(duplicate["cases"][0]))
        variants.append(duplicate)
        wrong_flag = deepcopy(original)
        wrong_flag["cases"][0]["stop_hook_active"] = "false"
        variants.append(wrong_flag)
        for dataset in variants:
            with self.subTest(dataset=dataset):
                self.dataset = dataset
                result = self.run_cli("packet")
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")

    def test_duplicate_json_fields_cannot_replace_a_return_with_allow(self):
        raw = json.dumps([self.review()]).replace('"verdict": "return"',
                                                '"verdict": "return", "verdict": "allow"')
        result = self.run_cli("evaluate", raw)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("duplicate JSON field", result.stderr)

    def test_non_json_constants_are_rejected_even_in_ignored_fields(self):
        review = self.review("allow")
        for value in (float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                review["extra"] = {"nested": value}
                result = self.run_cli("evaluate", json.dumps([review]))
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("invalid JSON constant", result.stderr)


if __name__ == "__main__":
    unittest.main()
