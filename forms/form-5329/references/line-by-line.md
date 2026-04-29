# Form 5329 Line-by-Line Reference

Complete lookup for every line on Form 5329. Use this when the agent needs
to confirm where a number belongs or what a line means. Lines are grouped
by Part. Line numbers reflect the 2024 revision of Form 5329; verify
against the current revision before filing.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Filer's legal name | Even if filed standalone |
| SSN | Filer's SSN | Or ITIN if no SSN |
| Address | Filer's mailing address | **Only when filing standalone**. Blank when attached to 1040. |
| Apartment / city / state / ZIP | Address fields | Standalone only |
| Foreign country | Box for foreign address | Standalone only |
| Amended return checkbox | Check if amending a prior 5329 | |

---

## Part I — Additional Tax on Early Distributions (Lines 1-4)

Applies under IRC §72(t) to distributions before age 59½ from:

- Traditional IRA, SEP-IRA, SIMPLE IRA
- Roth IRA (earnings portion only; basis comes out tax-free)
- 401(k), 403(b), governmental 457(b)
- Qualified annuity plans
- Modified endowment contracts (in some cases)

The 1099-R Box 7 distribution code is the first signal but not the final
authority. Common codes:

| Code | Meaning | Default 10% applies? |
|------|---------|----------------------|
| 1 | Early distribution, no known exception | Yes |
| 2 | Early distribution, exception applies (per custodian) | Custodian thinks no |
| 3 | Disability | No (but document) |
| 4 | Death | No |
| 7 | Normal distribution (post-59½) | No |
| 8 | Excess contribution returned in same year | No (but earnings may) |
| J | Early distribution from Roth IRA | Apply ordering rules — basis first |
| L | Loan treated as deemed distribution | Yes, if under 59½ |
| S | Early distribution from SIMPLE IRA in first 2 years | **25%, not 10%** |

If the custodian coded Box 7 as "1" but the user qualifies for an exception,
the user claims it on Line 2 — the IRS does not require the custodian to
recode.

### Line 1 — Early distributions includible in income

Sum of all distributions from the user's qualified plans, IRAs, and
similar accounts that were taken before age 59½ AND are includible in
income.

For Roth IRAs: only the earnings portion is includible in income (basis
comes out tax-free under the ordering rules). If the entire distribution
was Roth basis (contributions + conversions held 5+ years), Line 1 is 0
for that distribution. See [`references/early-distribution-exceptions.md`](./early-distribution-exceptions.md).

### Line 2 — Distributions excepted from additional tax

The amount of Line 1 that qualifies for an exception. The user enters the
amount and the two-digit code from the Form 5329 instructions:

| Code | Exception | IRC § |
|------|-----------|-------|
| 01 | Separation from service after age 55 (not IRAs) | §72(t)(2)(A)(v) |
| 02 | SoSEPP — substantially equal periodic payments | §72(t)(2)(A)(iv) |
| 03 | Disability | §72(t)(2)(A)(iii) + §72(m)(7) |
| 04 | Beneficiary distributions after death | §72(t)(2)(A)(ii) |
| 05 | Medical expenses > 7.5% of AGI | §72(t)(2)(B) |
| 06 | IRS levy | §72(t)(2)(A)(vii) |
| 07 | Higher education expenses (IRAs only) | §72(t)(2)(E) |
| 08 | First-time homebuyer (IRAs only, $10K lifetime) | §72(t)(2)(F) |
| 09 | Reservist called to active duty | §72(t)(2)(G) |
| 10 | Birth or adoption ($5,000/child) | §72(t)(2)(H) |
| 11 | Domestic abuse victim (SECURE 2.0 §314, 2024+; verify cap) | §72(t)(2)(K) |
| 12 | Terminal illness | §72(t)(2)(L) |
| 13 | Federally declared disaster | §72(t)(2)(M) + Notice |
| 14 | Emergency personal expense ($1,000, once/year) | §72(t)(2)(I) (SECURE 2.0 §115) |

Multiple exception codes can apply to portions of Line 1. The instructions
specify how to enter multiple codes. The total amount excepted goes in the
column; the codes go in the description column.

### Line 3 — Amount subject to additional tax

Line 1 − Line 2.

### Line 4 — Additional tax

Line 3 × 10%, **except**:
- Line 3 × 25% if the distribution was from a SIMPLE IRA within 2 years of
  the date the user first participated in the SIMPLE plan

The result flows to Schedule 2, Line 8.

---

## Part II — Additional Tax on Certain Distributions From Education Accounts and ABLE Accounts (Lines 5-8)

Applies to taxable distributions from Coverdell ESAs and ABLE accounts
that were not used for qualified expenses.

### Line 5 — Distributions includible in income

Total taxable portion of distributions from Coverdell ESAs and qualified
ABLE programs.

### Line 6 — Distributions excepted

Amounts that qualify for an exception:
- Death of the beneficiary
- Disability of the beneficiary
- Scholarship-equivalent (Coverdell)
- Military academy attendance (Coverdell)

### Line 7 — Subject to additional tax

Line 5 − Line 6.

### Line 8 — Additional tax

Line 7 × 10%. Flows to Schedule 2, Line 8.

---

## Part III — Additional Tax on Excess Contributions to Traditional IRAs (Lines 9-17)

The 6% excise tax under IRC §4973 on excess contributions to a traditional
IRA, applied each year the excess remains in the account.

### Line 9 — Current-year excess contribution

Contributions to traditional IRAs minus the lesser of:
- The user's deductible-and-nondeductible contribution limit for the year
  (the IRA contribution limit), AND
- The user's earned income for the year

### Line 10 — Prior-year excess from last year's Line 16

Carryover. If the user had no prior-year 5329, this is 0.

### Lines 11-13 — Adjustments

If the user took distributions of the excess (with earnings) before the
filing deadline, those reduce the excess for purposes of Lines 14-16.

### Line 14 — Adjusted prior-year excess after adjustments

The cleaned-up prior-year excess that remains.

### Line 15 — Total excess for the year

Line 9 + Line 14 (or similar — verify the current revision's wording).

### Line 16 — Smaller of total excess or account value

The 6% tax is calculated on the *smaller* of:
- The total excess remaining in the account, AND
- The fair market value of the IRA at year-end

This caps the tax. If the account lost value, the user can't be taxed on
more than what's actually there.

### Line 17 — Additional tax

Line 16 × 6%. Flows to Schedule 2, Line 8.

**Compounding warning**: an uncorrected excess incurs the 6% tax *every
year* until corrected. A $5,000 excess uncorrected for 5 years = $1,500
in cumulative tax.

---

## Part IV — Additional Tax on Excess Contributions to Roth IRAs (Lines 18-25)

Mirrors Part III but for Roth IRAs. The most common cause of Roth excess:

- User contributed early in the year before knowing their MAGI
- User crossed the Roth phaseout (MAGI between the limits) or fully
  exceeded the upper limit
- The contribution is now partially or fully ineligible

### Line 18 — Prior-year excess

Carryover from prior 5329 Line 24.

### Line 19 — Current-year excess Roth contribution

Contributions to Roth IRAs minus the user's allowed Roth contribution
(after applying the MAGI phaseout).

### Lines 20-23 — Adjustments

Distributions of excess + earnings before deadline; recharacterizations to
traditional IRAs.

### Line 24 — Total excess

Carries forward to next year if not corrected.

### Line 25 — Additional tax

Line 24 × 6%, capped at 6% of Roth IRA value at year-end. Flows to
Schedule 2, Line 8.

**Correction options for Roth excess**:

1. **Withdraw excess + earnings before filing deadline (incl. extensions)**
   — eliminates the 6% tax. Earnings are taxable in the year of
   contribution; if user is under 59½, earnings also subject to Part I.
2. **Recharacterize to traditional IRA** — treats the contribution as a
   traditional contribution from the start. Eliminates Roth-side excess
   but creates traditional-side issues if user also exceeded the
   traditional limit or wasn't deductible-eligible.
3. **Apply to next year** — if the user expects to be Roth-eligible next
   year and reduces next year's contribution, the carried-over excess
   absorbs into the new year's space. The 6% tax still applies in the
   year(s) the excess sat in the account.
4. **Pay the 6%** — accept the tax for the current year; correct next
   year. Reasonable when the alternative is recharacterization to a
   nondeductible traditional IRA (worse outcome for many).

---

## Part V — Additional Tax on Excess Contributions to Coverdell ESAs (Lines 26-32)

6% on excess contributions to a Coverdell Education Savings Account. The
limit is $2,000 per beneficiary per year (across all contributors), with
income phaseouts on contributors.

Same mechanics as Parts III/IV. Flows to Schedule 2, Line 8.

---

## Part VI — Additional Tax on Excess Contributions to Archer MSAs (Lines 33-39)

Rare. Most filers have HSAs (Part VII) instead of Archer MSAs.

---

## Part VII — Additional Tax on Excess Contributions to HSAs (Lines 40-47)

6% on excess contributions to a Health Savings Account.

HSA contribution limits are coverage-type-dependent:
- Self-only HDHP coverage
- Family HDHP coverage
- Plus a catch-up for age 55+

These limits change annually; the IRS issues a Revenue Procedure each
spring (typically May) for the *following* year's HDHP / HSA limits. Verify
against the most recent Rev. Proc. before computing.

Mechanics same as Part III. Flows to Schedule 2, Line 8.

For HSA distribution-side reporting, see the `form-8889` skill — that's a
separate form, not Form 5329.

---

## Part VIII — Additional Tax on Excess Contributions to ABLE Accounts (Lines 48-51)

6% on excess ABLE contributions. ABLE contribution limit is the federal
annual gift tax exclusion ($18,000 for 2024, $19,000 for 2025; verify
2026), with an additional ABLE-to-Work allowance for employed
beneficiaries. Mechanics same as Part III.

---

## Part IX — Additional Tax on Excess Accumulation in Qualified Retirement Plans (Lines 52-55)

The missed-RMD Part. Applies under IRC §4974.

### Line 52 — Required minimum distribution

The RMD that should have been taken from each account. Compute as:

```
RMD = (Account balance on December 31 of prior year) ÷ (Distribution period factor)
```

Distribution period factor comes from one of the IRS life-expectancy tables:

- **Uniform Lifetime Table** — most living owners; spouse beneficiary same age
- **Joint Life and Last Survivor Table** — owner with spouse beneficiary
  more than 10 years younger
- **Single Life Table** — beneficiaries of inherited accounts (with the
  10-year rule for non-eligible designated beneficiaries under SECURE Act,
  applies for deaths after 12/31/2019)

The tables are in IRS Pub 590-B, Appendix B.

If multiple accounts (e.g., two traditional IRAs and a 401(k)), the user
computes the RMD for each and totals. RMDs from IRAs may be aggregated
across IRA accounts. RMDs from 401(k)s may *not* be aggregated with each
other or with IRAs — each plan's RMD must come from that plan.

### Line 53 — Amount actually distributed

The amount the user actually received from the same accounts in the tax
year.

### Line 54 — Excess accumulation

Line 52 − Line 53. The shortfall.

### Line 55 — Additional tax

**Three rate paths**:

1. **25% × Line 54** — default rate (per SECURE 2.0, dropped from 50% to
   25% for tax years beginning after 12/31/2022)
2. **10% × Line 54** — if the user takes the missed amount within 2 years
   of the end of the year it should have been taken (SECURE 2.0 §302
   "corrective distribution" reduction; IRC §4974(e))
3. **0 (with waiver request)** — if the user requests a reasonable-cause
   waiver under IRC §4974(d). User writes 0 on Line 55 and attaches a
   statement explaining the cause and the corrective steps. See
   [`references/missed-rmd.md`](./missed-rmd.md) for the waiver template.

The result on Line 55 flows to Schedule 2, Line 8.

**Aggregation note**: if the user missed RMDs across multiple accounts,
each account's shortfall sums into Line 54. The waiver, if requested,
should identify each affected account in the attachment.

---

## How Form 5329 totals flow

Form 5329 is unusual: the tax from each Part flows to a single line on
Schedule 2 (Additional Taxes), Line 8.

Schedule 2 Line 8 → Schedule 2 Line 21 (total) → Form 1040 Line 23.

If the user has *only* a Form 5329 tax and no other Schedule 2 items, the
flow is direct: Form 5329 sum → Schedule 2 Line 8 → Schedule 2 Line 21 →
Form 1040 Line 23.

Always reconcile: the agent's draft total at the bottom of Form 5329 must
equal the number that ends up on Form 1040 Line 23 (after any other
Schedule 2 additions).

---

## Standalone signature block

When Form 5329 is filed standalone (not attached to a 1040), the form
itself has a signature line at the bottom — *only used in standalone
filing*. When attached to a 1040, the 1040 signature covers the 5329 and
the 5329 standalone signature line is left blank.
