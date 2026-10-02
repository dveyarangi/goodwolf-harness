"""Reproduce the evaluation against a committed revision in disposable repositories.

Run with Python 3.12+ and Git. No commands mutate the evaluated repository.
Results contain command output and are written beside this script.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
REVISION = "924d0b989401d3c4698133735bfbbabe0da4d329"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", GIT_CONFIG_GLOBAL="NUL" if os.name == "nt" else "/dev/null")
ENV.update(GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="safe.directory", GIT_CONFIG_VALUE_0=ROOT.as_posix())


def command(args, cwd, timeout=300):
    started = time.monotonic()
    result = subprocess.run(args, cwd=cwd, env=ENV, capture_output=True, encoding="utf-8", errors="replace", timeout=timeout)
    return dict(exit=result.returncode, seconds=round(time.monotonic() - started, 3), stdout=result.stdout, stderr=result.stderr)


def git(root, *args):
    result = command(["git", *args], root)
    if result["exit"]:
        raise RuntimeError(result)
    return result["stdout"].strip()


def commit(root, message):
    git(root, "add", "--all")
    git(root, "-c", "user.name=Evaluation fixture", "-c", "user.email=evaluation@example.invalid", "commit", "--quiet", "-m", message)
    return git(root, "rev-parse", "HEAD")


def digest(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file() and not p.is_symlink() and ".git" not in p.relative_to(root).parts}


def harness(source, target, mode, ref=None):
    args = [sys.executable, "-B", str(source / ".agents/scripts/gw/harness.py"), str(target), mode, "--from", str(source)]
    if ref:
        args += ["--at", ref]
    result = command(args, source)
    try:
        result["report"] = json.loads(result["stdout"])
    except ValueError:
        pass
    return result


def main():
    results = {"revision": REVISION, "python": sys.version, "platform": sys.platform, "checks": {}, "probes": {}}
    # The context owns this exact temporary root and removes only that root on exit.
    with tempfile.TemporaryDirectory(prefix="goodwolf-evaluation-") as location:
        workspace = Path(location).resolve()
        source = workspace / "source"
        source.mkdir()
        archive = subprocess.run(["git", "archive", "--format=tar", REVISION], cwd=ROOT, env=ENV, capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as files:
            for member in files.getmembers():
                destination = (source / member.name).resolve()
                if not destination.is_relative_to(source):
                    raise RuntimeError("archive path outside fixture")
                if member.isfile():
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(files.extractfile(member).read())
        git(source, "init", "--quiet", "--initial-branch=main")
        base = commit(source, "Exact evaluated revision content")
        before = digest(source)
        commands = {name: [sys.executable, "-B", f".agents/scripts/gw/{name}.py", "--check"]
                    for name in ("mechanisms", "inject_rules", "tickets", "maintain")}
        commands["tests"] = [sys.executable, "-B", "-m", "unittest", "discover", "-s", ".agents/scripts/gw/test", "-p", "test_*.py"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(command, args, source): name for name, args in commands.items()}
            for future in concurrent.futures.as_completed(futures):
                name = futures[future]
                results["checks"][name] = future.result()
                print(name, results["checks"][name]["exit"], results["checks"][name]["seconds"], flush=True)
        results["checks_preserve_files"] = before == digest(source)

        target = workspace / "recipient"
        target.mkdir()
        git(target, "init", "--quiet", "--initial-branch=main")
        results["probes"]["install"] = harness(source, target, "--install", base)
        results["probes"]["intact_check"] = harness(source, target, "--check")
        print("install", results["probes"]["install"]["exit"], flush=True)

        # A file outside the old manifest is explicitly classified as the recipient's own.
        collision = ".agents/evaluation-collision.txt"
        (target / collision).write_text("recipient's uncommitted work\n", encoding="utf-8")
        original = (target / collision).read_bytes()
        classified = harness(source, target, "--check")
        (source / collision).write_text("new upstream file\n", encoding="utf-8")
        added = commit(source, "Controlled upstream addition at recipient-owned path")
        updated = harness(source, target, "--update", added)
        results["probes"]["new_path_collision"] = {
            "classified_before": classified,
            "update": updated,
            "recipient_file_preserved": (target / collision).read_bytes() == original,
            "content_after": (target / collision).read_text(encoding="utf-8"),
        }
        print("new_path_collision preserved", results["probes"]["new_path_collision"]["recipient_file_preserved"], flush=True)

        # Bad local input can be detected before any installation work starts.
        invalid = workspace / "invalid-local"
        invalid.mkdir()
        git(invalid, "init", "--quiet", "--initial-branch=main")
        (invalid / "local.rules.md").write_text("# Local rules\n\nNo parseable rules.\n", encoding="utf-8")
        before = digest(invalid)
        refused = harness(source, invalid, "--install", base)
        after = digest(invalid)
        results["probes"]["refusal_side_effects"] = {
            "install": refused,
            "unchanged": before == after,
            "added": sorted(set(after) - set(before)),
            "changed": sorted(k for k in before if before[k] != after.get(k)),
        }
        print("refusal unchanged", before == after, flush=True)

        # Positive control: an actual edit to an old core file should be caught.
        damaged = target / ".agents/skills/recall/SKILL.md"
        damaged.write_bytes(damaged.read_bytes() + b"\nControlled drift for evaluation.\n")
        results["probes"]["core_drift"] = harness(source, target, "--check")

        # Preserve measurement definitions rather than treating raw volume as effectiveness.
        tracked = git(source, "ls-files").splitlines()
        stats = {}
        for group, paths in {
            "core_markdown": [p for p in tracked if p.startswith(".agents/") and p.endswith(".md")],
            "core_python": [p for p in tracked if p.startswith(".agents/scripts/gw/") and "/test/" not in p and p.endswith(".py")],
            "test_python": [p for p in tracked if p.startswith(".agents/scripts/gw/test/") and p.endswith(".py")],
            "docs_markdown": [p for p in tracked if p.startswith("docs/") and p.endswith(".md")],
        }.items():
            texts = [(source / p).read_text(encoding="utf-8") for p in paths]
            stats[group] = {"files": len(paths), "words_whitespace_split": sum(len(t.split()) for t in texts), "lines": sum(len(t.splitlines()) for t in texts)}
        stats["skills"] = len(list((source / ".agents/skills").glob("*/SKILL.md")))
        stats["declared_mechanisms"] = [p.name for p in (source / ".agents/mechanisms").iterdir() if p.is_dir()]
        stats["live_tickets"] = len(list((source / "docs/tickets").glob("[0-9]*.md")))
        stats["done_tickets"] = len(list((source / "docs/tickets/done").glob("*.md")))
        stats["queue_words"] = len((source / "docs/tickets/README.md").read_text(encoding="utf-8").split())
        stats["ci_paths"] = [p for p in tracked if p.startswith(".github/workflows/")]
        results["inventory"] = stats
        OUT.joinpath("results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
        print("saved", str(OUT / "results.json"), flush=True)


if __name__ == "__main__":
    main()
