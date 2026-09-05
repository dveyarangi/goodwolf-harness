# Installed harness

**The real skill files live in [`skills/`](./skills/).** Loaders are directory links to that folder:

- Codex — reads `.agents/skills` natively; no link needed.
- Claude Code — `.claude/skills` → `../.agents/skills`
- Cursor — `.cursor/skills` → `../.agents/skills`

This repository consumes its own method the way a recipient project does: the same `.agents/skills`
layout as Meteoscape and Forecast Collector, with this project's facts in `<project-local>` blocks.

The links are tracked as symlinks (mode 120000). Git for Windows writes `core.symlinks=false` on
clone, so they check out as text files. After clone, in this repo only:

```
git config --local core.symlinks true
git checkout -- .claude/skills .cursor/skills
```

Windows needs Developer Mode (Settings → System → For developers) or an elevated prompt to create
a directory symlink. If checkout still yields a file, delete it and run
`mklink /D .claude\skills ..\.agents\skills` (likewise for `.cursor\skills`). Creating these links
is part of the installer's job once it exists; a junction is not an acceptable substitute, git
would track it as a directory.

Which links are actually required is untested. Codex needs none; Cursor documents reading
`.agents/skills` directly; Claude Code may too. The host trials in
[01-0010.0020](../docs/tickets/01-0010.0020-live-alignment-across-hosts.md) settle it.

## What is installed

Bootstrap slices [01-0010.0020](../docs/tickets/01-0010.0020-live-alignment-across-hosts.md) and
[01-0010.0030](../docs/tickets/01-0010.0030-install-ticket.md): `align` (with its ADR, ARCH, EDGE
and GLOSSARY format shelf), `impact`, and `ticket` (with `TICKET-FORMAT.md`), from Meteoscape with
the deltas accepted in the [source selection](../docs/tickets/01-0010-dev-harness-shared-and-local.md#bootstrap-corpus-selection).

The pre-audit July corpus is kept under [`legacy/skills`](../legacy/skills/) as evidence only. Nothing loads it.
