# Form 5498 Box-by-Box Reference

Complete lookup for every box on Form 5498. Use this when the agent needs
to confirm what a box means or what a value indicates. Box numbers reflect
the current Form 5498 revision; verify against the IRS form for the
specific year being reviewed.

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

## Box 1 — IRA contributions (other than amounts in boxes 2-4 and 8-10)

**What it is**: Total **traditional IRA** contributions for the tax year,
including contributions designated for the prior year and made by April
15 (or October 15 if extension was filed) of the next year.

**What it excludes**: Rollovers (Box 2), Roth conversions (Box 3),
recharacterizations (Box 4), SEP contributions (Box 8), SIMPLE
contributions (Box 9), Roth IRA contributions (Box 10).

**Contribution year flag**: A contribution made in March 2026 designated
for tax year 2025 appears in Box 1 of the 2025-tax-year 5498 (mailed May
2026). The user's 2025 tax return should have already reflected the
contribution before it was deposited.

**Reconciliation**:
- Schedule 1 Line 20 (deductible IRA contribution)
- Form 8606 Line 1 (nondeductible contribution amount) — keep running
  basis total

**Common values**: For 2025, the IRA dollar limit is $7,000 ($8,000 age
50+) per Notice 2024-80. Verify 2026 against the equivalent fall-2025
notice.

---

## Box 2 — Rollover contributions

**What it is**: Total amount rolled over **into** this IRA during the
calendar year, from any source. Includes both:
- 60-day rollovers (user received a distribution and re-contributed
  within 60 days)
- Direct rollovers (trustee-to-trustee)

**What it excludes**: Roth conversions (Box 3), recharacterizations (Box 4).

**Reconciliation**:
- Form 1040 Line 5a (gross 401(k)/403(b)/etc. distribution)
- Form 1040 Line 5b ($0 taxable for direct rollover; "Rollover" notation
  if 60-day rollover)
- Corresponding 1099-R Box 7 codes:
  - **G** — Direct rollover from qualified plan to IRA or other plan
  - **H** — Direct rollover from designated Roth account to Roth IRA

**Edge case**: 60-day rollover where only part of the distribution was
rolled. The 1099-R shows the gross distribution. Box 2 of the 5498 shows
only the rolled-over portion. The non-rolled portion is taxable on Form
1040 Line 5b (and may be subject to 10% early-distribution tax if the
user is under 59½).

---

## Box 3 — Roth IRA conversion amount

**What it is**: Amount converted from a traditional IRA, SEP-IRA, or
SIMPLE IRA to a Roth IRA during the calendar year.

**Reconciliation**:
- 1099-R from the traditional IRA (Box 7 code 2 if user under 59½ — the
  conversion exception — or code 7 if user 59½+)
- Form 1040 Line 4a (gross distribution = Box 1 of the 1099-R)
- Form 1040 Line 4b (taxable portion, computed via Form 8606 Part II)
- Form 8606 Part II Lines 16-18 — apportions the conversion between
  taxable (pre-tax) and tax-free (basis) portions

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
- A second 5498 may exist (if recharacterized to a different account)
  showing the contribution on the receiving side
- The tax return should reflect the contribution as having been to the
  *destination* IRA type, not the original

**Edge case**: If the user recharacterized a Roth contribution to
traditional, Box 4 of the Roth 5498 shows the amount, AND Box 1 of the
traditional 5498 includes the same amount. The two 5498s together
describe the round trip.

---

## Box 5 — FMV of account on December 31

**What it is**: Fair market value of the IRA on the last day of the
calendar year.

**Why it matters**:
1. **Drives next year's RMD calculation**: Next year's RMD = Box 5 ÷
   distribution period factor for next year's age
2. **Caps the 6% excess contribution tax** under IRC §4973: tax = 6% ×
   min(excess, account value 12/31)
3. **Caps the 25%/10% missed-RMD tax** in some interpretations
4. **Used in Backdoor Roth pro-rata calculations**: aggregate basis ÷
   aggregate value (Box 5 across all traditional IRAs) determines the
   tax-free percentage of any conversion

**Multiple IRAs**: Sum Box 5 across all IRAs of the same type for the
applicable calculation. Traditional IRAs aggregate for RMD; SEP and
SIMPLE aggregate with traditional IRAs for RMD purposes; Roth IRAs do
NOT aggregate with traditional for the 8606 basis pro-rata
calculation (Roth has its own basis tracking).

---

## Box 6 — Life insurance cost

**What it is**: Cost of life insurance protection included in Box 1 for
certain qualified plans treated as IRAs (e.g., section 408 endowment
contracts).

**For most filers**: Blank. Skip.

**If populated**: The amount in Box 6 is includible in income for the
year and represents the cost of pure insurance (rather than retirement
savings). This is a niche case; refer to Pub 590-A or a CPA.

---

## Box 7 — IRA type (checkbox)

**What it is**: Indicator of which type of IRA this account is. One of:

| Box 7 value | Account type | Relevant contribution box |
|-------------|--------------|---------------------------|
| IRA | Traditional IRA | Box 1 |
| Roth IRA | Roth IRA | Box 10 |
| SEP | Simplified Employee Pension IRA | Box 8 |
| SIMPLE | Savings Incentive Match Plan IRA | Box 9 |

**Critical**: Box 7 must be consistent with the populated contribution
box. If Box 7 = "Roth IRA" but Box 1 (not Box 10) is populated, the
custodian made a coding error.

---

## Box 8 — SEP contributions

**What it is**: Total contributions to a SEP-IRA (Simplified Employee
Pension) for the year. Includes employer contributions and (for self-
employed individuals) the self-employed person's own SEP contribution.

**Reconciliation**:
- Schedule 1 Line 16 (self-employed SEP/SIMPLE/qualified plan deduction)
  — for self-employed filers
- W-2 Box 12 code F — for employees of an employer SEP plan, the
  employer-side contribution is excluded from W-2 Box 1 and recorded in
  Box 12 code F

**SEP limit (2025)**: The lesser of $70,000 or 25% of compensation
(specific formula for self-employed: 20% of net SE earnings after
deducting half of SE tax). Verify against Notice 2024-80; verify 2026
in equivalent fall-2025 notice.

---

## Box 9 — SIMPLE contributions

**What it is**: Total contributions to a SIMPLE-IRA for the year,
including employee deferrals and employer matching/non-elective
contributions.

**Reconciliation**:
- Schedule 1 Line 16 (for self-employed filers' SIMPLE plan)
- W-2 Box 12 code S — for employees of an employer SIMPLE plan, the
  employee deferral is recorded in Box 12 code S

**SIMPLE limit (2025)**: $16,500 employee deferral ($20,000 age 50+).
Plus mandatory employer match (3% of compensation) or non-elective
contribution (2% of compensation, capped). Verify 2026.

---

## Box 10 — Roth IRA contributions

**What it is**: Total Roth IRA contributions for the tax year. Like Box
1, includes contributions designated for the prior year and made by
April 15 (or October 15 with extension) of the next year.

**What it excludes**: Roth conversions (Box 3), rollovers (Box 2),
recharacterizations (Box 4).

**Reconciliation**: Roth contributions are **not deductible** and don't
appear on the return. The user's records must show Roth eligibility:
- MAGI below the applicable phaseout for the year (2025 phaseouts per
  Notice 2024-80: single $150K-$165K, MFJ $236K-$246K, MFS $0-$10K;
  verify 2026)
- Earned income ≥ contribution amount
- Aggregate contribution across all Roth accounts ≤ dollar limit

If Box 10 > the user's allowed contribution given MAGI, the difference
is excess. Use the `form-5329` skill Part IV.

---

## Box 11 — RMD required for next year (checkbox)

**What it is**: Indicator that the custodian has determined an RMD is
required for the calendar year following the 5498 year.

**When it should be checked**:
- Account holder reaches age 73 in the 5498 year (first RMD due by
  April 1 of the year after; in practice most take it by 12/31 of the
  year of turning 73)
- Account holder is 73+ and the account is a traditional IRA / SEP /
  SIMPLE
- Account is an inherited IRA where annual RMDs apply

**When it should NOT be checked**:
- Roth IRA owned by the original owner (no lifetime RMD)
- Account holder is under 73 and not subject to inherited-IRA RMDs

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
next year's age (using the Uniform Lifetime Table for most owners; the
Single Life Table for inherited accounts).

**Important caveat**: Box 12b is the custodian's computation for the
*single account*. If the user has multiple IRAs, the user must compute
the aggregate RMD and may take it from any one or combination of IRAs
(IRA RMD aggregation rule). Box 12b is informational.

---

## Boxes 13a, 13b, 13c — Postponed/late rollover contributions

**What they report**: Contributions postponed or repaid late under
specific provisions:
- 13a — Amount of postponed/late contribution
- 13b — Year for which the contribution applies
- 13c — Code identifying the type of postponed contribution
  (military reservist, qualified disaster, etc.)

**For most filers**: Blank.

**Specific cases**: Military reservists called to active duty have
extended contribution windows; federally declared disaster victims have
extended deadlines per IRS notices.

---

## Box 14a — Repayments

**What it reports**: Repayments of distributions allowed under SECURE
2.0:
- Birth or adoption distributions ($5,000 cap, repayable within 3 years)
- Emergency personal expense distributions ($1,000 cap, repayable within
  3 years)
- Terminal illness distributions
- Domestic abuse victim distributions ($10K cap, repayable within 3
  years)

**Reconciliation**: The repayment is treated as a rollover for tax
purposes — not taxable on receipt by the IRA. The user reports the
original distribution (and any tax exception under §72(t)) on the year
of distribution; the repayment is informational on the 5498.

---

## Box 14b — Code for Box 14a

**What it reports**: A two-letter code identifying the type of
distribution that was repaid. See the Form 5498 instructions for the
current code list.

---

## Box 15a — FMV of certain specified assets

**What it reports**: For self-directed IRAs holding hard-to-value assets,
the FMV of those specific assets. Examples:
- Real estate held in IRA
- Private placements
- Crypto (in custodians who treat it as a specified asset)
- LLCs / partnerships
- Promissory notes

**For most retail filers**: Blank.

**Why it matters**: Hard-to-value assets are a focus area for IRS
attention because of valuation disputes. Box 15a alerts the IRS that
non-public-market assets are in the account.

---

## Box 15b — Code for Box 15a

**What it reports**: A code identifying the asset type in Box 15a. Codes
include real estate, partnerships/LLCs, secured/unsecured debt, etc.
See the Form 5498 instructions for the current code list.

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
