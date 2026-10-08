# How the front page was reviewed by outside agents — 2026-10-08

A record of what was done, kept so it can be repeated. The front page was rewritten three times
in one session on
[q-0031](../questions/q-0031-what-is-the-harness-said-to-a-reader-who-arrives-cold-and-what-of-it-does-the-front-page-carry.md).
Each round was checked by agents that knew nothing of the project. At the end the user asked
that the process be saved for future use. It is a second look at produced work, by readers other
than its author, under criteria other than the author's. That is a case of
[q-0029](../questions/q-0029-how-is-produced-work-gone-over-again-over-what-scope-by-what-criteria-by-whom-and-to-what-result.md),
and it is filed there as one. This record describes; whether it becomes a skill is the user's
decision.

## The stages, in the order that worked

Each stage ran as one or more subagents in parallel. None was given another's output.

1. **What the field is now.** Two kinds of pass, both web-only and told nothing of the project:
   - *Genre*: how the front pages of the closest peers are written — opening line, section order,
     where install appears, length, examples, comparisons, limits, cost.
     [Result](readme-survey-2026-10-08.md).
   - *Capabilities*: the same fixed questions put to every peer, from current docs and releases,
     each answer dated and given a confidence. Three or four tools per pass, four passes at once.
     [Result](peer-capabilities-2026-10-08.md).

   The page's positioning is written from these, never from an older pass. The user struck a
   claim drawn from a pass twelve days old: the field had moved in that time.
2. **What the thing is, from outside.** Two `/discover` passes on the subject itself: one reading
   the repository cold from a fresh clone, one given only a functional description.
   [Result](discover-recall-structure-2026-10-08.md). These correct the author's account of what
   the thing is an instance of.
3. **Draft.** The author writes the page against the user's decisions.
4. **Cold reads.** The draft is copied to a scratch file. Two readers with different personas read
   only that file: no repository, no web, no links followed. Each reports, bluntly, in a fixed
   shape — see the prompts below.
5. **Fact-check against the tree.** Every claim the readers doubted is checked against the code
   and the records before it is rewritten. In this run the check found the page claiming that
   hooks delivered context in installed projects. The installer carries no hook wiring.
6. **Revise, then cold-read again with fresh agents.** A second round never reuses the first
   round's agents, which have seen the earlier draft.
7. **Record.** Each round's decisions, and the advice not taken with its reason, go into the
   question the page stands on.

## The reader prompts

Two personas did most of the work. They disagree usefully: one wants to be sold, the other
refuses to be.

- **A solo developer**: six months building a product with an agent most days; tired of
  re-explaining the project and of the agent undoing decisions; decides in two minutes.
- **A sceptical tech lead**: a year on agents in a large, long-lived codebase; dropped a
  spec-driven kit for its ceremony; allergic to coined vocabulary and marketing; judges a page by
  what concretely changes and what it costs.

The frame both were given:

> You are a cold reader. Read ONE file and nothing else on this machine: `<scratch copy of the
> page>`. Do not open any other local file, do not follow local links, do not search the web.
> Your host may have loaded some project instructions into your context: ignore them entirely;
> they are not addressed to you. Raw `<straw-dog question="…">` tags are stripped when GitHub
> renders the page — read their contents as plain text and ignore the tags.

Then the persona, and the report it owes:

1. After the title and the first two paragraphs only: what is this, how does it differ, do you
   keep reading?
2. Every phrase that describes the tool's machinery or vocabulary where the reader wanted to know
   what changes for them — quoted, section by section, exhaustive — and what it should say
   instead.
3. Claims not believed or not understood; over-claims and under-claims.
4. Questions about whichever section is under decision, for example "does this make the case for
   reliable self-modification?"
5. Tone: marketing, jargon, the author talking to themselves.
6. Section order; what to move, cut or merge.
7. Would you try it this week, and what stops you?
8. The five most important edits, each quoted before and after.

## What each round found

- **Round 1**, on the second draft:
  - **Method stated as result.** The opening switched pitch in its second paragraph.
  - **The self-change section.** It read as the maintainer's plumbing.
  - **The disqualifiers were buried**: no team support, no fast path, `CLAUDE.md` moved aside.
  - **Absolute promises** contradicted the page's own admission that rules are instructions, not
    enforcement.
- **Round 2**, on the third draft, with fresh agents:
  - **The opening.** "Forget everything" was false, and the workflow's weight was hidden.
  - **The self-change claim had no evidence.** Who notices a miss, and does a rewording hold?
  - **The ✦ claim could not be checked.**
  - **Works today and Not yet contradicted** each other about drafting the architecture.
  - **The hosts line was defensive.**
- **After round 2**, from the user:
  - "starts over from whatever static notes you left it" read as a chore laid on the user.
  - The version line in the morning scene was debugging output, not a benefit.

## Lessons for the next run

- **Hosts load the entry file into every subagent.** No pass was blind. Each must be told to
  ignore what it was given, and should say what it saw.
- **A subagent that launches its own background jobs can hand back before they finish.** That
  happens the moment its own turn ends, and it returns nothing. Tell research passes to do the
  work themselves.
- **Web fetches through a summarising model mangle detail**: years, command names. Have
  capability passes read raw files and date every claim.
- **The author's eye is the worst placed** to see method posing as result. The readers found
  phrases the author had already rewritten once.
- **A reader's advice is material, not a verdict.** Where it conflicted with a decision of the
  user's, the decision stood, and the record says so.
- **Check the readers' doubts against the tree before rewriting.** One doubt exposed a false claim
  the author had carried through three drafts.
