# Example: Solo Consultant with HSA, SEP-IRA, and SE Health Insurance

A higher-income solo consultant who maxes the available retirement and health-savings stack: HSA on an HDHP, SEP-IRA from net SE earnings, and self-employed health insurance for the HDHP premiums. The most adjustment-heavy "stacked" Schedule 1 a solo filer typically produces.

## The filer

- **Name**: Priya Shah
- **Status**: Single, no dependents
- **Tax year**: 2026
- **Business**: Independent management consulting (sole proprietor)
- **Health coverage**: marketplace HDHP all year, so HSA-eligible

## Inputs gathered

### Schedule C (already completed)

| Item | Amount |
|------|--------|
| Schedule C Line 1 (consulting fees, six clients) | $145,000 |
| Schedule C Line 28 (expenses: travel, software, coworking, conferences, etc.) | $25,000 |
| **Schedule C Line 31 (net profit)** | **$120,000** |

### Schedule SE

| Item | Amount |
|------|--------|
| Net SE earnings ($120,000 × 0.9235) | $110,820 |
| SE tax — Social Security portion ($110,820 × 0.124, full because below SS wage base; 2026 base TBD) | $13,742 |
| SE tax — Medicare portion ($110,820 × 0.029) | $3,214 |
| **SE tax total (Sch SE Line 12)** | **$16,956** |
| **Half of SE tax (Sch SE Line 13)** | **$8,478** |

(The Social Security wage base for 2026 is announced October 2025; for this example using 2025's $176,100 base, Priya's earnings are fully below it.)

### HSA contribution (outside payroll)

- HDHP self-only coverage all year
- HSA contribution: $4,300 (matches 2025 self-only cap; 2026 announced May 2025 — verify before filing)
- Made by individual deposit, not via payroll → goes on Line 13

### SEP-IRA contribution

- Priya established a SEP-IRA in 2025
- Contribution worksheet (IRS Pub 560 simplified):
  ```
  Net SE earnings (after Line 15) = $120,000 − $8,478 = $111,522
  Effective deduction rate         = 0.20 (≈ 25%/(1+25%))
  SEP contribution                 = $111,522 × 0.20 = $22,304
  Cap (2025): $70,000 — within limit ✓
  ```
- Priya contributes the full $22,304 → Line 16

### Self-employed health insurance

- HDHP marketplace premium: $5,400 for the year (self-only, no family)
- Eligibility: Priya was not eligible for any employer plan (single, sole proprietor, no spouse) → ✓
- Cap check: $5,400 < $120,000 SE income → ✓
- Goes on Line 17

### Other items

- Student loan interest paid: $850 (1098-E Box 1). Cap $2,500 ✓. Phaseout: 2025 single $80,000-$95,000 → Priya's MAGI is calculated *before* student loan interest deduction; she's above the upper bound (MAGI ≈ $120,000 − adjustments other than SLI). Phaseout fully eliminates Line 21. **Line 21 = $0.**
- Educator: not a teacher. $0.
- Traditional IRA: Priya considered but instead routes retirement savings to the SEP-IRA. $0 on Line 20.
- Alimony: none. Lines 2a / 19a = $0.
- Unemployment, Schedule E, Schedule F, Line 8 sub-lines: all $0.
- State refund: Priya took the standard deduction in 2025. Line 1 = $0.

## The completed Schedule 1 draft

```markdown
# Schedule 1 — DRAFT for tax year 2026

## Header
Name(s): Priya Shah
SSN: XXX-XX-XXXX
1099-K reported in error or for personal items sold at a loss: $0

## Part I — Additional Income
 1. Taxable refunds:                          $0
 2a. Alimony received:                        $0
 3. Business income (Schedule C):             $120,000
 4. Other gains:                              $0
 5. Rental, royalties, partnerships:          $0
 6. Farm income:                              $0
 7. Unemployment compensation:                $0
 8. Other income (8a-8z):                     $0
 9. Total other income:                       $0
10. ADDITIONAL INCOME (= Form 1040 Line 8):   $120,000

## Part II — Adjustments to Income
11. Educator expenses:                        $0
12. Reservist/artist/fee-basis:               $0
13. HSA deduction (Form 8889):                $4,300
14. Armed Forces moving:                      $0
15. Half of SE tax (Schedule SE):             $8,478
16. SEP-IRA contribution:                     $22,304
17. SE health insurance:                      $5,400
18. Early withdrawal penalty:                 $0
19a. Alimony paid:                            $0
20. Traditional IRA deduction:                $0
21. Student loan interest:                    $0   (phased out — MAGI above ceiling)
22. Reserved for future use:                  (blank)
23. Archer MSA deduction:                     $0
24. Other adjustments:                        $0
25. Total other adjustments:                  $0
26. ADJUSTMENTS TO INCOME (= Form 1040 Line 10): $40,482

## Required attachments
- [x] Schedule C (Line 3 = $120,000)
- [x] Schedule SE (Line 15 = $8,478)
- [x] Form 8889 (Line 13 = $4,300)

## Validation summary
- Math: Line 10 = $0+$0+$120,000+$0+$0+$0+$0+$0 = $120,000 ✓
        Line 26 = $0+$0+$4,300+$0+$8,478+$22,304+$5,400+$0+$0+$0+$0+$0+$0 = $40,482 ✓
- Sanity:
  - Line 3 ($120,000) > $400 → Schedule SE attached ✓
  - Line 13 ($4,300): HDHP coverage all year confirmed, contribution within self-only cap ✓
  - Line 16 ($22,304): within SEP-IRA cap of ~$22,304 (computed via 20% worksheet) ✓
  - Line 17 ($5,400): no employer plan eligibility (single, sole proprietor); within Line 3 cap ✓
  - Line 21 ($0): MAGI ~$120,000 above $95,000 single phaseout ceiling → fully phased out ✓
  - Line 1 = $0: standard deduction prior year ✓
- Next steps:
  - Schedule 1 Line 10 ($120,000) → Form 1040 Line 8
  - Schedule 1 Line 26 ($40,482) → Form 1040 Line 10
  - Form 1040 AGI = $120,000 − $40,482 = $79,518
  - Apply standard deduction (2026 single, ~$15,700 estimate)
  - QBI deduction (20% of QBI subject to phaseout — single phaseout begins ~$197,300 for 2025; verify 2026 figure; Priya is well below)

## Sources cited in this draft
- IRS Schedule 1 (Form 1040), 2025 revision
- IRS Form 1040 General Instructions
- IRS Publication 560 (SEP, SIMPLE, qualified plans)
- IRS Publication 969 (HSAs)
- IRC §61, §62, §162(l), §164(f), §221, §223, §408(k)
- Rev. Proc. 2024-25 (HSA limits 2025)
- Rev. Proc. 2024-40 (inflation adjustments 2025)
- Notice 2024-80 (retirement plan limits 2025)
```

## Why each non-obvious choice

**Why is the SEP-IRA contribution ~20% of Schedule C profit, not 25%?** The SEP-IRA cap formula for self-employed is:
- Deduction rate = 25% of "net earnings from self-employment after the §164(f) deduction"
- Net SE earnings = Schedule C profit × 0.9235 − Line 15 (half SE tax)
- The math collapses to 20% of (Schedule C profit − Line 15) because of the circular nature

For Priya: ($120,000 − $8,478) × 0.20 = $22,304. This is an **effective** 18.6% of Schedule C profit but the IRS describes it as "25% of net SE earnings" — same number, different rhetoric.

**Why isn't the student loan interest deductible?** The single-filer MAGI phaseout for student loan interest is $80,000-$95,000 in 2025 (verify 2026). Priya's MAGI is well above $95,000 even after Lines 13, 15, 16, 17. The deduction phases to **zero** for MAGI ≥ $95,000 single. Even though she paid $850 of qualifying interest, none of it is deductible above the line. (And it's not deductible elsewhere either — TCJA suspended miscellaneous itemized deductions.)

**Why both HSA (Line 13) AND SE health insurance (Line 17) for the same person?** They cover different things:
- **Line 17**: deduction for the **premium** (the monthly cost of the HDHP itself)
- **Line 13**: deduction for **HSA contributions** (separate savings account that pairs with the HDHP)

Both are allowed because the IRC sections are independent (§162(l) for premiums, §223 for HSA contributions). HDHP premiums are deductible above the line via §162(l); HSA contributions are deductible above the line via §223.

**Why didn't Priya max the HSA at $5,300 (assuming the 2026 cap rises slightly)?** She contributed $4,300 — matching the 2025 self-only cap. If 2026 self-only HSA cap is higher (announced May 2025), she has room to contribute more by the return due date (April 15, 2027). Could amend after.

**Why no Traditional IRA deduction even though Priya doesn't have a workplace plan?** Active-participant status applies to self-employed retirement plans too. By contributing to a SEP-IRA (a qualified plan she "actively participates" in), Priya becomes an active participant and is subject to the lower phaseout range for IRA deduction:
- Single, active participant: $77,000-$87,000 MAGI (2025)
- Priya's MAGI ~$80,000 — partially phased out
- The math is messy and the cap (max $7,000) is much smaller than the SEP. She elected to focus on the SEP only.

**Why is Line 19a $0 even though Priya's a high earner?** Alimony deduction requires a pre-2019 divorce decree. Priya isn't divorced. Even if she were, post-2018 decrees don't allow this deduction.

## Priya's tax outcome

```
Form 1040 Line 8  (additional income from Sch 1 L10):    $120,000
Form 1040 Line 9  (total income):                        $120,000
Form 1040 Line 10 (adjustments from Sch 1 L26):           $40,482
Form 1040 Line 11 (AGI):                                  $79,518
Form 1040 Line 12 (standard deduction, 2026 est.):        $15,700
Form 1040 Line 13 (QBI deduction, 20% of net QBI estimate):
                  ($120,000 − $8,478 SE half) × 0.20 ≈    $22,304
                  capped at lesser amounts; simplified:    $12,763
Form 1040 Line 15 (taxable income):                       $51,055
Federal income tax (single, ~12-22% brackets):           ~$5,800
Plus SE tax (full):                                       $16,956
Total federal:                                           ~$22,756
```

(QBI calculation simplified — actual computation runs through Form 8995 and accounts for taxable-income limit and W-2/UBIA tests for high earners. For a 2026 figure, Form 8995 is the reference.)

**Without Part II adjustments**, Priya's AGI would be $120,000, taxable income ~$95,000, federal income tax ~$15,500. The $40,482 of Schedule 1 adjustments saved approximately **$8,000-$9,500** of federal income tax (depending on QBI interaction), plus reductions in state tax and improved positioning for credits keyed to AGI.

## Audit-defense notes

- **Line 13 ($4,300)**: 5498-SA from HSA custodian (Fidelity/Lively/HealthEquity) confirms contribution; HDHP coverage verified by 1095-B from insurer
- **Line 16 ($22,304)**: 5498 from SEP-IRA custodian; Pub 560 worksheet retained
- **Line 17 ($5,400)**: 1095-A from marketplace; statement that Priya is sole proprietor with no employer plan eligibility
- **Line 15 ($8,478)**: Schedule SE Line 13 attached; mathematical from Schedule C profit
- **Line 3 ($120,000)**: Schedule C Line 31; 1099-NEC and 1099-K matching to Schedule C Line 1

Clean, defensible, all forms attached.
