# Example — Freelance Designer (Single, Sole Prop, Taxable-Income Limit Binding)

## Persona

**Maya Garcia**, 31, single, lives in Austin, TX. Operates "Garcia Design" as a sole proprietor (no LLC). Designs websites and brand identity for small businesses. Files Schedule C; this is her third year freelancing full-time.

For tax year 2025, Maya has only Schedule C income — no W-2, no K-1, no rental, no investment income beyond a small bank interest amount.

---

## Maya's tax data (2025)

### Schedule C

- Gross receipts: $58,000
- Total expenses: $8,000
- **Line 31 net profit: $50,000**

### Schedule SE

- Net earnings from SE: $50,000 × 0.9235 = $46,175
- SE tax: $46,175 × 0.153 = $7,065
- **½ SE tax (Line 13): $3,532**

### Schedule 1

- ½ SE tax (Line 15): $3,532
- SE retirement (Line 16, SEP-IRA): $1,500
- SE health insurance (Line 17): $4,200
- **Total SE adjustments: $9,232**

### Form 1040 (computed pre-QBI)

- Total income: $50,000 (Schedule C) + $0 (other) = $50,000
- Adjustments to income: $9,232
- **AGI (Line 11): $40,768**
- Standard deduction (single, 2025): $15,000
- **Taxable income before QBI: $25,768**

(Note: example assumes Maya has no other significant adjustments. Real-world might include HSA, student loan interest, etc.)

---

## Computing QBI

QBI for the Schedule C source:

```
QBI = $50,000 (Schedule C Line 31)
    − $3,532 (½ SE tax)
    − $4,200 (SE health insurance)
    − $1,500 (SEP-IRA)
    = $40,768
```

---

## Filling out Form 8995

### Header

- Name: Maya Garcia
- SSN: XXX-XX-1234

### Lines 1a-1e

| (i) Trade/business | (ii) TIN | (iii) QBI |
|--------------------|----------|-----------|
| Garcia Design | XXX-XX-1234 (Maya's SSN) | $40,768 |
| (rows 1b-1e blank) | | |

### Lines 2-4

- Line 2: $40,768
- Line 3: $0 (no prior loss)
- Line 4: $40,768

### Lines 5-9

- Line 5: $0 (no REIT or PTP)
- Line 6: $0
- Line 7: $0
- Lines 8-9: $0

### Lines 10-12

- Line 10: $40,768 × 0.20 = $8,154
- Line 11: $0 × 0.20 = $0
- Line 12: $8,154 + $0 = $8,154

### Lines 13-17

- Line 13: $25,768 (taxable income before QBI deduction)
- Line 14: $0 (no qualified dividends or LTCG)
- Line 15: $25,768 − $0 = $25,768
- Line 16: $25,768 × 0.20 = $5,154
- Line 17: lesser of $8,154 or $5,154 = **$5,154**

---

## Result

Maya's QBI deduction is **$5,154**. This flows to Form 1040 Line 13.

**Limiting factor:** Taxable income limit (Line 16). Her actual QBI would have produced an $8,154 deduction, but her taxable income is too low to support it. The $3,000 difference is *not* carried forward — the §199A taxable income limit is hard-capped, no carry.

---

## Updated Form 1040

- AGI: $40,768
- Standard deduction: $15,000
- QBI deduction: $5,154
- **Taxable income: $20,614**
- Federal income tax (2025 single brackets): 10% × $11,925 + 12% × $8,689 = $1,192 + $1,043 = $2,235
- SE tax: $7,065
- **Total federal tax: $9,300**

(Compare to without QBI: federal income tax would be $2,235 + 12% × $5,154 = $2,235 + $619 = $2,854. QBI saved Maya $619.)

---

## Insight for the agent

When the filer's taxable income is well below QBI, the §199A deduction is capped. This is common for solo filers in their first profitable years, anyone with significant adjustments to AGI (HSA, retirement, SE health insurance), or anyone with itemized deductions large relative to income.

The agent should surface this in the validation summary: "Your QBI of $40,768 supports an $8,154 deduction, but your taxable income of $25,768 caps the deduction at $5,154 (20% of taxable income excluding capital gain). Future income growth will unlock more of the deduction, up to the threshold."

---

## Validation summary

- Math: all checks passed ✓
- Threshold: $25,768 well below $241,950 single threshold ✓
- Sanity:
  - Line 17 = Line 16 (taxable income limit binding) — surfaced to user
  - QBI = 81.5% of Schedule C net profit — within expected 80-95% range ✓
- Carryforwards: None
- Next steps:
  - Form 8995 attaches to Form 1040
  - Line 17 ($5,154) goes to Form 1040 Line 13
  - Schedule SE (already complete) flows to Schedule 2 Line 4
  - File 1040 by April 15, 2026
