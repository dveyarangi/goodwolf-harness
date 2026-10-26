"""Recover the two infrastructure-failed judgements from the 2026-10-26 run.

The original run is immutable. This dated evidence script is not a retry policy.
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tomllib

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / ".agents/scripts/gw"))
import amendment


def recover(source, output):
    report = json.loads((source / "report.json").read_text(encoding="utf-8"))
    raw = (source / "case.json").read_bytes()
    case = json.loads(raw)
    amendment.validate_case(case)
    assert hashlib.sha256(raw).hexdigest() == report["case_sha256"]
    assert report["status"] == "incomplete" and report["verdict"] is None
    assert len(report["calls"]) == 27
    assert len(report["calibration"]) == len(case["calibration"]) == 8
    for result, sample in zip(report["calibration"], case["calibration"]):
        assert result["status"] == "ok" and result["answers"][0]["yes"] == sample["expected"]
    executions = {c["id"]: c for c in report["calls"] if c["purpose"] == "execution"}
    assert len(executions) == 9 and all(c["status"] == "ok" for c in executions.values())
    assert {(o["execution"], o["mode"]) for o in report["observations"]} == {
        (o["execution"], o["mode"]) for o in json.loads((source / "key.json").read_text(encoding="utf-8"))}
    failed = [o for o in report["observations"] if o["judgement"]["status"] != "ok"]
    assert len(failed) == 2
    for observation in failed:
        call = next(c for c in report["calls"] if c["id"] == observation["judgement"]["call"])
        assert call["purpose"] == "judge" and call["status"] == "error"
        assert "failed to install system skills" in call["error"]
    health = next(c for c in report["calls"] if c["purpose"] == "health")
    directory = source / "calls" / health["id"]
    command = json.loads((directory / "command.json").read_text(encoding="utf-8"))
    catalog = json.loads((directory / "model-catalog.json").read_text(encoding="utf-8"))
    assert hashlib.sha256(json.dumps(catalog, sort_keys=True).encode("utf-8")).hexdigest() == report["host"]["catalog_sha256"]
    disabled = tomllib.loads(next(c for c in command if c.startswith("skills.config=")))["skills"]["config"]
    assert all(s["enabled"] is False for s in disabled)
    host = amendment.CodexHost([command[0]], report["host"]["requested_model"], 600,
                               [s["path"] for s in disabled], catalog)
    host.version = subprocess.check_output([command[0], "--version"], text=True, encoding="utf-8", timeout=30).strip()
    assert host.version == report["host"]["version"]
    assert not any((p / ".git").exists() for p in (output, *output.parents))
    shutil.copytree(source, output)
    report["recovery"] = {"source": str(source), "reason": "Shared system-skills startup failed; only the two failed judge processes are repeated sequentially.",
                          "prior_judgements": []}
    for observation in failed:
        report["recovery"]["prior_judgements"].append({"execution": observation["execution"], "judgement": observation["judgement"]})
        observation["judgement"] = amendment.judge(case, executions[observation["execution"]]["text"],
                                                    case["questions"], host, output, report["calls"], "judge-recovery")
        amendment.save(output / "recovery-checkpoint.json", report)
    report.update(amendment.measure(case, report["observations"], report["calls"]))
    report["accounting"] = amendment.accounting(report["calls"], len(case["questions"]), recovery_calls=2)
    assert report["accounting"]["planned_calls"] == report["accounting"]["actual_calls"] == 29
    amendment.save(output / "report.json", report)
    print(json.dumps({k: report[k] for k in ("status", "verdict", "counts", "accounting")}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    recover(args.source.resolve(), args.output.resolve())
