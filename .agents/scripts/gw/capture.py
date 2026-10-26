# Mechanism: mechanism-shape
"""Preserve a noticed failure before its remedy exists; check saved observations, not behaviour."""

from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import sys

FORMAT = "failure-capture-1"
FIELDS = {"session", "message", "context", "loaded", "observed", "expected", "rules", "register", "limitations"}


def capture(draft: dict, destination: Path):
    validate_draft(draft)
    record = dict(draft, format=FORMAT, captured_at=datetime.now(timezone.utc).isoformat())
    record["sha256"] = digest(record)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    return record


def validate_draft(draft):
    if not isinstance(draft, dict) or set(draft) != FIELDS:
        raise ValueError("a failure draft needs exactly: " + ", ".join(sorted(FIELDS)))
    for name in ("session", "expected", "register"):
        require_text(draft[name], name)
    leaves = {"/observed": draft["observed"], "/message/content": draft["message"].get("content") if isinstance(draft["message"], dict) else None}
    message(draft["message"])
    if draft["message"]["role"] != "user":
        raise ValueError("message must carry the original user's role")
    if not isinstance(draft["context"], list):
        raise ValueError("context must be an ordered message list")
    for index, item in enumerate(draft["context"]):
        message(item)
        leaves[f"/context/{index}/content"] = item["content"]
    if not isinstance(draft["loaded"], list) or not draft["loaded"]:
        raise ValueError("loaded must contain instruction snapshots")
    for index, item in enumerate(draft["loaded"]):
        if not isinstance(item, dict) or set(item) != {"path", "text"}:
            raise ValueError("each loaded instruction needs path and text")
        require_text(item["path"], "loaded path")
        leaves[f"/loaded/{index}/text"] = item["text"]
    if not isinstance(draft["rules"], list) or not draft["rules"]:
        raise ValueError("rules must name the requirements in play")
    for rule in draft["rules"]:
        require_text(rule, "rule")
    if not isinstance(draft["limitations"], list):
        raise ValueError("limitations must be a list")
    labelled = {}
    for label in draft["limitations"]:
        if not isinstance(label, dict) or set(label) != {"field", "kind", "reason"}:
            raise ValueError("a limitation needs field, kind and reason")
        field, kind = label["field"], label["kind"]
        if not isinstance(field, str) or field not in leaves or field in labelled or kind not in ("missing", "reconstructed"):
            raise ValueError("unknown or repeated limitation")
        require_text(label["reason"], "limitation reason")
        if (kind == "missing") != (leaves[field] is None):
            raise ValueError("limitation contradicts its field: " + field)
        labelled[field] = kind
    for field, value in leaves.items():
        if value is None:
            if labelled.get(field) != "missing":
                raise ValueError("unlabelled missing evidence: " + field)
        else:
            require_text(value, field)


def require_text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(name + " must be nonempty text")


def message(value):
    if not isinstance(value, dict) or set(value) != {"role", "content"}:
        raise ValueError("a message needs role and content")
    if value["role"] not in ("system", "developer", "user", "assistant", "tool"):
        raise ValueError("unknown message role")
    if value["content"] is not None:
        require_text(value["content"], "message content")


def digest(record):
    value = {key: value for key, value in record.items() if key != "sha256"}
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def validate_record(record):
    if not isinstance(record, dict):
        raise ValueError("capture must be a JSON object")
    validate_draft({key: value for key, value in record.items() if key not in ("format", "captured_at", "sha256")})
    try:
        stamp = datetime.fromisoformat(record["captured_at"])
        if stamp.utcoffset() != timezone.utc.utcoffset(stamp):
            raise ValueError("not UTC")
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("captured_at must be a UTC ISO timestamp") from error
    if record.get("format") != FORMAT or not record.get("captured_at") or record.get("sha256") != digest(record):
        raise ValueError("capture metadata or digest does not match")


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON field: " + key)
            result[key] = value
        return result
    def finite(value):
        raise ValueError("non-JSON constant: " + value)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique, parse_constant=finite)


def check(root):
    diagnostics, count = [], 0
    for path in sorted(root.rglob("failure.json")):
        if path.relative_to(root).parts[0] == "done":
            continue
        count += 1
        try:
            validate_record(read_json(path))
        except (OSError, ValueError, TypeError, AttributeError) as error:
            diagnostics.append({"file": str(path), "error": str(error)})
    return {"checked": count, "diagnostics": diagnostics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--capture", type=Path, help="failure draft, without an amendment or verdict")
    mode.add_argument("--check", nargs="?", const=Path("docs/cases"), type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.capture:
            if args.output is None:
                parser.error("--capture requires --output")
            record = capture(read_json(args.capture), args.output)
            print(json.dumps({"file": str(args.output), "sha256": record["sha256"]}))
            return 0
        if args.output is not None:
            parser.error("--output belongs to --capture")
        report = check(args.check)
        print(json.dumps(report, ensure_ascii=False))
        return int(bool(report["diagnostics"]))
    except (OSError, ValueError, TypeError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    sys.exit(main())
