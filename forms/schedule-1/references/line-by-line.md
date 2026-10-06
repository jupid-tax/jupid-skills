# Schedule 1 Line-by-Line Reference

Complete lookup for every line on the 2025 Schedule 1 (Form 1040), filed in 2026, verified on 2026-10-06 against the form PDF and the Schedule 1 section of the 2025 Instructions for Form 1040. Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1040. Use this when the agent needs to confirm where an income item or adjustment belongs, what a line means, or what supporting form must be attached.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on Form 1040 | Filer's legal name (and spouse if MFJ) | Match the 1040 exactly |
| Your social security number | Filer's SSN/ITIN | Must match 1040 |

## Above-Part-I line — 1099-K reported in error or for personal items sold at a loss

The 2024+ Schedule 1 has a dedicated row above Part I for 1099-K amounts that are not taxable income. Two situations qualify:

1. **Personal items sold at a loss** — Used furniture, concert tickets, used electronics sold on Marketplace, eBay, or via PayPal Goods & Services for less than what the user paid for them.
2. **1099-K issued in error** — e.g., money for gifts or reimbursements included in box 1a, a wrong taxpayer, or a duplicate report.

A personal item sold at a **gain** does not go here; report it on Form 8949 / Schedule D. For 2025, a platform must issue a 1099-K only if payments exceed $20,000 and transactions exceed 200 (2025 Form 1040 instructions, Schedule 1 "Form(s) 1099-K").

Enter the amount here and **do not** put it on Line 8z. The IRS will see the 1099-K matched to the user's SSN and reconciled to zero taxable income.

If the 1099-K is for a real trade or business, that income belongs on Schedule C — not here, not on Line 8.

---

## Part I — Additional Income (Lines 1-10)

### Line 1 — Taxable refunds, credits, or offsets of state and local income taxes

| Belongs here | Does NOT belong here |
|--------------|----------------------|
| Prior-year state income tax refund **if** filer itemized last year and got a tax benefit | Refund when filer took standard deduction last year |
| Local income tax refund (same rules) | Federal income tax refund (never taxable) |
| Tax credit refunds (state EITC, state child credit) per Pub 525 worksheet | Property tax or sales tax refund (Line 8z recovery, per Pub 525) |

Reported on Form 1099-G Box 2 by the state.

**Tax benefit rule**: even if user itemized, if the prior-year SALT cap ($10,000 for 2018–2024; $40,000 for 2025, reduced above $500,000 MAGI but not below $10,000) was already maxed by other taxes, the state income tax deduction may not have produced a benefit — leaving Line 1 at $0. The refund is also not taxable to the extent itemized deductions did not exceed the standard deduction. See [`state-refund-taxability.md`](./state-refund-taxability.md) for the worksheet.

Refunds of property tax or general sales tax are **not** Line 1 items; any taxable recovery goes on Line 8z (2025 Form 1040 instructions, Line 1 Exception item 2 and Line 8z list).

**Source**: IRC §111; State and Local Income Tax Refund Worksheet, 2025 Form 1040 instructions (Schedule 1, line 1); IRS Publication 525 (Recoveries chapter).

### Line 2a — Alimony received

Only alimony received under a divorce or separation agreement **executed before January 1, 2019** is taxable here. Post-2018 decrees fall under TCJA — neither income to recipient nor deductible by payer.

If a pre-2019 decree was modified after 2018 to expressly adopt TCJA rules, the modification controls (no income).

Child support is never alimony. Property settlements are never alimony.

**Source**: IRC §71 (pre-TCJA, applies to pre-2019 decrees only).

### Line 2b — Date of original divorce or separation agreement

Required if Line 2a > 0. Enter the month and year of the original divorce or separation agreement, not the latest modification. If alimony comes from more than one agreement, enter the one that produced the most income and attach a statement listing the others (2025 Form 1040 instructions, Line 2b).

### Line 3 — Business income or (loss)

Net profit or loss from Schedule C Line 31. Sole proprietors and single-member LLCs taxed as disregarded entities.

If Line 31 is positive, Line 3 is positive. If Line 31 is a loss, Line 3 is in parentheses.

If the user has multiple Schedule Cs (e.g., two distinct businesses), file one Schedule C per business and sum the net results onto Line 3.

If Schedule C net profit > $400, Schedule SE is required.

**Source**: Form 1040 General Instructions, Schedule 1 Line 3.

### Line 4 — Other gains or (losses)

From Form 4797 line 18b (sales of business property; check the "4797" box) or, if Form 4797 isn't otherwise required, Form 4684 line 31 (casualties and thefts; check the "4684" box). The checkboxes are new on the 2025 form. Rare for solo filers. If the user sold a business asset (computer, vehicle, equipment) above its adjusted basis, Form 4797 captures the gain — and the result lands here.

Capital gains on stocks and personal investments do **not** belong on Line 4 — those go on Schedule D and flow to Form 1040 Line 7a.

### Line 5 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.

Net result from Schedule E:
- Part I: rental real estate and royalties
- Part II: partnerships and S corporations (K-1)
- Part III: estates and trusts (K-1)
- Part IV: REMICs

If a net loss, Line 5 is in parentheses (subject to passive activity rules — IRC §469).

A user who is a "real estate dealer" (regularly sells to customers) reports on Schedule C, not Schedule E. Most rental owners are investors, not dealers.

### Line 6 — Farm income or (loss)

From Schedule F Line 34. Farmers and ranchers use Schedule F instead of Schedule C. The net result lands here.

If Schedule F profit > $400, Schedule SE is required (with farm-specific options on Schedule SE Part II).

### Line 7 — Unemployment compensation

Form 1099-G Box 1, total unemployment compensation received during the year. Both state and federal unemployment benefits are taxable at the federal level.

**Repayments in the same year**: if the user received unemployment in 2025 and repaid an overpayment in 2025, subtract the repayment from the total received, check the line 7 box, and enter the amount repaid in the entry space (new on the 2025 form).

**Repayments in a later year**: if the user repaid in 2025 more than $3,000 of unemployment compensation included in income in an earlier year, see Repayments in Pub 525 (claim of right under IRC §1341).

**Contributions**: if the user contributed to a governmental unemployment compensation program and doesn't itemize, reduce Line 7 by those contributions (2025 Form 1040 instructions, Line 7).

**Pandemic-era exclusions** (the $10,200 ARPA exclusion for 2020 only) do not apply for 2025.

### Line 8 — Other income (8a through 8z)

Catchall structure for income that doesn't fit Lines 1-7. The 2025 form lists 22 specific sub-lines plus an "8z list" for anything not pre-printed.

| Sub-line | Description | Sign | Common source |
|----------|-------------|------|---------------|
| 8a | Net operating loss | Negative | NOL carryforward from a prior year |
| 8b | Gambling | Positive | W-2G + cash winnings (gross, no offsets) |
| 8c | Cancellation of debt | Positive | 1099-C, unless §108 exception applies |
| 8d | Foreign earned income and housing exclusion | Negative | Form 2555 line 45 |
| 8e | Income from Form 8853 | Positive | Form 8853 lines 8, 12, and 26 |
| 8f | Income from Form 8889 | Positive | Form 8889 lines 16 and 20 |
| 8g | Alaska Permanent Fund dividends | Positive | Annual PFD |
| 8h | Jury duty pay | Positive | Pay received for jury service |
| 8i | Prizes and awards | Positive | Game show, contest, raffle, scientific award |
| 8j | Activity not engaged in for profit (hobby) | Positive | Gross hobby income (no expense offset) |
| 8k | Stock options | Positive | Income from exercise of stock options not otherwise reported on Form 1040 line 1h |
| 8l | Income from rental of personal property (not a business) | Positive | Occasional rental of equipment/items |
| 8m | Olympic and Paralympic medals and prize money | Positive (often offset by 24c) | USOC distributions |
| 8n | Section 951(a) inclusion | Positive | Subpart F (CFC) |
| 8o | Section 951A(a) inclusion | Positive | GILTI |
| 8p | Section 461(l) excess business loss adjustment | Positive | Form 461 line 16 |
| 8q | Taxable distributions from an ABLE account | Positive | Excess ABLE distributions |
| 8r | Scholarship and fellowship grants not on W-2 | Positive | Taxable portion (room/board, not tuition) |
| 8s | Nontaxable amount of Medicaid waiver payments | Negative | Backs out wages already on Form 1040 |
| 8t | Pension or annuity from nonqualified deferred comp / nongovt §457 plan | Positive | May be shown in W-2 box 11 |
| 8u | Wages earned while incarcerated | Positive | Per IRS rule |
| 8v | Digital assets received as ordinary income | Positive | Ordinary income from digital assets not reported elsewhere, e.g., forks, staking, mining (when not Schedule C); not gifts or inheritances |
| 8z | Other income — list type and amount | Either | Catchall — must label |

For a deeper treatment of each Line 8 sub-type, see [`additional-income-types.md`](./additional-income-types.md).

### Line 9 — Total other income

Sum of Lines 8a through 8z. Some sub-lines are negatives (8a, 8d, 8s) — the total can be negative.

### Line 10 — Total additional income

```
Line 10 = Line 1 + Line 2a + Line 3 + Line 4 + Line 5 + Line 6 + Line 7 + Line 9
```

Flows to **Form 1040 Line 8**.

---

## Part II — Adjustments to Income (Lines 11-26)

These are the "above-the-line" deductions — they reduce AGI whether or not the user itemizes.

### Line 11 — Educator expenses

Up to $300 (2025 cap; $350 for 2026, Rev. Proc. 2025-32 §4.12) for unreimbursed classroom expenses by K-12 teachers, instructors, counselors, principals, or aides who worked at least **900 hours** in a school year at a school providing elementary or secondary education.

Qualifying expenses: books, supplies, computer equipment and software, professional development, and (per the 2025 instructions) personal protective equipment and disinfectant used to prevent the spread of coronavirus. Not home schooling or nonathletic supplies for health or PE courses.

Spouse can also claim if separately a qualifying educator (so MFJ can be up to $600 combined).

**Source**: IRC §62(a)(2)(D); Rev. Proc. 2024-40 ($300 for 2025).

### Line 12 — Reservists, performing artists, and fee-basis government officials (Form 2106)

Three narrow groups deduct unreimbursed business expenses on Form 2106:
1. **Armed Forces reservists** traveling more than 100 miles from home for reserve duty
2. **Qualifying performing artists** with at least 2 employers, $200+ wages from each of at least two, performing-arts expenses > 10% of gross income from the performing arts, and AGI ≤ $16,000 before this deduction (2025 Instructions for Form 2106, line 10)
3. **State or local government officials paid on a fee basis** (most aren't)

Most filers leave Line 12 blank. Other employees' business expenses are miscellaneous itemized deductions, eliminated for tax years after 2017 (IRC §67(h), made permanent by P.L. 119-21 §70110).

### Line 13 — Health savings account deduction (Form 8889)

HSA contributions made **outside payroll** (deductions through cafeteria-plan payroll are already excluded from Box 1 W-2 wages).

2025 contribution limits (Rev. Proc. 2024-25):
- Self-only HDHP: $4,300
- Family HDHP: $8,550
- Catch-up (age 55+): additional $1,000

2026 limits (Rev. Proc. 2025-19): $4,400 self-only, $8,750 family; catch-up stays $1,000.

Eligibility requires being covered by a qualifying HDHP and not enrolled in Medicare or other non-HDHP coverage. P.L. 119-21 lets an HSA-eligible individual also have telehealth and other remote care coverage, for plan years beginning after 2024 (2025 Instructions for Form 8889, What's New).

**Source**: IRC §223; IRS Publication 969; Form 8889 instructions.

### Line 14 — Moving expenses for members of the Armed Forces (Form 3903)

Active-duty service members on permanent change of station orders deduct moving costs. Check the line 14 box if claiming only storage fees during an absence from the United States. Civilians cannot deduct moving expenses: P.L. 119-21 §70113 made the post-2017 rule permanent; from 2026 it also covers certain intelligence community employees (IRC §217(k)).

**Source**: IRC §217(g), (k); Instructions for Form 3903 (2025).

### Line 15 — Deductible part of self-employment tax

Half of SE tax owed, calculated on Schedule SE Line 13. Represents the "employer-equivalent" portion of FICA.

**Example math**:
```
Net SE earnings = $40,000 × 0.9235 = $36,940
SE tax          = $36,940 × 0.153  = $5,652
Half of SE tax  = $5,652 / 2       = $2,826  → Line 15
```

If the user has Schedule C profit > $400 but Line 15 is blank, Schedule SE was skipped — block.

**Source**: IRC §164(f).

### Line 16 — Self-employed SEP, SIMPLE, and qualified plans

Owner's contribution to retirement plans for themselves (not employees — those go on Schedule C Line 19):

| Plan | 2025 cap | Notes |
|------|----------|-------|
| SEP-IRA | 25% plan rate, which for the owner works out to 20% of (net profit − Line 15), up to $70,000 | Pub 560 Deduction Worksheet for Self-Employed |
| SIMPLE IRA | $16,500 (or $20,000 with catch-up at 50+; $21,750 at ages 60–63) | New plan effective between Jan 1 and Oct 1 of the year |
| Solo 401(k) — employee deferral | $23,500 (or $31,000 with catch-up at 50+; $34,750 at ages 60–63) | Plus employer profit-share |
| Solo 401(k) — employer | 25% of compensation up to combined $70,000 | Catch-ups sit on top of the $70,000 |

2026 (Notice 2025-67): SEP/415(c) cap $72,000; 401(k) deferral $24,500, catch-up $8,000 (ages 60–63: $11,250); SIMPLE $17,000, catch-up $4,000 (ages 60–63: $5,250).

SEP contributions must be made by the **return due date including extensions** (Oct 15, 2026 for a 2025 return on extension). SIMPLE and 401(k) elective deferrals have their own timing rules (Pub 560).

**Source**: IRC §§408(k), 408(p), 401(k); Notice 2024-80; Notice 2025-67; Pub 560 (2025).

### Line 17 — Self-employed health insurance deduction

Health, dental, vision, and qualified long-term care premiums paid by a self-employed individual for themselves, spouse, dependents, and children under age 27 (even if not a dependent).

**Caps and disqualifiers**:
- Limited to net profit (and other earned income) from the business under which the plan is established, minus Schedule 1 Lines 15 and 16 (Self-Employed Health Insurance Deduction Worksheet in the 2025 Form 1040 instructions; use Form 7206 if there is more than one SE income source, Form 2555 is filed, or long-term care premiums are used)
- Cannot claim for any month the user, the user's spouse, a dependent, or a child under 27 was eligible to participate in an employer-subsidized plan (a QSEHRA counts), even if they didn't enroll
- Marketplace premiums with advance premium tax credit (or a PTC claim): use Pub 974 instead of the worksheet (circular calculation)

**Source**: IRC §162(l); 2025 Form 1040 instructions (Schedule 1, line 17); Instructions for Form 7206; Pub 974.

### Line 18 — Penalty on early withdrawal of savings

Early-withdrawal penalty on a CD or time-deposit savings, reported on Form 1099-INT Box 2 (or 1099-OID Box 3). The deduction is the penalty itself, separate from any interest income reported on Line 2b of Form 1040.

### Line 19a — Alimony paid

Alimony paid under a pre-2019 decree only. Post-2018: not deductible.

Child support is not alimony. Property settlements are not alimony.

### Line 19b — Recipient's SSN

Required if Line 19a > 0. Without a valid recipient SSN, the IRS rejects the deduction.

### Line 19c — Date of original divorce or separation agreement

Required if Line 19a > 0. Month and year of the original divorce or separation agreement.

### Line 20 — IRA deduction

Traditional IRA contributions, subject to phaseout based on whether the user (or spouse, if MFJ) is an "active participant" in an employer retirement plan during the year.

2025 phaseouts (Notice 2024-80; IRA Deduction Worksheet, 2025 Form 1040 instructions):
- Single / HOH, active participant: $79,000 – $89,000 MAGI
- MFJ / QSS, contributor active: $126,000 – $146,000 MAGI
- MFJ, spouse active (contributor not): $236,000 – $246,000 MAGI
- MFS, active (or spouse active) and lived together: $0 – $10,000 MAGI; MFS who lived apart all year is treated as single and checks the line 20 box

2025 contribution limits: $7,000 (under 50), $8,000 (50+).

2026 (Notice 2025-67): limits $7,500 / $8,600 (50+); phaseouts $81,000–$91,000 single, $129,000–$149,000 MFJ, $242,000–$252,000 spouse-active.

**Roth IRA contributions are NOT deductible** (after-tax) and do not appear on Line 20.

### Line 21 — Student loan interest deduction

Up to **$2,500** of qualified student loan interest paid during the year. Reported by the lender on Form 1098-E.

2025 MAGI phaseouts (Rev. Proc. 2024-40 §2.30; Student Loan Interest Deduction Worksheet, 2025 Form 1040 instructions):
- Single / HOH / QSS: $85,000 – $100,000 (full → zero)
- MFJ: $170,000 – $200,000 (full → zero)
- MFS: not allowed

2026 (Rev. Proc. 2025-32 §4.29): $85,000 – $100,000; MFJ $175,000 – $205,000.

The $2,500 cap is statutory (IRC §221) and does not change with inflation. Only the income phaseout adjusts.

Available with the standard deduction — one of the most-missed adjustments.

**Eligibility requires**:
- Loan was solely for qualified higher-education expenses
- Loan was for the user, spouse, or dependent at the time the loan was taken
- User is legally obligated on the loan
- Filer is not someone else's dependent

**Source**: IRC §221.

### Line 22 — Reserved for future use

Always blank. The IRS reserves line numbers for future legislative additions.

### Line 23 — Archer MSA deduction (Form 8853)

Archer Medical Savings Accounts predate HSAs. New entrants are largely closed (must have started before 2008 in most cases). Line 23 is rare.

**Source**: IRC §220.

### Line 24 — Other adjustments (24a through 24z)

Specific items that don't fit Lines 11-23.

| Sub-line | Description |
|----------|-------------|
| 24a | Jury duty pay turned over to employer (offsets Line 8h when employer paid wages during jury duty) |
| 24b | Deductible expenses related to Line 8l personal property rental |
| 24c | Nontaxable portion of Olympic/Paralympic medals and USOC prize money (offsets Line 8m if AGI ≤ $1M) |
| 24d | Reforestation amortization and expenses (IRC §194) |
| 24e | Repayment of supplemental unemployment benefits under the Trade Act of 1974 |
| 24f | Contributions to §501(c)(18)(D) pension plans |
| 24g | Contributions by certain chaplains to §403(b) plans |
| 24h | Attorney fees and court costs for unlawful discrimination claims (IRC §62(a)(20)) |
| 24i | Attorney fees and court costs related to IRS whistleblower awards (IRC §62(a)(21)) |
| 24j | Housing deduction from Form 2555 (foreign earned income) |
| 24k | Excess deductions of §67(e) expenses from Schedule K-1 (Form 1041) |
| 24z | Other adjustments — the 2025 instructions say "Leave line 24z blank" |

For most solo filers, Line 24 sub-lines are blank except 24a (if the user had jury duty and turned the pay over to their employer).

### Line 25 — Total other adjustments

Sum of Lines 24a through 24z.

### Line 26 — Total adjustments to income

```
Line 26 = Line 11 + Line 12 + Line 13 + Line 14 + Line 15 + Line 16 + Line 17 + Line 18 + Line 19a + Line 20 + Line 21 + Line 23 + Line 25
```

(Line 22 is blank.)

Flows to **Form 1040 Line 10**.

---

## Quick attachment map

| Schedule 1 line | Required attachment |
|-----------------|---------------------|
| Line 3 > 0 or < 0 | Schedule C |
| Net SE earnings (Line 3 × 92.35%) ≥ $400 | Schedule SE |
| Line 5 > 0 or < 0 | Schedule E |
| Line 6 > 0 or < 0 | Schedule F |
| Net farm SE earnings ≥ $400 | Schedule SE |
| Line 12 > 0 | Form 2106 |
| Line 13 > 0 | Form 8889 |
| Line 14 > 0 | Form 3903 |
| Line 15 > 0 | Schedule SE |
| Line 19a > 0 | 19b SSN + 19c decree date |
| Line 23 > 0 | Form 8853 |
| Line 8d < 0 | Form 2555 |
| Line 8e > 0 | Form 8853 |
| Line 8f > 0 | Form 8889 |

---

## Sources

- IRS Schedule 1 (Form 1040), 2025 revision (https://www.irs.gov/pub/irs-pdf/f1040s1.pdf)
- IRS Form 1040 General Instructions, 2025 revision (Schedule 1 line-by-line guidance, pp. 88–100)
- Instructions for Forms 2106, 3903, 7206, 8889 (2025)
- IRS Publications 17, 525, 560, 590-A, 969, 970, 974
- IRC §§61, 62, 67(h), 71, 111, 162(l), 164(f), 217(g), 217(k), 221, 223
- Rev. Proc. 2024-25 (HSA limits 2025); Rev. Proc. 2025-19 (2026)
- Rev. Proc. 2024-40 (inflation adjustments 2025); Rev. Proc. 2025-32 (2026)
- Notice 2024-80 (retirement plan and IRA limits 2025); Notice 2025-67 (2026)
