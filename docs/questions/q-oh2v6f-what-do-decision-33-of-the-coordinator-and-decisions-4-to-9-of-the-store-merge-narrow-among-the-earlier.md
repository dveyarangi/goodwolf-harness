# q-oh2v6f What do decision 33 of the coordinator and decisions 4 to 9 of the store merge narrow among the earlier decisions, and what do they leave unsaid of CI?

- **record of** what happened
- **part of** q-7ebz2f
- **state** closed:decided
- **answer** [q-7ebz2f, decisions 35 to 45, the list kept by decision 31](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md#decisions) — the user, 2026-11-09
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-09T07:51:27Z
- **struck** 0, last 2026-11-06T04:16Z

Opened 2026-11-06 by the scheduled `/maintain` pass with no person, sweeping the decisions landed
since bd36056e through 64334a6a. Decision 33 of
[q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md)
names 22, 5 and 29, and decisions 4 to 9 of
[q-7slcca](q-7slcca-how-do-two-copies-of-the-question-store-merge-and-where-in-git-do-their-changes-travel.md)
name 22, 29, 23 and 32; the question sits at the load-bearing rung, so the pass asks rather than
repairs. Below, a bare number is a decision of q-7ebz2f, and M with a number one of
q-7slcca.

- The decisions, the user, 2026-11-05: 33, one server across machines, for the questions and the
  rows; M4, the server works out which state is right, a merge deciding nothing new, the rare case
  going to a session's window; M5, a write stands where the server cannot be reached, the server
  merges it, the one place a merge happens; M6, a machine's hash in the row and the record; M7, a
  merge checked before its commit; M8, a header merging by field, the derived address in no file;
  M9, in the server mode a pull request carries no questions, CI reading the store's branch by a
  fetch, since it cannot reach the server.
- The earlier decisions they meet without naming them:
  - M1, "Git's own merge of the files is the merge rule … A conflict stands in git's own form",
    against M4 and M8; repeated in 29.
  - 18, "Only where no coordinator can be — an install's gate in a recipient, the tests — a check
    reads its own tree", and 26, "A fresh clone and CI need no copy of the questions", against M9.
    26 was brought back by M2 with those words in it.
  - 8, "One writer of the truth catches every race with one check", against M5: a write away from
    the server meets no fingerprint.
  - 27, "No home of the coordinator's own; no setup … raised by the first call", against 33's
    address, which the person sets.
  - Decision 3 of
    [q-crvu5f](q-crvu5f-what-carries-the-shared-place-every-session-reads-at-each-step.md),
    "between clones and machines carried by a push and a fetch of that namespace", against 33.
- Already held, each carrying a dated line from this pass:
  [q-upe7cs](q-upe7cs-does-decision-29-of-the-coordinator-narrow-its-earlier-decisions-that-raise-one-coordinator-on-a.md),
  whose option 1 keeps 4 and 5 for one machine, which 33 reverses, and which holds 10, 13 and 28;
  [q-khalk7](q-khalk7-do-decisions-23-24-and-26-of-the-coordinator-overturn-its-earlier-decisions-that-keep-the-store-in-the.md),
  the CI workflow's checkout against 18 and 26;
  [q-33lrbn](q-33lrbn-what-do-decisions-30-and-32-of-the-coordinator-narrow-and-what-do-they-leave-unsaid-of-the-local-folder.md),
  the rows in the local folder mode, where `.agents/skills/conclude/SKILL.md` line 37 and S3 in
  `.agents/mechanisms/session/session.rules.md` commit a row that M6 says does not travel;
  [q-ntoyr3](q-ntoyr3-does-the-coordinator-the-stores-one-writer-retire-the-product-answer-that-the-harness-locks-nothing.md),
  "every write";
  [q-n3osn2](q-n3osn2-what-do-decisions-1-2-and-3-of-the-store-merge-overturn-among-the-coordinator-decisions-and-what-do.md).
- What they leave unsaid: M9 has CI unable to reach the server, while
  [q-c2qp5n](q-c2qp5n-how-do-the-harnesss-checks-run-without-the-agent-at-push-and-in-the-projects-ci-beside-its-own-gates.md)
  lines 21 and 127 run all nine checks in CI and the RFC of
  [01-0010.0250.0090 the-rows-live-in-a-database](../tickets/01-0010.0250.0090-the-rows-live-in-a-database.md)
  lines 63 to 65 has `sessions.py --check` read the rows through the coordinator, with no row in any
  commit.
- Marked by this pass, in the decisions' own words and adding nothing: 33 in the out-of-scope lines
  of 01-0010.0250 and the RFC of 01-0010.0250.0030 and in the RFC of 01-0010.0250.0090; M5 at the
  refusals of the ticket and RFC of 01-0010.0250.0030; M6 in the RFC of 01-0010.0250.0090; M4 and M7
  in q-7slcca's own table. The workflow of
  [01-0010.0240.0020 this-trees-ci-runs-every-check](../tickets/01-0010.0240.0020-this-trees-ci-runs-every-check.md)
  waits on q-khalk7, and q-c2qp5n stands changed and uncommitted in
  the working tree.

Options:

1. **M1 marked narrowed by M4 and M8**, no log apart and git's history as the log kept; **18 and 26
   marked narrowed by M9**; **8 marked for writes through the server**; **27 marked for a tree on one
   machine**; **q-crvu5f's 3 marked across machines by 33**; in the server mode
   `sessions.py` leaves CI, which has no rows to read; q-upe7cs's option 1 rewritten
   so that 4 and 5 stand across machines, brought back by 33.
2. **Each is weighed apart at `/align`**, with the same questions: M1 reworded rather than marked;
   whether a direct body edit is refused at all; whether a second machine can pick up the address
   with no step of the person's; `sessions.py` kept in CI, reporting nothing there.

Recommendation: 1 — each of these states what still holds once its scope is written beside it, and
the marks fall into the pass decision 31 sets; only `sessions.py` in CI is a new choice, and a check
with nothing to read is a check that need not run.

Decision 10 of q-7slcca, the user, 2026-11-08, sends a write away from the one
server through a temporary server of the machine's own: 8's "a write away from the server meets
no fingerprint" leaves unsaid whether that server checks it.

The user, 2026-11-09: option 1, carried out in the pass decision 31 of q-7ebz2f sets.
