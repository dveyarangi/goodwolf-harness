#!/bin/sh
# Mechanism: session
# A commit that names no paths, stopped by Git (S5): in a tree where other sessions run, the index
# is shared, and such a commit takes whatever it holds. The clone's `pre-commit` runs this from the
# work tree's top, for an agent's commit made from the shared index: Git says by the index it hands
# the hook how the commit was asked for, `next-index-...` where its paths are named, `index` where
# none are, `index.lock` for `-a` and `-i`. No document of Git's promises those names.
#
# The hook itself lets the rest by, so that a commit that passes starts nothing while Git holds the
# index's lock, and a broken copy of this file stops no such commit. An agent is told by
# CLAUDE_CODE_CHILD_SESSION, which Claude Code gives the commands it runs and no terminal.
#
# Not seen: a directory or a glob among the paths, a commit that skips the hooks, another host.

# Git refuses paths while it concludes a merge or a cherry-pick, and commits from the shared index
# itself as it continues a revert or rewords in a rebase. `-a` takes every changed file there too.
case "${GIT_INDEX_FILE##*/}" in
    index)
        dir=$(git rev-parse --git-dir 2>/dev/null) || exit 0
        for state in MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD rebase-merge; do
            [ -e "$dir/$state" ] && exit 0
        done
        ;;
esac

cat >&2 <<'WHY'
S5: in a tree where other sessions run, the index is shared, and a commit that names no paths takes
whatever it holds. Commit with the paths named, `git commit -- <file>...`, each one this session
wrote or moved, and stage nothing ahead of it; to reword, `git commit --amend --only -m <message>`.
To conclude a merge or a cherry-pick, stage its files and commit without `-a` and without paths. A
change that named paths cannot carry - a mode, a rename of case alone, a file untracked and kept, a
part of a file - is the person's to allow.
WHY
exit 1
