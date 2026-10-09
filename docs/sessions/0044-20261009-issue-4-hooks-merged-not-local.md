# Session 44 — 2026-10-09: issue 4, core's hooks merged into the shared files, never a local one

Session `39bde226`. Asked to look at the new issue on the board:
[issue 4](https://github.com/dveyarangi/goodwolf-harness/issues/4), every fresh install ending
`arrived: false` because the three hosts' hook files the questions mechanism declares as parts are
never carried. The gap was already q-0018.0020.0005; the issue added two things the store did not
hold — a failed gate's report hides its reason, and the hook commands need `uv`.

## Decisions

- **Taken now, out of the queue's order** *(the user)*: "берём".
- **Merge, not carry** *(the user)*: core's hooks are merged into each host's file; carrying
  `.claude/settings.json` whole would overwrite a project's own settings.
- **The interpreter: found once per clone, read by a wrapper** *(the user)*. The user first chose a
  bare `python`. On this tree's own machine a bare `python` is the Microsoft Store stub, which runs
  nothing, and macOS and Linux often carry only `python3`; put to the user, they proposed the
  interpreter be found once and written to a file of the clone's own, with every hook run through a
  wrapper that reads it. Weighed: it rides the per-clone step `--links` already is; its cost is the
  wrapper, which must start without Python in whatever shell each host runs a hook in.
- **No local settings file** *(the user)*: "нет, никакого local". The host documentation read this
  session showed Claude Code merges hooks across `settings.json` and `settings.local.json`, so
  core's hooks could have gone into the uncommitted local file with an absolute interpreter path and
  no wrapper. Refused: Codex and Cursor have no local file, and one shape across the three hosts was
  preferred. The user had asked whether `settings.json` is meant to be committed at all: it is,
  for all three hosts — which is exactly why a machine's interpreter path cannot go in it.
- **Three tickets, core's hook entries authored under `.agents/`** *(the user)*: `/impact`
  recommended narrowing two slices to three — the merge alone makes an install arrive; the
  interpreter carries the only live, per-host unknowns; the gate's report is independent of both.
  Its assessment is on [01-0010](../tickets/01-0010-dev-harness-shared-and-local.md), *Hook wiring
  reaches a recipient*.

## What was done

- Opened q-0018.0020.0009, a failed gate saying why, from the issue.
- Read each host's documentation on hook files and shells and filed it with sources in
  q-0018.0020.0005's body.
- Recorded the `/impact` on the parent ticket.

## What went wrong

A parallel session, branched from this conversation, minted the three tickets
([`.0173`](../tickets/done/01-0010.0173-an-install-merges-cores-hooks-into-each-hosts-file.md),
[`.0174`](../tickets/done/01-0010.0174-each-hook-finds-its-interpreter.md),
[`.0176`](../tickets/done/01-0010.0176-a-failed-gate-says-why.md)), aligned `.0173` and wrote its RFC
while this one was still presenting the breakdown. Nothing was duplicated: the sessions file and
`git log` showed it before minting. Two sessions carrying one decision path at once is
q-0032's case; the check that caught it was reading the tree before writing, not a lock.

## Open questions touched

- **q-0018.0020.0005** — the merge is `.0173`'s, under way in another session at
  q-0018.0020.0005.0001; the interpreter is `.0174`'s, at q-0018.0020.0005.0002, waiting on
  `.0173` and on each host's Windows shell observed live — Cursor's is undocumented.
- **q-0018.0020.0009** — `.0176`, Ready, AFK, nobody on it; it edits the installer's gate, which
  `.0173` also edits.

## What continues

`.0173` in the session already on it. The next session here: `.0176` once `.0173` has landed, so
the two do not edit `harness.py` at once.
