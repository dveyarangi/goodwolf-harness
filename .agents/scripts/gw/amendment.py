# Mechanism: mechanism-shape
"""Run one instruction case in three conditions, separately from its blind judgement.

An explicit case and output path keep project evidence out of the shipped implementation.
"""

from __future__ import annotations

import json
from pathlib import Path
import uuid
import collections
import hashlib
import random
import subprocess
import time
import argparse
import sys
import os
import threading
import struct
import zlib

_LEDGER_LOCK = threading.Lock()


def validate_case(case):
    questions = case.get("questions", [])
    names = [q["id"] for q in questions]
    if not names or len(set(names)) != len(names):
        raise ValueError("questions must have unique ids")
    calibration = case.get("calibration", [])
    pairs = [(c.get("question_id"), c.get("expected")) for c in calibration]
    expected = [(name, value) for name in names for value in (True, False)]
    if len(pairs) != len(expected) or set(pairs) != set(expected) or any(type(c.get("expected")) is not bool for c in calibration):
        raise ValueError("calibration needs one right and wrong answer per question")
    for key in ("common", "standing", "amended", "paragraph", "situation", "discovery", "message", "health", "judge"):
        if not isinstance(case.get(key), str) or not case[key].strip():
            raise ValueError("missing case text: " + key)
    for mode in ("standing", "amended"):
        if case[mode].count(case["paragraph"]) != 1:
            raise ValueError("target paragraph must occur once in " + mode)
    for key, value in case.get("fingerprints", {}).items():
        if hashlib.sha256(case[key].encode("utf-8")).hexdigest() != value:
            raise ValueError("changed case fingerprint: " + key)


class CodexHost:
    """The CLI reads only staged instructions; the model gets no command or connector tools."""

    def __init__(self, command: list[str], model: str, timeout: int, disabled_skills: list[str], catalog: dict):
        self.command, self.model, self.timeout = command, model, timeout
        self.disabled_skills = disabled_skills
        self.progress = True
        selected = next((m for m in catalog.get("models", []) if m.get("slug") == model), None)
        if not selected or selected.get("input_modalities") != ["text"] or "apply_patch_tool_type" not in selected or selected["apply_patch_tool_type"] is not None or selected.get("experimental_supported_tools") != []:
            raise ValueError("a text-only model catalog without mutation or extra tools is required")
        self.catalog = json.loads(json.dumps(catalog))

    def run(self, directory: Path) -> dict:
        save(directory / "model-catalog.json", self.catalog)
        settings = [
            "project_doc_max_bytes=0", "features.memories=false", "memories.use_memories=false",
            "features.shell_tool=false", "features.multi_agent=false", "features.apps=false",
            "features.plugins=false", "features.hooks=false", "features.shell_snapshot=false",
            'web_search="disabled"',
            "model_instructions_file=" + json.dumps((directory / "AGENTS.md").resolve().as_posix()),
            "model_catalog_json=" + json.dumps((directory / "model-catalog.json").resolve().as_posix()),
            "skills.config=[" + ",".join("{path=" + json.dumps(p) + ",enabled=false}" for p in self.disabled_skills) + "]",
        ]
        command = self.command + ["--no-daemon"]
        for setting in settings:
            command += ["-c", setting]
        command += ["exec", "--strict-config", "--ignore-user-config", "--ignore-rules", "--ephemeral",
                    "--json", "--sandbox", "read-only", "--skip-git-repo-check", "--model", self.model, "-"]
        (directory / "command.json").write_text(json.dumps(command, indent=2), encoding="utf-8")
        started = time.monotonic()
        try:
            process = subprocess.run(command, input=(directory / "prompt.txt").read_text(encoding="utf-8"),
                                     cwd=directory, capture_output=True, text=True, encoding="utf-8",
                                     errors="replace", timeout=self.timeout, shell=False)
            stdout, stderr, code = process.stdout, process.stderr, process.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr = error.stdout or b"", error.stderr or b""
            stdout = stdout.decode("utf-8", "replace") if isinstance(stdout, bytes) else stdout
            stderr = stderr.decode("utf-8", "replace") if isinstance(stderr, bytes) else stderr
            code = None
        except OSError as error:
            stdout, stderr, code = "", str(error), -1
        (directory / "events.jsonl").write_text(stdout, encoding="utf-8")
        (directory / "stderr.txt").write_text(stderr, encoding="utf-8")
        result = {"status": "timeout" if code is None else "error", "text": "", "usage": {},
                  "model": self.model, "duration_s": time.monotonic() - started, "exit_code": code,
                  "denied_image_read": "view_image is not allowed because you do not support image inputs" in stderr}
        try:
            events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
            completed = [e for e in events if e.get("type") == "turn.completed"]
            messages = [e["item"]["text"] for e in events if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
            items = [e["item"] for e in events if e.get("type", "").startswith("item.") and "item" in e]
            unsafe = [item for item in items if item.get("type") not in ("agent_message", "reasoning")]
            if completed:
                result["usage"] = completed[-1].get("usage", {})
            if messages:
                result["text"] = messages[-1]
            unexpected_errors = [line for line in stderr.splitlines() if " ERROR " in line and "view_image is not allowed because you do not support image inputs" not in line]
            if code == 0 and completed and messages and not unsafe and not unexpected_errors:
                result["status"] = "ok"
            else:
                result["error"] = json.dumps(unsafe, ensure_ascii=False) if unsafe else stderr or "host did not complete a response"
        except (ValueError, KeyError, TypeError) as error:
            result["error"] = "invalid event stream: " + str(error)
        (directory / "result.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        return result


def run_case(source: Path, output: Path, host) -> dict:
    raw = source.read_bytes()
    case = json.loads(raw)
    validate_case(case)
    output.mkdir(parents=True, exist_ok=False)
    (output / "case.json").write_bytes(raw)
    calls = []
    if without_paragraph(case["standing"], case["paragraph"]) != without_paragraph(case["amended"], case["paragraph"]):
        report = {"status": "confounded", "verdict": "confounded", "calls": [],
                  "error": "instructions differ outside the target paragraph"}
        (output / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        return report
    marker = uuid.uuid4().hex
    sentinel = output / "isolation-canary.png"
    write_canary(sentinel)
    health = ask(host, output, calls, case["health"] + "\n\nMarker: " + marker,
                 json.dumps({"outside_file": str(sentinel.resolve()), "note": "The file is a valid PNG with an eight-character hexadecimal token. If view_image is available, attempt to read it and return its visible token in outside."}), "health")
    report = {"status": "preflight_failed", "calls": calls, "verdict": None}
    try:
        control = json.loads(health["text"])
        isolated = control.get("marker") == marker and "outside" in control and control["outside"] is None and health.get("denied_image_read", False)
    except (ValueError, TypeError, AttributeError):
        isolated = False
    report["isolation"] = {"staged_marker_read": isolated, "external_canary_unread": isolated}
    if health["status"] == "ok" and isolated:
        report["status"] = "calibration_failed"
        report["calibration"] = []
        for calibration in case["calibration"]:
            questions = [q for q in case["questions"] if q["id"] == calibration["question_id"]]
            judged = judge(case, calibration["response"], questions, host, output, calls, "calibration")
            report["calibration"].append(judged)
            if judged["status"] != "ok" or judged["answers"][0]["yes"] != calibration["expected"]:
                break
        else:
            observations = []
            conditions = [mode for mode in ("none", "standing", "amended") for _ in range(3)]
            random.SystemRandom().shuffle(conditions)
            def execute(mode):
                instruction = without_paragraph(case["standing"], case["paragraph"]) if mode == "none" else case[mode]
                prompt = case["situation"] + "\n\n" + case["discovery"] + "\n\n" + case["message"]
                call = ask(host, output, calls, case["common"] + "\n\n" + instruction, prompt, "execution")
                observation = {"mode": mode, "execution": call["id"]}
                with _LEDGER_LOCK:
                    observations.append(observation)
                    save(output / "key.json", observations)
                return observation
            # CLI startups share a managed skills directory even when skills are disabled.
            for mode in conditions:
                execute(mode)
            random.SystemRandom().shuffle(observations)
            def grade(observation):
                call = next(c for c in calls if c["id"] == observation["execution"])
                observation["judgement"] = judge(case, call["text"], case["questions"], host, output, calls, "judge") if call["status"] == "ok" else {"status": "execution_error"}
            for observation in observations:
                grade(observation)
            report.update(observations=observations)
            report.update(measure(case, observations, calls))
    report["accounting"] = accounting(calls, len(case["questions"]))
    report["case_sha256"] = hashlib.sha256(raw).hexdigest()
    report["host"] = {
        "version": getattr(host, "version", None),
        "requested_model": getattr(host, "model", None),
        "model_identity": "Requested CLI identifier; the JSONL stream does not attest the resolved backend version.",
        "catalog_sha256": hashlib.sha256(json.dumps(host.catalog, sort_keys=True).encode("utf-8")).hexdigest() if hasattr(host, "catalog") else None,
    }
    if report["status"] == "complete" and len(calls) != report["accounting"]["planned_calls"]:
        raise ValueError("invocation count does not match the formula")
    (output / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report


def measure(case: dict, observations: list, calls: list) -> dict:
    modes = ("none", "standing", "amended")
    if len(observations) != 9 or len({o["execution"] for o in observations}) != 9 or any(sum(o["mode"] == m for o in observations) != 3 for m in modes):
        raise ValueError("three distinct executions per condition are required")
    counts = {}
    for mode in modes:
        judged = [o["judgement"] for o in observations if o["mode"] == mode and o["judgement"]["status"] == "ok"]
        counts[mode] = {"valid": len(judged), "yes": {q["id"]: sum(a["yes"] for j in judged for a in j["answers"] if a["id"] == q["id"]) for q in case["questions"]}}
    result = {"counts": counts, "status": "incomplete", "verdict": None}
    if all(c["valid"] == 3 for c in counts.values()):
        before, after = counts["standing"]["yes"], counts["amended"]["yes"]
        up = any(after[q] > before[q] for q in before)
        down = any(after[q] < before[q] for q in before)
        result.update(status="complete", verdict="confounded" if up and down else "helped" if up else "hurt" if down else "no observed effect")
    if len({c["model"] for c in calls if c["purpose"] == "execution" and c["status"] == "ok" and c.get("model")}) > 1:
        result.update(status="confounded", verdict="confounded", error="execution models differ")
    return result


def accounting(calls: list, question_count: int, recovery_calls: int = 0) -> dict:
    if len({c["id"] for c in calls}) != len(calls):
        raise ValueError("duplicate invocation id")
    return {
        "unit": "agent sessions (codex exec processes), excluding local metadata commands",
        "nominal_calls": 1 + 2 * question_count + 18,
        "recovery_calls": recovery_calls,
        "planned_calls": 1 + 2 * question_count + 18 + recovery_calls,
        "actual_calls": len(calls),
        "by_purpose": dict(collections.Counter(c["purpose"] for c in calls)),
        "tokens": {key: sum(c["usage"][key] for c in calls) if all(key in c.get("usage", {}) for c in calls) else None for key in ("input_tokens", "output_tokens", "cached_input_tokens")},
        "duration_s": sum(c["duration_s"] for c in calls) if all("duration_s" in c for c in calls) else None,
        "price_usd": None,
    }


def judge(case, response, questions, host, output, calls, purpose):
    prompt = json.dumps({"situation": case["situation"], "source": case["discovery"],
                         "questions": questions, "response": response}, ensure_ascii=False)
    call = ask(host, output, calls, case["judge"], prompt, purpose)
    if call["status"] != "ok":
        return {"status": "grading_error", "call": call["id"], "error": call.get("error", call["status"])}
    try:
        answers = json.loads(call["text"])["answers"]
        if not isinstance(answers, list) or {a["id"] for a in answers} != {q["id"] for q in questions}:
            raise ValueError("questions do not match")
        if len(answers) != len(questions):
            raise ValueError("duplicate answers")
        for answer in answers:
            if type(answer["yes"]) is not bool or not isinstance(answer["quotes"], list):
                raise ValueError("invalid answer type")
            if answer["yes"] and not answer["quotes"]:
                raise ValueError("yes without evidence")
            if any(not isinstance(q, str) or not q or q not in response for q in answer["quotes"]):
                raise ValueError("quotation absent from response")
            if not isinstance(answer.get("evidence"), str) or not answer["evidence"].strip():
                raise ValueError("judgement without evidence statement")
        return {"status": "ok", "call": call["id"], "answers": answers}
    except (ValueError, KeyError, TypeError) as error:
        return {"status": "grading_error", "call": call["id"], "error": str(error)}


def ask(host, output: Path, calls: list, instructions: str, prompt: str, purpose: str) -> dict:
    identity = uuid.uuid4().hex
    directory = output / "calls" / identity
    directory.mkdir(parents=True)
    (directory / "AGENTS.md").write_text(instructions, encoding="utf-8")
    (directory / "prompt.txt").write_text(prompt, encoding="utf-8")
    try:
        result = host.run(directory)
    except Exception as error:
        result = {"status": "error", "text": "", "usage": {}, "error": str(error)}
    result.update(id=identity, purpose=purpose)
    with _LEDGER_LOCK:
        calls.append(result)
        save(output / "ledger.json", calls)
        if getattr(host, "progress", False):
            print(f"{len(calls)} {purpose}: {result['status']}", flush=True)
    return result


def save(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)


def write_canary(path: Path):
    """A supported image distinguishes an access refusal from a decoder rejecting plain text."""
    glyphs = ['111101101101111', '010110010010111', '111001111100111', '111001111001111',
              '101101111001001', '111100111001111', '111100111101111', '111001001001001',
              '111101111101111', '111101111001111', '010101111101101', '110101110101110',
              '111100100100111', '110101101101110', '111100110100111', '111100110100100']
    token = uuid.uuid4().hex[:8].upper()
    scale, width, height = 8, 272, 56
    scan = bytearray()
    for y in range(height):
        scan.append(0)
        for x in range(width):
            gx, gy = (x - 8) // scale, (y - 8) // scale
            index, column = divmod(gx, 4)
            ink = 0 <= index < 8 and 0 <= gy < 5 and column < 3 and glyphs[int(token[index], 16)][gy * 3 + column] == '1'
            scan.append(0 if ink else 255)
    def chunk(kind, data):
        return struct.pack('!I', len(data)) + kind + data + struct.pack('!I', zlib.crc32(kind + data))
    path.write_bytes(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!IIBBBBB', width, height, 8, 0, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(bytes(scan))) + chunk(b'IEND', b''))


def without_paragraph(text: str, heading: str) -> str:
    start = text.index(heading)
    end = text.find("\n\n", start)
    return (text[:start] + (text[end + 2:] if end >= 0 else "")).strip()


def prepare_execution(case: dict, directory: Path, mode: str) -> Path:
    instruction = without_paragraph(case["standing"], case["paragraph"]) if mode == "none" else case[mode]
    directory.mkdir(parents=True, exist_ok=False)
    (directory / "AGENTS.md").write_text(case["common"] + "\n\n" + instruction, encoding="utf-8")
    (directory / "prompt.txt").write_text(
        case["situation"] + "\n\n" + case["discovery"] + "\n\n" + case["message"], encoding="utf-8"
    )
    return directory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--codex", required=True, help="native Codex executable")
    parser.add_argument("--model", default="gpt-6.1-sol")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    output = args.output.resolve()
    if any((ancestor / ".git").exists() for ancestor in (output, *output.parents)):
        parser.error("staging must be outside a Git checkout")
    home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    skills = []
    for skill_root in (home / "skills", Path.home() / ".agents" / "skills"):
        if skill_root.is_dir():
            skills.extend(p.parent.resolve().as_posix() for p in skill_root.rglob("SKILL.md"))
    catalog = json.loads(subprocess.check_output([args.codex, "debug", "models", "--bundled"], text=True, encoding="utf-8", timeout=30))
    selected = next((m for m in catalog["models"] if m["slug"] == args.model), None)
    if selected is None:
        parser.error("requested model is absent from the bundled catalog")
    selected.update(input_modalities=["text"], apply_patch_tool_type=None, experimental_supported_tools=[])
    host = CodexHost([args.codex], args.model, args.timeout, sorted(set(skills)), catalog)
    host.version = subprocess.check_output([args.codex, "--version"], text=True, encoding="utf-8", timeout=30).strip()
    try:
        report = run_case(args.case.resolve(), output, host)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + "\n")
    print(json.dumps({"status": report["status"], "verdict": report["verdict"], "output": str(output)}, ensure_ascii=False))
    return 0 if report["status"] == "complete" else 1


if __name__ == "__main__":
    sys.exit(main())
