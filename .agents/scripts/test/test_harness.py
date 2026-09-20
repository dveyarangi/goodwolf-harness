"""Placing a ref of the repository into a tree that is not its own, updating it, and checking it."""

from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from repository import SCRIPTS, RepositoryCase

import harness

KEEPER = ".agents/skills/keeper/SKILL.md"
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
    "| part | where | owner |\n|---|---|---|\n| corpus reader | `.agents/scripts/docs_corpus.py` | nobody removable |\n\n"
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
        self.write(DOC, SAMPLE_DOC)
        self.write("AGENTS.md", ENTRY)
        self.write("CLAUDE.md", "@AGENTS.md\n")
        self.write(".agents/README.md", "# Installed harness\n\nSkills live under `skills/`.\n")
        self.write(".agents/glossary.md", "# The development method\n\n**Recipient**: a tree that received core.\n")
        for script in SCRIPTS.glob("*.py"):
            self.write(f".agents/scripts/{script.name}", script.read_text(encoding="utf-8"))
        self.write(".agents/scripts/test/test_arrival.py", ARRIVAL_TEST)
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


class TheSource(TwoTrees):
    def test_the_manifest_at_a_ref_is_core_plus_the_two_root_files_and_nothing_else(self) -> None:
        with harness.Source(str(self.source)) as source:
            ref = source.resolve("HEAD")
            manifest = source.manifest(ref)

        self.assertIn("AGENTS.md", manifest)
        self.assertIn("CLAUDE.md", manifest)
        self.assertIn(KEEPER, manifest)
        self.assertIn(".agents/scripts/test/test_arrival.py", manifest)
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
        self.assertTrue((self.target / ".agents/scripts/harness.py").is_file())
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

    def test_arrives_when_the_platform_makes_links_and_is_pending_with_the_command_when_it_does_not(self) -> None:
        status, report = self.run_harness("--install")

        gates = report["gates"]
        self.assertTrue(gates["ref"]["passed"], gates["ref"])
        self.assertTrue(gates["injector"]["passed"], gates["injector"])
        self.assertTrue(gates["shape"]["passed"], gates["shape"])
        self.assertTrue(gates["suite"]["passed"], gates["suite"])
        self.assertEqual(1, gates["suite"]["tests"])
        if platform_makes_symlinks():
            self.assertEqual(["made", "made"], [link["state"] for link in report["links"]])
            self.assertTrue(gates["links"]["passed"], gates["links"])
            self.assertTrue(report["arrived"])
            self.assertEqual(0, status)
        else:
            self.assertEqual(["pending", "pending"], [link["state"] for link in report["links"]])
            self.assertEqual(2, len(report["pending"]))
            self.assertIn(str(self.target / ".claude" / "skills"), report["pending"][0])
            self.assertIn("mklink /D" if os.name == "nt" else "ln -s", report["pending"][0])
            self.assertFalse(gates["links"]["passed"])
            self.assertFalse(report["arrived"])
            self.assertEqual(1, status)
        self.assertFalse(any("__pycache__" in path.parts for path in self.target.rglob("*")))

    def test_a_failing_shipped_suite_leaves_arrival_false_naming_the_gate(self) -> None:
        self.write(".agents/scripts/test/test_arrival.py", ARRIVAL_TEST.replace("assertTrue(True)", "assertTrue(False)"))
        self.commit("a broken suite")

        status, report = self.run_harness("--install")

        self.assertFalse(report["gates"]["suite"]["passed"])
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
