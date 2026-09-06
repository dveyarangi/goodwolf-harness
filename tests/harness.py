"""A disposable repository the maintenance scripts can be exercised against.

The scripts discover their corpus through Git and resolve paths against an explicit root, so
every behavioral test builds a real (tiny) repository in `tmp` rather than reaching into this
one. Nothing here may be imported by runtime code.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / ".agents" / "scripts"))


class RepositoryCase(unittest.TestCase):
    """A test whose subject is a freshly initialised repository at `self.root`."""

    def setUp(self) -> None:
        self._workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self._workspace.cleanup)
        self.root = Path(self._workspace.name).resolve()
        self.git("init", "--initial-branch", "main")
        self.git("config", "user.email", "harness@example.invalid")
        self.git("config", "user.name", "Harness")

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
