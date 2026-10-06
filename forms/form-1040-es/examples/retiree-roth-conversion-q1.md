# Example: Retiree with Roth Conversion + Capital Gain — Single Q1 Payment

A retiree planning a tax-efficient income year: large Roth IRA conversion in March plus a long-term capital gain from a brokerage sale in February. Income is heavily front-loaded. Single estimated tax payment in Q1 covers the year.

## The filer

- **Name**: Eleanor Park
- **Status**: Retired, age 68
- **Filing status**: Single (widowed; not eligible for QW after the second year)
- **State**: Florida (no state income tax)
- **Tax year being projected**: 2026
- **Prior tax year (2025)**: AGI $58,000, total tax $4,800

## The income picture

| Source | Timing | Amount |
|--------|--------|--------|
| Social Security | monthly | $36,000/yr |
| Required Minimum Distribution from traditional IRA | December | $24,000 |
| Roth conversion ($150,000 from IRA) | March 14, 2026 | $150,000 (taxable) |
| Long-term capital gain (sold appreciated mutual fund) | February 20, 2026 | $40,000 LTCG |
| Brokerage interest + dividends | year-round | $6,500 |

Total expected gross income: $256,500
- 85% of SS = $30,600 (taxable portion at this income level)
- IRA RMD = $24,000
- Roth conversion = $150,000
- LTCG = $40,000
- Interest + ordinary dividends = $6,500

Eleanor will elect 20% federal withholding on the IRA RMD via Form W-4R (the default for a nonperiodic IRA distribution is 10%), and 12% voluntary withholding on Social Security via Form W-4V — but for the conversion and the capital gain there's no withholding unless she elects it.

## Withholding planning

| Source | Withholding rate | Amount |
|--------|------------------|--------|
| Social Security (W-4V flat 12%) | 12% × $36,000 | $4,320 |
| IRA RMD ($24,000 × 20% elected on Form W-4R) | 20% | $4,800 |
| Brokerage (no withholding) | — | $0 |
| Roth conversion (no withholding by default) | — | $0 |
| Capital gain (no withholding) | — | $0 |
| **Total withholding** | | **$9,120** |

## Current-year tax projection

| Worksheet line | Amount |
|----------------|--------|
| Wages | $0 |
| Taxable SS (85%) | $30,600 |
| IRA distributions (RMD + Roth conversion) | $174,000 |
| LTCG + ordinary dividends | $46,500 (of which $40,000 LTCG, $6,500 interest+dividends) |
| **Line 1 (AGI)** | **$251,100** |
| Line 2a (standard deduction, single 65+) | $18,150 ($16,100 + $2,050; 2026 Form 1040-ES) |
| Line 2b (QBI) | $0 (no pass-through business) |
| Line 2c (Schedule 1-A) | $0 (the $6,000 senior deduction phases out by 6% of MAGI over $75,000, so it is fully phased out at her MAGI) |
| **Line 3 (taxable income)** | **$232,950** |
| Line 4 (tax on ordinary $192,950 + LTCG on $40,000) | computed below |
| Line 5 (AMT) | $0 |
| Line 6 | (= Line 4) |
| Line 7 (credits) | $0 |
| Line 8 | (= Line 4) |
| Line 9 (SE tax) | $0 (no self-employment) |
| Line 10 (NIIT 3.8%) | computed below |
| **Line 11a (total tax)** | sum below |
| Line 11b | $0 |
| **Line 11c** | (= Line 11a) |

### Detailed Line 4 — Qualified Dividends and Capital Gain Tax Worksheet

Ordinary taxable income (excluding LTCG): $232,950 − $40,000 = $192,950
LTCG portion: $40,000

Ordinary income tax (2026 Tax Rate Schedule X, 2026 Form 1040-ES):
- $17,966 on the first $105,700
- 24% on $105,700 to $192,950 = $20,940
- **Subtotal: $38,906**

LTCG rate: her ordinary income already exceeds the 2026 single 0% limit ($49,450), and total taxable income is under the 15% limit ($545,500; Rev. Proc. 2025-32 §4.03) → $40,000 × 15% = $6,000.

**Line 4 total = $38,906 + $6,000 = $44,906**

### Line 10 — NIIT

Net investment income = $40,000 LTCG + $6,500 interest+dividends = $46,500
AGI excess over $200,000 threshold = $251,100 − $200,000 = $51,100
NIIT base = min($46,500, $51,100) = $46,500
**NIIT = 3.8% × $46,500 = $1,767**

### Line 11a — Total tax

$44,906 + $0 + $1,767 = **$46,673**

## Apply safe harbor

Prior-year AGI $58,000 < $150,000, so 100% rule (not 110%).

```
Line 12a = 0.90 × $46,673 = $42,006
Line 12b = $4,800 × 1.00 = $4,800
Line 12c = min($42,006, $4,800) = $4,800
```

**Required annual payment: $4,800 (Safe Harbor B controls overwhelmingly)**

This is the power of the prior-year safe harbor: even though Eleanor's current-year tax will be ~$47K, she only needs to pre-pay $4,800 to avoid the §6654 penalty. The big balance ($37,553 after her $9,120 of withholding) is settled at filing in April 2027 with **no penalty**, just interest if paid late.

## Withholding vs. required

Withholding ($9,120) > required ($4,800). Eleanor is **already safe-harbored** by withholding alone. No estimated payments are required to avoid §6654 penalty.

## But Eleanor wants to budget

Eleanor doesn't want a $42K bill in April 2027. She prefers to pre-pay enough to roughly match her actual liability. The skill flags this as a **planning preference**, distinct from the §6654 safe-harbor minimum.

Eleanor decides to make a single Q1 estimated payment that brings her total prepaid (withholding + estimate) to approximately current-year tax:

Target total prepaid: $46,673 (full current-year tax)
Withholding: $9,120
Single Q1 payment: $46,673 − $9,120 = **$37,553**

Why Q1? Because the bulk of her income (Roth conversion in March, LTCG in February) hits in Q1 — paying then matches the liability to the period when income is realized. Paying in Q4 instead would also satisfy §6654 (since she's already safe-harbored by withholding), but Eleanor prefers cash-flow alignment.

Alternatively, she could spread $37,553 / 4 ≈ $9,388 per quarter for budgeting smoothness — also fine.

---

## The deliverable

```markdown
# Form 1040-ES — Estimated Tax Plan for tax year 2026

## Filer
- Name: Eleanor Park
- SSN: ***-**-**** (placeholder)
- Filing status: Single (age 68)
- State (for voucher mailing): FL (federal only — no state income tax)

## Prior-year baseline (tax year 2025)
- Prior-year AGI: $58,000
- Prior-year total tax (Line 24): $4,800
- 110% safe harbor applies: No (AGI $58,000 < $150,000)
- Prior-year safe harbor amount: $4,800 × 1.00 = $4,800

## Current-year projection (tax year 2026)
| Worksheet line | Amount |
|----------------|--------|
| 1.  Estimated AGI | $251,100 |
| 2a. Standard deduction (single, 65+) | $18,150 |
| 2b. QBI deduction | $0 |
| 2c. Schedule 1-A deductions | $0 |
| 2d. Total deductions | $18,150 |
| 3.  Taxable income | $232,950 |
| 4.  Tax (ordinary $38,906 + LTCG $6,000) | $44,906 |
| 5.  AMT | $0 |
| 6.  Subtotal | $44,906 |
| 7.  Credits | $0 |
| 8.  Subtotal | $44,906 |
| 9.  Self-employment tax | $0 |
| 10. NIIT (3.8% × $46,500) | $1,767 |
| 11a. Total tax | $46,673 |
| 11b. Refundable credits | $0 |
| 11c. Net total tax | $46,673 |
| 12a. 90% × Line 11c | $42,006 |
| 12b. Prior-year × 100% | $4,800 |
| 12c. Required annual payment (smaller) | $4,800 |
| 13. Expected withholding (SS + IRA) | $9,120 |
| 14a. Line 12c − Line 13 (§6654 minimum) | ≤ $0 (withholding $9,120 > required $4,800) — stop |
| Planning surplus to budget for actual liability | $37,553 |

## Installment schedule (planning, not §6654-required)
| Voucher | Due date | Amount | Channel | Reason |
|---------|----------|--------|---------|--------|
| Q1 | 2026-04-15 | $37,553 | Direct Pay | Match cash to Roth conversion + LTCG realized in Q1 |
| Q2 | 2026-06-15 | $0 | — | Already covered |
| Q3 | 2026-09-15 | $0 | — | Already covered |
| Q4 | 2027-01-15 | $0 | — | Already covered |
| **Total** | | **$37,553** | | |

## Method
- [x] Single-payment Q1 (planning preference; not §6654-required)
- [ ] Equal installments
- [ ] Annualized income (could use Schedule AI to show Q1-heavy income; not necessary since safe-harbored already)
- [ ] Single-payment farmer/fisher exception

## §6654 status
- §6654 minimum already satisfied by withholding alone ($9,120 > $4,800).
- The Q1 estimated payment is voluntary — for cash-flow planning, not penalty avoidance.
- If Eleanor skipped the Q1 payment entirely, NO penalty would apply. She'd just owe ~$37.6K at filing in April 2027, with interest only if she pays after April 15, 2027.

## Validation summary
- Math: all checks passed
- Sanity:
  - LTCG taxed at 15% (2026 thresholds, Rev. Proc. 2025-32 §4.03)
  - NIIT applies (AGI > $200K threshold; investment income $46,500)
  - Roth conversion timing: March 14 → income recognized in Q1 → annualization would also support heavy Q1 payment
  - Standard deduction includes the 65+ additional amount ($2,050 single for 2026)
  - Senior deduction (Schedule 1-A) fully phased out at MAGI $251,100
- Year-aware notes:
  - 2026 Tax Rate Schedules, standard deduction, and capital gain thresholds — 2026 Form 1040-ES / Rev. Proc. 2025-32
  - 2026 NIIT threshold $200K — NOT inflation-adjusted (static since 2013)

## Sources cited in this draft
- IRS Form 1040-ES, Rev. 2026
- IRC §6654 (estimated tax)
- IRC §6654(d)(1)(B) (lesser of 90% current / 100% prior)
- IRC §1411 (NIIT 3.8%)
- IRC §1(h) (preferential LTCG rates)
- IRC §408A(d)(3) (Roth conversion as taxable event)
- IRC §86 (taxability of Social Security benefits)
- Rev. Proc. 2025-32 (2026 figures)
- IRS Pub. 505
- IRS Pub. 575 (Pension and Annuity Income)
- IRS Pub. 590-A / 590-B (IRA contributions / distributions)
```

---

## Why each non-obvious choice

**Why is the §6654 minimum so low ($4,800) compared to actual tax ($46,673)?**
Because Safe Harbor B uses **prior-year tax** ($4,800), and the prior year was a normal income year. Eleanor's 2026 surge (Roth conversion + LTCG) doesn't change Safe Harbor B. She can satisfy §6654 with just $4,800 of prepaid tax (which her withholding already exceeds).

**Why doesn't she just pay $4,800 and pocket the rest until April 2027?**
She could. §6654 wouldn't penalize. But the IRS charges **interest** (not a §6654 penalty, but standard underpayment interest under §6601) on the unpaid balance from April 15, 2027 until paid. Eleanor prefers to prepay to avoid that interest cost — operationally cleaner.

**Why a single Q1 payment instead of four equal installments?**
Two reasons:
1. Cash-flow alignment: most of her 2026 income lands in Q1 (Roth conversion + LTCG), so paying then matches.
2. The annualized income method (Form 2210 Schedule AI) would also confirm Q1 is the right quarter for a large payment if §6654 were in play. Since it isn't, the timing is purely her preference.

**Why is the Roth conversion fully taxable?**
IRC §408A(d)(3) — converting from a traditional (pre-tax) IRA to a Roth (post-tax) IRA recognizes the full pre-tax balance as ordinary income in the year converted. Eleanor's $150K conversion adds $150K to ordinary income on Line 1.

**Why isn't the LTCG taxed at 0%?**
The 0% LTCG rate (2026 single) applies only up to $49,450 of taxable income. Eleanor's ordinary taxable income alone is $192,950, well above. So her LTCG falls into the 15% bracket. (Above $545,500 of taxable income — 2026 single — the 20% rate would apply; she's not there.)

**Why the QDCGT Worksheet instead of normal tax table?**
LTCG and qualified dividends get preferential rates. The QDCGT Worksheet (in the 1040 instructions) splits ordinary income from preferential income, applies brackets to ordinary, applies LTCG rates to preferential, and combines. Without the worksheet, the agent would over-tax the LTCG.

**What if Eleanor doesn't make the Q1 payment and the conversion turns out to be a bad idea?**
A Roth conversion can't be undone: the TCJA repealed recharacterization of conversions for tax years beginning after 2017 (IRC §408A(d)(6)(B)(iii)). The conversion is permanent. If Eleanor's circumstances change (e.g., big medical expense), she's stuck with the $150K of ordinary income for 2026.

This is why the agent flags the "verify before doing the conversion" step in the planning conversation.
