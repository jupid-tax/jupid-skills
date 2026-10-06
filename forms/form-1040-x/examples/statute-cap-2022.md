# Example: 2022 Refund Claim After a CP2000 — Timely, but Capped by the Lookback Rule

A single filer's 2022 return was already adjusted by a CP2000. In October 2026 he finds a deductible traditional IRA contribution he never claimed. The 3-year window has closed; a 2-year window remains open only because he paid the CP2000 tax in December 2024, and the refund is capped at that payment. All 2022 figures come from the 2022 Instructions for Form 1040 (prior-year PDF at https://www.irs.gov/pub/irs-prior/i1040gi--2022.pdf). Math and dates checked in Python (see notes file).

**CPA review flag:** this example shows how the agent documents a capped claim. How to present the barred amount on lines 22–23 and in Part II is a judgment call; the agent marks it for professional review before filing.

## The filer

- **Name**: Marcus Lindqvist (single), Ohio resident
- **Tax year amended**: 2022 (amendment prepared October 20, 2026)
- **Original return**: e-filed February 27, 2023; refund of $370 received
- **IRS changes**: CP2000 in 2024 added $4,650 of unreported Form 1099-MISC other income; Marcus agreed and paid the additional **$1,023 of tax** (plus interest) on **December 3, 2024**. No penalty was assessed (agent asked and checked the notice). No other amendment.

## Inputs gathered

### Original 2022 return

| Item | Amount |
|---|---|
| Wages (W-2 box 1) | $58,930 |
| Federal income tax withheld | $6,102 |
| Standard deduction, single (2022 Instructions for Form 1040) | $12,950 |
| Taxable income | $45,980 |
| Tax, 2022 Tax Table row $45,950–$46,000, Single | $5,732 |
| Overpayment refunded | $370 |

### As adjusted by the CP2000 (this becomes column A)

| Item | Amount |
|---|---|
| AGI ($58,930 + $4,650) | $63,580 |
| Taxable income | $50,630 |
| Tax, 2022 Tax Table row $50,600–$50,650, Single | $6,755 |
| Additional tax paid 12/03/2024 ($6,755 − $5,732) | $1,023 |

### The new information

- 2022 Form 5498 shows a **$6,000** traditional IRA contribution for 2022. It was never deducted.
- Agent asked: was Marcus covered by a workplace retirement plan in 2022? No (W-2 box 13 "Retirement plan" not checked). Age at end of 2022: 38.
- 2022 IRA Deduction Worksheet (2022 Instructions for Form 1040, Schedule 1 line 20): not covered by a plan, under 50 → deduction limit $6,000. Deduction: **$6,000** on 2022 Schedule 1, line 20.

## Step 1 — Should this be an amendment?

Yes. A missed adjustment changes AGI and tax (row 13 of [`../references/when-not-to-amend.md`](../references/when-not-to-amend.md)). The CP2000 case is closed and this change is unrelated to it, so it is a stand-alone Form 1040-X, not a CP2000 response.

## Step 2 — Deadline and lookback check

| Test | Date / amount | Source |
|---|---|---|
| 2022 due date | April 18, 2023 | 2022 Instructions for Form 1040 (Emancipation Day) |
| Deemed filing date | April 18, 2023 (filed early on 02/27/2023) | IRC §6513(a) |
| 3-year window | ended April 18, 2026: **closed** | IRC §6511(a) |
| Latest tax payment | $1,023 on December 3, 2024 | IRS account transcript / bank record |
| 2-year window | ends December 3, 2026: **open** if filed by then | IRC §6511(a) |
| Planned filing date | October 20, 2026 | |
| Lookback (2 years before filing) | October 20, 2024 – October 20, 2026 | IRC §6511(b)(2)(B) |
| Tax paid inside lookback | $1,023 (withholding is deemed paid in April 2023, outside it) | IRC §6513(b)(1) |
| **Maximum refundable** | **$1,023** | IRC §6511(b)(2)(B) |

The interest Marcus paid with the CP2000 balance is not tax and is not part of the cap computation; any interest the IRS owes him on an allowed refund is figured by the IRS.

## Step 3 — Corrected 2022 figures

- AGI: $63,580 − $6,000 = **$57,580**
- Taxable income: $57,580 − $12,950 = **$44,630**
- Tax: 2022 Tax Table row $44,600–$44,650, Single = **$5,435**

## The completed Form 1040-X draft

```markdown
# Form 1040-X — DRAFT amending tax year 2022
Form revision used: Form 1040-X (Rev. December 2025)

## Header
Tax year amended: 2022
Name / SSN: Marcus Lindqvist / XXX-XX-XXXX
Current address: <current address>
Presidential Election Campaign: no change
Amended return filing status: Single (original: Single)

## Lines 1–23
| Line | Description | A (as adjusted by CP2000) | B | C |
|---|---|---:|---:|---:|
| 1 | Adjusted gross income | 63,580 | (6,000) | 57,580 |
| 2 | Standard deduction | 12,950 | 0 | 12,950 |
| 3 | Line 1 − line 2 | 50,630 | (6,000) | 44,630 |
| 4a | QBI deduction | 0 | 0 | 0 |
| 4b | Schedule 1-A deductions (not available for 2022) | 0 | 0 | 0 |
| 5 | Taxable income | 50,630 | (6,000) | 44,630 |
| 6 | Tax (method: Table) | 6,755 | (1,320) | 5,435 |
| 7 | Nonrefundable credits | 0 | 0 | 0 |
| 8 | Line 6 − line 7 | 6,755 | (1,320) | 5,435 |
| 9 | Reserved | — | — | — |
| 10 | Other taxes | 0 | 0 | 0 |
| 11 | Total tax | 6,755 | (1,320) | 5,435 |
| 12 | Withholding | 6,102 | 0 | 6,102 |
| 13 | Estimated tax payments | 0 | 0 | 0 |
| 14 | Earned income credit | 0 | 0 | 0 |
| 15 | Refundable credits | 0 | 0 | 0 |
| 16 | Tax paid after return was filed (CP2000, excluding interest) | | | 1,023 |
| 17 | Total payments | | | 7,125 |
| 18 | Overpayment on original | | | 370 |
| 19 | Line 17 − line 18 | | | 6,755 |
| 20 | Amount you owe | | | 0 |
| 21 | Overpayment on this return (computed) | | | 1,320 |
| 22 | Refunded to you | | | 1,023 (see Part II; CPA to confirm presentation) |
| 23 | Applied to estimated tax | | | 0 |

## Part I — Dependents
No change.

## Part II — Explanation of changes
I made a $6,000 contribution to a traditional IRA for 2022 (Form 5498 attached) and
did not deduct it. I was not covered by an employer retirement plan in 2022, so the
full $6,000 is deductible on Schedule 1, line 20 (IRA deduction $6,000). Column A
reflects the IRS adjustment under CP2000 that added $4,650 of income; I paid the
resulting $1,023 of tax on 12/03/2024 (line 16, interest excluded). Corrected AGI is
$57,580, taxable income $44,630, and tax $5,435 from the 2022 Tax Table. The computed
overpayment is $1,320. Because this claim is filed more than 3 years after the return
was filed, under IRC §6511(b)(2)(B) the refund is limited to tax paid within the
2 years before this claim, $1,023; I request a refund of $1,023.

## Statute check
- Original filed 02/27/2023 → deemed filed 04/18/2023
- 3-year window ended 04/18/2026 (closed) | 2-year window from 12/03/2024 payment
  ends 12/03/2026 (open)
- Tax paid within lookback: $1,023 → maximum refundable $1,023
- Result: timely under the 2-year rule; refund capped at $1,023; $297 barred

## Attachments
- Completed, updated 2022 Form 1040 reflecting the CP2000 income and the IRA
  deduction, placed behind the 1040-X
- 2022 Schedule 1 (line 20 IRA deduction $6,000)
- Copy of 2022 Form 5498 (supporting statement, attached last)

## Filing channel
Paper. In 2026, e-file covers only the current and two prior tax periods (2025,
2024, 2023), so a 2022 amendment must be mailed. Ohio resident, not responding to a
notice → Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0052.
Send by certified mail or an IRS-designated private delivery service and keep the
receipt; the mailing date must be on or before 12/03/2026.

## Validation summary
- Math: all checks passed (C = A + B on every line; line 19 = 7,125 − 370 = 6,755;
  line 21 = 6,755 − 5,435 = 1,320)
- Sanity: column A uses CP2000-adjusted amounts; line 16 excludes CP2000 interest;
  2022 tax table and 2022 IRA limit used
- Statute: timely only under the 2-year rule; refund limited to $1,023
- Next steps: CPA review of the capped presentation; Ohio amended return check with
  the Ohio Department of Taxation; Where's My Amended Return about 3 weeks after
  mailing

## Sources cited in this draft
- Form 1040-X (Rev. December 2025) and Instructions (Rev. December 2025): column A
  "as previously adjusted", line 16, line 18, Where To File (Ogden address for Ohio)
- 2022 Instructions for Form 1040: due date April 18, 2023; standard deduction
  $12,950; Tax Table; IRA Deduction Worksheet ($6,000 under age 50)
- IRC §6511(a), §6511(b)(2)(B), §6513(a), §6513(b)(1)
- irs.gov Amended return FAQs (e-file limited to current and two prior periods)
```

## Why each non-obvious choice

**Why is column A not the original return?** The CP2000 changed the return. Column A must show the amounts "as previously adjusted", so the IRA deduction is measured from the CP2000-adjusted figures.

**Why does line 16 show $1,023 and not what Marcus actually paid?** Marcus paid tax plus interest. Line 16 includes additional tax paid after filing but excludes interest and penalties.

**Why only $1,023 when the computed overpayment is $1,320?** The 3-year window closed in April 2026. The claim survives only under the 2-year rule, and §6511(b)(2)(B) limits the refund to tax paid in the 2 years before the claim. His withholding counts as paid in April 2023 (§6513(b)(1)), far outside that period. The $297 difference cannot be refunded or credited.

**Why not wait and file in December?** The 2-year window closes December 3, 2026. Any delay risks losing the entire claim; the agent tells Marcus to mail it now with proof of mailing.

**What would have happened if Marcus had found the IRA deduction in February 2026?** A claim filed then would have been inside the 3-year window, the 3-year lookback (February 2023 to February 2026) would have included the withholding deemed paid in April 2023, and the full $1,320 would have been refundable. Claims filed in the last days before the 3-year deadline need the exact deemed-payment date checked against the lookback start; route those to a CPA.
