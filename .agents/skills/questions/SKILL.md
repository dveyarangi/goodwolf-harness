---
name: questions
description: See where the work stands among the open questions, or re-parent, merge or prune questions by hand. Read mid-turn for a declared line's other forms, and before closing, branching or dropping a question.
---

# The open questions

Every open question of this tree is one file in `docs/questions/`; the current question of each
running session is a line in `docs/questions/sessions`. `questions.py` is the only writer of
both. The window is the part of the store near a session's position, drawn before every message;
**depth** is the number of *part of* steps from a question to its root, derived, never written.

## Invoked by a person

- No argument: `questions.py --tree` and the session's window drawn whole,
  `--window --session <tag> --full`.
- With an argument: the tidy-up asked for, as a declared line — re-parent with `moves`, merge
  with `closes q-N: merged, q-M`, prune with `closes q-N: pruned, <reason>`.

Asked where things stand mid-session: `questions.py --wake --session <tag>`; it registers nothing.

## The declared line

`questions.py --declare "<line>" --session <tag>`. Clauses are separated by `; ` and apply left
to right; `at` is checked against the result and must name an open question. A line holds exactly
one `at`, or is `nothing`, which writes nothing.

| clause | writes |
|---|---|
| `at q-N` | this session's position |
| `opens q-N: <question>` · `opens q-N under q-P: <question>` | a new open question, a root or under q-P; q-N is the next free id the window names |
| `opens q-N between q-U and q-L: <question>` | a new question under q-U, with q-L moved under it; q-L must be part of q-U |
| `moves q-K under q-P` · `moves q-K to root` | a new parent; a cycle is refused |
| `depends q-A on q-B` | q-A cannot be asked until q-B is answered; a cycle is refused |
| `closes q-N: <kind>, <pointer>` | the closure, below |
| `suspects q-N` · `clears q-N` | the suspect flag |
| `leans q-N: <line>` | the lean |
| `assigns q-N to <path>` | the owner, the record holding the deliberation |

Free text may not hold `;`. A refused line writes nothing, says why, and lists the clauses; fix it
and declare again in the same turn. Under `debug=on` the first declared line heads the reply, after
the announce line when there is one; a line declared mid-turn is quoted where the reply reports
its event.

## Placing a message that answers nothing near

Name what the current question cannot be answered without deciding, or what the method's plan
expects here, and open that. When answering it narrows the current question and answering the
current one contributes to it, open it `between` the current question and its parent; when only
the first holds, open it beside, under the same parent, and add `depends <current> on <new>`.

## Closing

**When** an answer lands, a question is found wrong, two are found to be one, one is parked, one
is made irrelevant, or one is replaced. **Do** `closes` with its kind and pointer:

| kind | pointer |
|---|---|
| `decided` | a link to the doc, ADR or code that decided it, then who and when |
| `deferred` | `until <condition>, meanwhile <default>` |
| `merged` · `superseded` | the id it points to |
| `pruned` · `moot` | a one-line reason; a longer one goes to the owner's record and is linked |

The answer is never the deliberation itself. `suspects` every open child and dependent whose
assumption the answer changes; move `at` to the parent if the closed question was current.
**Then** the reply's declared line names the closure.

## Branching

**When** a question's shape hides parts whose expansion would change its answer, or a split comes
back from an impact pass. **Do** open each hidden part under it, with `depends` where one cannot
be asked before another; leave the parent open; place `at` on the first child that can be worked.
No answer lands on the parent until its children close or are deferred with a default. How a kind
of question branches is the method's instrument; the moment is this one.

## Dropping

**When** a held question is not worth holding: its answer is entailed by what is settled and
nobody can say what one might have thought instead; or answering it costs more than it is worth;
or the person drops it. **Do** close it `pruned` with its reason, after moving out the open
children that stand alone and closing the rest; a prune that leaves an open child is refused.
A pruned question is kept, never deleted. *Moot* is another answer's doing, *deferred* keeps a
default; *pruned* says the question should not have been held.

## Records

**An entry** — one file in `docs/questions/`, named `q-NNNN-<slug>.md`, the slug made by the script from
the question's words — so phrase a question short. Tier 2: read by the script, and by a person through this skill. What removes one: it
moves to `docs/questions/done/` with a wholly closed subtree nothing open depends on, a deferred
or suspect entry counting as open; it is never deleted.

```md
# q-0041 Which package manager do we use?

- **part of** q-0012
- **depends on** q-0007, q-0009
- **state** closed:decided, suspect
- **owner** [01-0011.0100](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md)
- **answer** [the ADR](../adr/0004-scripts-run-on-the-standard-library-alone.md) — the user, 2026-09-28
- **lean** the flat directory, for insertion cost
```

Every part but **state** is optional, and a closed entry must carry its **answer**. The state is
`open` or `closed:<kind>`, with `, suspect` after it at most. The id is placement and never
hierarchy; *part of* is the hierarchy's one home.

<straw-dog until="01-0010 says how registrations reach sessions that do not share the directory" ticket="docs/tickets/01-0010-dev-harness-shared-and-local.md">
**The sessions file** — one row of `docs/questions/sessions` per session:
`<tag> running|ended <YYYY-MM-DD> <q-id>|- [<q-id>,… up to four]` — its tag, whether it runs, the
date it last wrote, its current question or `-` before it has one, and its recent ones. Tier 1
through the window and the wake's read. What removes a row: kept by design — an ended row lets a
later wake offer to resume, and a running row silent for a week is reported, never removed.
</straw-dog>
