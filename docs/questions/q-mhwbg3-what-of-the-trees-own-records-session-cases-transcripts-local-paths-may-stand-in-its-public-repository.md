# q-mhwbg3 What of the tree's own records — session cases, transcripts, local paths — may stand in its public repository?

- **record of** what it intends to become
- **part of** q-fjlob4
- **state** open
- **opened** 2026-11-20T18:22:06Z
- **struck** 0, last 2026-11-20T18:22Z

Opened 2026-11-20 from [the outside audit of that day](../research/external-audit-2026-11-20.md):
77 tracked files carry the person's local home path, 74 of them in `docs/cases`, which holds
93 MB of raw session and API dumps, and the repository is public. The cases are what a rule
failure is replayed against ([q-j5s7gp](q-j5s7gp-how-is-a-recorded-rule-failure-replayed-as-a-test-against-the-amended-rule.md)),
so removing them is not free. The ways: keep them as they are; scrub the paths and keep the
cases; move the cases out of the public tree, now and in history; or close this tree and publish
core from a repository of its own, as
[q-m3pldh](q-m3pldh-how-is-core-published-as-releases-to-a-repository-of-its-own.md) asks.

## Decisions

1. The local paths are scrubbed and the cases kept *(the user, 2026-11-20: «Вычистить пути»)*.
   The local user name is replaced by `owner`, the same length, in every tracked file: 329 files,
   3982 places. The history still holds the earlier bytes; it is not rewritten. A run report's
   `case_sha256` names the case as it was run, before the scrub.
   2026-11-22: the one tracked archive, `docs/case-runs/discover-material/2026-10-26-raw.zip`,
   had escaped the scrub, its members compressed — 73 of 466 members, 521 places; found by the
   judge of q-47f7je's check. Its members scrubbed the same way and the archive rewritten, its
   record's digests brought to the new members.

2. The person's email address is scrubbed too *(the user, 2026-11-21: «Да, вычистить»)*: replaced
   by a same-length placeholder in 64 tracked files, the API inputs and sources of `docs/cases`,
   where the host's context carried it. The history is not rewritten.

3. The person's name is scrubbed too *(the user, 2026-11-21: «Да, убрать»)*: replaced by
   same-length placeholders in seven tracked files — four cases' transcripts and three files of the
   audit of 2026-09-05. The history is not rewritten.

4. The commit-author address that 25 cases quote from `git log` stays *(the user, 2026-11-21:
   «Да, оставить»)*: it stands in every commit's metadata, which any reader of the public
   repository sees, so scrubbing the cases hides nothing. Hiding it is git's configuration, not a
   scrub.

## Where it stands

Still open: nothing keeps a new case from bringing the path, the address or the name back — a check that refuses them is the rule-failure
register's to build, put to its keeper on 2026-11-20.
