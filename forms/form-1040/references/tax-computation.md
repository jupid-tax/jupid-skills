# Tax Computation Reference

How to compute Line 16 (Tax) on Form 1040. The IRS provides multiple methods depending on the taxpayer's income level and the types of income they have. Pick the right method — using the wrong one can over- or under-state tax by thousands.

**Legal basis**: IRC §1 (rate schedules), IRC §1(h) (preferential rates for net capital gain and qualified dividends), IRC §15 (tax in case of multiple rate schedules).

---

## Decision tree

```
Is taxable income (Line 15) < $100,000?
  → Use the Tax Tables (in the 1040 instructions, ~pages 66-77)

Is taxable income ≥ $100,000?
  → Use the Tax Computation Worksheet (1040 instructions ~page 78)

Did the filer have qualified dividends (3a > 0) OR net long-term capital gain on Schedule D?
  → Use the Qualified Dividends and Capital Gain Tax Worksheet (overrides Tax Tables / TCW)

Did the filer have 28%-rate gain (collectibles) OR unrecaptured §1250 gain?
  → Use the Schedule D Tax Worksheet (more complex; overrides QDCG)

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

Example: Line 15 = $44,039, Single. Look in the "$44,000 to $44,050" row, "Single" column. Tax ≈ $5,031 for 2025.

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
- Bracket: 32% bracket starts at $197,300 for single in 2025
- Use TCW row for "at least $197,300 but less than $250,525" → multiply by 32% and subtract a fixed adjustment
- The adjustment ensures the lower brackets (10/12/22/24%) are computed correctly

The TCW is more compact than the Tax Tables but produces exactly the same answer for any income level (the Tables stop at $100,000 to keep the booklet from being huge).

**For 2026, verify the TCW from the 2026 Form 1040 instructions. Brackets are inflation-adjusted annually under IRC §1(f).**

---

## Method 3: Qualified Dividends and Capital Gain Tax Worksheet (QDCG)

If the filer has qualified dividends (Line 3a > 0) OR net long-term capital gain on Schedule D, the QDCG Worksheet computes tax using preferential LTCG rates (0%, 15%, 20%) on the qualifying portion and regular rates on the rest.

The worksheet is in the 1040 instructions (~page 36).

### LTCG rate brackets (2025)

| Filing status | 0% rate | 15% rate | 20% rate |
|---------------|---------|----------|----------|
| Single | $0–$48,350 | $48,350–$533,400 | over $533,400 |
| MFJ / QSS | $0–$96,700 | $96,700–$600,050 | over $600,050 |
| MFS | $0–$48,350 | $48,350–$300,000 | over $300,000 |
| HoH | $0–$64,750 | $64,750–$566,700 | over $566,700 |

**For 2026, verify against Rev. Proc. 2025-XX.**

### Worksheet logic (high level)

1. Compute total taxable income (Line 15)
2. Identify the amount of qualified dividends + net LTCG (the "preferential portion")
3. Subtract preferential portion from Line 15 to get "ordinary taxable income"
4. Compute tax on ordinary taxable income using Tax Tables or TCW
5. Compute tax on preferential portion using LTCG brackets
6. Add the two = total tax for Line 16

The worksheet has 25+ lines to handle the bracket transitions correctly when ordinary income partially fills the 0% LTCG bracket etc.

### Why preferential rates matter

For a filer with $80,000 ordinary income + $20,000 qualified dividends (single):
- Without QDCG: tax all $100,000 at ordinary rates → ~$13,841
- With QDCG: ordinary portion taxed at ordinary rates, qualified dividends taxed at 15% LTCG rate → ~$13,841 − ($20,000 × (22% − 15%)) ≈ $12,441

That's $1,400 saved by using the right method. The IRS doesn't compute this for you; tax software does, but a paper filer or DIY user must use the worksheet.

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

Available only if the child's income is interest/dividends only, ≤ $13,000 (2025; verify 2026), and child is under 19 (or 24 if a student).

Generally a higher tax than the child filing separately due to "kiddie tax" rules. Most parents don't elect.

---

## Method 6: Form 4972

For lump-sum distributions from qualified retirement plans (e.g., a pension cash-out) where the filer was born before January 2, 1936. Allows 10-year averaging for tax computation. Very rare; specific to a shrinking demographic.

---

## Special situations

### Foreign earned income

If the filer claims the Foreign Earned Income Exclusion (Form 2555), tax is computed using the Foreign Earned Income Tax Worksheet (1040 instructions). Without the worksheet, the filer would pay tax on excluded income at the lowest brackets (since excluded income reduces taxable income), unfairly benefiting them. The worksheet "stacks" the excluded income on top so the included income is taxed at correct marginal rates.

### Capital loss

If Line 7 is a net capital loss, it's already capped at $3,000 ($1,500 MFS) on Schedule D. The loss reduces ordinary income on Line 7. Line 16 is computed normally on the (now smaller) Line 15.

### AMT

Alternative Minimum Tax is computed separately on Form 6251 and added to Line 17 (via Schedule 2 Line 1). Most filers post-TCJA owe $0 AMT — the exemption is high enough that only very high earners trigger it.

### Net Investment Income Tax

3.8% on net investment income for single filers with AGI > $200,000 / MFJ > $250,000. Computed on Form 8960. Lands on Line 17 (via Schedule 2 Line 12). Not part of regular Line 16 computation.

### Additional Medicare Tax

0.9% on wages + SE earnings exceeding $200,000 single / $250,000 MFJ. Form 8959. Lands on Line 17 (via Schedule 2 Line 11). Not part of Line 16.

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
