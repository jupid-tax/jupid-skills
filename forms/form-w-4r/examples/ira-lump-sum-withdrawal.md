# Example — 65-year-old taking $50K Traditional IRA distribution; rate set by projection

All 2026 figures: Rev. Proc. 2025-32 (brackets, standard deduction, $1,650 additional deduction for a married filer 65+, 0% capital gain band to $98,900 MFJ), P.L. 119-21 senior deduction ($6,000 per eligible person, 2025–2028), the Social Security Benefits Worksheet in the Form 1040 instructions, and the 2026 Form W-4R. Math checked in python.

## Scenario

**Filer**: Robert Tanaka, age 65, retired

**Distribution**: $50,000 cash withdrawal from his Traditional IRA at Fidelity

**Purpose**: Robert is retired and lives off Social Security ($30,000/year) plus IRA withdrawals. He's withdrawing $50,000 in 2026 to pay for his daughter's wedding. He wants withholding close to the tax so he neither owes a big bill (or a §6654 underpayment penalty) nor waits a year for a large refund.

**Key facts**:
- Robert is 65, so **no §72(t) additional tax** applies (he's past 59½)
- Filing status: Married Filing Jointly (his wife Sarah is 64 at the end of 2026, also retired, no income, not yet claiming Social Security); both have SSNs valid for employment
- Distribution is from a Traditional IRA, no basis (no Form 8606 history) → **other nonperiodic** under IRC §3405(b)
- **Default withholding: 10%** ($5,000); Robert can choose any whole-number rate 0–100 (he has a U.S. home address)
- No other withholding and no estimated payments for 2026

---

## Step 1 — Classify the payment

Walked the decision tree:

1. Wages or severance? No.
2. Nonresident alien? No.
3. Direct rollover / trustee-to-trustee transfer? No — cash to Robert.
4. Reasonably believed nontaxable (qualified Roth)? No — Traditional IRA.
5. Periodic? No — one-time withdrawal (and IRA distributions payable on demand are nonperiodic, per the form).
6. ERD? No — IRA distribution, not from a qualified plan / 403(b) / governmental 457(b).
7. → **Other nonperiodic**. W-4R, default 10%, any rate 0–100.

---

## Step 2 — Project the tax caused by the withdrawal

Robert's 2026 income picture:

| Source | Amount |
|--------|--------|
| Social Security (Robert) | $30,000 |
| Social Security (Sarah) | $0 (not yet claiming) |
| IRA distribution (this withdrawal) | $50,000 |
| Ordinary (nonqualified) dividends | $300 |
| Long-term capital gains | $1,200 (small taxable brokerage account) |

**Social Security taxability** (Social Security Benefits Worksheet, MFJ base amounts $32,000 / $44,000): provisional income = $15,000 (half of benefits) + $50,000 + $300 + $1,200 = $66,500. Excess over $32,000 = $34,500; over $44,000 = $22,500. Taxable = smaller of 85% × $30,000 = $25,500 or [85% × $22,500 + smaller of $6,000 or $15,000] = $19,125 + $6,000 = **$25,125**.

| Item | Amount |
|------|--------|
| Taxable Social Security | $25,125 |
| IRA distribution (fully taxable; basis $0) | $50,000 |
| Ordinary dividends | $300 |
| Long-term capital gains | $1,200 |
| **AGI** | **$76,625** |
| Less: 2026 standard deduction (MFJ $32,200 + $1,650 for Robert, 65) | $33,850 |
| Less: senior deduction (Schedule 1-A; Robert only; MAGI under $150,000) | $6,000 |
| **Taxable income** | **$36,775** (ordinary $35,575 + LTCG $1,200) |

Federal tax on $35,575 ordinary income (2026 MFJ: 10% to $24,800, 12% to $100,800):

- 10% on first $24,800 = $2,480
- 12% on next $10,775 = $1,293
- **Ordinary tax: $3,773**

Tax on the $1,200 LTCG: 0% (taxable income under the $98,900 MFJ 0% band).

**Estimated total federal tax: $3,773.**

Without the withdrawal, provisional income would be $16,500 (under $32,000), so none of the Social Security would be taxable and taxable income would be $0. **The whole $3,773 is caused by the withdrawal: 7.55% of $50,000 → round up to 8%.**

Why not just use the Marginal Rate Tables on the form? The simpler table approach (total income with the payment, $76,625 → MFJ band $57,000–$133,000) gives 12%. The tables assume the basic standard deduction only; they don't include Robert's $1,650 age-65 amount, the $6,000 senior deduction, or the way the withdrawal makes Social Security taxable, so here they overstate the rate.

---

## Step 3 — Determine the withholding rate

Robert's options:

| Line 2 | Withholding | Net to Robert | At filing (tax $3,773) |
|--------|-------------|---------------|------------------------|
| -0- | $0 | $50,000 | owes $3,773 |
| 8 (projection) | $4,000 | $46,000 | refund $227 |
| blank (10% default) | $5,000 | $45,000 | refund $1,227 |
| 12 (table, simpler method) | $6,000 | $44,000 | refund $2,227 |
| 22 | $11,000 | $39,000 | refund $7,227 |

Robert's preference: he doesn't want to owe at filing AND doesn't want to over-withhold. At "-0-" he would owe $3,773, which is more than $1,000 with no withholding, so a §6654 penalty could apply unless his 2025 tax was low enough for the prior-year safe harbor (ask before relying on that).

**Robert chooses: 8 on line 2.**

Alternatively, if Robert wants a cushion against a larger-than-expected tax, he can leave line 2 blank and accept the 10% default ($1,227 refund). He goes with 8.

---

## Form W-4R — DRAFT for Robert Tanaka

```
# Form W-4R — DRAFT

## Filing summary (not on the form)
- Recipient:                 Robert Tanaka
- Payer and account:         Fidelity, Traditional IRA ****4821
- Payment type:              Other nonperiodic (Traditional IRA distribution)
- Payment / taxable amount:  $50,000 / $50,000
- Elected withholding rate:  8% (line 2 = 8)
- Default rate that would apply without a W-4R: 10%
- Tax year of payment:       2026

## Form W-4R (2026) entries

1a  First name and middle initial: Robert           Last name: Tanaka
1b  Social security number: XXX-XX-XXXX
    Address: [Robert's home address]
    City or town, state, and ZIP code: [city, state, ZIP]
2   Rate: 8 %
    Signature: Robert Tanaka        Date: 04/15/2026

## Rate computation
- Tax with the withdrawal: $3,773; without: $0
- $3,773 ÷ $50,000 = 7.55% → rounded up to 8
- Marginal Rate Table (simpler method) would give 12; not used because the tables
  ignore the age-65 and senior deductions and the Social Security interaction

## Required actions
- [X] Robert signs and dates the form
- [X] Form delivered to Fidelity (portal distribution-request workflow)
- [X] Robert retains a copy

## Validation summary
- Classification: PASS — Other nonperiodic
- Rate within allowed range: PASS (8, whole number, 0–100; U.S. address on file)
- Recipient ID matches payer records: PASS

## Estimated tax impact
- Taxable amount:                           $50,000
- Withholding at 8%:                        $4,000
- After-withholding cash to Robert:         $46,000
- Projected tax caused by the withdrawal:   $3,773 → about $227 refund

## Reminders
- §72(t) additional tax: N/A — Robert is 65 (past 59½)
- The 8% election generally carries over to future payments from this IRA until
  he submits a new W-4R (2026 Form W-4R, page 1)
- State income tax withholding: separate state election in Fidelity's request; ask
  Fidelity which state rules apply
- Form 1099-R from Fidelity in early 2027: IRA distribution on 2026 Form 1040 line 4a/4b,
  box 4 withholding on line 25b (line numbers per the 2025 form; re-check on the 2026 form)

## Sources cited in this draft
- IRS Form W-4R (2026), page 2 (nonperiodic payments, line 2, Marginal Rate Tables method)
- IRC §3405(b) (other nonperiodic — 10% default)
- IRC §72 (taxation of distributions from retirement accounts)
- Rev. Proc. 2025-32 §§4.01, 4.03, 4.14 (2026 brackets, capital gain bands, standard deduction)
- P.L. 119-21 (senior deduction, Schedule 1-A)
- IRS Pub. 590-B (Distributions from IRAs); Pub. 915 / Form 1040 instructions (Social Security Benefits Worksheet)
```

---

## Filing channel

Robert delivers the W-4R election through Fidelity's online withdrawal request (menu names are typical, not verified; follow the screen labels):

1. Logs in at fidelity.com
2. Opens the withdrawal request for his Traditional IRA
3. Enters distribution amount: $50,000
4. **Federal tax withholding section**: the portal pre-selects the 10% default
5. Robert chooses a different rate and enters 8
6. State withholding: completes the separate state election shown on the request (asks Fidelity about his state's rules)
7. Direct deposit to his linked checking account
8. E-signs (typed name + acknowledgment + 2FA code)
9. Confirmation: distribution scheduled; net $46,000 before any state withholding

Form 1099-R will be issued in early 2027.

---

## What Robert should also do

- [X] Set a Form 1040 reminder for spring 2027 to reconcile (expects a small refund)
- [X] Remember the 8% election stays on file for later withdrawals from this IRA; submit a new W-4R if the next withdrawal's tax picture differs
- [X] Timing note to raise, not decide: a withdrawal split across two tax years changes how much Social Security becomes taxable each year. The wedding is in 2026, so cash flow drives the decision.

---

## Sources cited in this draft

- IRS Form W-4R (2026)
- IRC §3405(b) (other nonperiodic — 10% default)
- IRC §72 (taxation of distributions)
- Rev. Proc. 2025-32 (2026 inflation adjustments)
- P.L. 119-21 (senior deduction)
- IRS Pub. 590-B (IRA Distributions)
- IRS Pub. 915 (Social Security taxation)
- IRC §6654 (estimated tax — withholding at 8% covers the projected tax)
