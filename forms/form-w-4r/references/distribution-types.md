# Distribution types — ERD vs. nonperiodic vs. periodic vs. no-form scenarios

The biggest classification call when filling Form W-4R is determining what kind of distribution is being made. The classification drives the form choice (W-4R vs. W-4P vs. no form at all) and the default withholding rate. Misclassification is the most common reason recipients end up with under-withholding or, conversely, blocked distributions.

This reference walks the classifications in detail.

---

## Three categories under IRC §3405

### Category 1 — Periodic payments → Form W-4P

Authority: IRC §3405(a).

Definition: Designated distributions that are an annuity or similar periodic payment, paid in installments at regular intervals over a period of more than one year.

Examples:

- Monthly pension benefit from a defined benefit plan (lifetime annuity)
- 10-year, 20-year, life-with-period-certain annuity from a 403(b)
- Monthly distribution from a qualified retirement plan paid as a defined annuity option
- 10-year scheduled installments from an inherited IRA

**Form**: W-4P (NOT W-4R). W-4P is structurally similar to Form W-4 (wages) — uses tables and dependents to set withholding.

### Category 2 — Eligible Rollover Distributions (ERDs) → Form W-4R, 20% mandatory

Authority: IRC §3405(c) and §402(c).

Definition: A distribution from a qualified plan, 403(b), or 457(b) governmental plan that:

1. Is paid to the participant (not directly rolled over), AND
2. Is eligible to be rolled over to an IRA or another qualified plan

Most lump-sum distributions from employer plans are ERDs.

**Form**: W-4R; minimum withholding 20%.

Examples:

- 401(k) lump sum to participant after they leave the company
- 401(k) partial cash-out to participant
- Profit-sharing plan distribution to participant
- 403(b) lump sum to participant
- 457(b) governmental plan lump sum to participant (NOTE: 457(f) plans and non-governmental 457(b) plans have different rules — see Pub. 575)

### Category 3 — Other Nonperiodic → Form W-4R, 10% default

Authority: IRC §3405(b).

Definition: Distributions that are nonperiodic but NOT ERDs.

Examples:

- Traditional IRA cash withdrawal
- SEP-IRA cash withdrawal
- SIMPLE IRA cash withdrawal (after the 2-year holding period; before that, special rules apply)
- 401(k) hardship withdrawal (excluded from ERD definition)
- Required minimum distribution (RMD) (excluded from ERD definition)
- 401(k) corrective distribution (excess deferrals returned)
- Severance from employer when treated as nonperiodic (not as wages)
- Lump-sum from a non-qualified deferred compensation plan (in some cases)
- Non-spouse beneficiary distribution from a retirement account (generally)

**Form**: W-4R; default withholding 10% (can be 0–100%).

---

## "No form needed" scenarios

Some distributions don't require any withholding form:

### Direct trustee-to-trustee rollover

The funds move directly from one qualified plan / IRA / 403(b) / 457(b) to another. The participant never has constructive receipt. No withholding applies because there's no taxable distribution to the participant.

The transferring trustee codes Form 1099-R with **Distribution Code G** (direct rollover). Federal withholding on the 1099-R: $0.

The recipient signs a rollover request form with the transferring custodian (e.g., "direct rollover to receiving IRA at Fidelity"). No W-4R, no W-4P.

### Roth qualified distribution

A "qualified" Roth distribution requires:

1. The Roth account has been open for at least 5 years (counted from January 1 of the year the first contribution was made), AND
2. Distribution occurs after age 59½, after death, after disability (under §72(m)(7)), or for first-home purchase (up to $10,000 lifetime)

If both conditions are met, the entire distribution is **not taxable** — no withholding applies. W-4R is not needed.

(Roth distributions that are NOT qualified — e.g., earnings withdrawal before age 59½ — have a taxable component (the earnings, after basis is recovered). The taxable component is subject to default 10% withholding under §3405(b); W-4R is needed for the taxable portion.)

### IRA-to-IRA transfer (not a "rollover")

If the participant transfers funds from one IRA custodian to another IRA custodian (e.g., move from Fidelity Traditional IRA to Schwab Traditional IRA), this is a **trustee-to-trustee transfer**, not a "rollover" in the IRS sense. No 1099-R is issued. No W-4R needed. The funds simply move between custodians.

### Wages (use Form W-4)

If the payment is wages from an employer (regular salary, bonus, commission, severance treated as wages), the form is **W-4** (the wage withholding form), not W-4R. Most severance is treated as wages by the employer.

---

## Classification edge cases

### Severance: wages or nonperiodic?

Severance can be either, depending on the substance:

**Wages (W-4 applies)**:
- Tied to past services rendered
- Subject to FICA / FUTA in addition to income tax
- Paid through payroll
- Reported on Form W-2

**Nonperiodic distribution (W-4R applies)**:
- Lump sum after separation, distinct from regular pay
- Not subject to FICA / FUTA in some cases (rare; usually FICA still applies)
- Paid as a one-time check, not through regular payroll
- Reported on Form 1099-R or Form W-2 depending on employer treatment

**Most employers treat severance as wages.** This is the default and usually the right answer. The recipient should ask HR which form applies before electing.

### 401(k) lump sum vs. IRA cash withdrawal

Both are common; the rules differ:

| Aspect | 401(k) lump sum to participant | IRA cash withdrawal |
|--------|--------------------------------|---------------------|
| Type | Eligible rollover distribution | Other nonperiodic |
| Withholding | 20% mandatory minimum | 10% default; 0% allowed |
| Rollover within 60 days | Allowed (but loses the 20% withheld unless made whole) | Allowed (one rollover per 12 months across all IRAs) |
| Form 1099-R distribution code | Code 1 (early), 2 (early w/exception), or 7 (normal) | Code 1, 2, or 7 |
| Direct rollover available | Yes (use Code G — bypass withholding) | Trustee-to-trustee transfer (not technically "rollover" — no 1099-R) |

The big difference: 401(k) lump sums to participant trigger the 20% mandatory withholding. IRA withdrawals do not — the recipient can opt out (0% withholding) and pay tax via Form 1040.

### Hardship withdrawal vs. regular withdrawal from 401(k)

- **Hardship withdrawal**: NOT an ERD (IRC §402(c)(4)(C)). 10% default withholding under §3405(b). Cannot be rolled over.
- **Regular post-separation 401(k) lump sum**: IS an ERD. 20% mandatory withholding. Rollable.

If the participant is still employed and takes a hardship, classification = nonperiodic. If the participant has separated and takes a lump sum, classification = ERD.

### RMD treatment

Required Minimum Distributions (RMDs) under IRC §401(a)(9) are explicitly excluded from ERD definition (§402(c)(4)(B)). RMDs are "other nonperiodic" — 10% default withholding under §3405(b).

For Traditional IRA RMDs, custodians typically apply 10% by default unless the participant elects otherwise via W-4R.

For a participant taking BOTH an RMD and a larger distribution from the same 401(k) plan in the same year, the RMD portion is "other nonperiodic" (10% default) and the excess over the RMD is the ERD portion (20% mandatory). The payor often blends the rates — the W-4R can specify a single rate that satisfies both.

### SEPP — substantially equal periodic payments under §72(t)(2)(A)(iv)

If the recipient is under 59½ and wants to avoid the 10% §72(t) penalty by taking SEPP — a series of substantially equal payments computed under one of the IRS-approved methods (RMD method, fixed amortization, fixed annuitization) — the payments are typically treated as **periodic** for withholding purposes (since they span more than one year). Form W-4P, not W-4R.

If the SEPP is structured as annual lump sums for, say, 5 years, classification depends on the arrangement and the payor's interpretation. Consult the payor.

### Inherited IRA / inherited 401(k) distributions

Distributions to a non-spouse beneficiary from an inherited IRA / 401(k) are generally **not ERDs** — they are nonperiodic.

Exception: Spousal beneficiary can elect to roll over the deceased spouse's qualified plan to their own IRA — this is treated as an ERD (20% mandatory unless direct rollover).

For inherited Traditional IRAs, a non-spouse beneficiary takes RMDs (under §401(a)(9)) — these are nonperiodic, 10% default.

---

## Decision tree summary

```
Is the distribution from a Roth account, qualified?
  → No taxable component. No W-4R / W-4P.

Is the distribution a direct trustee-to-trustee rollover (Code G)?
  → No withholding. No W-4R / W-4P.

Is the distribution wages (severance treated as wages)?
  → Form W-4 (regular wage withholding).

Is the distribution paid in periodic installments scheduled for more than one year?
  → Form W-4P. Periodic withholding.

Is the distribution a one-time / nonperiodic payment from a retirement account?
  → Is it an ERD (lump sum from qualified plan, 403(b), 457(b) governmental)?
      → Yes: Form W-4R, 20% mandatory minimum. Direct rollover available to bypass.
      → No (IRA withdrawal, hardship, RMD, etc.): Form W-4R, 10% default, 0–100% allowed.
```

---

## Verification checklist before signing W-4R

- [ ] Distribution type confirmed (ERD vs. other nonperiodic vs. periodic)
- [ ] If periodic: wrong form — switch to W-4P
- [ ] If direct rollover: no form needed — confirm with payor
- [ ] If Roth qualified: no form needed — confirm with custodian
- [ ] If ERD: rate ≥ 20%
- [ ] If other nonperiodic: rate 0–100
- [ ] Not under 59½ (if so, also factor §72(t) 10% penalty paid separately)
- [ ] State withholding handled separately (state form, not W-4R)
