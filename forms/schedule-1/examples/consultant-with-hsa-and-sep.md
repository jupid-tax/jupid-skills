# Example: Solo Consultant with HSA, SEP-IRA, and SE Health Insurance

A higher-income solo consultant who maxes the available retirement and health-savings stack: HSA on an HDHP, SEP-IRA from net SE earnings, and self-employed health insurance for the HDHP premiums. The most adjustment-heavy "stacked" Schedule 1 a solo filer typically produces. Tax year 2025 (2025 Schedule 1, filed in 2026); math checked in Python.

## The filer

- **Name**: Priya Shah
- **Status**: Single, no dependents
- **Tax year**: 2025 (filing in 2026)
- **Business**: Independent management consulting (sole proprietor)
- **Health coverage**: self-only HDHP bought directly from an insurer (off the Marketplace, no premium tax credit) all year, so HSA-eligible

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
| SE tax — Social Security portion ($110,820 × 0.124, full because below the 2025 wage base of $176,100) | $13,742 |
| SE tax — Medicare portion ($110,820 × 0.029) | $3,214 |
| **SE tax total (Sch SE Line 12)** | **$16,956** |
| **Half of SE tax (Sch SE Line 13)** | **$8,478** |

(2025 Social Security wage base: $176,100 per the 2025 Schedule SE; Priya's earnings are fully below it. The 2026 base is $184,500.)

### HSA contribution (outside payroll)

- HDHP self-only coverage all year
- HSA contribution: $4,300 (the 2025 self-only cap, Rev. Proc. 2024-25; 2026 cap is $4,400 per Rev. Proc. 2025-19)
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

- HDHP premium paid to the insurer: $5,400 for the year (self-only, no family); no Marketplace advance PTC, so the Line 17 worksheet applies
- Eligibility: Priya was not eligible for any employer plan (single, sole proprietor, no spouse) → ✓
- Cap check: $5,400 < $89,218 ($120,000 − Line 15 $8,478 − Line 16 $22,304) → ✓
- Goes on Line 17

### Other items

- Student loan interest paid: $850 (1098-E Box 1). Cap $2,500 ✓. Phaseout: 2025 single $85,000–$100,000. Worksheet MAGI = Form 1040 line 9 ($120,000) − Schedule 1 lines 11–20, 23, 25 ($4,300 + $8,478 + $22,304 + $5,400 = $40,482) = $79,518, below $85,000. No reduction. **Line 21 = $850.**
- Educator: not a teacher. $0.
- Traditional IRA: Priya considered but instead routes retirement savings to the SEP-IRA. $0 on Line 20.
- Alimony: none. Lines 2a / 19a = $0.
- Unemployment, Schedule E, Schedule F, Line 8 sub-lines: all $0.
- State refund: Priya took the standard deduction for 2024. Line 1 = $0.

## The completed Schedule 1 draft

```markdown
# Schedule 1 — DRAFT for tax year 2025

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
21. Student loan interest:                    $850 (worksheet MAGI $79,518 < $85,000)
22. Reserved for future use:                  (blank)
23. Archer MSA deduction:                     $0
24. Other adjustments (24a-24k; 24z blank):   $0
25. Total other adjustments:                  $0
26. ADJUSTMENTS TO INCOME (= Form 1040 Line 10): $41,332

## Required attachments
- [x] Schedule C (Line 3 = $120,000)
- [x] Schedule SE (Line 15 = $8,478)
- [x] Form 8889 (Line 13 = $4,300)

## Validation summary
- Math: Line 10 = $0+$0+$120,000+$0+$0+$0+$0+$0 = $120,000 ✓
        Line 26 = $0+$0+$4,300+$0+$8,478+$22,304+$5,400+$0+$0+$0+$850+$0+$0 = $41,332 ✓
- Sanity:
  - Net SE earnings ($110,820) ≥ $400 → Schedule SE attached ✓
  - Line 13 ($4,300): HDHP coverage all year confirmed, contribution within self-only cap ✓
  - Line 16 ($22,304): within SEP-IRA cap of ~$22,304 (computed via 20% worksheet) ✓
  - Line 17 ($5,400): no employer plan eligibility (single, sole proprietor); within the $89,218 cap (Line 3 − Lines 15 and 16) ✓
  - Line 21 ($850): worksheet MAGI $79,518 below the $85,000 single phaseout start → no reduction ✓
  - Line 1 = $0: standard deduction prior year ✓
- Next steps:
  - Schedule 1 Line 10 ($120,000) → Form 1040 Line 8
  - Schedule 1 Line 26 ($41,332) → Form 1040 Line 10
  - Form 1040 line 11a AGI = $120,000 − $41,332 = $78,668
  - Apply standard deduction (2025 single, $15,750, line 12e)
  - QBI deduction (Form 8995; 2025 threshold $197,300 single per Rev. Proc. 2024-40, $201,750 for 2026; Priya is well below)

## Sources cited in this draft
- IRS Schedule 1 (Form 1040), 2025 revision, filed in 2026
- IRS Form 1040 General Instructions (2025)
- IRS Publication 560 (SEP, SIMPLE, qualified plans), 2025
- IRS Publication 969 (HSAs)
- IRC §61, §62, §162(l), §164(f), §221, §223, §408(k)
- Rev. Proc. 2024-25 (HSA limits 2025)
- Rev. Proc. 2024-40 (inflation adjustments 2025)
- Notice 2024-80 (retirement plan limits 2025)
```

## Why each non-obvious choice

**Why is the SEP-IRA contribution ~20% of Schedule C profit, not 25%?** The SEP-IRA cap formula for self-employed is:
- Plan contribution rate = 25% of compensation, where the owner's compensation is net earnings after the §164(f) deduction and after the contribution itself
- Pub 560 Deduction Worksheet for Self-Employed: start from Schedule C net profit − Line 15 (half SE tax); no 0.9235 factor here
- The 25% plan rate converts to a 20% self-employed rate (0.25 ÷ 1.25) because the contribution reduces compensation

For Priya: ($120,000 − $8,478) × 0.20 = $22,304. This is an **effective** 18.6% of Schedule C profit but the IRS describes it as "25% of net SE earnings" — same number, different rhetoric.

**Why is the student loan interest fully deductible for a $120,000 earner?** The phaseout uses worksheet MAGI, which already subtracts Lines 13, 15, 16, and 17. Priya's is $79,518, below the 2025 single phaseout start of $85,000 (Rev. Proc. 2024-40; $85,000 again for 2026 per Rev. Proc. 2025-32). The stacked adjustments are what keep Line 21 alive.

**Why both HSA (Line 13) AND SE health insurance (Line 17) for the same person?** They cover different things:
- **Line 17**: deduction for the **premium** (the monthly cost of the HDHP itself)
- **Line 13**: deduction for **HSA contributions** (separate savings account that pairs with the HDHP)

Both are allowed because the IRC sections are independent (§162(l) for premiums, §223 for HSA contributions). HDHP premiums are deductible above the line via §162(l); HSA contributions are deductible above the line via §223.

**Why $4,300 for the HSA?** That is the 2025 self-only cap (Rev. Proc. 2024-25); she is under 55, so no catch-up. Contributions for 2025 can be made until April 15, 2026. For 2026 the self-only cap is $4,400 (Rev. Proc. 2025-19).

**Why no Traditional IRA deduction even though Priya doesn't have a workplace plan?** Active-participant status applies to self-employed retirement plans too. By contributing to a SEP-IRA (a qualified plan she "actively participates" in), Priya becomes an active participant and is subject to the lower phaseout range for IRA deduction:
- Single, active participant: $79,000-$89,000 MAGI (2025, Notice 2024-80)
- Priya's IRA worksheet MAGI is $79,518 (line 9 minus Schedule 1 lines 11–19a, 23, 25) — partially phased out
- The math is messy and the cap (max $7,000) is much smaller than the SEP. She elected to focus on the SEP only.

**Why is Line 19a $0 even though Priya's a high earner?** Alimony deduction requires a pre-2019 divorce decree. Priya isn't divorced. Even if she were, post-2018 decrees don't allow this deduction.

## Priya's tax outcome

```
Form 1040 Line 8   (additional income from Sch 1 L10):   $120,000
Form 1040 Line 9   (total income):                       $120,000
Form 1040 Line 10  (adjustments from Sch 1 L26):          $41,332
Form 1040 Line 11a (AGI):                                 $78,668
Form 1040 Line 12e (standard deduction, 2025 single):     $15,750
Form 1040 Line 13a (QBI deduction, Form 8995):            $12,584
  QBI = $120,000 − $8,478 − $22,304 − $5,400 = $83,818
  lesser of 20% × $83,818 = $16,764 and
  20% × ($78,668 − $15,750) = $12,584
Form 1040 Line 15  (taxable income):                      $50,334
Federal income tax (2025 single, 10%/12%/22% brackets):   ~$5,987
Plus SE tax (full):                                       $16,956
Total federal:                                           ~$22,943
```

(QBI here runs through Form 8995 because taxable income before QBI is under the $197,300 threshold; above it, Form 8995-A and the W-2/UBIA tests apply.)

**Without Part II adjustments** (same QBI), Priya's AGI would be $120,000, the QBI deduction $16,764, taxable income $87,486, and federal income tax about $14,161. The $41,332 of Schedule 1 adjustments saved approximately **$8,170** of federal income tax, plus reductions in state tax and improved positioning for credits keyed to AGI.

## Audit-defense notes

- **Line 13 ($4,300)**: 5498-SA from HSA custodian (Fidelity/Lively/HealthEquity) confirms contribution; HDHP coverage verified by 1095-B from insurer
- **Line 16 ($22,304)**: 5498 from SEP-IRA custodian; Pub 560 worksheet retained
- **Line 17 ($5,400)**: insurer premium statements; statement that Priya is sole proprietor with no employer plan eligibility
- **Line 21 ($850)**: Form 1098-E from the servicer; worksheet showing MAGI $79,518
- **Line 15 ($8,478)**: Schedule SE Line 13 attached; mathematical from Schedule C profit
- **Line 3 ($120,000)**: Schedule C Line 31; 1099-NEC and 1099-K matching to Schedule C Line 1

Clean, defensible, all forms attached.
