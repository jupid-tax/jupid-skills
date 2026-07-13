---
name: cleanup-documents
description: >
  Use this skill when a business owner, solopreneur, accountant, or bookkeeper
  has a messy local folder of documents (invoices, receipts, bank statements,
  tax forms, contracts, identity documents, scans, photos of paper) and wants
  an agent to read each document, propose a folder structure, and sort every
  file into the right folder — by moving or by making verified copies — and
  optionally produce an Excel/CSV index of what went where.
  Triggers on phrases like "clean up my documents", "organize these files",
  "sort my invoices", "my downloads folder is a mess", "put receipts in
  folders", "organize my tax documents", "OCR these scans and file them",
  "make a document index", "make copies into folders", or "which of these
  files are invoices".
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
folder — moving or copying, the user chooses — and, if the user wants,
delivers a spreadsheet index describing every recognized document and where
it was filed.

Everything runs locally. Files are never deleted, never overwritten, and
every run writes an undo log that can restore the original layout in one
command.

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

1. **Never delete, never overwrite.** Files are moved or copied, per the
   user's choice. Name collisions get a numeric suffix. Every run writes an
   undo log; tell the user how to revert. Copy-mode undo removes only
   checksum-verified unchanged copies created by that run.
2. **Every classification states its basis.** "Invoice — has invoice number
   INV-2041, bill-to block, amount due $1,250" — not just "looks like an
   invoice". Files the agent cannot read or confidently classify go to
   `Needs Review`, never silently guessed into a category.
3. **Every decision gate is an option menu.** Scope, structure, mode,
   deliverable — each is presented as short numbered options with one
   recommended default, so the user picks instead of composing an answer.
   Nothing touches the file system before the structure, mode, and plan are
   confirmed.
4. **Documents stay local.** The agent reads files on the user's machine.
   Never upload documents to external services, and never ask the user to
   paste document contents into a hosted chat.
5. **Speak the user's language.** Dialogue, folder names, the index, and the
   closing summary follow the language the user writes in. Default folder
   names are English; translate them in the proposal when the user writes in
   another language.
6. **Always say where things are.** After any file-system change, give the
   absolute path to what was created or changed, and say explicitly what the
   user will see there (e.g. "the folders exist but are empty until you
   approve the plan").

## Presenting option menus

In Claude Code, use the native question dialog (AskUserQuestion) when it is
available. In Codex — or when no dialog tool exists — print a compact
numbered list. Either way:

- 2–4 options per gate, one marked **(recommended)**;
- the user can answer with a number, or free text that overrides the menu;
- "go ahead" / "давай" means: accept the recommended option and continue;
- one decision per message (the mode + naming gate below is the one
  deliberate exception).

The exact menu texts live in
[`references/dialogue-playbook.md`](./references/dialogue-playbook.md).

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
  taxonomy; this skill's taxonomy is documents).

---

## Workflow

Execute these steps in order. For the exact conversational script and menu
texts, load
[`references/dialogue-playbook.md`](./references/dialogue-playbook.md).

Keep all operational artifacts (`inventory.json`, `manifest.json`,
`plan.json`, undo logs) in your session's working area — never inside the
folder being cleaned.

### Step 1 — Locate and scope (Gate 1)

Ask for the folder path if not given. Run a fast top-level scan first:

```bash
python3 scripts/scan-inventory.py "/path/to/folder" --top-level --out inventory.json
```

Then present the **scope menu**: organize only loose top-level files
(recommended — existing subfolders usually carry structure someone chose),
include subfolders too, or a specific subfolder only. If the user includes
subfolders, rescan without `--top-level`; add `--exclude` patterns for
workspace folders. The scanner skips `.git`, `node_modules`, and previously
created category folders automatically, caps hashing of huge files, and
reports progress on stderr.

The inventory's `excluded_dirs` field lists every top-level folder the scan
skipped and why — show it at the scope gate so nothing is silently out of
scope. If a folder was wrongly treated as a previous run's category folder
(e.g. a user folder named `01.03.2024 scans`), rescan with
`--no-category-exclude` or an adjusted `--exclude`.

### Step 2 — Propose a structure (Gate 2)

Pick the preset that matches the inventory and present the **structure
menu**:

1. **Business / accounting** — the flat 7-folder default (invoices, receipts,
   statements, tax, payroll, contracts, needs-review). Recommended when the
   folder is business paperwork.
2. **Personal + business** — a two-level structure (Finance & Tax; Business &
   Legal; Employment & Recruitment; Identity, Immigration & Personal;
   Education & Family; Health, Travel & Insurance; Needs Review). Recommended
   when the scan shows identity documents, medical papers, CVs, or school
   files mixed in.
3. **Accountant multi-client** — client-name folders on top, a business
   taxonomy inside each.
4. **Custom** — the user describes it, the agent drafts it.

Show the full proposed tree for the recommended preset (adjusted to what the
inventory actually contains — drop empty categories, renumber contiguously),
and ask to confirm or adjust. Wait for explicit confirmation. Details and
variants: [`references/folder-taxonomy.md`](./references/folder-taxonomy.md).

### Step 3 — Mode and naming (Gate 3)

One message, two quick settings:

- **Mode**: copy — a safe trial, originals stay untouched, verified copies go
  into the new structure (recommended for a first run); move — originals are
  relocated; report only — classify and index, touch nothing.
- **File naming**: keep original names (default) or standardize to
  `YYYY-MM-DD Counterparty Type.ext`.

### Step 4 — Read and classify every document

For each file in the inventory:

- If it has a text excerpt, classify from the text.
- If it is flagged `needs_visual_read` (scan, photo, image-only PDF), open and
  read the file directly — the agent's own vision is the OCR engine. No
  external OCR service or API key is needed.
- Apply the decision rules in
  [`references/classification-rules.md`](./references/classification-rules.md).
- Record for every file: category (full target path), section/subcategory for
  two-level structures, document type, counterparty, document date, amount
  (if any), a one-line **basis** for the classification, and a confidence
  level.

Anything below high confidence goes to `Needs Review` — into its
`Unreadable`, `Password-Protected`, or `Ambiguous` subfolder, with a note.
For large folders, work in batches of 20–30 files and report progress. If
telling issued from received invoices matters, ask for the user's business
name once, early.

Write the results to `manifest.json` (schema in
[`references/classification-rules.md`](./references/classification-rules.md))
and derive `plan.json` from it.

### Step 5 — Show the plan, handle misfits, then apply (Gate 4)

Show the user a short summary before touching anything:

- file count per target folder;
- the full list of `Needs Review` files with reasons;
- duplicate groups found (duplicates are filed together, never deleted);
- **misfit clusters**: if 2+ documents of the same kind fit no confirmed
  category (concert tickets, magazine articles, personal photos), propose a
  new folder for them instead of dumping them in Needs Review — one menu:
  add the folder / leave in Needs Review / decide per file.

Then execute (add `--copy` when the user chose copy mode):

```bash
python3 scripts/apply-move-plan.py plan.json --copy --dry-run   # verify
python3 scripts/apply-move-plan.py plan.json --copy --execute   # apply
```

The script creates target folders, applies the plan with collision-safe
naming, refuses any destination outside the target root, verifies copies by
checksum, and writes two files next to `plan.json`:
`undo-log-<timestamp>.json` and `moves-result-<timestamp>.json` (the
source → final-path map used by the index in Step 7). Exit code 3 means some
planned files were skipped — re-check before proceeding. To revert a run:

```bash
python3 scripts/apply-move-plan.py --undo undo-log-<timestamp>.json
```

Move-mode undo restores files to their original places; copy-mode undo
deletes only copies whose checksum still matches the log (a copy the user
edited is kept and reported).

After applying, give the absolute path to the organized folder.

### Step 6 — Ask what the deliverable is (Gate 5)

One menu: Excel index (recommended) / CSV index / both / none — plus an
optional **audit log** (a Markdown run report: what was scanned, what the
user approved, counts, artifacts, the undo command). Index headers localize
to English or Russian via `--lang`; for other languages the script writes
English headers — rename them afterwards if the user wants.

### Step 7 — Deliver

If the user wants an index:

```bash
python3 scripts/build-index.py manifest.json --xlsx "Document Index.xlsx" \
    --moves moves-result-<timestamp>.json --lang en
```

Always pass `--moves` with the file written by Step 5 — without it the "Filed
To" column shows planned paths, not the real ones (collision renames, year
subfolders). Exception: in report-only mode nothing was applied, so omit
`--moves` and tell the user "Filed To" shows *planned* destinations.
`--lang ru` localizes headers and sheet names. Excel output
needs `openpyxl`; if it is not installed the script says so and falls back to
CSV. The index includes one row per document plus a summary sheet with counts
per category.

If the user wants the audit log, write it yourself as Markdown next to the
index: scope and approvals, counts per folder, Needs Review list, artifact
paths, undo command. No document contents — filenames and metadata only.

Close with: final counts per folder, the absolute path to the structure, the
`Needs Review` list, the undo command, and the index location.

---

## Output format

The final message to the user should follow (in the user's language):

```markdown
## Done — [N] documents organized (copies; originals untouched)

Everything is in /Users/anna/Documents — folders 01–07.

| Folder | Files |
|--------|-------|
| 01 Invoices | 34 |
| ... | ... |
| 07 Needs Review | 3 |

## Needs your attention
- `scan_004.jpg` — blurry photo, could not read; in 07 Needs Review/Unreadable.

## Index
Document Index.xlsx — one row per document with category, date, amount, basis.

## Undo
python3 scripts/apply-move-plan.py --undo undo-log-2026-07-13T14-02-11.json
(removes only the verified copies created by this run)
```

---

## Edge cases

- **Password-protected PDFs** — do not attempt to crack; file to
  `Needs Review/Password-Protected`, note it; offer to file them properly if
  the user provides the password.
- **Multi-document PDFs** (one PDF containing several receipts) — classify by
  the dominant content, note "bundle" in the manifest; offer splitting as a
  follow-up task, do not split silently.
- **Duplicates** — the inventory detects exact duplicates by checksum. File
  all copies to the same folder and flag the group in the manifest and index.
  Never delete duplicates without explicit instruction.
- **Already-organized subfolders** — default scope excludes them (Gate 1).
  Never flatten an existing subfolder without explicit approval.
- **Re-running later** — safe: the scanner automatically excludes the
  category folders created earlier, so a re-run organizes only new loose
  files into the existing structure.
- **Huge folders / huge files** — the scanner caps full hashing at
  `--max-hash-mb` (default 100 MB; larger files get a fast partial
  fingerprint) and prints progress; for classification, batch 20–30 files
  and report progress between batches.
- **Cloud-synced folders** (Dropbox, Google Drive, OneDrive) — moves and
  copies are normal file operations and sync fine, but warn the user to let
  sync finish before judging results on another device.
- **Non-document files** (apps, archives, media) — leave in place, list them
  in the closing summary as "not documents, not touched".

---

## Privacy rules

- Documents are read locally and stay local. Nothing is uploaded.
- The index spreadsheet contains document metadata (dates, amounts,
  counterparties). Tell the user it inherits the sensitivity of the documents
  and should be stored alongside them.
- Identity, immigration, and medical documents are classified by their
  letterhead and layout — read the minimum needed; never transcribe passport
  numbers, SSNs, or diagnoses into the manifest, index, or audit log.
- Do not read more of each document than classification requires.
- If the session runs in a hosted environment where local files are actually
  remote uploads, say so explicitly before scanning.

---

## Examples

- [`examples/cleanup-request.md`](./examples/cleanup-request.md)
  — copy-paste request for a messy-folder cleanup.
- [`examples/example-output.md`](./examples/example-output.md)
  — compact example of a full run: gates, plan, copy run, index.
