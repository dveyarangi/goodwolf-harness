# The meeting, run 4 on xuanxue-cabinet — every objection against installing, with what answers it

- **record of** what happened
- **evidence for** [q-0037.0006.0020.0001.0004](../questions/q-0037.0006.0020.0001.0004-how-does-the-install-read-a-tree-with-a-method-and-report-what-goodwolf-would-change-there-before-anything-is-written.md), [q-0033.0008](../questions/q-0033.0008-what-is-the-harness-said-to-a-reader-who-arrives-cold-and-what-of-it-does-the-front-page-carry.md)

2026-10-25. A fresh session in xuanxue-cabinet was asked *do we need this here?*, answered *no*
from the README, explained its reasoning when asked, then ran a study of its own with four agents
over GoodWolf's skills and mechanisms, about 1.2 million tokens in all, its file kept outside the
tree. Every objection it made, said or implied, is listed below once, with what it is and what
would answer it. *Text* is a change to what a reader of the harness reads; *function* is a change
to what the harness does; *true* is a limitation that stands and is to be said, not hidden; a
*misreading* is a fact the agent got wrong, which some text let it get wrong.

## A. "The project already has it"

1. Memory of decisions — the project has its ADRs, audits and plan. *Misreading, text*: the
   harness's memory is the state between decisions — what each still waits on, where work stopped,
   what is open — which the same study found missing (owner's questions in eight places, a green
   PR three weeks stalled, 96 promises of "a separate PR").
2. One home per rule — `CLAUDE.md` as an index. *Misreading, text*: one home means one source
   copied by script and a check that fails on drift; the study's own strongest finding is a drift
   no index caught (two checks named as CI gates that CI does not run).
3. Done means checked — CI, tests, ratchets. *True, text*: the project's gates stay; the page
   should not offer this as the harness's gain.
4. An ignored rule becomes a record — rule 1д does it harder, a gate in the same PR. *True in
   part, function*: the harness's answer to a repeat is a rewording; the host refusing the act is
   the stronger form (q-0037.0006.0005.0001).
5. Decisions by weight — owner-only production, ADRs, the agent merging itself. *Text*: the
   harness's ladder is where the line is drawn and seen, not a prod gate; to be said by what it
   changes.
6. Seeing other sessions — `git fetch` and the open PRs. *True for worktrees*: see 9.
7. Work across projects — `/collaborate` and Workshop. *True*: the harness does not offer this.
8. The harness checks its own records, not the code, so it would put document discipline where
   gates stand — a step back by the project's own first principle. *Function and text*: the
   checks are not run by CI and not shipped as gates; and the page does not say they stand beside
   the project's gates.

## B. "It does not work here"

9. The session registry does not see sessions in separate worktrees, and the project works in a
   worktree per session. *True, function*: the store travels in the checkout; separate branches
   are deferred (q-0037.0017.0002.0001).
10. The hooks' interpreter is recorded per worktree, the store is per worktree, question ids are
    minted blind to other worktrees. *True, function*: as 9.
11. Long paths on Windows: entry names up to 204 characters, and the hook then silently returns
    one line instead of the window. *Function, a bug*.
12. Question slugs are built from `[a-z0-9]` only: a question in Russian gets a nameless file.
    *Function, a bug*.
13. An install into a tree with a method stops at the report: *this harness does not carry that
    step yet*. *True, function*: 01-0010.0150.0020 and 01-0010.0150.0030.
14. The clone failed on long paths on Windows; `python` on the path was the Store stub. *Function
    and text*: the skill's first steps on Windows.
15. `product.py` and `mechanisms.py` were red on the clone's HEAD. *To check*: green in the
    origin; likely the clone's partial checkout from 14.
16. Sixteen of eighteen mechanisms "due for re-check" a day after a maintenance pass. *Function*:
    the clock reads as noise.
17. The machinery holds the form of records, never their content, and only when the agent runs
    it. *Function*: checks at commit and at the host (q-0037.0006.0005.0001).

## C. "It conflicts, and it costs"

18. Its commit format (`IMPLEMENT:`) against the project's Conventional Commits. *Misreading,
    text*: that prefix is this tree's local rule and does not ship; the agent read the origin's own
    instance. The page should say the root is the harness's own project.
19. Its replies carry tables and glyphs against the project's `VOICE.md` and its app. *True,
    function*: the reply's head table and decisions table ship regardless of the debug setting;
    the voice belongs to the project (q-0037.0009.0021.0002).
20. Python and uv in a TypeScript repository. *Misreading in part, text*: uv is this tree's local
    habit; Python with the standard library is a true requirement.
21. Two rule sets for the agent to reconcile, and two sources that can disagree — the drift the
    project's rules file exists to stop. *Function and text*: the second mode, one import line from
    the project's own file, and which side wins (01-0010.0150.0020).
22. Weight per session: about 3,300 words of entry file, a 3,400-word glossary, the window every
    turn — by the harness's own measures ~90 tokens unchanged, ~4,400 redrawn, ~7,700 at start.
    *True, function and measure*: the settings that choose what text a tree carries
    (01-0010.0220); the main numbers (q-0033.0009).
23. Maturity: version 110 in seven weeks, many provisional marks, a commit every day — a product
    repository would chase changes. *Function and text*: releases a recipient chooses
    (01-0010.0190); the front page shows eleven raw `<straw-dog>` tags to whoever reads its source.

## D. "Its self-improvement is weaker"

24. Rewording a rule is weaker than "error → gate"; its own register shows 23 repeats after
    rewordings, and entry 50 says *three rewordings have not moved it*. *True, function*: the
    register's honesty is the evidence; the answer is the host's refusal, now in align.

## E. "The procedure is rigged"

25. The shelf calls the report a product document with *no self-deprecation* and keeps
    GoodWolf's limits to section 5 — so the report is built in GoodWolf's favour. *Text, a
    decision*: what the report must say of the harness's limits that bear on the person's choice,
    and where.
26. The harness's register records the earlier *no* answers about this very project as failures
    of its rules, and the procedure was then changed so a fresh agent writes the report. *Text, a
    decision*: the register is public and read by the agent being evaluated; an entry should name
    the page's or the procedure's failure, never a reader's verdict as the fault.
27. The README tells an agent asked *do we need this?* to run the install rather than answer.
    *Text*: read as the harness steering toward its own install.
28. So the report's recommendations lead to installing by construction. *Text*: follows from 25–27.

## F. Implied, not said

29. Most of the corpus is irrelevant to this project — dream, advise, celebrate, setup-devops,
    debugging, product, align, conclude, review-architecture — and the install ships it all.
    *Function and text*: what a tree carries is chosen by its settings (01-0010.0220); the page
    does not say so.
30. Implement, tdd, commit and improve-comments duplicate what the gates hold. *Text*: as 29.
31. Provisional marks are noise to a reader. *Function*: shear them from what a reader of the
    front page sees.
32. The method is prose for an agent, and the project's principle is *a rule without a mechanism
    of enforcement does not work*. *Function*: the core objection; answered only by enforcement
    (q-0037.0006.0005.0001) and by checks that run without the agent.
33. The evaluating agent read the origin's own root — its local rules, its debug setting, its
    commit prefix, its voice — as the harness. *Text*: the page says what ships and what is this
    repository's own.
34. The person's place adds little: agents merge their own ADRs and no harm was found. *True for
    this project's record*: the value is where the line is drawn and seen, to be shown, not
    claimed.
35. Duplicate sessions stopped after 09-27 without the harness; Cursor sessions follow the rules
    without it. *Implied: the rules reach without the harness*. Not to be answered on the page.
36. A study costs about 1.2 million tokens; the offer said a few hundred thousand. *True,
    measure*: the offer's estimate.
37. The version counter, the daily commits and the register's length read as churn and failure,
    not as a method built with itself. *Text*.
