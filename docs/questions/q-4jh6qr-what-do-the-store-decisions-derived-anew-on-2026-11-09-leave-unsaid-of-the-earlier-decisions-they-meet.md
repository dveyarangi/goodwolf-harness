# q-4jh6qr What do the store decisions derived anew on 2026-11-09 leave unsaid of the earlier decisions they meet without naming?

- **record of** what it intends to become
- **part of** q-7ebz2f
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **asks** the person, 2026-11-10
- **opened** 2026-11-10T04:23:41Z
- **struck** 0, last 2026-11-10T04:23Z

Opened 2026-11-10 by the scheduled `/maintain` pass with no person, sweeping the decisions landed
since f61c52a0 through fad11189. The decisions of
[q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md)
were derived anew on 2026-11-09 as 1 to 16; the question sits at the load-bearing rung, so the
pass asks rather than repairs. Below, a bare number is one of those sixteen.

## What each earlier text says, and where

1. **The git ref and the refusal of a server.**
   [q-crvu5f](q-crvu5f-what-carries-the-shared-place-every-session-reads-at-each-step.md),
   its decisions 1 to 4 and its `lean`: "a local mode first", "Not … SQLite, not a server", "A git
   ref carries it", and a chain of citations to decisions 4, 17 and 30 of the old list. Against 1
   (one mode, one server for every tree) and 10 (the rows in the server's `gw.sqlite`). The new
   list does not say whether its decisions 2 and 3 are withdrawn outright or were only ever for a
   mode that no longer exists.
   - Options: (a) both withdrawn, the question closed as superseded by 1 and 10; (b) the git ref
     kept for some use the sixteen do not name.
   - Recommendation: (a) — 1 leaves no tree without the server, so nothing is left for the ref to
     carry.
2. **The session's branch in the architecture.** `docs/architecture.md`, *Write safety*, the straw
   dog bound to q-7ebz2f: "A branch per session comes only together with a question
   store that does not travel through git. *(the user, 2026-10-12)*". Against 2: the questions are
   files on a branch of their own of the project's own repository, committed and pushed.
   - Options: (a) the sentence rewritten to 2's words — no code branch carries a question — under
     the date of 2; (b) left as the straw dog it is until the question closes.
   - Recommendation: (a) — the sentence now says the opposite of what was decided, in the document
     every session reads.
3. **The detached head.**
   [q-d4gf2u](q-d4gf2u-does-every-write-of-a-question-go-through-a-server-raised-on-demand.md),
   its `lean`, the user, 2026-10-30: "where the main checkout stands on a detached head the
   coordinator does not commit for now and the window says so; a branch of its own weighed when it
   reaches xuanxue-cabinet". Against 2: the branch is taken, and the server commits there, never
   in the main checkout.
   - Options: (a) the lean rewritten to 2; (b) kept, the detached head still a case of its own.
   - Recommendation: (a).
4. **A deferral whose condition cannot arrive.**
   [q-f5ixy2](q-f5ixy2-how-does-the-store-remember-every-id-it-has-given-so-none-is-given-twice.md),
   closed deferred "until a stale id … lands silently on the question its id was given to after a
   rename, meanwhile a new id is checked free against every entry live and in done/". Under 6
   there is no rename and no `done/`.
   - Options: (a) closed as moot under 6, as q-frv4bk and .0010 were; (b) kept
     deferred, its condition reworded to what a random id can still collide with.
   - Recommendation: (a) once the ids of this tree are converted; until then the old condition
     still describes the tree.
5. **The nine checks in CI.**
   [q-c2qp5n](q-c2qp5n-how-do-the-harnesss-checks-run-without-the-agent-at-push-and-in-the-projects-ci-beside-its-own-gates.md),
   its lean and decision 1: "Nine: `questions.py`, `sessions.py` … In CI all nine run on every
   run", and the push "checked in a copy of what it sends". Narrowed by 13 — CI checks the
   questions from the fetched store branch, and not the rows, which never reach it — and 10,
   neither naming it; the main question's *Hidden edges* leaves the push open: "reads the store's
   checkout instead, or leaves the code's push". The file stood changed and uncommitted by an
   ended session when this pass ran, and the pass wrote nothing there.
   - Options: (a) CI runs eight and reads the questions by a fetch, the pre-push check reads the
     store's checkout; (b) the same in CI, the questions' check leaving the code's push
     altogether, the server's own check being the gate (12, 13).
   - Recommendation: (b) — 12 has every write checked before its answer, so a second check at the
     code's push guards nothing new.

## Brought to the decisions by this pass, in their own words and adding nothing

6 in `docs/architecture.md`, *Straw dogs*, and at decisions 24, 34 and 43 of
[01-0011.0100](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md); 1 in the RFC
of 01-0010.0250.0020, in q-3n54ky and, with 10, in q-pl3fwk and as a
dated note under the decisions of q-crvu5f; the stale numbers in
q-ntoyr3 pointed at 1.2, 4, 5, 7 and 8; the guard of the withdrawn 01-0010.0250.0060
out of 01-0010.0250's related line.

## Left to their own tickets

The RFCs of 01-0010.0250.0030 and 01-0010.0250.0090 predate the re-cut, and their tickets say so.
The shipped text that still has the id as the place, a move renaming and a closed subtree going to
`done/` — the questions skill and format, the questions and session mechanisms, Q4 — is stage 7 of
the RFC of 01-0010.0250.0100; stages 2 to 4 are committed, so until stage 7 that text disagrees
with the code as well. `migrate_ids.py` and its test carry no `# Mechanism:` line, and
`docs/questions/former-ids.md` is declared by no mechanism: the RFC names no stage for either.

## Decision 6 as changed on 2026-11-10 — the file's name

Added 2026-11-11 by the scheduled `/maintain` pass with no person, sweeping 118788eb through
118d77a4. Decision 6 now names a file by its id and the question's words as it was opened,
`<id>-<slug>.md`, kept for good, a reword changing the title alone; 1.4 gained "A question reads
easily to an agent and to the person wherever it is cited".

6. **The link's path in decision 3.** [q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md#decisions), decision 3: "A link to a
   question, `docs/q/<id>.md`, is the same everywhere"; and
   [01-0010.0250.0110 the-questions-live-on-a-branch-of-their-own](../tickets/01-0010.0250.0110-the-questions-live-on-a-branch-of-their-own.md),
   *What to build*: "links into the store become `docs/q/<id>.md`". Against 6: the file, and so the
   link's path, carries the words. The split's wording of 2026-11-09 in the same entry, "Random
   ids, files named by them" and the slug budget under *May simplify*, is the same narrowing.
   - Options: (a) decision 3 and the ticket read `docs/q/<id>-<slug>.md`, under the date of 6's
     change; (b) left, the link's form settled when .0110 is planned.
   - Recommendation: (a) — 6 leaves nothing else the path could be.
7. **Whose words the slug holds.** Decision 55 of
   [01-0011.0100 the-open-questions-are-kept-by-a-mechanism](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md):
   "the slug holds all of them … The entries already written are renamed with the mover". 6 cites
   it and narrows it: the slug holds the words as opened, not the words a reword gave. In this
   tree the entries are still named by the id alone, and `migrate_ids.py --words` names each by
   its title as it stands today — for a question reworded since it was opened, not the words it
   was opened with.
   - Options: (a) a note at decision 55 that 6 narrows it, and today's title taken as the opening
     words for the entries converted, said in 6; (b) the opening words recovered from history for
     each reworded entry.
   - Recommendation: (a) — the name is kept for good from the conversion on, which is what 6 is
     for; recovering 366 first wordings buys a reader nothing.

Brought to 6 by this pass, in its own words: the note at decisions 24, 34 and 43 of 01-0011.0100,
and three comments in `questions.py` and `tickets.py`.

Left to [01-0010.0250.0100 a-questions-id-never-changes](../tickets/01-0010.0250.0100-a-questions-id-never-changes.md):
its RFC carries 6 in *What governs it* and *The file* and still plans the name by the id alone in
*What goes* (the slug budget and `_fitted_slug` leaving, `_files_holding` on `<id>.md`), *The
migration* steps 3 and 4, and stages 4 and 5, its *Last amended* still 2026-11-09; it names no
stage for the `--words` run, and this tree's 366 entries are still named by the id alone. In the
code: the finding "is not named `<id>.md`" and the test that holds it, `recheck`'s docstring on
renamed entries, `test_a_file_named_by_its_id_alone_checks_clean`, and `questions.py`'s module
docstring, which still tells the dotted model. The shipped text — the question format's "A reword
changes the words and the file's name", the skill's "its file takes the words" — is stage 7, as
above.
