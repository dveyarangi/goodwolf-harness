"""Preflight: why a selection must not happen at all, and the proof that nothing moved."""

from __future__ import annotations

import subprocess

import unittest

from harness import RepositoryCase

import move_doc

TICKET = "docs/tickets/01-0010.0040-install-plan.md"
RFC = "docs/rfc/01-0010.0040-install-plan.md"
CLOSED_TICKET = "docs/tickets/done/01-0010.0040-install-plan.md"
CLOSED_RFC = "docs/rfc/done/01-0010.0040-install-plan.md"


class Refusal(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(TICKET, "# Install /plan\n")
        self.write(RFC, "# Install /plan — plan\n")
        self.write("docs/tickets/README.md", "# Queue\n\n[plan](01-0010.0040-install-plan.md)\n")
        self.commit()

    def refused_for(self, pairs: list[tuple[str, str]]) -> str:
        untouched = self.snapshot()
        why = move_doc.refusal(self.root, pairs)
        self.assertIsNotNone(why, f"expected a refusal for {pairs}")
        self.assertEqual(untouched, self.snapshot(), "a refusal must not change a single byte")
        return why

    def test_a_record_that_is_not_there_cannot_move(self) -> None:
        self.assertIn("not a record", self.refused_for([("docs/tickets/absent.md", CLOSED_TICKET)]))

    def test_only_markdown_records_move(self) -> None:
        self.write("docs/diagram.png", "not really a png")
        self.commit()
        self.assertIn("markdown", self.refused_for([("docs/diagram.png", "docs/done/diagram.png")]))

    def test_the_same_record_cannot_be_sent_to_two_homes(self) -> None:
        why = self.refused_for([(TICKET, CLOSED_TICKET), (TICKET, "docs/tickets/elsewhere.md")])
        self.assertIn("twice", why)

    def test_two_records_cannot_claim_one_home(self) -> None:
        why = self.refused_for([(TICKET, CLOSED_TICKET), (RFC, CLOSED_TICKET)])
        self.assertIn("claimed twice", why)

    def test_an_occupied_destination_is_never_overwritten(self) -> None:
        self.write(CLOSED_TICKET, "# An earlier record of the same name\n")
        self.commit()
        self.assertIn("already exists", self.refused_for([(TICKET, CLOSED_TICKET)]))

    def test_an_untracked_file_still_occupies_its_destination(self) -> None:
        self.write(CLOSED_TICKET, "# Minted this session, never staged\n")
        self.assertIn("already exists", self.refused_for([(TICKET, CLOSED_TICKET)]))

    def test_an_ignored_file_still_occupies_its_destination(self) -> None:
        self.write(".gitignore", "docs/tickets/done/\n")
        self.write(CLOSED_TICKET, "# Ignored, but really there\n")
        self.commit()
        self.assertIn("already exists", self.refused_for([(TICKET, CLOSED_TICKET)]))

    def test_a_record_cannot_move_to_where_it_already_is(self) -> None:
        self.assertIn("already there", self.refused_for([(TICKET, TICKET)]))

    def test_one_records_destination_cannot_be_another_records_home(self) -> None:
        why = self.refused_for([(TICKET, "docs/rfc/01-0010.0040-install-plan.md"), (RFC, CLOSED_RFC)])
        self.assertIn("overlap", why)

    def test_a_destination_differing_only_in_case_is_a_collision(self) -> None:
        why = self.refused_for([(TICKET, CLOSED_TICKET), (RFC, CLOSED_TICKET.upper())])
        self.assertIn("claimed twice", why)

    def test_a_destination_outside_the_repository_is_refused(self) -> None:
        why = self.refused_for([(TICKET, "../escaped/01-0010.0040-install-plan.md")])
        self.assertIn("outside the repository", why)

    def test_a_record_that_is_not_utf8_is_refused_rather_than_mangled(self) -> None:
        (self.root / "docs/tickets/binary.md").write_bytes(b"# Install \xff\xfe plan\n")
        self.commit()
        why = self.refused_for([("docs/tickets/binary.md", "docs/tickets/done/binary.md")])
        self.assertIn("not utf-8", why.lower())

    def test_an_eligible_paired_close_is_not_refused(self) -> None:
        self.assertIsNone(move_doc.refusal(self.root, [(TICKET, CLOSED_TICKET), (RFC, CLOSED_RFC)]))


class Preview(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(TICKET, "# Install /plan\n")
        self.write("docs/tickets/README.md", "# Queue\n\n[plan](01-0010.0040-install-plan.md)\n")
        self.commit()

    def test_a_preview_names_the_moves_and_the_citers_without_writing(self) -> None:
        untouched = self.snapshot()

        moves, citers = move_doc.preview(self.root, [(TICKET, CLOSED_TICKET)])

        self.assertEqual([(TICKET, CLOSED_TICKET)], moves)
        self.assertEqual(["docs/tickets/README.md"], citers)
        self.assertEqual(untouched, self.snapshot())


if __name__ == "__main__":
    unittest.main()


class Coverage(RepositoryCase):
    """A close may only claim complete repair when the whole corpus could actually be read."""

    def setUp(self) -> None:
        super().setUp()
        self.write(TICKET, "# Install /plan\n")
        self.commit()

    def test_a_record_the_scan_cannot_read_refuses_the_close(self) -> None:
        (self.root / "docs/notes.md").write_bytes(b"# Notes \xff\xfe with a stray byte\n")
        self.commit()
        untouched = self.snapshot()

        why = move_doc.refusal(self.root, [(TICKET, CLOSED_TICKET)])

        self.assertIn("docs/notes.md", why)
        self.assertIn("not utf-8", why.lower())
        self.assertEqual(untouched, self.snapshot())


class Escapes(RepositoryCase):
    """A destination that only looks like it is inside the repository."""

    def setUp(self) -> None:
        super().setUp()
        self.write(TICKET, "# Install /plan\n")
        self.commit()

    def test_a_destination_reached_through_a_junction_out_of_the_tree_is_refused(self) -> None:
        outside = self.root.parent / f"{self.root.name}-outside"
        outside.mkdir()
        self.addCleanup(outside.rmdir)
        if not self._junction("docs/escape", outside):
            self.skipTest("this platform cannot create a directory junction or symlink here")
        untouched = self.snapshot()

        why = move_doc.refusal(self.root, [(TICKET, "docs/escape/01-0010.0040-install-plan.md")])

        self.assertIn("outside the repository", why)
        self.assertEqual(untouched, self.snapshot())

    def _junction(self, name: str, target) -> bool:
        link = self.root / name
        link.parent.mkdir(parents=True, exist_ok=True)
        try:
            link.symlink_to(target, target_is_directory=True)
        except (OSError, NotImplementedError):
            made = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True
            )
            if made.returncode:
                return False
        self.addCleanup(link.rmdir)
        return True
