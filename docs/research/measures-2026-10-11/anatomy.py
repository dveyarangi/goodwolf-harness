"""What a token is spent on: usage fields, and API calls by the tool they end in."""
import collections
import glob
import json
import os
import sys

root = sys.argv[1]
fields = collections.Counter()
calls = collections.Counter()
by_tool = collections.Counter()
ctx = []
for path in glob.glob(os.path.join(root, "*.jsonl")):
    msgs = {}
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        m = d.get("message") or {}
        if d.get("type") != "assistant" or not isinstance(m, dict) or not m.get("usage"):
            continue
        e = msgs.setdefault(m.get("id"), {"u": m["usage"], "tools": []})
        for c in m.get("content") or []:
            if isinstance(c, dict) and c.get("type") == "tool_use":
                name = c.get("name", "")
                if name == "Bash":
                    cmd = (c.get("input") or {}).get("command", "")
                    name = "Bash:script" if ".agents/scripts" in cmd or "unittest" in cmd else ("Bash:git" if cmd.lstrip().startswith(("git", "cd")) and "git " in cmd else "Bash:other")
                e["tools"].append(name)
    for e in msgs.values():
        u = e["u"]
        t = 0
        for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"):
            v = u.get(k, 0) or 0
            fields[k] += v
            t += v
        ctx.append((u.get("cache_read_input_tokens", 0) or 0) + (u.get("cache_creation_input_tokens", 0) or 0) + (u.get("input_tokens", 0) or 0))
        key = e["tools"][0] if e["tools"] else "(text only — a reply)"
        calls[key] += 1
        by_tool[key] += t

T = sum(fields.values())
print(f"API calls: {sum(calls.values())}   tokens: {T / 1e9:.2f}B")
for k, v in fields.most_common():
    print(f"  {k:30s} {v / 1e6:8.0f}M  {100 * v / T:5.1f}%")
ctx.sort()
print(f"context read per call: median {ctx[len(ctx) // 2] / 1e3:.0f}k, p90 {ctx[int(len(ctx) * .9)] / 1e3:.0f}k")
print("\nAPI calls by the tool they end in (calls, share of tokens):")
for k, v in calls.most_common(18):
    print(f"  {k:28s} {v:7d}  {100 * by_tool[k] / T:5.1f}%")
