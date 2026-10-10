"""Per ISO week, Codex sessions whose cwd is one of the given paths: sessions, typed turns, tokens.

usage: codex_weeks.py <cwd> [<cwd> ...]
"""
import collections
import datetime
import glob
import json
import os
import sys

want = {os.path.normcase(os.path.normpath(p)) for p in sys.argv[1:]}
W = collections.defaultdict(collections.Counter)
for path in glob.glob(os.path.expanduser("~/.codex/sessions/*/*/*/*.jsonl")):
    cwd, last, w = None, None, None
    turns = collections.Counter()
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        p = d.get("payload") or {}
        if cwd is None and isinstance(p, dict) and p.get("cwd"):
            cwd = os.path.normcase(os.path.normpath(p["cwd"]))
            if cwd not in want:
                break
        ts = d.get("timestamp")
        if ts and w is None:
            y, n, _ = datetime.date.fromisoformat(ts[:10]).isocalendar()
            w = f"{y}-w{n:02d}"
        if d.get("type") == "event_msg" and p.get("type") == "task_started":
            turns[w] += 1
        if d.get("type") == "event_msg" and p.get("type") == "token_count" and (p.get("info") or {}).get("total_token_usage"):
            last = p["info"]["total_token_usage"]
    if cwd not in want or w is None:
        continue
    W[w]["sessions"] += 1
    W[w]["turns"] += sum(turns.values())
    if last:
        W[w]["tok"] += last.get("total_tokens", 0) or 0
        W[w]["cached"] += last.get("cached_input_tokens", 0) or 0
        W[w]["out"] += (last.get("output_tokens", 0) or 0)
        W[w]["reasoning"] += last.get("reasoning_output_tokens", 0) or 0

cols = ["sessions", "turns", "tok", "cached", "out", "reasoning"]
print("week      " + " ".join(f"{c:>10s}" for c in cols))
tot = collections.Counter()
for k in sorted(W):
    tot.update(W[k])
    print(f"{k}  " + " ".join(f"{(W[k][c] / 1e6 if c in ('tok', 'cached') else W[k][c]):10.0f}" for c in cols))
print("total     " + " ".join(f"{(tot[c] / 1e6 if c in ('tok', 'cached') else tot[c]):10.0f}" for c in cols))
print("(tok, cached in millions)")
