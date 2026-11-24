import json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
root = Path.home()/".claude/projects"
reg = Path("docs/rule-failures.md").read_text(encoding="utf-8")
hits = []
for m in re.finditer(r"^- [A-Z][A-Za-z ]+ · \S+ · (\S+)[^\n]*(?:\n  [^\n]*)*", reg, re.M):
    g = re.search(r"chat `([0-9a-f-]{36})`", m.group(0))
    if g:
        hits.append((g.group(1), datetime.fromisoformat(m.group(1).replace("Z", "+00:00")) if "T" in m.group(1) else None))
series = {}
def load(chat):
    if chat in series: return series[chat]
    out = []
    for f in root.rglob(chat + ".jsonl"):
        for line in f.open(encoding="utf-8", errors="replace"):
            if '"usage"' not in line: continue
            d = json.loads(line); u = (d.get("message") or {}).get("usage")
            if d.get("type") != "assistant" or not u: continue
            t = datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00"))
            c = sum(u.get(k) or 0 for k in ("cache_read_input_tokens","cache_creation_input_tokens","input_tokens"))
            if c: out.append((t, c))
    series[chat] = sorted(out)
    return series[chat]
band = lambda c: next(b for b in (200,400,600,10000) if c < b*1000)
f = Counter(); e = Counter()
for chat, t in hits:
    s = load(chat)
    if not s or not t: continue
    near = [c for x, c in s if x <= t]
    if not near: continue
    c = near[-1]; f[band(c)] += 1
    print(chat[:8], t.strftime("%m-%d %H:%M"), c//1000, "k")
for chat in series:
    for x, c in series[chat]: e[band(c)] += 1
n, en = sum(f.values()), sum(e.values())
for b in (200,400,600,10000): print(f"<{b}k: failures {f[b]}/{n}; requests {e[b]/en:.0%}")
use = Counter()
since = datetime(2026,11,10,tzinfo=timezone.utc)
chats = 0
for x in (root/"D--Dev-AI-agents").rglob("*.jsonl"):
    if x.stat().st_mtime < since.timestamp(): continue
    seen=set()
    for line in x.open(encoding="utf-8", errors="replace"):
        if '"tool_use"' not in line: continue
        d = json.loads(line)
        if d.get("type") != "assistant": continue
        for b in (d["message"].get("content") or []):
            if b.get("type") == "tool_use": use[b["name"]] += 1
print(use.most_common(40))
