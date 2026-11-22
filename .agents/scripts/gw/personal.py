# Mechanism: mechanism-shape
"""What is the person's own stays out of every file the repository speaks for: their home folder
written as a path, and each line of a list they keep in the clone's Git directory.

    python .agents/scripts/gw/personal.py --check

The home folder is read from the machine at run time and the list from `<git directory>/gw-personal`,
a file no commit can hold, one string to a line, `#` opening a comment — so nothing here, and
nothing the check reports, names anyone: a finding is a file, a line and a count. The files read
are the tracked ones and those not yet added and not ignored, since a record written this session
is the one to stop; a zip archive among them is read member by member, one inside another
included, and a finding in one is named `<archive>!<member>`. A list that is not UTF-8 text, or
UTF-16 under its byte-order mark, fails the check rather than guard nothing unseen.

The path is met as the folder's name under its parent's, whatever separates them: any run of
backslashes or slashes — one, or as many as each layer of JSON doubles it to —, their URL-encoded
forms, or the hyphen a host's own folder names put there. A name running on from, or into,
letters, digits or an underscore is not the path, and the folder's name alone is not looked for,
since a short one is an ordinary word: it goes on the list where it is wanted. Letters are
matched whatever their case, in a file of UTF-8 and in one of UTF-16 that opens with its
byte-order mark.

Exit 0 when no file holds either, 1 when one does, 2 on usage.
"""

from __future__ import annotations

import codecs
import io
import json
import re
import sys
import zipfile
from collections.abc import Callable, Iterator
from dataclasses import dataclass, field
from pathlib import Path, PurePath

sys.path.insert(0, str(Path(__file__).resolve().parent))

from docs_corpus import corpus  # noqa: E402  (path set just above)

USAGE = "usage: personal.py --check"
LIST = "gw-personal"
HOME_PATH = "holds the home folder's path"
LISTED = "holds a line of the person's list"
_ENCODED = ("%5c", "%2f")
_SEPARATOR = rf"(?:(?:[\\/]|{'|'.join(_ENCODED)})+|-)"
_UTF16 = (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)
_ZIP = b"PK"
UNREADABLE = f"the person's list, {LIST} in the Git directory, is not UTF-8 text: save it as UTF-8"


class Unreadable(Exception):
    """The person's list cannot be read as text, so what it guards is unknown."""


@dataclass(frozen=True)
class Note:
    where: str
    problem: str
    places: int

    def as_record(self) -> dict:
        return {"where": self.where, "problem": self.problem,
                "detail": f"{self.places} place{'' if self.places == 1 else 's'}"}


@dataclass
class Checked:
    files: int = 0
    listed: int = 0
    diagnostics: list[Note] = field(default_factory=list)

    def as_record(self) -> dict:
        return {"files": self.files, "listed": self.listed,
                "diagnostics": [note.as_record() for note in self.diagnostics]}


def check(root: Path, home: PurePath, listed: tuple[str, ...]) -> Checked:
    """Every file the repository speaks for: one note for a file holding the home path, one for a
    file holding a listed line, each at the first line that holds it, with the places counted."""
    path = _home_as_written(home)
    lines = tuple(line.casefold() for line in listed)
    checked = Checked(listed=len(listed))
    for name in corpus(root):
        checked.files += 1
        for where, data in _with_members(name, (root / name).read_bytes()):
            held = _text(data).casefold()
            for problem, places in ((HOME_PATH, _paths_in(held, path)), (LISTED, _lines_in(held, lines))):
                if places:
                    first = held.count("\n", 0, min(places)) + 1
                    checked.diagnostics.append(Note(f"{where}:{first}", problem, len(places)))
    return checked


def _with_members(name: str, data: bytes) -> Iterator[tuple[str, bytes]]:
    """A file's bytes, then each member of the zip archive it is, to any depth: what an archive
    holds is held compressed, and its own bytes show none of it."""
    yield name, data
    if not data.startswith(_ZIP) or not zipfile.is_zipfile(io.BytesIO(data)):
        return
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for member in archive.infolist():
            if not member.is_dir():
                yield from _with_members(f"{name}!{member.filename}", archive.read(member))


def listed(root: Path) -> tuple[str, ...]:
    """The person's list for this clone: the lines of its file, comments and blanks aside; none
    where the clone keeps no such file."""
    directory = _git_directory(root)
    if directory is None or not (directory / LIST).is_file():
        return ()
    data = (directory / LIST).read_bytes()
    try:
        text = data.decode("utf-16") if data.startswith(_UTF16) else data.decode("utf-8-sig")
    except UnicodeDecodeError as refused:
        raise Unreadable from refused
    lines = (line.strip() for line in text.splitlines())
    return tuple(line for line in lines if line and not line.startswith("#"))


def report(checked: Checked, out: Callable[[str], None] = print) -> int:
    out(json.dumps(checked.as_record(), indent=2, ensure_ascii=False))
    return 1 if checked.diagnostics else 0


def _home_as_written(home: PurePath) -> re.Pattern[str] | None:
    """The home folder under its parent's name, by any separator a record writes a path with,
    neither name running on into a longer word; a home with no named folder above it gives none,
    its own name being a word like any other."""
    if not home.name or not home.parent.name:
        return None
    above, name = (re.escape(part.casefold()) for part in (home.parent.name, home.name))
    return re.compile(rf"{above}{_SEPARATOR}{name}(?!\w)")


def _paths_in(held: str, path: re.Pattern[str] | None) -> list[int]:
    """Where the home path stands. What precedes it is read here and not by the pattern, which
    then opens on plain letters and is sought at a file's speed."""
    if path is None:
        return []
    return [met.start() for met in path.finditer(held) if not _runs_on_from_a_word(held, met.start())]


def _runs_on_from_a_word(held: str, at: int) -> bool:
    """Whether the letters at `at` continue a word begun before them; a URL-encoded separator
    ends in a letter or a digit and begins none."""
    if at == 0 or held[at - 3:at] in _ENCODED:
        return False
    return held[at - 1].isalnum() or held[at - 1] == "_"


def _lines_in(held: str, lines: tuple[str, ...]) -> list[int]:
    places: list[int] = []
    for line in lines:
        at = held.find(line)
        while at != -1:
            places.append(at)
            at = held.find(line, at + len(line))
    return places


def _text(data: bytes) -> str:
    """A file's bytes as text: UTF-16 where its byte-order mark says so, UTF-8 otherwise with its
    mark dropped, and a byte that is neither kept as a stand-in rather than refused."""
    if data.startswith(_UTF16):
        return data.decode("utf-16", errors="replace")
    return data.decode("utf-8-sig", errors="replace")


def _git_directory(root: Path) -> Path | None:
    """The clone's Git directory, read from the tree and by no process: `.git` itself, or for a
    linked worktree the directory its own names as common to the clone."""
    dot_git = root / ".git"
    if dot_git.is_dir():
        return dot_git
    if not dot_git.is_file():
        return None
    pointer = dot_git.read_text(encoding="utf-8").strip()
    if not pointer.startswith("gitdir:"):
        return None
    own = (root / pointer.removeprefix("gitdir:").strip()).resolve()
    common = own / "commondir"
    return (own / common.read_text(encoding="utf-8").strip()).resolve() if common.is_file() else own


def main(argv: list[str], root: Path, home: PurePath, out: Callable[[str], None] = print) -> int:
    if argv != ["--check"]:
        out(USAGE)
        return 2
    try:
        kept = listed(root)
    except Unreadable:
        out(UNREADABLE)
        return 1
    return report(check(root, home, kept), out)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3], Path.home()))
