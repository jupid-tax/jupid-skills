# Form 8995 — Line-by-Line Reference

Complete reference for every line on the simplified Form 8995. The form is a single page with 17 numbered lines. Sections below mirror the form layout.

---

## Header

### Name(s) shown on return

Enter exactly as on Form 1040. If filing jointly, both names if both have QBI sources; otherwise the taxpayer with QBI.

### Your taxpayer identification number

Primary filer's SSN (or ITIN). Use the same SSN as on Form 1040.

---

## Part I — Trade or Business Information (Lines 1a-1e)

The form has 5 row slots. If a filer has more than 5 QBI sources, attach a continuation statement listing the additional sources.

### Column (i): Trade, business, or aggregation name

A short, identifiable name. Examples:
- Sole prop: business name from Schedule C Line C, or filer's profession if no business name (e.g., "Garcia Design")
- Partnership K-1: partnership name (e.g., "Acme Marketing LLC")
- S-corp K-1: S-corp name (e.g., "XYZ Consulting Inc")
- Aggregated trades (only if a §199A aggregation election was made under Treas. Reg. §1.199A-4): use the aggregation name from the election statement

### Column (ii): Taxpayer identification number

- Sole prop with no EIN → filer's SSN
- Sole prop with EIN → the business EIN
- Partnership K-1 → the partnership EIN (from the K-1)
- S-corp K-1 → the S-corp EIN (from the K-1)

### Column (iii): Qualified business income or (loss)

This is **not** raw revenue or net profit. It is QBI as defined in IRC §199A(c) and Treas. Reg. §1.199A-3.

**For Schedule C sources:**

```
QBI = Schedule C Line 31 (net profit/loss)
    − ½ self-employment tax allocable to this Schedule C
    − Self-employed health insurance allocable to this Schedule C
    − Self-employed retirement contributions allocable to this Schedule C
```

For a single Schedule C, the entire amount of these adjustments is allocated to it. For multiple Schedule Cs, allocate proportionally to net profit. See [`qbi-adjustments.md`](./qbi-adjustments.md).

**For partnership K-1 sources:**

Use the QBI amount in Box 20 with code Z (Section 199A information). The K-1 statement should explicitly label QBI separately from total partnership income. If the K-1 doesn't break it out, request a corrected statement.

**For S-corp K-1 sources:**

Use the QBI amount in Box 17 with code V (Section 199A information). Same statement requirement as partnership K-1.

**For rental real estate:**

Only include if the rental qualifies as a trade or business under either:
- IRC §162 (general trade or business standard — facts and circumstances)
- The Section 199A safe harbor in Notice 2019-7 (250+ hours, separate books, contemporaneous records)

If neither applies, the rental income is not QBI and does not go here.

### Negative amounts

Column (iii) can be negative for a loss. The Line 2 sum may also be negative — in which case Line 2 is entered as 0 and the loss carries to next year's Line 3.

---

## Part I — QBI Component (Lines 2-4)

### Line 2: Total qualified business income or (loss)

Sum of Column (iii) on Lines 1a through 1e.

**If sum is positive:** enter the sum.

**If sum is negative:** enter 0. The negative amount becomes a "qualified business loss carryforward" — track it for next year's Line 3. Show the carryforward in the workpapers.

### Line 3: Qualified business net (loss) carryforward from prior year

If Line 16 from last year's Form 8995 (or the equivalent on Form 8995-A from last year) was negative, enter that amount as a negative number on Line 3.

If first-year filer or no prior loss, enter 0.

### Line 4: Total qualified business income component

Line 2 + Line 3. If the result is negative, enter 0 and treat the negative amount as a carryforward to next year.

---

## Part II — REIT/PTP Component (Lines 5-7, plus 8-9 carryforward mechanics)

### Line 5: Qualified REIT dividends and PTP income

Sum of:
- **Section 199A dividends from REITs** — Box 5 of Form 1099-DIV (NOT Box 1a, which is ordinary dividends)
- **Qualified publicly traded partnership (PTP) income** — from PTP K-1 statements; the PTP-issuer reports Section 199A info in the K-1 footnotes

REIT income is reported gross — no §199A adjustments needed (unlike sole prop QBI). PTP income is also reported as the qualified amount per the K-1.

### Line 6: Qualified REIT dividends and PTP (loss) carryforward

If prior year had a net REIT/PTP loss (Line 7 was floored at 0 because Line 5 + Line 6 was negative), the negative amount carries to this year's Line 6.

### Line 7: Total qualified REIT dividends and PTP income

Line 5 + Line 6. If negative, enter 0 and carry the negative to next year's Line 6.

### Lines 8-9 (carryforward mechanics)

The current Form 8995 includes Lines 8 and 9 to handle further REIT/PTP carryforward computation. These lines occasionally shift between revisions:

- **Line 8** — Qualified REIT/PTP component (often = Line 7 with no further reduction)
- **Line 9** — Loss carryforward used this year (typically 0 unless current-year income is offset by carryforward)

Always consult the latest IRS instructions at `https://www.irs.gov/pub/irs-pdf/i8995.pdf` for the exact line numbering for the tax year being filed.

---

## Part III — Combining and Limiting (Lines 10-17)

### Line 10: QBI component (Line 4 × 20%)

Multiply Line 4 by 0.20. Round to the nearest dollar.

### Line 11: REIT/PTP component (Line 7 × 20%)

Multiply Line 7 (or final REIT/PTP figure if Lines 8-9 modified it) by 0.20.

### Line 12: QBI deduction before income limitation

Line 10 + Line 11. This is the maximum potential §199A deduction before applying the taxable income limit.

### Line 13: Taxable income before QBI deduction

This line is conceptually tricky. It is the filer's taxable income computed *as if no QBI deduction were taken*.

**Practical formula** (after Form 1040 is otherwise complete):

```
Line 13 = Form 1040 Line 15 + Form 1040 Line 13 (the QBI deduction itself)
```

In other words, take current 1040 taxable income (Line 15) and add back the QBI deduction (Line 13) to recover pre-QBI taxable income.

**Estimating before 1040 is complete:**

```
Line 13 = AGI (1040 Line 11)
        − Standard deduction OR itemized deductions (1040 Line 12)
        (do not subtract QBI on this line — that's what we're computing)
```

For most simple filers: Line 13 = AGI − $15,000 (single 2025 standard deduction) or AGI − $30,000 (MFJ 2025 standard deduction).

### Line 14: Net capital gain

Sum of:
- **Qualified dividends** — Form 1040 Line 3a
- **Net long-term capital gain** — Schedule D Line 16, if Schedule D is required; otherwise Form 1040 Line 7

If neither, enter 0.

The §199A deduction excludes capital gain because long-term capital gains and qualified dividends are already taxed at preferential rates and Congress did not want to compound the benefit.

### Line 15: Subtract Line 14 from Line 13

Line 13 − Line 14. This is the income subject to the 20% taxable income limit.

### Line 16: 20% of Line 15 (taxable income limitation)

Line 15 × 0.20. This is the **upper bound** on the §199A deduction. The deduction can never exceed 20% of taxable income (excluding net capital gain).

### Line 17: Qualified business income deduction

The lesser of:
- Line 12 (20% of QBI + REIT/PTP)
- Line 16 (20% of taxable income excluding capital gain)

This is the final §199A deduction. It flows to **Form 1040, Line 13** (Qualified business income deduction).

---

## After the form

- **Attach Form 8995 to Form 1040** when filing — it is not standalone
- **Track carryforwards** in the workpapers for next year:
  - QBI loss carryforward = the negative amount of Line 2 (if any)
  - REIT/PTP loss carryforward = the negative amount of Line 7 (if any)
- **Reconcile Line 17 with Form 1040 Line 13** — they must match

---

## Year-over-year reconciliation

If the user files Form 8995 in consecutive years, verify:

- Line 3 on this year's form = the negative of (Line 2 negative amount carried forward) from last year
- Line 6 on this year's form = the negative of (Line 7 negative amount carried forward) from last year
- Filing status hasn't changed mid-year (if so, document the change)
- Threshold compliance — taxable income still below threshold

---

## Edge cases

### Filer is a beneficiary of a trust or estate with QBI

Trust/estate K-1 (Schedule K-1, Form 1041) reports QBI in Box 14, code I. Treat the same as partnership K-1 — list the trust/estate name in Column (i), the trust/estate EIN in Column (ii), the QBI amount in Column (iii).

### Filer has §199A aggregation election

If the filer has elected to aggregate two or more trades or businesses under Treas. Reg. §1.199A-4, list the aggregation as a single row in Lines 1a-1e using the aggregation's name. Attach the aggregation election statement to the return per Reg. §1.199A-4(c).

### Filer has prior-year loss but no current-year QBI

Line 1a-1e will be empty. Enter the loss carryforward on Line 3. Line 4 will be negative — enter 0. The carryforward continues to next year.

### Filer's total Line 12 = 0 but Line 7 > 0 (only REIT/PTP, no QBI)

This is valid. Form 8995 is still filed for the REIT/PTP deduction. Line 4 = 0, Line 7 > 0, Line 10 = 0, Line 11 > 0, Line 12 = Line 11.

### Self-employed filer with multiple Schedule Cs

Each Schedule C is a separate trade or business unless aggregated. List each on its own row in Lines 1a-1e. Allocate the SE tax adjustment proportionally to each business's share of net profit. See [`qbi-adjustments.md`](./qbi-adjustments.md) for the allocation formula.
