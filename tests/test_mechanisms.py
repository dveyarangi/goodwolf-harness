"""Reading a mechanism's declaration, and saying whether it is true."""

from __future__ import annotations

import contextlib
import io
import json
import unittest

from harness import RepositoryCase

import mechanisms

SLUG = "sample-shape"
MECHANISMS = ".agents/mechanisms"
DOC = f"{MECHANISMS}/{SLUG}/{SLUG}.md"
INSTRUCTION = ".agents/skills/sample/SKILL.md"
TRIGGER = "is sample work: use"

MOMENTS = (
    "| moment | instructed by | kind, and why |\n"
    "|---|---|---|\n"
    f"| doing the thing | `{INSTRUCTION}` | |\n"
    "| sweeping afterwards | — | not yet — nobody sweeps yet, "
    "[01-0002](../../../docs/tickets/01-0002-sweep.md) |\n"
)
PARTS = (
    "| part | where |\n"
    "|---|---|\n"
    f"| instruction file | `{INSTRUCTION}` |\n"
    f'| trigger | `AGENTS.md` → "{TRIGGER}" |\n'
)
RELIED_ON = (
    "| part | where | owner |\n"
    "|---|---|---|\n"
    "| corpus reader | `.agents/scripts/docs_corpus.py` | nobody removable |\n"
)


class Declared(RepositoryCase):
    """A tree holding one well-formed mechanism, which each test bends in exactly one way."""

    def setUp(self) -> None:
        super().setUp()
        self.write(INSTRUCTION, "# Sample\n")
        self.write("AGENTS.md", f"- Doing it {TRIGGER} /sample.\n")
        self.write(".agents/scripts/docs_corpus.py", "# shared\n")
        self.write("docs/tickets/01-0002-sweep.md", "# Sweep\n")
        self.write("docs/tickets/01-0001-sample.md", "# Sample\n")
        self.write("docs/mechanisms/sample-shape.evidence.md", "# Evidence\n")
        self.write(DOC, self.doc())

    def doc(self, **replaced: str) -> str:
        """The well-formed declaration, with any one section swapped for what a test is proving."""
        written = {
            "header": (
                f"# {SLUG} — one line saying what it is\n\n"
                f"- **instruction** `{INSTRUCTION}` — the act\n"
                "- **state** always on\n"
                "<project-local>\n"
                "- **evidence** `docs/mechanisms/sample-shape.evidence.md`\n"
                "</project-local>\n"
            ),
            "moments": MOMENTS,
            "parts": PARTS,
            "relied_on": RELIED_ON,
            "produces": "## What it produces, and who reads it\n\n"
            "The declaration, read by whoever amends this. Nothing else is emitted.\n",
            "grading":"## What would show it working, graded by someone who did not build it\n\n"
            "The next mechanism declared passes unedited, or the check changes to admit it.\n",
            **replaced,
        }
        return (
            f"{written['header']}\n"
            "## How it works\n\nProse nothing parses.\n\n"
            f"## Moments\n\n{written['moments']}\n"
            f"## Install adds, uninstall removes\n\n{written['parts']}\n"
            f"## Relies on, and does not own\n\n{written['relied_on']}\n"
            f"{written['produces']}\n"
            "## Not yet at the shape\n\nThe honest gaps.\n\n"
            "## What retires this\n\nA better shape.\n\n"
            f"{written['grading']}"
        )

    def header(self, bullets: str) -> str:
        """A header bending only the bullet under test; the rest stays well-formed."""
        if "**state**" not in bullets:
            bullets += "- **state** always on\n"
        return f"# {SLUG} — one line saying what it is\n\n{bullets}"

    def checked(self):
        return mechanisms.check(self.root)

    def problems(self) -> list[str]:
        return [note.problem for note in self.checked().diagnostics]


class AWellFormedDeclaration(Declared):
    def test_is_reported_true_with_its_parts_and_its_moments(self) -> None:
        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        self.assertEqual(1, len(checked.declarations))
        declared = checked.declarations[0]
        self.assertEqual(SLUG, declared.slug)
        self.assertEqual(INSTRUCTION, declared.instruction)
        self.assertEqual("always on", declared.state)
        self.assertEqual(2, len(declared.moments))
        self.assertEqual(2, len(declared.parts))
        self.assertEqual(1, len(declared.relied_on))


class ANamedPart(Declared):
    def test_that_does_not_resolve_is_reported_by_its_path(self) -> None:
        self.write(
            DOC,
            self.doc(
                parts="| part | where |\n|---|---|\n| a script | `.agents/scripts/nowhere.py` |\n"
            ),
        )

        problems = [note.problem for note in self.checked().diagnostics]

        self.assertEqual(1, len(problems))
        self.assertIn(".agents/scripts/nowhere.py", problems[0])

    def test_whose_anchor_phrase_is_not_in_the_file_it_names_is_reported(self) -> None:
        self.write(
            DOC,
            self.doc(
                parts='| part | where |\n|---|---|\n| trigger | `AGENTS.md` → "reworded away" |\n'
            ),
        )

        problems = [note.problem for note in self.checked().diagnostics]

        self.assertEqual(1, len(problems))
        self.assertIn("reworded away", problems[0])
        self.assertIn("AGENTS.md", problems[0])


class ANotYetReferent(Declared):
    def moments_naming(self, ticket: str) -> str:
        return (
            "| moment | instructed by | kind, and why |\n|---|---|---|\n"
            f"| sweeping | — | not yet — nobody sweeps yet, [t](../../../{ticket}) |\n"
        )

    def test_may_not_be_an_archived_ticket_since_closed_work_fills_no_gap(self) -> None:
        self.write("docs/tickets/done/01-0001-sample.md", "# Sample, closed\n")
        self.write(DOC, self.doc(moments=self.moments_naming("docs/tickets/done/01-0001-sample.md")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("docs/tickets/done/01-0001-sample.md", problems[0])
        self.assertIn("archived", problems[0])

    def test_follows_the_ticket_when_a_close_moves_it_and_is_then_reported(self) -> None:
        import move_doc

        self.write(DOC, self.doc(moments=self.moments_naming("docs/tickets/01-0002-sweep.md")))
        self.commit()
        self.assertEqual([], self.problems())

        with contextlib.redirect_stdout(io.StringIO()):
            status = move_doc.main(
                ["docs/tickets/01-0002-sweep.md", "docs/tickets/done/01-0002-sweep.md"],
                self.root,
            )

        self.assertEqual(0, status)
        problems = self.problems()
        self.assertEqual(1, len(problems))
        self.assertIn("docs/tickets/done/01-0002-sweep.md", problems[0])
        self.assertIn("archived", problems[0])

    def test_reports_nothing_skipped_since_every_check_can_always_run(self) -> None:
        self.assertNotIn("skipped", self.checked().as_record())


class TheInstruction(Declared):
    def test_may_not_be_the_doc_itself(self) -> None:
        self.write(DOC, self.doc(header=self.header(f"- **instruction** `{DOC}` — the act\n")))

        problems = [note.problem for note in self.checked().diagnostics]

        self.assertEqual(1, len(problems))
        self.assertIn("the doc", problems[0])

    def test_is_required(self) -> None:
        self.write(DOC, self.doc(header=self.header("- **state** always on\n")))

        problems = [note.problem for note in self.checked().diagnostics]

        self.assertEqual(1, len(problems))
        self.assertIn("instruction", problems[0])

    def test_must_resolve(self) -> None:
        self.write(
            DOC, self.doc(header=self.header("- **instruction** `.agents/skills/gone/SKILL.md`\n"))
        )

        problems = [note.problem for note in self.checked().diagnostics]

        self.assertEqual(1, len(problems))
        self.assertIn(".agents/skills/gone/SKILL.md", problems[0])


class AMomentsRow(Declared):
    def moments(self, *rows: str) -> str:
        header = "| moment | instructed by | kind, and why |\n|---|---|---|\n"
        return header + "".join(rows)

    def test_saying_not_yet_must_name_a_ticket(self) -> None:
        self.write(
            DOC,
            self.doc(moments=self.moments("| sweeping | — | not yet — nobody sweeps yet |\n")),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("not yet", problems[0])
        self.assertIn("sweeping", problems[0])

    def test_saying_not_yet_must_name_a_ticket_that_exists(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    "| sweeping | — | not yet — nobody sweeps yet, "
                    "[01-0009](../../../docs/tickets/01-0009-absent.md) |\n"
                )
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("docs/tickets/01-0009-absent.md", problems[0])

    def test_saying_elsewhere_names_a_repo_relative_path_not_one_beside_the_doc(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    f"| archiving | — | elsewhere — `{INSTRUCTION}` owns it |\n"
                )
            ),
        )

        self.assertEqual([], self.checked().diagnostics)

    def test_saying_elsewhere_must_name_an_instruction_file_that_exists(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    "| archiving | — | elsewhere — `.agents/skills/gone/SKILL.md` owns it |\n"
                )
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn(".agents/skills/gone/SKILL.md", problems[0])

    def test_saying_embedded_names_the_body_the_instruction_sits_in(self) -> None:
        sitting_here = f"| archiving | — | embedded — another mechanism's rule, here until installed, `{INSTRUCTION}` |\n"
        self.write(DOC, self.doc(moments=self.moments(sitting_here)))
        self.assertEqual([], self.checked().diagnostics)

        sitting_nowhere = sitting_here.replace(INSTRUCTION, ".agents/skills/gone/SKILL.md")
        self.write(DOC, self.doc(moments=self.moments(sitting_nowhere)))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn(".agents/skills/gone/SKILL.md", problems[0])
        self.assertIn("does not resolve", problems[0])

    def test_takes_the_first_code_span_as_the_referent(self) -> None:
        # The format's rule: one code span per absence cell. A skill named in backticks before
        # the path is what the check resolves, and it is reported rather than skipped over.
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    f"| archiving | — | elsewhere — `/other` owns it, `{INSTRUCTION}` |\n"
                )
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("names /other", problems[0])
        self.assertIn("does not resolve", problems[0])

    def test_declaring_a_kind_outside_the_vocabulary_is_reported_as_that(self) -> None:
        self.write(
            DOC, self.doc(moments=self.moments("| sweeping | — | someday — we will get to it |\n"))
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("someday", problems[0])

    def test_declaring_a_kind_without_saying_why_is_reported(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    "| sweeping | — | not yet — "
                    "[01-0002](../../../docs/tickets/01-0002-sweep.md) |\n"
                )
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("why", problems[0])

    def test_carrying_both_an_instruction_and_an_absence_is_reported(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    f"| doing the thing | `{INSTRUCTION}` | unowned by design — nobody acts |\n"
                )
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("both", problems[0])

    def test_carrying_neither_is_reported(self) -> None:
        self.write(DOC, self.doc(moments=self.moments("| sweeping | — | |\n")))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("neither", problems[0])

    def test_saying_unowned_by_design_may_not_carry_a_referent(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments=self.moments(
                    f"| looking a path up | — | unowned by design — `{INSTRUCTION}` does it |\n"
                )
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("unowned by design", problems[0])


class TheHeader(Declared):
    def test_ends_at_the_first_section_so_prose_cannot_restate_a_bullet(self) -> None:
        hijacked = "- **instruction** `.agents/skills/hijacked/SKILL.md` — in prose\n"
        self.write(DOC, self.doc().replace("Prose nothing parses.", hijacked))

        checked = self.checked()

        self.assertEqual(INSTRUCTION, checked.declarations[0].instruction)
        self.assertEqual([], checked.diagnostics)

    def test_names_an_evidence_file_that_exists_when_it_names_one(self) -> None:
        self.write(
            DOC,
            self.doc().replace(
                "docs/mechanisms/sample-shape.evidence.md", "docs/mechanisms/never-written.md"
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("docs/mechanisms/never-written.md", problems[0])

    def test_may_name_no_evidence_at_all(self) -> None:
        self.write(DOC, self.doc(header=self.header(f"- **instruction** `{INSTRUCTION}`\n")))

        self.assertEqual([], self.checked().diagnostics)

    def test_states_one_of_the_two_states_a_mechanism_can_be_in(self) -> None:
        self.write(DOC, self.doc().replace("- **state** always on", "- **state** occasionally on"))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("occasionally on", problems[0])

    def test_accepts_installed_as_the_other_state(self) -> None:
        self.write(DOC, self.doc().replace("- **state** always on", "- **state** installed"))

        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        self.assertEqual("installed", checked.declarations[0].state)


class TheRulesFile(Declared):
    def test_is_found_by_its_name_rather_than_by_a_bullet_declaring_it(self) -> None:
        self.write(f"{MECHANISMS}/{SLUG}/{SLUG}.rules.md", "# The rules, one section each\n")

        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        self.assertEqual(f"{MECHANISMS}/{SLUG}/{SLUG}.rules.md", checked.declarations[0].rules)

    def test_is_absent_for_a_mechanism_that_injects_nothing(self) -> None:
        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        self.assertIsNone(checked.declarations[0].rules)

    def test_under_a_name_the_injector_would_never_find_is_reported(self) -> None:
        self.write(f"{MECHANISMS}/{SLUG}/rules.md", "# The rules, misfiled\n")

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("rules.md", problems[0])


class TheDoc(Declared):
    def test_is_required_by_the_directory_that_should_hold_it(self) -> None:
        (self.root / MECHANISMS / "orphan").mkdir(parents=True)

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("orphan", problems[0])

    def test_must_name_what_would_show_the_mechanism_working(self) -> None:
        self.write(DOC, self.doc(grading="## What retires this, again\n\nNothing.\n"))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("show it working", problems[0])

    def test_must_account_for_what_the_mechanism_produces(self) -> None:
        self.write(DOC, self.doc(produces=""))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("produces", problems[0])

    def test_must_carry_a_moments_table(self) -> None:
        self.write(DOC, self.doc(moments="Every moment here is instructed.\n"))

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("Moments", problems[0])

    def test_reports_a_table_that_is_missing_a_column(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments="| moment | kind, and why |\n|---|---|\n| sweeping | unowned by design — nobody acts |\n"
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("instructed by", problems[0])

    def test_reports_a_row_whose_cells_do_not_match_the_header(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments="| moment | instructed by | kind, and why |\n|---|---|---|\n"
                "| sweeping | — |\n"
            ),
        )

        problems = self.problems()

        self.assertEqual(1, len(problems))
        self.assertIn("2", problems[0])
        self.assertIn("3", problems[0])

    def test_reads_an_escaped_pipe_as_part_of_a_cell_not_as_a_column(self) -> None:
        self.write(
            DOC,
            self.doc(
                moments="| moment | instructed by | kind, and why |\n|---|---|---|\n"
                f"| choosing install \\| retract | `{INSTRUCTION}` | |\n"
            ),
        )

        checked = self.checked()

        self.assertEqual([], checked.diagnostics)
        self.assertEqual("choosing install | retract", checked.declarations[0].moments[0].occasion)


class TheCommandLine(Declared):
    def run_check(self, *operands: str) -> tuple[int, str]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = mechanisms.main(list(operands), root=self.root)
        return status, said.getvalue()

    def test_refuses_a_bare_invocation_rather_than_choosing_a_mode(self) -> None:
        status, said = self.run_check()

        self.assertEqual(2, status)
        self.assertIn("--check", said)
        self.assertIn("--index", said)
        self.assertNotIn(SLUG, said)

    def test_refuses_a_scope_operand_it_has_no_use_for(self) -> None:
        status, said = self.run_check("--check", "docs")

        self.assertEqual(2, status)
        self.assertIn("--check", said)

    def test_reports_a_true_declaration_as_clean(self) -> None:
        status, said = self.run_check("--check")

        self.assertEqual(0, status)
        reported = json.loads(said)
        self.assertEqual([], reported["diagnostics"])
        self.assertEqual(SLUG, reported["declarations"][0]["mechanism"])

    def test_reports_a_false_declaration_with_a_non_zero_status(self) -> None:
        self.write(
            DOC, self.doc(parts="| part | where |\n|---|---|\n| a script | `.agents/gone.py` |\n")
        )

        status, said = self.run_check("--check")

        self.assertEqual(1, status)
        self.assertIn(".agents/gone.py", json.loads(said)["diagnostics"][0]["problem"])


class TheIndex(Declared):
    def rendered(self) -> str:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            mechanisms.main(["--index"], root=self.root)
        return said.getvalue()

    def test_has_one_row_for_each_directory_and_no_others(self) -> None:
        second = f"{MECHANISMS}/paired-close/paired-close.md"
        self.write(second, "# paired-close — a ticket and its RFC close together\n")

        rendered = self.rendered()

        rows = [line for line in rendered.splitlines() if line.startswith("| ")]
        self.assertEqual(3, len(rows))  # header plus one row per directory
        self.assertIn(SLUG, rendered)
        self.assertIn("paired-close", rendered)

    def test_shows_an_edit_to_a_doc_on_the_next_render(self) -> None:
        before = self.rendered()
        self.write(DOC, self.doc().replace("one line saying what it is", "reworded outright"))

        after = self.rendered()

        self.assertIn("one line saying what it is", before)
        self.assertIn("reworded outright", after)

    def test_is_rendered_without_writing_it_or_reading_a_committed_copy(self) -> None:
        self.write(f"{MECHANISMS}/README.md", "| mechanism |\n|---|\n| a stale copy |\n")
        self.commit()
        untouched = self.snapshot()

        rendered = self.rendered()

        self.assertNotIn("a stale copy", rendered)
        self.assertEqual(untouched, self.snapshot())

    def test_reports_a_doc_it_cannot_read_rather_than_dropping_the_row(self) -> None:
        self.write(f"{MECHANISMS}/unreadable/unreadable.md", "no heading, no bullets\n")

        rendered = self.rendered()

        self.assertIn("unreadable", rendered)
        rows = [line for line in rendered.splitlines() if line.startswith("| ")]
        self.assertEqual(3, len(rows))


if __name__ == "__main__":
    unittest.main()

