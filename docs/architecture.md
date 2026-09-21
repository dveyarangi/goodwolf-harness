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
with supporting scripts under `.agents/scripts/` performing mechanically derivable work.
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

This contract does not promise atomic multi-file writes, persisted transaction recovery or
safe simultaneous writers. Recheck expected file contents and destination absence before
applying changes; detected interference is a failure, not authority to overwrite it.

The writing technique belongs to helper implementation. Git is a recovery fallback for
committed or staged content; it does not generally recover overwritten unstaged edits.
Recovery must account for the actual working state and preserve unrelated changes. This
install adds no separate recovery mechanism.

### Straw dogs

[The entry contract](../AGENTS.md#straw-dogs) owns the `<straw-dog>` syntax, ticket binding,
expiry, and the duty to wrap when writing. Listing provides source locations and the written
condition and owner; the maintainer establishes whether the condition holds from evidence.
Unknown conditions remain unresolved. Mechanical removal follows that disposition and preserves
surviving agreements. Examples describing the syntax are distinct from operative statements.

A removal request identifies an entire obsolete statement; the mechanical tool does not
decide whether nested statements have also expired. Reject an outer-block removal while it
contains nested blocks. The maintainer disposes of children first and rescans before another
removal; active children and enduring agreements require preservation before the outer
statement can be removed.

In code the marking is a comment line beginning `TODO`: one naming its ticket is listed as a
straw dog with that owner, and leaves with the code rather than through the tool.

The listing tool may also guess, from the words a sentence carries or a `TODO` that names no
ticket, where a straw dog stands unwrapped. A guess is a finding for the maintainer, never a
diagnostic, and never moves the run's status; what has no named successor is a claim and is
left as written.

### Installed blocks

[The shape](../.agents/skills/mechanism/SKILL.md#rules-injection-and-retraction) owns what a
rule is and where it lives; [the format shelf](../.agents/skills/mechanism/MECHANISM-FORMAT.md)
owns the rules file's grammar. A rule's only authored home is its mechanism's rules file. It
reaches a skill as an `<installed by="<slug>">` block written by one generic installer: one
block per mechanism per target, holding every rule that mechanism sends there in its rules
file's order, each opening with its id, and nothing else, at the end of the section the anchor
line heads — after the section's own text and after every block already there, so blocks stand
in install order *(the user, 2026-09-21; until then directly after the anchor line)*. A section
runs to the next heading of the anchor's level or higher. A mechanism has one place in a target.
The entry file owns the prohibition on editing a block in place. The project's own rules file,
`local.rules.md` beside the entry file, is one more source: its block lands last in its section
and after every mechanism's in a target, and a rule in it may name the core rule it overrides,
which is rendered where the reader meets it.

The installer has a named mode or refuses. It validates every target of a file before writing
anything — target present, anchor matching exactly one line, block absent or matching — and a
refusal changes no file. Retraction removes exactly what installation added, leaving the target
byte-identical. A block that differs from its source is drift: the tool cannot tell an amended
source from an edited copy, so it refuses unless the caller says to overwrite, and then it
replaces the block whole and reports what it replaced. A mid-write failure follows
[interruption and recovery](#interruption-and-recovery).

A rules file's block is installed in every target it names, or the tree's check fails: an
absent block, a drifted block, and a block nothing owns — its owner has no rules file, or that
file does not name the file the block sits in — are each a diagnostic.
The installer writes no doc and decides nothing about a mechanism's state.

### Installing

[The install spec](spec/01-0010.0130-harness-installs-into-another-tree.md) owns the decisions;
this is the contract a recipient holds the harness mechanism to. The source is a repository at a
ref — cloned fresh on every run, read through git rather than a checkout, never a working tree —
so what a recipient receives is always what a commit holds, and the harness's own repository is
the default. The manifest is every file under the core directory at that ref plus the entry file
and the host stub, and nothing else; the project's local rules file is never in it and never
written.

What ships is transformed before it is written: the origin's own local blocks removed, every
straw-dog wrapper and every `TODO`'s ticket binding sheared with its content kept, the entry
file's announce line stamped `<repository>@<ref>, <date>`, and the result held to the same leak
rule the origin's check applies. A tree whose announce line carries the `@` is a recipient; the
line is its only revision record, and integrity is asked of the source: a check clones the
announced ref and compares file by file, line endings normalised and local blocks removed.

An install refuses a target that is not the top level of a git work tree, that already holds any
manifest path, or that is the source itself. An update refuses over a core file the recipient
edited unless told to overwrite, and then reports what it replaced; it never touches a file under
the core directory the manifest does not name, and reports it as the recipient's own; it refuses
an entry file still carrying a retired `<project-local>` block, whose content is the project's.
Every refusal changes no file. A loader link is a symlink resolving to the skills directory; a
junction, a directory or a file in its place is refused by name; a link that already resolves is
left alone; and where the platform refuses to create one, the run finishes everything else,
reports the link as pending with the exact elevated command for that tree. Nothing is
substituted for a link, and a link never decides arrival: the links are reported beside the
verdict, resolving or not.

Arrival is the check, and it takes seconds: the announced ref compared, the injector's check
clean with the local block last, the shape check clean — run as the target's own scripts. The
shipped suite is not part of it; a recipient that wants it names it in its own verification set.
Whether a host reads the link is not observable from inside a tree and is reported as
unverified. A mid-run failure follows [interruption and recovery](#interruption-and-recovery).
The project's verification set is the project's; core checks itself through this check, which a
recipient may list in its set.

## Deferred decisions

- The pacer owns session resumption and turn progression. This maintenance install does not
  define a scheduler, session retention window or automatic next cycle.
- Cross-project distribution, generalized local overrides and dependency tracking retain
  their existing owners in the shared-harness work.
