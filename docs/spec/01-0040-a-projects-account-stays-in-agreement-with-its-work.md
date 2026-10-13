# A project's account stays in agreement with its work

**Status:** **Accepted by the user, 2026-10-13**, with its modules and its testing decisions —
developed through `/spec` from the align on
[q-0037.0018](../questions/q-0037.0018-what-is-a-projects-product-document-to-the-method-and-which-of-the-methods-mechanisms-keeps-it-and-the-projects-work-in-agreement-both-ways.md),
whose eleven decisions it rests on and does not restate. The id is the one `/ticket` is to mint
for it.

## Problem Statement

A person steering coding agents keeps, at best, a document saying what the project is for — the
pains it relieves, the goals it must not lose, the causes, the answers. Nothing in the work reads
it. In this tree, on 2026-10-12: the queue's order named no pain, cause or answer; two pieces of
work landed with no row; 14 rows marked done linked to nothing that provides them; 43 of 47 rows
pointed at questions of how the harness is built rather than of what it is for. In the trees that
received the method, no product document exists at all, though each was seeded with the question
*What is this project for?*. The front page and the release notes, which are the same account told
to other readers, have no owner.

So the document drifts from the work in both directions: work appears that serves no stated
answer, and answers are declared that no work builds; and what the project says about itself
outward is written apart from what it decided inward.

## Solution

A mechanism of the method, `product`, keeps one account of what the project is for and tells it to
three readers: the product document inside, the root README to a reader arriving cold, the release
note to one updating.

The account is linked to the work through the question store and never through tickets. A purpose
question, once decided with something to build, closes; its answer becomes a numbered row in the
product document; a question opens under *How is this project built?* carrying a trace link to that
row. Questions under it inherit the link. What an answer's coverage is — absent, in progress,
present — is read from the questions that realize it, never written. The document points outward
only from a row whose answer is not chosen yet, to the purpose question it waits on. Building may
open a purpose question again (the zigzag); a pain is measured, never closed.

The development method and the store know nothing of the product: the store keeps an opaque trace
link, and the product mechanism installs its rules into `/align` and the questions skill and checks
the link with its own script. Beside the queue, which stays the person's to order, it shows what
each item realizes and which answers nothing realizes.

## User Stories

1. As a person steering agents, I want each decision about what the project is for to land as a row of one document, so that I can read the project's purpose in one place.
2. As a person, I want each answer row to keep an id that is never renumbered, so that links to it survive every edit of the document.
3. As a person, I want a decided purpose question to close the moment it is decided, so that product questions do not stay open for the length of the building.
4. As a person, I want deciding an answer to open its building question under *How is this project built?* in the same step, so that no decision waits for someone to remember to start it.
5. As an agent opening a question directly under the structure root, I want to be asked which answers it realizes, or to state that it realizes none, so that the reason the question exists is written while it is known.
6. As an agent opening a sub-question, I want it to inherit its parent's trace link without my writing it, so that the link costs nothing below the first level.
7. As a person, I want a question that realizes no answer to be visible as derived, so that work drifting away from the product shows up without being refused.
8. As a person, I want to see each answer's coverage — absent, in progress, present — derived from the questions that realize it, so that no one has to keep a status up to date by hand.
9. As a person, I want an answer that no question realizes to be reported, so that a declared answer nobody builds is seen.
10. As a person, I want a structure question with no trace link and no statement of derived to be reported as an orphan, so that a missing link is caught at the next check rather than never.
11. As a person, I want a trace link that names no existing answer to be reported, so that a renamed or mistyped answer does not silently break coverage.
12. As a person, I want a row whose answer is not chosen yet to point at the open purpose question it waits on, so that I see what is still undecided and where it is being decided.
13. As a person, I want that row to come up at the next session's start once its question closes, so that the document is rewritten when the decision lands.
14. As a person, I want a row bound to a question outside the purpose root to be reported, so that the document does not fill again with pointers into how things are built.
15. As a person, I want a purpose question that no row names to be reported, so that a product question is never asked off the document.
16. As a person ordering the queue, I want to see beside it which answers each item realizes, so that I order work knowing what each piece is for.
17. As a person ordering the queue, I want to see the answers no item realizes, grouped by goal and by pain, so that leaving something out is a choice made in sight.
18. As a person, I want building that shows an answer or its causes must change to open a new purpose question, so that the document is corrected from what the work learned.
19. As a person, I want a replaced answer to keep its id and a new answer to get a new one, so that history and links stay readable after the zigzag.
20. As a person, I want a pain never marked as closed, so that relief is read from its measure and not from a box ticked on an answer.
21. As a reader arriving cold, I want the root README to say what the project is for in the words of its product document, so that the front page and the decisions inside never disagree.
22. As a reader arriving cold, I want the README's account of how to take and extend the project to come from the edge records, so that it matches the contract.
23. As a recipient updating, I want a release note whose product half lists the answers whose coverage moved since the last release, and the causes and pains they touch, so that I know what the update brings me.
24. As a recipient updating, I want the note's contract half to come from the edge records' lines, so that what may break me is stated by the record that owns the contract.
25. As a person, I want the release note gathered from coverage rather than written from memory, so that nothing built since the last release is left out.
26. As a project that keeps no product document, I want the product check to find nothing and its rules to stay silent, so that a project without the mechanism in use is not burdened by it.
27. As a person, I want the product check in the verification set and in `/maintain`, so that drift is caught where every other record's drift is.
28. As a person, I want the store to keep the trace link without knowing what it points at, so that the development method works the same in a project with no product mechanism.
29. As a person, I want each seeded root's words to belong to the mechanism that owns the root, so that a project taking a different mechanism for its purpose is seeded with that mechanism's question.
30. As a person, I want the purpose root of a tree whose store predates the seed to be named once, so that the mechanism works in this tree, whose product questions sit under a root of another wording.

## Implementation Decisions

- **The trace link, in the question store.** A new part of a question holds its trace link: one or
  more opaque answer references, or the statement that the question is derived. A new store call
  writes it. Trace propagation is computed when the store is read — a question's effective link is
  its own or its nearest ancestor's — and never copied into children. The store validates the
  form only; it never resolves a reference. This is the deep module of the store side: one call to
  write, one function answering what a question realizes.
- **The `/product` skill, the instruction file.** It holds three formats beside it — the product
  document, the README's derivation, the release note — and the act of writing each. `/align`
  calls it at allocation; the person may call it to see coverage and the unrealized answers. A
  separate releases mechanism is not declared.
- **The product document's format.** Pains, goals, causes and answers; answers carry `A<n>` ids,
  never renumbered and only retired; a row whose answer is not chosen carries a straw dog bound to
  a question under the purpose root; a decided row carries no outward link. In a recipient the
  document is a record the mechanism declares at its path under `docs/`.
- **The product check, its own script.** Reads the document and the store and reports: an
  undecided row with no binding; a row bound outside the purpose root; a purpose question no row
  names; an orphan; an unrealized answer; a trace link naming no answer. On request it renders
  coverage per answer, the coverage that moved since a given point — which the release note reads
  — and, beside the queue, what each item realizes and the unrealized answers by goal and pain.
  Rendered on request, never committed. This is the mechanism's deep module: a tree in, findings
  and coverage out. It finds nothing in a tree with no product document.
- **Rules installed from the product rules file.** Into `/align`: when a purpose question is
  decided with something to build, `/product` lands the row, the question closes against it, and
  a structure question opens with its trace link. Into the questions skill: a question opened
  directly under the structure root states its answers or that it is derived. Into `/maintain`:
  run the product check. <straw-dog question="q-0037.0006.0024">Each holds where a project keeps a
  product document.</straw-dog>
- **The mechanism's doc.** Its moments — a purpose decision landing, the README derived, a release
  note gathered — what it produces and who reads each output, the release note among them; what
  retires it; what would show it working.
- **Seeding declared roots.** The store seeds, into an empty store, the roots the installed
  mechanisms declare, and its own shelf supplies the rest until their mechanisms exist; the product
  mechanism declares *What is this project for?*.
- **A tree's roots, by their words.** Every tree that took the method carries the three seeded
  roots; this tree, whose store predates the seed, takes them: q-0033 reworded as the purpose root,
  q-0033.0008 under it, every other root under a new structure root, q-0038.0001 under a new landscape root
  *(the user, 2026-10-13, replacing a purpose root named as a project-local answer)*.
<straw-dog question="q-0037.0018.0005">
- **The README's derivation** is open — generated whole from the document and the edge records, or
  written by hand and checked against them.
</straw-dog>
<straw-dog question="q-0037.0018.0004">
- **A pain's measure** is open and parked by the user. The document carries no measure field.
</straw-dog>
- **This tree's own migration** is instance work, not the mechanism's: q-0033 named as the purpose
  root; the rows of the product document numbered; the 43 bindings to structure questions turned
  into trace links on those questions; the 14 done rows given their coverage; the README derived
  anew.

## Testing Decisions

- A good test drives the script from outside over a fixture tree in a temporary directory and
  asserts only what can be seen: what was written, what was refused and why, which findings came
  back, what coverage was rendered. It never asserts an internal function's shape. The store's own
  tests are the prior art.
- Tested: the trace link in the store — writing, refusing a malformed link, propagation on read,
  derived; the product check — each finding in both polarities, coverage, the coverage that moved
  since a point, silence in a tree with no product document; seeding declared roots — a declared
  root seeded, the shelf filling the rest, nothing reseeded into a store that holds an entry.
- Not separately tested: the formats, the installed rules and the mechanism's declaration, which
  the existing checks — rule installation, the mechanism shape, the store check — already cover.
- The check is written before what it checks and seen to fail; run over this tree first, its count
  of prior findings is recorded rather than a manufactured zero.

## Out of Scope

- How a pain is measured, and weighting the queue by pain (q-0037.0018.0004, parked).
- Taking a mechanism alone or going without it (q-0037.0006.0024); until then the mechanism ships in
  core with its conditions.
- The landscape root's research mechanism and the development method as a declared mechanism;
  each keeps its root on the store's shelf until it exists.
- Publishing a release, which stays the harness's, and writing a contract line, which stays the
  edge mechanism's; the release-family tickets are re-cut at `/ticket`.
- Validating that an answer relieved its pain beyond its measure.

## Further Notes

- The vocabulary is requirements traceability's, taken whole: answer, trace link, realizes, trace
  propagation, coverage, allocation, orphan, derived, unrealized answer — in this project's
  glossary, bound to q-0037.0018 until the mechanism is accepted into the method.
- A discover pass of 2026-10-13, in q-0037.0018's body, names the known failure of this shape: links
  decay when nobody reads them. Every link here has a named reader — the check, the coverage
  rendering, the release note, the person ordering the queue.
- Precedents named by that pass: bidirectional traceability, stored one way and traversed the other;
  Hevner's three cycles of design science research for the three roots; Suh's zigzagging for the
  return from building to purpose.
