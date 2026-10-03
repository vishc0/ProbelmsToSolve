#!/usr/bin/env python3
"""Create, validate, and export CloudSetup opportunities and projects."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Any


SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OPPORTUNITY_FIELDS = {
    "schema_version",
    "id",
    "title",
    "summary",
    "status",
    "visibility",
    "domain",
    "owner",
    "project_id",
    "website",
    "updated",
}
PROJECT_FIELDS = {
    "schema_version",
    "id",
    "title",
    "summary",
    "status",
    "visibility",
    "domain",
    "source_opportunity",
    "steward",
    "website",
    "repository",
    "updated",
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def require_slug(value: str, label: str = "ID") -> str:
    if not SLUG.fullmatch(value):
        raise ValueError(f"{label} must use lowercase kebab-case: {value!r}")
    return value


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def copy_template(source: Path, target: Path, replacements: dict[str, str]) -> None:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing path: {target}")
    shutil.copytree(source, target)
    for path in target.rglob("*"):
        if not path.is_file() or path.name == ".gitkeep" or path.suffix == ".json":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for token, replacement in replacements.items():
            content = content.replace(token, replacement)
        path.write_text(content, encoding="utf-8")


def new_opportunity(args: argparse.Namespace, root: Path) -> Path:
    opportunity_id = require_slug(args.id, "Opportunity ID")
    require_slug(args.domain, "Domain")
    target = root / "catalog" / "opportunities" / opportunity_id
    replacements = {
        "{{OPPORTUNITY_ID}}": opportunity_id,
        "{{OPPORTUNITY_TITLE}}": args.title,
        "{{OPPORTUNITY_SUMMARY}}": args.summary,
        "{{DOMAIN_ID}}": args.domain,
        "{{OWNER_NAME}}": args.owner,
        "{{TODAY}}": date.today().isoformat(),
    }
    copy_template(root / "templates" / "opportunity", target, replacements)
    manifest_path = target / "opportunity.json"
    manifest = load_json(manifest_path)
    manifest.update(
        {
            "id": opportunity_id,
            "title": args.title,
            "summary": args.summary,
            "domain": args.domain,
            "owner": args.owner,
            "website": {"slug": opportunity_id, "featured": False},
            "updated": date.today().isoformat(),
        }
    )
    write_json(manifest_path, manifest)
    return target


def new_project(args: argparse.Namespace, root: Path) -> Path:
    project_id = require_slug(args.id, "Project ID")
    opportunity_id = require_slug(args.opportunity, "Opportunity ID")
    opportunity_path = (
        root / "catalog" / "opportunities" / opportunity_id / "opportunity.json"
    )
    if not opportunity_path.exists():
        raise FileNotFoundError(f"Opportunity manifest not found: {opportunity_path}")

    opportunity = load_json(opportunity_path)
    linked_project = opportunity.get("project_id")
    if linked_project and linked_project != project_id:
        raise ValueError(
            f"Opportunity {opportunity_id!r} is already linked to "
            f"project {linked_project!r}"
        )
    for stage in ("incubator", "reference"):
        existing = root / "projects" / stage / project_id
        if existing.exists():
            raise FileExistsError(f"Refusing to overwrite existing path: {existing}")
    target = root / "projects" / "incubator" / project_id
    replacements = {
        "{{PROJECT_ID}}": project_id,
        "{{PROJECT_TITLE}}": args.title,
        "{{PROJECT_SUMMARY}}": args.summary,
        "{{OPPORTUNITY_ID}}": opportunity_id,
        "{{DOMAIN_ID}}": opportunity["domain"],
        "{{STEWARD_NAME}}": args.steward,
        "{{TODAY}}": date.today().isoformat(),
    }
    copy_template(root / "templates" / "project", target, replacements)
    project_manifest_path = target / "project.json"
    project_manifest = load_json(project_manifest_path)
    project_manifest.update(
        {
            "id": project_id,
            "title": args.title,
            "summary": args.summary,
            "domain": opportunity["domain"],
            "source_opportunity": str(opportunity_path.relative_to(root)),
            "steward": {"name": args.steward, "github": ""},
            "website": {"slug": project_id, "featured": False},
            "repository": {
                "path": str(target.relative_to(root)),
                "license": "TBD",
            },
            "updated": date.today().isoformat(),
        }
    )
    write_json(project_manifest_path, project_manifest)
    opportunity["project_id"] = project_id
    opportunity["status"] = "incubating"
    opportunity["updated"] = date.today().isoformat()
    write_json(opportunity_path, opportunity)
    return target


def validate_manifest(
    path: Path, required: set[str], expected_id: str
) -> list[str]:
    errors: list[str] = []
    try:
        value = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON: {exc}"]
    missing = sorted(required - value.keys())
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(missing)}")
    if value.get("id") != expected_id:
        errors.append(f"{path}: id must match directory name {expected_id!r}")
    if value.get("visibility") not in {"draft", "public"}:
        errors.append(f"{path}: visibility must be 'draft' or 'public'")
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    opportunities: dict[str, dict[str, Any]] = {}
    for path in sorted((root / "catalog" / "opportunities").glob("*/opportunity.json")):
        errors.extend(validate_manifest(path, OPPORTUNITY_FIELDS, path.parent.name))
        if not errors or path.exists():
            try:
                opportunities[path.parent.name] = load_json(path)
            except (OSError, json.JSONDecodeError):
                pass

    projects: dict[str, dict[str, Any]] = {}
    for stage in ("incubator", "reference"):
        for path in sorted((root / "projects" / stage).glob("*/project.json")):
            errors.extend(validate_manifest(path, PROJECT_FIELDS, path.parent.name))
            try:
                project = load_json(path)
            except (OSError, json.JSONDecodeError):
                continue
            projects[path.parent.name] = project
            source = root / project.get("source_opportunity", "")
            if not source.is_file():
                errors.append(f"{path}: source_opportunity does not exist: {source}")

    for opportunity_id, opportunity in opportunities.items():
        project_id = opportunity.get("project_id")
        if project_id and project_id not in projects:
            errors.append(
                f"opportunity {opportunity_id}: project_id {project_id!r} was not found"
            )
    return errors


def export_catalog(root: Path, include_drafts: bool) -> dict[str, Any]:
    def include(item: dict[str, Any]) -> bool:
        return include_drafts or item.get("visibility") == "public"

    opportunities = []
    for path in sorted((root / "catalog" / "opportunities").glob("*/opportunity.json")):
        item = load_json(path)
        if include(item):
            item["content_path"] = str(path.with_name("OPPORTUNITY.md").relative_to(root))
            opportunities.append(item)

    projects = []
    for stage in ("incubator", "reference"):
        for path in sorted((root / "projects" / stage).glob("*/project.json")):
            item = load_json(path)
            if include(item):
                item["content_path"] = str(path.with_name("PROJECT.md").relative_to(root))
                projects.append(item)

    return {
        "schema_version": "1.0",
        "generated_at": date.today().isoformat(),
        "opportunities": opportunities,
        "projects": projects,
    }


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description="CloudSetup opportunity and project scaffolding"
    )
    command.add_argument(
        "--root", type=Path, default=repository_root(), help=argparse.SUPPRESS
    )
    subcommands = command.add_subparsers(dest="command", required=True)

    opportunity = subcommands.add_parser("new-opportunity")
    opportunity.add_argument("--id", required=True)
    opportunity.add_argument("--title", required=True)
    opportunity.add_argument("--summary", required=True)
    opportunity.add_argument("--domain", required=True)
    opportunity.add_argument("--owner", default="Unassigned")

    project = subcommands.add_parser("new-project")
    project.add_argument("--id", required=True)
    project.add_argument("--title", required=True)
    project.add_argument("--summary", required=True)
    project.add_argument("--opportunity", required=True)
    project.add_argument("--steward", default="Unassigned")

    subcommands.add_parser("validate")
    export = subcommands.add_parser("export-catalog")
    export.add_argument("--include-drafts", action="store_true")
    export.add_argument("--output", type=Path)
    return command


def main() -> int:
    args = parser().parse_args()
    root = args.root.resolve()
    try:
        if args.command == "new-opportunity":
            created = new_opportunity(args, root)
            print(f"Created opportunity: {created.relative_to(root)}")
        elif args.command == "new-project":
            created = new_project(args, root)
            print(f"Created project: {created.relative_to(root)}")
        elif args.command == "validate":
            errors = validate(root)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print("Foundry manifests are valid.")
        elif args.command == "export-catalog":
            content = json.dumps(
                export_catalog(root, args.include_drafts), indent=2
            ) + "\n"
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(content, encoding="utf-8")
                print(f"Wrote catalog: {args.output}")
            else:
                print(content, end="")
    except (FileExistsError, FileNotFoundError, KeyError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
