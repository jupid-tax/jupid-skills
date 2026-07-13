---
name: cleanup-documents
description: >
  Use this skill when a business owner, solopreneur, accountant, or bookkeeper
  has a messy local folder of documents (invoices, receipts, bank statements,
  tax forms, contracts, scans, photos of paper) and wants an agent to read each
  document, propose a folder structure, and sort every file into the right
  folder — optionally producing an Excel/CSV index of what went where.
  Triggers on phrases like "clean up my documents", "organize these files",
  "sort my invoices", "my downloads folder is a mess", "put receipts in
  folders", "organize my tax documents", "OCR these scans and file them",
  "make a document index", or "which of these files are invoices".
  Do NOT use this skill to interpret documents for tax advice or bookkeeping
  entries; use it to physically organize local files and index them.
workflow: Cleanup documents
audience: [accounting, bookkeeping, tax, small-business, solopreneur, admin]
last_verified: 2026-07-13
---

# Cleanup Documents

This skill turns an agent into a local document-filing clerk. The agent reads
every document in a messy folder (digital PDFs, scans, photos, office files),
agrees on a folder structure with the user, sorts each file into the right
folder, and — if the user wants — delivers a spreadsheet index describing every
recognized document and where it was filed.

Everything runs locally. Files are moved, never deleted, and every run writes
an undo log that can restore the original layout in one command.

---

## Use from GitHub

Canonical public link:

```text
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/cleanup-documents
```

When a user gives this GitHub link and asks to use or install the skill, first
determine the current runtime:

- If you are running in Codex, treat this as a Codex skill.
- If you are running in Claude Code, treat this as a Claude Code skill.
- If the runtime is unclear, ask one short question: "Are you using Codex or
  Claude Code?"

Do not make the user choose a different GitHub link. The same repository folder
is the source for both runtimes.

For one-off use without installation, read this `SKILL.md`, then load the
reference files only when needed for the user's task.

For repeated local use:

```bash
# Codex
mkdir -p ~/.codex/skills
cp -r workflows/cleanup-documents ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -r workflows/cleanup-documents ~/.claude/skills/
```

---

## Core rules

1. **Never delete, never overwrite.** Files are only moved (or copied if the
   user prefers). Name collisions get a numeric suffix. Every run writes an
   undo log; tell the user how to revert.
2. **Every classification states its basis.** "Invoice — has invoice number
   INV-2041, bill-to block, amount due $1,250" — not just "looks like an
   invoice". Files the agent cannot read or confidently classify go to
   `Needs Review`, never silently guessed into a category.
3. **Confirm before touching files.** The folder structure is agreed first,
   and a move plan summary is shown before anything is physically moved.
4. **Documents stay local.** The agent reads files on the user's machine.
   Never upload documents to external services, and never ask the user to
   paste document contents into a hosted chat.

---

## When to invoke

Engage this skill when the user asks to:

- clean up / organize a folder of mixed documents;
- separate invoices from receipts, statements, and other paperwork;
- OCR scans or photos of paper documents and file them;
- prepare a document folder for an accountant, bookkeeper, or tax filing;
- build an index / register of what documents exist;
- find duplicates in a document folder.

Do not engage this skill when:

- the user wants bookkeeping entries, tax conclusions, or data extraction into
  an accounting system (organize first; that is a separate task);
- the target is email inboxes or cloud drives via API rather than a local
  folder (the skill works on local files);
- the user wants to organize code, photos, or media libraries (different
  taxonomy; this skill's taxonomy is business documents).

---

## Workflow

Execute these steps in order. For the exact conversational script, load
[`references/dialogue-playbook.md`](./references/dialogue-playbook.md).

### Step 1 — Scan the source folder

Ask for the folder path if not given. Then build an inventory:

```bash
python3 scripts/scan-inventory.py "/path/to/messy-folder" --out inventory.json
```

The script walks the folder, extracts the text layer from documents (DOCX
needs nothing; digital PDFs use `pypdf` if installed, otherwise they are
flagged for visual reading), hashes every file to detect duplicates, and
flags scans/photos that have no text layer as `needs_visual_read`.

Do not classify anything yet. The inventory is input for the next two steps.

### Step 2 — Propose a folder structure

Propose the default structure, adjusted to what the inventory actually
contains (drop folders with no matching documents, add ones that are clearly
needed):

```text
01 Invoices              — bills you received and invoices you issued
02 Receipts              — purchase receipts, expense proofs
03 Bank & Card Statements
04 Tax Documents         — IRS/state forms, notices, filings
05 Payroll               — paystubs, W-2/1099 forms, payroll reports
06 Contracts & Legal     — agreements, leases, insurance policies
07 Needs Review          — unreadable, ambiguous, or uncategorized
```

Ask the user to confirm or adjust: rename folders, add/remove categories,
split invoices into issued vs. received, add year subfolders. Wait for
explicit confirmation before proceeding. For taxonomy variants and naming
rules, load [`references/folder-taxonomy.md`](./references/folder-taxonomy.md).

### Step 3 — Read and classify every document

For each file in the inventory:

- If it has a text excerpt, classify from the text.
- If it is flagged `needs_visual_read` (scan, photo, image-only PDF), open and
  read the file directly — the agent's own vision is the OCR engine. No
  external OCR service or API key is needed.
- Apply the decision rules in
  [`references/classification-rules.md`](./references/classification-rules.md).
- Record for every file: category, document type, counterparty, document date,
  amount (if any), a one-line **basis** for the classification, and a
  confidence level.

Anything below high confidence goes to `Needs Review` with a note. For large
folders, work in batches of 20–30 files and report progress.

Write the results to `manifest.json` (schema in
[`references/classification-rules.md`](./references/classification-rules.md))
and derive `plan.json` from it.

### Step 4 — Show the plan, then move

Show the user a short summary before touching anything:

- file count per target folder;
- the full list of `Needs Review` files with reasons;
- duplicate groups found (duplicates are filed together, never deleted).

Then execute:

```bash
python3 scripts/apply-move-plan.py plan.json --dry-run   # verify
python3 scripts/apply-move-plan.py plan.json --execute   # move files
```

The script creates target folders, moves files with collision-safe naming,
refuses any destination outside the target root, and writes two files next to
`plan.json`: `undo-log-<timestamp>.json` and `moves-result-<timestamp>.json`
(the source → final-path map used by the index in Step 6). Exit code 3 means
some planned files were skipped — re-check before proceeding. To revert a run:

```bash
python3 scripts/apply-move-plan.py --undo undo-log-<timestamp>.json
```

### Step 5 — Ask what the deliverable is

Ask one question:

```text
Folders are done. Do you also want a spreadsheet index of every recognized
document (file, category, counterparty, date, amount, where it was filed)?
Excel or CSV?
```

### Step 6 — Deliver

If the user wants an index:

```bash
python3 scripts/build-index.py manifest.json --xlsx "Document Index.xlsx" \
    --moves moves-result-<timestamp>.json
# or --csv "document-index.csv" (no dependencies)
```

Always pass `--moves` with the file written by Step 4 — without it the "Filed
To" column shows planned paths, not the real ones (collision renames, year
subfolders). Excel output needs `openpyxl`; if it is not installed the script
says so and falls back to CSV. The index includes one row per document plus a
summary sheet with counts per category.

Close with: final counts per folder, the `Needs Review` list, the undo
command, and the index location.

---

## Output format

The final message to the user should follow:

```markdown
## Done — [N] documents organized

| Folder | Files |
|--------|-------|
| 01 Invoices | 34 |
| ... | ... |
| 07 Needs Review | 3 |

## Needs your attention
- `scan_004.jpg` — blurry photo, could not read; left in Needs Review.

## Index
Document Index.xlsx — one row per document with category, date, amount, basis.

## Undo
python3 scripts/apply-move-plan.py --undo undo-log-2026-07-13T14-02-11.json
```

---

## Edge cases

- **Password-protected PDFs** — do not attempt to crack; file to
  `Needs Review`, note "password-protected".
- **Multi-document PDFs** (one PDF containing several receipts) — classify by
  the dominant content, note "bundle" in the manifest; offer splitting as a
  follow-up task, do not split silently.
- **Duplicates** — the inventory detects exact duplicates by checksum. File
  all copies to the same folder and flag the group in the manifest and index.
  Never delete duplicates without explicit instruction.
- **Already-organized subfolders** — ask before flattening. Default is to
  leave existing well-named subfolders untouched and organize only loose files.
- **Cloud-synced folders** (Dropbox, Google Drive, OneDrive) — moves are
  normal file operations and sync fine, but warn the user to let sync finish
  before judging results on another device.
- **Non-document files** (apps, archives, media) — leave in place, list them
  in the closing summary as "not documents, not touched".

---

## Privacy rules

- Documents are read locally and stay local. Nothing is uploaded.
- The index spreadsheet contains document metadata (dates, amounts,
  counterparties). Tell the user it inherits the sensitivity of the documents
  and should be stored alongside them.
- Do not read more of each document than classification requires.
- If the session runs in a hosted environment where local files are actually
  remote uploads, say so explicitly before scanning.

---

## Examples

- [`examples/cleanup-request.md`](./examples/cleanup-request.md)
  — copy-paste request for a messy-folder cleanup.
- [`examples/example-output.md`](./examples/example-output.md)
  — compact example of a full run: proposal, confirmation, move summary, index.
