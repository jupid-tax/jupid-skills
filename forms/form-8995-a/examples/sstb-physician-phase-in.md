# Example — Single Physician (SSTB, Phase-In Zone)

End-to-end Form 8995-A walkthrough for a sole-proprietor physician whose taxable income places her in the SSTB phase-in zone.

---

## Persona

**Dr. Patel.** Age 38. Single. Family-medicine physician operating as a sole proprietor (no LLC; just Schedule C). Practice located in a leased office; she employs one nurse and one receptionist as W-2 employees.

## 2025 Inputs

| Item | Amount |
|------|--------|
| Schedule C net profit | $300,000 |
| Self-employment tax (Schedule SE) | $22,632 |
| Deductible ½ SE tax | $11,316 |
| Self-employed health insurance | $9,000 |
| SEP-IRA contribution | $25,000 |
| W-2 wages paid (nurse + receptionist) | $80,000 |
| UBIA of qualified property | $50,000 (medical equipment, computers, exam-room furniture, all in service ≤ 7 years; within depreciable period) |
| Brokerage interest income | $36,000 |
| Standard deduction (single) | $15,000 |
| No other income, no other adjustments |

## Form 1040 build-up to taxable income before QBI

| Line | Item | Amount |
|------|------|--------|
| 1z | Wages | $0 |
| 2b | Taxable interest | $36,000 |
| 8 | Schedule C profit (via Schedule 1) | $300,000 |
| **9** | **Total income** | **$336,000** |
| 10 | Adjustments (½ SE tax + SE HI + SEP-IRA) | $45,316 |
| **11** | **AGI** | **$290,684** |
| 12 | Standard deduction (single, 2025) | $15,000 |
| | **Taxable income before QBI** | **$275,684** |

We'll round to **$275,000** for the worked numbers.

---

## SSTB Classification

Family medicine = Health = SSTB per IRC §199A(d)(2)(A)(i) and Treas. Reg. §1.199A-5(b)(2)(ii).

## Threshold check

- Threshold for single (2025): $241,950
- Phase-in top: $291,950
- Dr. Patel at $275,000 → **in the phase-in zone**
- Form 8995-A REQUIRED; Schedule A REQUIRED

---

## QBI computation

Schedule C profit: $300,000

QBI adjustments (allocable to the medical practice):
- Less ½ SE tax: ($11,316)
- Less SE health insurance: ($9,000)
- Less SEP-IRA contribution: ($25,000)

**QBI = $254,684**

---

## Form 8995-A Schedule A (SSTB phase-in)

| Line | Item | Value |
|------|------|-------|
| 1 | Trade name | Patel Family Medicine |
| 2 | Taxable income before QBI | $275,000 |
| 3 | Threshold (single, 2025) | $241,950 |
| 4 | Excess (L2 − L3) | $33,050 |
| 5 | Phase-in range | $50,000 |
| 6 | Phase-in % (L4/L5) | 0.6610 |
| 7 | Applicable % (1 − L6) | 0.3390 |
| 8 | Reduced QBI ($254,684 × 0.3390) | $86,338 |
| 9 | Reduced W-2 wages ($80,000 × 0.3390) | $27,120 |
| 10 | Reduced UBIA ($50,000 × 0.3390) | $16,950 |
| 11 | W-2/UBIA limit on reduced amounts | max(50% × 27,120, 25% × 27,120 + 2.5% × 16,950) = max(13,560, 7,204) = $13,560 |
| 12 | Tentative deduction on reduced amounts | min(20% × 86,338, 13,560) = min(17,268, 13,560) = $13,560 |

We need the original Part II Line 11 (without phase-in) to compute the reduction.

---

## Form 8995-A Part II (without Schedule A applied)

| Line | Item | Value |
|------|------|-------|
| 2 | QBI | $254,684 |
| 3 | 20% × L2 | $50,937 |
| 4 | W-2 wages | $80,000 |
| 5 | 50% × L4 | $40,000 |
| 6 | 25% × L4 | $20,000 |
| 7 | UBIA | $50,000 |
| 8 | 2.5% × L7 | $1,250 |
| 9 | L6 + L8 | $21,250 |
| 10 | Greater of L5 or L9 | $40,000 |
| 11 | Smaller of L3 or L10 | **$40,000** |

So the W-2 wage limit binds at $40,000 even before the SSTB phase-in (50% × $80,000 = $40,000 < 20% × $254,684 = $50,937).

## Schedule A Line 13 — phase-in reduction

L13 = L11 (Part II) − L12 (Schedule A) = $40,000 − $13,560 = **$26,440**

## Form 8995-A Part II Line 12-13 (with reduction)

| Line | Item | Value |
|------|------|-------|
| 12 | Phase-in reduction (Schedule A L13) | $26,440 |
| 13 | Adjusted QBI (L11 − L12) | $40,000 − $26,440 = **$13,560** |

---

## Form 8995-A Part IV

| Line | Item | Value |
|------|------|-------|
| 27 | Total QBI component (Part II L13) | $13,560 |
| 28 | Qualified REIT/PTP dividends | $0 |
| 29 | Prior-year REIT/PTP loss carryforward | $0 |
| 30 | L28 + L29 | $0 |
| 31 | 20% × L30 | $0 |
| 32 | L27 + L31 | $13,560 |
| 33 | Taxable income before QBI | $275,000 |
| 34 | Net capital gains | $0 |
| 35 | L33 − L34 | $275,000 |
| 36 | 20% × L35 | $55,000 |
| 37 | Smaller of L32 or L36 | **$13,560** |
| 38 | Patron reduction | $0 |
| 39 | **Final QBI deduction** | **$13,560** |

---

## Form 1040 Line 13 = $13,560

Without any of these limits, Dr. Patel might have entered $50,937 (20% × $254,684). The combination of (a) the W-2 wage limit and (b) the SSTB phase-in cost her $37,377 of deduction.

---

## Tax savings analysis

Federal marginal rate at $275,000 single is 32%. The $13,560 QBI deduction saves Dr. Patel about **$4,339** in federal tax.

If she had been able to claim the full 20% (e.g., if she were below the threshold), she would have saved about $16,300. The W-2/UBIA limit and SSTB phase-in cost her about $12,000 of savings.

## Planning takeaways

1. **W-2 wages matter.** If Dr. Patel had hired a third employee at $30,000/year, her W-2 wages would have been $110,000, the W-2 limit would be $55,000 (vs. $40,000), and the binding constraint would shift. Whether to hire is a separate business decision — but the QBI math favors W-2 staff over 1099 contractors above the threshold.

2. **Her brokerage interest income pushed her above the threshold.** If she had kept that interest at $20,000 instead of $36,000 (e.g., by holding more in a tax-deferred IRA), her taxable income would have been below the threshold and she could have used Form 8995 with no SSTB issues — claiming roughly the full 20% × QBI = $50,937.

3. **SEP-IRA is doing more than reducing taxes.** The $25,000 contribution reduces her QBI by $25,000 → reduces her tentative deduction by $5,000. Net of the deferred income tax (32% × $25,000 = $8,000), the SEP-IRA still wins, but it's not a no-brainer; a Solo 401(k) might let her contribute more.

---

## Form 1040 total tax

| Line | Item | Amount |
|------|------|--------|
| 11 | AGI | $290,684 |
| 12 | Standard deduction | $15,000 |
| 13 | QBI deduction | $13,560 |
| 15 | Taxable income | $262,124 |
| 16 | Tax (single, 2025 brackets) | $59,925 (approximately) |
| 22 | SE tax (from Schedule SE) | $22,632 |
| 23 | Total tax | $82,557 (approximately) |

Vs. taking the simple Form 8995 (incorrect path): she would have claimed $50,937 deduction → taxable income of $224,747 → tax of about $48,063 + SE $22,632 = $70,695. The IRS would catch this within ~12 months; CP2000 notice for $11,862 plus interest.
