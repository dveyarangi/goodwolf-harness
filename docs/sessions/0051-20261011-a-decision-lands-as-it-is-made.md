# Session 51 — a decision lands as it is made

- **record of** what happened

2026-10-11. Opened on `/recall` and went round the delivery ring twice: 01-0011.0110.0040.0020
planned, implemented, verified and closed, then 01-0011.0110.0060 the same. Between them the
reply's layout went under one straw dog, and the rule-failure register began counting slips.
Four other sessions ran beside this one all day, two of them writing the entry file.

## Decisions, and what chose them

**A ticket says when it was minted** (01-0011.0110.0040.0020, decision 1). The spec had the check
read a mint date from the header, which had none, while 26 of 34 live tickets held sections the
narrowed format no longer admits. An optional `Minted` would let a forgetful agent escape the
check unseen; a marker on the old tickets would live only for the migration. The user chose a
required field, every live ticket dated by its file's first commit — the strictness `.0010` had
chosen for its marks, for the same reason.

**An align's decisions are written in the question's file, never the ticket** — *однозначно*, the
user. Where in the file, and who sees a child's decision, took five rounds:

- *The question's `close` guards its list* was refuted first: high questions close rarely — *это
  проблематично особенно в случае высоко сидящих корневых вопросов* — so a guard there never fires.
- *The child points at the parent's list as a temporary home* was the user's own reading; the child
  is closed and owes nothing.
- *The parent sees descendants' decisions rendered in the window* was refuted by asking who reads a
  parent: an agent opening its file, or the person in an editor, sees no window.
- *One list per task, the ticket's question* was refuted by the user: *какой еще тикет если мы
  предыдущим решением вывели тикеты из уравнения?*
- *A child either lands its decision or hands it up* (the user) led to the archive: of 44 decided
  closures 37 pointed at a durable home, five at a ticket, none at a parent question, and no entry
  said why it handed up.

The turn came from the user: *возможно такое правило — быстрого приземления — должно приземлять как
straw-dog?* — and, asked not to flatter, the assessment held: the straw-dog machinery already has
binding, dueness and the wake's listing; R5 already lands an undeclared mechanism's rule this way;
and a decision in force where it is read beats a correct one in a drawer. The user went further —
*в самом начале проекта я вообще думал сделать ВСЕ собакой* — and the archive measured it: 37 of 44
decided children closed under an open parent, so most landings would be straw dogs, while 102 of
the tree's 150 are already one line. Two corrections shaped the rule: `suspect` is a different case
— *это родитель поменялся по внешним причинам. мой случай — родитель поменялся в результате своих
детей* — and an open child can sit under a closed parent, so the binding is to the nearest *open*
ancestor. Landed as the questions mechanism's Q6, installed in `/align`: final where no open
question can change the decision, a straw dog bound to that ancestor otherwise, and a line in a
question's `## Decisions` list only where there is nowhere to land yet. The question guards that
list (`close` refuses an item with no `→`), and the ticket guards nothing.

**A home is one predicate.** At the plan's second pass the owner clause in `due` was replaced: a
link is a home when it resolves outside the store, tickets and RFCs, read the same after `→` and in
an answer.

**The ticket's contract is stated in the format**, *the question it answers* wrapped as a straw dog
— *пометь, надо повесить на продумать* (q-0024.0009.0003.0002.0002).

**The reply's layout is one straw dog** bound to q-0023.0021 — the user is not sure whether a
debugging or an interaction mechanism will own it; the head table left Q1 and L6 retired into it
(v61, v62). With it, ⚖️ holds only what waits: a decision the agent had already taken had been
listed there for confirmation (rule failure 31).

**A slip no rule covers is registered** (rule failure 33, v67). A `questions.py --wake` run
without `--session` to read a straw dog registered a second session; it went unwritten because no
rule was broken, until the user asked whether it was written down *so you know later whether it is
the only one*.

**The mechanism shape holds its meta-rules in its own skill** (01-0011.0110.0060, v68). The align
had the two entry-file lines installed; the plan met *a mechanism has one place in a target*, the
shape's being `## Project-local`. The user saw past the fork: the proposed R9 *это дескрипшн
скилла* — the line restated `/mechanism`'s description at the same tier — and *тоже самое можно
провернуть и с An installed block is not yours, перевернув*: a prohibition turned into a use case,
its guard already in `inject_rules.py --check`. Nothing is installed in the entry file; the
glossary's *Meta-rule* follows. The ruling of 2026-09-20 — a hand-written rule in the entry file is
the copy the check cannot compare — stands: no line is hand-written there now, and a description
is tier 1, not tier 3.

## Principles without a home yet

- **Check a premise against the format before building on it.** Two plans this session stood on an
  assumption the format already refused: a mint date the header did not have, and a second place
  for a mechanism in one file.
- **Two tests for a tier-1 line**: does it restate a description read at the same tier, and does a
  check already hold it. Handed to q-0026.0006 as a lead, not landed as a rule.

## Done

01-0011.0110.0040.0020 — decisions land as made (Q6), the `## Decisions` list and its guard, `due`
by one home predicate, `Minted` on every live ticket, the contract; closed with its RFC.
01-0011.0110.0040's three slices are done; its own `/verify` waits. 01-0011.0110.0060 — the two
lines into `/mechanism`'s description, seven anchored rows out of the parts tables; closed with its
RFC, `harness.md`'s stale sentence repaired at the maintenance. q-0001.0010.0001 closed against the
new rules. The front page lost its L6 example. Entry contract v61, v62, v65, v67, v68 from here.

## What went wrong, and what it taught

- **Two sessions bumped the entry contract at once.** This session's v63 sat uncommitted while
  another landed v64 over it; renumbered v65 at the landing. An entry-file edit is committed the
  moment it is made, alone — done so for v67 and v68. q-0032 (locks) is where this belongs.
- **A new function shadowed an old one** of the same name in `questions.py`, silently: the close
  refusal never fired until a debug run showed the other `_landed` answering.
- **A command that writes was run to read** (rule failure 33).
- **A mark was set before reading another session's edits** to the files it covers; caught before
  the commit, read, and set again.
- **Three tests failed once each under load** across full runs and passed alone; their text was
  never captured. Four sessions running at once is the likely load; unproven.
- **An edit quoting a wrapped line did not apply** and its commit went without it; found by reading
  the result, committed after.

## Open questions touched

- q-0024.0009.0006 — `.0060` and `.0070` done, `.0080` next, which owns it.
- q-0024.0009.0003 — its three slices done; 01-0011.0110.0040's `/verify` next, its kind criterion
  open since no check holds an RFC's mark.
- q-0024.0009.0003.0002.0002 — must a board link each item to its question; open, a straw dog in the
  contract.
- q-0024.0009.0003.0002.0003 — deferred until no live ticket predates `Minted`.
- q-0001.0025 — straw dogs bound to a question, weighted by tier, as a ranking signal; open.
- q-0023.0021 — which mechanism owns a reply's layout; open.
- q-0026.0006 — reworded to what the shape should hold in its skill; the two tests as a lead.
- q-0025 — slips now counted beside rule failures.

## What continues

**First step:** the next cycle needs a nod — `/plan` for
[01-0011.0110.0080 a-doc-is-due-when-its-parts-move](../tickets/done/01-0011.0110.0080-a-doc-is-due-when-its-parts-move.md).
Then the place of 01-0011.0110.0050 in the queue, which the queue does not state, and
01-0011.0110.0040's own `/verify`.
