#!/usr/bin/env python3
"""Lightweight citation guard for IRS evidence research answers.

The script does not prove that citations are correct. It catches common process
failures: no source section, no official URLs, and material-looking bullets that
lack a nearby source marker.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


OFFICIAL_PATTERNS = (
    "irs.gov",
    "uscode.house.gov",
    "ecfr.gov",
    "federalregister.gov",
    "ustaxcourt.gov",
)

CLAIM_PREFIXES = ("- ", "* ", "| ")
SOURCE_RE = re.compile(r"(Source:|https?://|IRC Section|Treas\. Reg\.|Publication|Instructions)", re.I)


def is_material_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith(CLAIM_PREFIXES):
        return False
    if stripped.startswith("| ---") or stripped.startswith("| Point") or stripped.startswith("| Claim"):
        return False
    if len(stripped) < 35:
        return False
    return any(word in stripped.lower() for word in (
        "must",
        "required",
        "deduct",
        "deductible",
        "tax",
        "file",
        "filing",
        "penalty",
        "threshold",
        "income",
        "expense",
        "credit",
        "exclusion",
        "limit",
        "deadline",
    ))


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    lowered = text.lower()
    if "## authorities" not in lowered and "source:" not in lowered:
        errors.append("Missing an Authorities section or Source markers.")

    if not any(pattern in lowered for pattern in OFFICIAL_PATTERNS):
        errors.append("No official-source URL found.")

    for idx, line in enumerate(lines, start=1):
        if not is_material_line(line):
            continue
        nearby = "\n".join(lines[max(0, idx - 2): min(len(lines), idx + 2)])
        if not SOURCE_RE.search(nearby):
            errors.append(f"Line {idx} looks like a material claim without a nearby source: {line.strip()}")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate-citations.py path/to/answer.md", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    errors = validate(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Citation guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
