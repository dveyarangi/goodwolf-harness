"""Steps (API calls), output tokens and user turns per day, from Claude Code transcripts."""
import collections, glob, json, os, sys
steps, out, turns, tot = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
for path in glob.glob(os.path.join(sys.argv[1], "*.jsonl")):
    seen = set()
    for line in open(path, encoding="utf-8", errors="replace"):
        try: d = json.loads(line)
        except ValueError: continue
        day = (d.get("timestamp") or "")[:10]
        if not day: continue
        if d.get("type") == "user" and not d.get("isMeta"):
            c = d.get("message", {}).get("content")
            if isinstance(c, str) or (isinstance(c, list) and any(isinstance(x, dict) and x.get("type") == "text" for x in c)):
                turns[day] += 1
        m = d.get("message") or {}
        u = m.get("usage") if isinstance(m, dict) else None
        if d.get("type") == "assistant" and u and m.get("id") not in seen:
            seen.add(m.get("id")); steps[day] += 1; tot[day] += sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")); out[day] += u.get("output_tokens", 0) or 0
for day in sorted(steps):
    if day >= "2026-10-02": print(day, steps[day], out[day], turns[day], tot[day])
