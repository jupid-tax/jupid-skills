# Example: Business Debt Canceled — Sole Proprietor, Schedule C Line 6

A complete walkthrough of a 1099-C for canceled **business** debt held by a sole proprietor (or single-member LLC). This is the canonical "business cancellation routes to Schedule C, not Schedule 1" pattern. No exclusion applies in this example, illustrating the routing decision rather than an exclusion path.

If insolvency or another exclusion did apply to a business 1099-C, the workflow combines this routing with the Form 982 mechanics from the other examples.

---

## The borrower

- **Name:** Priya Sharma
- **Business:** Sharma Consulting LLC (single-member LLC, taxed as disregarded entity → Schedule C)
- **Business code (NAICS):** 541611 (Administrative management consulting)
- **Filing status:** Single
- **Tax year:** 2025 (filing in 2026)
- **Federal marginal bracket without the cancellation:** 24%

## Background

Priya runs a consulting business. In 2023 she opened a business credit line with a regional bank ($30,000 limit) for cash-flow smoothing. Used proceeds for: business software subscriptions, contractor payments, marketing, equipment. By mid-2024 she had drawn $22,000; cash flow problems followed. She negotiated with the bank in early 2025; bank accepted $6,000 and canceled the remaining $16,000.

She is **not** insolvent (her business has grown substantially in 2025; she has retirement savings and equipment). She did not file bankruptcy. The debt is purely business — she can document each draw was used for business purposes.

## The 1099-C

| Box | Field | Value |
|-----|-------|-------|
| 1 | Date of identifiable event | 2025-04-18 |
| 2 | Amount of debt discharged | $16,000 |
| 3 | Interest if included in Box 2 | $1,200 |
| 4 | Debt description | Business credit line |
| 5 | Borrower personally liable? | Yes (personal guarantee on the line) |
| 6 | Identifiable event code | F (by agreement) |
| 7 | FMV of property | (blank) |

## Step 1 — Confirm the 1099-C is hers

Form addressed to Priya Sharma with her SSN (single-member LLC; bank uses her SSN as the disregarded-entity owner). Matches her 1040 identity. ✅

If the bank had issued the 1099-C to the LLC's EIN: still routes to Priya's individual return because the LLC is disregarded. The agent would note the EIN/SSN mismatch and document why it's still her income.

## Step 2 — Read the form

Internal record built. Box 6 = F (negotiated settlement). Personal guarantee → recourse debt. No foreclosure (Box 7 blank).

## Step 3 — Classify the debt

**Business credit line used for business purposes** → **business debt**.

Default routing target: **Schedule C Line 6 (other income)** — not Schedule 1 Line 8c.

This is the routing decision the agent has to make explicitly. Schedule 1 Line 8c is for personal-debt cancellations; business cancellations for sole proprietors go on Schedule C as other income, where they're subject to **self-employment tax** along with other Schedule C income.

If Priya were a partnership, S-corp, or C-corp, the cancellation would route to the entity return (1065, 1120-S, or 1120) — not the individual 1040. As a single-member LLC taxed as disregarded entity, she reports on Schedule C.

## Step 4 — Test exclusions in order

### 4a. Bankruptcy — §108(a)(1)(A)

No bankruptcy. **Does not apply.**

### 4b. Insolvency — §108(a)(1)(B)

Worksheet 2 immediately before 2025-04-18:

**Liabilities:**

- Business credit line being canceled: $22,000 (pre-settlement balance — what was outstanding before the settlement payment)
- Wait: Priya paid the $6,000 settlement on 2025-04-18. The "immediately before" measurement is the moment before the bank's cancellation, which is contemporaneous with her settlement payment. Use $22,000 (full pre-settlement balance) as the liability.
- Other business debt: $4,000 (vendor accounts payable)
- Personal credit cards: $5,000
- Auto loan: $14,000
- **Total liabilities:** $45,000

**Assets:**

- Business checking: $11,000
- Personal checking + savings: $9,000
- 401(k): $48,000
- Brokerage: $22,000
- Car (KBB): $18,000
- Business equipment basis: $7,000
- **Total assets:** $115,000

**Insolvency = $45,000 − $115,000 = −$70,000.** Priya is **not** insolvent. §108(a)(1)(B) does not apply.

### 4c. Principal residence — §108(a)(1)(E)

Renter. **Does not apply.**

### 4d. Student loan — §108(f)

No student loan being canceled. **Does not apply.**

### 4e. Qualified farm — §108(a)(1)(C)

Not a farmer. **Does not apply.**

### 4f. Qualified real property business indebtedness — §108(a)(1)(D)

Priya doesn't own depreciable real property in her business (she works from a co-working space, equipment only). **Does not apply.**

## Step 5 — Determine reporting path

No exclusion applies. Full $16,000 is reportable as income.

- **Routing:** Schedule C Line 6 (other income)
- **No Form 982 needed**
- Income flows into Schedule C net profit, then Schedule SE for self-employment tax

## Step 6 — Apply attribute reduction

Not applicable (no exclusion claimed).

## Step 7 — Run validation checks

**Math:**

- [x] Box 2 ($16,000) matches Priya's recollection of the canceled balance
- [x] Insolvency tested: $45,000 − $115,000 = −$70,000 (not insolvent) ✓
- [x] Routing target = Schedule C Line 6 (business debt, sole proprietor) ✓
- [x] No Form 982 (no exclusion claimed) ✓

**Sanity:**

- [x] Box 6 = F + personal use of card → confirmed business use of every draw → routes to Schedule C, not Schedule 1
- [x] Single-member LLC → disregarded entity → Schedule C is correct
- [x] Personal guarantee (Box 5 = Yes) → recourse → standard cancellation income (no foreclosure)
- [x] No 1099-A received (no asset surrendered)
- [x] Single 1099-C (no aggregation issue)

**Cross-form:**

- [x] Schedule C Line 6 = $16,000 (added to other Line 6 items)
- [x] Schedule C net profit increases by $16,000 → flows to Schedule 1 Line 3
- [x] Schedule SE recomputed: net SE earnings × 92.35% × 15.3% (subject to SS wage base)
- [x] Self-employment tax increases by ~$2,260 (based on 16,000 × 0.9235 × 0.153)
- [x] Half of additional SE tax (~$1,130) deductible on Schedule 1 Line 15

## Step 8 — Deliverable: Reporting Plan

```markdown
# Form 1099-C Reporting Plan — DRAFT for tax year 2025

## 1099-C as reported by creditor
- Creditor: Regional Business Bank
- Box 1 (date of event):           2025-04-18
- Box 2 (amount discharged):       $16,000
- Box 3 (interest in Box 2):       $1,200
- Box 4 (debt description):        Business credit line
- Box 5 (personally liable):       Yes (personal guarantee)
- Box 6 (event code):              F (by agreement)
- Box 7 (FMV of property):         N/A

## Classification
- Debt type:                       Business (sole prop / SMLLC disregarded)
- Default reporting target:        Schedule C Line 6 (other income)

## Exclusion analysis
- Bankruptcy (§108(a)(1)(A)):      Does not apply
- Insolvency (§108(a)(1)(B)):
  - Liabilities immediately before: $45,000
  - Assets immediately before:      $115,000
  - Insolvency amount:              $0 (assets > liabilities)
  - Exclusion amount:               $0
- Principal residence (§108(a)(1)(E)): Does not apply (renter)
- Student loan (§108(f)):          Does not apply
- Qualified farm:                  Does not apply
- Qualified real property biz:     Does not apply (no depreciable real property)

## Reporting outcome
- Excluded via Form 982:           $0 (no exclusion applies)
- Reported as income:              $16,000 on Schedule C Line 6
- Federal income tax at 24% bracket: ~$3,840
- Additional self-employment tax (15.3% on 92.35%): ~$2,260
- Half-SE-tax deduction on Schedule 1 Line 15: ~$1,130
- **Net additional tax: ~$5,830** (income tax + SE tax − half-SE deduction at 24%)

## Form 982 draft
- Not required (no exclusion claimed)

## Required attachments
- None beyond what's already required for Schedule C and Schedule SE
- Retain 1099-C, settlement letter from bank, business credit line draw history
  showing business use of every draw — for ≥6 years

## Validation summary
- Math: all checks passed
- Sanity: business use of every credit-line draw documented; routes correctly to
  Schedule C; insolvency tested and not applicable
- Year-aware flags: none
- Next steps:
  - Add $16,000 to Schedule C Line 6 (Part I)
  - Recompute Schedule C net profit (Line 31)
  - Flow to Schedule 1 Line 3
  - Recompute Schedule SE (Lines 2-6, 10-13)
  - Update half-SE deduction on Schedule 1 Line 15
  - If Priya makes quarterly estimates, increase 2025 Q4 estimate by tax owed
    on this $16,000 to avoid underpayment penalty
  - Retain settlement letter as evidence of cancellation event for ≥6 years

## Sources cited in this plan
- IRC §61(a)(11) (canceled debt = income)
- IRC §108(a)(1)(B) (insolvency tested as fallback — not applicable)
- IRC §1402 (self-employment tax on Schedule C net earnings)
- IRS Pub 4681 (Chapter 1 — business debt cancellation)
- Schedule C Instructions (current revision) — Line 6 includes canceled business debt
- Schedule SE Instructions (current revision)
```

## Step 9 — Handoff

- Add $16,000 to Schedule C Line 6
- Recompute Schedule C net profit (Line 31)
- Recompute Schedule SE
- Adjust quarterly estimated payments for 2025 if not yet paid
- Retain documentation: 1099-C, settlement letter, credit line statements showing business use
- **Note:** No Form 982; no entry on Schedule 1 Line 8c

## Result

**Total additional federal tax: ~$5,830** (income tax $3,840 + net SE tax $1,990 after half-SE deduction).

The number is meaningful but the routing was correct: putting the $16,000 on Schedule 1 Line 8c instead would have **understated** Priya's SE tax by ~$2,260 (because Schedule 1 Line 8c income doesn't flow through Schedule SE). The IRS would catch this in cross-checking and assess back tax + interest + accuracy penalty.

---

## Why each non-obvious choice

**Why Schedule C Line 6 instead of Schedule 1 Line 8c?** Schedule 1 Line 8c is for **personal** canceled debt. Business debt forgiven for a sole proprietor goes on Schedule C as other income — Line 6. The Schedule C instructions specifically include canceled business debt as Line 6 income. This routing matters because Schedule C income is subject to self-employment tax; Schedule 1 Line 8c income is not. Reporting business cancellation on Schedule 1 understates SE tax.

**Why is Priya not insolvent even though she had cash-flow problems?** Insolvency is a balance-sheet concept (liabilities vs. assets at FMV), not a cash-flow concept. Priya has $48,000 in 401(k), $22,000 in brokerage, and other assets that vastly exceed her liabilities. Cash-flow distress without balance-sheet insolvency does not qualify for §108(a)(1)(B). This is a common confusion.

**Why is the personal guarantee relevant?** Box 5 = Yes (recourse) means the bank could go after Priya personally if she didn't pay. This is the typical case for business credit lines to small entities. Recourse vs. nonrecourse only matters here as a confirmation that there's actual cancellation income (vs. nonrecourse where the deficiency might fold into a disposition). With no foreclosure (Box 7 blank), the analysis is just standard cancellation income.

**What about the §108(a)(1)(D) qualified real property business indebtedness exclusion?** That exclusion is for non-corporate taxpayers with **depreciable real property** used in a trade or business. Priya's business is a consulting business with no real property. The exclusion doesn't apply. If Priya had owned a commercial building used in her business and the canceled debt was secured by that building, §108(a)(1)(D) might apply with a basis reduction.

**Why does this affect Schedule SE?** Self-employment tax under IRC §1402 applies to net earnings from self-employment, which is Schedule C net profit (with adjustments). Adding $16,000 to Schedule C net profit increases SE earnings, which increases SE tax at 15.3% on the portion below the SS wage base + 2.9% (or 3.8% with Additional Medicare) above. For Priya at 24% federal bracket, the SE tax is the bigger surprise — she expected income tax on the cancellation but didn't think about SE tax.

**What if Priya had used the credit line for a mix of business and personal expenses?** Allocate the canceled debt between business and personal portions. Business portion → Schedule C Line 6; personal portion → Schedule 1 Line 8c. The allocation must be defensible (transaction-level evidence of how each draw was used).

**What if Priya had been an S-corp?** The S-corp would receive the 1099-C and report the cancellation on Form 1120-S, passing through to Priya as a shareholder via K-1. Schedule C wouldn't be used. Different routing entirely.

**What if Priya were insolvent on the business side but solvent overall?** §108(a)(1)(B) is measured at the **taxpayer** level (the individual), not the business level. Even if her business has more liabilities than assets, her personal balance sheet (which includes the business as an asset for a sole prop / disregarded entity) is what matters. For sole props and SMLLCs, business assets and liabilities are owner's assets and liabilities for §108 purposes.
