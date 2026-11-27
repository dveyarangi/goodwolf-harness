# q-wjv4mi How does Claude Code refuse an agent's call that names a file on the project's list of secret holders?

- **record of** what it intends to become
- **part of** q-v6bnoz
- **state** open
- **owner** [01-0120.0010](../tickets/01-0120.0010-claude-code-refuses-a-call-that-names-a-listed-file.md)
- **rung** development: load-bearing, self-improvement: the method
- **lean** 2026-11-27: built through stage 4 of docs/rfc/01-0120.0010 - the script, the wrapper, the installer wiring with the host own rule for every listed file, the records; held by both, decision 1. Not done: the harness skill lines, shown to the person and waiting; stage 5, the refusal seen live in a tree with a list
- **opened** 2026-11-26T22:00:50Z
- **struck** 0, last 2026-11-26T22:00Z

## Decisions

1. **Claude Code's refusal is held by both: its own deny rule and the hook** *(the user,
   2026-11-27: "Обоими", of the three put to them after the live try — the hook alone, the
   host's rule alone, both)*. The rule, written from the list, is the floor and holds a search
   over a folder; the hook gives the reason and holds a shell's any command. What the try saw of
   each: [Claude Code's sidecar](../edge/hosts/claude-code.md), **Call refusal**. Its cost, put
   with it: the installer writes a rule for every listed file beside the hook's entry.

## What a recipient's sessions show, 2026-11-27

Round 5 of [the audit of the harness in DriftSense](../research/harness-in-driftsense-audit.md),
told to the keeper, counted there by hash and never printed. Over three days of that tree's
sessions in Claude Code, values shaped like a secret reached a session's context in 9 sessions of
23. Tool calls that read a file holding secrets came to 77, more than half of them on one
settings file the product's own code is built around; 163 more named such a file only in a
search.

What it bears on here:

- The print is common, not rare, where the secrets still stand in files.
- The file most read is one an agent has ordinary reason to read, so the refusal will be met
  often, and the reader of
  [01-0120.0020 an-agent-reads-a-listed-file-without-its-values](../tickets/01-0120.0020-an-agent-reads-a-listed-file-without-its-values.md)
  is what makes the refusal livable there.
- A search for text that mentions a listed file is told apart from a search of the file: the
  first passes, the second is refused — as the script stands.
