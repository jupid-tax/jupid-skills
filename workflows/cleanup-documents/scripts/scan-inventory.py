#!/usr/bin/env python3
"""Inventory a document folder: list files, extract text layers, find duplicates.

Usage:
    python3 scan-inventory.py /path/to/folder [--out inventory.json]
        [--top-level] [--exclude PATTERN ...] [--max-hash-mb 100] [--max-chars 1500]

Options:
    --top-level     scan only loose files at the top level (recommended first
                    pass; existing subfolders usually carry structure)
    --exclude       glob pattern for folder/file names to skip (repeatable),
                    e.g. --exclude "Codex" --exclude "*.bak"
    --max-hash-mb   files larger than this get a fast partial fingerprint
                    (first 4 MB + size) instead of a full hash (default 100)

Skipped automatically: hidden files, system files (.DS_Store etc.),
Office lock files (~$…), workspace folders (.git, node_modules, __pycache__,
.venv, venv), and top-level category folders from a previous cleanup run
(names like "01 Invoices" / "07 Needs Review") — so re-runs only pick up new
loose files.

Produces a JSON inventory consumed by the cleanup-documents skill. Pure
standard library; if `pypdf` (or `PyPDF2`) is installed, digital PDFs get a
text excerpt — otherwise they are flagged for visual reading by the agent.
Nothing is modified: this script only reads. Progress goes to stderr.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import logging
import re
import sys
import warnings
import zipfile
from datetime import datetime, timezone
from pathlib import Path

DOCUMENT_EXTS = {
    ".pdf": "pdf",
    ".png": "image", ".jpg": "image", ".jpeg": "image", ".heic": "image",
    ".tif": "image", ".tiff": "image", ".webp": "image", ".bmp": "image", ".gif": "image",
    ".docx": "word", ".doc": "word", ".rtf": "word", ".odt": "word", ".pages": "word",
    ".xlsx": "spreadsheet", ".xls": "spreadsheet", ".csv": "spreadsheet",
    ".numbers": "spreadsheet", ".ods": "spreadsheet",
    ".txt": "text", ".md": "text", ".eml": "email", ".msg": "email",
}

SYSTEM_FILES = {".ds_store", "thumbs.db", "desktop.ini", "icon\r", ".localized"}
WORKSPACE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
# top-level folders created by a previous cleanup run: "01 Invoices" etc.
CATEGORY_DIR_RE = re.compile(r"^\d{2}[ .-]")


def load_pdf_reader():
    """Return a PdfReader class from pypdf or PyPDF2, or None."""
    warnings.filterwarnings("ignore")
    for logger_name in ("pypdf", "PyPDF2"):
        logging.getLogger(logger_name).setLevel(logging.CRITICAL)
    try:
        from pypdf import PdfReader  # type: ignore
        return PdfReader
    except ImportError:
        pass
    try:
        from PyPDF2 import PdfReader  # type: ignore
        return PdfReader
    except ImportError:
        return None


def fingerprint(path: Path, max_hash_bytes: int) -> tuple:
    """Return (digest, hash_type). Large files get a partial fingerprint."""
    size = path.stat().st_size
    h = hashlib.sha256()
    if size > max_hash_bytes:
        with path.open("rb") as f:
            h.update(f.read(4 << 20))
        return f"partial-{size}-{h.hexdigest()}", "partial"
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest(), "full"


def clean_text(text: str, max_chars: int) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text[:max_chars]


def pdf_excerpt(path: Path, reader_cls, max_chars: int, max_pages: int = 2):
    """Return (excerpt, encrypted, page_count). Excerpt is None on failure."""
    if reader_cls is None:
        return None, False, None
    try:
        reader = reader_cls(str(path))
        if getattr(reader, "is_encrypted", False):
            return None, True, None
        pages = reader.pages
        chunks = []
        for page in pages[:max_pages]:
            chunks.append(page.extract_text() or "")
        text = clean_text("\n".join(chunks), max_chars)
        return (text if text else None), False, len(pages)
    except Exception:
        return None, False, None


def docx_excerpt(path: Path, max_chars: int):
    """Extract text from a .docx via stdlib zipfile — no dependencies."""
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="replace")
        # paragraph breaks, then strip tags
        xml = re.sub(r"</w:p>", "\n", xml)
        text = re.sub(r"<[^>]+>", "", xml)
        text = clean_text(text, max_chars)
        return text if text else None
    except Exception:
        return None


def text_excerpt(path: Path, max_chars: int):
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            return clean_text(f.read(max_chars * 4), max_chars) or None
    except Exception:
        return None


def excluded(rel_parts: tuple, name: str, patterns: list,
             category_exclude: bool) -> bool:
    for part in rel_parts:
        if part.startswith(".") or part.lower() in WORKSPACE_DIRS:
            return True
        if any(fnmatch.fnmatch(part, p) for p in patterns):
            return True
    # category folders from a previous run: only at the top level
    if category_exclude and len(rel_parts) > 1 and CATEGORY_DIR_RE.match(rel_parts[0]):
        return True
    return name.startswith("~$")


def excluded_top_dirs(root: Path, patterns: list, category_exclude: bool) -> list:
    """Top-level directories the scan will skip — reported, never silent."""
    out = []
    for path in sorted(root.iterdir()):
        if not path.is_dir():
            continue
        name = path.name
        if name.startswith(".") or name.lower() in WORKSPACE_DIRS:
            reason = "hidden/workspace"
        elif any(fnmatch.fnmatch(name, p) for p in patterns):
            reason = "matches --exclude"
        elif category_exclude and CATEGORY_DIR_RE.match(name):
            reason = "looks like a category folder from a previous run " \
                     "(rescan with --no-category-exclude to include it)"
        else:
            continue
        out.append({"dir": name, "reason": reason})
    return out


def collect_paths(root: Path, top_level: bool, patterns: list,
                  category_exclude: bool) -> list:
    paths = []
    candidates = sorted(root.iterdir()) if top_level else sorted(root.rglob("*"))
    for path in candidates:
        if not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if excluded(rel_parts, path.name, patterns, category_exclude):
            continue
        if path.name.lower() in SYSTEM_FILES:
            continue
        paths.append(path)
    return paths


def scan(root: Path, top_level: bool, patterns: list,
         max_chars: int, max_hash_mb: int, category_exclude: bool) -> dict:
    reader_cls = load_pdf_reader()
    max_hash_bytes = max_hash_mb << 20
    paths = collect_paths(root, top_level, patterns, category_exclude)
    files, skipped = [], []

    for i, path in enumerate(paths, start=1):
        if i % 25 == 0 or i == len(paths):
            print(f"  …scanned {i}/{len(paths)}", file=sys.stderr)

        ext = path.suffix.lower()
        kind = DOCUMENT_EXTS.get(ext)
        rel = str(path.relative_to(root))
        if kind is None:
            skipped.append(rel)
            continue

        digest, hash_type = fingerprint(path, max_hash_bytes)
        entry = {
            "path": rel,
            "ext": ext,
            "kind": kind,
            "size": path.stat().st_size,
            "mtime": datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
                     .strftime("%Y-%m-%d"),
            "sha256": digest,
            "hash_type": hash_type,
            "text_excerpt": None,
            "needs_visual_read": False,
            "encrypted": False,
            "pdf_pages": None,
        }

        if kind == "pdf":
            excerpt, encrypted, pages = pdf_excerpt(path, reader_cls, max_chars)
            entry.update(text_excerpt=excerpt, encrypted=encrypted, pdf_pages=pages)
            entry["needs_visual_read"] = excerpt is None and not encrypted
        elif kind == "word" and ext == ".docx":
            excerpt = docx_excerpt(path, max_chars)
            entry["text_excerpt"] = excerpt
            entry["needs_visual_read"] = excerpt is None
        elif kind in ("text", "email") or ext == ".csv":
            entry["text_excerpt"] = text_excerpt(path, max_chars)
        elif kind == "image":
            entry["needs_visual_read"] = True
        else:  # other word/spreadsheet formats: agent opens them itself
            entry["needs_visual_read"] = True

        files.append(entry)

    # duplicate groups by fingerprint; partial-hash collisions are re-checked
    # with a full hash so "duplicate" always means byte-identical
    by_hash: dict = {}
    for entry in files:
        by_hash.setdefault(entry["sha256"], []).append(entry)
    group_id = 0
    for key, twins in sorted(by_hash.items()):
        if len(twins) < 2:
            twins[0]["duplicate_group"] = None
            continue
        if key.startswith("partial-"):
            confirmed: dict = {}
            for entry in twins:
                full = hashlib.sha256((root / entry["path"]).read_bytes()).hexdigest()
                confirmed.setdefault(full, []).append(entry)
            subgroups = confirmed.values()
        else:
            subgroups = [twins]
        for subgroup in subgroups:
            if len(subgroup) > 1:
                group_id += 1
                for entry in subgroup:
                    entry["duplicate_group"] = group_id
            else:
                subgroup[0]["duplicate_group"] = None

    return {
        "root": str(root),
        "scope": "top-level" if top_level else "recursive",
        "excluded_dirs": excluded_top_dirs(root, patterns, category_exclude),
        "file_count": len(files),
        "needs_visual_read": sum(1 for f in files if f["needs_visual_read"]),
        "encrypted": sum(1 for f in files if f["encrypted"]),
        "duplicate_groups": group_id,
        "pdf_text_extraction": "available" if reader_cls else
            "unavailable (pip install pypdf to speed up digital PDFs)",
        "skipped_non_documents": skipped,
        "files": files,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("folder", help="folder to inventory (read-only)")
    ap.add_argument("--out", default="inventory.json", help="output JSON path")
    ap.add_argument("--top-level", action="store_true",
                    help="scan only loose top-level files, ignore subfolders")
    ap.add_argument("--exclude", action="append", default=[], metavar="PATTERN",
                    help="glob pattern of folder/file names to skip (repeatable)")
    ap.add_argument("--max-hash-mb", type=int, default=100,
                    help="partial fingerprint for files larger than this (MB)")
    ap.add_argument("--max-chars", type=int, default=1500,
                    help="max chars of text excerpt per file")
    ap.add_argument("--no-category-exclude", action="store_true",
                    help="also scan top-level folders that look like category "
                         "folders from a previous run (NN ...)")
    args = ap.parse_args()

    root = Path(args.folder).expanduser().resolve()
    if not root.is_dir():
        print(f"error: not a folder: {root}", file=sys.stderr)
        return 1

    inventory = scan(root, args.top_level, args.exclude,
                     args.max_chars, args.max_hash_mb,
                     category_exclude=not args.no_category_exclude)
    Path(args.out).write_text(json.dumps(inventory, indent=2, ensure_ascii=False),
                              encoding="utf-8")

    print(f"{inventory['file_count']} documents inventoried, {inventory['scope']} "
          f"({inventory['needs_visual_read']} need visual reading, "
          f"{inventory['encrypted']} encrypted, "
          f"{inventory['duplicate_groups']} duplicate groups, "
          f"{len(inventory['skipped_non_documents'])} non-documents skipped)")
    for item in inventory["excluded_dirs"]:
        print(f"  excluded dir: {item['dir']} — {item['reason']}")
    print(f"→ {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
