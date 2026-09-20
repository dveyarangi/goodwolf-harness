# Separation gets its ticket, and the premise answers to eight families

Session fourteen, opened 2026-09-09 and closed 2026-09-10. Woke with `/recall`, spent most of the
session on one question the user opened — what recording a project's local facts actually is —
minted the separation ticket through `/ticket`, and closed with a `/discover` pass over the whole
repository premise. Two commits, `TICKET` and `DISCOVER`. No implementation, no delivery slice
taken; the queue's candidate `.0050` is still untouched.

## Work completed

- **[01-0010.0130](../tickets/01-0010.0130-harness-installs-into-another-tree.md) is minted** — the
  distribution work the queue has carried as a deferred line since inception. Decision-bearing,
  `Ready`, its align to run **together with [01-0010.0110](../tickets/01-0010.0110-project-facets-injected.md)'s**
  on the user's direction. `/impact` recommended narrow rather than split and that was adopted: the
  loader *link* is this ticket's, the loader *surface* stays `.0120`'s, and `.0050` is recorded as
  constraining the manifest question rather than blocking the ticket. Its `/impact` is on the
  parent.
- **Six findings that cited nowhere maintained now have a home** on that ticket, on the user's
  direction: the four the frost_map probe left unowned, and two found this session.
- **[The `/discover` pass over the premise](../tickets/01-0010-dev-harness-shared-and-local.md#discover--the-premise-2026-09-10)**,
  filed verbatim on the parent. Eight families, deliberately disagreeing; its smuggling section is
  the part that costs something.

## The correction that reorganised the question

The user opened with a design: a tier-1 rule deciding core-or-local at every expansion, local
entries in one file in installed-rules format, installed into targets on redeployment — with the
stated cost that placement is lost, and the entry file's own self-declaring statement is local.

My reading was that `<project-local>` is four kinds of thing. **The user's correction was that the
autonomy switches are not one of them at all** — they are settings every project has, whose values
differ. That collapsed the taxonomy into one cut that is actually load-bearing: **who owns the
content, and what redeployment may do to it.** An installed rule is core's content in core's slot,
and overwriting it is the point. A switch value is the inverse — the project's content in core's
slot, and overwriting it is the defect. They cannot ride the same installer, because ownership runs
opposite ways.

Two consequences worth carrying into the align:

- **The stated con is smaller than it looked.** A rules file already carries `target` and `anchor`
  per rule, so placement is not lost. What is lost is *authoring in place* — writing the fact where
  you are reading it. That is an ergonomic cost, not an information one.
- **The self-declaring statement may be a facet after all.** It answers a question core has never
  asked out loud: *is this tree core's own home, or a recipient?* That answer decides whether a
  `docs/` reference is a leak or ordinary, which makes it the most load-bearing local fact here. It
  reads as unplaceable only because there is no slot for it.

## Found while tracing who reads the switches

All landed on `.0130`, none repaired — no implementation was authorized.

- **`/verify` reaches one fact three ways** in one file: two links into `docs/process.md`, then the
  prose *"The `repair` switch is in `AGENTS.md`."* `/ticket` reads the same switch set by a fourth
  route, by path into the block.
- **Four bare core→instance links**, in `/verify` (×3) and `/implement` (×1), outside any
  `<project-local>` block — `verify/SKILL.md` has no such block at all. Straight violations of
  *Core and instance* and ADR-0002, and four more links that dangle on arrival. The probe's 35 did
  not count them.
- **`docs/concerns.md` does not exist in this tree**, yet `/align` calls it *"this skill's
  artifact"* and `/edge` points into it. Core referencing a missing instance document **at home**,
  not only in a recipient — the same defect the probe found travelling, sitting here unnoticed.

## `/discover` did not get the isolation it assumes

The pass read no file, but opened its reply with this project's entry-contract line: project
instructions reach any subagent spawned here automatically. `/discover`'s method is *spawn a
separate process and tell it not to read this repository*, and in this harness that does not buy
isolation. The pass caught the other half unprompted — *"the epistemic sorting rule was supplied
with the question... I sorted my claims into bins I did not choose."*

**This is a defect in the mechanism, not in the material, and it has no owner.** Recorded with the
material and left.

## Open, with owners

- **The probe record contradicts the user's account.** It says *"nothing modified or deleted"* and
  records only the `.claude/skills` symlink as destroyed; the user's account is that frost_map's
  local entries were lost. The align rests on this evidence. On `.0130`'s open issues.
- **Whether the premise is a document problem or an agent problem.** The pass's sharpest structural
  observation: the substrate — an agent that re-reads everything each session — is named once and
  then every property is about documents. If that substrate is the determining fact, five of the
  eight families are borrowed clothes. No owner; it bears on the premise, not on a slice.
- **`/discover`'s isolation.** Above. No owner.
- **The user's grade on the mechanism shape**, pre-registered since 2026-09-07, still not given.
- **Two partial rows** in `mechanism-shape`'s doc, left after the 2026-09-09 `/maintain` pass.
- **Whether a recipient runs the shipped suite by default**, at ~70s. On `.0130`.

## Drift reported and not fixed

`/recall` reports drift; repairing it is `/maintain`'s.

- **[01-0010.0110](../tickets/01-0010.0110-project-facets-injected.md) reads `Planned (the injector
  precedes)`** — the injector landed at `01-0011.0020`. It has been unblocked and nothing noticed.
- **The queue's pacing prose still orders by the coherence chain** and names `.0050` the candidate
  on the old ordering. That separation moved ahead of it, on the user's call at session thirteen,
  lives only in that session record.
- **[.0050](../tickets/done/01-0011.0050-shape-checked.md) says "fifteen are installed as of
  2026-09-07"**; it is twenty-two.

## Housekeeping

Two commits this session, `43cafe8` and `2493b43`; **eight now unpushed**, including session
thirteen's six. `push=ask`. Verification set green throughout — 216 behavioural tests not re-run
this session, but `mechanisms.py`, `inject_rules.py`, `tickets.py --check` and `straw_dogs.py` all
clean after every edit; sixteen straw dogs, all bound. Entry contract v8 unchanged.

**Next step:** the joint `/align` of `.0130` and `.0110`, which is where both this session's
correction and the discover material are aimed. `next-cycle=ask`.
