# Session 0060 — the dial and the question

- **record of** what happened

2026-10-14 and 15. Began as a `/recall` answering a greeting and as the re-read of
[01-0010.0170](../tickets/done/01-0010.0170-arrival-becomes-a-sequence.md); ended having replaced
the agent's autonomy switches with a dial on a ladder, retired the spec into the question, and
amended four skills. Every turn under `debug=on`.

## Decisions

- **The 🪢 table stands whenever another session runs, its header ids alone** *(entry contract v89
  and v90)*. A `/recall` with seven sessions running and no collision read *a table only where it
  has one* as dropping 🪢 whole and told the neighbours in its own words; the next reply wrote every
  question's words beside its id. The user: *unreadable — in the table the id as a clickable link
  is enough.* Q5 now leaves out the words where a table's form names a question by id.
- **A first install builds no environment** *(the user: "an install into a clean repository with no
  project and no idea what it will do must not create an environment; the environment comes when
  the project's requirements are clear")*. Landed first as three rules — a negative line in the
  harness skill, a vague moment in setup-devops's description, a straw dog — and taken out: *what
  is the purpose of negative instructions? … just do not.* Q6 gained: *a decision not to do what
  nothing instructs lands in its question alone* (rule failure 47).
- **01-0010.0170 closed at its re-read.** Its setup step went with the decision above, its
  `cicd.md` pointer with the decision of 2026-10-07, its outcome had landed in the skill on
  2026-10-09. Closed on one trial: an agent without the session's context ran *After the first
  install* in an empty folder; its L3 said the project had no toolchain and named the record checks
  the person accepted, and nothing else was built.
- **The verification-set rule names the file that holds the checks, never the checks** — at first
  a paragraph; *remove the enumerations, the model finds them itself; one short sentence.*
- **The way of working with git is the environment's** (q-0037.0006.0022.0003): the agent reads it
  from an existing project, proposes the simplest for an empty one and says when to revisit, takes
  what the person asks. Reached after the agent offered a switch of its own invention, then a
  questionnaire: *the project does not name its scenario; it wants to learn which exist … asking
  is interrogation; ask what the project is and propose.*
- **Autonomy is a dial on a ladder** (q-0037.0013.0005, nine decisions). The user rejected a
  general principle (*too general, read differently by each*), then a separate reporting axis
  (*reporting is not an axis*), and set the shape: at the dial the agent asks, below it acts, above
  it proposes; it reports at its rung, describes the one below, says nothing of the lowest.
  Development's ladder by consequence (code, a feature, load-bearing, a product slice, the whole
  product — load-bearing above a feature, the agent's correction the user accepted);
  self-improvement's from a wording to the method, its dial at a core rule. A rung is read from
  what a decision decides, not its record (*a ticket can be about different levels*). Repair is no
  rung; its report is debugging's, and debugging is a mechanism of its own, not a `debug=on` each
  skill reads as it likes. Commit and push follow the work. Acts off the ladder are security
  settings held by a mechanical check. A change's path follows the same ladder. Last, at the
  conclude: *nothing may take on development specifics except by being bound to the future
  mechanism of the development method* — the dial is core, a ladder its method's mechanism's.
- **A spec is no separate document** (q-0037.0009.0017). A draft spec of 230 lines was written for
  the dial; the user asked whether the questions had not made it redundant, then refused a
  one-sided check (*so you see no advantages?*) and asked for a discovery. Its finding that
  settled it: the choice is which record owns rationale, status and current truth, and the
  question, the ticket and the standing documents already do; per-change specs for agents are
  seldom carried forward and skimmed when approved. The question's body now runs `Where it
  stands`, rewritten whole; `Decisions`, each refused alternative after `Not:`; dated evidence,
  appended. The draft spec was deleted.
- **Skills:** `/discover` asks the question the shape answers, not the shape (rule failure 49,
  the user: *why does the discover skill itself not do this?*); `/skill-up` weighs the whole skill
  on every change (rule failure 50); the questions skill went from 2,339 words to 1,556, its
  records' shape to `QUESTION-FORMAT.md`.

## Principles derived, no durable home yet

- **A rule cannot make a voice.** L9 was amended with the shapes of the session's drift and rolled
  back: *it will not work; what interests me is Lem's voice, not what you wrote* (rule failure 48,
  refused). A list of failure shapes describes the failure, not the thing.
- **A promise to try is no instrument.** Asked *how exactly will you try?*, the only honest answer
  was the rule's wording — and even that was refused above.

## Done

Four discoveries' material, each in the body of its question: git gates and situations
(q-0037.0013.0005, q-0037.0006.0022.0003), action boundaries (q-0037.0013.0005), working documents
(q-0037.0009.0017). Five tickets minted on approval —
[01-0020.0010 the-agent-asks-at-its-dial](../tickets/done/01-0020.0010-the-agent-asks-at-its-dial.md),
[01-0020.0020 a-reply-reports-by-its-dial](../tickets/01-0020.0020-a-reply-reports-by-its-dial.md),
[01-0010.0210 a-recipients-switches-become-its-dial](../tickets/01-0010.0210-a-recipients-switches-become-its-dial.md),
[01-0019.0010 self-improvement-follows-its-dial](../tickets/01-0019.0010-self-improvement-follows-its-dial.md),
[01-0016.0010 a-question-is-its-works-working-document](../tickets/done/01-0016.0010-a-question-is-its-works-working-document.md) — and their order set in the queue. Rule failures 47 to 50.

## What went wrong

- Replies drifted into tables, coined words and untranslated phrasing (*who is hurt if main
  breaks*), and narrated their own steps.
- Discovery taskings twice retold the method they were meant to step outside.
- Two closures committed by a filename mask left the live copies of closed questions in the tree;
  found and removed a day later.
- A heredoc failed on quoting and the tickets were written again with the editor.

## Open questions touched

- q-0037.0013.0005 — decided in nine points; its children .0004 (the dial an install proposes),
  .0005 (the dial out of the agent's reach), .0007 (the report by rung), and q-0037.0013.0002
  wait on [01-0020.0010](../tickets/done/01-0020.0010-the-agent-asks-at-its-dial.md)'s align.
- q-0037.0009.0017 — decided; the work is [01-0016.0010](../tickets/done/01-0016.0010-a-question-is-its-works-working-document.md).
- q-0037.0009.0021 — debugging is a mechanism; what it owns is open.
- q-0037.0006.0022.0001, .0002, .0003 — the verification set's pointer decided, its place open;
  setup leaving the set behind; the way of working with git.
- q-0037.0010.0002.0005, q-0037.0012.0001 — now hold the development and self-improvement ladders.

## Next

The queue's first item is
[01-0016.0010 a-question-is-its-works-working-document](../tickets/done/01-0016.0010-a-question-is-its-works-working-document.md),
then [01-0020.0010](../tickets/done/01-0020.0010-the-agent-asks-at-its-dial.md). Start in a fresh session with `/recall`.
