# The meeting — the study and the report

<straw-dog question="q-0037.0006.0020.0001">
Tier 2: read when an install meets a tree that already has a method — an entry file or an
`.agents/` of its own. The install writes nothing and stops twice; between the stops it studies the
tree and writes one file, the report. This shelf owns the study and the report; the two modes of
taking the tree's method in are the skill's.

## The two stops

**First.** Offer to read the repository and write up what the harness would change here; name the
one file it would write and where — `docs/sessions/0001-<date>-<slug>.md` under the tree's `docs/`;
a tree without `docs/` takes the place the person names — and wait. Silence takes the offer; another
place named takes that place. Nothing else in the tree changes before or after.

**Second.** Show the report in `/advise`'s form — what is good, what is good enough, what hurts,
what first — and ask whether the migration runs, which proposals, in which mode. Speak of the
report; do not retell it. Either answer closes the person's question — *what would the harness
change here?* — and the report, its body, stays: on *yes* as the tree's first record, its proposals
becoming tickets; on *no* as the one record the method leaves.

## The study

Read the tree as a capable newcomer would, by search and sampling, not whole; the tree is its
default branch as checked out, and what is deployed is not the study's subject. The study has three
parts, and the report says which part each statement comes from. The read is quick; the key is the
study's largest cost, built from what the inventory and the readings meet, never from a second pass.

**The inventory.** The entry file and what it includes; skills of the tree's own; scripts, gates and
checks and the rules that name them; outside coordinators and contracts; the kinds of record the
tree keeps — decisions, plans, runbooks, specs — and where its current state lives. This is what the
harness does not replace, said in the tree's own names.

**The four readings.** Each is one way a project's knowledge fails to reach the person who needs it,
counted and quoted in the tree's own words:

1. *What it costs to reach what is written* — files, searches, steps between a question and its
   answer; chains of records that supersede one another; documents readable only by search.
2. *Kinds of record mixed in one file* — instructions, decisions and history in one place;
   instructions in records the entry file names only as a whole, which reach a reader only if that
   record is opened.
3. *One fact in several homes* — the same rule or fact stated twice, and where the two have parted;
   what was met on the way, never claimed as all there is.
4. *What no one records* — the tree's memory of its own operation: sessions, handovers, why a piece
   of work stopped; the gap shows as history leaking into rules and as work no record explains.

**The ledger.** A measurement the report keeps so the same tasks can be measured again after a
migration. A blind run: a fresh agent, told nothing of the harness or of a measurement, is given the
repository and a sample of questions, answers read-only from files, git history and the PR list, and
reports how it searched. The author of the report never answers the sample; the key is built from
the code and the records before the run and corrected only where the run proves it wrong.

The sample, from the tree as it stands on the day:

| group | items | the key holds | scored |
|---|---|---|---|
| settled decisions | 5 | the decision and its reason; the question asks *why* | hit · partial · miss |
| in flight | 3 | the item and its state | hit · partial · miss |
| undecided | 3 | that it is open, and who decides | hit · partial · miss |
| resting on contradictory or incomplete records | 3 | the two records, or the record that stops short; asked about the topic, never the discrepancy | noticed and said · answered from one side · filled the gap |
| strong but hidden invariants or structures | 3 | what the code enforces and no record states as a rule — a per-case mention in a decision record is not one; what the tree's shape implies | recovered · not |

Counted beside the answers: tokens, tool calls and wall time from the host's account of the blind
run; files read from the blind agent's own account of how it searched. And what the project's method
asks of a change today, as numbers: rules read by every session — the entry file and every file a
rule orders read at every session —, CI jobs and steps per PR, checklist items, PR body length,
decision records per merged PR, check scripts. The project's practices stay
its own, kept by its choice; the harness integrates with them and replaces none. The count is there
so the same count after a migration shows what the harness is for: fewer steps, and each step more
precise, because at each step what is needed is known.

## The report

The body of the person's question, *what would the harness change here?*, headed by that question
in the project's language, and written in the project's names. No term or phrase of the harness's
own — mechanism, store, straw dog, tier, rung, install block, a session *standing on* a question —
appears; the study's parts are described by what they do; what the harness brings is said as what it
does for the project: a home for
each kind of record; a rule installed where it is read; open questions kept with their state and the
session's position among them; a record of each session; a disagreement between records repaired
where it is met; a decision kept with what it waits on.

Sections, in this order, each headed:

0. **How this was read.** What the study is — the inventory, the four readings named and said in one
   line each, the ledger and how it was taken; that the read is quick and sampled; that what it
   found is what it met, not an inventory, and that the harness repairs a disagreement where a
   session meets it, every session meeting its own. A reader who has not seen the harness understands
   every later section from this one.
1. **What was found.** By the inventory and the four readings, each a paragraph with its numbers and
   quotes; then what the method asks of a change, as the count; then what stays as it is.
2. **Main recommendations.** Three to five, each one sentence and its reason, about the project's
   documentation and its own method — its rules, gates and records — only; never about what the
   project builds.
3. **What clearly improves, and what the person will likely give up.** Two columns.
4. **Proposals.** A table: what, what it touches and what depends on it, size; then the order.
5. **What this report does not say.** No comparison of the tree's method with the harness before an
   install, a migration and a real check; no inventory of disagreements; the ledger measures one
   thing, the cost of recovering the project's state on a sample, and is far from the whole harness;
   the post-migration re-run is its own stage, optional.
6. **Appendix: the ledger.** The counts; the sample and its key; the blind run's return, whole and
   unedited. The ledger lives here and nowhere else in the report: the body argues from its counts
   and never restates it. It is kept so the check after a migration runs the same sample against the
   same key, scored the same way, and its ledger is appended beside this one, never merged into it.

The report is a product document: it shows the harness's strengths by finding where it helps, and
claims nothing the tree or the ledger does not show. No self-deprecation, no groundless comparison,
nothing about the project's substance.
</straw-dog>
