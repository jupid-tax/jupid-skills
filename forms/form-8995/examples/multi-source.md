# Example — Multi-Source QBI with REIT Dividends and Prior-Year Loss Carryforward

## Persona

**Priya Patel**, 38, single, lives in Denver, CO. Priya runs "Patel Consulting" as a sole proprietor (Schedule C) — strategy consulting for nonprofits. She also holds a small position in a real estate investment trust through her brokerage account, and she had a Schedule C loss in 2023 that generated a QBI loss carryforward.

For tax year 2025:
- Schedule C (Patel Consulting): $30,000 net profit
- 1099-DIV from Schwab (REIT ETF): Box 5 Section 199A dividends $250
- Prior-year QBI loss carryforward (from 2023 Form 8995 Line 16): -$3,000
- No K-1 income, no PTP income, no rental real estate

---

## Priya's tax data (2025)

### Schedule C

- Gross receipts: $42,000
- Total expenses: $12,000
- **Line 31 net profit: $30,000**

### Schedule SE

- Net earnings from SE: $30,000 × 0.9235 = $27,705
- SE tax: $27,705 × 0.153 = $4,239
- **½ SE tax (Line 13): $2,120**

### Schedule 1

- ½ SE tax (Line 15): $2,120
- SE health insurance (Line 17): $3,600
- SE retirement (Line 16, SEP-IRA): $0 (Priya didn't contribute this year)
- **Total SE adjustments: $5,720**

### 1099-DIV

- Box 1a (total ordinary dividends): $400
- Box 1b (qualified dividends): $300
- **Box 5 (Section 199A dividends): $250**

### Form 1040 (computed pre-QBI)

- Total income: $30,000 (Schedule C) + $400 (ordinary div) + $0 (other) = $30,400
- Adjustments to income: $5,720
- **AGI (Line 11): $24,680**
- Standard deduction (single, 2025): $15,000
- **Taxable income before QBI: $9,680**

(Note: this is unusually low taxable income for the example, but plausible for a consultant rebuilding their practice.)

---

## Threshold check

- 2025 single threshold: $241,950
- Priya's taxable income before QBI: $9,680
- ✓ Well below threshold — Form 8995 applies

---

## Computing QBI

### Schedule C QBI (with §199A adjustments)

```
QBI = $30,000 (Schedule C Line 31)
    − $2,120 (½ SE tax)
    − $3,600 (SE health insurance)
    − $0 (SE retirement)
    = $24,280
```

---

## Filling out Form 8995

### Header

- Name: Priya Patel
- SSN: XXX-XX-9999

### Lines 1a-1e

| (i) Trade/business | (ii) TIN | (iii) QBI |
|--------------------|----------|-----------|
| Patel Consulting | XXX-XX-9999 (Priya's SSN) | $24,280 |

### Lines 2-4

- Line 2: $24,280
- Line 3: -$3,000 (prior-year QBI loss carryforward)
- Line 4: $24,280 − $3,000 = $21,280

### Lines 5-9

- Line 5: $250 (REIT Section 199A dividends from 1099-DIV Box 5)
- Line 6: $0 (no REIT/PTP carryforward)
- Line 7: $250

### Lines 10-12

- Line 10: $21,280 × 0.20 = $4,256
- Line 11: $250 × 0.20 = $50
- Line 12: $4,256 + $50 = $4,306

### Lines 13-17

- Line 13: $9,680 (taxable income before QBI)
- Line 14: $300 (qualified dividends from 1099-DIV Box 1b; no LTCG)
- Line 15: $9,680 − $300 = $9,380
- Line 16: $9,380 × 0.20 = $1,876
- Line 17: lesser of $4,306 or $1,876 = **$1,876**

---

## Result

Priya's QBI deduction is **$1,876**. This flows to Form 1040 Line 13.

**Limiting factor:** Taxable income limit (Line 16). Her actual QBI + REIT could have produced a $4,306 deduction, but her taxable income is too low to support it.

---

## Updated Form 1040

- AGI: $24,680
- Standard deduction: $15,000
- QBI deduction: $1,876
- **Taxable income: $7,804**
- Federal income tax (2025 single brackets): 10% × $7,804 = $780
- SE tax: $4,239
- Total federal tax: $5,019

---

## Carryforward tracking

For Priya's 2026 filing, the agent must track:

- **QBI loss carryforward from 2023 was -$3,000.** This year Priya used the entire $3,000 (Line 4 = $21,280 = $24,280 − $3,000, both positive). **No carryforward to 2026.**
- **REIT/PTP carryforward: $0** (Line 7 was positive).
- **Unused §199A deduction is NOT a carryforward.** The $4,306 − $1,876 = $2,430 difference between Line 12 and the binding Line 16 is forfeited. §199A taxable income limit is hard-capped per year — it doesn't carry.

The agent should surface this in workpapers: "Used full $3,000 prior-year QBI loss this year. No carryforward to 2026. Note: $2,430 of potential deduction was lost to taxable income limit and does not carry."

---

## Insights for the agent

### REIT dividends are small but real

$250 in Box 5 produces $50 of additional Line 11 deduction. Don't skip Line 5 just because the dollar amount is small.

### Qualified dividends from regular stocks subtract twice — confirm with user

Priya's $300 in qualified dividends (Line 1b of 1099-DIV) appears in Form 1040 Line 3a. They reduce Line 15 of Form 8995 (subtracting net capital gain). They are NOT §199A dividends — those are only the Box 5 amounts.

### Carryforward consumed = good, but document it

When the carryforward is consumed in a current year, document this clearly. Otherwise next year's filer (or agent) might mistakenly carry it forward again, double-counting.

### Schedule C consultant with no SEP

Priya didn't make a SEP-IRA contribution this year. That means her QBI is higher than it would be if she had — but her taxable income is also higher (no Schedule 1 Line 16 deduction). Below the threshold, this is approximately a wash for §199A purposes.

---

## Validation summary

- Math: all checks passed ✓
- Threshold: $9,680 well below $241,950 single threshold ✓
- Sanity:
  - Line 17 = Line 16 (taxable income limit binding) — surfaced
  - Carryforward fully consumed — note in workpapers
  - REIT dividends from Box 5 (not Box 1a) confirmed ✓
  - QBI = 80.9% of Schedule C net profit — within expected range ✓
- Carryforwards: None for 2026 (loss carryforward fully used)
- Next steps:
  - Form 8995 attaches to Form 1040
  - Line 17 ($1,876) → Form 1040 Line 13
  - Schedule SE flows separately
  - File by April 15, 2026
