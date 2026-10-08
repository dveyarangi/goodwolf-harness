# Session 41 — the marks get out of the text's way

**2026-10-08.** Claude Code, session `7871cf30…`, Opus 5.5. Entry contract v34 at the start, v37
at the close. Sixteen commits of this session's own; the first seven pushed with v35 on the
user's word, the nine since wait. The parallel session `693642b7…` worked on the front page (q-0031)
in the same tree; its files — `README.md`, `.agents/skills/recall/SKILL.md` and its own commits —
were left alone.

The session opened as [session 40](0040-20261008-the-kinds-land-and-a-reply-shows-its-footing.md)
planned: its first claiming reply was itself the first test of
[01-0011.0110.0020 a-paragraph-shows-what-it-stands-on](../tickets/01-0011.0110.0020-a-paragraph-shows-what-it-stands-on.md),
and it passed — the marks came unasked. The user read them, and the rest of the session was the
form of the marks, reworked reply by reply on the user's reading, before the queue's next item
got past its opening question.

## What was decided, and what chose it

### The form of the marks — q-0030, v35 to v37

Every step was the user's reading of the reply before it; the rule, at its home in
[AGENTS.md](../../AGENTS.md), holds the result, and q-0030's body holds each step in the user's
words. What turned it:

- *The marks interfere too much with the text itself.* v34 opened each claiming paragraph with
  `💡 🧩 ⚓` inline. They moved out — to a blockquote, then to a closing parenthesis, the lamp
  last in the paragraph it governs.
- *Show not the classification but the kind: classification and value.* A bare `🧩 *Kind of
  record*` says nothing of where a thing went.
- *The box only in the rare case where you see a meta-principle the existing ones lack;
  otherwise nothing.* I had boxed a paragraph merely for having no principle; the box is for a
  gap in the list, worded, not for a claim without a lamp.
- *A blockquote for what needs the user's decision, and an icon.* I chose `⚖️`, the picture of
  *what do I choose?*; then *a table of one column, like the questions*; then *the first row a
  header, the icon in it alone*.
- *The classification marker and its paragraph — only candidates for a record, of no historical
  and no existing kind: changes and invariants, the invariants with their own icon.* This turned
  `🧩` from a mark any classification earns into the heading of a proposed text. It went through
  a table with a header cell, a table with the heading above it, and landed as *just the
  classification as a heading, made understandable, then the paragraph's ordinary output*:
  `🧩 **Proposed change — <record>**`, `⚓ **Proposed invariant — <record>**`.
- The footing: a blockquote at the end, then *is there an element to collapse it — a big block
  after the text confuses*. `<details>` does not render in the host; markdown footnotes do. The
  footnote's colon looked like noise, I swapped the syntax for plain `[1]` notes, and the user:
  *before, the footnotes were formatted; now they are plain text and noisy again* — so footnotes
  stay, colon and all. Then *the message being answered takes no footnote*, and *with no real
  source outside the session, no footnote*. With footnotes taking the footing, *the anchor icon is
  not needed — use it for invariants*.
- *Check that our formatting instruction has not grown — write for a capable model.* The
  paragraph had grown by accretion to a run-on of exceptions; rewritten to three bullets and a
  line, the line *a paragraph that links, narrates or restates carries no mark* dropped as implied
  by *claims or recommends*.

### Push is asked once per unit

*Why is push a decision at every step? Annoying.* Under `push=ask` I had re-listed the unpushed
commits in every reply while the marks moved one commit at a time. The push is now put once, at
a unit's end or at the conclude; the memory holds it.

### `.0040`'s size — open

The align on [01-0011.0110.0040 the-ticket-and-the-queue-are-what-comes-next](../tickets/01-0011.0110.0040-the-ticket-and-the-queue-are-what-comes-next.md)
opened on the user's question at minting: is it too large? The necessity gate passed — the queue
is 58 KB with a 37 KB *Completed step* line every `/recall` reads, four table cells had drifted
from the headers they copy, and ten of thirty-five live tickets hold a decisions section. I
recommended a split into four independent parts: the visible kind on every agent-edited record;
decisions in the question's body with `close` refusing one without a home and `/align`
retargeted; the queue's table rendered from the headers; the ticket's contract and the board
seam. The user has not answered; the session ended on the question.

## General principles derived, with no durable home yet

- **A form is graded on the rendered page, not the source.** `<details>`, footnote colons and
  plain brackets each looked right in the source and wrong in the host; each fix was only known
  good once the user saw it rendered. No rule says to test a reply's form in its renderer before
  making it a rule.
- **A mark earns its place by what the reader cannot already see.** The answered message, what
  this session read, a classification without its value — each was noise for the same reason.
  The last bullet of the rule states the footing's case; the principle itself is unnamed.

## What was done

- The marks rule rewritten seven times across v35–v37, its current text at the entry file, its
  history in q-0030's body and [the contract's findings](../research/entry-contract-findings.md).
- `.0020`'s first box checked: the marks came unasked in a fresh session.
- `/recall` at the start; `.0040`'s align opened and its necessity gate passed.
- One memory: push asked once per unit.

## What was refuted or went wrong

- **The plain `[1]` note**, my guess at the colon's fault, made the footing worse; reverted.
- **Inline marks, then blockquotes, then a framing table** — three forms the user rejected on
  sight. The cheaper path would have been to show two forms side by side once.
- **`sed` twice** on the findings, against the standing preference for edit tools.
- **One reply boxed a paragraph for having no principle**, before the box was narrowed.

## Open questions the session touched

- q-0030 "How does a reply show the principles each of its claims stands on, and where are the
  principles named for it?" — the form settled for now at v37; `.0020` waits on the user's week
  of grading and the first box that names a missing principle.
- q-0024.0009.0003 "How do the ticket and the queue hold what comes next alone, with the draft in
  the question's body?" — `.0040`'s align open, waiting on the user's answer to its size.

## What continues

- **First step of the next session:** the user's answer to `.0040`'s size. If split, `/ticket` →
  `/impact` on the four-part draft, presented, not minted. If the align waits, `.0050`, Ready and
  AFK.
- The unpushed commits — v36 and v37 — wait on the user's push.
- `df0f81c5…` and `s-1008-8a4e` still read running; `693642b7…` is live on q-0031.
