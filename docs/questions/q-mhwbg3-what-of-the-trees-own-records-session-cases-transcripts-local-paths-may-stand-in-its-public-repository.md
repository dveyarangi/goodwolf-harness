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

## Where it stands

Still open: the person's email address stands in 64 tracked files, most of them the API inputs of
`docs/cases`, carried there from the host's context; and nothing keeps a new case from bringing
the path back.
