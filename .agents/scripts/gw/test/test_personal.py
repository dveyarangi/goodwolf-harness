# Mechanism: mechanism-shape
"""No file the repository speaks for holding the person's home folder written as a path, or a
line of the list the person keeps in the clone's Git directory."""

from __future__ import annotations

import io
import json
import unittest
import zipfile
from pathlib import Path, PurePosixPath, PureWindowsPath

from repository import RepositoryCase, proves_a_process

import personal

HOME = PureWindowsPath(r"C:\Users\somebody")
ADDRESS = "somebody@example.com"


class Personal(RepositoryCase):
    def problems(self, home=HOME, listed: tuple[str, ...] = ()) -> list[tuple[str, str]]:
        return [(note.where, note.problem) for note in personal.check(self.root, home, listed).diagnostics]

    def test_a_tree_holding_neither_raises_nothing(self) -> None:
        self.write("docs/record.md", "A record of what happened, under C:\\Users\\owner\\work.\n")
        self.assertEqual(self.problems(listed=(ADDRESS,)), [])

    def test_the_home_folder_as_a_path_is_refused_at_its_file_and_line(self) -> None:
        self.write("docs/record.md", "first\nSource: C:\\Users\\somebody\\.claude\\x.jsonl\n")
        self.assertEqual(self.problems(), [("docs/record.md:2", personal.HOME_PATH)])

    def test_the_path_is_met_however_its_separators_are_written(self) -> None:
        forms = {
            "json.json": '{"cwd": "C:' + "\\" * 2 + "Users" + "\\" * 2 + 'somebody"}\n',
            "json-in-json.json": "C:" + "\\" * 4 + "Users" + "\\" * 4 + "somebody\n",
            "json-thrice.json": "C:" + "\\" * 8 + "Users" + "\\" * 8 + "somebody\n",
            "posix.md": "under /c/Users/somebody/work\n",
            "forward.md": "under C:/Users/somebody/work\n",
            "folder.md": "the folder C--Users-somebody-work\n",
            "cased.md": "under c:\\users\\SOMEBODY\\work\n",
            "url-backslash.md": "file:///C:%5CUsers%5Csomebody\n",
            "url-slash.md": "C%3A%2FUsers%2Fsomebody\n",
            "ending.md": "it ends at C:\\Users\\somebody",
            "opening.md": "Users/somebody opens the file, which ends on a word",
            "utf-16-be.txt": "\ufeffC:\\Users\\somebody\n".encode("utf-16-be"),
        }
        for name, text in forms.items():
            (self.root / name).write_bytes(text if isinstance(text, bytes) else text.encode())
        self.assertEqual(sorted(where for where, _ in self.problems()), sorted(f"{name}:1" for name in forms))

    def test_either_name_inside_a_longer_word_is_not_the_path(self) -> None:
        self.write(
            "docs/record.md",
            "superusers/somebody, end_users/somebody, 9users/somebody, Users/somebodyelse, Users/somebody2, "
            "Users/somebody_2 and Users somebody.\n",
        )
        self.assertEqual(self.problems(), [])
        self.write("docs/record.md", "home-alone, /home/alice and the github-homepage\n")
        self.assertEqual(self.problems(home=PurePosixPath("/home/al")), [])
        self.assertEqual(self.problems(home=PurePosixPath("/github/home")), [])

    def test_a_name_is_met_as_its_letters_and_not_as_a_pattern(self) -> None:
        self.write("docs/record.md", "under /home/firstxlast/work\n")
        self.assertEqual(self.problems(home=PurePosixPath("/home/first.last")), [])

    def test_the_folders_name_alone_is_not_the_path(self) -> None:
        self.write("docs/record.md", "somebody wrote this, and Users read it.\n")
        self.assertEqual(self.problems(), [])

    def test_a_home_elsewhere_is_read_the_same_way(self) -> None:
        self.write("docs/record.md", "under /home/somebody/work\n")
        self.assertEqual(self.problems(home=PurePosixPath("/home/somebody")), [("docs/record.md:1", personal.HOME_PATH)])

    def test_a_home_with_no_folder_above_it_is_not_looked_for(self) -> None:
        self.write("docs/record.md", "the root of it, /root, and a root cause.\n")
        self.assertEqual(self.problems(home=PurePosixPath("/root")), [])

    def test_a_home_named_in_another_script_is_met_as_the_machine_writes_it(self) -> None:
        self.write("docs/record.md", "under C:\\Users\\Жанна\\work\n")
        self.assertEqual(self.problems(home=PureWindowsPath("C:\\Users\\Жанна")), [("docs/record.md:1", personal.HOME_PATH)])

    def test_a_line_of_the_list_is_refused_whatever_its_case(self) -> None:
        self.write("docs/record.md", "one\ntwo\nwritten to Somebody@Example.com that day\n")
        self.assertEqual(self.problems(listed=(ADDRESS,)), [("docs/record.md:3", personal.LISTED)])

    def test_a_listed_name_in_another_script_is_refused_as_written_and_in_any_case(self) -> None:
        self.write("as-listed.md", "signed Жанна Иванова\n")
        self.write("lowered.md", "signed жанна иванова\n")
        self.write("raised.md", "signed ЖАННА ИВАНОВА\n")
        self.write("its-letters-elsewhere.md", "Жанр, Иван, новая анна и Жанна с Ивановой\n")
        self.assertEqual(
            self.problems(listed=("Жанна Иванова",)),
            [(f"{name}:1", personal.LISTED) for name in ("as-listed.md", "lowered.md", "raised.md")],
        )

    def test_a_file_of_utf_16_is_read_as_its_text(self) -> None:
        (self.root / "redirected.txt").write_bytes("first\nC:\\Users\\somebody and Somebody@example.com\n".encode("utf-16"))
        self.assertEqual(
            self.problems(listed=(ADDRESS,)),
            [("redirected.txt:2", personal.HOME_PATH), ("redirected.txt:2", personal.LISTED)],
        )

    def test_a_file_of_utf_16_cut_mid_character_is_read_to_where_it_is_cut(self) -> None:
        (self.root / "cut.txt").write_bytes("C:\\Users\\somebody\nand more".encode("utf-16") + b"\x00")
        self.assertEqual(self.problems(), [("cut.txt:1", personal.HOME_PATH)])

    def test_a_file_holding_both_is_named_once_for_each(self) -> None:
        self.write("docs/record.md", "C:\\Users\\somebody\nJane Somebody\n")
        self.assertEqual(
            self.problems(listed=("Jane Somebody",)),
            [("docs/record.md:1", personal.HOME_PATH), ("docs/record.md:2", personal.LISTED)],
        )

    def test_a_file_is_named_at_the_earliest_place_and_every_form_is_counted(self) -> None:
        self.write(
            "docs/record.md",
            "Jane Somebody\nC:" + "\\" * 2 + "Users" + "\\" * 2 + "somebody\nC:/Users/somebody\nC:\\Users\\somebody\n"
            + f"{ADDRESS} and {ADDRESS}\n",
        )
        notes = personal.check(self.root, HOME, (ADDRESS, "Jane Somebody")).diagnostics
        self.assertEqual(
            [(note.where, note.problem, note.places) for note in notes],
            [("docs/record.md:2", personal.HOME_PATH, 3), ("docs/record.md:1", personal.LISTED, 3)],
        )

    def test_a_report_counts_the_places_and_never_quotes_what_it_met(self) -> None:
        self.write("docs/record.md", f"{ADDRESS}\nand again {ADDRESS}, C:\\Users\\somebody\n")
        said: list[str] = []
        status = personal.report(personal.check(self.root, HOME, (ADDRESS,)), said.append)
        record = json.loads("\n".join(said))
        self.assertEqual(status, 1)
        self.assertEqual(
            [(note["where"], note["detail"]) for note in record["diagnostics"]],
            [("docs/record.md:2", "1 place"), ("docs/record.md:1", "2 places")],
        )
        self.assertNotIn("somebody", "\n".join(said).lower())

    def test_a_clean_tree_reports_what_it_read_and_passes(self) -> None:
        self.write("docs/record.md", "nothing of the person's\n")
        said: list[str] = []
        status = personal.report(personal.check(self.root, HOME, (ADDRESS,)), said.append)
        self.assertEqual(status, 0)
        self.assertEqual(json.loads("\n".join(said)), {"files": 1, "listed": 1, "diagnostics": []})

    def test_a_file_that_is_not_text_is_read_all_the_same(self) -> None:
        (self.root / "image.bin").write_bytes(b"\x00\xff\xfaC:\\Users\\somebody\x00")
        self.assertEqual(self.problems(), [("image.bin:1", personal.HOME_PATH)])

    def test_an_archive_is_read_member_by_member_and_one_inside_another(self) -> None:
        def archive(members: dict[str, bytes]) -> bytes:
            packed = io.BytesIO()
            with zipfile.ZipFile(packed, "w", zipfile.ZIP_DEFLATED) as written:
                for name, data in members.items():
                    written.writestr(name, data)
            return packed.getvalue()

        inner = archive({"deep.txt": f"one\ntwo\n{ADDRESS}\n".encode()})
        (self.root / "raw.zip").write_bytes(archive({
            "clean.txt": b"nothing of the person's\n",
            "logs/run.json": b'first\n{"cwd": "C:\\\\Users\\\\somebody"}\n',
            "inner.zip": inner,
        }))
        self.assertEqual(
            self.problems(listed=(ADDRESS,)),
            [("raw.zip!logs/run.json:2", personal.HOME_PATH), ("raw.zip!inner.zip!deep.txt:3", personal.LISTED)],
        )

    def test_a_file_that_only_opens_like_an_archive_is_read_as_it_is(self) -> None:
        (self.root / "notes.txt").write_bytes(b"PK is how it opens, under C:\\Users\\somebody\n")
        self.assertEqual(self.problems(), [("notes.txt:1", personal.HOME_PATH)])

    @proves_a_process
    def test_a_file_not_yet_added_is_read_and_an_ignored_one_is_not(self) -> None:
        self.write(".gitignore", "scratch/\n")
        self.write("tracked.md", "C:\\Users\\somebody\n")
        self.commit()
        self.write("written-this-session.md", "C:\\Users\\somebody\n")
        self.write("scratch/notes.md", "C:\\Users\\somebody\n")
        self.assertEqual(
            sorted(self.problems()),
            [("tracked.md:1", personal.HOME_PATH), ("written-this-session.md:1", personal.HOME_PATH)],
        )


class TheList(RepositoryCase):
    def keep(self, data: bytes, directory: Path | None = None) -> None:
        directory = directory or self.root / ".git"
        directory.mkdir(parents=True, exist_ok=True)
        (directory / personal.LIST).write_bytes(data)

    def test_the_list_is_the_lines_of_a_file_in_the_git_directory(self) -> None:
        self.keep(f"# what stays out of every commit\n\n{ADDRESS}\n  # set aside\n  Jane Somebody  \n".encode())
        self.assertEqual(personal.listed(self.root), (ADDRESS, "Jane Somebody"))

    def test_a_list_saved_with_a_byte_order_mark_keeps_its_first_line(self) -> None:
        self.keep(b"\xef\xbb\xbf" + f"{ADDRESS}\nJane Somebody\n".encode())
        self.assertEqual(personal.listed(self.root), (ADDRESS, "Jane Somebody"))

    def test_a_list_a_shell_wrote_as_utf_16_is_read(self) -> None:
        self.keep(f"{ADDRESS}\r\nЖанна Иванова\r\n".encode("utf-16"))
        self.assertEqual(personal.listed(self.root), (ADDRESS, "Жанна Иванова"))

    def test_a_list_that_is_not_text_is_refused_and_not_read_as_noise(self) -> None:
        self.keep("Жанна Иванова\n".encode("cp1251"))
        with self.assertRaises(personal.Unreadable):
            personal.listed(self.root)
        self.write("docs/record.md", "nothing of the person's\n")
        said: list[str] = []
        self.assertEqual(personal.main(["--check"], self.root, HOME, said.append), 1)
        self.assertEqual(said, [personal.UNREADABLE])

    def test_a_clone_with_no_list_has_an_empty_one(self) -> None:
        (self.root / ".git").mkdir()
        self.assertEqual(personal.listed(self.root), ())

    def test_a_tree_with_no_git_directory_has_an_empty_one(self) -> None:
        self.assertEqual(personal.listed(self.root), ())

    def test_a_linked_worktree_reads_the_list_of_the_clone_it_belongs_to(self) -> None:
        clone = self.another_repository()
        own = clone / ".git" / "worktrees" / "side"
        own.mkdir(parents=True)
        (own / "commondir").write_text("../..\n", encoding="utf-8")
        self.keep(f"{ADDRESS}\n".encode(), clone / ".git")
        (self.root / ".git").write_text(f"gitdir: {own.as_posix()}\n", encoding="utf-8")
        self.assertEqual(personal.listed(self.root), (ADDRESS,))

    def test_a_git_directory_kept_elsewhere_and_common_to_nothing_holds_its_own_list(self) -> None:
        elsewhere = self.another_repository() / "kept"
        self.keep(f"{ADDRESS}\n".encode(), elsewhere)
        (self.root / ".git").write_text(f"gitdir: {elsewhere.as_posix()}\n", encoding="utf-8")
        self.assertEqual(personal.listed(self.root), (ADDRESS,))


class WhatIsRead(RepositoryCase):
    """Git says what the upstream holds, so each case here is a real repository."""

    proves_a_process = True

    def publish(self) -> None:
        remote = self.another_repository() / "remote.git"
        self.git("init", "--bare", str(remote))
        self.git("remote", "add", "origin", str(remote))
        self.git("push", "--set-upstream", "origin", "HEAD")

    def run_check(self, *more: str) -> tuple[int, list[str]]:
        said: list[str] = []
        status = personal.main(["--check", *more], self.root, HOME, said.append)
        return status, [note["where"] for note in json.loads("\n".join(said))["diagnostics"]]

    def test_a_branch_with_no_upstream_is_read_whole(self) -> None:
        self.write("committed.md", "C:\\Users\\somebody\n")
        self.commit()
        self.assertIsNone(personal.unpublished(self.root))
        self.assertEqual(self.run_check(), (1, ["committed.md:1"]))

    def test_what_the_upstream_holds_is_not_read_again_and_all_reads_it(self) -> None:
        self.write("published.md", "C:\\Users\\somebody\n")
        self.commit()
        self.publish()
        self.assertEqual(personal.unpublished(self.root), [])
        self.assertEqual(self.run_check(), (0, []))
        self.assertEqual(self.run_check("--all"), (1, ["published.md:1"]))

    def test_what_a_commit_could_newly_publish_is_read(self) -> None:
        self.write(".gitignore", "scratch/\n")
        self.write("published.md", "C:\\Users\\somebody\n")
        self.write("changed.md", "nothing of the person's\n")
        self.write("removed.md", "nothing of the person's\n")
        self.commit()
        self.publish()
        self.write("committed.md", "C:\\Users\\somebody\n")
        self.commit("not pushed")
        self.write("changed.md", "now under C:\\Users\\somebody\n")
        self.write("written-this-session.md", "C:\\Users\\somebody\n")
        self.write("scratch/notes.md", "C:\\Users\\somebody\n")
        (self.root / "removed.md").unlink()
        self.assertEqual(
            sorted(personal.unpublished(self.root)), ["changed.md", "committed.md", "written-this-session.md"]
        )
        status, named = self.run_check()
        self.assertEqual((status, sorted(named)), (1, ["changed.md:1", "committed.md:1", "written-this-session.md:1"]))


class Usage(RepositoryCase):
    def test_anything_but_the_check_is_shown_the_usage(self) -> None:
        for argv in ([], ["--other"], ["--all"], ["--check", "more"], ["--check", "--all", "more"]):
            said: list[str] = []
            self.assertEqual(personal.main(argv, self.root, HOME, said.append), 2)
            self.assertEqual(said, [personal.USAGE])

    @proves_a_process
    def test_the_check_reads_the_tree_with_the_home_it_is_given(self) -> None:
        self.write("docs/record.md", "under C:\\Users\\somebody\\work\n")
        self.assertEqual(personal.main(["--check"], self.root, HOME, lambda _: None), 1)

    @proves_a_process
    def test_the_check_reads_the_tree_with_the_clones_list(self) -> None:
        (self.root / ".git" / personal.LIST).write_text(f"{ADDRESS}\n", encoding="utf-8")
        self.write("docs/record.md", f"written to {ADDRESS}\n")
        said: list[str] = []
        self.assertEqual(personal.main(["--check"], self.root, HOME, said.append), 1)
        record = json.loads("\n".join(said))
        self.assertEqual((record["listed"], [note["problem"] for note in record["diagnostics"]]), (1, [personal.LISTED]))


if __name__ == "__main__":
    unittest.main()
