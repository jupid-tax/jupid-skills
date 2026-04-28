# Example: W-2 Employee with Side Hustle (Sarah)

A complete walkthrough of Form 1040 for a W-2 day-job employee who also freelances on the side. This is the "tax year 2025" pattern for the rapidly growing side-hustler segment — 36% of US workers had freelance income in 2024.

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
| 3 | Social Security wages | $78,000 |
| 4 | Social Security tax withheld | $4,836 |
| 5 | Medicare wages | $78,000 |
| 6 | Medicare tax withheld | $1,131 |
| 12 | Code D (401(k)) | $6,000 |

(401(k) contributions on Code D already reduce box 1 federal wages — no separate adjustment on 1040.)

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
| Grammarly + Notion + Adobe subscriptions | 27a | $720 |
| Home office (simplified, 80 sq ft × $5) | 30 | $400 |
| Professional development (writing course) | 27a | $300 |
| Business portion of phone (40%) | 27a | $480 |
| Health insurance — covered by W-2 employer | — | not deductible |
| **Total expenses** | | **$1,900** |

Schedule C Line 31 net profit: $25,100 − $1,500 (Lines 8-27a) − $400 (home office) = **$23,200**

### Schedule SE

- Net earnings from SE: $23,200 × 92.35% = $21,425
- SE tax: $21,425 × 15.3% = **$3,278**
- Half SE tax (deductible): **$1,639**

### Above-the-line adjustments (Schedule 1 Part II)

- Half SE tax (L15): $1,639
- No SEP-IRA (Sarah hasn't set one up yet — flagged for 2026)
- No SE health insurance (covered by W-2 employer plan; employer plan disqualifies SE health insurance deduction per IRC §162(l)(2)(B))
- No student loan interest (paid off in prior year)
- **Total Schedule 1 Line 26**: **$1,639**

### QBI computation (Form 8995)

- QBI ≈ Schedule C profit − half SE tax = $23,200 − $1,639 = $21,561
- 20% × QBI = $4,312
- Taxable income before QBI: AGI $93,581 − standard $15,000 = $78,581
- 20% × $78,581 = $15,716
- QBI deduction = lesser = **$4,312**

### Estimated tax payments

Sarah underestimated SE tax exposure. She paid $0 in quarterly estimated taxes during 2025 (relied on W-2 withholding). Line 26 = $0.

### Digital assets

Sarah bought $500 of Bitcoin in 2025 and held. Did NOT sell, exchange, or use. Answer: **No**.

## The completed Form 1040 draft

```markdown
# Form 1040 — DRAFT for tax year 2025

## Header
Filing status: Single
Filer name: Sarah Mitchell     SSN: XXX-XX-XXXX
Address: 5678 Elm Ave, Austin, TX 78701
Digital assets question: No
Someone can claim you as dependent: No
You 65+: No
You blind: No

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
7. Capital gain/loss (Sch D):         $0
8. Schedule 1 additional income:      $23,200
9. TOTAL INCOME:                      $101,620

10. Adjustments (Schedule 1 L26):     $1,639
11. AGI:                              $99,981
12. Standard deduction (single):      $15,000
13. QBI deduction (Form 8995):        $4,312
14. Sum of 12 + 13:                   $19,312
15. TAXABLE INCOME:                   $80,669

## Page 2 — Tax, Credits, Payments
16. Tax (Tax Tables, single):         $12,791
17. Other taxes (Sch 2 L3):           $0
18. Sum:                              $12,791
19. CTC / ODC (Sch 8812):             $0
20. Other credits (Sch 3 L8):         $0
21. Subtract:                         $12,791
22. Other taxes (Sch 2 L21):          $3,278   (SE tax from Schedule SE)
23. TOTAL TAX:                        $16,069

25a. W-2 withholding:                 $11,400
25b. 1099 withholding:                $0
25c. Other withholding:               $0
26. Estimated tax payments:           $0
27. EITC:                             $0
28. Additional CTC (Sch 8812):        $0
29. Refundable AOTC:                  $0
31. Sch 3 L15 refundable:             $0
32. Sum (27 + 28 + 29 + 31):          $0
33. TOTAL PAYMENTS:                   $11,400

34. Overpayment (refund):             $0
35a. Refunded directly:               $0
36. Applied to next year:             $0
37. Amount you owe:                   $4,669
38. Estimated tax penalty:            (leave blank — IRS calculates)

## Required attachments
- [x] Schedule 1 (Schedule C income on L3 = $23,200; adjustments L26 = $1,639)
- [x] Schedule 2 (SE tax on L4 = $3,278)
- [x] Schedule C (sole prop business; via `schedule-c` skill)
- [x] Schedule SE (SE earnings > $400; via `schedule-se` skill)
- [x] Form 8995 (QBI deduction)
- [ ] Schedule 3 — not needed
- [ ] Schedule A — not needed (taking standard)
- [ ] Schedule B — not needed (interest $420 < $1,500)

## Validation summary
- Math: all checks passed
- Sanity warnings:
  - No quarterly estimates paid AND total tax ($16,069) > $5,000 → underpayment penalty very likely (Line 38)
  - Health insurance is via W-2 employer (correctly NOT on Schedule 1 L17)
  - QBI deduction claimed (often missed by side-hustlers)
  - 401(k) contribution of $6,000 is reflected in W-2 box 1 (not a separate adjustment)
- Next steps:
  - Pay $4,669 by April 15, 2026
  - Estimated tax penalty (~$200-300) calculated by IRS via Form 2210
  - Adjust 2026 W-4 to increase withholding OR start quarterly 1040-ES
  - Consider opening a SEP-IRA for 2026: 25% of $23,200 = $5,800 deduction available
  - Set aside ~30% of side hustle income for taxes going forward

## Sources cited in this draft
- IRS Form 1040, Rev. 2025
- IRC §1(c) (single rate schedule)
- IRC §162(l) (SE health insurance — disqualified due to W-2 employer plan)
- IRC §199A (QBI)
- IRC §1402(a) (SE tax)
- Rev. Proc. 2024-40 (2025 figures)
```

## Why each non-obvious choice

**Why no SE health insurance deduction?** IRC §162(l)(2)(B) disqualifies the SE health insurance deduction in any month the filer was eligible for an employer-subsidized health plan (theirs or spouse's). Sarah's W-2 employer offers coverage, so she cannot claim SE health insurance. If her W-2 employer didn't offer coverage and she bought a marketplace plan, she could deduct premiums on Schedule 1 Line 17.

**Why is W-2 box 1 = $78,000 instead of $84,000?** Sarah contributed $6,000 to her 401(k) on Code D. Pre-tax 401(k) contributions reduce box 1 federal wages. Her gross pay was $84,000; box 1 reports the post-401(k) $78,000.

**Why didn't Sarah qualify for Saver's Credit?** AGI threshold for Saver's Credit (single 2025) is $39,500. Sarah's AGI is $99,981 — well over the limit. No credit.

**Why is the underpayment penalty likely?** Safe harbor requires paying during the year either 90% of current-year tax ($16,069 × 90% = $14,462) OR 100% of prior-year tax. W-2 withholding alone covered $11,400, which is below either threshold. Penalty is calculated on Form 2210; expect roughly $200-300 for the shortfall.

**Why answer No to digital assets?** Sarah bought BTC but did not sell, exchange, or use it. Per IRS guidance, only disposals trigger the digital assets Yes — holding is No.

**Why is total income $101,620 ≠ AGI?** The above-the-line adjustments (L10) reduce gross income to AGI: $101,620 − $1,639 = $99,981. This $1,639 is just the half-SE-tax adjustment.

**Why not itemize?** Sarah's potential Schedule A items (Texas: $0 state income tax, $200 charitable, no mortgage) total ~$200 — far below the $15,000 standard deduction.

## What Sarah should change for 2026

1. **Set up a SEP-IRA**: $5,800 deduction available based on 2025 SE earnings
2. **Pay quarterly estimates**: $1,200/quarter for 2026 should cover the SE tax + income tax shortfall
3. **Consider increasing W-4 withholding**: simpler than quarterly estimates if the side hustle income is steady
4. **Track expenses better**: she missed deducting some side hustle costs (better software, better receipt tracking — Jupid does this automatically)
5. **Consider whether to incorporate**: at $25K side hustle revenue, it's not worth S-corp election yet (the FICA savings doesn't cover the S-corp compliance costs). Reassess at $80K+ side hustle revenue.

## Key lessons from Sarah's return

1. **W-2 + 1099 = both withholding AND quarterly estimates needed**: W-2 withholding covered her W-2 tax fine, but did nothing for the $3,278 SE tax + extra income tax on side hustle profit.
2. **Self-employed health insurance is conditional**: not deductible if you have employer coverage available, even if you don't use it.
3. **QBI applies even to side hustles**: $23,200 Schedule C × 20% = $4,312 deduction. Don't skip Form 8995.
4. **401(k) on W-2 is already reflected**: don't double-deduct on Schedule 1.
5. **Texas saves state tax but doesn't change federal**: Sarah pays the same federal tax whether she lives in TX (no state) or CA (high state). State tax is its own thing.
