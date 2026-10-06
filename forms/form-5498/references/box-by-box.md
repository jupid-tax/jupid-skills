# Form 5498 Box-by-Box Reference

Complete lookup for every box on Form 5498. Use this when the agent needs
to confirm what a box means or what a value indicates. Verified against
the 2025 Form 5498 and the 2025 Instructions for Forms 1099-R and 5498;
the 2026 Form 5498 keeps the same box numbers. Verify against the IRS form
for the specific year being reviewed
(https://www.irs.gov/forms-pubs/about-form-5498).

---

## Header section

| Field | What goes here | Notes |
|-------|----------------|-------|
| TRUSTEE'S/ISSUER'S name, address, TIN | Custodian (Fidelity, Vanguard, Schwab, etc.) | Same custodian on every 5498 from one account |
| PARTICIPANT'S name, address | Account holder's mailing address on file | Verify this is the user's current address |
| PARTICIPANT'S TIN (SSN) | Account holder's SSN | Should match the user's SSN exactly |
| Account number | Custodian's internal account number | Useful for tying to account statements |
| CORRECTED checkbox | Marked if this 5498 corrects a previously issued one | If checked, this replaces the prior 5498 |

---

## Box 1 — IRA contributions (other than amounts in boxes 2-4, 8-10, 13a, and 14a)

**What it is**: Total **traditional IRA** contributions for the tax year,
including contributions designated for that year and made by April 15 of
the next year. A filing extension does not extend this date. The amount
is gross: it includes any excess contribution even if it was later
withdrawn (2025 Instructions for Forms 1099-R and 5498, Box 1).

**What it excludes**: Rollovers (Box 2), Roth conversions (Box 3),
recharacterizations (Box 4), SEP contributions (Box 8), SIMPLE
contributions (Box 9), Roth IRA contributions (Box 10), postponed
contributions and late rollovers (Box 13a), repayments (Box 14a).

**Contribution year flag**: A contribution made in March 2026 designated
for tax year 2025 appears in Box 1 of the 2025-tax-year 5498 (furnished by
June 1, 2026). The user's 2025 tax return should have already reflected the
contribution, which was made before the return was filed.

**Reconciliation**:
- Schedule 1 Line 20 (deductible IRA contribution)
- Form 8606 Line 1 (nondeductible contribution amount) — keep running
  basis total

**Common values**: For 2025, the IRA dollar limit is $7,000 ($8,000 age
50+) per Notice 2024-80. For 2026, $7,500 ($8,600 age 50+) per Notice
2025-67.

---

## Box 2 — Rollover contributions

**What it is**: Total amount rolled over **into** this IRA during the
calendar year, from any source. Includes:
- 60-day rollovers (user received a distribution and re-contributed
  within 60 days)
- Direct rollovers from a qualified plan, 403(b), or governmental 457(b)
- Rollovers from a plan (other than an IRA) straight into a Roth IRA
- Military death gratuities and SGLI payments contributed to a Roth IRA

**What it excludes**: Roth conversions (Box 3), recharacterizations (Box 4),
late rollovers (Box 13a), repayments (Box 14a). Trustee-to-trustee
transfers between IRAs of the same type are not reported on Form 5498.

**Reconciliation**:
- Form 1040 Line 5a (gross 401(k)/403(b)/etc. distribution) or Line 4a
  (IRA-to-IRA 60-day rollover)
- Form 1040 Line 5b / 4b ($0 taxable if fully rolled over), with box 1
  ("Rollover") checked on Line 5c / 4c (2025 Form 1040)
- Corresponding 1099-R Box 7 codes:
  - **G** — Direct rollover from qualified plan to IRA or other plan
  - **H** — Direct rollover from designated Roth account to Roth IRA

**Edge case**: 60-day rollover where only part of the distribution was
rolled. The 1099-R shows the gross distribution. Box 2 of the 5498 shows
only the rolled-over portion. The non-rolled portion is taxable on Form
1040 Line 5b (and may be subject to 10% early-distribution tax if the
user is under 59½).

A rollover deposited after the 60-day window is reported in Box 13a
(code SC if the user self-certified under Rev. Proc. 2020-46, code PO for
a qualified plan loan offset), not Box 2.

---

## Box 3 — Roth IRA conversion amount

**What it is**: Amount converted from a traditional IRA, SEP-IRA, or
SIMPLE IRA to a Roth IRA during the calendar year.

**Reconciliation**:
- 1099-R from the traditional IRA (Box 7 code 2 if user under 59½ — the
  1099-R instructions list "A Roth IRA conversion" under code 2 — or
  code 7 if user 59½+)
- Form 1040 Line 4a (gross distribution = Box 1 of the 1099-R)
- Form 1040 Line 4b (taxable portion, computed via Form 8606 Part II)
- Form 8606 Part II Lines 16-18 — apportions the conversion between
  taxable (pre-tax) and tax-free (basis) portions; Line 17 comes from Part
  I Line 11 when the user has basis

**Critical mismatch warning**: Box 3 should equal Box 1 of the 1099-R
(the gross conversion). It should NOT equal Form 1040 Line 4b — that's
the *taxable* portion which is smaller if the user has basis.

If Box 3 = $25,000, 1099-R Box 1 = $25,000, but Form 1040 Line 4b =
$20,000, that's likely correct: the user had $5,000 of nondeductible
basis from prior 8606s and the pro-rata rule applied.

If Box 3 = $25,000 but the user reported $25,000 on Form 1040 Line 4b
(no Form 8606 used), they may have over-reported. Check whether the
user has any nondeductible IRA basis from prior years.

---

## Box 4 — Recharacterized contributions

**What it is**: Amount of contributions recharacterized between
traditional and Roth IRAs during the year. Recharacterization treats a
contribution to one type as if it had been made to the other type from
the start.

**TCJA change (2018+)**: Conversions can no longer be recharacterized.
Only contribution-recharacterizations are still permitted.

**Reconciliation**:
- The user's records should show a contribution being recharacterized
  via the custodian
- The **first** IRA's trustee reports the original contribution on that
  IRA's Form 5498 (Box 1 or Box 10) and the recharacterization as a
  distribution on Form 1099-R (code N for a same-year contribution, R for
  a prior-year one)
- The **second** IRA's trustee reports the amount received (FMV, with
  earnings) in Box 4 and checks the IRA type in Box 7
- The tax return should reflect the contribution as having been to the
  *destination* IRA type, not the original

**Edge case**: If the user recharacterized a Roth contribution to
traditional, Box 10 of the Roth 5498 still shows the original
contribution, the Roth custodian's 1099-R shows code N, and Box 4 of the
traditional 5498 shows the amount moved. Together they describe the round
trip (2025 Instructions for Forms 1099-R and 5498, "Recharacterizations").

---

## Box 5 — FMV of account on December 31

**What it is**: Fair market value of the IRA on the last day of the
calendar year.

**Why it matters**:
1. **Drives next year's RMD calculation**: Next year's RMD = Box 5 ÷
   distribution period factor for next year's age
2. **Caps the 6% excess contribution tax** under IRC §4973: tax = 6% ×
   min(excess, account value 12/31)
3. **Used in Backdoor Roth pro-rata calculations**: Form 8606 Line 6
   takes the December 31 value of all traditional / SEP / SIMPLE IRAs
   (plus outstanding rollovers); basis ÷ (Line 6 + distributions +
   conversions) is the tax-free percentage (Form 8606 Lines 6–10)

**Multiple IRAs**: Sum Box 5 across all IRAs of the same type for the
applicable calculation. Traditional IRAs aggregate for RMD; SEP and
SIMPLE aggregate with traditional IRAs for RMD purposes; Roth IRAs do
NOT aggregate with traditional for the 8606 basis pro-rata
calculation (Roth has its own basis tracking).

---

## Box 6 — Life insurance cost

**What it is**: For endowment contracts only, the part of Box 1 allocable
to the cost of life insurance.

**For most filers**: Blank. Skip.

**If populated**: Subtract the Box 6 amount from the allowable IRA
contribution included in Box 1 to figure the IRA deduction (Form 5498,
Instructions for Participant, Box 6). This is a niche case; refer to Pub
590-A or a CPA.

---

## Box 7 — IRA type (checkbox)

**What it is**: Indicator of which type of IRA this account is. One of:

| Box 7 value | Account type | Relevant contribution box |
|-------------|--------------|---------------------------|
| IRA | Traditional IRA | Box 1 |
| Roth IRA | Roth IRA | Box 10 |
| SEP | Simplified Employee Pension IRA | Box 8 |
| SIMPLE | Savings Incentive Match Plan IRA | Box 9 |
| SEP + Roth IRA | Roth SEP IRA | Box 8 |
| SIMPLE + Roth IRA | Roth SIMPLE IRA | Box 9 |

If the custodian does not know whether an account is a SEP IRA, it checks
"IRA" (2025 Instructions, Box 7).

**Critical**: Box 7 must be consistent with the populated contribution
box. If Box 7 = "Roth IRA" but Box 1 (not Box 10) is populated, the
custodian made a coding error.

---

## Box 8 — SEP contributions

**What it is**: SEP-IRA contributions **made during the calendar year**,
including contributions made in that year for the prior year and not
including contributions made in the next year for this year. Trustees do
not report which tax year a SEP contribution is for. Includes employer
contributions, salary deferrals under a SARSEP, the self-employed
person's own SEP contribution, and Roth SEP contributions (2025
Instructions, Box 8).

**Reconciliation**:
- Schedule 1 Line 16 (self-employed SEP/SIMPLE/qualified plan deduction)
  — for self-employed filers. The deduction belongs to the tax year the
  contribution is for, so a 2025 contribution deposited in 2026 is on the
  2026 Form 5498
- W-2 Box 12 code F — only SARSEP salary deferrals; ordinary employer SEP
  contributions are excluded from W-2 Box 1 and are not shown with a Box
  12 code

**SEP limit**: The lesser of 25% of compensation or $70,000 for 2025
(Notice 2024-80) / $72,000 for 2026 (Notice 2025-67); compensation counted
up to $350,000 / $360,000. Self-employed owner: about 20% of net SE
earnings after deducting half of SE tax (Pub. 560 rate table).

---

## Box 9 — SIMPLE contributions

**What it is**: SIMPLE-IRA contributions **made during the calendar
year** (same calendar-year basis as Box 8), including employee deferrals,
employer matching/non-elective contributions, and Roth SIMPLE
contributions.

**Reconciliation**:
- Schedule 1 Line 16 (for self-employed filers' SIMPLE plan)
- W-2 Box 12 code S — for employees of an employer SIMPLE plan, the
  employee deferral is recorded in Box 12 code S

**SIMPLE deferral limit**: $16,500 for 2025 ($20,000 age 50+; $21,750 at
ages 60-63) per Notice 2024-80; $17,000 for 2026 ($21,000 age 50+;
$22,250 at ages 60-63) per Notice 2025-67. Certain plans have a higher
base ($17,600 for 2025, $18,100 for 2026). Plus mandatory employer match
(3% of compensation) or non-elective contribution (2% of compensation,
capped).

---

## Box 10 — Roth IRA contributions

**What it is**: Total Roth IRA contributions for the tax year. Like Box
1, includes contributions designated for that year and made by April 15
of the next year (no extension). Also includes 529-to-Roth IRA rollovers
designated for the year (direct transfer, subject to the annual Roth
limit and a $35,000 lifetime limit, 529 account open more than 15 years).

**What it excludes**: Roth conversions (Box 3), rollovers (Box 2),
recharacterizations (Box 4).

**Reconciliation**: Roth contributions are **not deductible** and don't
appear on the return. The user's records must show Roth eligibility:
- MAGI below the applicable phaseout for the year (2025 phaseouts per
  Notice 2024-80: single/HOH $150K-$165K, MFJ $236K-$246K, MFS $0-$10K;
  2026 per Notice 2025-67: single/HOH $153K-$168K, MFJ $242K-$252K, MFS
  $0-$10K)
- Earned income ≥ contribution amount
- Aggregate contribution across all Roth accounts ≤ dollar limit

If Box 10 > the user's allowed contribution given MAGI, the difference
is excess. Use the `form-5329` skill Part IV.

---

## Box 11 — RMD required for next year (checkbox)

**What it is**: Indicator that the custodian has determined an RMD is
required for the calendar year following the 5498 year (2025 form: "Check
if RMD for 2026").

**When it should be checked**:
- Account holder reaches the applicable age in the following year (the
  box is checked for that year even though the first RMD can wait until
  April 1 of the year after it), and every later year. Applicable age: 73
  for owners who reach 72 after 2022 and 73 before 2033; 75 for owners who
  reach 74 after 2032 (IRC §401(a)(9)(C)(v))
- The account is a traditional IRA / SEP / SIMPLE

**When it should NOT be checked**:
- Roth IRA owned by the original owner (no lifetime RMD)
- Account holder will not reach the applicable age in the following year
- Inherited IRAs: until further guidance, custodians are not required to
  report RMDs for IRAs of deceased owners (unless a surviving spouse
  treats the IRA as their own), so the box is usually blank even when the
  beneficiary must take distributions (2025 Instructions, "RMDs")

**If Box 11 is wrong**: Contact the custodian for a corrected 5498. A
mistakenly checked Box 11 doesn't itself create a tax obligation, but
it can cause confusion and the custodian's automated RMD systems may
misfire.

---

## Box 12a — RMD date

**What it is**: The date the custodian computes as the RMD deadline.

**Typical values**:
- December 31 of the next year (for ongoing RMDs)
- April 1 of the next year (for first-year RMDs — the "required
  beginning date" delay)

---

## Box 12b — RMD amount

**What it is**: The custodian's computed RMD for the next calendar year.

**Computation**: Box 12b ≈ Box 5 ÷ distribution period factor for the
next year's age (Uniform Lifetime Table, Pub. 590-B Appendix B Table III;
custodians may assume the sole beneficiary is not a spouse more than 10
years younger).

**Important caveat**: Box 12b is the custodian's computation for the
*single account*. If the user has multiple IRAs, the user must compute
the aggregate RMD and may take it from any one or combination of IRAs
(IRA RMD aggregation rule). Box 12b is informational.

---

## Boxes 13a, 13b, 13c — Postponed/late rollover contributions

**What they report**: Postponed prior-year contributions and late
rollovers made during the calendar year:
- 13a — Amount of the postponed contribution or late rollover (not
  included in Box 1 or 2)
- 13b — Year for which a postponed contribution was made (blank for late
  rollovers and plan loan offset rollovers)
- 13c — Code: "FD" (federally designated disaster), "PO" (rollover of a
  qualified plan loan offset), "SC" (self-certified late rollover under
  Rev. Proc. 2020-46), or a combat-zone code (EO13239, EO12744, EO13119 /
  PL106-21, PL115-97)

**For most filers**: Blank.

**Specific cases**: Service in a combat zone, qualified hazardous duty
area, or direct support area extends the contribution period by the time
in the zone plus at least 180 days; federally declared disaster victims
get postponed deadlines per IRS announcements. Repayments of qualified
reservist distributions are not here — they go in Box 14a.

---

## Box 14a — Repayments

**What it reports**: Repayments of these distributions (2025 Instructions,
Box 14a; IRC §72(t)(2)):
- Qualified reservist distributions (code QR, §72(t)(2)(G))
- Qualified disaster distributions (code DD)
- Birth or adoption distributions (code BA, §72(t)(2)(H); $5,000 cap,
  repayable within 3 years)
- Emergency personal expense distributions (code EP, §72(t)(2)(I); $1,000
  cap, repayable within 3 years)
- Distributions to a domestic abuse victim (code DA, §72(t)(2)(K); cap
  $10,300 for 2025 and $10,500 for 2026 per Notices 2024-80 / 2025-67,
  repayable within 3 years)
- Terminally ill individual distributions (code TI, §72(t)(2)(L))

**Reconciliation**: The repayment is treated as a rollover for tax
purposes — not taxable on receipt by the IRA. The user reports the
original distribution (and any tax exception under §72(t)) on the year
of distribution; the repayment is informational on the 5498.

---

## Box 14b — Code for Box 14a

**What it reports**: The two-letter code for the repaid distribution:
QR, DD, BA, EP, DA, or TI.

---

## Box 15a — FMV of certain specified assets

**What it reports**: For self-directed IRAs holding hard-to-value assets,
the FMV as of December 31 of the investments in the categories coded in
Box 15b. Examples:
- Real estate held in IRA
- Private placements (non-traded stock)
- LLCs / partnerships
- Promissory notes and other non-traded debt
- Any other asset without a readily available FMV

**For most retail filers**: Blank.

**Why it matters**: Hard-to-value assets are a focus area for IRS
attention because of valuation disputes. Box 15a alerts the IRS that
non-public-market assets are in the account.

---

## Box 15b — Code for Box 15a

**What it reports**: Up to two codes for the asset types in Box 15a:
A (non-traded corporate stock), B (non-traded debt), C (non-traded LLC
interest), D (real estate), E (non-traded partnership or trust interest),
F (option not traded on an established exchange), G (other asset without
a readily available FMV), H (more than two types held).

---

## How custodian errors typically manifest

The most common 5498 errors the agent should watch for:

1. **Wrong contribution year designation** — March 15 contribution
   intended for prior year shows up in current year's Box 1
2. **Roth contribution miscoded as traditional** — Box 7 says "Roth IRA"
   but Box 1 (not Box 10) is populated, or vice versa
3. **Rollover double-counted as both Box 2 and a contribution** — if a
   rollover from another IRA was incorrectly flagged as a new
   contribution
4. **Box 11 checked for a Roth IRA** — Roth IRAs have no RMD for the
   original owner
5. **Box 5 stale or wrong** — should match the 12/31 account statement
6. **Box 3 conversion amount differs from 1099-R Box 1** — should match
   gross
