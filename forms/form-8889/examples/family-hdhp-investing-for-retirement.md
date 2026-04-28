# Example: Family HDHP, Investing for Retirement

End-to-end Form 8889 for a married couple treating the HSA as a long-horizon investment account. Tax year 2025.

---

## Background

- **Daniel**, age 38, employed at a tech company; covered by employer family HDHP that covers Daniel and his spouse Lisa
- **Lisa**, age 36, employed at a different company; her employer offers a self-only HDHP, but she elected coverage under Daniel's family HDHP instead
- Both HSA-eligible all 12 months of 2025 (no Medicare, no other disqualifying coverage, neither is a tax dependent)
- Combined household 24% federal bracket
- Daniel and Lisa agreed: Daniel funds the entire family limit into his HSA; Lisa contributes $0 to an HSA this year
- Daniel's HSA at Fidelity; he contributed $8,550 directly via bank transfer (NOT through cafeteria plan)
- They paid $2,400 of qualified medical expenses (doctor copays, prescriptions, dental cleanings) from their joint checking account in 2025 — receipts saved for future reimbursement
- Neither took any distribution from an HSA during 2025

---

## Daniel's Form 8889

Daniel is the primary contributor to the family HSA. He files Form 8889 for himself.

### Part I — HSA Contributions

```
Header
  Name: Daniel <last name>
  SSN: <Daniel's SSN>

Line 1: Coverage on Dec 1: Family ✓
Line 2: HSA contributions Daniel made (direct):     $8,550
Line 3: Contribution limit (family, 12 months):     $8,550
Line 4: Archer MSA contributions:                       $0
Line 5: Line 3 − Line 4:                            $8,550
Line 6: Line 5 (Daniel's allocated share, 100%):    $8,550
Line 7: Catch-up (under 55):                            $0
Line 8: Total limit:                                $8,550
Line 9: Employer contributions (W-2 Box 12 W):          $0
Line 10: Qualified HSA funding distribution:            $0
Line 11: Line 9 + Line 10:                              $0
Line 12: Line 2 + Line 11 (cap Line 8):             $8,550
Line 13: HSA deduction:                             $8,550
            → Schedule 1, Line 13
```

### Part II — HSA Distributions

```
Line 14a: Total distributions (1099-SA):                $0
Line 14b: Excess returns + rollovers:                   $0
Line 14c: Line 14a − Line 14b:                          $0
Line 15: Qualified medical expenses:                    $0
Line 16: Taxable HSA distributions:                     $0
Line 17a: Exception:                                  N/A
Line 17b: 20% additional tax:                           $0
```

Daniel took no distribution. Part II is all zeros.

### Part III — Failure to Maintain HDHP

Skip — Daniel did not use the last-month rule in a prior year.

### Reasoning

- **Why all $8,550 on Daniel**: Daniel and Lisa agreed Daniel would fund 100% of the family limit, so Lisa's allocated share of Line 6 is $0 and she doesn't file. Form 8889 instructions require each spouse with an HSA to file separately; Lisa has no HSA contributions or distributions, so she has no Form 8889 obligation.
- **Why Line 9 = $0**: Daniel contributed via bank transfer, not through his employer's cafeteria plan. The full $8,550 is direct (Line 2), so Line 13 captures the full deduction.
- **Why no distribution**: Daniel and Lisa pay current medical from cash and let the HSA balance compound. They've started the receipt pile for tax-free reimbursement decades from now.

### Combined household tax effect

| Item | Amount |
|------|--------|
| Daniel's HSA deduction (Schedule 1 Line 13) | $8,550 |
| Federal tax savings @ 24% | $2,052 |
| State tax savings (varies, est. 5%) | $428 |
| **Total first-year cash savings** | **~$2,480** |

If Daniel had instead routed the $8,550 through his employer's cafeteria plan, he'd also save 7.65% FICA = $654 more, for a total of ~$3,134. Worth investigating with his benefits administrator next open enrollment.

### Long-horizon math

Assumptions: $8,550 contributed annually, invested in a total-market index fund, 7% real return, $2,400/year of qualified medical expenses paid from cash with receipts saved.

- After 30 years: HSA balance ~$865,000; accumulated unreimbursed receipts ~$72,000
- At age 68, Daniel can withdraw $72,000 tax-free using the saved receipts
- Remaining ~$793,000 is available as Traditional-IRA-style retirement income (taxable but no penalty after 65)

---

## Lisa's Form 8889

Lisa contributed $0 and took no distribution → no Form 8889 obligation.

If Daniel and Lisa had instead split the family limit, e.g., $4,275 each, both would file:

### Lisa's hypothetical Form 8889 (50/50 split scenario)

```
Header
  Name: Lisa <last name>
  SSN: <Lisa's SSN>

Line 1: Family ✓
Line 2: HSA contributions Lisa made (direct):       $4,275
Line 3: Contribution limit (family, 12 months):     $8,550
Line 4: Archer MSA contributions:                       $0
Line 5: Line 3 − Line 4:                            $8,550
Line 6: Lisa's allocated share (50%):               $4,275
Line 7: Catch-up (under 55):                            $0
Line 8: Total limit:                                $4,275
Line 9: Employer contributions (W-2 Box 12 W):          $0
Line 10: Qualified HSA funding distribution:            $0
Line 11: Line 9 + Line 10:                              $0
Line 12: Line 2 + Line 11 (cap Line 8):             $4,275
Line 13: HSA deduction:                             $4,275
            → Schedule 1, Line 13
```

In the 50/50 scenario, Daniel's Form 8889 would also show Line 6 = $4,275 (his 50% share), Line 13 = $4,275. Combined Schedule 1 Line 13 = $8,550 (same total deduction, just split across two filers).

---

## Sources cited

- IRS Form 8889 (2025 revision)
- IRS Instructions for Form 8889 (2025 revision)
- IRC §223 (HSA eligibility, limits, distributions)
- IRC §213(d) (medical care definition)
- Rev. Proc. 2024-25 (2025 family HSA limit $8,550, self-only $4,300)
- IRS Publication 969
- IRS Publication 502
- Notice 2004-50 (HSA Q&A on documentation and qualified expenses)
