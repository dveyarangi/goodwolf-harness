# q-t5vmk3 How does core reach a recipient tree and leave it working, at a first install and at each update?

- **record of** what it intends to become
- **part of** q-veooj7
- **state** open
- **rung** development: a product slice, self-improvement: a rule
- **lean** the user, 2026-10-11: seven first installs in a day, the hook wiring stands; 2026-10-25: core works on Windows with long paths off and in any script, names fitted to a clone 128 deep, the store renamed to fit, the hook saying why a store is cut short (01-0010.0230); still open: the loader-link misjudgement and the release flow
- **opened** 2026-10-13T14:38:27Z
- **struck** 4, last 2026-10-25T19:28Z

## A fourth first install, 2026-10-11 — the clone landed in the project

Asked *install goodwolf-harness here* with the repository's URL, in an empty folder, the agent
ran the front page's first command, `git clone …`, into that folder, then the front page's next
step for a fresh clone, `--links`, in what was now the origin's own tree — and only then saw that
the front page describes another scenario. No install ran; nothing of the install skill was read:
in a fresh session the host loads no skill of the clone until the links exist, so the front page's
*Use it* is the only instruction an installing agent has, and its clone command names no
destination. The install itself needs no clone to read from — the script clones the repository
afresh — so the clone's one use is to hold the script and the skill. The front page is q-osjub2's.

**A fifth, the same day, after the front page said *beside your project — never into it*:** asked
*install <url> here* in an empty folder, the agent listed the folder and cloned into it before
reading anything. The clone precedes every text of ours, so no line on the front page can
prevent it; a line can only recover from it, and recovery by deleting the clone is what the
agent's permissions refused in the fourth run. The user: *it still happens.* What is left is the
installer: a clean clone of the origin standing where the project was meant holds nothing of the
person's, and could be turned in place into an install — the tree wiped, a fresh `git init`, core
installed from the repository at the clone's commit — on an explicit flag the front page names for
that case, the *source itself as target* refusal carrying the same hint.

## The clean clone's guard, repaired 2026-10-12

A judge probe under q-ctb74s found the guard read `git status` alone. Repaired under
repair=report against the rule the flag stands on — a clone holding anything of the person's is
refused (`run`'s and `_clean_clone_head`'s docstrings, the install skill). Tests written first
showed three ways through, not the one reported. A commit on HEAD that the origin lacks was already
refused, but by accident: the install could not resolve that commit in the source, and the refusal
named a ref rather than the person's work. An unpushed branch beside HEAD, and an ignored file of
the person's, were wiped. Naming `--at` skipped the guard entirely. The guard now refuses three
things whatever ref is named: a change; an ignored file other than the loader links and bytecode
caches that running the script leaves; a commit on any ref that no remote-tracking branch of origin
holds. Each refusal says to install into the project's own folder instead, or to push and move out
what the clone holds. The mechanism doc's target paragraph now states this. Verified by the full
suite. What remains uncertain: the remote-tracking branches are read as last fetched, so a commit
pushed from elsewhere after the last fetch still refuses. That errs toward refusing a clean clone.
It never wipes one that is not clean.

## An update from `06a2afd`, 2026-10-14

A recipient (meteoscape) updating from `06a2afd` to `8208fba` met three faults; it arrived with a
workaround for each. Two were repaired under repair=report, each with a test written first and
seen to fail as the recipient's run did:

- **The rehearsal crashed outside a repository.** The injection rehearsal, added 2026-10-13, runs
  over a scratch tree in the system's temporary folder; the injector lists a tree by Git, and
  that folder is inside none, so every install or update whose tree has a rules file crashed
  before its first write. The suite missed it: its process-proving fixture ships no rules file, and
  every other case answers listings from the folder. The scratch tree is now a repository of its
  own.
- **A front page the tree never received read as an edit.** An earlier ref's shipment is read
  with today's manifest, and the source's root `README.md` existed long before it shipped, so
  every tree installed before 2026-10-11 lacked a copy the comparison expected, and an update
  without `--overwrite` was refused. A missing copy of a root file placed beside core — the
  license, the front page — is no longer an edit; the next write restores it.

The third — the tree's own older script refusing a newer ref — is
[q-t4q6fi](q-t4q6fi-which-copy-of-the-script-runs-an-update-the-trees-own-or-the-incoming-refs.md).

## The migrations of 2026-11-15 — what the migrated trees met

research-harness, codename_japaka and game-gamma took core at `b1c55c76` while their ids were
migrated; the session that ran the migrations passed up what each met.

- **Mended.** A tree whose settings differ from the origin's read as edited in core. The entry
  file ships holding each mechanism's block as the origin's settings rendered it, the tree's
  installer renders the same rules under its own, and the comparison with the ref read the
  difference as an edit: a check said *not arrived* after a clean update, and an update asked
  for `--overwrite`. The comparison now sets such a block aside on both sides; whether it is the
  one the settings call for stays the injector's gate. Proved on game-gamma, debugging off: the
  check passes.
- **Mended.** The front page ships as written and lands beside the harness skill, where its six
  links written from the origin's root resolved to nothing. They are whole addresses now, and a
  test holds the page to it.
- **Left as it is.** `--from` naming a clone on disk whose folder is not the repository's name is
  refused — "the tree announces goodwolf-harness; --from names agents" — so no tree updates from
  this clone by `--from`; a run with no `--from` takes the tree's own source and passes. The
  user, 2026-11-16: "нет, только из репозитория. ничего не надо менять, пользователь не будет
  устанавливать из локальной папки, это происходит только у меня".
- **Open.** The citation reader takes `s[k,i→j](t)` inside an indented code block for a link:
  noise in a migration's report so far, a refusal once a check meets it.
- **Open.** A plain clone of the origin fails on Windows with long paths off, on the names under
  `docs/cases/*/source-artifacts`. The installer's own clone checks nothing out and is not
  touched by it.
- **Open.** A first install from the origin's head ends *not arrived* on the shape check —
  "debugging: local.rules.md does not resolve" — in a tree that has no local file yet. Met by
  the judge of the mended comparison in a scratch recipient, before and after the mend; not yet
  traced.
- **Open.** A tree under its own setting has its entry file written again at every update, the
  same ref included, and the injector re-render it: the outcome is right and the report names a
  file nothing changed in. Whether a copy already holds what ships is not yet read the way the
  comparison is.
- **Met once, mended there by hand.** xuanxue-workshop, updated to `b1c55c76` on 2026-11-15,
  kept its debugging in a local rule written before settings existed — a rule's prose saying
  `debug=on`. The settings read only the local file's table, so the update left the tree at the
  default, off, with nothing said; its ref gate then read the entry file as edited, the fault
  mended since, until `--set debug=on` was run. Of the trees on this machine it alone held the
  old form; the rest hold the table or set nothing. No change is proposed while it stays one
  tree. The same tree met the refusal of `--from` by a folder's name, and went around it and
  the long names under `docs/cases` at once by cloning without a checkout into a folder named
  as the repository is.
- **Mended.** fimonitor's update from `04e18cab` refused a file it had never touched as
  edited in core. Its install commit holds every `TODO` line of core's scripts with its question's
  id, though an installer at that ref shears them: the tree was written by an older clone's
  installer, whose grammar knew only the dotted form of an id, and a first install is not handed
  to the incoming ref's own installer as an update is. Today's reading of what that ref shipped
  then differs from the tree by those ids alone. The comparison now shears a copy's `TODO` ids
  as the shipment's are sheared, so such lines read as no edit and the next write brings them to
  form. Judged by another, who rebuilt the tree's scripts byte for byte with a clone's
  installer of 2026-11-02 and found the mend's own fault — one pass of the shear leaves the
  second of two ids a line names — so both sides are sheared alike. **Open** beside it: a first install run from an older clone writes a tree in that
  clone's transformations, whatever ref it installs.
- **Open, found by the judge of the mend above.** A tree's announce line names its ref by the
  short commit git gave on the day of its install; as the repository grows git abbreviates the
  same commit longer. studies announces `goodwolf-harness@b048a88`; today's clone names that
  commit `b048a88e`, so the entry file as shipped today differs from the tree's by one
  character of the stamp, reads as an edit in core, and its update would be refused. The
  mechanism's doc says the announce line is set aside when a copy is compared; the comparison
  sets aside the repository line and relies on the stamps being equal. Not mended.
