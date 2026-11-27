# q-wjv4mi How does Claude Code refuse an agent's call that names a file on the project's list of secret holders?

- **record of** what it intends to become
- **part of** q-v6bnoz
- **state** open
- **owner** [01-0120.0010](../tickets/01-0120.0010-claude-code-refuses-a-call-that-names-a-listed-file.md)
- **rung** development: load-bearing, self-improvement: the method
- **lean** 2026-11-27, the user: held by both - the host own deny rule for every listed file, and the hook; decision 1. Being built: docs/rfc/01-0120.0010, stage 1
- **opened** 2026-11-26T22:00:50Z
- **struck** 0, last 2026-11-26T22:00Z

## Decisions

1. **Claude Code's refusal is held by both: its own deny rule and the hook** *(the user,
   2026-11-27: "Обоими", of the three put to them after the live try — the hook alone, the
   host's rule alone, both)*. The rule, written from the list, is the floor and holds a search
   over a folder; the hook gives the reason and holds a shell's any command. What the try saw of
   each: [Claude Code's sidecar](../edge/hosts/claude-code.md), **Call refusal**. Its cost, put
   with it: the installer writes a rule for every listed file beside the hook's entry.
