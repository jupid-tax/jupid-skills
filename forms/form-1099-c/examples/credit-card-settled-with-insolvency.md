# Example: Settled Credit Card with Insolvency Exclusion

A complete walkthrough of a 1099-C for a personal credit card that was settled for less than the balance, where the borrower was insolvent immediately before the cancellation. This is the canonical "consumer insolvency" pattern and produces $0 federal tax via Form 982 Box 1b.

The numbers here mirror Jenna's case from the [companion blog post](https://jupid.com/blog/form-1099-c-cancellation-debt-2026), with the worksheet expanded.

---

## The borrower

- **Name:** Jenna Doe
- **Filing status:** Single
- **Tax year:** 2025 (filing in 2026)
- **Federal marginal bracket without the cancellation:** 22%

## The 1099-C

Jenna received a 1099-C in late January 2026 from Chase Card Services (her credit card issuer). She had owed $18,000; she negotiated a settlement, paid $5,000 in cash, and the bank canceled the remaining $13,000.

| Box | Field | Value |
|-----|-------|-------|
| 1 | Date of identifiable event | 2025-09-12 |
| 2 | Amount of debt discharged | $13,000 |
| 3 | Interest if included in Box 2 | $1,400 |
| 4 | Debt description | Credit card |
| 5 | Borrower personally liable? | Yes |
| 6 | Identifiable event code | F (by agreement) |
| 7 | FMV of property | (blank — no foreclosure) |

She has only this one 1099-C for 2025. The card was used for personal purchases; no business expenses. She did not file bankruptcy. She is not a homeowner (renter). She does not have student loans being discharged.

## Step 1 — Confirm the 1099-C is hers

Form is addressed to Jenna Doe with her SSN. Matches her 1040 identity. ✅

## Step 2 — Read the form

Internal record built in the prerequisites table above.

## Step 3 — Classify the debt

Personal credit card used for personal purchases → **personal debt**.

Default routing target: **Schedule 1 Line 8c**.

## Step 4 — Test exclusions in order

### 4a. Bankruptcy — §108(a)(1)(A)

Jenna has not filed bankruptcy. **Does not apply.**

### 4b. Insolvency — §108(a)(1)(B)

Jenna gathers her financial position immediately before 2025-09-12.

**Worksheet 2 — Liabilities (immediately before discharge)**

| Item | Amount |
|------|--------|
| Credit card being canceled (full $18,000 pre-settlement balance) | $18,000 |
| Other credit cards (Discover + Capital One) | $20,000 |
| Auto loan (Toyota Financial) | $25,000 |
| **Total liabilities** | **$63,000** |

**Worksheet 2 — Assets (immediately before discharge, at FMV)**

| Item | FMV | Source |
|------|-----|--------|
| Checking + savings | $5,000 | Bank statements 2025-09-12 |
| Car (2018 Toyota Corolla, 65k miles) | $12,000 | Kelley Blue Book private-party value |
| 401(k) balance | $25,000 | Vanguard statement 2025-09-12 |
| **Total assets** | **$42,000** | |

**Insolvency = $63,000 − $42,000 = $21,000**

Jenna is insolvent by $21,000 immediately before the cancellation. The canceled amount ($13,000) is **less than** her insolvency ($21,000), so she can exclude the **full $13,000**.

**Note on retirement account inclusion:** Jenna's 401(k) is included as an asset at face value, per Rev. Rul. 92-53 and Pub 4681. She had been told by a friend that 401(k)s are "protected" so didn't count — that's wrong for §108 federal tax purposes.

**Note on canceled-debt inclusion:** the $18,000 pre-settlement balance is in liabilities (not the post-settlement $0). §108(d)(3) measures "immediately before" the discharge.

### 4c. Qualified principal residence — §108(a)(1)(E)

Jenna rents. Not applicable. **Does not apply.**

### 4d. Student loan — §108(f)

No student loans being canceled. **Does not apply.**

### 4e/f. Farm / business real property

Not a farmer; no business real property. **Does not apply.**

## Step 5 — Determine reporting path

Insolvency fully covers the $13,000 cancellation.

- **Form 982 Box 1b** checked
- **Line 2** = $13,000
- **No income reported on Schedule 1 Line 8c**

## Step 6 — Apply attribute reduction

Jenna's tax attributes:

| Attribute | Amount |
|-----------|--------|
| NOL (current and carryover) | $0 |
| General business credits | $0 |
| Minimum tax credits | $0 |
| Capital loss carryover | $0 |
| Basis of business property | $0 |
| Passive activity losses | $0 |
| Foreign tax credit carryovers | $0 |

Jenna has no tax attributes to reduce. Part II of Form 982 = all zeros. The $13,000 exclusion is permanent (not deferred via attribute reduction).

## Step 7 — Validation checks

**Math:**

- [x] Box 2 amount ($13,000) agrees with what Jenna recalls being canceled
- [x] Liabilities − Assets = Insolvency: $63,000 − $42,000 = $21,000 ✓
- [x] Excluded amount ($13,000) ≤ Insolvency ($21,000) ✓
- [x] Form 982 Line 2 ($13,000) = sum of exclusions claimed ✓
- [x] No basis reduction on Line 10a/b (renter, no qualifying basis) ✓

**Sanity:**

- [x] Retirement accounts included as assets ✓
- [x] Canceled debt itself included in liabilities at face value ✓
- [x] Single 1099-C (no aggregation issue)
- [x] Box 6 = F, personal use confirmed (not business)
- [x] No principal-residence exclusion claimed (renter), so no year-status concern
- [x] No 1099-A received (no foreclosure layered analysis)

**Cross-form:**

- [x] Form 982 attached to 1040 ✓
- [x] Worksheet 2 prepared and retained (not filed, kept in records) ✓

## Step 8 — Deliverable: Reporting Plan

```markdown
# Form 1099-C Reporting Plan — DRAFT for tax year 2025

## 1099-C as reported by creditor
- Creditor: Chase Card Services
- Box 1 (date of event):           2025-09-12
- Box 2 (amount discharged):       $13,000
- Box 3 (interest in Box 2):       $1,400
- Box 4 (debt description):        Credit card
- Box 5 (personally liable):       Yes
- Box 6 (event code):              F (by agreement)
- Box 7 (FMV of property):         N/A

## Classification
- Debt type:                       Personal
- Default reporting target:        Schedule 1 Line 8c

## Exclusion analysis
- Bankruptcy (§108(a)(1)(A)):      Does not apply (no bankruptcy filed)
- Insolvency (§108(a)(1)(B)):
  - Liabilities immediately before: $63,000
  - Assets immediately before:      $42,000
  - Insolvency amount:              $21,000
  - Exclusion amount:               $13,000 (canceled < insolvency, full coverage)
- Principal residence (§108(a)(1)(E)): Does not apply (renter)
- Student loan (§108(f)):          Does not apply (no student loan)
- Farm / business real property:   Does not apply

## Reporting outcome
- Excluded via Form 982:           $13,000 (Box 1b checked)
- Reported as income:              $0 on Schedule 1 Line 8c
- Federal tax estimate at marginal rate: $0 (vs. ~$2,860 without the exclusion)

## Form 982 draft
- Part I:
  - Box 1a (Title 11):             ☐
  - Box 1b (insolvency):           ☑
  - Box 1c (qualified farm):       ☐
  - Box 1d (qualified real prop):  ☐
  - Box 1e (principal residence):  ☐
  - Line 2 (amount excluded):      $13,000
- Part II — attribute reduction:
  - Line 6 (NOL):                  $0
  - Line 7 (general business cr.): $0
  - Line 8 (minimum tax credits):  $0
  - Line 9 (capital loss carryov.): $0
  - Line 10a (basis non-deprec.):  $0
  - Line 10b (basis prin. res.):   $0
  - Line 11 (passive activity):    $0
  - Line 12 (foreign tax credits): $0
  - "No attributes to reduce"

## Required attachments
- [x] Form 982 (insolvency claimed)
- [x] Worksheet 2 from Pub 4681 (kept in records, not filed)

## Validation summary
- Math: all checks passed
- Sanity: retirement balance and pre-cancellation debt face both included
- Year-aware flags: none (no QPRI or ARPA student loan exclusion claimed)
- Next steps:
  - Attach Form 982 to 1040
  - Keep Worksheet 2, KBB printout, Vanguard statement, bank statements
    in tax records for 6 years
  - No basis adjustments; no carryforwards
  - Schedule SE not affected (personal debt)

## Sources cited in this plan
- IRC §61(a)(11) (canceled debt = income)
- IRC §108(a)(1)(B) (insolvency exclusion)
- IRC §108(d)(3) (insolvency definition)
- Rev. Rul. 92-53 (retirement accounts as §108 assets)
- IRS Pub 4681 (Worksheet 2)
- Form 982 and Instructions (current revision)
```

## Step 9 — Handoff

- Attach Form 982 to Jenna's 1040 (e-file or paper)
- Do **not** report the $13,000 on Schedule 1 Line 8c
- Retain Worksheet 2, KBB printout, Vanguard 401(k) statement, bank statements in tax file for 6 years
- No basis carryforward (no property basis reduced)
- Schedule SE unchanged (personal debt, no SE tax impact)

## Result

**Federal tax on the canceled debt: $0** (vs. ~$2,860 without the exclusion).

---

## Why each non-obvious choice

**Why include the 401(k) as an asset?** Rev. Rul. 92-53 and Pub 4681. State-law creditor protection doesn't matter for §108. Excluding the 401(k) would have inflated insolvency to $46,000, but in audit the IRS would correct it; the result for Jenna is the same exclusion ($13,000) because canceled < insolvency either way.

**Why include the full $18,000 (not the post-settlement $0) as a liability?** §108(d)(3) measures "immediately before" the discharge. The pre-settlement balance counts.

**Why is Box 3's $1,400 not separately treated?** Box 3 is informational. The Box 2 amount is the income figure; cash-method individual borrowers don't have basis in unpaid interest. The $1,400 is just part of the $13,000.

**Why is no income reported on Schedule 1 Line 8c?** The full $13,000 is excluded via Form 982. Reporting it on Schedule 1 and then trying to subtract it elsewhere would be wrong; Form 982 is the documented path.

**What if Jenna had been audited?** Her audit defense:

1. 1099-C in records (matches what Chase reported)
2. Worksheet 2 with line-item liabilities and assets
3. KBB printout for car FMV
4. Vanguard statement for 401(k)
5. Bank statements for checking + savings
6. Loan statements for auto loan and other credit cards
7. Original Chase statement showing the $18,000 pre-settlement balance
8. Form 982 attached to her 1040 with Box 1b and Line 2 = $13,000
