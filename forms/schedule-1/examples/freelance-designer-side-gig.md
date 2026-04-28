# Example: Freelance Designer with Side-Gig Etsy Income

The canonical "knowledge-worker freelancer with a side gig" pattern. Combines Schedule C net profit with above-the-line adjustments — student loan interest, SE health insurance, SEP-IRA, half SE tax. Mirrors the worked example in the [Jupid blog companion](https://jupid.com/blog/schedule-1-additional-income-adjustments-2026).

## The filer

- **Name**: Maya Lopez
- **Status**: Single, no dependents
- **Tax year**: 2026 (filing in 2027)
- **Primary work**: Freelance graphic design (sole proprietor)
- **Side activity**: Digital prints on Etsy
- **Both activities reported on a single Schedule C** (same business: design services + design product sales — same NAICS code, same EIN)

## Inputs gathered (Step 2-5 of workflow)

### Schedule C (already completed by `schedule-c` skill)

| Item | Amount |
|------|--------|
| Schedule C Line 1 (gross receipts: $45,300 design 1099s + $3,200 Etsy 1099-K) | $48,500 |
| Schedule C Line 28 (total expenses) | $8,500 |
| **Schedule C Line 31 (net profit)** | **$40,000** |

The Etsy 1099-K is a **trade or business** 1099-K, so it goes on Schedule C — **not** on the 1099-K reconciliation row above Part I and not on Line 8.

### Schedule SE (already completed by `schedule-se` skill)

| Item | Amount |
|------|--------|
| Net SE earnings ($40,000 × 0.9235) | $36,940 |
| SE tax ($36,940 × 0.153) | $5,652 |
| Half of SE tax (Line 13) | $2,826 |

### Part I — additional income items

Walked through with Maya:

- **Line 1 (state refund)**: Maya took the standard deduction in 2025. Line 1 = $0.
- **Line 2a (alimony received)**: No. Line 2a = $0.
- **Line 3 (Schedule C)**: $40,000.
- **Line 4 (other gains)**: No business asset sales. Line 4 = $0.
- **Line 5 (Schedule E)**: No rentals or K-1s. Line 5 = $0.
- **Line 6 (Schedule F)**: Not a farmer. Line 6 = $0.
- **Line 7 (unemployment)**: No 1099-G Box 1. Line 7 = $0.
- **Line 8a-8z**: Walked through every sub-line. None apply. Line 9 = $0.

### Part II — adjustments

- **Line 11 (educator)**: Not a K-12 teacher. $0.
- **Line 12 (reservist/artist)**: No. $0.
- **Line 13 (HSA)**: Maya is on a marketplace ACA plan that is NOT an HDHP. Not eligible. $0.
- **Line 14 (Armed Forces moving)**: No. $0.
- **Line 15 (half SE tax)**: $2,826 (from Schedule SE).
- **Line 16 (SEP-IRA)**: Maya contributed $1,500 to a SEP-IRA. Cap check: 20% of $40,000 (simplified) = $8,000. $1,500 is well under. ✓
- **Line 17 (SE health insurance)**: Maya paid $4,200 in marketplace ACA premiums. Eligibility check: Maya was not eligible for any employer plan (single, no spouse, not employed). ✓ Cap check: $4,200 < $40,000 SE income. ✓
- **Line 18 (early withdrawal)**: No. $0.
- **Line 19a (alimony paid)**: No. $0.
- **Line 20 (Traditional IRA)**: Maya didn't contribute (chose SEP-IRA instead). $0.
- **Line 21 (student loan interest)**: Maya paid $700 of student loan interest (1098-E Box 1). Cap check: $700 < $2,500. ✓ Phaseout check: Maya's MAGI is well below the $80,000 single phaseout. ✓
- **Line 22**: Blank.
- **Line 23 (Archer MSA)**: No. $0.
- **Line 24 (other)**: All sub-lines $0.

## The completed Schedule 1 draft

```markdown
# Schedule 1 — DRAFT for tax year 2026

## Header
Name(s): Maya Lopez
SSN: XXX-XX-XXXX
1099-K reported in error or for personal items sold at a loss: $0

## Part I — Additional Income
 1. Taxable refunds:                          $0
 2a. Alimony received:                        $0
 2b. Date of original decree:                 (n/a)
 3. Business income (Schedule C):             $40,000
 4. Other gains (Form 4797/4684):             $0
 5. Rental, royalties, partnerships (Sch E):  $0
 6. Farm income (Sch F):                      $0
 7. Unemployment compensation:                $0
 8. Other income:
    8a. Net operating loss:                   $0
    8b. Gambling:                             $0
    8c. Cancellation of debt:                 $0
    8d. Foreign earned income exclusion:      $0
    8e. Income from Form 8853:                $0
    8f. Income from Form 8889:                $0
    8g. Alaska PFD:                           $0
    8h. Jury duty pay:                        $0
    8i. Prizes and awards:                    $0
    8j. Hobby income:                         $0
    8k. Stock options:                        $0
    8l. Personal property rental:             $0
    8m. Olympic/Paralympic medals:            $0
    8n. §951(a) inclusion:                    $0
    8o. §951A(a) GILTI:                       $0
    8p. §461(l) excess loss:                  $0
    8q. ABLE distributions:                   $0
    8r. Scholarship/fellowship:               $0
    8s. Medicaid waiver (negative):           $0
    8t. NQDC / nongovt §457:                  $0
    8u. Wages while incarcerated:             $0
    8v. Digital assets (ordinary):            $0
    8z. Other (list):                         $0
 9. Total other income (sum 8a-8z):           $0
10. ADDITIONAL INCOME (= Form 1040 Line 8):   $40,000

## Part II — Adjustments to Income
11. Educator expenses:                        $0
12. Reservist/artist/fee-basis (Form 2106):   $0
13. HSA deduction (Form 8889):                $0
14. Armed Forces moving (Form 3903):          $0
15. Half of SE tax (Schedule SE):             $2,826
16. SEP-IRA / SIMPLE / qualified plans:       $1,500
17. SE health insurance:                      $4,200
18. Early withdrawal penalty:                 $0
19a. Alimony paid:                            $0
19b. Recipient SSN:                           (n/a)
19c. Date of original decree:                 (n/a)
20. Traditional IRA deduction:                $0
21. Student loan interest:                    $700
22. Reserved for future use:                  (blank)
23. Archer MSA deduction:                     $0
24. Other adjustments:
    24a. Jury duty turned over:               $0
    24b. Personal property rental expenses:   $0
    24c. Olympic/Paralympic offset:           $0
    ... (all other sub-lines):                $0
    24z. Other (list):                        $0
25. Total other adjustments (sum 24a-24z):    $0
26. ADJUSTMENTS TO INCOME (= Form 1040 Line 10): $9,226

## Required attachments
- [x] Schedule C (Line 3 = $40,000)
- [x] Schedule SE (Line 15 = $2,826)
- [ ] Form 8889 — N/A (no HSA)
- [ ] Form 3903 — N/A
- [ ] Form 2106 — N/A
- [ ] Form 8853 — N/A

## Validation summary
- Math: Line 9 = sum of 8a-8z = $0. Line 10 = $0 + $0 + $40,000 + $0 + $0 + $0 + $0 + $0 = $40,000. ✓
        Line 25 = $0. Line 26 = $0+$0+$0+$0+$2,826+$1,500+$4,200+$0+$0+$0+$700+$0+$0 = $9,226. ✓
- Sanity:
  - Line 3 ($40,000) > $400 → Schedule SE attached ✓
  - Line 17 ($4,200) ≤ Line 3 ($40,000) → IRC §162(l) cap satisfied ✓
  - Line 17: Maya not eligible for any employer plan → eligibility satisfied ✓
  - Line 21 ($700) ≤ $2,500 cap → ✓
  - Line 21: MAGI well below $80,000 single phaseout → no reduction ✓
  - Line 1 = $0: confirmed Maya took standard deduction in 2025 ✓
- Next steps:
  - Schedule 1 Line 10 ($40,000) → Form 1040 Line 8
  - Schedule 1 Line 26 ($9,226) → Form 1040 Line 10
  - Form 1040 AGI = $40,000 − $9,226 = $30,774
  - Apply standard deduction (~$15,700 single, 2026 estimate — verify) and QBI deduction (~$3,073 estimate)

## Sources cited in this draft
- IRS Schedule 1 (Form 1040), 2025 revision (carry-forward to 2026)
- IRS Form 1040 General Instructions
- IRC §61, §62, §162(l), §164(f), §221, §223
- Rev. Proc. 2024-40 (2025 inflation adjustments — 2026 figures pending)
- Notice 2024-80 (2025 retirement plan limits — 2026 pending)
```

## Why each non-obvious choice

**Why is the Etsy 1099-K not on Line 8 or the 1099-K reconciliation row?** The Etsy activity is a regular, profit-motive trade or business (Maya sells consistently, prices for profit, treats it like a side business). It belongs on **Schedule C**. The $3,200 1099-K shows up in Schedule C Line 1 alongside the $45,300 of design 1099-NECs. After expenses, the net flows once to Schedule 1 Line 3.

**Why is Line 13 (HSA) zero when Maya has marketplace health insurance?** HSAs require a qualifying **High-Deductible Health Plan**. Maya's marketplace ACA plan is a standard plan (deductible too low to qualify). She cannot contribute to an HSA, so Line 13 = $0. The premiums she paid go on Line 17 (SE health insurance), not Line 13.

**Why SEP-IRA only $1,500 when the cap is much higher?** Maya's effective SEP-IRA cap is ~20% of net SE earnings ≈ $8,000. She chose to contribute $1,500 — her actual contribution drives the deduction, not the cap. The cap is a ceiling, not a target.

**Why is the half-SE-tax (Line 15) deductible but not the full SE tax?** IRC §164(f) allows the deduction of the "employer-equivalent" half of FICA — mirroring how an employer deducts payroll tax for a W-2 employee. The other half is the "employee" portion and is not deductible.

**Why no IRA deduction (Line 20) alongside the SEP-IRA (Line 16)?** Maya could in principle have contributed to both a Traditional IRA and a SEP-IRA. She chose to focus the contribution on the SEP-IRA (higher cap, simpler accounting). Line 20 reflects only Traditional IRA contributions Maya actually made — zero.

**Why is the student loan interest deductible despite the standard deduction?** Above-the-line deductions (everything in Part II) are available **regardless of standard vs. itemized**. This is why Part II is so valuable — it produces a deduction without requiring Schedule A.

## What if Maya were audited

Defense by line:
- Line 3: cross-check 1099-NECs + Etsy 1099-K against Schedule C Line 1; expense substantiation per the Schedule C audit defense file
- Line 15: Schedule SE attached; calculation matches
- Line 16: SEP-IRA contribution confirmation from custodian (Vanguard, Fidelity, etc.)
- Line 17: marketplace 1095-A showing premiums paid; documentation that Maya was self-employed and not eligible for any employer plan during the year
- Line 21: 1098-E from servicer showing $700 interest

The four documents are easy to retrieve and self-evident — this is a clean return.

## Maya's tax outcome

```
Form 1040 Line 8  (additional income from Sch 1 L10):       $40,000
Form 1040 Line 9  (total income, no W-2 / interest / etc.): $40,000
Form 1040 Line 10 (adjustments from Sch 1 L26):              $9,226
Form 1040 Line 11 (AGI):                                    $30,774
Form 1040 Line 12 (standard deduction, 2026 single est.):   $15,700
Form 1040 Line 13 (QBI deduction, 20% of QBI estimate):      $3,073
Form 1040 Line 15 (taxable income):                         $12,001
Federal income tax (single, 10-12% brackets):               ~$1,200
Plus SE tax (full, not just half):                           $5,652
Total federal tax owed:                                     ~$6,852
```

Without the four Schedule 1 adjustments, AGI would have been $40,000, taxable income ~$21,200, federal income tax ~$2,400 (plus the $5,652 SE tax). The adjustments saved Maya roughly **$1,200** in federal income tax, plus better positioning for any state credits keyed to AGI.
