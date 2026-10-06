# Example — MFJ S-Corp Software Consultant (Above Threshold, Non-SSTB)

End-to-end Form 8995-A walkthrough for an S-corp owner above the §199A threshold whose business is non-SSTB. Tax year 2025 (filed in 2026); 2025 Form 8995-A and instructions.

---

## Persona

**Marcus Chen.** Age 42. Married filing jointly. Owns 100% of Chen Software Consulting Inc. (S-corp), which provides custom software development to enterprise clients. He has two W-2 employees (a senior developer and a project manager). Spouse Lisa works for a separate employer and receives $40,000 W-2.

## 2025 Inputs

| Item | Amount |
|------|--------|
| S-corp K-1 box 1 ordinary income | $400,000 |
| K-1 box 17 code V statement: QBI / W-2 wages / UBIA / SSTB | $400,000 / $350,000 / $80,000 / No |
| Marcus's reasonable comp from S-corp (W-2) | $150,000 |
| W-2 wages paid by S-corp (Marcus + employees) | $350,000 ($150K + $120K + $80K) |
| UBIA of qualified property | $80,000 (laptops, monitors, server hardware in service ≤ 5 years) |
| Lisa's W-2 from external employer | $40,000 |
| Joint AGI before deductions | (computed below) |
| Standard deduction (MFJ, 2025) | $31,500 |
| No itemized deductions, no Schedule 1-A deductions, no other income |

## Form 1040 build-up

| Line | Item | Amount |
|------|------|--------|
| 1a | Marcus's W-2 + Lisa's W-2 | $190,000 |
| 8 | Schedule E ordinary income (from K-1 box 1) | $400,000 |
| **9** | **Total income** | **$590,000** |
| 10 | Adjustments | $0 (no SE tax — S-corp owner; no SE HI deduction at the personal level for S-corp owner who has it through corp) |
| **11a** | **AGI** | **$590,000** |
| 12e | Standard deduction (MFJ, 2025) | $31,500 |
| 13b | Schedule 1-A deductions | $0 |
| | **Taxable income before QBI** | **$558,500** |

---

## SSTB Classification

Software development is **generally not an SSTB**: it is not one of the listed fields, and consulting under Treas. Reg. §1.199A-5(b)(2)(vii) means advice and counsel and "does not include the performance of services other than advice and counsel." The regulation has no software-specific example, so classification rests on the facts.

If Marcus described himself as a "consultant" but actually delivers software code, he's non-SSTB. If he were billed for advice alone (no code deliverable), that work could be consulting. The agent should confirm the nature of the work product and how it is billed.

## Threshold check

- Threshold for MFJ (2025): $394,600
- Phase-in top: $494,600
- Marcus at $558,500 → **above the top of the phase-in range**

Because the business is not an SSTB, there is no Schedule A. Above the top of the range, Part III does not apply and the W-2/UBIA limit applies in full.

---

## QBI computation

K-1 box 1 ordinary income: $400,000

For an S-corp K-1, QBI comes from the box 17 code V statement: $400,000. It matches box 1 here, and both are already after the corporation deducted Marcus's $150,000 of wages; do not subtract them again. Marcus claims no self-employed health insurance deduction or other owner-level deductions tied to the corporation (asked and confirmed), so nothing is subtracted.

**QBI = $400,000**

(If the code V statement showed a different QBI than box 1, for example $395,000, use the statement.)

---

## Form 8995-A Part I

| (a) Name | (b) SSTB | (c) Aggregation | (d) TIN | (e) Patron |
|----------|----------|-----------------|---------|------------|
| Chen Software Consulting Inc. | ☐ (software) | ☐ | XX-XXXXXXX | ☐ |

## Form 8995-A Part II

| Line | Item | Value |
|------|------|-------|
| 2 | QBI | $400,000 |
| 3 | 20% × L2 | $80,000 |
| 4 | W-2 wages | $350,000 |
| 5 | 50% × L4 | $175,000 |
| 6 | 25% × L4 | $87,500 |
| 7 | UBIA | $80,000 |
| 8 | 2.5% × L7 | $2,000 |
| 9 | L6 + L8 | $89,500 |
| 10 | Greater of L5 or L9 | $175,000 |
| 11 | Smaller of L3 or L10 | **$80,000** |
| 12 | Phased-in reduction | $0 (Part III not used: above the phase-in range) |
| 13 | Greater of L11 or L12 | **$80,000** |
| 14 | Patron reduction | $0 |
| 15 | L13 − L14 | $80,000 |
| 16 | Total QBI component | $80,000 |

The W-2 wage limit ($175,000) is well above the tentative 20% deduction ($80,000), so it doesn't bind. Marcus gets the full 20%.

---

## Form 8995-A Part IV

| Line | Item | Value |
|------|------|-------|
| 27 | Total QBI component | $80,000 |
| 28 | Qualified REIT/PTP dividends | $0 |
| 29 | Prior-year carryforward | $0 |
| 30 | L28 + L29 | $0 |
| 31 | 20% × L30 | $0 |
| 32 | L27 + L31 | $80,000 |
| 33 | Taxable income before QBI | $558,500 |
| 34 | Net capital gain + qualified dividends | $0 |
| 35 | L33 − L34 | $558,500 |
| 36 | 20% × L35 | $111,700 |
| 37 | Smaller of L32 or L36 | **$80,000** |
| 38 | DPAD under §199A(g) | $0 |
| 39 | **Total QBI deduction** | **$80,000** |
| 40 | REIT/PTP loss carryforward | $0 |

---

## Form 1040 line 13a = $80,000

Marcus keeps the full §199A deduction because:
1. Software is non-SSTB → no Schedule A
2. W-2 wages ($350,000) easily support the W-2/UBIA limit (50% × $350,000 = $175,000 vs. 20% × $400,000 = $80,000 needed)
3. The overall taxable-income cap (20% × $558,500 = $111,700) doesn't bind either

## Tax savings

Under the 2025 MFJ rate schedule (Rev. Proc. 2024-40 Table 1), taxable income of $558,500 is taxed at 35% above $501,050 and 32% below it. The $80,000 deduction removes $57,450 at 35% and $22,550 at 32%: it saves about **$27,324** in federal income tax.

---

## Planning takeaways

1. **Reasonable comp helps the QBI math.** Marcus's $150,000 W-2 from the S-corp is part of the W-2 wages that support the QBI limit. If he had paid himself only $80,000 reasonable comp (saving SS/Medicare on the difference), the W-2 wages would drop to $280,000, the 50% limit would drop to $140,000 — still above $80,000 needed, so no harm done THIS year. But if QBI rose or wages dropped, the trade-off would matter.

2. **Capital intensity (UBIA) doesn't help much here.** With $80,000 UBIA and $350,000 wages, the 25%-W-2-plus-2.5%-UBIA branch ($87,500 + $2,000 = $89,500) is already lower than the 50%-W-2 branch ($175,000). UBIA matters more for capital-intensive businesses (real estate) where W-2 wages alone don't suffice.

3. **Software is generally non-SSTB even when called consulting.** This is one of the most-mistaken classifications. The practical question is "what's the deliverable and what is billed?" Code = generally non-SSTB. Separately billed advice = consulting = SSTB.

4. **OBBBA permanence matters.** Without OBBBA 2025, §199A would have sunset 12/31/2025 and Marcus would lose this deduction for tax year 2026 onward. OBBBA made it permanent, so he can plan around it indefinitely.

---

## Form 1040 total tax

| Line | Item | Amount |
|------|------|--------|
| 11a | AGI | $590,000 |
| 12e | Standard deduction | $31,500 |
| 13a | QBI deduction | $80,000 |
| 15 | Taxable income | $478,500 |
| 16 | Tax (MFJ, 2025 rate schedule) | $107,246 |
| 24 | Total tax | $107,246 |

(No SE tax — S-corp owner. Marcus pays SS/Medicare only on his $150,000 W-2, not on the remaining profit. Combined wages of $190,000 are below the $250,000 MFJ Additional Medicare Tax threshold.)

Without QBI deduction: taxable income would be $558,500, tax $134,570. The deduction saves $27,324.
