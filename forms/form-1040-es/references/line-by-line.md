# Form 1040-ES Line-by-Line Reference

Complete walkthrough of every line on the 2026 Estimated Tax Worksheet (page 11 of the 2026 f1040es.pdf, package dated Feb 12, 2026) and every field on the four payment vouchers (the last pages of the PDF). Re-check the next year's package at https://www.irs.gov/forms-pubs/about-form-1040-es.

Form 1040-ES is unusual: the worksheet is for the user's records (not filed), and only the four vouchers are mailed (and only when paying by check). The agent uses the worksheet to compute the per-quarter installment.

---

## 2026 Estimated Tax Worksheet

### Line 1 — Adjusted Gross Income expected

Sum of all income the taxpayer expects, minus above-the-line adjustments:

**Income**:
- W-2 wages
- Schedule C net profit (after all expenses)
- Schedule E net rental, royalty, K-1 income
- Schedule F net farm profit
- Interest, dividends, capital gain (from sales projected for the year)
- Pension, IRA, 401(k) distributions
- Social Security (taxable portion)
- Roth conversion amount (fully taxable in year converted)
- Alimony from pre-2019 divorces (post-2018 alimony is not income to recipient)
- Unemployment compensation
- Gambling winnings, prize money

**Above-the-line adjustments** (Schedule 1 Part II):
- Educator expenses (up to $350 for 2026 — Rev. Proc. 2025-32 §4.12; $300 for 2025)
- HSA contribution
- Self-employed health insurance
- Half of self-employment tax (2026 SE Tax and Deduction Worksheet line 11)
- SEP-IRA, SIMPLE, solo 401(k) contributions (employer side)
- Self-employed retirement plan contributions
- Student loan interest (up to $2,500, verify 2026 phase-out)

**Critical**: do NOT include Roth IRA contributions (not deductible). Do NOT include traditional IRA contributions if covered by employer plan and over phase-out.

### Line 2a — Deductions

Pick the larger of:

- **Standard deduction** for 2026 (2026 Form 1040-ES What's New; Rev. Proc. 2025-32 §4.14):
  - Single or MFS: $16,100
  - MFJ or QSS: $32,200
  - HOH: $24,150
  - Additional for 65+ or blind: $1,650 each (married/QSS); $2,050 each (unmarried)
  - Plus, for non-itemizers, up to $1,000 ($2,000 MFJ) of cash charitable contributions (new for 2026)
- **Itemized deduction** estimate (if user expects to itemize): SALT (capped at $40,400 for 2026 under IRC §164(b)(7), reduced by 30% of MAGI over $505,000 but not below $10,000; the 2026 Form 1040-ES What's New prints the 2025 figures, $40,000 / $500,000), mortgage interest, charitable (only the part above 0.5% of AGI for 2026), medical > 7.5% AGI. For 2026, total itemized deductions are reduced by 5.4% of the lesser of itemized deductions or taxable income above $640,600 single/HOH ($768,700 MFJ; $384,350 MFS).

Use whichever is larger.

### Line 2b — QBI deduction

20% of qualified business income from pass-through entities (Schedule C, partnership, S-corp, sole proprietorship, certain rental). Subject to taxable-income thresholds and SSTB limitations under IRC §199A, which P.L. 119-21 made permanent.

For 2026: threshold $201,750 single/HOH ($403,500 MFJ; $201,775 MFS), phase-in range ending at $276,750 ($553,500 MFJ) — Rev. Proc. 2025-32 §4.26. New for 2026: a minimum $400 deduction if the user has at least $1,000 of QBI from an active trade or business (2026 Form 1040-ES What's New). (2025: $197,300 / $394,600 thresholds, Rev. Proc. 2024-40.)

If the user has straightforward QBI under threshold, simply: 20% × min(QBI, taxable income before QBI excluding net capital gain). If over threshold, use Form 8995-A or punt to a CPA (see [`../../form-8995-a/SKILL.md`](../../form-8995-a/SKILL.md)).

### Line 2c — Schedule 1-A deductions

Estimated Schedule 1-A (Form 1040) line 38: qualified tips (up to $25,000), qualified overtime (up to $12,500; $25,000 MFJ), qualified passenger vehicle loan interest (up to $10,000), enhanced deduction for seniors ($6,000 per eligible spouse, born before January 2, 1962 for 2026), each with MAGI phase-outs (2026 Form 1040-ES What's New).

### Line 2d — Add lines 2a, 2b, and 2c

### Line 3 — Taxable income

`Line 1 − Line 2d`. If negative, enter 0.

### Line 4 — Tax from rate schedule

Apply the **2026 Tax Rate Schedules** printed in the 2026 Form 1040-ES (page 9; Rev. Proc. 2025-32) to Line 3.

2026 single (Schedule X):
- 10%: $0 – $12,400
- 12%: $12,400 – $50,400
- 22%: $50,400 – $105,700
- 24%: $105,700 – $201,775
- 32%: $201,775 – $256,225
- 35%: $256,225 – $640,600
- 37%: $640,600+

MFJ (Schedule Y-1): 10% to $24,800; 12% to $100,800; 22% to $211,400; 24% to $403,550; 32% to $512,450; 35% to $768,700; 37% above. HOH and MFS: read Schedules Z and Y-2 on the same page.

**Special rate handling**:
- Long-term capital gain & qualified dividend: separate 0% / 15% / 20% rates per IRC §1(h); for 2026 the 0% rate applies up to $49,450 of taxable income single ($98,900 MFJ; $66,200 HOH) and 15% up to $545,500 single ($613,700 MFJ; $579,600 HOH) — Rev. Proc. 2025-32 §4.03. Use the Pub. 505 worksheet instead of the regular schedule.
- Section 1250 unrecaptured gain: 25% max
- Collectibles gain: 28% max

### Line 5 — Alternative Minimum Tax (AMT)

If applicable (Form 6251). Most filers under the 2026 AMT exemption ($90,100 single / $140,200 MFJ, phasing out at 50 cents per dollar above $500,000 / $1,000,000 — Rev. Proc. 2025-32 §4.10) will not owe AMT. High earners with significant ISO exercises, large SALT deductions (cap raised to $40,400 for 2026), or complex deductions may.

### Line 6 — Add Lines 4 and 5

### Line 7 — Credits

Project nonrefundable credits the user expects:

- Child Tax Credit: $2,200 per qualifying child under 17 for 2026 (Rev. Proc. 2025-32 §4.05; valid SSN required)
- Credit for Other Dependents: $500 per non-CTC dependent
- Foreign Tax Credit (Form 1116)
- Retirement Savings Contributions Credit (Form 8880)
- Child & Dependent Care Credit (Form 2441) — maximum credit rate 50% for 2026
- Lifetime Learning Credit (Form 8863) up to $2,000
- American Opportunity Credit (Form 8863) up to $2,500 (valid SSN required from 2026)
- NOT available for 2026: new / previously owned / commercial clean vehicle credits, energy efficient home improvement credit, residential clean energy credit (2026 Form 1040-ES, line 7 instructions)

### Line 8 — Subtract Line 7 from Line 6

### Line 9 — Self-employment tax

Computed with the 2026 Self-Employment Tax and Deduction Worksheet (page 8 of the 2026 Form 1040-ES), which mirrors Schedule SE:

```
SE_earnings = 0.9235 × net SE income (Schedule C profit + partnership SE income)
SS_portion = 0.124 × min(SE_earnings, SS_wage_base)
Medicare_portion = 0.029 × SE_earnings
SE_tax = SS_portion + Medicare_portion
```

For 2026: SS wage base = $184,500 (SE worksheet line 5; SSA). For 2025: $176,100.

If wages already at SS wage base from W-2 employment, no SS portion on SE income (only the 2.9% Medicare portion).

### Line 10 — Other taxes

Per the line 10 instructions, include the taxes that would go on Schedule 2 (Form 1040) lines 8 through 12, 14 through 17z, and 19, except household employment taxes (include only if the user has withholding or would otherwise need estimates) and the "Exception 2" taxes not due until the return date (Schedule 2 lines 13, 17b, 17k, 17m). Common items:

- **Additional Medicare 0.9%** (Form 8959): on wages + SE earnings above:
  - Single / HOH / QSS $200,000
  - MFJ $250,000
  - MFS $125,000
- **NIIT 3.8%** (Form 8960): on lesser of net investment income or MAGI excess over threshold ($200,000 single/HOH; $250,000 MFJ/QSS; $125,000 MFS). Investment income includes interest, dividends, capital gains, rental income (passive), royalties.
- **Additional tax on IRAs / retirement plans** (Schedule 2 line 8), e.g., 10% early-distribution tax

### Line 11a — Total tax

`Line 8 + Line 9 + Line 10`

### Line 11b — Refundable credits

- Earned Income Credit
- Additional Child Tax Credit (up to $1,700 per child for 2026)
- Fuel tax credit
- Net Premium Tax Credit (2026: no PTC above 400% FPL; no cap on excess-APTC repayment)
- American Opportunity Credit (40% refundable)
- Refundable adoption credit (up to $5,120 per child for 2026)
- Section 1341 credit

### Line 11c — Total 2026 estimated tax

`Line 11a − Line 11b` (not below zero). This is the figure used in the safe harbor.

### Line 12a — 90% safe harbor target

`0.90 × Line 11c` (66⅔% if at least two-thirds of gross income for 2025 or 2026 is from farming or fishing)

### Line 12b — Prior-year safe harbor target

```
prior_year_tax × (1.10 if prior_AGI > 150,000 (or 75,000 MFS) else 1.00)
```

The "tax" here is the 2025 Form 1040 Line 24, reduced by Schedule 2 lines 5 and 6, certain Schedule 2 line 8 taxes on excess contributions/accumulations, the Exception 2 taxes (Schedule 2 lines 13, 17b, 17k, 17m), and refundable credits on Form 1040 lines 27a, 28, 29, 30 and Schedule 3 lines 9 and 12 (2026 Form 1040-ES, "Figuring your 2025 tax"). The 110% rule does not apply to qualifying farmers/fishers.

**Edge cases**: if the user didn't file a 2025 return or the 2025 tax year was less than 12 months, skip Line 12b and use Line 12a. Joint 2026 / separate 2025 (or the reverse): follow the combination and allocation rules in the line 12b instructions.

### Line 12c — Required annual payment

`min(Line 12a, Line 12b)`. The taxpayer pays at least this much across the year (via withholding + estimated payments) to avoid §6654 penalty.

### Line 13 — Income tax withheld (expected)

Sum of:
- Federal withholding from W-2 (estimate based on YTD pay stub × 12/months-elapsed)
- Withholding from 1099-R pension distributions
- Voluntary withholding from Social Security (Form W-4V)
- Withholding from gambling winnings (W-2G) or backup withholding from 1099s
- Additional Medicare Tax withholding (counts here too)

Withholding is treated as paid evenly across the year per IRC §6654(g), even if actually withheld in Q4. This is a powerful planning lever — if the user can increase W-2 withholding late in the year, it counts as evenly distributed.

### Line 14a — Subtract Line 13 from Line 12c

`Line 12c − Line 13`. If ≤ $0, stop: no estimated payments required.

### Line 14b — Subtract Line 13 from Line 11c

`Line 11c − Line 13`. If less than $1,000, stop: no estimated payments required (the §6654(e)(1) de minimis rule).

### Line 15 — Installment amount

`¼ × Line 14a`, minus any 2025 overpayment applied to the installment (equal-installment method). This is the amount written on each of the four payment vouchers (Q1, Q2, Q3, Q4) if paying by check.

---

## Payment vouchers (last pages of the 2026 f1040es.pdf)

Each voucher has identical fields. Voucher number 1, 2, 3, or 4 is preprinted; the agent does not change it.

| Field | What goes here | Notes |
|-------|----------------|-------|
| Calendar year (top) | "2026" (or write in the year) | Matches the tax year |
| Voucher number | Preprinted (1, 2, 3, or 4) | |
| Amount of payment | From Line 15 (or adjusted for unequal installments) | Whole dollars + cents allowed |
| Filer's first name + initial + last name | Full legal name | Match SSA records |
| Filer's SSN | 9 digits | |
| If joint, spouse's first name + initial + last name | Match SSA records | Only if MFJ |
| If joint, spouse's SSN | 9 digits | Only if MFJ |
| Address | Street | |
| City, State, ZIP | Current mailing address | |
| Foreign country, province, postal code | Only if foreign address | |

The voucher is mailed with a check made out to "United States Treasury". Memo line: "2026 Form 1040-ES" + SSN. 2026 addresses: residents of AL, AK, AZ, CA, CO, FL, GA, HI, ID, KS, LA, MI, MS, MT, NE, NV, NM, NC, ND, OH, OR, PA, SC, SD, TN, TX, UT, WA, WY → Internal Revenue Service, P.O. Box 1300, Charlotte, NC 28201-1300; AR, CT, DE, DC, IL, IN, IA, KY, ME, MD, MA, MN, MO, NH, NJ, NY, OK, RI, VT, VA, WV, WI → Internal Revenue Service, P.O. Box 931100, Louisville, KY 40293-1100; foreign country, American Samoa, Puerto Rico, APO/FPO, Form 2555/4563 filers, dual-status aliens → P.O. Box 1303, Charlotte, NC 28201-1303 (2026 Form 1040-ES, "Where To File Your Estimated Tax Payment Voucher"). Re-verify each year.

If paying electronically, the voucher is **not** mailed.

---

## Due dates for tax year 2026

| Voucher | Period covered | Due date |
|---------|----------------|----------|
| 1 | Jan 1 – Mar 31, 2026 | April 15, 2026 |
| 2 | Apr 1 – May 31, 2026 | June 15, 2026 |
| 3 | Jun 1 – Aug 31, 2026 | September 15, 2026 |
| 4 | Sep 1 – Dec 31, 2026 | January 15, 2027 |

**Verify each year**: when a due date falls on a Saturday, Sunday, or legal holiday (DC and federal), the deadline shifts to the next business day per IRC §7503. Reconfirm against the IRS calendar before filing.

**Special rules**:
- **Farmers/fishers** (>2/3 gross from farming/fishing per IRC §6654(i)): single payment due Jan 15, 2027 OR file & pay by March 1, 2027.
- **Filing the 2026 return by February 1, 2027 with full payment**: replaces the Q4 voucher (per IRC §6654(h); 2026 Form 1040-ES, Payment Due Dates).
- **Disaster relief**: when IRS announces a disaster postponement, due dates may shift; check https://www.irs.gov/newsroom/tax-relief-in-disaster-situations.

---

## Worksheet computation order (algorithm summary)

```
1. AGI = sum of all income − above-the-line adjustments
2. Taxable income = AGI − standard/itemized deduction − QBI − Schedule 1-A deductions
3. Tentative tax = bracket(taxable_income, filing_status, tax_year)
4. Add AMT if applicable
5. Subtract nonrefundable credits
6. Add SE tax (from Schedule SE)
7. Add other taxes (Add'l Medicare, NIIT, etc.)
8. = total_tax
9. Subtract refundable credits → net_total_tax
10. safe_harbor_90 = 0.90 × net_total_tax
11. safe_harbor_prior = prior_tax × (1.10 if high-AGI else 1.00)
12. required = min(safe_harbor_90, safe_harbor_prior)
13. net_estimated = required − expected_withholding   (≤ 0 → no estimates)
14. if net_total_tax − expected_withholding < 1,000 → no estimates
15. per_quarter = net_estimated / 4
```

The agent runs this algorithm with the user's numbers and surfaces the result for each line as shown in the SKILL.md output template.
