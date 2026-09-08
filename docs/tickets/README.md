# Delivery status

**Last updated:** 2026-09-07

**Completed step:** `/maintain` on [01-0011.0022](done/01-0011.0022-shape-survives-second-mechanism.md), 2026-09-07 — the paired close of `.0022` and [`.0010`](done/01-0011.0010-mechanism-declared.md) together, four records in one invocation. What earlier passes decided is on the tickets that own it and in the session records under `docs/sessions/`; this paragraph restated them until 2026-09-07 and no longer does. The spec's ordering after the mechanism slices is unchanged: the four rule refactors, then [01-0020](01-0020-pacer.md), which wants the Tier 1 placement rule that [01-0018](01-0018-reachability-coherent.md) settles; [01-0010.0080](01-0010.0080-impact-work-shape.md) stays Ready beside them. The verification set is 115 behavioral tests over the maintenance scripts, plus `mechanisms.py --check` over the declared mechanisms; operative `<temporary>` blocks are what `temporary_statements.py docs AGENTS.md .agents` reports, six on 2026-09-07, all bound, no condition met.

**2026-09-07, the user** installed `/advise`, `/celebrate`, `/commit` and `/skill-up` directly, ahead of [01-0010.0100](01-0010.0100-remaining-named-corpus.md)'s align, because they are useful as they stand. That ticket is now `Partial` and records what remains: none of the four has been used once here, `/commit` still carries its own absolute permission rule instead of reading the entry file's switches, `/skill-up` documents neither `<temporary>` nor `<project-local>`, and `/edge` has not arrived. `/commit`'s `<project-local>` block landed carrying another project's gate set — `ruff`, `pyright`, `pytest`, and a `docs/cicd.md` this project does not have. The first repair substituted this project's commands into the same block; **the user corrected it the same day** — only global practice belongs in a core skill, and a local block should avoid being an override — so the block was deleted and the body now says to read a project's commands from where the project states them. The commit-prefix conflict is settled: the loop step wins, defined in `/commit`'s body, with `FIX` and `EQUIP` outside the ring — `EQUIP` because every other prefix is a verb. `/dream` arrived later the same day from the parent's own backlog rather than from `01-0010.0100`'s five; `/conclude` arrived at the end of 2026-09-07's session, too late to write that session's record; `/recall` has not, so wake is still by hand. How a project's local facts arrive at all is a new ticket, [01-0010.0110](01-0010.0110-project-facets-injected.md), which takes the deferred *local overrides* issue and aligns it into a spec.

**2026-09-07, `/plan` on [01-0011.0010](done/01-0011.0010-mechanism-declared.md).** Its RFC is
[written and validated once](../rfc/done/01-0011.0010-mechanism-declared.md): `/mechanism` plus a
`MECHANISM-FORMAT` shelf holding the grammar a script parses, a doc declaring `/mechanism` through
two machine-read tables, evidence under `docs/mechanisms/`, `.agents/README.md` re-partitioned into
the register, and `mechanisms.py` with its tests — the check written *before* the declaration it
checks. `/impact` returned **proceed**, and two of its findings changed the plan: the register is a
record, so this slice owes the record contract it would otherwise defer; and `.agents/README.md`
was already violating *Core and instance* with a dozen citations into `docs/`, which the
re-partition repairs rather than adds to. The pass also took an `/align` on `docs/process.md`:
line 68's definitions go to the glossary that already holds them, line 72 is obsolete once
`/mechanism` lands, and line 70 survives bound by `<temporary>` to
[.0022](done/01-0011.0022-shape-survives-second-mechanism.md) — so the document's shedding is
enumerated by `temporary_statements.py` rather than remembered. *Current constraint* goes with
them, contradicted by `AGENTS.md`'s own switches. Measured on the way: **every** section of
`docs/process.md` has an owner elsewhere; the two residues are the verification facet
([01-0010.0110](01-0010.0110-project-facets-injected.md)) and sequencing
([01-0020](01-0020-pacer.md)). It is not becoming an architecture document. That ticket also gained
**dream language** as a bootstrap facet, on the user's instruction — the first facet that is an
expression choice rather than a command, which is a question about the facet set's boundary and
its align now owns. Implemented 2026-09-07 across the RFC's five stages; the test count moved with
it, from 72 to 110.

**Second planning pass, same day, after reading Life directly** rather than through the spec's
account of it — `D:\Dev\AI\life`, its meta-rules, `mechanism-shape`, `skills` and `/mechanism`.
Four corrections, and the user's question drove the largest: *what will read the register — isn't
the script simply deriving it?* **It is.** Life's register is a migration ledger for mechanisms
with no directory to walk, and Life records both the writer it declined and the condition that
reverses the decline — half the rows having folders — which this tree meets at 100% on day one.
So **no file holds the register**; `.agents/mechanisms/*/` is the enumeration and
`mechanisms.py --index` renders it. That supersedes *the register is `.agents/README.md`* on the
spec, and empties the `<project-local>` block that decision implied: what is left in that file
travels, and its install narrative was a copy of this queue. `AGENTS.md`'s `Installed:` line went
with it on the user's decision — the host lists the skills every session. The other three
corrections: Life's own `/mechanism` allows **several** instruction files, so our one-file rule is
this project's tightening and not Life's practice restated; Life keeps `skills` as a **separate**
mechanism with `/skill-up` as its instruction file, confirming `/skill-up` is a sibling; and the
doc's shape is Life's — three-column moments where every row states *why*, and a parts table
titled *Install adds, uninstall removes*, which is also the definition of a **Part**: if
uninstalling would not remove it, it is relied-on, not owned. Four rules arrived that this tree
did not have — *name what will grade it, and it is not you*; *a check never watched failing is not
a check*; *run it over what already exists*; *absence is not clearance*. Announcements were **not**
taken: this tree has no hooks and no `settings.json`, so nothing can speak at wake. The
consequence is that nothing ran the check, which stage 5 fixes by putting it in the verification
set.

**Minted 2026-09-07 from that gap:** [01-0010.0120](01-0010.0120-host-delivery-surfaces.md), which
establishes what Claude Code, Codex and Cursor each place in front of an agent **without being
asked** — hooks and their analogues — the shared subset, and the substitutes where there is none.
`/impact` returned **proceed, narrowed** and found the connection this pass had missed:
[.0030](01-0011.0030-archive-backlog-listed.md)'s ratchet is *loud when it rises* and **nothing in
this tree can be loud**, so a planned slice rests on an unexamined assumption;
[01-0018](01-0018-reachability-coherent.md)'s *where a rule cannot reach an occasion, name the gap*
assumes the same answer; and the glossary's **Tier 1** entry has ended with *"intended Tier 1
placement and observed delivery are distinct facts"* since inception, with no owner. Both
narrowings applied — capability before portability, and unobservability carried as a criterion
rather than a footnote — with the first one **corrected by the user**: what the ticket delivers
follows from the matrix and is not fixed ahead of it. Announcements are the evidence case, not the
thing being built.

**Fifth pass, and a decision it turned into** *(the user, 2026-09-07)*: **the glossary splits.**
`.agents/glossary.md` takes the method's vocabulary and travels with core; `docs/glossary.md`
keeps this project's own domain, which a recipient owns outright. The pass found that core skills
are written in a vocabulary living in the instance half — a recipient replaces `docs/` whole — and
that **the corpus already assumed the split**: `/align`, `/tdd`, `/implement` and
`GLOSSARY-FORMAT` all mean the *domain* glossary, while only `/maintain` and `AGENTS.md` meant the
harness's own. One file has been playing both roles unnoticed, because this project's domain *is*
the harness. The placement was never argued either — `911b5b1` moved the file from root into
`docs/` in one clause of an install commit, a day before *Core and instance* existed. Taken inside
[01-0011.0010](done/01-0011.0010-mechanism-declared.md) rather than deferred, because its stage 1 adds
**Part** and a new core term landing in the instance half would be the defect committed while
describing it. What it does not fix — every other core skill's reliance on instance-half
documents — stays [01-0017](01-0017-io-graph-coherent.md)'s, which now carries the glossary as a
worked example rather than a precedent.

**How this queue is ordered** *(the user, 2026-09-07)*: the harness is self-building, so the governing consideration is which slice hands the next one a tool that makes the harness work better — not dependency order alone, and not size. A slice that only describes something ranks below one that gives the next slice a script, a check or a rule it can lean on. The pacer owns this once it exists ([01-0020](01-0020-pacer.md)); until then it is stated here and applied by hand. Open idea, unowned: `/impact` could name the *error classes that stay uncaught* if a slice is not built, and the queue could rank by which noise is loudest — a candidate extension of [01-0010.0080](01-0010.0080-impact-work-shape.md), not yet its scope.

**Working documents:** [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md), [working glossary](../glossary.md), and [pacer.md](../pacer.md), which holds the pacer's core rules resolved so far until [01-0020](01-0020-pacer.md) carries them. `docs/process.md` is preliminary under a `<temporary>` block; the pacer owns it once it exists. Local overrides are no longer deferred: [01-0010.0110](01-0010.0110-project-facets-injected.md) owns them. The spec is not accepted; [01-0010.0035](done/01-0010.0035-install-spec.md)'s RFC is [the install plan](../rfc/done/01-0010.0035-install-spec.md).
**Current stage:** [01-0011.0022](done/01-0011.0022-shape-survives-second-mechanism.md) and
[01-0011.0010](done/01-0011.0010-mechanism-declared.md) are **Done, 2026-09-07**, closed together
once the second mechanism was built with the shape and the check admitted it unchanged.
`/maintain` is declared; the check reports two declarations true; the body is numbered
instructions A1–F3 with two hand-copied blocks and the interim dueness rule inside temporary
statements; the evidence moved to `docs/mechanisms/`; `docs/process.md` shed *Mechanisms and
skills*, *Tree maintenance*, *Mechanical maintenance* and *Current documents and evidence*;
112 → 115 tests. **Next cycle needs a nod** (`next-cycle=ask`). By the ordering rule below, the
candidate is [.0020](01-0011.0020-rules-one-home.md), the injector: both declarations now carry
hand copies waiting for it, and it hands every later slice the tool it leans on. The paragraph
that follows is the pointer, not the record. The align read Life's `maintenance` mechanism directly
and falsified `.0022`'s premise before anything was built, which is why the clock is its own
ticket, [01-0011.0060](01-0011.0060-mechanism-rechecked-when-governing-moves.md). Every decision
of that align, what `/implement` reversed on the user's instruction — strengths, attribution,
prose — and what the two `/verify` passes repaired are on
[the closed ticket](done/01-0011.0022-shape-survives-second-mechanism.md); the facet restated on
[01-0010.0110](01-0010.0110-project-facets-injected.md), the rules-file input on
[.0020](01-0011.0020-rules-one-home.md), the skill structure on
[01-0010.0100](01-0010.0100-remaining-named-corpus.md), and three findings on
[01-0017](01-0017-io-graph-coherent.md). Wake still lands on `/align` until the pacer
exists. Resume by opening a fresh session here, confirming its
first line is the entry contract [AGENTS.md](../../AGENTS.md) declares, and taking the current pass
above. The prose in this queue is a chronological record of passes and still carries superseded
statements from earlier ones; consolidating it is `/maintain`'s at close.

| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Shared harness across projects](01-0010-dev-harness-shared-and-local.md) | In progress | HITL | Projects share a canonical development method, contribute improvements to it, and receive accepted changes mechanically while preserving project-specific behavior across Claude Code, Codex and Cursor. |
| [Align on harness work in Codex, Cursor and Claude Code](done/01-0010.0020-live-alignment-across-hosts.md) | Done (2026-09-06) | HITL | The user can open this repository in any of the three hosts and align on its current work using the same installed `/align` and `/impact`, current decisions and glossary, with evidence of which skills each host actually made available. |
| [Install /ticket](done/01-0010.0030-install-ticket.md) | Done (2026-09-06) | HITL | `/ticket` is installed under `.agents/skills` from the accepted selection, discoverable in Claude Code, and used once here to mint a real slice, with `/impact` called from it as the entry file says. |
| [Install /spec](done/01-0010.0035-install-spec.md) | Done (2026-09-06) | HITL | `/spec` is installed from the accepted selection, discoverable, and used once to develop the spec for completing this harness's delivery ring; `/plan`, `/implement`, `/verify` and `/maintain` follow that spec. |
| [Install /plan](done/01-0010.0040-install-plan.md) | Done (2026-09-06) | HITL | `/plan` is installed from the accepted selection, discoverable, and used once to write an RFC for the next ring slice, calling `/impact` as the entry file says. |
| [Install the implementation mechanism](done/01-0010.0050-install-implement.md) | Done (2026-09-06) | HITL | The implementation mechanism is installed — `/implement`, `/tdd` with its supporting files, and `/improve-comments` — discoverable, and used once to implement a planned harness slice. |
| [Install /verify](done/01-0010.0060-install-verify.md) | Done (2026-09-06) | HITL | `/verify` is installed from the accepted selection, discoverable, and used once as the verification of a landed harness slice — ticket, RFC, governing docs, and the project's verification set — under repair-and-report. |
| [Install /maintain](done/01-0010.0070-install-maintain.md) | Done (2026-09-06) | HITL | `/maintain` is installed, discoverable, and used once to complete a paired ticket+RFC close; it enumerates `<temporary>` blocks; denoise and sync-arch composition is aligned on this ticket. |
| [/impact recommends the work's shape](01-0010.0080-impact-work-shape.md) | Ready | HITL | `/impact` says whether the work it assessed is a spec, a ticket, an RFC or a re-slice, alongside its blast-radius verdict, so `/ticket` and `/plan` receive a routing answer instead of inferring one. |
| [Install /discover](done/01-0010.0090-install-discover.md) | Done (2026-09-06) | HITL | `/discover` is recorded as installed on this slice's authority, used the way `/impact` is and filing nothing, discoverable, and free of references to the estate it came from. |
| [A mechanism says what it is made of](done/01-0011.0010-mechanism-declared.md) | Done (2026-09-07) | HITL | `/mechanism` is installed carrying the shape, `/mechanism` itself is declared in its own directory with every part named and every moment carrying an instruction or a kind of absence, and a check says whether the declaration is true. |
| [A rule has one home and is installed, not copied](01-0011.0020-rules-one-home.md) | Planned (the declaration precedes) | AFK | A mechanism's rules live in one file and a single generic installer writes them as visibly owned blocks into skills the mechanism does not own, removes them leaving each target byte-identical, refuses rather than guesses, and reports a hand-edited block as drift rather than accepting it as a second opinion. |
| [A second mechanism is declared, and the shape holds or is amended](done/01-0011.0022-shape-survives-second-mechanism.md) | Done (2026-09-07) | HITL | `/maintain` is declared through the shape with its parts, its moments and its record obligation each carrying a state, the declaration passes the check `01-0011.0010` shipped, and what the second application breaks is amended in the shape rather than worked around in the declaration. |
| [The archive duty reaches the skill that archives](01-0011.0025-archive-duty-reaches-maintain.md) | Planned (the second mechanism precedes) | HITL | `/ticket` is declared through the shape, paired close's rules live in one file and are installed into `/maintain` so it carries the archive duty rather than only the permission form, and `/ticket`'s records declare a shape that a script enforces. |
| [Finished work that is not archived is listed](01-0011.0030-archive-backlog-listed.md) | Planned (the record shape precedes) | AFK | A command lists records whose work is finished and whose folder does not say so, and the standing count is held as a ratchet — silent at or below its mark, loud when it rises. |
| [The queue is read from the tickets](01-0011.0040-queue-derived-index.md) | Planned (the record shape precedes) | HITL | The queue's status, type and outcome are derived from the ticket headers that own them, so the queue cannot contradict a ticket, and the pacing prose stays hand-written. |
| [A mechanism's shape is observed, not asserted](01-0011.0050-shape-checked.md) | Planned (three declarations precede) | AFK | A check reports, across every declared mechanism, each moment's instruction or its kind of absence, and every installed skill is either named by a mechanism or sits in an allowlist with its reason. |
| [A mechanism is re-checked when what governs it moves](01-0011.0060-mechanism-rechecked-when-governing-moves.md) | Planned (own align precedes; three dependencies open) | HITL | `/maintain` reads which mechanisms are due from a derivation over the tree rather than inferring it: a mechanism's doc is due when the meta-rules moved since it was last checked, its records are due when its own surfaces moved or its records churned, the last check is a mark that only the closing step of a maintenance can move, and dueness is derived at every look and never stored. |
| [Hierarchy reads the same everywhere](01-0012-hierarchy-coherent.md) | Ready | HITL | Hierarchy — from what height a thing is looked at — has one account, and every statement about height across the entry file, process, glossary and skills either is that account or points at it. |
| [Scope reads the same everywhere](01-0014-scope-coherent.md) | Planned (hierarchy precedes) | HITL | Scope — the extent of what a pass, a ticket or a document covers — has one account, and every scope statement across the harness either is that account or points at it. |
| [Each skill owns its own responsibility](01-0016-responsibility-coherent.md) | Planned (hierarchy and scope precede) | HITL | Every skill states only what it owns and links for the rest; a rule appears once, in the skill responsible for it; contradictions between skills are resolved rather than coexisting. |
| [Every skill and document has named producers and consumers](01-0017-io-graph-coherent.md) | Planned (the first mechanism precedes) | HITL | Every mechanism in this tree is declared to the shape paired close proved, every installed skill is named by one or allowlisted with its reason, and the documents four skills transact against either exist with an owner or stop being referenced. |
| [Rules reach the occasion they are for](01-0018-reachability-coherent.md) | Planned (responsibility precedes) | HITL | A rule or skill that applies at an occasion is actually in front of the agent at that occasion, and where it cannot be, the gap is named rather than assumed away. |
| [A project's local facts are answered once and installed](01-0010.0110-project-facets-injected.md) | Planned (the injector precedes) | HITL | A project answers the harness's questions about its own facets once — its verification set, its gate commands, its host loaders — and those answers are installed into the places that need them, so no core skill carries a hand-written override and a recipient project has one place to answer rather than a corpus to edit. |
| [What each host can say without being asked](01-0010.0120-host-delivery-surfaces.md) | Ready | HITL | The harness knows, from observation rather than assumption, what Claude Code, Codex and Cursor each place in front of an agent without being asked; that capability is recorded with what cannot be confirmed about it; and the decision of whether this harness takes a dynamic tier-1 surface at all is landed in its durable home, unblocking the slices that assume one. |
| [The remaining named corpus arrives](01-0010.0100-remaining-named-corpus.md) | Partial (four of five installed 2026-09-07; nothing else met) | HITL | `/advise`, `/skill-up`, `/commit`, `/celebrate` and `/edge` are installed from the accepted selection, discoverable, each used once, and the core changes they owe are landed with them. |
| [Pacer](01-0020-pacer.md) | Planned (own align precedes) | HITL | The agent knows, on every turn, what it does after `/recall` and what the turn's reply is scoped to, from Tier 1 rules in the entry file; and after a session break the next session resumes the delivery ring at the step it stopped, stopping only for a HITL escalation. |
| [Life informs the dev harness](done/01-0010.0010-life-informs-dev-harness.md) | Done (2026-09-05) | HITL | Life's rule delivery and maintenance experience informs the dev harness, and the user can choose a concrete project-to-core-to-project propagation model. |

The [initial comparison](../research/audit-2026-09-05/REPORT.md) is complete. Decisions, rather than missing comparison evidence, now gate extraction.

[The adoption shortlist](01-0010-dev-harness-shared-and-local.md#adoption-shortlist--recommendations-awaiting-alignment) retains the broader open design decisions. [Life findings](../research/life-harness-findings.md) supply the supporting evidence; the completed research ticket does not remain open for implementation decisions owned by the parent.
