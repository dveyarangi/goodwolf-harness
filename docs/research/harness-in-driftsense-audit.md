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
| a question opened below the dial | lesson 1; L7 | **sent, no record**: told the store's session 2026-11-24; Q1 unchanged, no question holds it. Placed after this round as [q-sa75ul](../questions/q-sa75ul-which-questions-does-the-store-take-and-which-are-settled-in-the-turn-and-written-where-the-work-keeps.md), 2026-11-27 |
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
| the paired close names a mover without its path | register 2026-09-27 | **not sent**: ticket/P2 still names `move_doc.py` with no path, `.agents/mechanisms/ticket/ticket.rules.md:30`. Amended after this round, `b91d91be`, 2026-11-27 |
| a choice put to the person without what sets its options apart | register 2026-11-23; L6 | **not sent**: no rule in core says it. Placed after this round as [q-2cbkvs](../questions/q-2cbkvs-what-must-a-decision-put-to-the-person-carry-so-that-it-can-be-decided-from-the-reply-alone.md), 2026-11-27 |
| a part judged from lines that left out what decides it | register 2026-11-25 | **not sent**: no rule of the harness was in play |
| a Windows path written through a script's string lost its backslashes | register 2026-11-26 | **not sent** |
| the head table and the decisions table dropped with the debugging marks | register 2026-11-26 | **not sent**. Placed after this round as [q-4kvvec](../questions/q-4kvvec-does-a-tree-with-debug-off-keep-the-replys-frame-the-head-table-and-the-decisions-table-and-does-the.md), 2026-11-27 |

The project's own, with no cause in core: L1 what the repository is, L2 the dials, L5 the
verification set, L8 which host does what, L10 a screen used before it is planned twice, L13
commits and pushes.

**Counts, by cause:** 23 causes — 3 fixed in core, 13 open in core, 2 received with no record or
holder, 5 never sent; 6 local rules the project's own.

**What it taught about auditing a project's harness:** the baseline's search was scripted, but its
marks were not: a recipient's cause and core's fix share no id, and are matched by what they say.

## Round 1 — cost, 2026-11-27

Measured by [harness-in-driftsense-audit-cost.py](harness-in-driftsense-audit-cost.py), which prints
counts only, over DriftSense's Claude Code sessions of its harness tree, 2026-11-24 to 2026-11-26
(UTC): 23 sessions and their 115 subagents. A forked session's copied records count once. The
script was read by a reader who did not write it; its five faults were mended before these counts:
forks counted twice (5.6% of tokens), the person's messages miscounted both ways, messages to
subagents counted as messages to sessions, host tools counted as the method's.

Not counted: the Cursor sessions, where DriftSense builds its code (its L8), so product code's share
below is Claude Code's alone; frost_map's 64 sessions, a tree of its own; whether a message between
sessions was needed, which takes reading.

| measure | count |
|---|---|
| API calls | 7,019 |
| tokens | 1,784.9M: cache reads 1,734.1M (97.2%), cache writes 42.8M, output 8.0M, fresh input 0.01M |
| the person's messages | 469 (7 of them the same words again) — 15 calls and 3.8M tokens each |
| tokens per session | median 77.0M, largest 214.7M |
| tool calls | about 10,500; the host's task list and wrap-up 1,426 of them |
| messages between sessions | 252 sent to sessions, 364 received, 4 of them exact repeats |
| commits in the harness tree | 350: ALIGN 272 (78%), MAINTAIN 28, TICKET 17, PLAN 14, VERIFY 7, SKILL 5, HARNESS 4, RULE 1, no step 2 |
| commits in the product's repositories, the same days | 37: admin 14, the farmer frontend 21, the WRF coordinator 2 |

Tokens by what a call's tools worked on — a call's whole count, mostly the context it re-reads,
goes to its tools: replies with no tool 19.8%, the host's own tools 17.6%, scratch scripts 15.0%,
the method's records and scripts 14.5%, other 12.1%, product code 8.1%, git 4.2%, product records
3.4%, the web 2.5%, the host's files 1.1%, subagents 0.9%, the board 0.7%, mail 0.1% (counted, never
read).

Tokens the host attributes to a skill: 16.4%; `/recall` alone 8.5%, more than product code's share
by the measure above. Skills called: `/recall` 19, `/commit` 11, `/verify` 9, `/ticket` 7, `/align`,
`/plan`, `/impact` and `/skill-up` 4 each, others 1–2.

**For the person to set:** what share the method's own steps may take of a session, and what a
wake may cost; the next round on cost judges against it.

**What it taught about auditing a project's harness:** a measuring script needs a reader of its own
as much as a finding does: the first count was 5.6% high, and the person's messages off both ways.
