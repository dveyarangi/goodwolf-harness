# Session 44 — a store opens with three roots

**2026-10-09.** Claude Code, session `de339340…`. Entry contract v42 at the start, v44 at the
close, moved by a parallel session. Other sessions worked q-0033, q-0030 and q-0018.0020 in the
same tree; their files, `README.md` among them, were left alone.

## What was decided, and what chose it

### Every project's store starts with three roots, and nothing else

The user came with a proposal: a new project always gets three root questions — why it is needed
(product), how it is built and where it is developing (technical), what else it could be and who
its neighbours are, perhaps *what is this project?* (research) — and asked for sharper wordings,
by /discover among other means. Opened as q-0001.0022; one pass,
[discover-root-questions-2026-10-09](../research/discover-root-questions-2026-10-09.md).

What the pass changed. The trouble was where the roots divide, not how they are worded. The
technical root fused structure with trajectory. The research root fused four questions: what the
project is one of, what surrounds it, what else it could be, and what is not known. And *what is
this project?* is the question the whole tree answers, not a sibling of the other two. Re-filing
this tree's twenty roots under purpose, structure and situation put two thirds under structure
and none under situation, as the viable-system model predicts: the urgent starves the
exploratory.

The user's turns, in order:

- *Re-cut*, rather than keep the draft.
- The third root is *the space the project is in* — neighbours, history and evolution together,
  whose answers can move both purpose and structure. Worded together as *What landscape does this
  project evolve in?*
- *No parent*: *What is this project?* stays what the three answer together, never an entry.
- Each root is where a person's agency is spent. Purpose is agency itself: an operator picks the
  goal from the space of ideas. Structure needs agency where the model is ineffective, suboptimal
  or destructive. The landscape needs it to set the purpose and the principles of the structure,
  where the model misses.
- Strategy starts from the situation, so the landscape sets the purpose at the start. Then the
  project grows flesh, and the purpose can no longer turn into a dating site. How that weight
  shifts over a project's life was opened as q-0001.0022.0001.
- *Seed only the roots* — no links between them, no children.
- The words: *What is this project for?* · *How is this project built?* · *What landscape does
  this project evolve in?* *For* was preferred to *for, and for whom*; *built* to *work*.

Where the project's own trajectory lives was left out of the decision: only the roots are seeded,
so placing it is the project's own business.

Landed in the questions mechanism's doc, *Three roots from the start*.

### No constants in the installer

The agent's first framing of the ticket put the words in two homes, the doc and an installer
constant. The user: *what do we do about the single home? There must be no constants in the
installer.* The design that followed:

- the words sit on a shelf of the questions mechanism, `STORE-ARRIVAL.md`;
- the entries and the rule of when are the store script's, in `questions.seed`;
- the installer only calls it, as it already calls `inject_rules`.

A store holding no entry is seeded at an install and an update alike, by the delivery status's
precedent; the user agreed. The criterion's instrument is a fixture with its own words, and a test
that rewords the shelf, so an installer holding words of its own would be caught.

## What went wrong, and what it taught

### Four answers proposed on a question whose parts were not unfolded

Under q-0001.0022 the user said the landscape's answers can move the other roots. The agent
proposed a soft link and then, four replies running, a form and a next step. Each time the user's
answer reshaped the question rather than chose among options:

- the link is made toward an answer, not a question;
- *which database* depends on an answer too, so where is the difference?;
- *which database* already presupposes a database;
- *which language* presupposes a service, and *which kind holds tracks how set the project is*.

The user: *you hurry to make concrete and cut where it is not yet worth it; you know the problem is
not simple; do you think you have untangled it? If not, remember what we do for this.*

What the session did about it:

- The question was reworded open and branched into six parts, and a second /discover pass was
  taken: [discover-what-stands-on-an-answer-2026-10-09](../research/discover-what-stands-on-an-answer-2026-10-09.md).
- Rule failure 25: /questions' *Branching* now fires on a refutation that reshapes the question,
  and puts no answer of the parent to the person until its children close.

Later the user was lost — *what are we doing?* The answer: the roots no longer waited on the
links, since only the roots are seeded. So the work went back to the roots and finished them.

**A principle with no home yet.** When the person's answers keep reshaping the question, the work
is not ready to answer it. Unfold it and let the decision tables fall silent. The branching rule
now carries the trigger; whether ⚖️ tables should go quiet more generally is not written down.

### Edits by script

The ticket's boxes and status were flipped with `sed`, against the user's standing preference for
edits shown in the transcript. Said in the reply; later edits used the edit tool.

## What was done

- [01-0011.0100.0045 a-fresh-projects-store-opens-with-its-three-roots](../tickets/done/01-0011.0100.0045-a-fresh-projects-store-opens-with-its-three-roots.md),
  through /ticket, /impact, /plan, /implement, /verify and /maintain:
  - `questions.seed` and `--seed`;
  - the shelf;
  - the installer refusing a ref that cannot say the roots before writing anything, and calling
    the seed after the queue;
  - 15 tests; 572 in the suite.
- A repair at /verify, under `repair=report`: the architecture said *one file outside the manifest
  is written*, and now names both things written outside the manifest.
- /maintain: the paired close; five mechanisms re-checked at rules, two at output, nothing to
  change.

## Open questions touched

- **q-0001.0022.0001** — how the roots' weight shifts over a project's life. Holds the user's
  strategy-first reading; nothing chosen.
- **q-0001.0023** — how a change in one answer reaches what stood on it. Unfolded into six parts;
  no answer. The roots do not wait on it.
  - **.0001** holds five positions — one link, two kinds by a test, three kinds, a typed graph,
    kind as a role — and a reading of the roots and q-0033: every kind of link occurs; `depends
    on` is used for support; the straw dog is already a non-blocking link from text to a
    question.
  - **.0002** to **.0006** and **.0003.0001** hold the second pass's material as leans.
- This tree keeps its twenty roots. Whether to put them under the three was raised and never asked.

## What continues

The user picks the next item. Candidates:

- the branch of q-0001.0023 at .0001, reading this tree's links;
- q-0001.0022.0001.

The queue's own next item is unchanged: 01-0011.0100.0050, *A question branches before it is
answered*, which rule failure 25 now touches from the rule side.
