# Tax Computation Reference

How to compute Line 16 (Tax) on Form 1040 (2025 revision, filed in 2026; page numbers refer to the 2025 Instructions for Form 1040). The IRS provides multiple methods depending on the taxpayer's income level and the types of income they have. Pick the right method — using the wrong one can over- or under-state tax by thousands.

**Legal basis**: IRC §1 (rate schedules), IRC §1(h) (preferential rates for net capital gain and qualified dividends), IRC §15 (tax in case of multiple rate schedules).

---

## Decision tree

```
Is taxable income (Line 15) < $100,000?
  → Use the Tax Table (2025 instructions, pages 68–79)

Is taxable income ≥ $100,000?
  → Use the Tax Computation Worksheet (2025 instructions, page 80)

Did the filer have qualified dividends (3a > 0), capital gain distributions on 7a with no Schedule D, OR gains on both Schedule D lines 15 and 16?
  → Use the Qualified Dividends and Capital Gain Tax Worksheet (page 38; overrides Tax Table / TCW)

Did Schedule D line 18 (28%-rate gain, e.g. collectibles) or line 19 (unrecaptured §1250 gain) show more than zero, with gains on lines 15 and 16, OR does Form 4952 line 4g have an amount?
  → Use the Schedule D Tax Worksheet in the Schedule D instructions (overrides QDCG)

Is the filer a child with more than $2,700 of unearned income (under 18, or certain 18–23-year-olds)?
  → Use Form 8615

Did the filer claim the foreign earned income exclusion or housing exclusion/deduction (Form 2555)?
  → Use the Foreign Earned Income Tax Worksheet (page 37)

Did the filer report a child's interest/dividends on Form 8814?
  → Use the Form 8814 method to add tax on the child's income to parent's

Did the filer have a lump-sum distribution from a qualified retirement plan they choose to compute under 10-year averaging?
  → Use Form 4972

Most filers use Tax Tables or Tax Computation Worksheet. Self-employed filers without investments use those exclusively.
```

After computing, check the appropriate box on Line 16 indicating the method.

---

## Method 1: Tax Tables

For taxable income < $100,000.

The Tax Tables are in the back of the Form 1040 Instructions, organized by:
- Income range (in $50 increments)
- Filing status (Single, MFJ, MFS, HoH)

Look up Line 15 in the income range column, read across to the column for filing status. The number is the tax.

Example: Line 15 = $44,039, Single. Look in the "$44,000 to $44,050" row, "Single" column. Tax = $5,045 for 2025 (the table computes tax on the row's midpoint, $44,025, and rounds).

**The tables compute the bracket math automatically** — no need to multiply manually. The tables also handle the bracket transitions correctly.

---

## Method 2: Tax Computation Worksheet (TCW)

For taxable income ≥ $100,000.

The TCW (1040 instructions ~page 78) uses a formula to compute tax for each filing status and income range. Format for each row:

```
If your taxable income is at least $X but less than $Y:
  (a) multiply taxable income by [bracket %]
  (b) subtract [adjustment $]
  (c) result is your tax
```

The "adjustment" accounts for the lower brackets so you don't over-tax the lower portions.

**2025 single filer example** (taxable income $250,000):
- Bracket: 32% bracket starts above $197,300 for single in 2025
- Use the TCW row "Over $197,300 but not over $250,525" → $250,000 × 32% = $80,000, minus the $22,937.00 subtraction amount = $57,063
- The subtraction amount ensures the lower brackets (10/12/22/24%) are computed correctly

2025 TCW subtraction amounts (Section A single): 22% $5,086.00; 24% $7,153.00; 32% $22,937.00; 35% $30,452.75; 37% $42,979.75. MFJ/QSS (Section B): 22% $10,172.00; 24% $14,306.00; 32% $45,874.00; 35% $60,905.50; 37% $75,937.50.

The TCW applies the same brackets as the Tax Table; the Table computes tax at the midpoint of each $50 row and stops at $100,000, so the two can differ by a few dollars at the same income. Use whichever one the instructions require for the income level.

**For 2026, the bracket thresholds are published in Rev. Proc. 2025-32 §4.01 (single: 10% to $12,400, 12% to $50,400, 22% to $105,700, 24% to $201,775, 32% to $256,225, 35% to $640,600). Use the 2026 Form 1040 instructions' Tax Table and TCW once released; brackets are inflation-adjusted annually under IRC §1(f).**

---

## Method 3: Qualified Dividends and Capital Gain Tax Worksheet (QDCG)

If the filer has qualified dividends (Line 3a > 0) OR net long-term capital gain on Schedule D, the QDCG Worksheet computes tax using preferential LTCG rates (0%, 15%, 20%) on the qualifying portion and regular rates on the rest.

The worksheet is in the 2025 Form 1040 instructions (page 38).

### LTCG rate brackets (2025)

| Filing status | 0% rate | 15% rate | 20% rate |
|---------------|---------|----------|----------|
| Single | $0–$48,350 | $48,350–$533,400 | over $533,400 |
| MFJ / QSS | $0–$96,700 | $96,700–$600,050 | over $600,050 |
| MFS | $0–$48,350 | $48,350–$300,000 | over $300,000 |
| HoH | $0–$64,750 | $64,750–$566,700 | over $566,700 |

**2026** (Rev. Proc. 2025-32 §4.03): 0% up to $49,450 single/MFS, $98,900 MFJ/QSS, $66,200 HOH; 15% up to $545,500 single, $306,850 MFS, $613,700 MFJ/QSS, $579,600 HOH.

### Worksheet logic (high level)

1. Compute total taxable income (Line 15)
2. Identify the amount of qualified dividends + net LTCG (the "preferential portion")
3. Subtract preferential portion from Line 15 to get "ordinary taxable income"
4. Compute tax on ordinary taxable income using Tax Tables or TCW
5. Compute tax on preferential portion using LTCG brackets
6. Add the two = total tax for Line 16

The worksheet has 25+ lines to handle the bracket transitions correctly when ordinary income partially fills the 0% LTCG bracket etc.

### Why preferential rates matter

For a filer with $80,000 ordinary taxable income + $20,000 qualified dividends (single, 2025):
- Without QDCG: tax all $100,000 at ordinary rates (TCW) → $100,000 × 22% − $5,086 = $16,914
- With QDCG: $80,000 taxed from the Tax Table ($12,520) + $20,000 at 15% ($3,000) = $15,520

That's $1,394 saved by using the right method (about $20,000 × (22% − 15%)). The IRS doesn't compute this for you; tax software does, but a paper filer or DIY user must use the worksheet.

---

## Method 4: Schedule D Tax Worksheet

If the filer has 28%-rate gain (collectibles, certain small business stock) OR unrecaptured §1250 gain (depreciation recapture on real estate sold), the Schedule D Tax Worksheet replaces the QDCG Worksheet. It applies:
- 28% rate to collectibles gain
- 25% rate to unrecaptured §1250 gain
- 0/15/20% to remaining LTCG and qualified dividends
- Ordinary rates to remaining ordinary income

The worksheet is in the Schedule D instructions. Most individual filers don't trigger this; it's specific to investors with rare gain types.

---

## Method 5: Form 8814

If the filer chooses to report a child's interest and dividends on the parent's return (instead of the child filing their own return), use Form 8814. The child's income gets added to the parent's tax with a special calculation.

Available only if the child's income is interest, dividends, and capital gain distributions only, the child's gross income is more than $1,350 and less than $13,500 (2025 and 2026; Rev. Proc. 2024-40 §2.02, Rev. Proc. 2025-32 §4.02), and the child is under 19 (or under 24 if a full-time student).

Generally a higher tax than the child filing separately due to "kiddie tax" rules. Most parents don't elect.

---

## Method 6: Form 4972

For lump-sum distributions from qualified retirement plans (e.g., a pension cash-out) where the filer was born before January 2, 1936. Allows 10-year averaging for tax computation. Very rare; specific to a shrinking demographic.

---

## Special situations

### Foreign earned income

If the filer claims the Foreign Earned Income Exclusion (Form 2555), tax is computed using the Foreign Earned Income Tax Worksheet (1040 instructions). Without the worksheet, the filer would pay tax on excluded income at the lowest brackets (since excluded income reduces taxable income), unfairly benefiting them. The worksheet "stacks" the excluded income on top so the included income is taxed at correct marginal rates.

### Capital loss

If Line 7a is a net capital loss, it's already capped at $3,000 ($1,500 MFS) on Schedule D line 21. The loss reduces total income through Line 7a. Line 16 is computed normally on the (now smaller) Line 15.

### AMT

Alternative Minimum Tax is computed separately on Form 6251 and added to Line 17 (via Schedule 2 Line 2). Most filers post-TCJA owe $0 AMT — the exemption is high enough that only very high earners trigger it.

### Net Investment Income Tax

3.8% on the smaller of net investment income or MAGI over $200,000 (single/HOH), $250,000 (MFJ/QSS), $125,000 (MFS). Computed on Form 8960. Lands on Line 23 (via Schedule 2 Line 12 → Line 21). Not part of regular Line 16 computation.

### Additional Medicare Tax

0.9% on Medicare wages + SE earnings exceeding $200,000 single/HOH/QSS, $250,000 MFJ, $125,000 MFS. Form 8959. Lands on Line 23 (via Schedule 2 Line 11 → Line 21); any amount withheld goes on Line 25c. Not part of Line 16.

---

## Software vs. manual

Tax software handles all of these methods automatically — it picks the right worksheet based on the data entered. For a DIY paper filer or an agent producing an audit-grade draft:

1. Identify which method applies (decision tree at top)
2. Show the math step-by-step
3. State the method on Line 16's checkbox
4. Cross-check against tax software output if available

For agents: the deliverable from `SKILL.md` should explicitly note which method was used and show the worksheet computation.

---

## Sources

- IRC §1 — rate schedules
- IRC §1(h) — preferential rates on net capital gain and qualified dividends
- IRC §1(f) — annual inflation adjustment of brackets
- IRC §1(g) — kiddie tax
- IRC §55–59 — AMT
- IRC §1411 — Net Investment Income Tax
- IRC §3101(b)(2) — Additional Medicare Tax
- [Form 1040 Instructions](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — Tax Tables, TCW, QDCG, worksheets
- [Schedule D Instructions](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — Schedule D Tax Worksheet
- [Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) — AMT
- [Form 8814](https://www.irs.gov/pub/irs-pdf/f8814.pdf) — Parent's Election
- [Form 4972](https://www.irs.gov/pub/irs-pdf/f4972.pdf) — Lump-Sum Distributions
- [Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (worked examples)
- Rev. Proc. 2024-40 — 2025 brackets, including LTCG brackets
- Rev. Proc. 2025-32 — 2026 brackets and LTCG breakpoints
