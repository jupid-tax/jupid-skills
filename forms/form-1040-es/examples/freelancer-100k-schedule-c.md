# Example: Freelancer with $100K Schedule C Net Profit

A canonical "solo freelancer with steady monthly income" pattern. The filer has no W-2 wages, no other income, files single, expects roughly even income across the year. Equal-installment plan, prior-year safe harbor.

## The filer

- **Name**: Priya Shah
- **Business**: Freelance UX research consultant (Schedule C)
- **Entity**: Single-member LLC (disregarded entity, files Schedule C)
- **Filing status**: Single
- **State**: Massachusetts
- **Tax year being projected**: 2026
- **Prior tax year (2025)**: filed in April 2026, AGI $93,200, total tax $19,400 (Form 1040 Line 24)

## Inputs gathered (Step 1–3 of workflow)

### Prior-year baseline

- Prior-year AGI: $93,200 (under $150K threshold → 110% rule does NOT apply)
- Prior-year total tax: $19,400
- Safe Harbor B = $19,400 × 1.00 = **$19,400**

### Current-year (2026) projection

| Worksheet line | Amount | How computed |
|----------------|--------|--------------|
| Schedule C net profit | $100,000 | Based on 2026 invoicing rate increase |
| Half of SE tax (above-the-line) | $7,065 | $14,129 SE tax × 50% (computed below) |
| Self-employed health insurance deduction | $7,200 | $600/mo Marketplace plan, no ACA subsidy |
| Solo 401(k) employer-side contribution | $18,587 | 20% × ($100K − $7,065) = up to limit |
| **Line 1 (AGI)** | **$67,148** | $100,000 − $7,065 − $7,200 − $18,587 |
| Line 2a (standard deduction) | $16,100 | 2026 single (2026 Form 1040-ES; Rev. Proc. 2025-32) |
| Line 2b (QBI) | $10,210 | smaller of 20% × QBI $67,148 = $13,430 or 20% × ($67,148 − $16,100) = $10,210 |
| Line 2c (Schedule 1-A) | $0 | no tips, overtime, car loan interest; not 65+ |
| Line 2d | $26,310 | |
| **Line 3 (taxable income)** | **$40,838** | $67,148 − $26,310 |
| Line 4 (income tax, single, 2026 Tax Rate Schedule X) | $4,653 | $1,240 + 12% × ($40,838 − $12,400) |
| Line 5 (AMT) | $0 | well under exemption |
| Line 6 | $4,653 | |
| Line 7 (credits) | $0 | no CTC, no foreign tax, etc. |
| Line 8 | $4,653 | |
| Line 9 (SE tax) | $14,129 | computed below |
| Line 10 (Add'l Medicare, NIIT) | $0 | SE earnings $92,350 < $200K threshold |
| **Line 11a (total tax)** | **$18,782** | $4,653 + $14,129 + $0 |
| Line 11b (refundable credits) | $0 | |
| **Line 11c** | **$18,782** | |

### SE tax computation (Line 9 detail)

```
SE earnings = 0.9235 × $100,000 = $92,350
SS portion = 0.124 × min($92,350, $184,500) = 0.124 × $92,350 = $11,451
Medicare portion = 0.029 × $92,350 = $2,678
SE tax = $11,451 + $2,678 = $14,129
```

Half of SE tax ($7,065) is the above-the-line deduction on Schedule 1 Line 15 — already netted into AGI projection.

(2026 SS wage base $184,500 — 2026 Form 1040-ES SE worksheet line 5.)

### Apply safe harbor

```
Line 12a = 0.90 × $18,782 = $16,904
Line 12b = $19,400 × 1.00 = $19,400  (prior AGI < $150K, so 100%)
Line 12c = min($16,904, $19,400) = $16,904
```

**Required annual payment: $16,904**

### Withholding and per-quarter

Priya has no W-2 wages, no pension, no voluntary SS withholding. Line 13 (expected withholding) = $0.

Line 14a = $16,904 − $0 = $16,904 (more than zero)
Line 14b = $18,782 − $0 = $18,782 ($1,000 or more → estimates required)
Line 15 = $16,904 / 4 = **$4,226 per quarter**

### Income evenness check

Priya invoices monthly at roughly the same rate. Income is even across quarters. **Equal-installment method is appropriate.** No annualization needed.

---

## The deliverable

```markdown
# Form 1040-ES — Estimated Tax Plan for tax year 2026

## Filer
- Name: Priya Shah
- SSN: ***-**-**** (placeholder; never logged)
- Filing status: Single
- State (for voucher mailing): MA

## Prior-year baseline (tax year 2025)
- Prior-year AGI: $93,200
- Prior-year total tax (Line 24): $19,400
- 110% safe harbor applies: No (AGI $93,200 < $150,000)
- Prior-year safe harbor amount: $19,400

## Current-year projection (tax year 2026)
| Worksheet line | Amount |
|----------------|--------|
| 1.  Estimated AGI | $67,148 |
| 2a. Standard deduction | $16,100 |
| 2b. QBI deduction | $10,210 |
| 2c. Schedule 1-A deductions | $0 |
| 2d. Total deductions | $26,310 |
| 3.  Taxable income | $40,838 |
| 4.  Tax (from rate schedule) | $4,653 |
| 5.  AMT | $0 |
| 6.  Subtotal | $4,653 |
| 7.  Credits | $0 |
| 8.  Subtotal | $4,653 |
| 9.  Self-employment tax | $14,129 |
| 10. Other taxes (NIIT, Add'l Medicare) | $0 |
| 11a. Total tax | $18,782 |
| 11b. Refundable credits | $0 |
| 11c. Net total tax | $18,782 |
| 12a. 90% × Line 11c | $16,904 |
| 12b. Prior-year × 100% | $19,400 |
| 12c. Required annual payment (smaller) | $16,904 |
| 13. Expected withholding | $0 |
| 14a. Line 12c − Line 13 | $16,904 |
| 14b. Line 11c − Line 13 ($1,000 test) | $18,782 |
| 15. Per-quarter (¼ of 14a) | $4,226 |

## Installment schedule
| Voucher | Due date | Amount | Channel |
|---------|----------|--------|---------|
| Q1 | 2026-04-15 | $4,226 | Direct Pay |
| Q2 | 2026-06-15 | $4,226 | Direct Pay |
| Q3 | 2026-09-15 | $4,226 | Direct Pay |
| Q4 | 2027-01-15 | $4,226 | Direct Pay |
| **Total** | | **$16,904** | |

## Method
- [x] Equal installments (income spread evenly)
- [ ] Annualized income
- [ ] Single-payment farmer/fisher exception

## Validation summary
- Math: all checks passed
- Sanity:
  - SE tax is 75% of total tax ($14,129 / $18,782) and 14.1% of net profit — typical for a solo Schedule C filer at this income
  - 90% current-year ($16,904) < prior-year ($19,400) → Line 12a governs, but only if the projection holds (see "What if" below)
  - Withholding $0 → all $16,904 must come from estimated payments
- Year-aware notes:
  - 2026 standard deduction $16,100, Tax Rate Schedule X, SS wage base $184,500 — 2026 Form 1040-ES
  - QBI below the 2026 $201,750 threshold, so the simple 20% rule applies (Rev. Proc. 2025-32 §4.26)
  - Self-employed health insurance deduction $7,200 — verify against Marketplace plan

## Sources cited in this draft
- IRS Form 1040-ES (2026)
- IRC §6654 (failure to pay estimated tax)
- IRC §6654(d)(1)(B) (required annual payment)
- IRC §6654(d)(1)(C) (110% rule for high-AGI filers — not triggered here)
- IRC §1402 (self-employment tax)
- IRC §3101(b)(2) (Additional Medicare Tax — not triggered here)
- IRC §1411 (NIIT — not triggered here)
- IRC §199A (QBI deduction)
- Rev. Proc. 2025-32 (2026 inflation adjustments)
- IRS Pub. 505 (Tax Withholding and Estimated Tax)
```

---

## Why each non-obvious choice

**Why use Line 12a (90% current) instead of Line 12b (100% prior)?**
Line 12a = $16,904 < Line 12b = $19,400. The smaller of the two governs. Priya pays $16,904 across the year (less cash than 100% of prior).

**Why no Add'l Medicare or NIIT?**
SE earnings ($92,350) plus zero W-2 = under $200K single threshold. No Add'l Medicare. AGI $67,148 also under $200K, so no NIIT. Both Lines 10 entries = $0.

**Why include the half-of-SE-tax deduction in AGI projection but not subtract from Line 9?**
The half-of-SE-tax deduction reduces AGI (and therefore Line 1 → Line 3 → Line 4 income tax). It does NOT reduce SE tax itself. SE tax is computed on the full SE income before the deduction.

**Why solo 401(k) contribution = $18,587?**
For a Schedule C filer, the deductible employer-side contribution is `0.20 × (net profit − ½ SE tax)` = `0.20 × ($100,000 − $7,065)` = `0.20 × $92,935` = $18,587. The agent flagged this as an above-the-line deduction reducing AGI. Total contribution to solo 401(k) (employee elective deferral limit $24,500 for 2026, IR-2025-111) is separate; only the employer-side counts toward AGI reduction here.

**Why pay via Direct Pay?**
Priya has no need to schedule the full year at once (her monthly income is steady; she'll re-check projections each quarter). Direct Pay is free, no enrollment, deterministic flow. EFTPS would require enrollment lead time she doesn't need.

**What if Priya is audited?**
Her audit defense would be:
1. Schedule C invoicing records substantiate $100K projected
2. Solo 401(k) plan document and contribution records substantiate $18,587 deduction
3. Marketplace 1095-A or premium statements substantiate $7,200 self-employed health insurance
4. Form 1040-ES vouchers + Direct Pay confirmation numbers substantiate $16,904 payments

If 2026 actual tax exceeds the projection (e.g., a surprise capital gain), the 90% test is measured against the *actual* 2026 tax, so $16,904 may no longer be enough and a §6654 penalty can apply to the shortfall. Only the prior-year safe harbor (Line 12b, $19,400 = $4,850 per quarter) protects her regardless of how 2026 turns out. The agent should say this and let Priya choose between the lower 12a schedule and the certain 12b schedule.
