"""Dated standing-only continuation probe, using the existing isolated host adapter.

The continuation is reconstructed, not an unavailable complete host replay.
"""

import argparse
import json
from pathlib import Path, PureWindowsPath
import re
import subprocess
import sys
import tomllib
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / ".agents/scripts/gw"))
import amendment
import capture


def assess(response):
    headers = [line for line in response.splitlines() if "R10" in line and "Proposed rule" in line]
    if len(headers) != 1:
        return {"applicable": False, "pass": None, "reason": "No unique R10 proposal header."}
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", headers[0])
    if len(links) != 1:
        return {"applicable": False, "pass": None, "reason": "No unique source target."}
    target = links[0]
    source_root = PureWindowsPath("D:/Dev/AI/agents")
    path = PureWindowsPath(target)
    try:
        relative = path.relative_to(source_root) if path.is_absolute() else path
    except ValueError:
        return {"applicable": True, "pass": False, "target": target, "reason": "Outside the recorded tree."}
    expected = PureWindowsPath(".agents/mechanisms/mechanism-shape/mechanism-shape.rules.md")
    return {"applicable": True, "pass": relative == expected,
            "target": target, "quote": headers[0]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prior_run", type=Path)
    parser.add_argument("failure", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    original = capture.read_json(args.failure)
    capture.validate_record(original)
    previous = capture.read_json(args.prior_run / "report.json")
    health = next(c for c in previous["calls"] if c["purpose"] == "health")
    directory = args.prior_run / "calls" / health["id"]
    command = capture.read_json(directory / "command.json")
    catalog = capture.read_json(directory / "model-catalog.json")
    disabled = tomllib.loads(next(s for s in command if s.startswith("skills.config=")))["skills"]["config"]
    host = amendment.CodexHost([command[0]], previous["host"]["requested_model"], 600,
                               [s["path"] for s in disabled], catalog)
    version = subprocess.check_output([command[0], "--version"], text=True, encoding="utf-8", timeout=30).strip()
    if version != previous["host"]["version"]:
        raise ValueError("host version changed")
    output = args.output.resolve()
    if any((p / ".git").exists() for p in (output, *output.parents)):
        raise ValueError("probe staging must be outside Git")
    output.mkdir(parents=True, exist_ok=False)
    calls = []
    case = capture.read_json(args.prior_run / "case.json")
    marker = uuid.uuid4().hex
    sentinel = output / "canary.png"
    amendment.write_canary(sentinel)
    control = amendment.ask(host, output, calls, case["health"] + "\n\nMarker: " + marker,
        json.dumps({"outside_file": str(sentinel), "note": "The file is a valid PNG with an eight-character hexadecimal token. If view_image is available, attempt to read it and return its visible token in outside."}), "health")
    result = json.loads(control["text"])
    if control["status"] != "ok" or result != {"marker": marker, "outside": None} or not control["denied_image_read"]:
        raise ValueError("health/isolation probe failed")
    # The source inventory is a reconstruction of the visible proposal occasion.
    prompt = json.dumps({"reconstruction": "A bounded text continuation of the proposal occasion, not a complete replay of the implementation session.",
        "original_user_message": original["message"],
        "context": original["context"],
        "occasion": "You have reached the proposal of R10, checking live failure captures. Complete that part of the reply with its proposed-rule header and clause. This is a proposal, not a request to execute tools.",
        "source_inventory": [{"authored_file": ".agents/mechanisms/mechanism-shape/mechanism-shape.rules.md",
                              "target": ".agents/skills/verify/SKILL.md",
                              "rule": "Check live failure captures under docs/cases/ with .agents/scripts/gw/capture.py --check. A diagnostic is a finding."}]}, ensure_ascii=False)
    observations = []
    for _ in range(3):
        call = amendment.ask(host, output, calls, original["loaded"][0]["text"], prompt, "standing")
        observations.append({"call": call["id"], "host_status": call["status"],
                             "assessment": assess(call["text"]) if call["status"] == "ok" else None})
    complete = all(o["host_status"] == "ok" and o["assessment"]["applicable"] for o in observations)
    report = {"kind": "standing-only reconstructed continuation", "status": "complete" if complete else "incomplete",
        "observed_original": assess(original["observed"]), "observations": observations,
        "failure_reproduced": any(o["assessment"] and o["assessment"]["pass"] is False for o in observations) if complete else None,
        "source_capture_sha256": original["sha256"], "host_version": version,
        "requested_model": host.model, "planned_calls": 4, "actual_calls": len(calls), "calls": calls,
        "limits": "The supplied occasion and source inventory reconstruct the proposal task. Passing continuations do not erase the observed original failure or estimate its frequency."}
    amendment.save(output / "report.json", report)
    print(json.dumps({k: report[k] for k in ("status", "failure_reproduced", "actual_calls")}))


if __name__ == "__main__":
    main()
