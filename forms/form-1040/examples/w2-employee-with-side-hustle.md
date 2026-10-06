# Example: W-2 Employee with Side Hustle (Sarah)

A complete walkthrough of the 2025 Form 1040 (filed in 2026) for a W-2 day-job employee who also freelances on the side. Line numbers follow the 2025 form; amounts use the 2025 instructions (Tax Table, standard deduction $15,750 single). Math checked in python.

## The filer

- **Name**: Sarah Mitchell
- **Status**: Single, age 28, no dependents
- **Day job**: Marketing manager at a SaaS company, full-time W-2
- **Side hustle**: Freelance copywriting (evenings/weekends)
- **Tax year**: 2025 (filing in 2026)
- **State**: Texas (no state income tax — federal-only example)

## Inputs gathered

### W-2 from day job (Acme SaaS Inc.)

| Box | Item | Amount |
|-----|------|--------|
| 1 | Federal wages | $78,000 |
| 2 | Federal income tax withheld | $11,400 |
| 3 | Social Security wages | $84,000 |
| 4 | Social Security tax withheld | $5,208 |
| 5 | Medicare wages | $84,000 |
| 6 | Medicare tax withheld | $1,218 |
| 12 | Code D (401(k)) | $6,000 |

(401(k) contributions on Code D already reduce box 1 federal wages — no separate adjustment on 1040. They are still subject to social security and Medicare tax, so boxes 3 and 5 show the full $84,000.)

### Prior-year return (needed for the Line 38 test)

- 2024 Form 1040: W-2 only, AGI $78,000, total tax (2024 line 24) $9,007

### 1099-NEC from freelance clients (Schedule C)

| Source | Amount |
|--------|--------|
| Client A (SaaS marketing copy) | $14,500 |
| Client B (e-commerce product descriptions) | $5,200 |
| Client C (newsletter ghostwriting) | $4,800 |
| Cash from one local client | $600 |
| **Schedule C Line 1 gross receipts** | **$25,100** |

### 1099-INT (personal savings)

- $420 from high-yield savings account at Marcus

### Schedule C expenses

| Category | Line | Amount |
|----------|------|--------|
| Grammarly + Notion + Adobe subscriptions | Part V → 48 → 27b | $720 |
| Home office (simplified, 80 sq ft × $5) | 30 | $400 |
| Professional development (writing course) | Part V → 48 → 27b | $300 |
| Business portion of phone (40%) | Part V → 48 → 27b | $480 |
| Health insurance — covered by W-2 employer | — | not deductible |
| **Total expenses** | | **$1,900** |

(On the 2025 Schedule C, line 27a is the energy efficient commercial buildings deduction and line 27b is other expenses from Part V line 48.)

Schedule C Line 31 net profit: $25,100 − $1,500 (Line 28) − $400 (Line 30 home office) = **$23,200**

### Schedule SE

- Net earnings from SE (line 4a): $23,200 × 92.35% = $21,425
- SE tax (line 12): $21,425 × 12.4% = $2,657 + $21,425 × 2.9% = $621 = **$3,278** (line 8a: W-2 box 3 $84,000 is under the $176,100 wage base, so the full 12.4% applies)
- Half SE tax (line 13, deductible): **$1,639**

### Above-the-line adjustments (Schedule 1 Part II)

- Half SE tax (L15): $1,639
- No SEP-IRA contribution entered. A SEP for 2025 can still be set up and funded by the return due date, including extensions (Pub. 560); maximum 20% × ($23,200 − $1,639) = $4,312. Ask before finalizing.
- No SE health insurance (covered by W-2 employer plan; employer plan disqualifies SE health insurance deduction per IRC §162(l)(2)(B))
- No student loan interest (paid off in prior year)
- **Total Schedule 1 Line 26**: **$1,639**

### QBI computation (Form 8995)

- QBI ≈ Schedule C profit − half SE tax = $23,200 − $1,639 = $21,561
- 20% × QBI = $4,312
- Taxable income before QBI: AGI $99,981 − standard $15,750 = $84,231
- 20% × $84,231 = $16,846
- QBI deduction = lesser = **$4,312** (taxable income before QBI is under the $197,300 single threshold, so Form 8995)

### Estimated tax payments

Sarah underestimated SE tax exposure. She paid $0 in quarterly estimated taxes during 2025 (relied on W-2 withholding). Line 26 = $0.

### Digital assets

Sarah bought $500 of Bitcoin with U.S. dollars in 2025 and held it. She did not receive any digital asset as a reward, award, or payment, and did not sell, exchange, or otherwise dispose of any. Answer: **No** (purchase with real currency and holding are listed as "No" situations in the 2025 instructions).

## The completed Form 1040 draft

```markdown
# Form 1040 — DRAFT for tax year 2025

## Header
Filing status: Single
Filer name: Sarah Mitchell     SSN: XXX-XX-XXXX
Address: 5678 Elm Ave, Austin, TX 78701
Main home in the U.S. more than half of 2025: [x]
Digital assets question: No

Dependents: None

## Page 1 — Income
1a. Total W-2 wages:                  $78,000
1b. Household employee wages:         $0
1c. Tip income:                       $0
1d. Medicaid waiver payments:         $0
1e. Taxable dependent care benefits:  $0
1f. Adoption benefits:                $0
1g. Form 8919 wages:                  $0
1h. Other earned income:              $0
1i. Nontaxable combat pay election:   $0
1z. Sum of 1a-1h:                     $78,000

2a. Tax-exempt interest:              $0
2b. Taxable interest:                 $420
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
8. Schedule 1 additional income:      $23,200
9. TOTAL INCOME:                      $101,620

10. Adjustments (Schedule 1 L26):     $1,639
11a. AGI:                             $99,981

## Page 2 — Tax, Credits, Payments
11b. AGI (from 11a):                  $99,981
12a. Someone can claim you:           [ ]   12b. Spouse itemizes: [ ]   12c. Dual-status: [ ]
12d. Born before Jan 2, 1961 / blind: [ ] [ ]
12e. Standard deduction (single):     $15,750
13a. QBI deduction (Form 8995):       $4,312
13b. Schedule 1-A deductions:         $0     (no qualified tips, overtime, new-car loan interest; under 65)
14. Sum of 12e + 13a + 13b:           $20,062
15. TAXABLE INCOME:                   $79,919
16. Tax (Tax Table, single, row $79,900–79,950): $12,498
17. Schedule 2 L3:                    $0
18. Sum:                              $12,498
19. CTC / ODC (Sch 8812):             $0
20. Other credits (Sch 3 L8):         $0
21. Sum of 19 + 20:                   $0
22. Line 18 − line 21:                $12,498
23. Other taxes (Sch 2 L21):          $3,278   (SE tax from Schedule SE)
24. TOTAL TAX:                        $15,776

25a. W-2 withholding:                 $11,400
25b. 1099 withholding:                $0
25c. Other withholding:               $0
25d. Total withholding:               $11,400
26. Estimated tax payments:           $0
27a. EIC:                             $0
28. Additional CTC (Sch 8812):        $0
29. American opportunity credit:      $0
30. Refundable adoption credit:       $0
31. Sch 3 L15 refundable:             $0
32. Sum (27a + 28 + 29 + 30 + 31):    $0
33. TOTAL PAYMENTS:                   $11,400

34. Overpayment (refund):             $0
35a. Refunded directly:               $0
36. Applied to next year:             $0
37. Amount you owe:                   $4,376
38. Estimated tax penalty:            $0 (exception: line 25d $11,400 ≥ 100% of 2024 tax $9,007; 2024 AGI under $150,000)

## Required attachments
- [x] Schedule 1 (Schedule C income on L3 = $23,200; adjustments L26 = $1,639)
- [x] Schedule 2 (SE tax on L4 = $3,278; L21 = $3,278)
- [x] Schedule C (sole prop business; via `schedule-c` skill)
- [x] Schedule SE (net SE earnings $400 or more; via `schedule-se` skill)
- [x] Form 8995 (QBI deduction)
- [ ] Schedule 3 — not needed
- [ ] Schedule A — not needed (taking standard)
- [ ] Schedule B — not needed (taxable interest $420, not over $1,500; no dividends; no foreign accounts)
- [ ] Schedule 1-A — not needed (no qualifying items)

## Validation summary
- Math: all checks passed
- Sanity warnings:
  - Line 37 ($4,376) is at least $1,000 and more than 10% of the tax, but no Line 38 penalty: withholding covered 100% of her 2024 tax (i1040gi 2025, Line 38 exception). The exception won't help next year unless 2026 payments reach 100% of the 2025 tax ($15,776)
  - Health insurance is via W-2 employer (correctly NOT on Schedule 1 L17)
  - QBI deduction claimed (often missed by side-hustlers)
  - 401(k) contribution of $6,000 is reflected in W-2 box 1 (not a separate adjustment)
- Next steps:
  - Pay $4,376 by April 15, 2026
  - Adjust 2026 W-4 to increase withholding OR start quarterly 1040-ES (ask which)
  - Ask whether she wants a 2025 SEP contribution (deadline: return due date including extensions; max $4,312)

## Sources cited in this draft
- IRS Form 1040 (2025) and 2025 Instructions for Form 1040 (Tax Table; Line 38 exception)
- IRC §1(j) (rate tables)
- IRC §63 as amended by P.L. 119-21 (2025 standard deduction $15,750)
- IRC §162(l) (SE health insurance — disqualified due to W-2 employer plan)
- IRC §199A (QBI)
- IRC §§1401–1402 (SE tax); 2025 Schedule SE
- Pub. 560 (SEP deadline and self-employed rate)
- Rev. Proc. 2024-40 (2025 brackets)
```

## Why each non-obvious choice

**Why no SE health insurance deduction?** IRC §162(l)(2)(B) disqualifies the SE health insurance deduction in any month the filer was eligible for an employer-subsidized health plan (theirs or spouse's). Sarah's W-2 employer offers coverage, so she cannot claim SE health insurance. If her W-2 employer didn't offer coverage and she bought a marketplace plan, she could deduct premiums on Schedule 1 Line 17.

**Why is W-2 box 1 = $78,000 instead of $84,000?** Sarah contributed $6,000 to her 401(k) on Code D. Pre-tax 401(k) contributions reduce box 1 federal wages. Her gross pay was $84,000; box 1 reports the post-401(k) $78,000.

**Why didn't Sarah qualify for Saver's Credit?** AGI limit for Saver's Credit (single 2025) is $39,500 (2025 Form 8880 line 9). Sarah's AGI is $99,981 — well over the limit. No credit.

**Why no underpayment penalty?** Line 37 ($4,376) is at least $1,000 and more than 10% of the tax shown, and withholding ($11,400) is below 90% of the 2025 tax ($14,198). But the 2025 instructions' exception applies: her 2024 return covered 12 months, and lines 25d + 26 ($11,400) are at least 100% of the tax on her 2024 return ($9,007), with 2024 AGI not over $150,000. Withholding is treated as paid evenly through the year, so it meets every installment. Line 38 stays $0.

**Why answer No to digital assets?** Sarah bought BTC with dollars and held it. The 2025 question asks whether she received a digital asset as a reward, award, or payment, or sold, exchanged, or otherwise disposed of one. Buying with real currency and holding are "No" situations.

**Why is total income $101,620 ≠ AGI?** The above-the-line adjustments (L10) reduce gross income to AGI: $101,620 − $1,639 = $99,981. This $1,639 is just the half-SE-tax adjustment.

**Why not itemize?** Sarah's potential Schedule A items (Texas: $0 state income tax, $200 charitable, no mortgage) total ~$200 — far below the $15,750 standard deduction.

## What Sarah should change for 2026

1. **Retirement contribution**: a SEP for 2026 is limited to 20% of 2026 net earnings after half of SE tax (Pub. 560); the 2025 SEP is still possible until the 2025 return due date, including extensions
2. **Pay quarterly estimates**: if withholding stays at $11,400, $1,094 per quarter ($4,376 ÷ 4) reaches 100% of the 2025 tax ($15,776); the 100% (not 110%) figure applies because her 2025 AGI, $99,981, is not over $150,000
3. **Or increase W-4 withholding**: withholding counts as paid evenly through the year (see the `form-w4` skill)
4. **Keep records**: receipts and a mileage/phone-use log for every side-hustle expense she deducts
5. **Entity choice** (S corporation or not) is outside this skill; refer to a CPA

## Key lessons from Sarah's return

1. **W-2 + 1099 = plan for the side income**: W-2 withholding covered her W-2 tax, but not the $3,278 SE tax + extra income tax on side hustle profit. This year the prior-year exception saved her from the penalty; next year it may not.
2. **Self-employed health insurance is conditional**: not deductible if you have employer coverage available, even if you don't use it.
3. **QBI applies even to side hustles**: ($23,200 − $1,639 half SE tax) × 20% = $4,312 deduction on Line 13a. Don't skip Form 8995.
4. **401(k) on W-2 is already reflected**: don't double-deduct on Schedule 1.
5. **Texas saves state tax but doesn't change federal**: Sarah pays the same federal tax whether she lives in TX (no state) or CA (high state). State tax is its own thing.
