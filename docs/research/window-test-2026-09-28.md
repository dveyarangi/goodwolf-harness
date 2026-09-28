# The window test — what a model reads to place a message in a question store, 2026-09-28

A spike inside [01-0011.0100](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md)'s
align, run on the user's request after the question *is 30,000 entries something an agent can read
and understand the hierarchy from?* It measures three claims the align had been making: that a
model placing a message needs only the window (decisions 26 and 33); that a rendering of the whole
store is readable at all as the store grows; and which rendering a model reads hierarchy from best.
The generator, scorer, taxonomy, trials and every answer are kept beside this record in
[`window-test/`](./window-test/) so the test reruns when the format changes.

## Design

**Stores.** A taxonomy of 795 design questions of one realistic product — a multiplayer web
strategy game with backend, matchmaking, content pipeline, live-ops, billing and a modding SDK —
written once by a model to a fixed shape: 9 roots, root bias (8–25 children per root), most
leaves at depth 3–4, chains to depth 8, 55% closed over the six kinds, ids shuffled so they carry
no hierarchy. From it, four stores: **100** (a connected subtree of two roots), **1,000** (the
taxonomy plus one product-line copy, trimmed by dropping shallow leaves), **10,000** and **30,000**
(13 and 38 tagged product-line copies). Every node of a copy carries its product tag in the title.

**Renderings.** *flat*: one line per entry, `id | parent | state | title`, sorted by id.
*tree*: indented by depth. *paths*: `root/child/.../id  [state] title`, a directory listing.
*window*: from a stored current id, the path root to current, the open children of every
question on the path, every open question under the current root with its parent id, one line per
other root, and the recent positions — decision 33's content, rendered by a script.

**Tasks.** *place_near*: a real entry is hidden from the rendering and its title arrives as a new
question; the current position is one of its siblings; answer its parent. *place_far*: the same
with the current position in a different root. *path*: list the ancestors of a given id.
*children*: list the open direct children of a given id. Ground truth is the store's.

**Reader.** One fresh general-purpose subagent per trial (Sonnet), told to read only the one file
and answer one line. 83 trials: two per cell at 100 and 1,000, one per cell at 10,000 and 30,000,
whole-store renderings thinned at the large sizes. Scored by
[`score.py`](./window-test/score.py): *exact*, *near* (grandparent or sibling of the true parent),
*root* (a far jump under the window landing on the hidden question's root — the correct first-turn
outcome, since that root is one line in the window), *wrong*, *incomplete* where the reader said it
did not finish the file.

## Results

| size | rendering | place near | place far | path | children |
|---|---|---|---|---|---|
| 100 | flat | near, exact | wrong, exact | exact, exact | exact, exact |
| 100 | tree | exact, exact | exact, wrong | exact, exact | exact, exact |
| 100 | paths | exact, exact | exact, exact | exact, exact | exact, exact |
| 100 | window | exact, exact | root, root | exact, exact | exact, exact |
| 1,000 | flat | exact, exact | exact, wrong | exact, exact | exact, exact |
| 1,000 | tree | exact, exact | exact, exact | exact, exact | exact, exact |
| 1,000 | paths | exact, exact | exact, exact | exact, exact | exact, exact |
| 1,000 | window | exact, exact | root, wrong | exact, exact | exact, exact |
| 10,000 | flat | exact | — | exact, incomplete | — |
| 10,000 | tree | exact, incomplete | — | exact, incomplete | — |
| 10,000 | paths | exact | — | exact | — |
| 10,000 | window | exact | root | exact | exact |
| 30,000 | flat | exact, incomplete | — | — | — |
| 30,000 | window | exact, exact¹ | root, wrong | exact, exact | exact, exact |

¹ The second reader replied the exact parent in its hand-back and did not write its answer file;
scored from the hand-back.

**Cost per trial, from the readers' own usage.** Tokens include the subagent's fixed overhead,
about 59,000, which is why a 700-token window costs 60,000.

| rendering | size | lines read | tokens | seconds |
|---|---|---|---|---|
| window | 100 | 41 | 60,000 | 18–22 |
| window | 1,000 | 54 | 61,000 | 20–27 |
| window | 10,000 | 189 | 65,000 | 13–18 |
| window | 30,000 | 414 | 73,000–76,000 | 13–41 |
| flat / tree / paths | 100 | 115 | 63,000–67,000 | 20–60 |
| flat / tree / paths | 1,000 | 999 | 97,000–114,000 | 31–110 |
| flat / tree / paths | 10,000 | 3,000–10,000 | 197,000–537,000 | 80–175 |
| flat | 30,000 | 4,940 of 30,000 | 291,000 | 147 |

**What each miss was.**

- *100 flat near*: grandparent given for parent. *100 flat far*, *100 tree far*, *1,000 flat far*:
  a plausible neighbour in the wrong branch. Whole-store far placement: 9 of 12 exact.
- *Window far jumps*: 5 of 7 landed on the hidden question's root, the designed first-turn
  outcome; 2 of 7 chose another root's line. The window cannot do better on a far jump by
  construction, since the target's subtree is not in it.
- *Incomplete reads*: at 10,000 entries three whole-store readers stopped before the end of the
  file — after 3,000, 5,798 and 8,400 lines — and answered anyway; two of the three were right
  because the target's neighbourhood happened to be in what they had read. At 30,000 the flat
  reader read 4,940 lines, found the product block it needed, spot-checked the rest, and answered
  correctly by exploiting the copies' identical structure — which it explained in its hand-back.

## What the test says

1. **The window holds at every size, at constant cost.** Exact on every near placement, path
   and children task from 100 to 30,000 entries; the window itself grew from 700 to 9,000 tokens
   while the store grew three hundredfold. Decision 33's bound — the current root's open subtree —
   is what kept it flat: the 30,000 store has 342 roots and the window never saw more than one.
2. **Whole-store reading degrades silently, not loudly.** At 10,000 entries readers stop partway
   and answer with confidence; the answer file carries no sign of it unless the reader is told to
   say so. This is the hazard the user's question was pointing at, and it is worse than a refusal:
   a wrong placement from a partial read looks exactly like a right one. At 30,000 nothing read
   the file; the one reader that answered did so by recognising the synthetic copies.
3. **Rendering does not separate on accuracy at the sizes where a whole store is readable.**
   Flat, tree and paths are within one trial of each other at 100 and 1,000; paths was cleanest on
   far placement (4 of 4). So the choice of the store's *written* form is not decided by reader
   accuracy — the reader never reads the store — and falls to writing cost and insertion cost,
   which the passes already decided for flat files with a parent line.
4. **A far jump needs its second turn, and a search fallback would help.** Landing on the root is
   correct and insufficient; the second turn's window is that root's. Two of seven picked the
   wrong root from the other-roots lines, which in a real store lack the product tag that made
   these easy. A title search over the store when the judge says *nothing here* — decision 29's
   accepted-miss fallback — is the cheap repair.
5. **Token cost is dominated by the reader's fixed overhead, not by the window.** A jev-style
   judge with no agent overhead would read a 30,000-entry store's window for under 10,000 tokens.

## Limitations

- The large stores are tagged copies of one 795-node taxonomy. A reader can and did exploit the
  repetition; real stores of 30,000 distinct questions would be harder for whole-store reading and
  no easier for the window, whose content does not depend on the rest.
- One trial per cell at 10,000 and 30,000; two at the small sizes. The table is indicative, not
  statistical.
- The reader was Sonnet with the harness's full agent overhead; the judge in production may be
  smaller or larger. Accuracy claims are about this reader.
- The window's *path* and *children* tasks are trivial by construction, since the window prints
  the path; they measure reading, not finding. The placement tasks are the ones that matter.
- Far jumps under the window were scored on the first turn only; the second turn was not run.
