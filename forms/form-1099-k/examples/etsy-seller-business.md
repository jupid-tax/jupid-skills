# Example: Etsy Seller — Trade-or-Business Activity Reconciled to Schedule C

A complete walkthrough for the most common 1099-K reconciliation: a marketplace seller (Etsy / eBay / Poshmark / Amazon Handmade) running a clear trade-or-business and routing the 1099-K to Schedule C.

This is the canonical pattern from the Jupid blog companion's worked example.

## The filer

- **Name**: Maya Chen
- **Business**: Hand-screened textile prints sold on Etsy
- **Entity**: Sole proprietor, no LLC, files Schedule C under her SSN
- **Started**: Mid-2025; year-2026 is her first full-year operation
- **State**: Oregon
- **Tax year**: 2026

## The 1099-K

Etsy Payments, Inc. issued a 1099-K showing:

| Box | Value |
|-----|-------|
| Filer | Etsy Payments, Inc. (EIN ends in -2354) |
| Box 1a (Gross) | $4,800 |
| Transactions reported | Third party network |
| Box 1b (CNP) | Blank (not reported on third party network forms) |
| Box 3 (Transactions) | 312 |
| Box 4 (Federal tax withheld) | $0 |
| Boxes 5a-5l | Roughly even, $300-450 per month |
| Box 6 (State) | OR |
| Box 8 (State withholding) | $0 |

Note: $4,800 is **below** the federal $20,000 / 200 test, so Etsy was not federally required to file. A TPSO may still file below the threshold (IRS FS-2025-08, General information Q5). The form is valid; reconciliation runs the same way.

## Step 1 — Confirm form

Maya confirms the form title says "Payment Card and Third Party Network Transactions" — yes, it's a 1099-K. The transaction part of the test was met (312 > 200); the dollar part wasn't ($4,800 ≤ $20,000), but Etsy issued the form anyway. All income is taxable regardless of 1099-K issuance.

## Step 2 — Classify each portion

Maya pulls her Etsy transaction CSV. All 312 transactions are sales of her textile prints to Etsy buyers — clear trade-or-business activity (profit motive, regular operation, business-like records, separate Etsy account, separate business bank account she opened in 2025). Per IRC §183 / Treas. Reg. §1.183-2(b), this is a trade or business, not a hobby.

Classification: 100% of Box 1a → Schedule C trade-or-business income.

## Step 3 — Reconcile against Etsy's own records

- Etsy year-end gross-payments report: $4,800 ✓ matches Box 1a
- Sum of payouts to her bank from Etsy: $4,463 (deposits are net)
- The $337 difference is the $312 of 6.5% transaction fees Etsy kept from payouts plus the $25 refund. The other $145 of listing and ad fees was charged to her card. Confirmed from Etsy's monthly statements.

No corrected 1099-K needed.

## Step 4 — Cross-check against other 1099s

Maya received no 1099-NEC for Etsy sales. No double-reporting. She also had $620 in cash sales at two craft fairs — not on any 1099 but still business income.

## Step 5 — Map to Schedule C lines

| Line | Description | Amount |
|------|-------------|--------|
| Line 1 | Gross receipts ($4,800 from 1099-K + $620 cash) | $5,420 |
| Line 2 | Returns and allowances (one buyer return) | $25 |
| Line 3 | Line 1 − Line 2 | $5,395 |
| Line 4 | Cost of goods sold (from Part III) | $890 |
| Line 5 / Line 7 | Gross profit / gross income (no Line 6 income) | $4,505 |
| Line 9 | Car and truck expenses (70 mi Jan–Jun × $0.725 + 78 mi Jul–Dec × $0.76, 2026 standard rates) | $110 |
| Line 10 | Commissions and fees ($312 Etsy 6.5% transaction fees + $145 listing and ad fees) | $457 |
| Line 22 | Supplies (boxes, mailers, packing tape) | $215 |
| Line 27b | Other expenses (from Part V, line 48) — labeled rows: | $490 |
| | "Postage" (Maya buys her own postage for some shipments) | $190 |
| | "Booth fees" (two craft fair booth rentals) | $300 |
| **Line 28** | **Total expenses (Lines 8 through 27b)** | **$1,272** |
| Line 29 | Tentative profit (Line 7 − Line 28) | $3,233 |
| Line 30 | Home office (allocated portion of rent + utilities for studio space) | $164 |
| **Line 31** | **Net profit** (Line 29 − Line 30) | **$3,069** |

## Part III (Cost of Goods Sold) detail

| Line | Description | Amount |
|------|-------------|--------|
| Line 33 (a) | Cost (inventory method) | ✓ |
| Line 35 | Inventory at beginning of year | $0 (she carried no materials into 2026) |
| Line 36 | Purchases (fabric, ink, frames during 2026) | $1,015 |
| Line 39 | Other costs | $0 |
| Line 40 | Total | $1,015 |
| Line 41 | Inventory at end of year (unsold materials) | $125 |
| **Line 42** | **Cost of goods sold** (flows to Line 4) | **$890** |

## Step 6 — Schedule SE (self-employment tax)

Net profit of $3,069 from Schedule C Line 31 flows to:

- Schedule SE Line 2: $3,069
- Line 3: $3,069
- Line 4a: $3,069 × 0.9235 = $2,834
- Line 7: $184,500 (2026 Social Security wage base, https://www.ssa.gov/oact/cola/cbb.html; Maya has no W-2 wages)
- Line 10: $2,834 × 0.124 = $351 (Social Security portion)
- Line 11: $2,834 × 0.029 = $82 (Medicare portion)
- Line 12: SE tax = $351 + $82 = **$433**

Half of SE tax ($217, Schedule SE line 13) deducts above-the-line on Schedule 1 Line 15.

## Step 7 — Form 1040 ledger

| Line | Source | Amount |
|------|--------|--------|
| Schedule 1 Line 3 | Schedule C Line 31 net profit | $3,069 |
| Schedule 1 Line 15 | 1/2 SE tax deduction | $217 |
| Form 1040 Line 8 | Additional income (Schedule 1 Line 10) | $3,069 |
| Form 1040 Line 10 | Adjustments to income (Schedule 1 Line 26) | $217 |
| Form 1040 Line 23 | Schedule 2 line 21 (includes SE tax) | $433 |

## Step 8 — Validation

| Check | Result |
|-------|--------|
| Sum of classified portions equals Box 1a | $4,800 = $4,800 ✓ |
| Trade-or-business portion appears in Schedule C Line 1 | $5,420 ≥ $4,800 ✓ (extra is non-1099 cash sales) |
| Platform fees on Line 10, not netted into Line 1 | ✓ |
| Box 4 = $0, no Line 25b entry needed | ✓ |
| All sanity warnings cleared | ✓ |

## What Maya does NOT do

- She does NOT subtract Etsy's $312 transaction fees from the $4,800 before reporting Line 1. The gross stays $4,800; the fees are deducted separately on Line 10. Reporting $4,488 on Line 1 would create an IRS document-mismatch.
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
| Expense deductions | NONE — hobby expenses are miscellaneous itemized deductions, disallowed under IRC §67(g) (made permanent by P.L. 119-21 §70110) |
| SE tax | $0 (hobby income not subject to SE tax) |

Maya would pay federal income tax on the full $4,800 with no deductions, but no SE tax. For most marketplace sellers with regular activity, this is a worse outcome than Schedule C — which is why the trade-or-business classification matters.

## What if Maya had personal-item resales mixed in?

If Maya sold $4,800 of textile prints AND $200 of her old college sweaters via the same Etsy account, the reconciliation would split:

- Schedule C Line 1: $4,800 (the trade/business portion)
- Entry space at the top of Schedule 1: $200 (personal items sold at a loss; IRS FS-2025-08, What to do Q6)
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

She keeps this bundle at least 3 years after filing, 6 years if income she should have reported was more than 25% of the gross income shown, and records for property until the limitation period for the year she disposes of it ends (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records).

## Sources cited in this draft

- IRS Form 1099-K (current revision)
- IRS Instructions for Form 1099-K
- IRC §6050W (1099-K reporting)
- IRC §183 (hobby loss / profit motive)
- IRC §162 (trade or business expenses)
- IRC §1401 (self-employment tax 15.3%)
- Treasury Regulation §1.183-2(b) (9-factor profit-motive test)
- IRS FS-2025-08, Form 1099-K FAQs (Oct. 23, 2025)
- IRS standard mileage rates (2026: 72.5¢ Jan–Jun, 76¢ Jul–Dec)
- Schedule C (Form 1040) and instructions
- Schedule SE (Form 1040) and instructions
- Companion Jupid blog: [1099-K Guide 2026](https://jupid.com/blog/1099-k-guide-2026)
