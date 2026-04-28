# Example: Etsy Seller — Trade-or-Business Activity Reconciled to Schedule C

A complete walkthrough for the most common 1099-K reconciliation: a marketplace seller (Etsy / eBay / Poshmark / Amazon Handmade) running a clear trade-or-business and routing the 1099-K to Schedule C.

This is the canonical pattern from the Jupid blog companion's worked example.

## The filer

- **Name**: Maya Chen
- **Business**: Hand-screened textile prints sold on Etsy
- **Entity**: Sole proprietor, no LLC, files Schedule C under her SSN
- **Started**: Mid-2025; year-2026 is her first full-year operation
- **State**: Oregon (no state 1099-K threshold lower than federal)
- **Tax year**: 2026

## The 1099-K

Etsy Payments, Inc. issued a 1099-K showing:

| Box | Value |
|-----|-------|
| Filer | Etsy Payments, Inc. (EIN ends in -2354) |
| Box 1a (Gross) | $4,800 |
| Box 1b (CNP) | $4,800 |
| Box 2 (Transactions) | 312 |
| Box 4 (Federal tax withheld) | $0 |
| Boxes 5a-5l | Roughly even, $300-450 per month |
| Box 6 (State) | OR |
| Box 8 (State withholding) | $0 |

Note: $4,800 is **below** the federal $20,000 / 200 threshold, but Etsy issues 1099-Ks to all sellers who clear $600 (their voluntary internal policy). The form is valid; reconciliation runs the same way.

## Step 1 — Confirm form

Maya confirms the form title says "Payment Card and Third Party Network Transactions" — yes, it's a 1099-K. The 200-transaction count was met (312); the $20,000 dollar threshold wasn't, but Etsy issued voluntarily. All income is taxable regardless of 1099-K issuance.

## Step 2 — Classify each portion

Maya pulls her Etsy transaction CSV. All 312 transactions are sales of her textile prints to Etsy buyers — clear trade-or-business activity (profit motive, regular operation, business-like records, separate Etsy account, separate business bank account she opened in 2025). Per IRC §183 / Treas. Reg. §1.183-2(b), this is a trade or business, not a hobby.

Classification: 100% of Box 1a → Schedule C trade-or-business income.

## Step 3 — Reconcile against Etsy's own records

- Etsy year-end gross-payments report: $4,800 ✓ matches Box 1a
- Sum of monthly bank deposits from Etsy: $4,488 (gross minus Etsy's 6.5% transaction fees + listing/ad fees; deposits are net)
- The $312 difference traces to Etsy's fees, which Etsy keeps before depositing. Confirmed from Etsy's monthly statement.

No corrected 1099-K needed.

## Step 4 — Cross-check against other 1099s

Maya received no 1099-NEC for Etsy sales. No double-reporting. She also had $620 in cash sales at two craft fairs — not on any 1099 but still business income.

## Step 5 — Map to Schedule C lines

| Line | Description | Amount |
|------|-------------|--------|
| Line 1 | Gross receipts ($4,800 from 1099-K + $620 cash) | $5,420 |
| Line 2 | Returns and allowances (one buyer return) | $25 |
| Line 4 | Cost of goods sold (from Part III) | $890 |
| Line 9 | Car and truck expenses (148 mi × $0.70 standard rate for 2025) | $104 |
| Line 10 | Commissions and fees (Etsy 6.5% transaction fees + listing + ad fees) | $457 |
| Line 22 | Supplies (boxes, mailers, packing tape) | $215 |
| Line 27a | Other expenses — labeled sub-rows: | |
| | "Postage" (Maya buys her own postage for some shipments) | $190 |
| | "Booth fees" (two craft fair booth rentals) | $300 |
| Line 30 | Home office (allocated portion of rent + utilities for studio space) | $164 |
| **Line 28** | **Total expenses** | **$2,320** |
| **Line 31** | **Net profit** | **$3,100** |

## Part III (Cost of Goods Sold) detail

| Line | Description | Amount |
|------|-------------|--------|
| Line 33 (a) | Cost (inventory method) | ✓ |
| Line 35 | Inventory at beginning of year | $0 (first full year, no prior inventory) |
| Line 36 | Purchases (fabric, ink, frames during 2026) | $1,015 |
| Line 39 | Other costs | $0 |
| Line 40 | Total | $1,015 |
| Line 41 | Inventory at end of year (unsold materials) | $125 |
| **Line 42** | **Cost of goods sold** (flows to Line 4) | **$890** |

## Step 6 — Schedule SE (self-employment tax)

Net profit of $3,100 from Schedule C Line 31 flows to:

- Schedule SE Line 2: $3,100
- Line 3: $3,100
- Line 4a: $3,100 × 0.9235 = $2,863
- Line 7: $176,100 (Social Security wage base for 2025; 2026 amount published by SSA in Oct 2025 — verify)
- Line 10: $2,863 × 0.124 = $355 (Social Security portion)
- Line 11: $2,863 × 0.029 = $83 (Medicare portion)
- Line 12: SE tax = $355 + $83 = **$438**

Half of SE tax ($219) deducts above-the-line on Schedule 1 Line 15.

## Step 7 — Form 1040 ledger

| Line | Source | Amount |
|------|--------|--------|
| Schedule 1 Line 3 | Schedule C Line 31 net profit | $3,100 |
| Schedule 1 Line 15 | 1/2 SE tax deduction | $219 |
| Form 1040 Line 8 | Other income from Schedule 1 | $3,100 (less the Line 15 adjustment, netted at Line 10) |
| Form 1040 Line 23 | Other taxes (SE tax from Schedule SE) | $438 |

## Step 8 — Validation

| Check | Result |
|-------|--------|
| Sum of classified portions equals Box 1a | $4,800 = $4,800 ✓ |
| Trade-or-business portion appears in Schedule C Line 1 | $5,420 ≥ $4,800 ✓ (extra is non-1099 cash sales) |
| Platform fees on Line 10, not netted into Line 1 | ✓ |
| Box 4 = $0, no Line 25c entry needed | ✓ |
| All sanity warnings cleared | ✓ |

## What Maya does NOT do

- She does NOT subtract Etsy's $312 fees from the $4,800 before reporting Line 1. The gross stays $4,800; the fees are deducted separately on Line 10. Reporting $4,488 on Line 1 would create an IRS document-mismatch.
- She does NOT exclude the $620 cash sales from Line 1 because no 1099 documented them. All business income is reportable.
- She does NOT deduct the buyer-paid shipping that Etsy passed through. That money was never hers — it covered postage Etsy auto-purchased on her behalf. Only the $190 in postage Maya bought separately is deductible.
- She does NOT classify the activity as a hobby. The §183 profit-motive test is clearly met.

## What if the activity were a hobby?

If Maya were genuinely casual (sporadic, no profit motive, no business-like records), the reconciliation would change:

| Line | Hobby version |
|------|---------------|
| Schedule 1 Line 8j | $4,800 (Activity not engaged in for profit) |
| Schedule 1 Line 8j description | "Hobby income — Etsy print sales" |
| Schedule C | Not filed |
| Expense deductions | NONE — TCJA suspended hobby expense deductions through 2025 (IRC §67(g)) |
| SE tax | $0 (hobby income not subject to SE tax) |

Maya would pay federal income tax on the full $4,800 with no deductions, but no SE tax. For most marketplace sellers with regular activity, this is a worse outcome than Schedule C — which is why the trade-or-business classification matters.

## What if Maya had personal-item resales mixed in?

If Maya sold $4,800 of textile prints AND $200 of her old college sweaters via the same Etsy account, the reconciliation would split:

- Schedule C Line 1: $4,800 (the trade/business portion)
- Schedule 1 Line 8z: $200 (personal items sold at a loss, per Notice 2023-74)
- Schedule 1 Line 24z: $200 (offset of personal-item-loss portion)
- Sum: $5,000 → matches the hypothetical Box 1a

In practice, mixed Etsy accounts are rare (Etsy is set up for sellers, not personal resales) — Poshmark and Mercari are the more common platforms for that scenario.

## Audit-defense documentation Maya keeps

- The 1099-K (PDF download from Etsy)
- Etsy year-end gross-payments report (PDF)
- Etsy transaction CSV with monthly summaries
- Bank statements showing Etsy deposits (cross-reference)
- Receipts for fabric, ink, frames (COGS)
- Receipts for shipping supplies, postage
- Mileage log (paper or app like MileIQ)
- Booth-fee receipts from craft fairs
- Photos of her home studio (for home-office deduction defense)
- The completed Schedule C, Schedule SE, Schedule 1
- The reconciliation worksheet (this document, redacted)
- Form 1040 + e-file acceptance confirmation

She keeps this bundle for at least 6 years per IRS recordkeeping rules.

## Sources cited in this draft

- IRS Form 1099-K (current revision)
- IRS Instructions for Form 1099-K
- IRC §6050W (1099-K reporting)
- IRC §183 (hobby loss / profit motive)
- IRC §162 (trade or business expenses)
- IRC §1401 (self-employment tax 15.3%)
- Treasury Regulation §1.183-2(b) (9-factor profit-motive test)
- IRS Form 1099-K FAQs
- Schedule C (Form 1040) and instructions
- Schedule SE (Form 1040) and instructions
- Companion Jupid blog: [1099-K Guide 2026](https://jupid.com/blog/1099-k-guide-2026)
