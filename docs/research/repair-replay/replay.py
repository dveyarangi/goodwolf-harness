# Mechanism: mechanism-shape
"""Offline reader replay; no semantic inference and no live hook invocation."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("packet", "evaluate"))
    parser.add_argument("cases", type=Path)
    parser.add_argument("reviews", type=Path, nargs="?")
    args = parser.parse_args()
    try:
        cases = read_cases(args.cases)
        if args.command == "packet":
            if args.reviews is not None:
                raise ValueError("packet does not accept reviews")
            result = {"reader": Path(__file__).with_name("reader.md").read_text(encoding="utf-8"),
                      "cases": cases}
        else:
            if args.reviews is None:
                raise ValueError("evaluate requires a reviews file")
            result = evaluate(cases, read_json(args.reviews))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"replay: {error}", file=sys.stderr)
        return 1
    sys.stdout.buffer.write((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return 0


def read_cases(path):
    dataset = read_json(path)
    if not isinstance(dataset, dict):
        raise ValueError("cases must be an object")
    rule = require_text(dataset.get("rule"), "rule")
    if not isinstance(dataset.get("cases"), list) or not dataset["cases"]:
        raise ValueError("cases must be a nonempty array")
    cases = []
    seen = set()
    for source in dataset["cases"]:
        if not isinstance(source, dict):
            raise ValueError("each case must be an object")
        identity = require_text(source.get("id"), "case id")
        if identity in seen:
            raise ValueError("duplicate case id")
        seen.add(identity)
        if type(source.get("stop_hook_active")) is not bool:
            raise ValueError("stop_hook_active must be a boolean")
        case = {"id": identity, "sources": {"rule": rule,
                "conversation": require_text(source.get("conversation"), "conversation"),
                "work": require_text(source.get("work"), "work")},
                "stop_hook_active": source["stop_hook_active"]}
        canonical = json.dumps(case, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        case["sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        cases.append(case)
    return cases


def evaluate(cases, reviews):
    if not isinstance(reviews, list):
        raise ValueError("reviews must be an array")
    by_id = {case["id"]: case for case in cases}
    validated = {}
    for review in reviews:
        if not isinstance(review, dict):
            raise ValueError("each review must be an object")
        identity = require_text(review.get("case_id"), "review case id")
        if identity not in by_id or identity in validated:
            raise ValueError("unknown or duplicate review case id")
        case = by_id[identity]
        if review.get("case_sha256") != case["sha256"]:
            raise ValueError("review is for a different case version")
        verdict = review.get("verdict")
        if verdict not in ("allow", "return", "unknown"):
            raise ValueError("unknown verdict")
        require_text(review.get("reason"), "review reason")
        evidence = review.get("evidence")
        if not isinstance(evidence, list):
            raise ValueError("evidence must be an array")
        cited = set()
        for item in evidence:
            if not isinstance(item, dict):
                raise ValueError("each citation must be an object")
            name = require_text(item.get("source"), "citation source")
            quote = require_text(item.get("quote"), "citation quote")
            if name not in case["sources"] or quote not in case["sources"][name]:
                raise ValueError("citation does not occur in its named source")
            cited.add(name)
        if verdict == "return" and cited != set(case["sources"]):
            raise ValueError("return requires rule, conversation and work evidence")
        if verdict == "allow" and not cited:
            raise ValueError("allow requires evidence")
        validated[identity] = review
    if set(validated) != set(by_id):
        raise ValueError("each case requires exactly one review")

    report = []
    for case in cases:
        review = validated[case["id"]]
        verdict = review["verdict"]
        preview = None if verdict == "unknown" else {}
        if verdict == "return":
            preview = {"decision": "block", "reason": review["reason"]}
        status = verdict
        if case["stop_hook_active"]:
            status, preview = "limit_reached", None
        report.append({"case_id": case["id"], "status": status, "stop_preview": preview})
    return report


def require_text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")
    return value


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_fields,
                      parse_constant=invalid_constant)


def unique_fields(pairs):
    result = {}
    for name, value in pairs:
        if name in result:
            raise ValueError(f"duplicate JSON field: {name}")
        result[name] = value
    return result


def invalid_constant(value):
    raise ValueError(f"invalid JSON constant: {value}")


if __name__ == "__main__":
    raise SystemExit(main())
