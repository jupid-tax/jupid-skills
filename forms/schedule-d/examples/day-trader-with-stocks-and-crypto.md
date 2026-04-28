# Example: Day Trader with Stocks and Crypto — Sam (Schedule D)

This is the same Sam from [`forms/form-8949/examples/day-trader-with-stocks-and-crypto.md`](../../form-8949/examples/day-trader-with-stocks-and-crypto.md). Form 8949 produced the per-transaction detail; Schedule D rolls those totals up.

---

## Filer profile

- **Name:** Sam ___
- **Filing status:** Single
- **Tax year:** 2025
- **Other income:** $200,000 W-2 wages
- **Standard deduction:** $15,000 (single, 2025)
- **Other capital activity:** None besides Form 8949 entries below
- **Qualified dividends:** $1,500 (1099-DIV Box 1b from index funds)
- **Capital gain distributions (1099-DIV Box 2a):** $0
- **Prior-year capital loss carryover:** $0

## Form 8949 inputs (from companion example)

Sam's four primary 8949 entries from the Form 8949 example, plus one additional NVDA short-term loss for this Schedule D walkthrough:

| Form 8949 Box | Description | Holding | Net (h) |
|---------------|-------------|---------|---------|
| Box B | NVDA wash sale — disallowed loss | ST | $0 |
| Box C | ETH loss | ST | ($1,200) |
| Box C | NVDA flip (no wash, separate sale) | ST | ($2,000) |
| Box D | AAPL gain | LT | $15,000 |
| Box F | BTC gain | LT | $7,500 |

---

## Schedule D walkthrough

### Part I — Short-Term

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 1a | Box A aggregate | — | — | — | $0 |
| 1b | Box A 8949 | $0 | $0 | $0 | $0 |
| 2 | Box B 8949 | $5,750 | $6,750 | $1,000 | $0 |
| 3 | Box C 8949 | $7,300 | $10,500 | $0 | ($3,200) |
| 4 | Forms 6252/6781/8824 ST | — | — | — | $0 |
| 5 | K-1 ST | — | — | — | $0 |
| 6 | Prior-year ST carryover | — | — | — | $0 |
| **7** | **Net short-term** | — | — | — | **($3,200)** |

### Part II — Long-Term

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 8a | Box D aggregate | — | — | — | $0 |
| 8b | Box D 8949 | $23,000 | $8,000 | $0 | $15,000 |
| 9 | Box E 8949 | $0 | $0 | $0 | $0 |
| 10 | Box F 8949 | $40,000 | $32,500 | $0 | $7,500 |
| 11 | Forms 4797/6252/6781/8824 LT | — | — | — | $0 |
| 12 | K-1 LT | — | — | — | $0 |
| 13 | 1099-DIV Box 2a | — | — | — | $0 |
| 14 | Prior-year LT carryover | — | — | — | $0 |
| **15** | **Net long-term** | — | — | — | **$22,500** |

### Part III — Summary

| Line | Calculation | Amount |
|------|-------------|--------|
| 16 | Line 7 + Line 15 = ($3,200) + $22,500 | **$19,300** |
| 17 | Both Lines 15 and 16 are gains? | Yes |
| 18 | 28% Rate Gain Worksheet (collectibles, §1202) | $0 |
| 19 | Unrecaptured §1250 Gain Worksheet | $0 |
| 20 | Lines 18 and 19 both zero → Qualified Dividends and Capital Gain Tax Worksheet | Yes |
| 21 | Capital loss limitation | N/A (Line 16 is positive) |

→ Form 1040 Line 7: **$19,300** (long-term character carries through)

---

## Tax-rate computation — Qualified Dividends and Capital Gain Tax Worksheet

Sam's taxable income = $200,000 (wages) + $19,300 (Schedule D Line 16) + $1,500 (qualified dividends) − $15,000 (standard deduction) = **$205,800**.

The Qualified Dividends and Capital Gain Tax Worksheet computes:

```
Step 1: Taxable income (Form 1040 Line 15):              $205,800
Step 2: LT gain + qualified dividends:                    $20,800
        (Schedule D Line 16 + qualified dividends)
Step 3: Ordinary base = Step 1 − Step 2:                 $185,000
Step 4: Regular tax on $185,000 (single, 2025 tables):    $35,750 (approx)

Step 5: LTCG layer — $20,800 stacked on top of $185,000:
   - Already past 0% bracket (cutoff $48,350)
   - Within 15% bracket ($48,351 – $533,400):
        $20,800 × 15% = $3,120
   - 20% bracket starts at $533,400 → not reached

Step 6: Total federal tax = $35,750 + $3,120 = $38,870
```

Compare to the wrong-worksheet path (regular tables on full $205,800):
- Tax on $205,800 ≈ $40,622
- Difference: ~$1,752 overpayment if Sam used the regular tables instead

---

## NIIT — Form 8960

Sam's MAGI = AGI = $221,300 (wages + capital activity + dividends, before standard deduction). MAGI exceeds the $200,000 single threshold.

```
Net Investment Income:
   Interest:                      $0
   Ordinary dividends:        $1,500
   Net capital gain:         $19,300  (Schedule D Line 16)
   Total NII:                $20,800

MAGI excess: $221,300 − $200,000 = $21,300

NIIT base = MIN($20,800, $21,300) = $20,800
NIIT = $20,800 × 3.8% = $791

→ Schedule 2 Line 12 → Form 1040 Line 23
```

---

## Total federal tax on capital activity

```
LTCG tax (from Qualified Dividends Worksheet):     $3,120
NIIT:                                                $791
Total federal tax attributable to capital gains:   $3,911
```

The $3,200 short-term loss was already absorbed inside Schedule D against the $22,500 long-term gain — it did *not* separately reduce ordinary income. (Net loss only reduces ordinary income at Line 21 if Line 16 is overall negative, which it isn't here.)

If Sam had been in California, additional state tax of approximately $19,300 × 9.3% = $1,795 would apply (CA does not use a preferential capital-gain rate).

---

## Carryover to next year

Both Lines 7 and 15 net out within the year (Line 7 negative, Line 15 positive, Line 16 positive). No carryover to next year.

---

## Validation checks

- [x] Line 7 = sum of Box B, C totals + carryover = ($3,200)
- [x] Line 15 = sum of Box D, F totals + carryover = $22,500
- [x] Line 16 = Line 7 + Line 15 = $19,300 (positive)
- [x] Line 17 = Yes (both 15 and 16 are gains)
- [x] Lines 18, 19 = $0 → Qualified Dividends and Capital Gain Tax Worksheet
- [x] MAGI > $200K single → Form 8960 required
- [x] All Form 8949 page totals reconciled to Schedule D lines

---

## Hand-off downstream

- [x] **Form 8949** — already complete, attached
- [x] **Form 8960** — NIIT computed, $791
- [ ] **Form 1040 Line 7** — enter $19,300
- [ ] **Form 1040 Line 16** — enter $38,870 from Qualified Dividends and Capital Gain Tax Worksheet
- [ ] **Schedule 2 Line 12** — enter $791 NIIT
- [x] **California state return** — capital gain taxed at ordinary rate; no preferential treatment

---

## Sources

- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [Form 1040 Instructions — Qualified Dividends and Capital Gain Tax Worksheet](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf)
- [Form 8960 — NIIT](https://www.irs.gov/pub/irs-pdf/f8960.pdf)
- IRC §1(h), §1411
- Rev. Proc. 2024-40 (2025 inflation-adjusted brackets)
