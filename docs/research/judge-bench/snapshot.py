"""Lay out the tree each specimen's draft was written in, at the commit `key.json` names.

    uv run --offline --no-project python docs/research/judge-bench/snapshot.py <directory> [label ...]

Each label gets `<directory>/<label>/`, the repository as `git archive` gives it at the snapshot
commit — the last commit before the draft, so the tree holds nothing decided after it. Put the
directory outside the repository: a judge is pointed at it and must not find this bench there.
Keep its path short (`D:/jt`): the question store's file names outgrow Windows' path limit.
"""

import io
import json
import subprocess
import sys
import tarfile
from pathlib import Path

HERE = Path(__file__).parent
REPOSITORY = HERE.parents[2]


def main(argv: list[str]) -> None:
    target = Path(argv[0])
    key = json.loads((HERE / "key.json").read_text(encoding="utf-8"))
    for label in argv[1:] or list(key):
        archive = subprocess.run(
            ["git", "-C", str(REPOSITORY), "archive", key[label]["snapshot"]], capture_output=True, check=True
        ).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
            tree.extractall(target / label, filter="data")
        print(label, key[label]["snapshot"])


if __name__ == "__main__":
    main(sys.argv[1:])
