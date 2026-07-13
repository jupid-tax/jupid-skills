#!/usr/bin/env python3
"""Apply (or undo) a document move plan. Non-destructive by design.

Usage:
    python3 apply-move-plan.py plan.json --dry-run     # show what would happen (default)
    python3 apply-move-plan.py plan.json --execute     # move files, write undo log
    python3 apply-move-plan.py --undo undo-log-<ts>.json

Plan format (JSON):
    {
      "source_root": "/path/to/messy-folder",
      "target_root": "/path/to/messy-folder",      # optional, defaults to source_root
      "moves": [
        {"src": "IMG_2041.jpg", "dest_folder": "02 Receipts"},
        {"src": "scans/inv.pdf", "dest_folder": "01 Invoices", "dest_name": "inv.pdf"}
      ]
    }

Guarantees:
- never deletes, never overwrites (collisions get " (2)", " (3)"…);
- refuses any move that would land outside target_root or read outside
  source_root;
- every --execute writes an undo log and a moves-result-<ts>.json mapping each
  source file to its final location (feed it to build-index.py --moves), even
  if the run is interrupted mid-way.

Exit codes: 0 = clean; 2 = undo incomplete; 3 = some planned files were
missing or skipped (review the output before trusting the result).
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path


def is_within(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def collision_safe(dest: Path, taken: set) -> Path:
    n = 1
    candidate = dest
    while candidate.exists() or str(candidate) in taken:
        n += 1
        candidate = dest.with_name(f"{dest.stem} ({n}){dest.suffix}")
    taken.add(str(candidate))
    return candidate


def apply_plan(plan_path: Path, execute: bool) -> int:
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    source_root = Path(plan["source_root"]).expanduser().resolve()
    target_root = Path(plan.get("target_root", plan["source_root"])).expanduser().resolve()
    if not source_root.is_dir():
        print(f"error: source_root not found: {source_root}", file=sys.stderr)
        return 1

    moved, skipped, results, undo = [], [], [], []
    folder_counts: dict = {}
    taken: set = set()
    error = None

    try:
        for move in plan["moves"]:
            src = (source_root / move["src"]).resolve()
            if not is_within(src, source_root):
                skipped.append(f"{move['src']} — outside source root")
                continue
            if not src.is_file():
                skipped.append(f"{move['src']} — not found")
                continue

            dest_dir = (target_root / move["dest_folder"]).resolve()
            if not is_within(dest_dir, target_root):
                skipped.append(f"{move['src']} — dest folder escapes target root: "
                               f"{move['dest_folder']}")
                continue
            # Path(...).name strips any sneaky path separators in dest_name
            name = Path(move.get("dest_name", src.name)).name
            dest = collision_safe(dest_dir / name, taken)

            if execute:
                dest_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dest))
                undo.append({"from": str(dest), "to": str(src)})
            results.append({"src": move["src"],
                            "final": str(dest.relative_to(target_root))})
            folder_counts[move["dest_folder"]] = folder_counts.get(move["dest_folder"], 0) + 1
            moved.append(move["src"])
    except Exception as exc:  # keep the undo log even on a mid-run crash
        error = exc
    finally:
        if execute and undo:
            ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
            undo_path = (plan_path.parent / f"undo-log-{ts}.json").resolve()
            undo_path.write_text(json.dumps(undo, indent=2, ensure_ascii=False),
                                 encoding="utf-8")
            result_path = (plan_path.parent / f"moves-result-{ts}.json").resolve()
            result_path.write_text(json.dumps(results, indent=2, ensure_ascii=False),
                                   encoding="utf-8")

    mode = "MOVED" if execute else "DRY RUN — would move"
    print(f"{mode}: {len(moved)} files")
    for folder in sorted(folder_counts):
        print(f"  {folder}: {folder_counts[folder]}")
    if skipped:
        print(f"skipped: {len(skipped)}")
        for s in skipped:
            print(f"  ! {s}")
    if execute and undo:
        script = Path(sys.argv[0]).resolve()
        print(f"undo log → {undo_path}")
        print(f"result map → {result_path}")
        print(f'to revert: python3 "{script}" --undo "{undo_path}"')
    if error is not None:
        print(f"error: run interrupted: {error}", file=sys.stderr)
        return 1
    return 3 if skipped else 0


def undo_run(log_path: Path) -> int:
    entries = json.loads(log_path.read_text(encoding="utf-8"))
    restored, failed, emptied_dirs = 0, [], set()
    for entry in reversed(entries):
        src, dest = Path(entry["from"]), Path(entry["to"])
        if not src.is_file():
            failed.append(f"missing: {src}")
            continue
        if dest.exists():
            failed.append(f"occupied: {dest}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dest))
        emptied_dirs.add(src.parent)
        restored += 1
    # remove category folders the run created, if now empty
    for folder in sorted(emptied_dirs, key=lambda p: len(p.parts), reverse=True):
        try:
            folder.rmdir()  # only succeeds when empty
        except OSError:
            pass
    print(f"restored {restored} of {len(entries)} files")
    for f in failed:
        print(f"  ! {f}")
    return 0 if not failed else 2


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("plan", nargs="?", help="plan.json")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--dry-run", action="store_true", help="preview only (default)")
    group.add_argument("--execute", action="store_true", help="actually move files")
    group.add_argument("--undo", metavar="UNDO_LOG", help="revert a previous run")
    args = ap.parse_args()

    if args.undo:
        return undo_run(Path(args.undo))
    if not args.plan:
        ap.error("plan.json required (or --undo)")
    return apply_plan(Path(args.plan), execute=args.execute)


if __name__ == "__main__":
    sys.exit(main())
