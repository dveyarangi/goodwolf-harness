"""Count what a project's Claude Code sessions cost, printing counts only.

Round 1 of the audit in harness-in-driftsense-audit.md. Reads every transcript in one host
project folder, the subagents' with their parent's; prints no line of any transcript, no command,
no path and no message text: only counts, ids' first 8 characters, tool, skill and category names.

A forked session copies its parent's records: an API call, a tool call and a message are counted
once across the folder, by their ids, in the first session read that holds them.

A call's tokens are mostly the cached context it re-reads; its share goes whole to what the call's
tools worked on, split evenly between them. A share says what the calls did, not what the context
they carried held.

Usage: python -I harness-in-driftsense-audit-cost.py <host project folder> [--repo <git tree>]
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

METHOD = re.compile(
    r"\.agents[/\\]|docs[/\\](questions|sessions)[/\\]|rule-failures|AGENTS\.md|CLAUDE\.md|local\.rules"
)
CODE = re.compile(r"workspace[/\\](?!agents)[\w.-]+[/\\]")
RECORDS = re.compile(r"docs[/\\]")
SCRATCH = re.compile(r"[Tt]e?mp[/\\]|scratchpad")
HOST_FILES = re.compile(r"\.claude[/\\]")
METHOD_TOOLS = {"Skill", "SendMessage", "ListAgents"}
HOST_TOOLS = {"ToolSearch", "SubagentHandback", "Artifact", "SendUserFile"}
TOKENS = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
AGENT_ID = re.compile(r"^a[0-9a-f]{15,}$")


def category(name: str, given: dict) -> str:
    """Name what a tool call works on; the first that fits wins, in the order below."""
    if name in METHOD_TOOLS:
        return "method"
    if name in HOST_TOOLS or name.startswith("mcp__ccd_") or name.startswith("Task"):
        return "host"
    if name == "Agent":
        return "subagent"
    if name in ("WebFetch", "WebSearch") or name.startswith(("mcp__Claude_Browser", "mcp__claude-in-chrome")):
        return "web"
    if "notion" in name:
        return "board"
    if name.startswith("mcp__a8cdb81f"):
        return "mail (counted, never read)"
    text = " ".join(str(given.get(k, "")) for k in ("file_path", "path", "command", "pattern", "glob"))
    if name in ("Bash", "PowerShell") and re.match(r"\s*(cd \S+ *(&&|;) *)?git ", text):
        return "git"
    if METHOD.search(text):
        return "method"
    if CODE.search(text):
        return "product code"
    if RECORDS.search(text):
        return "product records"
    if SCRATCH.search(text):
        return "scratch"
    if HOST_FILES.search(text):
        return "host files"
    return "other"


def tool_input(block: dict) -> dict:
    given = block.get("input")
    return given if isinstance(given, dict) else {}


class Seen:
    """What the folder has counted already, so that a fork's copies count once."""

    def __init__(self) -> None:
        self.calls: set[str] = set()
        self.tools: set[str] = set()
        self.records: set[str] = set()
        self.prompts: set[str] = set()


def count(files: list[Path], seen: Seen) -> dict:
    tally = {
        "human": 0, "received": [], "sent": 0, "calls": 0, "tools": collections.Counter(),
        "skills_called": collections.Counter(), "tokens": collections.Counter(),
        "by_category": collections.Counter(), "by_skill": collections.Counter(),
        "first": None, "last": None, "subagents": sum("subagents" in f.parts for f in files),
    }
    usage: dict[str, tuple[dict, str]] = {}
    cats: dict[str, list[str]] = collections.defaultdict(list)
    for path in files:
        for line in path.open(encoding="utf-8", errors="replace"):
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            uuid = record.get("uuid")
            fresh = not uuid or uuid not in seen.records
            if uuid:
                seen.records.add(uuid)
            stamp = record.get("timestamp")
            if fresh and stamp and "subagents" not in path.parts:
                tally["first"] = min(filter(None, [tally["first"], stamp]))
                tally["last"] = max(filter(None, [tally["last"], stamp]))
            if record.get("type") == "user" and fresh and not record.get("isCompactSummary"):
                origin = record.get("turnOrigin")
                content = record.get("message", {}).get("content")
                if isinstance(content, list):
                    content = " ".join(b.get("text", "") for b in content if isinstance(b, dict))
                if origin == "human" and "subagents" not in path.parts and not record.get("isSidechain"):
                    # The host writes a reminder into the person's record; a record holding only
                    # that is not a message, and one message may span records of one prompt.
                    typed = re.sub(r"<system-reminder>.*?</system-reminder>", "", str(content), flags=re.S).strip()
                    prompt = record.get("promptId") or uuid
                    if typed and prompt not in seen.prompts:
                        seen.prompts.add(prompt)
                        tally["human"] += 1
                elif origin == "peer":
                    tally["received"].append(hashlib.sha256(str(content).encode()).hexdigest())
            if record.get("type") != "assistant":
                continue
            message = record.get("message", {})
            key = message.get("id")
            if not key or (key in seen.calls and key not in usage):
                continue  # a call another session of the folder already counted
            if key not in usage:
                seen.calls.add(key)
                tally["calls"] += 1
            spent = {k: int((message.get("usage") or {}).get(k) or 0) for k in TOKENS}
            usage[key] = (spent, record.get("attributionSkill") or "(none)")
            for block in message.get("content", []) or []:
                if not isinstance(block, dict) or block.get("type") != "tool_use":
                    continue
                if block.get("id") in seen.tools:
                    continue
                seen.tools.add(block.get("id"))
                name = block.get("name", "?")
                given = tool_input(block)
                tally["tools"][name] += 1
                cats[key].append(category(name, given))
                if name == "Skill":
                    tally["skills_called"][str(given.get("skill", "?"))[:40]] += 1
                if name == "SendMessage":
                    to = str(given.get("to", ""))
                    if to != "main" and not AGENT_ID.match(to):
                        tally["sent"] += 1
    for key, (spent, skill) in usage.items():
        total = sum(spent.values())
        tally["tokens"].update(spent)
        tally["by_skill"][skill] += total
        kinds = cats.get(key) or ["reply only"]
        for kind in kinds:
            tally["by_category"][kind] += total / len(kinds)
    return tally


def commits(repo: Path, since: str) -> collections.Counter:
    """Count a tree's commits since a day by the step its subject's head names."""
    out = subprocess.run(["git", "-C", str(repo), "log", f"--since={since}", "--format=%s"],
                         capture_output=True, text=True, encoding="utf-8").stdout
    heads = collections.Counter()
    for subject in out.splitlines():
        match = re.match(r"([A-Z][A-Z-]+):", subject)
        heads[match.group(1) if match else "(no step)"] += 1
    return heads


def main() -> None:
    folder = Path(sys.argv[1])
    repo = Path(sys.argv[sys.argv.index("--repo") + 1]) if "--repo" in sys.argv else None
    seen = Seen()
    totals = collections.Counter()
    by_category, by_skill = collections.Counter(), collections.Counter()
    skills, tools = collections.Counter(), collections.Counter()
    hashes: list[str] = []
    first = None
    print("session | span | human | calls | tokens (M) | output (k) | tool calls | subagents | sent | received")
    for top in sorted(folder.glob("*.jsonl"), key=lambda p: p.stat().st_mtime):
        sid = top.stem
        t = count([top, *sorted((folder / sid).glob("subagents/*.jsonl"))], seen)
        spent = sum(t["tokens"].values())
        print(f"{sid[:8]} | {(t['first'] or '')[:16]}..{(t['last'] or '')[11:16]} | {t['human']} | {t['calls']} | "
              f"{spent / 1e6:.1f} | {t['tokens']['output_tokens'] / 1e3:.0f} | {sum(t['tools'].values())} | "
              f"{t['subagents']} | {t['sent']} | {len(t['received'])}")
        first = min(filter(None, [first, t["first"]]))
        totals.update(t["tokens"])
        for k in ("human", "calls", "subagents", "sent"):
            totals[k] += t[k]
        totals["sessions"] += 1
        by_category.update(t["by_category"])
        by_skill.update(t["by_skill"])
        skills.update(t["skills_called"])
        tools.update(t["tools"])
        hashes.extend(t["received"])
    spent = sum(totals[k] for k in TOKENS)
    print("\ntotals:", {k: totals[k] for k in sorted(totals)}, f"all tokens {spent / 1e6:.1f}M")
    print("\ntokens by what the call's tools worked on (share):")
    for kind, n in by_category.most_common():
        print(f"  {kind}: {n / spent:.1%}")
    print("\ntokens by the skill the host attributes the call to (share):")
    for skill, n in by_skill.most_common(15):
        print(f"  {skill}: {n / spent:.1%}")
    print("\nskills called:", dict(skills.most_common()))
    print("\ntool calls:", dict(tools.most_common(20)))
    repeats = sum(n - 1 for n in collections.Counter(hashes).values() if n > 1)
    print(f"\nmessages received from other sessions: {len(hashes)}, of them exact repeats: {repeats}")
    if repo and first:
        print(f"\ncommits by step since {first[:10]}:", dict(commits(repo, first[:10]).most_common()))


if __name__ == "__main__":
    main()
