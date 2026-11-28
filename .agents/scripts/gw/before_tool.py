# Mechanism: harness
"""What a host's call before a tool is answered with: a refusal, where the call names a file the
project's list closes to agents.

    python .agents/scripts/gw/before_tool.py --hook <host>    (the host's payload on standard input)
    python .agents/scripts/gw/before_tool.py --line <host>    (one line for a session's start, or nothing)

A project that still holds secrets in files lists them in `local.closed.txt`, beside the entry
file, one path a line from the tree's root. In a tree that keeps the list the installer wires a
host's call before every tool to this script through the hooks' wrapper; a tree without it has no
such call. A call that names a listed file is answered with the host's own form of a refusal and
a reason the agent reads; any other is answered with nothing.

The script exits clean whenever it has decided. Where it cannot decide — a payload it cannot
read, a host it does not know — it fails, and the wrapper refuses the call: a value once printed
stays printed. It holds this one refusal and no table of refusals. The wrapper's refusal where
the script fails is on trial.
"""

# TODO q-hqk736: the wrapper's refusal of every call where this script cannot decide is on trial.

from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath

USAGE = "usage: before_tool.py --hook <host> | --line <host>"
LIST = "local.closed.txt"


def main(argv: list[str], root: Path | None = None) -> int:
    """Answers one call: the refusal on standard output, or nothing. A usage it does not know and
    a payload it cannot read are failures, never a silent pass. `--line` prints what a session's
    start is told of a list the host is not set to hold, and never fails."""
    if len(argv) != 2 or argv[0] not in ("--hook", "--line") or argv[1] not in _REFUSALS:
        print(USAGE, file=sys.stderr)
        return 2
    root = root or Path.cwd()
    closed = listed(root)
    if not closed:
        return 0
    if argv[0] == "--line":
        if said := _unheld(root, closed):
            print(said)
        return 0
    try:
        call = json.loads(sys.stdin.read())
        tool, tool_input = call["tool_name"], call["tool_input"]
    except (ValueError, KeyError, TypeError):
        print("before_tool: the host's payload could not be read", file=sys.stderr)
        return 1
    named = _named(closed, root, tool, tool_input, call.get("cwd"))
    if named:
        print(_REFUSALS[argv[1]](_reason(named)))
    return 0


def listed(root: Path) -> list[str]:
    """The files the tree closes to agents, each as its path from the root with `/` between its
    parts; none where the tree keeps no list."""
    try:
        text = (root / LIST).read_bytes().decode("utf-8-sig", "replace")
    except OSError:
        return []
    paths = []
    for line in text.replace("\r", "").split("\n"):
        line = line.strip().replace("\\", "/")
        if line and not line.startswith("#"):
            paths.append(line.removeprefix("./").lstrip("/"))
    return [path for path in paths if path]


def deny_rule(path: str) -> str:
    """The host's own rule that closes one listed file, in the form its documentation anchors at
    the folder of the settings that hold it."""
    return f"Read(/{path})"


def _unheld(root: Path, closed: list[str]) -> str:
    """One line where the tree keeps a list and the host's committed settings lack the call before
    a tool or a rule for one of its lines; `""` where both stand. A file that cannot be read holds
    neither."""
    try:
        settings = json.loads((root / HOST_FILE).read_text(encoding="utf-8"))
        hooks = [hook for entry in settings["hooks"]["PreToolUse"] for hook in entry["hooks"]]
        wired = any(str(hook.get("command", "")).endswith(ENTRY_ENDS) for hook in hooks)
        rules = settings.get("permissions", {}).get("deny", [])
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        wired, rules = False, []
    bare = [path for path in closed if deny_rule(path) not in rules]
    if wired and not bare:
        return ""
    lacking = "no call before a tool is wired" if not wired else "no rule of the host's stands for " + ", ".join(bare)
    return (
        f"This tree closes files to agents in `{LIST}` and Claude Code is not set to hold it: {lacking}. "
        "Run the harness's update at the ref this tree announces, `harness.py . --update --at <ref>`, "
        "then start a new session."
    )


def _named(closed: list[str], root: Path, tool: str, tool_input: object, cwd: object) -> str:
    """The listed file the call names, or `""`."""
    if not isinstance(tool_input, dict):
        return ""
    base = Path(cwd) if isinstance(cwd, str) and cwd else root
    if tool in _SHELLS:
        command = tool_input.get("command")
        return _is_held(closed, command) if isinstance(command, str) else ""
    if tool not in _PATH_FIELDS:
        return _named_in_any_string(closed, root, base, "", tool_input)
    for field in _PATH_FIELDS[tool]:
        value = tool_input.get(field)
        if not isinstance(value, str) or (field in _PATTERN_FIELDS and _WILDCARD.search(value)):
            continue
        if found := _is_listed(closed, root, base, value):
            return found
    return ""


def _named_in_any_string(closed: list[str], root: Path, base: Path, field: str, value: object) -> str:
    """For a tool the script does not know, an outside server's included: a field named `command`
    is a shell command, and every other string is a path and never text — a helper's prompt and a
    task list's lines pass a host's hook too, and a file's name in them is no call upon the file."""
    if isinstance(value, str):
        return _is_held(closed, value) if field == "command" else _is_listed(closed, root, base, value)
    inner = value.items() if isinstance(value, dict) else ((field, item) for item in value) if isinstance(value, list) else ()
    for key, item in inner:
        if found := _named_in_any_string(closed, root, base, str(key), item):
            return found
    return ""


def _is_held(closed: list[str], command: str) -> str:
    """The listed file a command's text holds: its name as a whole word, in any case. Coarse on
    purpose — a command that only mentions the name is refused too, since a command's folder is
    not known from its text."""
    text = command.casefold()
    for path in closed:
        name = re.escape(path.rsplit("/", 1)[-1].casefold())
        if re.search(rf"(?<![\w.\-]){name}(?![\w.\-])", text):
            return path
    return ""


def _is_listed(closed: list[str], root: Path, base: Path, value: str) -> str:
    """The listed file a path field's value is, made whole against the call's folder; letters
    compared without their case, separators as one."""
    whole = _plain(str(base / value.replace("\\", "/")))
    for path in closed:
        if whole == _plain(str(root / path)):
            return path
    return ""


def _plain(path: str) -> str:
    return PurePosixPath(path.replace("\\", "/")).as_posix().casefold()


def _reason(path: str) -> str:
    return (
        f"`{path}` is closed to agents: the project's list of files that hold secrets, `{LIST}`, names it. "
        "Do not read, search or change it another way. Ask the person for what you need from it."
    )


def _claude_code(reason: str) -> str:
    return json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }})


# The one place that knows a host: its committed settings and how the wrapper's entry there ends,
# the fields of its file tools that hold a path, and its form of a refusal.
HOST_FILE = ".claude/settings.json"
ENTRY_ENDS = "before-tool"
_PATH_FIELDS = {
    "Read": ("file_path",),
    "Edit": ("file_path",),
    "Write": ("file_path",),
    "MultiEdit": ("file_path",),
    "NotebookEdit": ("notebook_path",),
    "Grep": ("path", "glob"),
    "Glob": ("path", "pattern"),
}
# A pattern names a file only where it holds no wildcard: one that merely matches a listed file
# names nothing, and a name is not a value.
_PATTERN_FIELDS = ("glob", "pattern")
_WILDCARD = re.compile(r"[*?\[{]")
_SHELLS = ("Bash", "PowerShell")
_REFUSALS = {"claude-code": _claude_code}


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
