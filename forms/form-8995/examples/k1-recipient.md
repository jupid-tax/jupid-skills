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
- Box 17 code V (Section 199A information), attached statement:
  - QBI: $80,000
  - W-2 wages: $90,000 (irrelevant for Form 8995, only matters above threshold)
  - UBIA of qualified property: $5,000 (irrelevant for Form 8995)
  - SSTB: No
- Daniel's health insurance is through Sarah's employer plan, so he has no SE health insurance deduction tied to the S corporation

### Other income

- Qualified dividends (1099-DIV Box 1b): $1,500
- Bank interest (1099-INT Box 1): $200

### Form 1040 (computed pre-QBI)

- Total income: $160,000 (W-2) + $80,000 (K-1) + $1,500 (qual div) + $200 (interest) = $241,700
- Adjustments to income: $0 (none applicable)
- **AGI (Line 11a): $241,700**
- Standard deduction (MFJ, 2025, line 12e): $31,500
- Schedule 1-A deductions (line 13b): $0
- **Taxable income before QBI: $210,200**

---

## Threshold check

- 2025 MFJ threshold: $394,600
- Daniel and Sarah's taxable income before QBI: $210,200
- ✓ Below threshold — Form 8995 applies

---

## Computing QBI

The K-1 statement's QBI already reflects the S corporation's own deductions, including Daniel's wages. Owner-level deductions attributable to the business would still be subtracted (for a more-than-2% shareholder, mainly an SE health insurance deduction on Schedule 1 line 17). Daniel has none, so nothing is subtracted.

```
QBI from Kim Consulting Inc. = $80,000 (from Box 17 code V)
```

Daniel and Sarah have no other QBI sources.

---

## Filling out Form 8995

### Header

- Name: Daniel Kim & Sarah Kim
- SSN: XXX-XX-5678 (Daniel's)

### Line 1, rows i–v

| (a) Trade/business | (b) TIN | (c) QBI |
|--------------------|----------|-----------|
| Kim Consulting Inc. | XX-XXXXXXX (S-corp EIN) | $80,000 |

### Lines 2-5

- Line 2: $80,000
- Line 3: $0
- Line 4: $80,000
- Line 5: $80,000 × 0.20 = $16,000

### Lines 6-9

- Line 6: $0 (no REIT or PTP — qualified dividends from regular stock are not §199A dividends)
- Line 7: $0
- Line 8: $0
- Line 9: $0

### Lines 10-17

- Line 10: $16,000
- Line 11: $210,200 (taxable income before QBI)
- Line 12: $1,500 (qualified dividends; no net capital gain to add)
- Line 13: $210,200 − $1,500 = $208,700
- Line 14: $208,700 × 0.20 = $41,740
- Line 15: smaller of $16,000 or $41,740 = **$16,000**
- Lines 16-17: $0

---

## Result

Daniel and Sarah's QBI deduction is **$16,000**. This flows to Form 1040 line 13a.

**Limiting factor:** QBI itself (Line 10). The taxable income limit ($41,740) is much larger than the actual QBI deduction, so QBI is the binding constraint.

---

## Updated Form 1040

- AGI: $241,700
- Standard deduction: $31,500
- QBI deduction: $16,000
- **Taxable income: $194,200**

Ordinary taxable income (excluding the $1,500 of qualified dividends) drops from $208,700 to $192,700. Under the 2025 MFJ brackets (22% up to $206,700, 24% above; Rev. Proc. 2024-40 Table 1) that is $2,000 at 24% plus $14,000 at 22%: the deduction saves Daniel and Sarah about $3,560 in federal income tax.

---

## Insights for the agent

### The K-1 QBI already reflects entity-level deductions

The K-1 amount is what the S-corp's tax preparer computed after the entity's own deductions. The shareholder subtracts only owner-level deductions attributable to the business (here, none). Ask; don't assume.

### The reasonable compensation question matters indirectly

Daniel's W-2 from Kim Consulting reduces the S-corp's net income before it computes QBI. If Daniel had paid himself less salary, more would have flowed through as QBI — but the IRS requires reasonable compensation, so this is not a planning lever.

### Below threshold = ignore the W-2 wage and UBIA figures on the code V statement

Below the threshold, the W-2 wage and UBIA limits don't apply. The Section 199A statement reports them anyway because the S-corp doesn't know whether each shareholder will be above or below the threshold.

### Qualified dividends from regular stock are not §199A

Qualified dividends from C-corp stock (Apple, Microsoft, etc.) do not qualify for §199A. Only Section 199A dividends from REITs (1099-DIV Box 5) qualify. Daniel's $1,500 in qualified dividends does NOT go on Line 6 — it's included in Line 12 (net capital gain increased by qualified dividends), which subtracts from Line 11.

---

## Validation summary

- Math: all checks passed ✓
- Threshold: $210,200 below $394,600 MFJ threshold ✓
- Sanity:
  - QBI on row 1i, column (c) = K-1 Box 17 code V statement QBI ✓
  - No owner-level deductions to subtract (confirmed with user) ✓
  - SSTB status irrelevant below threshold ✓
- Carryforwards: None
- Next steps:
  - Form 8995 attaches to Form 1040
  - Line 15 ($16,000) → Form 1040 line 13a
  - Daniel and Sarah's federal tax computed on $194,200 taxable income
  - File jointly by April 15, 2026
