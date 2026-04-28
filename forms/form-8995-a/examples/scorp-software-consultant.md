# Example — MFJ S-Corp Software Consultant (Above Threshold, Non-SSTB)

End-to-end Form 8995-A walkthrough for an S-corp owner above the §199A threshold whose business is non-SSTB.

---

## Persona

**Marcus Chen.** Age 42. Married filing jointly. Owns 100% of Chen Software Consulting Inc. (S-corp), which provides custom software development to enterprise clients. He has two W-2 employees (a senior developer and a project manager). Spouse Lisa works for a separate employer and receives $40,000 W-2.

## 2025 Inputs

| Item | Amount |
|------|--------|
| S-corp K-1 box 1 ordinary income | $400,000 |
| Marcus's reasonable comp from S-corp (W-2) | $150,000 |
| W-2 wages paid by S-corp (Marcus + employees) | $350,000 ($150K + $120K + $80K) |
| UBIA of qualified property | $80,000 (laptops, monitors, server hardware in service ≤ 5 years) |
| Lisa's W-2 from external employer | $40,000 |
| Joint AGI before deductions | (computed below) |
| Standard deduction (MFJ, 2025) | $30,000 |
| No itemized deductions, no other income |

## Form 1040 build-up

| Line | Item | Amount |
|------|------|--------|
| 1a | Marcus's W-2 + Lisa's W-2 | $190,000 |
| 8 | Schedule E ordinary income (from K-1 box 1) | $400,000 |
| **9** | **Total income** | **$590,000** |
| 10 | Adjustments | $0 (no SE tax — S-corp owner; no SE HI deduction at the personal level for S-corp owner who has it through corp) |
| **11** | **AGI** | **$590,000** |
| 12 | Standard deduction (MFJ, 2025) | $30,000 |
| | **Taxable income before QBI** | **$560,000** |

For this example we'll round to **$550,000** to position Marcus clearly above the $483,900 MFJ threshold but with simpler numbers.

---

## SSTB Classification

Software development is **NOT SSTB**. Per Treas. Reg. §1.199A-5(b)(2)(vii), software development, programming, design, and IT services are explicitly excluded from "consulting" for §199A purposes. Example 4 in the regulation is on point.

If Marcus described himself as a "consultant" but actually delivers software code, he's non-SSTB. If he were giving pure advice (no code deliverable), he might be SSTB. The agent should confirm the nature of the work product.

## Threshold check

- Threshold for MFJ (2025): $483,900
- Phase-in top: $583,900
- Marcus at $550,000 → **above threshold but in phase-in window range**

But because Marcus is **not SSTB**, the phase-in doesn't apply to him. The phase-in is only for SSTBs. Above the threshold for non-SSTBs, the W-2/UBIA limit applies in full immediately. No Schedule A.

---

## QBI computation

K-1 box 1 ordinary income: $400,000

For S-corp K-1, QBI = box 1 box (already excludes Marcus's $150,000 W-2 because the corp deducted that as wages).

**QBI = $400,000**

(Verify against K-1 box 17 code V if provided. If the corp computed §199A QBI separately and reported $395,000 in box 17 code V, use $395,000. Often the two match.)

---

## Form 8995-A Part I

| (a) Name | (b) SSTB | (c) EIN |
|----------|----------|---------|
| Chen Software Consulting Inc. | No (software) | XX-XXXXXXX |

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
| 12 | Phase-in reduction | $0 (not SSTB) |
| 13 | Adjusted QBI | **$80,000** |

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
| 33 | Taxable income before QBI | $550,000 |
| 34 | Net capital gains | $0 |
| 35 | L33 − L34 | $550,000 |
| 36 | 20% × L35 | $110,000 |
| 37 | Smaller of L32 or L36 | **$80,000** |
| 38 | Patron reduction | $0 |
| 39 | **Final QBI deduction** | **$80,000** |

---

## Form 1040 Line 13 = $80,000

Marcus saves the full §199A deduction because:
1. Software is non-SSTB → no phase-in
2. W-2 wages ($350,000) easily support the W-2/UBIA limit (50% × $350,000 = $175,000 vs. 20% × $400,000 = $80,000 needed)
3. The overall taxable-income cap (20% × $550,000 = $110,000) doesn't bind either

## Tax savings

At Marcus's 35% federal marginal rate (MFJ, $550,000 taxable income), the $80,000 QBI deduction saves about **$28,000** in federal tax.

---

## Planning takeaways

1. **Reasonable comp helps the QBI math.** Marcus's $150,000 W-2 from the S-corp is part of the W-2 wages that support the QBI limit. If he had paid himself only $80,000 reasonable comp (saving SS/Medicare on the difference), the W-2 wages would drop to $280,000, the 50% limit would drop to $140,000 — still above $80,000 needed, so no harm done THIS year. But if QBI rose or wages dropped, the trade-off would matter.

2. **Capital intensity (UBIA) doesn't help much here.** With $80,000 UBIA and $350,000 wages, the 25%-W-2-plus-2.5%-UBIA branch ($87,500 + $2,000 = $89,500) is already lower than the 50%-W-2 branch ($175,000). UBIA matters more for capital-intensive businesses (real estate) where W-2 wages alone don't suffice.

3. **Software is non-SSTB even when called consulting.** This is one of the most-mistaken classifications. The dispositive question is "what's the deliverable?" Code = non-SSTB. Pure advice without code = consulting = SSTB.

4. **OBBBA permanence matters.** Without OBBBA 2025, §199A would have sunset 12/31/2025 and Marcus would lose this deduction for tax year 2026 onward. OBBBA made it permanent, so he can plan around it indefinitely.

---

## Form 1040 total tax

| Line | Item | Amount |
|------|------|--------|
| 11 | AGI | $590,000 |
| 12 | Standard deduction | $30,000 |
| 13 | QBI deduction | $80,000 |
| 15 | Taxable income | $480,000 |
| 16 | Tax (MFJ, 2025 brackets) | $113,127 (approximately) |
| 23 | Total tax | $113,127 |

(No SE tax — S-corp owner. Marcus pays SS/Medicare only on his $150,000 W-2, not on the $250,000 distribution.)

Without QBI deduction: taxable income would be $560,000, tax about $141,127. The $80,000 deduction × 35% = $28,000 saved as expected.
