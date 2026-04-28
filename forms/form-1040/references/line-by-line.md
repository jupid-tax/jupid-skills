# Form 1040 Line-by-Line Reference

Complete lookup for every line on Form 1040 page 1 and page 2. Use this when the agent needs to confirm where a number belongs or what a line means. Tax year 2025 figures from Rev. Proc. 2024-40; tax year 2026 figures must be verified against the latest IRS Revenue Procedure (typically released October–November 2025).

---

## Header (top of page 1)

### Filing status

Check exactly one box:

| Box | Status |
|-----|--------|
| 1 | Single |
| 2 | Married filing jointly (MFJ) |
| 3 | Married filing separately (MFS) — also enter spouse's name + SSN |
| 4 | Head of household (HoH) — qualifying person required |
| 5 | Qualifying surviving spouse (QSS) — must have dependent child; available the two years after spouse's death |

See [`filing-status.md`](./filing-status.md) for eligibility rules.

### Personal info

| Field | What goes here | Notes |
|-------|----------------|-------|
| Your first name + MI | Filer's legal first name and middle initial | Must match SSA records exactly. Wrong middle initial = e-file rejection. |
| Your last name | Filer's legal last name | Hyphenated, suffixes (Jr/Sr) per SSA |
| Your SSN | 9-digit SSN or ITIN | If ITIN, certain credits limited |
| Spouse first name + MI | Spouse legal first name | Required if MFJ or MFS |
| Spouse last name | Spouse legal last name | |
| Spouse SSN | 9-digit | |
| Home address | Street + apt | Where IRS mails correspondence |
| City, State, ZIP | | |
| Foreign country / province / postal code | Only if foreign | |
| Presidential Election Campaign | $3 designation, no tax impact | Check or leave blank |
| Digital assets | Yes/No | Yes if sold/exchanged/disposed of any crypto/NFT/digital asset; No if only held, received as gift, or transferred between own wallets |

### Standard deduction checkboxes

Check if any apply:
- "Someone can claim you as a dependent"
- "Someone can claim your spouse as a dependent" (MFJ/MFS)
- "Spouse itemizes on a separate return or you were a dual-status alien"

These reduce the standard deduction. A dependent's standard deduction for 2025 = greater of $1,350 or earned income + $450, capped at the regular standard deduction.

### Age/blindness

- "You: Were born before January 2, 1961" — adds the additional standard deduction
- "You: Are blind"
- "Spouse: Were born before January 2, 1961"
- "Spouse: Is blind"

For 2025: additional standard deduction is $1,600 each (MFJ/QSS) or $2,000 each (Single/HoH). MFS: $1,600 if spouse can be claimed; otherwise $2,000.

### Dependents grid

For each dependent (up to 4 on the form; attach a list for more):

| Field | What goes here |
|-------|----------------|
| First name + last name | Legal name |
| SSN | Required for CTC; ATIN/ITIN limits credit eligibility |
| Relationship | "Son", "Daughter", "Mother", "Niece", etc. |
| CTC checkbox | Check if qualifying child under 17 with valid SSN |
| ODC checkbox | Check if dependent doesn't qualify for CTC but does qualify for $500 Credit for Other Dependents |

See [`dependents.md`](./dependents.md) for the qualifying child / qualifying relative tests.

---

## Page 1 — Income (Lines 1-9)

### Line 1 — Wages and earned income (1a-1z)

| Sub-line | Field | What goes here |
|----------|-------|----------------|
| 1a | Total amount from Form(s) W-2, box 1 | Sum of all W-2 box 1 (federal wages, not state). For multiple W-2s, add box 1 across all. |
| 1b | Household employee wages not reported on W-2 | Wages > $50/quarter from being a household employee not reported on W-2. Rare. |
| 1c | Tip income not reported to employer | Cash tips not given to employer for inclusion in W-2. |
| 1d | Medicaid waiver payments not reported on W-2 | Notice 2014-7 in-home services payments excluded from box 1. |
| 1e | Taxable dependent care benefits | From Form 2441, Line 26. Excess over the exclusion limit. |
| 1f | Employer-provided adoption benefits | From Form 8839, Line 29. |
| 1g | Wages from Form 8919, line 6 | Misclassified worker uncollected SS/Medicare. Filer files Form 8919 to claim employee status. |
| 1h | Other earned income | Catch-all: foreign earned income before exclusion, disability pension if under retirement age, scholarships not used for tuition, household employee tips, etc. |
| 1i | Nontaxable combat pay election | For EITC computation. Combat pay is not taxable but can elect to include for EITC purposes. |
| 1z | **Total** | Sum of 1a-1h. (1i is informational, not added.) |

If self-employed only, Line 1 = $0. Self-employment income flows through Schedule C → Schedule 1 Line 3 → 1040 Line 8.

### Line 2 — Interest

| Sub-line | What goes here |
|----------|----------------|
| 2a | Tax-exempt interest. Mostly municipal bond interest (1099-INT box 8). Informational; not added to taxable income but used in MAGI calculations and Social Security taxability worksheet. |
| 2b | Taxable interest. 1099-INT box 1, brokerage 1099-B interest, accrued bond interest, business savings interest if not on Schedule C. |

If 2a + 2b > $1,500 OR foreign accounts, Schedule B required.

### Line 3 — Dividends

| Sub-line | What goes here |
|----------|----------------|
| 3a | Qualified dividends. 1099-DIV box 1b. Taxed at LTCG rates (0/15/20%). Most US C-corp dividends after holding period. |
| 3b | Ordinary dividends. 1099-DIV box 1a. Includes qualified — 3b is the total, 3a is the qualified subset. |

If 3b > $1,500, Schedule B required.

### Line 4 — IRA distributions

| Sub-line | What goes here |
|----------|----------------|
| 4a | Gross IRA distributions. 1099-R box 1, code 1/7/2/etc. Includes Roth and traditional. |
| 4b | Taxable amount. 1099-R box 2a if box 2b ("taxable amount not determined") is unchecked. Roth qualified distributions = 0. Backdoor Roth conversions go on Form 8606. |

### Line 5 — Pensions and annuities

| Sub-line | What goes here |
|----------|----------------|
| 5a | Gross pension/annuity. 1099-R box 1 for distribution code 7. |
| 5b | Taxable amount. Use Simplified Method or General Rule worksheet if box 2a unfilled. |

### Line 6 — Social Security

| Sub-line | What goes here |
|----------|----------------|
| 6a | Gross SS benefits. SSA-1099 box 5 (or RRB-1099). |
| 6b | Taxable SS. Compute via Social Security Benefits Worksheet (1040 instructions). 0 / 50% / 85% depending on combined income (AGI before SS + tax-exempt interest + half of SS) vs. base amounts: $25,000 / $34,000 single, $32,000 / $44,000 MFJ. |
| 6c | Lump-sum election checkbox. Rare — for retroactive lump-sum SS payments allocated across prior years. |

### Line 7 — Capital gain or loss

From Schedule D Line 16. If no Schedule D required (only capital gain distributions on 1099-DIV box 2a, no other transactions), enter from box 2a directly and check the "no Schedule D required" box.

Capital loss limited to $3,000 per year ($1,500 MFS). Excess carries forward.

### Line 8 — Additional income from Schedule 1

From Schedule 1 Line 10. Includes:
- Schedule C net profit (Schedule 1 Line 3)
- Rental, royalty, K-1 (Schedule 1 Line 5, from Schedule E)
- Farm (Schedule 1 Line 6, from Schedule F)
- Unemployment (Schedule 1 Line 7)
- Gambling winnings (Schedule 1 Line 8b)
- Alimony received pre-2019 divorce (Schedule 1 Line 2a)
- Cancellation of debt (Schedule 1 Line 8c)
- Jury duty (Schedule 1 Line 8h)
- Other miscellaneous income

### Line 9 — Total income

Sum: 1z + 2b + 3b + 4b + 5b + 6b + 7 + 8.

This is **gross income** before adjustments.

---

## AGI to taxable income (Lines 10-15)

### Line 10 — Adjustments to income

From Schedule 1 Line 26. Above-the-line deductions. Common items:
- L11 Educator expenses (up to $300; $600 MFJ if both educators)
- L13 HSA deduction (Form 8889)
- L14 Moving expenses (military only post-TCJA)
- L15 Deductible half of SE tax (Schedule SE Line 13)
- L16 Self-employed retirement plan (SEP / SIMPLE / Solo 401(k))
- L17 Self-employed health insurance
- L18 Penalty on early withdrawal of savings
- L19 Alimony paid (pre-2019 divorces)
- L20 IRA deduction
- L21 Student loan interest (up to $2,500; phased out at higher AGI)
- L24 Other adjustments

### Line 11 — Adjusted Gross Income (AGI)

Line 9 − Line 10. **The most important number on the return.** Base for:
- Medicare premium calculations (IRMAA)
- Financial aid (FAFSA)
- State income tax in many states
- Roth IRA contribution eligibility (phaseouts)
- ACA premium tax credit (within MAGI)
- Dozens of phaseout thresholds (CTC, EITC, education credits, etc.)

### Line 12 — Standard or itemized deduction

For tax year 2025 (Rev. Proc. 2024-40):

| Status | Standard deduction |
|--------|--------------------|
| Single | $15,000 |
| MFS | $15,000 |
| MFJ | $30,000 |
| Qualifying Surviving Spouse | $30,000 |
| Head of Household | $22,500 |

Additional for 65+ or blind:
- $1,600 each (MFJ, MFS, QSS)
- $2,000 each (Single, HoH)

For 2026, verify Rev. Proc. 2025-XX (typically announced October–November 2025).

If itemizing instead, enter Schedule A Line 17. Itemize when total Schedule A items exceed the standard deduction. Most filers (~90% post-TCJA) take the standard.

If "Someone can claim you as a dependent" was checked, the standard deduction is the greater of $1,350 (2025) or earned income + $450, capped at the regular standard deduction. Verify 2026 figures.

### Line 13 — QBI deduction

From Form 8995 (simplified) or Form 8995-A (full).

Up to 20% of qualified business income from:
- Schedule C profit
- Schedule E passthrough (K-1 from partnership / S-corp)
- Qualifying REIT dividends (1099-DIV box 5)
- Qualifying PTP income

Below the income threshold ($241,950 single / $383,900 MFJ for 2025; verify 2026), use Form 8995. Above threshold, use Form 8995-A — SSTB phaseouts and W-2 wage / UBIA limits apply.

QBI deduction = lesser of (20% × QBI) or (20% × (taxable income before QBI − net capital gains)).

Made permanent by OBBBA 2025.

### Line 14 — Sum of 12 + 13

Total deductions before applying to taxable income.

### Line 15 — Taxable income

Line 11 − Line 14. If negative, enter 0. **The number tax is calculated on.**

---

## Page 2 — Tax, Credits, Payments

### Line 16 — Tax

Compute tax on Line 15 using:
- **Tax Tables** if Line 15 < $100,000 — look up bracket in 1040 instructions
- **Tax Computation Worksheet** if Line 15 ≥ $100,000
- **Qualified Dividends and Capital Gain Tax Worksheet** if 3a > 0 OR Line 7 has net LTCG — uses preferential 0/15/20% LTCG rates
- **Schedule D Tax Worksheet** if 28%-rate gain (collectibles) or unrecaptured §1250 gain
- **Form 8814** if reporting child's interest/dividends
- **Form 4972** if lump-sum distribution from a qualified retirement plan

Check the appropriate box on Line 16 indicating which method.

See [`tax-computation.md`](./tax-computation.md).

### Line 17 — Other taxes from Schedule 2 Line 3

Schedule 2 Part I:
- Alternative Minimum Tax (Form 6251)
- Excess advance premium tax credit repayment (Form 8962)

Most filers owe $0 here.

### Line 18 — Sum of 16 + 17

Total tax before credits.

### Line 19 — CTC / ODC

From Schedule 8812.

For each qualifying child under 17 at year-end with a valid SSN: up to **$2,000** Child Tax Credit (2025).
For other dependents (children 17+, parents, qualifying relatives): **$500** Credit for Other Dependents (2025).

Phaseout: $50 per $1,000 of AGI over $200,000 single / $400,000 MFJ.

Non-refundable portion (capped at the tax on Line 18 minus other credits) goes here. Refundable portion (up to $1,700 per child for 2025) goes on Line 28.

See [`credits-overview.md`](./credits-overview.md).

### Line 20 — Other credits from Schedule 3 Line 8

Schedule 3 Part I non-refundable credits:
- L1 Foreign tax credit (Form 1116, or directly if < $300/$600)
- L2 Dependent care credit (Form 2441)
- L3 Education credits non-refundable portion (Form 8863)
- L4 Retirement savings contributions credit "Saver's Credit" (Form 8880)
- L5 Residential energy credits (Form 5695)
- L6a Business credits (Form 3800)
- L6b–L6m Other specific credits

### Line 21 — Subtract

Line 18 − (Line 19 + Line 20). Floor at 0.

### Line 22 — Other taxes from Schedule 2 Line 21

Schedule 2 Part II:
- L4 Self-employment tax (Schedule SE)
- L8 Additional tax on early IRA distribution (Form 5329)
- L9 Household employment taxes (Schedule H)
- L11 Additional Medicare Tax (Form 8959)
- L12 Net Investment Income Tax (Form 8960)
- L13 Section 965 deferred foreign income
- L14–L17 Other specific additional taxes
- L18 First-time homebuyer credit recapture
- L19 Recapture of other credits

For self-employed filers, Line 22 is usually the largest line on page 2 (SE tax = 15.3% × 92.35% × Schedule C profit, up to the SS wage base).

### Line 23 — Total tax

Line 21 + Line 22. **Total federal tax liability for the year.**

### Line 24 — (Reserved for future use)

The IRS reserves line numbers for future credits/taxes. Skip.

### Line 25 — Federal income tax withheld

| Sub-line | Source |
|----------|--------|
| 25a | W-2 box 2 sum across all W-2s |
| 25b | 1099 box 4 sum (1099-NEC, 1099-MISC, 1099-R, etc.) |
| 25c | Other forms — W-2G gambling withholding, Schedule K-1 backup withholding, 1042-S, etc. |

### Line 26 — 2025 estimated tax payments + prior year overpayment applied

Sum of:
- All quarterly Form 1040-ES payments made for the tax year
- Any prior-year refund elected to be applied to current year (from prior-year 1040 Line 36)

### Line 27 — EITC

Refundable credit for low-to-moderate income workers. From EIC tables (1040 instructions). Computed based on:
- Filing status
- Number of qualifying children (0, 1, 2, 3+)
- Earned income
- AGI

Maximum 2025 EITC: ~$8,046 for filers with 3+ qualifying children. Phaseouts vary by status and number of children.

Investment income limit for 2025: ~$11,950 (verify). Above this, no EITC.

### Line 28 — Additional Child Tax Credit

The refundable portion of CTC. Up to $1,700 per child for 2025 (verify 2026). Computed on Schedule 8812 Line 27.

### Line 29 — Refundable AOTC

40% of the American Opportunity Tax Credit, up to $1,000 per eligible student. From Form 8863 Line 8.

The other 60% (up to $1,500) is non-refundable and lands on Line 20 via Schedule 3 Line 3.

### Line 30 — (Reserved for future use)

Skip.

### Line 31 — Other payments and refundable credits from Schedule 3 Line 15

Schedule 3 Part II:
- L9 Net premium tax credit (Form 8962)
- L10 Amount paid with extension request (Form 4868)
- L11 Excess Social Security and tier 1 RRTA tax withheld (when filer had multiple employers and combined SS wages exceeded the wage base)
- L12 Credit for federal tax on fuels (Form 4136)
- L13a-L13z Other refundable credits

### Line 32 — Total other payments and refundable credits

Lines 27 + 28 + 29 + 31.

### Line 33 — Total payments

Lines 25a + 25b + 25c + 26 + 32.

### Line 34 — Overpayment (refund)

If Line 33 > Line 23: Line 33 − Line 23 = total overpayment.

### Lines 35a-35d — Direct deposit

| Sub-line | What goes here |
|----------|----------------|
| 35a | Amount of Line 34 to be refunded to taxpayer (via check or direct deposit) |
| 35b | Bank routing number (9 digits) |
| 35c | Type — Checking or Savings |
| 35d | Account number |

If splitting refund across multiple accounts, attach Form 8888.

### Line 36 — Applied to next year's estimated tax

Amount of Line 34 the taxpayer wants applied to next year's quarterly estimates.

Line 35a + Line 36 = Line 34.

### Line 37 — Amount you owe

If Line 23 > Line 33: Line 23 − Line 33 = balance due. Pay by April 15 to avoid late-payment interest and penalty.

### Line 38 — Estimated tax penalty

If quarterly estimates were underpaid during the year, IRS calculates a penalty using **Form 2210**.

Leave Line 38 blank to let the IRS calculate. Or compute on Form 2210 if claiming the annualized income exception (income arrived unevenly through the year) or wanting to verify the IRS number.

Safe harbor: pay during the year either 90% of current-year tax OR 100% of prior-year tax (110% if AGI > $150,000). If safe harbor met, no penalty.

### Signing

Both spouses sign on MFJ. Date. Occupation. Daytime phone. PIN if e-filing. If a paid preparer prepared the return, they sign too.

---

## Cross-line flows (most common)

| Source | Destination |
|--------|-------------|
| W-2 box 1 sum | Line 1a → Line 1z |
| W-2 box 2 sum | Line 25a |
| 1099-NEC/1099-K (self-employment) | Schedule C Line 1 → Line 31 → Schedule 1 Line 3 → Line 10 → 1040 Line 8 |
| Schedule C Line 31 (SE earnings) | Schedule SE Line 12 → SE tax Line 12 → Schedule 2 Line 4 → 1040 Line 22 |
| Schedule SE Line 13 (half SE tax) | Schedule 1 Line 15 → 1040 Line 10 (reduces AGI) |
| 1099-INT box 1 | Line 2b |
| 1099-DIV box 1a | Line 3b |
| 1099-DIV box 1b | Line 3a |
| 1099-B / Form 8949 | Schedule D → Line 7 |
| 1099-R box 2a | Line 4b or 5b |
| SSA-1099 box 5 | Line 6a; Line 6b via worksheet |
| Form 8995 Line 15 | 1040 Line 13 |
| Schedule 8812 Line 14 | 1040 Line 19 |
| Schedule 8812 Line 27 | 1040 Line 28 |
| Form 8863 Line 19 | Schedule 3 Line 3 → 1040 Line 20 |
| Form 8863 Line 8 | 1040 Line 29 |
| Form 2441 Line 11 | Schedule 3 Line 2 → 1040 Line 20 |
| Form 8889 Line 13 | Schedule 1 Line 13 → 1040 Line 10 |
| Form 4868 payment | Schedule 3 Line 10 → 1040 Line 31 |
