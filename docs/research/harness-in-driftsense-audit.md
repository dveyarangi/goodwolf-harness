# The harness in DriftSense — the audit's health records

The audit of [q-2iboch](../questions/q-2iboch-how-does-the-harness-fare-in-a-project-that-runs-it-judged-by-what-it-promises-first-audited-in.md),
by the method its body holds, a section per round.

## Round 0 — the baseline, 2026-11-27

What DriftSense already holds against core: its rule-failure register (7 entries), the 17 lessons it
sent, [recipient-lessons-2026-11-24](recipient-lessons-2026-11-24.md), and its 15 local rules. Each is
marked by its cause, once per cause, against core at `4ea662fa`, 184 commits after `ed0f4e1d`, the
core DriftSense runs.

Read: DriftSense's `docs/rule-failures.md` and `local.rules.md` at its working tree of 2026-11-27, the
lessons file, core's rules files, scripts and questions by search. No transcript was read.

| cause | where DriftSense holds it | in core |
|---|---|---|
| a question opened below the dial | lesson 1; L7 | **sent, no record**: told the store's session 2026-11-24; Q1 unchanged, no question holds it |
| urgent work | lesson 2; L9 | open: [q-4a4iit](../questions/q-4a4iit-how-does-urgent-work-go-through-the-method-small-or-wide-and-what-record-does-it-leave-after.md) |
| hazards weigh nothing | lesson 3; L11 | **fixed**: [q-6y4lwm](../questions/q-6y4lwm-how-does-a-hazard-which-leads-to-no-answer-of-the-product-weigh-in-what-comes-next.md) decided; hazards stand above the board's rows, `.agents/skills/pathfinder/SKILL.md:20` |
| silent zeros where status lives on another board | lesson 4; L12 | **fixed**: `9e37df11`, the path reads unread where no ticket carries a status |
| a promise made in a reply | lesson 5 | **fixed**: `c40e6217`, entry contract v141 |
| a per-clone part an update does not write | lesson 6 | open: [q-t5vmk3](../questions/q-t5vmk3-how-does-core-reach-a-recipient-tree-and-leave-it-working-at-a-first-install-and-at-each-update.md) |
| "install it with overwrite" misread | lesson 7 | open: q-t5vmk3 |
| a renamed skill leaves a project's links dead | lesson 8 | open: q-t5vmk3 |
| the edge check reads its folder's README | lesson 9 | **received, no holder**: `edges.py:123` still reads every `*.md`; no role names the edge mechanism |
| one chat as two sessions | lesson 10 | open: [q-hz2br4](../questions/q-hz2br4-how-is-one-chat-kept-from-standing-as-two-sessions-one-its-host-named-and-one-a-bare-wake-did.md) |
| a rule's override does not reach the script that carries it out | lesson 11; L3, L4 | open: [q-veooj7](../questions/q-veooj7-how-do-projects-share-one-development-method-without-losing-their-own-conventions.md) |
| friction beside a rule's failure | lesson 12 | open: [q-f7p2oh](../questions/q-f7p2oh-does-self-improvement-also-register-friction-work-that-succeeds-slowly-and-will-be-repeated-and-what-is.md) |
| pace: the task in hand against improvements | lesson 13 | open: [q-jn54hg](../questions/q-jn54hg-how-does-a-session-split-its-effort-between-the-task-in-hand-and-improvements-for-later-and-where-is.md) |
| a secret's value printed into a session's context | lesson 14; register 2026-11-25 | open, in work: [q-v6bnoz](../questions/q-v6bnoz-how-is-a-secrets-value-kept-out-of-what-a-session-prints-into-its-context.md), ticket 01-0120.0010 |
| hazards are found by nobody | lesson 15 | open: [q-hes7m3](../questions/q-hes7m3-who-finds-the-hazards-of-a-tree-and-does-maintain-flag-them.md) |
| what the nightly pass covers and tells the next | lesson 16 | open: [q-tug2bm](../questions/q-tug2bm-what-does-a-pass-with-no-person-read-of-a-tree-and-what-does-it-tell-the-next-pass-of-what-was-read-and.md) |
| a process that outlives the call that started it | lesson 17; register 2026-11-25 | open: [q-7v6dpa](../questions/q-7v6dpa-how-is-a-process-a-command-starts-kept-from-outliving-the-call-that-started-it.md) |
| roles, and the name a role's session bears | L14; L15, which overrides session/S11 | open: [q-p4sdnv](../questions/q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md), [q-jz3mlm](../questions/q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md), [q-mvd4pi](../questions/q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md) |
| the paired close names a mover without its path | register 2026-09-27 | **not sent**: ticket/P2 still names `move_doc.py` with no path, `.agents/mechanisms/ticket/ticket.rules.md:30` |
| a choice put to the person without what sets its options apart | register 2026-11-23; L6 | **not sent**: no rule in core says it |
| a part judged from lines that left out what decides it | register 2026-11-25 | **not sent**: no rule of the harness was in play |
| a Windows path written through a script's string lost its backslashes | register 2026-11-26 | **not sent** |
| the head table and the decisions table dropped with the debugging marks | register 2026-11-26 | **not sent** |

The project's own, with no cause in core: L1 what the repository is, L2 the dials, L5 the
verification set, L8 which host does what, L10 a screen used before it is planned twice, L13
commits and pushes.

**Counts, by cause:** 23 causes — 3 fixed in core, 13 open in core, 2 received with no record or
holder, 5 never sent; 6 local rules the project's own.

**What it taught about auditing a project's harness:** the baseline's search was scripted, but its
marks were not: a recipient's cause and core's fix share no id, and are matched by what they say.
