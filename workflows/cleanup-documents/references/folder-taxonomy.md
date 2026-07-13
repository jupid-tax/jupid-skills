# Folder Taxonomy

Presets, variants, and naming rules for document cleanup. Pick the preset
from the inventory, then tailor: drop categories with no matching documents,
renumber contiguously (no gaps), and translate folder names into the user's
language when they write in one.

## Preset 1 — Business / accounting (flat, 7 folders)

The default when the folder is business paperwork.

```text
01 Invoices              — bills received from vendors AND invoices issued to customers
02 Receipts              — purchase receipts, till slips, expense proofs, confirmations
03 Bank & Card Statements — bank, credit card, PayPal/Stripe/payment-processor statements
04 Tax Documents         — IRS/state forms, filed returns, notices, estimated-tax records
05 Payroll               — paystubs, W-2, 1099-NEC issued to contractors, payroll reports
06 Contracts & Legal     — agreements, engagement letters, leases, insurance policies, formation docs
07 Needs Review          — see "Needs Review subfolders" below
```

## Preset 2 — Personal + business (two levels)

Recommended when the scan shows identity documents, medical papers, CVs,
school files, or travel documents mixed into business paperwork — typical
for a real personal `Documents` folder.

```text
01 Finance & Tax
   Bills & Invoices
   Receipts
   Bank & Card Statements
   Tax Documents
   Payroll
02 Business & Legal
   Contracts & Agreements
   Company & Compliance
   Templates & Working Documents
03 Employment & Recruitment
   Employment Contracts & Job Offers
   CVs & Candidate Profiles
   References
04 Identity, Immigration & Personal
   Identity Documents
   Immigration & Residency
   Address & Official Correspondence
05 Education & Family
   School Reports
   Applications & Programmes
06 Health, Travel & Insurance
   Medical Documents
   Travel Documents
   Insurance
07 Needs Review
   Unreadable
   Password-Protected
   Ambiguous
```

Drop second-level folders that would be empty; a section with one subcategory
collapses to a single folder.

## Preset 3 — Accountant multi-client

For an accountant organizing documents for multiple clients: client names on
top, Preset 1 inside each. Detect this from the documents (multiple distinct
bill-to businesses) and confirm before assuming.

```text
Bluebird Design LLC/
   01 Invoices
   ...
Acme Consulting LLC/
   01 Invoices
   ...
_Needs Review/            — cross-client: unreadable or client-unclear files
```

## Needs Review subfolders

Always split Needs Review by what the user must do:

```text
Needs Review/
   Unreadable           — blurry scans, corrupt files; user re-scans or discards
   Password-Protected   — user supplies passwords, then re-run
   Ambiguous            — agent explains candidates; user decides
```

## Common variants (offer when the inventory suggests them)

### Split invoices by direction

For users who both issue and receive many invoices:

```text
01 Sales Invoices (issued)
02 Bills (received)
```

To tell direction, the agent needs the user's own business name — ask for it
once, at the structure gate.

### Year subfolders

For folders spanning multiple years (visible from document dates):

```text
01 Invoices/2024/
01 Invoices/2025/
```

Use the **document date**, not the file's modified date. Undated documents go
in the category root, not into a guessed year.

### Misfit clusters → new categories

When 2+ documents of the same kind fit no confirmed category (event tickets,
magazine articles, personal photos), propose a dedicated folder at the plan
gate instead of dumping them into Needs Review:

| Documents found | Folder to offer |
|-----------------|-----------------|
| tickets, event confirmations | `Events & Tickets` |
| articles, magazines, ebooks | `Articles & Reading` |
| policies, claims, certificates of insurance | `Insurance` |
| loan agreements, amortization schedules | `Loans & Financing` |
| purchase orders, packing slips | `Purchase Orders` |
| dividend/brokerage statements, K-1s | `Investments` |
| personal photos (not documents) | offer to leave in place — they may belong in a photo library, not here |

## Naming rules

### Folders

- Names the user chose win, verbatim, in any language.
- Numeric prefixes keep folders in workflow order; renumber contiguously
  when folders are dropped or added — no gaps.
- No trailing spaces or characters illegal on Windows (`< > : " / \ | ? *`)
  even on macOS/Linux — folders may be shared or synced cross-platform.

### Files — default: keep original names

Renaming is **opt-in** (Gate 3). Only if the user chose it, use:

```text
YYYY-MM-DD <counterparty> <type> <amount>.<ext>
2025-03-14 Verizon invoice 89.99.pdf
```

- Date = document date. Undated files keep their original name.
- If renaming, put the new name in the plan's `dest_name` and record the
  original in the manifest so the index and undo log stay truthful.

## What is NOT a document

Leave in place and list under "not documents, not touched" in the closing
summary: applications/executables, archives the agent has not opened (`.zip`
etc. — offer to look inside as a follow-up), audio/video projects, code and
data files, fonts, digital-signature sidecars (`.p7s`), and lock/temp files
(`~$…`, `.tmp`). System files (`.DS_Store`, `Thumbs.db`, desktop.ini) are
excluded from the inventory entirely.
