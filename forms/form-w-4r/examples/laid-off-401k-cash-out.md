# Example — Laid-off employee: severance is wages (W-4), the $24K 401(k) cash-out is the W-4R case

All 2026 figures: 2026 Form W-4R (ERD rules, Marginal Rate Tables, two-step method), Rev. Proc. 2025-32 (2026 single brackets, $16,100 standard deduction), Pub. 15 (2026) (severance and supplemental wages), Pub. 575 (2025), 2025 Instructions for Form 5329. Math checked in python.

## Scenario

**Filer**: Marcus Williams, age 38, laid off from BigCo Inc. in a workforce reduction at the end of September 2026

**Payments**:
1. $30,000 lump-sum severance from BigCo
2. A $24,000 cash-out of his BigCo 401(k) balance (pre-tax, no after-tax basis), which he wants as cash to cover expenses while job-hunting

**Purpose**: Marcus asks the agent to "fill out the W-4R for my severance and my 401(k)." The agent has to sort out which payment is a W-4R payment at all, then set the rate on the one that is.

**Key facts**:
- Age 38: under 59½. He separated from service before the year he turns 55, so §72(t) exception 01 does not apply; he names no other exception
- Filing status: Single, no dependents, SSN valid for employment, U.S. home address
- 2026 income picture: $75,000 of BigCo wages for January–September (already paid, regular W-4 withholding) + $30,000 severance + an expected $18,750 from a new job starting in October (3 months at $6,250)
- He confirmed with the IRS Tax Withholding Estimator that his wage withholding (including the severance at 22%) roughly covers the tax on his wages (see Step 2 for the $600 gap)

---

## Step 1 — Classify each payment

### Payment 1: $30,000 severance → wages, NOT a W-4R payment

"Severance payments are wages subject to social security and Medicare taxes, federal income tax withholding, and FUTA tax" (Pub. 15 (2026)). Severance pay is a supplemental wage (Pub. 15 (2026), section 7). Form W-4R only covers nonperiodic payments and eligible rollover distributions "from an employer retirement plan, annuity (including a commercial annuity), or individual retirement arrangement (IRA)" (2026 Form W-4R, Purpose of form). A severance check from BigCo's payroll is none of those.

→ **No W-4R for the severance.** BigCo withholds under the supplemental wage rules, and Marcus's tool for adjusting wage withholding is Form W-4 (see [`../../form-w4/SKILL.md`](../../form-w4/SKILL.md)).

### Payment 2: $24,000 401(k) cash-out → eligible rollover distribution (ERD)

Walked the decision tree:

1. Wages? No — paid by the 401(k) plan, not payroll.
2. Nonresident alien? No.
3. Direct rollover? No — Marcus wants cash.
4. Reasonably believed nontaxable? No — pre-tax 401(k).
5. Periodic? No — single payment.
6. ERD? **Yes** — a distribution from a qualified plan, eligible to be rolled over, not on the form's non-ERD list (not a hardship distribution, not an RMD).
7. → **W-4R, 20% default and floor.** "You can't choose withholding at a rate of less than 20% (including '-0-')... Don't give Form W-4R to your payer unless you want more than 20% withheld."

---

## Step 2 — The severance withholding (for context, not a W-4R)

If BigCo uses the 22% optional flat rate for supplemental wages (Pub. 15 (2026), section 7):

- Severance: $30,000
- Federal income tax withholding: $30,000 × 22% = $6,600
- Social security and Medicare (6.2% + 1.45%): $30,000 × 7.65% = $2,295 (his 2026 wages stay under the $184,500 wage base)
- Net before state tax: $30,000 − $6,600 − $2,295 = $21,105

Marcus's top rate is 24% (Step 3), so the 22% flat rate leaves about $600 (2% × $30,000) un-withheld on the severance. If he wants to cover it, the place is Step 4(c) on his new employer's W-4 — not the W-4R.

---

## Step 3 — Set the W-4R rate on the 401(k) cash-out

### The form's Marginal Rate Tables (single, 2026)

- **Step 1** — total income without the payment: $75,000 + $30,000 + $18,750 = **$123,750** → over $121,800 → **24%**
- **Step 2** — total income with the payment: $123,750 + $24,000 = **$147,750** → over $121,800 (under $217,875) → **24%**
- Same rate → the form says enter **24**

Cross-check with the 2026 rate schedule: taxable income $107,650 → tax $18,434; with the cash-out, taxable $131,650 → tax $24,194. Extra tax = $5,760 = exactly 24% of $24,000. ✓

### The §72(t) additional tax (not in the tables)

Marcus is under 59½ with no exception: 10% × $24,000 = **$2,400**, reported on Schedule 2 (Form 1040) line 8. Because his Form 1099-R will show code 1 and he owes the tax on the full amount, he can check the line 8 box instead of filing Form 5329 (2025 Instructions for Form 5329; 2025 Schedule 2).

Total tax caused by the cash-out: $5,760 + $2,400 = **$8,160 = 34%** of $24,000.

### Options

| Line 2 | Withheld | Cash to Marcus | Tax + §72(t) | Short at filing |
|--------|----------|----------------|--------------|-----------------|
| blank (20% default; no W-4R needed) | $4,800 | $19,200 | $8,160 | $3,360 |
| 24 (table rate) | $5,760 | $18,240 | $8,160 | $2,400 |
| 34 (table rate + 10) | $8,160 | $15,840 | $8,160 | $0 |

The agent shows the table and asks. Marcus doesn't want a bill in April and prefers withholding to quarterly estimates: **line 2 = 34**.

The agent also raises, without deciding: a direct rollover of the $24,000 to an IRA would avoid the 20% withholding, the income tax, and the §72(t) additional tax now; and once he leaves, cashing out is permanent for that money. Marcus confirms he needs the cash.

---

## Form W-4R — DRAFT for Marcus Williams (401(k) cash-out only)

```
# Form W-4R — DRAFT

## Filing summary (not on the form)
- Recipient:                 Marcus Williams
- Payer and account:         BigCo 401(k) Plan (recordkeeper per plan statement), account ****3307
- Payment type:              Eligible rollover distribution (401(k) cash-out after separation)
- Payment / taxable amount:  $24,000 / $24,000
- Elected withholding rate:  34% (line 2 = 34)
- Default rate that would apply without a W-4R: 20% (also the minimum)
- Tax year of payment:       2026

## Form W-4R (2026) entries

1a  First name and middle initial: Marcus           Last name: Williams
1b  Social security number: XXX-XX-XXXX
    Address: [Marcus's home address]
    City or town, state, and ZIP code: [city, state, ZIP]
2   Rate: 34 %
    Signature: Marcus Williams      Date: 10/12/2026

## Rate computation
- Total income without payment: $123,750 → table rate 24%
- Total income with payment: $147,750 → table rate 24%
- Same rate → 24; plus 10 points for the §72(t) additional tax at Marcus's request → 34
- Check: $24,000 × 34% = $8,160 = $5,760 income tax + $2,400 §72(t)

## Required actions
- [X] Marcus signs and dates the form
- [X] Form delivered with the plan's distribution request (portal or packet)
- [X] Marcus retains a copy

## Validation summary
- Classification: PASS — ERD (rate must be ≥ 20; 34 is allowed)
- Severance: correctly excluded (wages; Form W-4 territory)
- Rate within allowed range: PASS (whole number, 20–100)
- Recipient ID matches payer records: PASS
- Sanity warnings: §72(t) applies (age 38, no exception); covered by the extra 10 points

## Estimated tax impact
- Taxable amount:                    $24,000
- Withholding at 34%:                $8,160
- Cash to Marcus:                    $15,840
- Projected tax caused by cash-out:  $8,160 → difference $0

## Reminders
- §72(t) 10% additional tax: Schedule 2 line 8 (box checked; Form 5329 not required
  when the 1099-R shows code 1 and the full amount is subject to the tax)
- State income tax withholding: separate state election in the plan's request
- Form 1099-R from the plan in early 2027 (box 7 code 1); box 4 ($8,160) goes on
  Form 1040 line 25b (2025-form line number; re-check on the 2026 form)
- The severance appears on BigCo's Form W-2, not on the 1099-R

## Sources cited in this draft
- IRS Form W-4R (2026): eligible rollover distributions, line 2, Marginal Rate Tables, Example 1
- IRC §3405(c) (eligible rollover distributions — 20%); §402(c) (ERD definition)
- IRC §72(t) (additional tax on early distributions); 2025 Instructions for Form 5329 (exception 01)
- Rev. Proc. 2025-32 §§4.01, 4.14 (2026 single brackets and standard deduction)
- Pub. 15 (2026): severance payments are wages; section 7 supplemental wages
- Pub. 575 (2025): withholding on eligible rollover distributions; direct rollover option
```

---

## What Marcus actually does

- [X] **No W-4R for the severance.** It goes through BigCo payroll as supplemental wages (22% federal, 7.65% social security and Medicare), reported on his Form W-2
- [X] W-4R with **34** on line 2 goes to the 401(k) plan with the cash-out request
- [X] Optional: Step 4(c) on the new employer's W-4 to cover the ~$600 the 22% severance rate leaves short (use the form-w4 skill)

---

## Decision summary

| Question | Severance | 401(k) cash-out |
|----------|-----------|-----------------|
| Paid from a retirement plan, annuity, or IRA? | No (payroll) | Yes (qualified plan) |
| Form | **W-4** (wages) | **W-4R** |
| Default federal withholding | 22% optional flat rate or aggregate method (Pub. 15, section 7) | 20% (ERD floor) |
| Can the recipient go lower? | No W-4R election exists | No (20% minimum) |
| Social security / Medicare | Yes | No |
| Reported on | Form W-2 | Form 1099-R |

---

## Common confusion to avoid

1. **"Severance gets a W-4R"** — false. Severance payments are wages (Pub. 15 (2026)); Form W-4R covers payments from retirement plans, annuities, and IRAs.

2. **"FICA never applies to severance"** — false. Pub. 15 (2026) says severance payments are subject to social security, Medicare and FUTA tax (see also *United States v. Quality Stores, Inc.*, 572 U.S. 141 (2014)).

3. **"I can enter 0 on the W-4R for my 401(k) cash-out because I'll pay at filing"** — false for an ERD. The floor is 20%; only a direct rollover avoids withholding.

4. **"24% covers my 401(k) cash-out"** — only the income tax. Under 59½ with no exception, the §72(t) 10% is extra.

5. **"My ex-employer handed me a W-4R"** — ask what payment it is for. For a payment from the 401(k) plan, it's the right form; for severance, it isn't.

---

## Sources cited in this draft

- IRS Form W-4R (2026)
- IRS Form W-4 (2026) (wage withholding — the severance side)
- IRC §3402 and §3402(g) (wage and supplemental wage withholding); Treas. Reg. §31.3402(g)-1
- IRC §3405(c) (eligible rollover distributions)
- IRC §402(c) (eligible rollover distribution definition)
- IRC §72(t) (additional tax on early distributions)
- *United States v. Quality Stores, Inc.*, 572 U.S. 141 (2014) — severance subject to FICA
- IRS Pub. 15 (2026) (severance payments; section 7 supplemental wages)
- IRS Pub. 575 (2025) (eligible rollover distributions, direct rollovers)
- 2025 Instructions for Form 5329 (exception list)
