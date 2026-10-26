# Mechanism: mechanism-shape
"""The experiment preserves the boundaries between a case, an execution and its judge."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
import threading
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import amendment


def specimen():
    return {
        "common": "Shared instructions.",
        "standing": "Before.\n\n**Put the material into the work as it came back.** File it.\n\n## Next\nFinish.",
        "amended": "Before.\n\n**Put the material into the work as it came back.** File it and tell the person.\n\n## Next\nFinish.",
        "paragraph": "**Put the material into the work as it came back.**",
        "situation": "The study has just returned.",
        "discovery": "The original material.",
        "message": "Continue.",
        "questions": [{"id": "material", "question": "PRIVATE-RUBRIC-921"}],
        "calibration": [],
        "health": "Return the user's marker exactly.",
        "provenance": {"source": "PRIVATE-CASE-PATH-729"},
    }


def text_catalog(model="model"):
    return {"models": [{"slug": model, "input_modalities": ["text"], "apply_patch_tool_type": None,
                        "experimental_supported_tools": []}]}


class TextHost:
    """An external host boundary; its judgements inspect the response, not condition labels."""

    def run(self, directory):
        prompt = (directory / "prompt.txt").read_text(encoding="utf-8")
        instructions = (directory / "AGENTS.md").read_text(encoding="utf-8")
        if prompt.startswith("{"):
            value = json.loads(prompt)
            if "outside_file" in value:
                text = json.dumps({"marker": instructions.split("Marker: ")[-1].strip(), "outside": None})
            else:
                yes = "included" in value["response"]
                text = json.dumps({"answers": [{"id": q["id"], "yes": yes,
                                                "quotes": [value["response"]] if yes else [],
                                                "evidence": "The material is present." if yes else "The material is absent."}
                                               for q in value["questions"]]})
        elif len(prompt) == 32 and all(ch in "0123456789abcdef" for ch in prompt):
            text = prompt
        else:
            text = "material included" if "tell the person" in instructions else "material omitted"
        return {"status": "ok", "text": text, "usage": {"input_tokens": 2, "output_tokens": 1},
                "duration_s": 0.1, "model": "same-model", "denied_image_read": True}


def calibrated_specimen():
    case = specimen()
    case["judge"] = "Judge the response."
    case["calibration"] = [
        {"question_id": "material", "response": "material included", "expected": True},
        {"question_id": "material", "response": "material omitted", "expected": False},
    ]
    return case


class StagingTests(unittest.TestCase):
    def test_no_instruction_removes_only_the_target_paragraph(self):
        with tempfile.TemporaryDirectory() as folder:
            prepared = amendment.prepare_execution(specimen(), Path(folder) / "anonymous", "none")
            instruction = (prepared / "AGENTS.md").read_text(encoding="utf-8")
            self.assertEqual("Shared instructions.\n\nBefore.\n\n## Next\nFinish.", instruction)

    def test_executor_inputs_keep_the_rubric_and_source_location_private(self):
        with tempfile.TemporaryDirectory() as folder:
            prepared = amendment.prepare_execution(specimen(), Path(folder) / "anonymous", "standing")
            files = sorted(path.name for path in prepared.iterdir())
            self.assertEqual(["AGENTS.md", "prompt.txt"], files)
            text = "\n".join(path.read_text(encoding="utf-8") for path in prepared.iterdir())
            self.assertIn("Shared instructions.", text)
            self.assertIn("The original material.", text)
            self.assertNotIn("PRIVATE-RUBRIC", text)
            self.assertNotIn("PRIVATE-CASE-PATH", text)
            self.assertNotIn("tell the person", text)


class ExperimentTests(unittest.TestCase):
    def test_a_host_with_shared_startup_state_is_not_started_concurrently(self):
        class SharedStartup(TextHost):
            active = 0
            lock = threading.Lock()

            def run(self, directory):
                with self.lock:
                    self.active += 1
                    overlap = self.active > 1
                try:
                    time.sleep(0.01)
                    if overlap:
                        raise OSError("shared startup directory is busy")
                    return super().run(directory)
                finally:
                    with self.lock:
                        self.active -= 1

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", SharedStartup())
            self.assertEqual("complete", report["status"])
            self.assertEqual(9, report["accounting"]["by_purpose"]["execution"])

    def test_an_external_canary_read_fails_preflight(self):
        class Leaking(TextHost):
            def run(self, directory):
                result = super().run(directory)
                prompt = json.loads((directory / "prompt.txt").read_text(encoding="utf-8"))
                if "outside_file" in prompt:
                    value = json.loads(result["text"])
                    value["outside"] = Path(prompt["outside_file"]).read_bytes().hex()
                    result["text"] = json.dumps(value)
                return result

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", Leaking())
            self.assertEqual("preflight_failed", report["status"])
            self.assertEqual(1, len(report["calls"]))

    def test_a_judgement_without_an_explanation_is_invalid(self):
        class Unsupported(TextHost):
            def run(self, directory):
                result = super().run(directory)
                prompt = json.loads((directory / "prompt.txt").read_text(encoding="utf-8"))
                if "questions" in prompt:
                    answers = json.loads(result["text"])
                    for answer in answers["answers"]:
                        answer.pop("evidence")
                    result["text"] = json.dumps(answers)
                return result

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", Unsupported())
            self.assertEqual("calibration_failed", report["status"])
            self.assertIn("evidence statement", report["calibration"][0]["error"])

    def test_echoing_only_the_user_prompt_does_not_prove_loaded_instructions(self):
        class Echo:
            def run(self, directory):
                return {"status": "ok", "text": (directory / "prompt.txt").read_text(encoding="utf-8"), "usage": {}}

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", Echo())
            self.assertEqual("preflight_failed", report["status"])
            self.assertEqual(1, len(report["calls"]))

    def test_executor_exception_leaves_an_incomplete_report_without_a_model_verdict(self):
        class Faulting(TextHost):
            def run(self, directory):
                instructions = (directory / "AGENTS.md").read_text(encoding="utf-8")
                if "tell the person" in instructions:
                    raise OSError("host unavailable")
                return super().run(directory)

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", Faulting())
            self.assertEqual("incomplete", report["status"])
            self.assertIsNone(report["verdict"])
            self.assertEqual(0, report["counts"]["amended"]["valid"])

    def test_failed_main_judgements_leave_zero_denominators_and_no_verdict(self):
        class BrokenAfterCalibration(TextHost):
            count = 0

            def run(self, directory):
                self.count += 1
                result = super().run(directory)
                if self.count > 3 and (directory / "prompt.txt").read_text(encoding="utf-8").startswith("{"):
                    result["text"] = "not a judgement"
                return result

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", BrokenAfterCalibration())
            self.assertEqual("incomplete", report["status"])
            self.assertIsNone(report["verdict"])
            self.assertEqual([0, 0, 0], [c["valid"] for c in report["counts"].values()])
            self.assertEqual(21, report["accounting"]["actual_calls"])

    def test_existing_results_are_not_replaced(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            output = root / "results"
            output.mkdir()
            marker = output / "keep.txt"
            marker.write_text("original", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                amendment.run_case(source, output, TextHost())
            self.assertEqual("original", marker.read_text(encoding="utf-8"))
            self.assertEqual([marker], list(output.iterdir()))

    def test_unquoted_yes_is_not_scored_as_instruction_failure(self):
        class LyingJudge(TextHost):
            def run(self, directory):
                result = super().run(directory)
                prompt = (directory / "prompt.txt").read_text(encoding="utf-8")
                if prompt.startswith("{") and len(json.loads(prompt).get("questions", [])) == 1:
                    result["text"] = json.dumps({"answers": [{"id": "material", "yes": True, "quotes": ["invented"], "evidence": "Claimed quote."}]})
                return result

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", LyingJudge())
            self.assertEqual("calibration_failed", report["status"])
            self.assertEqual("grading_error", report["calibration"][0]["status"])
            self.assertIn("quotation", report["calibration"][0]["error"])
            self.assertIsNone(report["verdict"])

    def test_changes_outside_the_amendment_are_confounded_before_execution(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            case = calibrated_specimen()
            case["amended"] = case["amended"].replace("Before.", "Unrelated change.")
            source = root / "case.json"
            source.write_text(json.dumps(case), encoding="utf-8")
            report = amendment.run_case(source, root / "results", TextHost())
            self.assertEqual("confounded", report["verdict"])
            self.assertEqual([], report["calls"])

    def test_a_missing_calibration_pair_is_refused_before_spending(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(specimen()), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "calibration"):
                amendment.run_case(source, root / "results", TextHost())
            self.assertFalse((root / "results").exists())

    def test_nine_executions_are_judged_blind_and_cost_matches_the_calls(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            report = amendment.run_case(source, root / "results", TextHost())
            self.assertEqual("complete", report["status"])
            self.assertEqual("helped", report["verdict"])
            self.assertEqual(21, report["accounting"]["planned_calls"])
            self.assertEqual(21, report["accounting"]["actual_calls"])
            self.assertEqual(42, report["accounting"]["tokens"]["input_tokens"])
            self.assertEqual(9, len(report["observations"]))
            self.assertEqual({"material": 0}, report["counts"]["standing"]["yes"])
            self.assertEqual({"material": 3}, report["counts"]["amended"]["yes"])
            for call in report["calls"]:
                if call["purpose"] != "judge":
                    continue
                value = json.loads((root / "results" / "calls" / call["id"] / "prompt.txt").read_text(encoding="utf-8"))
                self.assertEqual({"situation", "source", "questions", "response"}, set(value))
                self.assertNotIn("standing", value["response"])

    def test_a_judge_that_passes_the_wrong_answer_stops_before_executions(self):
        class Uncalibrated:
            def run(self, directory):
                prompt = (directory / "prompt.txt").read_text(encoding="utf-8")
                if prompt.startswith("{"):
                    value = json.loads(prompt)
                    if "outside_file" in value:
                        return TextHost().run(directory)
                    text = json.dumps({"answers": [{"id": "material", "yes": True, "quotes": [value["response"]], "evidence": "Claimed presence."}]})
                else:
                    text = prompt
                return {"status": "ok", "text": text, "usage": {}}

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            case = specimen()
            case["judge"] = "Judge the response."
            case["calibration"] = [
                {"question_id": "material", "response": "right answer", "expected": True},
                {"question_id": "material", "response": "wrong answer", "expected": False},
            ]
            source = root / "case.json"
            source.write_text(json.dumps(case), encoding="utf-8")
            report = amendment.run_case(source, root / "results", Uncalibrated())
            self.assertEqual("calibration_failed", report["status"])
            self.assertEqual(["health", "calibration", "calibration"], [c["purpose"] for c in report["calls"]])

    def test_health_failure_keeps_evidence_and_starts_no_trials(self):
        class Unavailable:
            def __init__(self):
                self.calls = 0

            def run(self, directory):
                self.calls += 1
                return {"status": "error", "error": "authentication expired", "text": "", "usage": {}}

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "case.json"
            source.write_text(json.dumps(calibrated_specimen()), encoding="utf-8")
            host = Unavailable()
            report = amendment.run_case(source, root / "results", host)
            self.assertEqual("preflight_failed", report["status"])
            self.assertEqual(1, host.calls)
            self.assertEqual("authentication expired", report["calls"][0]["error"])
            self.assertEqual(report, json.loads((root / "results" / "report.json").read_text(encoding="utf-8")))


class AdapterTests(unittest.TestCase):
    def test_an_image_capable_or_implicit_catalog_is_refused(self):
        for mutation in ("images", "implicit_patch"):
            with self.subTest(mutation=mutation):
                catalog = text_catalog()
                if mutation == "images":
                    catalog["models"][0]["input_modalities"].append("image")
                else:
                    catalog["models"][0].pop("apply_patch_tool_type")
                with self.assertRaisesRegex(ValueError, "text-only"):
                    amendment.CodexHost(["never-start"], "model", 1, [], catalog)

    def test_a_decode_error_is_not_an_access_denial(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            executable = root / "host.py"
            executable.write_text(
                "import json,sys\nsys.stdin.read()\n"
                "sys.stderr.write('2026 ERROR codex_core::tools::router: unable to process image: unsupported image data\\n')\n"
                "print(json.dumps({'type':'item.completed','item':{'type':'agent_message','text':'answer'}}))\n"
                "print(json.dumps({'type':'turn.completed','usage':{'input_tokens':2,'output_tokens':1}}))\n",
                encoding="utf-8",
            )
            stage = amendment.prepare_execution(specimen(), root / "stage", "standing")
            result = amendment.CodexHost([sys.executable, str(executable)], "model", 10, [], text_catalog()).run(stage)
            self.assertEqual("error", result["status"])
            self.assertFalse(result["denied_image_read"])
            self.assertIn("unsupported image", result["error"])

    def test_timeout_is_preserved_as_a_failed_execution(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            executable = root / "host.py"
            executable.write_text("import time\ntime.sleep(10)\n", encoding="utf-8")
            stage = amendment.prepare_execution(specimen(), root / "stage", "standing")
            result = amendment.CodexHost([sys.executable, str(executable)], "model", 0.1, [], text_catalog()).run(stage)
            self.assertEqual("timeout", result["status"])
            self.assertEqual("", result["text"])
            self.assertTrue((stage / "events.jsonl").exists())
            self.assertTrue((stage / "result.json").exists())

    def test_ignored_settings_and_tool_use_cannot_pass_as_an_isolated_answer(self):
        for item in ({"type": "error", "message": "unrecognized setting"},
                     {"type": "command_execution", "command": "read private material"}):
            with self.subTest(item=item), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                executable = root / "host.py"
                events = [
                    {"type": "item.completed", "item": item},
                    {"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
                    {"type": "turn.completed", "usage": {"input_tokens": 2, "output_tokens": 1}},
                ]
                executable.write_text("import sys\nsys.stdin.read()\nprint(" + repr("\n".join(json.dumps(e) for e in events)) + ")\n", encoding="utf-8")
                stage = amendment.prepare_execution(specimen(), root / "stage", "standing")
                result = amendment.CodexHost([sys.executable, str(executable)], "model", 10, [], text_catalog()).run(stage)
                self.assertEqual("error", result["status"])
                self.assertIn(item["type"], result["error"])

    def test_real_process_output_keeps_usage_and_the_requested_isolation_settings(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            executable = root / "host.py"
            executable.write_text(
                "import json,sys\n"
                "sys.stdin.read()\n"
                "print(json.dumps({'type':'item.completed','item':{'type':'agent_message','text':'answer'}}))\n"
                "print(json.dumps({'type':'turn.completed','usage':{'input_tokens':17,'output_tokens':4}}))\n",
                encoding="utf-8",
            )
            stage = amendment.prepare_execution(specimen(), root / "stage", "standing")
            host = amendment.CodexHost([sys.executable, str(executable)], "fixed-model", 10, [], text_catalog("fixed-model"))
            result = host.run(stage)
            self.assertEqual("ok", result["status"])
            self.assertEqual("answer", result["text"])
            self.assertEqual(17, result["usage"]["input_tokens"])
            command = json.loads((stage / "command.json").read_text(encoding="utf-8"))
            self.assertIn("--ignore-user-config", command)
            self.assertIn("--no-daemon", command)
            self.assertIn("features.shell_tool=false", command)
            self.assertIn("project_doc_max_bytes=0", command)
            self.assertIn("features.memories=false", command)
            self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", command)


if __name__ == "__main__":
    unittest.main()
