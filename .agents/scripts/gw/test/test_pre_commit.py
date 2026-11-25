# Mechanism: session
"""A commit that names no paths is stopped by Git itself (S5), through real commits."""

from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path

from repository import RepositoryCase

SCRIPT = Path(__file__).resolve().parent.parent / "pre_commit.sh"
# What a clone's hook holds: a commit that passes is let by here, where it starts nothing, and any
# other is the tracked script's, called from the work tree's top, where Git runs the hook.
HOOK = (
    "#!/bin/sh\n"
    'case "${GIT_INDEX_FILE##*/}" in index | index.lock) ;; *) exit 0 ;; esac\n'
    '[ "$CLAUDE_CODE_CHILD_SESSION" = 1 ] && [ -f .agents/scripts/gw/pre_commit.sh ] || exit 0\n'
    "exec sh .agents/scripts/gw/pre_commit.sh\n"
)
MARKS = ("CLAUDECODE", "CLAUDE_CODE_CHILD_SESSION")


class Committing(RepositoryCase):
    """Two files are staged before each commit, one of them another session's."""

    proves_a_process = True

    def setUp(self) -> None:
        super().setUp()
        self.write("mine.md", "0\n")
        self.write("theirs.md", "0\n")
        self.write("docs/one.md", "0\n")
        self.commit("first")
        # Read as the clone has it: the file is absent until the script is written.
        self.write(".agents/scripts/gw/pre_commit.sh", SCRIPT.read_text(encoding="utf-8") if SCRIPT.is_file() else "")
        hook = self.root / ".git" / "hooks" / "pre-commit"
        hook.parent.mkdir(exist_ok=True)
        hook.write_text(HOOK, encoding="utf-8", newline="\n")
        os.chmod(hook, 0o755)
        self.drafts = 0

    def stage(self) -> None:
        self.drafts += 1
        for name in ("mine.md", "theirs.md"):
            self.write(name, f"{self.drafts}\n")
        self.git("add", "mine.md", "theirs.md")

    def asked(self, *arguments: str, agent: bool = True, **more: str) -> subprocess.CompletedProcess:
        environment = {name: value for name, value in os.environ.items() if name not in MARKS}
        if agent:
            environment.update(dict.fromkeys(MARKS, "1"))
        return subprocess.run(["git", *arguments], cwd=self.root, env={**environment, **more}, capture_output=True, encoding="utf-8")

    def took(self) -> list[str]:
        return self.git("show", "--name-only", "--format=", "HEAD").split()

    def assertStopped(self, *arguments: str) -> None:
        self.stage()
        before = self.git("rev-parse", "HEAD")
        done = self.asked(*arguments)
        self.assertNotEqual(0, done.returncode, arguments)
        self.assertIn("git commit -- <file>", done.stderr)
        self.assertEqual(before, self.git("rev-parse", "HEAD"))

    def assertTakes(self, files: list[str], *arguments: str, agent: bool = True, **more: str) -> None:
        self.stage()
        done = self.asked(*arguments, agent=agent, **more)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(files, self.took())


class ACommitInTheClone(Committing):
    """What passes and what is stopped, outside any operation of Git's own."""

    def test_an_agents_commit_naming_no_paths_is_stopped_and_told_why(self) -> None:
        for arguments in (
            ("commit", "-qm", "x"),
            ("commit", "-qam", "x"),
            ("commit", "-q", "--amend", "--no-edit"),
            ("commit", "-qm", "x", "-i", "--", "mine.md"),
            ("-c", "core.quotepath=off", "commit", "-qm", "git commit -- mine.md"),
        ):
            with self.subTest(arguments=arguments):
                self.assertStopped(*arguments)

    def test_a_commit_naming_its_paths_takes_them_alone(self) -> None:
        for arguments in (("-qm", "x", "--", "mine.md"), ("-qm", "x", "mine.md"), ("-qm", "it's; (so) `x`\n-- #", "--only", "mine.md")):
            with self.subTest(arguments=arguments):
                self.assertTakes(["mine.md"], "commit", *arguments)

    def test_rewording_the_last_commit_takes_nothing_of_the_index(self) -> None:
        self.assertTakes(["docs/one.md", "mine.md", "theirs.md"], "commit", "-q", "--amend", "--only", "-m", "reworded")

    def test_a_persons_own_commit_is_not_stopped(self) -> None:
        self.assertTakes(["mine.md", "theirs.md"], "commit", "-qm", "x", agent=False)

    def test_an_editors_terminal_that_carries_one_mark_of_the_two_is_a_persons(self) -> None:
        self.assertTakes(["mine.md", "theirs.md"], "commit", "-qm", "x", agent=False, CLAUDECODE="1")

    def test_a_tree_with_no_script_stops_nothing(self) -> None:
        (self.root / ".agents/scripts/gw/pre_commit.sh").unlink()

        self.assertTakes(["mine.md", "theirs.md"], "commit", "-qm", "x")

    def test_a_broken_script_stops_no_commit_that_names_its_paths_nor_a_persons(self) -> None:
        self.write(".agents/scripts/gw/pre_commit.sh", "<<<<<<< ours\n=======\n>>>>>>> theirs\n")

        self.assertTakes(["mine.md"], "commit", "-qm", "x", "--", "mine.md")
        self.assertTakes(["mine.md", "theirs.md"], "commit", "-qm", "x", agent=False)

    def test_a_commit_from_an_index_of_the_callers_own_is_not_stopped(self) -> None:
        own = str(self.root / ".git" / "own-index")
        self.git("read-tree", f"--index-output={own}", "HEAD")
        self.write("docs/one.md", "1\n")
        self.assertEqual(0, self.asked("add", "docs/one.md", GIT_INDEX_FILE=own).returncode)

        self.assertTakes(["docs/one.md"], "commit", "-qm", "x", GIT_INDEX_FILE=own)

    def test_in_a_linked_worktree_the_same_holds(self) -> None:
        tree = self.another_repository()
        self.git("add", ".agents")
        self.git("commit", "-qm", "the script", "--no-verify", "--", ".agents")
        self.git("worktree", "add", "-q", str(tree / "wt"), "-b", "w")
        top = tree / "wt"
        for named, want in ((("-qm", "x"), False), (("-qm", "x", "--", "mine.md"), True)):
            (top / "mine.md").write_text(f"{named}\n", encoding="utf-8")
            subprocess.run(["git", "add", "mine.md"], cwd=top, check=True)
            done = subprocess.run(["git", "commit", *named], cwd=top, capture_output=True, encoding="utf-8",
                                  env={**os.environ, **dict.fromkeys(MARKS, "1")})
            self.assertEqual(want, done.returncode == 0, done.stderr)


class ACommitGitLetsNameNoPaths(Committing):
    """Git refuses paths while it concludes a merge or a cherry-pick, and commits without them itself
    as it continues a revert or a rebase, so a commit there passes; `-a` takes every file and does not."""

    def conflict(self) -> None:
        self.git("checkout", "-qb", "side")
        self.write("docs/one.md", "side\n")
        self.git("commit", "-qm", "side", "--no-verify", "--", "docs/one.md")
        self.git("checkout", "-q", "main")
        self.write("docs/one.md", "main\n")
        self.git("commit", "-qm", "main", "--no-verify", "--", "docs/one.md")

    def concluded(self, *started: str) -> None:
        self.conflict()
        begun = self.asked(*started)
        self.assertNotEqual(0, begun.returncode, "a conflict was expected")
        self.write("docs/one.md", "both\n")
        self.git("add", "docs/one.md")

        done = self.asked("commit", "-qm", "concluded")

        self.assertEqual(0, done.returncode, done.stderr)

    def test_a_merge_is_concluded(self) -> None:
        self.concluded("merge", "-q", "side")

    def test_a_merge_concluded_with_every_changed_file_is_stopped(self) -> None:
        self.conflict()
        self.asked("merge", "-q", "side")
        self.write("docs/one.md", "both\n")
        self.git("add", "docs/one.md")

        self.assertStopped("commit", "-qam", "x")
        self.assertIn("without `-a`", self.asked("commit", "-qam", "x").stderr)

    def test_a_merge_in_a_linked_worktree_is_concluded_there_and_opens_nothing_here(self) -> None:
        self.conflict()
        tree = self.another_repository() / "wt"
        self.git("worktree", "add", "-q", str(tree), "-b", "w")
        marked = {**os.environ, **dict.fromkeys(MARKS, "1")}
        subprocess.run(["git", "merge", "-q", "side"], cwd=tree, env=marked, capture_output=True)
        self.assertStopped("commit", "-qm", "x")
        (tree / ".agents/scripts/gw").mkdir(parents=True, exist_ok=True)
        (tree / ".agents/scripts/gw/pre_commit.sh").write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
        (tree / "docs/one.md").write_text("both\n", encoding="utf-8")
        subprocess.run(["git", "add", "docs/one.md"], cwd=tree, check=True)

        done = subprocess.run(["git", "commit", "-qm", "m"], cwd=tree, env=marked, capture_output=True, encoding="utf-8")

        self.assertEqual(0, done.returncode, done.stderr)

    def test_a_rebase_and_a_revert_are_continued_by_git(self) -> None:
        for apply in ("--merge", "--apply"):
            with self.subTest(backend=apply):
                self.git("checkout", "-q", "main")
                self.git("branch", "-qD", "side") if "side" in self.git("branch", "--list", "side") else None
                self.conflict()
                self.assertNotEqual(0, self.asked("rebase", "-q", apply, "side").returncode, "a conflict was expected")
                self.write("docs/one.md", f"both {apply}\n")
                self.git("add", "docs/one.md")

                done = self.asked("-c", "core.editor=true", "rebase", "--continue")

                self.assertEqual(0, done.returncode, done.stderr)

    def test_a_rebase_of_the_apply_kind_opens_nothing(self) -> None:
        self.conflict()
        self.assertNotEqual(0, self.asked("rebase", "-q", "--apply", "side").returncode, "a conflict was expected")
        self.write("docs/one.md", "both\n")
        self.git("add", "docs/one.md")

        self.assertStopped("commit", "-qm", "x")

    def test_a_cherry_pick_is_concluded(self) -> None:
        self.concluded("cherry-pick", "side")

    def test_a_revert_is_concluded(self) -> None:
        self.conflict()
        self.write("docs/one.md", "later\n")
        self.git("commit", "-qm", "later", "--no-verify", "--", "docs/one.md")
        begun = self.asked("revert", "--no-edit", "HEAD~1")
        self.assertNotEqual(0, begun.returncode, "a conflict was expected")
        self.write("docs/one.md", "taken back\n")
        self.git("add", "docs/one.md")

        done = self.asked("commit", "-qm", "concluded")

        self.assertEqual(0, done.returncode, done.stderr)

    def test_a_rebase_is_continued(self) -> None:
        self.conflict()
        begun = self.asked("rebase", "-q", "--merge", "side")
        self.assertNotEqual(0, begun.returncode, "a conflict was expected")
        self.write("docs/one.md", "both\n")
        self.git("add", "docs/one.md")

        done = self.asked("commit", "-qm", "concluded")

        self.assertEqual(0, done.returncode, done.stderr)


if __name__ == "__main__":
    unittest.main()
