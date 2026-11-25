# q-an5uw2 Which work has a ticket and no question behind it?

- **record of** what happened
- **part of** q-ukkw6z
- **state** closed:decided
- **answer** [the ticket format](../../.agents/skills/ticket/TICKET-FORMAT.md#the-header) — the user, 2026-11-25
- **rung** self-improvement: a rule
- **lean** none: every ticket answers a question, a hazard one that asks the person
- **opened** 2026-11-24T23:13:06Z
- **struck** 0, last 2026-11-24T23:13Z

## Where it stands

None. Every ticket answers a question, a hazard's among them: a hazard is an open question that asks
the person, and its ticket is minted from it like any other
([q-huss2x](q-huss2x-how-is-the-path-ahead-found-and-shown-the-guesses-held-as-questions-each-weighed-against-the-three.md),
decision 8). Decisions 1 and 2 are taken back with what was built on them, and no ticket was minted
under them.

## The person, 2026-11-25

To the Путь session, answering its proposal that a hazard set aside be kept in a question of its own;
read by this session in that session's transcript, 23:09Z on 2026-11-24: "отложеная опасность это не
вопрос, это сразу тикет. вопросы нужны чтобы исследовать дерево идей, не записывать важные задачи,
разве не та?" The second sentence, which they put as a question, reaches further than hazards.

## Decisions

1. *(Taken back, decision 3.)* **A hazard the person set aside is a ticket at once, with no question** — the user, 2026-11-25, the
   words above; the form the agent's: a `Hazard` field in the place of `Answers`, saying who set it
   aside, the day and its reach, held by `tickets.py --check` and shown in `--list`. Landed on the
   words with no showing first (L13).
   → [the ticket format](../../.agents/skills/ticket/TICKET-FORMAT.md#the-header). Not: `Answers`
   optional — a ticket with neither would be read as finished. It narrowed the user's of 2026-09-27
   ([01-0011.0100 the-open-questions-are-kept-by-a-mechanism](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md),
   decision 23), of 2026-10-03
   ([01-0011.0100.0020 open-issues-are-entries-of-the-store](../tickets/done/01-0011.0100.0020-open-issues-are-entries-of-the-store.md#decisions-landed-at-this-tickets-align),
   decision 4) and of 2026-10-07
   ([q-7ld3wt](q-7ld3wt-what-kinds-of-written-thing-does-a-tree-hold-and-which-of-them-does-maintain-hold-in-agreement.md)).
2. *(Taken back with it, decision 3.)* **Nothing else stands without a question** — the user, 2026-11-25, to the agent's recommendation:
   "Yes, hazards only". A ticket reads what it is for in its question, and the window, the path and
   the product's reading of what realizes an answer go by it; a hazard serves no answer, so it loses
   none of that. The agent's: a fork met later in such a ticket is a question opened where Q1 places it.
   → [the ticket format](../../.agents/skills/ticket/TICKET-FORMAT.md#the-header). Not: any work whose
   form is already known.
3. **Decision 1 is taken back, and decision 2 with it** — the user, 2026-11-25, to the Путь session, read
   in its transcript: "если в одном месте это вопрос то в остальных тоже должен быть вопрос. наверное
   так лучше, потому что тогда не надо изобретать отдельные правила для тикетов опасности- будем их
   ловить через вопросы?", and, to a reply that named the ticket's form and
   [q-ixlyj2](q-ixlyj2-how-does-a-session-hold-a-ticket-with-no-question-behind-it.md) as what goes, "да,
   принимаю текст". The `Hazard` field, its check, list column and tests are off, the lines of the
   format, the ticket skill, its mechanism's doc and the glossary (*Ticket*, *Whiteboard*) with them; so is what
   narrowed the three earlier words, which stand as they did, and the same clause in
   [the spec](../spec/01-0011.0110-every-written-thing-has-a-source-of-truth.md) and
   [01-0011.0110.0040 the-ticket-and-the-queue-are-what-comes-next](../tickets/01-0011.0110.0040-the-ticket-and-the-queue-are-what-comes-next.md).
   → [the ticket format](../../.agents/skills/ticket/TICKET-FORMAT.md#the-header). Not: the form kept
   beside the question — two ways to hold one thing. A clause on where a fork of such a ticket is
   kept, taken by the person that day ("Да, добавь") and held ("Придержи"), falls with it:

   > - No `Open issues` section: a ticket's unresolved decisions and HITL forks are
   >   entries of the question store, each holding its own argument: under its `Answers`
   >   question, drawn with `questions.py --tree <its Answers id>`; a hazard's, opened where any
   >   question is and linked from its `What to build`.

## Evidence — one fresh reader, 2026-11-25

Given a made-up hazard, "not now, after the release", and the three files, it minted the ticket with
its `Hazard` field, no question and no stop. It met the approval of a split against *at once* and
took the second; the text now says which. It guessed at where a fork met later
is kept, at what brings the hazard back, and at a small
task "for later" that is no hazard: a question now, a ticket when taken up, though no line says so.
