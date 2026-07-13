# Example Output — Full Run

A compact trace of one cleanup, showing every dialogue gate.

## 1. Scan + structure proposal (agent)

```text
I scanned ~/Desktop/Business Docs 2025: 87 files — 61 PDFs, 24 photos/scans,
2 Word documents. 2 exact duplicates. 19 files need visual reading (scans
with no text layer).

Suggested structure:

01 Invoices              — bills you received and invoices you issued
02 Receipts              — purchase receipts, expense proofs
03 Bank & Card Statements
04 Tax Documents
05 Contracts & Legal
06 Needs Review

(No payroll documents found, so I dropped that folder and renumbered.)

Does this work, or do you want to rename, add, or remove folders?
```

## 2. User adjusts

```text
Split invoices — I issue invoices to clients and get bills from vendors.
My company is "Bluebird Design LLC". Add year subfolders for statements.
```

## 3. Plan summary (agent, after classification)

```text
All 87 files read. Here's the plan:

| Folder | Files |
|--------|-------|
| 01 Sales Invoices (issued) | 18 |
| 02 Bills (received) | 21 |
| 03 Receipts | 22 |
| 04 Bank & Card Statements/2024 | 6 |
| 04 Bank & Card Statements/2025 | 12 |
| 05 Tax Documents | 3 |
| 06 Contracts & Legal | 2 |
| 07 Needs Review | 3 |

Needs Review: IMG_4471.jpg (too blurry to read), statement_old.pdf
(password-protected), doc_final.pdf (no clear type — looks like a quote,
not an invoice).

2 exact duplicates (invoice_march.pdf = invoice_march(1).pdf) — filing both
to 02 Bills, flagged in the index.

OK to move the files?
```

## 4. Deliverable question (agent, after moving)

```text
Folders are done — 87 files moved, undo log saved.

Do you also want a spreadsheet index — one row per document with its
category, date, amount, and where it was filed? Excel or CSV?
```

## 5. Closing (agent)

```text
## Done — 87 documents organized

| Folder | Files |
|--------|-------|
| 01 Sales Invoices (issued) | 18 |
| 02 Bills (received) | 21 |
| 03 Receipts | 22 |
| 04 Bank & Card Statements | 18 |
| 05 Tax Documents | 3 |
| 06 Contracts & Legal | 2 |
| 07 Needs Review | 3 |

## Needs your attention
- IMG_4471.jpg — blurry photo, could not read
- statement_old.pdf — password-protected; if you have the password I can file it
- doc_final.pdf — looks like a price quote, not an invoice; tell me where it goes

## Index
Document Index.xlsx — 87 rows; every row shows the basis for its
classification. Spot-check a few before relying on it.

## Undo
python3 scripts/apply-move-plan.py --undo undo-log-2026-07-13T14-02-11.json
```

## Sample manifest rows behind this run

```json
[
  {
    "file": "invoice_2025_0312.pdf",
    "category": "02 Bills (received)",
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
    "category": "07 Needs Review",
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
