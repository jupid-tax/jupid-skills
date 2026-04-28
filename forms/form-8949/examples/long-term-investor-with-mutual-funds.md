# Example: Long-Term Investor with Mutual Funds (Retiree)

A retiree drawing down a long-held index fund position. This is the canonical "buy-and-hold" pattern — long-term gains, mostly Box D, with a sliver of Box E for very old shares acquired before the 2012 mutual fund cost-basis reporting cutoff.

## The filer

- **Name**: Patricia Wong
- **Filing status**: Married filing jointly
- **2025 ordinary income (Social Security taxable + pension + small Roth conversion)**: $80,000
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Brokerage accounts

| Source | Form | Box implication |
|--------|------|------------------|
| Vanguard | 1099-B | D for shares acquired after Jan 1, 2012; E for older shares |

Patricia owns one position: Vanguard Total Stock Market Index Fund Admiral Shares (VTSAX). She's been adding to it monthly via dollar-cost averaging since 2005, so her cost basis is spread across 240+ monthly buy lots. She uses **average cost** for the fund (default at Vanguard for most mutual fund holders).

### The sale

In 2025, Patricia sells 500 shares of VTSAX on August 18, 2025 to fund a kitchen remodel.

- Sale proceeds: 500 × $135 = **$67,500**
- Holding period: aggregated over 20 years of monthly buys → all long-term

Vanguard provides:

- 1099-B with the sale broken into two lines:
  - "Long-term, basis reported to IRS" — covered shares (acquired Jan 1, 2012 or later): 380 shares, average cost $80/share = $30,400 basis
  - "Long-term, basis NOT reported to IRS" — non-covered shares (acquired 2005–2011): 120 shares, average cost $42/share = $5,040 basis

Total proceeds $67,500 (380 × $135 = $51,300 covered + 120 × $135 = $16,200 non-covered)
Total basis $35,440
Total gain $32,060 — all long-term

## Step 3 — Box classification

| Lot group | Holding period | Basis on 1099-B? | Box |
|-----------|---------------|------------------|-----|
| 380 covered shares | Long-term | Yes | **D** |
| 120 non-covered shares | Long-term | No | **E** |

## Step 4 — Wash sale check

Patricia sold for cash to spend on a remodel. She's not buying VTSAX (or any substantially identical fund) within 30 days before or after. No wash sale.

If she had reinvested into another total-market fund (e.g., FZROX or SWTSX) within 30 days, the agent would surface the wash sale question — those funds are arguably "substantially identical" though the IRS hasn't drawn a clear line. In this case it doesn't matter because the transaction was a gain, not a loss (§1091 only applies to losses).

## Step 5 — Other codes

None. No collectibles, no §121, no nominee.

## Step 6 — Per-row math

| Lot group | (d) | (e) | (g) | (h) |
|-----------|-----|-----|-----|-----|
| 380 sh VTSAX (covered) | $51,300 | $30,400 | $0 | $20,900 |
| 120 sh VTSAX (non-covered) | $16,200 | $5,040 | $0 | $11,160 |

## The completed Form 8949 draft

```markdown
# Form 8949 — DRAFT for tax year 2025

## Filer
Name: Patricia Wong (joint with spouse Robert Wong)
SSN: XXX-XX-XXXX (and spouse)

## Part I — Short-Term Capital Gains and Losses
(no entries)

## Part II — Long-Term Capital Gains and Losses

### Box D — basis reported to IRS on 1099-B
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 380 sh VTSAX | VARIOUS | 08/18/25 | $51,300 | $30,400 | (none) | $0 | $20,900 |
| **Box D totals** | | | $51,300 | $30,400 | | $0 | $20,900 |

### Box E — basis NOT reported to IRS on 1099-B
| (a) | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----|--------------|----------|--------------|-----------|----------|---------|---------------|
| 120 sh VTSAX | VARIOUS | 08/18/25 | $16,200 | $5,040 | (none) | $0 | $11,160 |
| **Box E totals** | | | $16,200 | $5,040 | | $0 | $11,160 |

### Box F — no 1099-B received
(no entries)

## Roll-up to Schedule D

| Schedule D Line | Source | Amount |
|-----------------|--------|--------|
| 7  — Net short-term | | $0 |
| 8b — Box D net | covered VTSAX | $20,900 |
| 9  — Box E net | non-covered VTSAX | $11,160 |
| 10 — Box F net | | $0 |
| 13 — Capital gain distributions (1099-DIV Box 2a) | Vanguard 1099-DIV | $1,800 |
| 15 — Net long-term capital gain | | $33,860 |
| 16 — Total = Line 7 + Line 15 → Form 1040 Line 7 | | $33,860 |
```

(Line 13 picks up Vanguard's year-end capital gain distribution from the fund itself, which is a separate item from the share sale.)

## What Patricia owes

```
Total taxable income (joint) ≈ $80,000 ordinary + $33,860 LT cap gain = $113,860 (before standard deduction)
Less 2025 MFJ standard deduction: $30,000 (estimate)
Taxable income: $83,860

LTCG bracket math (2025 MFJ):
  0% bracket: up to $96,700
  15% bracket: $96,701 – $600,050

Patricia's $33,860 LT cap gain stacks on top of her ordinary income for bracket determination.
Ordinary taxable income: $50,000
Capital gain stacked on top: $33,860 → falls within $50,000 to $83,860
Both ordinary income and capital gain are below $96,700 → most of the cap gain is in the 0% LTCG bracket.

Approximate calc:
  $96,700 LTCG 0% bracket − $50,000 ordinary = $46,700 of LTCG taxed at 0%
  Patricia's full $33,860 fits below that → $33,860 × 0% = $0 federal LTCG tax
```

(Approximate. Actual calculation uses the Schedule D Tax Worksheet, which the agent runs in detail. The point: a retiree with low ordinary income often pays $0 federal tax on long-term capital gains.)

NIIT: MAGI is $113,860, below the $250K MFJ threshold. **No Form 8960 needed.**

## Required attachments

- [x] Schedule D (mandatory)
- [ ] Form 8960 — N/A (below threshold)
- [ ] Form 6781 — N/A
- [ ] Form 8824 — N/A

## Validation summary

- All shares long-term (>1 year by 14+ years for the oldest lot)
- Box D and Box E correctly split based on Vanguard's 1099-B labeling (covered vs non-covered, with the 2012 cutoff date)
- "VARIOUS" in column (b) is appropriate — average cost method aggregates 240+ buy lots into one weighted average
- No wash sale (transaction is a gain, not a loss)
- 1099-DIV Box 2a capital gain distribution properly captured on Schedule D Line 13
- Form 1040 digital asset question: No (no crypto activity)

## Step 10 — Hand off

The agent tells Patricia:

> Your sale of 500 sh VTSAX produced $32,060 of long-term gain plus $1,800 of capital gain distributions = $33,860 total long-term capital gain on Schedule D Line 15.
>
> Because your other ordinary income is below the LTCG 0% bracket cutoff for MFJ ($96,700 in 2025), your federal LTCG tax is **$0**.
>
> However, the gain still increases your total income for purposes of:
> - State tax (most states tax LTCG at the ordinary rate)
> - Social Security benefit taxation (the IRS provisional-income calculation includes capital gains; this may push more of your SS into the 85% taxable bracket)
> - Medicare IRMAA (a $33K spike in income two years out can trigger IRMAA premium surcharges in 2027)
>
> Plan: if you're going to sell more in future years, consider spreading sales across years to keep ordinary + LTCG below the 0% breakpoint.

## Step 11 — File

Patricia files via FFFF. The forms attached: 1040, Schedule D, two 8949 pages (Box D, Box E). Patricia's return is otherwise simple — Social Security, pension, standard deduction.
