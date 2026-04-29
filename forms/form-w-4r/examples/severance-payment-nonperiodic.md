# Example — Laid-off employee receiving $30K severance; W-4R vs. W-4

## Scenario

**Filer**: Marcus Williams, age 38, recently laid off from BigCo Inc. as part of a workforce reduction

**Distribution**: $30,000 lump-sum severance payment from BigCo

**Purpose**: Marcus needs to set the right federal tax withholding on his severance. The classification of severance — wages or nonperiodic — drives whether he files Form W-4 (wages) or Form W-4R (nonperiodic). The answer depends on how BigCo's payroll department treats the payment.

**Key facts**:
- Marcus is 38; §72(t) early-withdrawal penalty doesn't apply (severance isn't a retirement distribution)
- Filing status: Single, no dependents
- 2026 income picture: 9 months of BigCo W-2 wages totaling $75,000 (already paid, with regular W-4 withholding) + $30,000 severance + minimal other income
- Marcus is actively job-hunting; expects new employment within 2-3 months

---

## Step 1 — Classify the severance

Severance can be either **wages** or **nonperiodic distribution**, depending on the substance of the payment. Marcus calls BigCo's HR to clarify:

**HR's answer**: "BigCo treats severance as wages. The payment will go through payroll, FICA / FUTA will be withheld, and we'll report it on your Form W-2. You should update your Form W-4 if you want to change federal withholding."

This is the most common treatment. Most US employers treat severance as wages because:

- The payment is tied (loosely) to past services rendered
- Payroll systems are set up to process wages, not nonperiodic distributions
- Reporting on W-2 is administratively simpler than 1099-R
- FICA / FUTA are due on severance regardless of treatment under most case law (even when employer tries to characterize as nonperiodic, the IRS often imposes FICA)

→ **Form W-4 applies, not W-4R.**

---

## Step 2 — When would severance be W-4R?

Severance is treated as a **nonperiodic distribution** (W-4R) only when:

1. The payment is from a **deferred compensation plan or supplemental retirement arrangement** (rare for ordinary severance)
2. The employer's plan document explicitly classifies severance as a nonperiodic retirement distribution (very rare)
3. The severance is paid from a **trust** rather than from general employer assets (rare)

For 99% of severance recipients, the answer is W-4 (wages), not W-4R.

If Marcus's situation matched the rare W-4R case (e.g., his severance was paid from a non-qualified deferred compensation plan that distributes a lump sum at separation), the analysis below would shift to W-4R mechanics.

---

## Step 3 — Compute withholding under each scenario

### Scenario A — Severance treated as wages (W-4 applies)

This is BigCo's actual treatment.

BigCo's payroll calculates federal withholding on the $30,000 using either:

**Aggregate method**: Adds the severance to Marcus's regular paycheck and computes withholding as if it were a single paycheck for the period. Often results in over-withholding because the IRS withholding tables assume the high amount continues for the rest of the year.

**Percentage method (supplemental wage method)**: Treats the severance as supplemental wages and applies a flat **22% federal withholding rate** under IRS Reg. §31.3402(g)-1 (for supplemental wages up to $1 million). Most employers use this method for severance.

If BigCo uses the percentage method:

- Severance: $30,000
- Federal withholding: $30,000 × 22% = $6,600
- FICA (Social Security 6.2% + Medicare 1.45%): $30,000 × 7.65% = $2,295
- Net to Marcus (federal + FICA): $30,000 − $6,600 − $2,295 = $21,105 (before state)

State withholding adds state-specific amount.

### Scenario B — Severance treated as nonperiodic (W-4R applies — hypothetical)

If BigCo had treated the severance as a nonperiodic distribution (rare), Marcus would file W-4R.

- Default rate: 10% (other nonperiodic, not ERD because severance isn't from a qualified retirement plan)
- Marcus could elect 0% (no withholding) or up to 100%
- No FICA / FUTA in some severance arrangements (depending on facts)

If Marcus elects 22% on W-4R:

- Severance: $30,000
- Federal withholding: $30,000 × 22% = $6,600
- FICA: depends on facts ($0 if treated as deferred comp; $2,295 if FICA applies)
- Net: $23,400 (no FICA) or $21,105 (with FICA)

---

## Step 4 — What Marcus should do

Since BigCo treats the severance as wages, Marcus does NOT file W-4R. He may file an updated **W-4** if he wants to adjust withholding on the severance.

### W-4 update (Marcus's likely path)

Marcus calculates his expected 2026 tax liability:

| Source | Amount |
|--------|--------|
| BigCo wages (already paid) | $75,000 |
| Severance | $30,000 |
| Estimated new-job wages (3 months at ~$6,250/mo) | $18,750 |
| **Total wages** | **$123,750** |
| Less: 2026 standard deduction (single) | $15,700 (estimate) |
| Taxable income | $108,050 |

Federal tax on $108,050 (single 2026 estimated brackets):

- 10% on first $11,925 = $1,193
- 12% on next $36,550 = $4,386
- 22% on next $54,875 = $12,073
- 24% on next $4,700 = $1,128
- **Total: $18,780**

Marcus's withholding so far (BigCo W-2, 9 months at typical W-4 single):

- Approx $11,000 federal withheld year-to-date

Severance withholding at 22% supplemental rate: $6,600

After severance and YTD: $11,000 + $6,600 = $17,600 (close to estimated $18,780 liability)

Marcus's likely tax outcome: **owes ~$1,180 at filing**, or approximately break-even after factoring in his new-job withholding.

If Marcus wants to avoid owing at filing, he can:

1. Submit a new **W-4** to his next employer with "extra withholding" of ~$100/month for the rest of 2026
2. Or pay a Form 1040-ES estimated payment in October 2026 to cover the gap

**No W-4R is needed.**

---

## Step 5 — Hypothetical W-4R draft (for the rare nonperiodic-severance case)

If, hypothetically, BigCo had classified the severance as nonperiodic, Marcus's W-4R would look like:

```
# Form W-4R — DRAFT (hypothetical, severance treated as nonperiodic)

## Filing summary
- Recipient:                 Marcus Williams
- SSN:                       XXX-XX-XXXX
- Payor:                     BigCo Inc. Severance Plan
- Payment type:              Other nonperiodic (severance from deferred comp arrangement)
- Distribution amount:       $30,000
- Elected withholding rate:  22% (matches estimated marginal bracket)
- Default rate that would apply if blank: 10%
- Tax year of distribution:  2026

## Form W-4R (printable)

Withholding Certificate for Nonperiodic Payments and Eligible Rollover Distributions
For tax year 2026

Step 1 — Personal Information
Name:                Marcus Williams
Social Security number: XXX-XX-XXXX
Address:             [Marcus's address]
City, state, ZIP:    [city, state, ZIP]

Step 2 — Withholding Rate
1a. Payor name:      BigCo Inc.
1b. Payor address:   [BigCo HR / payroll address]

2.  Rate: 22 %

Step 3 — Sign Here
Signature: Marcus Williams
Date:      [date of severance acceptance]

## Reminders (hypothetical case)
- Severance treated as nonperiodic — W-4R applies
- Default 10% would under-withhold given Marcus's 22% marginal bracket
- 22% election aligns withholding with marginal rate
- §72(t) does NOT apply (severance isn't from a retirement account)
```

---

## What Marcus actually does

Since BigCo confirmed severance is treated as wages:

- [X] **NO W-4R filed.** Severance goes through BigCo payroll.
- [X] BigCo applies 22% supplemental withholding rate (the standard method for supplemental wages)
- [X] Severance reported on Form W-2 along with regular wages
- [X] FICA (7.65%) withheld
- [X] Marcus updates his **W-4** with his next employer if he wants to fine-tune withholding for the rest of 2026
- [X] Marcus pays a Form 1040-ES estimated payment in Q4 2026 if needed to cover the small gap (~$1,180)

---

## Decision summary

| Question | Answer |
|----------|--------|
| Is the severance from a qualified retirement plan? | No |
| Is the severance from a deferred compensation arrangement? | No (BigCo treats as wages) |
| Does BigCo's payroll process the severance as wages? | Yes |
| Form to use? | **W-4** (NOT W-4R) |
| Default federal withholding rate applied? | 22% supplemental rate |
| FICA / FUTA applied? | Yes |
| Reported on? | Form W-2 (with regular wages) |

---

## Common confusion to avoid

1. **"Severance always gets W-4R"** — false. Most severance is wages and uses W-4.

2. **"FICA never applies to severance"** — false in most cases. The Supreme Court in *United States v. Quality Stores, Inc.* (2014) held that severance is generally subject to FICA (with narrow exception for SUB plans).

3. **"W-4R can override the supplemental wage rate"** — false. W-4R applies to nonperiodic distributions from retirement-plan-like arrangements, not wages. For supplemental wages, the percentage method (22% / 37% over $1M) or aggregate method controls; the recipient's W-4 informs but doesn't override.

4. **"I should file both W-4 and W-4R to be safe"** — false and confusing. File only the one that applies. Filing the wrong form may delay the payment or cause mis-withholding.

5. **"My ex-employer asked me to fill W-4R"** — confirm with HR what the form is actually for. Some HR departments use W-4R for severance from deferred comp arrangements; others mistakenly hand out W-4R for ordinary wage severance. Ask: "Is this severance treated as wages or as a nonperiodic distribution?" The answer determines the form.

---

## Sources cited in this draft

- IRS Form W-4 (regular wage withholding — what Marcus actually uses)
- IRS Form W-4R (nonperiodic distributions — does NOT apply to Marcus)
- IRC §3402 (income tax withholding on wages)
- IRC §3402(g) (supplemental wages, including severance)
- Treas. Reg. §31.3402(g)-1 (supplemental wage withholding methods)
- IRC §3405 (withholding on retirement distributions — N/A to wage severance)
- *United States v. Quality Stores, Inc.*, 572 U.S. 141 (2014) — severance generally subject to FICA
- IRC §3121 (FICA wages definition)
- IRS Pub. 15 (Employer's Tax Guide — supplemental wage rules)
- IRS Pub. 525 (Taxable and Nontaxable Income — severance and unemployment)
