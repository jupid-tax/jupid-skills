# Example: Day Trader with Stocks and Crypto (Sam from the blog)

A complete walkthrough of Form 8949 for a filer with a mix of long-term equity gains, long-term crypto, a short-term wash sale, and a short-term crypto loss. This is the canonical "active retail filer" pattern — four transactions across four boxes.

## The filer

- **Name**: Sam Reyes
- **Filing status**: Single
- **2025 ordinary income (W-2 + interest)**: $190,000 → 32% federal marginal bracket
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Brokerage and exchange accounts

| Source | Form | Box implication |
|--------|------|------------------|
| Schwab | 1099-B | A or D (covered) |
| TD Ameritrade (transferred to Schwab mid-year) | 1099-B | B or E (basis not reported on transferred-in NVDA lot) |
| Coinbase | 1099-MISC + CSV | C or F (no 1099-B issued for asset sales) |

### Transactions

| # | Asset | Acquired | Sold | Proceeds | Basis | Notes |
|---|-------|----------|------|----------|-------|-------|
| 1 | 100 sh AAPL | 2020-03-15 | 2025-08-12 | $23,000 | $8,000 | Held > 5 yrs → long-term. Schwab 1099-B with basis reported. |
| 2 | 0.5 BTC | 2024-01-10 | 2025-09-22 | $40,000 | $25,000 | Held 1 yr 8 mo → long-term. Coinbase, no 1099-B. |
| 3 | 50 sh NVDA | 2025-09-15 | 2025-10-20 | $5,750 | $6,750 | Held 35 days → short-term, $1,000 loss. Transferred-in lot, basis not on 1099-B. Wash sale: bought 50 sh NVDA on 2025-11-05 at $130. |
| 4 | Various ETH | Apr–Jul 2025 (VARIOUS) | 2025-11-30 | $3,800 | $5,000 | All short-term lots. Coinbase, no 1099-B. |

## Step 3 — Box classification

| # | Holding period | Basis on 1099-B? | 1099-B issued? | Box |
|---|---------------|------------------|-----------------|-----|
| 1 AAPL | Long-term | Yes | Yes | **D** |
| 2 BTC | Long-term | n/a | No | **F** |
| 3 NVDA | Short-term | No (transferred-in) | Yes (without basis) | **B** |
| 4 ETH | Short-term | n/a | No | **C** |

Four different boxes — the agent will produce four 8949 pages.

## Step 4 — Wash sale check

For every loss transaction, check the 61-day window:

- **Transaction 3 (NVDA, $1,000 loss on Oct 20)**: bought 50 sh NVDA on Nov 5, 2025 — that's 16 days after the sale, well within 30 days. **Wash sale triggered.**
  - Code "W" in column (f)
  - $1,000 disallowed in column (g)
  - The Nov 5 lot's adjusted basis: $130 × 50 + $1,000 = $7,500
  - Holding period of the Nov 5 lot tacks back to Sept 15, 2025 (the original buy date)
- **Transaction 4 (ETH, $1,200 loss on Nov 30)**: §1091 does not currently apply to crypto (as of tax year 2025). No wash sale code. Loss fully allowed.
- Sam confirms he didn't buy AAPL or BTC anywhere in the 61-day windows around their gain transactions (gains aren't subject to §1091 anyway, but the agent confirms for completeness).

## Step 5 — Other adjustment codes

None apply. Sam is not selling collectibles, QSBS, or §1244 stock. Sam doesn't have a §121 home sale. No nominee 1099-Bs.

## Step 6 — Per-row gain/loss

For each row: (h) = (d) − (e) + (g)

| # | (d) | (e) | (g) | (h) |
|---|-----|-----|-----|-----|
| 1 AAPL | $23,000 | $8,000 | $0 | $15,000 |
| 2 BTC | $40,000 | $25,000 | $0 | $15,000 |
| 3 NVDA | $5,750 | $6,750 | $1,000 | $0 |
| 4 ETH | $3,800 | $5,000 | $0 | ($1,200) |

## The completed Form 8949 draft

```markdown
# Form 8949 — DRAFT for tax year 2025

## Filer
Name: Sam Reyes
SSN: XXX-XX-XXXX

## Part I — Short-Term Capital Gains and Losses

### Box A — basis reported to IRS on 1099-B
(no entries)

### Box B — basis NOT reported to IRS on 1099-B
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 50 sh NVDA | 09/15/25 | 10/20/25 | $5,750 | $6,750 | W | $1,000 | $0 |
| **Box B totals** | | | $5,750 | $6,750 | | $1,000 | $0 |

### Box C — no 1099-B received
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| Various ETH | VARIOUS | 11/30/25 | $3,800 | $5,000 | (none) | $0 | ($1,200) |
| **Box C totals** | | | $3,800 | $5,000 | | $0 | ($1,200) |

## Part II — Long-Term Capital Gains and Losses

### Box D — basis reported to IRS on 1099-B
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 100 sh AAPL | 03/15/20 | 08/12/25 | $23,000 | $8,000 | (none) | $0 | $15,000 |
| **Box D totals** | | | $23,000 | $8,000 | | $0 | $15,000 |

### Box E — basis NOT reported to IRS on 1099-B
(no entries)

### Box F — no 1099-B received
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 0.5 BTC | 01/10/24 | 09/22/25 | $40,000 | $25,000 | (none) | $0 | $15,000 |
| **Box F totals** | | | $40,000 | $25,000 | | $0 | $15,000 |

## Roll-up to Schedule D

| Schedule D Line | Source | Amount |
|-----------------|--------|--------|
| 1b — Box A net | (none) | $0 |
| 2  — Box B net | NVDA wash sale | $0 |
| 3  — Box C net | ETH short loss | ($1,200) |
| 7  — Net short-term capital gain/(loss) | | ($1,200) |
| 8b — Box D net | AAPL long-term | $15,000 |
| 9  — Box E net | (none) | $0 |
| 10 — Box F net | BTC long-term | $15,000 |
| 15 — Net long-term capital gain | | $30,000 |
| 16 — Total = Line 7 + Line 15 → Form 1040 Line 7 | | $28,800 |

## Wash sale tracking (carry to next year)
| Replacement lot | Original disallowed loss | New basis adjustment |
|-----------------|--------------------------|----------------------|
| 50 sh NVDA acquired 11/05/2025 at $130 | $1,000 (from 10/20/2025 sale) | New basis: $7,500 (was $6,500) |

## Capital loss carryover
Net loss does not exceed $3,000. Short-term loss of $1,200 absorbs into the $30,000 long-term gain at the Schedule D Line 16 level. No carryforward.

## Required attachments and downstream forms
- [ ] Schedule D (mandatory)
- [ ] Form 8960 (NIIT) — Sam's MAGI ≈ $218,800 ($190K W-2 + $28,800 net cap gain) — exceeds $200K single threshold
- [ ] Form 6781 — N/A (no §1256 contracts)
- [ ] Form 8824 — N/A (no §1031 exchange)

## Validation summary
- Math: all rows verified, (h) = (d) − (e) + (g)
- Box totals match row sums
- Wash sale on NVDA properly coded with W
- Crypto wash sale not triggered (§1091 doesn't apply to crypto in 2025; verified)
- Long-term holding periods confirmed (AAPL 5 yrs, BTC 1.7 yrs)
- ETH "Various" aggregation is acceptable (all short-term)
- Form 1040 digital asset question: Yes (BTC and ETH disposals)

## Sources cited in this draft
- IRS Form 8949 (rev. 2025)
- IRS Instructions for Form 8949 (2025)
- IRC §1001, §1(h), §1091, §1211, §1411
- Notice 2014-21 (crypto as property)
- Rev. Proc. 2024-40 (2025 LTCG brackets)
```

## Step 10 — Hand off

The agent tells Sam:

> Your 8949 totals roll into Schedule D Line 16 = $28,800 (net capital gain), which carries to Form 1040 Line 7. Tax math:
> - $30,000 long-term gain at the 15% LTCG rate = **$4,500**
> - $1,200 short-term loss already netted in Line 16
> - Effective LTCG tax: ~$4,320 ($28,800 × 15%)
> - Plus **NIIT 3.8%** on net investment income (estimate $28,800 × 3.8% = **$1,094**) — Form 8960
> - Total federal capital gains and NIIT: ~**$5,414**
>
> Save the wash sale tracking — when you sell that NVDA replacement lot in 2026 or later, your basis is $7,500, not $6,500.
>
> Don't forget Form 8960 in your return package. Most software handles this automatically when MAGI exceeds the threshold.

## Step 11 — File

Sam confirms he wants to e-file via FFFF. Agent proceeds with `filing.md` Section 1 — five forms total: 1040, Schedule D, four 8949 pages (Boxes B, C, D, F), and Form 8960.
