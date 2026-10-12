"""Print an agent's draft reply and the spoken exchanges after it.

    uv run --offline --no-project python show.py <session> <draft line> [exchanges after, default 6]
"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build import spoken, TRANSCRIPTS
sys.stdout.reconfigure(encoding="utf-8")

session, draft = sys.argv[1], int(sys.argv[2])
after = int(sys.argv[3]) if len(sys.argv) > 3 else 6
lines = (TRANSCRIPTS / f"{session}.jsonl").read_text(encoding="utf-8").splitlines()
shown, last = 0, None
for at in range(draft, len(lines)):
    try:
        e = json.loads(lines[at])
    except Exception:
        continue
    if e.get("isSidechain"):
        continue
    s = spoken(e)
    if not s or e["type"] == last:
        continue
    last = e["type"]
    label = "DRAFT" if at == draft else ("PERSON" if e["type"] == "user" else "AGENT")
    print(f"===== {label} (line {at}, {e.get('timestamp','')[:16]})\n{s[:6000] if at == draft else s[:2500]}\n")
    shown += 1
    if shown > after:
        break
