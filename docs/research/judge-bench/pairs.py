"""Every (agent reply, next person message) pair across the transcripts, as JSON lines — the pool
`candidates.json` was triaged from.

    uv run --offline --no-project python docs/research/judge-bench/pairs.py <out.jsonl>
"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build import spoken, TRANSCRIPTS

out = open(sys.argv[1], "w", encoding="utf-8")
n = 0
for path in sorted(TRANSCRIPTS.glob("*.jsonl")):
    events = []
    for at, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("isSidechain"):
            continue
        s = spoken(e)
        if s:
            events.append((at, e["type"], s, e.get("timestamp", "")))
    for i in range(len(events) - 1):
        at, who, said, ts = events[i]
        nat, nwho, nsaid, _ = events[i + 1]
        if who == "assistant" and nwho == "user":
            out.write(json.dumps({"session": path.stem, "draft": at, "request_next": nat, "ts": ts,
                                  "draft_len": len(said), "draft_head": said[:600], "next": nsaid[:800]},
                                 ensure_ascii=False) + "\n")
            n += 1
print(n)
