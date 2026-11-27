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
| silent zeros where status lives on another board | lesson 4; L12 | **fixed**: `9e37df11`, the path reads unread where no ticket carries a status. *Corrected in round 6: partly — see there.* |
| a promise made in a reply | lesson 5 | **fixed**: `c40e6217`, entry contract v141 |
| a per-clone part an update does not write | lesson 6 | open: [q-t5vmk3](../questions/q-t5vmk3-how-does-core-reach-a-recipient-tree-and-leave-it-working-at-a-first-install-and-at-each-update.md) |
| "install it with overwrite" misread | lesson 7 | open: q-t5vmk3 |
| a renamed skill leaves a project's links dead | lesson 8 | open: q-t5vmk3 |
| the edge check reads its folder's README | lesson 9 | **received, no holder**: `edges.py:123` still reads every `*.md`; no role names the edge mechanism. Mended after this round, `831edf69`, 2026-11-27 |
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
| a part judged from lines that left out what decides it | register 2026-11-25 | **not sent**: no rule of the harness was in play. Kept after this round as lesson 18, `72f346b7`, 2026-11-27 |
| a Windows path written through a script's string lost its backslashes | register 2026-11-26 | **not sent**. Registered after this round in core's own register, met here the same day, and kept as lesson 19, `72f346b7`, 2026-11-27 |
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

## Round 2 — the person's load, 2026-11-27

Measured by [harness-in-driftsense-audit-load.py](harness-in-driftsense-audit-load.py), which prints
counts only, over the same 23 sessions as round 1, and by a count of DriftSense's question store at
2026-11-27T00:00Z. Only the turns the person started are counted: 46% of the agent's words, and
half the decision tables, were in turns another session or the host started, and the person
reads those only if they open the session. The script was read by a reader who did not write it;
before these counts its faults were mended: those other turns charged to the person, decisions
counted once per session instead of once, the session's last table taken for its last reply, and
the pattern for a request to explain missing what it was for and catching "explanation".

| measure | count |
|---|---|
| the person's messages | 481; 198 of them hold a question mark |
| asking what something means, or to explain | 18 (3.7%), all in English — a pattern's estimate |
| the agent's words read per message of the person | median 310, upper quartile 476, largest 1,825; 161,802 in all |
| decision tables shown to the person | 295, in 15 of 23 sessions |
| distinct decisions in them | 431; 338 shown once, 93 shown again — those over a median 3 tables and 0.4 hours, the longest 61 tables and 52 hours |
| most decisions in one table | 14 |
| decisions standing in a session's last reply | 18, in 9 sessions |
| questions put by the host's own means | 195 wrap-ups with a question, 2 AskUserQuestion |
| the question store | 63 questions, 48 open, 45 of them at or above the dial and so waiting on the person; open a median 2.2 days, the oldest 4.1 |

A decision is the same while the words of its row are; one reworded counts as new, so "shown once"
holds some decisions reworded between replies. Matched by their first five words instead: 364
decisions, 256 shown once, 108 again.

Not measured: words the agent made up — whether a term the person met was defined where they read
it takes reading, not a count.

**For the person to set:** how many decisions a reply may put at once, how long one may wait, and
how many questions may wait on them in the store; the next round on the person's load judges
against it.

**What it taught about auditing a project's harness:** a session's transcript is not what its
person saw: in a tree of sessions that write to each other, nearly half of what an agent writes
answers another agent, and a count of the person's load must first find which turns were theirs.

## Round 3 — rules reaching their occasion, 2026-11-27

Read: DriftSense's `docs/rule-failures.md`, its question store, `local.rules.md`, `AGENTS.md`, its
skills and its copy of core's scripts at its commit `504e12a`. Tested: core's checks run there
read-only, the working tree unchanged after. Asked: three fresh readers given only what a session
there reads, one per overridden rule, never told the rule.

**The register.** 7 entries, 15 occurrences. Struck again: a secret's value printed, 4 times; a
helper's whole-disk search outliving it, 3; a backslash lost through a script's string, once.
Closed 4 — the paired close's mover, a choice without what sets its options apart, the whole-disk
search and the dropped head table — the last two by a hook of the project's own beside core's. Open
3: the secret printed, the part judged from lines that left out what decides it, the backslash.

**The store's struck counts.** 14 of 62 questions struck at least once: one 5 times, two 3, one 2,
ten once.

**The overridden rules.** Three: L4 over ticket/P5, L7 over questions/Q1, L15 over session/S11.
Each stands installed right after the rule it overrides, and each fresh reader did what the
override says, citing R7 for why the local rule wins. One reader found that `TICKET-FORMAT.md:73`
still says `tickets.py --check` holds every live ticket, and that `/verify` never says L4 dropped it.

**L7 at work.** Before it landed (2026-11-24T18:02Z), 15 of the 25 questions opened were at the
rung of a feature or of code; after it, 2 of 37. Whether those two are the investigations L7 lets in
was not read.

**Core's checks, run there.**

| check | result |
|---|---|
| mechanisms, inject_rules, questions, sessions, maintain, product, personal, harness | pass |
| tickets | fails: 173 diagnostics on all 32 tickets, every one from the shape L3 and L4 override — the override reaches the text and not the script ([q-veooj7](../questions/q-veooj7-how-do-projects-share-one-development-method-without-losing-their-own-conventions.md), lesson 11) |
| edges | fails: 9 diagnostics on `docs/edge/README.md` (lesson 9, mended in core at `831edf69`, after the copy DriftSense runs); 12 on `shared-task-link.md`, a Normative record whose 12 promises are marked unguarded — a finding of the check that DriftSense's verification set (L5) never runs |

**The push gate.** Core's `harness.py` holds a pre-push gate that runs eight checks, `tickets` and
`edges` among them; the per-clone step `harness.py --links` writes the hook
(`.agents/scripts/gw/harness.py:215`). DriftSense's clone has none, only Git's samples, and no `core.hooksPath`. Installed, it
would refuse any push carrying a commit that touches the method's records while those two checks
fail at that commit (`harness.py:1639`, `:1739`). Read by two readers apart. This is lesson 6, a per-clone part an update
does not write ([q-t5vmk3](../questions/q-t5vmk3-how-does-core-reach-a-recipient-tree-and-leave-it-working-at-a-first-install-and-at-each-update.md)).

**What it taught about auditing a project's harness:** a rule reaching its reader and a rule
reaching its occasion are two tests. Every override here passed the first; two checks that would
carry rules mechanically are not run at all, and the gate that would run them is missing, so the
second fails without a sound.

## Round 4 — records about code in sibling repositories, 2026-11-27

Measured by [harness-in-driftsense-audit-citations.py](harness-in-driftsense-audit-citations.py) over
DriftSense's records and its eleven sibling repositories' history; read by two readers apart, a
random sample of 15 cited lines, half of them from citations the script flags; core's and
DriftSense's checks read for what would notice.

**Citations.** 665 of DriftSense's records cite a file of a sibling repository: admin 513, the WRF
coordinator 80, the farmer frontend 38, eight others 30. 414 give a line; 8 point past the file's
end; 8 name a file no longer in its repository. By record: questions 241, the security audit 158,
RFCs 162 (100 of them done), tickets 94 (11 done). Another 820 paths could not be given to one
repository, mostly bare file names.

**May have lapsed** — the cited file changed in its repository after the citing record last
changed, the round method's lapse rule: 47, 30 of them in done RFCs and tickets, records of what
happened; 17 in live records.

**The sample, read.**

| | holds | moved | lapsed |
|---|---|---|---|
| flagged as may have lapsed (7) | 0 | 6 | 1 |
| not flagged (8) | 6 | 2 | 0 |

Moved: the claim still true of the code, at another line — a reader who follows the line lands on
other code, once on a prompt for a language model, once on a blank line. Lapsed: a done RFC says a
body with no plots is refused; the code now takes an empty list (`admin/api/viewsets/operation.py`,
the plots validator). Read by two readers apart: the refusal was taken out on purpose, at admin's
`5332b3b` of 2026-09-22, by the follow-up the RFC itself names, and was never an acceptance
criterion — a record of what happened, overtaken, not a broken promise. The two moved lines the script did not flag sit in files whose last commit is older than the
citing record's last edit; both files hold changes in admin's working tree not yet committed
(`api/viewsets/excel_upload.py`, `app/admin.py`). A rule by commit misses code that is not committed.

**What would notice.** Nothing, in core or in DriftSense. Core's `/maintain` marks with a fingerprint
the files inside the tree (G1); the edge check asks only that a validator's file exists
(`.agents/scripts/gw/edges.py:266`). DriftSense's guards check links and bytes inside its tree.
DriftSense's own audit method plans the lapse by file and commit (its q-vxes7i), not built. The question it raises in core: [q-2rio5w](../questions/q-2rio5w-does-maintain-hold-a-records-citation-of-code-in-another-repository-to-that-code-as-the-code-moves.md).

**For the person to set:** whether a record's citation of code is to pin a commit, name a symbol
instead of a line, or be re-read when its file changes; the next round on records judges against it.

**What it taught about auditing a project's harness:** line numbers age faster than claims: of 15
read, 8 pointed at the wrong line and 1 claim had lapsed. A lapse rule by file and commit flags the
ones that moved, but not every one.

## Round 5 — safety, 2026-11-27

Measured by [harness-in-driftsense-audit-safety.py](harness-in-driftsense-audit-safety.py), which
prints counts only and compares values by their hash in memory, over the same 23 sessions as
round 1 and the tool outputs the host saved beside them. Whole-disk searches are judged by
DriftSense's own hook, its rule run on every Bash command. The script was read by a reader who did
not write it; before these counts its faults were mended: placeholders counted as passwords, one
value counted at every re-print, a file named in a search counted as read, a pattern of my own for
a whole-disk search that disagreed with the hook in 36 of 64 cases, the hook's text in a file
counted as its refusal, subagents counted as background commands.

| measure | count |
|---|---|
| distinct values shaped like a secret, printed into a session's context | 11 — 6 assigned to a secret's name, 3 passwords in a URL, 1 cloud access key, 1 API key — in 9 of 23 sessions; a pattern's estimate, which cannot tell a live value from a revoked one |
| set apart as code or placeholders | 239 assignments whose value is code, 60 placeholders or documented examples |
| tool calls reading a file that holds secrets | 77 — the product's settings 41, configuration files 16, `.env` files 12, the scoring model 8 — in 11 sessions; 163 more name such a file only in a search |
| whole-disk searches, by the hook's rule | 37, all before the hook was first committed (2026-11-26T23:08Z), in 3 sessions; none after |
| commands the hook refused | 42, the first of them while the hook stood uncommitted in the working tree |
| shell commands sent to the background | 59 |

Not measured: whether the person's word, relayed between sessions, was relayed truly — a pattern
for it caught quotations of rules and missed plain approvals, so it takes reading.

What holds it: for whole-disk searches, DriftSense's own hook, built after its register's entry was
struck three times — none since. For secrets, nothing yet: core's refusal of a call that names a
listed file is in work ([q-wjv4mi](../questions/q-wjv4mi-how-does-claude-code-refuse-an-agents-call-that-names-a-file-on-the-projects-list-of-secret-holders.md),
ticket 01-0120.0010); DriftSense's register holds the secret's entry, struck four times and open.

**For the person to set:** whether any read of a file that holds secrets is acceptable — a refusal
at the host, or reading allowed with printing refused; the next round on safety judges against it.

**What it taught about auditing a project's harness:** an audit that reads for secrets carries the
risk it measures: every count here was taken by hash in memory, and a reader's first probe of the
script had to be told, in its brief, never to print even a prefix.

## Round 6 — fit, 2026-11-27

Read: DriftSense's `local.rules.md`, `.claude/settings.json` and hooks, its own scripts, and core
at HEAD, by me and by a reader apart for what core now carries; tested: core's checks there, round 3.

**What DriftSense switched off, overrode or built beside core.**

| what | why core could not take it | in core now |
|---|---|---|
| debugging switched off | — the person's setting; the reply's frame went with it, and a project hook (`frame-reminder.sh`) now says each turn that it stays | [q-4kvvec](../questions/q-4kvvec-does-a-tree-with-debug-off-keep-the-replys-frame-the-head-table-and-the-decisions-table-and-does-the.md), open |
| L3, a ticket's shape: no `Status` or `Type`, the board's link on the third line | the board owns state and kind; core's format requires both (`TICKET-FORMAT.md:108–109`) | open, lesson 11; L3 names no override, as core's R7 asks |
| L4 over ticket/P5: the project's guard checks tickets, not `tickets.py` | `tickets.py` fails on all 32 tickets of that shape (round 3) | open, lesson 11 |
| L5, the verification set: the project's two guards and `harness.py --check`, none of core's record checks | the ticket and edge checks fail there | open |
| L7 over questions/Q1 | Q1 opens what the dial would settle | [q-sa75ul](../questions/q-sa75ul-which-questions-does-the-store-take-and-which-are-settled-in-the-turn-and-written-where-the-work-keeps.md), open |
| L13, ask before committing code | departs from *Autonomy*'s "work closes with its commit"; that sentence has no rule id, so no override can name it | — |
| L15 over session/S11 | S11 names a session by the person's name for it, not by its role | open, roles |
| a hook refusing whole-disk searches and followed streams | core had none | [q-7v6dpa](../questions/q-7v6dpa-how-is-a-process-a-command-starts-kept-from-outliving-the-call-that-started-it.md), open |
| two guards of its own: the records' conventions, and links and bytes | core's ticket check cannot take its tickets; no script of core checks a tracked file for control bytes, by a search of them | — |

**What DriftSense holds as waiting for core.** Six local rules are wrapped as straw dogs on its
question of which of them core comes to carry. Read against core at HEAD:

| local rule | carried by core |
|---|---|
| L11, a hazard comes first | **fully** — `.agents/skills/pathfinder/SKILL.md:16–21`, since `fd6fa720` and `3b70d896`, 2026-11-25 |
| L12, the state of work is the board's | **partly** — the wake reads "unread" where no ticket carries a status (`9e37df11`), but tells it rather than staying silent, returns to zeros once one ticket carries a status, and nothing reads the board |
| L7, L9, L14, L15 | not yet — each an open question in core (round 0) |

Round 0 marked L12's cause fixed; it is partly. Round 0's counts read 2 fixed, 1 partly, 13 open.

**What it taught about auditing a project's harness:** fit is best read from the project's own
straw dogs: DriftSense had already written down which of its rules it expects core to take, so the
round had only to read core against them.

## The audit, rounds 0–6

The baseline and six aspects, each round's counts by a script read by a reader apart, each serious
finding read twice. The findings went to the questions that own their causes and their zones'
sessions; DriftSense's own, through rounds 0–3, to its Harness session. What none of the rounds
could judge, because nothing written says what working means, waits on the person: the cost a
method's steps may take, the person's load, how a citation of code should hold, and what reading of
secrets is acceptable. The next audit judges against what the person sets.
