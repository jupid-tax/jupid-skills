# Example: Medicare-Eligible Filer with Existing HSA

End-to-end Form 8889 for someone who just enrolled in Medicare and can no longer contribute to their HSA but continues to take qualified distributions. Tax year 2025.

---

## Background

- **Robert**, age 65, retired from a long career as an architect
- Enrolled in Medicare Part A (hospital) and Part B (medical) effective **March 1, 2025** — the month after his 65th birthday in February
- Did NOT take Social Security retirement benefits in 2025, so Part A is NOT retroactive — coverage is exactly the prospective enrollment date
- Had a self-only HDHP all year (employer retiree plan), but Medicare enrollment disqualifies HSA contributions from March 2025 forward
- HSA balance ~$180,000 at Fidelity, accumulated over 18 years of consistent contributions
- 24% federal bracket
- During 2025:
  - Made HSA contributions in January and February only (2 months × ~$358 self-only monthly allowance = $716, rounded to $700 he contributed via auto-deposit)
  - **Important**: he stopped his auto-deposit in February once Medicare took effect March 1
  - Took $14,200 in qualified distributions from the HSA: $8,400 for Medicare Part B premiums (2025 standard premium ~$185/mo × 11 months = ~$2,035; he also had IRMAA surcharges plus prescription costs), $5,800 for prescriptions, dental, and physical therapy after a knee surgery
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

  For Line 1, check Self-only (the coverage type during the eligible
  months). The contribution computation on Line 3 captures the limit.

Line 1: Self-only ✓
Line 2: HSA contributions Robert made (direct):       $700
Line 3: Contribution limit (2 eligible months):
        2 × ($4,300 / 12) = $716.67 ≈ $717
Line 4: Archer MSA contributions:                       $0
Line 5: Line 3 − Line 4:                              $717
Line 6: Line 5:                                       $717
Line 7: Catch-up (age 55+, eligible 2 months):
        2 × ($1,000 / 12) = $166.67 ≈ $167
Line 8: Total limit:                                  $884
Line 9: Employer contributions (W-2 Box 12 W):          $0
Line 10: Qualified HSA funding distribution:            $0
Line 11: Line 9 + Line 10:                              $0
Line 12: Line 2 + Line 11 (cap Line 8):               $700
Line 13: HSA deduction:                               $700
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

- **Why prorate to 2 months**: Robert was HSA-eligible only January and February (Medicare started March 1). The contribution limit prorates by eligible months, not by HDHP-coverage months. Self-only annual = $4,300 / 12 × 2 = $716.67. Catch-up annual = $1,000 / 12 × 2 = $166.67.
- **Why he didn't trip the excess-contribution wire**: He stopped his auto-deposit in February as soon as Medicare took effect March 1. Without that proactive stop, he'd have been over the prorated limit by ~$3,500 (the auto-deposit times the remaining months of the year), creating a 6% excise tax recurring annually until withdrawn.
- **Why Line 13 = $700 instead of using the catch-up**: Robert only contributed $700, all directly. The full Line 8 limit is $884 (=$717 base + $167 catch-up), but his actual contribution is below that. Line 13 = min($700, $884 − $0) = $700.
- **Why all distributions are qualified**:
  - **Medicare Part B premiums after age 65 are qualified medical expenses** under Pub 502. (Medicare Part A, B, and D are qualified after 65; Medigap is NOT.)
  - Prescriptions, dental, and physical therapy are all on the Pub 502 list.
  - Robert's $14,200 in distributions all reimbursed real qualified expenses, so Line 15 = Line 14c.
- **Why Line 17a / 17b are irrelevant**: Line 16 = $0, so no penalty. Even if there had been a non-qualified distribution, Robert is 65+ — Line 17a exception applies (no 20% penalty), though the amount would still be ordinary income.

### What if Robert had taken Social Security?

If Robert had filed for Social Security retirement benefits in 2025, Medicare Part A enrollment would be **retroactive** — up to 6 months back from the application date, or back to his 65th birthday (whichever is later). For example, if he filed for Social Security in October 2025, Part A would be effective May 2025 (the lesser of 6 months retroactive vs. age 65 in February). In that case:

- His HSA-eligible months would shrink to Jan–Apr (4 months) instead of Jan–Feb
- Line 3 would be 4 × ($4,300 / 12) = $1,433
- Line 7 catch-up would be 4 × ($1,000 / 12) = $333
- Line 8 = $1,766
- His $700 contribution would still fit, but if he had auto-deposited longer (e.g., through April), he'd need to recompute and possibly remove excess

In a worse case where Robert files for Social Security at age 68 (retroactive 6 months), but had been contributing to the HSA the whole time at age 68, the retroactive Part A would create excess contributions for the prior 6 months. He'd owe 6% excise tax per year unless the excess is withdrawn (and any earnings on it become taxable income).

This is why the agent should ALWAYS ask users 64+ about both current Medicare enrollment AND Social Security plans before drafting Form 8889.

---

## What Robert should do going forward

- **No more contributions**: He's permanently disqualified from HSA contributions while on Medicare. The $180,000 balance remains his to use for qualified medical expenses tax-free (no time limit).
- **Keep using the HSA for Medicare premiums and other qualified expenses**: Part B premiums alone may exceed $2,500/year per person. With IRMAA surcharges they can exceed $5,000/year. Plus prescriptions, dental, vision, hearing aids — all qualified.
- **At his discretion, use the HSA for non-medical expenses too**: After 65, non-qualified distributions are taxable but **no 20% penalty**. Effectively a Traditional IRA at 65+.
- **Save the qualified expense receipts**: Even at 65+, qualified expenses are tax-free, so documenting them keeps the tax-free portion clean.

---

## Sources cited

- IRS Form 8889 (2025 revision)
- IRS Instructions for Form 8889 (2025 revision) — Line 3 partial-year proration worksheet
- IRC §223(b)(7) (no contributions while enrolled in Medicare)
- IRC §223(f)(4)(B) (no 20% penalty after age 65)
- IRS Publication 969 (HSA + Medicare interaction)
- IRS Publication 502 (Medicare Part A, B, D as qualified medical expenses post-65)
- Rev. Proc. 2024-25 (2025 self-only limit $4,300, catch-up $1,000)
- Social Security Administration guidance on Medicare Part A retroactive enrollment (up to 6 months when claiming retirement benefits after age 65)
