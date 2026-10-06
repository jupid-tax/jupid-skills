# Form 8995-A — Line by Line Reference

Complete reference for every line on Form 8995-A and its four schedules. Use as a lookup when implementing Steps 6–8 (loss netting, Parts II–III per business, Part IV) of the workflow.

Verified against the **2025 Form 8995-A** (Created 9/12/25, https://www.irs.gov/pub/irs-pdf/f8995a.pdf), **2025 Schedule A (Form 8995-A)** (Created 12/12/25), **Schedules B, C and D (Form 8995-A) (Rev. December 2022)**, and the **2025 Instructions for Form 8995-A** (Jan 26, 2026, https://www.irs.gov/pub/irs-pdf/i8995a.pdf). The 2026 draft (https://www.irs.gov/pub/irs-dft/f8995a--dft.pdf) uses $201,750 / $201,775 MFS / $403,500 MFJ thresholds, a $75,000 / $150,000 phase-in range, and renumbers the end of Part IV (line 39 deduction before the minimum, line 40 minimum deduction, line 41 total, line 42 carryforward, line 43 ESBT box). Re-check the final revision each year.

Order of work (2025 i8995-A, Specific Instructions): complete Schedule D (patrons), Schedule A (SSTBs in the phase-in range), Schedule B (aggregations) and Schedule C (losses or loss carryforward) as applicable, then Part I.

---

## Part I — Trade, Business, or Aggregation Information

### Line 1, columns (a)–(e), rows A–C

- **(a) Trade, business, or aggregation name** — Business name; for a Schedule B aggregation enter "Aggregation 1, 2, 3"
- **(b) Check if specified service** — SSTB per IRC §199A(d)(2) and Treas. Reg. §1.199A-5(b)(2). See [`sstb-classification.md`](./sstb-classification.md)
- **(c) Check if aggregation** — checked for an aggregation row
- **(d) Taxpayer identification number** — EIN; a disregarded single-member LLC enters its EIN; without an EIN, SSN or ITIN. Leave blank for an aggregation
- **(e) Check if patron** — patron of an agricultural or horticultural cooperative

Three rows fit. With four or more trades or businesses, attach a statement with Parts I, II, and III for the others (i8995-A, Line 2). Only report qualified trades or businesses: an SSTB above the top of the phase-in range is not one.

---

## Part II — Determine Your Adjusted Qualified Business Income (per column A, B, C)

### Line 2 — Qualified business income from the trade, business, or aggregation

| Source | What goes on L2 |
|--------|-----------------|
| Schedule C (sole prop) | Line 31 net profit MINUS allocable ½ SE tax, SE health insurance, SE retirement contributions, and qualified tips deducted under §224 |
| S-corp K-1 | QBI from the box 17 code V statement (already after the corporation's deduction for the owner's wages); minus owner-level items such as a >2% shareholder's SE health insurance deduction |
| Partnership K-1 | QBI from the box 20 code Z statement (guaranteed payments in box 4 are not QBI and are already deducted in box 1); minus partner-level items (½ SE tax on partnership SE income, unreimbursed partnership expenses) |
| Schedule E rental rising to §162 trade/business | Net rental income |
| Rev. Proc. 2019-38 safe harbor rental enterprise | Net rental income (250-hour, separate-books, contemporaneous-records tests, statement attached) |
| SSTB in the phase-in range | Schedule A line 11 |
| Any business when Schedule C (Form 8995-A) is used | Schedule C line 1, column (c) |

Excluded from QBI per Treas. Reg. §1.199A-3(b)(2)(ii) and §199A(c)(4):
- Capital gains and losses
- Dividends (qualified REIT dividends go to Part IV)
- Interest income not allocable to a trade or business
- Reasonable compensation received by an S-corp shareholder
- Guaranteed payments to a partner; §707(a) payments for services
- Income not effectively connected with a US trade or business
- Qualified tips deducted under §224 (2025 and later)

Do not include losses or deductions still suspended under other Code sections (§§163(j), 179, 461(l), 465, 469, 704(d), 1366(d)); they enter QBI in the year allowed (i8995-A, "Determining your QBI").

### Line 3 — Multiply line 2 by 20%

If taxable income is $197,300 or less ($394,600 MFJ) for 2025 (patrons only reach this form at that income), skip lines 4 through 12 and enter line 3 on line 13.

### Line 4 — Allocable share of W-2 wages

W-2 wages of the trade or business (Treas. Reg. §1.199A-2(b); i8995-A "Determining your W-2 wages"):

- Wages paid to employees plus elective deferrals (Form W-2 box 12 codes D, E, F, G, S), figured from Forms W-2 for the calendar year ending with or within the tax year, by the unmodified box method, modified box 1 method, or tracking wages method
- Only wages properly allocable to QBI; amounts on a Form W-2 filed more than 60 days late (including extensions) don't count
- Excludes: statutory employee pay (W-2 box 13 checked), guaranteed payments, payments to independent contractors, amounts deducted under §224 (2025)
- For S-corps: includes the owner-employee's wages from the corporation
- If line 2 is zero for the business, line 4 must be zero

Multiple businesses: allocate W-2 wages to the business that generated the wage expense.

### Line 5 — Multiply line 4 by 50%

### Line 6 — Multiply line 4 by 25%

### Line 7 — Allocable share of UBIA of all qualified property

Unadjusted basis immediately after acquisition (Treas. Reg. §1.199A-2(c); i8995-A "Determining your UBIA"):

- Tangible property subject to depreciation under §167(a), held and used in producing QBI during and at the close of the year
- Excludes: land, intangibles, inventory
- Depreciable period ends on the later of 10 years after first placed in service or the last day of the last full year of the §168(c) recovery period; bonus depreciation doesn't change it
- Basis on the placed-in-service date, not adjusted basis; improvements are separate property
- Property acquired within 60 days of year end and disposed of within 120 days without 45 days of use is generally not qualified property
- Special rules for §1031 / §1033 replacement property and nonrecognition transfers
- If line 2 is zero for the business, line 7 must be zero

### Line 8 — Multiply line 7 by 2.5%

### Line 9 — Add lines 6 and 8

### Line 10 — Enter the greater of line 5 or line 9

The W-2 wage and UBIA limitation amount.

### Line 11 — W-2 wage and UBIA of qualified property limitation

The smaller of line 3 or line 10.

### Line 12 — Phased-in reduction

The amount from Part III line 26, if any. Part III applies only in the phase-in range and only when line 10 is less than line 3.

### Line 13 — QBI deduction before patron reduction

The greater of line 11 or line 12.

### Line 14 — Patron reduction

Schedule D (Form 8995-A) line 6, if any.

### Line 15 — Qualified business income component

Line 13 minus line 14. If zero or less, enter zero.

### Line 16 — Total qualified business income component

Add all line 15 amounts (all columns and any attached statements; complete line 16 only on the first page).

---

## Part III — Phased-in Reduction (per column)

Complete only if 2025 taxable income is more than $197,300 but not more than $247,300 ($394,600 and $494,600 MFJ) **and** line 10 is less than line 3. Applies to non-SSTBs and to SSTBs (after Schedule A).

| Line | Entry |
|------|-------|
| 17 | Amount from line 3 |
| 18 | Amount from line 10 |
| 19 | Line 17 − line 18 |
| 20 | Taxable income before QBI deduction |
| 21 | Threshold: $197,300 ($394,600 MFJ) for 2025 |
| 22 | Line 20 − line 21 |
| 23 | Phase-in range: $50,000 ($100,000 MFJ) for 2025 |
| 24 | Phase-in percentage: line 22 ÷ line 23 |
| 25 | Total phase-in reduction: line 19 × line 24 |
| 26 | Line 17 − line 25; enter here and on line 12 |

---

## Part IV — Determine Your QBI Deduction

### Line 27 — Total QBI component

Line 16.

### Line 28 — Qualified REIT dividends and PTP income or (loss)

- Qualified REIT dividends: Form 1099-DIV box 5 (shares held more than 45 days; not capital gain dividends or qualified dividends)
- Qualified PTP income or loss, including Schedule A line 24 for SSTB PTPs in the phase-in range
- Enter a net loss as a negative number

### Line 29 — Qualified REIT dividends and PTP (loss) carryforward from prior years

Prior-year Form 8995-A line 40 (or Form 8995 line 17), as a negative number.

### Line 30 — Combine lines 28 and 29

If less than zero, enter -0-.

### Line 31 — REIT and PTP component

Line 30 × 20%. Not subject to the W-2/UBIA limit.

### Line 32 — QBI deduction before the income limitation

Line 27 + line 31.

### Line 33 — Taxable income before QBI deduction

2025 Form 1040 / 1040-SR: line 11a minus lines 12e and 13b. Form 1040-NR: line 11a minus lines 12, 13b, and 13c. Form 1041: line 17 minus lines 18, 19, and 21.

### Line 34 — Net capital gain, increased by qualified dividends

Form 1040 line 3a plus net capital gain: the smaller of Schedule D line 15 or 16 (nothing added if either is zero or less), or Form 1040 line 7a if Schedule D isn't required.

### Line 35 — Subtract line 34 from line 33

If zero or less, enter -0-.

### Line 36 — Income limitation

Line 35 × 20%.

### Line 37 — QBI deduction before the DPAD

The smaller of line 32 or line 36.

### Line 38 — DPAD under §199A(g) allocated from a cooperative

Form 1099-PATR box 6. Not more than line 33 minus line 37.

### Line 39 — Total qualified business income deduction

Line 37 + line 38. Enter on 2025 Form 1040 / 1040-SR / 1040-NR line 13a (Form 1041 line 20).

### Line 40 — Total qualified REIT dividends and PTP (loss) carryforward

Combine lines 28 and 29; if zero or greater, enter -0-. Carries to next year's line 29.

---

## Schedule A — Specified Service Trades or Businesses (2025)

Complete only for an SSTB when 2025 taxable income is more than $197,300 but not more than $247,300 ($394,600 / $494,600 MFJ). Up to three columns; attach more Schedules A if needed.

### Part I — Other than PTPs

| Line | Entry |
|------|-------|
| 1a / 1b | Trade or business name / TIN |
| 2 | QBI or (loss) from the trade or business |
| 3 | Allocable share of W-2 wages |
| 4 | Allocable share of UBIA of qualified property |
| 5 | Taxable income before QBI deduction |
| 6 | Threshold: $197,300 ($394,600 MFJ) |
| 7 | Line 5 − line 6 |
| 8 | Phase-in range: $50,000 ($100,000 MFJ) |
| 9 | Line 7 ÷ line 8 |
| 10 | Applicable percentage: 100% − line 9 |
| 11 | Line 2 × line 10 → Schedule C (Form 8995-A) or Form 8995-A line 2 |
| 12 | Line 3 × line 10 → Form 8995-A line 4 |
| 13 | Line 4 × line 10 → Form 8995-A line 7 |

### Part II — Publicly Traded Partnerships

| Line | Entry |
|------|-------|
| 14 / 15 | PTP name / TIN |
| 16 | Qualified PTP income or (loss) |
| 17 | Total PTP SSTB income or (loss) |
| 18–23 | Taxable income, threshold, excess, phase-in range, ratio, applicable percentage (as lines 5–10) |
| 24 | Line 17 × line 23 → include on Form 8995-A line 28 |

A qualified SSTB loss allowed this year from a prior suspended loss is not put on Schedule A; its applicable percentage was fixed in the year incurred (i8995-A).

---

## Schedule B — Aggregation of Business Operations (Rev. December 2022)

One Schedule B per aggregation, numbered 1, 2, 3.

| Line | Entry |
|------|-------|
| 1 | Description of the aggregated trade or business and the factors met under Treas. Reg. §1.199A-4; attach any RPE's aggregation |
| 2 | Has the aggregation changed from the prior year? If yes, explain |
| 3 | Per business: (a) name, (b) TIN, (c) QBI or (loss), (d) W-2 wages, (e) UBIA |
| 4 | Totals of columns (c), (d), (e) → Schedule C (Form 8995-A) or Form 8995-A Part II for that aggregation |

Must be completed every year the aggregation is used. Failure to disclose may cause disaggregation (i8995-A, Aggregation).

---

## Schedule C — Loss Netting and Carryforward (Rev. December 2022)

Required if any trade, business, or aggregation has a qualified business loss this year, or there is a QBI net loss carryforward from prior years (even if the business that generated it no longer exists). Compute line 1 column (a) first, then lines 2–5, then line 1 columns (b) and (c).

| Line | Entry |
|------|-------|
| 1 (a) | QBI or (loss) per trade, business, or aggregation |
| 1 (b) | Reduction for loss netting: line 5 apportioned among businesses with positive QBI in proportion to their QBI |
| 1 (c) | Adjusted QBI: (a) + (b); if zero or less, 0 → Form 8995-A line 2 |
| 2 | QBI net (loss) carryforward from prior years (prior Schedule C line 6, or Form 8995 line 16; plus the QBI portion of previously suspended losses allowed this year) |
| 3 | Total of the losses: negative amounts on line 1(a) plus line 2 |
| 4 | Total of the positive amounts on line 1(a) |
| 5 | Smaller of the absolute value of line 3 or line 4, in parentheses |
| 6 | Carryforward: line 3 − line 5; if zero or more, 0 → next year's Schedule C line 2 or Form 8995 line 3 |

If adjusted QBI for a business is zero or less after netting, its W-2 wages and UBIA are zero on Part II.

---

## Schedule D — Special Rules for Patrons of Agricultural or Horticultural Cooperatives (Rev. December 2022)

| Line | Entry |
|------|-------|
| 1a / 1b | Trade, business, or aggregation name / TIN |
| 2 | QBI allocable to qualified payments from the cooperative (patronage dividends, per-unit retain allocations; Form 1099-PATR box 7) |
| 3 | Line 2 × 9% |
| 4 | W-2 wages (from Form 8995-A line 4) allocable to the qualified payments |
| 5 | Line 4 × 50% |
| 6 | Patron reduction: smaller of line 3 or line 5 → Form 8995-A line 14 |

The §199A(g) deduction passed through by the cooperative (1099-PATR box 6) goes on Form 8995-A line 38, not Schedule D.

---

## Cross-references

- See [`sstb-classification.md`](./sstb-classification.md) for SSTB rules
- See [`sstb-phase-in.md`](./sstb-phase-in.md) for Schedule A and Part III walkthroughs
- See [`qbi-computation.md`](./qbi-computation.md) for QBI mechanics by income type
- See [`aggregation.md`](./aggregation.md) for Schedule B election rules
- See [`loss-netting.md`](./loss-netting.md) for Schedule C of Form 8995-A
