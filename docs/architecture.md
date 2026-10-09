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

This contract does not promise atomic multi-file writes or persisted transaction recovery.
<straw-dog question="q-0032">
Nor does it promise safe simultaneous writers: two sessions in one tree may write the same file.
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
The sessions file is written only by the script, each session replacing its own line and no other,
so one session's write never refuses another's; a rename is the one write that touches every
line, and only the ids in it. A wholly closed subtree moves to `done/` with the mover in the
`close` call that finishes it; the maintainer's move is the sweep for what a closure left behind. A host's hook
delivers the window and registers the session under the host's own session id, and never fails
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
so what a recipient receives is always what a commit holds. Which repository that is, a tree says
once, in its harness skill's `Repository:` line — the only authored home of it, read as the
default when a run names no source, so a fork edits one line and everything it installs names the
fork. The manifest is core at that ref and nothing of the project's: the project's local rules
file is never in it and never written. Two things outside the manifest are written, each only when
absent, both read by a fresh tree's first session before anything has been written into it. The
delivery status: its words are the ticket mechanism's, declared with the record's shape and
carried in the shipment; the install places them and composes nothing. And a store's roots, into a
store holding no entry: their words are the questions mechanism's shelf, and its script writes
them, the install only calling it. A tree that already has either keeps it untouched, overwrite
included — from its first line each is the instance's. A third kind is merged rather than
written: each host's shared, committed hook file, never a local settings file, receives core's
hook entries beside the project's own *(the user, 2026-10-09)*. The entries' words are the
questions mechanism's shelf, shipped as core; an update replaces core's entries and removes one
that left core, and a check compares core's entries alone, so a project's own hook is never drift.
A host file that is not valid JSON is refused, not rewritten.

What ships is transformed before it is written: the origin's own local blocks removed, every
straw-dog wrapper and every `TODO`'s question binding sheared with its content kept, the entry
file's announce line stamped `<repository>@<ref>, <date>`, the harness skill's repository line
stamped with the source the run actually read, and the result held to the same leak rule the
origin's check applies. A tree whose announce line carries the `@` is a recipient; the line is
its only revision record, and integrity is asked of the source: a check clones the announced ref
and compares file by file, line endings normalised, local blocks and the blocks of the
recipient's own mechanisms removed and the repository line set aside — it is the recipient's own
fact living in a core file, as the announce line is, so a run from another source reads no edit
in core.

A target is a Git repository, because every script of core reads a tree through Git's listing —
tracked and untracked-but-unignored files, in Git's exact case — and the top level of its work
tree is where one installation's tree ends. An install into an empty folder inside no repository
runs `git init` there first and reports it: the root is not in question, and the person asked for
an install *(the user, 2026-10-07)*. Anything else that is not the top level of a work tree is
refused with the step — `git init` for a folder with files of its own, since where the root goes
is then the person's decision; the parent for a subfolder of a repository. An install also
refuses a target that already holds any manifest path, or that is the source itself. An update refuses over a core file the recipient
edited unless told to overwrite, and then reports what it replaced; it never touches a file under
the core directory the manifest does not name, and reports it as the recipient's own; it refuses
an entry file still carrying a retired `<project-local>` block, whose content is the project's.
Every refusal changes no file. A loader link is a symlink resolving to the skills directory; a
junction, a directory or a file in its place is refused by name; a link that already resolves is
left alone; and where the platform refuses to create one, the run finishes everything else,
reports the link as pending with the exact elevated command for that tree. Nothing is
substituted for a link, and a link never decides arrival: the links are reported beside the
verdict, resolving or not. The links are made in each clone and never committed, so a fresh clone
of a recipient gets them from `--links`, the link step run alone from the clone's own copy, with
no source; whatever plans a link names it in the clone's exclude file, which Git locates. The same
step records the interpreter that ran it in the clone's Git directory, which no commit carries:
every core hook runs through a wrapper that reads it, so a hook needs no `uv` and no `python` on
the path, and a clone without the record is told which step makes it *(the user, 2026-10-09)*. A
target Git refuses for dubious ownership is refused with that cause and Git's own command.

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
<straw-dog question="q-0018.0020.0002.0002">
Nothing does this yet: core is shared from the working tree and an update crosses an edge change
in silence, leaving what a recipient must amend to whoever reads the manifest diff.
</straw-dog>

Arrival is the check, and it takes seconds: the announced ref compared, the injector's check
clean with the local block last, the shape check clean — run as the target's own scripts. The
shipped suite is not part of it; a recipient that wants it names it in its own verification set.
Whether a host reads the link is not observable from inside a tree and is reported as
unverified. A mid-run failure follows [interruption and recovery](#interruption-and-recovery).
The project's verification set is the project's. A copy drifting from its ref is maintenance's to
find, never verification's *(the user, 2026-10-09)*.

## Deferred decisions

- The pacer owns session resumption and turn progression. This maintenance install does not
  define a scheduler, session retention window or automatic next cycle.
- Cross-project distribution, generalized local overrides and dependency tracking retain
  their existing owners in the shared-harness work.
