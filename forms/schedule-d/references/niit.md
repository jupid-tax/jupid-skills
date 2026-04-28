# Net Investment Income Tax (NIIT) — IRC §1411 / Form 8960

A 3.8% additional tax that lands on top of regular capital gains tax for higher-income filers. Capital gain reported on Schedule D is part of the NIIT base. If the filer's modified adjusted gross income (MAGI) exceeds the statutory threshold, Form 8960 must be completed and the NIIT routed to Schedule 2 → Form 1040.

---

## Statutory thresholds (IRC §1411(b))

| Filing status | MAGI threshold |
|---------------|-----------------|
| Single | $200,000 |
| Head of Household | $200,000 |
| Married Filing Jointly / Qualifying Surviving Spouse | $250,000 |
| Married Filing Separately | $125,000 |

These thresholds are **not indexed for inflation**. They have been frozen at these amounts since the tax was enacted in 2013. Each year, more filers cross into NIIT territory by virtue of nominal income growth alone.

For estates and trusts, the threshold is the dollar amount at which the highest tax bracket begins (Schedule D Line 18 territory) — much lower than for individuals.

---

## What counts as Net Investment Income (NII)

Per IRC §1411(c)(1), NII includes:

- **Interest** (taxable)
- **Dividends** (ordinary and qualified)
- **Capital gains** (from Schedule D — both short-term and long-term net gain)
- **Rental and royalty income** (unless from a non-passive real estate trade or business)
- **Non-qualified annuity distributions**
- **Income from passive activities** (passive loss rules from §469)

NII does **not** include:

- Wages, salaries, self-employment income (those are earned income, not investment)
- Distributions from qualified retirement plans (IRA, 401(k), pension)
- Tax-exempt interest (e.g., municipal bond interest)
- Operating gain from a non-passive trade or business
- Gain on sale of an active business interest (for the active owner)

**Capital gain from a primary residence sale** that is excluded under §121 is also excluded from NII. The non-excluded portion (above the $250K / $500K limit) is included.

---

## Computation

```
Step 1: Compute Net Investment Income (NII).
   NII = Investment income (interest + dividends + cap gain + rental + ...)
       − Allowable deductions (investment interest, state tax allocable to investment, etc.)
   NII is floored at zero (a net investment loss does not produce a negative NIIT base).

Step 2: Compute MAGI excess.
   MAGI excess = MAX(0, MAGI − threshold)

Step 3: NIIT base = MIN(NII, MAGI excess)

Step 4: NIIT = NIIT base × 3.8%
```

**Modified AGI (MAGI) for §1411** = Form 1040 Line 11 (AGI) + foreign earned income exclusion add-back (rare).

---

## Worked example

**Single filer, 2025:**
- Wages: $180,000
- Interest income: $5,000
- Ordinary dividends: $3,000
- Long-term capital gain (Schedule D Line 16): $40,000
- Rental net income (passive): $8,000
- AGI / MAGI: $236,000

```
NII = $5,000 + $3,000 + $40,000 + $8,000 = $56,000
   (no investment expenses for simplicity)

MAGI excess = $236,000 − $200,000 = $36,000

NIIT base = MIN($56,000, $36,000) = $36,000
NIIT = $36,000 × 3.8% = $1,368 → Schedule 2 Line 12 → Form 1040
```

The cap at MAGI excess matters — even though NII is $56,000, only $36,000 (the amount above the threshold) is subject to NIIT. As the user's MAGI grows, the cap loosens until NII becomes the binding constraint.

**Same filer, $300,000 MAGI:**
```
MAGI excess = $300,000 − $200,000 = $100,000
NIIT base = MIN($56,000, $100,000) = $56,000
NIIT = $56,000 × 3.8% = $2,128
```

Now the full NII is taxed because the MAGI excess is larger.

---

## Effective rates

Combining NIIT with the regular LTCG rate, a high-income filer pays:

| LTCG bracket | Regular rate | NIIT | Effective federal rate |
|---------------|--------------|------|-------------------------|
| 0% | 0% | 3.8% | 3.8% (rare — needs MAGI > threshold but taxable income in 0% bracket) |
| 15% | 15% | 3.8% | **18.8%** |
| 20% | 20% | 3.8% | **23.8%** |

For short-term gains taxed at the 37% top ordinary rate plus NIIT, the effective rate is **40.8%**.

State tax stacks on top — California can push the all-in long-term rate to 37.1% (20% federal + 3.8% NIIT + 13.3% top state).

---

## Form 8960 line walkthrough

| Line | Description | Source |
|------|-------------|--------|
| 1 | Taxable interest | Form 1040 Line 2b |
| 2 | Ordinary dividends | Form 1040 Line 3b |
| 3 | Annuities | Schedule 1 |
| 4a | Rental, royalty, partnership, S-corp | Schedule E |
| 4b | Adjustment for non-§1411 trade/business | (subtract working business income) |
| 5a | Net gain/loss from disposition | **Schedule D Line 16** + sales not on Sch D |
| 5b | Adjustment for non-§1411 dispositions | (subtract working business sale gain) |
| 5d | Net gain/loss after adjustments | computed |
| 6 | Adjustments for CFCs, PFICs | (rare) |
| 7 | Other modifications | (rare) |
| 8 | **Total investment income** | sum |
| 9 | Investment interest expense | Form 4952 |
| 10 | State income tax allocable | (allocation by ratio) |
| 11 | Misc deductions | (rare post-TCJA) |
| 12 | **Total deductions** | sum |
| 13 | **Net investment income** | Line 8 − Line 12 |
| 14 | MAGI | Form 1040 Line 11 + foreign earned income |
| 15 | Threshold | $200K / $250K / $125K |
| 16 | MAGI excess | Line 14 − Line 15 (if positive) |
| 17 | NIIT | MIN(Line 13, Line 16) × 3.8% |

Line 17 routes to Schedule 2 Line 12 → Form 1040 Line 23.

---

## Common errors

### Error: Forgetting NIIT entirely

**Pattern:** Filer at MAGI $250K single ignores NIIT, files only Schedule D + Form 1040.

**Impact:** Notice 12–18 months later from IRS recomputing the return with NIIT. Tax due plus interest and possibly underpayment penalty.

**Fix:** Always check MAGI against $200K / $250K / $125K thresholds. Form 8960 is short — about 15 minutes once the inputs are in place.

### Error: Including non-§1411 trade/business income

**Pattern:** Self-employed user with Schedule C income includes Schedule C net profit on Form 8960. Wrong — operating income from a non-passive trade or business is *not* NII.

**Impact:** Overpays NIIT.

**Fix:** Schedule C net profit doesn't appear on Form 8960. The §1411 rules carve out income from non-passive trades and businesses.

### Error: Using AGI instead of MAGI

**Pattern:** Filer takes Form 1040 Line 11 (AGI) and uses it directly without the foreign earned income add-back.

**Impact:** For most filers, MAGI = AGI, so this is harmless. For expats with §911 exclusion, MAGI is materially higher and missing the add-back understates NIIT.

**Fix:** Form 8960 Line 14 = AGI + §911 foreign earned income exclusion. Most filers' add-back is zero.

### Error: Including primary residence excluded gain

**Pattern:** User sold a home with $400,000 gain; first $250,000 (single) excluded under §121; user includes the full $400,000 on Form 8960 Line 5a.

**Impact:** Overpays NIIT by $9,500 ($250,000 × 3.8%).

**Fix:** Only the non-excluded portion ($150,000) is in NII. The §121 exclusion carries through to NIIT.

---

## Planning levers

For taxpayers near the NIIT threshold, several levers can reduce exposure:

1. **Tax-loss harvesting** — losses reduce Schedule D Line 16, which reduces NII.
2. **Timing of capital gains** — bunching gains in low-MAGI years and losses in high-MAGI years.
3. **Roth conversions** — increase MAGI in the conversion year (potentially triggering NIIT on existing investment income), but reduce future RMDs and future MAGI.
4. **Real estate "non-passive"** — for filers who qualify as real estate professionals under §469(c)(7), rental income is non-passive and excluded from NII. Strict rules.
5. **Investment interest expense** — deductible on Form 8960 Line 9, reducing NII. Most retail filers don't have material investment interest expense.

For high-net-worth filers, tax planning around NIIT typically takes place at the year-end. Schedule D timing is the largest controllable input.

---

## Sources

- [IRC §1411](https://www.law.cornell.edu/uscode/text/26/1411) — Imposition of tax
- [Form 8960](https://www.irs.gov/pub/irs-pdf/f8960.pdf) — Net Investment Income Tax
- [Instructions for Form 8960](https://www.irs.gov/pub/irs-pdf/i8960.pdf)
- [Treas. Reg. §1.1411](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.1411-1) — Final regulations under §1411
