import json
from datetime import datetime, timezone
from pathlib import Path
a = datetime(2026,11,17,tzinfo=timezone.utc)
tot = peer = 0.0; cold = []; peerturn = []; sims = 0.0
for f in (Path.home()/".claude/projects/D--Dev-AI-agents").rglob("*.jsonl"):
    if f.stat().st_mtime < a.timestamp(): continue
    sub = "subagents" in str(f); ev = []; seen = set()
    for line in f.open(encoding="utf-8", errors="replace"):
        if '"usage"' not in line and '"origin"' not in line: continue
        try: d = json.loads(line)
        except ValueError: continue
        ts = d.get("timestamp")
        if not ts: continue
        t = datetime.fromisoformat(ts.replace("Z","+00:00"))
        if t < a: continue
        o = d.get("origin")
        if d.get("type") == "user" and isinstance(o, dict): ev.append((t, "turn", o.get("kind")))
        m = d.get("message") or {}; u = m.get("usage")
        if d.get("type") == "assistant" and u and m.get("id") not in seen:
            seen.add(m["id"]); ev.append((t, "req", u))
    ev.sort(key=lambda e: e[0]); kind = None; first = False
    for t, w, v in ev:
        if w == "turn": kind, first = v, True; continue
        cr = v.get("cache_read_input_tokens") or 0; cw = v.get("cache_creation_input_tokens") or 0
        w1 = (v.get("cache_creation") or {}).get("ephemeral_1h_input_tokens") or 0
        c = .1*cr + 2*w1 + 1.25*(cw-w1) + 5*(v.get("output_tokens") or 0); tot += c
        if kind == "peer" and not sub:
            peer += c
            if cw > 150000: cold.append((c, cw))
            base = .1*min(cr, 130000) + (2*w1 + 1.25*(cw-w1) if cw <= 150000 else 2*95000) + 5*(v.get("output_tokens") or 0)
            sims += base
print(f"tree {tot/1e6:.1f}M, letters {peer/1e6:.1f}M, cold wakes by letters {len(cold)}: {sum(c for c,_ in cold)/1e6:.1f}M, avg {sum(w for _,w in cold)/max(1,len(cold))/1000:.0f}k")
print(f"same letters to chats cleared (contexts at most 130k, cold first request 95k): {sims/1e6:.1f}M; cold part {len(cold)*.19:.1f}M = {len(cold)*.19e6/tot:.1%}")
