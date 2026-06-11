#!/usr/bin/env python3
"""Parse a LinkedIn single-post analytics XLSX export into compact JSON.

This script intentionally uses only Python's standard library. It reads the
simple worksheet structure LinkedIn exports for single-post analytics and
computes common post-performance rates.
"""

from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


KEYS = {
    "Post URL": "post_url",
    "Post Date": "post_date",
    "Post Publish Time": "post_publish_time",
    "Impressions": "impressions",
    "Members reached": "members_reached",
    "Profile viewers from this post": "profile_viewers",
    "Followers gained from this post": "followers_gained",
    "Social engagements": "social_engagements",
    "Reactions": "reactions",
    "Comments": "comments",
    "Reposts": "reposts",
    "Saves": "saves",
    "Sends on LinkedIn": "sends",
    "Link engagements": "link_engagements",
    "Premium custom button engagements": "premium_custom_button_engagements",
}


def cell_col(cell_ref: str) -> int:
    letters = re.match(r"[A-Z]+", cell_ref)
    if not letters:
        return 0
    col = 0
    for ch in letters.group(0):
        col = col * 26 + (ord(ch) - ord("A") + 1)
    return col


def read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        xml = zf.read("xl/sharedStrings.xml")
    except KeyError:
        return []
    root = ET.fromstring(xml)
    strings: list[str] = []
    for si in root.findall("a:si", NS):
        parts = [t.text or "" for t in si.findall(".//a:t", NS)]
        strings.append("".join(parts))
    return strings


def cell_value(cell: ET.Element, shared: list[str]) -> str | None:
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        text = cell.find(".//a:t", NS)
        return text.text if text is not None else None
    value = cell.find("a:v", NS)
    if value is None or value.text is None:
        return None
    if cell_type == "s":
        idx = int(value.text)
        return shared[idx] if idx < len(shared) else value.text
    return value.text


def read_rows(path: Path) -> list[list[str | None]]:
    with zipfile.ZipFile(path) as zf:
        shared = read_shared_strings(zf)
        sheet_name = "xl/worksheets/sheet1.xml"
        xml = zf.read(sheet_name)
    root = ET.fromstring(xml)
    rows: list[list[str | None]] = []
    for row in root.findall(".//a:sheetData/a:row", NS):
        values_by_col: dict[int, str | None] = {}
        for cell in row.findall("a:c", NS):
            ref = cell.attrib.get("r", "")
            col = cell_col(ref)
            values_by_col[col] = cell_value(cell, shared)
        max_col = max(values_by_col, default=0)
        rows.append([values_by_col.get(i) for i in range(1, max_col + 1)])
    return rows


def parse_int(value: str | None) -> int | None:
    if value is None:
        return None
    cleaned = re.sub(r"[^0-9-]", "", str(value))
    return int(cleaned) if cleaned not in ("", "-") else None


def parse_percent(value: str | None) -> float | str | None:
    if value is None:
        return None
    text = str(value).strip()
    if text.startswith("<"):
        return text
    if text.endswith("%"):
        try:
            return float(text[:-1]) / 100
        except ValueError:
            return text
    return text


def safe_rate(numerator: int | None, denominator: int | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def parse_export(rows: list[list[str | None]]) -> dict[str, Any]:
    metadata: dict[str, str] = {}
    metrics: dict[str, int] = {}
    demographics: dict[str, list[dict[str, Any]]] = {}
    in_demographics = False

    for row in rows:
        label = row[0] if len(row) > 0 else None
        value = row[1] if len(row) > 1 else None
        pct = row[2] if len(row) > 2 else None
        if label == "Category":
            in_demographics = True
            continue
        if not label:
            continue
        if in_demographics:
            demographics.setdefault(str(label), []).append({
                "value": value,
                "percent": parse_percent(pct),
            })
            continue
        key = KEYS.get(str(label))
        if not key:
            continue
        if key.startswith("post_"):
            metadata[key] = value or ""
        else:
            parsed = parse_int(value)
            if parsed is not None:
                metrics[key] = parsed

    impressions = metrics.get("impressions")
    reached = metrics.get("members_reached")
    engagements = metrics.get("social_engagements")
    profile_viewers = metrics.get("profile_viewers")

    rates = {
        "engagement_rate_by_impressions": safe_rate(engagements, impressions),
        "engagement_rate_by_reach": safe_rate(engagements, reached),
        "comment_rate_by_impressions": safe_rate(metrics.get("comments"), impressions),
        "reaction_rate_by_impressions": safe_rate(metrics.get("reactions"), impressions),
        "save_rate_by_impressions": safe_rate(metrics.get("saves"), impressions),
        "profile_view_rate_by_impressions": safe_rate(profile_viewers, impressions),
        "profile_view_rate_by_reach": safe_rate(profile_viewers, reached),
        "follower_conversion_from_profile_views": safe_rate(metrics.get("followers_gained"), profile_viewers),
        "comment_share_of_social_engagements": safe_rate(metrics.get("comments"), engagements),
        "reaction_share_of_social_engagements": safe_rate(metrics.get("reactions"), engagements),
        "save_share_of_social_engagements": safe_rate(metrics.get("saves"), engagements),
        "impressions_per_reached_member": safe_rate(impressions, reached),
    }

    return {
        "metadata": metadata,
        "metrics": metrics,
        "rates": rates,
        "demographics": demographics,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: analyze-linkedin-post-export.py path/to/linkedin-export.xlsx", file=sys.stderr)
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2
    rows = read_rows(path)
    parsed = parse_export(rows)
    print(json.dumps(parsed, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

