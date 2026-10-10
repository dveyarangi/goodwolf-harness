"""Per ISO week for one project: what the agent spent (Claude Code transcripts) against what landed (git, question store).

usage: project_weeks.py <transcripts dir> <repo>
"""
import collections
import datetime
import glob
import json
import os
import re
import subprocess
import sys

transcripts, repo = sys.argv[1], sys.argv[2]
METHOD = re.compile(r"^(docs/|\.agents/|\.claude/|\.codex/|\.cursor/|AGENTS\.md|CLAUDE\.md|local\.rules\.md)|\.md$")


def week(day):
    y, w, _ = datetime.date.fromisoformat(day[:10]).isocalendar()
    return f"{y}-w{w:02d}"


def typed(d):
    """A message the person typed — not a tool result, a hook's injection or a host notice."""
    if d.get("type") != "user" or d.get("isMeta") or d.get("isCompactSummary"):
        return False
    c = d.get("message", {}).get("content")
    texts = [c] if isinstance(c, str) else [x.get("text", "") for x in (c or []) if isinstance(x, dict) and x.get("type") == "text"]
    texts = [t.strip() for t in texts if t and t.strip()]
    return bool(texts) and not all(t.startswith(("<", "[Request interrupted", "Caveat:")) for t in texts)


W = collections.defaultdict(collections.Counter)
for path in glob.glob(os.path.join(transcripts, "*.jsonl")):
    seen, started = set(), None
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        ts = d.get("timestamp")
        if not ts:
            continue
        w = week(ts)
        if started is None:
            started = w
            W[w]["sessions"] += 1
        if typed(d):
            W[w]["turns"] += 1
        m = d.get("message") or {}
        u = m.get("usage") if isinstance(m, dict) else None
        if d.get("type") == "assistant" and u and m.get("id") not in seen:
            seen.add(m.get("id"))
            W[w]["steps"] += 1
            W[w]["out"] += u.get("output_tokens", 0) or 0
            W[w]["tok"] += sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))

log = subprocess.run(["git", "-C", repo, "log", "--all", "--no-merges", "--numstat", "--format=@%ad %s", "--date=short"],
                     capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
w = None
for line in log.splitlines():
    if line.startswith("@"):
        w = week(line[1:11])
        W[w]["commits"] += 1
        if line[12:].startswith("FIX"):
            W[w]["fix"] += 1
    elif line.strip() and w:
        parts = line.split("\t")
        if len(parts) == 3 and parts[0].isdigit():
            n = int(parts[0]) + int(parts[1])
            W[w]["method_lines" if METHOD.search(parts[2]) else "code_lines"] += n

for f in glob.glob(os.path.join(repo, "docs", "questions", "done", "*.md")):
    m = re.search(r"^- \*\*answer\*\*.*?(\d{4}-\d{2}-\d{2})", open(f, encoding="utf-8").read(), re.M)
    if m:
        W[week(m.group(1))]["q_closed"] += 1

cols = ["sessions", "turns", "steps", "tok", "out", "commits", "fix", "code_lines", "method_lines", "q_closed"]
print("week      " + " ".join(f"{c:>12s}" for c in cols))
tot = collections.Counter()
for k in sorted(W):
    tot.update(W[k])
    print(f"{k}  " + " ".join(f"{(W[k][c] / 1e6 if c == 'tok' else W[k][c]):12.0f}" for c in cols))
print("total     " + " ".join(f"{(tot[c] / 1e6 if c == 'tok' else tot[c]):12.0f}" for c in cols))
print("(tok in millions)")
