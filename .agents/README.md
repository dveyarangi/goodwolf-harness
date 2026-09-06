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

Bootstrap slices [01-0010.0020](../docs/tickets/01-0010.0020-live-alignment-across-hosts.md),
[01-0010.0030](../docs/tickets/01-0010.0030-install-ticket.md),
[01-0010.0035](../docs/tickets/01-0010.0035-install-spec.md),
[01-0010.0040](../docs/tickets/done/01-0010.0040-install-plan.md),
[01-0010.0050](../docs/tickets/01-0010.0050-install-implement.md),
[01-0010.0060](../docs/tickets/01-0010.0060-install-verify.md), and
[01-0010.0070](../docs/tickets/done/01-0010.0070-install-maintain.md): `align` (with its ADR, ARCH, EDGE
and GLOSSARY format shelf), `impact`, `ticket` (with `TICKET-FORMAT.md`), `spec`, `plan`,
`implement`, `tdd` (with its five files), `improve-comments`, `verify`, and `maintain`, from
Meteoscape with the Forecast Collector `/plan` body, per the
[source selection](../docs/tickets/01-0010-dev-harness-shared-and-local.md#bootstrap-corpus-selection).
`maintain` composes the selected `denoise` and `sync-arch` and adds the `<temporary>` enumerator.

[01-0010.0090](../docs/tickets/done/01-0010.0090-install-discover.md) adds `discover` (with its
`EVIDENCE.md`). It came from a different estate and so is not in the audited source selection above,
which records only what was taken from Meteoscape, Forecast Collector and DriftSense; that ticket is
its authority. It is used the way `impact` is — run it, use what comes back in the work at hand —
and files nothing.

The pre-audit July corpus is kept under [`legacy/skills`](../legacy/skills/) as evidence only. Nothing loads it.

## Mechanical support

[`scripts/`](./scripts/) holds what `/maintain` derives and repairs mechanically: `move_doc.py`
closes a ticket and its RFC together and repairs the citations, `temporary_statements.py` reads
and retires expiring statements, and `docs_corpus.py` is the one view of the tree they share.
They run on the standard library alone. Their behavioral tests are in [`tests/`](../tests/) and
are part of the project's [verification set](../docs/process.md#verification).
