# Example: Insolvent Taxpayer Excluding $13K Credit Card Debt

A complete walkthrough of Form 982 Box 1b (insolvency exclusion) for canceled credit card debt. Pattern: Worksheet 2 confirms insolvency; full canceled amount excluded; attribute reduction applied.

## The filer

- **Name**: Jordan Reyes
- **Filing status**: Single
- **Tax year**: 2025 (filing in 2026)
- **Event**: Credit card issuer canceled $13,000 in October 2025 after a long collection period
- **1099-C received**: Box 2 = $13,000; Box 1 = 10/14/2025; Box 6 code = G (decision to discontinue collection)

Jordan was technically insolvent at the time of cancellation. They want to exclude the full $13,000 from income.

## Step 1 — Verify the 1099-C

- Box 2: $13,000 ✓
- Box 3: $0 (no separately stated interest)
- Box 4: "Citibank Visa account ending 4231"
- Box 5: Yes (borrower was personally liable)
- Box 6: G (decision to discontinue collection)
- Box 7: blank (no property; this is unsecured credit card)

The 1099-C is correct. Jordan agrees the $13,000 was discharged.

## Step 2 — Identify exclusion

Walk through:
- (A) Bankruptcy: no Title 11 case → skip
- (E) Principal residence: not real estate → skip
- (B) Insolvency: test required → continue with Worksheet 2
- (C) Farm: not a farmer → skip
- (D) QRPBI: no real property business debt → skip

Only insolvency could apply. Run Worksheet 2.

## Step 3 — Pub 4681 Worksheet 2

Snapshot date: 10/14/2025 (just before discharge).

### Liabilities (immediately before)

| Item | Amount |
|------|--------|
| Mortgage on primary residence | $148,000 |
| Other credit cards (3 active) | $19,200 |
| The canceled debt itself (Citibank) | $13,000 |
| Auto loan | $7,800 |
| Federal student loans | $42,500 |
| State tax debt (back taxes) | $3,200 |
| Past-due medical bills | $4,400 |
| **Total liabilities** | **$238,100** |

### Assets (FMV, immediately before)

| Item | Amount |
|------|--------|
| Checking + savings | $620 |
| Real estate: primary residence (Zillow estimate) | $172,000 |
| Vehicle (KBB used value) | $9,500 |
| Vested 401(k) | $34,800 |
| Roth IRA | $4,200 |
| Furniture / electronics (used / garage-sale value) | $1,800 |
| Life insurance cash value (small whole-life policy) | $2,300 |
| **Total assets** | **$225,220** |

### Insolvency calculation

```
Total liabilities:    $238,100
- Total assets (FMV): $225,220
= Insolvency:         $12,880
```

Jordan was insolvent by **$12,880** immediately before the discharge.

## Step 4 — Compute excluded amount

Lesser of:
- Canceled debt: $13,000
- Insolvency: $12,880

**Excluded amount: $12,880** (Form 982 Line 2)

**Included on Schedule 1 Line 8c**: $13,000 − $12,880 = **$120** (ordinary income)

This is a critical detail Jordan might have missed: insolvency caps the exclusion. The remaining $120 IS taxable income.

## Step 5 — Compute attribute reduction (§108(b))

Available attributes:
- Current-year NOL: $0 (Jordan had positive income)
- NOL carryovers: $0
- General business credit carryover: $0
- Minimum tax credit: $0
- Net capital loss + carryovers: $0
- Basis of depreciable property: $0 (no business assets; primary residence isn't depreciable)
- Passive activity loss carryovers: $0
- Foreign tax credit carryovers: $0
- **Other basis** (Line 9): basis of personal-use assets

Per §1017 ordering for Line 9, Jordan reduces basis in this order:
1. Real property used in trade/business (depreciable) — none
2. Personal property used in trade/business — none
3. Property held for income production — none
4. Inventory/AR — none
5. Personal-use property — vehicle ($9,500 basis), furniture ($1,800 used value), home (basis ~$165,000 from purchase)

The $12,880 reduction can apply to:
- Vehicle: $9,500 basis available
- Furniture: $1,800 available
- Home: $165,000 available (basis, not FMV — purchase price + improvements)

Jordan's choice: reduce home basis (preserves vehicle basis for future depreciation if they ever rent it out, though unlikely; preserves furniture's negligible basis).

After reduction: Home basis = $165,000 − $12,880 = **$152,120**.

This affects future home sale: when Jordan sells, capital gain will be $12,880 higher (offsetting the $12,880 not paid as tax now). At ~15% long-term capital gains rate, future tax cost ≈ $1,932. Compare to current marginal rate of ~22% if Jordan had paid tax on the $12,880 = $2,834. Net benefit to Jordan: ~$900 NPV (assuming home sale at far enough future point and §121 exclusion limits exhausted by other gain).

## Step 6 — §108(b)(5) election

Should Jordan elect §108(b)(5) to apply basis reduction first?

The election is moot here — Jordan has no NOLs, credits, or capital losses to "preserve". The default order would just go straight to Line 9 anyway. **Do not check Line 3.**

## The completed Form 982 draft

```markdown
# Form 982 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Jordan Reyes
Identifying number: XXX-XX-XXXX

## Part I — General Information

| Line | Description | Value |
|------|-------------|-------|
| 1a | Discharge in a Title 11 case | [ ] |
| 1b | Discharge to extent insolvent (NOT Title 11) | [x] |
| 1c | Discharge of qualified farm indebtedness | [ ] |
| 1d | Discharge of qualified real property business indebtedness | [ ] |
| 1e | Discharge of qualified principal residence indebtedness | [ ] |
| 2 | Total amount of discharged indebtedness excluded from gross income | $12,880 |
| 3 | Election under §108(b)(5) | [ ] |

## Part II — Reduction of Tax Attributes

| Line | Attribute | Amount reduced |
|------|-----------|----------------|
| 4 | Basis under §108(b)(5) or §108(c) | $0 |
| 5 | NOL (current + carryover) | $0 (none available) |
| 6 | General business credit | $0 |
| 7 | Minimum tax credit | $0 |
| 8 | Net capital loss + carryover | $0 |
| 9 | Basis of other property (default) | $12,880 (allocated to home) |
| 10 | Passive activity loss + credit | $0 |
| 11 | Foreign tax credit carryover | $0 |
| | **Total Line 4-11** | **$12,880 = Line 2** ✓ |

## Insolvency Worksheet 2 (Pub 4681) — retained, NOT filed

| Item | Value |
|------|-------|
| **Liabilities immediately before discharge** | |
| Mortgage on primary residence | $148,000 |
| Other credit cards | $19,200 |
| Canceled debt itself (Citibank) | $13,000 |
| Auto loan | $7,800 |
| Federal student loans | $42,500 |
| State tax debt | $3,200 |
| Past-due medical bills | $4,400 |
| **Total liabilities** | $238,100 |
| **Assets (FMV) immediately before discharge** | |
| Checking + savings | $620 |
| Primary residence (FMV) | $172,000 |
| Vehicle (KBB) | $9,500 |
| Vested 401(k) | $34,800 |
| Roth IRA | $4,200 |
| Furniture / electronics | $1,800 |
| Life insurance cash value | $2,300 |
| **Total assets** | $225,220 |
| **Insolvency = Liabilities − Assets** | $12,880 |
| **Excluded under (B): lesser of $13,000 or $12,880** | $12,880 |

## Required attachments / off-form items
- [x] Form 1099-C (kept with records)
- [x] Insolvency Worksheet (retained)
- [ ] Bankruptcy discharge order (N/A)
- [ ] §108(c) QRPBI election (N/A)
- [x] Basis reduction schedule for home: original $165,000 → $152,120
- [x] Schedule 1 Line 8c: $120 (non-excluded portion)

## Validation summary
- Math: all checks passed
  - Insolvency = $238,100 − $225,220 = $12,880 ✓
  - Excluded = lesser of $13,000 or $12,880 = $12,880 ✓
  - Lines 4-11 sum = $12,880 = Line 2 ✓
  - Schedule 1 Line 8c = $13,000 − $12,880 = $120 ✓
- Sanity:
  - Box 1b checked once; no other Line 1 boxes
  - Worksheet 2 includes retirement (401(k) + Roth IRA) — common omission, included correctly
  - Worksheet 2 includes life insurance cash value — common omission, included correctly
  - Canceled debt itself included in liabilities for "immediately before" snapshot — correct
  - $120 reported as ordinary income on Schedule 1 Line 8c — captures non-excluded portion
  - Home basis reduction recorded — affects future §121 home sale calculation
- §108(b)(5) election: NOT made (no NOLs / credits to preserve)
- Next steps:
  - Retain Worksheet 2, 1099-C, and asset/liability documentation for at least 3 years
  - Update home basis records: $165,000 → $152,120
  - Report $120 on Schedule 1 Line 8c
  - When home is sold in the future, use $152,120 as the adjusted basis (subject to §121 exclusion at sale)

## Sources cited in this draft
- IRS Form 982, 2025 revision
- IRS Instructions for Form 982, 2025 revision
- IRS Pub 4681 (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRS Pub 4681 Worksheet 2 (Insolvency Worksheet)
- IRC §61(a)(11) (discharge of indebtedness as gross income)
- IRC §108(a)(1)(B) (insolvency exclusion)
- IRC §108(b) (attribute reduction order)
- IRC §108(d)(3) (definition of insolvency)
- IRC §1017 (basis reduction allocation)
- Form 1099-C from Citibank dated 10/14/2025
```

## Why each non-obvious choice

**Why exclude only $12,880 instead of the full $13,000?** §108(a)(1)(B) caps the exclusion at the insolvency amount. Jordan was $12,880 insolvent; the remaining $120 of the $13,000 canceled debt is ordinary income. Many users miss this and exclude the entire 1099-C amount, which is wrong.

**Why include retirement accounts in the asset list?** §108(d)(3) tests insolvency using the FMV of ALL assets. Pub 4681 explicitly includes retirement balances. Tax court has consistently confirmed (e.g., Carlson v. Commissioner). Excluding retirement is the most common Worksheet 2 mistake.

**Why include the canceled debt itself in liabilities?** The insolvency test uses the snapshot IMMEDIATELY BEFORE the discharge. At that moment, the debt was still owed. After the discharge it goes away. Pub 4681 makes this explicit.

**Why apply basis reduction to the home rather than the vehicle?** The vehicle has limited basis ($9,500); reducing home basis ($165K) preserves more total basis flexibility. Both are personal-use property, so Jordan can choose. The home basis reduction may eventually be absorbed by §121's $250K single-filer exclusion at home sale, making it a low-cost reduction.

**Why not check the §108(b)(5) election?** Jordan has no NOLs, business credits, capital losses, or depreciable property. The election is meaningless without those attributes. The default order goes straight to Line 9 (other basis) regardless.

**What documentation does Jordan retain?**
1. Form 1099-C from Citibank
2. Citibank account statements showing the cancellation date and amount
3. Pub 4681 Worksheet 2 with all line items documented
4. Mortgage statement (Oct 2025) showing $148,000 balance
5. Other credit card statements (Oct 2025)
6. Auto loan statement
7. Student loan account statements
8. State tax debt notices
9. Medical bill statements
10. 401(k) and Roth IRA statements (Sept-Oct 2025)
11. Vehicle KBB printout (Oct 2025)
12. Home Zillow estimate or recent appraisal
13. Life insurance policy with cash value
14. Original home purchase records (basis substantiation)

Retain at least 3 years post-filing — and home basis records permanently (until the home is sold and §121 calculation is made).

**What if Jordan had been solvent?** If liabilities ≤ assets, the entire $13,000 would be ordinary income on Schedule 1 Line 8c. No Form 982 filed.

**What if Jordan was insolvent by $20,000 instead of $12,880?** Excluded amount = lesser of $13,000 (canceled) or $20,000 (insolvency) = $13,000 (full canceled amount). Schedule 1 Line 8c = $0. Form 982 Line 2 = $13,000. Lines 4-11 sum to $13,000.
