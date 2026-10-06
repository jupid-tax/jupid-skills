# Example: Day Trader with Stocks and Crypto — Sam (Schedule D)

This is the same Sam from [`forms/form-8949/examples/day-trader-with-stocks-and-crypto.md`](../../form-8949/examples/day-trader-with-stocks-and-crypto.md). Form 8949 produced the per-transaction detail; Schedule D rolls those totals up.

---

## Filer profile

- **Name:** Sam ___
- **Filing status:** Single
- **Tax year:** 2025
- **Other income:** $190,000 W-2 wages (the same $190,000 as the Form 8949 example; no interest)
- **Standard deduction:** $15,750 (single, 2025; 2025 Instructions for Form 1040, "Standard deduction amount increased")
- **Other capital activity:** None besides Form 8949 entries below
- **Qualified dividends:** $1,500 (1099-DIV Box 1b from index funds)
- **Capital gain distributions (1099-DIV Box 2a):** $0
- **Prior-year capital loss carryover:** $0

## Form 8949 inputs (from companion example)

Sam's four primary 8949 entries from the Form 8949 example (same amounts), plus one additional NVDA short-term loss and the $1,500 of qualified dividends above, added for this Schedule D walkthrough:

| Form 8949 Box | Description | Holding | Net (h) |
|---------------|-------------|---------|---------|
| Box B | NVDA wash sale — disallowed loss | ST | $0 |
| Box H | ETH loss (Coinbase 2025 Form 1099-DA, basis not reported) | ST | ($1,200) |
| Box C | NVDA flip (no wash, separate sale) | ST | ($2,000) |
| Box D | AAPL gain | LT | $15,000 |
| Box K | BTC gain (Coinbase 2025 Form 1099-DA, basis not reported) | LT | $15,000 |

The crypto rows sit in the 2025 digital-asset boxes H and K, not C and F (Instructions for Form 8949 (2025), p. 3). On Schedule D, Box H shares Line 2 with Box B and Box K shares Line 9 with Box E.

---

## Schedule D walkthrough

### Part I — Short-Term

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 1a | 1099-B / 1099-DA aggregate | — | — | — | $0 |
| 1b | Box A + Box G 8949 | $0 | $0 | $0 | $0 |
| 2 | Box B + Box H 8949 (NVDA wash + ETH) | $9,550 | $11,750 | $1,000 | ($1,200) |
| 3 | Box C + Box I 8949 (NVDA flip) | $3,500 | $5,500 | $0 | ($2,000) |
| 4 | Forms 6252/6781/8824 ST | — | — | — | $0 |
| 5 | K-1 ST | — | — | — | $0 |
| 6 | Prior-year ST carryover | — | — | — | $0 |
| **7** | **Net short-term** | — | — | — | **($3,200)** |

### Part II — Long-Term

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 8a | 1099-B / 1099-DA aggregate | — | — | — | $0 |
| 8b | Box D + Box J 8949 | $23,000 | $8,000 | $0 | $15,000 |
| 9 | Box E + Box K 8949 (BTC) | $40,000 | $25,000 | $0 | $15,000 |
| 10 | Box F + Box L 8949 | $0 | $0 | $0 | $0 |
| 11 | Forms 4797/6252/6781/8824 LT | — | — | — | $0 |
| 12 | K-1 LT | — | — | — | $0 |
| 13 | 1099-DIV Box 2a | — | — | — | $0 |
| 14 | Prior-year LT carryover | — | — | — | $0 |
| **15** | **Net long-term** | — | — | — | **$30,000** |

### Part III — Summary

| Line | Calculation | Amount |
|------|-------------|--------|
| 16 | Line 7 + Line 15 = ($3,200) + $30,000 | **$26,800** |
| 17 | Both Lines 15 and 16 are gains? | Yes |
| 18 | 28% Rate Gain Worksheet (collectibles, §1202) | $0 |
| 19 | Unrecaptured §1250 Gain Worksheet | $0 |
| 20 | Lines 18 and 19 both zero → Qualified Dividends and Capital Gain Tax Worksheet | Yes |
| 21 | Capital loss limitation | N/A (Line 16 is positive) |

→ Form 1040 Line 7: **$26,800** (long-term character carries through)

---

## Tax-rate computation — Qualified Dividends and Capital Gain Tax Worksheet

Sam's taxable income = $190,000 (wages) + $26,800 (Schedule D Line 16) + $1,500 (qualified dividends) − $15,750 (standard deduction) = **$202,550**.

The Qualified Dividends and Capital Gain Tax Worksheet computes:

```
Step 1: Taxable income (Form 1040 Line 15):              $202,550
Step 2: Net capital gain + qualified dividends:           $28,300
        (smaller of Schedule D Line 15 $30,000 or Line 16 $26,800,
         plus $1,500 qualified dividends)
Step 3: Ordinary base = Step 1 − Step 2:                 $174,250
Step 4: Regular tax on $174,250 (2025 Tax Computation
        Worksheet, single: × 24% − $7,153):              $34,667

Step 5: LTCG layer — $28,300 stacked on top of $174,250:
   - Already past 0% bracket (cutoff $48,350)
   - Within 15% bracket (up to $533,400):
        $28,300 × 15% = $4,245
   - 20% bracket starts at $533,400 → not reached

Step 6: Total federal tax = $34,667 + $4,245 = $38,912
```

Compare to the wrong-worksheet path (regular tax on the full $202,550: × 32% − $22,937):
- Tax on $202,550 = $41,879
- Difference: $2,967 overpayment if Sam used the regular computation instead

---

## NIIT — Form 8960

Sam's MAGI = AGI = $218,300 (wages + capital activity + dividends, before standard deduction). MAGI exceeds the $200,000 single threshold.

```
Net Investment Income:
   Interest:                      $0
   Ordinary dividends:        $1,500
   Net capital gain:         $26,800  (Schedule D Line 16)
   Total NII:                $28,300

MAGI excess: $218,300 − $200,000 = $18,300

NIIT base = MIN($28,300, $18,300) = $18,300
NIIT = $18,300 × 3.8% = $695

→ Schedule 2 Line 12 → Form 1040 Line 23
```

---

## Total federal tax on capital activity

```
LTCG tax (from Qualified Dividends Worksheet):     $4,245
NIIT:                                                $695
Total federal tax attributable to capital gains:   $4,940
```

The $3,200 short-term loss was already absorbed inside Schedule D against the $30,000 long-term gain — it did *not* separately reduce ordinary income. (Net loss only reduces ordinary income at Line 21 if Line 16 is overall negative, which it isn't here.)

If Sam had been in California, additional state tax of approximately $26,800 × 9.3% = $2,492 would apply (CA does not use a preferential capital-gain rate).

---

## Carryover to next year

Both Lines 7 and 15 net out within the year (Line 7 negative, Line 15 positive, Line 16 positive). No carryover to next year.

---

## Validation checks

- [x] Line 7 = Line 2 (Box B + Box H) + Line 3 (Box C) + carryover = ($3,200)
- [x] Line 15 = Line 8b (Box D) + Line 9 (Box K) + carryover = $30,000
- [x] Line 16 = Line 7 + Line 15 = $26,800 (positive)
- [x] Line 17 = Yes (both 15 and 16 are gains)
- [x] Lines 18, 19 = $0 → Qualified Dividends and Capital Gain Tax Worksheet
- [x] MAGI > $200K single → Form 8960 required
- [x] All Form 8949 page totals reconciled to Schedule D lines

---

## Hand-off downstream

- [x] **Form 8949** — already complete, attached
- [x] **Form 8960** — NIIT computed, $695
- [ ] **Form 1040 Line 7** — enter $26,800
- [ ] **Form 1040 Line 16** — enter $38,912 from Qualified Dividends and Capital Gain Tax Worksheet
- [ ] **Schedule 2 Line 12** — enter $695 NIIT
- [x] **California state return** — capital gain taxed at ordinary rate; no preferential treatment

---

## Sources

- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [Form 1040 Instructions — Qualified Dividends and Capital Gain Tax Worksheet](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf)
- [Form 8960 — NIIT](https://www.irs.gov/pub/irs-pdf/f8960.pdf)
- IRC §1(h), §1411
- Rev. Proc. 2024-40 (2025 inflation-adjusted brackets); 2025 Instructions for Form 1040 (Tax Computation Worksheet, Section A; standard deduction $15,750 single)
