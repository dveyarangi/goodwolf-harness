# Delivery status

**Last updated:** 2026-09-20

**Completed step:** `/maintain` on [01-0011.0050](done/01-0011.0050-shape-checked.md), 2026-09-20 — the paired close of the slice that made a `not yet` row a straw dog and every unclaimed skill say so on its own first line; the whole ring ran on it in one day, align to close. Before it, `/discover` over the repository premise, 2026-09-10, filed on [01-0010](01-0010-dev-harness-shared-and-local.md#discover--the-premise-2026-09-10), and `/maintain` on [01-0011.0025](done/01-0011.0025-archive-duty-reaches-maintain.md), 2026-09-09. What every earlier pass decided is on the tickets that own it and in the session records under `docs/sessions/`. **Separation now precedes the coherence chain** *(the user, 2026-09-09, on [the frost_map probe](../research/separation-probe-frost-map.md))*: [01-0010.0130](01-0010.0130-harness-installs-into-another-tree.md) takes its `/align` jointly with [01-0010.0110](01-0010.0110-project-facets-injected.md)'s. Behind them the spec's ordering is unchanged: the four rule refactors, then [01-0020](01-0020-pacer.md), which wants the Tier 1 placement rule that [01-0018](01-0018-reachability-coherent.md) settles; [01-0010.0080](01-0010.0080-impact-work-shape.md) stays Ready beside them. The verification set is 228 behavioral tests over the maintenance scripts, `mechanisms.py --check` over the declared mechanisms and every installed skill's claim, `inject_rules.py --check` over the rules files and their blocks, and `tickets.py --check` over the live ticket records; the straw dogs are what `straw_dogs.py docs AGENTS.md .agents` lists, 53 on 2026-09-20 (23 blocks, eleven `not yet` rows, nineteen skill claims, one `TODO`), all bound, no condition met — `tests` left that list on 2026-09-09 when the suite moved to `.agents/scripts/test/`, inside the scope `.agents` already covers. The suite runs in well under a minute since 2026-09-09 — 69s measured that day, 37.6s on 2026-09-10 — down from 118s: `setUp` was `git init` plus two `git config`, three process spawns and 59% of the wall clock, and each case now stamps a copy of one template `.git` that Git builds once per process.

<straw-dog until="01-0020 is done" ticket="docs/tickets/01-0020-pacer.md">
**How this queue is ordered** *(the user, 2026-09-07)*: the harness is self-building, so the governing consideration is which slice hands the next one a tool that makes the harness work better — not dependency order alone, and not size. A slice that only describes something ranks below one that gives the next slice a script, a check or a rule it can lean on. The pacer owns this once it exists ([01-0020](01-0020-pacer.md)); until then it is stated here and applied by hand.
</straw-dog>
Open idea, unowned: `/impact` could name the *error classes that stay uncaught* if a slice is not built, and the queue could rank by which noise is loudest — a candidate extension of [01-0010.0080](01-0010.0080-impact-work-shape.md), not yet its scope.

**Working documents:** [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md), [the install spec — accepted 2026-09-14](../spec/01-0010.0130-harness-installs-into-another-tree.md), [working glossary](../glossary.md), and [pacer.md](../pacer.md), which holds the pacer's core rules resolved so far until [01-0020](01-0020-pacer.md) carries them. `docs/process.md` is preliminary under a `<straw-dog>` block; the pacer owns it once it exists. Local overrides are no longer deferred: [01-0010.0110](01-0010.0110-project-facets-injected.md) owns them. The spec is not accepted; [01-0010.0035](done/01-0010.0035-install-spec.md)'s RFC is [the install plan](../rfc/done/01-0010.0035-install-spec.md).
**Current stage:** [01-0011.0025](done/01-0011.0025-archive-duty-reaches-maintain.md), the ticket
mechanism, is **Done, 2026-09-09**, and with it the defect the whole spec was written from is
closed: the archive duty now reaches `/maintain` as an installed block from `ticket.rules.md`
rather than as a hand copy nobody could check. Six rules across three targets — `/maintain`
takes paired close and the maintainer to run, `/plan` the basename rule, `/align` the resolution
rule. The ticket is declared as a record in `TICKET-FORMAT.md`, field by field, with its stage
read from the `Plan` bullet, and `tickets.py --check` holds every live ticket to it. `declared by`
left the shape entirely, on the user's question of what it was for. Every decision of the align
and its four `/plan` passes is on the closed ticket and its RFC; the two mechanism evidence files
carry the grades. **Three slices come free**: [.0030](01-0011.0030-archive-backlog-listed.md) and
[.0040](01-0011.0040-queue-derived-index.md) now have a record shape to read, and
[.0050](done/01-0011.0050-shape-checked.md) has its third declaration to sweep, so all three are Ready
and R6 waits on the last of them. By the ordering rule below `.0050` was the candidate among them:
it is the only one that gives the next slice a check, and it is AFK. **Separation overtook all three
on 2026-09-09.** Its joint `/align` ran 2026-09-10 → 11 and
[its spec was accepted 2026-09-14](../spec/01-0010.0130-harness-installs-into-another-tree.md);
`/ticket` minted nothing — both parents were rewritten to feature altitude 2026-09-15, since each
fits one RFC. The chain is now [01-0010.0140](01-0010.0140-core-stands-alone.md) →
[01-0010.0110](01-0010.0110-project-facets-injected.md) → [01-0010.0130](01-0010.0130-harness-installs-into-another-tree.md),
and `.0050` — once the manifest's gate and the referent's form — is **Done, 2026-09-20**: both
aligns ran that morning, `.0050` went through the whole ring in a day, and `.0140` is Ready.
**The candidate is `.0140`'s `/plan`**, opening with the sixteen bare links still in core wrapped
as straw dogs on that ticket. [01-0020](01-0020-pacer.md)'s align opened 2026-09-20 on the wake
rule alone — every session runs `/recall` first, at entry contract v9, wrapped on the ticket
until the pacer is declared and installs it — and its remaining decisions stay open.
**Next cycle needs a nod**
(`next-cycle=ask`). Resume by opening a fresh session here, confirming its first line is the entry
contract [AGENTS.md](../../AGENTS.md) declares and its first act is `/recall`, and taking the
current pass above; what follows the wake until the pacer exists is
[pacer.md](../pacer.md#core-rules--under-alignment)'s.

**Outside the ring, 2026-09-09, on the user's direction.** `/recall`, `/edge`, `/review-architecture`
and `/setup-devops` were installed from their accepted sources, which **completes the selection's
twenty working commands** and empties [01-0010](01-0010-dev-harness-shared-and-local.md)'s install
backlog; `legacy/` was deleted; the entry contract went to **v7** — retitled, `<project-local>` given
its own section, the self-hosting note moved into the block that owns it; and the suite's fixture was
rebuilt for speed. One ticket was minted,
[01-0010.0105](01-0010.0105-backlog-five-arrive.md), for the five commands the parent had held as a
backlog line rather than a record. **Three proposed tickets were not minted**: `/edge`'s declaration
and its `docs/edge/` question are [01-0010.0100](01-0010.0100-remaining-named-corpus.md)'s align,
declaring every installed skill is
[01-0017](01-0017-io-graph-coherent.md)'s — nineteen claims owed, not eleven — and where `/recall`
sits is [01-0020](01-0020-pacer.md)'s. Two decisions wait at `/align`: whether ADRs or tickets are
the home for a decision, which the entry file currently answers both ways, and what an entry-contract
version covers, which today names five of its nine sections.

| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Shared harness across projects](01-0010-dev-harness-shared-and-local.md) | In progress | HITL | Projects share a canonical development method, contribute improvements to it, and receive accepted changes mechanically while preserving project-specific behavior across Claude Code, Codex and Cursor. |
| [/impact recommends the work's shape](01-0010.0080-impact-work-shape.md) | Ready | HITL | `/impact` says whether the work it assessed is a spec, a ticket, an RFC or a re-slice, alongside its blast-radius verdict, so `/ticket` and `/plan` receive a routing answer instead of inferring one. |
| [The backlog five arrive with their adaptations](01-0010.0105-backlog-five-arrive.md) | Partial (three installed 2026-09-09) | HITL | `/conclude`, `/recall`, `/dream`, `/review-architecture` and `/setup-devops` carry the adaptations the selection names for them, each has been used once here, and the twenty selected working commands are complete with nothing left in the parent's backlog. |
| [Finished work that is not archived is listed](01-0011.0030-archive-backlog-listed.md) | Ready | AFK | A command lists records whose work is finished and whose folder does not say so, and the standing count is held as a ratchet — silent at or below its mark, loud when it rises. |
| [The queue is read from the tickets](01-0011.0040-queue-derived-index.md) | Ready | HITL | The queue's status, type and outcome are derived from the ticket headers that own them, so the queue cannot contradict a ticket, and the pacing prose stays hand-written. |
| [A mechanism is re-checked when what governs it moves](01-0011.0060-mechanism-rechecked-when-governing-moves.md) | Planned (own align precedes; 01-0010.0120 open) | HITL | `/maintain` reads which mechanisms are due from a derivation over the tree rather than inferring it: a mechanism's doc is due when the meta-rules moved since it was last checked, its records are due when its own surfaces moved or its records churned, the last check is a mark that only the closing step of a maintenance can move, and dueness is derived at every look and never stored. |
| [Hierarchy reads the same everywhere](01-0012-hierarchy-coherent.md) | Ready | HITL | Hierarchy — from what height a thing is looked at — has one account, and every statement about height across the entry file, process, glossary and skills either is that account or points at it. |
| [Scope reads the same everywhere](01-0014-scope-coherent.md) | Planned (hierarchy precedes) | HITL | Scope — the extent of what a pass, a ticket or a document covers — has one account, and every scope statement across the harness either is that account or points at it. |
| [Each skill owns its own responsibility](01-0016-responsibility-coherent.md) | Planned (hierarchy and scope precede) | HITL | Every skill states only what it owns and links for the rest; a rule appears once, in the skill responsible for it; contradictions between skills are resolved rather than coexisting. |
| [Every skill and document has named producers and consumers](01-0017-io-graph-coherent.md) | Planned (the first mechanism precedes) | HITL | Every mechanism in this tree is declared to the shape paired close proved, every installed skill is named by one or allowlisted with its reason, and the documents four skills transact against either exist with an owner or stop being referenced. |
| [A term reaches a record only if the glossary defines it](01-0017.0010-terms-defined-before-they-land.md) | In progress (align underway) | HITL | A term used as shared vocabulary is either defined in the glossary or is stopped as a decision before it reaches a record, every glossary rule has one authored home, and the rule that enforces this is where the occasion is rather than inside one skill nobody had invoked. |
| [Changing how the project builds is one edit](01-0017.0020-practice-swaps-in-one-edit.md) | In progress (align underway) | HITL | The transferable practice this harness carries — how tests are written, how architecture is documented — has one owner, so adopting a different practice is an edit to one mechanism instead of a refactor across scattered skills, and what belongs to that corpus rather than to the harness's own loop is settled rather than assumed. |
| [Rules reach the occasion they are for](01-0018-reachability-coherent.md) | Planned (responsibility precedes) | HITL | A rule or skill that applies at an occasion is actually in front of the agent at that occasion, and where it cannot be, the gap is named rather than assumed away. |
| [A project's local facts are answered once and installed](01-0010.0110-project-facets-injected.md) | Planned (01-0010.0140 precedes; spec accepted 2026-09-14) | HITL | A project writes every local override and answer into one file beside its entry file, in the format the injector already reads; the injector installs from it after every deployment, last, with an override naming the rule it overrides; no core file carries a `<project-local>` block; and this repository is the first project to do it. |
| [The harness installs into a tree that is not its own](01-0010.0130-harness-installs-into-another-tree.md) | Planned (01-0010.0110 precedes; spec accepted 2026-09-14) | HITL | A project that is not this one receives the harness by a repeatable install rather than by hand: what arrived is identified by a core revision, the recipient's own facts survive redeployment, the shipped checks pass on arrival, and an install that cannot complete stops and says why instead of substituting something that fits. |
| [Core stands alone, and a check says so at home](01-0010.0140-core-stands-alone.md) | Ready (aligned 2026-09-20) | HITL | A leak — a citation from core to a document only the instance has — fails at home, on every change, instead of on the next port: the entry file states what core may name under `docs/`, the mechanism check holds every core file to it, and the leaks are gone. |
| [What each host can say without being asked](01-0010.0120-host-delivery-surfaces.md) | Ready | HITL | The harness knows, from observation rather than assumption, what Claude Code, Codex and Cursor each place in front of an agent without being asked; that capability is recorded with what cannot be confirmed about it; and the decision of whether this harness takes a dynamic tier-1 surface at all is landed in its durable home, unblocking the slices that assume one. |
| [The remaining named corpus arrives](01-0010.0100-remaining-named-corpus.md) | Partial (all five installed by 2026-09-09; nothing else met) | HITL | `/advise`, `/skill-up`, `/commit`, `/celebrate` and `/edge` are installed from the accepted selection, discoverable, each used once, and the core changes they owe are landed with them. |
| [The harness changes its own rules by stated meta-rules](01-0019-harness-amends-itself-by-explicit-meta-rules.md) | Blocked (accumulating evidence) | HITL | Amending the harness's own rules follows stated meta-rules — how a failure is registered, when a rule is reworded, what counts as evidence that it did not work — instead of a judgement made afresh each time; and whether that is its own mechanism is answered from strikes rather than from argument. |
| [Pacer](01-0020-pacer.md) | In progress (align underway; first core rule landed 2026-09-20) | HITL | The agent knows, on every turn, what it does after `/recall` and what the turn's reply is scoped to, from Tier 1 rules in the entry file; and after a session break the next session resumes the delivery ring at the step it stopped, stopping only for a HITL escalation. |

The [initial comparison](../research/audit-2026-09-05/REPORT.md) is complete. Decisions, rather than missing comparison evidence, now gate extraction.

[The adoption shortlist](01-0010-dev-harness-shared-and-local.md#adoption-shortlist--recommendations-awaiting-alignment) retains the broader open design decisions. [Life findings](../research/life-harness-findings.md) supply the supporting evidence; the completed research ticket does not remain open for implementation decisions owned by the parent.
