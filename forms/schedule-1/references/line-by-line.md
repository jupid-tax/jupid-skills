# Schedule 1 Line-by-Line Reference

Complete lookup for every line on Schedule 1 (Form 1040). Use this when the agent needs to confirm where an income item or adjustment belongs, what a line means, or what supporting form must be attached.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on Form 1040 | Filer's legal name (and spouse if MFJ) | Match the 1040 exactly |
| Your social security number | Filer's SSN/ITIN | Must match 1040 |

## Above-Part-I line — 1099-K reported in error or for personal items sold at a loss

The 2024+ Schedule 1 has a dedicated row above Part I for 1099-K amounts that are not taxable income. Two situations qualify:

1. **Personal items sold at a loss** — Used furniture, concert tickets, used electronics sold on Marketplace, eBay, or via PayPal Goods & Services for less than what the user paid for them.
2. **1099-K issued in error** — Wrong taxpayer, duplicate report, or activity that's not a trade or business.

Enter the amount here and **do not** put it on Line 8z. The IRS will see the 1099-K matched to the user's SSN and reconciled to zero taxable income.

If the 1099-K is for a real trade or business, that income belongs on Schedule C — not here, not on Line 8.

---

## Part I — Additional Income (Lines 1-10)

### Line 1 — Taxable refunds, credits, or offsets of state and local income taxes

| Belongs here | Does NOT belong here |
|--------------|----------------------|
| Prior-year state income tax refund **if** filer itemized last year and got a tax benefit | Refund when filer took standard deduction last year |
| Local income tax refund (same rules) | Federal income tax refund (never taxable) |
| Tax credit refunds (state EITC, state child credit) per Pub 525 worksheet | Property tax refund (handled differently) |

Reported on Form 1099-G Box 2 by the state.

**Tax benefit rule**: even if user itemized, if the SALT cap ($10,000 since TCJA) was already maxed by property tax alone, the state income tax deduction may not have produced a benefit — leaving Line 1 at $0. See [`state-refund-taxability.md`](./state-refund-taxability.md) for the worksheet.

**Source**: IRC §111; IRS Publication 525 (Recoveries chapter).

### Line 2a — Alimony received

Only alimony received under a divorce or separation agreement **executed before January 1, 2019** is taxable here. Post-2018 decrees fall under TCJA — neither income to recipient nor deductible by payer.

If a pre-2019 decree was modified after 2018 to expressly adopt TCJA rules, the modification controls (no income).

Child support is never alimony. Property settlements are never alimony.

**Source**: IRC §71 (pre-TCJA, applies to pre-2019 decrees only).

### Line 2b — Date of original divorce or separation agreement

Date field. Required if Line 2a > 0. Use the date of the original decree, not the latest modification.

### Line 3 — Business income or (loss)

Net profit or loss from Schedule C Line 31. Sole proprietors and single-member LLCs taxed as disregarded entities.

If Line 31 is positive, Line 3 is positive. If Line 31 is a loss, Line 3 is in parentheses.

If the user has multiple Schedule Cs (e.g., two distinct businesses), file one Schedule C per business and sum the net results onto Line 3.

If Schedule C net profit > $400, Schedule SE is required.

**Source**: Form 1040 General Instructions, Schedule 1 Line 3.

### Line 4 — Other gains or (losses)

From Form 4797 (sales of business property) or Form 4684 (casualties and thefts of business or income-producing property). Rare for solo filers. If the user sold a business asset (computer, vehicle, equipment) above its adjusted basis, Form 4797 captures the gain — and the result lands here.

Capital gains on stocks and personal investments do **not** belong on Line 4 — those go on Schedule D and flow to Form 1040 Line 7.

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

**Repayments in the same year**: if the user received unemployment in 2026 and repaid an overpayment in 2026, net the repayment against Box 1 and check the box.

**Repayments in a later year**: the deduction goes on a different line in the year of repayment (claim of right under IRC §1341).

**Pandemic-era exclusions** (the $10,200 ARPA exclusion for 2020 only) do not apply for 2026.

### Line 8 — Other income (8a through 8z)

Catchall structure for income that doesn't fit Lines 1-7. The 2025 form lists 22 specific sub-lines plus an "8z list" for anything not pre-printed.

| Sub-line | Description | Sign | Common source |
|----------|-------------|------|---------------|
| 8a | Net operating loss | Negative | NOL carryforward from a prior year |
| 8b | Gambling | Positive | W-2G + cash winnings (gross, no offsets) |
| 8c | Cancellation of debt | Positive | 1099-C, unless §108 exception applies |
| 8d | Foreign earned income exclusion | Negative | Form 2555 |
| 8e | Income from Form 8853 | Positive | Archer MSA / LTC contracts |
| 8f | Income from Form 8889 | Positive | Non-qualified HSA distributions |
| 8g | Alaska Permanent Fund dividends | Positive | Annual PFD |
| 8h | Jury duty pay | Positive | Pay received for jury service |
| 8i | Prizes and awards | Positive | Game show, contest, raffle, scientific award |
| 8j | Activity not engaged in for profit (hobby) | Positive | Gross hobby income (no expense offset) |
| 8k | Stock options | Positive | Non-statutory stock options not on W-2 |
| 8l | Income from rental of personal property (not a business) | Positive | Occasional rental of equipment/items |
| 8m | Olympic and Paralympic medals and prize money | Positive (often offset by 24c) | USOC distributions |
| 8n | Section 951(a) inclusion | Positive | Subpart F (CFC) |
| 8o | Section 951A(a) inclusion | Positive | GILTI |
| 8p | Section 461(l) excess business loss adjustment | Positive | Disallowed loss add-back |
| 8q | Taxable distributions from an ABLE account | Positive | Excess ABLE distributions |
| 8r | Scholarship and fellowship grants not on W-2 | Positive | Taxable portion (room/board, not tuition) |
| 8s | Nontaxable amount of Medicaid waiver payments | Negative | Backs out wages already on Form 1040 |
| 8t | Pension or annuity from nonqualified deferred comp / nongovt §457 plan | Positive | Plan distribution |
| 8u | Wages earned while incarcerated | Positive | Per IRS rule |
| 8v | Digital assets received as ordinary income | Positive | Crypto received as payment, NFT royalties, mining/staking rewards (when not Schedule C) |
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

Up to $300 (2025 cap; 2026 figure typically announced October 2025) for unreimbursed classroom expenses by K-12 teachers, instructors, counselors, principals, or aides who worked at least **900 hours** in a school year at a school providing elementary or secondary education.

Qualifying expenses: books, supplies, computer equipment and software, COVID-19 protective items (per IRS Notice 2021-15 if still applicable), professional development.

Spouse can also claim if separately a qualifying educator (so MFJ can be up to $600 combined).

**Source**: IRC §62(a)(2)(D); Rev. Proc. 2024-40 ($300 for 2025).

### Line 12 — Reservists, performing artists, and fee-basis government officials (Form 2106)

Three narrow groups deduct unreimbursed business expenses on Form 2106:
1. **Armed Forces reservists** traveling more than 100 miles from home for reserve duty
2. **Qualifying performing artists** with at least 2 employers, $200+ from each, performing-arts expenses > 10% of AGI, and AGI ≤ $16,000 before this deduction
3. **State or local government officials paid on a fee basis** (most aren't)

Most filers leave Line 12 blank. TCJA removed the regular employee business expense deduction.

### Line 13 — Health savings account deduction (Form 8889)

HSA contributions made **outside payroll** (deductions through cafeteria-plan payroll are already excluded from Box 1 W-2 wages).

2025 contribution limits (Rev. Proc. 2024-25):
- Self-only HDHP: $4,300
- Family HDHP: $8,550
- Catch-up (age 55+): additional $1,000

2026 limits announced May 2025 — verify before filing.

Eligibility requires being covered by a qualifying HDHP and not enrolled in Medicare or other non-HDHP coverage.

**Source**: IRC §223; IRS Publication 969.

### Line 14 — Moving expenses for members of the Armed Forces (Form 3903)

Active-duty service members on permanent change of station orders deduct moving costs. Civilians cannot deduct moving expenses (TCJA suspended civilian moving deduction through 2025; verify 2026 status).

**Source**: IRC §217(g); IRS Publication 521.

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
| SEP-IRA | 25% of net SE earnings (after §164(f) deduction) up to $70,000 | Computed via worksheet |
| SIMPLE IRA | $16,500 (or $20,000 with catch-up at 50+) | Plan must be in place by Oct 1 |
| Solo 401(k) — employee deferral | $23,500 (or $31,000 with catch-up at 50+) | Plus employer profit-share |
| Solo 401(k) — employer | 25% of compensation up to combined $70,000 | Combined total limit |

2026 figures announced fall 2025 — verify.

Contribution must be made by the **return due date including extensions** (Oct 15, 2027 for tax year 2026 if filing on extension). SIMPLE has earlier deadlines.

**Source**: IRC §§408(k), 408(p), 401(k); Notice 2024-80.

### Line 17 — Self-employed health insurance deduction

Health, dental, vision, and qualified long-term care premiums paid by a self-employed individual for themselves, spouse, dependents, and children under age 27 (even if not a dependent).

**Caps and disqualifiers**:
- Limited to net Schedule C profit (after the §164(f) and Line 16 deductions — see worksheet in Pub 535)
- Cannot claim for any month the user **or the user's spouse** was eligible to participate in an employer-subsidized plan, even if they didn't enroll
- Marketplace ACA premiums net of any Premium Tax Credit (circular calculation handled by IRS-approved software)

**Source**: IRC §162(l); IRS Publication 535.

### Line 18 — Penalty on early withdrawal of savings

Early-withdrawal penalty on a CD or time-deposit savings, reported on Form 1099-INT Box 2 (or 1099-OID Box 3). The deduction is the penalty itself, separate from any interest income reported on Line 2b of Form 1040.

### Line 19a — Alimony paid

Alimony paid under a pre-2019 decree only. Post-2018: not deductible.

Child support is not alimony. Property settlements are not alimony.

### Line 19b — Recipient's SSN

Required if Line 19a > 0. Without a valid recipient SSN, the IRS rejects the deduction.

### Line 19c — Date of original divorce or separation agreement

Date field. Required if Line 19a > 0.

### Line 20 — IRA deduction

Traditional IRA contributions, subject to phaseout based on whether the user (or spouse, if MFJ) is an "active participant" in an employer retirement plan during the year.

2025 phaseouts (Rev. Proc. 2024-40):
- Single, active participant: $77,000 – $87,000 MAGI
- MFJ, contributor active: $123,000 – $143,000 MAGI
- MFJ, spouse active (contributor not): $230,000 – $240,000 MAGI
- MFS, active: $0 – $10,000 MAGI

2025 contribution limits: $7,000 (under 50), $8,000 (50+).

2026 figures announced fall 2025 — verify.

**Roth IRA contributions are NOT deductible** (after-tax) and do not appear on Line 20.

### Line 21 — Student loan interest deduction

Up to **$2,500** of qualified student loan interest paid during the year. Reported by the lender on Form 1098-E.

2025 MAGI phaseouts (Rev. Proc. 2024-40):
- Single / HoH: $80,000 – $95,000 (full → zero)
- MFJ: $165,000 – $195,000 (full → zero)
- MFS: not allowed

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
| 24z | Other adjustments — list type and amount |

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
| Line 3 > $400 | Schedule SE |
| Line 5 > 0 or < 0 | Schedule E |
| Line 6 > 0 or < 0 | Schedule F |
| Line 6 > $400 | Schedule SE (with farm method) |
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

- IRS Schedule 1 (Form 1040), 2025 revision
- IRS Form 1040 General Instructions, 2025 revision (Schedule 1 line-by-line guidance)
- IRS Publications 17, 525, 535, 521, 969, 970
- IRC §§61, 62, 71, 111, 162(l), 164(f), 217(g), 221, 223
- Rev. Proc. 2024-25 (HSA limits 2025)
- Rev. Proc. 2024-40 (inflation adjustments 2025)
- Notice 2024-80 (retirement plan limits 2025)
