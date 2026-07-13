# Dialogue Playbook

Use this when guiding a business owner or accountant through a document
cleanup. The user is often non-technical: they have a folder full of PDFs,
scans, and photos, and they want it fixed. Keep every message short and end
each one with exactly one question or one clear next action.

## Message 1 — locate the mess

If the folder path was not given:

```text
Which folder should I clean up? Drag it into the chat or paste the path.
```

If the user describes several locations, do one folder per run. Suggest
starting with the messiest.

## Message 2 — propose the structure

After scanning, propose the structure in one compact block and ask one
yes/adjust question:

```text
I scanned the folder: 148 files — mostly PDFs, 31 photos/scans, 4 duplicates.

Here is the structure I suggest:

01 Invoices              — bills you received and invoices you issued
02 Receipts              — purchase receipts, expense proofs
03 Bank & Card Statements
04 Tax Documents
05 Payroll
06 Contracts & Legal
07 Needs Review          — anything I can't read or confidently place

Does this work, or do you want to rename, add, or remove folders?
Common tweaks: split invoices into "issued" vs "received", add year
subfolders (2024/2025), add an "Insurance" folder.
```

Rules for this step:

- Tailor the list: if the scan found no payroll documents, drop `05 Payroll`
  and say so. If it found many of one type, offer a split.
- Accept the user's names verbatim, including non-English folder names.
- Do not proceed until the user has confirmed. "Looks fine" counts as
  confirmation; silence does not.

## Message 3 — progress during classification

For folders over ~30 files, report progress in batches so the user is not
staring at silence:

```text
Read 60 of 148… so far: 22 invoices, 15 receipts, 9 statements, 3 for review.
```

Do not ask questions mid-classification unless a genuinely blocking ambiguity
appears (e.g., the user's own company name is needed to tell issued invoices
from received ones — ask once, early).

## Message 4 — show the plan before moving

```text
All 148 files read. Here's the plan:

| Folder | Files |
|--------|-------|
| 01 Invoices | 52 |
| 02 Receipts | 41 |
| 03 Bank & Card Statements | 24 |
| 04 Tax Documents | 11 |
| 06 Contracts & Legal | 9 |
| 07 Needs Review | 7 |

Needs Review: 3 blurry photos, 2 password-protected PDFs, 2 ambiguous
documents (details in the index).

4 exact duplicates found — I'll file them together and flag them, not delete.

OK to move the files?
```

Wait for confirmation, run the dry-run silently, then execute.

## Message 5 — the deliverable question

Exactly one question, asked after the folders are done:

```text
Folders are done. Do you also want a spreadsheet index — one row per document
with its category, date, amount, and where it was filed? Excel or CSV?
```

## Message 6 — closing

Use the Output format from `SKILL.md`: counts table, Needs Review list with
reasons, index location, undo command. One screen, no fluff.

## Avoid bad behavior

Do not say:

```text
I've organized your documents using advanced AI classification.
```

Say:

```text
52 invoices filed. Every row in the index shows why a file was classified the
way it was — spot-check a few before you rely on it.
```

Do not:

- move a single file before the structure is confirmed and the plan is shown;
- hide the Needs Review pile at the bottom of a long message — it is the one
  part the user must act on;
- ask more than one question per message;
- rename files unless the user asked (renaming is an opt-in extra, see
  `folder-taxonomy.md`).
