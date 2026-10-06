# Example: Medicare-Eligible Filer with Existing HSA

End-to-end Form 8889 for someone who just enrolled in Medicare and can no longer contribute to their HSA but continues to take qualified distributions. Tax year 2025.

---

## Background

- **Robert**, age 65, unmarried, retired from a long career as an architect
- Enrolled in Medicare Part A (hospital) and Part B (medical) during February, his 65th-birthday month, so coverage started **March 1, 2025** (sign-up in the birthday month → coverage the next month, medicare.gov)
- Did NOT take Social Security retirement benefits in 2025, so Part A is NOT retroactive — coverage is exactly the prospective enrollment date
- Had a self-only HDHP all year (employer retiree plan), but Medicare enrollment disqualifies HSA contributions from March 2025 forward
- HSA balance ~$180,000 at Fidelity, accumulated over 18 years of consistent contributions
- 24% federal bracket
- During 2025:
  - Contributed $700 by auto-deposit in January and February only (his limit for those 2 months is $883, see Line 3)
  - **Important**: he stopped his auto-deposit in February once Medicare took effect March 1
  - Took $14,200 in qualified distributions from the HSA: $8,400 for Medicare Part B premiums with IRMAA surcharges and Part D costs (the 2025 standard Part B premium alone is $185.00/mo × 10 months, March–December = $1,850), $5,800 for prescriptions, dental, and physical therapy after a knee surgery
- Did NOT take any non-qualified distributions

---

## Form 8889

### Part I — HSA Contributions

```
Header
  Name: Robert <last name>
  SSN: <Robert's SSN>

Line 1: Coverage on Dec 1: (NONE — Robert is on Medicare, not HSA-eligible)

  Note: Form 8889 instructions are tricky here. Line 1 reflects HDHP
  coverage status. Robert HAD self-only HDHP all year, but he was NOT
  HSA-ELIGIBLE from March onward due to Medicare enrollment. The
  contribution limit on Line 3 is prorated by ELIGIBLE months
  (Jan + Feb = 2), not by HDHP coverage months.

  For Line 1, check Self-only (his only HDHP coverage during the
  year). The contribution computation on Line 3 captures the limit.

Line 1: Self-only ✓
Line 2: HSA contributions Robert made (direct):       $700
Line 3: Contribution limit (Line 3 worksheet, 55+, self-only):
        Jan $5,300 + Feb $5,300 + Mar–Dec $0 (Medicare) = $10,600
        $10,600 / 12 = $883.33 ≈ $883
Line 4: Archer MSA contributions:                       $0
Line 5: Line 3 − Line 4:                              $883
Line 6: Line 5:                                       $883
Line 7: Additional contribution (not married):          $0
Line 8: Line 6 + Line 7:                              $883
Line 9: Employer contributions (W-2 Box 12 W):          $0
Line 10: Qualified HSA funding distribution:            $0
Line 11: Line 9 + Line 10:                              $0
Line 12: Line 8 − Line 11:                            $883
Line 13: HSA deduction (smaller of Line 2 or 12):     $700
            → Schedule 1, Line 13
```

### Part II — HSA Distributions

```
Line 14a: Total distributions (1099-SA Box 1):     $14,200
Line 14b: Excess returns + rollovers:                   $0
Line 14c: Line 14a − Line 14b:                     $14,200
Line 15: Qualified medical expenses:               $14,200
Line 16: Taxable HSA distributions:                     $0
Line 17a: Exception (age 65+):                  Not needed (Line 16 = 0)
Line 17b: 20% additional tax:                           $0
```

### Part III — Failure to Maintain HDHP

Skip — Robert did not use the last-month rule.

### Reasoning

- **Why prorate to 2 months**: Robert was HSA-eligible only January and February (Medicare started March 1; the worksheet enters -0- for Medicare months). He was not eligible on December 1, so the last-month rule does not apply. Because he is unmarried and 55+, the $1,000 additional contribution is built into each worksheet month ($4,300 + $1,000 = $5,300) and Line 7 stays $0: $5,300 × 2 ÷ 12 = $883.33 (Pub. 969 (2025) uses the same method: "$5,300 × 6 ÷ 12").
- **Why he didn't trip the excess-contribution wire**: He stopped his auto-deposit in February as soon as Medicare took effect March 1. Without that stop, every later deposit would have been an excess contribution, creating a 6% excise tax recurring annually until withdrawn.
- **Why Line 13 = $700**: Robert only contributed $700, all directly. Line 12 is $883, so Line 13 = smaller of $700 or $883 = $700.
- **Why all distributions are qualified**:
  - **Medicare Part B premiums after age 65 are qualified medical expenses** under Pub 502. (Medicare Part A, B, and D are qualified after 65; Medigap is NOT.)
  - Prescriptions, dental, and physical therapy are all on the Pub 502 list.
  - Robert's $14,200 in distributions all reimbursed real qualified expenses, so Line 15 = Line 14c.
- **Why Line 17a / 17b are irrelevant**: Line 16 = $0, so no penalty. Even if there had been a non-qualified distribution, Robert is 65+ — Line 17a exception applies (no 20% penalty), though the amount would still be ordinary income.

### What if Robert had taken Social Security?

Suppose instead Robert had skipped Medicare at 65 and filed for Social Security retirement benefits in October 2025. Premium-free Part A would start **6 months back** from the application, but not before the month he turned 65 (medicare.gov, "When does Medicare coverage start?"): April 1, 2025. In that case:

- His HSA-eligible months would be Jan–Mar (3 months) instead of Jan–Feb
- Line 3 would be 3 × ($5,300 / 12) = $1,325
- Line 7 = $0 (unmarried); Line 8 = $1,325
- His $700 contribution would still fit, but if he had auto-deposited through October, every deposit for April onward would be excess and he'd need to remove it

In a worse case where Robert files for Social Security at age 68 (retroactive 6 months), but had been contributing to the HSA the whole time at age 68, the retroactive Part A would create excess contributions for the prior 6 months. He'd owe 6% excise tax per year unless the excess is withdrawn (and any earnings on it become taxable income).

This is why the agent should ALWAYS ask users 64+ about both current Medicare enrollment AND Social Security plans before drafting Form 8889.

---

## What Robert should do going forward

- **No more contributions**: He's permanently disqualified from HSA contributions while on Medicare. The $180,000 balance remains his to use for qualified medical expenses tax-free (no time limit).
- **Keep using the HSA for Medicare premiums and other qualified expenses**: Part B premiums ($185.00/month standard for 2025) plus any IRMAA surcharges, Part D premiums, prescriptions, dental, vision, hearing aids — all qualified once he is 65 (Medigap premiums are not).
- **At his discretion, use the HSA for non-medical expenses too**: After 65, non-qualified distributions are taxable but **no 20% penalty**. Effectively a Traditional IRA at 65+.
- **Save the qualified expense receipts**: Even at 65+, qualified expenses are tax-free, so documenting them keeps the tax-free portion clean.

---

## Sources cited

- IRS Form 8889 (2025 revision)
- IRS Instructions for Form 8889 (2025 revision) — Line 3 partial-year proration worksheet
- IRC §223(b)(7) (no contributions while enrolled in Medicare)
- IRC §223(f)(4)(C) (no 20% penalty after Medicare eligibility age, 65)
- IRS Publication 969 (HSA + Medicare interaction)
- IRS Publication 502 (Medicare Part A, B, D as qualified medical expenses post-65)
- Rev. Proc. 2024-25 (2025 self-only limit $4,300); IRC §223(b)(3)(B) ($1,000 additional contribution)
- Medicare.gov, "When does Medicare coverage start?" (Part A starts 6 months back from a sign-up or Social Security application after 65, not before the month of turning 65)
- CMS fact sheet, "2025 Medicare Parts A & B Premiums and Deductibles" (Part B standard premium $185.00/month)
