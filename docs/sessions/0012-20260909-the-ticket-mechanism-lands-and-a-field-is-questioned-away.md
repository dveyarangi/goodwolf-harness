# The ticket mechanism lands, and a field is questioned away

Session twelve, 2026-09-08 into 2026-09-09. One full ring on
[01-0011.0025](../tickets/done/01-0011.0025-archive-duty-reaches-maintain.md): `/align` → `/plan`
→ `/implement` → `/verify` → `/maintain`, plus `/advise` on the ticketing process inside the
align. Wake was by hand; `/recall` is still not installed. Seven commits.

## Work completed

- **[01-0011.0025](../tickets/done/01-0011.0025-archive-duty-reaches-maintain.md) closed.** The
  ticket mechanism is declared. Its six rules live in `ticket.rules.md` and reach `/maintain`,
  `/plan` and `/align` as installed blocks. The ticket is declared as a record in
  `TICKET-FORMAT.md`, and `tickets.py --check` holds every live one to it. 173 → 216 tests.
- **The defect the spec was written from is closed.** The archive duty that lost five tickets on
  2026-09-06 now reaches the skill that archives mechanically, in both directions.
- **The queue shed its history**: fourteen Done rows out, 1579 words to 873.
- **The entry contract went to v6.**

Every decision is on the closed ticket, its RFC, and the three mechanism evidence files. What
follows is only what those do not hold.

## What the user's questions removed

Three of this session's changes were reversals of my own work, each opened by a short question.

- **"What is declared by for?"** It fed one check that had never fired across three mechanisms,
  and duplicated the evidence's first paragraph. I had just spent a stage making it a link. The
  field left the shape entirely; the rule became *a `not yet` row may not name an archived
  ticket*, which catches the same mistake a day later and every other stale gap, and needs no
  field.
- **"Why can a straw dog not sit in a rules file?"** It can. I had generalised from the installed
  block, which the listing blanks, to the rules file, which it does not. Two probes settled it in
  a minute. The claim had gone unchallenged through four `/plan` passes and three `/verify`
  passes.
- **"Wrap what is authored — what does that mean?"** The phrase named the act and left the reader
  to infer the thing, and its first draft called an installed block a *copy*, which the glossary
  reserves against for exactly that noun.

The pattern: each was a claim I had reasoned to and never tested, and each cost more to carry than
to check. The straw-dog listing cannot see this class, and neither could three verification
passes, because the text was well-formed and internally consistent every time.

## Open, with owners

- **Next cycle needs a nod** (`next-cycle=ask`). By the ordering rule the candidate is
  [.0050](../tickets/done/01-0011.0050-shape-checked.md), the shape check: the only Ready slice that
  hands the next one a check, and AFK. [.0030](../tickets/01-0011.0030-archive-backlog-listed.md)
  and [.0040](../tickets/01-0011.0040-queue-derived-index.md) are Ready beside it.
- **The `not yet` links are a live violation of the core rule.** Every referent is a markdown link
  from `.agents/` into `docs/tickets/`, outside any `<project-local>` or `<straw-dog>` block, and
  the format mandates the form. It travels into a recipient as a dangling link. Routed to
  [.0050](../tickets/done/01-0011.0050-shape-checked.md) with the ticket-number form as one candidate;
  that align decides. Surfaced by the same question that removed `declared by`, and not fixed in
  this slice because the format is the shape's to change.
- **The user's grade on the shape** is still not given, pre-registered on both mechanism docs
  since 2026-09-07: did the shape change because `/maintain` did not fit it, or was the
  declaration bent? The third declaration has now added its own answer to `/maintain`'s evidence.
- **P4 waits for `/spec`**, in `/maintain`'s body inside a straw dog bound to
  [01-0017](../tickets/01-0017-io-graph-coherent.md).
- **P8 waits for the derived queue**, wrapped at its home in `ticket.rules.md`, bound to
  [.0040](../tickets/01-0011.0040-queue-derived-index.md).
- **The abbreviation limitation in `tickets.py`.** An outcome containing a sentence-ending
  abbreviation followed by a capital is read as two sentences. No live instance; the rule is
  amended when one appears rather than pre-empted. On the RFC.

## Session through the advise questions

**Great:** the three questions above. Each took one line from the user and removed a mechanism,
a field, or a wrong claim from the tree. *"What is declared by for?"* is the one to remember: the
answer was a permanent field feeding a never-fired guard, and nothing in the harness would ever
have asked.

**Good enough:** four `/plan` passes, each finding less than the last, with the fourth finding
only what the second and third had written. Stopping there was right. Three `/verify` passes with
three different lenses — criteria, prose, behaviour — each finding what the others could not,
including a duplicated moments row I had introduced myself.

**Questionable:** the `declared by` link work was built, tested and committed before anyone asked
what the field was for. The necessity gate belongs on a field as much as on a mechanism, and
`/align` opens with one; I did not apply it to an existing field I was amending.

**Missing:** I twice claimed a constraint without testing it — that a code span cannot be
rewritten, which was right, and that a rules file cannot hold a straw dog, which was wrong. The
same sentence pattern produced both. A claim about what a tool cannot do is cheap to check and I
checked neither until asked.

## Housekeeping

Seven commits: `ALIGN`, `PLAN`, three `IMPLEMENT`, `VERIFY`, `MAINTAIN`. Verification set is 216
behavioural tests, `mechanisms.py --check`, `inject_rules.py --check` and `tickets.py --check`.
Sixteen straw dogs, all bound, no diagnostics. Three mechanisms declared: `mechanism-shape`,
`maintain`, `ticket`.
