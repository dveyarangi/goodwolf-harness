# Session 0058 — the product line lands, and the tree takes its three roots

- **record of** what happened

2026-10-13, session `local_540b00a6`. Opened on a greeting; closed
[01-0011.0110.0055 a-projects-code-names-what-governs-it](../tickets/done/01-0011.0110.0055-a-projects-code-names-what-governs-it.md),
then four slices of the product line —
[01-0040.0010 an-answers-coverage-is-read-from-the-questions-that-realize-it](../tickets/done/01-0040.0010-an-answers-coverage-is-read-from-the-questions-that-realize-it.md),
[01-0040.0015 this-trees-store-takes-the-three-seeded-roots](../tickets/done/01-0040.0015-this-trees-store-takes-the-three-seeded-roots.md),
[01-0040.0020 drift-between-the-document-and-the-work-is-found](../tickets/done/01-0040.0020-drift-between-the-document-and-the-work-is-found.md),
[01-0040.0040 this-trees-account-runs-on-the-mechanism](../tickets/done/01-0040.0040-this-trees-account-runs-on-the-mechanism.md) —
and brought every open question of the tree to an answer of the product document.

## Decisions, and what chose them

**The pointer rule grew by one word, no more.** The frost_map trial of `.0055` — a fresh session
given the task alone — brought 13 comments to 15 pointers, all resolving, and reported eight places
it guessed. The agent proposed answering five of them in the rule's text; the user: *make sure you
are not inflating the rules, and add* — and when the rule had grown one word while the question's
record grew seven lines: *I asked you to make sure you don't inflate, and you inflated them at
once?* The test that cut it: did the session stop, or only ask? It stopped once — a phrase two rules
back — so *name the rule* became *name each such rule*; the rest the rule already answered. The
record kept one sentence.

**A trace link names its answer by id and name.** The plan had a bare `A7`; the user: *A7 tells no
one anything unless they see the whole picture.* As a ticket is named by id and slug, the link
became `A7 "<name>"`, the id matched and the name checked word for word
([q-0037.0018.0006](../questions/done/q-0037.0018.0006-how-is-an-answers-coverage-read-from-the-questions-that-realize-it.md)).
**Only open and decided questions realize** — a pruned question built nothing — settled by the agent
as reversible, coverage never being stored.

**The tree takes the three seeded roots.** For the drift check the agent proposed a line naming the
purpose root in the document, and asking links of every question outside it, since this tree had
twenty roots and no structure root. The user turned it: *shouldn't we redo our roots? massive, but
I think it will be useful.* With the seeded roots everywhere, the purpose-root line need not exist,
and the orphan scope became the spec's own. q-0033 took the words *What is this project for?*, with
the front-page question under it (*q-0031 is a product question*); *How is this project built?*
(q-0037) took eighteen roots; *What landscape does this project evolve in?* (q-0038) took the
measurement question and, later, abstraction height (*that is landscape*). Decisions in
[q-0037.0018.0009.0001](../questions/done/q-0037.0018.0009.0001-how-does-this-trees-store-take-the-three-seeded-roots.md),
landed in [the spec](../spec/01-0040-a-projects-account-stays-in-agreement-with-its-work.md).

**What is broken fails the check; what is missing is reported** — the agent's recommendation, the
user's agreement
([q-0037.0018.0007](../questions/done/q-0037.0018.0007-how-is-drift-between-a-product-document-and-the-work-found.md)):
an unrealized answer is a state, not an error, and a check that failed on it would stop every
commit.

**The answers keep `A`.** Asked *are these basically a features list? why "A"?*, the user kept the
traceability vocabulary taken whole the same day. The method's glossary was not given those words:
*not yet; these words are very general.*

**The names are the user's.** Forty-eight answer names drafted from each row's first words were
accepted with sixteen links the agent proposed; two old bindings were rebound. Four more answers
were added when the last orphans showed work no row described, each named again in plain words
after the user's objections — *what script?*, *I don't understand what A10 is about*, *sessions
collaborate, no?*, *people don't share a project, they develop it together*.

## Principles derived, with no home yet

- **A rule amended from a trial takes only what made the trial stop**, not what the trial asked
  about. Applied to the pointer rule; not written into `/skill-up` or `/mechanism`.
- **A table proposing links to a person carries what each link is to**, not only the key — the
  amended Q5 covers questions, not answers or other keyed rows.

## What went wrong, and what it taught

- **Counters stood in for by words.** A reply wrote *🎫 / ❓ / 🐕 как в окне* when the window had
  been cut and its tail not read; another session landed it as rule failure 43, entry contract v86.
- **Bare ids and *как было* in a proposal table**, so the user could judge nothing — rule failure 17
  struck a fifth time; Q5 now says no word stands in for a question the reader has not been shown
  (v88).
- **Question ids in core prose.** `.0010` wrote *q-0035, decision 4* into code comments and the
  product doc's table; core names a question only in a binding. `/verify` did not catch it; the root
  move exposed it, and it was repaired.
- **Jargon to a person.** *Coverage*, *derived*, *orphan* and long English names reached the user
  without explanation; the user said *I don't understand anything* twice before the chain was told
  in plain words.

## Done, briefly

- `.0055` closed: frost_map updated by the user, the trial read, every pointer resolving.
- The question store keeps `realizes`, the `realize` call, `realizes()` with propagation on read,
  and an entry's own `trace_link`; never drawn in the window.
- The `product` mechanism: its doc, its rules file with U1 into `/maintain`, `/product` and the
  document's format, `product.py --check` and `--coverage`; `product.py --check` in the verification
  set.
- The store's roots moved; every id under them renamed by the store; entry contract v87 (bindings
  alone) and v88 (Q5).
- `docs/product.md`: 52 answers, A1–A52; written statuses gone; trace links on every building
  question. The check went 48 diagnostics, 154 orphans, 5 unnamed → 0, 0, 0; coverage 44 in
  progress, 4 present, 4 absent.
- Docs brought to landings of another session: the harness doc for 01-0035.0030's refusal, the
  ticket doc for the mover's interference.

## Open questions touched

- [q-0037.0018](../questions/q-0037.0018-what-is-a-projects-product-document-to-the-method-and-which-of-the-methods-mechanisms-keeps-it.md) — `.0010`, `.0015`, `.0020`, `.0040` done; `.0030`, `.0050`, `.0060`, `.0070` left.
- [q-0033](../questions/q-0033-what-is-this-project-for.md) — now the purpose root; its open
  questions wait as undecided answers A15, A21, A51, A52.
- [q-0037.0010.0009.0004.0002.0001](../questions/q-0037.0010.0009.0004.0002.0001-how-does-code-in-one-repository-name-a-rule-that-a-record-in-another.md)
  — opened from the trial's collector; untouched since.
- [q-0037.0011](../questions/q-0037.0011-does-each-rule-reach-the-occasion-it-is-for.md) — Q5 amended at v88; graded by the next table a session draws.

## What continues

The first step of the next session: `/plan` on
[01-0040.0030 a-decided-purpose-question-opens-its-building](../tickets/done/01-0040.0030-a-decided-purpose-question-opens-its-building.md),
the rules that make a decided purpose question land its answer and open its building question with
a link — so the document stays covered without a session like this one.
