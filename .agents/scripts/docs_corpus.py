"""What the repository's records are, and where their citations point.

The maintenance scripts share one view of the tree: every file Git speaks for, and the markdown
citation grammar those files are written in. Both take an explicit repository root, so a synthetic
corpus in a temporary directory runs through the exact code the live tree runs through.
"""

from __future__ import annotations

import posixpath
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable
from urllib.parse import quote, unquote

_INLINE = re.compile(r'(!?\[[^\]]*\]\(\s*)(<[^>]*>|[^)\s]+)((?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?\s*\))', re.S)
_DEFINITION = re.compile(r'(^[ ]{0,3}\[[^\]]+\]:[ \t]*)(<[^>]*>|\S+)((?:[ \t]+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?[ \t]*$)', re.M)
_BINDING = re.compile(r'(<straw-dog\b[^<>]*?\bticket\s*=\s*")([^"]*)(")', re.S)
# The installed block's tag, shared with the injector that writes it and the listing that skips it.
INSTALLED_OPENING = re.compile(r'<installed by="([^"]+)">')
INSTALLED_CLOSING = "</installed>"
_FENCE = re.compile(r"^\s*(```|~~~)")
_CODE_SPAN = re.compile(r"`[^`]*`")
_ELSEWHERE = re.compile(r"^(?:https?|mailto|ftps?|tel|data|news|irc):|^//|^#")
_DRIVE = re.compile(r"^[A-Za-z]:/")


@dataclass(frozen=True)
class Target:
    """Where one citation points, in the pieces a record move can change.

    `path` is decoded and slash-separated so two spellings of the same file compare equal; `scheme`,
    `separator` and `encoded` remember how the citation was written, so re-aiming it changes the
    destination and nothing else about its form.
    """

    scheme: str
    path: str
    fragment: str
    separator: str
    encoded: bool
    elsewhere: bool

    @property
    def absolute(self) -> bool:
        return bool(_DRIVE.match(self.path)) or self.path.startswith("/")

    def aimed_at(self, path: str) -> str:
        """The same citation, written the same way, pointing at `path`."""
        written = path.replace("/", self.separator)
        if self.encoded:
            written = quote(written, safe="/\\:")
        return self.scheme + written + self.fragment


def target_of(written: str) -> Target:
    """Read a citation's written destination. A `file:` URI is local; an `https:` one is elsewhere."""
    path, marker, anchor = written.partition("#")
    fragment = marker + anchor
    if _ELSEWHERE.match(written):
        return Target("", path, fragment, "/", False, elsewhere=True)
    scheme = ""
    if path[:5].lower() == "file:":
        body = path[5:]
        slashes = len(body) - len(body.lstrip("/"))
        # `file:///D:/…` and `file:///docs/…` differ only in what follows the slashes; keep them
        # verbatim in the scheme so the rebuilt URI is byte-identical outside the path.
        keep = slashes if _DRIVE.match(body[slashes:]) else max(slashes - 1, 0)
        scheme, path = "file:" + body[:keep], body[keep:]
    separator = "\\" if "\\" in path and "/" not in path else "/"
    encoded = "%" in path
    if encoded:
        path = unquote(path)
    return Target(scheme, path.replace("\\", "/"), fragment, separator, encoded, elsewhere=False)


def cited_record(root: Path, citing: str, target: Target) -> str | None:
    """The root-relative record a citation names, or `None` when it points outside this repository.

    An absolute path or a `file:` URI to a record in this tree is the same citation as a relative
    one — syntax alone cannot excuse it from a move.
    """
    if target.elsewhere or not target.path:
        return None
    if not target.absolute:
        return posixpath.normpath(posixpath.join(posixpath.dirname(citing), target.path))
    try:
        inside = Path(target.path).resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return None
    return inside.as_posix()


def corpus(root: Path) -> list[str]:
    """Every file the repository speaks for: tracked plus untracked-but-unignored, exact case.

    Exact-case names come from Git so case drift a Windows working tree hides stays visible, and
    untracked files are included so a record minted this session resolves before `git add`.
    """
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=root,
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    seen: dict[str, None] = {}
    for name in listing.stdout.split("\0"):
        if name and (root / name).is_file():
            seen.setdefault(name, None)
    return list(seen)


def with_citations_retargeted(text: str, retarget) -> str:
    """Every prose citation re-aimed by `retarget`; a `None` answer leaves that citation alone.

    Fenced blocks and inline code are illustrations of the syntax, not promises about a file, so
    they are never rewritten.
    """
    return _outside_code(text, lambda prose: _prose_retargeted(prose, retarget))


def with_owner_bindings_retargeted(text: str, retarget) -> str:
    """Every operative `<straw-dog ticket="…">` binding re-aimed by `retarget`.

    A binding is a root-relative path to the ticket whose work retires the straw dog, so it follows
    that ticket into `done/` exactly as a link would. `retarget` is given and returns a root-relative
    name; an illustration of the syntax binds nothing and is left alone.
    """
    return _outside_code(text, lambda prose: _prose_bindings_retargeted(prose, retarget))


def _outside_code(text: str, rewrite: Callable[[str], str]) -> str:
    """Apply `rewrite` to the document's prose, passing fenced blocks through untouched."""
    rewritten: list[str] = []
    prose: list[str] = []
    inside_fence = False
    for line in text.splitlines(keepends=True):
        if _FENCE.match(line):
            rewritten.append(rewrite("".join(prose)))
            prose.clear()
            rewritten.append(line)
            inside_fence = not inside_fence
        elif inside_fence:
            rewritten.append(line)
        else:
            prose.append(line)
    rewritten.append(rewrite("".join(prose)))
    return "".join(rewritten)


def _prose_bindings_retargeted(text: str, retarget) -> str:
    code_spans = [span.span() for span in _CODE_SPAN.finditer(text)]

    def rewritten(match: re.Match[str]) -> str:
        if any(start <= match.start(2) < end for start, end in code_spans):
            return match.group(0)
        final = retarget(match.group(2))
        return match.group(0) if final is None else match.group(1) + final + match.group(3)

    return _BINDING.sub(rewritten, text)


def citations(text: str) -> list[str]:
    """Every destination this module recognises as a citation, in document order.

    Reads through the one grammar `with_citations_retargeted` rewrites, so nothing can be checked
    that would not also have been repaired.
    """
    found: list[str] = []

    def collect(target: str) -> None:
        found.append(target)
        return None

    with_citations_retargeted(text, collect)
    return found


def without_code(text: str) -> str:
    """The same text, character for character, with every code span and fenced block blanked out.

    Positions are preserved so a search over the result still points at the real line, and an
    illustration of a path can never be mistaken for a claim about a file.
    """
    kept: list[str] = []
    inside_fence = False
    for line in text.splitlines(keepends=True):
        if _FENCE.match(line):
            inside_fence = not inside_fence
            kept.append(_blanked(line))
        elif inside_fence:
            kept.append(_blanked(line))
        else:
            kept.append(_CODE_SPAN.sub(lambda span: _blanked(span.group(0)), line))
    return "".join(kept)


def _blanked(text: str) -> str:
    return "".join(character if character in "\r\n" else " " for character in text)


def _prose_retargeted(text: str, retarget) -> str:
    """Both citation forms that name a file: the inline link and the reference definition."""
    code_spans = [span.span() for span in _CODE_SPAN.finditer(text)]

    def rewritten(match: re.Match[str]) -> str:
        if any(start <= match.start(2) < end for start, end in code_spans):
            return match.group(0)
        bracketed = match.group(2).startswith("<") and match.group(2).endswith(">")
        target = match.group(2)[1:-1] if bracketed else match.group(2)
        final = retarget(target)
        if final is None:
            return match.group(0)
        return match.group(1) + (f"<{final}>" if bracketed else final) + match.group(3)

    return _DEFINITION.sub(rewritten, _INLINE.sub(rewritten, text))
