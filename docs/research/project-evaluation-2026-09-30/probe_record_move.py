"""Exercise a source edit between deriving a record move and applying it."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest import mock

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
REVISION = "924d0b989401d3c4698133735bfbbabe0da4d329"
ENV = dict(os.environ, GIT_CONFIG_GLOBAL="NUL" if os.name == "nt" else "/dev/null",
           GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="safe.directory", GIT_CONFIG_VALUE_0=ROOT.as_posix())


def main():
    with tempfile.TemporaryDirectory(prefix="goodwolf-move-probe-") as location:
        workspace = Path(location).resolve()
        scripts = workspace / "scripts"
        scripts.mkdir()
        for filename in ("docs_corpus.py", "move_doc.py"):
            content = subprocess.run(["git", "show", f"{REVISION}:.agents/scripts/gw/{filename}"], cwd=ROOT,
                                     env=ENV, capture_output=True, check=True).stdout
            (scripts / filename).write_bytes(content)
        sys.path.insert(0, str(scripts))
        import move_doc

        target = workspace / "recipient"
        target.mkdir()
        subprocess.run(["git", "init", "--quiet", str(target)], env=ENV, check=True)
        source = target / "record.md"
        destination = target / "done/record.md"
        source.write_text("# Original\n", encoding="utf-8")
        (target / "index.md").write_text("[Record](record.md)\n", encoding="utf-8")
        pairs = [("record.md", "done/record.md")]
        refusal = move_doc.refusal(target, pairs)
        derive = move_doc._change_set
        messages = []

        def another_editor_writes_after_the_plan(*args):
            planned = derive(*args)
            source.write_text("# Original\n\nAnother session's new, uncommitted decision.\n", encoding="utf-8")
            return planned

        failure = None
        with mock.patch.object(move_doc, "_change_set", another_editor_writes_after_the_plan):
            try:
                move_doc.perform(target, pairs, announce=messages.append)
            except Exception as error:
                failure = repr(error)
        result = {
            "revision": REVISION,
            "interleaving": "another editor changes source after _change_set derives operations, before the first operation applies",
            "preflight_refusal": refusal,
            "exception": failure,
            "announcements": messages,
            "source_exists": source.exists(),
            "destination_content": destination.read_text(encoding="utf-8") if destination.exists() else None,
            "index_content": (target / "index.md").read_text(encoding="utf-8"),
            "new_decision_preserved": any("Another session" in p.read_text(encoding="utf-8") for p in target.rglob("*.md")),
        }
        Path(__file__).with_name("record-move-result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
