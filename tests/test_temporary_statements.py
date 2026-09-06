"""Enumerating the statements that expire, and taking out the ones that have."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import unittest

from harness import RepositoryCase

import temporary_statements

PACER = "docs/tickets/01-0020-pacer.md"
OWNER = 'ticket="docs/tickets/01-0020-pacer.md"'


class Survey(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")

    def surveyed(self, *paths: str):
        return temporary_statements.survey(self.root, list(paths or ["docs"]))

    def test_an_operative_statement_is_reported_with_its_condition_and_owner(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n"
            f'<temporary until="/pacer is installed" {OWNER}>\n'
            "This document is a suggestion of sequence.\n"
            "</temporary>\n\n## Work\n",
        )

        found = self.surveyed().statements

        self.assertEqual(1, len(found))
        self.assertEqual("docs/process.md", found[0].path)
        self.assertEqual(3, found[0].opens)
        self.assertEqual(5, found[0].closes)
        self.assertEqual("/pacer is installed", found[0].until)
        self.assertEqual(PACER, found[0].ticket)
        self.assertEqual(0, found[0].depth)

    def test_a_scope_with_nothing_expiring_is_a_clean_result_not_a_failure(self) -> None:
        self.write("docs/process.md", "# Process\n\nNothing here expires.\n")

        surveyed = self.surveyed()

        self.assertEqual([], surveyed.statements)
        self.assertEqual([], surveyed.diagnostics)

    def test_an_illustration_of_the_syntax_is_not_a_statement(self) -> None:
        self.write(
            "docs/entry.md",
            "# Entry\n\n"
            'A statement is wrapped in `<temporary until="condition" ticket="path">`.\n\n'
            "```md\n"
            '<temporary until="x" ticket="y">rule</temporary>\n'
            "```\n",
        )

        self.assertEqual([], self.surveyed().statements)

    def test_a_nested_statement_is_reported_and_so_is_the_parent_that_holds_it(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n"
            f'<temporary until="/pacer is installed" {OWNER}>\n'
            "Outer rule.\n"
            f'<temporary until="/ticket is installed" {OWNER}>\n'
            "Inner rule.\n</temporary>\nMore outer.\n</temporary>\n",
        )

        outer, inner = self.surveyed().statements

        self.assertEqual((3, 9, 0, 1), (outer.opens, outer.closes, outer.depth, outer.contains))
        self.assertEqual((5, 7, 1, 0), (inner.opens, inner.closes, inner.depth, inner.contains))

    def test_an_opening_tag_wrapped_across_lines_is_one_statement(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n<temporary\n"
            '  until="/pacer is installed"\n'
            f"  {OWNER}>\nRule.\n</temporary>\n",
        )

        found = self.surveyed().statements

        self.assertEqual(1, len(found))
        self.assertEqual("/pacer is installed", found[0].until)

    def test_a_statement_bound_to_no_ticket_is_a_diagnostic(self) -> None:
        self.write("docs/process.md", '# Process\n\n<temporary until="someday">Rule.</temporary>\n')

        self.assertEqual(["unbound"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_statement_with_no_condition_is_a_diagnostic(self) -> None:
        self.write("docs/process.md", f"# Process\n\n<temporary {OWNER}>Rule.</temporary>\n")

        self.assertEqual(["no condition"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_statement_naming_a_ticket_that_is_not_there_is_a_diagnostic(self) -> None:
        self.write(
            "docs/process.md",
            '# Process\n\n<temporary until="x" ticket="docs/tickets/absent.md">Rule.</temporary>\n',
        )

        self.assertEqual(["unknown owner"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_tag_that_never_closes_stays_visible_as_a_diagnostic(self) -> None:
        self.write("docs/process.md", f'# Process\n\n<temporary until="x" {OWNER}>\nRule.\n')

        self.assertEqual(["never closed"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_closing_tag_with_nothing_open_stays_visible_as_a_diagnostic(self) -> None:
        self.write("docs/process.md", "# Process\n\nRule.\n</temporary>\n")

        self.assertEqual(["never opened"], [note.problem for note in self.surveyed().diagnostics])

    def test_a_malformed_tag_stays_visible_as_a_diagnostic(self) -> None:
        self.write("docs/process.md", '# Process\n\n<temporary until="unterminated\nRule.\n')

        self.assertEqual(["malformed"], [note.problem for note in self.surveyed().diagnostics])


class Removal(RepositoryCase):
    """The one mechanical edit this tool makes, and everything it refuses to guess."""

    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")
        self.before = (
            "# Process\r\n\r\n"
            f'<temporary until="/pacer is installed" {OWNER}>\r\n'
            "This document is a suggestion of sequence.\r\n"
            "</temporary>\r\n\r\n## Work\r\n"
        )
        self.write("docs/process.md", self.before)

    def fingerprint(self) -> str:
        return "sha256:" + hashlib.sha256((self.root / "docs/process.md").read_bytes()).hexdigest()

    def nest_a_statement_inside_the_pacer_block(self) -> None:
        self.write(
            "docs/process.md",
            "# Process\n\n"
            f'<temporary until="/pacer is installed" {OWNER}>\n'
            "Outer.\n"
            f'<temporary until="/ticket is installed" {OWNER}>\n'
            "Inner.\n</temporary>\n</temporary>\n",
        )

    def test_removing_an_expired_statement_takes_the_block_and_nothing_else(self) -> None:
        temporary_statements.remove_statement(self.root, "docs/process.md", 3, self.fingerprint())

        self.assertEqual("# Process\r\n\r\n\r\n## Work\r\n", self.read("docs/process.md"))

    def test_a_fingerprint_from_before_someone_elses_edit_removes_nothing(self) -> None:
        stale = self.fingerprint()
        self.write("docs/process.md", self.before + "A note added since.\r\n")
        untouched = self.snapshot()

        with self.assertRaises(temporary_statements.Refused):
            temporary_statements.remove_statement(self.root, "docs/process.md", 3, stale)

        self.assertEqual(untouched, self.snapshot())

    def test_an_outer_statement_is_never_removed_over_a_statement_it_contains(self) -> None:
        self.nest_a_statement_inside_the_pacer_block()
        untouched = self.snapshot()

        with self.assertRaises(temporary_statements.Refused) as refused:
            temporary_statements.remove_statement(self.root, "docs/process.md", 3, self.fingerprint())

        self.assertIn("contains", str(refused.exception))
        self.assertEqual(untouched, self.snapshot())

    def test_the_parent_can_go_only_after_the_child_and_only_on_a_fresh_reading(self) -> None:
        self.nest_a_statement_inside_the_pacer_block()
        before_the_child_went = self.fingerprint()

        temporary_statements.remove_statement(self.root, "docs/process.md", 5, before_the_child_went)
        with self.assertRaises(temporary_statements.Refused):
            temporary_statements.remove_statement(
                self.root, "docs/process.md", 3, before_the_child_went
            )
        rescanned = temporary_statements.survey(self.root, ["docs/process.md"]).statements
        temporary_statements.remove_statement(self.root, "docs/process.md", 3, self.fingerprint())

        self.assertEqual([3], [statement.opens for statement in rescanned])
        self.assertEqual("# Process\n\n", self.read("docs/process.md"))

    def test_a_path_outside_the_repository_is_refused(self) -> None:
        with self.assertRaises(temporary_statements.Refused):
            temporary_statements.remove_statement(self.root, "../elsewhere.md", 3, self.fingerprint())


class CommandLine(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        self.write(PACER, "# Pacer\n")
        self.write(
            "docs/process.md",
            f'# Process\n\n<temporary until="/pacer is installed" {OWNER}>\nRule.\n</temporary>\n',
        )

    def run_tool(self, *argv: str) -> tuple[int, str]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = temporary_statements.main(list(argv), root=self.root)
        return status, said.getvalue()

    def test_a_clean_scope_reports_its_statements_as_json_and_succeeds(self) -> None:
        status, said = self.run_tool("docs")

        reported = json.loads(said)
        self.assertEqual(0, status)
        self.assertEqual("/pacer is installed", reported["statements"][0]["until"])
        self.assertEqual([], reported["diagnostics"])

    def test_a_diagnostic_makes_the_run_fail_even_though_it_read_everything(self) -> None:
        self.write("docs/other.md", '# Other\n\n<temporary until="x">Rule.</temporary>\n')

        status, said = self.run_tool("docs")

        self.assertEqual(1, status)
        self.assertEqual("unbound", json.loads(said)["diagnostics"][0]["problem"])

    def test_a_scope_naming_something_that_is_not_there_is_refused_not_reported_clean(self) -> None:
        status, said = self.run_tool("docs", "docs/typo")

        self.assertEqual(2, status)
        self.assertIn("refused", said)
        self.assertIn("docs/typo", said)

    def test_a_refused_scope_reports_no_survey_at_all(self) -> None:
        """A partial scope must not surface as a result a maintainer could read as complete."""
        status, said = self.run_tool("docs/typo")

        self.assertEqual(2, status)
        self.assertNotIn('"statements"', said)

    def test_asking_for_usage_is_answered_not_scanned_as_a_scope(self) -> None:
        status, said = self.run_tool("--help")

        self.assertEqual(0, status)
        self.assertIn("usage", said)
        self.assertNotIn('"scanned"', said)

    def test_an_unknown_flag_is_a_usage_error_rather_than_an_empty_scan(self) -> None:
        status, said = self.run_tool("--recurse")

        self.assertEqual(2, status)
        self.assertIn("usage", said)
        self.assertNotIn('"scanned"', said)

    def test_a_removal_names_its_line_after_the_final_colon_so_drive_letters_survive(self) -> None:
        digest = "sha256:" + hashlib.sha256((self.root / "docs/process.md").read_bytes()).hexdigest()

        status, _ = self.run_tool("--remove", "docs/process.md:3", "--expect", digest)

        self.assertEqual(0, status)
        self.assertEqual("# Process\n\n", self.read("docs/process.md"))


if __name__ == "__main__":
    unittest.main()
