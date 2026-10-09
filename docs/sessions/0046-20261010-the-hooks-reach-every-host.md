# Session 46 — the hooks reach every host

**2026-10-09 to 2026-10-10.** Claude Code, one conversation, resumed by its host under three ids
(`53bad90a…`, `93929df3…`, `e588cd44…`). Entry contract v44 at the start, v50 by the end, raised
by parallel sessions. It began from a transcript the user pasted: the harness installed into a
fresh study folder, `D:\Dev\AI\studies`, and the questions it raised.

## What was decided, and what chose it

### The core-copy check is maintenance, never verification — q-0018.0012

- The installing agent had put `harness.py . --check` into the study tree's verification set.
  Measured: five seconds, all of it a whole clone of the harness repository over the network, on
  every `/verify`.
- The first amendment let it into the set "when the person asks". The user refused that: *how
  would a user know why? it is not part of verification at all, it is part of maintain; and it has
  to be offered with its product reason*; and *to be added, it must be fast*. The skill now offers
  nothing for the set; [01-0010.0180](../tickets/01-0010.0180-harness-names-its-maintenance.md)
  carries the re-check, reading no network and offered with its reason — an edit made inside core
  is caught when it is made, rather than at the next update.
- A second amendment, "each rule of the local file is the person's", was refused as untrue: *it
  can be the agent's*. The format already says authority is whoever decided; what went wrong in
  the study tree was the agent's choice signed with the user's name. [Rule failure
  26](../rule-failures.md) records both.

### Core's hooks are merged into each host's file — 01-0010.0173

- The split into three slices was approved. Where core's hook entries are authored took a second
  explanation; the user chose a file under `.agents/` over reading the origin's own host files,
  which would carry whatever this tree puts there for itself.
- The user: *why not just call it settings.json and copy?* Copying was refuted: a project that
  already uses Claude Code has its own `.claude/settings.json`, an absent-only copy would freeze
  core's hooks forever, and an update would erase the project's own. The naming was right, and
  the agent's Markdown shelf with fenced JSON blocks gave way to three JSON files at their host
  files' own paths under `.agents/skills/questions/hooks/` — the destination is the path, and the
  installer holds no host path.

### Every hook is launched by Git — 01-0010.0174

- A throwaway probe folder, run by the user in Claude Code and Cursor, showed what no
  documentation said: Claude Code runs a hook under Git Bash, Cursor under Windows PowerShell 5.1,
  where neither `sh` nor a bare `x.cmd` resolves. The planned pair of wrappers, POSIX and `cmd`,
  was dropped for one: `git -c "alias.gw-hook=!sh .agents/scripts/gw/hook.sh" gw-hook <host>` runs
  in Git Bash, PowerShell and `cmd`, from the repository's top level whatever folder the shell
  stands in. Git is already required of every tree core reaches.
- The interpreter record moved from an excluded `.agents/interpreter` to the clone's Git
  directory: no exclude line, invisible to the listing, never committable.
- Codex needed a current CLI (`0.162`; the installed `0.1.2505…` had no hooks) and an API key.
- The user: *do not describe anything in the skill* — the two-step update a pre-shelf recipient
  needs stays in the RFC.

### A dropped target loses its block on the next install — 01-0011.0120

From the study tree's agent: removing L3 left its block in `verify/SKILL.md`, and it had to
restore the old local file byte for byte to retract it. Installing now removes its own source's
block from every file the rules file no longer names, by retraction's cut.

## What was done

- [01-0010.0173](../tickets/done/01-0010.0173-an-install-merges-cores-hooks-into-each-hosts-file.md),
  [01-0010.0174](../tickets/done/01-0010.0174-each-hook-finds-its-interpreter.md),
  [01-0010.0176](../tickets/done/01-0010.0176-a-failed-gate-says-why.md) (a failed gate reports
  the script's diagnostics, not its closing brackets) and
  [01-0011.0120](../tickets/done/01-0011.0120-a-dropped-target-loses-its-block.md) — minted,
  planned, built, verified and closed with their RFCs.
- Live: an install from a scratch clone into an empty folder arrived; an update of a copy of the
  study tree left its hand-copied hooks unchanged; the hooks delivered the window in all three
  hosts and with neither `uv` nor `python` on the path.
- The front page's `uv` caveat and the product matrix's partial row retired with q-0018.0020.0005.
- Charts of tickets and questions over the git history, for the user: 80 tickets, 36 live; 142
  questions open, 39 closed, the open count growing faster than closures.

## A principle with no home yet

**Probe a host's undocumented behaviour before the plan names a command for it.** The RFC's first
draft fixed two wrappers from documentation; ten minutes of probing replaced them with one. Where
this belongs — `/plan`'s *cheapest real example*, or a rule of its own — is unsettled.

## What went wrong

- The first amendment of the harness skill overreached twice before it was right; each was landed
  and committed before the user read it.
- Twice the agent edited a record through `sed` rather than the edit tool, against the user's
  standing preference that edits be visible as they happen.
- The suite's guard against a test touching the live question store tripped on parallel sessions'
  writes three or four times per run, a different test each time; each passed alone. It is
  q-0032's.

## Open questions touched

- **q-0018.0020.0003** — a first install's verification set: the skill now leaves it empty without
  a toolchain; its shape still waits on q-0018.0022.0001.
- **q-0018.0012** — what `/maintain` re-checks for the harness: the core-copy re-check, fast and
  offered, waits on 01-0010.0180.
- **q-0018.0020** — the hook wiring is done; the loader-link misjudgement, the first install's last
  step and the release flow remain.

## What continues

The queue's next item. The study tree can take `--update` twice — to a ref holding `.0173`, then
to the head — to replace its hand-copied `uv` hooks.
