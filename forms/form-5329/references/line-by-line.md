# Form 5329 Line-by-Line Reference

Complete lookup for every line on Form 5329. Use this when the agent needs
to confirm where a number belongs or what a line means. Lines are grouped
by Part. Line numbers were verified against the 2025 Form 5329 (created
6/12/25) and the 2025 Instructions for Form 5329 (Nov 19, 2025), filed in
2026. Re-check the next revision at
https://www.irs.gov/forms-pubs/about-form-5329 before filing.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Name of the individual subject to the additional tax | If both spouses owe a 5329 tax, each completes a separate form; the combined tax goes on Schedule 2 (Form 1040), line 8 |
| SSN | That individual's SSN | |
| Address | Filer's mailing address | **Only when filing Form 5329 by itself.** Blank when attached to a 1040. |
| Foreign country / province / postal code | Foreign address fields | Standalone only |
| Amended return checkbox | Check if this is an amended 2025 Form 5329 | Use the prior year's form for a prior year |

Above Part I the form says: if you only owe the 10% tax on the full amount
of your early distributions (Form 1099-R box 7 code 1 correctly shown), you
may report it directly on Schedule 2 (Form 1040), line 8, without Form 5329.

---

## Part I — Additional Tax on Early Distributions (Lines 1-4)

Applies under IRC §72(t) to taxable distributions before age 59½ from a
qualified retirement plan (including an IRA) or a modified endowment
contract. Qualified disaster recovery distributions are not reported here
(Form 8915-F).

The 1099-R box 7 distribution code is the first signal but not the final
authority (2025 Instructions for Forms 1099-R and 5498, box 7 codes):

| Code | Meaning | Part I effect |
|------|---------|---------------|
| 1 | Early distribution, no known exception | 10% unless the user has an exception (claim it on Line 2) |
| 2 | Early distribution, exception applies | No Form 5329 needed if the exception covers the whole distribution |
| 3 | Disability | No Form 5329 needed |
| 4 | Death | No Form 5329 needed |
| 7 | Normal distribution | No Part I |
| 8 / P | Excess contributions plus earnings taxable in the current / a prior year | Earnings go on Line 1 and Line 2 with exception 21 if under 59½ |
| J | Early distribution from a Roth IRA, no known exception | Use Form 8606 Part III; Line 1 = Form 8606 line 25c plus any recapture amount |
| L | Loan treated as deemed distribution under §72(p) | Line 1 if under 59½ |
| S | Early distribution from a SIMPLE IRA in the first 2 years, no known exception | 25%, not 10% (Line 4) |

Who must file Part I (2025 Instructions, "Who Must File"): a distribution
subject to the tax with box 7 not showing an exception, or showing one that
does not cover the whole distribution; any Roth IRA distribution with an
amount on Form 8606 line 25c, a recapture amount, or a qualified first-time
homebuyer distribution.

### Line 1 — Early distributions includible in income

Early distributions includible in income (other than qualified disaster
recovery distributions), including earnings on withdrawn excess IRA
contributions included in income in 2025, and prohibited transactions
treated as distributions (borrowing from or pledging an IRA).

- **Designated Roth account**: box 2a of the 2025 Form 1099-R, plus any
  in-plan Roth rollover recapture amount.
- **Roth IRA**: Form 8606 line 25c, plus a qualified first-time homebuyer
  distribution from Form 8606 line 20 (also on Line 2 with exception 09),
  plus the recapture amount allocated to the taxable part of conversions
  or rollovers made in 2021 through 2025. Regular contributions come out
  first; if they cover the distribution, Line 1 is 0 for it. See
  [`early-distribution-exceptions.md`](./early-distribution-exceptions.md).

### Line 2 — Distributions not subject to the additional tax

The amount of Line 1 that qualifies for an exception, with the exception
number (01–23) in the space provided. **If more than one exception
applies, enter 99** (2025 Instructions, Line 2):

| No. | Exception (2025 Instructions for Form 5329, Line 2) | IRC § |
|-----|-----------|-------|
| 01 | Qualified retirement plan (not IRA) distributions after separation from service in or after the year you reach 55 (50 for qualified public safety employees and private sector firefighters, or 25 years of service under the plan, if earlier) | §72(t)(2)(A)(v), (t)(10) |
| 02 | Series of substantially equal periodic payments (after separation if from an employer plan) | §72(t)(2)(A)(iv) |
| 03 | Total and permanent disability | §72(t)(2)(A)(iii), §72(m)(7) |
| 04 | Death (not for modified endowment contracts) | §72(t)(2)(A)(ii) |
| 05 | Unreimbursed medical expenses paid during the year minus 7.5% of AGI | §72(t)(2)(B) |
| 06 | Qualified plan distributions to an alternate payee under a QDRO (not IRAs) | §72(t)(2)(C) |
| 07 | IRA distributions to certain unemployed individuals for health insurance premiums | §72(t)(2)(D) |
| 08 | IRA distributions for qualified higher education expenses | §72(t)(2)(E) |
| 09 | IRA distributions for a first home, up to $10,000 | §72(t)(2)(F) |
| 10 | Qualified plan distributions due to an IRS levy | §72(t)(2)(A)(vii) |
| 11 | Qualified reservist distributions (active duty at least 180 days) | §72(t)(2)(G) |
| 12 | Distributions coded 1, J, or S in box 7 received at age 59½ or older | — |
| 13 | Section 457 plan distributions not from a rollover from a qualified plan | — |
| 14 | Employer plan distributions under a pre-March 1, 1986 written election | — |
| 15 | Dividends on section 404(k) stock | §72(t)(2)(A)(vi) |
| 16 | Annuity distributions allocable to investment before August 14, 1982 | — |
| 17 | Phased retirement annuity payments to federal employees | §72(t)(2)(A)(viii) |
| 18 | Permissible withdrawals under §414(w) (eligible automatic contribution arrangements) | §414(w) |
| 19 | Qualified birth or adoption distributions, up to $5,000, within 1 year of the birth or adoption; attach a statement with the child's name, age, and TIN | §72(t)(2)(H) |
| 20 | Terminal illness (physician-certified, death expected within 84 months) | §72(t)(2)(L) |
| 21 | Corrective distributions of the income on excess contributions made by the due date including extensions | §72(t)(2)(A)(ix) |
| 22 | Domestic abuse victim distributions within 1 year of the abuse; lesser of $10,300 (2025; $10,500 for 2026) or 50% of the vested balance | §72(t)(2)(K) |
| 23 | Emergency personal expense distributions; one per calendar year, lesser of $1,000 or the vested balance over $1,000 | §72(t)(2)(I) |
| 99 | More than one exception applies | — |

Dollar limits for 22 and 23: Pub. 590-B (2025), "Domestic abuse victim
distributions" and "Emergency personal expense distributions"; 2026 domestic
abuse limit: Notice 2025-67.

### Line 3 — Amount subject to additional tax

Line 1 − Line 2.

### Line 4 — Additional tax

Line 3 × 10%, **except**:
- 25% for the part of Line 3 that is a SIMPLE IRA distribution received
  within 2 years from the date the user first participated in the SIMPLE
  IRA plan (box 7 code S)

The result goes on Schedule 2 (Form 1040), line 8.

---

## Part II — Additional Tax on Certain Distributions From Education Accounts and ABLE Accounts (Lines 5-8)

Applies to amounts included in income from a Coverdell ESA or a qualified
tuition program (QTP, Schedule 1 line 8z) or from an ABLE account (Schedule
1 line 8q).

| Line | Entry |
|------|-------|
| 5 | Distributions included in income from a Coverdell ESA, a QTP, or an ABLE account |
| 6 | Part of Line 5 not subject to the additional tax (see the Line 6 instructions: e.g., death or disability of the beneficiary, scholarships, military academy attendance) |
| 7 | Line 5 − Line 6 |
| 8 | 10% of Line 7 → Schedule 2, line 8 |

---

## Part III — Additional Tax on Excess Contributions to Traditional IRAs (Lines 9-17)

The 6% excise tax under IRC §4973 on excess contributions to traditional
IRAs (including traditional SEP and SIMPLE IRAs per the Part III heading),
applied each year the excess remains.

| Line | Entry (2025 form) |
|------|-------------------|
| 9 | Excess contributions from line 16 of the 2024 Form 5329 (only if 2024 line 17 was more than zero). If zero, go to line 15 |
| 10 | If 2025 traditional IRA contributions are less than the maximum allowable: contribution limit minus 2025 traditional **and** Roth IRA contributions; otherwise -0- |
| 11 | 2025 traditional IRA distributions included in income (not the withdrawn contributions on Line 12) |
| 12 | 2025 distributions of prior-year excess contributions (returned in 2025, not deducted, per the Line 12 conditions) |
| 13 | Line 10 + Line 11 + Line 12 |
| 14 | Prior-year excess remaining: Line 9 − Line 13, not less than 0 |
| 15 | Excess contributions for 2025 (contributions over the limit, not counting amounts withdrawn by the due date with earnings, and not counting rollovers) |
| 16 | Total excess: Line 14 + Line 15 (carries to next year's Line 9) |
| 17 | 6% × the smaller of Line 16 or the value of the traditional IRAs on December 31, 2025 (including 2025 contributions made in 2026) → Schedule 2, line 8 |

2025 contribution limit (Line 10 instructions): the smaller of taxable
compensation or $7,000 ($8,000 if 50 or older at the end of 2025). 2026:
$7,500 ($8,600 if 50 or older) (Notice 2025-67). The Line 10 amount also
goes on line 11a or 11b of the IRA Deduction Worksheet (the smaller of
Line 10 or Line 9 minus Lines 11 and 12).

**Withdrawal before the due date** (Line 15 instructions): withdraw the
excess by the due date including extensions, take no deduction for it, and
withdraw the earnings. The earnings are income (Pub. 590-A: for the year
the excess contribution was made); if under 59½, put them on Line 1 and on
Line 2 with exception 21. Timely filers who missed it can still withdraw
within 6 months of the due date excluding extensions and amend ("Filed
pursuant to section 301.9100-2").

**Compounding warning**: an uncorrected excess incurs the 6% tax *every
year* until corrected. A $5,000 excess uncorrected for 5 years = $1,500
in cumulative tax.

---

## Part IV — Additional Tax on Excess Contributions to Roth IRAs (Lines 18-25)

Mirrors Part III for Roth IRAs (including Roth SEP and Roth SIMPLE IRAs).
The most common cause of Roth excess: the user contributed before knowing
their MAGI and ended the year inside or above the phaseout.

| Line | Entry (2025 form) |
|------|-------------------|
| 18 | Excess contributions from line 24 of the 2024 Form 5329 (only if 2024 line 25 was more than zero). If zero, go to line 23 |
| 19 | If 2025 Roth contributions are less than the Roth limit: the difference; otherwise -0- |
| 20 | 2025 distributions from Roth IRAs: generally Form 8606 line 19 plus qualified distributions (if the entire Roth balance was withdrawn, not less than Line 18) |
| 21 | Line 19 + Line 20 |
| 22 | Prior-year excess remaining: Line 18 − Line 21, not less than 0 |
| 23 | Excess Roth contributions for 2025 (over the Roth limit, not counting amounts withdrawn by the due date with earnings, and not counting rollovers) |
| 24 | Total excess: Line 22 + Line 23 (carries to next year's Line 18) |
| 25 | 6% × the smaller of Line 24 or the value of the Roth IRAs on December 31, 2025 (including 2025 contributions made in 2026) → Schedule 2, line 8 |

Roth limit (Line 19 instructions): the traditional IRA limit reduced by
traditional IRA contributions, further reduced or eliminated when modified
AGI is over $236,000 (MFJ or qualifying surviving spouse), $150,000 (single,
HOH, or MFS not living with the spouse at any time in 2025), or $0 (MFS and
lived with the spouse at any time in 2025). Phaseout ranges: 2025 $150,000–
$165,000 single / $236,000–$246,000 MFJ (Notice 2024-80); 2026 $153,000–
$168,000 / $242,000–$252,000 (Notice 2025-67); MFS living with spouse $0–
$10,000.

**Correction options for Roth excess**:

1. **Withdraw excess + earnings by the due date (incl. extensions)**
   — eliminates the 6% tax. Earnings are taxable (Pub. 590-A: for the year
   the excess contribution was made); if user is under 59½, the earnings
   go on Part I Line 1 and Line 2 with exception 21, so no 10% tax.
2. **Recharacterize to traditional IRA** — treats the contribution as a
   traditional contribution from the start. Eliminates Roth-side excess
   but creates traditional-side issues if user also exceeded the
   traditional limit or wasn't deductible-eligible.
3. **Apply to next year** — if the user is Roth-eligible next year and
   contributes less, the unused limit (Line 19) absorbs the carried-over
   excess. The 6% tax still applies in the year(s) the excess sat in the
   account.
4. **Pay the 6%** — accept the tax for the current year; correct next
   year.

---

## Part V — Additional Tax on Excess Contributions to Coverdell ESAs (Lines 26-33)

Same structure as Parts III/IV: Line 26 prior-year excess (2024 line 32),
Line 27 unused 2025 limit, Line 28 2025 Coverdell distributions, Line 29 =
27 + 28, Line 30 = 26 − 29 (not below 0), Line 31 2025 excess, Line 32 =
30 + 31, Line 33 = 6% × smaller of Line 32 or the December 31, 2025 value
→ Schedule 2, line 8. Limit: smaller of $2,000 or the sum of what the
contributors may contribute (Line 27 instructions).

---

## Part VI — Additional Tax on Excess Contributions to Archer MSAs (Lines 34-41)

Line 34 prior-year excess (2024 line 40), Line 35 unused 2025 limit, Line
36 2025 Archer MSA distributions from Form 8853 line 8, Line 37 = 35 + 36,
Line 38 = 34 − 37 (not below 0), Line 39 2025 excess, Line 40 = 38 + 39,
Line 41 = 6% × smaller of Line 40 or the December 31, 2025 value →
Schedule 2, line 8. Rare; most filers have HSAs (Part VII).

---

## Part VII — Additional Tax on Excess Contributions to HSAs (Lines 42-49)

| Line | Entry (2025 form) |
|------|-------------------|
| 42 | Excess contributions from line 48 of the 2024 Form 5329 (only if 2024 line 49 was more than zero). If zero, go to line 47 |
| 43 | If 2025 HSA contributions (Form 8889 line 2) are less than the limit (Form 8889 line 12): the difference; otherwise -0- |
| 44 | 2025 HSA distributions from Form 8889, line 16 |
| 45 | Line 43 + Line 44 |
| 46 | Prior-year excess remaining: Line 42 − Line 45, not less than 0 |
| 47 | Excess contributions for 2025: Form 8889 line 2 (unless withdrawn by the due date incl. extensions) over Form 8889 line 12, plus any excess employer contributions |
| 48 | Total excess: Line 46 + Line 47 |
| 49 | 6% × the smaller of Line 48 or the value of the HSAs on December 31, 2025 (including 2025 contributions made in 2026) → Schedule 2, line 8 |

Also include on 2025 Form 8889 line 13 the smaller of Line 43 or Line 42
minus Line 44 (2025 Instructions, Line 43). Withdrawn excess and earnings go
on Form 8889 lines 14a and 14b, not on Line 47.

HSA limits: 2025 $4,300 self-only / $8,550 family (Rev. Proc. 2024-25);
2026 $4,400 / $8,750 (Rev. Proc. 2025-19); +$1,000 at 55+. For the
HSA-side reporting, see [`../../form-8889/SKILL.md`](../../form-8889/SKILL.md).

---

## Part VIII — Additional Tax on Excess Contributions to an ABLE Account (Lines 50-51)

| Line | Entry |
|------|-------|
| 50 | Excess contributions for 2025 (see the Line 50 instructions) |
| 51 | 6% × the smaller of Line 50 or the value of the ABLE account on December 31, 2025 → Schedule 2, line 8 |

The general ABLE limit is the annual gift tax exclusion ($19,000 for 2025,
Rev. Proc. 2024-40; $19,000 for 2026, Rev. Proc. 2025-32), with an
additional allowance for employed beneficiaries.

---

## Part IX — Additional Tax on Excess Accumulation in Qualified Retirement Plans (Lines 52a-55)

The missed-RMD Part. Applies under IRC §4974. The tax is 25% of the excess
accumulation, reduced to 10% for a plan whose full shortfall was
distributed during the correction window (and the return reflecting the
tax was filed in that window).

| Line | Entry (2025 form) |
|------|-------------------|
| 52a | 2025 minimum required distribution from all plans for which the user received the full excess accumulation during the correction window |
| 52b | 2025 minimum required distribution from all other plans |
| 53a | Amount distributed during 2025 from the plans on Line 52a |
| 53b | Amount distributed during 2025 from the plans on Line 52b |
| 54a | (Line 52a − Line 53a) × 10%, not less than 0 |
| 54b | (Line 52b − Line 53b) × 25%, not less than 0 |
| 55 | Line 54a + Line 54b → Schedule 2 (Form 1040), line 8 (or Form 1041, Schedule G, line 8) |

Lines 53a/53b exclude any distribution received after the RMD deadline or
during the correction window (2025 Instructions, Lines 53a and 53b).

### RMD amount (Lines 52a/52b)

```
RMD = (Account balance on December 31 of prior year) ÷ (Distribution period factor)
```

Distribution period factor comes from Pub. 590-B (2025), Appendix B:

- **Table III (Uniform Lifetime)** — most living owners
- **Table II (Joint Life and Last Survivor)** — owner whose sole
  beneficiary is a spouse more than 10 years younger
- **Table I (Single Life)** — beneficiaries of inherited accounts (with the
  10-year rule for non-eligible designated beneficiaries for deaths after
  12/31/2019)

The custodian's reported RMD amount may be used. IRA RMDs are figured per
IRA but may be withdrawn from any of the owner's traditional IRAs; inherited
IRAs aggregate only with IRAs inherited from the same decedent; 403(b)
RMDs may be totaled and taken from any 403(b); other qualified plans
cannot be aggregated (2025 Instructions, Lines 53a and 53b).

### Correction window (2025 Instructions, Reduced tax rate)

Ends on the earliest of: the date a deficiency notice for this tax is
mailed, the date the tax is assessed, or the last day of the second
taxable year that begins after the end of the taxable year in which the tax
is imposed (for a missed 2025 RMD: December 31, 2027).

### Reasonable-cause waiver (IRC §4974(d))

1. Complete Lines 52a/52b and 53a/53b as instructed.
2. Write "RC" and the shortfall amount to be waived in parentheses on the
   dotted line next to Line 54a and/or 54b; subtract it from the shortfall
   and enter the result (at that line's rate) on Line 54a/54b.
3. Complete Line 55 and pay any tax shown. Attach a statement of
   explanation. See [`missed-rmd.md`](./missed-rmd.md) for the template.

The IRS reviews the request; if it is not granted, the IRS notifies the
user of the additional tax.

---

## How Form 5329 totals flow

The tax from each Part (Lines 4, 8, 17, 25, 33, 41, 49, 51, 55) goes on
Schedule 2 (Form 1040), line 8 ("Additional tax on IRAs or other
tax-favored accounts"). Spouses each filing a 5329 combine their taxes on
that line.

Schedule 2 line 8 → Schedule 2 line 21 (total other taxes) → Form 1040
line 23 (2025 forms).

---

## Standalone signature block

When Form 5329 is filed by itself (no 1040 required), the user completes
the address on page 1 and signs and dates page 3; it cannot be filed
electronically. When attached to a 1040, the 1040 signature covers the
5329 and the standalone signature block is left blank.
