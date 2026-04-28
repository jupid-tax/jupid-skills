# Example: Big Loss Year with Carryover — Maya

A retail investor whose 2025 portfolio took a big hit and ends the year with a net capital loss exceeding the $3,000 deduction limit. Demonstrates the IRC §1211 cap, IRC §1212 carryforward, and the Capital Loss Carryover Worksheet.

---

## Filer profile

- **Name:** Maya ___
- **Filing status:** Single
- **Tax year:** 2025
- **Wages:** $95,000
- **Standard deduction:** $15,000 (single, 2025)
- **Qualified dividends:** $800
- **Capital gain distributions (1099-DIV Box 2a):** $0
- **Prior-year capital loss carryover:** $0 (first year with loss)

## 2025 transaction summary (already on Form 8949)

| Form 8949 Box | Description | Holding | Net (h) |
|---------------|-------------|---------|---------|
| Box A | TSLA — bought Mar 2025, sold Aug 2025 | ST | ($8,500) |
| Box A | NVDA — bought Apr 2025, sold Sept 2025 | ST | ($4,200) |
| Box C | SOL — held 8 months, sold at loss | ST | ($3,300) |
| Box D | AAPL — held 4 years, sold at gain | LT | $5,200 |
| Box F | BTC — held 2 years, sold at loss | LT | ($14,500) |

---

## Schedule D walkthrough

### Part I — Short-Term

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 1b | Box A 8949 (TSLA + NVDA) | $40,000 | $52,700 | $0 | ($12,700) |
| 2 | Box B 8949 | — | — | — | $0 |
| 3 | Box C 8949 (SOL) | $4,500 | $7,800 | $0 | ($3,300) |
| 4 | Forms 6252/6781/8824 ST | — | — | — | $0 |
| 5 | K-1 ST | — | — | — | $0 |
| 6 | Prior-year ST carryover | — | — | — | $0 |
| **7** | **Net short-term** | — | — | — | **($16,000)** |

### Part II — Long-Term

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 8b | Box D 8949 (AAPL) | $12,000 | $6,800 | $0 | $5,200 |
| 9 | Box E 8949 | — | — | — | $0 |
| 10 | Box F 8949 (BTC) | $25,000 | $39,500 | $0 | ($14,500) |
| 11 | Forms 4797/6252/6781/8824 LT | — | — | — | $0 |
| 12 | K-1 LT | — | — | — | $0 |
| 13 | 1099-DIV Box 2a | — | — | — | $0 |
| 14 | Prior-year LT carryover | — | — | — | $0 |
| **15** | **Net long-term** | — | — | — | **($9,300)** |

### Part III — Summary

| Line | Calculation | Amount |
|------|-------------|--------|
| 16 | Line 7 + Line 15 = ($16,000) + ($9,300) | **($25,300)** |
| 17 | Both Lines 15 and 16 are gains? | No (loss) → skip to Line 21 |
| 18 | 28% Rate Gain Worksheet | N/A |
| 19 | Unrecaptured §1250 Gain Worksheet | N/A |
| 21 | Capital loss limitation: smaller of $25,300 or $3,000 | **($3,000)** |
| 22 | Has qualified dividends → use Qualified Dividends and Capital Gain Tax Worksheet for the dividend portion | Yes |

→ Form 1040 Line 7: **($3,000)** (loss limited; reduces ordinary income)

---

## Capital Loss Carryover Worksheet (for use next year)

The worksheet (in Schedule D instructions) takes 2025's information and computes how much carries forward to 2026, broken down by character.

**Step 1:** Total loss available to carry over.
```
Total 2025 capital loss (|Line 16|):     $25,300
Amount used in 2025 (Line 21):            $3,000
Total carryover to 2026:                 $22,300
```

**Step 2:** Allocate by character.

The order of absorption: short-term loss first absorbs the $3,000 ordinary-income deduction; remaining short-term offsets long-term gain (it already did within the year). So the $3,000 used in 2025 came out of short-term.

```
Net short-term loss in 2025:           ($16,000)
Less amount used against ordinary:      $3,000
Short-term carryforward to 2026:      ($13,000)

Net long-term loss in 2025:             ($9,300)
Less amount used:                            $0
Long-term carryforward to 2026:        ($9,300)

Total carryforward verify: $13,000 + $9,300 = $22,300 ✓
```

**Saved for 2026 Schedule D:**
- Line 6: ($13,000) short-term carryforward
- Line 14: ($9,300) long-term carryforward

---

## Tax computation

Maya's taxable income:
```
Wages:                          $95,000
Capital loss (Line 21):         ($3,000)
Qualified dividends:                $800
Other income:                        $0
AGI:                            $92,800
Standard deduction:            ($15,000)
Taxable income:                 $77,800
```

Because Schedule D Line 16 is a loss, no preferential capital gain rate applies on Schedule D activity. But Maya has $800 of qualified dividends, which still get preferential treatment.

**Qualified Dividends and Capital Gain Tax Worksheet:**

```
Step 1: Taxable income:              $77,800
Step 2: Qualified dividends:            $800 (LT gain is zero on Line 15 in this case for QD&CG calc)

   Note: For the worksheet, only the Line 13 capital gain distributions
   and qualified dividends matter when Line 16 is a loss. Net LT loss
   does not produce a preferential layer.

Step 3: Ordinary base = $77,800 − $800 = $77,000
Step 4: Tax on $77,000 (single 2025 tables):     $12,150 (approx)

Step 5: Preferential layer — $800 stacked on top:
   Within 15% LTCG bracket (taxable income $77,000–$77,800 well under $533,400):
   $800 × 15% = $120

Step 6: Total federal tax = $12,150 + $120 = $12,270
```

**NIIT — Form 8960:** MAGI $92,800 well below the $200,000 single threshold. No NIIT.

---

## Validation checks

- [x] Line 7 = ($16,000) (Box A + Box C totals)
- [x] Line 15 = ($9,300) (Box D + Box F totals)
- [x] Line 16 = Line 7 + Line 15 = ($25,300)
- [x] Line 16 < 0 → Line 21 applies
- [x] Line 21 = MIN(|$25,300|, $3,000) = ($3,000) — single filer
- [x] Capital Loss Carryover Worksheet built; ST $13,000 + LT $9,300 = $22,300 = total minus used
- [x] No NIIT exposure (MAGI under threshold)

---

## What Maya should know going forward

1. **The $22,300 carryforward is real money.** If Maya realizes a $20,000 gain in 2027, the carryforward will fully offset it (saving $3,000 to $4,000 in tax depending on bracket and character).

2. **Character matters.** Short-term carryforward of $13,000 first offsets future short-term gains. Long-term carryforward of $9,300 first offsets future long-term gains. Tax planning to harvest the right kind of gain in future years can extract more value.

3. **Don't lose the worksheet.** The Capital Loss Carryover Worksheet must be saved with this year's records and entered on next year's Schedule D Lines 6 and 14. Tax software typically tracks this automatically; manual filers must be diligent.

4. **State carryover may differ.** If Maya is in New Jersey, the $22,300 has zero state value (NJ doesn't allow capital loss carryforward). California allows it but with state-specific AGI rules.

---

## Hand-off downstream

- [x] **Form 8949** — all entries reported, all boxes used as appropriate
- [ ] **Form 1040 Line 7** — enter ($3,000) [from Line 21]
- [ ] **Form 1040 Line 16** — enter $12,270 from Qualified Dividends and Capital Gain Tax Worksheet
- [x] **Capital Loss Carryover Worksheet** — saved for 2026 use
- [x] **No Form 8960** — MAGI below threshold
- [x] **State return** — flag NJ-style restrictions if applicable

---

## Sources

- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — contains Capital Loss Carryover Worksheet
- IRC §1211(b) (loss limit), §1212(b) (carryforward indefinite)
- Rev. Proc. 2024-40 (2025 brackets)
