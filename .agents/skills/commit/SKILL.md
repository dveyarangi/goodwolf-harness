---
name: commit
description: >-
  Use when committing or pushing changes to the repository.
---

<straw-dog question="q-0037.0009.0005">Mechanism: not yet</straw-dog>

- Commit the work in current session only. Do not commit changes of other session that might represent a work in progress. When in doubt, ask user.

- Look at pending changes; group them by content aligning with origin topic, ticket, rfc or change type (documentation, code, CI, skills).

- Separate implementation and documentation commits.

- Write the subject in the project's own convention, where it states one.

- In case the file changes belong to several groups, commit the file with the group forming its dominant topic and mention the bleed in that commit's message.

- Do not reference sessions in commit comments, sessions are ephemeral.

- Unless already working in branch or instructed to branch - commit to default branch.

- Work the person holds back stays on its own branch, never merged into the shared main until they
  release it: whatever stands on main may be published.

- When committing a code change, first run the checks the repository defines for itself — its
  linter, its formatter in check mode, its type checker, its tests. Pure doc changes need none
  of them. **Read them from where the project states them; never carry them here.** A commit
  skill holding a project's commands is a second home for them, and it is wrong for every
  project but the one it was written in.

- Commit and push only as the entry file's `commit` and `push` switches allow; a push is its own
  permission, never implied by a commit's.

<installed by="local">
**L8** Prefix the subject with the loop step that produced the work, uppercase, then a colon — one of
these and no other: `ALIGN`, `TICKET`, `PLAN`, `IMPLEMENT`, `VERIFY`, `MAINTAIN`,
`DISCOVER`, `RECALL`, `CONCLUDE`; outside the ring, `FIX` for a repair taken on its own, `EQUIP`
for a change to the harness's own installation, `DREAM` for a record the second lobe wrote. A
name for what the commit touched — the entry file, the local rules, the question store, an RFC —
is not a step: a rule landed at an align is `ALIGN`, a question opened while planning is `PLAN`.
One prefix per commit; where the work spans two steps, take the dominant one and name the bleed in
the message.
</installed>
