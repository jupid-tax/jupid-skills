# HSA Eligibility Reference

To be HSA-eligible for a given month, **all four** conditions must be true on the **first day** of that month. If any condition fails, the user is ineligible for that month — no contribution allowed for that month (with the limited exception of the last-month rule).

Authority: IRC §223(c).

---

## The four conditions

### 1. Enrolled in a qualifying HDHP

The plan must meet IRS minimum deductible and maximum out-of-pocket thresholds (which change yearly). For 2025:

| Coverage | Minimum deductible | Maximum out-of-pocket |
|----------|--------------------|-----------------------|
| Self-only | $1,650 | $8,300 |
| Family | $3,300 | $16,600 |

For 2026: TBD. Verify the current Revenue Procedure (typically published May–June).

The HDHP must:
- Have a deductible at or above the minimum
- Have an out-of-pocket maximum at or below the maximum
- Generally not pay any benefits before the deductible is met (with exceptions for preventive care and certain telehealth services per current IRS guidance)

If the user has an HDHP through one employer and a non-HDHP plan through another (e.g., spouse's employer), the non-HDHP coverage may disqualify them — see condition 2.

### 2. No other disqualifying health coverage

Disqualifying:

- Spouse's family-coverage HMO/PPO that also covers the user
- General-purpose Flexible Spending Account (FSA) on the user OR the user's spouse — both disqualify
- General-purpose Health Reimbursement Arrangement (HRA)
- TRICARE
- A second non-HDHP plan covering the user (e.g., parent's plan, second-employer plan)
- VA medical benefits received in the past 3 months (limited exception for service-connected disabilities)

Not disqualifying:

- Coverage limited to dental, vision, accident, disability, long-term care
- Limited-purpose FSAs (dental and vision only)
- Post-deductible HRAs (HRA pays only after HDHP deductible is met)
- Suspended HRAs
- Wellness EAPs
- Discount cards
- Workers' compensation, automobile, property and liability insurance for medical care

**Common trap**: If the user's spouse has a general-purpose FSA at their employer that is "available" to the user (typical default), the user is disqualified. The fix is for the spouse to elect a limited-purpose FSA or none. Spouses who carry a general-purpose FSA must watch out — many people don't realize the spouse's FSA disqualifies the HSA-account-holder spouse.

### 3. Not enrolled in Medicare

Any part of Medicare (A, B, C, or D) disqualifies HSA contributions starting the month of enrollment.

**Distributions are still allowed**: an existing HSA can pay qualified medical expenses including Medicare premiums (A, B, D — but NOT Medigap) tax-free. Only contributions are blocked.

**Medicare Part A retroactive enrollment**: when a person claims Social Security retirement benefits after age 65, Medicare Part A enrollment is **automatic and retroactive up to 6 months** (or back to the 65th birthday, whichever is later). This can retroactively disqualify HSA contributions that the person made during those months — creating excess contributions. The user must withdraw the excess plus earnings or pay 6% excise tax annually.

**Strategy**: someone planning to delay Social Security past 65 can continue HSA contributions until the month they enroll in Medicare. Once they take Social Security, Part A retroactivity kicks in, so they should plan to stop HSA contributions 6 months before the Social Security claim.

### 4. Not claimed as a dependent

If the user can be claimed as a dependent on someone else's tax return — even if the other person doesn't actually claim them — the user is HSA-ineligible. This commonly affects:

- Adult children on a parent's HDHP who are still tax dependents
- Adult children on a parent's HDHP who are NOT tax dependents (e.g., 24-year-old earning enough not to be a dependent) — this category IS eligible

The plan-coverage definition of "dependent" (which extends to age 26 under ACA) is different from the IRS tax-dependent definition (gross-income and support tests). A 22-year-old on a parent's HDHP who earns $30K and supports themselves is **plan-covered** but **not a tax dependent** — they can open and contribute to their own HSA.

---

## Eligibility table for the agent

When the user describes coverage, build this table and verify each cell before computing Line 3.

| Month | HDHP coverage | Disqualifying coverage | Medicare | Tax dependent | HSA-eligible? |
|-------|---------------|------------------------|----------|---------------|---------------|
| Jan | self-only / family / none | yes / no | yes / no | yes / no | computed |
| Feb | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| Dec | ... | ... | ... | ... | ... |

Eligible? = (HDHP coverage ≠ none) AND (No disqualifying coverage) AND (No Medicare) AND (Not a tax dependent).

Use the table to compute Line 3 (full annual or prorated). The agent should ASK each line if not specified — do not default to "eligible all 12 months".

---

## What HDHP coverage does NOT mean

Common misconceptions:

- **"My deductible is high so it's an HDHP"** — wrong. The plan must explicitly meet the IRS HDHP minimums. Many high-deductible plans on Healthcare.gov are NOT HSA-eligible because they pay benefits before the deductible (e.g., $30 office visit copay before deductible).
- **"My plan documents say HDHP"** — usually correct, but verify the deductible and OOP max against the current year's IRS thresholds.
- **"Bronze plan = HDHP"** — not necessarily. Many bronze plans have copays before the deductible, which disqualifies HSA-eligibility.

The plan's Summary of Benefits and Coverage (SBC) should explicitly state "HSA-qualified" or "HDHP" if it qualifies. When in doubt, the user should call the insurer's member services line.

---

## When eligibility breaks mid-year

### Loss of HDHP coverage

Job loss, plan change, or aging out: contributions stop the month coverage ends. Distributions for qualified medical expenses can continue indefinitely from the existing balance.

### Acquisition of disqualifying coverage

Spouse signs up for a general-purpose FSA: user becomes ineligible the month the FSA becomes effective.

### Medicare enrollment

Contributions stop the month of enrollment (or earlier if Part A retroactive).

### Becomes a tax dependent

Rare (most filers don't move from independent to dependent), but can happen with major income changes or moving back in with parents. Eligibility ends the year they become a dependent.

In all of the above, the contribution limit on Line 3 is **prorated** by months of eligibility — unless the user invokes the last-month rule (eligible on December 1 → full annual allowed, with 12-month testing period to follow).
