"""Baseline: tokens per Claude Code session, and their split by skill (attributionSkill)."""
import collections
import glob
import json
import os
import statistics
import sys

root = sys.argv[1]
sessions = []
by_skill = collections.Counter()
by_skill_out = collections.Counter()
for path in glob.glob(os.path.join(root, "*.jsonl")):
    tot = out = cread = turns = 0
    first = last = None
    seen = set()
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        ts = d.get("timestamp")
        if ts:
            first = first or ts
            last = ts
        if d.get("type") == "user":
            c = d.get("message", {}).get("content")
            if isinstance(c, str) or (isinstance(c, list) and any(x.get("type") == "text" for x in c if isinstance(x, dict))):
                if not d.get("isMeta"):
                    turns += 1
        m = d.get("message") or {}
        u = m.get("usage") if isinstance(m, dict) else None
        if d.get("type") != "assistant" or not u:
            continue
        mid = m.get("id")
        if mid in seen:  # one API message is split over several lines with the same usage
            continue
        seen.add(mid)
        t = sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))
        tot += t
        out += u.get("output_tokens", 0) or 0
        cread += u.get("cache_read_input_tokens", 0) or 0
        skill = d.get("attributionSkill") or "(none)"
        by_skill[skill] += t
        by_skill_out[skill] += u.get("output_tokens", 0) or 0
    if tot:
        sessions.append((first, tot, out, turns))

sessions.sort()
print(f"sessions with usage: {len(sessions)}")
tots = [s[1] for s in sessions]
outs = [s[2] for s in sessions]
turns = [s[3] for s in sessions]
print(f"tokens/session  median {statistics.median(tots)/1e6:.1f}M  mean {statistics.mean(tots)/1e6:.1f}M  total {sum(tots)/1e9:.2f}B")
print(f"output/session  median {statistics.median(outs)/1e3:.0f}k  total {sum(outs)/1e6:.1f}M")
print(f"user turns/session median {statistics.median(turns)}  total {sum(turns)}")
print(f"tokens per user turn: {sum(tots)/max(1,sum(turns))/1e3:.0f}k")
print("\nby week (sessions, total tokens, tokens/turn):")
weeks = collections.defaultdict(lambda: [0, 0, 0])
for first, t, o, n in sessions:
    import datetime
    w = datetime.date.fromisoformat(first[:10]).isocalendar()[1]
    weeks[w][0] += 1; weeks[w][1] += t; weeks[w][2] += n
for w in sorted(weeks):
    s, t, n = weeks[w]
    print(f"  wk{w}: {s:3d} sessions  {t/1e6:7.0f}M  {t/max(1,n)/1e3:5.0f}k/turn")
print("\nshare by skill (all tokens / output tokens):")
all_t = sum(by_skill.values()); all_o = sum(by_skill_out.values())
for k, v in by_skill.most_common(20):
    print(f"  {k:28s} {100*v/all_t:5.1f}%  {100*by_skill_out[k]/all_o:5.1f}%")
