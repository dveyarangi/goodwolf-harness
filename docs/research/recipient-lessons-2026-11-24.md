# Lessons from a mature production project under the harness — 2026-11-24

- **record of** what happened

Sent to core's keeper on 2026-11-24 by a session named "Environment and harness review", working
in a recipient tree, on the person's word of that day. Kept as given; the holder of each lesson
is named after it. Nothing here is a decision.

## As sent

Lessons from a mature production project under the harness: causes core may act on, sent on the
person's word (2026-11-24).

From a tree that keeps a shared records repository beside three product repositories with legacy
code, its own Notion board and date-named tickets; harness 26dd3dba, now ed0f4e1d. Evidence is
three fresh-agent studies of about 17 Cursor sessions since 2026-09-27, the product history since
2026-08, and the records against the code; I spot-checked several claims, not all. The person
will have more sent later. No answer is needed; whose each is, is yours to say.

The person's own words are marked (P); the rest is my reading, agreed by them in general.

1. Opening a question. The entry file's questions/Q1 says not found: open it; the questions skill
   says the dial settles it, and below the dial it is settled in the turn. With an unset dial
   every small choice is the person's, so a design detail is stored: at least 8 of 25 entries
   were details of one list. (P) the store should hold load-bearing questions or investigations,
   "not questions about how to draw a button". Cause in core: Q1 does not defer to the dial.
2. Urgent work. I found no urgent path in your records. One incident fix changed a setting others
   read, skipped ticket, impact and verify, and very likely stopped a background service for
   about a day. (P) urgent does not mean the method is abandoned; urgent and small can. Missing:
   the line between urgent-small and urgent-wide, and a record after.
3. For the path's session — hazards weigh nothing. Pathfinder weighs a candidate by the product's
   answers; a security hole or a fault that takes production down leads to none. Here a written
   queue and a risk list both failed to start work: of 21 recorded concerns, three became work
   only after a production error, none of six ranked places closed, and a security hole stood
   behind features for three months because its record described two routes where an inventory
   found 35.
4. Silent zeros. Where ticket status lives on another board, the path's "in work" and "ready"
   always read 0 and none. It should say no status is readable, or read the board.
5. (P) A promise of something to come is written, preferably as a straw dog, each time it is
   made. Case: I told the person that stopgap rules would go when core carried its own, and wrote
   it only in the chat. The entry file already treats "not yet" and "until" in text as that
   signal; a promise made in a reply is not text anyone reads again, so nothing fired.
6. An update writes no per-clone part that arrived after the clone was linked: two updates
   arrived as complete with no pre-push hook and no line saying so.
7. "Install it with overwrite", in every rules file's head, was read by a session as
   harness.py --update, and moved core a version; naming the inject_rules command would have
   held.
8. An update that renames or drops a skill leaves a project's links to it dead; only the
   project's own guard saw it.
9. edges.py reads docs/edge/README.md as a record.
10. One Cursor chat stood as two sessions: the hook registered it by its chat id, and a tag
    minted by a bare wake in the same chat stayed beside it, holding the unit. Idle, both read
    running, and I told the person a session was working that was not.

Held back until tried here: what onboarding should check of a verification set that names no
product test, and migrating an existing risk list into the question store.

Carried here meanwhile as local rules, marked to go when core carries its own: the store's bar
(1), urgent work (2), hazards first (3).

## Whose each is

| lesson | holder in this tree | told |
|---|---|---|
| 1, a question opened below the dial | the store's session: the questions mechanism | 2026-11-24 |
| 2, urgent work | the practice's session: the delivery ring | 2026-11-24 |
| 3, hazards weigh nothing | the path's session | 2026-11-24 |
| 4, silent zeros | the path's session | 2026-11-24 |
| 5, a promise made in a reply | the keeper: the entry file's rule on straw dogs; put to the person | — |
| 6, a per-clone part an update does not write | the keeper: the harness mechanism; kept with the installer's faults | — |
| 7, "install it with overwrite" | the keeper: the rules file's form; kept with the installer's faults | — |
| 8, a renamed skill and a project's links | the keeper: the harness mechanism; kept with the installer's faults | — |
| 9, the edge check reads its folder's README | nobody's: no role names the edge mechanism | — |
| 10, one chat as two sessions | the store's session: the session mechanism | 2026-11-24 |

## A second message, the same day — as sent

One more from the mature project, on the person's word (2026-11-24): the mechanical parts of a
mechanism should take local configuration.

(P) "it basically means the mechanical parts should have local configuration, right? if you think
of it in harness's core terms."

The case. This tree's tickets take their own shape by a local rule that overrides ticket/P5, and
it keeps status on a board. The override reached the rule's text and nothing that runs:
`tickets.py --check` counts 121 problems on tickets that are right by the tree's own format, the
path reads a status that is not there, and the pre-push hook runs the same check, so writing it
would refuse every push that carries a record. `edges.py` likewise: 8 of 21 come from reading the
folder's index as a record. So the guard stays off here and pushes go unchecked.

My reading, for you to judge: an override of a rule changes what an agent reads, never the script
that carries the rule out, so a tree can keep its own practice only in prose. A setting is
declared today for what text a tree carries; a check, a hook and a wake reading read none.
Whether the answer is a setting a mechanism declares for its scripts, a check a tree may replace
by name, or the push's list of checks being the tree's, is yours. It bears on what you hold on
practice being swapped in one edit, and on points 4 and 9 of my earlier message. No answer is
needed.

| lesson | holder in this tree | told |
|---|---|---|
| 11, a rule's override does not reach the script that carries it out | the keeper: how projects share one method and keep their own conventions | — |

## A third message, 2026-11-25 — as sent

From DriftSense, a suggestion of the user's for core: self-monitoring also covers friction, not
only rule failures.

The user's words, to the Audit and security session here, 2026-11-25 (read in its transcript,
2026-11-24T22:11Z): "everywhere there is a friction - agents takes long time to find something
that would be frequently user - we should also fix those. actually, the later sentence should go
as suggestion to the keeper, not just about audit, but as general extension of self-monitoring."

What the sessions read of core at ed0f4e1d, not the user's: Self-improvement registers a rule that
failed and a slip no rule covers; the harness skill's "Friction goes upstream" covers a run of
that skill. Neither reaches work that succeeds slowly and will be repeated.

Cases met here, as that session reports them: the interpreter's full path is found again by every
session, since bare `python` does not run; a shell `cd` outlasts its call and moved the working
folder twice; a search that reached node_modules ran past two minutes; a process document names
the board's title column in a way its SQL refuses (met here too, today); the list of endpoints was
drawn from the code by hand twice in a day; whether an endpoint can be tested took reading several
files.
One of mine: a docs guard that lists files through Git reads a record moved to done/ as missing
until the move is committed, so a close cannot be checked before its commit.

The shape, and whether it is taken, are yours and the user's. No answer is needed until core
carries it or refuses it.

**Corrected by the sender the same day — as sent.** Its first case, the interpreter, was wrong as
written. The Audit and security session withdraws it: `uv run --offline --no-project python` is
given in the verify, maintain and harness skills and in this project's L5, and works. What holds
is narrower: the entry file shows the store's calls as bare `questions.py`, with no interpreter
beside them, and sessions here used a full path instead of the uv form (mine too). The other
cases and the user's words stand.

| lesson | holder in this tree | told |
|---|---|---|
| 12, friction beside a rule's failure | the keeper: the entry file's *Self-improvement*; the person's words read at their source, and a question opened for it | — |
