# A mechanism is one skill, and Life had most of it written down already

**Date:** 2026-09-07 (opened 2026-09-06)
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and the owning tickets. This record is a snapshot of the seventh session, in Claude Code. `/conclude` is not installed; this was written by hand at the user's request.

## Work completed

Ran `/align` on [01-0011.0010](../tickets/01-0011.0010-mechanism-declared.md). It **amended the spec accepted the day before** rather than applying it. The turn that did it was the user's instruction to go read Life properly: its `/mechanism` skill, `mechanism-shape` doc and register, `evidence-sidecars`, `maintenance` with its rules file, and `/mechanism`'s own `EVIDENCE.md`. Three things this spec had reasoned to independently came back wrong.

Ran `/ticket` on the re-slice, with `/impact` returning **narrow** and changing two things before presentation. Five children became seven; two mechanisms that had no slice got one.

Four skills arrived mid-session — `/advise`, `/celebrate`, `/commit`, `/skill-up` — brought in by the user as-is, ahead of [01-0010.0100](../tickets/01-0010.0100-remaining-named-corpus.md)'s align. `/dream` followed. Registered rather than absorbed: that ticket is now `Partial` and lists what each still owes.

Five commits, `abf7e77` through this session's last.

## Settled decisions and their owners

- **A mechanism has exactly one instruction file.** Rules it needs in skills it does not own are injected pointers, never second instruction files → [the spec](../spec/01-0011-mechanism-shape.md). `/maintain` is therefore not a part of anything it maintains; it is the mechanism *for* maintaining mechanisms and acts from outside.
- **The shape lives in `/mechanism`'s body, not in a doc.** The cut is *when is this read*, and the shape is read while incepting or amending one. This inverts what [01-0011.0010](../tickets/01-0011.0010-mechanism-declared.md) was minted saying.
- **Doc is the instruction's *why*; evidence is the doc's *why*** — the user's, and it dissolved a question Life left open for its own operator rather than answering it. The third shape is called **evidence**, not *sidecar*: *sidecar* names where a file sits and never what is in it. **Provenance stays inline**, because attribution at the moment of reading is what makes a rule challengeable.
- **The three properties are not three co-equal states.** Delivery becomes a **moments table**, single authorship becomes a structural injection rule, indexing belongs to the record contract. Life tried the whole-mechanism verdict and abandoned it for a stated reason → [the spec](../spec/01-0011-mechanism-shape.md).
- **Records have a declared shape and it is enforced**, not optional for records that happen to look unstructured → the user, correcting a draft that had made it HITL per mechanism.
- **First `/mechanism`, then `/maintain`, then `/ticket`.** *Paired close* is a behavior of `/ticket`, not a mechanism — it is not a skill, and one instruction file per mechanism forbids it.
- **The register is `.agents/README.md`**, this project's rows in a `<project-local>` block, not a new file under `docs/` → the user.
- **Core and instance**, now in [AGENTS.md](../../AGENTS.md): `docs/` is substituted whole in a harness instance, so nothing under `.agents/` may reference a file in it — except from a `<project-local>` or `<temporary>` block. Placement is not the rule; this repository's own architecture belongs in `docs/`.
- **Only global practice belongs in a core skill**, and a `<project-local>` block should avoid being an override → the user, correcting a repair of mine that had swapped one override for another.
- **Commit prefixes are the loop step that produced the work**, `FIX` and `EQUIP` outside the ring. Defined in `/commit`'s body because it is global practice.

## Open, with owners

- Whether a `<project-local>` block may ever override rather than answer, and how a new project's facts reach the skills that need them → [01-0010.0110](../tickets/01-0010.0110-project-facets-injected.md), which takes the *local overrides* issue the queue had carried as deferred since inception.
- Where repair-and-report lives. Re-counted this session: **three skills touch it, two restate it** — not the five I claimed. The evidence now points at `/verify` → [01-0016](../tickets/01-0016-responsibility-coherent.md).
- Whether the queue's rendered table is committed → [01-0011.0040](../tickets/01-0011.0040-queue-derived-index.md), unchanged.
- Four references from core into this project's own documents, which the new rule makes violations → their owning tickets.
- `/advise`, `/celebrate`, `/commit`, `/skill-up`: none used once here, `/commit` still carries its own absolute permission rule, `/skill-up` documents neither `<temporary>` nor `<project-local>`, `/edge` has not arrived → [01-0010.0100](../tickets/01-0010.0100-remaining-named-corpus.md).

## Session through the advise questions

**Great:** the user sending me back to Life in detail. Everything load-bearing this session turned on what came back — the skill/doc inversion, the moments table replacing a triple I had defended twice, and the measured 41%-wrong queue index that makes [01-0011.0040](../tickets/01-0011.0040-queue-derived-index.md)'s case far better than our two paraphrased rows did. **Good enough:** `/impact` on my own re-slice draft, which caught that declaring `/maintain` exercises neither injection nor the record rule, and forced the slice to say so instead of claiming a test it does not run. **Questionable:** I proposed *owned when exactly one mechanism relies on it* as an ownership rule and had to withdraw it two turns later — Life had already rejected exactly that, and the constraint binds scripts rather than docs. I had read the file that says so. **Missing:** I asked eight questions before writing anything. Several were answerable from the tree, and two — the sidecar and the register — were dissolved by a rule the user stated in one line each time. **Redundant:** three of my recommendations were reversals of Life decisions I had just quoted approvingly in the same message. **Out of balance:** I wrote every file change through Python scripts. The user could not see a single diff, two defects came out of it (CRLF into three LF files, six apostrophes mangled to `'''`), and both would have been visible in an Edit. That is now a standing rule. **Hidden edges:** the `<project-local>` block is what made another project's gate set look legitimate — a designated place for local facts gives a reader no way to tell an answer from an import. **Easier:** a session where the mechanism directory exists, so a rule has somewhere to go and the check can say whether it got there. **Next:** `/plan` for [01-0011.0010](../tickets/01-0011.0010-mechanism-declared.md)'s RFC, under `next-cycle=ask`.

## Housekeeping

`AGENTS.md` gained *Core and instance* — written wrong first (as a placement rule), corrected by the user the same turn to a dependency rule. The glossary gained **Moment**, **Doc**, **Evidence**, **Provenance**, **Authority** and **Tier**, and **Mechanism** and **Skill** were rewritten to say *exactly one instruction file*. `/commit`'s `<project-local>` block was repaired once and then deleted, which was the correct repair. The re-slice renumbered nothing: `.0022` and `.0025` split the gap between `.0020` and `.0030` per `TICKET-FORMAT`. Verification set unchanged at 72 tests, green at every commit.
