# Schedule D — Line-by-Line Reference

This document expands every line on Schedule D (Form 1040). Pull from the linked form and instructions for the year being filed; the IRS revises line wording from year to year, but the structure has been stable since the 2018 redesign.

**Companion sources:**
- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [Publication 550](https://www.irs.gov/publications/p550)

---

## Header

**Name(s) shown on return** — Exact match to Form 1040. If filing jointly, both names must appear.

**Your social security number** — Filer's SSN; matches Form 1040.

---

## Part I — Short-Term Capital Gains and Losses (assets held one year or less)

Part I covers **assets held one year or less**. Net short-term gain is taxed at the user's ordinary income rate (10% – 37% brackets).

### Line 1a — Totals for short-term transactions reported on Form 1099-B showing basis was reported to the IRS and for which **no adjustments are required**

This is the optional aggregation line. Use only if **all** of the following are true:

- The 1099-B reports basis to the IRS (this is Box A)
- The 1099-B's basis matches the user's records (no correction needed)
- No wash sale adjustment is required (broker-reported wash sales already on the 1099-B do require Form 8949 entry, however)
- No other column (g) adjustment is needed

Enter the totals from the 1099-Bs directly: column (d) proceeds total, column (e) basis total, column (h) gain/loss.

If any of the conditions fails, the transaction must be reported on Form 8949 Box A and rolled to Line 1b instead.

### Line 1b — Totals for all short-term transactions reported on Form 8949 with Box A checked

Sum of column (d), (e), (g), and (h) from every Form 8949 Part I, Box A page. The IRS computer matches Line 1b column (d) totals against the broker's transmitted 1099-B Box 1d totals; mismatches trigger automated notices.

### Line 2 — Totals for all short-term transactions reported on Form 8949 with Box B checked

Box B = short-term, basis NOT reported on 1099-B. Common causes: shares acquired before broker basis reporting (pre-2011 covered date), transferred-in lots without basis history.

### Line 3 — Totals for all short-term transactions reported on Form 8949 with Box C checked

Box C = short-term, no 1099-B issued. Common causes: crypto sales (most US exchanges still don't issue 1099-B, though 1099-DA is rolling out for tax year 2025+), private placements, peer-to-peer asset sales.

### Line 4 — Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824

Combined entry for:
- **Form 6252** — Installment sales: short-term gain recognized in the current year on a multi-year installment sale
- **Form 4684** — Casualty or theft loss on personal-use property; rare in this position
- **Form 6781** — §1256 contracts (futures, broad-based index options): the **40% short-term portion** of the marked-to-market gain or loss
- **Form 8824** — Like-kind exchanges: any "boot" received that triggered short-term gain

Do not double-count: if a transaction is on Form 8949, it does not also go on Line 4.

### Line 5 — Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1

From Schedule K-1:
- **Form 1065 (partnership) K-1** — Box 8 short-term capital gain
- **Form 1120-S (S-corp) K-1** — Box 7 short-term capital gain
- **Form 1041 (estate/trust) K-1** — Box 3 short-term capital gain

### Line 6 — Short-term capital loss carryover

Negative number (a loss). From the prior-year Capital Loss Carryover Worksheet, the short-term portion of the unused loss.

If the user used software last year, the software typically tracks this; otherwise the user must locate the prior-year worksheet.

### Line 7 — Net short-term capital gain or (loss). Combine lines 1a through 6

Arithmetic sum of column (h) from Lines 1a, 1b, 2, 3, plus Lines 4, 5, 6 amounts.

This is the year's net short-term result before combining with long-term. Net short-term loss can offset long-term gain at Line 16.

---

## Part II — Long-Term Capital Gains and Losses (assets held more than one year)

Part II covers **assets held more than one year**. Net long-term gain is taxed at the preferential 0/15/20% rate (or 25% / 28% for special asset categories).

### Line 8a — Totals for long-term transactions reported on Form 1099-B showing basis was reported to the IRS and for which **no adjustments are required**

Same aggregation rules as Line 1a, applied to Box D (long-term, basis reported).

### Line 8b — Totals for all long-term transactions reported on Form 8949 with Box D checked

Sum from Form 8949 Part II, Box D pages.

### Line 9 — Totals for all long-term transactions reported on Form 8949 with Box E checked

Box E = long-term, basis NOT reported on 1099-B. Common: mutual fund shares acquired before 2012, transferred-in long-held lots.

### Line 10 — Totals for all long-term transactions reported on Form 8949 with Box F checked

Box F = long-term, no 1099-B issued. Common: long-held crypto (more than one year), real estate, collectibles.

### Line 11 — Gain from Form 4797 (§1231); long-term gain from Forms 2439, 6252, 6781 and 8824

Combined entry for:
- **Form 4797** — Net §1231 gain (after netting and depreciation recapture as ordinary income on Form 4797 Part III). Net §1231 *losses* don't come here — they go to ordinary income directly via Form 4797.
- **Form 2439** — Undistributed long-term capital gains from a regulated investment company or REIT (rare in personal returns)
- **Form 6252** — Long-term portion of installment sale gain
- **Form 6781** — 60% long-term portion of §1256 contract gain/loss
- **Form 8824** — Long-term portion of like-kind exchange boot

### Line 12 — Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1

K-1 long-term capital gain boxes:
- 1065 K-1 Box 9a
- 1120-S K-1 Box 8a
- 1041 K-1 Box 4a

### Line 13 — Capital gain distributions

From Form 1099-DIV Box 2a — capital gain distributions from mutual funds, REITs, and certain regulated investment companies. **Always treated as long-term** regardless of how long the fund shares have been held.

If your only Schedule D activity is Line 13 (Box 2a only, no 8949 entries), you may be able to skip Schedule D and report directly on Form 1040 Line 7 — see the Schedule D instructions for the exact conditions.

### Line 14 — Long-term capital loss carryover

Negative number. From the prior-year Capital Loss Carryover Worksheet, long-term portion.

### Line 15 — Net long-term capital gain or (loss). Combine lines 8a through 14

Sum of column (h) from Lines 8a, 8b, 9, 10 plus Lines 11, 12, 13, 14.

---

## Part III — Summary

### Line 16 — Combine lines 7 and 15 and enter the result

If positive → flows to Form 1040 Line 7 (assuming Line 17 = Yes).

If negative → continue to Line 21 for the loss limitation.

If zero → no capital gain/loss for the year.

### Line 17 — Are lines 15 and 16 both gains?

- **Yes** → Go to Line 18.
- **No** → Skip to Line 22.

This branch determines whether the preferential capital gain rate applies. If Line 15 is negative or zero, you don't have net long-term gain, so no preferential rate applies; you simply use the regular tax tables (or the small-case Qualified Dividends part of the worksheet if you have qualified dividends).

### Line 18 — 28% Rate Gain Worksheet result

If you have:
- Form 8949 entries with code **C** (collectibles) — gold, silver, art, antiques, wine, classic cars held as investments
- Form 8949 entries with code **Q** (§1202 QSBS partial-exclusion gain)

You must compute the 28% Rate Gain Worksheet (in Schedule D instructions). The result goes on Line 18.

The 28% rate is a *maximum* rate — if the user's ordinary bracket is below 28%, they pay the lower ordinary rate on the collectibles gain. The Schedule D Tax Worksheet handles this automatically.

### Line 19 — Unrecaptured Section 1250 Gain Worksheet result

If you sold real estate (or other §1250 property) with prior depreciation, the depreciation portion (up to gain) is "unrecaptured §1250 gain" taxed at a maximum 25% rate.

The Unrecaptured §1250 Gain Worksheet (in Schedule D instructions) walks through the computation. Common inputs: sale of rental real estate. Sale of a primary residence with rental years can also produce §1250 unrecaptured gain on the rental portion.

### Line 20 — Are lines 18 and 19 both zero or blank?

- **Yes** → Use the Qualified Dividends and Capital Gain Tax Worksheet in the Form 1040 instructions to compute your tax.
- **No** → Use the Schedule D Tax Worksheet in the Schedule D instructions.

This is the single most consequential line on Schedule D. The wrong worksheet can mean thousands of dollars of overpayment or underpayment.

### Line 21 — If line 16 is a loss, enter the smaller of (Line 16 as a positive number) or ($3,000) ($1,500 if MFS)

Apply the IRC §1211(b) loss limit. Enter the capped amount as a *negative* number; this is what flows to Form 1040 Line 7 to reduce ordinary income.

The remainder (Line 16 absolute value minus Line 21) feeds the Capital Loss Carryover Worksheet for next year.

### Line 22 — Do you have qualified dividends on Form 1040 line 3a?

- **Yes** → Use the Qualified Dividends and Capital Gain Tax Worksheet.
- **No** → Use the regular tax tables.

Line 22 only matters when Line 16 is a loss or zero (so you didn't reach a capital-gain rate worksheet via Lines 17–20). Even with no net capital gain, qualified dividends still get preferential treatment.

---

## Worksheets included with Schedule D Instructions

These worksheets are all in the **Instructions for Schedule D** (i1040sd.pdf), not the form itself. The agent must compute them outside the form and enter the results on Lines 18, 19, and 21.

1. **28% Rate Gain Worksheet** — Pulls collectibles gain (code C) and unexcluded §1202 gain (code Q) into a separate bucket taxed at maximum 28%. Used to populate Line 18.
2. **Unrecaptured Section 1250 Gain Worksheet** — Pulls real estate depreciation (up to gain) into a separate bucket taxed at maximum 25%. Used to populate Line 19.
3. **Capital Loss Carryover Worksheet** — Computes the short-term and long-term carryforward to next year when Line 16 is a loss exceeding the $3,000 / $1,500 MFS limit.
4. **Schedule D Tax Worksheet** — Computes total tax when Line 18 or 19 is greater than zero. Layers ordinary, 25%, 28%, and 0/15/20% rates.

The **Qualified Dividends and Capital Gain Tax Worksheet** is in the **Form 1040 Instructions** (not Schedule D's), but is the simpler tax computation used when Line 18 and Line 19 are both zero.

See [`tax-rate-worksheets.md`](./tax-rate-worksheets.md) for step-by-step on the two main worksheets.

---

## Common patterns

### Pattern: Stocks-only retail filer with covered shares

- All transactions on 1099-B from one broker, all basis reported
- Line 1a or 1b only (Part I), Line 8a or 8b only (Part II)
- Line 7 + Line 15 = Line 16 → Form 1040 Line 7
- Use Qualified Dividends and Capital Gain Tax Worksheet
- No NIIT unless MAGI > threshold

### Pattern: Crypto-only filer

- All transactions on Form 8949 Boxes C (short) and F (long) — no 1099-B issued
- Roll to Schedule D Lines 3 and 10
- Same downstream as above

### Pattern: Mixed retail + crypto

- Boxes A/B/C and D/E/F populated
- Lines 1b, 2, 3 (Part I); Lines 8b, 9, 10 (Part II)
- Schedule D mathematics is straightforward; the work is upstream on Form 8949

### Pattern: Big loss year

- Line 7 or Line 15 (or both) is negative; Line 16 is negative
- Line 21 caps loss at $3,000 ($1,500 MFS)
- Capital Loss Carryover Worksheet produces ST and LT carryforwards

### Pattern: Real estate sale with depreciation

- Form 4797 first (depreciation recapture as ordinary income; net §1231 gain converts to LT capital)
- Schedule D Line 11 receives the §1231 LT gain
- Unrecaptured §1250 Gain Worksheet → Line 19
- Schedule D Tax Worksheet (not Qualified Dividends and Capital Gain Tax Worksheet)

### Pattern: §1202 QSBS exclusion

- Form 8949 with code Q (partial exclusion) or X (full exclusion)
- Excluded portion in column (g) — never appears on Schedule D
- Included portion (if any) flows through 8949 → Schedule D normally
- Code Q amount also feeds 28% Rate Gain Worksheet → Line 18 (the included §1202 portion is taxed at 28% max if not fully excluded)

---

## Sources

- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses
- IRC §1(h), §1211, §1212, §1411, §1202, §1231, §1250
