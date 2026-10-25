# Mechanism: mechanism-shape
"""Installing a mechanism's rules into skills, its own included, and taking them out again."""

from __future__ import annotations

import contextlib
import io
import json
import os
import stat
import unittest

from repository import RepositoryCase

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

    def test_a_crlf_target_round_trips_byte_identical_too(self) -> None:
        self.write(TARGET, TARGET_TEXT.replace("\n", "\r\n"))
        before = self.snapshot()

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])
        self.assertEqual(0, self.run_installer(SLUG, "--retract")[0])

        self.assertEqual(before, self.snapshot())

    def test_install_writes_one_block_in_file_order_under_an_empty_anchor_section(self) -> None:
        self.run_installer(SLUG, "--install")

        self.assertEqual(
            TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n{INSTALLED}\n"),
            self.read(TARGET),
        )

    def test_a_block_lands_at_the_end_of_the_anchors_section_after_its_content(self) -> None:
        text = TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\nThe section's own prose.\n\n- and a bullet\n")
        self.write(TARGET, text)
        before = self.snapshot()

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        self.assertEqual(text.replace("- and a bullet\n", f"- and a bullet\n\n{INSTALLED}\n"), self.read(TARGET))
        self.assertEqual(0, self.run_installer(SLUG, "--retract")[0])
        self.assertEqual(before, self.snapshot())

    def test_a_section_ends_at_the_next_heading_of_its_own_level_or_higher_and_not_at_a_subheading(self) -> None:
        text = TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n### A subsection\n\nStill inside.\n")
        self.write(TARGET, text)

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        self.assertEqual(text.replace("Still inside.\n", f"Still inside.\n\n{INSTALLED}\n"), self.read(TARGET))

    def test_a_heading_drawn_in_a_fence_does_not_end_the_section(self) -> None:
        text = TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n```md\n## Not a heading\n```\n\nAfter the fence.\n")
        self.write(TARGET, text)

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        self.assertEqual(text.replace("After the fence.\n", f"After the fence.\n\n{INSTALLED}\n"), self.read(TARGET))

    def test_a_straw_dog_opening_on_the_next_section_is_left_to_that_section(self) -> None:
        text = TARGET_TEXT.replace(
            "## Finish\n", 'Own prose.\n\n<straw-dog question="q-0001">\n\n## Finish\n'
        ).replace("- **F1** Report.\n", "- **F1** Report.\n</straw-dog>\n")
        self.write(TARGET, text)

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        self.assertEqual(text.replace("Own prose.\n", f"Own prose.\n\n{INSTALLED}\n"), self.read(TARGET))

    def test_a_section_that_ends_the_file_takes_the_block_after_its_last_line(self) -> None:
        text = "# Keeper\n\n" f"{ANCHOR}\n\nLast prose.\n"
        self.write(TARGET, text)

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        self.assertEqual(f"{text}\n{INSTALLED}\n", self.read(TARGET))

    def test_blocks_of_two_mechanisms_at_one_anchor_stand_in_install_order(self) -> None:
        other = "other-shape"
        self.write(
            f".agents/mechanisms/{other}/{other}.rules.md",
            rules_file().replace(SLUG, other),
        )
        self.run_installer(SLUG, "--install")

        self.assertEqual(0, self.run_installer(other, "--install")[0])

        written = self.read(TARGET)
        self.assertLess(written.index(f'<installed by="{SLUG}">'), written.index(f'<installed by="{other}">'))
        self.assertIn(f"</installed>\n\n<installed by=\"{other}\">", written)
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_an_anchor_that_is_a_subheading_inside_a_tagged_span_takes_the_block_and_gives_it_back(self) -> None:
        anchor = "### Record resolutions inline"
        target_text = (
            "# Advisor\n\n<what-to-do>\nInterview me.\n</what-to-do>\n\n"
            f"<supporting-info>\n\n## During the session\n\n{anchor}\n\n"
            "Strike the question and answer beside it.\n\n### Offer ADRs sparingly\n\n"
            "Rarely.\n\n</supporting-info>\n"
        )
        self.write(TARGET, target_text)
        self.write(RULES, rules_file(table=f"| target | anchor |\n|---|---|\n| `{TARGET}` | `{anchor}` |\n"))
        before = self.snapshot()

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])
        installed = self.read(TARGET)
        self.assertEqual(0, self.run_installer(SLUG, "--retract")[0])

        self.assertEqual(
            target_text.replace("beside it.\n", f"beside it.\n\n{INSTALLED}\n"), installed
        )
        self.assertEqual(before, self.snapshot())

    def test_installing_twice_changes_nothing_and_reports_the_block_present(self) -> None:
        self.run_installer(SLUG, "--install")
        once = self.snapshot()

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status)
        self.assertEqual(once, self.snapshot())
        self.assertEqual("present", report["targets"][0]["state"])


LOCAL = "local"
LOCAL_FILE = "local.rules.md"

LOCAL_INSTALLED = (
    f'<installed by="{LOCAL}">\n'
    "**L1** Commit only on explicit permission.\n"
    "</installed>"
)


def local_file(
    table: str | None = None,
    sections: str | None = None,
) -> str:
    """The project's own rules file, beside the entry file, in the grammar a mechanism's uses."""
    table = (
        table
        if table is not None
        else "| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n"
    )
    sections = (
        sections
        if sections is not None
        else (
            "## L1 — commit is asked\n\n"
            f"- **target** `{TARGET}`\n"
            "- **authority** the user, 2026-09-05\n\n"
            "<rule>\n"
            "Commit only on explicit permission.\n"
            "</rule>\n"
        )
    )
    return f"# {LOCAL} — this project's rules\n\nRead by the installer alone.\n\n{table}\n{sections}"


class LocalSource(RepositoryCase):
    """A project's own rules file beside the entry file, read as one more source."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)
        self.write(LOCAL_FILE, local_file())

    def run_installer(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = inject_rules.main(list(operands), root=self.root)
        text = said.getvalue()
        try:
            return status, json.loads(text)
        except json.JSONDecodeError:
            return status, {"said": text}

    def test_the_local_file_installs_from_the_root_and_the_check_reports_its_block(self) -> None:
        self.run_installer(SLUG, "--install")

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(0, status, report)
        self.assertIn(LOCAL_INSTALLED, self.read(TARGET))
        status, report = self.run_installer("--check")
        self.assertEqual(0, status, report)
        self.assertEqual(2, report["rules files"])
        self.assertIn({"slug": LOCAL, "target": TARGET, "state": "present"}, report["blocks"])

    # local last

    def test_the_local_block_lands_after_every_block_at_its_anchor(self) -> None:
        self.run_installer(SLUG, "--install")

        self.assertEqual(0, self.run_installer(LOCAL, "--install")[0])

        written = self.read(TARGET)
        self.assertLess(written.index(INSTALLED), written.index(LOCAL_INSTALLED))
        self.assertIn(f"{INSTALLED}\n\n{LOCAL_INSTALLED}\n\n## Finish", written)
        self.assertEqual(0, self.run_installer(LOCAL, "--retract")[0])
        self.assertEqual(TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n{INSTALLED}\n"), self.read(TARGET))

    def test_a_mechanism_installed_after_the_local_block_still_lands_before_it(self) -> None:
        self.run_installer(LOCAL, "--install")

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        written = self.read(TARGET)
        self.assertLess(written.index(INSTALLED), written.index(LOCAL_INSTALLED))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_local_anchor_ahead_of_a_mechanism_block_is_refused_naming_that_block(self) -> None:
        self.write(TARGET, TARGET_TEXT.replace("- **A1** Keep things.\n", "- **A1** Keep things.\n\n## Local\n"))
        self.write(LOCAL_FILE, local_file(table="| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `## Local` |\n"))
        self.run_installer(SLUG, "--install")
        untouched = self.snapshot()

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(1, status)
        self.assertIn("not be last", report["refusals"][0])
        self.assertIn(SLUG, report["refusals"][0])
        self.assertEqual(untouched, self.snapshot())

    # overrides

    def overriding(self, cited: str, targets: str = f"- **target** `{TARGET}`\n") -> str:
        return local_file(sections=(
            "## L1 — the pair need not close together here\n\n"
            f"{targets}"
            f"- **overrides** `{cited}`\n"
            "- **authority** the user, 2026-09-21\n\n"
            "<rule>\nClose the ticket alone.\n</rule>\n"
        ))

    def test_an_override_names_the_rule_where_the_reader_meets_it_and_lands_after_it(self) -> None:
        self.write(LOCAL_FILE, self.overriding(f"{SLUG}/R2"))
        self.run_installer(SLUG, "--install")

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(0, status, report)
        written = self.read(TARGET)
        self.assertIn(f'<installed by="{LOCAL}">\n**L1** *(overrides {SLUG}/R2)* Close the ticket alone.\n</installed>', written)
        self.assertLess(written.index("**R2**"), written.index("**L1**"))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_an_override_of_a_slug_with_no_rules_file_is_refused_naming_the_entry(self) -> None:
        self.write(LOCAL_FILE, self.overriding("nobody/R2"))
        untouched = self.snapshot()

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(1, status)
        self.assertIn("L1 overrides nobody/R2", report["refusals"][0])
        self.assertIn("no rules file", report["refusals"][0])
        self.assertEqual(untouched, self.snapshot())

    def test_an_override_of_an_id_the_rules_file_does_not_define_is_refused(self) -> None:
        self.write(LOCAL_FILE, self.overriding(f"{SLUG}/R9"))

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(1, status)
        self.assertIn("does not define", report["refusals"][0])
        self.assertIn("L1", report["refusals"][0])

    def test_an_override_of_a_rule_not_installed_in_that_target_is_refused(self) -> None:
        elsewhere = ".agents/skills/other/SKILL.md"
        self.write(elsewhere, TARGET_TEXT)
        self.write(LOCAL_FILE, self.overriding(f"{SLUG}/R2", targets=f"- **target** `{elsewhere}`\n").replace(
            f"| `{TARGET}` | `{ANCHOR}` |", f"| `{elsewhere}` | `{ANCHOR}` |"
        ))

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(1, status)
        self.assertIn(f"not installed in {elsewhere}", report["refusals"][0])

    def test_two_overrides_bullets_refuse(self) -> None:
        doubled = self.overriding(f"{SLUG}/R2").replace(
            f"- **overrides** `{SLUG}/R2`\n", f"- **overrides** `{SLUG}/R2`\n- **overrides** `{SLUG}/R1`\n"
        )
        self.write(LOCAL_FILE, doubled)

        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(1, status)
        self.assertIn("overrides more than once", report["refusals"][0])

    def test_a_drifted_override_is_refused_at_check_the_same_as_any_rule(self) -> None:
        self.write(LOCAL_FILE, self.overriding(f"{SLUG}/R2"))
        self.run_installer(SLUG, "--install")
        self.run_installer(LOCAL, "--install")
        self.write(LOCAL_FILE, self.overriding(f"{SLUG}/R9"))

        status, report = self.run_installer("--check")

        self.assertEqual(1, status)
        self.assertTrue(any("does not define" in note for note in report["diagnostics"]), report)

    def test_a_local_block_written_ahead_of_a_mechanism_block_is_not_last(self) -> None:
        self.write(TARGET, TARGET_TEXT.replace(f"{ANCHOR}\n", f"{ANCHOR}\n\n{LOCAL_INSTALLED}\n\n{INSTALLED}\n"))

        status, report = self.run_installer("--check")

        self.assertEqual(1, status)
        self.assertIn({"slug": LOCAL, "target": TARGET, "state": "not last"}, report["blocks"])

    def test_a_mechanism_directory_named_local_is_refused_and_a_diagnostic(self) -> None:
        self.write(f".agents/mechanisms/{LOCAL}/{LOCAL}.rules.md", rules_file())
        untouched = self.snapshot()

        status, report = self.run_installer(LOCAL, "--install")
        self.assertEqual(1, status)
        self.assertIn("collides", report["refusals"][0])
        self.assertEqual(untouched, self.snapshot())

        status, report = self.run_installer("--check")
        self.assertEqual(1, status)
        self.assertTrue(any("collides" in note for note in report["diagnostics"]), report)


class Refusing(RepositoryCase):
    """Every refusal writes nothing and says why. Each test bends the fixture in one way."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)

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

    def test_no_mode_or_two_modes_is_usage(self) -> None:
        for operands in ([SLUG], [SLUG, "--install", "--retract"]):
            with self.subTest(operands=operands):
                self.assert_refused(2, "usage", *operands)

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

    def test_a_section_without_exactly_one_span_refuses(self) -> None:
        spans = {
            "none": rules_file().replace("<rule>\n", "", 1),
            "two": rules_file().replace("</rule>\n\n## R2", "</rule>\n\n<rule>\nAgain.\n</rule>\n\n## R2"),
        }
        for count, written in spans.items():
            with self.subTest(spans=count):
                self.write(RULES, written)
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

    def test_a_body_holding_a_straw_dog_tag_refuses(self) -> None:
        wrapped = rules_file().replace(
            "Move story out",
            '<straw-dog question="q-0002">\nMove story out',
        ).replace("into its evidence.", "into its evidence.\n</straw-dog>")
        self.write(RULES, wrapped)

        self.assert_refused(1, "straw dog", SLUG, "--install")

    def test_a_section_wrapped_in_a_straw_dog_installs_the_rule_and_not_the_tag(self) -> None:
        marked = rules_file().replace(
            "## R2 — story leaves the doc",
            '<straw-dog question="q-0002">\n'
            "## R2 — story leaves the doc",
        ).replace("</rule>\n", "</rule>\n</straw-dog>\n", 2)
        self.write(RULES, marked)

        self.assertEqual(0, self.run_installer(SLUG, "--install")[0])

        written = self.read(TARGET)
        self.assertIn("**R2** Move story out of a doc into its evidence.", written)
        self.assertNotIn("straw-dog", written)

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
        two_targets = rules_file(table=table).replace(
            f"- **target** `{TARGET}`\n- **authority** the user, 2026-09-07\n\n<rule>\nCheck",
            f"- **target** `{TARGET}`\n- **target** `{other}`\n- **authority** the user, 2026-09-07\n\n<rule>\nCheck",
        )
        self.write(RULES, two_targets)
        self.assert_refused(1, "target missing", SLUG, "--install")


class Drifting(RepositoryCase):
    """A block that no longer says what its rules file says."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)
        self.run_installer(SLUG, "--install")

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

    def test_an_edited_block_is_found_and_called_drifted_never_absent(self) -> None:
        installed = self.read(TARGET)
        for endings in ("\n", "\r\n"):
            with self.subTest(endings=endings):
                self.write(TARGET, installed.replace("\n", endings))
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

    def test_retract_of_an_absent_block_is_reported_not_refused(self) -> None:
        self.run_installer(SLUG, "--retract")

        status, report = self.run_installer(SLUG, "--retract")

        self.assertEqual(0, status)
        self.assertEqual("absent", report["targets"][0]["state"])


class FailingMidWrite(RepositoryCase):
    """Preflight passed, the first target was written, the second cannot be: say so, roll nothing back."""

    OTHER = ".agents/skills/other/SKILL.md"

    def setUp(self) -> None:
        super().setUp()
        table = "| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n| `{self.OTHER}` | `{ANCHOR}` |\n"
        self.write(RULES, rules_file(table=table).replace(
            f"- **target** `{TARGET}`\n- **authority** the user, 2026-09-07\n\n<rule>\nCheck",
            f"- **target** `{TARGET}`\n- **target** `{self.OTHER}`\n- **authority** the user, 2026-09-07\n\n<rule>\nCheck",
        ))
        self.write(TARGET, TARGET_TEXT)
        self.write(self.OTHER, TARGET_TEXT)
        os.chmod(self.root / self.OTHER, stat.S_IREAD)
        self.addCleanup(os.chmod, self.root / self.OTHER, stat.S_IWRITE | stat.S_IREAD)
        try:
            with (self.root / self.OTHER).open("a", encoding="utf-8"):
                pass
        except PermissionError:
            pass
        else:
            self.skipTest("this user may write a read-only file, as root may")

    def test_a_target_that_cannot_be_written_is_reported_with_what_landed_and_what_did_not(self) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = inject_rules.main([SLUG, "--install"], root=self.root)
        report = json.loads(said.getvalue())

        self.assertEqual(1, status)
        self.assertEqual([TARGET], report["done"])
        self.assertEqual([], report["pending"])
        self.assertIn(self.OTHER, report["refusals"][0])
        self.assertIn(f'<installed by="{SLUG}">', self.read(TARGET))
        self.assertEqual(TARGET_TEXT, self.read(self.OTHER))


SECOND = ".agents/skills/sweeper/SKILL.md"


class DroppingATarget(RepositoryCase):
    """A rules file that stops naming a target: the next install takes its block out of it."""

    def setUp(self) -> None:
        super().setUp()
        self.write(TARGET, TARGET_TEXT)
        self.write(SECOND, TARGET_TEXT.replace("# Keeper", "# Sweeper"))
        self.before = self.read(SECOND)
        self.write(RULES, rules_file(
            table=f"| target | anchor |\n|---|---|\n| `{TARGET}` | `{ANCHOR}` |\n| `{SECOND}` | `{ANCHOR}` |\n",
            sections=self.section("R1", TARGET) + "\n" + self.section("R2", SECOND),
        ))
        self.run_installer(SLUG, "--install")
        self.write(RULES, rules_file(sections=self.section("R1", TARGET)))

    @staticmethod
    def section(rule: str, target: str) -> str:
        return (
            f"## {rule} — a rule\n\n- **target** `{target}`\n- **authority** the user, 2026-09-07\n\n"
            f"<rule>\nRule {rule}.\n</rule>\n"
        )

    def run_installer(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = inject_rules.main(list(operands), root=self.root)
        return status, json.loads(said.getvalue())

    def test_the_next_install_removes_the_block_names_it_and_the_check_passes(self) -> None:
        self.assertIn(f'<installed by="{SLUG}">', self.read(SECOND))

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status, report)
        self.assertEqual(self.before, self.read(SECOND))
        removed = [target for target in report["targets"] if target["target"] == SECOND]
        self.assertEqual("removed", removed[0]["state"])
        self.assertIn("Rule R2.", removed[0]["removed"])
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_block_of_a_slug_with_no_rules_file_stays(self) -> None:
        ghost = '\n<installed by="ghost">\n**G1** Nobody owns this.\n</installed>\n'
        self.write(SECOND, self.read(SECOND) + ghost)

        self.run_installer(SLUG, "--install", "--overwrite")

        self.assertIn('<installed by="ghost">', self.read(SECOND))
        self.assertNotIn(f'<installed by="{SLUG}">', self.read(SECOND))

    def test_a_refusal_on_a_named_target_leaves_the_dropped_block_in_place(self) -> None:
        self.write(TARGET, TARGET_TEXT.replace(ANCHOR, "## Another heading"))
        held = self.read(SECOND)

        status, report = self.run_installer(SLUG, "--install", "--overwrite")

        self.assertEqual(1, status)
        self.assertTrue(report["refusals"])
        self.assertEqual(held, self.read(SECOND))


GROUP = ".agents/skills/*/SKILL.md"
HEARS = "## What the person hears"


def speaking_skill(name: str, speaks: bool = True) -> str:
    """A skill's file, holding the group's heading or not."""
    heard = f"{HEARS}\n\nWhat was done.\n\n" if speaks else ""
    return f"# {name}\n\nIts work.\n\n{heard}## Finish\n\nDone.\n"


class Grouping(RepositoryCase):
    """A rules file whose anchor-table row is a path pattern: its block reaches every file the
    pattern matches that holds the heading, whether the rules file knew of it or not."""

    def setUp(self) -> None:
        super().setUp()
        self.write(".agents/skills/alpha/SKILL.md", speaking_skill("Alpha"))
        self.write(".agents/skills/beta/SKILL.md", speaking_skill("Beta"))
        self.write(".agents/skills/gamma/SKILL.md", speaking_skill("Gamma", speaks=False))
        self.write("docs/notes.md", speaking_skill("Notes"))
        self.before = {name: self.read(name) for name in self.files()}
        self.write(RULES, self.group_rules())

    @staticmethod
    def group_rules(table: str = "") -> str:
        return rules_file(
            table=table or f"| target | anchor |\n|---|---|\n| `{GROUP}` | `{HEARS}` |\n",
            sections=(
                f"## V1 — the voice\n\n- **target** `{GROUP}`\n- **authority** the user, 2026-10-25\n\n"
                "<rule>\nSpeak in the project's voice.\n</rule>\n"
            ),
        )

    @staticmethod
    def files() -> list[str]:
        return [
            ".agents/skills/alpha/SKILL.md",
            ".agents/skills/beta/SKILL.md",
            ".agents/skills/gamma/SKILL.md",
            "docs/notes.md",
        ]

    def run_installer(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = inject_rules.main(list(operands), root=self.root)
        return status, json.loads(said.getvalue())

    def holds_block(self, name: str) -> bool:
        return f'<installed by="{SLUG}">' in self.read(name)

    def test_the_block_reaches_every_matching_file_that_holds_the_heading_and_no_other(self) -> None:
        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status, report)
        self.assertTrue(self.holds_block(".agents/skills/alpha/SKILL.md"))
        self.assertTrue(self.holds_block(".agents/skills/beta/SKILL.md"))
        self.assertFalse(self.holds_block(".agents/skills/gamma/SKILL.md"), "it does not hold the heading")
        self.assertFalse(self.holds_block("docs/notes.md"), "the pattern does not match it")
        self.assertIn("**V1** Speak in the project's voice.", self.read(".agents/skills/alpha/SKILL.md"))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_file_that_comes_to_hold_the_heading_is_reported_then_filled(self) -> None:
        self.run_installer(SLUG, "--install")
        self.write(".agents/skills/gamma/SKILL.md", speaking_skill("Gamma"))

        status, report = self.run_installer("--check")

        self.assertEqual(1, status)
        self.assertIn(f"{SLUG} in .agents/skills/gamma/SKILL.md: absent", report["diagnostics"])
        self.run_installer(SLUG, "--install")
        self.assertTrue(self.holds_block(".agents/skills/gamma/SKILL.md"))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_file_that_stops_holding_the_heading_holds_an_orphan_the_next_install_takes_out(self) -> None:
        self.run_installer(SLUG, "--install")
        beta = self.read(".agents/skills/beta/SKILL.md")
        self.write(".agents/skills/beta/SKILL.md", beta.replace(HEARS, "## What it leaves"))

        status, report = self.run_installer("--check")

        self.assertEqual(1, status)
        self.assertIn(f"orphan block of {SLUG} in .agents/skills/beta/SKILL.md", report["diagnostics"])
        self.run_installer(SLUG, "--install")
        self.assertFalse(self.holds_block(".agents/skills/beta/SKILL.md"))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_group_with_no_member_installs_nothing_and_is_no_finding(self) -> None:
        for name in self.files():
            self.write(name, self.read(name).replace(HEARS, "## Something else"))

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status, report)
        self.assertEqual([], report["refusals"])
        self.assertFalse(any(self.holds_block(name) for name in self.files()))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_file_named_explicitly_and_matched_by_the_pattern_holds_one_block_at_the_named_place(self) -> None:
        self.write(RULES, rules_file(
            table=(
                f"| target | anchor |\n|---|---|\n| `{GROUP}` | `{HEARS}` |\n"
                "| `.agents/skills/alpha/SKILL.md` | `## Finish` |\n"
            ),
            sections=(
                f"## V1 — the voice\n\n- **target** `{GROUP}`\n- **authority** the user, 2026-10-25\n\n"
                "<rule>\nSpeak in the project's voice.\n</rule>\n\n"
                "## F1 — the finish\n\n- **target** `.agents/skills/alpha/SKILL.md`\n"
                "- **authority** the user, 2026-10-25\n\n<rule>\nFinish cleanly.\n</rule>\n"
            ),
        ))

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(0, status, report)
        alpha = self.read(".agents/skills/alpha/SKILL.md")
        self.assertEqual(1, alpha.count(f'<installed by="{SLUG}">'), alpha)
        self.assertLess(alpha.index("## Finish"), alpha.index(f'<installed by="{SLUG}">'), "the named row places it")
        self.assertLess(alpha.index("**V1** Speak in the project's voice."), alpha.index("**F1** Finish cleanly."))
        self.assertNotIn("Finish cleanly.", self.read(".agents/skills/beta/SKILL.md"))
        self.assertEqual(0, self.run_installer("--check")[0])

    def test_a_file_two_groups_reach_is_refused(self) -> None:
        self.write(RULES, self.group_rules(
            f"| target | anchor |\n|---|---|\n| `{GROUP}` | `{HEARS}` |\n"
            f"| `.agents/skills/a*/SKILL.md` | `## Finish` |\n"
        ))

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(1, status)
        self.assertIn("alpha", " ".join(report.get("refusals", [])) + report.get("said", ""))
        self.assertFalse(any(self.holds_block(name) for name in self.files()))

    def test_a_member_holding_the_heading_twice_is_refused_and_nothing_is_written(self) -> None:
        self.write(".agents/skills/beta/SKILL.md", speaking_skill("Beta") + f"\n{HEARS}\n\nAgain.\n")

        status, report = self.run_installer(SLUG, "--install")

        self.assertEqual(1, status)
        self.assertTrue(any("ambiguous" in refusal for refusal in report["refusals"]), report)
        self.assertFalse(self.holds_block(".agents/skills/alpha/SKILL.md"), "a refusal writes nothing")

    def test_retract_leaves_every_member_as_it_was(self) -> None:
        self.run_installer(SLUG, "--install")

        status, report = self.run_installer(SLUG, "--retract")

        self.assertEqual(0, status, report)
        self.assertEqual(self.before, {name: self.read(name) for name in self.files()})


class Checking(RepositoryCase):
    """The sweep: every rules file against its targets, every block against the rules files."""

    def setUp(self) -> None:
        super().setUp()
        self.write(RULES, rules_file())
        self.write(TARGET, TARGET_TEXT)

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


DECLARING = "sample-debugging"
DECLARING_RULES = f".agents/mechanisms/{DECLARING}/{DECLARING}.rules.md"
DECLARATION = (
    "| setting | values | default | set by |\n|---|---|---|---|\n"
    "| `debug` | `on` · `off` | `off` | a wording |\n"
)


def declaring_file(declaration: str = DECLARATION, when: str = "- **when** debug=on\n") -> str:
    """A mechanism that declares `debug` and sends the target one rule that stands always and one
    that stands while `debug` is on."""
    return (
        f"# {DECLARING} — rules installed elsewhere\n\nRead by the installer alone.\n\n"
        "| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n\n"
        f"{declaration}\n"
        "## D1 — always\n\n"
        f"- **target** `{TARGET}`\n"
        "- **authority** the user, 2026-10-23\n\n"
        "<rule>\nAlways here.\n</rule>\n\n"
        "## D2 — while debugging\n\n"
        f"- **target** `{TARGET}`\n"
        f"{when}"
        "- **authority** the user, 2026-10-23\n\n"
        "<rule>\nOnly while debugging.\n</rule>\n"
    )


def values_table(value: str | None) -> str:
    return "" if value is None else f"\n| setting | value |\n|---|---|\n| `debug` | `{value}` |\n"


def local_with_value(value: str | None) -> str:
    """The project's file: the anchor table, the values table where a value is set, one rule."""
    return local_file(
        table="| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n" + values_table(value)
    )


BLOCK_ON = f'<installed by="{DECLARING}">\n**D1** Always here.\n\n**D2** Only while debugging.\n</installed>'
BLOCK_OFF = f'<installed by="{DECLARING}">\n**D1** Always here.\n</installed>'


class TheSettings(RepositoryCase):
    """A mechanism declaring a setting, a rule conditioned on it, and the project's value."""

    def setUp(self) -> None:
        super().setUp()
        self.write(DECLARING_RULES, declaring_file())
        self.write(TARGET, TARGET_TEXT)
        self.write(LOCAL_FILE, local_with_value("on"))

    def run_installer(self, *operands: str) -> tuple[int, dict | str]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = inject_rules.main(list(operands), root=self.root)
        text = said.getvalue()
        try:
            return status, json.loads(text)
        except json.JSONDecodeError:
            return status, text

    def test_the_local_files_values_table_is_not_read_as_anchors(self) -> None:
        status, report = self.run_installer(LOCAL, "--install")

        self.assertEqual(0, status, report)
        self.assertEqual([TARGET], [one["target"] for one in report["targets"]])
        self.assertIn(LOCAL_INSTALLED, self.read(TARGET))

    def test_a_rule_whose_condition_holds_is_installed_and_one_whose_does_not_is_left_out(self) -> None:
        self.run_installer(DECLARING, "--install")
        self.assertIn(BLOCK_ON, self.read(TARGET))

        self.write(TARGET, TARGET_TEXT)
        self.write(LOCAL_FILE, local_with_value("off"))
        self.run_installer(DECLARING, "--install")
        self.assertIn(BLOCK_OFF, self.read(TARGET))

        self.write(TARGET, TARGET_TEXT)
        self.write(LOCAL_FILE, local_with_value(None))
        self.run_installer(DECLARING, "--install")
        self.assertIn(BLOCK_OFF, self.read(TARGET), "a setting the local file leaves unset stands at its default")

    def test_changing_the_value_then_running_moves_the_rule_both_ways_without_overwrite(self) -> None:
        self.run_installer("--install")
        self.assertIn(BLOCK_ON, self.read(TARGET))

        self.write(LOCAL_FILE, local_with_value("off"))
        status, report = self.run_installer("--install")

        self.assertEqual(0, status, report)
        self.assertIn(BLOCK_OFF, self.read(TARGET))
        self.assertNotIn(BLOCK_ON, self.read(TARGET))
        states = {(one["slug"], target["state"]) for one in report["sources"] for target in one["targets"]}
        self.assertIn((DECLARING, "re-rendered"), states)

        self.write(LOCAL_FILE, local_with_value("on"))
        self.run_installer("--install")
        self.assertIn(BLOCK_ON, self.read(TARGET))
        once = self.snapshot()
        self.run_installer("--install")
        self.assertEqual(once, self.snapshot(), "run twice, the second run changes nothing")

    def test_a_rule_of_several_paragraphs_moves_both_ways_without_overwrite(self) -> None:
        self.write(DECLARING_RULES, declaring_file().replace(
            "<rule>\nOnly while debugging.\n</rule>", "<rule>\nOnly while debugging.\n\n- and its list.\n</rule>"
        ))
        self.run_installer("--install")
        self.assertIn("**D2** Only while debugging.\n\n- and its list.", self.read(TARGET))

        self.write(LOCAL_FILE, local_with_value("off"))
        status, report = self.run_installer("--install")

        self.assertEqual(0, status, report)
        self.assertIn(BLOCK_OFF, self.read(TARGET), "a blank line inside a rule is not an edit")

        self.write(LOCAL_FILE, local_with_value("on"))
        status, report = self.run_installer("--install")
        self.assertEqual(0, status, report)
        self.assertIn("**D2** Only while debugging.\n\n- and its list.", self.read(TARGET))

    def test_a_target_emptied_by_its_conditions_loses_its_block_and_the_report_says_removed(self) -> None:
        self.write(DECLARING_RULES, declaring_file().replace("## D1 — always", "## D1 — also while debugging").replace(
            "- **authority** the user, 2026-10-23\n\n<rule>\nAlways here.", "- **when** debug=on\n- **authority** the user, 2026-10-23\n\n<rule>\nAlways here."
        ))
        self.run_installer(DECLARING, "--install")
        self.assertIn(f'<installed by="{DECLARING}">', self.read(TARGET))

        self.write(LOCAL_FILE, local_with_value("off"))
        status, report = self.run_installer(DECLARING, "--install")

        self.assertEqual(0, status, report)
        self.assertEqual("removed", report["targets"][0]["state"])
        self.assertEqual(TARGET_TEXT, self.read(TARGET))
        status, report = self.run_installer(DECLARING, "--install")
        self.assertEqual("not called for", report["targets"][0]["state"])

    def test_a_condition_on_an_undeclared_setting_or_value_is_refused_and_a_diagnostic(self) -> None:
        for when, said in (
            ("- **when** verbose=on\n", "verbose, which no mechanism declares"),
            ("- **when** debug=loud\n", "debug=`loud`, which is none of `on`, `off`"),
        ):
            with self.subTest(when=when):
                self.write(DECLARING_RULES, declaring_file(when=when))
                before = self.snapshot()

                status, report = self.run_installer(DECLARING, "--install")

                self.assertEqual(1, status)
                self.assertIn(said, report["refusals"][0])
                self.assertEqual(before, self.snapshot())
                _, checked = self.run_installer("--check")
                self.assertTrue(any(said in one for one in checked["diagnostics"]), checked["diagnostics"])

    def test_a_local_value_no_declaration_holds_is_refused_and_a_diagnostic(self) -> None:
        for table, said in (
            (values_table("loud"), "sets debug to `loud`"),
            ("\n| setting | value |\n|---|---|\n| `verbose` | `on` |\n", "sets verbose, which no mechanism declares"),
        ):
            with self.subTest(said=said):
                self.write(LOCAL_FILE, local_file(table="| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n" + table))

                status, report = self.run_installer("--install")

                self.assertEqual(1, status)
                self.assertIn(said, report["refusals"][0])
                _, checked = self.run_installer("--check")
                self.assertTrue(any(said in one for one in checked["diagnostics"]), checked["diagnostics"])

    def test_a_setting_declared_by_two_mechanisms_is_a_diagnostic(self) -> None:
        self.write(RULES, rules_file(table="| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n\n{DECLARATION}"))

        _, checked = self.run_installer("--check")

        self.assertTrue(any("declared by" in one and "and by" in one for one in checked["diagnostics"]), checked["diagnostics"])

    def test_the_local_file_declares_nothing_and_a_mechanism_sets_nothing(self) -> None:
        self.write(LOCAL_FILE, local_file(table="| target | anchor |\n|---|---|\n" f"| `{TARGET}` | `{ANCHOR}` |\n\n{DECLARATION}"))
        status, report = self.run_installer(LOCAL, "--install")
        self.assertEqual(1, status)
        self.assertIn("declared by the mechanism it belongs to", report["refusals"][0])

        self.write(DECLARING_RULES, declaring_file(declaration=DECLARATION + values_table("on")))
        status, report = self.run_installer(DECLARING, "--install")
        self.assertEqual(1, status)
        self.assertIn("values are the project's", report["refusals"][0])

    def test_set_writes_the_local_files_row_and_runs_the_installer(self) -> None:
        self.write(LOCAL_FILE, local_with_value(None))
        self.run_installer("--install")
        self.assertIn(BLOCK_OFF, self.read(TARGET))

        status, report = self.run_installer("--set", "debug=on")

        self.assertEqual(0, status, report)
        self.assertIn("| `debug` | `on` |", self.read(LOCAL_FILE))
        self.assertIn(BLOCK_ON, self.read(TARGET))
        self.assertIn(LOCAL_INSTALLED, self.read(TARGET), "the local file's own rule survives the write")

        status, report = self.run_installer("--set", "debug=off")
        self.assertEqual(0, status, report)
        self.assertEqual(1, self.read(LOCAL_FILE).count("| `debug` |"), "the row is rewritten, not added")
        self.assertIn(BLOCK_OFF, self.read(TARGET))

    def test_set_on_an_undeclared_name_or_value_refuses_and_writes_nothing(self) -> None:
        for said, refusal in (("debug=loud", "none of"), ("verbose=on", "no mechanism declares"), ("debug", "not `<setting>=<value>`")):
            with self.subTest(said=said):
                before = self.snapshot()

                status, report = self.run_installer("--set", said)

                self.assertEqual(1, status)
                self.assertIn(refusal, report["refusals"][0])
                self.assertEqual(before, self.snapshot())

    def test_settings_renders_the_table_and_writes_nothing(self) -> None:
        before = self.snapshot()

        status, table = self.run_installer("--settings")

        self.assertEqual(0, status)
        self.assertIn("| `debug` | `on` · `off` | `off` | `on` | a wording | sample-debugging |", table)
        self.assertEqual(before, self.snapshot())

    def test_the_checks_line_is_one_line_when_out_of_step_and_nothing_when_not(self) -> None:
        self.run_installer("--install")
        status, said = self.run_installer("--check", "--line")
        self.assertEqual((0, ""), (status, said.strip()))

        self.write(LOCAL_FILE, local_with_value("off"))
        status, said = self.run_installer("--check", "--line")

        self.assertEqual(1, status)
        self.assertEqual(1, len(said.strip().splitlines()))
        self.assertIn("out of step", said)
        self.assertIn("inject_rules.py --install", said)

    def test_a_block_edited_by_hand_still_refuses_without_overwrite(self) -> None:
        self.run_installer(DECLARING, "--install")
        self.write(TARGET, self.read(TARGET).replace("Always here.", "Always here, edited."))

        status, report = self.run_installer(DECLARING, "--install")

        self.assertEqual(1, status)
        self.assertIn("differs from the rules file", report["refusals"][0])
        _, checked = self.run_installer("--check")
        self.assertIn(f"{DECLARING} in {TARGET}: drifted", checked["diagnostics"])

    def test_the_run_installs_every_source_in_the_harnesss_order_and_stops_at_a_refusal(self) -> None:
        self.write(RULES, rules_file())

        status, report = self.run_installer("--install")

        self.assertEqual(0, status, report)
        self.assertEqual([DECLARING, SLUG, LOCAL], [one["slug"] for one in report["sources"]])
        text = self.read(TARGET)
        self.assertLess(text.index(f'<installed by="{DECLARING}">'), text.index(f'<installed by="{SLUG}">'))
        self.assertLess(text.index(f'<installed by="{SLUG}">'), text.index(f'<installed by="{LOCAL}">'))

        self.write(RULES, rules_file(sections=""))
        status, report = self.run_installer("--install")
        self.assertEqual(1, status)
        self.assertTrue(report["refusals"][0].startswith(f"{SLUG}:"), report["refusals"])
