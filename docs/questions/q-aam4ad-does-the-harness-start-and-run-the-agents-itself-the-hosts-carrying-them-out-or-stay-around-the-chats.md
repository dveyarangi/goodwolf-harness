# q-aam4ad Does the harness start and run the agents itself, the hosts carrying them out, or stay around the chats the person opens?

- **record of** what it intends to become
- **part of** q-m6unv4
- **state** open
- **rung** development: the whole product, self-improvement: the method
- **asks** the person, 2026-11-25
- **opened** 2026-11-25T06:54:42Z
- **struck** 0, last 2026-11-25T06:54Z

The align on the person's words of 2026-11-22, opened on their word of 2026-11-25: "проведи align
по словам от 22 ноября". The words, in paraphrase, stand in
[q-m6unv4](q-m6unv4-what-is-this-project-for.md), *The harness drives the agents*: each role or group of roles run in
short agents the harness starts, the next run picking up; the harness owning roles, state,
scheduling, permissions and messaging; Claude Code and Codex carrying the runs out; a UI that
observes and controls it.

## What the words asked for, and where each part stands — 2026-11-25

| part | where it stands |
|---|---|
| a role outlives a short run | accepted 2026-11-25 as one life, a chat that clears itself and opens by the recall; a first trial passed on an align, the whole being rewritten — [q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md), held by another session |
| a session that starts others | no directing session, 2026-11-15; a hub chat thought of for later, 2026-11-24; how far one starts sessions by itself is open — [q-ja5mp4](q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md) |
| a state shared by all | one server for every change of a question, accepted 2026-11-09 — [q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md) |
| a dashboard that also controls | a web page on that server, the lean of 2026-10-29, writing to sessions later — [q-pcnqd5](q-pcnqd5-how-does-the-person-see-the-whole-state-of-the-work-at-a-glance-the-questions-as-a-graph-the-records.md) |
| a role's permissions, prompt and tools | open — [q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md); refusals by the host [q-bsd3ga](q-bsd3ga-which-forbidden-actions-does-the-host-refuse-instead-of-trusting-the-agent.md); the host's app has no switch for tools by role |
| messages that cost less, their form held | the form of a reply is the voice's; that the harness renders it, no question found by name |
| the mechanisms' rules reaching the agent in full; tools in place of instructions for a procedure | scripts and hooks, a mechanism at a time; no one question found by name |

What no part answers is this question: whether a run is begun by the harness's own code, or by a
person in a host's app. [The glossary](../../.agents/glossary.md)'s *Harness* says it is not the
runtime that runs the model and its tools; a harness that starts a host is not that runtime
either, and the definition settles nothing of it.

## The necessity gate — 2026-11-25

The customer is the person, with their trees. Two problems were named: the standing chats cost too
much, and the sessions are neither seen nor controlled well enough.

- **Cost.** [The measure](../research/measures-2026-11-25/REPORT.md) of 17 to 24 November: in this
  tree 37 % of the week's units were begun by another session's letter, 28 % by the person; in
  fimonitor, half of all the units, 4 % by letters, 58 % by the person, 34 % by subagents. Clearing
  chats is put at some 22 % of this tree, roughly, unbuilt. A run the harness starts would save
  beyond that whatever its smaller opening saves; nothing measures it.
- **Sight and control.** Not counted. What the host's app cannot do, as the records have it: give
  a role its own tools, start a role nobody opened without the person's click, show what waits on
  the person in every session on one page.
- **The order.** The person's, [the roadmap](../roadmap.md): "расход первым".
- **The means exist.** Read on this machine the same day: `claude` 2.1.299 and `codex` 0.162.1
  answer from a shell; what a run started so costs, or whether it shows in the app, is not tried.

The load-bearing assumption is that a fresh run started by the harness does a role's work at less
cost and no worse than a chat that cleared itself. The cheapest example that could prove it wrong
is one role woken for the same piece of work both ways, as q-p4sdnv already proposes.
