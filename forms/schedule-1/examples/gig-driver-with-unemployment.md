# Example: Gig Driver Who Received Unemployment Early in the Year

A common pattern: filer was laid off in late 2024, collected unemployment for the first three months of 2025, then started driving for Uber + Lyft + DoorDash. The 2025 return (filed in 2026) needs to report unemployment (Line 7) AND Schedule C net profit from rideshare (Line 3), with the half-SE-tax adjustment (Line 15) and SE health insurance from individual coverage (Line 17). Math checked in Python.

## The filer

- **Name**: Marcus Chen
- **Status**: Single, no dependents
- **Tax year**: 2025 (filing in 2026)
- **First Q1**: laid off from prior W-2 job; collected unemployment Jan-March
- **April onward**: drove for Uber, Lyft, and DoorDash full-time; bought an individual health plan directly from an insurer (off the Marketplace, so no premium tax credit)

## Inputs gathered

### Unemployment (Form 1099-G Box 1)

- $9,800 received Jan 6 - March 28, 2025
- No repayments (the line 7 repayment box stays unchecked)

### Schedule C (already completed by `schedule-c` skill)

| Item | Amount |
|------|--------|
| Schedule C Line 1 (Uber 1099-K + Lyft 1099-K + DoorDash 1099-NEC) | $52,400 |
| Schedule C Line 28 (total expenses: standard mileage 28,000 mi × $0.70 = $19,600 (2025 rate, Notice 2025-5), plus $1,200 phone and supplies) | $20,800 |
| **Schedule C Line 31 (net profit)** | **$31,600** |

The rideshare 1099-Ks (Uber, Lyft) and DoorDash 1099-NEC are all trade-or-business income → Schedule C → Schedule 1 Line 3.

### Schedule SE

| Item | Amount |
|------|--------|
| Net SE earnings ($31,600 × 0.9235) | $29,183 |
| SE tax ($29,182 × 0.153) | $4,465 |
| Half of SE tax (Line 13) | $2,232 |

### Part I — additional income items

- **Line 1 (state refund)**: Marcus took the standard deduction for 2024. Line 1 = $0.
- **Line 2a (alimony received)**: No. $0.
- **Line 3 (Schedule C)**: $31,600.
- **Line 4 (other gains)**: No. $0.
- **Line 5 (Schedule E)**: No. $0.
- **Line 6 (Schedule F)**: No. $0.
- **Line 7 (unemployment)**: $9,800 from 1099-G Box 1.
- **Line 8a-8z**: All $0. Marcus had no gambling, no prizes, no jury duty, no hobby income, no digital asset income. Line 9 = $0.

### Part II — adjustments

- **Line 11 (educator)**: No. $0.
- **Line 12 (reservist/artist)**: No. $0.
- **Line 13 (HSA)**: his individual plan is not an HDHP. $0.
- **Line 14 (Armed Forces moving)**: No. $0.
- **Line 15 (half SE tax)**: $2,232 (from Schedule SE).
- **Line 16 (SEP-IRA)**: Marcus is putting money toward an emergency fund, not retirement, this year. $0.
- **Line 17 (SE health insurance)**: Marcus paid $3,600 in premiums on the individual plan for **April through December** (9 months) — the period he was self-employed and NOT eligible for any employer plan. Eligibility check: ✓ for those 9 months. No Marketplace advance premium tax credit, so the Line 17 worksheet applies (with APTC he would use Pub 974). The Jan-March COBRA premiums (~$800) from his prior employer plan are **NOT** deductible here — he was not self-employed yet (no SE earnings during that period). They could potentially be itemized on Schedule A medical, subject to AGI floor.
- **Line 18 (early withdrawal)**: No. $0.
- **Line 19a (alimony paid)**: No. $0.
- **Line 20 (Traditional IRA)**: No contribution this year. $0.
- **Line 21 (student loan interest)**: Marcus paid $1,100 of student loan interest on his prior degree (1098-E Box 1). Cap check: $1,100 < $2,500. ✓ Phaseout check: MAGI well below the $85,000 single phaseout start (2025). ✓
- **Line 22**: Blank.
- **Line 23 (Archer MSA)**: No. $0.
- **Line 24 (other)**: All sub-lines $0.

## The completed Schedule 1 draft

```markdown
# Schedule 1 — DRAFT for tax year 2025

## Header
Name(s): Marcus Chen
SSN: XXX-XX-XXXX
1099-K reported in error or for personal items sold at a loss: $0

## Part I — Additional Income
 1. Taxable refunds:                          $0
 2a. Alimony received:                        $0
 3. Business income (Schedule C):             $31,600
 4. Other gains:                              $0
 5. Rental, royalties, partnerships:          $0
 6. Farm income:                              $0
 7. Unemployment compensation:                $9,800
 8. Other income (8a-8z, all sub-lines):      $0
 9. Total other income:                       $0
10. ADDITIONAL INCOME (= Form 1040 Line 8):   $41,400

## Part II — Adjustments to Income
11. Educator expenses:                        $0
12. Reservist/artist/fee-basis:               $0
13. HSA deduction:                            $0
14. Armed Forces moving:                      $0
15. Half of SE tax:                           $2,232
16. SEP-IRA / SIMPLE / qualified plans:       $0
17. SE health insurance:                      $3,600
18. Early withdrawal penalty:                 $0
19a. Alimony paid:                            $0
20. Traditional IRA deduction:                $0
21. Student loan interest:                    $1,100
22. Reserved for future use:                  (blank)
23. Archer MSA deduction:                     $0
24. Other adjustments (24a-24k; 24z blank):   $0
25. Total other adjustments:                  $0
26. ADJUSTMENTS TO INCOME (= Form 1040 Line 10): $6,932

## Required attachments
- [x] Schedule C (Line 3 = $31,600)
- [x] Schedule SE (Line 15 = $2,232)
- [ ] Form 8889 — N/A
- [ ] Form 3903 — N/A

## Validation summary
- Math: Line 10 = $0+$0+$31,600+$0+$0+$0+$9,800+$0 = $41,400 ✓
        Line 26 = $0+$0+$0+$0+$2,232+$0+$3,600+$0+$0+$0+$1,100+$0+$0 = $6,932 ✓
- Sanity:
  - Net SE earnings ($29,183) ≥ $400 → Schedule SE attached ✓
  - Line 7 ($9,800) corroborated by 1099-G Box 1 ✓
  - Line 17 ($3,600): only the 9 months of SE-eligible coverage; Jan-Mar COBRA excluded ✓
  - Line 17 ($3,600) ≤ $29,368 (Line 3 − Line 15; Line 16 is $0) → cap satisfied ✓
  - Line 21 ($1,100) ≤ $2,500 cap ✓
  - Line 1 = $0: standard deduction prior year confirmed ✓
- Next steps:
  - Schedule 1 Line 10 ($41,400) → Form 1040 Line 8
  - Schedule 1 Line 26 ($6,932) → Form 1040 Line 10
  - Form 1040 line 11a AGI = $41,400 − $6,932 = $34,468

## Sources cited in this draft
- IRS Schedule 1 (Form 1040), 2025 revision, filed in 2026
- IRS Form 1040 General Instructions (2025)
- IRC §61, §62, §85, §162(l), §164(f), §221
- Notice 2025-5 (2025 standard mileage rate, 70 cents)
- Form 1099-G (state UI)
- Form 1098-E (student loan interest)
- Insurer premium statements (individual coverage)
```

## Why each non-obvious choice

**Why is unemployment fully taxable when "I'm just trying to get back on my feet"?** Federal tax law treats unemployment compensation as ordinary income (IRC §85). The pandemic-era ARPA exclusion of $10,200 (for tax year 2020 only) does not apply for 2025. Marcus owes federal income tax on the full $9,800.

**Why isn't COBRA deductible on Line 17?** Line 17 (SE health insurance, IRC §162(l)) requires that the deduction be for premiums paid "with respect to a trade or business in which the individual was an active participant." During Jan-March, Marcus had no SE income — he was unemployed. The COBRA premiums during that period don't tie to any business activity. They could potentially be itemized as medical expenses on Schedule A (subject to AGI floor and itemizing election) but cannot go above the line.

**Why split out months for Line 17?** IRC §162(l)(2)(B) is a month-by-month test. The eligibility test ("not eligible for an employer-subsidized plan and conducting a trade or business") must be met in each month claimed. Marcus's nine months of individual coverage starting April pass; the three months of COBRA before that don't.

**Why no SEP-IRA when there's net SE income?** Marcus has the eligibility but didn't contribute. Line 16 reflects actual contributions, not eligibility. A SEP-IRA for 2025 can still be set up and funded by the return due date (April 15, 2026, or October 15, 2026 with an extension); if he does that before filing, it goes on this return's Line 16.

**Why does Line 7 increase Marcus's AGI even though he's already paid into the unemployment system?** In most states, unemployment benefits are funded by employer payroll taxes (SUI/FUTA), not employee contributions. Either way, IRC §85 makes the benefit fully taxable. (Where a worker did contribute to a governmental unemployment program and doesn't itemize, the 2025 instructions let Line 7 be reduced by those contributions.)

## Marcus's tax outcome

```
Form 1040 Line 8   (additional income from Sch 1 L10):   $41,400
Form 1040 Line 9   (total income):                       $41,400
Form 1040 Line 10  (adjustments from Sch 1 L26):          $6,932
Form 1040 Line 11a (AGI):                                $34,468
Form 1040 Line 12e (standard deduction, 2025 single):    $15,750
Form 1040 Line 13a (QBI deduction):                       $3,744
  (lesser of 20% × QBI $25,768 = $5,154 and
   20% × ($34,468 − $15,750) = $3,744)
Form 1040 Line 15  (taxable income):                     $14,974
Federal income tax (2025 single, 10%/12% brackets):      ~$1,558
Plus SE tax (full):                                       $4,465
Total federal:                                           ~$6,023
```

Use the 2025 Tax Table for the exact line 16 figure.

**Quarterly estimates next year**: Marcus must start paying quarterly estimated taxes via Form 1040-ES going forward. SE tax alone is a meaningful liability not withheld at source. Hand the numbers to the `form-1040-es` skill ([`../../form-1040-es/SKILL.md`](../../form-1040-es/SKILL.md)) for the 2026 vouchers.

## What if Marcus had filed without Schedule 1

If Marcus had only filed Form 1040 with the W-2 from his prior job (which doesn't exist for 2025 — he was laid off at the end of 2024), he'd be missing both the $9,800 unemployment income (CP2000 from IRS) AND the $31,600 Schedule C profit (likely caught by 1099 matching from Uber/Lyft/DoorDash). The IRS sees both 1099-G and 1099-NEC/1099-K on its end — the return must reconcile to those. Schedule 1 is non-optional given his income mix.
