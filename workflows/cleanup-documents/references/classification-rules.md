# Classification Rules

How to decide what a document is, and the manifest schema that records the
decision. The core rule: **every classification states its basis** — the
concrete features in the document that drove the decision. A classification
without a basis is a guess, and guesses go to Needs Review.

## Decision order

Check in this order; first confident match wins.

### 1. Bank & Card Statement

Signals: bank/issuer letterhead, statement period ("Statement period
03/01–03/31"), opening/closing balance, a transaction table spanning the
period, account number (usually masked), "minimum payment due" (cards).

Distinguish from an invoice: a statement summarizes many transactions on an
account; an invoice demands payment for specific goods/services.

### 2. Tax Document

Signals: IRS or state tax agency form number (W-2, W-9, 1099-*, 1040, 941,
1120, K-1, CP-series notices), "Department of the Treasury", EIN/SSN fields,
tax year prominently displayed, e-file confirmations, estimated-tax vouchers.

Note: a 1099-NEC the user **issued to a contractor** is payroll-adjacent —
default it to Tax Documents but mention the ambiguity in the manifest basis;
follow the user's structure if they created a Payroll folder for it.

### 3. Payroll

Signals: paystub layout (gross pay, deductions, net pay, YTD columns),
employee name + pay period, payroll-provider branding (Gusto, ADP, Paychex),
payroll journal/summary reports.

### 4. Invoice

Signals: the word "Invoice" / "Bill" / "Tax Invoice", an invoice number, a
bill-to / sold-to block, line items with quantities and prices, subtotal +
tax + **amount due**, payment terms ("Net 30", due date).

Direction (needs the user's business name):
- user's business in the **bill-to** block → received bill (payable);
- user's business in the **header/from** block → issued invoice (receivable).

### 5. Receipt

Signals: "Receipt", "Paid", "Payment received", $0 balance due, a completed
card transaction (last-4, auth code), till-slip layout, order confirmations
**with payment confirmation**.

Invoice vs receipt: an invoice asks for money (amount due > 0); a receipt
proves money moved. An invoice stamped "PAID" is a receipt for filing
purposes — say so in the basis.

### 6. Contract & Legal

Signals: "Agreement", "Terms", party recitals ("between X and Y"), numbered
clauses, signature blocks, effective dates, leases, engagement letters,
insurance policies (policy number, coverage schedule), formation documents
(articles of organization, EIN assignment letter CP 575).

### 7. Needs Review

Everything that fails the above with high confidence, plus:

- unreadable scans/photos (blurry, cropped, too dark);
- password-protected files;
- documents in a language the agent cannot read reliably — say which;
- multi-document bundles with no dominant type;
- documents that match two categories equally well — record both candidates
  in the basis.

## Confidence

Only two levels matter operationally:

- **high** — the basis cites specific features; the file is moved to its
  category.
- **low** — anything less; the file goes to Needs Review. There is no
  "medium": if the agent hesitates, the user reviews.

## Manifest schema

One JSON array, one object per file. This is the contract between the agent
and `scripts/build-index.py` / `scripts/apply-move-plan.py` (derive `plan.json`
moves from `file` → `category`).

```json
{
  "file": "scans/IMG_2041.jpg",
  "category": "02 Receipts",
  "doc_type": "receipt",
  "counterparty": "Home Depot",
  "doc_date": "2025-03-14",
  "amount": 84.12,
  "currency": "USD",
  "basis": "Till-slip layout, 'TOTAL 84.12', Visa ...4412 approval code, Home Depot header",
  "confidence": "high",
  "needs_review": false,
  "review_reason": null,
  "duplicate_group": null,
  "source": "visual_read"
}
```

Field notes:

- `file` — path relative to the source folder root, as in `inventory.json`.
- `category` — exactly one of the user-confirmed folder names.
- `doc_type` — finer-grained: invoice_issued, invoice_received, receipt,
  bank_statement, card_statement, tax_form, tax_notice, paystub, contract,
  insurance_policy, other.
- `doc_date`, `amount`, `currency` — null when absent or unreadable. Never
  invent them.
- `basis` — one line, concrete features. Required for every file, including
  Needs Review (where it explains the failure).
- `source` — `text_layer` (classified from extracted text) or `visual_read`
  (agent read the rendered document).
- `duplicate_group` — integer id shared by files with identical checksums,
  from the inventory; null otherwise.

## Reading discipline

- Read only what classification needs: the first page usually suffices;
  check the last page only when the first is ambiguous (totals pages,
  signature blocks).
- For statements and contracts running dozens of pages, never read the whole
  file.
- Trust the extracted text layer when it exists; fall back to visual reading
  when the text layer is empty, garbled, or clearly partial.
