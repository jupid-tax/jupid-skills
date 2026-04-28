# Form 8889 Line-by-Line Reference

Complete lookup for every line on Form 8889. Use this when the agent needs to confirm what a line means or how it computes.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | HSA owner's legal name (the filer) | Each spouse with their own HSA files a separate 8889 |
| SSN | Filer's SSN | Spouse's HSA uses spouse's SSN on a separate 8889 |

---

## Part I — HSA Contributions

### Line 1 — Coverage type

Check **Self-only** or **Family**. The box reflects HDHP coverage on the **first day of the last month** of the tax year (December 1). If coverage type changed mid-year, the contribution-limit math on Line 3 follows the Limitation Chart and Worksheet — Line 1 still records December 1 status.

If the user had no HDHP coverage on December 1 but had earlier in the year, they cannot use the last-month rule and must prorate Line 3 by months of eligibility.

### Line 2 — HSA contributions you made

Direct contributions to the HSA, **outside payroll**:

| Belongs on Line 2 | Belongs elsewhere |
|-------------------|-------------------|
| Personal bank transfers to HSA custodian | Cafeteria-plan contributions (Section 125) → Line 9 |
| Checks written to the HSA | Employer-only contributions → Line 9 |
| Contributions by a family member on the user's behalf | Rollovers from another HSA → not reported as contribution |
| Post-tax payroll deductions routed by the user | IRA-to-HSA funding distribution → Line 10 |

**Contributions made between Jan 1 and Apr 15 of the next year**: ASK the user whether they designated the contribution for the prior or current year. The custodian usually defaults to current year unless the user specifies on the deposit slip. Once 1099-SA / 5498-SA is issued, the designation is locked.

### Line 3 — Contribution limit

The annual contribution limit, computed by month-by-month allowance:

**If eligible all 12 months with same coverage type:**
- Self-only: $4,300 (2025) → 2026 TBD, verify Rev. Proc.
- Family: $8,550 (2025) → 2026 TBD, verify Rev. Proc.

**If eligibility or coverage changed mid-year:**

For each month, take the coverage on the first day of that month. Sum the monthly allowances:

```
Monthly allowance (self-only) = annual self-only limit / 12
Monthly allowance (family)    = annual family limit / 12
Monthly allowance (none)      = $0
```

**Last-month rule (IRC §223(b)(8))**: if eligible on December 1, may contribute the full annual amount even if not eligible earlier. Triggers a 12-month testing period in the next calendar year — Part III applies if eligibility breaks during testing.

Limitation Chart and Worksheet is in the Form 8889 Instructions.

### Line 4 — Archer MSA contributions

Contributions to a separate Archer Medical Savings Account. The Archer MSA program is closed to new enrollees. For most filers, **$0**.

### Line 5

`Line 5 = Line 3 − Line 4`. Computed.

### Line 6 — Allocation

Default: `Line 6 = Line 5`. For MFJ couples where both spouses are covered under one **family** HDHP, the family contribution limit is **shared between the spouses by agreement**. The split is documented on each spouse's Line 6. Common splits: 100/0, 50/50, or anything else they agree on. The total of both spouses' Line 6 cannot exceed the family limit (Line 5).

### Line 7 — Catch-up contribution

$1,000 if the user is age 55 or older by the end of the tax year **and** HSA-eligible. Statutory amount, not adjusted for inflation (IRC §223(b)(3)).

Each spouse age 55+ gets their own $1,000 catch-up, but it must go into **their own** HSA, not the spouse's. A spouse without their own HSA cannot make a catch-up contribution.

### Line 8

`Line 8 = Line 6 + Line 7`. The full annual contribution limit including catch-up.

### Line 9 — Employer contributions

Comes from **W-2 Box 12, code W**. Includes:

- Direct employer contributions to the HSA
- Cafeteria-plan (Section 125) contributions — technically employer contributions in tax terms, even though funded by employee salary deferral

These amounts are **already excluded from Box 1 wages**. The user cannot deduct them again on Line 13 — this is a frequent error.

### Line 10 — Qualified HSA funding distribution

A one-time, lifetime tax-free transfer from an IRA (Traditional or Roth) to an HSA, capped at the user's annual HSA contribution limit (Line 8). Authority: IRC §408(d)(9).

The transfer counts against the annual HSA limit — useful only if the user can't otherwise afford the contribution and wants to fund it from IRA assets.

**Testing period**: 12 months. If HSA eligibility lapses during the 12 months following the funding distribution, the transfer becomes taxable plus a 10% additional tax.

Niche. Most filers leave at $0.

### Line 11

`Line 11 = Line 9 + Line 10`. Computed.

### Line 12

`Line 12 = Line 2 + Line 11`, capped at Line 8. Computed. Represents total contributions counted against the limit.

### Line 13 — HSA deduction

`Line 13 = min(Line 2, Line 8 − Line 11)`. The deductible portion of direct contributions.

**Flows to Schedule 1, Line 13** — above-the-line, no itemizing required. Reduces AGI dollar-for-dollar.

If `Line 2 + Line 9 > Line 8`, the user has an **excess contribution**. Withdraw the excess plus earnings by the unextended tax-filing deadline (with extensions) or pay a **6% excise tax every year** the excess remains. Form 5329 Part VII.

---

## Part II — HSA Distributions

### Line 14a — Total distributions

From **Form 1099-SA, Box 1**. The custodian sends 1099-SA in late January.

Every dollar on Box 1 must appear on Line 14a. Underreporting triggers a CP2000 notice within 12–18 months of filing.

### Line 14b — Excess returns and rollovers

| Belongs on Line 14b | Notes |
|---------------------|-------|
| Excess contributions withdrawn before filing deadline | Plus the earnings on those excess amounts |
| HSA-to-HSA rollovers | One allowed per 12-month period |
| Mistaken distributions returned to the HSA | Within deadlines specified by the custodian |

### Line 14c

`Line 14c = Line 14a − Line 14b`. Net distribution to evaluate for taxability.

### Line 15 — Qualified medical expenses paid from HSA

The portion of Line 14c used for **qualified medical expenses** under IRC §213(d) and Pub 502. See [`qualified-medical-expenses.md`](./qualified-medical-expenses.md) for the full list.

Receipts are not attached to the return but must be kept. The IRS can request documentation up to 3 years (longer for substantial omissions) after filing — and forever for purposes of the open-ended reimbursement window.

`Line 15` cannot exceed `Line 14c`. If the user paid more in qualified medical expenses than they distributed from the HSA, the excess is irrelevant for Form 8889 (and may be deductible on Schedule A if it exceeds the 7.5% AGI floor, but that's separate).

### Line 16 — Taxable HSA distributions

`Line 16 = Line 14c − Line 15`. The portion of the distribution that did **not** go to qualified medical expenses.

**Flows to Schedule 1, Line 8f** (Other income — Income from Form 8889). Taxed at the user's ordinary rate.

### Line 17a — Exception

Check if **any** of these applies to the Line 16 amount:

- Distribution made **after the account holder's death** (paid to a beneficiary)
- Account holder became **disabled** per IRC §72(m)(7)
- Account holder reached **age 65** before the distribution

If 17a is checked, the 20% additional tax does NOT apply. The Line 16 amount is still taxable as ordinary income, just without the penalty.

### Line 17b — Additional 20% tax

`Line 17b = Line 16 × 20%`, unless 17a exception applies (then $0).

**Flows to Schedule 2, Line 17c** (Additional tax on HSA distributions).

---

## Part III — Income and Additional Tax for Failure to Maintain HDHP Coverage

Only complete Part III if BOTH:

1. The user used the **last-month rule** in a prior tax year to make a full annual contribution
2. The user **failed to remain HSA-eligible** for the full 12-month testing period in the year after

If both apply, the prior-year over-contribution becomes taxable income this year, plus a 10% additional tax.

### Line 18 — Total contributions

The amount the user contributed under the last-month rule that they would NOT have been allowed to contribute under proration. Calculated as:

```
Line 18 = (full annual limit − prorated limit based on actual eligible months in prior year)
```

### Line 19 — Months of failure

Months in the testing period during which the user was not HSA-eligible.

### Line 20 — Taxable amount

`Line 20 = Line 18`. Reported as taxable income on **Schedule 1, Line 8f**.

### Line 21 — Additional 10% tax

`Line 21 = Line 20 × 10%`. **Flows to Schedule 2, Line 17c.**

This is **separate** from the Part II 20% additional tax. Both can apply in the same year if the user also took non-qualified distributions.

---

## Common cross-form flows

| Form 8889 line | Where it lands |
|----------------|----------------|
| Line 13 (deduction) | Schedule 1, Line 13 |
| Line 16 (taxable distribution) | Schedule 1, Line 8f |
| Line 17b (20% additional tax) | Schedule 2, Line 17c |
| Line 20 (Part III taxable amount) | Schedule 1, Line 8f |
| Line 21 (10% additional tax) | Schedule 2, Line 17c |

If the same Schedule 1 / Schedule 2 line has multiple sources, sum them on the destination line.

---

## Edge cases

### MFJ with two HSAs

Each spouse files **a separate Form 8889** with their own SSN. The family contribution limit (if both covered under one family HDHP) is allocated between them by agreement. Catch-up contributions go into each spouse's own HSA. Distributions are reported on the spouse who owns the account.

### HSA holder dies during the year

Distributions to a non-spouse beneficiary: account ceases to be an HSA, fair market value becomes taxable to the beneficiary.
Distributions to a spouse beneficiary: HSA continues as the spouse's HSA, no immediate tax.
Final-year Form 8889 for the deceased: the executor files reporting any contributions and distributions through date of death.

### Mid-year switch from self-only to family or vice versa

Use the Limitation Chart and Worksheet from the instructions. For each month, count the coverage on the first day. The Greater Coverage Rule: if you had family coverage even one month, you may use the family limit for the year via the last-month rule (subject to testing period).

### HSA holder enrolls in Medicare mid-year

Last eligible month = month before Medicare enrollment. Prorate Line 3 accordingly. Note Medicare Part A retroactive enrollment up to 6 months when claiming Social Security after 65 — this can retroactively disqualify HSA contributions made during those months and create excess contributions.

### Both spouses have their own HSA and family HDHP

Each must split the family limit by agreement on their respective Line 6. Each can add their own $1,000 catch-up to their own HSA on their own Line 7.
