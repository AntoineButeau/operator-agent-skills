#!/usr/bin/env python3
"""Local repository validator for operator-agent-skills."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PACKS = 39
EXPECTED_SKILLS = 156
REQUIRED_SECTIONS = [
    "#",
    "## Use when",
    "## Inputs",
    "## Workflow",
    "## Output",
    "## Human review gates",
    "## Failure modes",
    "## Example prompt",
]
BANNED_PATTERNS = [
    "TO" + "DO",
    "TB" + "D",
    "FIX" + "ME",
    "place" + "holder",
    r"\[paste context\]",
    "lorem" + " ipsum",
]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - diagnostic path
        fail(errors, f"Invalid JSON at {path.relative_to(ROOT)}: {exc}")
        return {}


def yaml_field(text: str, field: str) -> str | None:
    match = re.search(rf'^\s*{re.escape(field)}:\s*["\']?([^"\'\n]+)["\']?\s*$', text, re.M)
    return match.group(1).strip() if match else None


def validate_skill(path: Path, errors: list[str]) -> None:
    text = path.read_text()
    lines = text.splitlines()
    headings = {line.strip() for line in lines if line.startswith("#")}
    if not lines or not lines[0].startswith("# "):
        fail(errors, f"{path.relative_to(ROOT)} must start with a level-one heading")
    for section in REQUIRED_SECTIONS[1:]:
        if section not in headings:
            fail(errors, f"{path.relative_to(ROOT)} missing required section {section}")


def validate_banned_strings(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(errors="ignore")
        for pattern in BANNED_PATTERNS:
            flags = re.I if pattern != r"\[paste context\]" else 0
            if re.search(pattern, text, flags):
                fail(errors, f"Banned draft marker found in {path.relative_to(ROOT)}: {pattern}")


def main() -> int:
    errors: list[str] = []
    packs_dir = ROOT / "packs"
    manifest_path = ROOT / "manifest.json"
    manifest = read_json(manifest_path, errors)

    pack_dirs = sorted(p for p in packs_dir.iterdir() if p.is_dir())
    if len(pack_dirs) != EXPECTED_PACKS:
        fail(errors, f"Expected {EXPECTED_PACKS} pack folders, found {len(pack_dirs)}")

    skills = sorted((ROOT / "packs").glob("*/skills/*.md"))
    if len(skills) != EXPECTED_SKILLS:
        fail(errors, f"Expected {EXPECTED_SKILLS} skill files, found {len(skills)}")

    if manifest:
        if manifest.get("pack_count") != len(pack_dirs):
            fail(errors, f"manifest pack_count {manifest.get('pack_count')} does not match {len(pack_dirs)}")
        if manifest.get("skill_count") != len(skills):
            fail(errors, f"manifest skill_count {manifest.get('skill_count')} does not match {len(skills)}")
        if len(manifest.get("packs", [])) != len(pack_dirs):
            fail(errors, f"manifest packs length {len(manifest.get('packs', []))} does not match {len(pack_dirs)}")

    manifest_pack_paths = set()
    for pack in manifest.get("packs", []):
        pack_path = ROOT / pack.get("path", "")
        manifest_pack_paths.add(pack_path.resolve())
        if not pack_path.exists():
            fail(errors, f"Manifest pack path missing: {pack.get('path')}")
            continue
        if pack.get("maturity") not in {"draft", "usable"}:
            fail(errors, f"Manifest pack {pack.get('id')} has invalid maturity {pack.get('maturity')}")
        if not (pack.get("ghost_series_status") or pack.get("ghost_series_url")):
            fail(errors, f"Manifest pack {pack.get('id')} missing Ghost series field")
        for skill in pack.get("skills", []):
            skill_path = pack_path / skill.get("path", "")
            if not skill_path.exists():
                fail(errors, f"Manifest skill path missing: {pack.get('path')}/{skill.get('path')}")

    for pack_dir in pack_dirs:
        for required in ["README.md", "pack.yaml", "skills"]:
            if not (pack_dir / required).exists():
                fail(errors, f"{pack_dir.relative_to(ROOT)} missing {required}")
        skill_files = sorted((pack_dir / "skills").glob("*.md"))
        if len(skill_files) < 3:
            fail(errors, f"{pack_dir.relative_to(ROOT)} has fewer than 3 skills")
        for skill_path in skill_files:
            validate_skill(skill_path, errors)

        yaml_path = pack_dir / "pack.yaml"
        if yaml_path.exists():
            y = yaml_path.read_text()
            if yaml_field(y, "maturity") not in {"draft", "usable"}:
                fail(errors, f"{yaml_path.relative_to(ROOT)} missing valid maturity")
            if not (yaml_field(y, "ghost_series_status") or yaml_field(y, "ghost_series_url")):
                fail(errors, f"{yaml_path.relative_to(ROOT)} missing Ghost series field")

        readme_path = pack_dir / "README.md"
        if readme_path.exists():
            readme = readme_path.read_text()
            pack_id = pack_dir.name.split("-", 1)[1]
            if f"examples/by-pack/{pack_id}.md" not in readme:
                fail(errors, f"{readme_path.relative_to(ROOT)} does not link to its example")
            if "## Ghost backlinks" not in readme:
                fail(errors, f"{readme_path.relative_to(ROOT)} missing Ghost backlinks section")

    validate_banned_strings(errors)

    if (ROOT / ".github" / "workflows").exists():
        fail(errors, ".github/workflows must not exist")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {len(pack_dirs)} packs, {len(skills)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
