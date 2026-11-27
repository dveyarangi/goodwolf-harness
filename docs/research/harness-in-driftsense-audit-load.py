"""Count the person's load in a project's Claude Code sessions, printing counts only.

Round 2 of the audit in harness-in-driftsense-audit.md. Reads the top-level transcripts of one host
project folder; prints no line of any transcript and no message text: only counts, ages and ids'
first 8 characters. A forked session's copied records count once, by their ids.

- The person's messages: records the host marks as the person's turn, its own reminders taken out,
  one per prompt.
- Asked to explain: such a message matching a request for meaning or explanation, in Russian or
  English — a pattern, so a count to read as an estimate; beside it, the messages holding a `?`.
- Reading: the words of the agent's text in the turns the person started, from one message of the
  person to the next; turns another session or the host started are left out.
- Decisions waiting: the rows of a reply's `⚖️ Decisions` table; a row is the same decision while
  its words are, or with `--loose` while its first five are; its age runs from the first table that
  shows it to the last, across sessions; only tables in turns the person started.
- Asked by the host's own means: AskUserQuestion calls, and wrap-ups that carry a question.

Usage: python -I harness-in-driftsense-audit-load.py <host project folder> [--loose]
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
import statistics
import sys
from datetime import datetime
from pathlib import Path

REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
EXPLAIN = re.compile(
    r"\b(поясни|объясни|разъясни|растолкуй|не понял|не понимаю|непонятн|что (значит|такое|ты имеешь)|в смысле|"
    r"explain\b|what (does|do|is|are) .{0,40}\bmean\b|what do you mean|i don'?t (get|understand)|unclear)",
    re.I,
)
LOOSE = "--loose" in sys.argv  # a row is the same decision while its first five words are
DECISIONS = re.compile(r"^\|\s*⚖️\s*Decisions\s*\|", re.M)


def text_of(content) -> str:
    if isinstance(content, list):
        return " ".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return content if isinstance(content, str) else ""


def decision_rows(text: str) -> list[str]:
    """The rows under a reply's decisions table, hashed; the header and its rule left out."""
    match = DECISIONS.search(text)
    if not match:
        return []
    rows = []
    for line in text[match.end():].splitlines()[1:]:
        line = line.strip()
        if not line.startswith("|"):
            break
        if re.fullmatch(r"\|[\s|:-]*\|?", line):
            continue
        words = re.sub(r"[*_`|~\[\]()]", " ", line).lower().split()
        key = " ".join(words[:5]) if LOOSE else " ".join(words)
        rows.append(hashlib.sha256(key.encode()).hexdigest())
    return rows


def when(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def main() -> None:
    folder = Path(sys.argv[1])
    seen_records: set[str] = set()
    seen_prompts: set[str] = set()
    totals = collections.Counter()
    reading: list[int] = []
    first: dict[str, tuple[datetime, int]] = {}
    last: dict[str, tuple[datetime, int]] = {}
    shown = 0
    open_at_end: list[int] = []
    widest: list[int] = []
    print("session | messages | asked to explain | with a question mark | median words read per message | "
          "decision tables shown | most at once | left at end | AskUserQuestion | wrap-up asks")
    for top in sorted(folder.glob("*.jsonl"), key=lambda p: p.stat().st_mtime):
        s = collections.Counter()
        origin = None
        words = 0
        per_message: list[int] = []
        last_text_rows: list[str] | None = None
        most = 0
        for line in top.open(encoding="utf-8", errors="replace"):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            uuid = record.get("uuid")
            if uuid and uuid in seen_records:
                continue
            if uuid:
                seen_records.add(uuid)
            kind = record.get("type")
            if kind == "user" and not record.get("isSidechain") and record.get("turnOrigin"):
                # A turn belongs to whoever started it: the person, another session, the host.
                origin = record["turnOrigin"]
                if origin == "human" and not record.get("isCompactSummary"):
                    typed = REMINDER.sub("", text_of(record.get("message", {}).get("content"))).strip()
                    prompt = record.get("promptId") or uuid
                    if typed and prompt not in seen_prompts:
                        seen_prompts.add(prompt)
                        if s["messages"]:
                            per_message.append(words)
                        words = 0
                        s["messages"] += 1
                        s["explain"] += bool(EXPLAIN.search(typed))
                        s["question_mark"] += "?" in typed
            if kind != "assistant" or record.get("isSidechain") or origin != "human":
                continue
            message = record.get("message", {})
            for block in message.get("content", []) or []:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use":
                    name = block.get("name", "")
                    given = block.get("input") if isinstance(block.get("input"), dict) else {}
                    s["ask_tool"] += name == "AskUserQuestion"
                    s["wrap_ask"] += name.endswith("wrap_up") and bool(given.get("ask"))
                    continue
                if block.get("type") != "text":
                    continue
                text = block.get("text", "")
                words += len(text.split())
                rows = decision_rows(text)
                last_text_rows = rows
                if not rows:
                    continue
                shown += 1
                s["tables"] += 1
                stamp = when(record.get("timestamp"))
                for row in rows:
                    first.setdefault(row, (stamp, shown))
                    last[row] = (stamp, shown)
                most = max(most, len(rows))
        if s["messages"]:
            per_message.append(words)
        open_at_end.append(len(last_text_rows or []))
        widest.append(most)
        reading.extend(per_message)
        totals.update(s)
        print(f"{top.stem[:8]} | {s['messages']} | {s['explain']} | {s['question_mark']} | "
              f"{statistics.median(per_message) if per_message else 0:.0f} | {s['tables']} | "
              f"{most} | {len(last_text_rows or [])} | {s['ask_tool']} | {s['wrap_ask']}")
    print("\ntotals:", dict(totals))
    if reading:
        print(f"words read per message of the person, in the turns it started: median {statistics.median(reading):.0f}, "
              f"upper quartile {statistics.quantiles(reading, n=4)[2]:.0f}, largest {max(reading)}, all {sum(reading)}")
    if first:
        hours = {row: (last[row][0] - first[row][0]).total_seconds() / 3600 for row in first}
        spans = {row: last[row][1] - first[row][1] + 1 for row in first}
        again = [row for row in first if spans[row] > 1]
        print(f"distinct decisions shown: {len(first)}; shown in one table only: {len(first) - len(again)}")
        if again:
            q = lambda xs: (statistics.median(xs), statistics.quantiles(xs, n=4)[2], max(xs))
            print("shown again: %d; tables apart median %.0f, upper quartile %.0f, largest %d; "
                  "hours median %.1f, upper quartile %.1f, largest %.1f"
                  % (len(again), *q([spans[r] for r in again]), *q([hours[r] for r in again])))
        print(f"most decisions in one table: {max(widest)}; standing in a session's last reply: "
              f"{sum(open_at_end)} across {sum(1 for n in open_at_end if n)} sessions")


if __name__ == "__main__":
    main()
