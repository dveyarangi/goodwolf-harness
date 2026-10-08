# q-0031 What is the harness, said to a reader who arrives cold, and what of it does the front page carry?

- **state** open
- **struck** 0, last 2026-10-07T23:12Z

Opened 2026-10-08 when the user asked for the front page to be rethought: the page of 2026-09-26
called the harness *an institutional memory in the repository*, and the tree had since gained the
question store, the four kinds of record by source of truth, the turn placed on its question, and
the whiteboard. The user's candidate line: *persistent project cognition for stateless coding
agents: preserve architectural truth, unresolved reasoning and work state so fresh agents can
retrieve narrowly instead of repeatedly rediscovering the codebase.*

What the draft of 2026-10-08 took from it and what it refused, for the user to weigh:

- Taken: *stateless*; *unresolved reasoning* as a first-class thing kept — the store earns it, and
  the old page had no word for it; *retrieve narrowly* — the window and the tiers are exactly that.
- Refused in the draft: *cognition*, on the ground that the harness is not a memory architecture.
  **That ground was wrong** *(the user challenged it, 2026-10-08)*: the
  [discover pass](../research/discover-what-this-is.md) rated family E, a self-improving agent
  memory architecture, medium-high, and its second model rated *organizational memory for an
  ephemeral workforce* high. It is a memory architecture — of the project, not of the agent. What
  sets it apart within that family: the memory is the project's and outlives every agent, shared
  across hosts and readable by a person; retrieval is by position in the question tree, not by
  similarity; and each record carries its source of truth and so the direction of its repair,
  which makes it closer to truth maintenance than to recall. *Cognition* in the user's phrase
  reads as distributed cognition — transient agents and durable artifacts as one system — which is
  defensible; the remaining objection is only how a cold reader takes the word, and that is
  untested.
- Refused: *rediscovering the codebase*. Code is the one thing an agent recovers well; what it
  cannot recover from code is the why, the rejected, the open and the stopped. The loss the page
  names is re-deciding, re-asking and re-doing.
- Missing from the line, and kept on the page: that the records are *kept true* — the kind of each
  record fixes the direction of its repair — and that the method governs itself. Without the
  first, the page describes a docs folder.

**Two `/discover` passes of 2026-10-08**, filed whole in
[discover-recall-structure-2026-10-08](../research/discover-recall-structure-2026-10-08.md), at
the user's request. The user had struck two claims: that embeddings are what sets the recall apart
(*embeddings are already going out of use*), and that a source of truth per record replaces a
recall structure (*it does not mean there is none*). What the material bears on this question:

- **The embedding claim is narrower than either side put it.** Single-vector top-k as the only
  path is losing ground, most clearly in coding agents, where agent-driven grep and navigation are
  now the backbone. Hybrids that keep an embedding channel remain the default in the memory
  literature, and Cursor measured grep plus semantic search beating grep alone. The field's
  attention moved from *which retriever* to *who controls retrieval, and how memory is written and
  verified*. So "no embeddings" sets nothing apart. What may set the harness apart is what selects
  instead.
- **The recall structure is rich, and has several selectors.** Position: the window is a
  locality prefetch, or shelf-browsing around the current call number. Activation: the strike
  count is ACT-R's base level with no decay. Dependency: suspect entries and due straw dogs come
  back because a supporting answer moved, which is truth maintenance. Obligation: tier-1 rules
  force reads. Pull is orienteering from hubs, with grep as the last resort. Neither pass found a
  published peer for a per-message push keyed on the session's position, rather than the query,
  together with a mandatory placement before the reply. Both say this is absence of evidence.
- **The source-of-truth sort is a separate axis.** Both passes read it as reconciliation or truth
  maintenance, not as recall. The user was right: it does not stand in for recall.
- **Weaknesses both passes name, measured or from the records:** the strike count never decays,
  so old questions stay ranked; the wake grows with every session ever registered, 104 lines,
  mostly ended sessions; the queue every recall reads is 58 KB, its history line 36 KB;
  single-parent placement is where rule failure 18 struck; a wrong placement makes the next push
  wrong; nothing measures whether a pushed line was used; Cursor gets no per-message push.

**The second draft, 2026-10-08, built around what the reader gets.** The user: *two axes are not
all there is in the harness; it has to be presented as a useful tool, not as a technical
curiosity.* The draft now opens on the jobs: eight problems of working with agents over weeks,
each with what changes. Then come a real example from this tree, who it is for and who not yet,
what it costs in measured sizes, and only then how it works, with the two axes inside it. Its
evidence is the [adoption panel](../research/adoption-panel-2026-09-26.md). Its six runs came
back *not for my case* on merit, while crediting the decision model. Across the runs the readers
asked for three things: the team limit up front, cost figures, and a worked example. The
greenfield reader's *the ceremony has nothing to bite on yet* became the page's line on who it is
not for.

The first example drafted was false. It said a fresh session picked up overnight what an
afternoon align had left. The transcripts show one conversation, resumed by the host under three
ids. It was replaced by a story the records bear out: q-0024.0009 was opened on 2026-10-05 and
left with its lean. The new conversation of 2026-10-06 went for the queue's next item, came back
to that question through it, and by 2026-10-08 had turned it into a spec, five tickets and two
landed slices.

Decisions of 2026-09-26 that still bind the page: written for a cold human and for an agent handed
the link; points into core, never into `docs/`; the title *GoodWolf Harness*; not a second home
for the flow. The page is kept out of the install manifest, so a published core has no front page
— [01-0010.0190](../tickets/01-0010.0190-core-is-published-as-a-release.md)'s.

Drift the rewrite found: the switches line read `commit=ask` against L2's `commit=auto` since
2026-10-05. Repaired in the draft.

Still open under this question: whether the page shows the diagram, which does not draw the store;
whether a worked example and cost figures ever land on it (waits on q-0018.0008).
