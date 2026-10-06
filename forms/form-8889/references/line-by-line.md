# Form 8889 Line-by-Line Reference

Complete lookup for every line on Form 8889. Use this when the agent needs to confirm what a line means or how it computes.

Verified against the 2025 Form 8889 (created 3/28/25) and the 2025 Instructions for Form 8889 (Nov 25, 2025), filed in 2026. Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-8889.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | HSA owner's legal name (the filer) | Each spouse with their own HSA files a separate 8889 |
| SSN | Filer's SSN | Spouse's HSA uses spouse's SSN on a separate 8889 |

---

## Part I — HSA Contributions

### Line 1 — Coverage type

Check **Self-only** or **Family**. If the user was covered by a self-only HDHP and a family HDHP at different times, check the plan in effect for the longer period. If they were covered by both at the same time, or had family coverage on the first day of the last month of the tax year (December 1), check **Family**. Spouses covered by a family HDHP are treated as family whether they file jointly or separately (2025 Instructions for Form 8889, Line 1).

If the user had no HDHP coverage on December 1 but had earlier in the year, they cannot use the last-month rule and must use the Line 3 Limitation Chart and Worksheet.

### Line 2 — HSA contributions you made

Direct contributions to the HSA, **outside payroll**:

| Belongs on Line 2 | Belongs elsewhere |
|-------------------|-------------------|
| Personal bank transfers to HSA custodian | Cafeteria-plan contributions (Section 125) → Line 9 |
| Checks written to the HSA | Employer-only contributions → Line 9 |
| Contributions by a family member on the user's behalf | Rollovers from another HSA → not reported as contribution |
| After-tax payroll deductions sent to the HSA (not through a cafeteria plan) | IRA-to-HSA funding distribution → Line 10 |

**Contributions made between Jan 1 and Apr 15 of the next year**: ASK the user whether they designated the contribution for the prior or current year. Contributions for 2025 count on Line 2 if made by April 15, 2026, the unextended due date (later for combat-zone service, Pub. 3). The custodian usually defaults to current year unless the user specifies on the deposit slip; the 5498-SA box 3 shows what the custodian recorded as prior-year.

### Line 3 — Contribution limit

The annual contribution limit, computed by month-by-month allowance:

**If eligible all 12 months with same coverage type:**
- Self-only: $4,300 (2025, Rev. Proc. 2024-25); $4,400 (2026, Rev. Proc. 2025-19)
- Family: $8,550 (2025); $8,750 (2026)
- Add $1,000 if the user was 55+ at year-end and unmarried, or married with self-only coverage all year. Married with family coverage: the $1,000 goes on Line 7, not Line 3.

**If not eligible on December 1 (Line 3 Limitation Chart and Worksheet):**

For each month, take the coverage on the first day of that month (enter -0- for a Medicare month or a month not eligible). Total the 12 months and divide by 12:

```
2025 month, self-only = $4,300 ($5,300 if 55+ at year-end)
2025 month, family    = $8,550 ($9,550 if unmarried and 55+)
Not eligible / Medicare = $0
Line 3 = total of 12 months / 12
```

**Last-month rule (IRC §223(b)(8))**: if eligible on December 1, the user is treated as eligible all year with the December 1 coverage. If eligible all year (or treated so) but the coverage type changed, Line 3 = the greater of the worksheet result or the full amount for the December 1 coverage; family coverage on December 1 → enter the full family amount. Starts a testing period from December 1 through December 31 of the next year — Part III applies if eligibility breaks during testing.

### Line 4 — Archer MSA contributions

Contributions to a separate Archer Medical Savings Account. The Archer MSA program is closed to new enrollees. For most filers, **$0**.

### Line 5

`Line 5 = Line 3 − Line 4`. Computed.

### Line 6 — Allocation

Default: `Line 6 = Line 5`. For spouses who have separate HSAs and had family coverage at any time during the year, the family contribution limit is **split equally unless they agree on a different allocation** (such as allocating nothing to one spouse). The split is documented on each spouse's Line 6. If family coverage did not apply for every month, follow Steps 1–4 in the Line 6 instructions (split only the family-month portion). The total of both spouses' Line 6 cannot exceed the family limit (Line 5).

### Line 7 — Additional contribution amount

Only for a user who was age 55 or older at the end of the tax year, **married**, and the user or spouse had family HDHP coverage. Amount = $1,000 × months eligible (not enrolled in Medicare) ÷ 12; $1,000 if all 12 months (Additional Contribution Amount Worksheet). Statutory amount, not adjusted for inflation (IRC §223(b)(3)). Everyone else who is 55+ includes the $1,000 on Line 3 instead.

Each spouse age 55+ gets their own $1,000, but it must go into **their own** HSA, not the spouse's. A spouse without their own HSA cannot make an additional contribution.

### Line 8

`Line 8 = Line 6 + Line 7`. The full annual contribution limit including any additional contribution.

### Line 9 — Employer contributions

Comes from **W-2 Box 12, code W**. Includes:

- Direct employer contributions to the HSA
- Cafeteria-plan (Section 125) contributions — technically employer contributions in tax terms, even though funded by employee salary deferral

These amounts are **already excluded from Box 1 wages**. The user cannot deduct them again on Line 13 — this is a frequent error.

Use the Employer Contribution Worksheet when the 2025 W-2 code W includes contributions for 2024, or when the employer made 2025 contributions in 2026: Line 9 = code W − prior-year amounts + contributions for this year made next year.

### Line 10 — Qualified HSA funding distribution

A one-time, lifetime tax-free direct trustee-to-trustee transfer from a traditional or Roth IRA (not an ongoing SEP or SIMPLE IRA) to an HSA. The amount excluded is capped by the user's age and HDHP coverage at the time of the transfer. A second transfer is allowed in the same year only if the first was made under self-only coverage and the user later switches to family coverage. Authority: IRC §408(d)(9).

The transfer counts against the annual HSA limit and is not deductible.

**Testing period**: from the month of the transfer through the last day of the 12th month after it (example: June 17, 2025 transfer → testing period through June 30, 2026). If HSA eligibility lapses during it (other than death or disability), the transfer is included in income on Part III Line 19 plus a 10% additional tax.

Niche. Most filers leave at $0.

### Line 11

`Line 11 = Line 9 + Line 10`. Computed.

### Line 12

`Line 12 = Line 8 − Line 11`. If zero or less, enter -0-. Computed. Represents the room left in the limit after employer contributions and funding distributions.

### Line 13 — HSA deduction

`Line 13 = smaller of Line 2 or Line 12`. The deductible portion of direct contributions.

**Flows to Schedule 1, Line 13** — above-the-line, no itemizing required. Reduces AGI dollar-for-dollar. On a joint return with two Forms 8889, combine both Line 13 amounts on Schedule 1.

If `Line 2 > Line 13`, the difference is an **excess contribution**. Withdraw the excess plus earnings by the due date of the return, including extensions (report the earnings as other income for the year withdrawn), or pay a **6% excise tax every year** the excess remains. Form 5329 Part VII. If the return was filed on time without the withdrawal, the withdrawal can still be made within 6 months of the original due date (excluding extensions) with an amended return marked "Filed pursuant to section 301.9100-2".

---

## Part II — HSA Distributions

### Line 14a — Total distributions

From **Form 1099-SA, Box 1**. The custodian sends 1099-SA in late January.

Every dollar on Box 1 must appear on Line 14a. Underreporting triggers a CP2000 notice within 12–18 months of filing.

### Line 14b — Excess returns and rollovers

| Belongs on Line 14b | Notes |
|---------------------|-------|
| Excess contributions withdrawn by the due date of the return, including extensions | Plus the earnings on those excess amounts |
| HSA-to-HSA rollovers | Completed within 60 days; one rollover contribution per 1-year period |

Not on Line 14b: a mistaken distribution the user repaid. The custodian does not report it on Form 1099-SA (or corrects a filed one), so it is not in Line 14a either (Instructions for Forms 1099-SA and 5498-SA, "HSA Mistaken Distributions"). Direct trustee-to-trustee transfers are not distributions and are not entered at all.

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

Check if **any** of these applies to any part of the Line 16 amount (IRC §223(f)(4)(B)–(C)):

- Distribution made **after the account beneficiary's death**
- Distribution made after the account beneficiary became **disabled** per IRC §72(m)(7)
- Distribution made after the account beneficiary turned **age 65**

If 17a is checked, enter on Line 17b 20% of only the part of Line 16 that meets no exception. The excepted part is still taxable as ordinary income, just without the penalty.

### Line 17b — Additional 20% tax

`Line 17b = 20% × (Line 16 − the part covered by a 17a exception)`.

**Flows to Schedule 2, Line 17c** (Additional tax on HSA distributions).

---

## Part III — Income and Additional Tax for Failure to Maintain HDHP Coverage

Complete Part III if the user **failed to remain HSA-eligible** (other than because of death or disability) during the testing period for either:

1. The **last-month rule** used in a prior tax year (testing period December 1 through December 31 of the following year), or
2. A **qualified HSA funding distribution** (testing period from the month of the transfer through the last day of the 12th month after it)

The amount is included in income in the year eligibility fails, plus a 10% additional tax.

### Line 18 — Last-month rule

Use the Line 3 Limitation Chart and Worksheet for the year the contribution was made to find what the user could have contributed without the last-month rule. Line 18 = the amount actually contributed minus that redetermined amount (not less than 0):

```
Line 18 = contributions made for the prior year − worksheet limit for that year without the last-month rule
```

### Line 19 — Qualified HSA funding distribution

The total qualified HSA funding distribution (Line 10 of the year it was made) whose testing period failed.

### Line 20 — Total income

`Line 20 = Line 18 + Line 19`. Reported as income on **Schedule 1, Line 8f**.

### Line 21 — Additional 10% tax

`Line 21 = Line 20 × 10%`. **Flows to Schedule 2, Line 17d.**

This is **separate** from the Part II 20% additional tax. Both can apply in the same year if the user also took non-qualified distributions.

---

## Common cross-form flows

| Form 8889 line | Where it lands |
|----------------|----------------|
| Line 13 (deduction) | Schedule 1, Line 13 |
| Line 16 (taxable distribution) | Schedule 1, Line 8f |
| Line 17b (20% additional tax) | Schedule 2, Line 17c |
| Line 20 (Part III taxable amount) | Schedule 1, Line 8f |
| Line 21 (10% additional tax) | Schedule 2, Line 17d |

If the same Schedule 1 / Schedule 2 line has multiple sources, sum them on the destination line.

---

## Edge cases

### MFJ with two HSAs

Each spouse files **a separate Form 8889** with their own SSN. The family contribution limit (if either has family coverage) is split equally unless they agree otherwise. Additional ($1,000) contributions go into each spouse's own HSA. Distributions are reported on the spouse who owns the account.

### HSA holder dies during the year

Spouse is the designated beneficiary: the HSA is treated as the surviving spouse's HSA, no immediate tax.
Non-spouse beneficiary: the account stops being an HSA on the date of death. The beneficiary writes "Death of HSA account beneficiary" across the top of their own Form 8889, skips Part I, enters the fair market value at the date of death on Line 14a, and on Line 15 (if not the estate) the decedent's qualified medical expenses paid within 1 year after death. No 20% additional tax.
Estate is the beneficiary: the value at the date of death goes on the decedent's final return.

### Mid-year switch from self-only to family or vice versa

If the user was eligible all year (or treated as eligible under the last-month rule), Line 3 = the greater of the Limitation Chart and Worksheet result or the full amount for the coverage held on December 1. Family coverage on December 1 → full family amount (subject to the testing period if the user was not otherwise eligible all year). Family coverage earlier in the year but self-only on December 1 does **not** give the full family amount; the worksheet counts the family months only.

### HSA holder enrolls in Medicare mid-year

Last eligible month = month before Medicare enrollment. Enter -0- on the worksheet for each Medicare month. Premium-free Part A taken after 65 starts 6 months back from the sign-up or Social Security application, but not before the month the person turned 65 (medicare.gov, "When does Medicare coverage start?"); contributions for those retroactive months are excess contributions (Pub. 969 (2025), "Enrolled in Medicare").

### Both spouses have their own HSA and family HDHP

Each splits the family limit on their respective Line 6 (equally unless they agree otherwise). Each 55+ spouse can add their own $1,000 to their own HSA on their own Line 7.
