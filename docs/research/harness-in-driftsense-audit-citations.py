"""Count a project's records' citations of code in its sibling repositories, and which may have lapsed.

Round 4 of the audit in harness-in-driftsense-audit.md. Reads the records under `<tree>/docs` and
the git history of every sibling repository beside the tree; prints counts only, and with
`--sample N <file>` writes N citations with line numbers, drawn at random from those whose file
still exists, half from those that may have lapsed, for readers to check — paths and line numbers,
no file content. A record under a `done` folder is a record of what happened, and is counted apart.

A citation is a path to a code file, with or without `:line` or `:from-to`, prefixed by its
repository's folder or not. An unprefixed path is given to the repository that holds that file,
if exactly one does. A citation *may have lapsed* when its file changed in its repository after
the citing record last changed in the tree — the lapse rule of the round method: by file and commit.

Usage: python -I harness-in-driftsense-audit-citations.py <tree> [--sample N <file>]
"""

from __future__ import annotations

import collections
import random
import re
import subprocess
import sys
from pathlib import Path

CODE = r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.(?:py|js|jsx|ts|tsx|sql|html|css|scss|yml|yaml|sh|json|toml|cfg|ini)"
CITE = re.compile(rf"(?<![\w/.-])({CODE})(?::(\d+)(?:[-–](\d+))?)?")
NOT_READ = ("settings.py", "cfg.py", "score_model.py", ".env", "readonly-db-access-grant")


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=60).stdout.strip()


def changed_at(repo: Path, path: str, cache: dict) -> int:
    key = (repo, path)
    if key not in cache:
        out = git(repo, "log", "-1", "--format=%ct", "--", path)
        cache[key] = int(out) if out.isdigit() else 0
    return cache[key]


def main() -> None:
    tree = Path(sys.argv[1]).resolve()
    repos = {p.name: p for p in tree.parent.iterdir() if p.is_dir() and (p / ".git").exists() and p != tree}
    files = {name: set(git(repo, "ls-files").splitlines()) for name, repo in repos.items()}
    cache: dict = {}
    tally = collections.Counter()
    by_repo = collections.Counter()
    by_kind = collections.Counter()
    lines_ok = collections.Counter()
    lapse_by_kind = collections.Counter()
    with_line: list[tuple[str, str, str, int, bool]] = []
    for record in sorted((tree / "docs").rglob("*.md")):
        rel = record.relative_to(tree).as_posix()
        kind = rel.split("/")[1] if rel.count("/") > 1 else "docs"
        kind += " (done)" if "/done/" in rel else ""
        text = record.read_text(encoding="utf-8", errors="replace")
        written = None
        for match in CITE.finditer(text):
            path, start = match.group(1), match.group(2)
            head = path.split("/")[0]
            if head in repos:
                repo, inner = head, path[len(head) + 1:]
            else:
                holders = [name for name in repos if path in files[name]]
                if len(holders) != 1:
                    tally["not a sibling's file, or ambiguous"] += 1
                    continue
                repo, inner = holders[0], path
            tally["citations"] += 1
            by_repo[repo] += 1
            by_kind[kind] += 1
            if inner not in files[repo]:
                tally["file no longer in its repository"] += 1
                continue
            tally["line given" if start else "no line"] += 1
            if written is None:
                out = git(tree, "log", "-1", "--format=%ct", "--", rel)
                written = int(out) if out.isdigit() else 0
            lapsed = changed_at(repos[repo], inner, cache) > written
            tally["may have lapsed" if lapsed else "unchanged since"] += 1
            if lapsed:
                lapse_by_kind[kind] += 1
            if start:
                size = sum(1 for _ in (repos[repo] / inner).open(encoding="utf-8", errors="replace"))
                end = int(match.group(3) or start)
                lines_ok["line beyond the file's end" if max(int(start), end) > size else "line within the file"] += 1
                if lapsed:
                    lines_ok["line given and may have lapsed"] += 1
                if not any(n in inner for n in NOT_READ):
                    with_line.append((rel, repo, inner, int(start), lapsed))
    print("citations of sibling code:", dict(tally))
    print("by repository:", dict(by_repo.most_common()))
    print("by kind of record:", dict(by_kind.most_common()))
    print("lines:", dict(lines_ok))
    print("may have lapsed, by kind of record:", dict(lapse_by_kind.most_common()))
    if "--sample" in sys.argv:
        n, out = int(sys.argv[sys.argv.index("--sample") + 1]), Path(sys.argv[sys.argv.index("--sample") + 2])
        random.seed(20261127)
        # Half from those that may have lapsed, half from the rest, so both are read.
        picked = []
        for flag in (True, False):
            pool = [c for c in with_line if c[4] is flag]
            picked += random.sample(pool, min(n // 2, len(pool)))
        out.write_text("\n".join(f"{r} | {repo}/{p}:{line} | {'may have lapsed' if lapsed else 'unchanged since'}"
                                  for r, repo, p, line, lapsed in picked) + "\n", encoding="utf-8")
        print(f"sample of {len(picked)} written")


if __name__ == "__main__":
    main()
