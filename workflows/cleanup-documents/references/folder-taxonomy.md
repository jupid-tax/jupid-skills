# Folder Taxonomy

Default structure, variants, and naming rules for business-document cleanup.

## Default structure (7 folders)

```text
01 Invoices              — bills received from vendors AND invoices issued to customers
02 Receipts              — purchase receipts, till slips, expense proofs, confirmations
03 Bank & Card Statements — bank, credit card, PayPal/Stripe/payment-processor statements
04 Tax Documents         — IRS/state forms, filed returns, notices, estimated-tax records
05 Payroll               — paystubs, W-2, 1099-NEC issued to contractors, payroll reports
06 Contracts & Legal     — agreements, engagement letters, leases, insurance policies, formation docs
07 Needs Review          — unreadable, password-protected, ambiguous, or out-of-scope
```

Numeric prefixes keep the folders in workflow order in every file manager.
Keep them unless the user objects. When a folder is dropped or added,
renumber so the prefixes stay contiguous — no gaps.

## Common variants

Offer these when the inventory suggests them; never impose them.

### Split invoices by direction

For users who both issue and receive many invoices:

```text
01 Sales Invoices (issued)
02 Bills (received)
```

To tell direction, the agent needs the user's own business name — ask for it
once, early in classification.

### Year subfolders

For folders spanning multiple years (visible from document dates):

```text
01 Invoices/2024/
01 Invoices/2025/
```

Use the **document date**, not the file's modified date. Undated documents go
in the category root, not into a guessed year.

### Extra categories worth offering when the scan finds them

| Documents found | Folder to offer |
|-----------------|-----------------|
| policies, claims, certificates of insurance | `Insurance` |
| loan agreements, amortization schedules | `Loans & Financing` |
| purchase orders, packing slips | `Purchase Orders` |
| dividend/brokerage statements, K-1s | `Investments` |
| utility bills kept separately from other bills | `Utilities` |
| personal (non-business) documents mixed in | `Personal` — offer, and note they may not belong here at all |

### Client-per-folder (accountants)

If the user is an accountant organizing documents for multiple clients, the
top level is client names and the taxonomy above repeats inside each client.
Detect this from the documents (multiple distinct bill-to businesses) and ask
before assuming.

## Naming rules

### Folders

- Names the user chose win, verbatim, in any language.
- No trailing spaces or characters illegal on Windows (`< > : " / \ | ? *`)
  even on macOS/Linux — folders may be shared or synced cross-platform.

### Files — default: keep original names

Renaming is **opt-in**. Only if the user asks for it, use:

```text
YYYY-MM-DD <counterparty> <type> <amount>.<ext>
2025-03-14 Verizon invoice 89.99.pdf
```

- Date = document date. Undated files keep their original name.
- If renaming, record `original_name → new_name` in the manifest so the index
  and undo log stay truthful.

## What is NOT a document

Leave in place and list under "not documents, not touched" in the closing
summary: applications/executables, archives the agent has not opened (`.zip`
etc. — offer to look inside as a follow-up), code and data files, fonts,
media libraries, and system files (`.DS_Store`, `Thumbs.db`, desktop.ini) —
these are also excluded from the inventory entirely.
