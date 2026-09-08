# maintain — rules installed into skills this mechanism does not own

Machine input for the installer, read by nobody at session time. One section per rule, each
naming its target, its anchor and its tier, and stating its authority. The section grammar is
[01-0011.0020](../../../docs/tickets/01-0011.0020-rules-one-home.md)'s; this file is written to
the shape that ticket states and is installed by nothing until its installer exists.

## What an inceptor hands `/maintain`

- **target** `.agents/skills/mechanism/SKILL.md`
- **anchor** `## Incept`
- **tier** 2 — read when incepting a mechanism
- **authority** strict — the user, 2026-09-07

Name what `/maintain` must do for this mechanism — a maintainer script to run, records to
re-check when its surfaces move — as rules in its rules file targeting `/maintain`. Nothing is
written into `/maintain` by hand.
