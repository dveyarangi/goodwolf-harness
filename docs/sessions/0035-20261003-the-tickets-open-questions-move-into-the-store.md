# Session 35 — the tickets' open questions move into the store

**2026-10-03.** Claude Code, one conversation under three host session tags — `9f9f0714…`, then
`b10d79ee…` and `27fb8892…` after two resumes, the first two ended at `/maintain`. Entry contract
v22 at the wake, v24 at the close.

## What was done

[01-0011.0100.0020 open-issues-are-entries-of-the-store](../tickets/01-0011.0100.0020-open-issues-are-entries-of-the-store.md)
went through `/align`, `/plan` (with its own validation passes), `/implement` and `/verify`; its
decisions 1 to 6 are on the ticket. On the way the user split out
[01-0011.0100.0018 a-question-id-says-where-it-sits](../tickets/done/01-0011.0100.0018-a-question-id-says-where-it-sits.md),
which went from `/ticket` to its paired close the same day. The store's ids now nest, step by one;
an entry holds its own argument; a closure archives the subtree it finishes; every live ticket
names its question in `Answers`, and the *Open issues* section is gone from the format and from
the fifteen tickets that held one. The commits from `28c4efa` to `b7c0685` hold the detail.

Three `FIX`es on the user's word: the debug table holds the turn's path (v23); a question is named
by its id and its words, Q5 (v24, [rule failure 17](../rule-failures.md)); and, at `.0018`'s
verify, fenced examples are never rewritten and a freed id may return — the one risk deferred as
q-0001.0013 "How does the store remember every id it has given, so none is given twice?", its
remedy to be designed afresh if it strikes.

`xuanxue-workshop` was updated by hand from a local clone to `goodwolf-harness@ebde4ab`; its one
question renamed from the step-of-ten `q-0010` to `q-0001`; its `Repository:` line put back to
GitHub.

## What went wrong, and what it taught

- A one-off renumbering script wrote new ids before rewriting bare ids, and a compacted id equal
  to another's old id was caught twice. The restore was refused by the auto-mode classifier as
  irreversible; the user chose a repair in place, from each file's committed text with the map
  applied once. The product's rename cannot meet the chain — its new ids are free when drawn.
- The rename's bare-id pass cannot tell a reference from an example; fences now exempt, prose
  examples still rewritten (seen in two RFCs, repaired by hand).
- Core comments named a ticket by bare id, `.0020`'s decision N, and passed `.0018`'s verify; the
  leak check reads paths only — q-0018.0017 "Does the leak check catch a ticket named by a bare id
  in core?".
- A review the user could not follow cost two rounds: tickets and questions named by bare ids and
  a coined phrase. Q5 is the amendment; this fold's later review was its first grading.

## What continues

- **`/maintain`**: `.0020`'s paired close with its RFC — next, and `next-cycle=ask`.
- **Push**: `main` is seven commits ahead of `origin/main`; `xuanxue-workshop` announces
  `ebde4ab`, which a check from GitHub cannot resolve until they are pushed (`push=ask`).
- **`xuanxue-workshop`'s loader links**: `.claude/skills` and `.cursor/skills` are missing; the two
  `mklink /D` commands need an elevated prompt, or Windows' developer mode.
- **Open questions this session leaned**: q-0001 "How are the open questions of this tree kept, so
  that none is lost?"; q-0001.0006 "How does a conversation keep its position when its host
  resumes it under a new session id?", with two fresh resumes as evidence; q-0001.0010.0001 "Where
  do the arguments of closed questions live, now that an entry holds its own?", the tickets'
  *Decisions landed* sections; q-0018.0017 above.
- `docs/pacer.md` keeps an *Open issues* section of its own; it folds with
  [01-0020 pacer](../tickets/01-0020-pacer.md)'s align.
