"""Per week: tokens and user turns against units of work done — tickets closed, acceptance boxes checked."""
import collections
import datetime
import glob
import json
import os
import re
import sys

transcripts, tickets = sys.argv[1], sys.argv[2]


def week(day):
    return datetime.date.fromisoformat(day).isocalendar()[1]


tok = collections.Counter()
turns = collections.Counter()
for path in glob.glob(os.path.join(transcripts, "*.jsonl")):
    seen = set()
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        ts = d.get("timestamp")
        if not ts:
            continue
        w = week(ts[:10])
        if d.get("type") == "user" and not d.get("isMeta"):
            c = d.get("message", {}).get("content")
            if isinstance(c, str) or (isinstance(c, list) and any(isinstance(x, dict) and x.get("type") == "text" for x in c)):
                turns[w] += 1
        m = d.get("message") or {}
        u = m.get("usage") if isinstance(m, dict) else None
        if d.get("type") == "assistant" and u and m.get("id") not in seen:
            seen.add(m.get("id"))
            tok[w] += sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))

done = collections.Counter()
boxes = collections.Counter()
for path in glob.glob(os.path.join(tickets, "*.md")):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"Done \((\d{4}-\d{2}-\d{2})\)", text)
    if not m:
        continue
    w = week(m.group(1))
    done[w] += 1
    boxes[w] += len(re.findall(r"^\s*- \[x\]", text, re.M))

print("week  tokens  turns  tickets  boxes  | Mtok/ticket  turns/ticket  Mtok/box  turns/box")
for w in sorted(set(tok) | set(done)):
    t, n, k, b = tok[w] / 1e6, turns[w], done[w], boxes[w]
    per = lambda x, y: f"{x / y:8.0f}" if y else "       -"
    perf = lambda x, y: f"{x / y:8.1f}" if y else "       -"
    print(f"wk{w}  {t:6.0f}M {n:5d}  {k:6d}  {b:5d}  | {per(t, k)}  {per(n, k)}     {perf(t, b)}  {perf(n, b)}")
T, N, K, B = sum(tok.values()) / 1e6, sum(turns.values()), sum(done.values()), sum(boxes.values())
print(f"all   {T:6.0f}M {N:5d}  {K:6d}  {B:5d}  | {T / K:8.0f}  {N / K:8.0f}     {T / B:8.1f}  {N / B:8.1f}")
