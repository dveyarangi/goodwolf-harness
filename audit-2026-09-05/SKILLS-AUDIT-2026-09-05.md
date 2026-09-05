# Skills corpus audit — 2026-09-05

> **Superseded 2026-09-05** by [REPORT.md](REPORT.md), which corrects this file: M and A do have `tdd/tests.md`; no `skill-up` carries a real `<project-local>` block; counts are H 13/22, M 21/33, A 21/36, F 19/30; F has four skill-path commits; `skills-main` is Matt Pocock's collection; Codex discovers `.agents/skills` natively. Kept as evidence only.

Four in-scope copies, plus three out-of-scope lineages found on the way.

| Key | Path | Skills / files | Git | Last skill change | Loader links |
|---|---|---|---|---|---|
| H | `D:\Dev\AI\.agents\skills` | 13 / 22 | none | 2026-07-21 | none (nothing loads it) |
| M | `D:\Dev\AI\meteoscape\.agents\skills` | 21 / 32 | tracked, ~30 `SKILL:` commits | 2026-08-24 | `.claude/skills`, `.codex/skills`, `.cursor/skills` → `../.agents/skills` |
| A | `D:\Dev\DriftSense\workspace\agents\skills` | 23 / 35 | own nested repo (untracked in `workspace`), 3 commits | 2026-08-24 | `.cursor/skills` → `../skills` only. No `.claude`, no `.codex` |
| F | `D:\Dev\DriftSense\workspace\forecast_collector\.agents\skills` | 21 / 30 | tracked, 5 `SKILL:` commits | 2026-09-03 | `.claude/skills`, `.claude/codex` (stray), `.codex/skills`, `.cursor/skills` → `../.agents/skills` |

`D:\Dev\AI\agents` (the intended canonical home) does not exist yet.

## Lineage

```
skills-main (Anthropic repo, Jun 12)  --tdd/* only-->  H
H (Jul)  -->  M (evolved Jul - Aug 24, git)
                |--> A  (copied Aug 12, re-synced ~Aug 24, then Notion-flavoured)
                '--> M/.agents/skills.zip (Aug 26, byte-identical to M) --> F (seeded Aug 27, evolved to Sep 3)
weather-mcp/.cursor/skills (Jun, 7 skills: align, conclude, denoise, review-architecture, tdd, to-issues, write-prd) - ancestor of H
life/.agents/skills (24 skills, every overlapping file differs from M, own conventions: EVIDENCE.md, skills-unused/) - separate lineage, out of scope
life-2 - Aug 26 copy of life, no git
```

Every copy is CRLF except the five `tdd/*.md` appendix files inherited LF from skills-main. Not a
discrepancy, but the sync mechanic must normalise line endings or every diff is noise.

## Per-file matrix (md5 prefix)

```
FILE                              H          M          A          F
advise/SKILL.md                   2fddb8     7c6130     7c6130     b58247   F reverted to H wording
align/ADR-FORMAT.md               d33ec2     063d75     063d75     063d75
align/ARCH-FORMAT.md              d47e04     64d335     64d335     e623a6   F: trailing newline only
align/CONCERNS-FORMAT.md          -          -          b4eaad     -        A-only, portable
align/EDGE-FORMAT.md              -          aa56ad     f42d49     2031ab   A: link retarget; F: CRLF only
align/GLOSSARY-FORMAT.md          34d091     34d091     34d091     010428   F: +project-local
align/SKILL.md                    6eac71     6c955d     40a1dd     141f73   A: cites CONCERNS-FORMAT; F: +project-local
celebrate/SKILL.md                -          e533c2     e533c2     e533c2
commit/SKILL.md                   -          2f9726     a05435     0de1db   project-local only
conclude/SKILL.md                 83eb67     f74ee4     f74ee4     404c91   F: CRLF only
denoise/SKILL.md                  3d14c4     1708cf     1708cf     b6aed4   F: +project-local
dream/SKILL.md                    -          3f7c1f     3f7c1f     -        F lacks
edge/SKILL.md                     -          c98ca9     c98ca9     -        F lacks
impact/SKILL.md                   -          ef978c     ef978c     48ac96   F: +trigger phrase in description
implement/SKILL.md                93aed5     722560     722560     8b7d4a   F: +project-local
improve-comments/SKILL.md         b5c376     b69dbe     b69dbe     b69dbe
plan-impl/SKILL.md                85611f     007afa     007afa     8fb07a   F: body tweak + project-local
recall/SKILL.md                   -          bad240     38fc13     c937a4   A: project-local; F: +body rule +project-local
review-architecture/REFERENCE.md  f40250     75b632     75b632     75b632   H keeps old issue template (dropped Aug 7)
review-architecture/SKILL.md      4e2654     e0e342     e0e342     e0e342
review-impl/SKILL.md              -          1599e1     1599e1     e61ccf   F: +"use /implement to amend"
setup-devops/SKILL.md             a2b20b     9b98c5     9b98c5     9b98c5
skill-up/SKILL.md                 -          ae7cf5     185fa5     ae7cf5   A is BEHIND (pre-Aug-24 wording)
sync-arch/SKILL.md                520cf6     40d0f4     6283bb     e0ded4   A: whitespace; F: +project-local
tdd/{deep-modules,interface-design,mocking,refactoring}.md   identical everywhere
tdd/SKILL.md                      7ca080     2611d6     2611d6     2611d6
tdd/tests.md                      253c99     MISSING    MISSING    253c99   M and A have a broken link to it
to-spec/INITIATIVE-FORMAT.md      -          -          37636a     -        A-only, arguably portable
to-spec/SKILL.md                  b6c593     10101e     5728a1     a90981   A: +initiative step; F: newline only
to-tickets/NOTION-FORMAT.md       -          -          551f71     -        A-only, project-local (Notion tracker)
to-tickets/SKILL.md               bf763d     419307     3e31bf     556f44   A: Notion minting; F: +3.1 impact check
to-tickets/TICKET-FORMAT.md       -          36d380     62621a     59b990   three different documents by design
workflow.excalidraw               -          yes        -          -
```

## Who is ahead of whom

- **H is behind everything.** Every shared file is older; 8 skills and 4 appendices exist only downstream. Nothing in H is worth porting except `tdd/tests.md` (which M and A lost) and the `advise` wording that F independently returned to.
- **M is the trunk.** Richest git history, the source of both A and F. Its state as of 2026-08-24 is the common ancestor of A and F.
- **A = M + Notion process.** Body changes are confined to `to-spec`, `to-tickets`, `align` (all pointing at A-only appendices) and `<project-local>` blocks. One regression: `skill-up/SKILL.md` is the pre-Aug-24 version (lost "fixing defects as you port" and "A skill present in only one corpus is either local by intent or not yet ported — ask which").
- **F = M + ten days of real use.** The only copy with body-level improvements since the fork, in five commits (Aug 29 – Sep 3). Candidates to port into canonical:
  1. `recall`: an open ticket whose work landed but whose criteria are unchecked is the next session's first item.
  2. `review-impl`: "Use /implement to amend found discrepancies".
  3. `plan-impl`: "Repeat validation using same /plan-impl skill".
  4. `to-tickets`: step 3.1, run /impact on the proposed split.
  5. `impact`: description gains a trigger phrase ("Use when asked to check impact of issue or it's slice").
  6. `advise`: rewritten back toward the H wording (dropped "hidden edges", merged questionable/missing). Preference or regression — needs your call.

  F also drops `dream`, `edge`, `workflow.excalidraw`, and trims `TICKET-FORMAT.md` (removed cross-release lines and the illustrative examples).

## Project-local surface (what the sync must leave alone)

| Copy | `<project-local>` blocks | Local appendices |
|---|---|---|
| H | none | none |
| M | commit, recall, skill-up | TICKET-FORMAT (numbered queue) |
| A | commit, recall, skill-up | TICKET-FORMAT (Notion), NOTION-FORMAT, CONCERNS-FORMAT, INITIATIVE-FORMAT |
| F | align, GLOSSARY-FORMAT, commit, denoise, implement, plan-impl, recall, skill-up, sync-arch | TICKET-FORMAT (single release) |

The `skill-up` skill already states the contract: bodies are portable, `*-FORMAT.md` / `REFERENCE.md`
appendices and `<project-local>` blocks are local. Two frictions today: `skill-up` carries a
`<project-local>` block in every copy although it is a body skill, and `TICKET-FORMAT.md` is treated
as fully local in all three copies while its first half (numbering rules, status vocabulary, ticket
shape) is near-identical prose.

## Non-skill harness pieces that ride along

- `scripts/move_doc.py`: three variants. M uses `uv run` and `path.read_text`; F uses `./venv/Scripts/python.exe` and explicit `open`; A is a third hash. Logic identical, invocation line is project-local.
- F-only: `scripts/plan_impl_loop.py` + `.cursor/hooks.json` + `.cursor/hooks/plan_impl_loop.cmd` (Cursor re-invokes /plan-impl until the RFC reads `Pass: 3`). Cursor-specific; Claude Code and Codex have no equivalent registered.
- `README.md` in each `.agents`: three different texts for the same symlink recipe; F's is the most complete (covers all three loaders). M and A READMEs also carry two agent-instruction bullets that belong in `CLAUDE.md`/rules, not in the harness README.
- Home-level: `~/.cursor/skills` has 5 unrelated skills; `~/.claude/skills` and `~/.codex/skills` are empty. No global loader points at any corpus.

## Loader coverage per framework

| Project | Claude Code | Codex | Cursor |
|---|---|---|---|
| meteoscape | yes, symlink | yes, symlink | yes, symlink |
| DriftSense/agents | no | no | yes, symlink |
| forecast_collector | yes, symlink (+ stray `.claude/codex`) | yes, symlink | yes, symlink + hooks |
| `.agents` (H) | no | no | no |

## Where the /align skill is

- Newest body: `D:\Dev\AI\meteoscape\.agents\skills\align\SKILL.md` (Aug 24, 8.5 KB) with ADR/ARCH/EDGE/GLOSSARY formats; A adds CONCERNS-FORMAT.
- H's copy (Jul 17, 4.9 KB) is stale.
- Nothing under `D:\Dev\AI\.agents` is loadable by Claude Code today: there is no `.claude/skills` link here, so `/align` is not in this session's skill list.
