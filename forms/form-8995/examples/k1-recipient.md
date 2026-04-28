# Example — S-corp Shareholder with K-1 QBI (No Schedule C)

## Persona

**Daniel Kim**, 42, married filing jointly, lives in Seattle, WA. Daniel is the sole shareholder of "Kim Consulting Inc.", an S-corporation that provides IT consulting. He pays himself reasonable W-2 compensation and takes additional profits as distributions. Daniel does not file a Schedule C — his S-corp issues him a K-1 each year.

For tax year 2025, Daniel and his spouse Sarah have:
- Daniel's W-2 from Kim Consulting Inc.: $90,000
- Sarah's W-2 from a different employer: $70,000
- K-1 from Kim Consulting Inc. (Box 1: $80,000 ordinary business income; Section 199A statement: QBI $80,000)
- Joint qualified dividends from a brokerage: $1,500
- Bank interest: $200

---

## Daniel's tax data (2025)

### W-2 income

- Daniel's W-2: $90,000
- Sarah's W-2: $70,000
- **Total wages: $160,000**

### K-1 (Form 1120-S)

- Box 1 (ordinary business income): $80,000
- Box 17 code V (Section 199A QBI): $80,000
- Box 17 code W (W-2 wages from S-corp): $90,000 (irrelevant for Form 8995, only matters above threshold)
- Box 17 code X (UBIA): $5,000 (irrelevant for Form 8995)
- SSTB: No

### Other income

- Qualified dividends (1099-DIV Box 1b): $1,500
- Bank interest (1099-INT Box 1): $200

### Form 1040 (computed pre-QBI)

- Total income: $160,000 (W-2) + $80,000 (K-1) + $1,500 (qual div) + $200 (interest) = $241,700
- Adjustments to income: $0 (none applicable)
- **AGI (Line 11): $241,700**
- Standard deduction (MFJ, 2025): $30,000
- **Taxable income before QBI: $211,700**

---

## Threshold check

- 2025 MFJ threshold: $483,900
- Daniel and Sarah's taxable income before QBI: $211,700
- ✓ Below threshold — Form 8995 applies

---

## Computing QBI

K-1 QBI is reported pre-adjustment. There are no §199A adjustments to subtract (those only apply to Schedule C, not K-1).

```
QBI from Kim Consulting Inc. = $80,000 (from Box 17 code V)
```

Daniel and Sarah have no other QBI sources.

---

## Filling out Form 8995

### Header

- Name: Daniel Kim & Sarah Kim
- SSN: XXX-XX-5678 (Daniel's)

### Lines 1a-1e

| (i) Trade/business | (ii) TIN | (iii) QBI |
|--------------------|----------|-----------|
| Kim Consulting Inc. | XX-XXXXXXX (S-corp EIN) | $80,000 |

### Lines 2-4

- Line 2: $80,000
- Line 3: $0
- Line 4: $80,000

### Lines 5-9

- Line 5: $0 (no REIT or PTP — qualified dividends from regular stock are not §199A dividends)
- Line 6: $0
- Line 7: $0

### Lines 10-12

- Line 10: $80,000 × 0.20 = $16,000
- Line 11: $0
- Line 12: $16,000

### Lines 13-17

- Line 13: $211,700 (taxable income before QBI)
- Line 14: $1,500 (qualified dividends; no LTCG to add)
- Line 15: $211,700 − $1,500 = $210,200
- Line 16: $210,200 × 0.20 = $42,040
- Line 17: lesser of $16,000 or $42,040 = **$16,000**

---

## Result

Daniel and Sarah's QBI deduction is **$16,000**. This flows to Form 1040 Line 13.

**Limiting factor:** QBI itself (Line 12). The taxable income limit ($42,040) is much larger than the actual QBI deduction, so QBI is the binding constraint.

---

## Updated Form 1040

- AGI: $241,700
- Standard deduction: $30,000
- QBI deduction: $16,000
- **Taxable income: $195,700**

At the 22-24% MFJ marginal bracket, the $16,000 deduction saves Daniel and Sarah roughly $3,700 in federal income tax.

---

## Insights for the agent

### The K-1 QBI is reported gross — no adjustments

Unlike sole-prop QBI, the K-1 amount is what the S-corp's tax preparer computed after applying the entity's own §199A adjustments. The shareholder doesn't subtract anything further.

### The reasonable compensation question matters indirectly

Daniel's W-2 from Kim Consulting reduces the S-corp's net income before it computes QBI. If Daniel had paid himself less salary, more would have flowed through as QBI — but the IRS requires reasonable compensation, so this is not a planning lever.

### Below threshold = ignore Box 17 codes W, X

Below the threshold, the W-2 wage and UBIA limits don't apply. The Section 199A statement reports them anyway because the S-corp doesn't know whether each shareholder will be above or below the threshold.

### Qualified dividends from regular stock are not §199A

Qualified dividends from C-corp stock (Apple, Microsoft, etc.) do not qualify for §199A. Only Section 199A dividends from REITs (1099-DIV Box 5) qualify. Daniel's $1,500 in qualified dividends does NOT go on Line 5 — it's included in Line 14 as net capital gain (which subtracts from Line 13).

---

## Validation summary

- Math: all checks passed ✓
- Threshold: $211,700 below $483,900 MFJ threshold ✓
- Sanity:
  - QBI on Line 1c (iii) = K-1 Box 17 code V exactly ✓
  - No SE adjustments needed (K-1 source) ✓
  - SSTB status irrelevant below threshold ✓
- Carryforwards: None
- Next steps:
  - Form 8995 attaches to Form 1040
  - Line 17 ($16,000) → Form 1040 Line 13
  - Daniel and Sarah's federal tax computed on $195,700 taxable income
  - File jointly by April 15, 2026
