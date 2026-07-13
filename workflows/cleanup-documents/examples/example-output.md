# Example Output — Full Run

A compact trace of one cleanup, showing every dialogue gate. The run below is
in English; with a Russian-speaking user every message, folder name, and the
index would be in Russian (`--lang ru`).

## Gate 1 — scope (agent, after fast top-level scan)

```text
I scanned ~/Documents (nothing was changed): 127 loose files at the top
level — 89 PDFs, 17 Word files, 13 images, 8 spreadsheets — plus 13 existing
subfolders and 22 non-documents (videos, audio projects).

What should I organize?

1. Only the 127 loose top-level files (recommended) — existing subfolders
   stay exactly as they are
2. Everything, including subfolders
3. One specific subfolder — tell me which

Reply with a number, or say "go ahead" for option 1.
```

## Gate 2 — structure (agent)

```text
This folder mixes business paperwork with personal documents (IDs, medical,
CVs, school files), so I recommend preset 2:

1. Business / accounting — 7 flat folders
2. Personal + business (recommended):

   01 Finance & Tax        — Bills & Invoices / Receipts / Bank & Card
                             Statements / Tax Documents
   02 Business & Legal     — Contracts & Agreements / Company & Compliance
   03 Employment & Recruitment — Contracts & Offers / CVs & Candidates /
                             References
   04 Identity, Immigration & Personal — Identity Documents / Immigration /
                             Official Correspondence
   05 Education & Family
   06 Health, Travel & Insurance
   07 Needs Review         — Unreadable / Password-Protected / Ambiguous

3. Multi-client — one folder per client
4. Custom — describe what you want

You can also tweak option 2: rename, add/remove, year subfolders.
```

## Gate 3 — mode and naming (agent)

```text
Two quick settings before I start reading the documents:

Mode:
1. Copy (recommended for a first run) — originals stay where they are
2. Move — files are relocated; undo puts them back
3. Report only — classify and index, touch nothing

File names:
A. Keep original names (recommended)
B. Standardize to "YYYY-MM-DD Counterparty Type.pdf"

Say "go ahead" for 1 + A.
```

User: `go ahead`

## Gate 4 — plan and misfits (agent, after classification)

```text
All 127 files read. Here's the plan (nothing is applied yet):

| Folder | Files |
|--------|-------|
| 01 Finance & Tax | 31 |
| 02 Business & Legal | 22 |
| 03 Employment & Recruitment | 23 |
| 04 Identity, Immigration & Personal | 17 |
| 05 Education & Family | 8 |
| 06 Health, Travel & Insurance | 20 |
| 07 Needs Review | 6 |

Finance documents with verified dates get year subfolders (2024/2025).

Needs Review: 2 unreadable photos, 1 password-protected school report,
1 corrupt PDF that won't open, and 2 misfits — a concert ticket and a
magazine article. For the misfits:

1. Add "08 Events & Reading" for them (recommended)
2. Leave them in 07 Needs Review/Ambiguous
3. Decide file by file

7 exact-duplicate groups found — I'll file all copies together and flag
them, not delete.

Approve the plan? (Copy mode — originals stay untouched.)
```

## After applying (agent)

```text
Done — 127 verified copies created, originals untouched.

The folders are at /Users/anna/Documents (01–08, next to your existing
folders). Every copy was checksum-verified against its original.
```

## Gate 5 — deliverable (agent)

```text
What do you want as the record?

1. Excel index (recommended) — one row per document: category, date, amount,
   counterparty, where it was filed, and why
2. CSV index
3. Both
4. None

I can also add an audit log — a short Markdown report of this run (what was
scanned, what you approved, counts, undo command). Want it?
```

## Closing (agent)

```text
## Done — 127 documents organized (copies; originals untouched)

Everything is in /Users/anna/Documents, folders 01–08.

| Folder | Files |
|--------|-------|
| 01 Finance & Tax | 31 |
| 02 Business & Legal | 22 |
| 03 Employment & Recruitment | 23 |
| 04 Identity, Immigration & Personal | 17 |
| 05 Education & Family | 8 |
| 06 Health, Travel & Insurance | 20 |
| 07 Needs Review | 4 |
| 08 Events & Reading | 2 |

## Needs your attention (07 Needs Review)
- IMG_4471.jpg — blurry photo (Unreadable)
- IMG_4480.jpg — blurry photo (Unreadable)
- Year 11 Progress Report.pdf — password-protected; give me the password and
  I'll file it
- quote_final.pdf — corrupt file, won't open; re-download if you need it

## Index
Document Index.xlsx — 127 rows; every row shows the basis for its
classification. Spot-check a few before you rely on it.

## Undo
python3 scripts/apply-move-plan.py --undo undo-log-2026-07-13T14-02-11.json
(removes only the verified copies created by this run)
```

## Sample manifest rows behind this run

```json
[
  {
    "file": "invoice_2025_0312.pdf",
    "category": "01 Finance & Tax/Bills & Invoices/2025",
    "section": "01 Finance & Tax",
    "subcategory": "Bills & Invoices",
    "doc_type": "invoice_received",
    "counterparty": "Verizon Business",
    "doc_date": "2025-03-12",
    "amount": 89.99,
    "currency": "USD",
    "basis": "Header 'Invoice #VZ-88213', bill-to Bluebird Design LLC, amount due $89.99, Net 30",
    "confidence": "high",
    "needs_review": false,
    "review_reason": null,
    "duplicate_group": null,
    "source": "text_layer"
  },
  {
    "file": "IMG_4471.jpg",
    "category": "07 Needs Review/Unreadable",
    "section": "07 Needs Review",
    "subcategory": "Unreadable",
    "doc_type": "other",
    "counterparty": null,
    "doc_date": null,
    "amount": null,
    "currency": null,
    "basis": "Photo too blurry to read any text reliably",
    "confidence": "low",
    "needs_review": true,
    "review_reason": "unreadable scan",
    "duplicate_group": null,
    "source": "visual_read"
  }
]
```
