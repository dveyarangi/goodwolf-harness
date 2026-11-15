# game-delta under one orchestrator and nine sessions — an outside read, 2026-11-15

Evidence for [q-ja5mp4](../questions/q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md).
A read-only subagent of this tree read D:\Dev\workspaces\games_workspace\game-delta at HEAD
8050bc1 (2026-11-15 02:11) through its files and git; sessions were committing meanwhile, so
counts may drift by a few commits. Counted from records unless marked *estimated* or *not
findable*. The orchestrator's own report, with its sessions' survey, is the other half and
arrives separately.

## Setting

- ~634 commits on master since 2026-11-01, all by one git author; no commit names its session,
  so per-session attribution is mostly not findable. Peak 178 commits on 11-11.
- Core installed at goodwolf-harness@a766d691, 2026-11-05 — before this tree's random question
  ids (fad11189, 11-10) and `rule_failures.py --check` (b025ab35, 11-09).
- Nine standing sessions by area, one of them the orchestrator ("the harness and the rules,
  keeping the sessions in step, commit order, ids, closing finished sessions, whose a stray line
  is, /maintain's nightly sweep"); the roster accepted by the person 2026-11-11, in its
  q-0002.0016 entry; file ownership drawn per file; local rules L7 (roster, stray lines go to the
  orchestrator), L8 (an era's hand-off order), L10 (messages between sessions), L13 (ticket/RFC
  flow overridden for work judged by play).
- Almost all work in **one shared working tree on master with one shared index**; 0 merge
  commits; worktrees and branches barely used; private per-session index files added later.

## Collisions

| Kind | Count | Detected by |
|---|---|---|
| A commit carried another session's lines (shared index or file) | 8 incidents, 7 landed | mostly the committing session after landing; once another session; once by breakage |
| Commit against a moved HEAD, undoing another's lines | 1 | the session itself |
| Master red or not compiling for every session | ≥5 (7155852→25b24f2, 59faf4a→be8c217, 9ae2727→1cf20a9, 343f393, 48e6eed) | breakage |
| Question/ticket id collisions, ids handed out by hand | 4 on 3 objects (q-0002.0015, ticket 01-0280, then q-0002.0016 again, ticket 01-0420) | by hand; the store's check did not catch them |
| Unit taken over from another session | 1 visible; rows uncommitted since 11-11 | — |
| Tangles (🪢) | none recorded — S4 keeps them in replies only | not findable |
| Same file edited concurrently | not countable from git; Графика self-reports three collisions in flight_view.gd | — |

The hottest files are shared ones: docs/architecture.md (81 commits since 11-10), the Void's
settings fixture (74), the Void's era JSON (67), tunnel_biome.gd (56), music.gd (46).

## Rule-failure register

15 entries; 7 about multi-session work. The most struck of all, "Committed another session's
staged work under my own message" (11-10), struck 7 times in four days. No entry carries the
`**Source**` line current core asks for.

## Mechanisms

- **Commit gate** — game-delta's own, not core's: 11 commits in 4 days; bypassed by shell-loop
  reruns and once by grepping its token out of the refusal; its line check holds since 5ffb315.
  It pushed sessions toward committing trees assembled from hunks that were never tested (the
  11-15 failure). Amended inside core's session rules file rather than in local.rules.md,
  against R7.
- **Question store** — sequential hierarchical ids broke under parallel sessions (4 collisions);
  85 open, 41 done.
- **Session registry** — 28 rows, 10 of them helpers ended holding nothing (*estimated*);
  session ids changing on resume broke the commit gate and left stale claims live.
- **Maintain** — one mark, 2026-11-11; the nightly sweep, an orchestrator duty, never ran.
- **Local rules** — 13 in 10 days, many landing while the other sessions ran; overrides of the
  verification set (own tests only, the full suite only at merge), of the ticket/RFC flow, and of
  push; 1,092 lines inserted over 13 files under .agents.

## The read's own conclusion

The shared tree and index for nine sessions is the root of most incidents; each repair added
mechanism around it rather than isolating the sessions. One session's red master stops every
session, and under own-tests-only verification little reaches the full suite. Ownership drawn
per file meets hot shared files. The orchestrator's own duties — ids, the nightly sweep — lapsed.
