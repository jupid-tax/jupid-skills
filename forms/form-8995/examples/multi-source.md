# Example — Multi-Source QBI with REIT Dividends and Prior-Year Loss Carryforward

## Persona

**Priya Patel**, 38, single, lives in Denver, CO. Priya runs "Patel Consulting" as a sole proprietor (Schedule C) — strategy consulting for nonprofits. She also holds a small position in a real estate investment trust through her brokerage account, and she had a Schedule C loss in 2024 that generated a QBI loss carryforward.

For tax year 2025:
- Schedule C (Patel Consulting): $30,000 net profit
- 1099-DIV from Schwab (REIT ETF): Box 5 Section 199A dividends $250
- Prior-year QBI loss carryforward (from 2024 Form 8995 Line 16): -$3,000
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
- Box 1b (qualified dividends): $150
- **Box 5 (Section 199A dividends): $250** (Box 1b and Box 5 are separate parts of Box 1a: a qualified REIT dividend is never a qualified dividend)
- Priya held the fund shares all year, so the 45-day holding period is met

### Form 1040 (computed pre-QBI)

- Total income: $30,000 (Schedule C) + $400 (ordinary div) + $0 (other) = $30,400
- Adjustments to income: $5,720
- **AGI (Line 11a): $24,680**
- Standard deduction (single, 2025, line 12e): $15,750
- Schedule 1-A deductions (line 13b): $0
- **Taxable income before QBI: $8,930**

(Note: this is unusually low taxable income for the example, but plausible for a consultant rebuilding their practice.)

---

## Threshold check

- 2025 single threshold: $197,300
- Priya's taxable income before QBI: $8,930
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

### Line 1, rows i–v

| (a) Trade/business | (b) TIN | (c) QBI |
|--------------------|----------|-----------|
| Patel Consulting | XXX-XX-9999 (Priya's SSN) | $24,280 |

### Lines 2-5

- Line 2: $24,280
- Line 3: ($3,000) (prior-year QBI loss carryforward)
- Line 4: $24,280 − $3,000 = $21,280
- Line 5: $21,280 × 0.20 = $4,256

### Lines 6-9

- Line 6: $250 (REIT Section 199A dividends from 1099-DIV Box 5)
- Line 7: $0 (no REIT/PTP carryforward)
- Line 8: $250
- Line 9: $250 × 0.20 = $50

### Lines 10-17

- Line 10: $4,256 + $50 = $4,306
- Line 11: $8,930 (taxable income before QBI)
- Line 12: $150 (qualified dividends from 1099-DIV Box 1b; no net capital gain)
- Line 13: $8,930 − $150 = $8,780
- Line 14: $8,780 × 0.20 = $1,756
- Line 15: smaller of $4,306 or $1,756 = **$1,756**
- Line 16: $0 (lines 2 + 3 = $21,280, positive)
- Line 17: $0

---

## Result

Priya's QBI deduction is **$1,756**. This flows to Form 1040 line 13a.

**Limiting factor:** Taxable income limit (Line 14). Her actual QBI + REIT could have produced a $4,306 deduction, but her taxable income is too low to support it.

---

## Updated Form 1040

- AGI: $24,680
- Standard deduction: $15,750
- QBI deduction: $1,756
- **Taxable income: $7,174**
- Federal income tax (Qualified Dividends and Capital Gain Tax Worksheet): $150 of qualified dividends at 0%; tax on the remaining $7,024 from the 2025 Tax Table ($7,000–$7,050, single) = $703
- SE tax: $4,239
- Total federal tax: $4,942

---

## Carryforward tracking

For Priya's 2026 filing, the agent must track:

- **QBI loss carryforward from 2024 was -$3,000.** This year Priya used the entire $3,000 (Line 4 = $21,280 = $24,280 − $3,000, both positive). **No carryforward to 2026.**
- **REIT/PTP carryforward: $0** (Line 17 = $0; lines 6 + 7 were positive).
- **Unused §199A deduction is NOT a carryforward.** The $4,306 − $1,756 = $2,550 difference between Line 10 and the binding Line 14 is forfeited. §199A taxable income limit is hard-capped per year — it doesn't carry.

The agent should surface this in workpapers: "Used full $3,000 prior-year QBI loss this year. No carryforward to 2026. Note: $2,550 of potential deduction was lost to taxable income limit and does not carry."

---

## Insights for the agent

### REIT dividends are small but real

$250 in Box 5 produces $50 of additional Line 9 deduction. Don't skip Line 6 just because the dollar amount is small.

### Qualified dividends from regular stocks subtract twice — confirm with user

Priya's $150 in qualified dividends (Box 1b of 1099-DIV) appears in Form 1040 line 3a. They go on Line 12 of Form 8995 and reduce Line 13. They are NOT §199A dividends — those are only the Box 5 amounts.

### Carryforward consumed = good, but document it

When the carryforward is consumed in a current year, document this clearly. Otherwise next year's filer (or agent) might mistakenly carry it forward again, double-counting.

### Schedule C consultant with no SEP

Priya didn't make a SEP-IRA contribution this year. That means her QBI is higher than it would be if she had — but her taxable income is also higher (no Schedule 1 Line 16 deduction). Below the threshold, this is approximately a wash for §199A purposes.

---

## Validation summary

- Math: all checks passed ✓
- Threshold: $8,930 well below $197,300 single threshold ✓
- Sanity:
  - Line 15 = Line 14 (taxable income limit binding) — surfaced
  - Carryforward fully consumed — note in workpapers
  - REIT dividends from Box 5 (not Box 1a) confirmed ✓
  - QBI = 80.9% of Schedule C net profit — within expected range ✓
- Carryforwards: None for 2026 (loss carryforward fully used)
- Next steps:
  - Form 8995 attaches to Form 1040
  - Line 15 ($1,756) → Form 1040 line 13a
  - Schedule SE flows separately
  - File by April 15, 2026
