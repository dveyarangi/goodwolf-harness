# maintain — holds documentation, implementation and records in agreement, and repairs the drift

- **instruction** `.agents/skills/maintain/SKILL.md` — the pass: scope, the four things, temporary statements, archiving, finish
- **state** installed
<project-local>
- **evidence** `docs/mechanisms/maintain.evidence.md`
- **declared by** `docs/tickets/done/01-0011.0022-shape-survives-second-mechanism.md`
</project-local>

## How it works

`/maintain` holds four things in agreement, per documentation-and-implementation pair a project
has: docs are derived work of the meta-rules and take their format; docs and their implementation
agree, both ways; live records are derived work of their declared format; every fact has one home.
Its occasion is **drift** — a governing side that moved with no landing behind it, or a sum of
clean landings that no longer agrees. Agreement over a landed slice is verification's, at
`/verify`, and this mechanism does not repeat it.

It is **installed**. A tree without it still runs its ring, unmaintained; the parts table below is
what an installer adds and an uninstaller removes, and no installer exists yet — that moment is
declared, not assumed away. It is reached from the ring in the entry file and from `/verify`
naming it. Nothing in the entry file is its part: the ring belongs to the loop, and this
mechanism sits on it.

Its record is the marks — one row per mechanism per level, moved only by the closing step of a
maintenance, from which dueness is derived. **It does not have them yet.** Until the clock
exists, the body carries an interim rule inside a temporary statement: every declared mechanism
in a pass's scope is due at every pass. That rule is loud in the enumerator and retires with the
clock's ticket.

Two rows below read `embedded`: the body carries, inside a temporary statement, a hand copy of
the ticket mechanism's rules on paired close, bound to the ticket that replaces it with an
installed block, so the enumerator lists it until then. The mechanism shape's rules on records
and re-checks reach the body as an installed block. That is the honest state of a duty that was
written in one skill's files while another skill had to act on it.

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
| P1 | the user, 2026-09-06 — a ticket closes only after its verification box is checked |
| A3, B2, D3 | drafted into the process document 2026-09-05, never separately decided |
| B3 | a maintenance pass, 2026-09-07, from `TICKET-FORMAT` stating the duty unconditionally |
| C2, C3 | the install RFC of 2026-09-06 |
| E1–E3 | `/denoise` as selected, 2026-09-05 |
| the mechanism shape's block, R1–R4 | the user, 2026-09-07, in the shape's rules file; installed here |
| the ticket mechanism's rules, P1–P4 | copied by hand until `01-0011.0025` installs them |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| declaring a scope and running a pass over it | `.agents/skills/maintain/SKILL.md` | |
| re-checking derived work when what governs it moved — a doc against the meta-rules, an implementation against its doc, records against their format | `.agents/skills/maintain/SKILL.md` | |
| holding a landed slice to its governing docs, both ways | — | elsewhere — landing-time agreement is verification, `.agents/skills/verify/SKILL.md` |
| knowing a re-check is due | — | not yet — nothing gives *since* a meaning until the marks exist, [.0060](../../../docs/tickets/01-0011.0060-mechanism-rechecked-when-governing-moves.md) |
| deciding whether a temporary statement's condition holds, and retiring the block | `.agents/skills/maintain/SKILL.md` | |
| cleaning prose and records to one home per fact | `.agents/skills/maintain/SKILL.md` | |
| closing a finished ticket with its RFC | — | embedded — the ticket mechanism's paired close, sitting in this body until its rules file installs it, `.agents/skills/maintain/SKILL.md` |
| updating the header and queue row at close | — | embedded — the ticket mechanism's record shape, same home, same repair, `.agents/skills/maintain/SKILL.md` |
| checking a mechanism's records against their declared format | `.agents/skills/maintain/SKILL.md` | |
| repairing mechanically, history included | — | elsewhere — a meta-rule, read where it lives, `.agents/skills/mechanism/SKILL.md` |
| disposing of a concern | — | not yet — the concern index has never existed, [01-0017](../../../docs/tickets/01-0017-io-graph-coherent.md) |
| checking links outside a close | — | not yet — the only link check is the mover's note over records a close rewrote, [01-0017](../../../docs/tickets/01-0017-io-graph-coherent.md) |
| cleaning inline comments in scope | — | elsewhere — verification applies the comment skill to landed work, `.agents/skills/verify/SKILL.md` |
| running the verification set the scope touched | `.agents/skills/maintain/SKILL.md` | |
| installing this mechanism into a tree, and removing it | — | not yet — no installer exists, [01-0010](../../../docs/tickets/01-0010-dev-harness-shared-and-local.md) |
| picking up a dream | — | unowned by design — the entry file says *may*, a permission and not a duty, while the dream skill is experimental |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/maintain/SKILL.md` |
| this doc | `.agents/mechanisms/maintain/maintain.md` |
| its rules file | `.agents/mechanisms/maintain/maintain.rules.md` |
| the enumerator | `.agents/scripts/temporary_statements.py` |
| its tests | `tests/test_temporary_statements.py` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the mover | `.agents/scripts/move_doc.py` | the ticket mechanism, from `01-0011.0025`; a declared gap until then |
| the mover's tests | `tests/test_paired_close.py` | same |
| the mover's tests | `tests/test_refusals.py` | same |
| the mover's tests | `tests/test_citations.py` | same |
| the mover's tests | `tests/test_command_line.py` | same |
| the mover's tests | `tests/test_failure_contract.py` | same |
| citation reader | `.agents/scripts/docs_corpus.py` | same gap; `01-0011.0025` claims it, and it is not a live question while nothing installs or extracts |
| test harness | `tests/harness.py` | same |
| the shape check | `.agents/scripts/mechanisms.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The pass's report** — read by the person who asked for the pass, and by `/conclude` when
  the session is recorded.
- **Repaired files** — read by whoever reads them next; the report names each repair and the
  rule it restored.
- **Moved records** — read through their repaired citations; the mover reports what it
  rewrote and what it could not.
- **A retired temporary statement's replacement sentence** — read where the block was.
- **The rules file** — one rule, M1, targeting `/mechanism`'s *Incept*, read by the installer
  alone and installed there as this mechanism's block.

Nothing else. No record until the marks; no index.

## Not yet at the shape

**The marks.** A maintenance mechanism is record-bearing by design, and this one has no record.
Dueness is inferred, which the body forbids in the same breath as it permits it, inside a
temporary statement.

**Two `embedded` rows.** The ticket mechanism's rules are instructed from the wrong home, inside
a temporary statement the enumerator lists, and the body says so.

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
[01-0011.0022](../../../docs/tickets/done/01-0011.0022-shape-survives-second-mechanism.md)'s align.

**The user** grades the shape amendments this declaration forced — installed text replacing
injected pointers, a sentence about another mechanism being that mechanism's, and the record
obligation moving from *none by property* to *not yet*: did the shape change because
`/maintain` did not fit it, or was this declaration bent to fit the shape? A declaration
hand-fixed until the check went quiet reads identically to success.

**The session that declares the ticket mechanism**, at
[.0025](../../../docs/tickets/01-0011.0025-archive-duty-reaches-maintain.md), grades this
declaration as the first to lean on it: it takes the mover and the citation reader as its own,
installs the paired-close block into the body, and retires the two `embedded` rows. Did those
land against this doc as written, or did the doc have to be rewritten to receive them?
