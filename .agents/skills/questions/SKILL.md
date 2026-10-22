---
name: questions
description: See where the work stands among the open questions, or re-parent, merge or prune questions by hand. Read mid-turn for the store's other calls, and before closing, branching or dropping a question.
---

Mechanism: questions

# The open questions

Every open question of this tree is one file in `docs/questions/`; the current question of each
running session is its row, the session mechanism's, under `docs/sessions/rows/`. `questions.py` is
the only writer of an entry's parts, and writes the row's position through the session's script;
an entry's body is written by hand. The window is the part of the store near a session's position, drawn before every message;
**depth** is the number of *part of* steps from a question to its root, derived, never written.

## Invoked by a person

- No argument: `questions.py --tree` and the session's window drawn whole,
  `--window --session <tag> --full`.
- With an argument: the tidy-up asked for, as calls — re-parent with `move`, merge with
  `close q-N merged q-M`, prune with `close q-N pruned '<reason>'`.

Asked where things stand mid-session: `questions.py --wake --session <tag>`; it registers nothing.

## The calls

`questions.py <call> … --session <tag>`, one event each, validated and written whole; `--help`
after a call says what it takes.

| call | writes |
|---|---|
| `at q-N` | this session's position, an open question |
| `open '<question>'` · `--under q-P` | a new open question, a root or under q-P; prints the id it was given |
| `open '<question>' --between q-U q-L` | a new question under q-U, with q-L moved under it and renamed; q-L must be part of q-U |
| `move q-K --under q-P` · `move q-K --to-root` | a new parent, q-K and everything under it renamed; a cycle is refused |
| `reword q-N '<question>'` | an open question's new words; its id, parts and body stay, and its file takes the words |
| `depend q-A --on q-B` · `undepend q-A --on q-B` | q-A cannot be asked until q-B is answered, or no longer waits; a cycle is refused |
| `close q-N <kind> '<pointer>'` | the closure, below |
| `suspect q-N` · `clear q-N` | the suspect flag |
| `lean q-N '<line>'` | the lean |
| `assign q-N <path>` | the owner, the record of the work that answers the question |
| `realize q-N '<link>'` | the trace link, `A7 "<name>", …` or `derived`, replacing the one it carried |

`open` leaves the session where it stands: to stand on the new question, call `at` on the id it
printed. A refused call writes nothing and says why; fix it and call again in the same turn.

Free text goes in single quotes, which neither bash nor PowerShell expands; a text holding an
apostrophe goes in double quotes, with no backtick or `$` inside.

## A raised question

**Look it up first.** Every question a message raises is looked for before anything is opened, in
*the docs*: the architecture, ADRs, the glossary, the mechanism docs, the code, and the decisions
waiting in the `## Decisions` lists of the questions' bodies, where a decision sits until it has
a home. Found, point to it and open nothing; a settled question is not reopened without new evidence against its answer. An
answer that leaves part unsettled is found only in part: the rest is a raised question of its
own. There is no need to search `done/`: a decided entry links to what holds its answer.

**Who settles what is not found.** The dial does, as the entry file's *Autonomy* says: a decision
below its ladder's dial, settle in the turn and report it; at the dial, settle it and show it before
it lands; above, it is the person's — settled in the turn, it goes to its home; not settled, open
it. Unsure of its rung, take the higher.

**A question's rung.** Give a question you open its parent's rung on each ladder, raised where the
question already shows a higher one —
`questions.py rung q-N '<ladder>: <rung>, ...' --session <tag>` — and raise it when a higher
decision turns up. Never lower it; the person may.

**A request.** *Build X* is a proposed answer: lean it on the question X answers — *what is X
for?* — or open that question when none is held. Open *how to build X?* under it once X is
accepted; the ticket's plan answers it. A trivial request is settled by doing it.

**Where to open it.** Under the lowest question that contains it, whatever the session stands
on. One that bears on the current question — what that question cannot be answered without
deciding, or what the method's plan expects here — is opened `--between` the current question's
parent and the current question when answering it narrows the current one and answering the
current one contributes to it; when only the first holds, beside it, under the same parent, with
`depend <current> --on <new>`.

**Outgrown words.** When the discussion on a question has moved past its words — it took in a
related topic, or found what it was really asking — `reword` it in the turn that notices, as often
as that happens: the id stays, so nothing bound to it moves. A closed question is never reworded.
<straw-dog question="q-0037.0001.0021">
Reword when everything under the question still belongs under the new words; open a parent when
the old question stays a distinct part of the wider one.
</straw-dog>

**A missing parent.** When only a far question contains the message and two or more of its
children resemble it, the question those children jointly serve is missing. Size it by the
children, never by the message. Test it: would you look under it for this question? `open` it
under the far one, `move` each child you would look for under it, leave a child you doubt where
it is, call `at` on it, and say in the reply which moved and which you left. Neither the number
of children moved nor a second parent that would sit inside or around this one is a reason to
ask. Ask only when two parents would each take the same children. Then the turn is uncharted,
and the ask names each parent you weighed and the children it would take.

**Uncharted.** The reply does the work asked and puts the question's home to the user: the
question the message is one case of, never the message restated, the homes you weighed, and the
one you would choose. The row repeats in every reply until the user answers; then open it where
they said.

<installed by="product">
**U3** A question opened right under *How is this project built?* gets its trace link at once: the
answers it realizes — `questions.py realize q-N 'A7 "<name>"'` — or `realize q-N derived` for
none.
</installed>

## Closing

**When** an answer lands, a question is found wrong, two are found to be one, one is parked, one
is made irrelevant, or one is replaced. **Do** `close` with its kind and pointer:

| kind | pointer |
|---|---|
| `decided` | a link to the doc, ADR or code that decided it, then who and when |
| `deferred` | `until <condition>, meanwhile <default>` |
| `merged` · `superseded` | the id it points to |
| `pruned` · `moot` | a one-line reason; a longer one goes to the entry's body |

The answer is never the deliberation itself. `suspect` every open child and dependent whose
assumption the answer changes; call `at` on the parent first if the closed question was current.
A `close` that finishes a subtree moves it to `docs/questions/done/` itself and says so; a closed
question with an open, deferred or suspect child stays live until that child closes. A `close`
refuses while the question's `## Decisions` list holds a decision with no home: land it, or move
it to the nearest open question above that holds everyone who needs it — on a merge or a
supersession, to the question it points to. Closing against a
decision still waiting in such a list, cite the list: the straw dogs waiting on the question come
due once every link of its answer is a home — never a question's list, a ticket or an RFC.

## Branching

**When** a question's shape hides parts whose expansion would change its answer; a split comes
back from an impact pass; or the person refutes a proposed answer by reshaping the question rather
than by choosing among its options. **Do** open each hidden part under it, with `depend` where one
cannot be asked before another; leave the parent open; call `at` on the first child that can be
worked. No answer lands on the parent, and none is put to the person as a proposal or a decision,
until its children close or are deferred with a default. How a kind
of question branches is the method's instrument; the moment is this one.

## Dropping

**When** a held question is not worth holding: its answer is entailed by what is settled and
nobody can say what one might have thought instead; or answering it costs more than it is worth;
or the person drops it. **Do** close it `pruned` with its reason, after moving out the open
children that stand alone and closing the rest; a prune that leaves an open child is refused.
A pruned question is kept, never deleted. *Moot* is another answer's doing, *deferred* keeps a
default; *pruned* says the question should not have been held.

## Records

The shape of an entry and its body is [QUESTION-FORMAT.md](./QUESTION-FORMAT.md)'s;
read it before writing a body.
