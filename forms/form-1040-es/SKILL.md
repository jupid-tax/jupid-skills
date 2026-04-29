---
name: form-1040-es
description: >
  Use this skill when an individual taxpayer needs to compute, schedule, or pay
  federal estimated income tax for the current year using Form 1040-ES.
  Triggers on phrases like "estimated tax payment", "1040-ES", "quarterly tax
  payment", "self-employment estimated tax", "avoid underpayment penalty",
  "how much should I pay quarterly", "safe harbor estimated tax", "Roth
  conversion estimated tax". Do NOT use for: corporate estimated tax (Form
  1120-W), employer payroll tax deposits (Form 941/944), W-2 withholding
  adjustment (Form W-4), or computing the underpayment penalty itself
  (Form 2210 — sister skill).
form: Form 1040-ES (Estimated Tax for Individuals)
audience: [solo, freelance, llc1, scorp, individual]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f1040es.pdf
---

# Form 1040-ES — Estimated Tax for Individuals

This skill produces an audit-grade quarterly-estimated-tax plan for an individual filer: computes projected total tax for the current year, applies the IRC §6654 safe harbor, allocates the required annual payment across the four installments, and emits filled payment vouchers (or the data needed for IRS Direct Pay / EFTPS).

The math is mechanical once the inputs are known. The judgment is in *which safe harbor applies* and *whether income is even or uneven across quarters* (which controls whether the user must use the annualized-income method on Form 2210 Schedule AI). When facts are missing, the agent must ASK rather than guess — wrong defaults silently understate tax and trigger IRC §6654 underpayment penalties.

**Companion guide for end users:** [Form 1040-ES Instructions: Complete 2026 Guide](https://jupid.com/blog/form-1040-es-instructions-guide-2026) on the Jupid blog. Same rules, narrative-style. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1040-ES, "1040-ES", "estimated taxes", "quarterly taxes", "Q1/Q2/Q3/Q4 estimate"
- The user describes income not subject to withholding: net Schedule C profit, net rental income, partnership / S-corp K-1 distributive share, large investment income, capital gains, IRA-to-Roth conversions, large bonus or RSU vest, gambling winnings, gig income
- The user says "I owe taxes and want to avoid a penalty next year" or "withholding isn't enough"
- The user asks how to pay safely so the IRS doesn't assess a §6654 penalty
- The user just filed a return showing balance due > $1,000 — they likely owe estimated tax for the current year (Form 1040-ES Worksheet starts from prior year)

Do **not** engage this skill when:

- The taxpayer is a C-corporation → use the (forthcoming) `form-1120-w` skill
- The taxpayer is an employer asking about payroll tax deposits → use the (forthcoming) `form-941` skill
- The user only needs to fix paycheck withholding → use the (forthcoming) `form-w-4` skill
- The user is computing the **penalty** itself for an already-underpaid year → use the `form-2210` skill (this skill prevents the penalty; Form 2210 measures it)
- The user is filing a return for a deceased taxpayer for estimates after death → consult Pub 559 (estates), out of scope here

If the user has both an S-corp salary (W-2 with withholding) and K-1 distributions, **both** sides matter: salary withholding counts toward the safe harbor, but K-1 income is not withheld on. The agent must combine them.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the estimates cover (typically the current calendar year). The 2026 tax year is paid via four installments due in 2026 and Jan 2027.
2. **Filing status** for the year being projected (Single, MFJ, MFS, HOH, QW). This drives bracket schedules.
3. **Prior-year (Year N−1) total tax** — Form 1040 Line 24 minus refundable credits already counted, equivalently the "tax shown on the return" used by IRC §6654(d)(1)(B). Required to compute the prior-year safe harbor.
4. **Prior-year AGI** — needed to determine whether the 110% safe harbor applies (AGI > $150,000; $75,000 for MFS). Per IRC §6654(d)(1)(C).
5. **Current-year income projections**, broken down by category:
   - Wages with withholding (and projected federal withholding amount)
   - Self-employment net profit (Schedule C / Schedule F / partnership SE)
   - Interest, dividends (qualified vs ordinary), capital gains (short vs long)
   - Rental net income (Schedule E)
   - K-1 income from S-corps / partnerships
   - Other (alimony, pension, Roth conversion, unemployment, gambling)
6. **Current-year deduction posture** — standard deduction or itemized estimate; QBI eligibility flag for pass-through income.
7. **Current-year credits** projected (CTC, education, foreign tax credit, etc.)
8. **Existing withholding sources** — W-2, 1099-R pension, Social Security voluntary withholding, prior estimated payments already made this year.
9. **Income evenness** — does the user expect income evenly across the year, or is it lumpy (e.g., Q4-only bonus, single Roth conversion in March, capital gain on a single sale)? Drives whether to use equal installments or annualized income method.
10. **Payment method preference** — IRS Direct Pay (free, ACH), EFTPS (free, requires enrollment), debit/credit card (fee), check + paper voucher.

For MFJ filers who may file separately, ask which scenario governs; the safe-harbor numbers split.

For users with farming/fishing income > 2/3 of gross — special rules apply (single Jan 15 installment OR file by March 1) per IRC §6654(i). Ask if applicable.

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm taxpayer category

Confirm the user is an individual (or grantor trust treated as the grantor). If they're a C-corp, partnership, or estate/trust, redirect:
- C-corp → Form 1120-W
- Partnership → no entity-level estimated tax; partners pay on their own 1040-ES
- Estate/non-grantor trust → Form 1041-ES

### Step 2 — Establish the prior-year safe harbor amount

The §6654(d)(1)(B) safe harbor: pay **100% of prior-year tax** (or **110% if prior-year AGI > $150,000**, or > $75,000 if MFS). Compute:

```
safe_harbor_prior = prior_year_tax × (1.10 if prior_AGI > 150,000 (or 75,000 MFS) else 1.00)
```

This is one of two safe harbors; lower of the two ends up controlling.

### Step 3 — Project current-year tax

Use the 1040-ES worksheet (page 8 of the form PDF). Compute:

1. **Estimated AGI** for the current year
2. **Less** standard or itemized deduction (estimate)
3. **Less** QBI deduction (20% of qualified pass-through, subject to taxable-income limits — load `references/qbi.md` if relevant)
4. **= Taxable income**
5. **Tax on taxable income** using current-year brackets — the agent must use the 2026 brackets published in IRS Rev. Proc. 2025-XX (verify before filing); for 2025 returns, see Rev. Proc. 2024-40
6. **Plus** additional taxes (SE tax via Schedule SE, Additional Medicare 0.9% via Form 8959 if wages+SE > threshold, NIIT 3.8% via Form 8960 if MAGI > threshold)
7. **Less** credits (CTC, foreign tax, education, etc.)
8. **= Total estimated tax**

The required annual payment is **90% of this number** per §6654(d)(1)(B)(i).

### Step 4 — Apply the safe harbor min

```
required_annual_payment = min(
  0.90 × current_year_estimated_tax,
  safe_harbor_prior_year   (from Step 2)
)
```

Pay this amount across the four installments (after subtracting expected withholding).

If withholding alone covers the required annual payment, no estimated payments are needed; the user is automatically safe-harbored.

### Step 5 — Allocate across the four installments

**Default (even-income method)**: divide `required_annual_payment − projected_withholding` by 4. Each installment is one-quarter due on:

- Q1: April 15, 2026 (covers Jan 1 – Mar 31)
- Q2: June 15, 2026 (covers Apr 1 – May 31)
- Q3: September 15, 2026 (covers Jun 1 – Aug 31)
- Q4: January 15, 2027 (covers Sep 1 – Dec 31)

(Per IRC §6654(c). When a due date falls on a weekend/holiday, it shifts to the next business day; verify against the IRS calendar before filing.)

**Annualized-income method**: if income is uneven, the user may pay more in later installments by completing Form 2210 Schedule AI when filing. The agent's job here is to flag this option, not to compute it (that's the `form-2210` skill). For the prospective plan, the agent can still recommend a heavier Q3 or Q4 if the user's income is back-loaded.

### Step 6 — Decide payment channel

- **IRS Direct Pay** — free, ACH from checking/savings, one-time per payment. https://www.irs.gov/payments/direct-pay
- **EFTPS** — free, requires enrollment (PIN mailed within 5–7 business days). https://www.eftps.gov
- **Debit / credit card** — small flat fee for debit, ~1.85% for credit. https://www.irs.gov/payments
- **Check + paper voucher** — mail Form 1040-ES voucher with check made payable to "United States Treasury". Address varies by state — see Form 1040-ES voucher instructions.

For agent-driven payments, Direct Pay is the canonical channel (no enrollment, deterministic flow). See `filing.md`.

### Step 7 — Run validation checks

See **Validation** below.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next forms/actions the user will need:

- **If estimated payments planned**: schedule reminders 5 business days before each due date
- **If income changes mid-year**: re-run the worksheet at Q3 (after Aug financials) and adjust Q4 voucher
- **If a single large event** (Roth conversion, asset sale, bonus): load `references/uneven-income.md` for guidance on whether to bunch the payment or annualize on Form 2210
- **At year-end**: verify total payments + withholding ≥ safe harbor minimum; if short, top up by Q4 voucher (Jan 15)
- **At return filing**: Form 1040 Line 26 reports total estimated payments; if underpaid despite safe-harbor planning, the user computes the penalty on Form 2210

### Step 10 — Submit (optional)

If the agent has browser-automation tooling and the user explicitly authorizes payment, follow [`filing.md`](./filing.md) for IRS Direct Pay flow.

---

## Line-by-line guidance

Form 1040-ES has a worksheet (page 8) and four payment vouchers (pages 9–12). For full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level summary below.

### 2026 Estimated Tax Worksheet (page 8 of f1040es.pdf)

| Line | Field | Notes |
|------|-------|-------|
| 1 | Adjusted gross income expected | Sum of all income categories minus above-the-line adjustments |
| 2a | Standard or itemized deduction | Use larger; standard deduction for 2026 set by Rev. Proc. — verify |
| 2b | QBI deduction | 20% × qualified pass-through income, subject to limits (IRC §199A) |
| 3 | Subtract Line 2 from Line 1 | Taxable income |
| 4 | Tax (from rate schedule) | Use 2026 brackets — verify Rev. Proc. before filing |
| 5 | Alternative Minimum Tax | Form 6251 if applicable |
| 6 | Add Lines 4 and 5 | |
| 7 | Credits | CTC, foreign tax, education, retirement savings, etc. |
| 8 | Subtract Line 7 from Line 6 | |
| 9 | Self-employment tax | 92.35% × SE earnings × 15.3% (with SS cap on the 12.4% portion) |
| 10 | Other taxes | NIIT, Additional Medicare, Section 965, etc. |
| 11a | Total tax | Sum of 8 + 9 + 10 |
| 11b | Refundable credits | Earned Income Credit, ACTC, premium tax credit |
| 11c | Subtract 11b from 11a | |
| 12a | 90% × Line 11c | One safe-harbor target |
| 12b | Prior-year tax × 100% (or 110%) | Other safe-harbor target |
| 12c | Smaller of 12a or 12b | Required annual payment |
| 13 | Income tax withheld + expected | Subtract from 12c |
| 14a | Subtract 13 from 12c | If ≤ $0, no estimates required |
| 14b | Divide Line 14a by 4 | Per-quarter installment |

### Payment vouchers (pages 9–12)

Each voucher (4 total) has identical fields:

- Filer's name, SSN
- Spouse's name, SSN (if MFJ)
- Address (street, city, state, ZIP)
- Amount of payment (cents allowed)
- Tax year (preprinted or write in)
- Voucher number (1, 2, 3, or 4 — preprinted)

Mail to the IRS address listed on the voucher instructions for the filer's state. Make check payable to "United States Treasury" and write "2026 Form 1040-ES" + SSN on the memo line.

If paying electronically (Direct Pay, EFTPS, card), the voucher is **not mailed**.

---

## Validation

Run these checks before declaring the plan ready. Surface any failure — don't silently fix.

### Math checks

- [ ] Worksheet Line 3 = Line 1 − Line 2a − Line 2b
- [ ] Worksheet Line 6 = Line 4 + Line 5
- [ ] Worksheet Line 11a = Line 8 + Line 9 + Line 10
- [ ] Worksheet Line 11c = Line 11a − Line 11b
- [ ] Worksheet Line 12a = 0.90 × Line 11c (rounded)
- [ ] Worksheet Line 12b correctly applies 110% if prior AGI > $150K (or $75K MFS), else 100%
- [ ] Worksheet Line 12c = min(12a, 12b)
- [ ] Worksheet Line 14a = Line 12c − Line 13
- [ ] Sum of four installment amounts = Line 14a (within ±$1 rounding)

### Sanity checks (warn, don't block)

- [ ] Self-employment tax computed: 92.35% × net SE earnings, then 15.3% up to SS wage base, 2.9% above. (2025 SS base: $176,100 per SSA. 2026 base announced ~Oct 2025 — verify.)
- [ ] Additional Medicare 0.9%: applies only to wages + SE earnings above filing-status threshold ($200K single, $250K MFJ, $125K MFS) per IRC §3101(b)(2). No employer match on this portion.
- [ ] NIIT 3.8%: applies to lesser of net investment income or AGI excess over MAGI threshold ($200K single, $250K MFJ, $125K MFS) per IRC §1411.
- [ ] If user has Roth conversion: the conversion amount is fully ordinary income in the year converted; estimated tax should cover it.
- [ ] If user has long-term capital gain pushing income into 20% LTCG bracket: ensure preferential rate is applied (don't tax LTCG at ordinary rates).
- [ ] If MFS spouse plans to file separately: verify $75,000 AGI threshold applied for 110% safe harbor.
- [ ] Withholding shortfall (Line 14a) > $1,000 confirms estimated payments are required (de minimis exception under §6654(e)(1) excuses filers with < $1,000 owed).
- [ ] No estimates required if total tax for prior year was zero AND the user was a US citizen / resident alien for the full year AND the prior tax year was 12 months (per §6654(e)(2)).

### Cross-form checks

- [ ] If user receives W-2 wages with withholding, those count as paid evenly across the year per §6654(g) — even if actually withheld late in the year. This often eliminates the need for separate estimates.
- [ ] If user is making estimated payments and ALSO has W-2 withholding, the worksheet subtracts withholding before computing the per-quarter voucher.
- [ ] Farmers/fishers (>2/3 gross income from farming/fishing): single payment due Jan 15 OR file & pay by March 1 — check IRC §6654(i) before applying default quarterly.

---

## Output format

The agent's deliverable is an **estimated-tax plan** the user can act on. Format:

```markdown
# Form 1040-ES — Estimated Tax Plan for tax year YYYY

## Filer
- Name: <legal name>
- SSN: <use placeholder, never log real SSN>
- Filing status: Single | MFJ | MFS | HOH | QW
- State (for voucher mailing): XX

## Prior-year baseline (tax year YYYY−1)
- Prior-year AGI: $XXX,XXX
- Prior-year total tax (Line 24): $X,XXX
- 110% safe harbor applies: Yes (AGI > $150K) | No
- Prior-year safe harbor amount: $X,XXX

## Current-year projection (tax year YYYY)
| Worksheet line | Amount |
|----------------|--------|
| 1.  Estimated AGI | $XXX,XXX |
| 2a. Standard / itemized deduction | $XX,XXX |
| 2b. QBI deduction | $X,XXX |
| 3.  Taxable income | $XXX,XXX |
| 4.  Tax (from rate schedule) | $XX,XXX |
| 5.  AMT | $X |
| 6.  Subtotal | $XX,XXX |
| 7.  Credits | $X,XXX |
| 8.  Subtotal | $XX,XXX |
| 9.  Self-employment tax | $X,XXX |
| 10. Other taxes (NIIT, Add'l Medicare) | $X,XXX |
| 11a. Total tax | $XX,XXX |
| 11b. Refundable credits | $0 |
| 11c. Net total tax | $XX,XXX |
| 12a. 90% × Line 11c | $XX,XXX |
| 12b. Prior-year × 100% (or 110%) | $XX,XXX |
| 12c. Required annual payment (smaller) | $XX,XXX |
| 13. Expected withholding | $X,XXX |
| 14a. Net required estimated payments | $XX,XXX |
| 14b. Per-quarter (÷ 4) | $X,XXX |

## Installment schedule
| Voucher | Due date | Amount | Channel |
|---------|----------|--------|---------|
| Q1 | 2026-04-15 | $X,XXX | Direct Pay |
| Q2 | 2026-06-15 | $X,XXX | Direct Pay |
| Q3 | 2026-09-15 | $X,XXX | Direct Pay |
| Q4 | 2027-01-15 | $X,XXX | Direct Pay |
| **Total** | | **$XX,XXX** | |

## Method
- [ ] Equal installments (income spread evenly)
- [ ] Annualized income (income uneven; will file Form 2210 Schedule AI)
- [ ] Single-payment farmer/fisher exception (>2/3 gross from farming/fishing)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Year-aware notes:
  - 2026 brackets verified against Rev. Proc. YYYY-XX (or flagged as TBD)
  - 2026 SS wage base verified against SSA announcement (or flagged as TBD)
  - 2026 standard deduction verified against Rev. Proc. (or flagged as TBD)

## Sources cited in this draft
- IRS Form 1040-ES (revision date YYYY)
- IRC §6654 (failure to pay estimated tax)
- IRC §1411 (NIIT)
- IRC §3101(b)(2) (Additional Medicare Tax)
- IRC §199A (QBI deduction)
- Rev. Proc. YYYY-XX (current-year inflation adjustments)
- Notice YYYY-XX (current-year mileage rate, if Schedule C income)
- IRS Pub. 505 (Tax Withholding and Estimated Tax)
```

The plan is **not** a filing — it's a forward-looking calendar with computed amounts. The user (or agent, with consent) submits each voucher when due.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete walkthrough of the 1040-ES worksheet (page 8) and the four vouchers (pages 9–12)
- [`references/safe-harbor-rules.md`](./references/safe-harbor-rules.md) — IRC §6654 safe harbors, 90% / 100% / 110% rules, de minimis $1,000 exception, withholding-as-paid-evenly rule
- [`references/uneven-income.md`](./references/uneven-income.md) — Annualized income installment method (Form 2210 Schedule AI), when to use it, what changes per quarter
- [`references/se-tax-niit-amt.md`](./references/se-tax-niit-amt.md) — Self-employment tax computation, NIIT 3.8%, Additional Medicare 0.9%, AMT — all flow into Line 9–10 of the worksheet
- [`references/payment-channels.md`](./references/payment-channels.md) — Direct Pay vs EFTPS vs card vs check/voucher; trade-offs and operational steps
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes that trigger IRC §6654 penalties despite "paying estimates"
- [`filing.md`](./filing.md) — Browser-automation playbook for IRS Direct Pay submission

## Examples

End-to-end worked plans. Use these as patterns when the user's situation is similar.

- [`examples/freelancer-100k-schedule-c.md`](./examples/freelancer-100k-schedule-c.md) — Service freelancer, $100K Schedule C net profit, equal installments
- [`examples/w2-side-gig-q4-topup.md`](./examples/w2-side-gig-q4-topup.md) — W-2 employee with side income, fixes shortfall via single Q4 voucher
- [`examples/retiree-roth-conversion-q1.md`](./examples/retiree-roth-conversion-q1.md) — Retiree with Roth conversion + capital gain spike, single Q1 estimated payment

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed — the IRS updates the form, brackets, wage bases, and thresholds annually.

- [Form 1040-ES Instructions: Complete 2026 Guide](https://jupid.com/blog/form-1040-es-instructions-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1040-ES (latest)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) — combined form, worksheet, and instructions
- [About Form 1040-ES](https://www.irs.gov/forms-pubs/about-form-1040-es) — IRS landing page with archive of past revisions
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (the deep authority on §6654)
- [IRS Direct Pay](https://www.irs.gov/payments/direct-pay) — primary electronic payment channel
- [EFTPS](https://www.eftps.gov) — Electronic Federal Tax Payment System
- [Pay by Card or Digital Wallet](https://www.irs.gov/payments/pay-your-taxes-by-debit-or-credit-card) — third-party processor list and fees
- IRC §6654 — failure by individual to pay estimated tax
- IRC §6654(d)(1)(B) — required annual payment (lesser of 90% current / 100% prior)
- IRC §6654(d)(1)(C) — 110% rule for high-income filers
- IRC §6654(e)(1) — de minimis $1,000 exception
- IRC §6654(g) — withholding treated as paid evenly across the year
- IRC §6654(i) — farmers and fishers special rule
- IRC §1411 — Net Investment Income Tax (3.8%)
- IRC §3101(b)(2) — Additional Medicare Tax (0.9%)
- IRC §199A — Qualified Business Income deduction (20%)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025 (verify 2026 procedure when published)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a plan, that the output is a starting point and that complex situations (large capital events, foreign income, multi-state, AMT, NIIT optimization) warrant a licensed tax professional's review.
