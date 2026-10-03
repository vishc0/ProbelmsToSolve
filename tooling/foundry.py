#!/usr/bin/env python3
"""Create, validate, index, and export CloudSetup foundry records."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Iterable


SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PROVENANCE_LABELS = {
    "source-claim", "external-evidence", "ai-inference", "human-direction",
    "human-decision", "implementation-result",
}
COMMON_FIELDS = {
    "schema_version", "record_type", "id", "title", "summary", "status",
    "visibility", "owner", "links", "facets", "provenance", "created", "updated",
}
FACET_VALUES = {
    "mission": {"everyday-ai-empowerment"},
    "capability": {"sensing", "verification"},
    "population": {"households", "workers", "communities", "institutions"},
    "geography": {"local", "national", "global"},
    "topic": {
        "addiction", "ai-control", "compute-governance", "consumer-protection",
        "energy-resilience", "household-costs", "mental-health",
        "research-evaluation", "supply-chains",
    },
}
LEGACY_OPPORTUNITY_FIELDS = {
    "schema_version", "id", "title", "summary", "status", "visibility",
    "domain", "owner", "project_id", "website", "updated",
}
LEGACY_PROJECT_FIELDS = {
    "schema_version", "id", "title", "summary", "status", "visibility",
    "domain", "source_opportunity", "steward", "website", "repository", "updated",
}
RECORD_LOCATIONS = {
    "domain": ("catalog/domains", "domain.json", "README.md"),
    "problem": ("catalog/problems", "problem.json", "PROBLEM.md"),
    "cluster": ("catalog/clusters", "cluster.json", "CLUSTER.md"),
    "opportunity": ("catalog/opportunities", "opportunity.json", "OPPORTUNITY.md"),
    "solution": ("catalog/solutions", "solution.json", "SOLUTION.md"),
}
LINK_TARGETS = {
    "domains": "domain", "problems": "problem", "clusters": "cluster",
    "opportunities": "opportunity", "projects": "project", "solutions": "solution",
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def require_slug(value: str, label: str = "ID") -> str:
    if not SLUG.fullmatch(value):
        raise ValueError(f"{label} must use lowercase kebab-case: {value!r}")
    return value


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"JSON record must be an object: {path}")
    return value


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


def scaffold_record(
    root: Path,
    record_type: str,
    record_id: str,
    replacements: dict[str, str],
    updates: dict[str, Any],
) -> Path:
    base, manifest_name, _ = RECORD_LOCATIONS[record_type]
    target = root / base / record_id
    copy_template(root / "templates" / record_type, target, replacements)
    manifest_path = target / manifest_name
    manifest = load_json(manifest_path)
    manifest["created"] = date.today().isoformat()
    manifest.update(updates)
    write_json(manifest_path, manifest)
    return target


def common_replacements(args: argparse.Namespace, prefix: str) -> dict[str, str]:
    return {
        f"{{{{{prefix}_ID}}}}": args.id,
        f"{{{{{prefix}_TITLE}}}}": args.title,
        f"{{{{{prefix}_SUMMARY}}}}": args.summary,
        "{{OWNER_NAME}}": args.owner,
        "{{TODAY}}": date.today().isoformat(),
    }


def checked_slugs(values: Iterable[str], label: str) -> list[str]:
    return [require_slug(value, label) for value in values]


def requested_facets(args: argparse.Namespace) -> dict[str, list[str]]:
    return {
        name: checked_slugs(getattr(args, name, None) or [], f"{name} facet")
        for name in FACET_VALUES
    }


def new_domain(args: argparse.Namespace, root: Path) -> Path:
    record_id = require_slug(args.id, "Domain ID")
    return scaffold_record(
        root, "domain", record_id, common_replacements(args, "DOMAIN"),
        {"id": record_id, "title": args.title, "summary": args.summary,
         "owner": args.owner, "parent": getattr(args, "parent", None),
         "aliases": checked_slugs(getattr(args, "alias", None) or [], "Alias"),
         "facets": requested_facets(args), "updated": date.today().isoformat()},
    )


def new_problem(args: argparse.Namespace, root: Path) -> Path:
    record_id = require_slug(args.id, "Problem ID")
    domains = checked_slugs(args.domain, "Domain")
    clusters = checked_slugs(args.cluster or [], "Cluster")
    return scaffold_record(
        root, "problem", record_id, common_replacements(args, "PROBLEM"),
        {"id": record_id, "title": args.title, "summary": args.summary,
         "owner": args.owner, "links": {"domains": domains, "clusters": clusters},
         "facets": requested_facets(args),
         "updated": date.today().isoformat()},
    )


def new_cluster(args: argparse.Namespace, root: Path) -> Path:
    record_id = require_slug(args.id, "Cluster ID")
    domains = checked_slugs(args.domain, "Domain")
    return scaffold_record(
        root, "cluster", record_id, common_replacements(args, "CLUSTER"),
        {"id": record_id, "title": args.title, "summary": args.summary,
         "owner": args.owner, "links": {"domains": domains},
         "facets": requested_facets(args),
         "updated": date.today().isoformat()},
    )


def new_solution(args: argparse.Namespace, root: Path) -> Path:
    record_id = require_slug(args.id, "Solution ID")
    links = {
        "domains": checked_slugs(args.domain, "Domain"),
        "clusters": checked_slugs(args.cluster or [], "Cluster"),
    }
    return scaffold_record(
        root, "solution", record_id, common_replacements(args, "SOLUTION"),
        {"id": record_id, "title": args.title, "summary": args.summary,
         "owner": args.owner, "links": links, "facets": requested_facets(args),
         "updated": date.today().isoformat()},
    )


def new_opportunity(args: argparse.Namespace, root: Path) -> Path:
    opportunity_id = require_slug(args.id, "Opportunity ID")
    domain = require_slug(args.domain, "Domain")
    replacements = common_replacements(args, "OPPORTUNITY") | {"{{DOMAIN_ID}}": domain}
    clusters = checked_slugs(getattr(args, "cluster", None) or [], "Cluster")
    return scaffold_record(
        root, "opportunity", opportunity_id, replacements,
        {"id": opportunity_id, "title": args.title, "summary": args.summary,
         "domain": domain, "owner": args.owner,
         "links": {"domains": [domain], "clusters": clusters,
                   "projects": [], "solutions": []},
         "facets": requested_facets(args),
         "website": {"slug": opportunity_id, "featured": False},
         "updated": date.today().isoformat()},
    )


def new_project(args: argparse.Namespace, root: Path) -> Path:
    project_id = require_slug(args.id, "Project ID")
    requested = args.opportunity
    opportunity_ids = checked_slugs(
        [requested] if isinstance(requested, str) else requested,
        "Opportunity ID",
    )
    opportunities = []
    for opportunity_id in opportunity_ids:
        opportunity_path = (
            root / "catalog/opportunities" / opportunity_id / "opportunity.json"
        )
        if not opportunity_path.exists():
            raise FileNotFoundError(
                f"Opportunity manifest not found: {opportunity_path}"
            )
        opportunities.append((opportunity_path, load_json(opportunity_path)))
    for stage in ("incubator", "reference"):
        existing = root / "projects" / stage / project_id
        if existing.exists():
            raise FileExistsError(f"Refusing to overwrite existing path: {existing}")
    target = root / "projects/incubator" / project_id
    opportunity_id = opportunity_ids[0]
    opportunity_path = opportunities[0][0]
    domain = opportunities[0][1]["domain"]
    domains = sorted({item["domain"] for _, item in opportunities})
    solutions = checked_slugs(getattr(args, "solution", None) or [], "Solution")
    replacements = {
        "{{PROJECT_ID}}": project_id, "{{PROJECT_TITLE}}": args.title,
        "{{PROJECT_SUMMARY}}": args.summary, "{{OPPORTUNITY_ID}}": opportunity_id,
        "{{DOMAIN_ID}}": domain, "{{STEWARD_NAME}}": args.steward,
        "{{TODAY}}": date.today().isoformat(),
    }
    copy_template(root / "templates/project", target, replacements)
    project_path = target / "project.json"
    project = load_json(project_path)
    project.update({
        "id": project_id, "title": args.title, "summary": args.summary,
        "domain": domain, "owner": args.steward,
        "source_opportunity": str(opportunity_path.relative_to(root)),
        "steward": {"name": args.steward, "github": ""},
        "links": {"domains": domains, "opportunities": opportunity_ids,
                  "solutions": solutions},
        "facets": {
            name: sorted({
                facet
                for _, opportunity in opportunities
                for facet in opportunity.get("facets", {}).get(name, [])
            })
            for name in FACET_VALUES
        },
        "website": {"slug": project_id, "featured": False},
        "repository": {"path": str(target.relative_to(root)), "license": "TBD"},
        "created": date.today().isoformat(),
        "updated": date.today().isoformat(),
    })
    write_json(project_path, project)
    for linked_path, opportunity in opportunities:
        opportunity.setdefault("project_id", project_id)
        opportunity["status"] = "incubating"
        opportunity.setdefault("links", {}).setdefault("projects", [])
        if project_id not in opportunity["links"]["projects"]:
            opportunity["links"]["projects"].append(project_id)
        opportunity["updated"] = date.today().isoformat()
        write_json(linked_path, opportunity)
    return target


def manifest_paths(root: Path) -> list[tuple[str, Path]]:
    paths: list[tuple[str, Path]] = []
    for record_type, (base, filename, _) in RECORD_LOCATIONS.items():
        paths.extend(
            (record_type, path)
            for path in sorted((root / base).glob(f"*/{filename}"))
        )
    for stage in ("incubator", "reference"):
        paths.extend(
            ("project", path)
            for path in sorted((root / "projects" / stage).glob("*/project.json"))
        )
    return paths


def read_records(
    root: Path,
) -> tuple[dict[str, dict[str, dict[str, Any]]], list[str]]:
    records: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    errors: list[str] = []
    seen: dict[str, tuple[str, Path]] = {}
    for expected_type, path in manifest_paths(root):
        try:
            value = load_json(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: invalid JSON: {exc}")
            continue
        record_id = value.get("id")
        if not isinstance(record_id, str):
            errors.append(f"{path.relative_to(root)}: id must be a string")
            continue
        if record_id in seen:
            prior_type, prior_path = seen[record_id]
            errors.append(
                f"duplicate id {record_id!r}: {prior_type} "
                f"{prior_path.relative_to(root)} and {expected_type} "
                f"{path.relative_to(root)}"
            )
        else:
            seen[record_id] = (expected_type, path)
        value["_path"] = path
        records[expected_type][record_id] = value
    return records, errors


def validate_manifest(
    path: Path,
    value: dict[str, Any],
    expected_type: str,
    root: Path,
) -> list[str]:
    label = str(path.relative_to(root))
    legacy = (
        value.get("schema_version") == "1.0"
        and expected_type in {"opportunity", "project"}
    )
    if legacy and expected_type == "opportunity":
        required = LEGACY_OPPORTUNITY_FIELDS
    elif legacy:
        required = LEGACY_PROJECT_FIELDS
    else:
        required = COMMON_FIELDS
    errors: list[str] = []
    missing = sorted(required - value.keys())
    if missing:
        errors.append(f"{label}: missing fields: {', '.join(missing)}")
    if value.get("id") != path.parent.name:
        errors.append(f"{label}: id must match directory name {path.parent.name!r}")
    if not legacy and value.get("record_type") != expected_type:
        errors.append(f"{label}: record_type must be {expected_type!r}")
    if value.get("visibility") not in {"draft", "public"}:
        errors.append(f"{label}: visibility must be 'draft' or 'public'")
    for field in ("title", "summary", "status"):
        if field in value and (
            not isinstance(value[field], str) or not value[field].strip()
        ):
            errors.append(f"{label}: {field} must be a non-empty string")
    if not legacy:
        provenance = value.get("provenance")
        if (
            not isinstance(provenance, dict)
            or provenance.get("label") not in PROVENANCE_LABELS
        ):
            errors.append(f"{label}: provenance.label is missing or unsupported")
        if not isinstance(value.get("links"), dict):
            errors.append(f"{label}: links must be an object")
        facets = value.get("facets")
        if not isinstance(facets, dict):
            errors.append(f"{label}: facets must be an object")
        else:
            unknown_keys = sorted(set(facets) - set(FACET_VALUES))
            if unknown_keys:
                errors.append(
                    f"{label}: unknown facet types: {', '.join(unknown_keys)}"
                )
            for facet_type, allowed in FACET_VALUES.items():
                values = facets.get(facet_type, [])
                if (
                    not isinstance(values, list)
                    or any(not isinstance(item, str) for item in values)
                ):
                    errors.append(f"{label}: facets.{facet_type} must be a list")
                    continue
                if len(values) != len(set(values)):
                    errors.append(
                        f"{label}: facets.{facet_type} contains duplicate values"
                    )
                unknown_values = sorted(set(values) - allowed)
                if unknown_values:
                    errors.append(
                        f"{label}: unknown {facet_type} facet values: "
                        f"{', '.join(unknown_values)}"
                    )
        for field in ("created", "updated"):
            try:
                date.fromisoformat(value.get(field, ""))
            except (TypeError, ValueError):
                errors.append(f"{label}: {field} must be an ISO date")
    return errors


def validate(root: Path) -> list[str]:
    records, errors = read_records(root)
    domain_aliases: dict[str, str] = {}
    for domain_id, domain in records.get("domain", {}).items():
        label = f"domain {domain_id}"
        aliases = domain.get("aliases", [])
        if not isinstance(aliases, list) or any(
            not isinstance(alias, str) or not SLUG.fullmatch(alias)
            for alias in aliases
        ):
            errors.append(f"{label}: aliases must be a list of kebab-case ids")
            continue
        for alias in aliases:
            if alias in records["domain"] or alias in domain_aliases:
                errors.append(f"{label}: domain alias {alias!r} is not unique")
            else:
                domain_aliases[alias] = domain_id
        parent = domain.get("parent")
        if parent is not None and parent not in records["domain"]:
            errors.append(f"{label}: parent domain {parent!r} was not found")
        if parent == domain_id:
            errors.append(f"{label}: parent cannot refer to itself")

    for record_type, items in records.items():
        for value in items.values():
            errors.extend(
                validate_manifest(value["_path"], value, record_type, root)
            )

    # New catalog areas are record-only. Content-only legacy opportunities and
    # projects remain allowed until their owners promote them to records.
    for record_type in ("domain", "problem", "cluster", "solution"):
        base, filename, _ = RECORD_LOCATIONS[record_type]
        folders = sorted(path for path in (root / base).glob("*") if path.is_dir())
        for folder in folders:
            if not (folder / filename).is_file():
                errors.append(f"{folder.relative_to(root)}: missing {filename}")

    for record_type, items in records.items():
        for record_id, value in items.items():
            label = f"{record_type} {record_id}"
            links = value.get("links", {})
            if isinstance(links, dict):
                for link_name, target_type in LINK_TARGETS.items():
                    references = links.get(link_name, [])
                    if (
                        not isinstance(references, list)
                        or any(not isinstance(item, str) for item in references)
                    ):
                        errors.append(
                            f"{label}: links.{link_name} must be a list of ids"
                        )
                        continue
                    if len(references) != len(set(references)):
                        errors.append(
                            f"{label}: links.{link_name} contains duplicate ids"
                        )
                    for reference in references:
                        if (
                            reference not in records.get(target_type, {})
                            and not (
                                target_type == "domain"
                                and reference in domain_aliases
                            )
                        ):
                            errors.append(
                                f"{label}: referenced {target_type} "
                                f"{reference!r} was not found"
                            )
            if record_type in {"opportunity", "project"}:
                domain = value.get("domain")
                if (
                    domain
                    and domain not in records.get("domain", {})
                    and domain not in domain_aliases
                ):
                    errors.append(f"{label}: domain {domain!r} was not found")
            if record_type == "opportunity":
                project_id = value.get("project_id")
                if project_id and project_id not in records.get("project", {}):
                    errors.append(
                        f"{label}: project_id {project_id!r} was not found"
                    )
            if record_type == "project":
                source = value.get("source_opportunity")
                source_path = (root / source) if isinstance(source, str) else None
                opportunity_paths = {
                    item["_path"].resolve()
                    for item in records.get("opportunity", {}).values()
                }
                if (
                    source_path is None
                    or not source_path.is_file()
                    or source_path.resolve() not in opportunity_paths
                ):
                    errors.append(
                        f"{label}: source_opportunity is not a registered "
                        f"opportunity: {source!r}"
                    )
    return sorted(set(errors))


def public_record(value: dict[str, Any]) -> dict[str, Any]:
    return {key: item for key, item in value.items() if not key.startswith("_")}


def export_catalog(root: Path, include_drafts: bool) -> dict[str, Any]:
    records, errors = read_records(root)
    if errors:
        raise ValueError("; ".join(errors))
    result: dict[str, Any] = {
        "schema_version": "2.0",
        "generated_at": date.today().isoformat(),
    }
    types = (
        ("domains", "domain"), ("problems", "problem"), ("clusters", "cluster"),
        ("opportunities", "opportunity"), ("projects", "project"),
        ("solutions", "solution"),
    )
    for plural, record_type in types:
        items = []
        for value in records[record_type].values():
            if not include_drafts and value.get("visibility") != "public":
                continue
            item = public_record(value)
            path = value["_path"]
            if record_type == "project":
                content_name = "PROJECT.md"
            else:
                content_name = RECORD_LOCATIONS[record_type][2]
            content_path = path.with_name(content_name)
            if content_path.is_file():
                item["content_path"] = str(content_path.relative_to(root))
            items.append(item)
        result[plural] = sorted(items, key=lambda item: item["id"])
    return result


def record_link(root: Path, output: Path, value: dict[str, Any]) -> str:
    target = value["_path"]
    record_type = value.get("record_type")
    if record_type == "project" or target.name == "project.json":
        content = target.with_name("PROJECT.md")
    else:
        content_name = RECORD_LOCATIONS.get(
            record_type or target.stem, ("", "", target.name)
        )[2]
        content = target.with_name(content_name)
    target = content if content.is_file() else target
    return Path(os.path.relpath(target, output.parent)).as_posix()


def write_index(
    path: Path,
    title: str,
    sections: list[tuple[str, list[str]]],
) -> None:
    lines = [
        f"# {title}", "",
        "<!-- Generated by tooling/foundry.py index; do not edit. -->", "",
    ]
    if not sections:
        lines.append("No records registered.")
    for heading, entries in sections:
        lines.extend([f"## {heading}", ""])
        lines.extend(entries or ["No linked records."])
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def item_line(
    root: Path,
    output: Path,
    kind: str,
    value: dict[str, Any],
) -> str:
    return (
        f"- **{kind.title()}:** "
        f"[{value['title']}]({record_link(root, output, value)}) "
        f"— {value['status']}"
    )


def generate_indexes(root: Path) -> list[Path]:
    errors = validate(root)
    if errors:
        raise ValueError("Cannot generate indexes:\n" + "\n".join(errors))
    records, _ = read_records(root)
    outputs = [
        root / "catalog/domains/README.md",
        root / "catalog/indexes/by-domain.md",
        root / "catalog/indexes/by-cluster.md",
        root / "catalog/indexes/by-state.md",
        root / "catalog/indexes/by-solution.md",
        root / "catalog/indexes/by-facet.md",
    ]

    domain_aliases = {
        alias: domain_id
        for domain_id, domain in records["domain"].items()
        for alias in domain.get("aliases", [])
    }

    def domain_sections(output: Path) -> list[tuple[str, list[str]]]:
        sections = []
        ordered_domains = sorted(
            records["domain"].items(),
            key=lambda pair: (pair[1].get("parent") is not None, pair[0]),
        )
        for domain_id, domain in ordered_domains:
            entries = [domain["summary"], ""]
            parent = domain.get("parent")
            if parent:
                entries.extend([f"Subdomain of `{parent}`.", ""])
            else:
                entries.extend(["Top-level sector domain.", ""])
            aliases = domain.get("aliases", [])
            if aliases:
                entries.extend(
                    [f"Compatibility aliases: {', '.join(f'`{alias}`' for alias in aliases)}.", ""]
                )
            for kind in (
                "problem", "cluster", "opportunity", "project", "solution",
            ):
                values = sorted(
                    records[kind].values(), key=lambda item: item["title"]
                )
                for value in values:
                    links = value.get("links", {})
                    if (
                        domain_id in {
                            domain_aliases.get(item, item)
                            for item in links.get("domains", [])
                        }
                        or domain_aliases.get(value.get("domain"), value.get("domain"))
                        == domain_id
                    ):
                        entries.append(item_line(root, output, kind, value))
            heading = (
                f"[{domain['title']}]({record_link(root, output, domain)})"
            )
            sections.append((heading, entries))
        return sections

    write_index(outputs[0], "Domain Catalog", domain_sections(outputs[0]))
    write_index(outputs[1], "Catalog by Domain", domain_sections(outputs[1]))

    cluster_sections = []
    for cluster_id, cluster in sorted(records["cluster"].items()):
        entries = [cluster["summary"], ""]
        for kind in ("problem", "opportunity", "solution"):
            values = sorted(
                records[kind].values(), key=lambda item: item["title"]
            )
            for value in values:
                if cluster_id in value.get("links", {}).get("clusters", []):
                    entries.append(item_line(root, outputs[2], kind, value))
        cluster_sections.append((cluster["title"], entries))
    write_index(outputs[2], "Catalog by Problem Cluster", cluster_sections)

    states: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for kind, items in records.items():
        for value in items.values():
            states[value["status"]].append((kind, value))
    state_sections = []
    for state, values in sorted(states.items()):
        ordered = sorted(values, key=lambda pair: (pair[0], pair[1]["title"]))
        entries = [
            item_line(root, outputs[3], kind, value)
            for kind, value in ordered
        ]
        state_sections.append((state.replace("-", " ").title(), entries))
    write_index(outputs[3], "Catalog by Lifecycle State", state_sections)

    solution_sections = []
    for solution_id, solution in sorted(records["solution"].items()):
        entries = [solution["summary"], ""]
        projects = sorted(
            records["project"].values(), key=lambda item: item["title"]
        )
        for project in projects:
            if solution_id in project.get("links", {}).get("solutions", []):
                entries.append(
                    item_line(root, outputs[4], "project", project)
                )
        solution_sections.append((solution["title"], entries))
    write_index(outputs[4], "Catalog by Solution Pattern", solution_sections)
    facet_sections = []
    for facet_type, allowed in FACET_VALUES.items():
        for facet in sorted(allowed):
            entries = []
            for kind, items in records.items():
                for value in sorted(items.values(), key=lambda item: item["title"]):
                    if facet in value.get("facets", {}).get(facet_type, []):
                        entries.append(item_line(root, outputs[5], kind, value))
            if entries:
                facet_sections.append(
                    (f"{facet_type.title()}: {facet.replace('-', ' ').title()}", entries)
                )
    write_index(outputs[5], "Catalog by Facet", facet_sections)
    return outputs


def add_common_arguments(
    command: argparse.ArgumentParser,
    repeated_domains: bool = False,
) -> None:
    command.add_argument("--id", required=True)
    command.add_argument("--title", required=True)
    command.add_argument("--summary", required=True)
    command.add_argument("--owner", default="Unassigned")
    if repeated_domains:
        command.add_argument("--domain", action="append", required=True)
    for facet_type in FACET_VALUES:
        command.add_argument(f"--{facet_type}", action="append")


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description="CloudSetup foundry record tooling"
    )
    command.add_argument(
        "--root", type=Path, default=repository_root(), help=argparse.SUPPRESS
    )
    subcommands = command.add_subparsers(dest="command", required=True)
    domain = subcommands.add_parser("new-domain")
    add_common_arguments(domain)
    domain.add_argument("--parent")
    domain.add_argument("--alias", action="append")
    problem = subcommands.add_parser("new-problem")
    add_common_arguments(problem, repeated_domains=True)
    problem.add_argument("--cluster", action="append")
    cluster = subcommands.add_parser("new-cluster")
    add_common_arguments(cluster, repeated_domains=True)
    solution = subcommands.add_parser("new-solution")
    add_common_arguments(solution, repeated_domains=True)
    solution.add_argument("--cluster", action="append")
    opportunity = subcommands.add_parser("new-opportunity")
    add_common_arguments(opportunity)
    opportunity.add_argument("--domain", required=True)
    opportunity.add_argument("--cluster", action="append")
    project = subcommands.add_parser("new-project")
    project.add_argument("--id", required=True)
    project.add_argument("--title", required=True)
    project.add_argument("--summary", required=True)
    project.add_argument("--opportunity", action="append", required=True)
    project.add_argument("--solution", action="append")
    project.add_argument("--steward", default="Unassigned")
    subcommands.add_parser("validate")
    subcommands.add_parser("index")
    export = subcommands.add_parser("export-catalog")
    export.add_argument("--include-drafts", action="store_true")
    export.add_argument("--output", type=Path)
    return command


def main() -> int:
    args = parser().parse_args()
    root = args.root.resolve()
    try:
        creators = {
            "new-domain": new_domain,
            "new-problem": new_problem,
            "new-cluster": new_cluster,
            "new-solution": new_solution,
            "new-opportunity": new_opportunity,
            "new-project": new_project,
        }
        if args.command in creators:
            created = creators[args.command](args, root)
            kind = args.command.removeprefix("new-")
            print(f"Created {kind}: {created.relative_to(root)}")
        elif args.command == "validate":
            errors = validate(root)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print("Foundry records and references are valid.")
        elif args.command == "index":
            for path in generate_indexes(root):
                print(f"Wrote index: {path.relative_to(root)}")
        elif args.command == "export-catalog":
            content = (
                json.dumps(
                    export_catalog(root, args.include_drafts), indent=2
                )
                + "\n"
            )
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
