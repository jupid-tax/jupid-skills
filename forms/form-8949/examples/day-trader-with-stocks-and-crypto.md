# Example: Day Trader with Stocks and Crypto (Sam from the blog)

A complete walkthrough of Form 8949 for a filer with a mix of long-term equity gains, long-term crypto, a short-term wash sale, and a short-term crypto loss. This is the canonical "active retail filer" pattern — four transactions across four boxes, two of them the digital-asset boxes added on the 2025 Form 8949.

## The filer

- **Name**: Sam Reyes
- **Filing status**: Single
- **2025 ordinary income (W-2 wages, no interest)**: $190,000 → $174,250 taxable after the $15,750 single standard deduction → 24% federal marginal bracket (2025 Instructions for Form 1040: standard deduction; Tax Computation Worksheet, Section A)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Brokerage and exchange accounts

| Source | Form | Box implication |
|--------|------|------------------|
| Schwab | 1099-B | A or D (covered) |
| TD Ameritrade (transferred to Schwab mid-year) | 1099-B | B or E (basis not reported on transferred-in NVDA lot) |
| Coinbase | 2025 Form 1099-DA (gross proceeds only; box 2 not checked; code Y) + 1099-MISC + CSV | H or K (digital asset on a 1099-DA, basis not reported) |

### Transactions

| # | Asset | Acquired | Sold | Proceeds | Basis | Notes |
|---|-------|----------|------|----------|-------|-------|
| 1 | 100 sh AAPL | 2020-03-15 | 2025-08-12 | $23,000 | $8,000 | Held > 5 yrs → long-term. Schwab 1099-B with basis reported. |
| 2 | 0.5 BTC | 2024-01-10 | 2025-09-22 | $40,000 | $25,000 | Held 1 yr 8 mo → long-term. Coinbase 1099-DA: box 1f $40,000, box 1g blank. Basis from Sam's Coinbase CSV. |
| 3 | 50 sh NVDA | 2025-09-15 | 2025-10-20 | $5,750 | $6,750 | Held 35 days → short-term, $1,000 loss. Transferred-in lot, basis not on 1099-B. Wash sale: bought 50 sh NVDA on 2025-11-05 at $130. |
| 4 | Various ETH | Apr–Jul 2025 (VARIOUS) | 2025-11-30 | $3,800 | $5,000 | All short-term lots. Coinbase 1099-DA: box 1f $3,800, box 1g blank. Basis from Sam's Coinbase CSV. |

## Step 3 — Box classification

| # | Holding period | Form received | Basis reported to IRS? | Box |
|---|---------------|---------------|------------------------|-----|
| 1 AAPL | Long-term | 1099-B | Yes | **D** |
| 2 BTC | Long-term | 1099-DA | No (box 2 not checked) | **K** |
| 3 NVDA | Short-term | 1099-B | No (transferred-in) | **B** |
| 4 ETH | Short-term | 1099-DA | No (box 2 not checked) | **H** |

Four different boxes — the agent will produce four 8949 pages. The 1099-DA shows code Y (holding period unknown to the broker), so the agent dates both crypto sales from Sam's CSV lots. Box F and Box C are not options for the crypto: the 2025 instructions bar digital assets from them (Instructions for Form 8949 (2025), p. 3).

## Step 4 — Wash sale check

For every loss transaction, check the 61-day window:

- **Transaction 3 (NVDA, $1,000 loss on Oct 20)**: bought 50 sh NVDA on Nov 5, 2025 — that's 16 days after the sale, well within 30 days. **Wash sale triggered.**
  - Code "W" in column (f)
  - $1,000 disallowed in column (g)
  - The Nov 5 lot's adjusted basis: $130 × 50 + $1,000 = $7,500
  - Holding period of the Nov 5 lot tacks back to Sept 15, 2025 (the original buy date)
- **Transaction 4 (ETH, $1,200 loss on Nov 30)**: §1091 does not currently apply to crypto (as of tax year 2025; ETH is not a tokenized security). No wash sale code. Loss fully allowed.
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

### Box C — no 1099-B or 1099-DA received (not a digital asset)
(no entries)

### Box H — digital assets, basis NOT reported to IRS on 1099-DA
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| Various ETH | VARIOUS | 11/30/25 | $3,800 | $5,000 | (none) | $0 | ($1,200) |
| **Box H totals** | | | $3,800 | $5,000 | | $0 | ($1,200) |

## Part II — Long-Term Capital Gains and Losses

### Box D — basis reported to IRS on 1099-B
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 100 sh AAPL | 03/15/20 | 08/12/25 | $23,000 | $8,000 | (none) | $0 | $15,000 |
| **Box D totals** | | | $23,000 | $8,000 | | $0 | $15,000 |

### Box E — basis NOT reported to IRS on 1099-B
(no entries)

### Box F — no 1099-B or 1099-DA received (not a digital asset)
(no entries)

### Box K — digital assets, basis NOT reported to IRS on 1099-DA
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 0.5 BTC | 01/10/24 | 09/22/25 | $40,000 | $25,000 | (none) | $0 | $15,000 |
| **Box K totals** | | | $40,000 | $25,000 | | $0 | $15,000 |

## Roll-up to Schedule D

| Schedule D Line | Source | Amount |
|-----------------|--------|--------|
| 1b — Box A + Box G net | (none) | $0 |
| 2  — Box B + Box H net | NVDA wash sale $0 + ETH short loss ($1,200) | ($1,200) |
| 3  — Box C + Box I net | (none) | $0 |
| 7  — Net short-term capital gain/(loss) | | ($1,200) |
| 8b — Box D + Box J net | AAPL long-term | $15,000 |
| 9  — Box E + Box K net | BTC long-term | $15,000 |
| 10 — Box F + Box L net | (none) | $0 |
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
- Box H and Box K proceeds ($3,800 and $40,000) match Coinbase 1099-DA box 1f
- Long-term holding periods confirmed (AAPL 5 yrs, BTC 1.7 yrs)
- ETH "Various" aggregation is acceptable (all short-term)
- Form 1040 digital asset question: Yes (BTC and ETH disposals)

## Sources cited in this draft
- IRS Form 8949 (rev. 2025)
- IRS Instructions for Form 8949 (2025)
- IRS Instructions for Form 1099-DA (2025)
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
> - Plus **NIIT 3.8%** on the smaller of net investment income ($28,800) or MAGI over $200,000 ($218,800 − $200,000 = $18,800): $18,800 × 3.8% = **$714** — Form 8960
> - Total federal capital gains and NIIT: ~**$5,034**
>
> Save the wash sale tracking — when you sell that NVDA replacement lot in 2026 or later, your basis is $7,500, not $6,500.
>
> Don't forget Form 8960 in your return package. Most software handles this automatically when MAGI exceeds the threshold.

## Step 11 — File

Sam confirms he wants to e-file via FFFF. Agent proceeds with `filing.md` Section 1 — five forms total: 1040, Schedule D, four 8949 pages (Boxes B, H, D, K), and Form 8960.
