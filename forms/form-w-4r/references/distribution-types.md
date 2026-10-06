# Distribution types — ERD vs. nonperiodic vs. periodic vs. no-form scenarios

The biggest classification call when filling Form W-4R is determining what kind of payment is being made. The classification drives the form choice (W-4R vs. W-4P vs. W-4 vs. no form at all) and the default withholding rate. Verified 2026-10-06 against the 2026 Form W-4R, Pub. 505 (2026) chapter 1, Pub. 575 (2025), Pub. 590-B (2025) and Pub. 15 (2026).

This reference walks the classifications in detail.

---

## What Form W-4R covers

Form W-4R is for "your nonperiodic payment or eligible rollover distribution from an employer retirement plan, annuity (including a commercial annuity), or individual retirement arrangement (IRA)" (2026 Form W-4R, Purpose of form). Withholding applies only to the taxable part of payments from an employer pension, annuity, profit-sharing or stock bonus plan, any other deferred compensation plan, a traditional IRA, or a commercial annuity (Pub. 575 (2025), "Withholding Tax and Estimated Tax"). It does **not** cover wages, and Pub. 505 (2026) says to use Form W-4 for military retirement pay and payments from certain nonqualified deferred compensation plans.

---

## Three categories under IRC §3405

### Category 1 — Periodic payments → Form W-4P

Authority: IRC §3405(a).

Definition (form text): "payments made in installments at regular intervals over a period of more than 1 year." Pub. 575 (2025): "amounts paid at regular intervals (such as weekly, monthly, or yearly) for a period of time greater than 1 year (such as for 15 years or for life)."

Examples:

- Monthly pension benefit from a defined benefit plan (lifetime annuity)
- 10-year, 20-year, or life-with-period-certain annuity payments from a plan or 403(b)
- Installment payments from a plan scheduled over more than one year

**Form**: W-4P (NOT W-4R). If no W-4P is given, tax is withheld as if Single with no adjustments in Steps 2–4 (Pub. 575 (2025)).

**IRA exception**: "Distributions from an IRA that are payable on demand are treated as nonperiodic payments" (2026 Form W-4R, page 2). Regular withdrawals from an IRA the owner can stop or change at will are W-4R payments.

### Category 2 — Eligible Rollover Distributions (ERDs) → Form W-4R, 20%

Authority: IRC §3405(c) and §402(c).

Definition (form text): "Distributions you receive from qualified retirement plans (for example, 401(k) plans and section 457(b) plans maintained by a governmental employer) or tax-sheltered annuities that are eligible to be rolled over to an IRA or qualified plan are subject to a 20% default rate of withholding on the taxable amount of the distribution."

Most lump-sum and partial cash-outs from employer plans paid to the participant are ERDs. IRA distributions are never ERDs for this purpose.

**Form**: W-4R; 20% default and floor. Give a W-4R only for more than 20%.

Examples:

- 401(k) lump sum paid to the participant after leaving the company
- 401(k) partial cash-out paid to the participant
- Profit-sharing, money purchase, or ESOP distribution paid in cash to the participant
- 403(b) lump sum paid to the participant
- Governmental 457(b) lump sum paid to the participant (non-governmental 457(b) and 457(f) plans have different rules — see Pub. 575 and Pub. 957)
- Surviving spouse's distribution from a deceased participant's plan, if eligible for rollover

No withholding is required on an ERD paid to the participant if it and earlier ERDs from the same plan that year total less than $200, or if it consists solely of employer securities plus $200 or less of cash; withholding doesn't apply to net unrealized appreciation in employer securities (Pub. 575 (2025), "Withholding requirements").

### Category 3 — Other Nonperiodic → Form W-4R, 10% default

Authority: IRC §3405(b).

Definition: payments that are not periodic and not ERDs.

Examples:

- Traditional, SEP, or SIMPLE IRA cash withdrawal (including IRA distributions payable on demand)
- Required minimum distribution (RMD) — not an ERD (form; §402(c)(4)(B))
- 401(k) or 403(b) hardship distribution — not an ERD (form; §402(c)(4)(C))
- Series of substantially equal payments over life or 10+ years — not an ERD (§402(c)(4)(A); Pub. 575 (2025)), and often periodic (W-4P) if from a plan
- Corrective distributions of excess contributions or excess deferrals — not ERDs (Pub. 575 (2025))
- Distributions from a pension-linked emergency savings account, eligible distributions to a domestic abuse victim, qualified disaster recovery distributions, qualified birth or adoption distributions, qualified long-term care distributions, emergency personal expense distributions — listed on the 2026 form as not ERDs for these withholding rules
- Nonperiodic payment from a commercial annuity
- Traditional IRA to Roth IRA conversion (reported as a traditional IRA distribution even when done trustee-to-trustee or with the same trustee; Instructions for Forms 1099-R and 5498, "Reporting Roth IRA conversions")

**Form**: W-4R; default 10% (can be 0–100%, generally not below 10% if delivered outside the U.S. and its territories).

---

## "No form needed" scenarios

### Direct rollover (plan → IRA or plan)

The plan pays the funds directly to another qualified plan or to a traditional or Roth IRA. "There is no withholding" (Pub. 575 (2025), Table 1; IRC §3405(c)(2)). The plan codes Form 1099-R with **code G**. A direct rollover of pre-tax money to a Roth IRA is still not subject to withholding, but the taxable amount is income (no 10% additional tax applies; Pub. 575 (2025), "Rollovers to Roth IRAs").

The recipient signs the plan's direct-rollover election. No W-4R, no W-4P.

### IRA-to-IRA trustee-to-trustee transfer

A transfer between IRA trustees is not a distribution or a rollover; it is not reported on Form 1099-R (Pub. 590-B (2025); Instructions for Forms 1099-R and 5498, "Transfers"). No W-4R.

### Roth distribution not includible in income

"There will be no withholding on any part of a distribution where it is reasonable to believe that it won't be includible in gross income" (Pub. 575 (2025)). A qualified Roth IRA distribution (5-year period met, counted from January 1 of the year of the first contribution, AND made after age 59½, after death, on account of disability, or for a first home up to $10,000; IRC §408A(d)(2)) is not taxable, so no withholding applies.

A nonqualified Roth distribution may have a taxable part (earnings, after contributions and conversions come out first under the ordering rules in Pub. 590-B). Ask the custodian how it withholds; any withholding applies to the taxable part only.

### Wages, including severance (use Form W-4)

"Severance payments are wages subject to social security and Medicare taxes, federal income tax withholding, and FUTA tax" (Pub. 15 (2026)). Severance pay is a supplemental wage (Pub. 15 (2026), section 7): the employer withholds at the 22% optional flat rate or by aggregating with regular wages (37% mandatory on supplemental wages over $1 million in the year). Form W-4R never applies. Redirect to [`../../form-w4/SKILL.md`](../../form-w4/SKILL.md).

Payments from certain nonqualified deferred compensation plans are also wage withholding (Form W-4), per Pub. 505 (2026), chapter 1.

### Nonresident aliens and foreign estates

"Do not use Form W-4R. See Pub. 515... and Pub. 519" (2026 Form W-4R, page 2). A U.S. citizen or resident who gives no U.S. or territory home address can't elect out of withholding; a payee who certifies non-U.S. status may be subject to 30% nonresident withholding unless a treaty reduces it (Pub. 575 (2025)).

---

## Classification edge cases

### 401(k) lump sum vs. IRA cash withdrawal

| Aspect | 401(k) lump sum to participant | IRA cash withdrawal |
|--------|--------------------------------|---------------------|
| Type | Eligible rollover distribution | Other nonperiodic |
| Withholding | 20% default and floor | 10% default; 0% allowed (U.S. address) |
| 60-day rollover | Allowed; replace the 20% withheld from other funds to roll over the full amount | Allowed; one IRA-to-IRA rollover per 12 months (Pub. 590-B) |
| Form 1099-R code | 1 (early, no known exception), 2 (early, exception), or 7 (normal) | 1, 2, or 7 |
| Moving money without withholding | Direct rollover (code G) | Trustee-to-trustee transfer (not reported) |

### Hardship withdrawal vs. regular withdrawal from 401(k)

- **Hardship distribution**: NOT an ERD (IRC §402(c)(4)(C); form list). 10% default under §3405(b). Cannot be rolled over. Hardship is not a §72(t) exception.
- **Post-separation 401(k) lump sum**: an ERD. 20% withholding unless directly rolled over.

### RMD treatment

RMDs under IRC §401(a)(9) are excluded from the ERD definition (§402(c)(4)(B); the form calls them "Distributions required by federal law"). They are other nonperiodic (10% default) unless paid as periodic installments (W-4P). IRA owners must begin RMDs by the required beginning date based on age 73 (Pub. 590-B (2025)).

If a participant takes an RMD and a larger distribution from the same plan in one year, the RMD part is not an ERD and the excess is. Ask the plan how it applies the W-4R rate to each part; a rate of 20% or more satisfies both.

### Substantially equal periodic payments (§72(t)(2)(A)(iv))

From an IRA payable on demand: nonperiodic (form rule) → W-4R. From an employer plan as scheduled installments over more than one year: periodic → W-4P. Either way, not an ERD. Confirm with the payer.

### Inherited IRA / inherited plan distributions

A surviving spouse can roll over a deceased spouse's plan distribution; it is an ERD if eligible for rollover. A non-spouse beneficiary can move plan money to an inherited IRA only by direct rollover; ask the plan how it withholds on amounts paid to a non-spouse beneficiary. Inherited IRA withdrawals (payable on demand) are other nonperiodic, 10% default.

---

## Decision tree summary

```
Is it wages, a bonus, or severance pay?
  → Form W-4 (wage withholding). Not W-4R.

Is the payee a nonresident alien or a foreign estate?
  → Not W-4R (Pub. 515 / Pub. 519).

Is it a direct rollover (plan → IRA/plan) or an IRA trustee-to-trustee transfer?
  → No withholding. No W-4R / W-4P.

Is it reasonable to believe none of it is taxable (e.g., qualified Roth distribution)?
  → No withholding. No W-4R.

Is it paid in installments at regular intervals over more than 1 year (and not an IRA payable on demand)?
  → Form W-4P. Periodic withholding.

Otherwise it is nonperiodic:
  → Is it an ERD (from a qualified plan, 403(b), or governmental 457(b), eligible for rollover,
     and not on the form's non-ERD list)?
      → Yes: Form W-4R, 20% default and floor; direct rollover avoids withholding.
      → No (IRA withdrawal, hardship, RMD, etc.): Form W-4R, 10% default, 0–100% allowed.
```

---

## Verification checklist before signing W-4R

- [ ] Payment type confirmed (ERD vs. other nonperiodic vs. periodic vs. wages)
- [ ] If periodic: wrong form — switch to W-4P
- [ ] If wages or severance: wrong form — Form W-4
- [ ] If direct rollover or transfer: no form needed — confirm with payer
- [ ] If Roth: confirm with custodian whether any part is taxable
- [ ] If ERD: rate ≥ 20%
- [ ] If other nonperiodic: rate 0–100 (10–100 if delivered outside the U.S.)
- [ ] Under 59½? Factor the §72(t) 10% additional tax (not in the default rates)
- [ ] State withholding handled separately (payer's state election)
