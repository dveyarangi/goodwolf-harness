# Harness architecture

This document records the agreed maintenance boundaries and, since 2026-09-21, the contract by
which core reaches another tree. It does not define contribution back or releases. Terms belong
in a glossary — the method's in
[`.agents/glossary.md`](../.agents/glossary.md), this project's own in [`docs/glossary.md`](glossary.md); maintenance
policy is `/maintain`'s body, declared at [`.agents/mechanisms/maintain/`](../.agents/mechanisms/maintain/maintain.md).

## Current and agreed target

The installed skills support the whole delivery ring, and `/maintain` is declared through the
mechanism shape. Skill bodies have one physical home under `.agents/skills`, with host access
described in [the installed harness](../.agents/README.md).

The mechanism is one maintenance skill directing an integrated procedure over a declared scope,
with supporting scripts under `.agents/scripts/gw/` performing mechanically derivable work.
The first live scope is recorded in the owning ticket; scope does not exempt relevant
dependencies or affected references from maintenance.

## Responsibilities

- `/maintain` holds four things in agreement at drift scope — docs to the meta-rules, docs to
  their implementation both ways, live records to their format, every fact to one home — and
  repairs under the repair policy; it handles straw dogs and determines eligibility
  for archive operations. Agreement over a landed slice is `/verify`'s.
- Supporting scripts enumerate artifacts and perform mechanical transformations. They do
  not invent completion evidence, decide architectural questions, or turn an arbitrary
  expiry condition into authority to execute code.
- `/align` owns unresolved decisions. `/verify` owns verification of delivered work against
  its ticket, RFC, governing documents and the project's verification set.
- A ticket's header owns its delivery state; what comes next is the path's reading, shown at
  every `/recall`; the live tickets are listed from their headers on request, never copied
  ([01-0011.0040](tickets/done/01-0011.0040-the-ticket-list-is-rendered-never-copied.md), the user,
  2026-10-10). Tickets and RFCs retain work decisions and evidence;
  the mechanism's [evidence record](mechanisms/maintain.evidence.md) retains observations
  that inform maintenance of the mechanism itself.

## Contract surfaces

### Scope and coverage

The maintenance caller declares the work being maintained. Applicable obligations and their
dependencies determine the covered artifacts; a filename-only selection cannot establish
semantic completeness. A narrow close can require reference repairs across the repository
without certifying architecture or unrelated work across that repository.

### Paired record close

[Ticket format](../.agents/skills/ticket/TICKET-FORMAT.md#one-basename-per-work-item)
governs eligibility and destinations. The caller determines that the criteria, including
verification, are met before submitting the ticket and RFC together for movement. The ticket
maintainer holds every live ticket to the shape the format declares and reports a pair whose
halves sit in different folder states; it decides nothing about eligibility.

The mechanical operation preserves basenames, repairs the moved records' outgoing and mutual
references, and repairs incoming references. Historical records participate: repairs preserve
their recorded facts, evidence and decisions. Moving a record does not itself establish that
its work was verified, and a failed operation is unfinished maintenance.

Reference identity depends on its resolved target. A local absolute reference to a selected
record follows that record just as a relative reference does; references outside the move's
mapping retain their targets. A reference rewrite preserves bytes outside the changed target.

### Interruption and recovery

Before writing, the mover validates the complete selection and derives the required moves
and reference changes. A preflight refusal changes no files. The operation does not alter
the Git index; staging and commit remain caller actions under the project's autonomy rules.

If an I/O error occurs after mutation starts, stop, return failure and report completed
operations, pending operations and the failed path. Do not automatically roll back.
The maintainer inspects actual files and recovers under the existing repair policy before
reporting completion. Emit operation progress as it occurs; after abrupt termination the
last attempted operation can be uncertain and must be checked against the filesystem.

This contract does not promise atomic multi-file writes or persisted transaction recovery.
Nor does it promise safe simultaneous writers. Keeping two sessions out of one file is the host's
responsibility — its edit tool refusing a write over a file changed since the agent read it, and a
worktree per session where it offers one — not the harness's: it locks nothing. Its own scripts refuse a write to an entry that moved since it was
read. *(the user, 2026-10-11)*
Whatever stands on the shared main may be published; work the person holds back stays on its own
branch until they release it. *(the user, 2026-10-12)*
<straw-dog question="q-0037.0017.0005.0001">
Sessions share one checkout and its main. A branch per session comes only together with a
question store that does not travel through git. *(the user, 2026-10-12)*
</straw-dog>
Recheck expected file contents and destination absence before applying changes; detected
interference is a failure, not authority to overwrite it.

The writing technique belongs to helper implementation. Git is a recovery fallback for
committed or staged content; it does not generally recover overwritten unstaged edits.
Recovery must account for the actual working state and preserve unrelated changes. This
install adds no separate recovery mechanism.

### Straw dogs

[The entry contract](../AGENTS.md#straw-dogs) owns the `<straw-dog>` syntax and the duty to wrap.
A straw dog binds to a question of the store, never to a ticket — the one record of this tree
core names. Whether it is due is derived from the store at every look; the maintainer decides
how its text is rewritten. A rename of the store's ids carries every binding
([01-0011.0100.0030 a-straw-dog-is-bound-to-the-question-it-waits-on](tickets/done/01-0011.0100.0030-a-straw-dog-is-bound-to-the-question-it-waits-on.md#decisions-landed-at-this-tickets-align)).
Mechanical removal follows the maintainer's disposition and preserves surviving agreements.
Examples describing the syntax are distinct from operative statements.

A removal request identifies an entire obsolete statement; the mechanical tool does not
decide whether nested statements have also expired. Reject an outer-block removal while it
contains nested blocks. The maintainer disposes of children first and rescans before another
removal; active children and enduring agreements require preservation before the outer
statement can be removed.

In code the marking is a comment line beginning `TODO` that names its question; it leaves with
the code rather than through the tool.

The listing tool may also guess, from the words a sentence carries or a `TODO` that names no
question, where a straw dog stands unwrapped. A guess is a finding for the maintainer, never a
diagnostic, and never moves the run's status; what has no named successor is a claim and is
left as written.

### Question store

The store is shared by every session working in the tree; a position is one session's. An entry's
parts are written only by the script's calls, one per event; its body, the question's argument,
is written by hand, and every call keeps it as it found it
([decision 3](tickets/done/01-0011.0100.0020-open-issues-are-entries-of-the-store.md#decisions-landed-at-this-tickets-align)).
A write re-reads every entry it changes and refuses one that moved since it was read — a hand edit
included; detected interference is a failure, as in
[interruption and recovery](#interruption-and-recovery). A new question's id is the script's to
draw, and one another session took meanwhile is drawn again. An id says where the question sits —
a root `q-NNNN`, a child its parent's id and one more position — and stays true: a re-parent
renames the moved subtree in the same call, its files and every id and link to them across the
records under `docs/`, mechanically and without forwarding the old ids
([decision 6](tickets/done/01-0011.0100.0020-open-issues-are-entries-of-the-store.md#decisions-landed-at-this-tickets-align)).
A session's row is [the session mechanism](../.agents/mechanisms/session/session.md)'s, and the
mechanism manages every session from any one of them: any session writes any row through the
session script *(the user, 2026-10-25)*. A row is one file, replaced in one rename, so a reader
never meets half of it and nothing is locked; a wake ends the silent and removes the long ended, a
rename rewrites the ids a row names, and a takeover moves a held unit and leaves its mark in the
holder's row *(the user, 2026-10-10 and 2026-10-25)*. A wholly closed subtree moves to `done/` with the mover in the `close` call that
finishes it; the maintainer's move is the sweep for what a closure left behind. A host's hook
delivers the window and registers the session under the host's steadiest id, and never fails
the host: a problem becomes a line of context. Everything else is
[the questions mechanism](../.agents/mechanisms/questions/questions.md)'s.

### Installed blocks

[The shape](../.agents/skills/mechanism/SKILL.md#rules-injection-and-retraction) owns what a
rule is and where it lives; [the format shelf](../.agents/skills/mechanism/MECHANISM-FORMAT.md)
owns the rules file's grammar. A rule's only authored home is its mechanism's rules file. It
reaches a skill as an `<installed by="<slug>">` block written by one generic installer: one
block per mechanism per target, holding every rule that mechanism sends there in its rules
file's order, each opening with its id, and nothing else, at the end of the section the anchor
line heads — after the section's own text and after every block already there, so blocks stand
in install order *(the user, 2026-09-21; until then directly after the anchor line)*. A section
runs to the next heading of the anchor's level or higher. A mechanism has one place in a target:
a file its own row names and a group of the same source also reaches holds one block, at the named
row's anchor, carrying both rows' rules; a file two groups reach is refused *(the user,
2026-10-25)*.
The entry file owns the prohibition on editing a block in place. The project's own rules file,
`local.rules.md` beside the entry file, is one more source: its block lands last in its section
and after every mechanism's in a target, and a rule in it may name the core rule it overrides,
which is rendered where the reader meets it.

The installer has a named mode or refuses. It validates every target of a file before writing
anything — target present, its anchor matching exactly one line, block absent or matching and in its anchor's section — and a
refusal changes no file. Retraction removes exactly what installation added, leaving the target
byte-identical. A block that differs from its source is drift: the tool cannot tell an amended
source from an edited copy, so it refuses unless the caller says to overwrite, and then it
replaces the block whole and reports what it replaced. A mid-write failure follows
[interruption and recovery](#interruption-and-recovery).

A target is a file, or a group: a path pattern whose members are the files it wholly matches that hold its anchor line — a matching file without it is no member, and a group may have none *(the user, 2026-10-25)*. A rules file's block is installed in every target it names, each member of a group included, or the tree's check fails: an
absent block, a drifted block, and a block nothing owns — its owner has no rules file, or that
file does not name the file the block sits in — are each a diagnostic. Installing a rules file
also takes its own block out of every file it no longer names, by retraction's cut, and reports
what left *(the user, 2026-10-09)*.
The installer writes no doc and decides nothing about a mechanism's state.

**A tree carries the method's text its settings call for.** A mechanism declares the settings it
owns in its rules file — name, values, default, who may set it — and the project sets their
values in its local file, a setting left unset standing at its default; a rule of any installed
mechanism may name a condition of its installation, `when <setting>=<value>`, and the installer
writes it into its targets only while every condition holds, taking it out by retraction's cut
when none does. A block that differs from its rendering only in which of its file's own rules
it holds differs by the settings alone and is re-rendered without being asked; an edited copy or
an amended source still refuses. The run over every source, mechanisms then local, is
idempotent and is what an install, an update and a changed setting all run; the agent is the
interface to the values, by one call that refuses, writes, runs and reports, and a hand edit is
drift the next session's start reports and repairs *(the user, 2026-10-22 and 2026-10-23,
q-0037.0006.0026)*. The settings table is rendered on request and never committed. A setting a
script reads at run time is read from the main checkout's local file — the working tree of the
project's common Git directory — and not from the session's own branch, which may carry another
value; it is set there *(the user, 2026-10-30,
[q-0037.0017.0005.0001](questions/q-0037.0017.0005.0001-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of.md) decision 12)*.

### Installing

The install contract is the harness mechanism's, in [its doc](../.agents/mechanisms/harness/harness.md):
the source a repository at a ref and never a working tree, the manifest and what is written or
merged outside it, the transformation, the announce and repository lines, what a target is and
what an install and an update refuse, the loader links and the interpreter record, and arrival as
the check. [The install spec](spec/01-0010.0130-harness-installs-into-another-tree.md) owns the
decisions behind it. The project's verification set is the project's: arrival runs none of it.
<straw-dog question="q-0037.0006.0022">A clone's push runs the method's checks through a hook the
link step writes only inside the project and never over the project's own; a push that carries a
file of the method is checked in a temporary copy of what it sends, and any finding in that copy
refuses it; the decision is
[q-0037.0006.0022.0004](questions/q-0037.0006.0022.0004-how-do-the-harnesss-checks-run-without-the-agent-at-push-and-in-the-projects-ci.md)'s.</straw-dog>

**The edge, and what crosses it.** The core–instance interaction is everything an instance must
know to integrate core, customise it and stay coherent across core changes: a rule id, a target
and its anchor, a script's path and command, a skill's name, the announce form, and a behaviour a
recipient's files rely on. Its engineering record is the origin's and does not ship; what a client
meets is derived from it — the front page and the harness skill. A change to it is registered
where it is made and reaches a recipient as a **release**: core published to a repository of its
own, each publish carrying a note written for an instance — what moved, from where to where, what
the instance amends. A recipient reads the notes standing between its ref and the latest before it
takes them, and whether to take them is the installing agent's decision with its user, never the
script's. *(The user, 2026-09-21.)*
<straw-dog question="q-0037.0006.0020.0002.0002">
Nothing does this yet: core is shared from the working tree and an update crosses an edge change
in silence, leaving what a recipient must amend to whoever reads the manifest diff.
</straw-dog>

## Deferred decisions

- The pacer dissolved (q-0037.0019): the ring's rules are the practice mechanism's, which work
  comes next is the pathfinder's; where a session resumes is the session mechanism's. This
  maintenance install does not define a scheduler or an automatic next cycle.
- Cross-project distribution, generalized local overrides and dependency tracking retain
  their existing owners in the shared-harness work.
