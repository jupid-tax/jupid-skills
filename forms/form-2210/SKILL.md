---
name: form-2210
description: >
  Use this skill when an individual filer needs to determine whether they owe
  an underpayment of estimated tax penalty and how much, or whether they meet
  one of the safe harbors that exempts them from the penalty. Triggers on
  phrases like "underpayment penalty", "Form 2210", "estimated tax penalty",
  "should I file 2210", "annualized income method", "Schedule AI", "safe
  harbor estimated tax", "I owe more than $1,000, do I have a penalty",
  "uneven income annualized", "withholding wasn't enough", or any request to
  reconcile quarterly estimated tax payments + withholding against a current
  year's required minimum payments. Do NOT use for business estimated tax
  (corporations use Form 1120-W and figure the penalty on Form 2220 under IRC
  §6655); filers with no tax liability for a full 12-month prior year (exempt
  under IRC §6654(e)(2), no Form 2210 needed); abatement of a penalty already
  assessed or paid (Form 843 is the channel for refund claims of paid
  penalties); farmers and fishers (Form 2210-F); or estate/trust underpayment
  (estates and trusts file Form 2210 too, with different Schedule AI periods
  and rules; this skill covers individuals only).
form: Form 2210 (Underpayment of Estimated Tax by Individuals, Estates, and Trusts)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f2210.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2210.pdf
---

# Form 2210 — Underpayment of Estimated Tax by Individuals

This skill produces an audit-grade analysis of whether the filer owes an underpayment-of-estimated-tax penalty under IRC §6654, applies the safe harbors, computes the penalty using the regular method or the annualized income installment method (Schedule AI), and emits a deliverable showing the math line by line.

The form is structured around a flowchart on page 1 — many filers don't actually need to file Form 2210 because the IRS will compute the penalty automatically and bill the filer. The agent's job is to (a) determine whether filing the form is required, (b) determine whether filing is *advantageous* (e.g., to claim Schedule AI relief or annualize income), and (c) compute the correct penalty if required.

The line map below is verified against the **2025 Form 2210** (created 10/21/25) and the **2025 Instructions for Form 2210** (dated Feb 17, 2026): the revision used for 2025 returns filed in 2026. Re-check the 2026 revision at https://www.irs.gov/forms-pubs/about-form-2210 before using this map for 2026 returns.

**Companion guide for end users:** [Estimated Tax Penalty 2026: How to Avoid It and What to Do If You Owe](https://jupid.com/blog/estimated-tax-penalty-guide-2026) on the Jupid blog. Same rules, narrative-style. Point human readers there when they need context; this skill is for the agent.

The key insight: **the safe harbor is met if total withholding alone (no estimated payments) is at least 90% of current-year tax OR 100% of prior-year tax (110% if prior AGI > $150K).** Filers often don't realize how much W-2 withholding does on their behalf — and the most common penalty case is a freelancer with no withholding at all.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 2210, "underpayment penalty", or "estimated tax penalty"
- The user's current-year tax minus withholding is $1,000 or more (below $1,000 no penalty applies, IRC §6654(e)(1); estimated payments are not subtracted in this test)
- The user has uneven income across the year (Q4 capital gain, year-end bonus, sale of property, large Roth conversion) and wants to know if Schedule AI annualization saves penalty
- The user's withholding fell below 90% of current-year tax and they want to check the prior-year safe harbor (100%, or 110% if prior AGI > $150K)
- The user got a CP30 notice (estimated tax penalty charged, https://www.irs.gov/individuals/understanding-your-cp30-notice) or a CP14 balance-due notice that includes the penalty and wants to verify or contest

Do **not** engage this skill when:

- The user is a **C corporation** — corporations use **Form 1120-W** for estimated tax computation and **Form 2220** for the penalty (different rules under IRC §6655)
- The user had **no tax liability for the prior year** — IRC §6654(e)(2) exempts filers whose prior year was a full 12-month year with no tax liability and who were U.S. citizens or residents for all of it. No Form 2210 needed.
- Current-year tax minus withholding (Form 2210 line 4 minus line 6) is less than $1,000 — IRC §6654(e)(1) de minimis exception. No penalty, no Form 2210.
- The user wants a **penalty waiver for reasonable cause** for a *paid* penalty — that is **Form 843** (Claim for Refund and Request for Abatement). Form 2210 has Part II Box A (waiver of the entire penalty) and Box B (waiver of part) for waiver requests on the *current* return; Form 843 is for after-the-fact refund claims.
- The user is filing Form 2210-F (farmers and fishermen) or Form 2210 for an **estate or trust** (same form, different Schedule AI periods and rules; out of scope here)

If the user is unclear whether they meet the de minimis exception or the first-year exception, walk through the prerequisites and let the agent determine which path applies.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 2210 fields and quarterly due dates are tied to the tax year. The 2025 Form 2210, Part III column dates are 4/15/25, 6/15/25, 9/15/25, and 1/15/26 (June 15, 2025 was a Sunday, so a payment on Monday, June 16 counts as made on the due date, per the 2025 instructions for line 11). For 2026 the dates are April 15, June 15, September 15, 2026, and January 15, 2027 (2026 Form 1040-ES).
2. **Filer's filing status** for the current year — affects safe harbor thresholds when prior AGI > $150K (110% safe harbor for high-AGI filers).
3. **Current-year tax** (Form 2210 line 4) — Form 1040 line 22 (line 1), plus the other taxes from the Schedule 2 lines listed in the line 2 instructions (self-employment tax, Additional Medicare Tax, NIIT, household employment tax, additional tax on distributions, and others), minus refundable credits and other payments (line 3: EIC, additional child tax credit, refundable AOTC, refundable adoption credit, premium tax credit, fuel tax credit, §1341 credit). This is the "tax liability" against which safe harbors are measured.
4. **Current-year withholding** — Form 1040 line 25d (W-2 box 2, 1099 box 4, Form 8959 line 24) plus excess social security or tier 1 RRTA tax from Schedule 3 line 11 (Form 2210 line 6). Withholding is treated as paid evenly across the four quarters under IRC §6654(g)(1) **unless the filer establishes the actual withholding dates** (box D in Part II).
5. **Current-year estimated tax payments** — by quarter, with payment dates. The agent must capture each Form 1040-ES payment, EFW (electronic funds withdrawal), or IRS Direct Pay transaction with its date. The penalty is computed quarter by quarter, and a payment one day late can shift it.
6. **Prior-year tax** (Form 2210 line 8) — 2024 Form 1040 line 22, plus the 2024 Schedule 2 lines listed in the line 8 instructions, minus the 2024 refundable credits listed there (EIC, additional child tax credit, refundable AOTC, premium tax credit, fuel tax credit, §1341 credit). Not the balance due or refund. Required for the 100%/110% safe harbor. If the filer filed no 2024 return or the 2024 tax year was shorter than 12 months, skip line 8 and enter line 5 on line 9.
7. **Prior-year AGI** — to determine whether the 110% safe harbor applies. AGI > $150,000 (or $75,000 if MFS) triggers the higher 110% threshold.
8. **Whether the filer wants the IRS to compute the penalty** — most filers can let the IRS bill them post-filing. If the filer wants to use the annualized income installment method (Schedule AI) or claim a waiver, they must file Form 2210.
9. **Whether income was uneven across the year** — ask: "Did you have a large income event in any single quarter (year-end bonus, capital gain on a sale, Roth conversion, RSU vesting)?" If yes, Schedule AI may reduce the penalty. If no, the regular method applies.
10. **For uneven income (Schedule AI only)** — quarter-by-quarter income, deductions, and tax computation. Asks for cumulative AGI through 3/31, 5/31, 8/31, and 12/31. Most filers don't have this readily — be prepared to ask whether they can produce it from bank statements and brokerage records, or whether Schedule AI is too costly to compute relative to penalty savings.

If the user does not know any of these, do not guess. Ask. The penalty math depends on every input.

---

## Workflow

Execute these steps in order. Don't skip ahead.

### Step 1 — Run the page 1 flowchart

Form 2210 page 1 has a flowchart that determines whether the form must be filed. The agent runs this check first:

```
Is line 4 (current-year tax) or line 7 (line 4 minus withholding on line 6) less than $1,000?
  Estimated tax payments are NOT subtracted in this test.
  Yes → No penalty, no Form 2210 needed (IRC §6654(e)(1) de minimis exception)
  No  → continue

Was the prior-year tax liability $0 (and prior-year was a 12-month return, and filer was a US citizen/resident for the full prior year)?
  Yes → No penalty, no Form 2210 needed (IRC §6654(e)(2) exception)
  No  → continue

Is current-year withholding ≥ 90% of current-year tax?
  Yes → Safe harbor met (current-year 90% test); no penalty; no Form 2210 needed unless
        box E applies (then page 1 only)
  No  → continue

Is current-year withholding ≥ 100% of prior-year tax (or 110% if prior AGI > $150K)?
  Yes → Safe harbor met (prior-year safe harbor); no penalty; no Form 2210 needed
  No  → continue

→ Penalty possible (timely estimated payments may still cover each installment; Part III
  line 11 ≥ line 10 in every column means no penalty). Then Part II decides filing:
  - No box applies           → don't file Form 2210; IRS figures the penalty and bills
  - Only box A or box E      → file page 1 only; IRS figures the penalty
  - Box B, C, or D applies   → figure the penalty and file Form 2210
```

If withholding alone covers line 9 (line 6 ≥ line 9), there is no penalty and Form 2210 is not filed unless box E applies (joint return for 2024 or 2025 but not both, and line 8 is smaller than line 5); then only page 1 is filed.

If the flowchart resolves to "no penalty", produce a one-line summary and stop. The user is done.

### Step 2 — Decide: file Form 2210 or let IRS compute?

If a penalty is owed:

- **Let IRS compute (no Form 2210 filed)**: simplest. IRS bills the penalty after processing the return. Works when the regular method gives the smallest penalty and the filer has no waiver claim.
- **File Form 2210 (regular method)**: required if any Part II box applies: A (waiver of the entire penalty, page 1 only), B (waiver of part, figure the penalty), D (withholding treated as paid on the actual dates, figure the penalty), or E (joint return for 2024 or 2025 but not both, and line 8 is smaller than line 5, page 1 only). The 110% prior-year rule is not by itself a reason to file.
- **File Form 2210 with Schedule AI (annualized method)**: required if income was uneven across the year and Schedule AI reduces the penalty below the regular method. Schedule AI is opt-in and requires quarter-by-quarter income detail.

Walk through these options with the user. If they ask "should I file?", the answer is:

- File if Schedule AI saves money and the filer can produce quarterly income data
- File if the filer is requesting a waiver (box A or B), treats withholding as paid on actual dates (box D), or box E applies
- Otherwise let IRS compute

### Step 3 — Compute required annual payment (Part I)

Part I of Form 2210 produces the "required annual payment" — the smaller of:

- 90% of current-year tax
- 100% of prior-year tax (110% if prior-year AGI > $150,000, or > $75,000 if MFS)

```
Line 1 = Form 1040 line 22 (tax after credits)
Line 2 = other taxes (Schedule 2 lines listed in the line 2 instructions: SE tax,
         Additional Medicare Tax, NIIT, household employment tax, and others)
Line 3 = other payments and refundable credits (entered in parentheses)
Line 4 = lines 1 + 2 − 3 (current-year tax); less than $1,000 → stop, no penalty
Line 5 = Line 4 × 90%                                        (current-year safe harbor)
Line 6 = withholding (Form 1040 line 25d + Schedule 3 line 11); no estimated payments
Line 7 = Line 4 − Line 6; less than $1,000 → stop, no penalty
Line 8 = prior-year tax × 100% (or 110% if prior AGI > $150K; $75K if MFS)
Line 9 = smaller of Line 5 or Line 8                         (the "required annual payment")
```

The required annual payment splits into four equal required installments (25% of line 9 each, Part III line 10) under the regular method. If the payments credited to an installment fall short of it, that installment is underpaid.

### Step 4 — Allocate withholding across quarters

Default (under IRC §6654(g)(1)): treat total annual withholding as paid evenly — $W ÷ 4 per quarter — *unless* the filer elects actual-date treatment. For most filers (steady W-2 income), even allocation is correct.

Even allocation usually helps when withholding is concentrated late in the year (a Q4 bonus). If withholding was concentrated early (e.g., a large bonus in January), actual-date treatment may lower the penalty. To use it, check box D in Part II, enter withholding in Part III line 11 by the dates it was actually withheld, and attach Form 2210. IRC §6654(g)(2) lets the filer apply this separately to wage withholding and to other withholding.

### Step 5 — Compute underpayments per installment (Part III, Section A, lines 10–18)

Work one column at a time, (a) through (d):

```
Line 10 = required installment (25% of line 9, or Schedule AI line 27 if box C)
Line 11 = payments in the column's window: withholding (1/4 per column unless box D),
          estimated payments made through 4/15, after 4/15 through 6/15, after 6/15
          through 9/15, after 9/15 through 1/15 (mailed payments: postmark date),
          prior-year overpayment applied (generally treated as paid 4/15)
Line 12 = line 18 (overpayment) of the previous column
Line 13 = line 11 + line 12
Line 14 = lines 16 + 17 of the previous column (earlier underpayment still unpaid)
Line 15 = line 13 − line 14 (zero or less → 0; column (a): line 11)
Line 16 = if line 15 is zero, line 14 − line 13; otherwise 0
Line 17 = underpayment: line 10 − line 15 if line 10 ≥ line 15
Line 18 = overpayment: line 15 − line 10 if line 15 > line 10
```

Payments are applied first to the earliest unpaid installment, even if the filer designated them for a later period (IRC §6654(b)(3)). A late payment therefore stops the penalty on the oldest underpayment first. If the return is filed and the full balance paid by January 31 of the following year, the amount paid with the return goes on line 11, column (d), and there is no penalty for the January 15 installment (IRC §6654(h)). If line 11 ≥ line 10 in every column, there is no penalty.

### Step 6 — Apply the penalty rate (Part III, Section B, line 19)

The penalty rate is the **federal short-term rate plus 3 percentage points** (IRC §6621(a)(2)), set for each calendar quarter and published in a revenue ruling (for example, Rev. Rul. 2024-25, IRB 2024-49, set 7% for January–March 2025). The IRS lists every quarter at https://www.irs.gov/payments/quarterly-interest-rates. The §6654 penalty is simple interest: daily compounding does not apply to it (IRC §6622(b)).

The 2025 instructions' penalty worksheet (Worksheet for Form 2210, Part III, Section B) uses **0.07 in all four rate periods**: April 16–June 30, 2025; July 1–September 30, 2025; October 1–December 31, 2025; January 1–April 15, 2026. The IRS table matches: 7% for every quarter of 2025. For 2026 underpayments (2026 Form 2210, filed in 2027) the rates published so far are 7% (Q1), 6% (Q2), 7% (Q3), 7% (Q4); the January–April 2027 rate is not yet published.

For each column's line 17 underpayment, in each rate period:

```
Penalty = underpayment × (days unpaid in the rate period ÷ 365) × rate for that period
days unpaid = from the due date (or start of the rate period) to the date the
              underpayment is paid, or the end of the rate period, whichever is earlier;
              never past April 15 of the following year
```

Table 2 of the 2025 instructions gives full-period day counts (for example, column (a): 76, 92, 92, 105 days). Total penalty = worksheet line 14 = Form 2210 line 19 = Form 1040 line 38.

### Step 7 — If using Schedule AI (annualized method), recompute Step 3 quarter-by-quarter

Schedule AI replaces the "required annual payment ÷ 4" with quarter-specific amounts based on actual cumulative income through each quarter-end. This benefits filers with back-loaded income (Q4 sale, year-end bonus).

The Schedule AI columns:
- Column (a): 1/1 through 3/31 → annualization factor 4
- Column (b): 1/1 through 5/31 → annualization factor 2.4
- Column (c): 1/1 through 8/31 → annualization factor 1.5
- Column (d): 1/1 through 12/31 → annualization factor 1

For each column, compute (2025 Schedule AI line numbers):
1. Line 1: AGI for the period (cumulative from January 1; subtract the deductible half of the period's SE tax)
2. Line 3: annualize: line 1 × annualization amount (line 2)
3. Lines 4–11: subtract the full standard deduction (not prorated) or annualized itemized deductions, and the QBI deduction
4. Line 14: tax on line 13 (OBBBA items not handled elsewhere, such as Schedule 1-A deductions, are adjusted here per the 2025 instructions); line 15: annualized SE tax from Part II (lines 28–36); line 16: other taxes (Additional Medicare Tax, NIIT, AMT); line 18: credits
5. Line 21: line 19 (annualized tax) × the applicable percentage (22.5% / 45% / 67.5% / 90%). There is no step that divides the annualized tax back down: the applicable percentages already do that.
6. Lines 22–27: line 23 = line 21 minus installments in earlier columns; line 26 = the regular 25% installment plus any unused regular amount carried from the previous column; line 27 = the smaller of line 23 or line 26, entered on Part III line 10.

If Schedule AI is used for any due date, it is used for all of them (2025 instructions). Line 27 still picks the smaller of the annualized installment or the regular installment in each column, and any reduction is recaptured in later columns through lines 23–26 (IRC §6654(d)(2)(A)(ii)). Compute both methods and compare the total penalty.

See `references/annualized-income-method.md` for the full Schedule AI worksheet structure.

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State next steps:

- **If no penalty (safe harbor met)**: no Form 2210 to file; one-line confirmation in the return file
- **If penalty + filer chose IRS-computes**: leave Form 1040 line 38 blank (Form 1040 instructions); IRS bills after processing
- **If penalty + Form 2210 filed**: Form 2210 attached to Form 1040, penalty amount enters Form 1040 Line 38
- **For next year**: based on this year's experience, recommend updated Form W-4 (extra withholding), updated quarterly estimates via Form 1040-ES, or both. The goal is to land within the safe harbor next year.

### Step 11 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains the FFFF / paid software / paper decision tree and field-by-field mapping for Form 2210 specifically. If the user only wants a draft and will file themselves, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Required Annual Payment

Determines whether a penalty is even possible by checking the safe harbors.

| Line | What goes here |
|------|----------------|
| 1 | 2025 Form 1040 line 22 (tax after credits) |
| 2 | Other taxes: Schedule 2 lines 4, 8 (additional tax on distributions only), 9, 11, 12, 14, 15, 16, 17a, 17c–17j, 17l, 17z, and 19 |
| 3 | Other payments and refundable credits, in parentheses (EIC, ACTC, refundable AOTC, refundable adoption credit, PTC, fuel tax credit, §1341 credit; 75% of the §1062 farmland net tax liability under Notice 2026-3) |
| 4 | Lines 1 + 2 − 3 (current-year tax). If less than $1,000, stop: no penalty |
| 5 | Line 4 × 90% |
| 6 | Withholding: Form 1040 line 25d plus Schedule 3 line 11. No estimated payments |
| 7 | Line 4 − Line 6. If less than $1,000, stop: no penalty |
| 8 | Maximum required annual payment based on prior year's tax (100%, or 110% if 2024 AGI > $150,000; $75,000 MFS) |
| 9 | Required annual payment: smaller of line 5 or line 8 |

(Verified against the 2025 Form 2210 and its instructions; re-check the 2026 revision before use.)

### Part II — Reasons for Filing

Five boxes. If none applies, don't file Form 2210.

- **Box A**: waiver of the **entire** penalty. File page 1 only; the penalty is not figured
- **Box B**: waiver of **part** of the penalty. Figure the penalty, enter the waived amount in parentheses next to line 19, file Form 2210
- **Box C**: annualized income installment method (Schedule AI). Figure the penalty, file Form 2210
- **Box D**: withholding treated as paid on the dates actually withheld. Figure the penalty, file Form 2210
- **Box E**: joint return for 2024 or 2025 but not both, and line 8 is smaller than line 5. File page 1 only

Waiver grounds (IRC §6654(e)(3)): the filer retired after reaching age 62 or became disabled in 2024 or 2025 and the underpayment was due to reasonable cause; or the underpayment was due to a casualty, disaster, or other unusual circumstance. Attach a statement and documentation (retirement date and age, disability date, police or insurance reports). For federally declared disasters the IRS applies relief automatically by county; generally don't file Form 2210 for that, except to use Schedule AI.

### Part III — Penalty Computation

There is no short method on the current form. Section A (lines 10–18) figures the underpayment per column; Section B (line 19) takes the total from the penalty worksheet in the instructions:

```
Each column (a)–(d):
  Line 10 = 25% of line 9 (or Schedule AI line 27)
  Line 11 = withholding (1/4 per column unless box D) + estimated tax paid in the window
  Lines 12–16 = carry earlier overpayments forward and apply payments to earlier underpayments first
  Line 17 = underpayment for the column
Penalty worksheet: line 17 × days unpaid ÷ 365 × rate, per rate period (0.07 in all four 2025 periods)
Line 19 = worksheet line 14 → Form 1040 line 38
```

### Schedule AI — Annualized Income Installment Method

Quarter-by-quarter recomputation of required installments based on actual cumulative income. Opt-in. See `references/annualized-income-method.md` for full worksheet structure.

---

## Validation

Run every check. Surface failures — don't silently fix.

### Math checks

- [ ] Line 1 matches Form 1040 line 22; line 4 = lines 1 + 2 − 3
- [ ] Line 5 = Line 4 × 0.90
- [ ] Line 6 (withholding) = Form 1040 line 25d + Schedule 3 line 11 (no estimated payments)
- [ ] Line 7 = Line 4 − Line 6
- [ ] Line 9 (required annual payment) = smaller of Line 5 or Line 8
- [ ] Part III lines 12–18 apply each column's payments to earlier underpayments first; line 17 per column follows that flow
- [ ] Each penalty amount = line 17 underpayment × (days unpaid in the rate period / 365) × rate for that period
- [ ] Total penalty (worksheet line 14) = Form 2210 line 19 = Form 1040 line 38
- [ ] Schedule AI cumulative percentages: 22.5% (Q1), 45% (Q2), 67.5% (Q3), 90% (Q4), applied to the annualized tax with no further division
- [ ] Schedule AI annualization factors: 4 (Q1), 2.4 (Q2), 1.5 (Q3), 1 (Q4)
- [ ] Schedule AI line 27 installments sum to no more than line 9 plus any recapture; line 27 = smaller of line 23 or line 26

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filer used Schedule AI but income was actually fairly even across the year — Schedule AI may not save money; show the regular method too
- [ ] Filer did NOT use Schedule AI but income was clearly uneven (one quarter > 50% of total) — flag that Schedule AI may save money; offer to compute it
- [ ] Filer's withholding alone covers the prior-year safe harbor → no penalty; the agent should confirm before computing the Schedule AI math
- [ ] Filer's prior-year tax was zero AND prior year was a full 12-month return → first-year exception applies; no penalty; no Form 2210
- [ ] Filer paid all quarterly estimates exactly on the due date but used a payment method (paper check) that took 3+ days to clear → confirm the IRS-recorded payment date matches the filer's "paid by" date
- [ ] Penalty < $50 → consider just letting IRS compute and bill; the analytical effort exceeds the dollar value
- [ ] Filer is using prior-year safe harbor (Line 8) but prior-year AGI was > $150K and applied 100% threshold → should be 110%; recompute
- [ ] Filer made a Q4 estimated tax payment on January 15+ to "back-fill" a Q1/Q2/Q3 underpayment — this DOES NOT undo the prior-quarter penalty; it only stops further accrual on the underpaid amount

### Cross-form checks

- [ ] If the filer figured the penalty, Form 1040 line 38 = Form 2210 line 19 (after any box B waiver amount), added to line 37 or subtracted from the overpayment
- [ ] If filer let IRS compute (no Form 2210 attached, or page 1 only with box A or E), Form 1040 line 38 is left blank
- [ ] If filer claims a waiver via Box A or B, the written statement and documentation are attached
- [ ] If next-year planning suggests increased withholding, Form W-4 update should be filed with the employer
- [ ] If next-year planning suggests increased estimated tax, Form 1040-ES voucher schedule should be drafted

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 2210 or paste into tax software. Format:

```markdown
# Form 2210 — DRAFT for tax year YYYY

## Filing decision
- [ ] No Form 2210 needed (safe harbor met or de minimis exception)
- [ ] No Form 2210 — let IRS compute penalty and bill
- [ ] File Form 2210 with regular method
- [ ] File Form 2210 with Schedule AI (annualized income installment method)

## Header
Name(s) shown on return:    <filer name(s)>
Your SSN:                   <SSN>
Filing status:              <Single | HoH | QSS | MFJ | MFS>
Prior-year AGI:             $XXX,XXX  → safe-harbor multiplier: 100% | 110%

## Part I — Required Annual Payment
1. Form 1040 line 22:                               $XX,XXX
2. Other taxes (Schedule 2 lines per instructions): $XXX
3. (Other payments and refundable credits):         ($XXX)
4. Current-year tax (1 + 2 − 3):                    $XX,XXX
5. Line 4 × 90%:                                    $XX,XXX
6. Withholding:                                     $XX,XXX
7. Line 4 − Line 6 (< $1,000 → no penalty):         $XX,XXX
8. Prior-year tax × (100% or 110%):                 $XX,XXX
9. Required annual payment (smaller of 5 or 8):     $XX,XXX

## Part II — Reasons for Filing (check all that apply)
- [ ] Box A: waiver of entire penalty (page 1 only)
- [ ] Box B: waiver of part of the penalty
- [ ] Box C: annualized income installment method (Schedule AI)
- [ ] Box D: withholding treated as paid on actual dates
- [ ] Box E: joint return in only one of the two years, and line 8 < line 5 (page 1 only)
- [ ] None (don't file Form 2210)
Written explanation (box A or B): <attached | N/A>

## Part III, Section A — Underpayment per column

| Line | (a) 4/15 | (b) 6/15 | (c) 9/15 | (d) 1/15 |
|------|----------|----------|----------|----------|
| 10 Required installment | $X | $X | $X | $X |
| 11 Estimated tax paid and tax withheld | $X | $X | $X | $X |
| 12 Overpayment from previous column | | $X | $X | $X |
| 13 Line 11 + 12 | | $X | $X | $X |
| 14 Lines 16 + 17 of previous column | | $X | $X | $X |
| 15 Line 13 − 14 | $X | $X | $X | $X |
| 16 Line 14 − 13 if line 15 is zero | | $X | $X | $X |
| 17 Underpayment | $X | $X | $X | $X |
| 18 Overpayment | $X | $X | $X | |

## Part III, Section B — Penalty worksheet

| Column | Underpayment (line 17) | Paid on | Days by rate period | Rate | Penalty |
|--------|------------------------|---------|---------------------|------|---------|
| (a)    | $X                     | date    | XX / XX / XX / XX   | 7%   | $XX     |
| (b)    | $X                     | date    | XX / XX / XX        | 7%   | $XX     |
| (c)    | $X                     | date    | XX / XX             | 7%   | $XX     |
| (d)    | $X                     | date    | XX                  | 7%   | $XX     |
| **Line 19 total penalty** |     |         |                     |      | **$XXX** |

## Schedule AI — Annualized Income Installment Method (if used)
(See references/annualized-income-method.md for full worksheet)
(a) AGI 1/1–3/31:   $XX,XXX → line 21 $X,XXX, line 23 $X,XXX, line 26 $X,XXX → line 27 $X,XXX
(b) AGI 1/1–5/31:   $XX,XXX → line 21 $X,XXX, line 23 $X,XXX, line 26 $X,XXX → line 27 $X,XXX
(c) AGI 1/1–8/31:   $XX,XXX → line 21 $X,XXX, line 23 $X,XXX, line 26 $X,XXX → line 27 $X,XXX
(d) AGI 1/1–12/31:  $XX,XXX → line 21 $X,XXX, line 23 $X,XXX, line 26 $X,XXX → line 27 $X,XXX

Schedule AI total penalty:                                   $XXX
Regular method total penalty:                                $XXX
Method chosen (lower):                                       <Schedule AI | regular>

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Filing decision: <see top — Form 2210 needed and chosen method>
- Penalty: $XXX (or $0 if safe harbor met)
- Next steps:
  - <handoff items from Step 10>
  - <updated Form W-4 / Form 1040-ES recommendation for next year>

## Sources cited in this draft
- IRS Form 2210 (revision date YYYY-MM-DD)
- IRS Instructions for Form 2210 (revision date YYYY-MM-DD)
- IRC §6654 (estimated tax penalty for individuals)
- IRC §6654(e)(1) ($1,000 de minimis)
- IRC §6654(e)(2) (no prior-year tax liability)
- IRC §6654(d)(1)(B), (C) (90% / 100% / 110% required annual payment)
- IRC §6654(g)(1) (withholding allocated evenly across quarters by default)
- IRC §6621(a)(2), §6622(b) (rate; no daily compounding)
- IRS quarterly interest rates page or Revenue Ruling YYYY-XX (penalty rate for each rate period)
- (any other authority used)
```

Show every line, including zeros. The deliverable is a starting point — the user still has to enter it into Form 1040 e-file software or paper Form 2210.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 2210 line with examples and edge cases
- [`references/safe-harbors.md`](./references/safe-harbors.md) — The 90% / 100% / 110% rules under IRC §6654(d), with worked safe-harbor examples
- [`references/annualized-income-method.md`](./references/annualized-income-method.md) — Schedule AI worksheet, annualization factors, when it saves penalty
- [`references/penalty-rates.md`](./references/penalty-rates.md) — How the penalty rate is set (federal short-term rate + 3 points), 2025–2026 rates, where to look up the current-quarter rate
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 2210 alongside Form 1040 via FFFF, paper, or generic tax software

## Examples

End-to-end worked Form 2210 drafts. Use these as patterns when the user's situation is similar.

- [`examples/w2-plus-side-gig.md`](./examples/w2-plus-side-gig.md) — W-2 employee with under-withheld side-gig income; analyzes 90% / 100% safe harbor; minimal penalty
- [`examples/freelancer-uneven-income.md`](./examples/freelancer-uneven-income.md) — Freelancer with $0 Q1, $80K Q4; Schedule AI lowers the penalty from about $197 to about $161 because the low prior-year safe harbor already caps the regular installments
- [`examples/retiree-roth-conversion.md`](./examples/retiree-roth-conversion.md) — Retirees with steady SS + IRA distributions + large Q4 Roth conversion; elected withholding on the conversion meets the prior-year safe harbor; without it, Schedule AI cuts the penalty from about $382 to about $162

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf) — the form itself
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf) — line-by-line IRS guidance, current-year penalty rate table
- [About Form 2210](https://www.irs.gov/forms-pubs/about-form-2210) — IRS landing page with archive of past revisions
- [Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) — Estimated Tax for Individuals (the quarterly voucher; companion to Form 2210)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (the 2026 edition covers withholding and estimated tax; for the penalty and Schedule AI it points to the Instructions for Form 2210)
- [Quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) — underpayment rate for each calendar quarter (2025: 7% all quarters; 2026: 7%, 6%, 7%, 7%)
- [Understanding your CP30 notice](https://www.irs.gov/individuals/understanding-your-cp30-notice) — the IRS notice for an estimated tax penalty
- [Estimated Tax Penalty 2026: How to Avoid It and What to Do If You Owe](https://jupid.com/blog/estimated-tax-penalty-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 843](https://www.irs.gov/pub/irs-pdf/f843.pdf) — Claim for Refund and Request for Abatement (used for after-the-fact penalty waiver requests on already-paid penalties)
- IRC §6654 — Failure by individual to pay estimated income tax
- IRC §6654(b)(3) — Payments credited to the earliest unpaid installment
- IRC §6654(d)(1)(B) — Required annual payment: 90% of current-year tax or 100% of prior-year tax
- IRC §6654(d)(1)(C) — Higher-AGI 110% safe harbor for filers with prior-year AGI > $150K
- IRC §6654(d)(2) — Annualized income installment, recapture of reductions
- IRC §6654(e)(1) — $1,000 de minimis exception
- IRC §6654(e)(2) — No prior-year tax liability exception
- IRC §6654(e)(3) — Waivers (casualty, disaster, unusual circumstances; retired after 62 or disabled)
- IRC §6654(g)(1) — Withholding allocated equally across quarters unless actual dates are established
- IRC §6654(h) — No penalty for the 4th installment if the return is filed and tax paid by January 31
- IRC §6621(a)(2), (b) — Underpayment rate (federal short-term rate + 3 points), set each calendar quarter
- IRC §6622(b) — Daily compounding does not apply to the §6654 penalty

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and IRC sections. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations — multi-state residency, retroactive payments, partial waiver claims, fiscal-year filers — warrant a licensed tax professional's review.
