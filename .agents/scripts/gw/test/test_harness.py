"""Placing a ref of the repository into a tree that is not its own, updating it, and checking it."""

from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from repository import SCRIPTS, RepositoryCase

import harness

KEEPER = ".agents/skills/keeper/SKILL.md"
HARNESS_SKILL = ".agents/skills/harness/SKILL.md"
TICKET_SKILL = ".agents/skills/ticket/SKILL.md"
QUEUE_ARRIVAL = ".agents/skills/ticket/QUEUE-ARRIVAL.md"
DELIVERY_STATUS = "docs/tickets/README.md"
TICKET_SKILL_TEXT = (
    "---\nname: ticket\ndescription: mints tickets\n---\n\n"
    "Mechanism: unowned by design — this fixture's core declares only sample\n\n"
    "Mint them.\n"
)
QUEUE_ARRIVAL_TEXT = (
    "# What the queue says before anything has happened in it\n\n"
    "Machine input for the install, read by nobody at session time.\n\n"
    "```delivery-status\n# Delivery status\n\nCore arrived at `{ref}` and nothing is in flight.\n```\n"
)
HARNESS_SKILL_TEXT = (
    "---\nname: harness\ndescription: places core\n---\n\n"
    "Mechanism: unowned by design — this fixture's core declares only sample\n\n"
    "Repository: https://github.com/example/placed-by-the-fixture.git\n\n"
    "The claim line comes first because the shape check reads the body's first line; the\n"
    "repository line sits below it, which is what core's own harness skill does.\n"
)
DOC = ".agents/mechanisms/sample/sample.md"
TICKET = "docs/tickets/01-0002-sweep.md"
WRAPPED_RULE = "Run the sweep first in every session."
ENTRY = (
    "# Entry contract\n\n"
    "Entry contract: v3, 2026-09-01.\n\n"
    "Open your first reply with the line above.\n\n"
    f'<straw-dog until="the sweep is a mechanism" ticket="{TICKET}">\n'
    f"{WRAPPED_RULE}\n"
    "</straw-dog>\n\n"
    "## Project-local\n\n"
    '<installed by="local">\n'
    "**L1** The origin's own answer, which must not travel.\n"
    "</installed>\n\n"
    "- Doing it is sample work: use /keeper.\n"
)
SAMPLE_DOC = (
    "# sample — one line saying what it is\n\n"
    f"- **instruction** `{KEEPER}` — the act\n"
    "- **state** installed\n\n"
    "## How it works\n\nProse nothing parses.\n\n"
    "## Moments\n\n"
    "| moment | instructed by | kind, and why |\n|---|---|---|\n"
    f"| keeping | `{KEEPER}` | |\n"
    f'| sweeping | — | <straw-dog until="somebody sweeps" ticket="{TICKET}">not yet</straw-dog> |\n\n'
    "## Install adds, uninstall removes\n\n"
    f"| part | where |\n|---|---|\n| instruction file | `{KEEPER}` |\n\n"
    "## Relies on, and does not own\n\n"
    "| part | where | owner |\n|---|---|---|\n| corpus reader | `.agents/scripts/gw/docs_corpus.py` | nobody removable |\n\n"
    "## What it produces, and who reads it\n\nThe declaration, read by whoever amends this.\n\n"
    "## Not yet at the shape\n\nThe honest gaps.\n\n"
    "## What retires this\n\nA better shape.\n\n"
    "## What would show it working, graded by someone who did not build it\n\n"
    "The next mechanism declared passes unedited.\n"
)
ARRIVAL_TEST = (
    "import unittest\n\n\n"
    "class Arrival(unittest.TestCase):\n"
    "    def test_the_scripts_arrived(self):\n"
    "        self.assertTrue(True)\n"
)


def platform_makes_symlinks() -> bool:
    """Whether this machine lets a process create a directory symlink; the platform's answer is
    read from a run, never assumed, so the case proves whichever path the machine takes."""
    with tempfile.TemporaryDirectory() as workspace:
        real = Path(workspace) / "real"
        real.mkdir()
        try:
            os.symlink("real", Path(workspace) / "link", target_is_directory=True)
        except OSError:
            return False
        return True


class TwoTrees(RepositoryCase):
    """A source repository holding a small core with the live scripts, and a target beside it."""

    def setUp(self) -> None:
        super().setUp()
        self.source = self.root
        self.seed_source()
        self.target = self.another_repository()

    def seed_source(self) -> None:
        self.write(KEEPER, "---\nname: keeper\ndescription: keeps\n---\n\n# Keeper\n\nKeep things.\n")
        self.write(HARNESS_SKILL, HARNESS_SKILL_TEXT)
        self.write(TICKET_SKILL, TICKET_SKILL_TEXT)
        self.write(QUEUE_ARRIVAL, QUEUE_ARRIVAL_TEXT)
        self.write(DOC, SAMPLE_DOC)
        self.write("AGENTS.md", ENTRY)
        self.write("CLAUDE.md", "@AGENTS.md\n")
        self.write(".agents/README.md", "# Installed harness\n\nSkills live under `skills/`.\n")
        self.write(".agents/glossary.md", "# The development method\n\n**Recipient**: a tree that received core.\n")
        for script in SCRIPTS.glob("*.py"):
            self.write(f".agents/scripts/gw/{script.name}", script.read_text(encoding="utf-8"))
        self.write(".agents/scripts/gw/test/test_arrival.py", ARRIVAL_TEST)
        self.write(TICKET, "# Sweep\n")
        self.write("README.md", "# The repository's front page, never shipped\n")
        self.write("local.rules.md", "# local — never shipped\n")
        self.commit("core")

    def run_harness(self, *operands: str) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), *operands, "--from", str(self.source)])
        return status, json.loads(said.getvalue())

    def target_text(self, name: str) -> str:
        with (self.target / name).open(encoding="utf-8", newline="") as handle:
            return handle.read()

    def target_snapshot(self) -> dict[str, bytes]:
        files = {
            path.relative_to(self.target).as_posix(): path.read_bytes()
            for path in sorted(self.target.rglob("*"))
            if path.is_file() and ".git" not in path.relative_to(self.target).parts
        }
        index = subprocess.run(
            ["git", "ls-files", "--stage"], cwd=self.target, capture_output=True, encoding="utf-8", check=True
        ).stdout
        return {**files, "<index>": index.encode()}

    def short_head(self) -> str:
        return self.git("rev-parse", "--short", "HEAD").strip()


# --- the pure parts -----------------------------------------------------------------------------


class TheShear(unittest.TestCase):
    def test_a_block_wrapper_leaves_with_its_lines_and_the_rule_stays(self) -> None:
        text = "# A\n\n<straw-dog until=\"x\" ticket=\"docs/tickets/t.md\">\nThe rule.\n</straw-dog>\n\n## B\n"

        self.assertEqual("# A\n\nThe rule.\n\n## B\n", harness.sheared("a.md", text))

    def test_an_inline_wrapper_in_a_table_cell_leaves_the_row_a_row(self) -> None:
        text = '| sweeping | — | <straw-dog until="x" ticket="docs/tickets/t.md">not yet</straw-dog> |\n'

        self.assertEqual("| sweeping | — | not yet |\n", harness.sheared("a.md", text))

    def test_nested_wrappers_all_leave_and_the_content_is_joined_as_written(self) -> None:
        text = (
            '<straw-dog until="outer" ticket="docs/tickets/t.md">\n'
            'Outer says <straw-dog until="inner" ticket="docs/tickets/u.md">inner</straw-dog> too.\n'
            "</straw-dog>\n"
        )

        self.assertEqual("Outer says inner too.\n", harness.sheared("a.md", text))

    def test_a_wrapper_drawn_in_a_fence_or_a_code_span_is_left_alone(self) -> None:
        text = (
            "Write `<straw-dog until=\"c\" ticket=\"p\">` around it.\n\n"
            "```md\n<straw-dog until=\"x\" ticket=\"y\">rule</straw-dog>\n```\n"
        )

        self.assertEqual(text, harness.sheared("a.md", text))

    def test_sheared_text_sheared_again_is_unchanged(self) -> None:
        once = harness.sheared("a.md", '<straw-dog until="x" ticket="docs/tickets/t.md">\nRule.\n</straw-dog>\n')

        self.assertEqual(once, harness.sheared("a.md", once))

    def test_an_unbalanced_wrapper_refuses_naming_the_file(self) -> None:
        with self.assertRaises(harness.Refused) as refused:
            harness.sheared("a.md", '<straw-dog until="x" ticket="docs/tickets/t.md">\nRule.\n')

        self.assertIn("a.md", str(refused.exception))
        self.assertIn("never closes", str(refused.exception))

    def test_a_todo_loses_its_binding_and_keeps_its_words(self) -> None:
        code = "x = 1\n# TODO docs/tickets/01-0002-sweep.md: the shear strips\n# this on install.\n"

        self.assertEqual("x = 1\n# TODO: the shear strips\n# this on install.\n", harness.todo_bindings_sheared(code))

    def test_a_todo_naming_no_ticket_is_untouched(self) -> None:
        code = "# TODO: split this.\n"

        self.assertEqual(code, harness.todo_bindings_sheared(code))


class TheLocalBlockStrip(unittest.TestCase):
    def test_the_block_and_the_newline_the_installer_added_leave_and_the_rest_is_byte_identical(self) -> None:
        around = "## Project-local\n\n<installed by=\"shape\">\n**R7** Core's.\n</installed>\n"
        text = around + '\n<installed by="local">\n**L1** Ours.\n</installed>\n' + "\n## Straw dogs\n"

        self.assertEqual(around + "\n## Straw dogs\n", harness.without_local_blocks("AGENTS.md", text))

    def test_a_file_with_no_local_block_passes_unchanged(self) -> None:
        self.assertEqual("# A\n", harness.without_local_blocks("a.md", "# A\n"))


class TheStamp(unittest.TestCase):
    def test_the_announce_line_names_the_repository_and_the_ref_and_keeps_the_lines_ending(self) -> None:
        ref = harness.Ref("goodwolf-harness", "abc" * 13 + "d", "abc1234", "2026-09-20")
        text = "# Entry contract\r\n\r\nEntry contract: v13, 2026-09-20.\r\n\r\nOpen with it.\r\n"

        self.assertEqual(
            "# Entry contract\r\n\r\nEntry contract: goodwolf-harness@abc1234, 2026-09-20.\r\n\r\nOpen with it.\r\n",
            harness.stamped(text, ref),
        )

    def test_an_entry_file_with_no_announce_line_refuses(self) -> None:
        ref = harness.Ref("goodwolf-harness", "a" * 40, "aaaaaaa", "2026-09-20")

        with self.assertRaises(harness.Refused) as refused:
            harness.stamped("# Something else\n", ref)

        self.assertIn("not the harness", str(refused.exception))


class TheRepositoryLine(unittest.TestCase):
    """The line naming where core comes from: read as a default, stamped, and set aside."""

    def test_the_default_is_the_line_this_tree_authors(self) -> None:
        skill = SCRIPTS.parents[1] / "skills/harness/SKILL.md"
        authored = harness.REPOSITORY.search(skill.read_text(encoding="utf-8"))

        self.assertIsNotNone(authored, "core's own harness skill must author the line")
        self.assertEqual(authored.group("url"), harness.home())

    def test_the_stamp_replaces_the_url_and_keeps_the_lines_ending(self) -> None:
        ref = harness.Ref("goodwolf-harness", "a" * 40, "aaaaaaa", "2026-09-20")
        text = "---\nname: harness\n---\r\n\r\nRepository: https://example.invalid/old.git\r\n\r\nProse.\r\n"

        self.assertEqual(
            "---\nname: harness\n---\r\n\r\nRepository: https://example.invalid/new.git\r\n\r\nProse.\r\n",
            harness.repository_stamped(text, ref, "https://example.invalid/new.git"),
        )

    def test_a_skill_with_no_line_is_not_the_harness(self) -> None:
        ref = harness.Ref("goodwolf-harness", "a" * 40, "aaaaaaa", "2026-09-20")

        with self.assertRaises(harness.Refused) as refused:
            harness.repository_stamped("---\nname: harness\n---\n\nProse.\n", ref, "https://example.invalid/x.git")

        self.assertIn("not the harness", str(refused.exception))

    def test_the_line_leaves_with_its_newline_and_only_from_the_harness_skill(self) -> None:
        text = "A\n\nRepository: https://example.invalid/x.git\n\nB\n"

        self.assertEqual("A\n\n\nB\n", harness.without_repository_line(HARNESS_SKILL, text))
        self.assertEqual(text, harness.without_repository_line(KEEPER, text))

    def test_a_line_with_anything_after_the_url_is_not_the_line(self) -> None:
        self.assertIsNone(harness.REPOSITORY.search("Repository: https://example.invalid/x.git and more\n"))

    def test_a_url_is_told_verbatim_and_a_path_absolutely(self) -> None:
        self.assertEqual(
            "https://github.com/x/y.git", harness.resolved("https://github.com/x/y.git")
        )
        self.assertEqual(Path(".").resolve().as_posix(), harness.resolved("."))


class TheSource(TwoTrees):
    def test_the_manifest_at_a_ref_is_core_plus_the_two_root_files_and_nothing_else(self) -> None:
        with harness.Source(str(self.source)) as source:
            ref = source.resolve("HEAD")
            manifest = list(source.files(ref))

        self.assertIn("AGENTS.md", manifest)
        self.assertIn("CLAUDE.md", manifest)
        self.assertIn(KEEPER, manifest)
        self.assertIn(".agents/scripts/gw/test/test_arrival.py", manifest)
        self.assertNotIn("README.md", manifest)
        self.assertNotIn("local.rules.md", manifest)
        self.assertNotIn(TICKET, manifest)

    def test_a_tagged_commit_is_announced_by_its_tag_and_an_untagged_one_by_its_short_commit(self) -> None:
        with harness.Source(str(self.source)) as source:
            untagged = source.resolve("HEAD")
        self.git("tag", "v1")
        with harness.Source(str(self.source)) as source:
            tagged = source.resolve("HEAD")

        self.assertEqual(self.short_head(), untagged.announced)
        self.assertEqual("v1", tagged.announced)
        self.assertEqual(self.source.name, tagged.repository)
        self.assertEqual("Entry contract: " + self.source.name + "@v1, " + tagged.date + ".", tagged.stamp)

    def test_a_ref_that_does_not_resolve_refuses_naming_both(self) -> None:
        with harness.Source(str(self.source)) as source, self.assertRaises(harness.Refused) as refused:
            source.resolve("no-such-ref")

        self.assertIn("no-such-ref", str(refused.exception))
        self.assertIn(str(self.source), str(refused.exception))

    def test_the_repository_name_is_the_last_segment_without_dot_git(self) -> None:
        self.assertEqual("goodwolf-harness", harness.repository_name("https://github.com/x/goodwolf-harness.git"))
        self.assertEqual("agents", harness.repository_name("D:\\Dev\\AI\\agents\\"))


# --- refusals ------------------------------------------------------------------------------------


class ARefusal(TwoTrees):
    """Each writes nothing, and names its step."""

    def assert_refused(self, operands: tuple[str, ...], *said: str) -> None:
        before = self.target_snapshot()

        status, report = self.run_harness(*operands)

        self.assertEqual(1, status)
        self.assertEqual(1, len(report["refusals"]), report)
        for word in said:
            self.assertIn(word, report["refusals"][0])
        self.assertEqual(before, self.target_snapshot())

    def test_a_target_that_is_not_a_work_tree_root(self) -> None:
        inside = self.target / "inside"
        inside.mkdir()
        self.target = inside

        self.assert_refused(("--install",), "target:", "top level")

    def test_the_source_itself_by_its_remote(self) -> None:
        subprocess.run(["git", "remote", "add", "origin", str(self.source)], cwd=self.target, check=True)

        self.assert_refused(("--install",), "target:", "the source itself")

    def test_install_over_a_present_manifest_path(self) -> None:
        for present in ("AGENTS.md", "CLAUDE.md", KEEPER):
            with self.subTest(present=present):
                shutil.rmtree(self.target / ".agents", ignore_errors=True)
                for stale in ("AGENTS.md", "CLAUDE.md"):
                    (self.target / stale).unlink(missing_ok=True)
                (self.target / present).parent.mkdir(parents=True, exist_ok=True)
                (self.target / present).write_text("theirs\n", encoding="utf-8")

                self.assert_refused(("--install",), "install:", present, "--update")

    def test_update_without_core(self) -> None:
        self.assert_refused(("--update",), "update:", "--install")

    def test_update_over_an_entry_file_holding_a_retired_tag(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n<project-local>\ntheirs\n</project-local>\n", encoding="utf-8")

        self.assert_refused(("--update",), "update:", "<project-local>", "local.rules.md")

    def test_update_over_an_edited_core_file_without_overwrite(self) -> None:
        self.run_harness("--install")
        (self.target / KEEPER).write_text("# Keeper, edited by hand\n", encoding="utf-8")

        self.assert_refused(("--update",), "update:", KEEPER, "--overwrite")

    def test_update_when_the_tree_announces_no_ref_without_overwrite(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"{self.source.name}@", "v"), encoding="utf-8")

        self.assert_refused(("--update",), "update:", "no ref", "--overwrite")

    def test_a_tree_announcing_another_repository(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"{self.source.name}@", "other@"), encoding="utf-8")

        self.assert_refused(("--check",), "announces other", self.source.name)

    def test_a_ref_that_does_not_resolve(self) -> None:
        self.assert_refused(("--install", "--at", "nowhere"), "ref:", "nowhere")

    def test_a_docs_link_inside_a_straw_dog_at_the_ref_cannot_ship(self) -> None:
        self.write(
            KEEPER,
            "# Keeper\n\n"
            f'<straw-dog until="x" ticket="{TICKET}">\nSee [the sweep](../../../{TICKET}).\n</straw-dog>\n',
        )
        self.commit("a leak")

        self.assert_refused(("--install",), "ship:", KEEPER, TICKET)

    def test_a_check_of_a_tree_that_is_not_a_recipient(self) -> None:
        self.assert_refused(("--check",), "check:", "not a recipient")

    @unittest.skipUnless(os.name == "nt", "a junction is a Windows object")
    def test_a_junction_where_a_link_goes(self) -> None:
        (self.target / ".agents" / "skills").mkdir(parents=True)
        (self.target / ".claude").mkdir()
        made = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(self.target / ".claude" / "skills"), str(self.target / ".agents" / "skills")],
            capture_output=True,
        )
        self.assertEqual(0, made.returncode, made.stderr)
        shutil.rmtree(self.target / ".agents")

        self.assert_refused(("--install",), "link:", ".claude/skills", "junction")

    def test_a_directory_of_the_recipients_own_where_a_link_goes(self) -> None:
        (self.target / ".cursor" / "skills").mkdir(parents=True)

        self.assert_refused(("--install",), "link:", ".cursor/skills", "recipient's own")


# --- install -------------------------------------------------------------------------------------


class AnInstall(TwoTrees):
    def test_lands_the_manifest_transformed_and_nothing_outside_it(self) -> None:
        status, report = self.run_harness("--install")

        self.assertTrue((self.target / KEEPER).is_file())
        self.assertTrue((self.target / ".agents/scripts/gw/harness.py").is_file())
        self.assertFalse((self.target / "README.md").exists())
        self.assertFalse((self.target / "local.rules.md").exists())
        self.assertFalse((self.target / TICKET).exists())
        entry = self.target_text("AGENTS.md")
        self.assertIn(f"Entry contract: {self.source.name}@{self.short_head()}, ", entry)
        self.assertIn(WRAPPED_RULE, entry)
        self.assertNotIn("<straw-dog", entry)
        self.assertNotIn('<installed by="local">', entry)
        self.assertEqual("| sweeping | — | not yet |", next(
            line for line in self.target_text(DOC).splitlines() if line.startswith("| sweeping")
        ))
        for name in report["written"]:
            if name.endswith(".md"):
                self.assertNotIn("<straw-dog", self.target_text(name), name)
        self.assertEqual("@AGENTS.md\n", self.target_text("CLAUDE.md"))

    def test_arrives_on_three_gates_and_reports_the_links_made_or_pending_with_the_command(self) -> None:
        status, report = self.run_harness("--install")

        self.assertEqual(["ref", "injector", "shape"], list(report["gates"]))
        for name, gate in report["gates"].items():
            self.assertTrue(gate["passed"], (name, gate))
        self.assertTrue(report["arrived"])
        self.assertEqual(0, status)
        if platform_makes_symlinks():
            self.assertEqual(["made", "made"], [link["state"] for link in report["links"]])
            self.assertEqual({".claude/skills": True, ".cursor/skills": True}, report["links_resolve"])
        else:
            self.assertEqual(["pending", "pending"], [link["state"] for link in report["links"]])
            self.assertEqual(2, len(report["pending"]))
            self.assertIn(str(self.target / ".claude" / "skills"), report["pending"][0])
            self.assertIn("mklink /D" if os.name == "nt" else "ln -s", report["pending"][0])
            self.assertEqual({".claude/skills": False, ".cursor/skills": False}, report["links_resolve"])
        self.assertFalse(any("__pycache__" in path.parts for path in self.target.rglob("*")))

    def test_the_shipped_suite_is_not_run_by_the_gate(self) -> None:
        self.write(".agents/scripts/gw/test/test_arrival.py", ARRIVAL_TEST.replace("assertTrue(True)", "assertTrue(False)"))
        self.commit("a broken suite")

        status, report = self.run_harness("--install")

        self.assertNotIn("suite", report["gates"])
        self.assertTrue(report["arrived"])

    def test_a_shape_diagnostic_in_the_recipient_leaves_arrival_false_naming_the_gate(self) -> None:
        self.write(".agents/skills/silent/SKILL.md", "# Silent\n\nNamed by nothing, claiming nothing.\n")
        self.commit("a silent skill")

        status, report = self.run_harness("--install")

        self.assertFalse(report["gates"]["shape"]["passed"])
        self.assertFalse(report["arrived"])
        self.assertEqual(1, status)

    def test_a_file_edited_after_install_is_named_by_the_check(self) -> None:
        self.run_harness("--install")
        (self.target / KEEPER).write_text("# Keeper, edited\n", encoding="utf-8")

        status, report = self.run_harness("--check")

        self.assertEqual([KEEPER], report["gates"]["ref"]["differs"])
        self.assertFalse(report["arrived"])

    def test_a_crlf_copy_of_a_shipped_file_is_not_an_edit(self) -> None:
        self.run_harness("--install")
        copy = self.target / KEEPER
        copy.write_bytes(copy.read_bytes().replace(b"\n", b"\r\n"))

        status, report = self.run_harness("--check")

        self.assertEqual([], report["gates"]["ref"]["differs"])


# --- update --------------------------------------------------------------------------------------


class AnUpdate(TwoTrees):
    def setUp(self) -> None:
        super().setUp()
        self.run_harness("--install")
        self.write_target(
            "local.rules.md",
            "# local — this project's rules\n\n| target | anchor |\n|---|---|\n| `AGENTS.md` | `## Project-local` |\n\n"
            "## L1 — ours\n\n- **target** `AGENTS.md`\n- **authority** the user, 2026-09-21\n\n<rule>\nOur answer.\n</rule>\n",
        )
        self.local_before = (self.target / "local.rules.md").read_bytes()

    def write_target(self, name: str, text: str) -> None:
        path = self.target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(text)

    def test_leaves_the_local_file_byte_identical_and_restores_its_block_last(self) -> None:
        self.write(KEEPER, "# Keeper\n\nKeep more things.\n")
        self.commit("core moved")

        status, report = self.run_harness("--update")

        self.assertEqual(self.local_before, (self.target / "local.rules.md").read_bytes())
        self.assertIn("Keep more things.", self.target_text(KEEPER))
        entry = self.target_text("AGENTS.md")
        self.assertIn('<installed by="local">\n**L1** Our answer.\n</installed>', entry)
        self.assertGreater(entry.index('<installed by="local">'), entry.index("## Project-local"))
        self.assertIn(f"@{self.short_head()}, ", entry)
        self.assertTrue(report["gates"]["ref"]["passed"], report["gates"]["ref"])
        self.assertTrue(report["gates"]["injector"]["passed"], report["gates"]["injector"])

    def test_deletes_what_left_the_manifest_when_the_line_announces_a_ref(self) -> None:
        self.git("rm", "-q", ".agents/glossary.md")
        self.commit("the glossary leaves")

        status, report = self.run_harness("--update")

        self.assertEqual([".agents/glossary.md"], report["deleted"])
        self.assertFalse((self.target / ".agents/glossary.md").exists())

    def test_reports_the_recipients_own_files_under_core_and_leaves_them(self) -> None:
        self.write_target(".agents/skills/theirs/SKILL.md", "Mechanism: unowned by design — theirs\n\n# Theirs\n")

        status, report = self.run_harness("--update")

        self.assertEqual([".agents/skills/theirs/SKILL.md"], report["own"])
        self.assertTrue((self.target / ".agents/skills/theirs/SKILL.md").is_file())

    def test_with_no_announced_ref_overwrite_replaces_every_core_file_and_deletes_nothing(self) -> None:
        entry = self.target / "AGENTS.md"
        entry.write_text(entry.read_text(encoding="utf-8").replace(f"{self.source.name}@", "v"), encoding="utf-8")
        self.write_target(".agents/stale.md", "left over from a hand install\n")
        self.git("rm", "-q", ".agents/glossary.md")
        self.commit("the glossary leaves")

        status, report = self.run_harness("--update", "--overwrite")

        self.assertEqual([], report["deleted"])
        self.assertTrue((self.target / ".agents/glossary.md").exists())
        self.assertIn(".agents/stale.md", report["own"])
        self.assertIn(f"@{self.short_head()}, ", self.target_text("AGENTS.md"))

    def test_overwrite_replaces_an_edited_core_file_and_names_it(self) -> None:
        (self.target / KEEPER).write_text("# Keeper, edited\n", encoding="utf-8")

        status, report = self.run_harness("--update", "--overwrite")

        self.assertEqual([KEEPER], report["replaced"])
        self.assertIn("Keep things.", self.target_text(KEEPER))

    def test_a_link_that_resolves_is_left_alone(self) -> None:
        if not platform_makes_symlinks():
            self.skipTest("this platform refuses to create a symlink; a kept link cannot be made")

        status, report = self.run_harness("--update")

        self.assertEqual(["kept", "kept"], [link["state"] for link in report["links"]])

    def test_an_injector_refusal_is_unfinished_and_names_the_resume(self) -> None:
        self.write_target(
            "local.rules.md",
            "# local\n\n| target | anchor |\n|---|---|\n| `AGENTS.md` | `## Project-local` |\n\n"
            "## L1 — ours\n\n- **target** `AGENTS.md`\n- **overrides** `sample/P9`\n"
            "- **authority** the user, 2026-09-21\n\n<rule>\nOur answer.\n</rule>\n",
        )

        status, report = self.run_harness("--update")

        self.assertEqual(1, status)
        self.assertIn("inject:", report["refusals"][0])
        self.assertIn("L1 overrides sample/P9", report["refusals"][0])
        self.assertIn("harness.py . --check", report["refusals"][0])
        self.assertIn("Keep things.", self.target_text(KEEPER))


class AnUpdateAcrossTheScriptsMove(TwoTrees):
    """A recipient holding core from before the scripts moved under `gw/` takes the ref after."""

    def test_the_old_paths_leave_as_what_left_the_manifest_and_the_gate_runs_at_the_new_path(self) -> None:
        old_paths = sorted(f".agents/scripts/{script.name}" for script in SCRIPTS.glob("*.py"))
        old_paths.append(".agents/scripts/test/test_arrival.py")
        self.git("mv", ".agents/scripts/gw/test", ".agents/scripts/test")
        for script in SCRIPTS.glob("*.py"):
            self.git("mv", f".agents/scripts/gw/{script.name}", f".agents/scripts/{script.name}")
        self.commit("before the move")
        before_the_move = self.short_head()
        self.git("mv", ".agents/scripts/test", ".agents/scripts/gw/test")
        for script in SCRIPTS.glob("*.py"):
            self.git("mv", f".agents/scripts/{script.name}", f".agents/scripts/gw/{script.name}")
        self.commit("the move")

        installed, report = self.run_harness("--install", "--at", before_the_move)
        self.assertEqual(1, installed, report)
        self.assertFalse(report["gates"]["injector"]["passed"], "the gate looks under gw/, which the old ref lacks")
        self.assertTrue((self.target / ".agents/scripts/harness.py").is_file())

        updated, report = self.run_harness("--update")

        self.assertEqual(0, updated, report)
        self.assertEqual(sorted(old_paths), sorted(report["deleted"]))
        self.assertFalse((self.target / ".agents/scripts/harness.py").exists())
        self.assertFalse((self.target / ".agents/scripts/test").exists())
        self.assertTrue((self.target / ".agents/scripts/gw/harness.py").is_file())
        self.assertTrue(report["arrived"], report["gates"])


# --- where core came from -------------------------------------------------------------------------


class TheSourceARecipientHolds(TwoTrees):
    """The stamped line, what it survives, and what a recipient can do with no `--from`."""

    def stamped_line(self) -> str:
        found = harness.REPOSITORY.search(self.target_text(HARNESS_SKILL))
        self.assertIsNotNone(found, "the recipient's harness skill must carry the line")
        return found.group("url")

    def test_a_path_from_is_stamped_resolved_so_it_does_not_depend_on_where_anyone_stood(self) -> None:
        said = io.StringIO()
        with contextlib.chdir(self.source.parent), contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--install", "--from", self.source.name])

        self.assertEqual(0, status, said.getvalue())
        self.assertEqual(self.source.resolve().as_posix(), self.stamped_line())

    def test_a_url_from_is_stamped_verbatim(self) -> None:
        # A `file://` URL is a real URL git can clone and a path that does not exist as one, so
        # the stamp is exercised end to end without reaching the network.
        url = self.source.resolve().as_uri()

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--install", "--from", url])

        self.assertEqual(0, status, said.getvalue())
        self.assertEqual(url, self.stamped_line())

    def test_an_update_from_another_source_replaces_nothing_in_core(self) -> None:
        self.run_harness("--install")
        beside = self.another_repository() / self.source.name
        subprocess.run(["git", "clone", "--quiet", str(self.source), str(beside)], check=True)

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--update", "--from", str(beside)])
        report = json.loads(said.getvalue())

        self.assertEqual([], report["refusals"])
        self.assertEqual([], report["replaced"])
        self.assertEqual(0, status, report["gates"])
        self.assertEqual(beside.resolve().as_posix(), self.stamped_line())

    def test_a_script_whose_skill_lost_the_line_refuses_naming_the_file_and_the_flag(self) -> None:
        self.run_harness("--install")
        skill = self.target / HARNESS_SKILL
        skill.write_text(
            harness.without_repository_line(HARNESS_SKILL, skill.read_text(encoding="utf-8")), encoding="utf-8"
        )

        done = subprocess.run(
            [sys.executable, str(self.target / ".agents/scripts/gw/harness.py"), str(self.target), "--check"],
            capture_output=True,
            encoding="utf-8",
        )
        refusal = json.loads(done.stdout)["refusals"][0]

        self.assertIn(HARNESS_SKILL, refusal)
        self.assertIn("--from", refusal)
        self.assertIn("no Repository line", refusal)

    def test_a_ref_whose_harness_skill_has_no_line_is_refused_and_nothing_is_written(self) -> None:
        self.write(HARNESS_SKILL, "---\nname: harness\ndescription: places core\n---\n\nNo line here.\n")
        self.commit("the line goes")
        before = self.target_snapshot()

        status, report = self.run_harness("--install")

        self.assertEqual(1, status)
        self.assertIn("not the harness", report["refusals"][0])
        self.assertEqual(before, self.target_snapshot())

    def test_a_check_from_another_source_reads_no_edit_in_core_but_still_sees_a_real_one(self) -> None:
        self.run_harness("--install")
        # The same repository by name, at another path: the announce line still agrees, so what is
        # under test is the skill's line alone and not the name comparison beside it.
        beside = self.another_repository() / self.source.name
        subprocess.run(["git", "clone", "--quiet", str(self.source), str(beside)], check=True)

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            harness.main([str(self.target), "--check", "--from", str(beside)])
        from_elsewhere = json.loads(said.getvalue())
        self.assertEqual([], from_elsewhere["refusals"])

        self.assertNotIn(HARNESS_SKILL, from_elsewhere["gates"]["ref"]["differs"])

        skill = self.target / HARNESS_SKILL
        skill.write_text(skill.read_text(encoding="utf-8") + "\nAn edit in core.\n", encoding="utf-8")
        _, edited = self.run_harness("--check")

        self.assertIn(HARNESS_SKILL, edited["gates"]["ref"]["differs"])

    def test_a_recipients_own_script_checks_with_no_from(self) -> None:
        self.run_harness("--install")

        done = subprocess.run(
            [sys.executable, str(self.target / ".agents/scripts/gw/harness.py"), str(self.target), "--check"],
            capture_output=True,
            encoding="utf-8",
        )

        self.assertEqual(self.source.resolve().as_posix(), json.loads(done.stdout)["repository"])
        self.assertTrue(json.loads(done.stdout)["gates"]["ref"]["passed"], done.stdout)

    def test_a_tree_whose_two_lines_name_different_repositories_is_refused(self) -> None:
        self.run_harness("--install")
        entry = self.target / "AGENTS.md"
        entry.write_text(
            entry.read_text(encoding="utf-8").replace(self.source.name, "somewhere-else", 1), encoding="utf-8"
        )

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            harness.main([str(self.target), "--check", "--from", str(self.source)])

        self.assertIn("somewhere-else", json.loads(said.getvalue())["refusals"][0])

    def test_a_source_path_holding_a_docs_segment_is_not_read_as_a_citation(self) -> None:
        nested = self.another_repository() / "docs" / "core"
        shutil.copytree(self.source, nested, ignore=shutil.ignore_patterns())

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = harness.main([str(self.target), "--install", "--from", str(nested)])
        report = json.loads(said.getvalue())

        self.assertEqual([], report["refusals"])
        self.assertIn("/docs/core", self.stamped_line())
        self.assertEqual(0, status, report["gates"])


# --- the one door that arrives with content ---------------------------------------------------


class TheDeliveryStatus(TwoTrees):
    """A fresh tree's first session reads the queue before anything has been written into it."""

    def test_an_install_writes_it_in_the_refs_own_words(self) -> None:
        self.write(
            QUEUE_ARRIVAL,
            QUEUE_ARRIVAL_TEXT.replace("nothing is in flight", "the queue is empty, reworded"),
        )
        self.commit("the mechanism rewords its own record")

        status, report = self.run_harness("--install")
        written = self.target_text(DELIVERY_STATUS)

        self.assertEqual(0, status, report)
        self.assertIn("the queue is empty, reworded", written)
        self.assertIn(report["ref"]["announced"], written)
        self.assertNotIn("{ref}", written)
        self.assertIn(DELIVERY_STATUS, report["written"])

    def test_an_install_leaves_a_record_the_tree_brought_with_it(self) -> None:
        # An install refuses only over manifest paths, and this is not one — so a tree that
        # already keeps its own docs/ receives core beside them. ai-game-1 is that shape.
        theirs = "# Материалы\n\nThe project's own queue, in its own words.\n"
        record = self.target / DELIVERY_STATUS
        record.parent.mkdir(parents=True, exist_ok=True)
        record.write_text(theirs, encoding="utf-8", newline="")

        status, report = self.run_harness("--install")

        self.assertEqual(0, status, report["refusals"])
        self.assertEqual(theirs, self.target_text(DELIVERY_STATUS))
        self.assertNotIn(DELIVERY_STATUS, report["written"])
        self.assertTrue(any(DELIVERY_STATUS in note for note in report["notes"]), report["notes"])

    def test_a_record_that_already_exists_is_the_projects_and_overwrite_does_not_reach_it(self) -> None:
        self.run_harness("--install")
        theirs = "# Delivery status\n\nRows the project wrote.\n"
        (self.target / DELIVERY_STATUS).write_text(theirs, encoding="utf-8", newline="")

        _, report = self.run_harness("--update", "--overwrite")

        self.assertEqual(theirs, self.target_text(DELIVERY_STATUS))
        self.assertNotIn(DELIVERY_STATUS, report["written"])
        self.assertTrue(any(DELIVERY_STATUS in note for note in report["notes"]), report["notes"])

    def test_an_update_gives_one_to_a_tree_that_received_core_without_it(self) -> None:
        self.run_harness("--install")
        (self.target / DELIVERY_STATUS).unlink()

        _, report = self.run_harness("--update")

        self.assertIn(DELIVERY_STATUS, report["written"])
        self.assertIn("Core arrived", self.target_text(DELIVERY_STATUS))

    def test_a_ref_with_no_shelf_or_no_block_is_refused_and_nothing_is_written(self) -> None:
        for spoil, reason in (
            (lambda: (self.root / QUEUE_ARRIVAL).unlink(), "this is not the harness"),
            (lambda: self.write(QUEUE_ARRIVAL, "# Arrival\n\nNo block.\n"), "declares no arrival state"),
        ):
            with self.subTest(reason=reason):
                self.write(QUEUE_ARRIVAL, QUEUE_ARRIVAL_TEXT)
                spoil()
                self.commit("spoil the shelf")
                before = self.target_snapshot()

                status, report = self.run_harness("--install")

                self.assertEqual(1, status)
                self.assertIn(reason, report["refusals"][0])
                self.assertEqual(before, self.target_snapshot())

    def test_the_recipients_check_never_reports_the_record(self) -> None:
        self.run_harness("--install")

        _, report = self.run_harness("--check")

        self.assertTrue(report["gates"]["ref"]["passed"], report["gates"])
        self.assertNotIn(DELIVERY_STATUS, report["gates"]["ref"]["differs"])
        self.assertNotIn(DELIVERY_STATUS, report["gates"]["ref"]["own"])

    def test_an_arrival_state_naming_a_document_still_installs(self) -> None:
        # The fence is blanked before the citation reader looks, so what the block names is not a
        # citation. Without that, a path under docs/ here would refuse the whole install.
        self.write(QUEUE_ARRIVAL, QUEUE_ARRIVAL_TEXT.replace("in flight.", "in flight; see docs/private/plan.md."))
        self.commit("an arrival state that names a document")

        status, report = self.run_harness("--install")

        self.assertEqual(0, status, report["refusals"])
        self.assertIn("docs/private/plan.md", self.target_text(DELIVERY_STATUS))


class TheCommandLine(unittest.TestCase):
    def run_main(self, *operands: str) -> int:
        with contextlib.redirect_stdout(io.StringIO()):
            return harness.main(list(operands))

    def test_no_mode_two_modes_or_no_target_is_usage(self) -> None:
        self.assertEqual(2, self.run_main("x"))
        self.assertEqual(2, self.run_main("x", "--install", "--check"))
        self.assertEqual(2, self.run_main("--install"))

    def test_overwrite_belongs_to_update_and_at_never_to_check(self) -> None:
        self.assertEqual(2, self.run_main("x", "--install", "--overwrite"))
        self.assertEqual(2, self.run_main("x", "--check", "--at", "v1"))


if __name__ == "__main__":
    unittest.main()
