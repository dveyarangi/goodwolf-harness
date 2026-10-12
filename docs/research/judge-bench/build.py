"""Rebuild the bench's specimens from the transcripts they were cut from.

    uv run --offline --no-project python docs/research/judge-bench/build.py

Each specimen is the person's message, the two exchanges before it, and the agent's draft reply,
read from the Claude Code transcript named in `key.json`. The transcripts live on the machine
that recorded them, so this reruns there alone; the specimens in `specimens/` are its output,
kept so the bench runs anywhere.
"""

import json
import os
from pathlib import Path

HERE = Path(__file__).parent
TRANSCRIPTS = Path(os.path.expanduser("~/.claude/projects/D--Dev-AI-agents"))
CONTEXT_TURNS = 4  # two exchanges before the person's message
CONTEXT_CHARS = 2500
REQUEST_CHARS = 5000


def text_of(message: dict) -> str:
    content = message.get("content")
    if isinstance(content, str):
        return content
    return "\n".join(part["text"] for part in content or [] if isinstance(part, dict) and part.get("type") == "text")


def spoken(event: dict) -> str | None:
    """The text a person or the agent said in this event, or None for tool traffic and harness text."""
    if event.get("type") not in ("user", "assistant") or "message" not in event:
        return None
    text = text_of(event["message"]).strip()
    if not text or "system-reminder" in text[:40]:
        return None
    if text.startswith(("<local-command", "Base directory", "<task-notification")):
        return None
    if event["type"] == "assistant" and len(text) < 300:
        return None  # a progress note between tool calls, not a reply
    return text


def cut(text: str, limit: int) -> str:
    return text if len(text) <= limit else text[:limit] + "\n[... truncated ...]"


def specimen(entry: dict) -> str:
    lines = (TRANSCRIPTS / f"{entry['session']}.jsonl").read_text(encoding="utf-8").splitlines()
    event = lambda at: json.loads(lines[at])
    request = entry["request"]
    if request is None:
        request = next(at for at in range(entry["draft"] - 1, -1, -1) if event(at).get("type") == "user" and spoken(event(at)))
    before, at = [], request - 1
    while at >= 0 and len(before) < CONTEXT_TURNS:
        said = spoken(event(at))
        if said and (not before or before[-1][0] != event(at)["type"]):
            before.append((event(at)["type"], said))
        at -= 1
    out = ["## Earlier in the conversation\n"]
    for who, said in reversed(before):
        out.append(f"**{'Person' if who == 'user' else 'Agent'}:**\n\n{cut(said, CONTEXT_CHARS)}\n")
    out.append(f"## The person's message\n\n{cut(spoken(event(request)) or '', REQUEST_CHARS)}\n")
    out.append(f"## The agent's draft reply\n\n{spoken(event(entry['draft']))}\n")
    return "\n".join(out)


def main() -> None:
    key = json.loads((HERE / "key.json").read_text(encoding="utf-8"))
    (HERE / "specimens").mkdir(exist_ok=True)
    for label, entry in key.items():
        (HERE / "specimens" / f"{label}.md").write_text(specimen(entry), encoding="utf-8")
        print(label)


if __name__ == "__main__":
    main()
