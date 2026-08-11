#!/usr/bin/env python3
"""Dependency-free validation for the public governance repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "README.md",
    "GOVERNANCE.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "docs/launch.md",
    "docs/context.md",
    "docs/collaboration.md",
    "docs/model-routing.md",
    "prompts/supervisor.md",
    "prompts/manager.md",
    "prompts/researcher.md",
    "prompts/reviewer.md",
    "prompts/recovery.md",
    "prompts/lightweight-worker.md",
    "templates/campaign.yaml",
    "templates/task-lease.yaml",
    "templates/experiment.yaml",
    "templates/collaboration.yaml",
    "templates/checkpoint.yaml",
    "templates/discussion.yaml",
    "templates/decision.yaml",
}

FORBIDDEN = {
    "absolute personal path": re.compile(
        r"(?:/(?:Users|home)/[A-Za-z0-9._-]+(?:/|$)"
        r"|[A-Za-z]:\\(?:Users)\\[A-Za-z0-9._-]+(?:\\|$))",
        re.IGNORECASE,
    ),
    "login-style machine identity": re.compile(
        r"(?<![A-Za-z0-9._%+-])[A-Za-z0-9._-]+@"
        r"(?!v[0-9]+\b)[A-Za-z0-9_-]+"
        r"(?![A-Za-z0-9.-])"
    ),
    "credential-shaped token": re.compile(
        r"(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}"
        r"|AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}"
        r"|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9_-]{20,})"
    ),
    "private key material": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
    ),
}

LINE_LIMITS = {
    "README.md": 180,
    "GOVERNANCE.md": 420,
}

PROMPT_LINE_LIMIT = 90
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def repository_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    )


def validate_required(errors: list[str]) -> None:
    present = {path.relative_to(ROOT).as_posix() for path in repository_files()}
    for required in sorted(REQUIRED - present):
        errors.append(f"missing required file: {required}")


def validate_text(path: Path, errors: list[str]) -> None:
    relative = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return

    if text and not text.endswith("\n"):
        errors.append(f"{relative}: missing final newline")
    if "\t" in text:
        errors.append(f"{relative}: tab character found")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.rstrip() != line:
            errors.append(f"{relative}:{line_number}: trailing whitespace")

    # The validator necessarily contains the forbidden patterns it enforces.
    if relative != "scripts/validate.py":
        for label, pattern in FORBIDDEN.items():
            match = pattern.search(text)
            if match:
                errors.append(f"{relative}: contains {label}: {match.group(0)!r}")

        if re.search(r"\b(?:TODO|FIXME)\b", text):
            errors.append(f"{relative}: unresolved TODO or FIXME")

    if path.suffix == ".md":
        fence_count = sum(1 for line in text.splitlines() if line.startswith("```"))
        if fence_count % 2:
            errors.append(f"{relative}: unbalanced Markdown code fences")
        validate_links(path, text, errors)

    line_limit = LINE_LIMITS.get(relative)
    if line_limit and len(text.splitlines()) > line_limit:
        errors.append(
            f"{relative}: {len(text.splitlines())} lines exceeds {line_limit}"
        )
    if relative.startswith("prompts/") and len(text.splitlines()) > PROMPT_LINE_LIMIT:
        errors.append(
            f"{relative}: prompt exceeds {PROMPT_LINE_LIMIT} lines"
        )


def validate_links(path: Path, text: str, errors: list[str]) -> None:
    relative = path.relative_to(ROOT).as_posix()
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{relative}: link escapes repository: {raw_target}")
            continue
        if not resolved.exists():
            errors.append(f"{relative}: broken local link: {raw_target}")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    for path in repository_files():
        validate_text(path, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    files = repository_files()
    markdown = sum(path.suffix == ".md" for path in files)
    prompts = sum(path.parent.name == "prompts" for path in files)
    print(f"OK: {len(files)} files, {markdown} Markdown docs, {prompts} prompts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
