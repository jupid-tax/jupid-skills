#!/usr/bin/env python3
"""Inventory a document folder: list files, extract text layers, find duplicates.

Usage:
    python3 scan-inventory.py /path/to/folder [--out inventory.json] [--max-chars 1500]

Produces a JSON inventory consumed by the cleanup-documents skill. Pure
standard library; if `pypdf` (or `PyPDF2`) is installed, digital PDFs get a
text excerpt — otherwise they are flagged for visual reading by the agent.
Nothing is modified: this script only reads.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
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

SYSTEM_FILES = {".ds_store", "thumbs.db", "desktop.ini", "icon\r"}


def load_pdf_reader():
    """Return a PdfReader class from pypdf or PyPDF2, or None."""
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


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


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


def scan(root: Path, max_chars: int) -> dict:
    reader_cls = load_pdf_reader()
    files, skipped = [], []

    for path in sorted(root.rglob("*")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        if not path.is_file() or path.name.lower() in SYSTEM_FILES:
            continue

        ext = path.suffix.lower()
        kind = DOCUMENT_EXTS.get(ext)
        rel = str(path.relative_to(root))
        if kind is None:
            skipped.append(rel)
            continue

        entry = {
            "path": rel,
            "ext": ext,
            "kind": kind,
            "size": path.stat().st_size,
            "mtime": datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
                     .strftime("%Y-%m-%d"),
            "sha256": sha256_of(path),
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

    # duplicate groups by checksum
    by_hash: dict[str, list[dict]] = {}
    for entry in files:
        by_hash.setdefault(entry["sha256"], []).append(entry)
    group_id = 0
    for twins in by_hash.values():
        if len(twins) > 1:
            group_id += 1
            for entry in twins:
                entry["duplicate_group"] = group_id
        else:
            twins[0]["duplicate_group"] = None

    return {
        "root": str(root),
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
    ap.add_argument("--max-chars", type=int, default=1500,
                    help="max chars of text excerpt per file")
    args = ap.parse_args()

    root = Path(args.folder).expanduser().resolve()
    if not root.is_dir():
        print(f"error: not a folder: {root}", file=sys.stderr)
        return 1

    inventory = scan(root, args.max_chars)
    Path(args.out).write_text(json.dumps(inventory, indent=2, ensure_ascii=False),
                              encoding="utf-8")

    print(f"{inventory['file_count']} documents inventoried "
          f"({inventory['needs_visual_read']} need visual reading, "
          f"{inventory['encrypted']} encrypted, "
          f"{inventory['duplicate_groups']} duplicate groups, "
          f"{len(inventory['skipped_non_documents'])} non-documents skipped)")
    print(f"→ {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
