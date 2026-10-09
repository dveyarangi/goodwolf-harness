# What the harness has, or lacks, against its pains — one inventory, 2026-10-09

Built 2026-10-09 by one read-only agent, consolidating what earlier passes found about the
harness's answers to the causes, pains and goals of [the product document](../product.md). It is
meant as the list a future mechanism's output is compared against (q-0018.0011.0004), so it keeps
every item any pass named, deduplicated, and prefers a row too many to a finding lost. It is one
agent's consolidation, not an oracle: the oracle is this list after the person has ruled on each
item.

**Sources**, cited by number in every row:

1. [docs/product.md](../product.md) — the matrix (48 rows), C1–C12, pains 1–3, G1–G2, the harness-pain section.
2. [product-audit-2026-10-09](product-audit-2026-10-09.md) — a read-only sweep of the tree.
3. [q-0033](../questions/q-0033-which-pains-of-developing-software-with-coding-agents-does-the-harness-exist-to-relieve-and-what-answers-each.md) — earlier sortings, the answers table, the chain with Today/Missing.
4. [q-0033.0005](../questions/q-0033.0005-how-does-the-product-document-stay-true-as-mechanisms-and-work-appear-without-the-question-tree-being-forced-into-it.md) — the matrix rows sorted into eight categories.
5. [discover-recall-structure-2026-10-08](discover-recall-structure-2026-10-08.md) — two outside passes: **5A** read the repository cold, **5B** had a functional description only.
6. [peer-capabilities-2026-10-08](peer-capabilities-2026-10-08.md) — the harness's row and the notes on what is rare.
7. [front-page-review-by-outside-agents-2026-10-08](front-page-review-by-outside-agents-2026-10-08.md) — two rounds of cold readers.
8. **8a** [q-0018.0011.0004](../questions/q-0018.0011.0004-how-does-an-arrival-find-what-a-project-exists-to-solve-and-the-answers-it-already-has-in-its-documents-and-its-code.md), **8b** [q-0027.0002](../questions/q-0027.0002-which-questions-stop-for-a-human.md).

**T** marks a claim spot-checked against the tree in this run, by grep or a file read, at
`01cbb85`. Checked: 19 of 24 skills carry `Mechanism: not yet`; five declared mechanisms
(`harness`, `maintain`, `mechanism-shape`, `questions`, `ticket`); no `docs/edge/`; the queue
`docs/tickets/README.md` is 61,977 bytes; `AGENTS.md` is 247 lines, 15,849 bytes; the rule-failure
register holds 26 entries; the sessions file holds 56 `ended` and 10 `running` lines; the wake
(`questions.py` `_wake_read`) lists every other session, ended ones included; the strike is a count
gated by `STRIKE_AFTER = 12h` with no decay, the wake showing `WAKE_STRUCK_LINES = 5`; host hook
files exist only in this repository (`.claude/settings.json`: SessionStart and UserPromptSubmit;
`.codex/hooks.json`: SessionStart, UserPromptSubmit, PostCompact; `.cursor/hooks.json`:
sessionStart and preCompact), and nothing under `.agents/` carries hook wiring for a recipient;
`questions.py` has `_unmarked_suspects` and `_declared` (refusing a moved entry); `straw_dogs.py`
takes `--remove … --expect`; *one step per reply* appears only in `.agents/glossary.md` and
`docs/pacer.md`; the `Host` table in `questions.py` says its rows are "documented, not observed";
every ticket the sources cite exists; question q-0026.0002, cited by source 2, exists nowhere in
the tree.

**Keys.**

*What it is in the tree* — the eight categories of source 4, plus three this inventory needed:

| key | meaning |
|---|---|
| M:`name` | declared mechanism |
| S | undeclared skill (`Mechanism: not yet`) |
| E | rule hand-written in the entry file, no owning rules file |
| I:`name` | rule installed in the entry file by mechanism `name` |
| L | local rule (the project-local block) |
| R | record with a format, no mechanism |
| D | definition only |
| X | behaviour of a declared mechanism's script that no mechanism doc states |
| Q | absent — question only |
| N | absent — no question at all *(added)* |
| H | research record of a process done by hand *(added)* |

*Status* — ✓ in the tree; ◐ partly; ✗ absent; — not applicable.

*In product.md?* — the matrix row it maps to, by the numbers below; **H** the harness-pain section;
**W** the "Who it is for" straw dog; **CE** the "Correction and evaluation" section; *partly* when a
row mentions it without making it its subject; **missing** when nothing in the document names it.

<details><summary>Matrix row numbers P1–P48, in the document's order</summary>

| # | row | # | row |
|---|---|---|---|
| P1 | the question store | P25 | rules written to a form |
| P2 | neighbourhood handed over | P26 | each skill states only what it owns; every output has a reader |
| P3 | position through a compaction and a resume | P27 | whether a rule reaches its occasion observed |
| P4 | session resumes at the step | P28 | a document informs |
| P5 | provisional text bound; suspect answers | P29 | decisions in the architecture; who decided each rule |
| P6 | a question split before answered | P30 | which side wins |
| P7 | a judge outside the agent for placement | P31 | load-bearing written down, the rest in code |
| P8 | a question nobody reaches kept from sinking | P32 | an edited thing carries its mark back |
| P9 | `/align` | P33 | the queue derived, its order the person's |
| P10 | one vocabulary | P34 | a contract per product surface |
| P11 | a task takes its form in its question | P35 | `/maintain` |
| P12 | the load-bearing test | P36 | the rule-failure register |
| P13 | HITL/AFK, spec, breakdown, switches, repair | P37 | a failure replayed as a test |
| P14 | which kinds of decision stop for the person | P38 | the method measured with and without |
| P15 | a record of where models are weak | P39 | its cost counted |
| P16 | visible footing | P40 | `/dream`, `/advise` |
| P17 | guards on model weaknesses | P41 | sessions see each other; store refuses moved entry; own-work commit |
| P18 | guards on the checks | P42 | no session overwrites another's write |
| P19 | delivery | P43 | a starting session takes a free area |
| P20 | the project's checks and who may change them | P44 | one step per reply |
| P21 | a failure traced to its cause | P45 | the work's shape; lighter and heavier paths |
| P22 | what would show a mechanism working | P46 | writes that refuse rather than overwrite |
| P23 | the harness's own tests | P47 | roles bounding permissions |
| P24 | one home per rule, at its tier | P48 | the host refuses |

</details>

---

## A. Answers the harness has or plans

### The shared exploration space

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A1 | Question store: open questions as a tree, each with state, lean, `depends on`, owner | M:`questions` | C3, C4; 1, 2, 3 | ✓ | — | P1 | 1, 2, 3, 4, 5A, 5B, 6 |
| A2 | Every message placed on the lowest question containing it before the reply; five turn kinds; `at`/`open` | I:`questions` (Q1) | C3, C4; 1, 2, 3 | ✓ | — | P1 | 1, 3, 4, 5A, 5B |
| A3 | A missing parent opened; a question reworded when its wording is outdated | M:`questions` | C3; 3 | ◐ rewording open | q-0001.0021 | P1 *partly* | 3, 5A |
| A4 | An uncharted turn put to the person, every reply until answered | I:`questions` | C3, C9; 3 | ✓ | — | P1 *partly* | 3, 5A |
| A5 | Strike count: a return after ≥12 h counted; the wake shows the five most struck | X (`questions.py`) | C4; 3 | ✓ (no decay, T) | — | P1 ("returned to rise") | 1, 3, 5A, 5B, T |
| A6 | Leans: a one-line current leaning per question, written at `/conclude` | M:`questions` | C4; 1, 3 | ✓ | — | P1 | 1, 3, 5A, 5B |
| A7 | Deferral with a stated condition, re-checked at every wake (tickler) | X (`questions.py`) | C4; 3 | ✓ | — | **missing** | 5A, 5B, T |
| A8 | Wake read at session start: most struck, sessions, deferred, straw dogs due, suspects, roots, window | X + host hooks | C4; 1, 2, 3 | ◐ this repository only | q-0018.0020.0005 | P2 | 1, 3, 5A, 5B, 7, T |
| A9 | Per-message window: path to root, children on it, open under the root, other roots and sessions; one line when unchanged; "position, never relevance" | X + host hooks | C3, C4; 1, 2, 3 | ◐ Claude Code, Codex; Cursor at start only | q-0018.0020.0005, q-0018.0023 | P2 | 1, 2, 3, 5A, 5B, 6, T |
| A10 | Hook wiring carried into an installed project, merged into each host's file | Q (RFC on ticket) | C4; 1, 2 | ✗ (T) | q-0018.0020.0005 (.0001, .0002); 01-0010.0173 | P2 *partly* (status text) | 1, 3, 7, T |
| A11 | Position kept through a compaction and a resume under a new session id | M:`questions` | C4; 1, 2 | ◐ one host | q-0001.0006 | P3 | 1, 2, 4 |
| A12 | Fingerprint forgotten at a compaction, so the next window is drawn whole | X + hooks | C4; 1 | ✓ where hooked (Codex PostCompact, Cursor preCompact, T) | — | P3 *partly* | 5A, 5B, T |
| A13 | `/recall` at every wake: reads the queue, last session records, open tickets, architecture, git; follows references "until they converge"; cites where a question is still open or treats it as settled; takes the queue's order, never re-ranks | S + E (straw dog) | C4, C9; 1, 2, 3 | ◐ wake rule is a straw dog | q-0027, q-0027.0001 | **missing** (own row; named in P4's status) | 2, 3, 4, 5A |
| A14 | `/conclude`: session record, leans, `--end` | S | C4; 1, 2 | ◐ nothing makes a session end with it | q-0023.0006, q-0018.0003 | **missing** | 2, 3, 4, 5A |
| A15 | Session records: dated narrative minutes of each session | R | C4, C10; 1, 3 | ✓ | — | **missing** | 3, 5A, 5B |
| A16 | A session resumes the work at the step it stopped (the pacer) | D (`docs/pacer.md`, a document) | C4; 1, 2 | ◐ | q-0027; 01-0020 | P4 | 1, 2, 4, 5A |
| A17 | Straw dogs: provisional text bound to its question; *due* computed at every look; listed at the wake; removal needs `--expect <fingerprint>` | E + X (`straw_dogs.py`) | C3, C6; 3, G1 | ✓ owner open | q-0023.0001 | P5 | 1, 3, 4, 5A, T |
| A18 | Suspect answers: dependents marked when an answer changes; the check reports unmarked suspects; the wake lists them | M:`questions` | C6; 3, G1 | ✓ marking is the agent's call | q-0001.0023 (.0001–.0006) | P5 | 1, 2, 3, 5A, T |
| A19 | A question split into the parts it needs before anyone answers it | Q | C2, C3; 1, 2 | ✗ | q-0001.0020; 01-0011.0100.0050 | P6 | 1, 2, 4, T (rule failure 25) |
| A20 | A judge outside the agent for where a message belongs | Q | C3; 1, 3 | ✗ | q-0001.0016.0001 | P7 | 1, 3, 4 |
| A21 | A question nobody reaches kept from sinking unseen | Q | C4; 3 | ✗ | q-0001.0018 | P8 | 1, 3, 4, 5A |
| A22 | Finished questions archived to `done/`; a close that finishes a subtree moves it | M:`questions` | C4; 2 | ✓ | — | P35 *partly* | 2, 5A |
| A23 | Ids renamed everywhere on a re-parent; the mover repairs citations, so the link graph stays resolvable | X (`questions.py`, `move_doc.py`) | C4, C6; 1, 2 | ✓ | — | **missing** | 5A |
| A24 | The store remembers every id it gave, so a stale id never lands on another question | Q (deferred) | C4, C5; 1 | ✗ | q-0001.0013 | **missing** | 5A |
| A25 | Whiteboard: a question's body gathers material until its form is seen; a ticket minted only then | D; decided, not landed | C3; 1, 2 | ◐ | q-0024.0009.0003.0002; 01-0011.0110.0040.0020 | P11 | 1, 2, 3, 4, 5A |
| A26 | The window test: placement measured on synthetic stores of 795 to 30,000 entries | H (research record) | C3, C7 | ✓ once | — | **missing** | 5A |

### Alignment of intent

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A27 | `/align`: one question at a time with a recommended answer; facts looked up, decisions to the person; stress-tests against the domain model | S | C3, C9, C11; 1, 2, 3 | ✓ | q-0023.0003 | P9 | 1, 2, 3, 4 |
| A28 | Necessity gate: `/align` opens on the present customer, the observable problem, why what exists cannot serve; `/impact` asks "a demonstrated problem? narrower?"; "Build X" is a proposed answer to "what is X for?" | S + M:`questions` | C11, C3; 2 | ✓ | — | P9 *partly* (only `/align`'s opening) | 1, 2 |
| A29 | The necessity gate at project scale: an arrival's align is not done until one difficulty the project solves is found | N (in 8a's body) | C3, C11; 1, 3 | ✗ | q-0018.0011.0004 | **missing** | 8a |
| A30 | Glossaries (method and project) with *Avoid* lists | R (format inside `/align`) | C3; 1, 3 | ✓ | — | P10 | 1, 2, 3, 4, 5A |
| A31 | A term kept out of a record until the glossary defines it | Q | C3; 1, 3 | ✗ | q-0024.0001, q-0024.0001.0001; 01-0017.0010 | P10 | 1, 2 |
| A32 | `/spec`: substantial work gets agreed scope, behaviour and tests before decomposition | S | C3, C8; 1, 3 | ✓ | q-0023.0017 | P13 *partly* ("a spec accepted") | 3, 4 |
| A33 | `/discover`: an outside view before saying what a thing is | S | C2, C11; 1, 2 | ✓ | q-0023.0007 | P17 | 1, 3, 4, 5, 7 |
| A34 | Plain language for the person: P10 opens an align on what a ticket is; `/recall` "no moonspeak"; L6 glyphs as thinking anchors | I:`ticket` + S + L | C10; 3 | ✓ | — | P16 *partly* ("in plain words") | 2, T |

### Decisions placed by their weight

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A35 | The load-bearing test, with its counter-test | E | C2, C8, C9; 1, 2, 3 | ✓ | q-0024.0002.0001 | P12 | 1, 2, 3, 4 |
| A36 | `/impact` routes load-bearing work to the person and a spec, local work to the agent and a ticket | S | C2, C8, C9; 1, 2, 3 | ✓ | q-0023.0010 | P12 | 1, 3, 4 |
| A37 | A raised question settled inside the turn: looked up first; one bearing no load settled and reported; one bearing load to the person; doubt counts as load | M:`questions` (skill text) | C9, C2; 3 | ✓ | — | P12 | 1, 2, 3 |
| A38 | HITL or AFK on every ticket | M:`ticket` | C2, C9; 1, 3 | ✓ | — | P13 | 1, 3, 4 |
| A39 | Human checkpoints: every decision at `/align`, spec accepted, breakdown approved, commit, push, next cycle | E (the loop) | C9; 3 | ✓ | — | P13 | 1, 3 |
| A40 | Switches commit, push, next-cycle, breakdown, repair: `ask` or `auto`, set in the local block | E + L | C9, C12; 2, 3, G2 | ✓ | — | P13 | 1, 2, 3, 4 |
| A41 | Repair fixed and reported only under four stated conditions, otherwise `/align` | E | C9, C12; 3, G2 | ✓ | — | P13 | 1, 3, 4 |
| A42 | Which kinds of decision stop for the person; a HITL/AFK mark on questions; a found, unconfirmed answer is HITL | Q | C9, C2; 2, 3 | ✗ | q-0027.0002 (q-0033.0002 merged in); 01-0020 | P14 (narrower: no mark on questions) | 1, 2, 3, 4, 8a, 8b |
| A43 | An authorization under which the agent may close a question itself; who may close it as a right over the store | Q | C9, C12; 3, G2 | ✗ | q-0027.0002, q-0016 | P14, P47 *partly* | 8a, 8b |
| A44 | A record of where models are known to be weak, deciding which decisions go to the person | Q (pieces in `questions` doc and the register) | C2, C9; 1, 3 | ✗ | q-0033.0001 | P15 | 1, 3, 4 |
| A45 | No reopening a settled decision without new evidence | E | C2; G1 | ✓ | — | P17 | 1, 3, 4, 5A |

### Visible footing

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A46 | Rows heading each reply: the question it ends on, opened, closed, process, uncharted, banter | I:`questions` + L6 | C10, C2; 1, 3 | ✓ under `debug=on` | — | P16 | 1, 3, 4 |
| A47 | Principle marks on paragraphs; proposed-change and proposed-invariant blocks; footnotes for outside grounds | E (straw dog) | C10; 1, 3 | ◐ being graded | q-0030 | P16 | 1, 3, 4 |
| A48 | ⚖️ Decisions and 🍂 Drift tables in every reply that has them | E (straw dog) | C10, C9; 3 | ◐ | q-0030 | P16 | 3, 4 |
| A49 | A ticket named by a link with its slug (P9); a question by id with its wording (Q5) | I:`ticket`, I:`questions` | C10; 3 | ✓ | — | **missing** | T |
| A50 | Who decided each rule, and when | E convention + rules files | C1, C6, C10; 3, G1 | ✓ | — | P29 | 1, 3 |
| A51 | Every step leaves a record (by-product of the delivery skills) | S (by-product) | C10; 1, 3 | ✓ | — | P16 | 1, 2, 3 |

### Guards on known model weaknesses

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A52 | *One shape is not a class*: preserve a seam until a second shape forces the concept | E | C2, C11; 1, 2 | ✓ | — | P17 | 1, 3, 4, 5A |
| A53 | The shape's context and structure explored | E | C2; 1 | ✓ | — | P17 *partly* | 3, 4 |
| A54 | *Occam*: fewest parts, remove before adding | E | C11, C8; 2 | ✓ | — | P17 | 1, 2, 3, 4 |
| A55 | *A capable reader*: state the rule and its pointer, nothing a script or glossary already does | E | C8, C1; 2 | ✓ | — | **missing** | 2, 4 |
| A56 | *Tier is paid by every session*; a skill description names use cases only | E (straw dog) | C8, C1; 2 | ◐ | q-0025.0002 | P24 | 1, 2, 3, 4, 5A |
| A57 | Adversarial planning: the cheapest example that could prove the design wrong; counterexamples (empty, partial, raced); facts apart from assumptions | S (`/plan`, `/align`) | C2; 1 | ✓ | — | P17 | 1, 2 |
| A58 | Guards on the checks: written before the thing and seen to fail both ways; absence is not clearance; zero tests is not a pass; fixtures built the way the real thing came to be | M:`mechanism-shape` (skill) + S (`/verify`) | C7; 1, G1 | ✓ | — | P18 | 1, 2 |

### Delivery and evaluation

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A59 | Tickets with checkable criteria; thin vertical slices; breakdown | M:`ticket` | C3, C7; 1, 2 | ✓ | — | P19 | 1, 3, 4 |
| A60 | `/plan`: an RFC validated against the governing docs and code | S | C6, C7; 1, 2 | ✓ | q-0023.0013 | P19 | 1, 3, 4 |
| A61 | `/tdd`: red, green, refactor | S | C7; 1 | ✓ | q-0023.0018 | P19 | 1, 3, 4 |
| A62 | `/implement`, with a `TODO` naming the question for anything an open answer will change | S | C6; 1 | ✓ | q-0023.0011 | **missing** | 2, 4 |
| A63 | `/verify` against ticket, RFC, docs and the verification set; repair-and-report | S | C7; 1 | ✓ | q-0023.0019 | P19 | 1, 3, 4 |
| A64 | `/commit`: only this session's work; the project's checks run before a code commit | S | C5, C7; 1, G2 | ✓ | q-0023.0005 | P19, P41 | 1, 2, 4 |
| A65 | The verification set, and a rule that a validator is never weakened; where it lives and its shape | S rule + Q | C7; 1 | ◐ | q-0018.0022, q-0018.0022.0001 | P20 | 1, 2, 3, 4 |
| A66 | `/setup-devops`: creates the toolchain and CI the verification set runs | S | C7; 1 | ◐ | q-0023.0015, q-0018.0003.0001 | **missing** | 2, 4 |
| A67 | `/review-architecture`: deepening opportunities | S | 1 | ◐ | q-0018.0003.0002, q-0023.0014 | **missing** | 2, 4 |
| A68 | `/improve-comments`; *document load-bearing, code and comment the rest* | S + E (straw dog) | C6, C8; 1, 2, G1 | ◐ | q-0024.0002.0005, q-0023.0012 | P31 | 1, 2, 4 |
| A69 | A failure traced to its cause — an instruction, a decision boundary, a task's form | R (register) + Q | C7; 1, G1 | ◐ to an instruction only | q-0033.0003 | P21, CE | 1, 2, 3 |
| A70 | Each mechanism names what would show it working, graded by someone who did not build it | M:`mechanism-shape` (Incept step 6) | C7; G1 | ✓ for the five declared | — | P22 | 1, 2, 4 |
| A71 | The harness's own tests catch what their names promise | Q | C7; G1 | ✗ | q-0021; 01-0011.0090 | P23 | 1, 2, 4 |
| A72 | A second look at produced work as one pass: scope, criteria, who, result | Q | C7; 1, G1 | ✗ | q-0029 (.0001–.0004); 01-0030 | **missing** | 2, 3, 7 |
| A73 | A tree's invariants declared as criteria a pass applies | Q | C7, C6; G1 | ✗ | q-0029.0005 | **missing** | 2 |
| A74 | Cold reads by outside agents with personas, doubts fact-checked against the tree before rewriting | H | C7, C10; 1 | ◐ run once by hand; a skill is the user's call | q-0029 | **missing** | 7 |

### Instructions that reach the agent

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A75 | One home per rule: rules files; the installer copies installed blocks to their anchors and checks them | M:`mechanism-shape` + M:`harness` | C1; 1, 2, G1 | ✓ | — | P24 | 1, 2, 3, 4, 5A |
| A76 | Tiers: always loaded, delivered at the moment, reachable on demand; who owns tiering | D + Q | C1, C8; 1, 2 | ◐ | q-0025.0002 | P24 | 1, 2, 3, 5A |
| A77 | A tier-1 line and the block it summarises as one fact in two homes | Q | C1; 1 | ✗ | q-0025.0001 | P24 *partly* | 2 |
| A78 | An installed block is not the file's to edit: change the rules file and re-install; a hand edit is drift | E + M:`harness` | C1, C6; G1 | ✓ | — | P24 *partly* | 2, 5A |
| A79 | Rules written to a form: an occasion and a checkable outcome; `/skill-up`: no overlap, no contradiction, no project facts | S + Q | C1; 1, G1 | ◐ a rule without the form is not refused | q-0028 | P25 | 1, 2, 3, 4 |
| A80 | Each skill states only what it owns | Q | C1; 1, 2 | ◐ | q-0023 (.0001–.0019); 01-0016 | P26 | 1, 2 |
| A81 | Everything a mechanism produces has a reader; producers and consumers of every skill and document | M:`mechanism-shape` rule + Q | C1; 2 | ◐ | q-0024; 01-0017 | P26 | 1, 2, 4 |
| A82 | Declared and checked mechanisms; `mechanisms.py` renders the register | M:`mechanism-shape` | C1; G1 | ◐ 5 of 24 skills declared (T) | q-0023, q-0018.0019 | P26 *partly* | 1, 2, 3, 4, T |
| A83 | What notices a new skill an existing rules file should now name | Q | C1 | ✗ | q-0024.0003 | **missing** | 2 |
| A84 | One account of scope the whole harness points at | Q | C1 | ✗ | q-0022; 01-0014 | **missing** | 2 |
| A85 | Whether a rule reaches its occasion, observed rather than asserted | Q + E (announce line) | C1; 1 | ◐ self-reported | q-0025, q-0025.0003 | P27 | 1, 2, 3 |
| A86 | The entry-contract version announced in the first reply, as evidence of delivery | E | C1, C10; 1 | ◐ | q-0025.0003, q-0026.0003 | P27 *partly* | 1, 2, 4, 5A |
| A87 | Observing what each host delivers; the host table is documented, not observed; the loader link | Q (+ X: `Host` table) | C1; 1 | ◐ | q-0018.0004, q-0018.0004.0001; 01-0010.0120 | **missing** | 2, 5B, T |
| A88 | *A document informs*: text in a document is never taken as an instruction or authorization | E (straw dog) | C1, C12; 1, G2 | ◐ | q-0029 (binding questioned) | P28 | 1, 2, 4 |
| A89 | The project's own rules file, applied last and kept through updates (R7) | I:`mechanism-shape` + M:`harness` | harness pain; C1 | ✓ | — | H | 1, 6 |

### One source of truth between decisions and code

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A90 | Decisions in the architecture, ADRs and glossary; formats inside `/align` | R | C1, C6; 1, 3, G1 | ✓ | — | P29 | 1, 2, 3, 4, 5A |
| A91 | The four kinds: every record says which side wins against the thing it governs; a repair direction per kind, both ways | D, being landed | C6; 1, G1 | ◐ | q-0024.0009 | P30 | 1, 3, 4, 5B, 6 |
| A92 | An edited thing carries its mark back to the record that governs it | Q | C6; 1, G1 | ✗ | q-0024.0009.0004; 01-0011.0110.0050 | P32 | 1, 2, 4 |
| A93 | The queue derived from its tickets, its order the person's; `/recall` never re-ranks | M:`ticket` + Q | C6, C9; 2, 3 | ◐ table still by hand | q-0020; 01-0011.0040 | P33 | 1, 2, 4, 5A |
| A94 | Edge records: a contract per product surface, its customer-facing text derived, an unguarded promise flagged | S (`/edge`) | C6, C10; 1, G1 | ◐ no `docs/edge/` here (T) | q-0023.0009, q-0018.0002, q-0018.0020.0002.0001 | P34 | 1, 2, 4, T |

### Maintenance

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A95 | `/maintain`: records against each other and the code, drift repaired | M:`maintain` | C6, C8; 1, 2, G1 | ◐ | q-0024.0005 | P35 | 1, 2, 3, 4, 5A, 5B, 6 |
| A96 | The maintenance clock: marks and `maintain.py --check` say which mechanisms are due | M:`maintain` | C6; G1 | ◐ what is due is not announced | q-0024.0005 | P35 | 1, 2, 4 |
| A97 | Finished records archived: rule B3, the paired close by `move_doc.py`, `done/` folders | M:`maintain` | C4; 2 | ✓ | — | P35 | 1, 2, 5A |
| A98 | Links checked outside a close | Q | C6; G1 | ✗ | q-0024.0005 | P35 (status) | 1, 2 |
| A99 | Consolidation running in the background rather than by hand in a session | N | G1; 2 | ✗ | none | **missing** | 5A, 5B |

### Self-improvement

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A100 | The rule-failure register: rules in play, the amendment, a repeat strikes the entry; the next occurrence grades the rewording | R + E (straw dog) | C7, C1; 1, G1 | ✓ 26 entries (T) | q-0026 | P36 | 1, 2, 3, 4, 5A, 5B, 6, T |
| A101 | Per-mechanism evidence records | R (per declared mechanism) | C7; G1 | ✓ | — | P22, P36 *partly* | 3 |
| A102 | A recorded failure replayed as a test against the amended rule; what the tester is kept from seeing | Q | C7, C1; 1, G1 | ◐ by hand at times | q-0026.0004, q-0026.0004.0001 | P37 | 1, 2, 3, 4 |
| A103 | Harness self-amendment by stated meta-rules, as its own mechanism | Q | C7, C1; G1 | ✗ | q-0026, q-0026.0001 | **missing** | 2, 4 |
| A104 | The method measured on the same tasks with and without it | Q | C7; 1, G1 | ✗ | q-0017 | P38 | 1, 2, 3, 4 |
| A105 | Its cost counted, and what it saves (cost measured on the front page; savings not) | Q | C7, C8; 2, G1 | ✗ | q-0018.0008; 01-0010.0168 | P39 | 1, 2, 3, 4 |
| A106 | `/dream`: a free pass over the record for principles, hidden edges, imbalance | S | C7; G1 | ◐ experimental | q-0023.0008, q-0018.0003 | P40 | 1, 2, 4, 5A |
| A107 | `/advise`: a strategic read | S | G1 | ◐ | q-0023.0002, q-0018.0002 | P40 | 1, 2, 4 |
| A108 | `/skill-up`: the writing rules for any instruction | S | C1; 1 | ✓ | q-0023.0016 | P25 | 2, 3, 4 |
| A109 | `/mechanism`: what counts as a mechanism; incept, declare, check, retire | M:`mechanism-shape` | C1, C7; G1 | ✓ | — | P22, P26 *partly* | 2, 4 |
| A110 | A failure or an improvement found in a project reaches the harness | Q | C7; G1 | ✗ | q-0018.0014, q-0018.0018; 01-0010.0205 | H | 1, 2 |

### Coordination between sessions

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A111 | A shared sessions file: each session sees where the others stand | M:`questions` | C5; 1, 2 | ◐ one working directory | q-0018.0015 | P41 | 1, 2, 3, 4, 5A, 5B, 6 |
| A112 | The store refuses a write to an entry that moved since it was read | X (`questions.py` `_declared`, T) | C5, C12; G2 | ✓ | — | P41 | 1, 3, 4, T |
| A113 | No session overwrites another's write (locks are one way) | Q | C5, C12; 1, 2, G2 | ✗ | q-0032 | P42 | 1, 2, 3, 4, 6 |
| A114 | A starting session takes an area no other session is in | Q | C5; 2 | ✗ | q-0016.0001 | P43 | 1, 3, 4 |
| A115 | A session's held context invalidated when another session changes a record it holds | N | C5; 1, 2 | ✗ | none (q-0032 is the write side) | **missing** | 5B |
| A116 | Several people steering agents on one project | Q | all pains | ✗ | q-0033.0004 | W | 1, 2, 6, 7 |

### Process weighed to the work

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A117 | One step per reply, with a point to reassess at its end | D (glossary, `docs/pacer.md`, T) | C8, C9; 2, 3 | ◐ defined, not instructed | q-0027; 01-0020 | P44 | 1, 2, 3, 4, T |
| A118 | A lighter path for small work and a heavier one for large; `/impact` recommends the work's shape | Q | C8; 2, 3 | ✗ | q-0027.0003, q-0018.0001; 01-0010.0080 | P45 | 1, 2, 3, 4, 6, 7 |
| A119 | A control component that schedules the skills (the pacer as a blackboard's control) | D ("idea under alignment") | C8, C4 | ✗ | 01-0020, q-0027 | P4, P44 *partly* | 2, 4, 5A |

### Refusing harm

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A120 | Writes that refuse rather than overwrite: a refusal writes nothing; interference is a failure, never permission; the installer refuses rather than guesses; a retraction leaves the file byte-identical | X (contract in `docs/architecture.md`) | C12; G2 | ✓ / ◐ (see C1) | — | P46 | 1, 2, 4, T |
| A121 | D3: never invent a past fact; preserve the facts an archived record holds | M:`maintain` rule (T) | C10; G1, G2 | ✓ | — | **missing** | 2, T |
| A122 | Push waits for a yes, and only `/conclude` asks | E switch | C12; G2 | ✓ | — | P46 | 1, 2 |
| A123 | An agent's role bounding its permissions, its rights over the records and its skills | Q | C12, C5; G2 | ✗ | q-0016 | P47 | 1, 2, 4 |
| A124 | The host refuses an action a rule forbids | Q | C12; G2 | ✗ | q-0018.0005 | P48 | 1, 3, 4, 7 |
| A125 | Secrets kept from leaking — G2 names it; nothing answers it | N | G2 | ✗ | none | **missing** (G2 text only) | 1, 3 |

### The harness's own pain: fit and update

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A126 | `harness.py --check`: the installed copy matches its release | M:`harness` | harness pain | ✓ | — | H | 1, 2, 4 |
| A127 | The leak check: core never depends on a project's own documents | M:`harness` (ref gate) | harness pain; C1 | ✓ a bare-id case open | q-0018.0017 | H | 1, 2 |
| A128 | An update stops rather than overwrite a hand edit | M:`harness` | harness pain; G2 | ✓ | — | H | 1, 2 |
| A129 | An install meets an existing `CLAUDE.md`/`AGENTS.md`: moved aside, one mode only | M:`harness` | harness pain | ◐ | q-0018.0020.0001, .0001.0001 | H | 1, 7 |
| A130 | An install drafts an architecture and glossary from the project's material | Q | harness pain; C3 | ✗ | q-0018.0011 (.0001–.0003); 01-0010.0175 | H | 1, 2, 7 |
| A131 | An arrival finds what the project exists to solve: an align on pains and causes, then a pass over docs and code whose findings become questions hung under the causes (a generated question tree) | Q | C3, C6; harness pain | ✗ | q-0018.0011.0004 | **missing** (H names q-0018.0011 only) | 4, 8a |
| A132 | Causes the person has not recognized found by discovery, owned by the root that keeps the landscape and evolution | N | C3 | ✗ | none | **missing** | 8a |
| A133 | A first install ends with the project's own verification set | Q | harness pain; C7 | ✗ (rule failure 26, T) | q-0018.0020.0003; 01-0010.0170 | H | 1, 2, T |
| A134 | A recipient's own mechanisms have a declared home and are checked like the shipped ones | Q | harness pain; C1 | ✗ | q-0018.0019 | H | 1, 2 |
| A135 | An update says what changed and what the project must do; releases | Q | harness pain | ✗ | q-0018.0020.0002 (.0002, .0003); 01-0010.0160, .0185, .0190, .0195 | H | 1, 2 |
| A136 | What maintenance re-checks for the harness inside a project | Q | harness pain | ✗ | q-0018.0012; 01-0010.0180 | H | 1, 2 |
| A137 | A shipped skill's name colliding with a project's own command | Q | harness pain | ✗ | q-0018.0020.0001.0002 | H | 1, 2 |
| A138 | A project changes how it builds in one edit | Q | harness pain | ✗ | q-0024.0002; 01-0017.0020 | H | 1, 2 |
| A139 | Uninstall | Q | harness pain | ✗ | q-0018.0013 | H | 1 |
| A140 | More hosts than three | Q | harness pain | ◐ three of fifteen to fifty | q-0018.0023 | H | 1, 2, 6, 7 |
| A141 | An install removes its own block from a file it no longer names | Q | harness pain; C1 | ✗ | q-0024.0010; 01-0011.0120 | **missing** | T |

### The product document itself

| # | item | what it is | serves | status | waits on | product.md | sources |
|---|---|---|---|---|---|---|---|
| A142 | A product mark on questions (`product C…`, `structure`, `evolution`), collected at a release into the note's product half; the matrix derived, not hand-kept | Q (intention) | C6, C10; G1 | ✗ | q-0033.0005; 01-0010.0190 | **missing** | 4 |
| A143 | An owner of `docs/product.md`'s coherence in clean core (a painted door) | Q | C1, C6 | ✗ | q-0033.0005 | **missing** | 4 |
| A144 | The harness's own historical rules counted as seed, reflected as straw dogs until the meta-rules mechanism owns them | D (decided) | C1 | ◐ | q-0026, q-0026.0001 | **missing** | 4 |
| A145 | Correction and evaluation together: work evaluated against its criteria and checks, a failure correcting whatever let it through | D (cross-cutting) | all; C7 | ◐ | q-0033.0003 | CE | 1, 2, 3 |
| A146 | `/celebrate` | S | no cause | — | q-0023.0004, q-0018.0002 | **missing** (rightly) | 2, 4 |

---

## B. Weaknesses found in what exists

| # | weakness | affects | evidence, source | open question |
|---|---|---|---|---|
| B1 | The strike count never decays, so old heavily struck questions keep their rank; frequency without decay entrenches | A5, A8 | 5A (family F), 5B (F2, F6); T: count gated by 12 h, no decay | **none** (recorded in q-0031's body; q-0001.0018 is the opposite face) |
| B2 | A revisit count mixes two signals: important or stuck | A5 | 5B (F2) | **none** |
| B3 | The wake grows without bound: one line per session ever registered, ended ones included; 104 lines, 10.8 KB at `369cd8b` | A8 | 5A measured; T: `_wake_read` lists every other session, 56 ended lines | **none** (recorded in q-0031) |
| B4 | Stale presence markers: a session that crashed still reads `running` and misleads the others | A111 | 5B (F6); T: 10 `running` lines | **none** |
| B5 | Hubs accrete: the queue every `/recall` reads was 58 KB, its history line 36 KB | A13, A93 | 5A measured; T: 61,977 bytes now | q-0020 partly (deriving the table); size **none** |
| B6 | The agent may not take a hub's prose as its criterion: a recall ranked by its own criterion (rule failure 14) | A13, A93 | 5A from the register | **none** |
| B7 | `/recall`'s stopping rule "until they converge" has no count | A13 | 5A (family B) | **none** |
| B8 | Needs shift during the search (berrypicking) | A13 | 5A | **none** |
| B9 | Navigation by exact ids and links misses paraphrase; no content search; concept search is where the design is expected to lose | A13, A23 | 5A, 5B (Cursor, turbopuffer measurements) | **none** (finding recorded in q-0031) |
| B10 | Single-parent placement forces one home on a message that has two; rule failure 18: five amendments, four strikes in one day | A2, A1 | 5A (family C), 5B (F3, "a city is not a tree") | q-0001.0016.0001 partly; multi-parent **none** |
| B11 | A wrong placement makes the next push wrong; errors at upper levels of a hierarchy spread downward | A2, A9 | 5B (Silla & Freitas) | q-0001.0016.0001 |
| B12 | How often the gate classifies correctly is not measured, beyond the synthetic window test | A2, A26 | 5B | q-0001.0016.0001 partly |
| B13 | Nothing measures whether a pushed line was used, or what the session fetched that the push missed | A8, A9 | 5B (F1, rung 5) | **none** (q-0025 covers rules, not the window) |
| B14 | Locality prefetch helps only if tree adjacency matches how work moves | A9 | 5B (F1) | **none** |
| B15 | Spreading activation reaches only items with an edge to the focus | A9 | 5B (F2) | **none** |
| B16 | Pushed context rots as it grows; similar-but-irrelevant material misleads | A8, A9, A75 | 5A, 5B (Chroma) | q-0018.0008 partly |
| B17 | The entry file is above the host's recommended size (under 200 lines): 232 lines, 15 KB then | A75, A76 | 5A; T: 247 lines, 15,849 bytes now | q-0025.0002, q-0018.0008 partly |
| B18 | About 31 KB is pushed before the first pull (entry file, 24 descriptions, wake) | A8, A75 | 5A measured | q-0018.0008 |
| B19 | Context files may lower task success and raise cost over 20%; the evidence is mixed | whole approach | 5A, 5B (ETH Zurich 2026 and two other studies) | q-0017, q-0018.0008 |
| B20 | Adherence falls as instruction count rises; per-message pushes add to the density | A75, A9 | 5B (IFScale) | q-0025.0002 partly |
| B21 | A pushed copy goes stale against its source: a pass was preloaded v33 while `HEAD` was v34 | A86, A75 | 5A observed | q-0025.0003 partly |
| B22 | Expressive ids are not stable identity: a re-parent renames them, and an old id held elsewhere lands on another question | A23, A24 | 5A (family C) | q-0001.0013 (deferred) |
| B23 | Early structure biases later classing | A1 | 5A | **none** |
| B24 | Hierarchical directories lost to search as corpora grew; the store had 121 live entries | A1 | 5A; T: 146 live entry files now | **none** |
| B25 | An unrecorded dependency means silent staleness ("a skipped question is found by impasse") | A18 | 5A (family D) | q-0001.0023.0003, q-0001.0023.0005 |
| B26 | Recording justifications costs a call per event | A18, A2 | 5A | q-0018.0008 partly |
| B27 | Invalidation spreads too far | A18 | 5A | q-0001.0023.0002 |
| B28 | Invalidate when written or verify when used is not chosen | A18 | 5A (Zep against Copilot) | q-0001.0023.0006 |
| B29 | Marking suspects is the agent's call | A18 | 2 | q-0001.0023.0002 |
| B30 | Capture burden and the writer–beneficiary asymmetry; the person still pays to read | A1, A15, A90 | 5A (family E), 5B (F3) | q-0018.0008 partly |
| B31 | Rationale stores grow faster than they are read | A15, A90 | 5A | **none** |
| B32 | Typed fields (state, owner, parent, dependency) are where the literature predicts drift | A1 | 5B (F3) | **none** (the store's check covers form only) |
| B33 | A trusted system fails when review lapses; capture inflates until review is abandoned; deferred lists grow without bound; clarifying becomes ceremony | A1, A7, A2 | 5A (family G), 5B (F8) | q-0001.0018 partly; ceremony q-0027.0003 |
| B34 | Consolidation (`/maintain`, `/dream`, rewording) runs only by hand in a session | A95, A106, A100 | 5A, 5B | **none** |
| B35 | Context collapse: iterative rewording of a self-maintained playbook erodes detail | A100 | 5B (ACE) | q-0026.0004 partly |
| B36 | Self-reference: the system maintains its own desired state with no outside check | A91, A100 | 5B (F7, F9) | q-0017, q-0029.0003 partly |
| B37 | Desired state goes stale: a permanently authoritative decision enforces something obsolete | A90, A45 | 5B (F7) | q-0001.0023.0005 partly |
| B38 | A record of ambiguous kind makes two repair directions fight | A91 | 5B (F7) | q-0024.0009 |
| B39 | Drift accumulates between periodic resyncs | A95 | 5B (F7) | q-0024.0005 partly |
| B40 | Nothing invalidates a session's held context when another session writes | A111, A115 | 5B (F1, rung 6) | **none** |
| B41 | Write contention and lost updates on a shared file | A111, A113 | 5B (F6); 6 (awareness without locks) | q-0032 |
| B42 | The push depends on host hooks: none in an installed project, none per message in Cursor; without hooks recall falls back to a static file | A8, A9, A10 | 2, 5A, 5B, 7; T | q-0018.0020.0005, q-0018.0023 |
| B43 | The receiver restates the incoming request, not the inherited state; nothing checks that a session took in the handoff | A8, A13 | 5B (F5, I-PASS) | **none** |
| B44 | Handoffs become copy-forward: stale items carried without re-verification | A15, A6 | 5B (F5) | **none** |
| B45 | No published evaluation exists of a position-keyed per-message push or a mandatory placement gate | A2, A9 | 5A, 5B | q-0017 partly |
| B46 | Hosts load the entry file into every subagent, so no outside pass is blind | A33, A74 | 5, 7 | **none** |
| B47 | Window fingerprints sit in the system temp directory, shared across trees; one pass deleted the live tree's | A9, A12 | 5 (intro) | **none** |
| B48 | Rules are instructions, not enforcement; the page's absolute promises contradicted it | A40, A120, A124 | 7 | q-0018.0005 |
| B49 | The self-change claim had no evidence: who notices a miss, does a rewording hold? | A100 | 7 | q-0026.0004, q-0017 |
| B50 | No fast path; the workflow's weight was hidden | A118 | 6, 7 | q-0027.0003 |
| B51 | `CLAUDE.md` moved aside at install, a disqualifier for readers | A129 | 7 | q-0018.0020.0001.0001 |
| B52 | No team support, a disqualifier | A116 | 6, 7 | q-0033.0004 |
| B53 | Three hosts against fifteen to fifty; one author, one month old | A140 | 6, 7 | q-0018.0023; age **none** |
| B54 | 19 of 24 skills are undeclared; the matrix credits general rules and undeclared skills as mechanisms | A82, matrix | 2, 4; T | q-0023, q-0033.0005 |
| B55 | *A document informs* is bound to q-0029, a binding the audit reads as wrong | A88 | 2 | **none** |
| B56 | What is due is never announced; links are checked only when records move | A96, A98 | 1, 2 | q-0024.0005 |
| B57 | Nothing makes a session end with `/conclude`; the wake rule is a straw dog | A13, A14 | 2 | q-0027 |
| B58 | A rule without an occasion and outcome is not refused | A79 | 1 | q-0028 |
| B59 | Delivery evidence is self-reported by the agent | A85, A86 | 1, 2 | q-0025.0003, q-0018.0004.0001 |
| B60 | The host table is documented, not observed | A87 | T | q-0018.0004 |
| B61 | The guarded-writes contract lives in `docs/architecture.md`, this project's own document, not in core | A120 | 4 | **none** |
| B62 | Matrix rows mix kinds and are not maintained; a new mechanism or work appearing with no row is caught by nothing | the product document | 4 | q-0033.0005 |
| B63 | A mark people must fill in tends toward a cause chosen just to have one | A142 | 4 | q-0033.0005 |
| B64 | Comparing two generated lists measures their agreement, not their truth | A131, this list | 2, 8a | q-0018.0011.0004 |
| B65 | A first install took the harness's own check as a recipient's verification set (rule failure 26) | A133 | T | q-0018.0020.0003 |
| B66 | Answers proposed four times on a question whose parts were not unfolded (rule failure 25) | A19 | T | q-0001.0020 |
| B67 | Works today and Not yet contradicted each other on drafting the architecture; the ✦ claim could not be checked | A130, front page | 7 | q-0018.0011, q-0031 |

---

## C. Disagreements between sources

| # | item | one reading | the other |
|---|---|---|---|
| C1 | Guarded writes (A120) | 1: ✓ | 2: ◐; 4: script behaviour no mechanism doc states, its contract in an instance document |
| C2 | G2's answers | 3: "G2 has no answer at all"; "the only answer today is trust" | 1, 2: guarded writes and the switches answer it |
| C3 | What would show a mechanism working (A70) | 1: ✓, "every mechanism" | 2: ✓ only for the five declared; 4: a derived matrix shrinks to five |
| C4 | *Document load-bearing, code the rest* (A68) | 2: ✓, though straw-dogged | 1: ◐ "a rule, not yet settled" |
| C5 | *A document informs* (A88) | 1: bound to q-0029 | 2: that binding looks wrong |
| C6 | Edge records (A94) | 1: waits on q-0023.0009 | 2: also q-0018.0002 |
| C7 | Orientation at start and per-message push (A8, A9) | 6: harness row Y and Y, "rare" | 1: ◐ two hosts of three, an installed project fetches by rule; 5A: Cursor at start only; 7: the page's claim of hooks in installed projects was false |
| C8 | Drift checked and repaired (A95) | 6: Y | 1: ◐ |
| C9 | A failed instruction leads to its amendment (A100) | 6: Y, rare in the field; 1: ✓ | 5B: run by hand, with context-collapse risk; 7: no evidence that a rewording holds |
| C10 | What a matrix row is | 1: "Each row is a mechanism" | 4 (the user): the full matrix "is full of mechanisms that are not mechanisms"; 2 §5: several rows are implementation detail |
| C11 | Pain columns per answer | 3: visible footing serves 1, 2, 3; HITL 1, 3; switches 2, 3; guards C2 only, 1, 2; tiers 1, 2; coordination C5 only | 1: visible footing 1, 3; HITL and switches merged, 1, 2, 3, G2; guards C2, C11, 1, 2, 3; tiers 1, 2, G1; coordination C5, C12, G2 |
| C12 | Scope of C4 | 3: lost between sessions | 1 (after 2 §4): also at a compaction and a resume under a new identity |
| C13 | The register's size | 3: 22 entries | T: 26 |
| C14 | Sizes measured | 5A: queue 58 KB; entry file 232 lines, 15 KB; 121 live entries | T: 61,977 bytes; 247 lines, 15,849 bytes; 146 live entry files |
| C15 | Audit corrections not carried into 1 | 2: guarded writes ◐; the q-0029 binding wrong; "where knowledge lives" ✓; arrival harvest and reporting upstream as separate open parts | 1: guarded writes ✓; q-0029 kept; ◐; harness pain names q-0018.0011 and q-0018.0014 only, not q-0018.0011.0004 or q-0018.0018 |
| C16 | The audit's own check | 2: "every question id it cites exists and is open" | T: q-0026.0002, which it cites, exists nowhere in the tree — not the audit's error: it existed when the audit ran and was re-parented to q-0026.0004.0001 the same day, after the audit was filed with the old id |
| C17 | Decision kinds and the HITL mark (A42) | 1: P14, the project says which kinds of decision stop | 8a, 8b: a HITL/AFK mark on questions and an authorization under which the agent closes some itself — wider than P14 |
| C18 | Position through a compaction (A11, A12) | 2: landed for Claude Code only; 1: ◐ in one host | T: Codex and Cursor carry compaction hooks that redraw the window; keeping a position under a new id is what is single-host |
| C19 | A second look as one pass (A72) | 3: missing, part of correction and evaluation | 2 §5: restructures `/verify` and `/maintain` rather than answering a cause |
| C20 | One step per reply (A117) | 2 (on `aa54092`): ✓ should be ◐ | 1 now ◐; 4: definition only — settled since |
| C21 | `/dream` (A106) | 2: experimental | 1: in use, not declared; 5A: consolidation by hand, once a day |
| C22 | The pacer (A16, A119) | 2: resumption bound to 01-0020 | 4: `docs/pacer.md` is a document, which informs; 5A: "idea under alignment", so no control component exists |

---

## D. Counts

Counted by a script over the tables above.

- **Items in A:** 146.
- **By status:** ✓ 60; ◐ 40; ✗ 45; — 1 (`/celebrate`). A120 is counted ✓, with the audit's ◐ in C1.
- **By what it is**, each item under its first key:

  | key | count |
  |---|---|
  | Q (absent — question only) | 44 |
  | M (declared mechanism) | 25 |
  | S (undeclared skill) | 24 |
  | E (entry-file rule) | 18 |
  | X (script behaviour) | 8 |
  | D (definition only) | 8 |
  | I (installed rule) | 6 |
  | R (record with a format) | 6 |
  | N (absent — no question) | 5 |
  | H (research record) | 2 |
  | L (local rule) | 0 as a first key; 2 as a second |

- **In product.md:** 98 map to a matrix row, 17 of them only *partly*; 15 to the harness-pain
  section; 1 to the team straw dog; 1 to the correction-and-evaluation section. **31 are
  missing**, one of them rightly (`/celebrate`).
- **Weaknesses in B:** 67. 26 carry **none** for all or part of them; 19 have no open question at
  all.
- **Disagreements in C:** 22.

## E. Added on a second check — findings not on disk when the inventory was built

The consolidating agent read only files. Two sources were not on disk:

- **The cold readers' raw reports.** Four reports — a solo developer and a sceptical tech lead,
  two rounds of each, 2026-10-08 — exist only in the conversation. Their record on disk is a
  summary.
- **Statements made in this conversation** that no record had yet carried.

The agent that ran the conversation added these items on 2026-10-09, after a search of the
inventory for each found no row. Numbering continues A.

| # | item | what it is | serves | status | waits on | in product.md? | source |
|---|---|---|---|---|---|---|---|
| A147 | the micromanagement end of the agency scale measured: how many stops for the person's yes a day of work costs at the defaults | absent, no question | 3, 2 | ✗ | none (nearest q-0018.0008, q-0027.0002) | **missing** | cold read, tech lead |
| A148 | an install meeting an existing entry file in two modes: the harness takes over and absorbs the project's rules, or it is added by one import line | absent, question only | harness pain | ✗ | q-0018.0020.0001, q-0018.0020.0001.0001 | partly (one mode named) | the user, 2026-10-08 |
| A149 | loader links that work on Windows without elevation, and a teammate's fresh clone that does not check them out as text files | script behaviour, partial | harness pain, 2 | ◐ | q-0018.0004.0001, q-0018.0020.0006 | **missing** | cold reads, both rounds; adoption panel 2026-09-26 |
| A150 | the cost of placing every message measured: tokens and latency per reply | absent, question only | 2, C8 | ✗ | q-0018.0008 | **missing** | cold read, round 2 |
| A151 | the context a fresh project's session reads, measured rather than estimated | absent, question only | 2, C8 | ✗ | q-0018.0008 | **missing** (the README gives an estimate) | cold read, round 2 |
| A152 | a bound on rules piling up as rewordings land: pruning, a budget, contradiction found | absent, no question (the register says *nothing here authorises deleting a rule*; q-0026.0001's lean refuses deletion on repeated failure) | G1, C1 | ✗ | none | **missing** | cold read, tech lead |
| A153 | who notices that a rule did not fire — in practice the person, which spends the person's attention | entry-file rule (self-improvement), partial | 3, C7 | ◐ | q-0026 | **missing** | cold read, tech lead |
| A154 | in an installed project, where a rewording lands: the project's local rules, or a core file the next update would stop on | absent, question only | G1, harness pain | ✗ | q-0018.0018, q-0026 | **missing** | cold read, tech lead |
| A155 | a project's override meeting an update that changed or removed the rule it overrides | absent, no question | harness pain | ✗ | none (nearest q-0018.0020.0002) | **missing** | cold read, tech lead |
| A156 | the weight of the method's vocabulary on the person: the number of commands and coined terms a reader meets | absent, no question | 2, 3, C8 | ✗ | none (nearest q-0024.0001) | **missing** | cold reads, both rounds |
| A157 | the README's claims held to the tree, so the front page cannot promise hook delivery an install lacks | absent, question only | C10 | ✗ | q-0031 | **missing** | the second cold read's fact-check, 2026-10-08 |

**Section D after E:** 157 items; 41 missing from product.md.

**A disagreement resolved after E.** C's reading that the audit's *the q-0029 binding on "a
document informs" looks wrong* is refuted by the record. The rule was written on 2026-10-05 as a
straw dog *until what holds a tree's invariants is settled* (`entry-contract-findings.md`, v31).
That is q-0029 and, precisely, q-0029.0005 "Where are a tree's invariants declared as criteria a
pass applies?". The binding stands.

## F. The rule-failure register, entry by entry

Added 2026-10-09 at the user's request. One read-only agent read `docs/rule-failures.md` whole,
checked each entry's state against the tree on disk (`AGENTS.md` at v49), and mapped it onto the
causes and onto section A. Every question id below exists and is open.

| # | entry | date | rules in play | weakness, said generally | cause | state now | inventory | open question |
|---|---|---|---|---|---|---|---|---|
| 1 | a concern written where a ticket was wanted | 09-10 | the ticket format against `/align`'s old *concerns* clause | two rules each satisfiable, no boundary; salience won | C1 | proposed, not landed — overtaken: the concerns file is gone, questions go to the store | A1, A103 | **none** for the boundary |
| 2 | a partial sweep reported as a settled count | 09-10 | `/maintain` B1, B2 | a rule scoped to one skill, its occasion everywhere | C1, C10 | not landed; routed to 01-0018, still open | A95, A85, A76 | q-0025 |
| 3 | the straw-dog rule at tier 1, three straw dogs unwrapped | 09-14 | entry file *Straw dogs*; `/mechanism`'s three homes; R5 | imperative buried; a home table admitting the wrong category; one occasion of two | C1, C6 | landed, struck twice, amended after each | A17, A75 | q-0023.0001 |
| 4 | the wake rule in a diagram; a greeting got a greeting | 09-20 | the loop diagram; `docs/pacer.md` | an instruction with no verb; the sentence rule scoped too narrowly | C1, C4 | landed (v9), graded: *the rule fired*; reworded since by 23 | A13, A16 | q-0027 |
| 5 | "allowlist", so a list was built | 09-20 | R4, R6; *authored home* | a noun naming an artifact beat a prohibition worded with another noun | C1, C11 | landed; never graded | A75, A81 | **none** |
| 6 | the binding form on two tickets; bare ids on six closed ones | 09-20 | decisions held only on tickets → *Core and instance*, *Straw dogs* | a decision held only in read-once records; the first fix repeated the fault | C1, C6 | landed (v12) in two steps; not graded | A127, A17 | q-0018.0017 |
| 7 | a declaration named its script's verbs | 09-23 | *Document load-bearing*; the format's title line; `/maintain` scope | text beside its implementation takes its words | C1, C6 | landed, struck once, amended (v19); residue: `harness` still has no rules file | A55, A82, A136 | q-0018.0012 |
| 8 | a nested skill's output contract ended the caller's turn | 09-23 | `/ticket` steps; `/impact`'s *Output only* | two output contracts, no precedence; the last read won | C1 | landed; not graded | A36, A59 | **none** |
| 9 | a fixture made by today's code stood for yesterday's tree | 09-24 | `/verify`'s validator bullet | the rule checks the assertion, not where its fixture came from | C7 | landed, with a code fix; not graded | A58 | q-0021 |
| 10 | a claim about what sets the harness apart, drafted from inside | 09-26 | `/discover`'s description; `/align`'s external reality; *shape context* | the sharpest occasion in the body, not the description; an outside check met by sources sharing the frame | C2, C1 | landed; not graded | A33, A56 | q-0023.0007; q-0025.0002 in part |
| 11 | a copy step landed in the architecture | 09-26 | the load-bearing counter-test; `/plan`'s architecture rule | an unqualified noun skipped a test in another file | C1, C11, C8 | landed, struck once, amended | A35, A60, A68 | q-0024.0002.0005 |
| 12 | a queue answer named tickets by position | 09-26 | P9; the slug rule; the queue's link text | met by the letter, failed the reader; copied from a hub that broke it | C1, C10 | landed, reworded twice, replayed four times; residue: queue rows carry no slug | A49, A93, A102 | q-0020; q-0026.0004 |
| 13 | skill descriptions fixed by adding their method | 09-27 | the tiering rule; R8 | a permissive phrase read as licence | C1, C8 | landed; *not yet replayed* | A56, A80 | q-0025.0002 |
| 14 | a recall ranked by a criterion the queue does not use | 09-27 | the ordering rule in the queue's prose; `/recall` | a criterion in a document's prose read as state; the skill named none | C9, C2, C1 | landed, reworded the same day; *not yet replayed* | A13, A93 | q-0027; q-0020 |
| 15 | a record's format placed in a mechanism's doc | 09-27 | `/mechanism` three homes and records; the format's §Records | three statements of one rule disagreed; the most specific won | C1 | landed; *not yet replayed* | A109, A75 | **none** (nearest q-0024.0004) |
| 16 | placing stopped once the window said nothing moved | 10-03 | Q1; the hook's unchanged line | the rule buried at session start; the text at the occasion read as nothing to do | C1, C10 | landed | A2, A9, A85 | q-0001.0016; q-0025 |
| 17 | a reply named what it asked by bare ids | 10-03 | P9; no rule for question ids → Q5 | a rule's slot reached one kind and not the kind derived from it | C10, C1 | Q5 landed (v24); P9 left as a repeat to strike, not struck | A49 | **none** |
| 18 | six turns of seven showed the wrong question | 10-05 | Q1; the skill's *missing parent* | a judgement with nothing to count; a case missing; the rule in a skill not opened | C1, C3, C2 | landed (v26), struck four times in one day, amended after each | A2, A3 | q-0001.0016; q-0001.0016.0001 |
| 19 | a stale handoff reported as drift | 10-08 | `/recall`'s snapshot bullet against its drift bullet | the exemption in one bullet, the occasion read in another | C1 | landed (v39) | A13, A15 | **none** |
| 20 | a landed rule copied into the host's memory | 10-08 | the host's memory instructions; *Self-improvement* → L7 | the governing rule outside the tree; habit won | C1 | landed (v40), L7 | **none** (nearest A75) | **none** |
| 21 | a reply spoke of the push the conclude owns | 10-08 | the `push` switch; `/conclude` | one verb named, neighbouring acts uncovered | C1 | landed (v41) | A122 | **none** |
| 22 | a lamp cited a rule's id | 10-08 | *A paragraph shows what it stands on* | a placeholder filled loosely; the sentence on names above the bullet read | C10, C1 | landed (v42), reworded since — whether v49's wording regressed needs a judgement | A47 | q-0030 |
| 23 | a rollback ran `/recall` twice | 10-09 | the wake straw dog; the hook's start read | an ambiguous term — session as the host's id or the conversation | C4, C1 | landed (v43) | A11, A13 | q-0027; q-0001.0006 |
| 24 | landed text quoted without its 🧩 | 10-09 | the 🧩 bullet | *proposed* read as excluding text just landed — a boundary in time | C10, C1 | landed (v44) | A47 | q-0030 |
| 25 | answers proposed four times on an unfolded question | 10-09 | `/questions` *Branching*; the ⚖️ table | a trigger the agent is known to fail at, with no sign named; an output owed every reply pulled toward a decision | C2, C3, C9 | landed | A19 | q-0001.0020 |
| 26 | a project with no code got the harness's check as its set | 10-09 | the harness skill's *after the first install*; `harness.md` | an optional example, the only concrete command in reach, read as the default; the empty case unnamed | C1, C7, C11 | landed | A133, A65 | q-0018.0020.0003; q-0018.0022.0001 |

**State counts:**

| state | entries |
|---|---|
| landed, never struck | 20 |
| landed and later struck | 4, with 8 strikes; amended after every strike |
| proposed or routed, not landed | 2 (1 overtaken, 2 routed to 01-0018) |
| refused | 0 |

Grading: one entry graded (4, it fired), one replayed (12), three marked *not yet replayed*
(13, 14, 15). The rest record no grade.

**Patterns across entries:**

- **Wording filled loosely, or met by its letter:** 5, 7, 12, 13, 17, 21, 22, 23, 24, 26.
- **The rule's home not read at its occasion** — wrong tier, file or bullet, or a scope narrower
  than the behaviour: 2, 4, 10, 11, 12, 16, 18, 19, 20, 22.
- **Two satisfiable rules with no boundary or precedence:** 1, 3, 8, 15, 25.
- **A rule or decision held in a document, record or diagram instead of an instruction:**
  3, 4, 6, 12, 14.
- **A judgement with nothing to count, where models are weak:** 10, 11, 18, 25.
- **One occasion bound, a second missed:** 3, 9, 24.
- **Text beside its implementation takes its shape:** 7, 9, 11.
- **Copying from a source just read:** 12, 14.
- **The fix repeated the failure:** 4, 6.
- **The person is the detector every time:** all 26 were caught by the user, or by a hunt the user
  asked for.
- **Amendment churn:** 18 landed five times in a day, 3 three times; every amendment adds text and
  none removes any.

**Weaknesses the register adds to section B**, numbered on:

| # | weakness | evidence | open question |
|---|---|---|---|
| B68 | rules each satisfiable with no stated boundary or precedence between them | entries 1, 3, 8, 15, 25 | **none** (nearest q-0023) |
| B69 | a rule's placeholder or noun filled loosely, or met by its letter | 5, 7, 12, 13, 17, 21–24, 26 | q-0025 (its lean names it) |
| B70 | a rule's home not read at its occasion, as a class — beyond the size and density rows | 2, 10, 11, 12, 16, 18, 19, 22 | q-0025 |
| B71 | rules and decisions kept in documents or tickets read as state, not as instructions | 4, 6, 14 | q-0029 (*a document informs*) |
| B72 | text written beside its implementation inherits its verbs | 7, 9, 11 | **none** |
| B73 | grading is never triggered or tracked: *graded by the next …* recorded once in 26 | 4, 12, 13–15 | q-0026.0004 in part |
| B74 | the person is always the detector of a missed rule | all 26 | q-0026 in part (A153) |
| B75 | rules only grow: every amendment adds and none removes | 3, 18 | **none** (A152) |
| B76 | a later rewrite can silently undo an amendment, and the register does not notice | 14, 16, 22 | **none** |
| B77 | instructions outside the tree — the host's prompt and memory — compete with rules inside it | 20 | **none** |
| B78 | register entries stay open with no closure marker; the register's own closing rule has no field | 1, 2 | q-0026 |

**Section D after F:** 157 items in A; 78 weaknesses in B, 11 of them from the register, five
of those with no open question at all.
