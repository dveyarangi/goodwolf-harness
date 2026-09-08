# Harness architecture

This document records the agreed maintenance boundaries. It does not define the remaining
cross-project distribution system. Terms belong in a glossary — the method's in
[`.agents/glossary.md`](../.agents/glossary.md), this project's own in [`docs/glossary.md`](glossary.md); maintenance
policy is `/maintain`'s body, declared at [`.agents/mechanisms/maintain/`](../.agents/mechanisms/maintain/maintain.md).

## Current and agreed target

The installed skills support the whole delivery ring. `/maintain` and its supporting scripts
landed 2026-09-06 under [01-0010.0070](tickets/done/01-0010.0070-install-maintain.md), closed the
same day, and `/maintain` was declared through the mechanism shape on 2026-09-07. Skill bodies
have one physical home under `.agents/skills`, with host access described in
[the installed harness](../.agents/README.md).

The mechanism is one maintenance skill directing an integrated procedure over a declared scope,
with supporting scripts under `.agents/scripts/` performing mechanically derivable work.
The first live scope is recorded in the owning ticket; scope does not exempt relevant
dependencies or affected references from maintenance.

## Responsibilities

- `/maintain` holds four things in agreement at drift scope — docs to the meta-rules, docs to
  their implementation both ways, live records to their format, every fact to one home — and
  repairs under the repair policy; it handles temporary statements and determines eligibility
  for archive operations. Agreement over a landed slice is `/verify`'s.
- Supporting scripts enumerate artifacts and perform mechanical transformations. They do
  not invent completion evidence, decide architectural questions, or turn an arbitrary
  expiry condition into authority to execute code.
- `/align` owns unresolved decisions. `/verify` owns verification of delivered work against
  its ticket, RFC, governing documents and the project's verification set.
- The queue owns current delivery state. Tickets and RFCs retain work decisions and evidence;
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
verification, are met before submitting the ticket and RFC together for movement.

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

This contract does not promise atomic multi-file writes, persisted transaction recovery or
safe simultaneous writers. Recheck expected file contents and destination absence before
applying changes; detected interference is a failure, not authority to overwrite it.

The writing technique belongs to helper implementation. Git is a recovery fallback for
committed or staged content; it does not generally recover overwritten unstaged edits.
Recovery must account for the actual working state and preserve unrelated changes. This
install adds no separate recovery mechanism.

### Temporary statements

[The entry contract](../AGENTS.md#temporary-statements) owns temporary-statement syntax,
ticket binding and expiry. Enumeration provides source locations and the written condition
and owner; the maintainer establishes whether the condition holds from evidence. Unknown
conditions remain unresolved. Mechanical removal follows that disposition and preserves
surviving agreements. Examples describing the syntax are distinct from operative statements.

A removal request identifies an entire obsolete statement; the mechanical tool does not
decide whether nested statements have also expired. Reject an outer-block removal while it
contains nested blocks. The maintainer disposes of children first and rescans before another
removal; active children and enduring agreements require preservation before the outer
statement can be removed.

### Installed blocks

[The shape](../.agents/skills/mechanism/SKILL.md#rules-injection-and-retraction) owns what a
rule is and where it lives; [the format shelf](../.agents/skills/mechanism/MECHANISM-FORMAT.md)
owns the rules file's grammar. A rule's only authored home is its mechanism's rules file. It
reaches a skill as an `<installed by="<slug>">` block written by one generic installer: one
block per mechanism per target, holding every rule that mechanism sends there in its rules
file's order, each opening with its id, and nothing else, after the anchor line the rules file
names for that target. A mechanism has one place in a target. The entry file owns the
prohibition on editing a block in place.

The installer has a named mode or refuses. It validates every target of a file before writing
anything — target present, anchor matching exactly one line, block absent or matching — and a
refusal changes no file. Retraction removes exactly what installation added, leaving the target
byte-identical. A block that differs from its source is drift: the tool cannot tell an amended
source from an edited copy, so it refuses unless the caller says to overwrite, and then it
replaces the block whole and reports what it replaced. A mid-write failure follows
[interruption and recovery](#interruption-and-recovery).

A rules file's block is installed in every target it names, or the tree's check fails: an
absent block, a drifted block, and a block whose owner has no rules file are each a diagnostic.
The installer writes no doc and decides nothing about a mechanism's state.

## Deferred decisions

- The pacer owns session resumption and turn progression. This maintenance install does not
  define a scheduler, session retention window or automatic next cycle.
- Cross-project distribution, generalized local overrides and dependency tracking retain
  their existing owners in the shared-harness work.
