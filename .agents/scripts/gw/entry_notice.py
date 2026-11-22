# Mechanism: harness
"""What a running session is shown of an entry file that changed under it.

    python .agents/scripts/gw/entry_notice.py --hook <host>    (the host's payload on standard input)

A host loads the entry file when a session starts and after it compacts the session's context;
between those a session reasons from the text it loaded, whatever the file has become. This is
the harness mechanism's hook line: the hooks' wrapper runs it before the store's hook and hands
on what it prints, so the text reaches the agent with the message that starts its next turn.

It remembers, per session, the file's text as the session's context holds it. The context taking
the file in anew moves that memory and prints nothing. A message that finds the file other than
the memory prints each passage that differs, as it was and as it is now, and moves the memory —
so one change is printed once, and several between two messages are one notice.
"""

from __future__ import annotations

import difflib
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import questions  # noqa: E402  (path set just above)
import sessions  # noqa: E402

USAGE = "usage: entry_notice.py --hook <host>"
# The name the shape check reads in every tree, `mechanisms.py`; not imported, since this script
# starts before every message and that one loads slowly.
ENTRY_FILE = "AGENTS.md"
# Past this many characters the notice asks for a read instead of carrying lines: the wrapper hands
# it on in an environment variable, a host cuts a hook's output short — Claude Code at 10,000
# characters — and lines longer than the read they stand in for save nothing.
BUDGET = 8000
_FOLLOWED_SHOWN = 80
_HEADING = re.compile(r"#{1,6} \S")


def main(argv: list[str], root: Path | None = None) -> int:
    """Prints the notice or nothing. Run as the hook it exits clean whatever it met: a hook that
    fails can hold back the person's message, and the store's hook, run next on the same payload,
    already names what is wrong with it. Only a call that is not the hook's is refused."""
    if len(argv) != 2 or argv[0] != "--hook":
        print(USAGE, file=sys.stderr)
        return 2
    try:
        said = _line(root or Path.cwd(), argv[1], questions.hook_input())
    except Exception:  # noqa: BLE001 — the boundary to a host: nothing may escape it
        return 0
    if said:
        # The entry file holds glyphs and letters a Windows console's code page cannot write, and
        # the wrapper hands on what it captured as it is, a carriage return at each line's end too.
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", newline="\n")
        print(said)
    return 0


def _line(root: Path, host_name: str, payload: str) -> str:
    """The event read as one of the two acts, or as neither: a host's start and its compaction
    are its context taking the file in anew; its message, where the answer reaches the agent,
    asks what changed since."""
    host, event, tag = questions.session_of(host_name, payload)
    if event is None:
        return ""
    if event == host.starts or event in host.compactions:
        taken_in(root, tag)
        return ""
    if event == host.messages:
        return changed(root, tag)
    return ""


def taken_in(root: Path, tag: str) -> None:
    """The session's context took the entry file in anew — at its start, or after a compaction:
    what it holds is the file as it stands."""
    now = _entry_file(root)
    if now is not None:
        _remember(root, tag, now)


def changed(root: Path, tag: str) -> str:
    """What a message is shown of the entry file: the passages that differ from the text the
    session's context holds, or nothing. A session with no memory — its start seen by no hook —
    is shown nothing, since nothing says what its context holds."""
    now = _entry_file(root)
    if now is None:
        return ""
    held = _remembered(root, tag)
    if held == now:
        return ""
    # Moved before the notice is handed on, and nothing reports back whether it reached the
    # agent: a notice lost on its way is not given again.
    _remember(root, tag, now)
    if held is None:
        return ""
    passages = _passages(_lines(held), _lines(now))
    if not passages:
        return ""
    notice = _notice(passages)
    return notice if len(notice) <= BUDGET else _read_again(passages)


# --- what differs ---------------------------------------------------------------------------------


@dataclass
class Passage:
    """A run of lines that differs, placed in the file as it is now: under the nearest heading
    above it and after the line it follows, which is how a new passage is found in a context that
    holds only the old text."""

    heading: str | None
    follows: str | None
    was: list[str]
    now: list[str]


def _lines(text: str) -> list[str]:
    """The lines that carry text, their endings and trailing spaces aside: a checkout that turns
    line endings, or a blank line come or gone, changes nothing a session reasons from."""
    return [line.rstrip() for line in text.splitlines() if line.strip()]


def _passages(was: list[str], now: list[str]) -> list[Passage]:
    # Every line is matched: left to itself the matcher sets aside lines that recur in a file of
    # two hundred or more, and a rule's recurring lead would then read as changed.
    matcher = difflib.SequenceMatcher(None, was, now, autojunk=False)
    headings = _headings_above(now)
    return [
        Passage(
            headings[new_from],
            now[new_from - 1] if new_from else None,
            was[old_from:old_to],
            now[new_from:new_to],
        )
        for kind, old_from, old_to, new_from, new_to in matcher.get_opcodes()
        if kind != "equal"
    ]


def _headings_above(lines: list[str]) -> list[str | None]:
    """For each line, and for the file's end, the nearest heading above it. A line opening with
    `#` inside a code fence is a comment of the code shown there, never a heading."""
    above: list[str | None] = []
    heading, fenced = None, False
    for line in lines:
        above.append(heading)
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        elif not fenced and _HEADING.match(line):
            heading = line
    return [*above, heading]


# --- what is said ---------------------------------------------------------------------------------


def _notice(passages: list[Passage]) -> str:
    count = "1 passage, below" if len(passages) == 1 else f"{len(passages)} passages, each below"
    head = (
        f"entry file changed: {ENTRY_FILE} differs from the text your context holds — {count} as it was and "
        "as it is now. Read `was` as replaced by `now`; the rest of the file stands as your context holds it. "
        # A host that saves a long hook output to a file leaves only its head in context; the
        # count above and this sentence are within that head.
        "Where this text is cut short, its whole stands at the head of the output the host saved: read it "
        f"there, or read {ENTRY_FILE} again."
    )
    return "\n\n".join([head, *(_said(number, passage) for number, passage in enumerate(passages, 1))])


def _said(number: int, passage: Passage) -> str:
    place = f"under `{passage.heading}`" if passage.heading else "at the file's head"
    if not passage.was:
        return "\n".join([f"{number}. {place}, new{_after(passage)}", "now:", *passage.now])
    if not passage.now:
        return "\n".join([f"{number}. {place}, removed", "was:", *passage.was])
    return "\n".join([f"{number}. {place}", "was:", *passage.was, "now:", *passage.now])


def _after(passage: Passage) -> str:
    """The line a new passage follows, cut where it runs long; nothing where that line is the
    heading already named, or the passage opens the file."""
    followed = passage.follows
    if followed is None or followed == passage.heading:
        return ""
    if len(followed) > _FOLLOWED_SHOWN:
        followed = f"{followed[: _FOLLOWED_SHOWN - 1]}…"
    return f" after `{followed}`"


def _read_again(passages: list[Passage]) -> str:
    count = "1 passage" if len(passages) == 1 else f"{len(passages)} passages"
    return (
        f"entry file changed: {ENTRY_FILE} differs from the text your context holds in {count}, too many "
        f"lines to show here. Read {ENTRY_FILE} again; it replaces the text your context holds."
    )


# --- the file and the memory ----------------------------------------------------------------------


def _entry_file(root: Path) -> str | None:
    entry = root / ENTRY_FILE
    return entry.read_bytes().decode("utf-8", errors="replace") if entry.is_file() else None


def _memory(root: Path, tag: str) -> Path:
    return Path(f"{sessions.memory(root, tag)}.entry")


def _remembered(root: Path, tag: str) -> str | None:
    memory = _memory(root, tag)
    return memory.read_bytes().decode("utf-8", errors="replace") if memory.is_file() else None


def _remember(root: Path, tag: str, text: str) -> None:
    """Written beside and moved into place, so a hook cut short leaves the earlier memory whole
    rather than half a file that the next message would read as a change."""
    memory = _memory(root, tag)
    memory.parent.mkdir(parents=True, exist_ok=True)
    beside = memory.with_name(f"{memory.name}.{os.getpid()}")
    beside.write_bytes(text.encode("utf-8"))
    os.replace(beside, memory)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
