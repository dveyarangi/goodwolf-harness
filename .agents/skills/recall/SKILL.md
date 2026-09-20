---
name: recall
description: Determine where the project stands and what to work on next, with the decisions already taken surfaced alongside the questions genuinely still open. Use when asked what is next, where things stand, or to continue or pick up work.
---

<straw-dog until="01-0020 settles where /recall sits" ticket="docs/tickets/01-0020-pacer.md">Mechanism: not yet</straw-dog>


Your goal is to surf through available docs and code and find out actual state of the project and the current and/or next things to focus on, without re-opening anything already settled.

- Investigate last sessions and actual tickets against the roadmap/version plan and find out where are we standing. Sessions, `tickets/done` and `rfc/done` are dated snapshots — read them for *why*, never for *whether* something is still open. Check `git status` and recent log too: uncommitted work is part of the actual state.
- An open ticket or RFC whose work has landed in the tree, but whose acceptance criteria are not all checked, is the next session's first item. The still-open ticket is the evidence the work is unfinished; a session record is not. Live verification that could not complete in the shipping session is the usual remainder.
- Browse architecture, open questions and concerns; find out relevant decisions and items; make sure to look up for concern resolution or state all over the doc/code base - most of pending items are supposed to be at least referenced in existing documentation. Be thorough. Follow the references of the item in flight until they converge, rather than reading each doc in isolation.
- Every question you surface as open must cite where it is *still* open — in a maintained doc (delivery status, concerns, architecture, ADRs, glossary, edge records) or in the working tree. Otherwise it is settled: cite the deciding artifact instead, including the code where the code settled it. A question with no home at all is a documentation gap, so report it as one.
- Build a compact summary of current state of the project and bring up all relevant items for current or next task, including the decisions already taken that bear on it, each with its reference. The summary must be written in simple but precise language, no moonspeak.

- In case of ambiguity, present it too user. In case when continuation requires decision making, invoke /align skill.
- Report drift you hit while reading (stale headers, docs the tree has outrun) rather than fixing it — fixing is outside recall's scope.
