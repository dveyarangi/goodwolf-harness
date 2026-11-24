"""Was the skill an act needs in the session's context when the act was made?

Usage: skill_use.py <a project's transcripts directory> [<rows.csv to write>]

Read from Claude Code's transcripts; calls no model. A one-off read, kept so the numbers can be
read again; no mechanism's part. One row per file, turn and kind of act, the skill's state taken
at the turn's first such act; an act a forked or resumed transcript copies is counted once, in the
transcript that starts earliest.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

EDITS = {"Edit", "Write", "MultiEdit"}
SHELLS = {"Bash", "PowerShell"}
LOADERS = {"Skill", "SlashCommand"}

INSTRUCTION = re.compile(
    r"(?:^|[\\/])(?:AGENTS\.md|CLAUDE\.md|local\.rules\.md)$"
    r"|[\\/]mechanisms[\\/][^\\/]+[\\/][^\\/]*rules\.md$"
    r"|[\\/]skills[\\/][^\\/]+[\\/][^\\/]+\.md$",
    re.I,
)
SCRATCH = re.compile(r"[\\/](?:Temp|tmp|scratchpad)[\\/]", re.I)
TICKET = re.compile(r"[\\/]docs[\\/]tickets[\\/](?!README)[^\\/]+\.md$", re.I)
PLAN = re.compile(r"[\\/]docs[\\/]rfc[\\/](?!README)[^\\/]+\.md$", re.I)
PRODUCT = re.compile(r"[\\/]docs[\\/]product\.md$", re.I)
EDGE = re.compile(r"[\\/]docs[\\/]edge[\\/].+\.md$", re.I)
COMMIT = re.compile(r"\bgit\s+(?:-[cC]\s+\S+\s+)*commit\b")
FRAME = "\U0001F9E9 **Proposed rule"
SKILL_FILE = re.compile(r"[\\/]skills[\\/]([\w-]+)[\\/]SKILL\.md$", re.I)
TYPED = re.compile(r"<command-name>/?([\w:-]+)</command-name>")
# a shell command that prints a skill's file, and one that writes an instruction file
SHELL_READ = re.compile(
    r"\b(?:cat|head|tail|less|more|type|bat|Get-Content|gc|sed\s+-n)\b[^|;&\n]*?skills[\\/]([\w-]+)[\\/]SKILL\.md",
    re.I,
)
SHELL_PATH = (r"(?:AGENTS\.md|local\.rules\.md|skills[\\/][\w-]+[\\/][\w.-]+\.md"
              r"|mechanisms[\\/][\w-]+[\\/][\w.-]*rules\.md)")
SHELL_WRITE = re.compile(
    rf"(?:write_text|write_bytes|sed\s+-i|Set-Content|Out-File|open\([^)]*['\"][wa]['\"])[\s\S]*{SHELL_PATH}"
    rf"|{SHELL_PATH}[\s\S]*(?:write_text|write_bytes)"
    rf"|>>?\s*[\"']?[\w./\\-]*{SHELL_PATH}",
    re.I,
)

SHELL_MADE = "an instruction file written through the shell, by a pattern's guess"

# act, the skill it needs, the instant (UTC) that skill entered the tree
ENTERED = "2026-09-06T21:44:57"
RECENT = "2026-11-01"
ACTS = (
    ("an instruction file edited", "skill-up", ENTERED),
    (SHELL_MADE, "skill-up", ENTERED),
    ("a rule's frame drawn in a reply", "skill-up", ENTERED),
    ("a ticket written new", "ticket", "2026-09-06"),
    ("a plan written new", "plan", "2026-09-06"),
    ("a commit made", "commit", ENTERED),
    ("the product document edited", "product", "2026-10-13"),
    ("an edge record edited", "edge", "2026-09-09"),
)
SKILL = {act: skill for act, skill, _ in ACTS}
SINCE = {act: since for act, _, since in ACTS}
CONFIRMED = {"a ticket written new", "a plan written new"}  # held until the host says the file was created
STATES = ("invoked in the turn", "invoked earlier, no compaction between",
          "carried across a compaction", "its file read, not invoked", "neither")


def acts_of(part) -> list[tuple[str, str]]:
    """Each act a part of a reply makes, with the way it was made."""
    if part.get("type") == "text":
        return [("a rule's frame drawn in a reply", "reply")] if FRAME in part.get("text", "") else []
    if part.get("type") != "tool_use":
        return []
    name, given = part.get("name"), part.get("input") or {}
    if name in SHELLS:
        command = str(given.get("command", ""))
        found = [("a commit made", "shell")] if COMMIT.search(command) else []
        if SHELL_WRITE.search(command):
            found.append((SHELL_MADE, "shell"))
        return found
    if name not in EDITS:
        return []
    path = str(given.get("file_path", ""))
    if SCRATCH.search(path):
        return []
    found = []
    if INSTRUCTION.search(path):
        found.append("an instruction file edited")
    if name == "Write" and TICKET.search(path):
        found.append("a ticket written new")
    if name == "Write" and PLAN.search(path):
        found.append("a plan written new")
    if PRODUCT.search(path):
        found.append("the product document edited")
    if EDGE.search(path):
        found.append("an edge record edited")
    return [(act, "tool") for act in found]


def invoked_by(part) -> list[str]:
    if part.get("type") != "tool_use" or part.get("name") not in LOADERS:
        return []
    given = part.get("input") or {}
    asked = str(given.get("skill") or given.get("command") or "").strip()
    return [asked.split()[0].lstrip("/").rsplit(":", 1)[-1]] if asked else []


def read_by(part) -> list[str]:
    """The skills whose file a tool call prints: the host's Read, or the shell."""
    if part.get("type") != "tool_use":
        return []
    name, given = part.get("name"), part.get("input") or {}
    if name == "Read":
        found = SKILL_FILE.search(str(given.get("file_path", "")))
        return [found.group(1)] if found else []
    if name in SHELLS:
        return SHELL_READ.findall(str(given.get("command", "")))
    return []


def text_of(entry) -> str:
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return content
    return " ".join(part.get("text", "") for part in content or [] if isinstance(part, dict))


def starts_a_turn(entry) -> bool:
    if entry.get("type") != "user" or entry.get("isMeta") or entry.get("isCompactSummary"):
        return False
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    parts = [part for part in content or [] if isinstance(part, dict)]
    return any(part.get("type") == "text" for part in parts) and not any(
        part.get("type") == "tool_result" for part in parts
    )


def created(entry) -> list[str]:
    """The tool calls this entry reports as having created a file."""
    result = entry.get("toolUseResult")
    if not isinstance(result, dict) or result.get("type") != "create":
        return []
    content = (entry.get("message") or {}).get("content") or []
    return [part.get("tool_use_id") for part in content
            if isinstance(part, dict) and part.get("type") == "tool_result"]


def first_instant(path: Path) -> str:
    with path.open(encoding="utf-8", errors="replace") as lines:
        for line in lines:
            found = re.search(r'"timestamp":"([^"]+)"', line)
            if found:
                return found.group(1)
    return "9"


def read(path: Path, seen: set) -> list[dict]:
    turn = 0
    invoked: dict[str, list] = {}  # skill -> [the turn it was invoked in, compactions since]
    printed: dict[str, int] = {}  # skill -> the turn its file was last printed in, since the last compaction
    rows: dict[tuple, dict] = {}
    waiting: dict[str, tuple] = {}  # tool call -> the row it makes once the host confirms it
    with path.open(encoding="utf-8", errors="replace") as lines:
        for line in lines:
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            kind = entry.get("type")
            if entry.get("subtype") == "compact_boundary":
                printed = {}
                for held in invoked.values():
                    held[1] += 1
                continue
            attachment = entry.get("attachment") or {}
            if kind == "attachment" and attachment.get("type") == "invoked_skills":
                # what the host carried across the compaction; the rest it dropped
                names = [skill.get("name", "").rsplit(":", 1)[-1] for skill in attachment.get("skills") or []]
                invoked = {name: invoked.get(name, [None, 1]) for name in names if name}
                continue
            for call in created(entry):
                if call in waiting:
                    key, row = waiting.pop(call)
                    rows.setdefault(key, row)
            if starts_a_turn(entry):
                turn += 1
                for name in TYPED.findall(text_of(entry)):
                    invoked[name.rsplit(":", 1)[-1]] = [turn, 0]
                continue
            if kind != "assistant":
                continue
            instant = entry.get("timestamp", "")
            day = instant[:10]
            message = entry.get("message") or {}
            for part in message.get("content") or []:
                if not isinstance(part, dict):
                    continue
                for name in invoked_by(part):
                    invoked[name] = [turn, 0]
                for name in read_by(part):
                    printed[name] = turn
                for act, way in acts_of(part):
                    mark = (part.get("id") or message.get("id") or entry.get("uuid"), act)
                    if mark in seen:
                        continue
                    seen.add(mark)
                    if (turn, act) in rows or instant < SINCE[act]:
                        continue
                    held = invoked.get(SKILL[act])
                    if held is not None and held[1]:
                        state, age = STATES[2], held[1]
                    elif held is not None:
                        state, age = STATES[0 if held[0] == turn else 1], 0
                    elif SKILL[act] in printed:
                        state, age = STATES[3], ""
                    else:
                        state, age = STATES[4], ""
                    row = {
                        "session": path.stem[:8], "day": day, "week": week(day), "turn": turn,
                        "act": act, "made through": way, "skill": SKILL[act], "state": state,
                        "compactions since the load, at least": age,
                    }
                    if act in CONFIRMED:
                        waiting[part.get("id")] = ((turn, act), row)
                    else:
                        rows[(turn, act)] = row
    return list(rows.values())


def week(day: str) -> str:
    try:
        year, number, _ = date.fromisoformat(day).isocalendar()
    except ValueError:
        return "?"
    return f"{year}-W{number:02d}"


def share(count: int, whole: int) -> str:
    return f"{count} ({int(100 * count / whole + 0.5)} %)" if whole else "0"


def table(head: list[str], lines: list[list]) -> None:
    print("| " + " | ".join(head) + " |")
    print("|" + "---|" * len(head))
    for line in lines:
        print("| " + " | ".join(str(cell) for cell in line) + " |")
    print()


def by(rows: list[dict], key) -> dict:
    grouped = defaultdict(Counter)
    for row in rows:
        grouped[key(row)][row["state"]] += 1
    return grouped


def states(counts: Counter) -> list:
    whole = sum(counts.values())
    return [whole] + [share(counts[state], whole) for state in STATES]


def main(projects: Path, out: Path | None) -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    files = sorted(projects.glob("*.jsonl"), key=first_instant)
    seen: set = set()
    rows = [row for path in files for row in read(path, seen)]
    days = sorted(row["day"] for row in rows if row["day"])
    print(f"{len(files)} transcripts; {len(rows)} rows, one per transcript, turn and kind of act, "
          f"{days[0]} to {days[-1]}\n")
    head = ["rows", *STATES]

    print("By act\n")
    grouped = by(rows, lambda row: row["act"])
    counted = [act for act, _, _ in ACTS if act != SHELL_MADE]
    table(["act", "skill", *head], [[act, f"`/{SKILL[act]}`", *states(grouped[act])] for act in counted])

    print(f"By act, from {RECENT}\n")
    recent = by([row for row in rows if row["day"] >= RECENT], lambda row: row["act"])
    table(["act", "skill", *head], [[act, f"`/{SKILL[act]}`", *states(recent[act])] for act in counted])

    guess = grouped[SHELL_MADE]
    print(f"Beside the tables, a pattern's guess: {sum(guess.values())} rows where a shell command looks to have "
          f"written an instruction file, {sum(guess[state] for state in STATES[:3])} of them with the skill "
          f"invoked or carried.\n")

    print("By month, every act together\n")
    grouped = by([row for row in rows if row["act"] != SHELL_MADE], lambda row: row["day"][:7])
    table(["month", *head], [[month, *states(grouped[month])] for month in sorted(grouped)])

    print("By week, an instruction file edited and a rule's frame drawn\n")
    rules = [row for row in rows if row["skill"] == "skill-up" and row["act"] != SHELL_MADE]
    grouped = by(rules, lambda row: row["week"])
    table(["week", *head], [[name, *states(grouped[name])] for name in sorted(grouped)])

    print("Carried loads: how many compactions old at least, and in how many transcripts\n")
    ages, sessions = Counter(), defaultdict(set)
    for row in rows:
        if row["state"] == STATES[2]:
            age = row["compactions since the load, at least"]
            name = "1" if age == 1 else "2 or 3" if age <= 3 else "4 to 9" if age <= 9 else "10 or more"
            ages[name] += 1
            sessions[name].add(row["session"])
    table(["compactions since the load, at least", "rows", "transcripts"],
          [[name, ages[name], len(sessions[name])] for name in ("1", "2 or 3", "4 to 9", "10 or more")])

    if out:
        with out.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(sorted(rows, key=lambda row: (row["day"], row["session"], row["turn"])))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]) if len(sys.argv) > 2 else None)
