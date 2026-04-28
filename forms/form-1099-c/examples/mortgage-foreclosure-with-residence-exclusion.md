# Example: Mortgage Foreclosure with Principal Residence Exclusion

A complete walkthrough of a 1099-C arising from foreclosure of a borrower's principal residence, where §108(a)(1)(E) qualified principal residence indebtedness exclusion applies. This is the canonical "homeowner foreclosure" pattern.

This example assumes the §108(a)(1)(E) exclusion is in effect for the tax year (verified through Dec 31, 2025; **2026 status to be re-verified before filing**).

---

## The borrower

- **Name:** Marcus Chen
- **Filing status:** Married filing jointly
- **Tax year:** 2025 (filing in 2026)
- **Federal marginal bracket without the cancellation:** 24%

## Background

Marcus and his spouse bought a home in 2018 for $420,000 with a $400,000 fixed-rate mortgage. By 2024 they had paid the mortgage down to $385,000. Job loss in mid-2024 led to default; the lender foreclosed in 2025. The home sold at the foreclosure sale for $310,000 (FMV at that time). The lender canceled the remaining deficiency of $75,000 ($385,000 − $310,000) and issued both a 1099-A and a 1099-C in early 2026.

**Loan history (acquisition indebtedness only):**

- 2018-04 — Purchase mortgage: $400,000 acquisition debt
- 2020-08 — Refinanced at lower rate, kept balance at $390,000 (no cash-out)
- No HELOC, no second mortgage, no cash-out refinancing

All mortgage debt is acquisition indebtedness on the principal residence. ✅

## The 1099-C

| Box | Field | Value |
|-----|-------|-------|
| 1 | Date of identifiable event | 2025-08-22 |
| 2 | Amount of debt discharged | $75,000 |
| 3 | Interest if included in Box 2 | $0 |
| 4 | Debt description | Mortgage |
| 5 | Borrower personally liable? | Yes (recourse mortgage; state allows deficiency) |
| 6 | Identifiable event code | B (foreclosure) |
| 7 | FMV of property | $310,000 |

## The 1099-A (also received)

For completeness — the 1099-A documents the disposition:

| Box | Field | Value |
|-----|-------|-------|
| 1 | Date of acquisition or abandonment | 2025-08-22 |
| 2 | Balance of principal outstanding | $385,000 |
| 4 | FMV of property | $310,000 |
| 5 | Borrower personally liable? | Yes |

## Step 1 — Confirm the 1099-C is theirs

Form addressed to Marcus and spouse, joint mortgage. ✅ Joint return; either spouse can claim.

## Step 2 — Read the form

Internal record built. Box 6 = B (judicial foreclosure), Box 5 = Yes (recourse) → both a disposition (gain/loss) and a cancellation event. The disposition follows Pub 4681 Chapter 2; the cancellation follows §108.

## Step 3 — Classify the debt

Personal mortgage on principal residence → **personal debt**, but eligible for §108(a)(1)(E) qualified principal residence exclusion.

Default routing target if no exclusion: Schedule 1 Line 8c.

## Step 4 — Test exclusions in order

### 4a. Bankruptcy — §108(a)(1)(A)

No bankruptcy filed. **Does not apply.**

### 4b. Insolvency — §108(a)(1)(B)

Marcus considers insolvency as a fallback in case §108(a)(1)(E) doesn't fully cover. Worksheet 2 immediately before 2025-08-22:

**Liabilities:**

- Mortgage being foreclosed: $385,000
- Auto loans (two cars): $32,000
- Credit cards: $18,000
- Student loans: $48,000
- **Total liabilities:** $483,000

**Assets:**

- Home (FMV at foreclosure): $310,000
- Cars (KBB): $24,000
- 401(k) (combined): $145,000
- Roth IRA: $42,000
- Cash: $8,000
- **Total assets:** $529,000

**Insolvency = $483,000 − $529,000 = −$46,000.** Marcus is **not** insolvent. §108(a)(1)(B) does not apply.

### 4c. Qualified principal residence indebtedness — §108(a)(1)(E) ✅

**Test:**

- Acquisition indebtedness on principal residence? Yes — original purchase + rate refinance, no cash-out.
- Marcus's principal residence? Yes — primary home since 2018-04.
- Within the $750,000 cap (MFJ uses full $750,000)? Yes — canceled amount is $75,000.
- **Year-aware:** §108(a)(1)(E) is in effect for tax year 2025 (extended through 2025-12-31 by Consolidated Appropriations Act 2021). ✓

**Result:** Full $75,000 excluded under §108(a)(1)(E).

### 4d/e/f. Other exclusions

Not applicable.

## Step 5 — Determine reporting path

Principal residence exclusion fully covers $75,000.

- **Form 982 Box 1e** checked
- **Line 2** = $75,000
- **Line 10b** (basis of principal residence reduction) = $75,000
- **No income reported on Schedule 1 Line 8c**

## Disposition analysis (separate from §108)

The foreclosure is also a sale of the home for tax purposes. For recourse debt:

- Amount realized = lesser of (a) FMV at foreclosure ($310,000) or (b) outstanding loan balance ($385,000) = $310,000
- Adjusted basis (purchase price + improvements − §108(h)(1) reduction): Marcus's basis pre-reduction was $420,000 (purchase) + $15,000 (kitchen 2021) = $435,000.
- After §108(h)(1) reduction of $75,000: new basis = $360,000.
- Gain/loss on sale = Amount realized ($310,000) − Adjusted basis ($360,000) = **$50,000 loss**.
- Loss on personal residence is **not deductible** under IRC §165(c). The loss is realized economically but not for tax purposes.

If Marcus's home had been sold at a gain, IRC §121 would have excluded up to $500,000 of gain (MFJ, used home as principal residence ≥2 of last 5 years). The §108(h)(1) basis reduction would have eaten into the §121 exclusion margin but not produced taxable gain on these numbers.

## Step 6 — Apply attribute reduction

For §108(a)(1)(E) the only attribute reduced is the **basis of the principal residence**, on Form 982 Line 10b. Other Part II lines (NOL, business credits, etc.) are not affected by §108(h)(1).

- Line 10b = $75,000

The new basis of the home ($360,000) is recorded for Marcus's records — relevant if they buy a new home or for any future tax events.

## Step 7 — Validation checks

**Math:**

- [x] Box 2 ($75,000) = lender's reported deficiency
- [x] §108(a)(1)(E) cap ($750,000 MFJ) > $75,000 ✓
- [x] Form 982 Line 2 ($75,000) = Line 10b ($75,000) for QPRI exclusion ✓
- [x] No double-counting: $75,000 excluded as cancellation, separately the disposition shows $50,000 nondeductible loss

**Sanity:**

- [x] Acquisition indebtedness confirmed (no cash-out, no HELOC misuse)
- [x] Principal residence confirmed (utility bills, voter registration)
- [x] §108(a)(1)(E) in effect for 2025 ✓
- [x] 1099-A received → foreclosure disposition computed separately ✓
- [x] Recourse loan (Box 5 = Yes) → both events occur (separate disposition + cancellation)
- [x] Insolvency tested as fallback (not insolvent — but QPRI fully covers anyway)

**Cross-form:**

- [x] Form 982 attached to 1040
- [x] No Schedule D entry (personal residence loss is nondeductible; no entry required)
- [x] Basis records updated to $360,000 in tax file

## Step 8 — Deliverable: Reporting Plan

```markdown
# Form 1099-C Reporting Plan — DRAFT for tax year 2025

## 1099-C as reported by creditor
- Creditor: Wells Fargo Home Mortgage
- Box 1 (date of event):           2025-08-22
- Box 2 (amount discharged):       $75,000
- Box 3 (interest in Box 2):       $0
- Box 4 (debt description):        Mortgage
- Box 5 (personally liable):       Yes (recourse)
- Box 6 (event code):              B (foreclosure)
- Box 7 (FMV of property):         $310,000

## Classification
- Debt type:                       Personal — principal residence mortgage
- Default reporting target:        Schedule 1 Line 8c (if no exclusion)

## Exclusion analysis
- Bankruptcy (§108(a)(1)(A)):      Does not apply
- Insolvency (§108(a)(1)(B)):
  - Liabilities immediately before: $483,000
  - Assets immediately before:      $529,000
  - Insolvency amount:              $0 (assets > liabilities; not insolvent)
  - Exclusion amount:               $0 (does not apply)
- Principal residence (§108(a)(1)(E)): Applies
  - Year-status: Verified in effect for tax year 2025
  - Exclusion amount:               $75,000 (within $750,000 MFJ cap)
- Student loan (§108(f)):          Does not apply
- Farm / business real property:   Does not apply

## Reporting outcome
- Excluded via Form 982:           $75,000 (Box 1e checked)
- Reported as income:              $0 on Schedule 1 Line 8c
- Federal tax estimate at marginal rate: $0 (vs. ~$18,000 without exclusion)

## Form 982 draft
- Part I:
  - Box 1e (principal residence):  ☑
  - Line 2 (amount excluded):      $75,000
- Part II — attribute reduction:
  - Line 10b (basis prin. res.):   $75,000
  - All other lines:               $0

## Disposition analysis (Pub 4681 Chapter 2)
- Amount realized (recourse):      $310,000 (lower of FMV or balance)
- Basis pre-reduction:             $435,000 (purchase $420k + improvements $15k)
- §108(h)(1) basis reduction:      ($75,000)
- Adjusted basis:                  $360,000
- Loss on disposition:             $50,000
- Tax treatment:                   Nondeductible (personal residence loss, IRC §165(c))

## Required attachments
- [x] Form 982 (Box 1e checked)
- No Schedule D entry (loss is nondeductible)
- Worksheet 2 retained as fallback documentation (insolvency tested)

## Validation summary
- Math: all checks passed
- Sanity: acquisition indebtedness confirmed; principal residence confirmed
- Year-aware flags: §108(a)(1)(E) verified in effect for 2025; verify for 2026 if any
  late-arriving cancellations
- Next steps:
  - Attach Form 982 to MFJ 1040
  - Retain HUD-1 from purchase, refinance docs, improvement receipts,
    1099-A, 1099-C, foreclosure documents
  - Update basis records for any future home purchase analysis
  - Schedule D not needed (no deductible loss on personal residence)

## Sources cited in this plan
- IRC §108(a)(1)(E), §108(h) (qualified principal residence indebtedness)
- IRC §163(h)(3)(B) (acquisition indebtedness)
- IRC §165(c) (nondeductibility of personal residence loss)
- Pub 4681 (foreclosure analysis, Chapter 2)
- Form 982 and Instructions (current revision)
- Consolidated Appropriations Act 2021 (extension of §108(a)(1)(E) through 2025)
```

## Step 9 — Handoff

- Attach Form 982 to MFJ 1040
- No Schedule 1 Line 8c entry
- Disposition: foreclosure produces $50,000 nondeductible personal residence loss; no Schedule D entry needed
- Update home-basis records to $360,000 (relevant if Marcus and spouse later buy a new home and want to track)
- Retain documentation: HUD-1, refinance docs, improvement receipts, 1099-A, 1099-C, foreclosure court documents

## Result

**Federal tax on the canceled mortgage debt: $0** (vs. ~$18,000 without the exclusion).

---

## Why each non-obvious choice

**Why §108(a)(1)(E) and not insolvency?** Marcus tested insolvency first as a fallback, but he is **not** insolvent — assets exceed liabilities by $46,000. Without §108(a)(1)(E), he would have owed tax on the full $75,000. The principal residence exclusion is the entire benefit here.

**Why not cash-out the basis reduction immediately?** The §108(h)(1) basis reduction is mandatory and reduces the home's basis. Since Marcus no longer owns the home (foreclosed), the reduced basis informs the disposition analysis (smaller basis = smaller loss). For personal residences this only matters if there's gain (where §121 helps); for losses, the basis reduction means a smaller nondeductible loss.

**Why is the loss nondeductible?** IRC §165(c) limits individual loss deductions to losses incurred in a trade or business, transactions for profit, or casualty/theft. Sale of a personal residence at a loss is none of these.

**Why test insolvency at all if QPRI fully covers?** Two reasons: (1) audit defense — documenting that insolvency was tested shows complete analysis; (2) backup — if QPRI's year-status is later challenged or rules change retroactively, having the insolvency test on file is useful. For 2025 with QPRI confirmed in effect, the test is belt-and-suspenders.

**What if §108(a)(1)(E) had lapsed?** Insolvency would not have helped (Marcus not insolvent). Marcus would owe tax on the full $75,000 ($18,000 federal at 24%). This is exactly why year-status verification matters — extension delays can produce real tax exposure for foreclosure borrowers.

**What if the loan had been nonrecourse (Box 5 = No)?** No separate cancellation income. The full $385,000 outstanding balance would be the amount realized in the disposition, producing a $50,000 nondeductible loss ($385,000 − $435,000 basis). §108 would not apply at all; Form 982 would not be needed.

**What if Marcus had a HELOC for non-housing purposes?** That portion would not qualify for §108(a)(1)(E). Allocate canceled debt between QPRI (excluded) and non-QPRI (test insolvency or report as income). See Pub 4681 Worksheet 1.
