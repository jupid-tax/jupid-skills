# Example — Single Physician (SSTB, Phase-In Range)

End-to-end Form 8995-A walkthrough for a sole-proprietor physician whose taxable income places her in the SSTB phase-in range. Tax year 2025 (filed in 2026); 2025 Form 8995-A, Schedule A, and instructions.

---

## Persona

**Dr. Patel.** Age 38. Single. Family-medicine physician operating as a sole proprietor (no LLC; just Schedule C). Practice located in a leased office; she employs one nurse and one receptionist as W-2 employees.

## 2025 Inputs

| Item | Amount |
|------|--------|
| Schedule C net profit | $280,000 |
| Net earnings from self-employment ($280,000 × 0.9235) | $258,580 |
| Self-employment tax (Schedule SE line 12: $176,100 × 12.4% + $258,580 × 2.9%) | $29,335 |
| Deductible ½ SE tax (Schedule SE line 13) | $14,668 |
| Self-employed health insurance | $9,000 |
| SEP-IRA contribution | $25,000 |
| W-2 wages paid (nurse + receptionist) | $80,000 |
| UBIA of qualified property | $50,000 (medical equipment, computers, exam-room furniture, all in service ≤ 7 years; within depreciable period) |
| Brokerage interest income | $4,800 |
| Standard deduction (single, 2025) | $15,750 |
| No other income, no Schedule 1-A deductions, no other adjustments |

## Form 1040 build-up to taxable income before QBI

| Line | Item | Amount |
|------|------|--------|
| 1z | Wages | $0 |
| 2b | Taxable interest | $4,800 |
| 8 | Schedule C profit (via Schedule 1) | $280,000 |
| **9** | **Total income** | **$284,800** |
| 10 | Adjustments (½ SE tax + SE HI + SEP-IRA) | $48,668 |
| **11a** | **AGI** | **$236,132** |
| 12e | Standard deduction (single, 2025) | $15,750 |
| 13b | Schedule 1-A deductions | $0 |
| | **Taxable income before QBI (11a − 12e − 13b)** | **$220,382** |

---

## SSTB Classification

Family medicine = Health = SSTB per IRC §199A(d)(2)(A) and Treas. Reg. §1.199A-5(b)(2)(ii).

## Threshold check

- Threshold (2025, all returns other than MFJ): $197,300
- Phase-in top: $247,300
- Dr. Patel at $220,382 → **in the phase-in range**
- Form 8995-A REQUIRED; Schedule A REQUIRED

---

## QBI computation

Schedule C profit: $280,000

QBI adjustments (allocable to the medical practice):
- Less ½ SE tax: ($14,668)
- Less SE health insurance: ($9,000)
- Less SEP-IRA contribution: ($25,000)

**QBI = $231,332**

---

## Schedule A (Form 8995-A), Part I

| Line | Item | Value |
|------|------|-------|
| 1a / 1b | Trade name / TIN | Patel Family Medicine / XX-XXXXXXX |
| 2 | QBI | $231,332 |
| 3 | W-2 wages | $80,000 |
| 4 | UBIA | $50,000 |
| 5 | Taxable income before QBI | $220,382 |
| 6 | Threshold | $197,300 |
| 7 | L5 − L6 | $23,082 |
| 8 | Phase-in range | $50,000 |
| 9 | L7 ÷ L8 | 0.46164 |
| 10 | Applicable percentage (100% − L9) | 53.836% |
| 11 | L2 × L10 → Form 8995-A line 2 | $124,540 |
| 12 | L3 × L10 → Form 8995-A line 4 | $43,069 |
| 13 | L4 × L10 → Form 8995-A line 7 | $26,918 |

---

## Form 8995-A Part I

| (a) Name | (b) SSTB | (c) Aggregation | (d) TIN | (e) Patron |
|----------|----------|-----------------|---------|------------|
| Patel Family Medicine | ☑ | ☐ | XX-XXXXXXX | ☐ |

## Form 8995-A Part II (column A)

| Line | Item | Value |
|------|------|-------|
| 2 | QBI (Schedule A line 11) | $124,540 |
| 3 | 20% × L2 | $24,908 |
| 4 | W-2 wages (Schedule A line 12) | $43,069 |
| 5 | 50% × L4 | $21,535 |
| 6 | 25% × L4 | $10,767 |
| 7 | UBIA (Schedule A line 13) | $26,918 |
| 8 | 2.5% × L7 | $673 |
| 9 | L6 + L8 | $11,440 |
| 10 | Greater of L5 or L9 | $21,535 |
| 11 | Smaller of L3 or L10 | $21,535 |
| 12 | Phased-in reduction (Part III line 26) | $23,351 |
| 13 | Greater of L11 or L12 | **$23,351** |
| 14 | Patron reduction | $0 |
| 15 | L13 − L14 | $23,351 |
| 16 | Total QBI component | $23,351 |

## Form 8995-A Part III (line 10 < line 3 and taxable income in range)

| Line | Item | Value |
|------|------|-------|
| 17 | Line 3 | $24,908 |
| 18 | Line 10 | $21,535 |
| 19 | L17 − L18 | $3,373 |
| 20 | Taxable income before QBI | $220,382 |
| 21 | Threshold | $197,300 |
| 22 | L20 − L21 | $23,082 |
| 23 | Phase-in range | $50,000 |
| 24 | L22 ÷ L23 | 46.164% |
| 25 | L19 × L24 | $1,557 |
| 26 | L17 − L25 → line 12 | $23,351 |

The wage limit binds (50% × $43,069 = $21,535 is below 20% of the reduced QBI, $24,908), but because she is inside the phase-in range Part III phases that limit in: line 13 takes the larger $23,351.

---

## Form 8995-A Part IV

| Line | Item | Value |
|------|------|-------|
| 27 | Total QBI component (line 16) | $23,351 |
| 28 | Qualified REIT/PTP income | $0 |
| 29 | Prior-year REIT/PTP loss carryforward | $0 |
| 30 | L28 + L29 | $0 |
| 31 | 20% × L30 | $0 |
| 32 | L27 + L31 | $23,351 |
| 33 | Taxable income before QBI | $220,382 |
| 34 | Net capital gain + qualified dividends | $0 |
| 35 | L33 − L34 | $220,382 |
| 36 | 20% × L35 | $44,076 |
| 37 | Smaller of L32 or L36 | **$23,351** |
| 38 | DPAD under §199A(g) | $0 |
| 39 | **Total QBI deduction** | **$23,351** |
| 40 | REIT/PTP loss carryforward | $0 |

---

## Form 1040 line 13a = $23,351

Without the SSTB phase-in and the W-2/UBIA limit, the deduction would have been the smaller of 20% × $231,332 = $46,266 or the line 36 income limitation of $44,076. The two limits cost her $20,725 of deduction ($44,076 − $23,351).

---

## Tax savings analysis

Taxable income falls from $220,382 to $197,031. Under the 2025 single rate schedule (Rev. Proc. 2024-40 Table 3) the tax falls from $47,585 to $40,134: the $23,351 deduction saves Dr. Patel about **$7,451** in federal income tax.

## Planning takeaways

1. **W-2 wages matter.** Line 10 ($21,535) is below line 3 ($24,908), so the wage limit binds and only Part III keeps part of the gap. Report this; whether to change staffing or payroll is a business decision for the user and a CPA.

2. **Inside the phase-in range, taxable income works twice.** Each $1,000 of extra taxable income lowers the Schedule A applicable percentage by 2 points ($1,000 ÷ $50,000) and raises the Part III phase-in percentage by the same amount. At $247,300 or more (2025), the practice's QBI would not count at all.

3. **The SEP-IRA contribution cuts both ways.** The $25,000 contribution reduces QBI by $25,000 and also reduces taxable income by $25,000, which raises the applicable percentage. Run the form both ways before anyone draws a conclusion; this skill does not recommend contribution amounts.

---

## Form 1040 total tax

| Line | Item | Amount |
|------|------|--------|
| 11a | AGI | $236,132 |
| 12e | Standard deduction | $15,750 |
| 13a | QBI deduction | $23,351 |
| 15 | Taxable income | $197,031 |
| 16 | Tax (single, 2025 rate schedule) | $40,134 |
| Sch. 2 line 4 | SE tax (Schedule SE) | $29,335 |
| Sch. 2 line 11 | Additional Medicare Tax (Form 8959: ($258,580 − $200,000) × 0.9%) | $527 |
| Sch. 2 line 12 | Net investment income tax (Form 8960: $4,800 × 3.8%; MAGI exceeds $200,000 by more than $4,800) | $182 |
| 24 | Total tax | $70,178 |

Vs. taking the simple Form 8995 (incorrect path above the threshold): she would have claimed $44,076 (20% of QBI capped at 20% of taxable income), overstating the deduction by $20,725.
