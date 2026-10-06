# Example: Solo Consultant with Schedule C (Daniel)

A complete walkthrough of the 2025 Form 1040 (filed in 2026) for a single freelance consultant with Schedule C income, retirement contributions, self-employed health insurance, and student loan interest. This is the canonical "self-employed knowledge worker" pattern. Line numbers follow the 2025 form; math checked in python.

## The filer

- **Name**: Daniel Chen
- **Status**: Single, age 32, no dependents
- **Business**: Freelance management consulting
- **Tax year**: 2025 (filing in 2026)
- **State**: California (state return separate)

## Inputs gathered (Step 2 of workflow)

### Income sources

| Source | Tax document | Amount | Goes to |
|--------|--------------|--------|---------|
| Acme Brand consulting | 1099-NEC | $51,600 | Schedule C |
| Other agency clients | 1099-NEC | $21,400 | Schedule C |
| Stripe direct invoices | none (38 payments; no 1099-K because 2025 reporting requires more than $20,000 AND more than 200 transactions) | $29,300 | Schedule C |
| Cash payments | none | $1,800 | Schedule C |
| **Schedule C Line 1** | | **$104,100** | |
| Personal Wells Fargo savings | 1099-INT | $1,200 | 1040 Line 2b |

No W-2 wages. No dependents. No spouse. Income without a 1099 is still reported.

Prior-year facts (for the Line 38 test): 2024 total tax (2024 Form 1040 line 24) $13,000; 2024 AGI under $150,000; 2025 estimated payments $3,500 on each of the four due dates.

### Schedule C bottom line

Built with the `schedule-c` skill:

- Line 7: Gross income $104,100
- Line 28: Total expenses $19,000
- Line 29: Tentative profit $85,100
- Line 30: Home office (simplified, 120 sq ft × $5) $600
- **Line 31: Net profit $84,500**

### Schedule SE

Per the `schedule-se` skill (2025 Schedule SE, whole dollars):
- Net earnings from self-employment (line 4a): $84,500 × 92.35% = $78,036
- SE tax (line 12): $78,036 × 12.4% = $9,676 + $78,036 × 2.9% = $2,263 = **$11,939**
- Half SE tax (line 13, deductible): **$5,970**

### Above-the-line adjustments (Schedule 1 Part II)

- Half SE tax (L15): $5,970
- SEP-IRA contribution (L16): $5,000
- Self-employed health insurance (L17): $4,200 (no employer-subsidized plan available to him)
- Student loan interest (L21): $700 (MAGI under the $85,000 start of the 2025 single phaseout)
- **Total Schedule 1 Line 26**: **$15,870**

### QBI computation (Form 8995)

Taxable income before QBI is under the 2025 threshold ($197,300 single), so simplified Form 8995.
- QBI = Schedule C profit − half SE tax − SE health insurance − SEP-IRA = $84,500 − $5,970 − $4,200 − $5,000 = **$69,330**
- Taxable income before QBI = AGI − standard deduction = $69,830 − $15,750 = $54,080
- 20% × QBI = $13,866
- 20% × taxable income before QBI = $10,816
- QBI deduction = lesser = **$10,816**

### No other schedules

- No itemized (renter, no mortgage; California income tax plus small charity stay well under the $15,750 standard deduction)
- No Schedule 1-A items (no qualified tips or overtime, no new-car loan, under 65)
- No Schedule D (no investments sold)
- No Schedule E (no rentals)

## The completed Form 1040 draft

```markdown
# Form 1040 — DRAFT for tax year 2025

## Header
Filing status: Single
Filer name: Daniel Chen     SSN: XXX-XX-XXXX
Address: 1234 Market St, San Francisco, CA 94103
Main home in the U.S. more than half of 2025: [x]
Digital assets question: No

Dependents: None

## Page 1 — Income
1a. Total W-2 wages:                  $0
1b. Household employee wages:         $0
1c. Tip income:                       $0
1d. Medicaid waiver payments:         $0
1e. Taxable dependent care benefits:  $0
1f. Adoption benefits:                $0
1g. Form 8919 wages:                  $0
1h. Other earned income:              $0
1i. Nontaxable combat pay election:   $0
1z. Sum of 1a-1h:                     $0

2a. Tax-exempt interest:              $0
2b. Taxable interest:                 $1,200
3a. Qualified dividends:              $0
3b. Ordinary dividends:               $0
4a. IRA distributions:                $0
4b. Taxable IRA distributions:        $0
5a. Pensions and annuities:           $0
5b. Taxable pensions:                 $0
6a. Social Security benefits:         $0
6b. Taxable SS:                       $0
6c. Lump-sum election:                [ ]
6d. MFS lived apart:                  [ ]
7a. Capital gain/loss (Sch D):        $0
7b. Schedule D not required / child's gain: [ ] [ ]
8. Schedule 1 additional income:      $84,500
9. TOTAL INCOME:                      $85,700

10. Adjustments (Schedule 1 L26):     $15,870
11a. AGI:                             $69,830

## Page 2 — Tax, Credits, Payments
11b. AGI (from 11a):                  $69,830
12a–12d. Dependent / spouse itemizes / dual-status / 65+ / blind: all [ ]
12e. Standard deduction (single):     $15,750
13a. QBI deduction (Form 8995):       $10,816
13b. Schedule 1-A deductions:         $0
14. Sum of 12e + 13a + 13b:           $26,566
15. TAXABLE INCOME:                   $43,264
16. Tax (Tax Table, single, row $43,250–43,300): $4,955
17. Schedule 2 L3:                    $0
18. Sum:                              $4,955
19. CTC / ODC (Sch 8812):             $0
20. Other credits (Sch 3 L8):         $0
21. Sum of 19 + 20:                   $0
22. Line 18 − line 21:                $4,955
23. Other taxes (Sch 2 L21):          $11,939   (SE tax from Schedule SE)
24. TOTAL TAX:                        $16,894

25a. W-2 withholding:                 $0
25b. 1099 withholding:                $0
25c. Other withholding:               $0
25d. Total withholding:               $0
26. Estimated tax payments:           $14,000
27a. EIC:                             $0
28. Additional CTC (Sch 8812):        $0
29. American opportunity credit:      $0
30. Refundable adoption credit:       $0
31. Sch 3 L15 refundable:             $0
32. Sum (27a + 28 + 29 + 30 + 31):    $0
33. TOTAL PAYMENTS:                   $14,000

34. Overpayment (refund):             $0
35a. Refunded directly:               $0
35b. Routing #:                       N/A
35c. Account type:                    N/A
35d. Account #:                       N/A
36. Applied to next year:             $0
37. Amount you owe:                   $2,894
38. Estimated tax penalty:            $0 (exception: lines 25d + 26 = $14,000 ≥ 100% of 2024 tax $13,000; 2024 AGI under $150,000)

## Required attachments
- [x] Schedule 1 (Schedule C income on L3 = $84,500; adjustments on L26 = $15,870)
- [x] Schedule 2 (SE tax on L4 = $11,939; total L21 = $11,939)
- [x] Schedule C (sole prop business; via `schedule-c` skill)
- [x] Schedule SE (net SE earnings $400 or more; via `schedule-se` skill)
- [x] Form 8995 (QBI deduction)
- [ ] Schedule 3 — not needed (no credits)
- [ ] Schedule A — not needed (taking standard)
- [ ] Schedule B — not needed (taxable interest $1,200, not over $1,500; no dividends; no foreign accounts)

## Validation summary
- Math: all checks passed
- Sanity warnings:
  - Daniel owes $2,894, but no Line 38 penalty: his four $3,500 payments covered 100% of his 2024 tax on time
  - QBI claimed correctly (often missed — flagged)
  - Schedule SE present (required when net SE earnings are $400 or more)
  - No quarterly state estimates verified — California separate return needed
- Next steps:
  - Pay $2,894 by April 15, 2026 to avoid the late-payment penalty and interest
  - 2026 estimates (per `form-1040-es` skill): 100% of the 2025 tax ($16,894) is $4,223.50 per quarter (100%, not 110%, because his 2025 AGI of $69,830 is not over $150,000), or 90% of the 2026 tax if that is lower
  - File California state return separately
  - Keep records for 3 years (audit window)

## Sources cited in this draft
- IRS Form 1040 (2025)
- 2025 Instructions for Form 1040 (Tax Table; Line 38 exception)
- IRC §1(j) (rate tables)
- IRC §63 as amended by P.L. 119-21 (2025 standard deduction $15,750)
- IRC §199A (QBI deduction, made permanent by P.L. 119-21)
- IRC §164(f) (half SE tax adjustment)
- IRC §162(l) (SE health insurance deduction)
- IRC §221 (student loan interest)
- IRC §§1401–1402 (SE tax); 2025 Schedule SE
- Rev. Proc. 2024-40 (2025 brackets, student loan phaseout)
```

## Why each non-obvious choice

**Why the $5,000 SEP-IRA, not a Solo 401(k)?** That was Daniel's choice; the skill doesn't pick plans. His contribution is well within the SEP limit: for a self-employed person, 20% of net earnings after half of SE tax (Pub. 560 rate table: 25% plan rate = 0.20 self-employed rate), here 20% × ($84,500 − $5,970) = $15,706, capped at $70,000 for 2025. A one-participant 401(k) adds employee deferrals but requires Form 5500-EZ once plan assets exceed $250,000.

**Why didn't Daniel itemize?** Schedule A items: California income tax paid (the 2025 SALT limit of $40,000 doesn't bind), no mortgage (renter), small charitable contributions (~$500), no major medical. Total Schedule A stays well under the $15,750 standard deduction. Standard wins.

**Why is QBI $10,816 and not $13,866?** QBI deduction is capped at the lesser of (20% × QBI) or (20% × taxable income before QBI, minus net capital gain). Daniel's taxable income before QBI = AGI $69,830 − standard $15,750 = $54,080. 20% × $54,080 = $10,816 (Form 8995 lines 11–15).

**Why is Line 16 $4,955 and not $4,953?** Taxable income under $100,000 must use the Tax Table, which taxes the midpoint of each $50 row ($43,275 here). The rate schedule on the exact $43,264 gives $4,953; the Table gives $4,955.

**Why no estimated tax penalty (Line 38)?** Line 37 ($2,894) is at least $1,000 and more than 10% of the tax, so the test starts. But the 2025 instructions' exception applies: his 2024 return covered 12 months, lines 25d + 26 ($14,000) are at least 100% of his 2024 tax ($13,000), his 2024 AGI was not over $150,000, and he paid $3,500 on each due date. Form 2210 isn't needed.

**Why $14,000 in estimated payments?** Daniel paid $3,500/quarter (4 × $3,500 = $14,000), about 108% of his 2024 tax, assuming the 110% rule applied. It didn't (2024 AGI under $150,000), so 100% would have been enough. For 2025, his actual tax is $16,894 — $2,894 more than paid.

**Why answer "No" to digital assets?** Daniel held a small Coinbase position bought in 2022. In 2025 he didn't receive any digital asset as a reward, award, or payment and didn't sell, exchange, or otherwise dispose of any. Holding alone is a "No" situation in the 2025 instructions.

## What if Daniel had been audited?

His audit defense would be:
1. Schedule C income matches all 1099-NECs + 1099-K + bank deposits for cash payments
2. SE tax computed correctly on Schedule SE
3. SEP-IRA contribution documented with custodian statement
4. SE health insurance documented with marketplace 1095-A and premiums paid
5. Student loan interest matches 1098-E from servicer
6. QBI computation traceable through Form 8995
7. Estimated payments documented via IRS account transcript
8. Bank routing/account verified for refund — but not applicable since balance due

## Key Form 1040 lessons from Daniel's return

1. **Self-employed people pay TWO taxes**: income tax (Line 16) + SE tax (Line 23). For Daniel, SE tax is more than 2× income tax.
2. **AGI matters more than gross income**: $84,500 profit → $69,830 AGI after $15,870 in above-the-line adjustments. Lower AGI = lower phaseouts of credits and benefits.
3. **QBI is the easy money**: up to 20% off business income (Line 13a), made permanent by P.L. 119-21. Always check eligibility.
4. **Quarterly estimates protect the self-employed**: $3,500 paid on each due date met the prior-year exception, so the $2,894 balance carries no penalty.
5. **Schedule C → Schedule 1 → Line 8** and **Schedule SE → Schedule 2 → Line 23** — these flows are non-obvious to first-time self-employed filers.
