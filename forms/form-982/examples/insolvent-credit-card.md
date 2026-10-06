# Example: Insolvent Taxpayer Excluding $12,880 of $13K Credit Card Debt

A complete walkthrough of Form 982 Box 1b (insolvency exclusion) for canceled credit card debt. Pattern: the Pub. 4681 Insolvency Worksheet shows $12,880 of insolvency; that amount is excluded and $120 is taxable; the line 10a smallest-of test for a nonbusiness debt gives $0, so Part II is all zeros. Lines follow Form 982 (Rev. March 2018) and its Instructions (Rev. December 2021).

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
- (B) Insolvency: test required → continue with the Insolvency Worksheet
- (C) Farm: not a farmer → skip
- (D) QRPBI: no real property business debt → skip

Only insolvency could apply. Run the Insolvency Worksheet.

## Step 3 — Pub. 4681 Insolvency Worksheet

Snapshot date: 10/14/2025 (just before discharge).

### Liabilities (immediately before)

| Item | Worksheet line | Amount |
|------|----------------|--------|
| Mortgage on primary residence | 2 | $148,000 |
| Other credit cards (3 active) | 1 | $19,200 |
| The canceled debt itself (Citibank) | 1 | $13,000 |
| Auto loan | 3 | $7,800 |
| Federal student loans | 5 | $42,500 |
| State tax debt (back taxes) | 10 | $3,200 |
| Past-due medical bills | 4 | $4,400 |
| **Total liabilities** | **15** | **$238,100** |

### Assets (FMV, immediately before)

| Item | Worksheet line | Amount |
|------|----------------|--------|
| Checking + savings | 16 | $620 |
| Real estate: primary residence (Zillow estimate) | 17 | $172,000 |
| Vehicle (KBB used value) | 18 | $9,500 |
| Vested 401(k) | 28 | $34,800 |
| Roth IRA | 28 | $4,200 |
| Furniture / electronics (used / garage-sale value) | 20 | $1,800 |
| Life insurance cash value (small whole-life policy) | 31 | $2,300 |
| **Total assets** | **37** | **$225,220** |

### Insolvency calculation

```
Total liabilities:    $238,100
- Total assets (FMV): $225,220
= Insolvency:         $12,880
```

Jordan was insolvent by **$12,880** immediately before the discharge (worksheet line 38).

## Step 4 — Compute excluded amount

Lesser of:
- Canceled debt: $13,000
- Insolvency: $12,880

**Excluded amount: $12,880** (Form 982 Line 2)

**Included on Schedule 1 Line 8c**: $13,000 − $12,880 = **$120** (ordinary income)

This is a critical detail Jordan might have missed: insolvency caps the exclusion. The remaining $120 IS taxable income.

## Step 5 — Compute attribute reduction (§108(b))

Available attributes:
- 2025 NOL and NOL carryovers: $0 (Jordan had positive income)
- General business credit carryover: $0
- Minimum tax credit: $0
- Net capital loss + carryovers: $0
- Depreciable property: none (no business assets; the home is personal-use)
- Passive activity loss and credit carryovers: $0
- Foreign tax credit carryovers: $0
- Basis of nondepreciable (personal-use) property, from Jordan's records (cost, not FMV):
  - Home: $165,000 (purchase price plus improvements)
  - Vehicle: $24,600 (2021 purchase price)
  - Furniture and electronics: $7,350 (cost)
  - Total: **$196,950**

Jordan's only attribute is basis in nondepreciable property, so follow the "A nonbusiness debt" steps in the Form 982 instructions. Line 10a = the **smallest** of:

| Test | Computation | Amount |
|------|-------------|--------|
| (a) Basis of nondepreciable property | $165,000 + $24,600 + $7,350 | $196,950 |
| (b) Nonbusiness debt excluded on line 2 | | $12,880 |
| (c) Bases of property + money held immediately after the discharge, minus liabilities immediately after | ($196,950 + $620) − ($238,100 − $13,000 = $225,100) = −$27,530 | $0 |
| **Line 10a** | smallest | **$0** |

No basis is reduced, so Jordan's home basis stays $165,000. Line 2 ($12,880) does not equal the Part II total ($0); the instructions allow that when the attributes, as limited, are smaller than the exclusion (i982 Line 2; §1017(b)(2)).

The bases above leave out the 401(k), the Roth IRA, and the life insurance policy. Counting their bases (for example Roth contributions or premiums paid) would change line 10a only if total bases exceeded $224,480 ($225,100 of liabilities after the discharge minus $620 of cash). Ask if that could be the case; here it is not.

## Step 6 — §108(b)(5) election (Line 5) and Line 3

Should Jordan elect §108(b)(5) to apply basis reduction first?

The election is moot here — Jordan has no depreciable property, and no NOLs, credits, or capital losses to "preserve". **Line 5 = $0.** Line 3 (treating real property held for sale as depreciable) doesn't apply: **No**.

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
| 3 | Elect to treat §1221(a)(1) real property as depreciable property? | No |

## Part II — Reduction of Tax Attributes (amount excluded applied)

| Line | Attribute | Amount |
|------|-----------|--------|
| 4 | QRPBI basis reduction | $0 |
| 5 | §108(b)(5) election | $0 |
| 6 | NOL (2025 + carryovers) | $0 (none available) |
| 7 | General business credit | $0 |
| 8 | Minimum tax credit | $0 |
| 9 | Net capital loss + carryover | $0 |
| 10a | Basis of nondepreciable and depreciable property | $0 (smallest of $196,950 / $12,880 / $0) |
| 10b | Basis of principal residence (1e only) | $0 |
| 11a–11c | Farm debt basis | $0 |
| 12 | Passive activity loss + credit | $0 |
| 13 | Foreign tax credit carryover | $0 |

Part II total $0 ≤ Line 2 $12,880 (allowed: i982 Line 2).

### Line 10a computation
| (a) Basis of nondepreciable property | $196,950 |
| (b) Nonbusiness debt on line 2 | $12,880 |
| (c) Bases $196,950 + money $620 − liabilities after $225,100 (not below $0) | $0 |
| Line 10a = smallest | $0 |

## Part III
Blank (corporations only)

## Insolvency Worksheet (Pub. 4681) — retained, NOT filed

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
| **Insolvency = Liabilities − Assets (worksheet line 38)** | $12,880 |
| **Excluded under (B): lesser of $13,000 or $12,880** | $12,880 |

## Required attachments / off-form items
- [x] Form 1099-C (kept with records)
- [x] Insolvency Worksheet (retained)
- [ ] Bankruptcy discharge order (N/A)
- [ ] §108(c) QRPBI election (N/A)
- [ ] Basis reduction schedule (N/A: line 10a = $0; home basis stays $165,000)
- [x] Schedule 1 Line 8c: $120 (non-excluded portion)

## Validation summary
- Math: all checks passed
  - Insolvency = $238,100 − $225,220 = $12,880 ✓
  - Excluded = lesser of $13,000 or $12,880 = $12,880 ✓
  - Line 10a = smallest of $196,950, $12,880, $0 = $0 ✓
  - Part II total $0 ≤ Line 2 $12,880 ✓ (need not be equal)
  - Schedule 1 Line 8c = $13,000 − $12,880 = $120 ✓
- Sanity:
  - Box 1b only; no title 11 case, no principal residence debt
  - Insolvency Worksheet includes retirement (401(k) + Roth IRA, line 28) — common omission, included correctly
  - Insolvency Worksheet includes life insurance cash value (line 31) — common omission, included correctly
  - Canceled debt itself included in liabilities for "immediately before" snapshot — correct
  - $120 reported as ordinary income on Schedule 1 Line 8c — captures non-excluded portion
  - No basis reduction: the §1017(b)(2) limit (test (c)) is $0
- §108(b)(5) election: NOT made (Line 5 = $0; no depreciable property)
- Next steps:
  - Retain the Insolvency Worksheet, 1099-C, and asset/liability documentation for at least 3 years
  - Keep home, vehicle, and furniture basis records (unchanged) for future sales
  - Report $120 on Schedule 1 Line 8c

## Sources cited in this draft
- IRS Form 982 (Rev. March 2018)
- IRS Instructions for Form 982 (Rev. December 2021), "A nonbusiness debt" and Line 2
- IRS Pub. 4681 (2025) (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRS Pub. 4681 (2025) Insolvency Worksheet
- IRC §61(a)(11) (discharge of indebtedness as gross income)
- IRC §108(a)(1)(B) (insolvency exclusion)
- IRC §108(b) (attribute reduction order)
- IRC §108(d)(3) (definition of insolvency)
- IRC §1017(b)(2) (basis reduction limit in insolvency cases)
- Form 1099-C from Citibank dated 10/14/2025
```

## Why each non-obvious choice

**Why exclude only $12,880 instead of the full $13,000?** §108(a)(1)(B) caps the exclusion at the insolvency amount. Jordan was $12,880 insolvent; the remaining $120 of the $13,000 canceled debt is ordinary income. Many users miss this and exclude the entire 1099-C amount, which is wrong.

**Why include retirement accounts in the asset list?** §108(d)(3) tests insolvency using the FMV of ALL assets. Pub. 4681 counts exempt assets such as retirement accounts and pension interests (worksheet lines 28–29), and Carlson v. Commissioner, 116 T.C. 87 (2001), held that assets exempt from creditors count. Excluding retirement is a common worksheet mistake.

**Why include the canceled debt itself in liabilities?** The insolvency test uses the snapshot IMMEDIATELY BEFORE the discharge. At that moment, the debt was still owed. After the discharge it goes away. Pub. 4681's repossession example does the same: it counts the full $8,500 car loan balance before the cancellation.

**Why is Part II all zeros when $12,880 was excluded?** In an insolvency case, basis reduction can't exceed the excess of the bases of property plus money held immediately after the discharge over the liabilities immediately after (§1017(b)(2); test (c) in the i982 "A nonbusiness debt" steps). Jordan's liabilities after the discharge ($225,100) exceed bases plus cash ($197,570), so the limit is $0. Had test (c) been positive, the reduction would be spread over the personal-use property in proportion to basis (Pub. 4681 car example: 91% furniture / 9% jewelry); Jordan could not pick the home or the car.

**Why not use the §108(b)(5) election (Line 5)?** Jordan has no depreciable property, so there is nothing for it to reduce. Line 3 is a different election (real property held for sale) and doesn't apply either.

**What documentation does Jordan retain?**
1. Form 1099-C from Citibank
2. Citibank account statements showing the cancellation date and amount
3. Pub. 4681 Insolvency Worksheet with all line items documented
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
14. Original home purchase and improvement records, car purchase contract, furniture receipts (basis substantiation for line 10a)

Retain for at least 3 years after filing; keep basis records until the period of limitations expires for the year each property is sold (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records).

**What if Jordan had been solvent?** If liabilities ≤ assets, the entire $13,000 would be ordinary income on Schedule 1 Line 8c. No Form 982 filed.

**What if Jordan was insolvent by $20,000 instead of $12,880?** Excluded amount = lesser of $13,000 (canceled) or $20,000 (insolvency) = $13,000 (full canceled amount). Schedule 1 Line 8c = $0. Form 982 Line 2 = $13,000. Line 10a is still the smallest-of test: (b) becomes $13,000 and (c) stays $0, so line 10a = $0.
