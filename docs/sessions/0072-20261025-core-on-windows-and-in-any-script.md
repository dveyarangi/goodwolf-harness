# Session 0072 — core on Windows and in any script

- **record of** what happened

2026-10-25. Started by the session weighing the objections of the run-4 meeting in xuanxue-cabinet
([the objections](../research/meeting-run4-objections.md), items 11, 12 and 14). The user had
decided to fix the cheap and embarrassing ones in parallel. This session fixed three bugs an
evaluating agent met on Windows through the delivery ring, then renamed the store on the user's
word.

## Decisions

- **One ticket for three bugs.** [01-0010.0230](../tickets/done/01-0010.0230-core-works-on-windows-and-in-any-script.md)
  answers [q-0037.0006.0020.0014](../questions/done/q-0037.0006.0020.0014-what-stops-core-working-in-a-recipient-on-windows-or-in-a-language-other-than-english.md).
  Each bug touched a few lines and no record's format, so splitting them would have tripled the
  ceremony for nothing.
- **A name is fitted to a clone 128 characters deep, not to this tree's root.** The old fit
  measured from `D:\Dev\AI\agents` (16 characters), so it never cut, while a clone into a
  session's scratch folder stands about 120 deep. The room is a constant, `CLONE_ROOM`. A name
  also keeps within 255 UTF-8 bytes (`NAME_LIMIT`), and the fit cuts inside a word where a script
  writes none between words. The check also accepts the fit names were written by before, so no
  recipient's names break.
- **A slug keeps letters, digits and their marks in any script, NFC.** `[^\W_]` alone was the
  first version; the verifier showed it splits Hindi and Thai at their vowel marks.
- **The hook refuses only where the machine cannot hold the path.** That means Windows with
  `LongPathsEnabled` off, read from the registry, against the names `HEAD` holds. The first
  version read missing files from the index, but a checkout stopped by the limit writes no index,
  so it saw nothing. It also refused falsely after an uncommitted move. Both came from the
  verifier: it reproduced a real clone, which the test fixture did not.
- **`python` on Windows.** `hook.sh` already ran the interpreter the link step recorded, so the
  fix is text: the harness skill's install step and the wrapper's notice name `py -3`.
- **The store renamed, the user: "переименовывай".** All 110 over-long entries went through
  `move_doc`, since the store's `reword` refuses closed questions and unchanged words. The
  longest tracked path is now 130 characters. A clone with `core.longpaths=false` into a
  123-character folder checked out whole.
- **The guard was dropped, the user: "забей".** A check over every tracked path, a store call
  `fit` and a suite test were proposed;
  [q-0037.0006.0020.0015](../questions/done/q-0037.0006.0020.0015-what-keeps-every-path-a-tree-holds-within-what-a-clone-on-windows-can-check-out.md)
  was pruned. Nothing fails today if a long name is written by hand.

## What went wrong

- **The builder's tests passed for the wrong reason twice.** The hook test deleted a file with the
  index intact, a state no real clone leaves. The fit test measured from the test's short temp
  root. An independent verifier caught both by reproducing the real case. The lesson: a promise
  about a state the world produces is tested on that state, as `/verify` already says.
- **A race with another session.** While the rename was being staged, another session closed
  q-0037.0010.0009.0007 into `done/`. The rename's commit dropped the entry; the restore then put
  it in `HEAD` twice. Two small commits settled it. Staging by building each file's blob from
  `HEAD` kept the other sessions' uncommitted edits out of the commits.
- **Six needless messages.** Six sessions were told their entries' files moved, read from the
  store's register, which keeps a session "running" until its conclude or three hours of silence.
  One was closed in the app, and all six started a turn on the message. A rename is neither found
  nor opened in another's subtree, and calls go by id. The user dropped registering it.
- **Heredocs through the Bash tool** twice left a NUL byte or failed to parse. Writing the script
  to a file first worked.

## Open, and what continues

- [q-0037.0006.0020](../questions/q-0037.0006.0020-how-does-core-reach-a-recipient-tree-and-leave-it-working-at-a-first-install-and-at-each.md)
  stays open on the loader-link misjudgement and the release flow.
- The follow-ups the verifier left are in
  [the plan's out-of-scope list](../rfc/done/01-0010.0230-core-works-on-windows-and-in-any-script.md):
  - Windows long paths on but Git's off: reasoned, not probed.
  - The citation reader stops at a combining mark.
  - The fit counts code points where Windows counts UTF-16 units.
  - Twin detection's stopwords are English only.
- First step of the next session in this subtree: none pressing. A fresh session in
  xuanxue-cabinet would show whether objections 11, 12 and 14 are gone from its reading.
