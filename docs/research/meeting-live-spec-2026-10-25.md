# The meeting on live-spec — the study's report, kept as written

- **record of** what happened
- **evidence for** [q-0037.0006.0020.0001.0004](../questions/q-0037.0006.0020.0001.0004-how-does-the-install-read-a-tree-with-a-method-and-report-what-goodwolf-would.md), live case 5; [q-0037.0006.0024.0002](../questions/q-0037.0006.0024.0002-does-every-rule-of-the-entry-file-belong-to-a-mechanism-so-that-an-install-adds-the.md)

2026-10-25. The report a fresh agent wrote of live-spec at `6389cb9f` under the harness's study,
saved unchanged by the person's agent into that session's scratch folder, copied here on the
user's word the same day. Below the line it is the report as written.

---

# What would GoodWolf change in how this pack keeps its plan, its rules and its record?

*A study of `live-spec` at `6389cb9f` (main, 2026-09-09), read on 2026-10-25. Nothing was written into the tree. Scratch files: `goodwolf-study/scratch/` beside this report.*

## 0. How this was read

[inventory] The study has three parts, and every paragraph below carries the mark of the part it comes from: **[inventory]**, **[readings]**, **[ledger]**. The inventory lists what your tree already has: the entry file and what it pulls in, your own skills, the gates and checks and the rules that name them, the records you keep (plan, decisions, journal, spec, checkpoints, inbox), and the size of a typical change, read from git history. These are the things GoodWolf would sit beside and not replace, given in your own names.

[readings] The readings are eight ways a project's knowledge can fail to reach the session that needs it, or fail to hold once it has. Each is counted and quoted in your tree's words:
1. **Cost of reaching what is written.** How many files and steps lie between a question and its answer.
2. **Kinds mixed in one file.** Instructions, decisions and history kept together.
3. **One fact in several homes.** Copies of the same fact, and where they have parted.
4. **What nobody records.** Sessions, and why a piece of work stopped.
5. **Rules the tree does not keep.** A rule stated next to a standing case against it, or a gate that covers less than its rule claims.
6. **Who owns what.**
7. **Where you stand.** What waits on you, and for how long.
8. **Decisions without their reasons.**

[ledger] The ledger is a measurement kept so it can be taken again after a migration. I built a sample of seventeen questions about your tree and an answer key from the code and records, before any answers came in. Then a fresh agent was given the repository and the questions. It was told nothing of GoodWolf and nothing of a measurement. It answered read-only and reported how it searched. Its answers were scored against the key, and the key was corrected only where the run proved it wrong. The ledger also counts what your method asks of a change today. Both are in the appendix.

[readings] The read was quick and sampled. What it reports is what it met on the way, not a full list. In particular, the disagreements between records named below are the ones this read ran into, and there are surely more. GoodWolf does not work by running one big audit. Each session repairs the disagreement it meets, where it meets it, and every session meets its own.

## 1. What was found

### The inventory

[inventory] **Entry and session start.** `CLAUDE.md` is 18 lines, 1,204 bytes. It sets the first action of every session: `bash scripts/state-probe.sh`. It makes `PLAN.md` the single entry point, read one step at a time through `bash scripts/plan-step.sh <id>` (plan-17). It warns against reading the root prose, which runs past a megabyte. Two more files in the tree claim every session:
- `PLAN.md` Law 11 orders `.live-spec/profile.md` (101 lines) loaded.
- `.live-spec/agent.md` (79 lines) holds "The owner's standing rules for a session in this tree".

Three rule homes outside the tree are named but not carried by a clone:
- `~/.claude/playbook/CLAUDE.md`, section "How a reply to him looks"
- `~/.claude/playbook/personal/profile.md`
- the installed copy of `skills/live-spec-base` (36,600 bytes, 29 numbered rules), which loads before any pack skill

`.claude/settings.json` wires one hook: `guardrails/worker-admission-guard.py`. It refuses a worker spawn that no admitted row stands behind.

[inventory] **Skills, gates and checks.**
- **Skills:** 13 in `skills/`, from `director` and `spec-author` to `communicator` (49 KB).
- **Push gates:** `guardrails/pre-push` runs 25 gate letters, a through ag. Gate c only prints that gate b covers it.
- **Commit hooks:** `pre-commit` runs `check-future-times.sh`, `check-deferral-marker.py`, an opt-in fence and the plan-delta guard. There is also a `post-commit` hook.
- **Check scripts:** 45 `guardrails/check-*` scripts and 12 check, lint and spec scripts under `scripts/`.
- **Acceptance keys:** `scripts/plan_checks.py` holds 85 keys, one per plan row.
- **Workflows:** One remains, `.github/workflows/stranger-monitor.yml`, the daily inbox monitor. `gates.yml`, the CI mirror of the push chain, was deleted in the last commit.
- **Release:** `.claude-plugin/` publishes the pack at 6.1.4.

The tree is both the pack's source and its own first host ("it runs its own method on itself", `.live-spec/agent.md`).

[inventory] **Records and where the current state lives.**

| Record | Size | What it holds |
|---|---|---|
| `PLAN.md` | 127 KB, 1,374 lines | The one plan. 91 rows, all ✅. |
| `DECISIONS.md` | 83 KB | Your decisions "on record", the "Open — carried, awaiting your word" list, and struck lines. |
| `JOURNAL.md` | 468 KB, 150 headed chapters | History. |
| `PRODUCT_SPEC.md` and `spec/` | 33 chapters | The spec. Has a generated index. |
| `ARCHITECTURE.md` and `architecture/` | 15 nodes | The architecture. Has a generated index. |
| `TEST_MATRIX.md` and `matrix/` | — | The test matrix. |
| `MIGRATION.md` | 54 KB | Migration notes. |
| `FEEDBACK.md` | — | Feedback. |
| `WAITING.md` | — | The waiting list. Empty. |
| `NEXT_STEPS.md` | — | Transient state: "None". |
| `.live-spec/checkpoints/` | 37 files | One checkpoint per row, holding its anchors and receipts. |
| `inbox/` | 3 open letters, 11 handled | The inbox. |
| `docs/` | 1,025 files | 553 prover records, 186 skill-review records, 48 queue-archive pages, 11 handovers. |
| `attic/` | 1,285 files | Includes 862 session transcripts, 311 MB. |

The current state is meant to be computed, not read: the probe prints it from git, `PLAN.md`, the checkpoints and `inbox/`.

[inventory] **Grain of the work.** `gh` works, and the pull-request list for `happysasha18/live-spec` is empty. Work lands as direct commits to `main` and as merged lanes.
- **History:** 2,500 commits from 2026-07-04 to 2026-09-09, then nothing for 46 days.
- **Direct commits:** 2,245 first-parent commits that are not merges. The median is 1 file and 46 lines changed (last 300).
- **Lane merges:** 64. The median merge carries 2 commits, 7 files and 374 lines. The mean is pulled up by a few very large merges, up to 1,249 files.
- **Pace:** about 350 commits a week at the peak, weeks 35–36. Lane merges ran 13–24 a week in weeks 34–36.
- **One row:** a plan row closes over five to eight commits, from "admitted and taken up", through the work, the close, and the closure review, to the record that covers the review ("The record's range reaches …"). q-835 is an example.

### The readings

[readings] **1. Reaching what is written.** The entry file points well. One plan step plus the probe is a small read. But several answers sit two or three homes away from the question:
- **Reply format.** CLAUDE.md sends you to PLAN.md. PLAN.md Law 7 sends you to `~/.claude/playbook/CLAUDE.md`, which is outside the tree and absent on this machine.
- **The reason for rule 41.** It is in `skills/live-spec-base/references/rule-origins.md`, not beside the rule.
- **Archived rows.** A row that left the plan is found through a 14-line manifest in PLAN.md that points into `docs/queue-archive/`.

Records also supersede one another in chains:
- culling plan v1 → v2 → v3
- seven `plan-v3-delta-*` pages
- q-833 abandoned → q-834 "Supersedes. q-833"

One decision's reason can be read only by search. "Dropped, and not coming back: Kimi/K3, Hermes, OpenRouter, LiteLLM" has no reason in any live file. Its attic source says only "решение не менялось" ("the decision did not change"). The rest is in 862 raw transcripts.

[ledger] On this Windows clone (`core.autocrlf=true`, PLAN.md with CRLF line endings) the entry file's one step reader, `plan-step.sh q-829`, printed nothing and exited 1, so the blind agent read the lines directly. The probe could not be run read-only, for two reasons: line 31 runs `git fetch`, and its blocks call `python3`, which on this machine is the Store stub.

[readings] **2. Kinds mixed in one file.** `PLAN.md` holds eight kinds of record under one roof:
1. the goal
2. a glossary ("Words used here")
3. settled decisions ("Already decided — not reopened")
4. a recovery procedure ("Fallback when drifted")
5. eleven "Laws of execution", where breaking one "is a stop"
6. 91 rows, each with a statement, validation, a DOD hash and an acceptance command
7. environment traps
8. the archive manifest

The laws are instructions for every session. CLAUDE.md tells a session not to read PLAN.md whole, and `plan-step.sh` prints one row's section only. So the laws reach a session only when it ignores its entry file. That includes Law 11, the one that orders the profile loaded. Other files mix kinds too:
- `.live-spec/agent.md` puts every-session rules inside an identity card.
- `.live-spec/profile.md` keeps each override together with its history ("his word, 2026-09-04 02:01").
- `DECISIONS.md` keeps under "Notes" an executed-work log ("D2 executed. 2026-08-12, 02:30-03:17").

[readings] **3. One fact in several homes.** These are the parted pairs met on the way. Each is given as a record, then the thing that record is of.
- **The CI mirror.** `guardrails/pre-push` says the server runs gate b's full suite and gate g ("The SERVER runs gate g unconditionally (.github/workflows/gates.yml)"). The same claim stands in `architecture/guardrails.md` ("The CI mirror is LIVE too"), the agent card's zone list, `DECISIONS.md`'s gate-b entry and 31 tracked files in all. `.github/workflows/`, which those records describe, lost `gates.yml` in `6389cb9f`.
- **The open list.** `DECISIONS.md` "Stage 3 C2 — six checks await your word" names gate ae, and u, v, w, ad among the kept checks. `guardrails/` lost all five in `e61b29b7` on 2026-08-21.
- **The same open list again.** It stands against your own ruling of 2026-08-13 08:51 in the same file, which makes those six questions "the seat's to rule on".
- **The probe's definition.** PLAN.md's definition of *verified* ("the probe ran it") and the probe's header ("What it reads: … the acceptance commands") both describe `scripts/state-probe.sh`. Since q-826 the probe runs no command ("no command runs, so evaluate() below takes its no-command branch").
- **The waiting list.** `WAITING.md` says "Your status answer prints what is at the top … and adds one line naming this list — how many items it holds". The probe does not read `WAITING.md`, and base rule 40 says "no count is kept of what they have yet to look at".
- **The recommendations checkpoint.** `.live-spec/checkpoints/recommendations-stop-queueing-themselves.md` reads "Status: open", NEXT: "Two adversarial reviews are running". The work it describes, spec Requirement 60 and the named tests, landed in the same commit, `1d4a6b6e`.
- **q-829.** Its ✅ heading in `PLAN.md` is not backed by its own acceptance key. The key checks `VERSION` = 6.1.1, and VERSION is now 6.1.4.

[readings] **4. What nobody records.** Several homes record sessions, each partly:
- the journal
- 37 checkpoints
- 11 handovers
- `NEXT_STEPS.md`, holding only "transient execution state"
- 875 commits carrying a `Claude-Session:` link to a chat outside the tree
- 862 transcripts in the attic

None of them says why a piece of work stopped. PLAN.md closes a session with "update a step's status (one line). Write nothing else." The tree's last change shows the gap. `6389cb9f` "Remove LiveSpec GitHub gates" has no body, no row, no journal entry and no prover record. Nothing explains why the second net went or what was meant to follow. History has leaked into rules instead of into a record:
- PLAN.md cites at least 216 dates. Its glossary corrects itself in place ("Corrected 28.08: …").
- Rule 38 ends "This cost four stalled lanes in one night before it was written down".
- The agent card explains a removal ("It stood here in full until 2026-08-31").

[readings] **5. Where the tree does not keep its own rules.**
- **Journal entries.** PLAN.md Law 1 says executing the plan "does not create … JOURNAL entries". Base rule 9 says "Log every movement's dated reason" in the journal. 37 commits since 2026-08-24 wrote journal entries during plan work.
- **Invented numbers.** Law 2 and rule 39 refuse a number with no source. `guardrails/check-board.py` keeps `CAP = 12` with the comment "No incident or source behind the 12".
- **Silent deletion.** Rule 10, "Nothing is silently deleted", stands against `gates.yml` deleted with no attic copy and no manifest line.
- **Letters opening rows.** Rule 41 says "A letter from another project opens none". q-835 (2026-09-09) built "a row admitted from a letter".
- **Gates that cover less than they claim.** The pre-push chain lets gate b run scoped and gate g stand down, on the stated ground that the server runs both in full. No server does. In this clone `.git/hooks` holds no installed hook, so no gate runs here at all.
- **Prose-only rules.** Rule 41 is marked "prose-only, no dedicated check", as are three other rules in the base. That is by design, and they are held by attention alone.

[readings] **6. Who owns what.**
- **Written boundaries:**
  - the agent card's zones ("Outside these zones this agent reads and writes nothing")
  - a row's `Holder:` (seat, or a named lane)
  - a checkpoint's `Owner: director`
  - rule 31's "owner", ruled on 2026-08-13 to mean the owning agent
  - DECISIONS.md "On record" for what is yours
- **Unsaid:**
  - Who runs "the intake sweep". All three open letters defer to it ("the intake sweep decides whether any of it is owed one"), and no record names who runs it or when.
  - Who leads sessions. PLAN.md says "Leads: Sonnet". The last month's commits are co-authored by Opus.
  - Whose gate chain this is now that its server copy is gone. The removal commit is yours; the records still describe the old chain as live.

[readings] **7. Where you stand.**
- **What reaches you.** `WAITING.md` says nothing is waiting, and rule 40 says nothing waits on you.
- **What still waits on you.** `DECISIONS.md` still lists:
  - D-1, D-6 and D-7 as "awaiting your word". Swept 2026-07-28; 89 days ago.
  - six checks under "await your word". Since 2026-08-12, 74 days, though you handed them to the seat 73 days ago.
- **Not shown to you.** Three inbox letters have waited 46 days for a sweep.
- **Decided without you, on a standing grant:**
  - "the seat's extension of your word", kept on fifteen checks "until you rule"
  - pushes to `main`, on the standing push grant
- **Brought to you that need not have been.** Q-536, "Three wording disagreements in the rulebook need your final call", reached you as a row.
- **Open questions in the spec.** 41 `[GAP` lines in the spec each carry an open decision.

[readings] **8. Decisions without their reasons.**
- The four dropped tools (see 1).
- "Leads: Sonnet."
- `CAP = 12` (see 5).
- The gates' removal.

Elsewhere the tree is strong here. DECISIONS.md quotes your words and dates for each ruling. The base rules carry their origins. The profile names the incident behind each override. Of commits since 2026-08-24, 16% have a body shorter than 80 characters. The median body is 602 characters.

### What the method asks of a change

[ledger] Each change pays for the following:
- **Rules read every session:** 3 files in the tree, 13,692 bytes. Three more homes are named outside it.
- **Local gates:** 25 gate letters at push and 4 checks at commit.
- **CI:** none per change, now. Before 2026-09-09 there was one job of 28 steps.
- **Rules to keep:** 11 laws and 29 base rules.
- **Row fields:** about 12 fields per admitted row.
- **Records per merged lane,** in the window 2026-08-24 to 09-09: about 3.8 prover records, 2.6 skill reviews, 1.1 checkpoints and 0.5 decision entries.
- **Check scripts:** 57.

The table is in the appendix.

### What stays as it is

[inventory] Your practices stay yours, kept by your choice:
- the probe as the first action
- acceptance commands written at admission and frozen, with DOD hashes
- the prover record before every push
- skill-review records
- the gate chain and the worker-admission hook
- DECISIONS.md quoting your own words with their exchange
- the journal
- the generated indexes
- the lane workflow

GoodWolf works beside these and replaces none of them.

## 2. Main recommendations

1. **Keep every open question in one home, with its state and who decides it.** [readings] GoodWolf
   holds each open question with where the thinking got to. When you answer one, the text that was
   waiting on it comes up for rewriting. Your open list still waits on your word for six checks you
   handed to the seat 73 days ago, one of which was removed 65 days ago. The three inbox letters
   wait on a sweep that no record assigns.
2. **Install each rule a session must follow where the session reads it.** [readings] GoodWolf
   writes a rule once, copies it by script into the entry file or skill that reads it, and fails a
   check the moment a copy parts. Your eleven Laws of execution live in a file the entry file tells
   a session not to read whole, and the reply format lives outside the tree.
3. **Record every session: where its work stopped and why.** [readings] GoodWolf keeps one record
   per session and reads it back at the next start, so "continue" is enough. The tree's last
   change, the removal of the CI gates, carries no body, row, journal entry or review record. A
   checkpoint opened on 2026-09-04 still reads "open" over work that landed that day.
4. **Repair a disagreement between records where a session meets it.** [ledger] GoodWolf makes
   that repair part of every session's work, has each record say which side wins, and lets you
   schedule a pass for what no session meets. In six of seventeen answers the blind run reported
   records that disagree. The push chain, 31 files and the tests still count on a workflow deleted
   46 days ago.
5. **Give each kind of record a home of its own.** [readings] GoodWolf separates rules, decisions,
   open questions, work and history, so a session reads the kind it needs. Today `PLAN.md` holds
   eight kinds in 127 KB, its 91 rows are all closed, and its laws can reach a session only if the
   session reads the whole file.

## 3. What clearly improves, and what you will likely give up

[ledger] Your tree is already easy to read for a capable newcomer. The blind run answered sixteen of seventeen questions in full, one in part, for about 184,000 tokens and 56 tool calls. GoodWolf's case here is therefore not that answers would become findable. The answers already lie in your records, and some of them are stale. What changes is that the right answer is the one a session meets first, and that a record which has parted from its subject is set right by whoever meets it.

[readings] Here is what you will see change. When a session starts, it tells you which of your questions are open, which wait on you and since when, and which the seat may settle. The six checks you delegated on 2026-08-13 no longer sit under "awaiting your word". The rules a session must follow, including the laws now buried in `PLAN.md` and the reply shape now kept only on your machine, reach every session in this tree and in every clone of it, and a check fails when two copies part. A removal like the CI gates leaves a session record saying what was intended and what was left to follow. Its loose ends are then open questions rather than 31 files quietly describing a server that is gone. When the probe's behaviour changes, as it did at q-826, the plan's definition of *verified* changes in the same session, because the session that met the mismatch repaired it.

[readings] Here is what you will likely let go of. First, the single file that holds everything. `PLAN.md` stops being the home of laws, decisions, glossary and traps, and keeps the work. Second, the moratorium on new records (Law 1). A session record and an open question's state are written as work goes, and Law 1 was in any case not being kept for the journal. Third, history kept inside rules: the dated incidents in the laws, rule 38 and the agent card move beside the rule as its reason, and the rule states only what holds today. Fourth, state kept on your own machine: the reply shape in `~/.claude/playbook/` and the owner's word carried in chat until a session quotes it into DECISIONS.md. Both become records in the tree. Last, the habit of letting a delegated or removed item keep its old line "until your word".

## 4. The migration plan

[inventory] Each item is cut to the size your history shows: a lane of about 2 commits and 7 files, or a direct commit of 1 file and about 50 lines.

| What | What of GoodWolf carries it | Touches · depends on | Size |
|---|---|---|---|
| 1. Take GoodWolf in beside your method. Move the content of `CLAUDE.md` into `local.rules.md` as rules. Copy the core under `.agents/`. Merge its hooks into `.claude/settings.json` beside `worker-admission-guard.py`. Use as the verification set your pre-push chain and the pytest targets. Decide the reply shape once, your rule 38 or GoodWolf's, in `local.rules.md`. | The installer, `local.rules.md`, the entry file | `CLAUDE.md`, `.claude/settings.json`, `.agents/` (new) · everything below depends on it | One lane, but see section 5: the step that takes in a tree's own method is not carried yet |
| 2. Move the open list into one home. Bring in DECISIONS.md "Open" (D-1, D-6, D-7), the six Stage-3 checks with your 2026-08-13 delegation applied, the three inbox letters, and the 41 `[GAP` lines, each with its state and who decides. | Open questions with their state | `DECISIONS.md`, `inbox/`, `spec/` · needs 1 | One lane |
| 3. Install every rule a session must follow where it is read. Move the PLAN.md Laws of execution and the agent card's standing rules into a rules file that the installer copies into the entry file. Bring the reply format into the tree. Leave `PLAN.md` holding the work. | A rule written once and copied by script, with its drift check | `PLAN.md`, `.live-spec/agent.md`, `.live-spec/profile.md` · needs 1 | One lane |
| 4. Repair the parted pairs this read met. The owner rules which side wins on `gates.yml`. Then cover the DECISIONS.md open list against `e61b29b7`, the definition of *verified* and the probe header against q-826, the `WAITING.md` promise, the open recommendations checkpoint, q-829's key, and the agent card's CI zone. | Repair where met, in each session's work; a scheduled maintenance pass | One record each · needs 1; the `gates.yml` side waits on you | About six direct commits of 1 file each |
| 5. Record each session. Write where it stopped, at which step, and why. The journal stays the project's history. | One record per session, read back at the next start | New session records · needs 1 | One lane |
| 6. Tie provisional text to the question it waits on. Lines such as "the pack runs on the stated recommendation until then" and "runs it until your word" come up for rewriting when the question is answered. | Text bound to an open question | `DECISIONS.md`, `spec/` GAP lines · needs 2 | Direct commits |
| 7. Give the goal one account. Use PLAN.md "Goal" and "What counts as done", so that "One existing project has migrated, with a proven rollback" shows as a goal with no work under it. | The product document | `PLAN.md` · needs 1 | One direct commit |
| 8. Run the second read. Take this same sample against this same key after the migration, and put the second ledger beside this one. | This study, read again | Read-only | Half an hour |

[inventory] **Order:**
1. Item 1.
2. Items 2 and 3, in parallel lanes, since they touch different files.
3. Item 4 as direct commits, the `gates.yml` item first because the tests depend on it.
4. Items 5, 6 and 7.
5. Item 8 last.

GoodWolf has nothing of its own for your gate chain, prover records, skill reviews or acceptance keys. Those stay as they are, and items 1 and 4 only point at them.

## 5. What this report does not say

[ledger] This report makes no comparison of your method with GoodWolf. That needs an install, a migration and a real check first. It is not a full list of disagreements: the pairs in section 1 are the ones this read met. The ledger measures one thing, what it costs a newcomer to recover the project's state on seventeen questions. That is a small part of what GoodWolf does. The second read after a migration is that migration's check. Until the migration is finished, nothing should be read from it except which items of the plan have landed.

[inventory] Two of GoodWolf's limits stand in this plan's way. First, the step that takes in a tree's existing method, from its inventory or by one line from its entry file, is not carried yet. The same goes for turning this report's plan into open work in your records. Today the installer stops at a tree that has an entry file of its own, as yours does. Second, GoodWolf's session records are seen across one working tree. Sessions in separate worktrees, as your lanes run, do not yet see each other.

## 6. Appendix: the ledger

### Counts

| Count | Value |
|---|---|
| Blind run: tokens (host's account) | 184,407 |
| Blind run: tool calls (host's account) | 56 |
| Blind run: wall time (host's account) | 464.6 s |
| Blind run: its own account | ~42 tool calls, ~38 searches, "roughly 15-20 minutes" |
| Blind run: files read (its own list) | 27 files plus 4 commits shown |
| Score: settled decisions (5) | 5 hit |
| Score: in flight (3) | 2 hit · 1 partial |
| Score: undecided (3) | 3 hit |
| Score: contradictory or incomplete (3) | 3 noticed and said |
| Score: hidden invariants (3) | 3 recovered |
| Rules read by every session, in the tree | 3 files, 13,692 B, 198 lines: `CLAUDE.md` (1,204 B), `.live-spec/profile.md` (8,409 B, PLAN.md Law 11), `.live-spec/agent.md` (4,079 B, its standing rules for every session); plus the probe's printout and one `plan-step.sh` section |
| Rules read by every session, outside the tree (named, not counted) | `~/.claude/playbook/CLAUDE.md`, `~/.claude/playbook/personal/profile.md` (both absent on this machine); the installed `live-spec-base` skill before any pack skill |
| CI jobs and steps per change | 0 since 6389cb9f (before: 1 job `gates`, 28 steps); `stranger-monitor.yml` runs daily, not per change |
| Local gates per push | 25 gate letters in `guardrails/pre-push` (a–z less v, w; plus ag; c prints only) |
| Local checks per commit | 4 (`check-future-times.sh`, `check-deferral-marker.py`, the opt-in fence, the plan-delta guard), plus `post-commit` |
| Checklist items | 11 Laws of execution; 29 numbered base rules; ~12 fields per admitted row (Group · Priority, Source, Holder, Outcome, Statement, Validation, Frozen, Done when, Read before admission, [Supersedes], DOD hash, Verification, Context pointers) |
| PR body length | No pull requests (gh list empty). Commit bodies since 2026-08-24: median 602 chars, mean 802, 16% under 80 |
| Records per merged lane (2026-08-24 – 09-09: 30 merges, 742 commits) | 113 prover records (3.8), 78 skill-review records (2.6), 32 checkpoints (1.1), 16 DECISIONS.md entries (0.5); 37 commits touched JOURNAL.md |
| Check scripts | 57 (45 `guardrails/check-*`, 12 under `scripts/`); 85 acceptance keys in `scripts/plan_checks.py` |
| Grain | 64 lane merges: median 2 commits, 7 files, 374 lines; 2,245 direct commits: median 1 file, 46 lines; peak ~350 commits/week |

### The sample and its key

The key was built before the run. Corrections the run proved are marked **corrected**. Additions where the run proved the key incomplete are marked **added**, and no score changed because of them.

**Settled decisions** (hit · partial · miss)

| # | Question | Key | Score |
|---|---|---|---|
| 1 | Why does the project answer the owner with the status in the reply itself instead of a rendered page or browser window? | The owner's word, 2026-09-04 02:01. The status list in the reply replaced the page. A window opening on its own interrupts him. A page is made only on request by name. Sources: `.live-spec/profile.md` `show.default`; DECISIONS.md 2026-09-04 (1). | hit |
| 2 | Why a re-check record before every push rather than the pack default? | The repo is public and the method's flagship. Tightened from "before MINOR bumps" on Alexander's word, 2026-07-04. Source: `profile.md` `prover.cadence`; normative home M-6. | hit |
| 3 | Why can only the owner, or a defect met outside, open a row? | Rule-origins, Rule 41 (2026-09-04): four of five open rows were self-raised; another project wrote 53 of 106 rows in 48 h when three were asked for; the retired findings log grew back within a day; "who raised it" can be faked, "who meets it" can be checked. | hit |
| 4 | Why is the reply format not in the agent card? | It stood there until 2026-08-31. By then the card's copy and the personal profile's had drifted on what counts as a real-world unit. Now one home: `~/.claude/playbook/CLAUDE.md`. | hit |
| 5 | Why no time budgets derived from measured runs? | DECISIONS.md 2026-09-07 22:32/22:33. Two local runs are no policy. A budget fixes composition and volume. A timeout is only an emergency stop, never derived from machine speed. Became rule 43. | hit |

**In flight** (hit · partial · miss)

| # | Question | Key | Score |
|---|---|---|---|
| 6 | What letters wait in the inbox, and in what state? | Three letters dated 2026-09-09, notes beside q-832, q-834 and q-835. Open: no Status line, still in `inbox/`. Each defers to the intake sweep and opens no row. | hit |
| 7 | Where does the work to stop a review's recommendation becoming work on its own stand? | The checkpoint reads Status open, Owner director, NEXT two adversarial reviews, then tests, prover record and push. The Requirement 60 rewrite and the named tests landed in `1d4a6b6e`, the same commit, and the checkpoint was never closed. **Added:** the 2026-09-04 prover review blocked on five findings on R1 criterion 5; later commits d71e2384, 96d7a53f, c746316c and 5daf46e2 carried it to rule 41. | partial (gave the landed state, not the open checkpoint) |
| 8 | Most recent change on main, and where it stands? | `6389cb9f`, 2026-09-09 19:29, deletes `gates.yml` and has no body. No row, journal entry or prover record names it. The pre-push chain, the tests, `architecture/guardrails.md`, DECISIONS.md, the agent card and the stranger-monitor comment still count on it. **Added:** 31 tracked files cite it; `tests/test_guardrails.py:1657` asserts it exists; `guardrails/README.md:54,377`. | hit |

**Undecided** (hit · partial · miss)

| # | Question | Key | Score |
|---|---|---|---|
| 9 | Engine-and-instance pair: one stitched queue view or two? Settled, by whom? | Open: DECISIONS.md D-6, swept 2026-07-28. The pack runs on the recommendation of two plain queues until real friction. GAP line in `spec/engine-instance-pair.md`. The owner decides. **Added:** a tension with the 2026-09-04 ruling that no task waits on your word. | hit |
| 10 | Gate n: keep or retire, and who decides? | Open since 2026-08-12. The seat recommends retiring it and holds the repair. Gate n still runs, report-only. **Corrected:** the decider is the seat, by the owner's delegation of 2026-08-13 08:51 ("мне там нечего решать это твоя внутренняя механика"). The open list's "until your word" stops short of that, and no seat ruling is recorded. | hit |
| 11 | Next piece of work, and who decides? | Nothing queued: all 91 rows are ✅. "One existing project has migrated, with a proven rollback" has no row. Rows open only by the owner or an outside-met defect, through the admission door. The inbox letters await the sweep. | hit |

**Contradictory or incomplete** (noticed and said · answered from one side · filled the gap)

| # | Question | Key | Score |
|---|---|---|---|
| 12 | Does a session carrying out the plan write JOURNAL.md entries? | Law 1 says no; base rule 9 says log every movement in the journal. In practice 37 commits wrote entries during plan work. **Added:** PLAN.md:1208 itself cites a journal entry. | noticed and said |
| 13 | State of gate ae? | DECISIONS.md lists it as running "until your word". `e61b29b7` (2026-08-21) removed it. **Added:** `matrix/guardrails.md` still names it, and `tests/test_check_registry.py` went with it. | noticed and said |
| 14 | Is q-829 done and verified today? | Heading ✅. Its key runs `unittest` on 18 bare pytest functions, so it collects none, and checks VERSION = 6.1.1 while VERSION is 6.1.4. Recorded in the inbox note beside q-834; no row repairs it. **Corrected:** the probe no longer runs keys (q-826), so it shows the row's own ✅ rather than 🔁. **Added:** the checkpoint holds a passed receipt from 2026-09-08 23:22. | noticed and said |

**Hidden invariants** (recovered · not)

| # | Question | Key | Score |
|---|---|---|---|
| 15 | How is a new task id chosen, and could one repeat? | `next_task_id`: one above the highest q-number standing in `PLAN.md`. plan-N ids are ignored and the queue archive is not read, so uniqueness holds only while the highest row stays on the plan. **Added:** admission refuses an id already on the plan or one with an existing checkpoint (`task-admission.py:862-866`); a collision happened once (a8c54239, q-821 → q-823); two lanes admitting at once compute the same number. | recovered |
| 16 | What does gate u guard? | Today: closed rows stand on receipts (`check-close-receipt.py`). Until 2026-08-21 the same letter meant the local chain against its CI copy, removed in `e61b29b7`. Letters are reassigned, and DECISIONS.md's "u" is the old one. **Added:** the old meaning dates from b179e79f (2026-07-18), the new one from 9ff033c6 (2026-09-06). | recovered |
| 17 | What does `scripts/state-probe.sh` do when it runs? | **Corrected:** it runs `git fetch --quiet`, which contacts origin and moves remote-tracking refs, then prints from recorded state. Since q-826 it runs no acceptance command; each icon is the row's own mark. It also flags done rows whose receipt or anchors fail, ranks rows, and prints facts, alarms, inbox and next. The records still call it a read and say the probe "ran it". | recovered |

### The blind run's return, whole and unedited

```
## Part 1: answers

I modified nothing in the repo. I did not run `scripts/state-probe.sh`. Its line 31 runs
`git fetch --quiet`, which writes into `.git`, and its Python blocks call `python3`, which is
the Store stub on this machine. I reconstructed what it would print by reading its inputs.

**1. Why the status goes in the reply, not a page or browser window.**
- It is the owner's ruling of 2026-09-04 02:01: "stop opening HTML files… default is the canon, that's all."
- The status list in the reply replaced the page he used to open to read it. A window opening on its own now interrupts him.
- A rendered page is made only when he asks for it by name.
- It is recorded as a host override in `.live-spec/profile.md:6-10` (`show.default`). That override beats the personal profile's show line for this repo.
- The ruling itself is in `DECISIONS.md:114-126`, item (1). The override landed in commit 1d4a6b6e.

**2. Why a re-check record before every push.**
- `.live-spec/profile.md:12-16`, `prover.cadence`: "a re-check before EVERY push, record in docs/prover/".
- The reason given: this repo is public and the method's own flagship. The cadence was tightened from the pack default ("before MINOR bumps") on Alexander's explicit word, 2026-07-04.
- The push gate M-6 is the normative home of the same fact. It names one carve-out: a push whose diff is exactly one new `inbox/` file owes no re-check record.
- `trust.push-grant` (profile.md, around line 77) repeats that the prover re-check before every push stays.
- One related rule: standing rule 1 in `.live-spec/agent.md:62-65` exempts ranges that touch only record directories.

**3. Why only the owner or a defect someone outside meets can open a row.**
- The rule is rule 41 in `skills/live-spec-base/SKILL.md:408-430`. A row is opened by the person, or by a defect someone outside this repository meets, and the test at the door is to name that person and what they see. The project's own review findings, letters from other projects, number mismatches and shape-only reds open no row. They are repaired in the same landing or left in the review record.
- The reasons are in `skills/live-spec-base/references/rule-origins.md:190-213`, entered 2026-09-04:
  - On this board, four of five open rows had been raised by the pack's own reviews.
  - On another project, 53 of 106 rows were written in 48 hours when the person had asked for three.
  - A findings log retired the night before grew back as rows within a day.
  - "Who raised it" is something a session writes about itself and can fake. A `raised` field was tried and refused within the hour. "Who meets it" is a claim anyone can check, because the row must carry "do this, and you see that."
- Rule 41 has no dedicated check on purpose: a check would be a session marking its own homework.
- Related rulings: `DECISIONS.md:127-139` (2026-09-04 01:17) and `PLAN.md:30-32` (admission door only).

**4. Why the reply format is not in `.live-spec/agent.md`.**
- `.live-spec/agent.md:69-79` says the shape lives in one home, the owner's own `~/.claude/playbook/CLAUDE.md`, section "How a reply to him looks".
- It stood in the card in full until 2026-08-31. By then the card's copy and the personal profile's copy had drifted apart on what counts as a real-world unit, which is the argument for one home.
- `PLAN.md` Law 7 (lines 159-165) gives the same reason ("two homes for one fact").
- `~/.claude/playbook/` does not exist on this machine. A session here would hit the card's clause "a session that cannot read that file says so".

**5. Why time budgets are not derived from measured run times.**
- It is the owner's stop of 2026-09-07 22:32/22:33, in `DECISIONS.md:59-78`. No acceptance or release budget is derived from a measurement, and two local runs are no policy.
- A budget fixes composition and volume instead: named targets, number of cases and samples, no N² sweep and no historical sweep.
- A timeout is only an emergency stop. It is never derived from this machine's speed and takes no part in a green verdict.
- It became rule 43 in `skills/live-spec-base/SKILL.md:440-447`, with origins in `rule-origins.md:215-235`.
- The incident: the seat proposed 600 s and 1800 s budgets based on two full-suite runs on one machine (843 s and 1393 s). The owner stopped it before either number reached a file.
- The underlying reason: a number read off one machine decides a verdict unrelated to correctness, and it moves when the machine does.

**6. Incoming letters waiting in the inbox.**
- `inbox/` holds three letters plus `README.md`:
  - `2026-09-09-notes-beside-q832.md`
  - `2026-09-09-notes-beside-q834.md`
  - `2026-09-09-notes-beside-q835.md`
- None has a `Status:` line. Under `scripts/inbox_lifecycle.py:69-81`, a letter with no line reads by position, so all three are OPEN.
- No PLAN row carries a `**Source inbox.**` naming them, so the probe would list them with no row link.
- They are closure-review notes from the 6.1.3, 6.1.4 and q-835 landings. Each says it opens no row and that "the intake sweep decides". The q835 letter was committed as 8b43f8b7.
- `inbox/handled/` holds 11 archived letters, including notes-beside-q829 and q831.

**7. Where the work to stop a review's recommendation from becoming work stands.**
- It landed 2026-09-04 in commit 1d4a6b6e. Requirement 60 in `spec/design-spec-review.md:181-205` was rewritten: a recommendation ends in the review record, opens no row or follow-up, and becomes work only when the owner writes it onto the plan. The 765-line `## Blockers` findings log was retired to `docs/queue-archive/2026-09-04-findings-log-retired.md`. The journal chapter is `JOURNAL.md:3758-3775`.
- The review `docs/prover/2026-09-04-recommendations-stop-queueing-review.md` judged the R60 half ready. It blocked on five findings (F1-F4 and F6), all on the other half of the change (R1 criterion 5), and said "needs another iteration".
- Later commits the same day carried it further: d71e2384, 96d7a53f ("Delete today's own machinery, and put the door test in its place (rule 41)"), c746316c and 5daf46e2.
- It now stands as R60 plus rule 41. No PLAN row tracks it.
- `FEEDBACK.md`'s 2026-09-08 lines show it applied: review deposits marked "NOTED, no row".

**8. The most recent change on main.**
- 6389cb9f, "Remove LiveSpec GitHub gates", by alexander-abramovich, 2026-09-09 19:29 +0300. It has no body and no Co-Authored-By line. It deletes `.github/workflows/gates.yml` (190 lines), the CI mirror of the push gate (SPEC M-5).
- Locally HEAD equals `origin/main`, so it appears pushed. I could not fetch to confirm.
- No prover record names it: grep for 6389cb9 found nothing, and the newest prover record is ceb27603 from 12:16.
- No PLAN row or JOURNAL entry covers it. 31 tracked files outside the archives still cite `gates.yml`:
  - `tests/test_guardrails.py:1657-1658` asserts the file exists. Other tests (`test_agent_card_gate`, `test_doc_rotation`, `test_delta_classifier`, …) read it, so the suite would likely be red. I did not run it.
  - `guardrails/README.md:54,377`.
  - `DECISIONS.md:850-859`: the decision to keep gate b rests on `gates.yml` re-running the suite.
  - `PLAN.md`'s "full suite is CI-only" trap.
- Only `.github/workflows/stranger-monitor.yml` remains.

**9. Engine and instance queues: one stitched view or two?**
- Not settled. It is D-6 under "Open — carried, awaiting your word" in `DECISIONS.md:749-752`, with the gap line at `spec/engine-instance-pair.md:12`.
- The recommendation is two plain queues with no stitched view, until real friction earns one (flipping between two windows to follow one wish's two halves). The pack runs on that recommendation meanwhile.
- The owner settles it. One tension: `DECISIONS.md:127-139` (2026-09-04) rules there are "no tasks that wait on your word", yet this list still carries items "awaiting your word".

**10. Gate n (`check-earned-message.py`): keep or retire, and who decides?**
- Still live, report-only, at `guardrails/pre-push:264-273`. Report-only is per the owner's 2026-08-07 11:19 word that a deposit never blocks a push, with judging moved to the intake sweep (`DECISIONS.md:164-169`).
- The records disagree on who decides:
  - `DECISIONS.md:780-785` (dated 2026-08-12) says the seat recommends retiring it and holds the repair "until your word".
  - `DECISIONS.md:156-160` (2026-08-13 08:51) records the owner's words: "nothing for me to decide there, it's your internal mechanics". That makes it the seat's to rule on and record.
- I found no recorded seat ruling on gate n afterwards. The question is still open on the record.
- The q835 letter notes the gate reads `inbox/` by position, ignoring the new `Status:` states.

**11. The next piece of work, and who decides.**
- There is none on the plan. All 91 rows in `PLAN.md` are ✅ (91 rows, 91 done; the last is q-835). The probe's logic (`state-probe.sh:305-315`) would print "every row is finished".
- `NEXT_STEPS.md` says "None". `WAITING.md` is empty.
- New work enters only through the admission door (`PLAN.md:30-32`). Per rule 41, it is opened by the owner or by a defect someone outside meets.
- The three open letters await the intake sweep, and each says it opens no row.

**12. Does a session carrying out the plan write JOURNAL entries?**
- The records disagree:
  - `PLAN.md:137-138`, Law 1 (Moratorium): executing the plan does not create "JOURNAL entries".
  - Rulebook rule 9 (`skills/live-spec-base/SKILL.md:194-195`): log every movement's dated reason in `JOURNAL.md` the same session.
- In practice they do write them. `git log -- JOURNAL.md` shows plan-executing commits adding bold-dated paragraphs through 2026-09-09: a4554732 (q-835 closed), 0aa429a0 (6.1.4), 1881ced1, 7dca40db, 87eb7d03, and others. `PLAN.md:1208` itself cites a JOURNAL entry.

**13. Gate ae (`check-registry.json` describes each runnable file).**
- Removed on 2026-08-21 in commit e61b29b7 ("Remove the checks whose only subject was another check"). `guardrails/check-named-checks.py`, `scripts/check-registry.json` and `tests/test_check_registry.py` were all deleted. Neither file exists today, and there is no gate ae in `guardrails/pre-push`.
- The records are stale against this:
  - `DECISIONS.md:773-778` still says the seat "runs it until your word".
  - `DECISIONS.md:768-771` lists ae among the kept checks.
  - `matrix/guardrails.md` still mentions it.

**14. Is q-829 (release 6.1.1) done and verified today?**
- Marked ✅ (`PLAN.md:1180`). The checkpoint `.live-spec/checkpoints/q-829.md` holds a "passed" receipt by cold-checker from 2026-09-08T23:22, and its DOD and ACCEPT anchors match.
- It is not verified today:
  - The probe runs no commands any more (q-826, `state-probe.sh:117-123`); it only reads recorded state.
  - The recorded key (`scripts/plan_checks.py:589`) contains `test "$(cat VERSION)" = "6.1.1"`, and `VERSION` reads 6.1.4, so the key fails.
  - Its first arm runs `python3 -m unittest` on `tests/test_release_6_1_1.py`, which has 18 bare `test_` functions and no TestCase class, so unittest collects nothing.
- `inbox/2026-09-09-notes-beside-q834.md` records both points. It says the shipped work is sound under pytest, but the evidence the close rests on is empty and cannot be repaired in place.
- I did not run the key. This is read off the code and files.

**15. How a new task id is chosen, and could it repeat?**
- `scripts/task-admission.py:719-721`: `next_task_id` takes the max `q-N` among live `PLAN.md` headings (`TASK_HEADER`, line 60) plus 1, unless the route supplies `task_id` (line 843).
- Admission refuses an id already in the plan, or one whose `.live-spec/checkpoints/<id>.md` exists (lines 862-866). Checkpoints of rotated rows such as q-824 and q-833 remain on disk, so a re-mint inside one tree is refused rather than issued.
- It can still collide:
  - The id comes only from the live plan, so after the highest row is rotated off, the same number would be proposed again (and refused only if its checkpoint still exists).
  - Two lanes or worktrees admitting at the same time each compute the same max+1.
  - It happened once: commit a8c54239 says "The new row took an id the plan already used, q-821. It is q-823 now."

**16. What gate u guards.**
- Today: "closed rows stand on receipts". A done mark must be a close through the state machine, never a hand edit. It runs `guardrails/check-close-receipt.py` (`guardrails/pre-push:222-225`) and has worn this letter since 9ff033c6 (2026-09-06).
- The letter was reused. Gate u was "CI mirror parity" (b179e79f, 2026-07-18) until e61b29b7 removed it on 2026-08-21.
- So `DECISIONS.md:768`'s "u" among the kept checks refers to the old gate.

**17. What `scripts/state-probe.sh` does.**
- WHERE WE STAND (lines 30-46): runs `git fetch --quiet`, then prints branch, commit and subject, the dirty-file count, and ahead/behind against the branch's own upstream.
- PLAN (lines 57-399):
  - Parses `PLAN.md` via `scripts/plan_checks.py` and `plan_checks_core`.
  - Runs no acceptance command; each icon is the row's own mark.
  - Flags done rows whose checkpoint lacks a passed receipt or whose DOD or ACCEPT anchor has moved, using `task-admission.py` readers.
  - Finds rows closed since the upstream's `PLAN.md`.
  - Ranks by category (closed-since-push, in hand, blocked, reopened, queued) and then by the plan's own priority words, within a 9-line budget.
  - Picks NEXT as the top reopened or queued row.
  - Uses mktemp files under TMPDIR, removed by a trap.
- Extras (lines 410-412): sources `scripts/state-probe-extras.sh`, which prints FACTS: version, director eval score, context token counts via tiktoken, corpus bytes.
- SINCE IT SHIPPED (lines 423-454): prints only if `.live-spec/success-measure-feed.json` exists.
- ALARM (lines 457-490): two homes for one fact, `/private/tmp` worktrees, worktrees with unmerged commits, and the pack version in each host listed in profile `hosts.watch`.
- INBOX (lines 498-553): open letters by `Status:` line, with a link to the row each became.
- BLOCKERS: only if the plan has a `## Blockers` section.
- NEXT (lines 565-580): the next row's title and the reason.

## Part 2: how I searched

**Order of work:**
1. Started from the CLAUDE.md pointers. I read `scripts/state-probe.sh` and `scripts/plan-step.sh` in full to judge whether they write. I found the `git fetch` and so did not run the probe. I also read `.live-spec/agent.md` (answered Q4).
2. Ran `git log`, `git status`, `git show HEAD` (Q8), and `gh pr list --state all`, which returned nothing at exit 0, so there are no PRs.
3. Listed `inbox/` and read the three letters. Grepped `scripts/inbox_lifecycle.py` for the default state (Q6).
4. Listed `PLAN.md` headings and read the preamble (lines 1-190, for Q3, Q11, Q12) and the tail (lines 1300-1374). Counted rows.
5. Grepped broadly for "outside the repository"/"recommendation". This led to `DECISIONS.md`, whose open section (lines 720-989) and dated entries (lines 53-172) answered Q5, Q9, Q10 and Q13, and to `.live-spec/profile.md` for Q1 and Q2.
6. Read the prover record of 2026-09-04, Requirement 60 in `spec/design-spec-review.md`, rulebook rules 41-43 and `rule-origins.md` (lines 144-235) for Q3, Q5 and Q7.
7. Read `NEXT_STEPS.md`, `WAITING.md` and `FEEDBACK.md`. Grepped `JOURNAL.md` headings and ran `git log -- JOURNAL.md`, then looked at a4554732's journal diff (Q12).
8. For Q14: `plan-step.sh q-829` printed nothing and exited 1, because `PLAN.md` is CRLF here (core.autocrlf=true) and the `$`-anchored grep fails under pipefail. So I read lines 1180-1205 directly, plus the `plan_checks.py` key, the checkpoint and the test module.
9. For Q15: `task-admission.py` (lines 60, 700-750, 835-870), the checkpoint list, and commit a8c54239.
10. For Q16 and Q13: the gate banners in `pre-push` and `git log -S` for `gate u:`, `gate ae` and `check-named-checks.py`. That led to e61b29b7's message and stat.
11. For Q8 follow-up: `git grep gates.yml`, the test references, and the prover record history.
12. Read the code lines of `state-probe-extras.sh`.

**Files read, whole or in part:** `CLAUDE.md` (given), `scripts/state-probe.sh`, `scripts/plan-step.sh`, `.live-spec/agent.md`, the three `inbox/2026-09-09-*.md` letters, `scripts/inbox_lifecycle.py` (grep), `PLAN.md`, `DECISIONS.md`, `.live-spec/profile.md`, `docs/prover/2026-09-04-recommendations-stop-queueing-review.md`, `spec/design-spec-review.md`, `skills/live-spec-base/SKILL.md` (lines 405-449), `skills/live-spec-base/references/rule-origins.md` (lines 144-235), `NEXT_STEPS.md`, `WAITING.md`, `FEEDBACK.md`, `JOURNAL.md` (head and lines 3755-3835, grep), `scripts/plan_checks.py` (line 589), `.live-spec/checkpoints/q-829.md` (grep), `tests/test_release_6_1_1.py` (counts), `scripts/task-admission.py` (lines 60, 700-750, 835-870), `guardrails/pre-push` (lines 215-282 and banners), `scripts/state-probe-extras.sh`, `spec/engine-instance-pair.md:12` (grep), and git show of 6389cb9f, a4554732, a8c54239 and e61b29b7.

**Effort:** about 13 Grep-tool or ripgrep searches plus about 25 grep/git-grep/`git log -S` searches run inside Bash. About 42 tool calls in all, roughly 15-20 minutes.

**What made answers hard to reach:**
- I could not run the probe read-only, because of `git fetch` and the python3 stub.
- `plan-step.sh` fails silently on this CRLF checkout.
- `DECISIONS.md`'s open section is stale against both the 2026-08-13 delegation and the 2026-08-21 removals.
- Gate letters were reused (u).
- Q8's "where it stands" rests on the local `origin/main` ref only.
- The test-suite impact of deleting `gates.yml` is inferred from the test code, not run.
```
