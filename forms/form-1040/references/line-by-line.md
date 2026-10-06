# Form 1040 Line-by-Line Reference

Complete lookup for every line on Form 1040 page 1 and page 2. Use this when the agent needs to confirm where a number belongs or what a line means. The line map was verified against the **2025 Form 1040 (filed in 2026)** and the 2025 Instructions for Form 1040; re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1040 before using it for a 2026 return. Tax year 2025 dollar figures come from Rev. Proc. 2024-40 as changed by P.L. 119-21 (One Big Beautiful Bill Act); tax year 2026 figures come from Rev. Proc. 2025-32.

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
| Main home in the U.S. checkbox | New for 2025 | Check if the main home (and spouse's, if joint) was in the U.S. for more than half of 2025; used for EIC eligibility |
| Deceased / date of death | Top of page 1 | Check and enter the date for a taxpayer or spouse who died before the return was filed |
| Presidential Election Campaign | $3 designation, no tax impact | Check or leave blank |
| Digital assets | Yes/No | Yes if during 2025 the user (a) received a digital asset as a reward, award, or payment for property or services, or (b) sold, exchanged, or otherwise disposed of one; No if only bought with real currency, held, or transferred between own wallets |

The filing status block also has a box to check (with the spouse's name) if treating a nonresident alien or dual-status alien spouse as a U.S. resident for the whole year, and a name line for an HOH/QSS qualifying child who is not your dependent.

### Dependents section

Numbered rows for up to 4 dependents (check the box and attach a statement for more):

| Row | What goes here |
|-----|----------------|
| (1) First name, (2) Last name | Legal name |
| (3) SSN | Required for CTC (SSN valid for employment, issued by the return due date including extensions); ITIN/ATIN allows ODC only. Enter "Died" for a child born and died in 2025 with no SSN and attach proof of live birth |
| (4) Relationship | "Son", "Daughter", "Mother", "Niece", etc. |
| (5)(a) Yes | Lived with you more than half of 2025 |
| (5)(b) And in the U.S. | Lived with you in the U.S. more than half of 2025 (EIC test) |
| (6) Full-time student / Permanently and totally disabled | Check if the age test is met through student status or disability |
| (7) Child tax credit / Credit for other dependents | One box per dependent: CTC for a qualifying child under 17 with the required SSN; ODC ($500) for other dependents who are U.S. citizens, nationals, or resident aliens |

For the CTC/ACTC the filer (or at least one spouse on a joint return) must also have an SSN valid for employment issued by the due date including extensions; the other spouse needs an SSN or ITIN. ODC requires the filer (and spouse) to have an SSN or ITIN by the due date (2025 Instructions for Form 1040, line 19).

Below the rows: a checkbox for MFS or HOH filers who lived apart from the spouse for the last 6 months of 2025 or are legally separated and did not live in the same household at year-end.

See [`dependents.md`](./dependents.md) for the qualifying child / qualifying relative tests.

---

## Page 1 — Income (Lines 1-9)

### Line 1 — Wages and earned income (1a-1z)

| Sub-line | Field | What goes here |
|----------|-------|----------------|
| 1a | Total amount from Form(s) W-2, box 1 | Sum of all W-2 box 1 (federal wages, not state). For multiple W-2s, add box 1 across all. Wages earned while incarcerated go on Schedule 1 line 8u, and nonqualified deferred compensation / nongovernmental 457 pensions reported in box 1 go on Schedule 1 line 8t, not here. |
| 1b | Household employee wages not reported on W-2 | Household-employee wages with no W-2 (an employer need not issue a W-2 if it paid less than $2,800 in 2025). |
| 1c | Tip income not reported on line 1a | Tips not reported to the employer, allocated tips from W-2 box 8 (unless the user can prove less), and noncash tips. SS/Medicare on these goes on Schedule 2 line 5 via Form 4137. |
| 1d | Medicaid waiver payments not reported on W-2 | Taxable Medicaid waiver payments not on a W-2, plus nontaxable ones the user elects to include in earned income for a credit (offset on Schedule 1 line 8s). |
| 1e | Taxable dependent care benefits | From Form 2441, line 26. Excess over the exclusion limit. |
| 1f | Employer-provided adoption benefits | From Form 8839, line 31. |
| 1g | Wages from Form 8919, line 6 | Worker who believes they were misclassified; Form 8919 also computes the employee share of SS/Medicare (Schedule 2 line 6). |
| 1h | Other earned income | Strike or lockout benefits, excess elective deferrals (over $23,500 for 2025, catch-up excluded), disability pensions received before minimum retirement age, corrective distributions of excess deferrals. Scholarships not on a W-2 go on Schedule 1 line 8r instead. |
| 1i | Nontaxable combat pay election | For EIC computation. Combat pay is not taxable but can elect to include for EIC purposes. |
| 1z | **Total** | Sum of 1a-1h. (1i is informational, not added.) |

If self-employed only, Line 1 = $0. Self-employment income flows through Schedule C → Schedule 1 Line 3 → 1040 Line 8.

### Line 2 — Interest

| Sub-line | What goes here |
|----------|----------------|
| 2a | Tax-exempt interest. Mostly municipal bond interest (1099-INT box 8). Informational; not added to taxable income but used in MAGI calculations and Social Security taxability worksheet. |
| 2b | Taxable interest. 1099-INT box 1, brokerage 1099-B interest, accrued bond interest, business savings interest if not on Schedule C. |

If taxable interest (2b) is over $1,500, or the user had a foreign account or a foreign trust, Schedule B is required.

### Line 3 — Dividends

| Sub-line | What goes here |
|----------|----------------|
| 3a | Qualified dividends. 1099-DIV box 1b. Taxed at LTCG rates (0/15/20%). Most US C-corp dividends after holding period. |
| 3b | Ordinary dividends. 1099-DIV box 1a. Includes qualified — 3b is the total, 3a is the qualified subset. |

If 3b is over $1,500 (or the user received ordinary dividends as a nominee), Schedule B is required. 3c: check box 1 / box 2 if a child's qualified / ordinary dividends are included via Form 8814.

### Line 4 — IRA distributions

| Sub-line | What goes here |
|----------|----------------|
| 4a | Gross IRA distributions. 1099-R box 1, code 1/7/2/etc. Includes Roth and traditional. |
| 4b | Taxable amount. 1099-R box 2a if box 2b ("taxable amount not determined") is unchecked. Roth qualified distributions = 0. Backdoor Roth conversions go on Form 8606. |
| 4c | Checkbox 1 Rollover, 2 QCD (qualified charitable distribution), 3 other (e.g., "HFD"). A fully rolled-over distribution shows 4b = 0 with box 1 checked. |

### Line 5 — Pensions and annuities

| Sub-line | What goes here |
|----------|----------------|
| 5a | Gross pension/annuity. 1099-R box 1 for pensions, annuities, and 401(k), 403(b), and governmental 457(b) distributions (IRA distributions go on 4a). |
| 5b | Taxable amount. Use Simplified Method or General Rule worksheet if box 2a unfilled. |
| 5c | Checkbox 1 Rollover, 2 PSO (retired public safety officer insurance premiums), 3 other. |

### Line 6 — Social Security

| Sub-line | What goes here |
|----------|----------------|
| 6a | SS benefits. SSA-1099 box 5 net benefits (or RRB-1099). |
| 6b | Taxable SS. Compute via Social Security Benefits Worksheet (1040 instructions). 0 / up to 50% / up to 85% depending on combined income (other income + tax-exempt interest + half of SS, less most Schedule 1 adjustments) vs. base amounts: $25,000 / $34,000 single, HOH, QSS, or MFS living apart all year; $32,000 / $44,000 MFJ; $0 for MFS who lived with the spouse at any time. |
| 6c | Lump-sum election checkbox. Rare — for retroactive lump-sum SS payments allocated across prior years (Pub. 915). |
| 6d | MFS who lived apart from the spouse for all of 2025 checks this box (omitting it can cause a math error notice). |

### Line 7a / 7b — Capital gain or loss

7a comes from Schedule D (line 16, or line 21 if a loss). If no Schedule D is required (only capital gain distributions on 1099-DIV box 2a, no capital losses, no QOF deferral), enter box 2a directly on 7a and check "Schedule D not required" on 7b. Check the 7b "Includes child's capital gain or (loss)" box and enter the Form 8814 line 10 amount when reporting a child's gain.

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

Sum: 1z + 2b + 3b + 4b + 5b + 6b + 7a + 8.

This is **gross income** before adjustments.

---

## AGI and taxable income (Lines 10-15)

### Line 10 — Adjustments to income

From Schedule 1 Line 26. Above-the-line deductions. Common items:
- L11 Educator expenses (up to $300 for 2025; $600 MFJ if both educators; $350 for 2026)
- L13 HSA deduction (Form 8889)
- L14 Moving expenses (members of the Armed Forces only)
- L15 Deductible part of SE tax (Schedule SE Line 13)
- L16 Self-employed SEP, SIMPLE, and qualified plans
- L17 Self-employed health insurance
- L18 Penalty on early withdrawal of savings
- L19a Alimony paid (pre-2019 divorces; recipient SSN on 19b)
- L20 IRA deduction
- L21 Student loan interest (up to $2,500; 2025 phaseout $85,000–$100,000 MAGI, $170,000–$200,000 MFJ)
- L23 Archer MSA deduction
- L24a–L24z Other adjustments (total on L25)

### Line 11a — Adjusted Gross Income (AGI)

Line 9 − Line 10. **The most important number on the return.** Base for:
- Medicare premium calculations (IRMAA)
- Financial aid (FAFSA)
- State income tax in many states
- Roth IRA contribution eligibility (phaseouts)
- ACA premium tax credit (within MAGI)
- Dozens of phaseout thresholds (CTC, EITC, education credits, etc.)

### Line 11b — AGI repeated

Top of page 2: enter the Line 11a amount again.

### Lines 12a–12d — Standard deduction checkboxes

| Line | Check if | Effect |
|------|----------|--------|
| 12a | Someone can claim you, or your spouse (joint return), as a dependent | Use the Standard Deduction Worksheet for Dependents: greater of $1,350 or earned income + $450 (2025), capped at the regular amount, plus any 12d additions |
| 12b | MFS and your spouse itemizes | Standard deduction is zero; itemize |
| 12c | Dual-status alien (unless electing joint worldwide taxation) | Standard deduction is zero |
| 12d | You / spouse born before January 2, 1961, or blind at end of 2025 | Adds $1,600 per box (MFJ, QSS, MFS) or $2,000 per box (Single, HOH). Don't check spouse boxes on HOH; on MFS only if the spouse had no income, isn't filing, and can't be claimed by someone else |

### Line 12e — Standard or itemized deduction

For tax year 2025 (P.L. 119-21 §70102; 2025 Instructions for Form 1040, line 12e):

| Status | Standard deduction |
|--------|--------------------|
| Single | $15,750 |
| MFS | $15,750 |
| MFJ | $31,500 |
| Qualifying Surviving Spouse | $31,500 |
| Head of Household | $23,625 |

With 12d boxes (2025 chart): Single $17,750 / $19,750; MFJ $33,100 / $34,700 / $36,300 / $37,900; QSS $33,100 / $34,700; MFS $17,350 / $18,950 / $20,550 / $22,150; HOH $25,625 / $27,625.

For 2026 (Rev. Proc. 2025-32 §4.14): $16,100 single/MFS, $32,200 MFJ/QSS, $24,150 HOH; additional $1,650 ($2,050 unmarried, not a surviving spouse); dependent $1,350 or earned income + $450.

If itemizing instead, enter Schedule A Line 17. Itemize when total Schedule A items exceed the standard deduction. The 2025 SALT cap on Schedule A is $40,000 ($20,000 MFS), reduced when MAGI exceeds $500,000 ($250,000 MFS) but not below $10,000 ($5,000 MFS).

### Line 13a — QBI deduction

From Form 8995 line 15 (simplified) or Form 8995-A line 39 (full).

Up to 20% of qualified business income from:
- Schedule C profit
- Schedule E passthrough (K-1 from partnership / S-corp)
- Qualifying REIT dividends (1099-DIV box 5)
- Qualifying PTP income

If 2025 taxable income before the QBI deduction is at or below $197,300 ($394,600 MFJ) and the user is not a patron of a specified agricultural or horticultural cooperative, use Form 8995. Otherwise use Form 8995-A — SSTB phaseouts and W-2 wage / UBIA limits apply. 2026 thresholds: $201,750 / $403,500 (Rev. Proc. 2025-32 §4.26).

QBI deduction = lesser of (20% × QBI) or (20% × (taxable income before QBI − net capital gain)).

Made permanent by OBBBA 2025.

### Line 13b — Additional deductions from Schedule 1-A

From Schedule 1-A line 38 (new for 2025; available whether the user itemizes or not):
- No tax on tips: up to $25,000 of qualified tips, reduced above $150,000 MAGI ($300,000 MFJ); valid SSN; joint return if married
- No tax on overtime: up to $12,500 ($25,000 MFJ) of qualified overtime compensation, same phaseout and SSN/joint rules
- No tax on car loan interest: up to $10,000 of qualified passenger vehicle loan interest on a new, U.S.-assembled vehicle bought for personal use (VIN required), reduced above $100,000 MAGI ($200,000 MFJ)
- Enhanced deduction for seniors: $6,000 per person born before January 2, 1961 ($12,000 if both spouses qualify), reduced above $75,000 MAGI ($150,000 MFJ); valid SSN; joint return if married

Source: 2025 Instructions for Form 1040, What's New and Schedule 1-A instructions.

### Line 14 — Sum of 12e + 13a + 13b

Total deductions before applying to taxable income.

### Line 15 — Taxable income

Line 11b − Line 14. If zero or less, enter 0. **The number tax is calculated on.**

---

## Page 2 — Tax, Credits, Payments

### Line 16 — Tax

Compute tax on Line 15 using:
- **Tax Table** if Line 15 is less than $100,000 — look up the $50 row in the 1040 instructions (p. 68 of the 2025 instructions)
- **Tax Computation Worksheet** if Line 15 is $100,000 or more (p. 80)
- **Qualified Dividends and Capital Gain Tax Worksheet** if 3a > 0, or capital gain distributions on 7a without Schedule D, or Schedule D lines 15 and 16 both gains — uses preferential 0/15/20% rates
- **Schedule D Tax Worksheet** if Schedule D line 18 or 19 (28%-rate gain, unrecaptured §1250 gain) is more than zero and lines 15 and 16 are gains, or Form 4952 line 4g has an amount
- **Form 8615** for a child with more than $2,700 of unearned income; **Foreign Earned Income Tax Worksheet** if Form 2555 is filed

Check box 1 (Form 8814), box 2 (Form 4972), or box 3 (other, with the code such as "962", "ECR", "1291TAX") on Line 16 when those taxes are included.

See [`tax-computation.md`](./tax-computation.md).

### Line 17 — Amount from Schedule 2 Line 3

Schedule 2 Part I:
- Lines 1a–1z: excess advance premium tax credit repayment (Form 8962), clean vehicle credit repayments, Form 4255 items, other additions
- Line 2: Alternative Minimum Tax (Form 6251)

Most filers owe $0 here.

### Line 18 — Sum of 16 + 17

Total tax before credits.

### Line 19 — CTC / ODC

From Schedule 8812 line 14.

For each qualifying child under 17 at year-end with an SSN valid for employment issued by the due date: up to **$2,200** Child Tax Credit (2025 and 2026; P.L. 119-21, Rev. Proc. 2025-32 §4.05).
For other dependents (children 17+, parents, qualifying relatives, children without the required SSN): **$500** Credit for Other Dependents.

Phaseout: $50 per $1,000 (or fraction) of modified AGI over $200,000 ($400,000 MFJ) (Schedule 8812 lines 9–11).

Line 19 is the smaller of the credit after phaseout and the Credit Limit Worksheet A amount. The refundable portion (up to $1,700 per child for 2025 and 2026) goes on Line 28.

See [`credits-overview.md`](./credits-overview.md) and the [`schedule-8812`](../../schedule-8812/SKILL.md) skill.

### Line 20 — Other credits from Schedule 3 Line 8

Schedule 3 Part I non-refundable credits:
- L1 Foreign tax credit (Form 1116, or directly if ≤ $300/$600)
- L2 Dependent care credit (Form 2441 line 11)
- L3 Education credits non-refundable portion (Form 8863 line 19)
- L4 Retirement savings contributions credit "Saver's Credit" (Form 8880)
- L5a Residential clean energy credit (Form 5695 line 15); L5b Energy efficient home improvement credit (Form 5695 line 32)
- L6a General business credit (Form 3800); L6b prior-year minimum tax (Form 8801); L6c adoption credit, nonrefundable part (Form 8839); L6d–L6z other credits (total on L7)

### Line 21 — Sum of 19 + 20

Total nonrefundable credits.

### Line 22 — Line 18 minus Line 21

Floor at 0.

### Line 23 — Other taxes from Schedule 2 Line 21

Schedule 2 Part II:
- L4 Self-employment tax (Schedule SE)
- L5 SS and Medicare tax on unreported tip income (Form 4137); L6 uncollected SS/Medicare on wages (Form 8919); L7 = 5 + 6
- L8 Additional tax on IRAs or other tax-favored accounts (Form 5329)
- L9 Household employment taxes (Schedule H)
- L10 Reserved for future use
- L11 Additional Medicare Tax (Form 8959)
- L12 Net Investment Income Tax (Form 8960)
- L13 Uncollected SS/Medicare or RRTA tax on tips or group-term life insurance (W-2 box 12)
- L14–L15 Interest on certain installment-sale deferred tax
- L16 Recapture of low-income housing credit (Form 8611)
- L17a–L17z Other additional taxes (total on L18)
- L19 Recapture of net EPE (Form 4255)
- L20 Section 965 net tax liability installment (not added to line 21)

For self-employed filers, Line 23 is usually the largest line on page 2 (Schedule SE: 12.4% up to the Social Security wage base plus 2.9% on all net earnings from self-employment, which are 92.35% of net profit).

### Line 24 — Total tax

Line 22 + Line 23. **Total federal tax for the year.**

### Line 25 — Federal income tax withheld

| Sub-line | Source |
|----------|--------|
| 25a | W-2 box 2 sum across all W-2s |
| 25b | 1099 box 4 (1099-R, 1099-INT, 1099-DIV, 1099-G, 1099-NEC, 1099-MISC, etc.), SSA-1099 box 6, RRB-1099 box 10 |
| 25c | Other forms — W-2G box 4, Additional Medicare Tax withheld (Form 8959 line 24), Schedule K-1 withholding, Forms 1042-S, 8805, 8288-A |
| 25d | Total of 25a through 25c |

### Line 26 — 2025 estimated tax payments + prior year overpayment applied

Sum of:
- All Form 1040-ES payments made for the tax year
- Any prior-year refund elected to be applied to the current year (from the prior-year 1040 line 36, or an amended return)

New on the 2025 form: if the user made joint estimated payments with a former spouse (divorced in 2025), enter the former spouse's SSN in the space on Line 26.

### Line 27a / 27b / 27c — EIC

27a: refundable credit for low-to-moderate income workers. From the EIC worksheets and table (1040 instructions). Computed based on:
- Filing status
- Number of qualifying children (0, 1, 2, 3+)
- Earned income
- AGI

Maximum 2025 EIC: $649 (no child), $4,328 (1), $7,152 (2), $8,046 (3+). No credit once AGI (or earned income, if greater) reaches $19,104 / $50,434 / $57,310 / $61,555 ($26,214 / $57,554 / $64,430 / $68,675 MFJ) (Rev. Proc. 2024-40 §2.06). 2026 maximum with 3+ children: $8,231 (Rev. Proc. 2025-32 §4.06).

Investment income limit for 2025: $11,950. Above this, no EIC.

27b: check for clergy filing Schedule SE whose Schedule SE line 2 includes amounts also on Line 1z. 27c: check if the user does not want to claim the EIC or the EIC instructions say to check it.

### Line 28 — Additional Child Tax Credit

The refundable portion of the CTC. Up to $1,700 per child for 2025 and 2026 (Rev. Proc. 2024-40 §2.05; Rev. Proc. 2025-32 §4.05). Computed on Schedule 8812 line 27; generally 15% of earned income above $2,500 (Schedule 8812 lines 18a–20). Check the Line 28 box if the user does not want to claim the ACTC. Returns claiming the ACTC are not refunded before mid-February.

### Line 29 — Refundable AOTC

40% of the American Opportunity Tax Credit, up to $1,000 per eligible student. From Form 8863 Line 8.

The other 60% (up to $1,500) is non-refundable and lands on Line 20 via Schedule 3 Line 3.

### Line 30 — Refundable adoption credit

New for 2025: up to $5,000 of the adoption credit per eligible child is refundable (P.L. 119-21). Enter Form 8839 line 13. The nonrefundable remainder goes on Schedule 3 line 6c.

### Line 31 — Other payments and refundable credits from Schedule 3 Line 15

Schedule 3 Part II:
- L9 Net premium tax credit (Form 8962)
- L10 Amount paid with extension request (Form 4868)
- L11 Excess Social Security and tier 1 RRTA tax withheld (when filer had multiple employers and combined SS wages exceeded the wage base)
- L12 Credit for federal tax on fuels (Form 4136)
- L13a-L13z Other payments or refundable credits (total on L14)

### Line 32 — Total other payments and refundable credits

Lines 27a + 28 + 29 + 30 + 31.

### Line 33 — Total payments

Lines 25d + 26 + 32.

### Line 34 — Overpayment (refund)

If Line 33 > Line 24: Line 33 − Line 24 = total overpayment.

### Lines 35a-35d — Direct deposit

| Sub-line | What goes here |
|----------|----------------|
| 35a | Amount of Line 34 to be refunded to taxpayer (via check or direct deposit); check the box if Form 8888 is attached |
| 35b | Bank routing number (9 digits) |
| 35c | Type — Checking or Savings |
| 35d | Account number |

If splitting refund across multiple accounts, attach Form 8888.

### Line 36 — Applied to next year's estimated tax

Amount of Line 34 the taxpayer wants applied to next year's estimated tax. This election can't be changed later.

Line 35a + Line 36 = Line 34.

### Line 37 — Amount you owe

If Line 24 > Line 33: Line 24 − Line 33 = balance due (add any Line 38 penalty). Pay by April 15 to avoid late-payment interest and penalty; the instructions recommend electronic payment (IRS.gov/Payments). Mail a check only with Form 1040-V.

### Line 38 — Estimated tax penalty

The user may owe the penalty if Line 37 is at least $1,000 and more than 10% of the tax shown on the return, or if estimated tax was short on any due date (even with a refund).

No penalty if the 2024 return covered 12 months and either the 2024 return showed no tax (U.S. citizen or resident all year) or Lines 25d + 26 + Schedule 3 line 11 are at least 100% of the 2024 tax (110% if 2024 AGI was over $150,000, $75,000 if MFS), paid on time (2025 Instructions for Form 1040, line 38). The current-year test (90% of 2025 tax) is applied on Form 2210.

Leave Line 38 blank to let the IRS calculate, or compute on Form 2210 if claiming the annualized income exception (income arrived unevenly through the year) or wanting to verify the IRS number.

### Signing

Both spouses sign on MFJ. Date. Occupation. Daytime phone and email. Identity Protection PIN if the IRS issued one. Self-Select PIN if e-filing. If a paid preparer prepared the return, they sign too.

---

## Cross-line flows (most common)

| Source | Destination |
|--------|-------------|
| W-2 box 1 sum | Line 1a → Line 1z |
| W-2 box 2 sum | Line 25a |
| 1099-NEC/1099-K (self-employment) | Schedule C Line 1 → Line 31 → Schedule 1 Line 3 → Line 10 → 1040 Line 8 |
| Schedule C Line 31 (net profit) | Schedule SE Line 2 → SE tax Line 12 → Schedule 2 Line 4 → Schedule 2 Line 21 → 1040 Line 23 |
| Schedule SE Line 13 (half SE tax) | Schedule 1 Line 15 → Schedule 1 Line 26 → 1040 Line 10 (reduces AGI) |
| 1099-INT box 1 | Line 2b |
| 1099-DIV box 1a | Line 3b |
| 1099-DIV box 1b | Line 3a |
| 1099-B / 1099-DA / Form 8949 | Schedule D → Line 7a |
| 1099-R box 2a | Line 4b or 5b |
| SSA-1099 box 5 | Line 6a; Line 6b via worksheet |
| Schedule A Line 17 | 1040 Line 12e |
| Form 8995 Line 15 (8995-A Line 39) | 1040 Line 13a |
| Schedule 1-A Line 38 | 1040 Line 13b |
| Schedule 8812 Line 14 | 1040 Line 19 |
| Schedule 8812 Line 27 | 1040 Line 28 |
| Form 8863 Line 19 | Schedule 3 Line 3 → 1040 Line 20 |
| Form 8863 Line 8 | 1040 Line 29 |
| Form 8839 Line 13 | 1040 Line 30 |
| Form 2441 Line 11 | Schedule 3 Line 2 → 1040 Line 20 |
| Form 8889 Line 13 | Schedule 1 Line 13 → 1040 Line 10 |
| Form 8959 Line 24 (withheld) | 1040 Line 25c |
| Form 4868 payment | Schedule 3 Line 10 → 1040 Line 31 |
