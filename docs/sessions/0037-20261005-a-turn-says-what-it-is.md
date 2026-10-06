# Session 37 — a turn says what it is

**2026-10-04 to 2026-10-05.** Claude Code, one conversation, which its host resumed under a new
session id three times: `bd200f86…`, `8121b2f7…`, `5a9026da…`, `17658ee1…`. Entry contract v25 at
the wake, v26 at the close.

## What was done

A `/maintain` pass over the whole tree, nothing due: nine stale session rows ended, the queue's
counts repaired, its two decisions waiting at `/align` moved into the store as q-0024.0006 "Is an
ADR or a ticket the home for a decision?" and q-0026.0003 "What does an entry-contract version
cover?", four dead links repaired.

Two `FIX`es on the user's report from xuanxue-workshop: an update run by Codex removed both loader
links and was then refused the privilege to make new ones. A repoint now makes the replacement
first; the story is in [the harness's evidence](../mechanisms/harness.evidence.md).

Then [01-0011.0100.0040 the-turn-is-steered-from-the-store](../tickets/done/01-0011.0100.0040-the-turn-is-steered-from-the-store.md)
ran `/align`, three `/plan` passes, `/implement`, `/verify` and `/maintain`; its eight decisions
are on the ticket. The slice was minted to build a judge and became what a turn shows: the
question that contains its message, a question it opened, a process, or uncharted. The commits
from `e3c8593` to `071388a` hold the detail; all pushed.

## What went wrong, and what it taught

- The align's necessity gate reported no observed problem. The user pointed at the reply headers
  of this same conversation: six of seven showed a question the turn did not stand on. That is
  rule failure 18, and it became the ticket.
- The first recommendation was put in decision numbers, as if the user had read what the agent
  had. The user stopped it; later ones were put in plain words.
- Three proposals in a row were answered by the user dissolving them: a turn count for an
  unplaced question, a wait for the user before opening a missing parent, a brake on the renames
  a regrouping costs. Each had guarded against a judgement the agent can make.
- The installer fix was started before the user said to. They accepted it.
- The seven-message replay was appended to the evidence by a shell command, against the user's
  standing preference for edit tools.

## What continues

- **First in the next session**: the ticket's last box. A fresh session's wake shows `▶ /recall`
  and its first question a `↳` or a `+` row; if so, `/maintain` closes the ticket with its RFC.
- **Next in the queue** after it: [01-0011.0100.0050 a-question-branches-before-it-is-answered](../tickets/01-0011.0100.0050-a-question-branches-before-it-is-answered.md),
  its `/align` first. It was planned around a judge on the draft, and the judge on the request
  was just held back: its gate should be read against that.
- **Open questions this session opened or leaned**: q-0001.0016.0001 "Does placing a message
  need a judge outside the agent that answers it?"; q-0024.0006 and q-0026.0003, above;
  q-0001.0006 "How does a conversation keep its position when its host resumes it under a new
  session id?", struck three more times here.
- **Never found**: why correct loader links were judged wrong under Codex. The installer's report
  now says where a repointed link pointed, so the next occurrence answers it.
- **Recipients**: xuanxue-workshop takes the installer fix and the reworded rule at its next
  update.
