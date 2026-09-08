"""Installing a mechanism's rules into skills it does not own, and taking them out again."""

from __future__ import annotations

import contextlib
import io
import json
import unittest

from harness import RepositoryCase

import inject_rules

SLUG = "sample-shape"
RULES = f".agents/mechanisms/{SLUG}/{SLUG}.rules.md"
TARGET = ".agents/skills/keeper/SKILL.md"
ANCHOR = "## Installed from other mechanisms"

TARGET_TEXT = (
    "# Keeper\n\n"
    "- **A1** Keep things.\n\n"
    f"{ANCHOR}\n\n"
    "## Finish\n\n"
    "- **F1** Report.\n"
)

INSTALLED = (
    f'<installed by="{SLUG}">\n'
    "**R1** Check the records with their script — format never\n"
    "content, live rows only.\n"
    "\n"
    "**R2** Move story out of a doc into its evidence.\n"
    "</installed>"
)


def rules_file(
    table: str | None = None,
    sections: str | None = None,
) -> str:
    table = (
        table
        if table is not None
        else "| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n"
    )
    sections = (
        sections
        if sections is not None
        else (
            "## R1 — records are checked\n\n"
            f"- **target** `{TARGET}`\n"
            "- **authority** the user, 2026-09-07\n\n"
            "<rule>\n"
            "Check the records with their script — format never\n"
            "content, live rows only.\n"
            "</rule>\n\n"
            "## R2 — story leaves the doc\n\n"
            f"- **target** `{TARGET}`\n"
            "- **authority** the user, 2026-09-07\n\n"
            "<rule>\n"
            "Move story out of a doc into its evidence.\n"
            "</rule>\n"
        )
    )
    return f"# {SLUG} — rules installed elsewhere\n\nRead by the installer alone.\n\n{table}\n{sections}"


class Installing(RepositoryCase):
    """A tree holding one mechanism with two rules and one skill they install into."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)
        self.commit()

    def run_installer(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = inject_rules.main(list(operands), root=self.root)
        text = said.getvalue()
        try:
            return status, json.loads(text)
        except json.JSONDecodeError:
            return status, {"said": text}

    def test_install_then_retract_leaves_the_tree_byte_identical(self) -> None:
        before = self.snapshot()

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])
        self.assertNotEqual(before, self.snapshot())
        self.assertEqual(0, self.run_installer(SLUG, "--retract")[0])

        self.assertEqual(before, self.snapshot())

    def test_install_writes_one_block_after_the_anchor_in_file_order(self) -> None:
        self.run_installer(SLUG, "--install")

        self.assertEqual(
            TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n{INSTALLED}\n"),
            self.read(TARGET),
        )

    def test_installing_twice_changes_nothing_and_reports_the_block_present(self) -> None:
        self.run_installer(SLUG, "--install")
        once = self.snapshot()

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status)
        self.assertEqual(once, self.snapshot())
        self.assertEqual("present", report["targets"][0]["state"])


class Refusing(RepositoryCase):
    """Every refusal writes nothing and says why. Each test bends the fixture in one way."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)
        self.commit()

    def run_installer(self, *operands: str) -> tuple[int, str]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = inject_rules.main(list(operands), root=self.root)
        return status, said.getvalue()

    def assert_refused(self, expected_status: int, reason: str, *operands: str) -> None:
        untouched = self.snapshot()
        status, said = self.run_installer(*operands)
        self.assertEqual(expected_status, status, said)
        self.assertIn(reason, said)
        self.assertEqual(untouched, self.snapshot())

    # usage

    def test_no_mode_is_usage(self) -> None:
        self.assert_refused(2, "usage", SLUG)

    def test_two_modes_is_usage(self) -> None:
        self.assert_refused(2, "usage", SLUG, "--install", "--retract")

    def test_a_slug_with_check_is_usage(self) -> None:
        self.assert_refused(2, "usage", SLUG, "--check")

    def test_overwrite_with_retract_is_usage(self) -> None:
        self.assert_refused(2, "usage", SLUG, "--retract", "--overwrite")

    def test_a_slug_with_no_rules_file_is_refused(self) -> None:
        self.assert_refused(1, "no rules file", "nobody", "--install")

    # the anchor

    def test_a_missing_anchor_refuses(self) -> None:
        self.write(TARGET, TARGET_TEXT.replace(ANCHOR, "## Something else"))
        self.assert_refused(1, "not found", SLUG, "--install")

    def test_an_ambiguous_anchor_refuses(self) -> None:
        self.write(TARGET, TARGET_TEXT + f"\n{ANCHOR}\n")
        self.assert_refused(1, "ambiguous", SLUG, "--install")

    def test_an_anchor_that_is_an_unterminated_last_line_refuses(self) -> None:
        self.write(TARGET, "# Keeper\n\n" + ANCHOR)
        self.assert_refused(1, "no newline", SLUG, "--install")

    def test_an_anchor_inside_a_fence_is_not_an_anchor(self) -> None:
        self.write(TARGET, f"# Keeper\n\n```md\n{ANCHOR}\n```\n")
        self.assert_refused(1, "not found", SLUG, "--install")

    # the table

    def test_a_target_named_twice_in_the_table_refuses(self) -> None:
        row = f"| `{TARGET}` | `{ANCHOR}` |\n"
        self.write(RULES, rules_file(table="| target | anchor |\n|---|---|\n" + row + row))
        self.assert_refused(1, "named twice", SLUG, "--install")

    def test_a_target_with_no_table_row_refuses(self) -> None:
        self.write(RULES, rules_file(table="| target | anchor |\n|---|---|\n"))
        self.assert_refused(1, "no row in the anchor table", SLUG, "--install")

    # the sections

    def test_a_section_without_a_target_refuses(self) -> None:
        self.write(RULES, rules_file().replace(f"- **target** `{TARGET}`\n", "", 1))
        self.assert_refused(1, "names no target", SLUG, "--install")

    def test_a_section_without_authority_refuses(self) -> None:
        self.write(RULES, rules_file().replace("- **authority** the user, 2026-09-07\n", "", 1))
        self.assert_refused(1, "authority exactly once", SLUG, "--install")

    def test_a_section_without_a_span_refuses(self) -> None:
        self.write(RULES, rules_file().replace("<rule>\n", "", 1))
        self.assert_refused(1, "exactly one <rule>", SLUG, "--install")

    def test_a_section_with_two_spans_refuses(self) -> None:
        doubled = rules_file().replace("</rule>\n\n## R2", "</rule>\n\n<rule>\nAgain.\n</rule>\n\n## R2")
        self.write(RULES, doubled)
        self.assert_refused(1, "exactly one <rule>", SLUG, "--install")

    def test_a_duplicate_id_refuses(self) -> None:
        self.write(RULES, rules_file().replace("## R2 — story", "## R1 — story"))
        self.assert_refused(1, "appears twice", SLUG, "--install")

    def test_a_file_with_no_sections_refuses(self) -> None:
        self.write(RULES, rules_file(sections=""))
        self.assert_refused(1, "no rule sections", SLUG, "--install")

    # the body

    def test_a_body_holding_the_closing_tag_refuses(self) -> None:
        self.write(RULES, rules_file().replace("Move story out", "Move </installed> out"))
        self.assert_refused(1, "installed tag", SLUG, "--install")

    def test_a_body_holding_a_citation_refuses(self) -> None:
        self.write(RULES, rules_file().replace("its evidence.", "[its evidence](../../docs/x.md)."))
        self.assert_refused(1, "citation", SLUG, "--install")

    def test_a_body_holding_a_heading_line_refuses(self) -> None:
        self.write(RULES, rules_file().replace("Move story out", "## Move story out"))
        self.assert_refused(1, "heading line", SLUG, "--install")

    # the target's blocks

    def test_two_blocks_of_one_slug_in_one_file_refuse(self) -> None:
        self.write(TARGET, TARGET_TEXT + f"\n{INSTALLED}\n\n{INSTALLED}\n")
        self.assert_refused(1, "two blocks", SLUG, "--install")

    def test_a_block_that_never_closes_refuses(self) -> None:
        self.write(TARGET, TARGET_TEXT + f'\n<installed by="{SLUG}">\nlost\n')
        self.assert_refused(1, "never closes", SLUG, "--install")

    def test_a_tag_inside_a_fence_is_not_a_block(self) -> None:
        self.write(TARGET, TARGET_TEXT + f"\n```md\n{INSTALLED}\n```\n")
        untouched = self.read(TARGET)

        status, said = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status, said)
        self.assertEqual(2, self.read(TARGET).count(f'<installed by="{SLUG}">'))
        self.assertIn(untouched.split(ANCHOR)[1], self.read(TARGET))

    def test_preflight_is_all_or_nothing(self) -> None:
        other = ".agents/skills/other/SKILL.md"
        table = "| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n| `{other}` | `{ANCHOR}` |\n"
        sections = rules_file().split("| `")[0]  # unused; the sections are rebuilt below
        two_targets = rules_file(table=table).replace(
            f"- **target** `{TARGET}`\n- **authority** the user, 2026-09-07\n\n<rule>\nCheck",
            f"- **target** `{TARGET}`\n- **target** `{other}`\n- **authority** the user, 2026-09-07\n\n<rule>\nCheck",
        )
        self.write(RULES, two_targets)
        self.assertNotEqual(sections, "")
        self.assert_refused(1, "target missing", SLUG, "--install")


class Drifting(RepositoryCase):
    """A block that no longer says what its rules file says."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)
        self.run_installer(SLUG, "--install")
        self.commit()

    def run_installer(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = inject_rules.main(list(operands), root=self.root)
        return status, json.loads(said.getvalue())

    def edit_the_block(self) -> None:
        self.write(TARGET, self.read(TARGET).replace("live rows only.", "live rows only, mostly."))

    def test_an_edited_block_refuses_install_and_names_the_target(self) -> None:
        self.edit_the_block()
        edited = self.snapshot()

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(1, status)
        self.assertIn(TARGET, report["refusals"][0])
        self.assertIn("differs", report["refusals"][0])
        self.assertEqual(edited, self.snapshot())

    def test_an_edited_block_refuses_retract(self) -> None:
        self.edit_the_block()
        edited = self.snapshot()

        status, report = self.run_installer(SLUG, "--retract")

        self.assertEqual(1, status)
        self.assertIn("differs", report["refusals"][0])
        self.assertEqual(edited, self.snapshot())

    def test_overwrite_replaces_the_block_whole_and_reports_what_it_replaced(self) -> None:
        self.edit_the_block()

        status, report = self.run_installer(SLUG, "--install", "--overwrite")

        self.assertEqual(0, status)
        self.assertEqual("overwritten", report["targets"][0]["state"])
        self.assertIn("mostly", report["targets"][0]["replaced"])
        self.assertEqual(TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n{INSTALLED}\n"), self.read(TARGET))

    def test_adding_a_rule_at_the_source_is_the_overwrite_road(self) -> None:
        self.write(
            RULES,
            rules_file()
            + f"\n## R3 — indexes are derived\n\n- **target** `{TARGET}`\n"
            "- **authority** the user, 2026-09-07\n\n<rule>\nRender an index on request.\n</rule>\n",
        )
        installed = self.snapshot()

        status, report = self.run_installer(SLUG, "--install")
        self.assertEqual(1, status)
        self.assertIn("differs", report["refusals"][0])
        self.assertEqual(installed, self.snapshot())

        status, report = self.run_installer(SLUG, "--install", "--overwrite")
        self.assertEqual(0, status)
        self.assertIn("**R3** Render an index on request.\n</installed>", self.read(TARGET))

    def test_an_edited_block_is_found_and_called_drifted_never_absent(self) -> None:
        self.edit_the_block()

        status, report = self.run_installer("--check")

        self.assertEqual(1, status)
        self.assertEqual("drifted", report["blocks"][0]["state"])

    def test_a_block_matching_modulo_line_endings_is_present(self) -> None:
        self.write(TARGET, self.read(TARGET).replace("\n", "\r\n"))

        status, report = self.run_installer("--check")

        self.assertEqual(0, status, report)
        self.assertEqual("present", report["blocks"][0]["state"])

    def test_a_crlf_rules_file_still_matches_its_lf_block(self) -> None:
        # Life's defect: the source came back from autocrlf with CRLF, the installed side was
        # normalised, the rendered side was not, and every block read as drifted.
        self.write(RULES, rules_file().replace("\n", "\r\n"))

        status, report = self.run_installer("--check")

        self.assertEqual(0, status, report)
        self.assertEqual("present", report["blocks"][0]["state"])

    def test_a_real_edit_under_crlf_is_still_drifted(self) -> None:
        self.write(TARGET, self.read(TARGET).replace("\n", "\r\n").replace("live rows only.", "live rows."))

        status, report = self.run_installer("--check")

        self.assertEqual(1, status)
        self.assertEqual("drifted", report["blocks"][0]["state"])

    def test_retract_of_an_absent_block_is_reported_not_refused(self) -> None:
        self.run_installer(SLUG, "--retract")

        status, report = self.run_installer(SLUG, "--retract")

        self.assertEqual(0, status)
        self.assertEqual("absent", report["targets"][0]["state"])


class Checking(RepositoryCase):
    """The sweep: every rules file against its targets, every block against the rules files."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)
        self.commit()

    def checked(self) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = inject_rules.main(["--check"], root=self.root)
        return status, json.loads(said.getvalue())

    def test_an_uninstalled_block_is_absent_and_a_diagnostic(self) -> None:
        status, report = self.checked()

        self.assertEqual(1, status)
        self.assertEqual("absent", report["blocks"][0]["state"])
        self.assertEqual(1, report["rules files"])
        self.assertTrue(report["diagnostics"])

    def test_an_installed_block_is_present_and_the_run_is_clean(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            inject_rules.main([SLUG, "--install"], root=self.root)

        status, report = self.checked()

        self.assertEqual(0, status)
        self.assertEqual([], report["diagnostics"])

    def test_a_block_of_a_slug_with_no_rules_file_is_an_orphan(self) -> None:
        self.write("docs/notes.md", '# Notes\n\n<installed by="gone">\nleft behind\n</installed>\n')

        status, report = self.checked()

        self.assertEqual(1, status)
        self.assertEqual([{"slug": "gone", "file": "docs/notes.md"}], report["orphans"])

    def test_a_block_in_a_file_its_rules_file_does_not_target_is_an_orphan(self) -> None:
        self.write("docs/notes.md", f"# Notes\n\n{INSTALLED}\n")

        status, report = self.checked()

        self.assertEqual(1, status)
        self.assertEqual([{"slug": SLUG, "file": "docs/notes.md"}], report["orphans"])

    def test_an_unparseable_rules_file_is_a_diagnostic(self) -> None:
        self.write(RULES, rules_file(sections=""))

        status, report = self.checked()

        self.assertEqual(1, status)
        self.assertIn("no rule sections", report["diagnostics"][0])

    def test_a_tree_with_no_rules_file_reports_zero_and_is_clean(self) -> None:
        (self.root / RULES).unlink()

        status, report = self.checked()

        self.assertEqual(0, status)
        self.assertEqual(0, report["rules files"])

    def test_a_missing_target_and_a_missing_anchor_are_named(self) -> None:
        self.write(TARGET, "# Keeper\n")
        status, report = self.checked()
        self.assertEqual("anchor missing", report["blocks"][0]["state"])

        (self.root / TARGET).unlink()
        status, report = self.checked()
        self.assertEqual("target missing", report["blocks"][0]["state"])


if __name__ == "__main__":
    unittest.main()
