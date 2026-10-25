# What GoodWolf is said by

- **record of** what happened

**2026-10-25.** Opened on a question about the dials; turned on an outside article asking what a
harness is, and ended with what the project is said by landing in two skills: `/product` now loads
when an agent is about to say what the project is, and `/skill-up` keeps a skill's moments in its
description. On the way the front page's three principles were brought to the question they serve,
and the word *harness* was settled by the product session.

## Decisions, and what chose them

**Whether GoodWolf is a harness, by Theo's definition** — Theo (t3.gg), *What is a "harness"?*,
2026-10-23, read in the built-in browser after a direct fetch was refused: the harness is what
lets a model act — the tools, the call syntax, the parser that runs a call, the result returned,
the tool list; the interface apart; an agent a harness and a model, its differences a
configuration. The agent answered *no* and was right on the narrow reading: the tree's only hooks
are `SessionStart` and `UserPromptSubmit`, which inject context and see no tool call; Claude Code
parses and runs every call. The person pushed three times — *it directs the model, not just a
passive rulebook*; *goodwolf reads all that, spots tool calls and invokes them* (refuted from
`.claude/settings.json` and `hook.sh`); *so it is just a configuration? really?* — and the fourth
push turned it: *after all our product work you still position it as just memory across
sessions?* The agent had never opened `docs/product.md`. Read, it says GoodWolf is a harness that
keeps an agent's work coherent, against three pains — ineffective, suboptimal, the person's agency
off its point — a different axis from Theo's: his harness gives the agent hands, this one the reins.
The noun itself was the product session's to settle: q-0033.0011 closed with the name kept, a
harness meant as the user harness, after Böckeler, never the runtime; the method's glossary
rewritten so.

**Rule failure 78, and its amendment** *(the user, 2026-10-25)*. Registered: what the project is
was said without its product document. Drafted through `/skill-up`, tried on two fresh judges. The
first found the new occasion firing and the clause a rival to `/discover`'s, the body silent on
it; the second, on *by its own account*, found the two complements. The person then asked: *did
you even invoke the product skill … the moment should be in product skill description, not body*.
The goal the agent had opened with the occasion was cut to what to do there. Landed:
`/product`'s description names the moment, goal 5 tells the project by its pains and answers, the
product mechanism's Moments has the row.

**Rule failure 79, and its amendment** *(the user, 2026-10-25)*: *the skill-up should distinguish
between moment and instruction and know to place them accordingly*. The glossary already had
*moment*. Landed in `/skill-up`: the description narrates the skill's moments, the body holds what
to do at them and never restates when.

**The front page's three principles brought to q-0033.0008** *(the user, 2026-10-25)*. Said at the
align on q-0037.0006.0020.0001.0006 and sent here by that session: no self-deprecation; the
meeting agent brought to a full check of its own project; everything that matters with why, and
the offer to check. Asked *и это все выводы?*, the agent drew five conclusions, recorded with
them: the cold reader makes the inside agent's mistake; the noun holds the first line; a check in
place of a caveat; the cabinet agent's findings are the product's pains in its project; a number
answers what silence leaves open. The README is not this session's to edit — it is told by
01-0040.0070, in its align, where the principles were passed.

## Done

- Rule failures 78 and 79 registered, amended and closed — [docs/rule-failures.md](../rule-failures.md).
- `/product`'s description and goal 5, its mechanism's Moments row, `/skill-up`'s description
  paragraph.
- q-0033.0008: the principles as its lean, the conclusions and the settled noun in its body.
- Findings sent to the product session twice: Theo's definition, which it could not open, and the
  principles and conclusions for 01-0040.0070.

## What went wrong, and what it taught

- **What the project is was told from its implementation**, three replies in a row, the product
  document never opened, though the front page is derived from it — the trap that document was
  found against. A comparison with a peer was taken for `/discover`'s occasion, the outside view
  in hand, and the inside account was not looked for.
- **A judge's finding was taken where it pointed.** The judge said the body never said to read the
  document; the agent put the occasion into the body, where it reaches nothing. A judge reads what
  is in front of it; where the fix goes is the builder's call.
- **"Reinstall the copies" assumed a copy.** `.claude/skills` is a link to `.agents/skills`; the
  installer checks were run instead.

## Principles with no durable home yet

- **Two senses of harness meet every reader.** One reading is the runtime, the other the layer
  around it; a page that names neither is read in the reader's sense. The glossary now holds this
  tree's sense; how the page says it is q-0033.0008's.

## Open questions touched

- [q-0033.0008](../questions/q-0033.0008-what-is-the-harness-said-to-a-reader-who-arrives-cold-and-what-of-it-does-the-front-page-carry.md)
  — open; the lean is the three principles; it waits on the page being told by 01-0040.0070.
- [q-0037.0013.0005](../questions/q-0037.0013.0005-which-of-the-agents-acts-need-the-persons-yes-and-which-does-it-do-on-its-own.md)
  — open, placed on for the dials, answered from the entry file; its lean of 2026-10-15 stands.
- [q-0033.0011](../questions/done/q-0033.0011-what-kind-of-thing-is-the-harness-in-the-words-of-the-landscape-it-is-read-in-and-what-noun-names-it.md)
  — closed by the product session: the user harness.
- The store's check suspects q-0033.0008 and q-0033.0008.0001 of being one question; met, not
  touched.

## What continues

The align of 01-0040.0070, held by the product session: whether the three principles become its
criteria is the person's there. The first step of the next session on the front page is that
align, the page told from the product document with the noun settled.
