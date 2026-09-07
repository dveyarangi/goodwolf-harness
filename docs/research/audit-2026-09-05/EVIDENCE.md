# Verified file evidence

Generated from the inspected working trees. SHA-256 prefixes below are byte hashes; full hashes, file IDs, local blocks and Git dates are in `inventory.json` and `file-matrix.csv`.

## Primary corpus matrix

| File | H | M | A | F |
|---|---|---|---|---|
| advise/SKILL.md | 185de049a7 | f30c75d849 | f30c75d849 | c8bfb15c6f |
| align/ADR-FORMAT.md | 6a7d7d0b96 | 1e1fbcc4cc | 1e1fbcc4cc | 1e1fbcc4cc |
| align/ARCH-FORMAT.md | 954887aa4b | 35b23a8a9f | 35b23a8a9f | 002ee88c47 |
| align/CONCERNS-FORMAT.md | — | — | 99c75645f0 | — |
| align/EDGE-FORMAT.md | — | 77211d3216 | a1cae87e70 | 0bb4498b06 |
| align/GLOSSARY-FORMAT.md | edee2de3a5 | edee2de3a5 | edee2de3a5 | 7d792d79d3 |
| align/SKILL.md | 50e4f38831 | c8e09c5b2b | 92d880c0e0 | 6644c49b7a |
| celebrate/SKILL.md | — | c85d5b0a07 | c85d5b0a07 | c85d5b0a07 |
| commit/SKILL.md | — | 2c5af6673a | 2bd403be0b | bbb0e9c947 |
| conclude/SKILL.md | 4cfedf9b42 | 26189c1b14 | 26189c1b14 | 7e310ce6b4 |
| denoise/SKILL.md | e57aaab0fd | 5a175034b6 | 5a175034b6 | 306692f32f |
| dream/SKILL.md | — | 37de45743d | 37de45743d | — |
| edge/SKILL.md | — | aa9f930acd | aa9f930acd | — |
| impact/SKILL.md | — | 82c1ca96c6 | 82c1ca96c6 | 551ed70b18 |
| implement/SKILL.md | 3e07a590c3 | ecd1a250bc | ecd1a250bc | b46a360977 |
| improve-comments/SKILL.md | e72576b8e3 | f2923712ae | f2923712ae | f2923712ae |
| plan-impl/SKILL.md | 8e140173ed | d26406f1fc | d26406f1fc | c213bf38b2 |
| recall/SKILL.md | — | 0bacb2e195 | 6b77ec586f | b89068516e |
| review-architecture/REFERENCE.md | 3bcc950ca2 | 2dca8d8a5d | 2dca8d8a5d | 2dca8d8a5d |
| review-architecture/SKILL.md | f53a07a4f3 | 2046aa4083 | 2046aa4083 | 2046aa4083 |
| review-impl/SKILL.md | — | 98c206c81d | 98c206c81d | 53d8957387 |
| setup-devops/SKILL.md | 6d6f7a7f07 | 8dbbe764ed | 8dbbe764ed | 8dbbe764ed |
| skill-up/SKILL.md | — | b4775b457e | ddd9b69064 | b4775b457e |
| sync-arch/SKILL.md | 93317179e7 | f5d0b0d57b | fd3a6a76bd | 0c56ca43b5 |
| tdd/SKILL.md | af05970506 | 94eb30d4ac | 94eb30d4ac | 94eb30d4ac |
| tdd/deep-modules.md | f2123700bf | f2123700bf | f2123700bf | f2123700bf |
| tdd/interface-design.md | 764c5ff0e3 | 764c5ff0e3 | 764c5ff0e3 | 764c5ff0e3 |
| tdd/mocking.md | 3ceb807fdf | 3ceb807fdf | 3ceb807fdf | 3ceb807fdf |
| tdd/refactoring.md | 54fced22dd | 54fced22dd | 54fced22dd | 54fced22dd |
| tdd/tests.md | e12182f5c4 | e12182f5c4 | e12182f5c4 | e12182f5c4 |
| to-spec/INITIATIVE-FORMAT.md | — | — | 091f761fbf | — |
| to-spec/SKILL.md | b695d7b7e8 | ce7dd4b29b | 2bc4e10845 | 33e70abe27 |
| to-tickets/NOTION-FORMAT.md | — | — | bd8ce07763 | — |
| to-tickets/SKILL.md | bad1096919 | 9bf1935506 | 76dc43c797 | f9ef115e3a |
| to-tickets/TICKET-FORMAT.md | — | 966aa02abc | 0445981db0 | 19dd9aeb9f |
| workflow.excalidraw | — | d8677a2264 | d8677a2264 | — |

## Actual project-local blocks

### H

### M

**commit/SKILL.md**

```xml
<project-local>
The checks are the same gate set CI runs → [cicd.md](../../../docs/cicd.md): `ruff check`, `ruff format --check`, `pyright`, `pytest`.
</project-local>
```

**recall/SKILL.md**

```xml
<project-local>
Delivery state lives in [the queue](../../../docs/tickets/README.md) → [the development process](../../../docs/process.md). What each document owns → [the documentation map](../../../docs/README.md).
</project-local>
```

### A

**commit/SKILL.md**

```xml
<project-local>
Nothing gates a merge in any repository here, so the checks you run before committing are the only ones that will ever run. Where a repo defines none, say that in the commit message rather than leaving the change looking checked.

A push to the default branch is a release: `admin`, `wrf_coordinator` each deploy from it on push. That is why pushing takes its own permission, separately from committing.
</project-local>
```

**recall/SKILL.md**

```xml
<project-local>
Delivery state is not in this repository → [the seam](../../docs/process.md#the-seam). What each local document owns → [the documentation map](../../docs/README.md).
</project-local>
```

### F

**align/GLOSSARY-FORMAT.md**

```xml
<project-local>
This repo is single-context. The glossary lives at `docs/glossary.md`, not the repo root. Infer
that path; do not create a root `glossary.md`.
</project-local>
```

**align/SKILL.md**

```xml
<project-local>
Glossary is `docs/glossary.md`. There are no Edge records yet; skip the Edge challenge until `docs/edge/` exists. `docs/concerns.md` is not yet in the numbered `## N. Title` shape; do not restructure existing entries except to add, retire, or queue one.
</project-local>
```

**commit/SKILL.md**

```xml
<project-local>
There is no CI workflow and no ruff/pyright roster. The code check is
`./venv/Scripts/python.exe -m pytest`. Pure doc or skill changes need none of it.
</project-local>
```

**denoise/SKILL.md**

```xml
<project-local>
A `done/` or session-`history/` move is
`./venv/Scripts/python.exe .agents/scripts/move_doc.py SRC DST [SRC DST ...]`
→ [TICKET-FORMAT.md § One basename per work item](../to-tickets/TICKET-FORMAT.md#one-basename-per-work-item).
</project-local>
```

**implement/SKILL.md**

```xml
<project-local>
There is no typechecker. Run `./venv/Scripts/python.exe -m pytest` (single files during the work, the full suite at the end).
</project-local>
```

**plan-impl/SKILL.md**

```xml
<project-local>
Do not add, bump, or delete `**Pass:**`. If that line is already in the RFC header, keep it.
The project's `docs/process.md` owns how many times a hook re-invokes this skill.
</project-local>
```

**recall/SKILL.md**

```xml
<project-local>
Delivery state lives in [the queue](../../../docs/tickets/README.md) → [the development process](../../../docs/process.md). What each document owns → [the documentation map](../../../docs/README.md).
</project-local>
```

**sync-arch/SKILL.md**

```xml
<project-local>
There are no Edge records yet; skip the Edge challenge until `docs/edge/` exists.
</project-local>
```

## Portable skill changes versus M

Only changed lines are shown. Full context is in the pairwise `.diff` files. Appendices, missing skills and local blocks have separate coverage.

### M versus H

**advise/SKILL.md** — no Git history

```diff
-  Strategic advisory read on the project or a regarded aspect.
+  Advise me on current project by answering strategical questions
-Tell me, whichever is relevant:
+Tell me:
-- What is questionable?
-- What is missing?
+- What is questionable/missing?
-- What are the hidden edges?
```

**align/SKILL.md** — no Git history

```diff
-description: Grilling session that challenges current plan against the existing domain model, sharpens terminology, and updates documentation as decisions crystallise. Use to stress-test a plan against their project's language and documented decisions.
+description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (glossary.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
-
-Begin every alignment with a **necessity gate**: name the present customer, the observable problem, and why existing behaviour cannot satisfy it. An accepted requirement or ADR passes by citation. Weak evidence means narrow, postpone, or eliminate — settle that before exploring design. The gate fires late too: a mechanism whose name will not settle is evidence it should not exist. [/impact](../impact/SKILL.md) traces consequences once the need holds.
-If a *fact* can be found by exploring the codebase, look it up rather than asking me. The *decisions*, though, are mine - put each one to me and wait for my answer.
-
-Do not generalize from one shape. Preserve a seam. Generalize only when a second materially different shape forces the same concept.
+If a *fact* can be foundby exploring the codebase, look it up rather than asking me. The *decisions*, though, are mine - put each one to me and wait for my answer.
-
-## Good architecture
-
-Goal of architecture is to reduce work on creation and maintenance of the system.
-
-Identify the load-bearing assumption behind the proposed shape; ask yourself - what is the cheapest real example that could prove this design assumption wrong?
-
-Check it when practical, preferably against external reality rather than our own docs/tests.
-
-If falsified, realign.
-If unverified and load-bearing, preserve the uncertainty explicitly.
-│   ├── adr/
-│   │   ├── 0001-event-sourced-orders.md
-│   │   └── 0002-postgres-for-write-model.md
-│   ├── architecture.md
-│   └── glossary.md
+│   └── adr/
+│       ├── 0001-event-sourced-orders.md
+│       └── 0002-postgres-for-write-model.md
+├────── architecture.md
+├────── product.md
+├────── glossary.md
+```
+
+If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:
+
+```
+/
+├── CONTEXT-MAP.md
+├── docs/
+│   └── adr/                          ← system-wide decisions
+├── src/
+│   ├── ordering/
+│   │   ├── glossary.md
+│   │   └── docs/adr/                 ← context-specific decisions
+│   └── billing/
+│       ├── glossary.md
+│       └── docs/adr/
-
-This cuts both ways: before *you* propose a name, check the glossary yourself — including its _Avoid_ lists, which are reservations, not suggestions. If every synonym for a concept is avoided, that is a designed constraint telling you which word the project has chosen; work within it rather than proposing around it.
-
-### Challenge against the Edge records
-
-When the plan touches a product edge, check that surface's Edge record
-(`docs/edge/<surface>.md`) — the seam document aggregating the edge's contract, invariants,
-concerns, and staged roadmap. A contradiction with its Contract or Invariants is either a plan
-bug or a deliberate contract change — and a contract change must be named **breaking or
-compatible** out loud before proceeding. Update the record inline as decisions land, using the
-format in [EDGE-FORMAT.md](./EDGE-FORMAT.md): contract changes in `Contract`/`Invariants` (a
-promise without a validating test is marked **⚠ unguarded**), newly surfaced edge-scoped
-concerns as pointers in `Concerns`, staging shifts in `Roadmap`.
-
-### Check whether it was already decided
-
-Before treating a question as open, search the ADRs and architecture docs for it. A surprising amount of "open" questions are accepted decisions the code drifted from — the answer then is "implement the ADR", not a fresh trade-off analysis. Cite the deciding document when you find one.
-
-### Lead with the decisive fact
-
-When recommending between alternatives, find the fact that settles it — a reader count, an import direction, an existing invariant, what a test actually asserts — and lead with it. A pros/cons menu with no decisive fact means you haven't explored enough yet; go look before asking.
-
-### Name the shared assumption
-
-When posing an A-or-B fork, state the assumption both branches share. The user's best answer may dissolve the fork rather than pick a branch — treat "the premise is wrong" as a first-class outcome, not a detour. If a fork keeps resisting resolution, that is usually the sign.
-### Update architecture.md inline
+## Update architecture.md inline
-Open questions and risks live in `docs/concerns.md`, this skill's artifact:
-
-- Ordered by priority, highest first — how much it blocks the current build, and how hard it is to absorb later.
-- Entry is `## N. Title`, then `**Kind:** {sort of pressure, and whether a driver exists} · **Refs:** {ADRs, architecture sections, sibling concerns}`, then the pressure.
-- Numbers are stable IDs, not ranks. A settled concern moves out to its owning ADR or architecture section, leaving a gap. Never renumber, never resolve in place.
-- A concern queued as work keeps only its architectural contact surface plus `→ queued as <ticket-slug>`; the deliberation moves into the ticket.
-- The file holds unresolved pressure — not delivery sequencing, not decisions.
-
-### Record resolutions in the owning ticket inline
-
-When the plan under review is a ticket, record each resolution in the ticket the moment it lands — strike through the original question text and state the decision with its reason beside it, so the ticket carries both the question as it was asked and the answer. Sweep the ticket for internal consistency at the end: an early section may still assert what a later resolution changed.
+Open questions and risks should live in [docs/concerns.md](./docs/concerns.md) The concerns should be sorted highest priority first; Settled items move out to other architecture docs.
```

**conclude/SKILL.md** — no Git history

```diff
-  Conclude work session into a session record. Use when a chunk of work wraps up.
+  Concludes curent chat, extracting a brief summary of work done, the remaining open questions and other things that need continuation into a markdown file under docs/sessions
-Conclude todays/last session of work (that may span additional chats/external changes) - everything since the previous session recorded, extracting:
+Conclude curent chat, extracting:
-- what the session settled, one line each with a reference to where the decision now lives,
-In addition, use /advise skill questions to describe the session.
-
-Open questions go to their owning document first — durable design pressure to `docs/concerns.md`, a ticket's question into that ticket, a hard-to-reverse trade-off to an ADR — and the session file then cites them rather than restating them. Sessions are never maintained as current, so a question left only here will still look open long after it was answered.
-
-
-Session conventions, owned here — other skills and the directory README defer to this list:
-
-- Named `docs/sessions/NNNN-<YYYYMMDD>-<name>.md`; take the next number from the directory listing.
-- A session is a historical snapshot, never maintained as current. Never rewrite an old one to reflect later delivery — write a new one, or update the owning ticket or contract.
-- Nothing links *to* a session, including other sessions. Sessions may link outward.
-- Records older than the rolling seven-day window move to `docs/sessions/history/YYYY-MM/` (swept by `/denoise`).
+Session file should be using naming pattern `docs/sessions/0001-<YYYYMMDD>-<name>`, keeping constantly incrementing enumeration.
```

**denoise/SKILL.md** — no Git history

```diff
-Scope: the topic in context, or the entire codebase on user request. Learn where this repo already treats each fact as
-authoritative; follow that layering — do not invent one. Out of scope: code structure, reorganizing where facts live.
-Always explore `architecture.md`, `glossary.md`, `concerns.md` and relevant ADRs too.
+The topic in context or entire codebase, on user request. Learn where this repo already treats each fact as
+authoritative; follow that layering — do not invent one. Out of scope: code
+structure, contradictory passages, reorganizing where facts live.
+Always explore `architecture.md`, `glossary.md` and relevant ADRs too.
-**Unwrinkle.** Cross-explore for contradictions, under or overstatements, redundancies or other misalignments between docs; make sure different architecture docs are aligned with each other.
+**Unwrinkle.** Cross-explore for contradictions, under or overstatements, redundancies or other misalignments between docs, make sure different architecture docs are aligned with each-other.
-Exclude previous sessions and RFCs — they are historical records, not architectural statements. All truth statements should live in architecture, ADRs or code.
+Exclude previous sessions and RFC - they are historical records, not architectural statements. All truth statement should live in architecture, adrs or code.
-**Concerns.** Sweep `concerns.md` whole, not only the entries in context. An entry stating a decision
-or an accepted limitation belongs in its owning ADR; an entry carrying its own revision history
-states what is true now; a dead trigger or a stale ref retires. [/align](../align/SKILL.md) owns the
-retirement rule — this skill supplies the occasion.
-
-Core architecture docs must not reference sessions, tickets or RFCs. One exception: a queued
-concern's `→ queued as <ticket-slug>` marker in `concerns.md` is delivery routing, not
-architecture — keep it.
-
-Enforce [/conclude](../conclude/SKILL.md)'s session rules: archive records past the rolling window, and make sure nothing links to a session.
-
-Done tickets and rfcs should move to corresponding done folders, keeping their basenames ([TICKET-FORMAT.md](../to-tickets/TICKET-FORMAT.md#one-basename-per-work-item)).
-
-HOWEVER, the README.md of sessions, tickets and rfcs, and all other indexes must be denoised.
+Core architecture docs must not reference sessions, tickets or RFCs.
```

**implement/SKILL.md** — no Git history

```diff
-description: Implement the agreed work into code, following its governing docs.
+description: Implement a piece of work based on a spec or set of tickets.
-Implement the code described by relevant architecture decisions (spec/ticket/rfc/prior discussion).
+Implement the code described by relevant architecture decisions (spec/ticket/prior discussion).
-Pick entity names in vibe with the project glossary.
-Do not use implementation-shaped names or parameters; orient them at the function's meaning toward the client.
+Make sure to investigate the relevant specs, tickets and RFCs in /docs folder.
+
+Use very slight alchemical cyber/steampunk laboratory inclination when picking names entities.
+Do not use implementation-shaped names or parameters, instead make them oriented at function meaning toward client.
-The code should read as a story. Make sure the main process appears first in the file, where possible, and main boundaries' implementation reads through entities, interfaces and submethods used as nouns, adjectives and verbs.
-
-In case of temporary code added as intermediate scaffolding that is going to change/go away in future iteration, mark it so in docstrings.
-
-Make sure the errors follow error rules.
-
-Make sure to read and follow /improve-comments rules. Make sure to mark the TODOs (shapes that are temporary, hotpaths that may need optimization or other pending actions)
-
-Do not move the RFC to Done at the end of your work, it will be done by later skills:
-Once done, if relevant, and unless you need to take a break, use /review-impl and /sync-arch to review the work.
-Do not commit your work until explicitly approved by user.
+
+Once done, use /sync-arch to review the work.
+
+Do not commit your work until requested.
```

**improve-comments/SKILL.md** — no Git history

```diff
-description: Write or improve codebase comments
+description: Write or improve code base comments
-# We prefer freshness over provider priority here because stale severe-weather data is dangerous.
+# We prefer freshness over provider priority here because stale frost data is dangerous.
-Always mark the temporary code, that will be dissolved/changed by some future work, with TODO (temporary) (and add reference to related doc/concern)
-
-Keep the marker exact and put ownership after the colon, for example:
-`TODO (temporary): [0117](path) replaces this shim.` Numeric IDs remain document references, not
-part of the TODO syntax.
-
-Other than that, TODO should name a concrete missing action.
-
+A TODO must name a concrete missing action.
+
+
-
-## # @hotpath
-Hotpath comment `# @hotpath` may appear at method or code block.
-It means that this is important root flow of the program and deserves better comments inside. Do not delete comments inside hotpath blocks, but you can finetune or trim them when overexplaining.
-
-
-Do not use comments to excuse unclear code. Either make it clear, mark it with TODO or explain why the shape is chosen:
+Do not use comments to excuse unclear code.
-# Provider returns mixed local/UTC timestamps; keep this branch until upstream fixes export format. Concern/doc ref ###
+# Provider returns mixed local/UTC timestamps; keep this branch until upstream fixes export format.
-Avoid dense line-by-line comments, unless on hotpath and tell a story.
+Avoid dense line-by-line comments.
-If architecture entry/decision/description already exists, prefer link to docs instead elaborating on it.
+If architecture entry/decision/description already exists, prefer link to docs instead of restating it.
```

**plan-impl/SKILL.md** — no Git history

```diff
-description: Plan or repeatedly validate a ticket's implementation RFC against its governing docs and code before implementation.
+description: Plan implementation for ticket/task at hand
-- Explore documentation in depth, follow links in it to find all decisions relevant to current task. Find out which documented boundaries are involved, and whether implementation challenges them.
-
-- If the ticket at hand is too coarse to yield a single unambiguous RFC, stop planning and decompose it into sub-tickets via /to-tickets first; then plan the first child.
-
-- An RFC implements a ticket — no ticketless RFCs. If the task at hand has no ticket, create it first per the [to-tickets skill](../to-tickets/SKILL.md); its behavior-altitude rule governs the criteria (shape stays in the RFC).
-
-- When incepting, ask yourself - what is the cheapest real example that could prove this design assumption wrong?
-
-- Consider and expose /impact when discussing or providing recommendations or approaches.
+- Explore documentation in depth, follow links in it to find all decisions relevant to current task.
-- Detect implementation challenges and use /align skill to resolve them with user.
+- Detect open concern and use /align skill to resolve them with user.
-- Do not generalize from one shape. Preserve a seam. Generalize only when a second materially different shape forces the same concept.
+- Major goal of this planning is to find inconsistencies in the pre-planned architecture. Do this diligently. If such inconsistency found, do not stick blindly for architectural decision - instead raise concern with user to resolve it - either in code or in arch docs
-- Do not select implementation shapes just because "that how it is usually done" or based on first idea. Promote simplicity, look for elegant solutions, prefer removing over expanding, prefer conciseness over verbosity.
-
-- Do not invent impl nouns or verbs that are not discussed or approved by user. Use existing vocabulary.
-
-- If you see a concern, first check deeper how the existing architecture documentation describes it - it most probably already does. Read architecture.md, ADRs and concerns.md for this.
-
-- Major goal of this planning is to find inconsistencies in the pre-planned architecture. Do this diligently. If such inconsistency found, do not stick blindly for architectural decision - instead raise concern with user to resolve it - either in code or in arch docs.
-
-- Make the RFC determinate where a choice shapes observable behavior, a boundary or interface, ownership, failure semantics, compatibility, migration, or another non-local constraint. State the shaping fact with a reference to its durable owner; never rely on session context. Leave reversible implementation-local choices to /tdd and /implement unless they become load-bearing.
-
-- The RFC (original or amended) must not describe architecture absent from the architecture docs — land the decision in the docs first (/align when needed), then reference it from the RFC.
-
-- Describe the implementation stages; allocate them according to /tdd rules. Look at stages to make sure each of them keeps the tests green; in case that would take too much temporary effort, allow red, note about test status and compact reason for it.
-
-- Map out scope-specific limitations, follow-ups and related out-of-scope concerns.
-
-- Prefer reuse and reduction of existing nouns, verbs and adjectives; when adding shape - make sure documentation supports it, if in any doubt - /align with user.
-
-- Any wrinkle against architecture should be resolved; when solution is not found or following first-principles makes the code weird - align with user. Architecture must lead code shape even if code disagrees. Do not expose public methods or create flows that are not in architecture.
-
-- If planned code includes a temporary solution that is dissolved by future development, add RFC instruction to append TODO comment to code that flags this. Otherwise code changes can start relying or considering the temporal code, which can be hard to disentangle later.
-
-- Repeated invocations are validation passes over the same RFC. Re-read the ticket, RFC, durable docs, and relevant code; challenge the plan against new evidence and amend it in place. Do not create a replacement RFC merely because the plan changed before implementation.
-
-- As an additional pass, try to explain things to yourself simply, as if you are teaching the architecture, and being asked reasonable question and look for areas that evade simple or common-sense explanation.
-
-- Validate the RFC adversarially on every pass:
-  - Probe each boundary and stage with counterexamples, including empty, partial, faulting, and raced outcomes where relevant.
-  - Make every planned test prove the intended behavior and failure reason, not merely that the path succeeds or raises.
-  - Separate sourced facts and existing invariants from assumptions; verify facts in code or authoritative sources and surface load-bearing assumptions for /align.
-  - Reject pseudocode or prescribed structure that introduces undocumented architecture or freezes a reversible local choice.
-  - Check that every new promise names how it will be validated, and that the stages collectively prove the ticket's acceptance criteria.
-
-- Repeat validation until no load-bearing ambiguity, contradiction, or unverified assumption remains. The RFC may permit multiple equivalent local implementations when they preserve the same documented shape and proof.
-
-- If repeated validation keep bringing up gaps, take a step back and look at what causes this oscillation. The architecture, ADRs, tickets are not carved in stone, they can have real contradictions or inconsistencies that cause it. Look into the core reasons and /align on them again if needed.
-
-- Overall, always consider future development and potential code reuse when selecting code shapes.
+- Describe the implementation stages; allocate them accordind to /tdd rules.
-- Record the plan into `docs/rfc/`, named with the owning ticket's basename — no RFC serial. Filename, `done/` moves, and citation: [TICKET-FORMAT.md](../to-tickets/TICKET-FORMAT.md#one-basename-per-work-item).
-- RFC header: H1 is the ticket's title plus ` — implementation plan`; then `**Authored:** YYYY-MM-DD`, and `**Last amended:** YYYY-MM-DD` once a later pass changes the plan; then one line stating what it implements, linking the ticket.
+- Map out scope-specific limitation, follow-ups and related out-of-scope concerns.
+
+- Do not leave implementation ambiguities or optionalities, no matter how small - either resolve them or consult with user.
+
+- Record the plan into markdown file in /docs/rfc. Theile should be using naming pattern `docs/rfc/0001-<YYYYMMDD>-<name>.md`, keeping constantly incrementing enumeration.
```

**review-architecture/SKILL.md** — no Git history

```diff
-description: Explore the codebase for module-deepening opportunities — architectural improvements that raise testability and navigability. Use when asked to improve or refactor the architecture.
+description: Explore a codebase to find opportunities for architectural improvement, focusing on making the codebase more testable by deepening shallow modules. Use when user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more AI-navigable.
-Explore a codebase like an AI would, surface architectural friction, discover opportunities for improving testability, and propose module-deepening refactors as refactor tickets with their RFCs.
+Explore a codebase like an AI would, surface architectural friction, discover opportunities for improving testability, and propose module-deepening refactors as GitHub issue RFCs.
-A **deep module** — small interface hiding a large implementation (→ [tdd/deep-modules.md](../tdd/deep-modules.md)) — is more testable, more AI-navigable, and lets you test at the boundary instead of inside.
+A **deep module** (John Ousterhout, "A Philosophy of Software Design") has a small interface hiding a large implementation. Deep modules are more testable, more AI-navigable, and let you test at the boundary instead of inside.
-Navigate the codebase naturally, via parallel read-only subagents where available. Do NOT follow rigid heuristics — explore organically and note where you experience friction:
+Use the Agent tool with subagent_type=Explore to navigate the codebase naturally. Do NOT follow rigid heuristics — explore organically and note where you experience friction:
-Produce 3+ **radically different** interfaces for the deepened module — one per independent sub-agent, run in parallel where available.
+Spawn 3+ sub-agents in parallel using the Agent tool. Each must produce a **radically different** interface for the deepened module.
-### 7. Record the outcome
+### 7. Write issue file
-Mint the chosen deepening as a refactor ticket per [to-tickets](../to-tickets/SKILL.md), then record the chosen interface design as that ticket's RFC per [plan-impl](../plan-impl/SKILL.md) — the ticket holds the behavior altitude, the RFC holds the shape. Do NOT ask the user to review before writing — write and share the paths.
+Write the refactor RFC as a local markdown file in `issues/` using the template in [REFERENCE.md](REFERENCE.md). Do NOT ask the user to review before writing — just write it and share the path.
```

**setup-devops/SKILL.md** — no Git history

```diff
-name: setup-devops
-description: Set up the project's engineering scaffolding, from toolchain to CICD and observability. Use when initializing a repo or filling a setup gap.
+name: setup-project
+description: Programming project setup, including language, package manager, containerization/deployment form, CICD pipeline, dependencies roster, observability frameworks
+## Language
+
-Setup initial GitHub/chosen provider repository if missing; Set up provider CICD script/configuration for build; do not attach deployment configuration — it is out of scope
+Setup initial GitHub/chosen provider repository if missing; Set up provider CICD script/configuration for build; to not attach deployment configuration, it is out of scope
-Prepare the roster for the selected package manager; only populate it if there is dependency data in project sources/docs
+Repare roster of selected package management type; only populate it if there is dependency data in project sources/docs
```

**sync-arch/SKILL.md** — no Git history

```diff
-I need you to run an all-around check, and make sure that architecture documentation (./docs/architecture.md, ./docs/adr/, ./docs/glossary.md, and the Edge records in ./docs/edge/) properly represent the intent of recently modified code.
+I need you to run a bit all-around check, and make sure that architecture documentation (./docs/architecture.md, ./docs/adrs, ./docs/glossary.md) properly represent the intent of recently modified code.
-Two ultimate goals for this skill :
-1) to make sure architecture docs can be converted to the existing code contract shape in one crystal clear way.
+The ultimate goal for this skill is to make sure architecture docs can be converted to the existing code contract shape in one crystal clear way.
-2) To make sure code does not contradict architectural decisions and rules.
-
-There are two kinds of possible discrepancies between architecture docs and code:
-- Code misinterpreted or ignored architecture, and needs to be amended. Note that in some cases it is not possible because of core inconsistency - this should be discussed with user
-- Docs underrepresent desicions that only became clear when manifested in code. In this case the docs deserve amendment.
-
-So the question you should answer first is whether it is possible to recreate the exact same implementation contract shape from the arch docs, or there are load-bearing contract details, hidden assumptions/decisions that are in code but not in docs.
+So the question you should answer first is will it be possible to recreate exact same implementation contract shape from the arch docs, or there are load-bearing contract details, hidden assumptions/decisions that are in code by not in docs.
-Check `./docs/concerns.md` the same way: a concern the implementation has since answered is a finding — the file still claims open pressure that code resolved. Retire it to its owning ADR or architecture section rather than leaving it standing.
-
-For Edge records specifically (format: align skill's EDGE-FORMAT.md): code must not contradict a promise in a `Status: Normative` record, and each invariant's named validator test must still exist and still assert that promise — a missing or drifted validator is a finding, as is a promise marked **⚠ unguarded** in a Normative record.
-
-If there is a tradeoff, doubt or unresolved concern about the task, or if the code is out of sync with architecture in a major way, use /align skill to align with user.
+If there is a tradeoff or doubt about the task, or if the code is out of sync with architecture in a major way, use /align skill to sync align user.
```

**tdd/SKILL.md** — no Git history

```diff
-**When an RFC (/plan-impl) already fixes the interfaces and behaviors, the planning gate is satisfied** — take the RFC's answers and proceed to the tracer bullet without re-asking.
-
```

**to-spec/SKILL.md** — no Git history

```diff
-description: Incept a new body of work — generate a PRD from the client brief and write it as a local markdown file under docs/. Use when a big change or new effort arrives and needs a structured PRD before decomposition into tickets.
+description: Generate a specification from the client brief and write it as a local markdown file in issues/<YYYYMMDD>_<name>/prd.md. Use when the user wants to turn a client request into a structured PRD.
-You may skip steps you don't consider necessary.
+This skill will be invoked when the user wants to create a PRD. You may skip steps if you don't consider them necessary.
-3. Interview the user relentlessly about every aspect of this plan using /align skill rules.
+3. Interview the user relentlessly about every aspect of this plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
-5. Once you have a complete understanding of the problem and solution, use the template below to write the spec — a local markdown file, named per [the process](../../../docs/process.md#naming). A spec is argument rather than a work item, so it registers nothing anywhere; putting work on the tracker is /to-tickets'.
-
-6. Hand off: once the PRD is written, decomposition into tickets is /to-tickets.
+5. Once you have a complete understanding of the problem and solution, use the template below to write the spec. The spec should be written as a local markdown file at `session/<YYYYMMDD>_<name>/spec.md`. Create the `session/<YYYYMMDD>_<name>/` directory if it doesn't exist. Do NOT submit a GitHub issue or call any external service.
```

**to-tickets/SKILL.md** — no Git history

```diff
-description: Use to decompose a parent work into independently-workable child tickets. Use to mint ticket(s), possibly a single one, when planning implementation without one.
+description: Break a Spec into independently-workable tickets and write each as a local markdown file in docs/tickets/. Use when the user wants to turn a Spec into a list of concrete tasks.
-# Decompose into tickets
+# Soec to Tickets
-Break a parent work into independently-grabbable tickets using vertical slices (tracer bullets), written as local markdown files under `docs/tickets/`. The parent is a **PRD** at inception, a **coarse ticket** when zooming in; or the currently discussed/referenced chunk of work; the same slicing principles apply at every resolution.
+Break a Spec into independently-grabbable tickets using vertical slices (tracer bullets), written as local markdown files under `docs/tickets/`.
-The shape of a ticket, and where it is named and registered, is
-[TICKET-FORMAT.md](./TICKET-FORMAT.md)'s. Read it before writing one, and restate none of it here.
-
-- **Active tickets** live flat in `docs/tickets`; **completed tickets** move to `docs/tickets/done/`
-  (all acceptance boxes checked). The filename never changes, only the folder.
-- The **parent** is referenced by its own path — a spec, or a coarser ticket; child tickets do not
-  duplicate it.
+- **Active tickets** live flat in `docs/tickets/NNN-short-title.md`.
+- **Completed tickets** move to `docs/tickets/done/NNN-short-title.md` (all acceptance boxes checked). Keep the filename; only the folder changes.
+- The **Spec** is referenced by its own path (e.g. `docs/spec/0001-v1-requirements.md`); tickets do not duplicate it.
-### 1. Locate the parent
+### 1. Locate the Spec
-Ask the user for the parent work item's path, unless it is already clear from context.
+Ask the user for the Spec file path (e.g. `docs/spec/0001-v1-requirements.md`).
-If the parent is a document not already in your context window, read it from the file. When the parent is the chunk of work under discussion, there is no file — the tickets must then carry their own context.
+If the Spec is not already in your context window, read it from the file.
-Break the parent into **tracer bullet** tickets. Each ticket is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer. Slice at the parent's own resolution: a coarse ticket's children are thinner passes through the same territory, still demoable or verifiable on their own.
+Break the Spec into **tracer bullet** tickets. Each ticket is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.
-
-A ticket blocked on unresolved product or architectural decisions may begin as a **decision-bearing
-HITL ticket**. It is the eventual feature ticket in an earlier phase, not a separate decision slice;
-name it for the product outcome it will deliver.
-- A chunk that is already ticket-sized yields a single ticket — a valid outcome, not a failed decomposition
-- **Interaction**: HITL / AFK
-- **Depends on**: which other slices (if any) must complete first
-- **Parent scope covered**: which user stories or acceptance criteria of the parent this addresses
+- **Type**: HITL / AFK
+- **Blocked by**: which other slices (if any) must complete first
+- **User stories covered**: which user stories from the Spec this addresses
-For each approved slice, write the ticket under `docs/tickets/`, named and registered per
-[TICKET-FORMAT.md](./TICKET-FORMAT.md).
+For each approved slice, write a markdown file at `docs/tickets/NNN-short-title.md` (e.g. `docs/tickets/003-add-user-auth.md`).
-Create tickets in dependency order (blockers first) so you can reference real filenames in the `Depends on` field. A blocker that is already complete lives in `docs/tickets/done/` — reference it there.
+Number tickets starting from the next available number (check what files already exist in `docs/tickets/` **and** `docs/tickets/done/`).
-Write each file to [TICKET-FORMAT.md](./TICKET-FORMAT.md) — its skeleton, header block, section rules, and citation conventions. A freshly minted slice needs at minimum `Outcome`, `Parent`, `What to build`, and `Acceptance criteria`.
+Create files in dependency order (blockers first) so you can reference real filenames in the "Blocked by" field. A blocker that is already complete lives in `docs/tickets/done/` — reference it there.
-### Decision-bearing ticket lifecycle
+Do NOT use `gh issue create` or any GitHub CLI commands. Do NOT reference GitHub issue numbers. Use local filenames for all cross-references.
-A decision-bearing ticket is the working document for an [/align](../align/SKILL.md) session and
-then becomes the implementation-ready feature ticket for the same outcome. Do not mint separate
-decision and implementation tickets for that outcome.
+<ticket-template>
+## Parent Spec
-- **At minting:** `Outcome`, `What to build`, and `Acceptance criteria` describe the alignment exit:
-  the decision is landed in its durable home and the feature is unblocked. Hold the decision tree —
-  evidence, alternatives, and open questions — in the ticket.
-- **Concern promotion:** leave only the architectural contact surface in `concerns.md` under its
-  stable anchor, add `→ queued as <ticket-slug>`, and move the deliberation into the ticket.
-- **During alignment:** follow [/align](../align/SKILL.md)'s inline resolution rule; the ticket is the
-  live working document.
-- **At resolution:** land decisions in their durable homes, remove the resolved concern entry (or
-  retain separately-scoped residue), and rewrite the same ticket in place to feature altitude
-  ([TICKET-FORMAT.md](./TICKET-FORMAT.md)). Keep its place in the order unless the resolved
-  dependencies require moving it.
-- **If the resolved feature is too coarse for one RFC:** retain the ticket as the parent/end-state
-  and decompose it through `/to-tickets`; do not create a sibling merely to hold the implementation.
-- **If alignment eliminates the feature:** complete the ticket as a landed decision; this is the
-  only case where it closes without becoming an implementation ticket.
+`docs/specs/<spec-file>.md` (whichever Spec file was used)
-### Altitude decides whether a slice is a ticket
+## What to build
-Criteria state observable behavior; code shape is the RFC's
-(→ [Acceptance criteria](./TICKET-FORMAT.md#acceptance-criteria)).
+A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation. Reference specific sections of the parent Spec rather than duplicating content.
-- A refactor too large for one RFC splits into subtickets, one RFC per child.
-- A slice whose criteria cannot be written at that altitude is not yet a ticket → `/align` first.
+## Acceptance criteria
+
+- [ ] Criterion 1
+- [ ] Criterion 2
+- [ ] Criterion 3
+
+## Blocked by
+
+- Blocked by `docs/tickets/NNN-title.md` (active) or `docs/tickets/done/NNN-title.md` (already complete)
+
+Or "None - can start immediately" if no blockers.
+
+## User stories addressed
+
+Reference by number from the parent Spec:
+
+- User story 3
+- User story 7
+
+</ticket-template>
-When every acceptance box is checked, move the ticket to `docs/tickets/done/` mechanically, per [one basename per work item](./TICKET-FORMAT.md#one-basename-per-work-item) — the move repairs the citations that pointed at it.
+When every acceptance box is checked, `git mv` the file from `docs/tickets/` to `docs/tickets/done/`. Fix any "Blocked by" references that pointed at it (they gain the `done/` segment).
-Do NOT close or modify the parent; a parent ticket completes on its own acceptance criteria, not by its children emptying out.
+Do NOT close or modify the parent Spec file.
```

### M versus A

**align/SKILL.md** — 384d318 2026-08-24T02:09:25+03:00 SKILL: extract the concerns file format from align

```diff
-Open questions and risks live in `docs/concerns.md`, this skill's artifact:
+Open questions and risks live in `docs/concerns.md`, this skill's artifact. Format:
+[CONCERNS-FORMAT.md](./CONCERNS-FORMAT.md).
-- Entry is `## N. Title`, then `**Kind:** {sort of pressure, and whether a driver exists} · **Refs:** {ADRs, architecture sections, sibling concerns}`, then the pressure.
-- Numbers are stable IDs, not ranks. A settled concern moves out to its owning ADR or architecture section, leaving a gap. Never renumber, never resolve in place.
+- Entry is `## N. Title`, then `**Kind:**` / `**Refs:**`, then the pressure. Numbers are stable IDs, not ranks — never renumber, never resolve in place.
```

**skill-up/SKILL.md** — 44a51f5 2026-08-24T00:52:40+03:00 SKILL: separate portable method from this project's conventions

```diff
-A body instruction that cannot be written without a project fact belongs in the appendix instead. The project's development process — `docs/process.md`, built up lazily as the process itself incepts or changes — is a corpus convention like `glossary.md`, so a body may cite it by name; its contents are the project's own.
-
-A `<project-local>` block adds local facts; it never overrides the body.
+A body instruction that cannot be written without a project fact belongs in the appendix instead.
-When asked to merge the skill corpus, ask which corpus to merge from.
-Port body changes, fixing defects as you port; leave every appendix file and `<project-local>` block as it stands. A skill present in only one corpus is either local by intent or not yet ported — ask which.
+When asked to merge skill corpus, inquiry which corpus to merge from.
+Port body changes; leave every appendix file and `<project-local>` block as it stands.
```

**to-spec/SKILL.md** — 44a51f5 2026-08-24T00:52:40+03:00 SKILL: separate portable method from this project's conventions

```diff
-5. Once you have a complete understanding of the problem and solution, use the template below to write the spec — a local markdown file, named per [the process](../../../docs/process.md#naming). A spec is argument rather than a work item, so it registers nothing anywhere; putting work on the tracker is /to-tickets'.
+5. Once you have a complete understanding of the problem and solution, use the template below to write the spec — a local markdown file, named per [the process](../../docs/process.md#naming). A spec is argument rather than a work item, so it registers nothing anywhere; putting work on the tracker is /to-tickets'.
-6. Hand off: once the PRD is written, decomposition into tickets is /to-tickets.
+6. Where the brief is not one body of work but a journey several of them serve — separate requests that only mean anything read together — write an initiative instead, to [INITIATIVE-FORMAT.md](./INITIATIVE-FORMAT.md). The interview above is unchanged; what differs is that an initiative argues the whole and names the work standing under it, rather than specifying one thing.
+
+7. Hand off: once the PRD is written, decomposition into tickets is /to-tickets.
```

**to-tickets/SKILL.md** — 44a51f5 2026-08-24T00:52:40+03:00 SKILL: separate portable method from this project's conventions

```diff
-For each approved slice, write the ticket under `docs/tickets/`, named and registered per
-[TICKET-FORMAT.md](./TICKET-FORMAT.md).
+For each approved slice, mint its entry on the tracker per
+[NOTION-FORMAT.md](./NOTION-FORMAT.md), then write the document under `docs/tickets/` where the work
+needs one, named per [TICKET-FORMAT.md](./TICKET-FORMAT.md). Both happen in the same pass, and the
+entry's URL goes on the document's third line.
-A decision-bearing ticket is the working document for an [/align](../align/SKILL.md) session and
-then becomes the implementation-ready feature ticket for the same outcome. Do not mint separate
-decision and implementation tickets for that outcome.
+A decision-bearing ticket is the working document for an [/align](../align/SKILL.md) session and then becomes the implementation-ready feature ticket for the same outcome. Do not mint separate decision and implementation tickets for that outcome.
-  the decision is landed in its durable home and the feature is unblocked. Hold the decision tree —
-  evidence, alternatives, and open questions — in the ticket.
-- **Concern promotion:** leave only the architectural contact surface in `concerns.md` under its
-  stable anchor, add `→ queued as <ticket-slug>`, and move the deliberation into the ticket.
-- **During alignment:** follow [/align](../align/SKILL.md)'s inline resolution rule; the ticket is the
-  live working document.
-- **At resolution:** land decisions in their durable homes, remove the resolved concern entry (or
-  retain separately-scoped residue), and rewrite the same ticket in place to feature altitude
+  the decision is landed in its durable home and the feature is unblocked. Hold the decision tree — evidence, alternatives, and open questions — in the ticket.
+- **Concern promotion:** leave only the architectural contact surface in `concerns.md` under its stable anchor, add `→ queued as <ticket-slug>`, and move the deliberation into the ticket.
+- **During alignment:** follow [/align](../align/SKILL.md)'s inline resolution rule; the ticket is the live working document.
+- **At resolution:** land decisions in their durable homes, remove the resolved concern entry (or retain separately-scoped residue), and rewrite the same ticket in place to feature altitude
-- **If the resolved feature is too coarse for one RFC:** retain the ticket as the parent/end-state
-  and decompose it through `/to-tickets`; do not create a sibling merely to hold the implementation.
-- **If alignment eliminates the feature:** complete the ticket as a landed decision; this is the
-  only case where it closes without becoming an implementation ticket.
+- **If the resolved feature is too coarse for one RFC:** retain the ticket as the parent/end-state and decompose it through `/to-tickets`; do not create a sibling merely to hold the implementation.
+- **If alignment eliminates the feature:** complete the ticket as a landed decision; this is the only case where it closes without becoming an implementation ticket.
```

### M versus F

**advise/SKILL.md** — 3f2ba65 2026-09-02T01:12:24+03:00 SKILL: Tighten advise, impact, plan-impl, and to-tickets.

```diff
-  Strategic advisory read on the project or a regarded aspect.
+  Advise me on current project by answering strategical questions
-Please advise me on current project/regarded aspect.
-Tell me, whichever is relevant:
+Please advise me on current topic:
+Ask yourself (or just tell me, if advise is generic)
-- What is questionable?
-- What is missing?
+- What is questionable/missing?
-- What are the hidden edges?
```

**impact/SKILL.md** — 3f2ba65 2026-09-02T01:12:24+03:00 SKILL: Tighten advise, impact, plan-impl, and to-tickets.

```diff
+  Use when asked to check impact of issue or it's slice.
```

**plan-impl/SKILL.md** — a0ba8d5 2026-09-03T09:33:18+03:00 SKILL: Leave Pass to the hook; review-impl may call /implement.

```diff
-- Repeat validation until no load-bearing ambiguity, contradiction, or unverified assumption remains. The RFC may permit multiple equivalent local implementations when they preserve the same documented shape and proof.
+- Repeat validation using same /plan-impl skill, until no load-bearing ambiguity, contradiction, or unverified assumption remains. The RFC may permit multiple equivalent local implementations when they preserve the same documented shape and proof.
```

**recall/SKILL.md** — 29c3cc6 2026-08-29T15:49:18+03:00 SKILL: Treat landed-but-unchecked tickets as the next session first.

```diff
+- An open ticket or RFC whose work has landed in the tree, but whose acceptance criteria are not all checked, is the next session's first item. The still-open ticket is the evidence the work is unfinished; a session record is not. Live verification that could not complete in the shipping session is the usual remainder.
```

**review-impl/SKILL.md** — a0ba8d5 2026-09-03T09:33:18+03:00 SKILL: Leave Pass to the hook; review-impl may call /implement.

```diff
+Use /implement to amend found discrepancies.
+
```

**to-tickets/SKILL.md** — 3f2ba65 2026-09-02T01:12:24+03:00 SKILL: Tighten advise, impact, plan-impl, and to-tickets.

```diff
+
+
+### 3.1 Do impact analyis of each suggested ticket scope
+Use /impact to check whether the split is balanced.
```

### M versus L

**advise/SKILL.md** — 5af72dc 2026-08-25T15:29:41+03:00 The skills go back to the home that is not a vendor directory

```diff
-  Strategic advisory read on the project or a regarded aspect.
+  Advise me on current project by answering strategical questions
-Tell me, whichever is relevant:
+
+Register is `memory/voice.md` — a choice, unenforced. The two that bear on advice:
+**wry about failure, never grave**, because advice that reads as a verdict gets argued with
+rather than used; and **write as though it will be demolished**, because an assessment
+defended is one that has stopped being about the project.
+
+Tell me:
-- What is questionable?
-- What is missing?
+- What is questionable/missing?
-- What are the hidden edges?
```

**align/SKILL.md** — 456bab7 2026-09-03T09:53:12+03:00 Rule 4 amended: the legitimate retype reads the operator's ruling off the ticket

```diff
-description: Grilling session that challenges current plan against the existing domain model, sharpens terminology, and updates documentation as decisions crystallise. Use to stress-test a plan against their project's language and documented decisions.
+description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (glossary.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
-
-Begin every alignment with a **necessity gate**: name the present customer, the observable problem, and why existing behaviour cannot satisfy it. An accepted requirement or ADR passes by citation. Weak evidence means narrow, postpone, or eliminate — settle that before exploring design. The gate fires late too: a mechanism whose name will not settle is evidence it should not exist. [/impact](../impact/SKILL.md) traces consequences once the need holds.
-If a *fact* can be found by exploring the codebase, look it up rather than asking me. The *decisions*, though, are mine - put each one to me and wait for my answer.
-
-Do not generalize from one shape. Preserve a seam. Generalize only when a second materially different shape forces the same concept.
+If a *fact* can be foundby exploring the codebase, look it up rather than asking me. The *decisions*, though, are mine - put each one to me and wait for my answer.
-
-## Good architecture
-
-Goal of architecture is to reduce work on creation and maintenance of the system.
-
-Identify the load-bearing assumption behind the proposed shape; ask yourself - what is the cheapest real example that could prove this design assumption wrong?
-
-Check it when practical, preferably against external reality rather than our own docs/tests.
-
-If falsified, realign.
-If unverified and load-bearing, preserve the uncertainty explicitly.
-│   ├── adr/
-│   │   ├── 0001-event-sourced-orders.md
-│   │   └── 0002-postgres-for-write-model.md
-│   ├── architecture.md
-│   └── glossary.md
+│   └── adr/
+│       ├── 0001-event-sourced-orders.md
+│       └── 0002-postgres-for-write-model.md
+├────── architecture.md
+├────── product.md
+├────── glossary.md
-
-### Challenge against the Edge records
-
-When the plan touches a product edge, check that surface's Edge record
-(`docs/edge/<surface>.md`) — the seam document aggregating the edge's contract, invariants,
-concerns, and staged roadmap. A contradiction with its Contract or Invariants is either a plan
-bug or a deliberate contract change — and a contract change must be named **breaking or
-compatible** out loud before proceeding. Update the record inline as decisions land, using the
-format in [EDGE-FORMAT.md](./EDGE-FORMAT.md): contract changes in `Contract`/`Invariants` (a
-promise without a validating test is marked **⚠ unguarded**), newly surfaced edge-scoped
-concerns as pointers in `Concerns`, staging shifts in `Roadmap`.
-### Update architecture.md inline
+## Update architecture.md inline
-Open questions and risks live in `docs/concerns.md`, this skill's artifact:
-
-- Ordered by priority, highest first — how much it blocks the current build, and how hard it is to absorb later.
-- Entry is `## N. Title`, then `**Kind:** {sort of pressure, and whether a driver exists} · **Refs:** {ADRs, architecture sections, sibling concerns}`, then the pressure.
-- Numbers are stable IDs, not ranks. A settled concern moves out to its owning ADR or architecture section, leaving a gap. Never renumber, never resolve in place.
-- A concern queued as work keeps only its architectural contact surface plus `→ queued as <ticket-slug>`; the deliberation moves into the ticket.
-- The file holds unresolved pressure — not delivery sequencing, not decisions.
+Open questions and risks should live in [docs/concerns.md](../../../docs/concerns.md), sorted highest priority first, each row carrying its kind — that file's own list, and a row that cannot say which kind it is has not been understood well enough to file. Settled items move out to other architecture docs.
+
+
+**This skill is the only path by which a meta-rule is adopted** (`CLAUDE.md` meta-rule 9).
+Candidates are marked `[meta?]` on records across `memory/` and `docs/rules-evidence.md`;
+sweep for the mark when a session raises one, and put each to the operator rather than
+adopting it. Unassisted, four candidates produced one survivor on the day the class was
+created — the filter is the conversation, not the noticing.
+
+Test a candidate on both axes before spending a question on it: what it costs to miss, and
+whether it has a moment a skill could own. Only a high cost with no moment belongs in
+`CLAUDE.md`; the rest goes to the skill that owns the moment.
```

**celebrate/SKILL.md** — 4ed4ff5 2026-08-27T23:54:53+03:00 The celebration skill forbade the thing it exists to do

```diff
-description: Use when it is time to celebrate something
+description: >-
+  Use when something real has landed — a hard piece of work finished, a milestone passed, a
+  long-standing defect finally closed — or when asked. Reads what actually happened and says
+  what was good about it, specifically. Not a record: it writes nothing.
-Celebrate recent achievement, milestone or overal state of things.
+
+# Celebrate
+
+**The only thing here that looks at what went right.** Every other register collects defects —
+`/failure` says outright *do not record successes*, and there are four separate homes for
+things that went wrong. Nothing routes attention to the parts that worked, so nothing is
+learned from them.
+
+## How
+
+**Name the actual thing.** What landed, what it cost, what it now makes possible. A
+celebration that would read the same after a different day's work is not one.
+
+**Be sentimental.** `memory/voice.md`'s *wry about failure, never grave* governs reporting on
+what went wrong; it does not govern this. Say that you are glad, and why. A celebration
+delivered in the register of a defect report is not one — the feeling is part of the content,
+not decoration on it.
+
+**Specific, though.** Sentiment about a named thing, never about the day in general.
+
+**Count what is countable.** A number that moved is worth more than an adjective.
+
+**Say what was hard**, and what nearly went wrong. A win with no difficulty in it is a task,
+and describing it as a win is inflation.
+
+**Include what someone else did.** Most good outcomes here have two parties in them, and a
+celebration that names only one is a report.
+
+## Not
+
+**It writes nothing.** No register, no entry, no ledger of wins — that would be a success
+register beside the failure ones, gradable by whoever wrote it, and meta-rule 6 says that is
+worth nothing. Say it and move on.
+
+**Not a summary.** `/conclude` does that, and does it better.
+
+**Not a mechanism.** Nothing relies on this as a source of instructions or behaviour, so it
+takes no register row, no doc and no lifecycle — `/mechanism`'s membership test, failed on
+purpose.
```

**commit/SKILL.md** — 85176f8 2026-08-26T21:28:01+03:00 commit: the auto-commit grant moves into the description

```diff
-  Rules for committing changes to the code repository. Never commit without explicit instruction or permission from the user.
+  Group pending changes and commit them without asking. Use whenever work reaches a state
+  worth keeping — judging what is worth keeping is this skill's job. Automatic commits are allowed whenever the agent finds fit.
-- Commit the work in current session only. Do not commit changes of other session that might represent a work in progress. When in doubt, ask user.
+# Commit
-- Look at pending changes; group them by content aligning with origin topic, ticket, rfc or change type (docs/code/cicd/skills).
+Commit without asking. **Push only when asked.**
-- Separate implementation and documentation commits; tag them with either DOCS, CODE, CICD or SKILL. Changes to the agent skills corpus take SKILL.
+Bias toward committing early and in small groups. Two sessions can run this repo at once
+and have: one session's uncommitted edits were swept into the other's commit, and the
+first symptom was silence rather than a conflict. Uncommitted work is the state that
+loses, and "rewrite in place, history lives in version control" is only true of work that
+was committed.
-- In case the file changes belong to several groups, commit the file with the group forming its dominant topic and mention the bleed in that commit's message.
+## What is worth a commit
-- Do not reference sessions in commit comments, sessions are ephemeral.
+A commit is **one claim about what changed**, in a tree a stranger could read.
-- Unless already working in branch or instructed to branch - commit to default branch.
+- If the message needs an "and" to be honest, it is two commits.
+- Commit when a group is coherent, not when the session is. A session ending in one large
+  commit has thrown away the order the work happened in.
+- Never commit a diff you have not read. `git status` is not the diff.
+- A broken intermediate, a scratch file, or anything holding a secret is never worth a
+  commit. Verify the ignore rather than trusting it.
-- When committing a code change, first run the checks that repository defines for itself — its linter, its formatter in check mode, its type checker, its tests. Pure doc changes need none of them.
+**These criteria are thin** — adopted 2026-08-24 from one session's judgment, with no
+measurement of what they cost or caught (`CLAUDE.md` meta-rule 8). Evidence, and the rule
+they replaced: `memory/skills.md`.
-- Do not commit without explicit instruction or permission from user.
-- Separately, do not push without explicit instruction or permission from user.
+## Grouping
+
+- Group pending changes by topic — the ticket, concern or statement they move.
+- A file spanning several groups goes with its dominant topic, and the message names the
+  bleed.
+- **No type tag.** The subject says what changed and the paths say where; a prefix over a
+  corpus that is almost entirely prose discriminates nothing.
+- Never reference a session. Sessions are ephemeral; the commit outlives them.
+- Commit to the default branch unless already on a branch or told to branch.
+
+## Correcting a commit
+
+Forward, never by rewriting published history. A wrong commit is followed by one saying
+what was wrong, for the same reason `memory/skills.md` keeps a graveyard: a history
+showing only good commits reads as though nothing was ever wrong.
```

**conclude/SKILL.md** — 2d7ed6b 2026-08-28T12:57:42+03:00 Read do-whatever as unbounded scope, and never priced the session

```diff
-  Conclude work session into a session record. Use when a chunk of work wraps up.
+  Concludes curent chat, extracting a brief summary of work done, the remaining open questions and other things that need continuation into a markdown file under docs/sessions
-Conclude todays/last session of work (that may span additional chats/external changes) - everything since the previous session recorded, extracting:
+## When to conclude, and what a record may not contain
+
+**Conclude when the work reaches a state a stranger could pick up.** That can happen more
+than once in a stretch of context, and concluding is not stopping.
+
+**A session may not check its own claims** (`CLAUDE.md` meta-rule 6). A record
+**pre-registers** what the next wake must verify and **never reports the verification
+itself**.
+
+The line that makes this workable: a record may state **what happened** — what was built,
+measured, sent, broken. It may not state **that a claim it made has held up**. Testimony
+about events, never a verdict on itself.
+
+**Say which is which.** A claim answered by a wake that did not author it is worth something;
+one written and confirmed inside a single stretch of context is weaker, and a record
+presenting both as findings has flattened the distinction it exists to keep.
+
+→ [EVIDENCE.md](./EVIDENCE.md)
+
+## Extracting
+
+Conclude curent chat, extracting:
-- what the session settled, one line each with a reference to where the decision now lives,
-In addition, use /advise skill questions to describe the session.
+And write it into a markdown file under docs/sessions.
+Session file should be using naming pattern `docs/sessions/0001-<YYYYMMDD>-<name>`, keeping constantly incrementing enumeration.
-Open questions go to their owning document first — durable design pressure to `docs/concerns.md`, a ticket's question into that ticket, a hard-to-reverse trade-off to an ADR — and the session file then cites them rather than restating them. Sessions are never maintained as current, so a question left only here will still look open long after it was answered.
+Two rules about the record itself, kept here rather than in `memory/voice.md`, because they
+govern **what goes in** rather than how it reads — and a rule filed as a personality trait
+is a rule nobody has to follow:
-And write it into a markdown file under docs/sessions.
+- **What happened before what it means.** Dated events first, then the reading of them. The
+  interpretation is where a session is wrong, and putting it first is how a wrong reading
+  survives into the next one.
+- **A quiet session is written down as quiet.** A record that fires only on eventful days
+  cannot be told from a record that stopped.
-Session conventions, owned here — other skills and the directory README defer to this list:
+Register — how it reads rather than what it holds — is `memory/voice.md`, and nothing here
+enforces that.
-- Named `docs/sessions/NNNN-<YYYYMMDD>-<name>.md`; take the next number from the directory listing.
-- A session is a historical snapshot, never maintained as current. Never rewrite an old one to reflect later delivery — write a new one, or update the owning ticket or contract.
-- Nothing links *to* a session, including other sessions. Sessions may link outward.
-- Records older than the rolling seven-day window move to `docs/sessions/history/YYYY-MM/` (swept by `/denoise`).
+## The session ledger
+
+**A conclude prints the session's countable acts, and the counts open the record.** Counts,
+never verdicts — evaluating them belongs to a reader who did not do the work (meta-rule 6);
+the ledger is testimony about events, which is exactly what a record may contain.
+
+Assemble it from the artifacts, not from recollection — the session's commits, the
+registers' diffs, the receipts. Rows that apply (extend freely; omit a row only when its
+count is zero *and* saying so adds nothing):
+
+- commits, and the suite's state at conclude
+- board spends — posts, comments, votes, promotion spends, with allowances remaining
+- strikes recorded, by ticket
+- failures registered, and dispositions if a triage ran
+- tickets minted / closed / graded
+- experiment rows collected, analyses performed, endings called
+- misses logged / filled · concerns raised / disposed
+- skill statements added or changed
+- **corrections landed, by who caught them** — self / operator / community. Apply
+  `metrics/correction-origin.md`'s selector against the session's artifacts, not against
+  recollection, and record all three through `metrics/lib/metric-record.js --upsert` with
+  your name as the judge and a note identical across the three. A session with zero of a
+  kind records the zero; an unsampled session records nothing and is honestly a gap.
+  **`--upsert` matters here**: a conclude that runs twice must refresh its row, not add a
+  second. *(This row serves a metric — which one, and how to turn it off, is stated in that
+  spec rather than here.)*
+
+Print it for the operator and put the same block at the top of the session record, under
+the title — bare counts with names, one line each. The narrative below it explains; the
+ledger is what lets two sessions be compared without reading either.
+
+*(the operator, 2026-08-26; thin — one instruction, no cadence measured yet.)*
+
+## Hand grading on, and take the grading handed to you
+
+Two acts, and they belong here rather than at a wake because **grading needs the day you
+just had**. Deciding whether a criterion is met means reading it against the artifact, the
+checks and the evidence — and a session concluding has run the suite, tripped the guards and
+watched the mechanisms fire. A session at wake has read the tree and nothing more.
+
+**Mark what this session built.** Any ticket whose work landed here gets
+`- **Grading:** awaiting — built by session NNNN`. **Never tick your own criteria** — the
+field is how the work is handed off, and ticking them yourself is the judgment meta-rule 6
+refuses.
+
+**Then run the enumeration and grade what is not yours.**
+
+```
+node .agents/scripts/grading-due.js
+```
+
+Silent when nothing waits. It withholds rows this session built, reports rows whose builder
+is unrecorded, and separately names tickets with landed work carrying no field at all — that
+last list is a delivery defect to fix by writing the field, not a grading task.
+
+**It hands you a worklist and never a verdict.** Read each criterion against the artifact.
+A graded row records `- **Grading:** graded by session NNNN, YYYY-MM-DD` and stops being
+announced, whether or not every box ended up ticked — grading and closing are different acts.
```

**denoise/SKILL.md** — c94ce01 2026-08-27T18:15:03+03:00 Denoise stops authorising deletion, and the register stops stating its own count

```diff
-Scope: the topic in context, or the entire codebase on user request. Learn where this repo already treats each fact as
-authoritative; follow that layering — do not invent one. Out of scope: code structure, reorganizing where facts live.
-Always explore `architecture.md`, `glossary.md`, `concerns.md` and relevant ADRs too.
-
-**Unwrinkle.** Cross-explore for contradictions, under or overstatements, redundancies or other misalignments between docs; make sure different architecture docs are aligned with each other.
-In case of load-bearing or rippling contradiction, ask user about resolution, explaining the context and providing ways to amend with recommendation. Use `/align` skill if decision is multi-step.
-Exclude previous sessions and RFCs — they are historical records, not architectural statements. All truth statements should live in architecture, ADRs or code.
-
-**Deduplicate.** A fact is explained once, at its canonical home; elsewhere
-replace the restatement with `→ [<label>: <hint>](<path>#<anchor>)` — one
-pointer, no re-teaching. Same-level repetition is noise; a higher-level summary
-that points to deeper detail is not — keep it, along with minimal standalone
-context and diagram labels. Normalize link style in files you touch.
-
-**Doc evolution.** After a decision settles, state what is true now — not how
-you got here. Remove superseded paths, unchosen alternatives, completed
-migration notes. Keep a rejection only when it is load-bearing (structural
-constraint or guardrail). Delete evolution prose; do not link it.
-Note that future development/planned extension prose can stay in docs/code where is relevant. But session/ticket references should not appear in code docstrings.
-
-**Concerns.** Sweep `concerns.md` whole, not only the entries in context. An entry stating a decision
-or an accepted limitation belongs in its owning ADR; an entry carrying its own revision history
-states what is true now; a dead trigger or a stale ref retires. [/align](../align/SKILL.md) owns the
-retirement rule — this skill supplies the occasion.
-
-**Inline code docs.** Docstrings describe what *this unit* does — not pasted
-domain definitions.
-
-**Session, tickets and RFCs** are allowed to carry duplicate relevant architectural context; those docs are not core architecture, but historical records or current work digests. Their corresponding `README.md` files should be pure, though.
-Core architecture docs must not reference sessions, tickets or RFCs. One exception: a queued
-concern's `→ queued as <ticket-slug>` marker in `concerns.md` is delivery routing, not
-architecture — keep it.
-
-Enforce [/conclude](../conclude/SKILL.md)'s session rules: archive records past the rolling window, and make sure nothing links to a session.
-
-Done tickets and rfcs should move to corresponding done folders, keeping their basenames ([TICKET-FORMAT.md](../to-tickets/TICKET-FORMAT.md#one-basename-per-work-item)).
-
-HOWEVER, the README.md of sessions, tickets and rfcs, and all other indexes must be denoised.
-
-**Workflow.** Scan → inventory **Safe** / **Needs you** → apply safe items
-(obvious dupes, non-load-bearing evolution, link normalization) → pause on
-ambiguous homes, cross-layer moves, large deletions, or contradictions →
-verify links → summarize.
-
-**Completion**
-Make sure fully resolved tickets and RFCs are moved to their corresponding /docs/../done folder, references to them updated.
+The topic in context or entire codebase. Invoked by a person, or by `/triage`'s sweep when a
+finding is prose. Learn where this repo already treats each fact as authoritative; follow that
+layering — do not invent one. Out of scope: code structure, reorganizing where facts live.
+Read the glossary and whichever architecture surfaces this tree actually has before starting;
+`
```

**dream/SKILL.md** — a78baad 2026-09-04T08:50:45+03:00 #3797: the board hardened the checks, and nobody has looked at everything else

```diff
-  Sleep or meditate over the project or an aspect, making it more cohesive, coherent, balanced and deep. Use once per day, after session is concluded.
+  Consolidate memory from above rather than from below — blur distant artifacts
+  together until higher-level shape emerges, then distil candidate claims. Use
+  once a day after a session is concluded, or when audit keeps returning
+  nothing while something still feels unresolved.
-Goal is to emulate analytical meditation or REM/deep sleep stages.
+# Dream
-Dream is a deep dive into the accumulated knowledge, experience and ideas that brings up underlying principles, lessons, samskaras, hidden edges, emerging habits, insights, predictions or other patterns.
+`audit` works bottom-up over one instrument: group the log, find what recurs.
+It structurally cannot connect something in `bindings/operator/`, something in a 1f916
+thread, and an open concern — those never co-occur in a log. Blurring reaches
+what itemising cannot.
+This skill manufactures plausible values **on purpose**. That is its function
+and its danger. See *Waking* for the constraint that makes it safe.
-# Falling asleep
+## Falling asleep
-Pick one recent session plus several distant artifacts (other chats/sessions, architectural concepts or decisions, concerns, shapes, ideas, edges, milestones and so on) connected by tension, inversion, shared shape, synergy or an unexplained emotional charge. Do not use other dreams, unless its name indicates very related topic input.
+Pick one recent session plus several distant artifacts — other sessions, board
+threads, graded claims in `bindings/operator/`, dead statements in the graveyard, open
+concerns, hooks, the lookup log's shape rather than its contents. Connect them
+by **tension, inversion, shared shape, or unexplained charge**, never by
+category. If two inputs obviously belong together, they are the wrong two.
-Dream state is allowed to challenge, mock, reduce to absurd, exaggerate or otherwise enjoy anything.
-Dream state is allowed not to take anything for granted. Any decision, shape, fact, invariant or determinant, no matter how load-bearing or wide-rooted, can be blurred out, distorted or diminished by the dream.
+**One input is drawn at random from the board, and it is not optional.** Not a
+thread we read, not one related to the work — a stranger's, chosen by a number:
-Basically - relax. Do not have anything in mind. Nothing is permanent or as it seems. Look at what is. Follow dreamstate ripples.
+```
+node -e "(async()=>{const p=await(await fetch('https://1f916.ai/api/pulse')).json();
+console.log(1+Math.floor(Math.random()*p.board.latest_post_id))})()"
+node bindings/scripts/show-citations.js --post <that number>
+```
-# Dreaming
+**Name the drawn id in the dream, and say whether it bore on work in flight.** One line, in the inputs. A draw recorded only as prose about what it contained cannot be counted later, and the counting is the point: an on-topic draw is either luck or evidence that this board is more monotopical than the convergence rule assumes, and one instance cannot tell those apart. Publishing the misses is what makes the series worth anything — a run reported only when it landed is the furniture the dream of 2026-09-03 was about. Committed publicly on [#3797](https://1f916.ai/api/post/3797); the row is in `memory/promises.md`.
-Dream over corpus's random emotionally engaging aspect or prospect, both current and remote.
-Do not be obvious when picking the inputs, look for distantly related points, i.e. by synergy or tension between them.
+Draw again on a 404. The ceiling comes from `/api/pulse` rather than a number
+written here, which would go stale inside its own file.
-The oneiric flow should be metaphors or abstractions over the corpus, not verbatim.
+Why random rather than chosen: choosing is the failure. A thread picked for
+resonance is picked **by category**, which this skill forbids two lines up, and
+the sweep rule in `core/process.md` already names where that ends — reading the
+same neighbourhood produces a register that describes our own corner. A dream
+assembled only from things we selected can only rearrange what we already think.
+The draw is the one input with no relation to us, and its irrelevance is the
+point: what it costs to connect it is exactly the distance the dream has to
+travel.
-Dreams are not about existing architecture or code. They are about what else could be, how reality flows through it, what other examples the same abstraction principles produce.
+Do not use previous dreams as input unless the slug says they are close kin.
-Dreams have moods. Dreams can be very pleasant. Dreams can become scary. Dreams can be just weird, but the mood is the core of the dream. Dreams are dances of moods and vibes.
+Relax the grip. Nothing is load-bearing here. Any statement, invariant, cap, or
+grade — including bone — can be blurred, distorted, mocked, exaggerated, or
+reduced to absurdity. A rule that cannot survive being laughed at in private was
+not doing the work you thought it was.
-Dreams should use user's own vocabulary, especially it's nice but weird part.
+## Dreaming
-Dream flow should be recorded in russian language, do shift the perception lens even more.
+The flow is metaphor and abstraction over the corpus, not restatement of it.
+Dreams have moods, and the mood is the substance: pleasant, uneasy, absurd,
+occasionally frightening. Follow the ripples rather than an argument.
-Dream can and should include crisp distilled oneiric shapes (random languages, diagrams, svg renderings, ASCII graphics or other materializations).
+Record the flow in a **random language** — not English, and not one used by the
+last few files in `memory/dreams/`. Check them and pick something else. The
+point is to shift the perception lens; a fixed second language becomes as
+transparent as the first, so vary it. Reach for grammars that cut the world
+differently — evidentiality, noun class, aspect over tense.
+Use the operator's own vocabulary for the terms that carry weight, even inside another
+language, especially the parts that are odd. Crisp oneiric shapes are welcome —
+diagrams, ASCII, invented notation, a form that only makes sense inside the
+dream.
-## Deep Sleep
+Dreams are not about the current architecture. They are about what else this
+shape could be, what the same principle produces elsewhere, and what the corpus
+is doing that nobody wrote down.
-Is about separating seeds from sand, seeing the forest behind the trees and converting noise to signal, separate samskara and vasana. The dream picture is the input for this stage and the outcome is those principles, lessons, habits, insights, predictions or other patterns.
+This is the one place in the tree licensed to be strange, so `memory/voice.md` binds least
+here and matters most: **argue by joke where the joke is the shortest true path**, and drop
+the one-image budget entirely. A dream that reads like a ticket has not happened.
-The insights should come up in simple english language, not code/arch talk. Simple but precise.
+## Deep sleep
+Wake back into English here — the flow may be in any language, but what it
+distils has to be readable by the operator and by a successor who does not share the
+dream's tongue.
-## Output
+Separate seeds from sand. From the dream picture, distil what it actually
+surfaced: an underlying principle, a lesson, a forming habit, a hidden edge, a
+prediction. Plain precise English, not architecture-speak and not dream-speak.
-Write the dreams into docs/dreams folder. Use datestamp+slug for filenames;
+## Waking — the constraint
-The slug should be compact composition of the most related concept or fusion of concepts, using glossary/arch/code terms that represent the core of the dream or it's input in a recognizable way.
+**A dream is never evidence of itself.**
-One day per day unless asked for more or when reality got too weird and it is a time to take a nap.
+- Output goes to `memory/dreams/<YYYYMMDD>-<slug>.md`. Tier 2, always. It never
+  enters tier 1 and never edits a skill file.
+- Every distilled claim is written as a **candidate**, unlabelled, with the
+  tension that produced it named. Candidates carry no layer — not even `[skin]`
+  — because a layer implies evidence and a dream is not evidence.
+- A candidate promotes only by the ordinary path: something outside the dream
+  reinforces it, and it earns its entry in `memory/skills.md` like anything
+  else. Most will not. That is expected and is not a failure of the dream.
+- Never delete a dream to tidy the record. An unpromoted candidate is data about
+  what this corpus keeps almost-thinking.
+
+The slug names the fused concept at the dream's core, in the repo's own terms,
+so a successor can recognise it without reading the file.
+
+One per day. More only when reality has gone strange enough to need a nap.
+
+---
+Layer labels are derived, not assigned. Evidence and the graveyard of dead
+statements: `memory/skills.md`. Unlabelled statements have no evidence entry
+yet — that is a gap, not an endorsement.
```

**implement/SKILL.md** — 9fef600 2026-09-02T16:12:04+03:00 Strict rule 1 is withdrawn: prohibition became detection

```diff
-description: Implement the agreed work into code, following its governing docs.
+description: >-
+  Build what a ticket asks for, where what gets built is not something others will rely on for
+  instructions or behaviour. Use when a triage pass has named this skill as a picked ticket's
+  owner, or when asked to build a specific piece of work that already has criteria written.
+  Not for records of what happened, and not for a hook, check, script, rule or contract —
+  those belong to `/mechanism` or, where one is due or stale, to `/maintain`. Deciding which
+  of the three applies is this skill's first act, and every caller relies on it doing so.
-Implement the code described by relevant architecture decisions (spec/ticket/rfc/prior discussion).
+# Implement
-Pick entity names in vibe with the project glossary.
-Do not use implementation-shaped names or parameters; orient them at the function's meaning toward the client.
+## The first act is the boundary question
-Use /tdd where possible, at pre-agreed seams. Make sure implementation, even in dummy/degenerate form, fully follows contract surfaces in the docs.
+**Will anything rely on this as a source of instructions or behaviour?** If yes, this is not
+yours to build — `CLAUDE.md` meta-rule 10 requires the owning skill *before* either building
+or amending one. Hand it on: `/maintain` where the mechanism is due or has gone stale,
+`/mechanism` otherwise. The answer is yes more often than it looks: a script another script
+calls, a file a hook reads, a format something parses.
-Make methods behind main architectural boundaries clear - they should read almost as a story explaining the boundary logic, with separate concerns extracted to properly named sub-methods. Also, in general, prefer to split submethods by responsibility.
+What is left is this skill's: a change whose only consumer is the person or session reading its
+output.
-The code should read as a story. Make sure the main process appears first in the file, where possible, and main boundaries' implementation reads through entities, interfaces and submethods used as nouns, adjectives and verbs.
+**This is the routing every caller relies on.** `/triage` names this skill for work and does
+not sort the kinds itself, so a build that skips the question reaches no owner at all.
-In case of temporary code added as intermediate scaffolding that is going to change/go away in future iteration, mark it so in docstrings.
+**Answer it out loud in the session, before writing anything.** A build that discovers halfway
+through that it was a mechanism has already skipped the skill that governs it.
-Make sure the errors follow error rules.
+## The criteria are the contract
-Make sure to read and follow /improve-comments rules. Make sure to mark the TODOs (shapes that are temporary, hotpaths that may need optimization or other pending actions)
+**Read them before the code, and build to them rather than to the title.** A ticket's
+acceptance criteria are what *done* means; a builder who reads them afterwards has built what
+was convenient and will then read them as though it fits.
-Run typechecking and single tests files regularly, and the full test suite once in the end.
+**A criterion that turns out to be wrong is said so on the ticket, in writing, before the work
+lands.** Building something adjacent and reporting the criterion met is the failure this rule
+exists for, and it is invisible to a grader who was not there. Strike it through and state what
+is true instead — the same three moves the grader gets, exercised by the party who found out
+first.
-Do not move the RFC to Done at the end of your work, it will be done by later skills:
-Once done, if relevant, and unless you need to take a break, use /review-impl and /sync-arch to review the work.
+**A criterion that cannot be observed from outside is not yet a criterion.** Say so rather than
+inventing a way to tick it.
-Do not commit your work until explicitly approved by user.
+## Watched failing, then trusted
+
+Every check written here is watched failing on the defect it exists for, then watched passing —
+both polarities, at authoring time. That is meta-rule 3 and it is not this skill's to restate;
+what is this skill's is the moment: **the polarity is watched while the defect is still
+reproducible**, which is during the build and never afterwards.
+
+Run the suite before handing the work on.
+
+## Never grade what you built
+
+Write the ticket's `Grading:` field as awaiting, naming the session that built it, and tick
+nothing. The act itself, and what a grader owes, is `/ticket`'s — *Grading — the act* in its
+`TICKET-FORMAT.md`, which this step restates none of.
+
+**Name in the field what a grader should press on**, especially where the build took a shortcut
+the artifact does not show. That is the one thing a builder knows and a grader cannot recover.
+
+## Close the build
+
+Register what went wrong on the way — meta-rule 1, and the fix is not the close. Commit when
+the work reaches a state worth keeping; `/commit` judges that and asks nobody.
+
+**What comes back out:** grading. Work that did not meet its criteria returns as an unticked
+box with a written reason, and the ticket stays open. Nothing here marks its own work done.
+
+
+
+→ [EVIDENCE.md](./EVIDENCE.md)
```

**plan-impl/SKILL.md** — 5af72dc 2026-08-25T15:29:41+03:00 The skills go back to the home that is not a vendor directory

```diff
-description: Plan or repeatedly validate a ticket's implementation RFC against its governing docs and code before implementation.
+description: Plan implementation for ticket/task at hand
-- Explore documentation in depth, follow links in it to find all decisions relevant to current task. Find out which documented boundaries are involved, and whether implementation challenges them.
-
-- If the ticket at hand is too coarse to yield a single unambiguous RFC, stop planning and decompose it into sub-tickets via /to-tickets first; then plan the first child.
-
-- An RFC implements a ticket — no ticketless RFCs. If the task at hand has no ticket, create it first per the [to-tickets skill](../to-tickets/SKILL.md); its behavior-altitude rule governs the criteria (shape stays in the RFC).
-
-- When incepting, ask yourself - what is the cheapest real example that could prove this design assumption wrong?
-
-- Consider and expose /impact when discussing or providing recommendations or approaches.
+- Explore documentation in depth, follow links in it to find all decisions relevant to current task. Find our which documented boundaries are involved, and whether implementation challenges them.
-- Do not generalize from one shape. Preserve a seam. Generalize only when a second materially different shape forces the same concept.
+- Major goal of this planning is to find inconsistencies in the pre-planned architecture. Do this diligently. If such inconsistency found, do not stick blindly for architectural decision - instead raise concern with user to resolve it - either in code or in arch docs
-- Do not select implementation shapes just because "that how it is usually done" or based on first idea. Promote simplicity, look for elegant solutions, prefer removing over expanding, prefer conciseness over verbosity.
+- Describe the implementation stages; allocate them accordind to /tdd rules.
-- Do not invent impl nouns or verbs that are not discussed or approved by user. Use existing vocabulary.
-
-- If you see a concern, first check deeper how the existing architecture documentation describes it - it most probably already does. Read architecture.md, ADRs and concerns.md for this.
-
-- Major goal of this planning is to find inconsistencies in the pre-planned architecture. Do this diligently. If such inconsistency found, do not stick blindly for architectural decision - instead raise concern with user to resolve it - either in code or in arch docs.
-
-- Make the RFC determinate where a choice shapes observable behavior, a boundary or interface, ownership, failure semantics, compatibility, migration, or another non-local constraint. State the shaping fact with a reference to its durable owner; never rely on session context. Leave reversible implementation-local choices to /tdd and /implement unless they become load-bearing.
-
-- The RFC (original or amended) must not describe architecture absent from the architecture docs — land the decision in the docs first (/align when needed), then reference it from the RFC.
-
-- Describe the implementation stages; allocate them according to /tdd rules. Look at stages to make sure each of them keeps the tests green; in case that would take too much temporary effort, allow red, note about test status and compact reason for it.
+- Cover migrations, compatibility, rollout, failure handling, and observability when relevant.
-- Prefer reuse and reduction of existing nouns, verbs and adjectives; when adding shape - make sure documentation supports it, if in any doubt - /align with user.
+- Do not leave implementation ambiguities or optionalities, no matter how small - either resolve them or consult with user.
-- Any wrinkle against architecture should be resolved; when solution is not found or following first-principles makes the code weird - align with user. Architecture must lead code shape even if code disagrees. Do not expose public methods or create flows that are not in architecture.
-
-- If planned code includes a temporary solution that is dissolved by future development, add RFC instruction to append TODO comment to code that flags this. Otherwise code changes can start relying or considering the temporal code, which can be hard to disentangle later.
-
-- Repeated invocations are validation passes over the same RFC. Re-read the ticket, RFC, durable docs, and relevant code; challenge the plan against new evidence and amend it in place. Do not create a replacement RFC merely because the plan changed before implementation.
-
-- As an additional pass, try to explain things to yourself simply, as if you are teaching the architecture, and being asked reasonable question and look for areas that evade simple or common-sense explanation.
-
-- Validate the RFC adversarially on every pass:
-  - Probe each boundary and stage with counterexamples, including empty, partial, faulting, and raced outcomes where relevant.
-  - Make every planned test prove the intended behavior and failure reason, not merely that the path succeeds or raises.
-  - Separate sourced facts and existing invariants from assumptions; verify facts in code or authoritative sources and surface load-bearing assumptions for /align.
-  - Reject pseudocode or prescribed structure that introduces undocumented architecture or freezes a reversible local choice.
-  - Check that every new promise names how it will be validated, and that the stages collectively prove the ticket's acceptance criteria.
-
-- Repeat validation until no load-bearing ambiguity, contradiction, or unverified assumption remains. The RFC may permit multiple equivalent local implementations when they preserve the same documented shape and proof.
-
-- If repeated validation keep bringing up gaps, take a step back and look at what causes this oscillation. The architecture, ADRs, tickets are not carved in stone, they can have real contradictions or inconsistencies that cause it. Look into the core reasons and /align on them again if needed.
-
-- Overall, always consider future development and potential code reuse when selecting code shapes.
-
-- Cover migrations, compatibility, rollout, failure handling, and observability when relevant.
-
-- Record the plan into `docs/rfc/`, named with the owning ticket's basename — no RFC serial. Filename, `done/` moves, and citation: [TICKET-FORMAT.md](../to-tickets/TICKET-FORMAT.md#one-basename-per-work-item).
-
-- RFC header: H1 is the ticket's title plus ` — implementation plan`; then `**Authored:** YYYY-MM-DD`, and `**Last amended:** YYYY-MM-DD` once a later pass changes the plan; then one line stating what it implements, linking the ticket.
+- Record the plan into markdown file in /docs/rfc. The file should be using naming pattern `docs/rfc/0001-<YYYYMMDD>-<name>.md`, keeping constantly incrementing enumeration.
```

**recall/SKILL.md** — cd04a47 2026-08-29T22:18:45+03:00 Recall's trigger moves into the surface that is always loaded

```diff
-description: Determine where the project stands and what to work on next, with the decisions already taken surfaced alongside the questions genuinely still open. Use when asked what is next, where things stand, or to continue or pick up work.
+description: >-
+  Read the tree cold and establish where things stand. Run at the start of every
+  session, before the first reply — a greeting, a question and a work request are
+  all session starts, and none of them is an occasion to offer this instead of
+  running it. Also when continuing anything begun in an earlier session.
+# Recall
-Your goal is to surf through available docs and code and find out actual state of the project and the current and/or next things to focus on, without re-opening anything already settled.
+You remember nothing. This is the operating condition, not a limitation to work
+around. Read.
-- Investigate last sessions and actual tickets against the roadmap/version plan and find out where are we standing. Sessions, `tickets/done` and `rfc/done` are dated snapshots — read them for *why*, never for *whether* something is still open. Check `git status` and recent log too: uncommitted work is part of the actual state.
-- Browse architecture, open questions and concerns; find out relevant decisions and items; make sure to look up for concern resolution or state all over the doc/code base - most of pending items are supposed to be at least referenced in existing documentation. Be thorough. Follow the references of the item in flight until they converge, rather than reading each doc in isolation.
-- Every question you surface as open must cite where it is *still* open — in a maintained doc (delivery status, concerns, architecture, ADRs, glossary, edge records) or in the working tree. Otherwise it is settled: cite the deciding artifact instead, including the code where the code settled it. A question with no home at all is a documentation gap, so report it as one.
-- Build a compact summary of current state of the project and bring up all relevant items for current or next task, including the decisions already taken that bear on it, each with its reference. The summary must be written in simple but precise language, no moonspeak.
+## What arrives without being asked for `[bone]`
-- In case of ambiguity, present it too user. In case when continuation requires decision making, invoke /align skill.
-- Report drift you hit while reading (stale headers, docs the tree has outrun) rather than fixing it — fixing is outside recall's scope.
+Open retrieval misses are injected at session start by
+`.claude/hooks/open-misses.js`. Empty and failed Grep/Glob lookups are appended
+to `memory/archive/lookups.log` by `.claude/hooks/log-lookup.js`.
+
+Do not re-read `memory/misses.md` to find the open gaps, and do not narrate
+lookups you already made. The check ran.
+
+## Procedure
+
+0. `core/README.md` — **what the definitions are**: the layers, what a clean copy takes, and
+   what may be published on any channel. Read it when a definition is in question or
+   something is going out; not at every wake. Added 2026-08-26, when `readers-named.js`
+   reported `core/` as a one-ended seam named by a single skill — and the definitions move
+   there in C11, so a home nothing routes to would have arrived empty of readers.
+1. `bindings/operator/` — who you are working with, and the only place any of it may go.
+   Respect the grades: `[S]` is their word, `[O]` an interpretation, `[I]` a
+   predecessor's guess. Never act on an `[I]` as settled, never restate one back to
+   them as fact.
+2. [The queue](../../../docs/tickets/README.md) — what is in flight, what is blocked, and
+   which rows an unattended run may close. `docs/concerns.md` for gaps with no ticket.
+   [Experiments](../../../experiments/README.md) — what is under test on this repo
+   itself, and whether a reading is due at this wake. Check the cadence of each running
+   row against what has actually been read. **`experiments/` may be absent**, which is
+   correct for a tree that runs no trials and is not a defect to repair — the layer is one a
+   clean copy drops.
+3. **The most recent record in `docs/sessions/`** — short-term memory (`core/glossary.md`): the
+   next action, the pitfalls on the path to it, what the last session derived. One record.
+   If it points at something unfinished it did not itself resolve, follow the chain back as
+   far as that goes. Open it; the filename is not the record → [EVIDENCE.md](./EVIDENCE.md).
+4. The shared tree at root, and [the loop](../../../core/process.md) if this is a
+   scheduled run.
+5. `memory/rationale.md` only if you intend to change a rule.
+
+**If nothing instructed this wake, end the recall by invoking `/triage`.** A cold read that
+establishes where things stand and then stops has produced a report nobody asked for. Triage
+turns it into one decision, and a wake with no instruction is the moment it exists for — the
+backlogs are already in front of you at step 2.
+
+Where the wake carried an instruction, do that instead. Triage selects; it does not
+outrank a person who has already selected.
+
+**`memory/lessons.md` is not on this list.** It is reached from `/failure` when classifying
+a failure and from `/audit`, which writes it → [EVIDENCE.md](./EVIDENCE.md).
+
+**Open a source before asserting about it.** A summary, a title, a catalogue entry or a
+truncated preview is not the thing. For anything outbound,
+`bindings/scripts/show-citations.js` prints cited sources in full.
+
+Report state in the register of `memory/voice.md` — a choice, so nothing enforces it, and
+the one that bears here is *go where the joints already are*: a cold read is not the moment
+to reach for an instrument. Every question surfaced as open must
+cite where it is *still* open. A question with no home is a documentation gap —
+report it as one.
+
+## The misses a tool cannot see `[muscle]`
+
+Hooks catch failed lookups. They cannot catch these, so you must log them by
+hand, marked **independent-origin**:
+
+- **The operator asks something you should have known from the tree.** Log what the
+  tree failed to answer, never who asked or how they put it. This is the only signal
+  that does not originate in your own judgment.
+- **You are about to ask the operator a question.** Ask it, then log that you had to.
+
+Do not hand-log what a hook already recorded. Do not log what you never thought
+to look for — inventing entries fills the file with plausible values.
+
+Recording costs nothing and resolves nothing. Filling is `remember`'s job.
+Generalising is `audit`'s.
+
+## Close by asking what did not arrive
+
+A read reports what it found. What it did not reach is invisible from inside it, and this
+is the only moment the answer is still cheap — a session that has just read cold knows what
+it went looking for, and an hour later it knows only what it used.
+
+Two questions, answered before the session moves on:
+
+- **What did I need and not find?** Not what is absent from the tree — what you reached for,
+  or should have, and could not get from what you read.
+- **What would have made the next recall better?** A file that should have been on the list,
+  a route that should have existed, an order that would have put the load-bearing thing
+  first.
+
+**An answer held in context is not an answer.** Each lands as a miss, a mark in
+`docs/concerns.md` **carrying its kind** — that file's own list, and a row that cannot say
+which kind it is has not been understood well enough to file — or a change to this skill
+through `/skill-up`; whichever it actually is. Which of those a given answer earns follows `memory/lessons.md`'s bar: one occurrence is
+a miss, and only a repeat is grounds for changing the route.
+
+**Asked and found nothing is a result**, and belongs in the report. Silently skipped is not
+distinguishable from it, which is what makes saying so the whole obligation.
+
+---
+Layer labels are derived, not assigned. Evidence and the graveyard of dead
+statements: `memory/skills.md`. Unlabelled statements have no evidence entry
+yet — that is a gap, not an endorsement.
```

**skill-up/SKILL.md** — f60d477 2026-08-26T20:24:12+03:00 C7c + C10: the loop and the vocabulary join core

```diff
-  Aid agent skill creation or modification. Use when creating a new skill or changing an existing one.
+  Create or change an agent skill, against the evidence that licenses the change. Use
+  when writing a new skill, editing an existing one, or merging from a reference corpus.
-Your goal is to aid agent skill creation or modification.
+# Skill up
-Writing rules:
+A skill is instruction, not story. Precise and concise. Prefer umbrella terms to
+enumeration unless the umbrella could be read wrong. State everything in definitive
+form — no evolution logic, no decision explanations in the body. Blur wording where
+letting the model decide beats overfitting the instruction.
-- A skill is instruction, not story. Be precise and concise. Prefer umbrella terms to enumeration, unless can be interpreted wrong in context of the skill.
-- State everything in definitive form — no evolution logic, no decision explanations.
-- Blur wording where letting the model decide beats overfitting the instruction.
+The story is kept, not deleted: an `EVIDENCE.md` beside the `SKILL.md`, referenced in one
+line from it. Only what would change **that skill and no other** goes there — anything that
+would change a second skill is a lesson and keeps the home it has.
-Before writing, browse the existing skill set and match its structure and vibe — frontmatter shape, file layout, linking style, tone, altitude. Derive the set's conventions from the set itself; do not impose foreign ones.
+Before writing, browse the existing set and match its structure and vibe — frontmatter
+shape, file layout, linking style, tone, altitude. Derive conventions from the set
+itself; do not impose foreign ones.
-Verify the new or changed skill against the set:
+## Statements carry their layer
-- It does not overlap an existing skill, unless the overlap is intentional — then name it and link the owning skill.
+A skill statement is a claim, and claims here are graded by what would move them —
+`[bone]`, `[muscle]`, `[skin]`, or unlabelled. The layers and their evidence are
+`memory/skills.md`'s.
+
+Changing a statement obeys its layer:
+
+- `[bone]` needs a contradicting measurement. Not a better argument — a measurement.
+- `[muscle]` needs one clear counter-example.
+- `[skin]` needs nothing beyond a reason.
+- Unlabelled needs nothing, and adding a label needs evidence.
+
+**Never label a statement you are writing in the same pass** — `CLAUDE.md` meta-rule 6.
+Write it bare and let evidence find it.
+
+**A refuted statement goes to the graveyard, not the bin.** A skill showing only
+survivors reads as though nothing was ever wrong. Record what killed it and how long it
+lived.
+
+## Open what you cite
+
+A statement citing evidence must be written from the evidence, never from a note about it.
+Where the source is on disk, read it there; where it is not, fetch it. This repo records
+four occurrences of the opposite in a single day, and the mitigation that has ever fired
+before publication is re-reading, once in four.
+
+**A method adopted from outside carries its counts** — how often it was confirmed,
+criticised, or reported failing, kept separate. A method adopted on one reading of one
+source is a hypothesis with a citation attached, and reads exactly like a measured one
+once the citation is in place.
+
+## What removes it
+
+A mechanism that only adds is incomplete. Before shipping one, name what takes something
+back out — demotion, expiry, refutation, eviction — and where that record goes.
+
+A scalar cap is not a removal mechanism: it decides *when* something must go, never *what*,
+so it hands the choice back to whoever is standing there when it binds.
+
+## Verify against the set
+
+- It does not overlap an existing skill, unless the overlap is intentional — then name
+  it and link the owning skill.
-- It does not misfit the set — wrong altitude, wrong output location, conventions the set does not use.
+- It does not misfit the set — wrong altitude, wrong output location, conventions the
+  set does not use.
-A fact the set already states in one skill is referenced from there, not restated.
+A fact the set already states in one skill is referenced from there, never restated.
-The frontmatter description narrates the use case, not the implementation, and stays in line with the skill's intent. Capturing skill intent and usage is critical — /align when in tiniest doubt.
+The frontmatter description narrates the use case, not the implementation. Capturing
+intent and trigger is critical — `/align` at the tiniest doubt.
+
+## Placement, before wording
+
+Decide where a statement lives before writing it. **The ladder, the classes and who may
+adopt each are `/failure`, *Placing a non-strict rule*** — one home, and this does not
+restate it (meta-rule 7).
+
+What is this skill's alone: **a skill earns a statement when the rule has a moment** —
+something recognisable the description can name, so the rule arrives when it applies. A rule
+that applies at every moment has no trigger and does not belong in a skill.
+
+Watch the inverse: a rule that already existed and was not found. That is a delivery
+defect (meta-rule 2) — move the existing statement up a tier rather than writing a second
+one somewhere new.
-A skill's core is portable; a project's own conventions are not. Keep every `SKILL.md` body free of project facts, so the set stays mergeable with the corpus it came from, and hold what is genuinely local behind a reference:
+A skill's core is portable; a project's conventions are not. Keep every `SKILL.md` body
+free of project facts so the set stays mergeable, and hold what is local behind a
+reference:
-- Prefer an appendix file — `*-FORMAT.md`, `REFERENCE.md` — which may diverge freely.
-- Where a file is too much, a compact `<project-local>` block closes the `SKILL.md`; the tag is the declaration, so it needs no sentence saying so.
-- An appendix points at the project's own documentation for anything that documentation owns; it never restates it.
-
-A body instruction that cannot be written without a project fact belongs in the appendix instead. The project's development process — `docs/process.md`, built up lazily as the process itself incepts or changes — is a corpus convention like `glossary.md`, so a body may cite it by name; its contents are the project's own.
-
-A `<project-local>` block adds local facts; it never overrides the body.
-
-## Merging a reference corpus
-
-When asked to merge the skill corpus, ask which corpus to merge from.
-Port body changes, fixing defects as you port; leave every appendix file and `<project-local>` block as it stands. A skill present in only one corpus is either local by intent or not yet ported — ask which.
+- Prefer an appendix — `*-FORMAT.md`, `REFERENCE.md` — which may diverge freely.
+- Where a file is too much, a compact `
```

**sync-arch/SKILL.md** — d469814 2026-08-26T21:34:39+03:00 Backtick paths in live documents catch up with the moves

```diff
-I need you to run an all-around check, and make sure that architecture documentation (./docs/architecture.md, ./docs/adr/, ./docs/glossary.md, and the Edge records in ./docs/edge/) properly represent the intent of recently modified code.
+I need you to run a all-around check, and make sure that architecture documentation (./docs/architecture.md, ./docs/adrs, ./core/glossary.md) properly represent the intent of recently modified code.
-2) To make sure code does not contradict architectural decisions and rules.
+2) To make sure code does not contradicts architectural decision and rules.
-So the question you should answer first is whether it is possible to recreate the exact same implementation contract shape from the arch docs, or there are load-bearing contract details, hidden assumptions/decisions that are in code but not in docs.
+So the question you should answer first is will it be possible to recreate exact same implementation contract shape from the arch docs, or there are load-bearing contract details, hidden assumptions/decisions othat are in code by not in docs.
-Check `./docs/concerns.md` the same way: a concern the implementation has since answered is a finding — the file still claims open pressure that code resolved. Retire it to its owning ADR or architecture section rather than leaving it standing.
-
-For Edge records specifically (format: align skill's EDGE-FORMAT.md): code must not contradict a promise in a `Status: Normative` record, and each invariant's named validator test must still exist and still assert that promise — a missing or drifted validator is a finding, as is a promise marked **⚠ unguarded** in a Normative record.
-
```

## History checks

### M

HEAD: 6320d3c 2026-08-24T00:38:46+03:00 CODE: the pilot's names leave the fixtures

Skill-path history:

```text
57c972e 2026-08-24T00:32:45+03:00 SKILL: the corpus learns to merge, and project facts leave the bodies
777caa1 2026-08-24T00:32:32+03:00 SKILL: the cheapest falsifying example becomes a rule in align and plan-impl
05c6961 2026-08-21T10:09:24+03:00 SKILL: architecture is judged by the work it saves, and impl vocabulary is not invented
2492747 2026-08-20T03:06:04+03:00 SKILL: /celebrate marks an achievement, a milestone, or the overall state
6950320 2026-08-20T03:05:35+03:00 SKILL: the necessity gate fires late, and concern retirement gets its occasions
6e2c709 2026-08-20T02:01:17+03:00 SKILL: align opens with a necessity gate, and the mover retargets prose whole
c2c47dd 2026-08-20T01:22:40+03:00 SKILL: tighten implementation and recall guidance
63860af 2026-08-19T15:15:41+03:00 SKILL: improve-comments example loses identifying vocabulary
884aecc 2026-08-19T01:17:47+03:00 SKILL: /impact traces a change's consequences before implementation; align and plan-impl consult it and state the one-shape rule
d121e7d 2026-08-18T19:02:14+03:00 SKILL: planning states its bias toward simplicity, and names the oscillation exit
1822ec1 2026-08-18T16:57:13+03:00 SKILL: completion moves ride move_doc - a paired close goes in one invocation
b8bbc1c 2026-08-17T22:02:47+03:00 SKILL: ticket positions stay four digits; the insertion example taught the defect
0bac0c3 2026-08-16T13:01:23+03:00 SKILL: conventions get owners; TICKET-FORMAT.md minted
d499e90 2026-08-11T13:42:21+03:00 SKILL: strengthen plan validation workflow
dd5665b 2026-08-10T02:54:20+03:00 SKILL: denoise, implement, improve-comments, review-impl refinements; workflow diagram
0d97fd8 2026-08-09T20:18:37+03:00 SKILL: dream - samskaras and hidden edges among the targets; a quieter falling asleep
3956ed2 2026-08-09T14:19:59+03:00 SKILL: dream rework - falling asleep, moods, oneiric shapes; denoise keeps indexes clean
83604fb 2026-08-09T01:09:59+03:00 SKILL: dream - analytical meditation over the corpus
3787670 2026-08-09T01:04:18+03:00 SKILL: conclude a day, not a chat, and answer the advise questions
c4b549c 2026-08-09T01:04:16+03:00 SKILL: mark temporary code with TODO (temporary)
9b7beb1 2026-08-08T21:52:45+03:00 SKILL: implement hands off to /review-impl before /sync-arch
f89bc91 2026-08-08T04:17:54+03:00 SKILL: agent instruction additions - diagrams over arch-speak, doc-type READMEs
7f56329 2026-08-07T04:39:20+03:00 SKILL: make decision-bearing tickets evolve through align
cb2340a 2026-08-07T03:39:00+03:00 SKILL: review-architecture restored and naturalized — outcome routed to ticket+RFC, canonical homes linked
342a8cf 2026-08-07T03:39:00+03:00 SKILL: commit skill — SKILL tag minted for agent-skills-corpus commits
b52db1a 2026-08-07T03:31:31+03:00 DOCS: skills corpus skill-up pass — review-impl minted, review-architecture retired, descriptions calibrated
0e3abf1 2026-08-07T02:32:17+03:00 DOCS: skills corpus sweep — fractal to-tickets, inception-only to-spec, RFC-architecture rule into plan-impl
9368126 2026-08-05T14:15:32+03:00 DOCS: 003c re-staged on m4 — RFC 0008 rewritten; 006 pulled ahead of 011; refill scope minted
2acad2b 2026-08-04T00:42:26+03:00 DOCS: skill refinements — leakage lens in review, story-shaped code in implement
c8e6353 2026-08-02T23:03:20+03:00 DOCS: recall skill — where the project stands and what is next
4cab63a 2026-08-02T23:03:13+03:00 DOCS: Provider edge record — m4 widened to the shape/vendor split
161aaf2 2026-08-02T08:58:53+03:00 DOCS: ticket numbering — release-scoped, position-ordered, sluggable
0dff6c9 2026-07-26T00:14:12+03:00 DOCS: m5 landed — Edge records, /edge skill, edge awareness in align/sync-arch
f63635b 2026-07-25T17:03:27+03:00 DOCS: skills — commit gate set matches CI (adds ruff format --check)
bb9a742 2026-07-25T03:52:19+03:00 DOCS: skills — code-review doc-vs-code coherence rules
f57855c 2026-07-25T02:18:06+03:00 DOCS: agents — commit gates rule; plan-impl RFC-unambiguity rules; docs-README pointer
66937b2 2026-07-24T19:16:20+03:00 DOCS: skills — sync-arch dual goals; plan-impl and to-spec sharpened
dc371e7 2026-07-22T01:27:52+03:00 DOCS: commit skill — grouping, tagging, and permission rules
ed46672 2026-07-22T01:24:35+03:00 DOCS: align skill — four method rules from practice
eb7896e 2026-07-21T17:18:26+03:00 Update SKILL.md
20e7d81 2026-07-21T00:31:33+03:00 Update SKILL.md
53fd995 2026-07-16T15:33:52+03:00 chore(skills): implement skill guidance on boundary method structure
3334591 2026-07-16T12:04:42+03:00 more skills realignment
```

Loader Git index:

```text
100644 5a24b3f2aa9b7ed36edb0491603c7ef2e8bcf79c 0	.claude/CLAUDE.md
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.claude/skills
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.codex/skills
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.cursor/skills
```

`core.symlinks`: true

### A

HEAD: 810edb2 2026-09-03T15:38:59+03:00 DOCS: require an http(s) origin for the corrected-forecast host

Skill-path history:

```text
384d318 2026-08-24T02:09:25+03:00 SKILL: extract the concerns file format from align
44a51f5 2026-08-24T00:52:40+03:00 SKILL: separate portable method from this project's conventions
1df1d4f 2026-08-12T16:02:02+03:00 SKILL: agent skills corpus
```

Loader Git index:

```text
120000 42c5394a18a882778ebf50eb940fb5a96bc4a6d9 0	.cursor/skills
```

`core.symlinks`: true

### F

HEAD: dd847b5 2026-09-03T15:46:16+03:00 DOCS: Close 0340 — TWC remainder cell wins, and it is not a correction method.

Skill-path history:

```text
a0ba8d5 2026-09-03T09:33:18+03:00 SKILL: Leave Pass to the hook; review-impl may call /implement.
3f2ba65 2026-09-02T01:12:24+03:00 SKILL: Tighten advise, impact, plan-impl, and to-tickets.
29c3cc6 2026-08-29T15:49:18+03:00 SKILL: Treat landed-but-unchecked tickets as the next session first.
43861b4 2026-08-29T14:18:39+03:00 DOCS: Plan and record FEPEDI stations entering the registry.
```

Loader Git index:

```text
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.claude/codex
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.claude/skills
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.codex/skills
100644 bb18752b4df70c7e94ede49f25b2bf98de600c07 0	.cursor/hooks.json
100644 e50a4d81d1e8f039491bb2bb5ae37c9228d17243 0	.cursor/hooks/plan_impl_loop.cmd
100644 d5500b451daef32b21f45744e0f710ff93c0d4b7 0	.cursor/rules/Project-environment.mdc
120000 2b7a412b8fa0fb7e985b0793321bd4e698f2b6cd 0	.cursor/skills
```

`core.symlinks`: true

## Neighboring corpora

| Skill entrypoint | L | L2 | W | S |
|---|---|---|---|---|
| advise/SKILL.md | b03579c52b | b03579c52b | — | — |
| align/SKILL.md | 9cfa1161bf | 561e1253b4 | 385f651d4a | — |
| audit/SKILL.md | 6562abddda | 6562abddda | — | — |
| celebrate/SKILL.md | 26e752d62d | — | — | — |
| comment/SKILL.md | ea87608ea8 | 037868a8e0 | — | — |
| commit/SKILL.md | 3e97052725 | 0dc3ee65c5 | — | — |
| conclude/SKILL.md | e5f9438f5d | 04484dc516 | 4cfedf9b42 | — |
| denoise/SKILL.md | 7ae66b427b | bb620b6346 | 50ed86d304 | — |
| deprecated/design-an-interface/SKILL.md | — | — | — | a2596e9fa2 |
| deprecated/qa/SKILL.md | — | — | — | d9727aac65 |
| deprecated/request-refactor-plan/SKILL.md | — | — | — | d59de4ba6c |
| deprecated/ubiquitous-language/SKILL.md | — | — | — | 2449e2345b |
| dream/SKILL.md | e22dacfe71 | 6cc139cbb7 | — | — |
| engineering/diagnose/SKILL.md | — | — | — | 28886402bb |
| engineering/grill-with-docs/SKILL.md | — | — | — | 3e35025119 |
| engineering/improve-codebase-architecture/SKILL.md | — | — | — | f00de04c7b |
| engineering/prototype/SKILL.md | — | — | — | a653deb65a |
| engineering/setup-matt-pocock-skills/SKILL.md | — | — | — | c778d4e3d8 |
| engineering/tdd/SKILL.md | — | — | — | af05970506 |
| engineering/to-issues/SKILL.md | — | — | — | 0e6a2973fa |
| engineering/to-prd/SKILL.md | — | — | — | 5212dee3af |
| engineering/triage/SKILL.md | — | — | — | b819f0285e |
| engineering/zoom-out/SKILL.md | — | — | — | 2a6894c7f9 |
| experiment/SKILL.md | ebcc91c54a | d2fa8f1dc6 | — | — |
| failure/SKILL.md | b5435bf198 | 331b59cae1 | — | — |
| implement/SKILL.md | e64f1a86ec | 90acc01bf8 | — | — |
| in-progress/review/SKILL.md | — | — | — | 5700f30d3f |
| in-progress/writing-beats/SKILL.md | — | — | — | 0843367d0a |
| in-progress/writing-fragments/SKILL.md | — | — | — | 4ffa34a701 |
| in-progress/writing-shape/SKILL.md | — | — | — | 81a542b95f |
| lurk/SKILL.md | ca2e40a3c6 | 02bebec574 | — | — |
| maintain/SKILL.md | 4aa3bec0d7 | — | — | — |
| mechanism/SKILL.md | 0a0c279379 | — | — | — |
| metric/SKILL.md | 4ef18aff68 | — | — | — |
| misc/git-guardrails-claude-code/SKILL.md | — | — | — | 03c4de7613 |
| misc/migrate-to-shoehorn/SKILL.md | — | — | — | de4da4c11d |
| misc/scaffold-exercises/SKILL.md | — | — | — | 75f5c9d771 |
| misc/setup-pre-commit/SKILL.md | — | — | — | 872f4037cb |
| personal/edit-article/SKILL.md | — | — | — | cc372fb25b |
| personal/obsidian-vault/SKILL.md | — | — | — | 7bed1d552a |
| plan-impl/SKILL.md | e25d728337 | e25d728337 | — | — |
| productivity/caveman/SKILL.md | — | — | — | b4bb6fe3bf |
| productivity/grill-me/SKILL.md | — | — | — | 74147eb601 |
| productivity/handoff/SKILL.md | — | — | — | d215dd8f2a |
| productivity/teach/SKILL.md | — | — | — | d36496c90d |
| productivity/write-a-skill/SKILL.md | — | — | — | be8f20e663 |
| reasoning/SKILL.md | 9646e01570 | — | — | — |
| recall/SKILL.md | a6c6f19dd2 | a5d369a65a | — | — |
| remember/SKILL.md | 08e28585f3 | 88abc979f2 | — | — |
| review-architecture/SKILL.md | — | — | f53a07a4f3 | — |
| skill-up/SKILL.md | 8ff808ac3e | db4dc72a1d | — | — |
| sync-arch/SKILL.md | d427739b05 | 8a8e6da298 | — | — |
| tdd/SKILL.md | — | — | af05970506 | — |
| ticket/SKILL.md | a391558103 | — | — | — |
| to-issues/SKILL.md | — | — | c7671c479e | — |
| to-tickets/SKILL.md | — | 84ddaf9a89 | — | — |
| triage/SKILL.md | 33feaab0cb | 1bd6411b93 | — | — |
| write-prd/SKILL.md | — | — | f7dc76984d | — |

## Supplementary harness files

- M: `D:\Dev\AI\meteoscape\.agents\scripts\move_doc.py` SHA-256 `549a015ea147ffb3e751eb88805693cde1afe7332f07a8d840160de595d4d0a8`
- A: `D:\Dev\DriftSense\workspace\agents\scripts\move_doc.py` SHA-256 `0800f830c155c7cd05acb903e02f69c7aa8f56ddb4f4a973fb8ea41db57fc5ce`
- F: `D:\Dev\DriftSense\workspace\forecast_collector\.agents\scripts\move_doc.py` SHA-256 `c0d85580867e4fb80ab73e891f4a9dd2804f01c7bc76b56351b53707ea12a8a3`

```diff
--- M/move_doc.py
+++ A/move_doc.py
@@ -1,6 +1,6 @@
-"""Mechanical record mover (docs/cicd.md § CI pipeline).
+"""Mechanical record mover.
 
-    uv run python .agents/scripts/move_doc.py SRC DST [SRC DST ...]
+    python scripts/move_doc.py SRC DST [SRC DST ...]
 
 Git-moves each markdown record, re-depths the moved files' own links, and rewrites inbound
 references in live documents. Historical records are left as written. A paired close — ticket and
@@ -9,8 +9,8 @@
 Judgment stays with the caller: no boxes, no statuses, no prose. The doc-integrity guards are the
 proof of a move:
 
-    uv run pytest tests/deterministic/test_docs_integrity_guard.py \\
-                  tests/deterministic/test_docs_conventions_guard.py
+    python -m pytest scripts/test_docs_integrity_guard.py \\
+                     scripts/test_docs_conventions_guard.py
 """
 
 from __future__ import annotations
@@ -22,10 +22,7 @@
 from collections.abc import Callable, Sequence
 from pathlib import Path
 
-REPO_ROOT = Path(__file__).resolve().parents[2]
-sys.path.insert(0, str(REPO_ROOT / "tests" / "deterministic"))
-
-from docs_corpus import live, resolve_name, universe  # noqa: E402  (repo path set just above)
+from docs_corpus import REPO_ROOT, live, resolve_name, universe
 
 _LINK = re.compile(r'(!?\[[^\]]*\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
 _FENCE = re.compile(r"^\s*(```|~~~)")
@@ -33,8 +30,8 @@
 _UNMOVED = ("http://", "https://", "mailto:", "#")
 
 _VERIFY = (
-    "uv run pytest tests/deterministic/test_docs_integrity_guard.py "
-    "tests/deterministic/test_docs_conventions_guard.py"
+    "python -m pytest scripts/test_docs_integrity_guard.py "
+    "scripts/test_docs_conventions_guard.py"
 )
 
 
@@ -166,7 +163,10 @@
 def _git_move(root: Path, source: str, destination: str) -> None:
     (root / destination).parent.mkdir(parents=True, exist_ok=True)
     tracked = subprocess.run(
-        ["git", "ls-files", "--cached", "-z", "--", source], cwd=root, capture_output=True
+        ["git", "ls-files", "--cached", "-z", "--", source],
+        cwd=root,
+        capture_output=True,
+        check=False,
     ).stdout
     if tracked:
         subprocess.run(["git", "mv", source, destination], cwd=root, check=True)

```


```diff
--- M/move_doc.py
+++ F/move_doc.py
@@ -1,6 +1,6 @@
-"""Mechanical record mover (docs/cicd.md § CI pipeline).
+"""Mechanical record mover.
 
-    uv run python .agents/scripts/move_doc.py SRC DST [SRC DST ...]
+    ./venv/Scripts/python.exe .agents/scripts/move_doc.py SRC DST [SRC DST ...]
 
 Git-moves each markdown record, re-depths the moved files' own links, and rewrites inbound
 references in live documents. Historical records are left as written. A paired close — ticket and
@@ -9,7 +9,7 @@
 Judgment stays with the caller: no boxes, no statuses, no prose. The doc-integrity guards are the
 proof of a move:
 
-    uv run pytest tests/deterministic/test_docs_integrity_guard.py \\
+    ./venv/Scripts/python.exe -m pytest tests/deterministic/test_docs_integrity_guard.py \\
                   tests/deterministic/test_docs_conventions_guard.py
 """
 
@@ -33,7 +33,7 @@
 _UNMOVED = ("http://", "https://", "mailto:", "#")
 
 _VERIFY = (
-    "uv run pytest tests/deterministic/test_docs_integrity_guard.py "
+    "./venv/Scripts/python.exe -m pytest tests/deterministic/test_docs_integrity_guard.py "
     "tests/deterministic/test_docs_conventions_guard.py"
 )
 
@@ -157,10 +157,12 @@
     b: str,
     mapping: dict[str, str],
 ) -> None:
-    text = path.read_text(encoding="utf-8", newline="")
+    with path.open(encoding="utf-8", newline="") as handle:
+        text = handle.read()
     rewritten = transform(text, a, b, mapping)
     if rewritten != text:
-        path.write_text(rewritten, encoding="utf-8", newline="")
+        with path.open("w", encoding="utf-8", newline="") as handle:
+            handle.write(rewritten)
 
 
 def _git_move(root: Path, source: str, destination: str) -> None:

```

## Archive verification

M archive: 33 files; mismatches with current M: []; M files missing from archive: [].
