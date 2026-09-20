# maintain — holds documentation, implementation and records in agreement, and repairs the drift

- **instruction** `.agents/skills/maintain/SKILL.md` — the pass: scope, the four things, straw dogs, archiving, finish
- **state** installed
<project-local>
- **evidence** `docs/mechanisms/maintain.evidence.md`
</project-local>

## How it works

`/maintain` holds four things in agreement, per documentation-and-implementation pair a project
has: docs are derived work of the meta-rules and take their format; docs and their implementation
agree, both ways; live records are derived work of their declared format; every fact has one home.
Its occasion is **drift** — a governing side that moved with no landing behind it, or a sum of
clean landings that no longer agrees. Agreement over a landed slice is verification's, at
`/verify`, and this mechanism does not repeat it.

It is **installed**. A tree without it still runs its ring, unmaintained; the parts table below is
what an installer adds and an uninstaller removes. It is reached from the ring in the entry file
and from `/verify` naming it. Nothing in the entry file is its part: the ring belongs to the loop,
and this mechanism sits on it.

<straw-dog until="01-0010 is done" ticket="docs/tickets/01-0010-dev-harness-shared-and-local.md">
No installer exists yet; that moment is declared below, not assumed away.
</straw-dog>

Its record is the marks — one row per mechanism per level, moved only by the closing step of a
maintenance, from which dueness is derived.

<straw-dog until="01-0011.0060 is done" ticket="docs/tickets/01-0011.0060-mechanism-rechecked-when-governing-moves.md">
**It does not have them yet.** Until the clock exists, the body carries an interim rule inside a
straw dog: every declared mechanism in a pass's scope is due at every pass. That rule is loud in
the listing and retires with the clock's ticket.
</straw-dog>

The ticket mechanism's rules on paired close and on its records, and the mechanism shape's rules
on records and re-checks, reach the body as installed blocks.

<straw-dog until="01-0017 is done" ticket="docs/tickets/01-0017-io-graph-coherent.md">
One rule sits in the body by hand inside a straw dog: a spec's agreements before archiving it,
which is `/spec`'s and waits for `/spec` to be declared.
</straw-dog>

The body names no other skill except `/align`. What is not this mechanism's is stated as what it
does not do — a landed slice is verified, not maintained — never as who does it instead; this
table is where the other party is named.

**Who decided each rule.** The body carries rules by ID and no attribution, because attribution
serves the maintainer at amend time, not the agent at execution; this doc carries it. A rule with
a name and date below is that person's to amend, through `/align`; the rest came with the selected
skills or with a pass under the repair policy, and a maintainer may amend them under
repair-and-report, recording the cause in the evidence.

| rule | decided by |
|---|---|
| A1, A2, A4 | the user, 2026-09-07 |
| B1, D4 | the user, 2026-09-06 |
| C1 | the user, 2026-09-06 — eligibility is the maintainer's, never the script's |
| A3, B2, D3 | drafted into the process document 2026-09-05, never separately decided |
| B3 | a maintenance pass, 2026-09-07, from `TICKET-FORMAT` stating the duty unconditionally |
| C2, C3 | the install RFC of 2026-09-06 |
| E1–E3 | `/denoise` as selected, 2026-09-05 |
| the mechanism shape's block, R1–R4 | the user, 2026-09-07, in the shape's rules file; installed here |
| the ticket mechanism's block, P1, P2, P3, P5 | in the ticket mechanism's rules file, where each rule carries its own authority; installed here from `01-0011.0025` |
| P4 | drafted into the process document 2026-09-05 as a spec rule; held here by hand for `/spec`, undeclared |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| declaring a scope and running a pass over it | `.agents/skills/maintain/SKILL.md` | |
| re-checking derived work when what governs it moved — a doc against the meta-rules, an implementation against its doc, records against their format | `.agents/skills/maintain/SKILL.md` | |
| holding a landed slice to its governing docs, both ways | — | elsewhere — landing-time agreement is verification, `.agents/skills/verify/SKILL.md` |
| knowing a re-check is due | — | <straw-dog until="the marks exist and give *since* a meaning" ticket="docs/tickets/01-0011.0060-mechanism-rechecked-when-governing-moves.md">not yet</straw-dog> |
| deciding whether a straw dog's condition holds, and retiring the block | `.agents/skills/maintain/SKILL.md` | |
| guessing where a straw dog nobody wrapped stands, and judging each guess | `.agents/scripts/straw_dogs.py` | |
| cleaning prose and records to one home per fact | `.agents/skills/maintain/SKILL.md` | |
| closing a finished ticket with its RFC | `.agents/skills/maintain/SKILL.md` | |
| updating the header at close | `.agents/skills/maintain/SKILL.md` | |
| checking a mechanism's records against their declared format, the ticket records among them | `.agents/skills/maintain/SKILL.md` | |
| repairing mechanically, history included | — | elsewhere — a meta-rule, read where it lives, `.agents/skills/mechanism/SKILL.md` |
| disposing of a concern | — | <straw-dog until="a skill instructs disposing of a concern" ticket="docs/tickets/01-0017-io-graph-coherent.md">not yet</straw-dog> |
| checking links outside a close | — | <straw-dog until="a link check runs outside a close, not only the mover's note over records a close rewrote" ticket="docs/tickets/01-0017-io-graph-coherent.md">not yet</straw-dog> |
| cleaning inline comments in scope | — | elsewhere — verification applies the comment skill to landed work, `.agents/skills/verify/SKILL.md` |
| running the verification set the scope touched | `.agents/skills/maintain/SKILL.md` | |
| installing this mechanism into a tree, and removing it | — | <straw-dog until="an installer exists" ticket="docs/tickets/01-0010-dev-harness-shared-and-local.md">not yet</straw-dog> |
| picking up a dream | — | unowned by design — the entry file says *may*, a permission and not a duty, while the dream skill is experimental |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/maintain/SKILL.md` |
| this doc | `.agents/mechanisms/maintain/maintain.md` |
| its rules file | `.agents/mechanisms/maintain/maintain.rules.md` |
| the listing script | `.agents/scripts/straw_dogs.py` |
| its tests | `.agents/scripts/test/test_straw_dogs.py` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the mover | `.agents/scripts/move_doc.py` | `ticket` |
| the mover's tests | `.agents/scripts/test/test_paired_close.py` | `ticket` |
| the mover's tests | `.agents/scripts/test/test_refusals.py` | `ticket` |
| the mover's tests | `.agents/scripts/test/test_citations.py` | `ticket` |
| the mover's tests | `.agents/scripts/test/test_command_line.py` | `ticket` |
| the mover's tests | `.agents/scripts/test/test_failure_contract.py` | `ticket` |
| the ticket maintainer | `.agents/scripts/tickets.py` | `ticket` |
| citation reader | `.agents/scripts/docs_corpus.py` | `mechanism-shape`, the one that cannot leave |
| test harness | `.agents/scripts/test/harness.py` | `mechanism-shape` |
| the shape check | `.agents/scripts/mechanisms.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The pass's report** — read by the person who asked for the pass, and by `/conclude` when
  the session is recorded.
- **Repaired files** — read by whoever reads them next; the report names each repair and the
  rule it restored.
- **Moved records** — read through their repaired citations; the mover reports what it
  rewrote and what it could not.
- **A retired straw dog's replacement sentence** — read where the block was.
- **The listing script's guesses** — read by the maintainer at T3 over a declared scope, and by
  `/verify` over the files a slice touched; never by a check, since a guess is judged and never
  fails a run.
- **The rules file** — one rule, M1, targeting `/mechanism`'s *Incept*, read by the installer
  alone and installed there as this mechanism's block.

Nothing else; no index.

<straw-dog until="01-0011.0060 is done" ticket="docs/tickets/01-0011.0060-mechanism-rechecked-when-governing-moves.md">
No record until the marks.
</straw-dog>

## Not yet at the shape

**The marks.** A maintenance mechanism is record-bearing by design, and this one has no record.
Dueness is inferred, which the body forbids in the same breath as it permits it, inside a straw
dog.

<straw-dog until="01-0017 is done" ticket="docs/tickets/01-0017-io-graph-coherent.md">
**One rule held by hand.** P4 is `/spec`'s, and `/spec` is undeclared, so the body carries it
inside a straw dog bound to the ticket that declares the rest of the corpus.
</straw-dog>

**Four `not yet` rows**, each naming a ticket that exists.

**This mechanism has never been run against a mechanism other than the one that wrote the
shape.** The first declaration named `/maintain` as instructing re-checks while the body carried
one sentence; this declaration is where the body first honours it.

## What retires this

A tree in which every one of the four agreements is held by a script in the verification set,
leaving a pass no judgment to apply. Until then this is the judgment half and the scripts are its
parts.

## What would show it working, graded by someone who did not build it

Two graders, two questions, pre-registered at
<straw-dog until="01-0010.0140 is done" ticket="docs/tickets/01-0010.0140-core-stands-alone.md">[01-0011.0022](../../../docs/tickets/done/01-0011.0022-shape-survives-second-mechanism.md)</straw-dog>'s align.

**The user** grades the shape amendments this declaration forced — installed text replacing
injected pointers, a sentence about another mechanism being that mechanism's, and the record
obligation moving from *none by property* to *not yet*: did the shape change because
`/maintain` did not fit it, or was this declaration bent to fit the shape? A declaration
hand-fixed until the check went quiet reads identically to success.

**The session that declares the ticket mechanism**, at
<straw-dog until="01-0010.0140 is done" ticket="docs/tickets/01-0010.0140-core-stands-alone.md">[.0025](../../../docs/tickets/done/01-0011.0025-archive-duty-reaches-maintain.md)</straw-dog>, grades this
declaration as the first to lean on it: it takes the mover and the citation reader as its own,
installs the paired-close block into the body, and retires the two `embedded` rows. Did those
land against this doc as written, or did the doc have to be rewritten to receive them? **Graded
2026-09-09**; the answer is in <straw-dog until="01-0010.0140 is done" ticket="docs/tickets/01-0010.0140-core-stands-alone.md">[the evidence](../../../docs/mechanisms/maintain.evidence.md)</straw-dog>.
