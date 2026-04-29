# IRC §6654 Safe Harbor Rules

The estimated-tax safe harbors under IRC §6654 determine whether a taxpayer owes an underpayment penalty. The agent applies the lower of the two harbors to compute the required annual payment.

This file describes the rules in operational detail. For penalty computation when underpayment has already occurred, use the `form-2210` skill — this file is for prospective planning only.

---

## The two safe harbors

A taxpayer avoids the §6654 penalty if total payments (withholding + timely estimates) for the year equal or exceed the **smaller** of:

### Safe Harbor A — 90% of current year (IRC §6654(d)(1)(B)(i))

`0.90 × current_year_total_tax`

The "total tax" is Form 1040 Line 24 minus refundable credits (per IRS Pub. 505 definition).

This harbor is intuitive but requires the taxpayer to project current-year tax accurately. For lumpy income (S-corp K-1 in Q4, capital gain in Q3, Roth conversion in Q1), the projection is hard.

### Safe Harbor B — 100% (or 110%) of prior year (IRC §6654(d)(1)(B)(ii))

```
safe_harbor_B = prior_year_tax × (1.10 if prior_AGI > 150,000 (or 75,000 MFS) else 1.00)
```

The 110% rule applies if prior-year AGI exceeds $150,000 (or $75,000 if MFS) — IRC §6654(d)(1)(C). This threshold is **not** inflation-adjusted; it has been static since the Taxpayer Relief Act of 1997.

This harbor is **certain** — the prior-year tax is a known number. The taxpayer cannot underpay if they pay 100% (or 110%) of last year, no matter what current-year income looks like. This is the planner's friend when income is lumpy.

**Edge cases**:
- Prior tax year was less than 12 months → Safe Harbor B is **not** available; only 90% current-year applies (per Pub. 505).
- Prior year had zero tax AND taxpayer was US citizen/resident for the full prior year AND the prior year was 12 months → no estimated tax required at all per §6654(e)(2).

---

## Required annual payment

`required_annual_payment = min(SafeHarbor_A, SafeHarbor_B)`

The taxpayer pays this much across four installments (or via withholding, which counts the same).

If withholding alone covers the required annual payment, the taxpayer is automatically safe-harbored — no estimated payments needed.

---

## De minimis exception (IRC §6654(e)(1))

If the **balance due at filing** would be less than $1,000 after subtracting withholding and refundable credits, no penalty applies regardless of safe-harbor compliance.

This exception is for filers whose income is mostly W-2 wages with adequate withholding plus a small amount of side income. It does NOT excuse a taxpayer who fails to make required estimates and ends up owing > $1,000.

---

## Withholding-as-paid-evenly rule (IRC §6654(g))

W-2 withholding is treated as paid evenly across the year, regardless of when it was actually withheld. This means:

- Late-year withholding "fixes" early-year underpayment retroactively
- A taxpayer who realizes in November they're under-withheld can ask their employer for additional Q4 withholding (Form W-4 Line 4(c) extra withholding) and the IRS treats the additional amount as if paid 25% in each prior quarter
- Estimated payments do **not** get the same treatment — they're applied to the quarter in which paid (with limited exceptions)

**Planning lever**: a taxpayer with both W-2 wages and 1099 income often prefers to fix shortfalls via increased W-2 withholding rather than estimated payments, because withholding is retroactively credited.

---

## The four installment due dates (IRC §6654(c))

| Installment | Period | Due date |
|-------------|--------|----------|
| 1 | Jan 1 – Mar 31 | April 15 |
| 2 | Apr 1 – May 31 | June 15 |
| 3 | Jun 1 – Aug 31 | September 15 |
| 4 | Sep 1 – Dec 31 | January 15 (next year) |

The "quarters" are unequal (3, 2, 3, 4 months). This is intentional under §6654(c).

When a due date falls on a weekend or DC/federal holiday, it shifts to the next business day per IRC §7503. The agent must verify the exact date each year — Patriot's Day (April 19 in MA/ME) and Emancipation Day (April 16 in DC) shift Tax Day occasionally.

---

## Per-installment requirement (IRC §6654(d)(1)(A))

The required annual payment is divided into **four equal installments** (25% each) by default. A taxpayer who underpays one installment can be assessed a penalty even if the year-end total is correct.

Example: required annual payment = $20,000.
- Q1 must have $5,000 cumulative paid by April 15
- Q2 must have $10,000 cumulative paid by June 15
- Q3 must have $15,000 cumulative paid by September 15
- Q4 must have $20,000 cumulative paid by January 15

A taxpayer who pays $0 in Q1, Q2, Q3 and then $20,000 in Q4 owes a penalty for the Q1, Q2, Q3 underpayments — even though the year-end total is correct.

**Withholding** counts toward each installment proportionally (per §6654(g)) — see above.

---

## Annualized income installment method (IRC §6654(d)(2))

If income is uneven across the year, the taxpayer can elect the annualized-income method on **Form 2210 Schedule AI** when filing. This method computes the required installment based on income actually earned through each cumulative period:

| Installment | Annualization period |
|-------------|---------------------|
| 1 | Jan 1 – Mar 31 (3 months) |
| 2 | Jan 1 – May 31 (5 months) |
| 3 | Jan 1 – Aug 31 (8 months) |
| 4 | Jan 1 – Dec 31 (12 months) |

For each period, compute annualized AGI = (period AGI) × (12 / period months). Apply the safe-harbor math, then back out the cumulative installment requirement.

This method is mechanical but cumbersome — Schedule AI has 30+ lines per quarter. It saves penalty when income is genuinely back-loaded (large Q4 bonus, single Roth conversion in Q3).

For prospective planning, the agent flags the annualized option if the user reports lumpy income — but doesn't compute Schedule AI itself (that's the `form-2210` skill at filing time).

---

## Special rule: farmers and fishers (IRC §6654(i))

If at least 2/3 of gross income is from farming or fishing in the current OR prior year, the taxpayer may either:

1. Pay one installment by **January 15** equal to the full required annual payment (66.67% of current-year tax — note: 66.67%, not 90% — is the safe harbor for farmers/fishers per §6654(i)(2)), OR
2. File the return and pay the entire balance by **March 1** of the following year — no estimates required.

This rule is narrow but critical for the few filers it applies to.

---

## Who is exempt from §6654 entirely

- Individuals with no tax liability for the prior year if (i) US citizen/resident for full prior year, (ii) prior year was 12 months, (iii) total prior-year tax = 0 — per §6654(e)(2)
- Individuals whose total tax minus withholding/credits is less than $1,000 — §6654(e)(1)
- Decedents during the year of death (estate computes its own §6654)
- Estates and trusts in their first 2 years (§6654(l))

---

## What this skill does NOT compute

This skill is **prospective**: it builds a payment schedule that satisfies the safe harbor.

This skill does NOT:
- Compute the actual underpayment penalty for an already-underpaid year (Form 2210)
- Annualize income across cumulative periods (Form 2210 Schedule AI)
- Handle estate/trust §6654 (Form 1041-ES)
- Handle nonresident alien rules (Form 1040-NR-ES)

For any of those, the agent must redirect to the appropriate form's skill or to a CPA.

---

## Summary algorithm

```
def required_annual_payment(prior_tax, prior_agi, filing_status, current_tax):
    if filing_status == "MFS":
        threshold = 75000
    else:
        threshold = 150000

    multiplier = 1.10 if prior_agi > threshold else 1.00
    safe_harbor_B = prior_tax * multiplier
    safe_harbor_A = 0.90 * current_tax
    return min(safe_harbor_A, safe_harbor_B)


def per_installment(required, withholding, method="equal"):
    net = required - withholding
    if net <= 1000:
        return 0  # de minimis
    if method == "equal":
        return [net / 4] * 4
    elif method == "annualized":
        # delegate to form-2210 skill / Schedule AI
        raise NotImplementedError("Use form-2210 Schedule AI")
```

The agent runs this with the user's numbers and surfaces every input for verification.
