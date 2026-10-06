# Session 38 — three issues close, and the pass gets its ticket

**2026-10-05 to 2026-10-07.** Claude Code, one conversation, which its host resumed under three
session ids: `5d42dc06…`, `f1e6d9b5…`, `5b274edf…`. Entry contract v30 at the wake, v31 at the
close. Twenty-four commits, all pushed. A forked session worked on rewording a question in the
same tree throughout; its files were left out of every commit here.

## What was done

- **The update in a recipient.** The user pasted xuanxue-workshop's two update reports. The loader
  links held after the make-first fix. The comparison read the block a recipient's own mechanism
  installs into a core skill as an edit in core, so `arrived` was false of a correct tree and
  every update needed `--overwrite`; a `FIX` sets aside the block of every mechanism whose rules
  file stands in the tree and never shipped. The install and update questions were gathered under
  one parent, q-0018.0020 "How does core reach a recipient tree and leave it working, at a first
  install and at each update?".
- **Issue 2** ran `/align`: a document under `docs/` informs and neither instructs an agent nor
  authorizes it to act; met while reading, it is not acted on and reported as drift. Landed by
  hand in the entry file as a straw dog, v31; nothing installed into `/maintain`. The record is
  [the entry contract's evidence](../research/entry-contract-findings.md). Closed on GitHub.
- **The pass.** The question of who checks a rule with no moment widened, in the user's words,
  into judging as a method — a second pass on the same object under mostly different rules and
  data. An outside pass, [filed verbatim](../research/discover-second-pass-2026-10-05.md), found
  no accepted umbrella term and several fields that keep the activities apart. Formalized as
  [01-0030 a-second-look-is-a-pass](../tickets/01-0030-a-second-look-is-a-pass.md): three working
  words, six operations, nine parameters, five forks under q-0029 — a candidate mechanism the
  user revises before anything is built. Its align's necessity gate did not pass; the user chose
  another issue.
- **Issue 1** closed through two tickets.
  [01-0010.0172](../tickets/done/01-0010.0172-a-first-install-says-what-stopped-it.md): the
  ownership refusal carries Git's own `safe.directory` command; a pending link is an accepted
  state *(the user)*; `harness.py . --links` is the per-clone step, no source and no network;
  every planned link is named in the clone's exclude file, which Git locates; the links stay
  untracked, the tracked-with-repair option written into ADR-0003 as declined.
  [01-0010.0171](../tickets/done/01-0010.0171-an-empty-folder-is-initialised-on-install.md), split
  from `.0170`: an empty folder inside no repository is initialised by `--install` *(the user)*; a
  folder holding files or a subfolder is refused with the step; the architecture now says why a
  target is a repository.
- **Issue 3**: `/skill-up`'s description gained *agent instructions written in a reply*, one word
  narrower than asked. Closed.
- The switches: commit to `auto`; push to `auto` and back to `ask` the same hour, since another
  session shares the tree.

## What went wrong, and what it taught

- The caller and signature edits of the comparison fix were applied with a script, against the
  user's standing preference for edit tools. Owned in the reply; the later work used the tools.
- The close commit of `.0172` swept in one of the forked session's files; taken back out with an
  amend before the push. A shared working tree needs an explicit add list every time.
- Git's own ownership knob proves nothing on a Git older than 2.35.2; the suite's machine runs
  2.32. The refusal is proved against Git's message, and the knob's test skips where Git predates
  the check. In the harness's evidence.
- The host resumed the conversation under three ids, each leaving a running row:
  q-0001.0006 "How does a conversation keep its position when its host resumes it under a new
  session id?", struck again.
- The first recommendation on the maintain half of issue 2 — write it by hand and wait for an
  undeclared practice mechanism — missed that both candidate owners were declared; the user's
  framing, a generic rule or maintain's own job, was better, and better again when they said
  maintain needs no injection.

## What continues

- **`.0040`'s last box** waits only for the user's grade: this conversation's first turn gave a
  fresh session's `▶` row and a `↳` with a `+` at its first question.
- **Next in the queue**, under `next-cycle=ask`:
  [01-0010.0170 arrival-becomes-a-sequence](../tickets/01-0010.0170-arrival-becomes-a-sequence.md),
  Ready and AFK, the first install's last step.
- **01-0030** waits for the user's revision of the shape; its gate needs an observed problem,
  and the cheapest test is `/verify` described by the pass's nine parameters.
- **Left from issue 2:** no glossary entry for *invariant* yet, and `/maintain`'s own text still
  says "docs to the meta-rules" rather than naming the entry file's rules — both held back while
  the vocabulary is under q-0029. `docs/process.md` holds method text in instruction form, noted
  on q-0024.0002.0003 "What does docs/process.md keep once method text leaves it?".
- **Opened and left open:** q-0024.0008 "Does every mechanism that governs what is written owe
  /maintain a re-check of it, installed from its own rules?" and q-0024.0009 "What kinds of
  written thing does a tree hold, and which of them does /maintain hold in agreement?";
  q-0001.0021 "How is a question reworded once the work shows its wording is outdated, and when
  does rewording replace opening a parent?", which the forked session took up;
  q-0018.0020.0006 "Why did an update run by Codex judge correct loader links wrong?", still
  unexplained, the links having held since.
- **The forked session's files** are uncommitted in the tree: the questions script, its tests,
  skill, doc and rules file, `AGENTS.md` and the entry contract's record.
