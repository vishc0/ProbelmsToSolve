from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "foundry", REPOSITORY_ROOT / "tooling" / "foundry.py"
)
assert SPEC and SPEC.loader
foundry = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(foundry)


class FoundryToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for relative in (
            "templates/opportunity",
            "templates/project",
            "catalog/opportunities",
            "projects/incubator",
            "projects/reference",
        ):
            (self.root / relative).mkdir(parents=True, exist_ok=True)
        for template in ("opportunity", "project"):
            source = REPOSITORY_ROOT / "templates" / template
            target = self.root / "templates" / template
            for path in source.rglob("*"):
                destination = target / path.relative_to(source)
                if path.is_dir():
                    destination.mkdir(parents=True, exist_ok=True)
                else:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(path.read_bytes())

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_create_link_validate_and_export(self) -> None:
        opportunity_args = argparse.Namespace(
            id="verification-audit",
            title='Verification "Audit"',
            summary="Detect unauthorized compute with bounded sampling.",
            domain="compute-governance",
            owner="Test Owner",
        )
        foundry.new_opportunity(opportunity_args, self.root)

        project_args = argparse.Namespace(
            id="audit-simulator",
            title="Audit Simulator",
            summary="A reusable verification simulator.",
            opportunity="verification-audit",
            steward="Test Steward",
        )
        foundry.new_project(project_args, self.root)

        self.assertEqual(foundry.validate(self.root), [])
        opportunity = json.loads(
            (
                self.root
                / "catalog/opportunities/verification-audit/opportunity.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(opportunity["project_id"], "audit-simulator")
        self.assertEqual(opportunity["title"], 'Verification "Audit"')

        project_path = self.root / "projects/incubator/audit-simulator/project.json"
        project = json.loads(project_path.read_text(encoding="utf-8"))
        self.assertEqual(
            project["source_opportunity"],
            "catalog/opportunities/verification-audit/opportunity.json",
        )

        self.assertEqual(foundry.export_catalog(self.root, False)["projects"], [])
        project["visibility"] = "public"
        project_path.write_text(json.dumps(project), encoding="utf-8")
        self.assertEqual(
            len(foundry.export_catalog(self.root, False)["projects"]), 1
        )

    def test_refuses_to_overwrite_opportunity(self) -> None:
        args = argparse.Namespace(
            id="existing-item",
            title="Existing Item",
            summary="Test",
            domain="test-domain",
            owner="Owner",
        )
        foundry.new_opportunity(args, self.root)
        with self.assertRaises(FileExistsError):
            foundry.new_opportunity(args, self.root)

    def test_rejects_invalid_slug(self) -> None:
        with self.assertRaises(ValueError):
            foundry.require_slug("Not Valid")

    def test_refuses_second_project_for_same_opportunity(self) -> None:
        opportunity_args = argparse.Namespace(
            id="single-owner",
            title="Single Owner",
            summary="One opportunity link.",
            domain="test-domain",
            owner="Owner",
        )
        foundry.new_opportunity(opportunity_args, self.root)
        first = argparse.Namespace(
            id="first-project",
            title="First Project",
            summary="First",
            opportunity="single-owner",
            steward="Steward",
        )
        foundry.new_project(first, self.root)
        second = argparse.Namespace(
            id="second-project",
            title="Second Project",
            summary="Second",
            opportunity="single-owner",
            steward="Steward",
        )
        with self.assertRaises(ValueError):
            foundry.new_project(second, self.root)


if __name__ == "__main__":
    unittest.main()
