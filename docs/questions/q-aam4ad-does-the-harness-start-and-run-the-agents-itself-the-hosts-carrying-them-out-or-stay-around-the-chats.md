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

## What the words asked for, and what answers each part since — 2026-11-25

The person, of the first form of this question: "а с тех пор мы уже не решили или решаем часть этих
проблем другими средствами?" Most of it, read in the records and git the same day:

| part | built | decided or asked, not built |
|---|---|---|
| standing chats cost too much | the window shortened (9e37df11); a sleeping session told from one awake (0271f182); no frames in a reply to a session (v142, v143); six of the host's tools off in this clone, on trial | a chat that clears itself, one trial passed, the whole being rewritten; the bound at 20 and 50 % — [q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md), held by another session |
| a role outlives a short run | the wake opens with the name, the question and the unit (1262601d) | the same; a role understood from the task, `/recall` offering the roles on which work hangs — the same, decisions 2 and 8 |
| sight of the sessions and the work | the window's list of running sessions; the path at every recall (01-0060.0010); the board, drawn in the chat when asked ([BOARD.md](../../.agents/skills/pathfinder/BOARD.md)) | the server's web page — [q-pcnqd5](q-pcnqd5-how-does-the-person-see-the-whole-state-of-the-work-at-a-glance-the-questions-as-a-graph-the-records.md); what a drawing shows — [q-p7qw6i](q-p7qw6i-what-does-a-drawing-of-the-work-show-its-groups-their-subgroups-and-which-pulls-which-and-by-what.md); who puts a question that waits on the person — [q-2ng6nb](q-2ng6nb-which-session-puts-a-question-that-asks-the-person-and-how-is-it-known-that-it-was-put.md) |
| control of them from one place | the person's word to one session goes on to the holder quoted (L13); a pass with no person on the host's schedule | a hub chat, the person's "в будущем" of 2026-11-24 — [q-ja5mp4](q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md); writing to sessions through the page, later |
| a run begun without the person's click | a session the host's schedule starts; a card the person clicks | how far one session starts others — [q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md) |
| a role's permissions, tools and prompt | a commit that names no paths stopped in this clone, on trial | a role's bounds — [q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md); an edit waits for its skill, 01-0010.0125.0010 Ready — [q-bsd3ga](q-bsd3ga-which-forbidden-actions-does-the-host-refuse-instead-of-trusting-the-agent.md); tools by role, which the host's app has no switch for |
| the rules reaching the agent in full | a running session shown what changed in the entry file (990ac6d7) | the window past a host's cap, its hole — [q-dhrg3r](q-dhrg3r-what-does-the-window-show-once-the-open-questions-outgrow-what-a-host-puts-in-the-agent-context.md) |
| a state shared by all | a session in a worktree runs the harness (01-0010.0250.0020) | one server for every write, its tickets Planned — [q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md) |
| messages that cost less, their form held | the voice a role of its own | [q-53jkvy](q-53jkvy-is-the-voice-a-reply-speaks-in-its-own-mechanism-owning-how-everything-the-person-hears-is-said-apart.md); that the harness renders a message, no question found by name |

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
  the person in every session on one page. The records' own board and wake carry part of the last.
- **The order.** The person's, [the roadmap](../roadmap.md): "расход первым".
- **The means exist.** Read on this machine the same day: `claude` 2.1.299 and `codex` 0.162.1
  print their versions from a shell; what a run started so costs, or whether it shows in the app, is not tried.

The load-bearing assumption is that a fresh run started by the harness does a role's work at less
cost and no worse than a chat that cleared itself. The cheapest example that could prove it wrong
is one role woken for the same piece of work both ways, as q-p4sdnv already proposes.
