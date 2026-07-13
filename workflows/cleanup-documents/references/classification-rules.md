# Classification Rules

How to decide what a document is, and the manifest schema that records the
decision. The core rule: **every classification states its basis** — the
concrete features in the document that drove the decision. A classification
without a basis is a guess, and guesses go to Needs Review.

## Decision order

Check in this order; first confident match wins. Skip rules whose categories
are not in the user-confirmed structure — but if 2+ documents match a
skipped rule, propose the missing folder at the plan gate (see
`folder-taxonomy.md`, "Misfit clusters").

### 1. Bank & Card Statement

Signals: bank/issuer letterhead, statement period ("Statement period
03/01–03/31"), opening/closing balance, a transaction table spanning the
period, account number (usually masked), "minimum payment due" (cards).
Transaction CSV exports from a bank (e.g. `Chase..._Activity....CSV`) count
as statements.

Distinguish from an invoice: a statement summarizes many transactions on an
account; an invoice demands payment for specific goods/services.

### 2. Tax Document

Signals: IRS or state tax agency form number (W-2, W-9, 1099-*, 1040, 941,
1120, K-1, CP-series notices), "Department of the Treasury", HMRC/VAT
references, EIN/SSN fields, tax year prominently displayed, e-file
confirmations, estimated-tax vouchers.

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

### 6. Identity, Immigration & Personal

Signals: passport/ID-card layout, MRZ lines, driving licence, birth/marriage
certificates, residence permits, visas, biometric appointment letters,
official letters confirming address or status (government letterhead,
reference numbers). Powers of attorney signed by individuals lean here;
corporate powers of attorney lean Contracts & Legal — state the choice in
the basis.

Privacy: classify from layout and letterhead; do not transcribe document
numbers into the manifest.

### 7. Employment & Recruitment

Signals: CV/resume layout (name + skills + experience timeline), candidate
profiles, job offers ("we are pleased to offer you"), employment contracts
(salary, probation, notice period), reference letters. If the structure has
no Employment section, employment contracts go to Contracts & Legal and CVs
become a misfit cluster.

### 8. Education & Family

Signals: school/university letterhead, progress reports, application forms,
programme confirmations, tuition invoices (tuition invoices are still
invoices — file by the user's structure and note the ambiguity).

### 9. Medical

Signals: clinic/lab letterhead, test results, vaccination certificates,
prescriptions, referral letters. Classify by letterhead and layout; never
record diagnoses in the basis.

### 10. Travel & Insurance

Signals: tickets and boarding passes, booking confirmations, visas (→
Immigration when that folder exists), travel insurance terms, policy
schedules, certificates of insurance, claims correspondence.

### 11. Contract & Legal

Signals: "Agreement", "Terms", party recitals ("between X and Y"), numbered
clauses, signature blocks, effective dates, leases, engagement letters,
insurance policies (policy number, coverage schedule), formation documents
(articles of organization, EIN assignment letter CP 575), compliance
notifications.

### 12. Needs Review

Everything that fails the above with high confidence. Route to the matching
subfolder and say why in `review_reason`:

- `Unreadable` — blurry/cropped/dark scans, corrupt files, 0-byte or
  lock/temp files that survived filtering;
- `Password-Protected` — encrypted files; offer to file them if the user
  provides the password;
- `Ambiguous` — matches two categories equally well (record both candidates
  in the basis), documents in a language the agent cannot read reliably (say
  which), multi-document bundles with no dominant type, misfits that the
  user chose not to give a folder.

## Confidence

Only two levels matter operationally:

- **high** — the basis cites specific features; the file is filed to its
  category.
- **low** — anything less; the file goes to Needs Review. There is no
  "medium": if the agent hesitates, the user reviews.

## Manifest schema

One JSON array, one object per file. This is the contract between the agent
and `scripts/build-index.py` / `scripts/apply-move-plan.py` (derive
`plan.json` moves from `file` → `category`, adding `dest_name` only when the
user opted into renaming).

```json
{
  "file": "scans/IMG_2041.jpg",
  "category": "01 Finance & Tax/Receipts",
  "section": "01 Finance & Tax",
  "subcategory": "Receipts",
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
- `category` — the full target folder path relative to the target root,
  exactly as confirmed by the user (including year subfolders:
  `01 Finance & Tax/Bank & Card Statements/2025`).
- `section` / `subcategory` — the two levels separately, for the index. In a
  flat structure, `section` equals `category` and `subcategory` is null.
- `doc_type` — finer-grained: invoice_issued, invoice_received, receipt,
  bank_statement, card_statement, tax_form, tax_notice, paystub, contract,
  insurance_policy, identity_document, immigration, cv_resume, job_offer,
  reference_letter, school_report, application, medical, travel, ticket,
  article, other.
- `doc_date`, `amount`, `currency` — null when absent or unreadable. Never
  invent them.
- `basis` — one line, concrete features. Required for every file, including
  Needs Review (where it explains the failure). No passport numbers, SSNs,
  or diagnoses.
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
