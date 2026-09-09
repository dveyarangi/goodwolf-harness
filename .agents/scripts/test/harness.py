"""A disposable repository the maintenance scripts can be exercised against.

The scripts discover their corpus through Git and resolve paths against an explicit root, so
every behavioral test builds a real (tiny) repository in `tmp` rather than reaching into this
one. Nothing here may be imported by runtime code.
"""

from __future__ import annotations

import atexit
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

_TEMPLATE: Path | None = None


def _template() -> Path:
    """The `.git` every case is stamped from, built once per process.

    `git init` and its two identity settings are three process spawns — some 320ms on Windows —
    and every case paid them, which was most of the suite's wall clock. Copying this directory
    gives the same repository for a twenty-fifth of that. Git builds it, with an empty init
    template so no sample hook joins the copy, so a case still receives a real repository rather
    than a hand-rolled imitation of one.
    """
    global _TEMPLATE
    if _TEMPLATE is None:
        workspace = tempfile.TemporaryDirectory()
        atexit.register(workspace.cleanup)
        no_hooks = Path(workspace.name) / "no-hooks"
        no_hooks.mkdir()
        seed = Path(workspace.name) / "seed"
        subprocess.run(
            ["git", "init", "--initial-branch", "main", "--template", str(no_hooks), str(seed)],
            capture_output=True,
            encoding="utf-8",
            check=True,
        )
        with (seed / ".git" / "config").open("a", encoding="utf-8") as handle:
            handle.write("[user]\n\temail = harness@example.invalid\n\tname = Harness\n")
        _TEMPLATE = seed / ".git"
    return _TEMPLATE


class RepositoryCase(unittest.TestCase):
    """A test whose subject is a freshly initialised repository at `self.root`."""

    def setUp(self) -> None:
        self._workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self._workspace.cleanup)
        self.root = Path(self._workspace.name).resolve()
        shutil.copytree(_template(), self.root / ".git")

    def git(self, *arguments: str) -> str:
        done = subprocess.run(
            ["git", *arguments], cwd=self.root, capture_output=True, encoding="utf-8", check=True
        )
        return done.stdout

    def write(self, name: str, text: str) -> Path:
        """Place a record at a root-relative name, byte-exact — no newline translation."""
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        return path

    def read(self, name: str) -> str:
        with (self.root / name).open(encoding="utf-8", newline="") as handle:
            return handle.read()

    def commit(self, message: str = "records") -> None:
        self.git("add", "-A")
        self.git("commit", "-m", message)

    def snapshot(self) -> dict[str, bytes]:
        """Every working-tree byte plus the index, so a refusal can be shown to change nothing."""
        files = {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in sorted(self.root.rglob("*"))
            if path.is_file() and ".git" not in path.relative_to(self.root).parts
        }
        return {**files, "<index>": self.git("ls-files", "--stage").encode()}
