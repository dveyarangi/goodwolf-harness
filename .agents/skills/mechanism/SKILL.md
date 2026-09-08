---
name: mechanism
description: >-
  Use before building or amending a mechanism — a part of how the work is done
  here: a skill, a check, a record, the loop itself. Owns what counts as one,
  what it is made of, where each part lives, and how one is incepted, declared,
  checked and retired. Not for what the project produces.
---

# Build and amend mechanisms

The only home of the shape. A rule carrying a name and date is that person's to amend.

## Is it a mechanism

A mechanism is part of **how the work gets done** — the development method and its
machinery. What the project produces is not one, however much depends on it.

Test: does other work rely on this as a source of instruction or behavior *about how
to work*? Then it is a mechanism and owes a declaration.

- A system, never a file. One spans skills, scripts, records, and rules injected into
  skills it did not write.
- **One mechanism, one instruction file — a skill** *(the user, 2026-09-06)*. Rules it
  needs elsewhere are installed as text from its rules file, never second instruction
  files, and no body restates one *(the user, 2026-09-07)*.
- Writing an entry into a record is not mechanism work. It belongs to the skill that
  owns the entry.

A skill belonging to no mechanism goes in the allowlist, with its reason.

## Three homes, and the chain

| home | holds | reaches a session |
|---|---|---|
| `AGENTS.md` | meta-rules and general rules | at start, every session |
| `.agents/skills/<name>/` | the act, and every rule read *in the work it governs* | when the skill is invoked |
| `.agents/mechanisms/<slug>/` | why the instruction is what it is: parts, moments, and the mechanism's rules in their single home | when installing, amending or debugging |

The cut is **when is this read**. There is no fourth home.

> The doc is the instruction's *why*. The evidence is the doc's *why*.
> *(the user, 2026-09-06)*

- Doc and instruction file are never the same file.
- One evidence per mechanism, belonging to its doc. It lives **outside `.agents/`**, in
  the project's own document tree, filename carrying the slug *(the user,
  2026-09-06)* — it cites records that cannot travel — and the doc names its path from
  inside a `<project-local>` block.
- A skill's `EVIDENCE.md` predating its declaration is an unsorted mixture: doc
  material to the doc, the doc's own why to the evidence.

Working parts stay where the harness needs them — skills, scripts, tests. Directory,
doc sections and what a script parses are
[MECHANISM-FORMAT.md](./MECHANISM-FORMAT.md)'s; restate none of it here.

## Moments

A moment is an occasion at which a person acts on the mechanism. Every one carries an
instruction or a stated kind of absence, and either way a clause saying why.

| kind | means | carries |
|---|---|---|
| `elsewhere` | instructed, by another mechanism | the instruction file that does it |
| `embedded` | instructed, from the wrong home | where the instruction sits |
| `unowned by design` | no rule warranted | its reason, nothing else |
| `not yet` | a genuine gap | a ticket that exists |

There is no *none needed*: if nobody acts, it is not a moment. A `not yet` never names
the mechanism's own migration ticket. The verdict is per moment, never per mechanism.

## Rules, injection and retraction

A rule lives in one file — `<slug>.rules.md`, in the mechanism's own directory. Nothing
reads it at session time: a generic core installer, never a per-mechanism one, writes
its rules into the targets as delimited and visibly owned blocks, and that is the only
form in which they reach anyone. A copy in a target is **installed, never authored**.

- Removable as written: retraction leaves the target byte-identical.
- **No default mode.** A bare invocation refuses.
- **Refuse rather than guess** — missing target, missing anchor, block present and differing.
  A hand-edited block is drift to report, not a second opinion.
- A rules file's block is installed in every target it names, or the check fails.

The installer is `inject_rules.py`: `<slug> --install`, with `--overwrite` when the source has
moved; `<slug> --retract`; `--check` over the tree, in the verification set. Grammar and block
form: [MECHANISM-FORMAT.md](./MECHANISM-FORMAT.md#the-rules-file).

A mechanism that injects nothing has no rules file.

**A sentence about another mechanism is that mechanism's** *(the user, 2026-09-07)*. What
shapes how mechanisms are built around it — what `/maintain` must be handed at inception, for
one — is a rule in its rules file, installed here, never authored here. Its core function
reaches a session through its own description, strengthened at tier 1 where warranted; a
principle that resonates through the whole harness may land in `AGENTS.md` — that mechanism's
decision, rare, and investigated first.

## Mechanical by construction

A mechanism is designed from inception for mechanical derivation, checking and repair: its
identity, governing sources, dependencies and record contracts are explicit enough for a script
to enumerate what a change affects. Anything that can be maintained mechanically is; a missing
script is written as part of the repair; archived records are not exempt *(the user,
2026-09-05)*.

## What it produces

**Everything a mechanism produces is read by someone, or the doc says why nobody does**
*(the user, 2026-09-07)*. Name each artifact and its reader: a person at a stated moment, another
mechanism, a script, a check. An output with no reader is either dead weight or a missing reader,
and which of the two it is only becomes answerable once it is written down.

This covers what the mechanism emits as well as what it ships — a report nobody opens, a record
nothing indexes, a file dropped where nothing looks.

## Records

<installed by="mechanism-shape">
**R1** Check a record-bearing mechanism's records with its maintainer script — format never
content, live rows only. Where the script is missing, write it: that is the maintenance.

**R4** Render an index on request; never commit one beside its records.
</installed>

A mechanism with records declares what a record is — its fields, what a row means, its
tier, what removes a finished entry — inside the record's own file *(the user, 2026-09-07)*.

## Incept

<installed by="maintain">
**M1** Name what `/maintain` must do for this mechanism — a maintainer script to run, records to
re-check when its surfaces move — as rules in its rules file targeting `/maintain`. Nothing is
written into `/maintain` by hand.
</installed>

1. **`/align` first**, on what the mechanism is in plain terms: its moments, its
   authority, its record shape, its index, the tier of each part, what retires it.
2. Write the doc to [MECHANISM-FORMAT.md](./MECHANISM-FORMAT.md), naming the parts it
   owns and the parts it relies on with their owners; and its rules file, installed before
   the doc is checked.
3. **Write the check before the thing it checks**, watching every diagnostic fail in
   both polarities.
4. **Run it over what already exists** and record the count of prior violations — or
   state that there was no prior corpus, rather than a manufactured zero.
5. Name what retires it.
6. **Name what would show it working, graded by someone who did not build it.**
   Pre-register it so a later session can answer without asking what was meant.

Absence is not clearance: a clean run means nothing was caught, never that the tree
obeys.

## Amend and retire

Editing a skill that is an instruction file is amending its mechanism — run the steps
still live, aligning again when the shape itself moves. Amend a rule in its rules file, then
install it with overwrite; the block in a target is never the place. A mechanism is re-checked
when what governs it has moved; which skill does that is its doc's row, not this body's
sentence.

Retiring runs `--retract` first, then removes the mechanism's parts and its directory, its
own trigger among them. An always-on mechanism cannot be retired.

## Siblings

- [`/skill-up`](../skill-up/SKILL.md) writes a skill's text; this governs the system it
  belongs to. Both apply when a skill is an instruction file.
- [`/impact`](../impact/SKILL.md) traces a change's consequences; this asks whether a
  mechanism is sound at both ends.
- [`/maintain`](../maintain/SKILL.md) applies the shape's rules and owns none of them; what it
  asks of an inceptor is its own rule, installed above.
- [`/align`](../align/SKILL.md) is called by incept, before anything is built.
