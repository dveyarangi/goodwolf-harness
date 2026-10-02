"""Check whether the saved window experiment can be rescored or regenerated."""
from __future__ import annotations

import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[3]
REVISION = "924d0b989401d3c4698133735bfbbabe0da4d329"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8", PYTHONHASHSEED="1",
           GIT_CONFIG_GLOBAL="NUL" if os.name == "nt" else "/dev/null",
           GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="safe.directory", GIT_CONFIG_VALUE_0=ROOT.as_posix())


def run(script, directory):
    p = subprocess.run([sys.executable, "-B", script], cwd=directory, env=ENV, capture_output=True,
                       encoding="utf-8", errors="replace", timeout=120)
    return {"exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def main():
    with tempfile.TemporaryDirectory(prefix="goodwolf-research-probe-") as location:
        workspace = Path(location).resolve()
        archive = subprocess.run(["git", "archive", "--format=tar", REVISION, "docs/research/window-test"],
                                 cwd=ROOT, env=ENV, capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as files:
            for member in files.getmembers():
                path = (workspace / member.name).resolve()
                if not path.is_relative_to(workspace):
                    raise RuntimeError("archive path outside fixture")
                if member.isfile():
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(files.extractfile(member).read())
        experiment = workspace / "docs/research/window-test"
        saved = json.loads((experiment / "trials.json").read_text(encoding="utf-8"))
        result = {"revision": REVISION, "hash_seed": "1", "saved_trials": len(saved),
                  "answer_files": len(list((experiment / "answers").glob("*.txt"))),
                  "score_as_committed": run("score.py", experiment)}
        result["generate"] = run("gen.py", experiment)
        generated = json.loads((experiment / "trials.json").read_text(encoding="utf-8"))
        result["generated_trials"] = len(generated)
        result["generated_missing_tag"] = sum("tag" not in t for t in generated)
        result["changed_trial_truths"] = sum(a["truth"] != b["truth"] for a, b in zip(saved, generated))
        result["score_after_generate"] = run("score.py", experiment)
        Path(__file__).with_name("research-result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
