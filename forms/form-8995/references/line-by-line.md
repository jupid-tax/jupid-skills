# Form 8995 — Line-by-Line Reference

Complete reference for every line on the simplified Form 8995. The form is a single page with 17 numbered lines. Sections below mirror the form layout.

Verified against the **2025 Form 8995** (Created 9/12/25, https://www.irs.gov/pub/irs-pdf/f8995.pdf) and the **2025 Instructions for Form 8995** (Jan 26, 2026, https://www.irs.gov/pub/irs-pdf/i8995.pdf). The 2026 draft (https://www.irs.gov/pub/irs-dft/f8995--dft.pdf, Created 5/1/26) keeps lines 1–14, then adds line 15 (deduction before the minimum), line 16 (minimum deduction for active QBI, IRC §199A(i)), line 17 (deduction), lines 18–19 (carryforwards) and line 20 (ESBT box). Re-check the final revision each year.

---

## Header

### Name(s) shown on return

Enter exactly as on Form 1040. If filing jointly, both names if both have QBI sources; otherwise the taxpayer with QBI.

### Your taxpayer identification number

Primary filer's SSN (or ITIN). Use the same SSN as on Form 1040.

---

## Line 1 — Trade, business, or aggregation (rows 1i–1v)

The form has 5 rows (i through v). If a filer has more than 5 trades or businesses, attach a statement with the name and TIN of each additional one and include their income and loss in the line 2 total (i8995, Line 2).

### Column (a): Trade, business, or aggregation name

A short, identifiable name. Examples:
- Sole prop: business name from Schedule C Line C, or filer's profession if no business name (e.g., "Garcia Design")
- Partnership K-1: partnership name (e.g., "Acme Marketing LLC")
- S-corp K-1: S-corp name (e.g., "XYZ Consulting Inc")
- Aggregated trades (Treas. Reg. §1.199A-4): enter the aggregation group name ("Aggregation 1, 2, 3") and leave column (b) blank; attach Schedule B (Form 8995-A) or a similar schedule (i8995, Line 1)
- Rental real estate under the Rev. Proc. 2019-38 safe harbor: enter each enterprise as identified on the safe-harbor statement ("Enterprise 1, 2, 3")

### Column (b): Taxpayer identification number

- Business with an EIN → the EIN (a single-member LLC disregarded for tax uses the LLC's EIN)
- No EIN → filer's SSN or ITIN
- Partnership / S-corp / trust K-1 → the entity's EIN (from the K-1)

### Column (c): Qualified business income or (loss)

This is **not** raw revenue or net profit. It is QBI as defined in IRC §199A(c) and Treas. Reg. §1.199A-3.

**For Schedule C sources:**

```
QBI = Schedule C Line 31 (net profit/loss)
    − ½ self-employment tax allocable to this Schedule C
    − Self-employed health insurance allocable to this Schedule C
    − Self-employed retirement contributions allocable to this Schedule C
    − Qualified tips from this business deducted under §224 on Schedule 1-A (2025 and later)
```

For a single Schedule C, the entire amount of these adjustments is allocated to it. For multiple Schedule Cs, allocate proportionally to net profit. See [`qbi-adjustments.md`](./qbi-adjustments.md).

**For partnership K-1 sources:**

Use the QBI amount from the Section 199A statement (Box 20, code Z). Then subtract partner-level deductions attributable to that partnership (½ SE tax on its self-employment income, SE health insurance and retirement contributions based on that income, unreimbursed partnership expenses, interest on debt used to buy the interest). If the K-1 doesn't break QBI out, request the statement.

**For S-corp K-1 sources:**

Use the QBI amount from the Section 199A statement (Box 17, code V). If the shareholder owns more than 2% and deducts SE health insurance on Schedule 1 line 17 based on S corporation wages, subtract that deduction.

**For rental real estate:**

Only include if the rental qualifies as a trade or business under either:
- IRC §162 (general trade or business standard — facts and circumstances)
- The Section 199A safe harbor in Rev. Proc. 2019-38 (250+ hours of rental services, separate books, contemporaneous records)

If neither applies, the rental income is not QBI and does not go here.

**Do not include** losses or deductions still suspended by other Code sections (§§163(j), 179, 461(l), 465, 469, 704(d), 1366(d)) or qualified portions of previously suspended losses allowed this year; those go on line 3 (i8995, Line 1).

### Negative amounts

Column (c) can be negative for a loss. Line 2 may also be negative; the floor is applied on line 4, and the loss carries to next year through line 16.

---

## QBI Component (Lines 2–5)

### Line 2: Total qualified business income or (loss)

Combine column (c) of rows 1i through 1v. The result can be negative. Do not floor it.

### Line 3: Qualified business net (loss) carryforward from the prior year

Last year's Form 8995 line 16 (or Schedule C (Form 8995-A) line 6 if last year's return used Form 8995-A), entered as a negative number in parentheses. Also include the qualified portion of previously suspended losses allowed in calculating taxable income this year (i8995, Line 3).

If first-year filer or no prior loss, enter 0.

### Line 4: Total qualified business income

Line 2 + Line 3. If zero or less, enter -0-. A net loss means no QBI component this year; the loss carries forward (line 16).

### Line 5: Qualified business income component

Line 4 × 20% (0.20).

---

## REIT/PTP Component (Lines 6–9)

### Line 6: Qualified REIT dividends and PTP income or (loss)

Sum of:
- **Section 199A dividends from REITs** — Box 5 of Form 1099-DIV (NOT Box 1a, which is ordinary dividends). Box 5 shows what "may be eligible"; the shares must have been held more than 45 days (Treas. Reg. §1.199A-3(c)(2)(ii)).
- **Qualified publicly traded partnership (PTP) income or loss** — from PTP K-1 Section 199A statements

Enter income as a positive number and losses as a negative number (i8995, Line 6). No §199A adjustments apply.

### Line 7: Qualified REIT dividends and PTP (loss) carryforward from the prior year

Last year's Form 8995 line 17 (or Form 8995-A line 40), as a negative number in parentheses. Also include the qualified portion of previously suspended PTP losses allowed this year (i8995, Line 7).

### Line 8: Total qualified REIT dividends and PTP income

Line 6 + Line 7. If zero or less, enter -0-. A negative amount carries forward (line 17).

### Line 9: REIT and PTP component

Line 8 × 20% (0.20).

---

## Combining and Limiting (Lines 10–15)

### Line 10: QBI deduction before the income limitation

Line 5 + Line 9.

### Line 11: Taxable income before qualified business income deduction

Per the 2025 instructions:
- Form 1040 / 1040-SR: **line 11a minus lines 12e and 13b**
- Form 1040-NR: line 11a minus lines 12, 13b, and 13c
- Form 1041: line 17 minus lines 18, 19, and 21

Line 12e is the standard or itemized deduction; line 13b is the Schedule 1-A deductions (qualified tips, qualified overtime, car loan interest, enhanced deduction for seniors). Practical check after Form 1040 is complete: line 11 here = Form 1040 line 15 + line 13a.

For simple filers using the 2025 standard deduction: AGI − $15,750 (single or MFS), − $31,500 (MFJ or QSS), − $23,625 (HOH) (2025 Form 1040 page 2), minus any Schedule 1-A deductions.

### Line 12: Net capital gain, increased by qualified dividends

- **Qualified dividends** — Form 1040 line 3a
- **plus net capital gain** — if Schedule D is required, the smaller of Schedule D line 15 or line 16; if either is zero or less, add nothing. If Schedule D isn't required, Form 1040 line 7a

If neither, enter 0. The §199A deduction is limited to 20% of taxable income in excess of net capital gain as defined in §1(h), which includes qualified dividends (IRC §199A(a)(2)).

### Line 13: Subtract line 12 from line 11

If zero or less, enter -0-.

### Line 14: Income limitation

Line 13 × 20% (0.20). This is the **upper bound** on the §199A deduction.

### Line 15: Qualified business income deduction

The smaller of:
- Line 10 (20% of QBI + 20% of REIT/PTP)
- Line 14 (20% of taxable income excluding net capital gain)

This is the final §199A deduction. It flows to **Form 1040 / 1040-SR / 1040-NR line 13a** (2025), Form 1041 line 20.

---

## Carryforwards (Lines 16–17)

### Line 16: Total qualified business (loss) carryforward

Line 2 + Line 3. If greater than zero, enter -0-. A negative amount carries to next year's line 3 and offsets QBI in later years even if the business that generated it no longer exists (i8995, Line 16).

### Line 17: Total qualified REIT dividends and PTP (loss) carryforward

Line 6 + Line 7. If greater than zero, enter -0-. A negative amount carries to next year's line 7 (i8995, Line 17).

---

## After the form

- **Attach Form 8995 to Form 1040** when filing — it is not standalone
- **Track carryforwards** in the workpapers for next year: line 16 and line 17
- **Reconcile Line 15 with Form 1040 line 13a** — they must match

---

## Year-over-year reconciliation

If the user files Form 8995 in consecutive years, verify:

- Line 3 on this year's form = last year's line 16
- Line 7 on this year's form = last year's line 17
- Filing status hasn't changed mid-year (if so, document the change)
- Threshold compliance — taxable income still at or below the threshold for the year ($197,300 / $394,600 MFJ for 2025; $201,750 / $201,775 MFS / $403,500 MFJ for 2026)

---

## Edge cases

### Filer is a beneficiary of a trust or estate with QBI

Trust/estate K-1 (Schedule K-1, Form 1041) reports Section 199A information in Box 14, code I. Treat the same as partnership K-1 — list the trust/estate name in column (a), the trust/estate EIN in column (b), the QBI amount in column (c).

### Filer has §199A aggregation election

If the filer aggregates two or more trades or businesses under Treas. Reg. §1.199A-4, list the aggregation as a single row using the aggregation name ("Aggregation 1"), leave column (b) blank, and attach Schedule B (Form 8995-A) or a similar schedule (i8995, Line 1). Aggregations must be reported consistently in later years.

### Filer has prior-year loss but no current-year QBI

Rows 1i–1v will be empty. Enter the loss carryforward on Line 3. Line 4 = 0, Line 16 = the loss (carries again).

### Only REIT/PTP, no QBI

This is valid. Form 8995 is still filed for the REIT/PTP deduction. Line 4 = 0, Line 5 = 0, Line 8 > 0, Line 9 > 0, Line 10 = Line 9.

### Self-employed filer with multiple Schedule Cs

Each Schedule C is a separate trade or business unless aggregated. List each on its own row. Allocate the SE tax adjustment proportionally to each business's share of net profit. See [`qbi-adjustments.md`](./qbi-adjustments.md) for the allocation formula.

### Tax year 2026 and later: $400 minimum deduction

For tax years beginning after December 31, 2025, the deduction is the greater of the computed amount or $400 for a taxpayer whose aggregate QBI from all active qualified trades or businesses (material participation under §469(h)) is at least $1,000 (IRC §199A(i), added by P.L. 119-21 §70105; Rev. Proc. 2025-32 §2.12). The 2026 draft form computes it on new lines 15–17. Ask whether the user materially participates; do not assume.
