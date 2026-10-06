---
name: form-940
description: >
  Use this skill when an employer (sole proprietor, single-member LLC, partnership,
  S corporation, C corporation, or other business with W-2 employees) must prepare
  Form 940, the Employer's Annual Federal Unemployment (FUTA) Tax Return, including
  Schedule A (Form 940) for multi-state employers and employers in a credit
  reduction state. Triggers on phrases like "Form 940", "FUTA return", "federal
  unemployment tax", "FUTA tax due", "Schedule A Form 940", "credit reduction state",
  "California FUTA credit reduction", "FUTA deposit", "$7,000 FUTA wage base",
  "S-corp FUTA", "amend Form 940", "late state unemployment tax FUTA credit".
  Do NOT use for: household employers reporting a nanny or housekeeper on their
  Form 1040 — use schedule-h; Social Security, Medicare, and income tax withholding
  returns — use form-941; state unemployment (SUTA) wage reports — state forms, out
  of scope; agricultural employers' Form 943; aggregate filers (section 3504 agents,
  CPEOs) who need Schedule R (Form 940); independent contractor payments — use
  form-1099-nec.
form: Form 940 (Employer's Annual Federal Unemployment (FUTA) Tax Return)
audience: [employer, llc1, llcm, partnership, scorp, ccorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f940.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i940.pdf
---

# Form 940 — Employer's Annual Federal Unemployment (FUTA) Tax Return

This skill produces an audit-grade draft of Form 940 and, when needed, Schedule A (Form 940) from a year of payroll records: total payments, FUTA-exempt payments, each employee's excess over the $7,000 wage base, the state unemployment credit, any credit reduction, deposits, and the quarterly liability schedule. The arithmetic is short. The judgment sits in four places: which payments are exempt on line 4, whether state unemployment tax was paid on time and on the same wages (line 9 or the line 10 worksheet), whether a credit reduction state applies (line 11 and Schedule A), and whether the $500 deposit rule was met each quarter. The agent asks when any of those facts is missing.

**Revision verified.** The line map was built from the text of the **2025 Form 940** (Created 6/2/25; filed in 2026), the **2025 Instructions for Form 940** (dated Nov 18, 2025), and the **2025 Schedule A (Form 940)** (Created 11/12/25). It was compared against the **2026 draft Form 940** (Created 3/25/26), **2026 draft Schedule A** (Created 3/18/26), and **2026 draft instructions** (dated Sep 22, 2026): line numbers and line wording are unchanged. The 2026 final form, final instructions, and final 2026 credit reduction rates must be re-checked before use at [About Form 940](https://www.irs.gov/forms-pubs/about-form-940) and IRS.gov/DraftForms.

**Companion guide for end users:** [Form 940 Instructions 2026: FUTA Line by Line, FUTA vs SUTA vs FICA, and Credit Reduction States](https://jupid.com/blog/form-940-instructions-futa-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when any of the following is true:

- The user names Form 940, Schedule A (Form 940), FUTA, or federal unemployment tax.
- The user has W-2 employees and asks what is due in January or February for the prior year's unemployment tax.
- The user operates in California or the U.S. Virgin Islands (credit reduction jurisdictions on the 2025 Schedule A) and asks why FUTA is more than $42 per employee.
- The user paid state unemployment tax late, or the state excluded some wages (for example corporate officers), and asks how that changes FUTA.
- The user runs an S corporation and pays the shareholder-officer a salary.
- The user needs to amend a filed Form 940 (there is no Form 940-X; the same year's form is used with box a checked).

Do not engage, and route instead, when:

- The employer only has household employees (nanny, housekeeper, caregiver) and reports them on Form 1040 → [`../schedule-h/SKILL.md`](../schedule-h/SKILL.md). The Instructions for Form 940 say household employers generally file Schedule H instead of Form 940.
- The user asks about Social Security, Medicare, or withheld income tax → [`../form-941/SKILL.md`](../form-941/SKILL.md).
- The user only pays independent contractors → no Form 940; [`../form-1099-nec/SKILL.md`](../form-1099-nec/SKILL.md).
- The user needs an EIN before filing → [`../form-ss-4/SKILL.md`](../form-ss-4/SKILL.md).
- The user wants penalty abatement → [`../form-843/SKILL.md`](../form-843/SKILL.md) (the Form 940 instructions say not to request abatement on Form 940).
- The filer is a section 3504 agent or CPEO filing an aggregate return with Schedule R (Form 940), an agricultural employer, a 501(c)(3) organization, a state or local government, or a tribal government employer → state that this skill does not cover it and recommend a payroll professional.

Boundary with Schedule H: an employer that has business employees and household employees may report the household employees' FUTA on Form 940 instead of Schedule H, but then must also report their Social Security, Medicare, and withheld income tax on Form 941, 943, or 944 (Instructions for Form 940, "For Employers of Household Employees"; Pub. 926, "Payment option for business employers"). Ask which route the user wants before including household wages on line 3.

---

## Prerequisites

Collect these inputs before drafting. If any is missing, ask the question shown and stop until the user answers.

1. **Tax year.** "Which calendar year is this Form 940 for?" Due dates, credit reduction rates, and the dependent care exclusion limit depend on it.
2. **Filing requirement facts.** "In this year or the prior year, did you pay $1,500 or more of wages in any calendar quarter, or have at least one employee on some part of a day in 20 or more different weeks?" (Instructions for Form 940, "Who Must File Form 940?"; IRC §3306(a)(1)). Do not count partners of a partnership.
3. **Entity identity.** Legal name exactly as on the EIN application (Form SS-4), trade name, EIN, address. A disregarded single-member LLC files under its own name and EIN, not the owner's. Never accept an SSN in the EIN field.
4. **Type of return.** Amended, successor employer, no payments to employees this year, or final return. Ask each one explicitly.
5. **Per-employee annual payments**, by calendar quarter: wages, bonuses, commissions, taxable fringe benefits, reported tips of $20 or more a month, and employer-paid benefits (health plan contributions, employer retirement contributions, dependent care). A payroll register export is the best source.
6. **Exempt payment detail** for line 4, by type (fringe benefits, group-term life, retirement/pension, dependent care, other). Ask: "Which of these amounts are employer health plan contributions, employer 401(k) or SIMPLE contributions (not employee deferrals), dependent care assistance, or payments to your spouse, parent, or child under 21?"
7. **States.** Every state where state unemployment tax was required, and whether any is a credit reduction state for the year.
8. **State unemployment payments.** For each state: assigned experience rate(s) and rate periods, taxable state unemployment wages, contributions paid by the Form 940 due date, contributions paid after it, and contributions still unpaid. Exclude penalties, interest, special administrative taxes, voluntary contributions, and amounts withheld from employees (Instructions for Form 940, "Credit for State Unemployment Tax Paid to a State Unemployment Fund").
9. **Wages excluded from state unemployment tax.** "Did your state exclude any wages from unemployment tax, for example corporate officer wages?" Do not assume; this varies by state.
10. **FUTA deposits** made during the year (date and amount, EFTPS or IRS Direct Pay confirmation), plus any prior-year overpayment applied.
11. **Successor employer facts**, if the business was acquired during the year: predecessor's wages to continuing employees and whether the predecessor was required to file Form 940.

For S corporations, also ask:

- The shareholder-officer's W-2 wages, and whether health insurance premiums for a more-than-2% shareholder were included in W-2 box 1. Those premiums are excluded from FUTA wages (Pub. 15 (2026), section 5, "Health insurance plans"; Announcement 92-16) and belong on line 4.
- Whether the state taxed the officer's wages for unemployment purposes.
- Shareholder distributions are not wages and never go on line 3 (Pub. 15 (2026), section 15 table, "Officers or shareholders of an S corporation"). Reasonable-compensation judgments are out of scope; refer to a CPA.

For a household employer who also has a business, ask: "Do you want to report your household employee on your business payroll (Form 941 or 944 plus Form 940), or on Schedule H with your Form 1040?"

---

## Workflow

Execute in order.

### Step 1 — Confirm the filer and the filing requirement

Apply the $1,500-per-quarter or 20-weeks test for the current and prior year. If neither is met and the user has no other reason to file, say so and stop. If the user made no payments to employees this year but must file (test met last year), the return is box c: sign Part 7 and file (Instructions for Form 940, "Type of Return").

### Step 2 — Build the per-employee table

```
| Employee | Q1 pay | Q2 pay | Q3 pay | Q4 pay | Total pay (line 3) | Exempt (line 4, by box) | Excess over $7,000 (line 5) | FUTA wages by quarter |
```

FUTA wages for an employee are the first $7,000 of payments after removing exempt payments, assigned to the quarters in which they were paid (Instructions for Form 940, "How Do You Figure Your FUTA Tax Liability for Each Quarter?").

### Step 3 — Part 1 (lines 1a, 1b, 2)

One state → two-letter code on line 1a. More than one state → check 1b and complete Schedule A. Wages in a credit reduction state → check line 2 and complete Schedule A. Complete line 1a or 1b even when the state rate was 0%.

### Step 4 — Part 2 (lines 3–8)

Line 3 = all payments for employee services. Line 4 = only exempt payments already included on line 3, with boxes 4a–4e checked. Line 5 = sum of each employee's payments above $7,000 after removing that employee's line 4 amounts. Line 6 = 4 + 5. Line 7 = 3 − 6. Line 8 = line 7 × 0.006.

### Step 5 — Part 3 adjustments (lines 9–11)

- All taxable FUTA wages excluded from state unemployment tax → line 9 = line 7 × 0.054; lines 10 and 11 stay blank. A 0% assigned state rate is not an exclusion.
- Some wages excluded, or any state tax paid after the Form 940 due date → run the line 10 worksheet in [`references/state-credit-line-9-10.md`](./references/state-credit-line-9-10.md); enter worksheet line 7 on line 10. Keep the worksheet; do not attach it.
- Credit reduction state wages → build Schedule A per [`references/credit-reduction-schedule-a.md`](./references/credit-reduction-schedule-a.md); total goes on line 11. If the final rates for the year are not yet published (2026 rates follow the Department of Labor's November 2026 determination), stop and tell the user the draft cannot be finished; never use the DOL "potential" rates.
- Multi-state employer with no credit reduction state → still check line 1b and list every state on Schedule A; line 11 stays blank.

### Step 6 — Part 4 (lines 12–15)

Line 12 = 8 + 9 + 10 + 11. Line 13 = FUTA deposited for the year, including a prior-year overpayment applied. Line 14 or line 15a, never both. Ask the refund-or-apply question for line 15b and collect direct deposit details only if the user wants a refund.

### Step 7 — Part 5 (lines 16a–17)

Only if line 12 is more than $500. Enter liability incurred per quarter, not deposits; leave a zero quarter blank. Figure 16d as line 17 minus (16a + 16b + 16c), with line 17 copied from line 12. Credit reduction amounts are recorded as fourth-quarter liability. Check each quarter against the deposit rule in [`references/deposits-and-due-dates.md`](./references/deposits-and-due-dates.md) and flag any deposit that was due and not made.

### Step 8 — Parts 6 and 7

Ask whether the user wants a third-party designee (a named person, phone, and a five-digit PIN the designee picks). Identify the signer allowed for the entity type.

### Step 9 — Validate

Run every check in **Validation**. Surface failures; do not silently fix.

### Step 10 — Produce the deliverable

Use **Output format**. Show every line, with blanks shown as "blank" so the reviewer sees the line was considered.

### Step 11 — Hand off

State the due date, the payment route, attachments (Schedule A), and related obligations: Forms 941 or 944 for the same wages, W-2/W-3, and the state's own unemployment reports.

### Step 12 — File (only if the user authorizes it)

Follow [`filing.md`](./filing.md): channel decision tree, mailing addresses, signature options, consent and security rules.

---

## Line-by-line guidance

The full map from the PDF text is in [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

### Key figures (year-dependent; re-verify each year)

| Item | 2025 return | 2026 return | Source |
|---|---|---|---|
| FUTA rate / maximum credit / net rate | 6.0% / 5.4% / 0.6% | Same | I940 "How Do You Figure Your FUTA Tax Liability"; Pub. 15 (2026) §14; IRC §3301, §3302 |
| Wage base per employee | $7,000 | $7,000 | I940; IRC §3306(b)(1) |
| Filing test (general) | $1,500 in a quarter or 20 weeks, in 2024 or 2025 | Same test, 2025 or 2026 | I940; Pub. 15 (2026) §14 |
| Household FUTA test | $1,000 cash in a quarter of 2024 or 2025 | 2025 or 2026 | I940; Pub. 15 (2026) §14 |
| Deposit trigger | Cumulative liability over $500 | Same | I940; Treas. Reg. §31.6302(c)-3 |
| Form 940 due date | Feb 2, 2026 (Feb 10 if all FUTA deposited when due) | Feb 1, 2027 (Feb 10, 2027) | I940; I940 2026 draft |
| Credit reduction | CA 0.012, VI 0.045 | Pending; DOL potential list: CA 0.015 + est. 0.038 add-on, VI 0.048 | Schedule A 2025 p. 2; DOL potential 2026 list |
| Dependent care exclusion (line 4d) | $5,000 ($2,500 MFS) | $7,500 ($3,750 MFS) | I940 line 4; I940 2026 draft |
| Late state tax credit | 90% of the credit timely payment would earn | Same | I940 worksheet line 5d; IRC §3302(a)(3) |

### Header and type of return

- EIN, legal name (as used on Form SS-4), trade name, address; name and EIN also go at the top of page 2.
- Boxes: a. Amended; b. Successor employer; c. No payments to employees in the year; d. Final: business closed or stopped paying wages. More than one box may apply. A final return needs an attached statement naming who keeps the payroll records and where.
- "Aggregate Return Filers Only" (section 3504 agent, CPEO, other third party): leave blank for an ordinary employer.

### Part 1

| Line | Entry | Rule |
|---|---|---|
| 1a | Two-letter state code | One state only; required even at a 0% rate |
| 1b | Checkbox | More than one state; attach Schedule A |
| 2 | Checkbox | Wages paid in a credit reduction state; attach Schedule A |

### Part 2

| Line | Entry | Rule |
|---|---|---|
| 3 | Total payments to all employees | Includes taxable and exempt payments: wages, bonuses, vacation pay, sick pay, value of goods and lodging, section 125 benefits, employer 401(k), Archer MSA, adoption assistance, SIMPLE contributions, nonqualified deferred comp, reported tips of $20+ a month, predecessor payments (successor), payments to nonemployees the state treats as employees |
| 4 | Exempt payments, boxes 4a–4e | Only if already on line 3. 4a fringe benefits (certain meals and lodging, accident or health plan contributions incl. certain HSA/Archer MSA, section 125 benefits); 4b group-term life; 4c retirement/pension (employer qualified-plan contributions, not elective deferrals); 4d dependent care ($5,000 per employee, $2,500 MFS for 2025; $7,500 / $3,750 per the 2026 draft instructions); 4e other (workers' comp, H-2A and certain agricultural pay, household pay reported on Schedule H, services by your parent, spouse, or child under 21, certain fishing, certain statutory employees, nonemployees treated as employees by the state) |
| 5 | Excess over $7,000 | Per employee, after removing that employee's line 4 amounts |
| 6 | Line 4 + line 5 | |
| 7 | Line 3 − line 6 | Total taxable FUTA wages |
| 8 | Line 7 × 0.006 | Assumes the full 5.4% credit |

Moving expense and bicycle commuting reimbursements are not exempt and never go on line 4 (Instructions for Form 940, Reminders; P.L. 119-21 made the elimination permanent after 2025).

### Part 3

| Line | Entry | Rule |
|---|---|---|
| 9 | Line 7 × 0.054 | Only if ALL taxable FUTA wages were excluded from state unemployment tax; then skip to line 12 |
| 10 | Worksheet line 7 | SOME wages excluded, or ANY state tax paid after the Form 940 due date |
| 11 | Schedule A total | Credit reduction; skip if line 9 was used |

### Part 4

| Line | Entry | Rule |
|---|---|---|
| 12 | 8 + 9 + 10 + 11 | Total FUTA tax after adjustments |
| 13 | FUTA deposited | Includes prior-year overpayment applied |
| 14 | 12 − 13 if positive | More than $500 must be deposited; $500 or less may be paid with the return; under $1 is not paid |
| 15a | 13 − 12 if positive | |
| 15b | Apply to next return / Send a refund | Neither or both checked → applied to next return |
| 15c–15e | Routing (9 digits, starts 01–12 or 21–32), checking or savings, account (up to 17 characters) | Refunds are issued by direct deposit |

### Part 5

Lines 16a–16d (quarterly liability) and line 17 (total, must equal line 12), only when line 12 is more than $500.

### Parts 6 and 7

Designee name, phone, five-digit PIN; the authorization expires one year after the Form 940 due date. Signers: sole proprietor (owner); partnership or LLC taxed as one (responsible partner, member, or officer); corporation or LLC taxed as one (president, vice president, or other principal officer); disregarded single-member LLC (owner or principal officer); trust or estate (fiduciary); or an agent with a valid power of attorney or Form 8655. A paid preparer signs the preparer block and enters a PTIN.

### Entry format

Enter dollars and cents without dollar signs, or round every entry to whole dollars (drop under 50 cents, raise 50–99 cents). Leave zero lines blank (Instructions for Form 940, "Completing Your Form 940").

---

## Validation

### Math checks

- [ ] Line 3 = sum of every employee's total payments in the per-employee table
- [ ] Line 4 ≤ line 3, and each line 4 amount is also inside line 3
- [ ] Line 5 = Σ max(0, employee payments − employee exempt payments − $7,000)
- [ ] Line 6 = line 4 + line 5; line 7 = line 3 − line 6
- [ ] Line 7 = Σ min($7,000, employee payments − employee exempt payments) (independent recomputation)
- [ ] Line 8 = line 7 × 0.006 (to the cent, or whole dollars if rounding)
- [ ] If line 9 > 0: line 9 = line 7 × 0.054, and lines 10 and 11 are blank
- [ ] If line 10 > 0: worksheet line 7 = worksheet line 1 − worksheet line 6, and worksheet line 1 = line 7 × 0.054
- [ ] Line 11 = Schedule A total credit reduction
- [ ] Line 12 = 8 + 9 + 10 + 11
- [ ] Only one of line 14 or line 15a has an amount
- [ ] If line 12 > $500: 16a + 16b + 16c + 16d = line 17 = line 12
- [ ] Sum of quarterly FUTA wages (Part 5 basis) = line 7

### Sanity checks (warn, do not block)

- [ ] Line 7 ÷ number of employees > $7,000 → impossible; recheck line 5
- [ ] Line 8 > $42 × number of employees paid during the year → recheck
- [ ] An employee's elective 401(k) deferral appears on line 4 → remove; only employer contributions go on 4c
- [ ] Lines 1a and 1b both blank, line 9 blank, and line 7 > 0 → the instructions require a state on 1a/1b, or line 9 when all wages were excluded from state tax
- [ ] State is CA or VI (2025) and line 2 is unchecked → Schedule A missing
- [ ] Line 14 > $500 → a deposit was required; FTD penalty risk; deposit through EFT rather than paying with the return
- [ ] Any quarter where cumulative undeposited liability exceeded $500 with no deposit by the last day of the following month → FTD penalty risk
- [ ] Line 10 > 0 → confirm the user understands the late or excluded wages; ask if state payments after the due date could still be made (90% credit)
- [ ] Household employee wages on line 3 while the user also files Schedule H → double reporting; pick one route
- [ ] S corporation: line 3 includes shareholder distributions → remove
- [ ] Box c checked but line 3 > 0 → contradiction

### Cross-form checks

- [ ] EIN and legal name match Forms 941, W-2, W-3
- [ ] Line 3 is reconcilable to Forms 941 line 2 totals plus pre-tax amounts that reduce income tax wages (differences must be explainable)
- [ ] Each state on Schedule A matches a state unemployment account the user actually holds

---

## Output format

```markdown
# Form 940 — DRAFT for tax year YYYY

Form revision used: Form 940 (YYYY), Created M/D/YY; Instructions for Form 940 (YYYY)

## Header
EIN: XX-XXXXXXX
Name (not trade name): <legal name>
Trade name: <or blank>
Address: <street, city, state, ZIP>
Type of return: [ ] a. Amended  [ ] b. Successor employer  [ ] c. No payments to employees  [ ] d. Final
Aggregate Return Filers Only: blank

## Part 1
1a. State (one state only): XX | blank
1b. Multi-state employer: [ ] (Schedule A attached)
2.  Credit reduction state wages: [ ] (Schedule A attached)

## Part 2
3. Total payments to all employees:            $X,XXX.XX
4. Payments exempt from FUTA tax:              $X,XXX.XX   [ ]4a [ ]4b [ ]4c [ ]4d [ ]4e
5. Payments in excess of $7,000:               $X,XXX.XX
6. Subtotal (4 + 5):                           $X,XXX.XX
7. Total taxable FUTA wages (3 − 6):           $X,XXX.XX
8. FUTA tax before adjustments (7 × 0.006):    $X,XXX.XX

## Part 3
9.  All wages excluded from SUTA (7 × 0.054):  blank | $X
10. Line 10 worksheet result:                  blank | $X
11. Credit reduction (Schedule A total):       blank | $X

## Part 4
12. Total FUTA tax after adjustments:          $X,XXX.XX
13. FUTA tax deposited for the year:           $X,XXX.XX
14. Balance due:                               blank | $X
15a. Overpayment:                              blank | $X
15b. [ ] Apply to next return  [ ] Send a refund
15c–15e. Direct deposit: <only if refund; never echo full account number in logs>

## Part 5 (only if line 12 > $500)
16a. Q1 liability:  $X | blank
16b. Q2 liability:  $X | blank
16c. Q3 liability:  $X | blank
16d. Q4 liability:  $X | blank
17.  Total (= line 12): $X

## Part 6 — Designee: Yes (name, phone, PIN chosen by designee) | No
## Part 7 — Signer: <name, title>; phone; date (signature left to the user)

## Schedule A (if line 1b or 2 checked)
| State | Checked | FUTA taxable wages (credit reduction states only) | Rate | Credit reduction |
| Total credit reduction (= line 11) | | | | $X |

## Supporting schedules (keep, do not attach)
- Per-employee table (payments, exempt, excess, FUTA wages by quarter)
- Line 10 worksheet, if used
- Deposit log (quarter, liability, cumulative undeposited, deposit date, amount)

## Validation summary
- Math: all checks passed | <failures>
- Sanity: <warnings>
- Deposit compliance: <each quarter: required? made on time?>

## Filing
- Due date: <date>; later date <date> available only if every FUTA deposit was made when due
- Payment route: EFT deposit (EFTPS, Direct Pay, business tax account) | with return (only if line 14 ≤ $500)
- Attachments: Schedule A (if applicable); statement for a final return

## Sources cited in this draft
- Form 940 (YYYY) and Instructions for Form 940 (YYYY)
- Schedule A (Form 940) (YYYY) and its instructions
- Pub. 15 (YYYY), sections 3, 5, 11, 12, 14
- IRC §§3301, 3302, 3306; Treas. Reg. §31.6302(c)-3
```

The draft is not a filed return. The user or their provider transcribes it, signs it, and files it.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every Form 940 line and box from the 2025 PDF text, with the 2026 draft differences
- [`references/state-credit-line-9-10.md`](./references/state-credit-line-9-10.md) — the 5.4% credit, "on time" for FUTA purposes, line 9 versus line 10, the line 10 worksheet with the IRS example recomputed
- [`references/credit-reduction-schedule-a.md`](./references/credit-reduction-schedule-a.md) — credit reduction rules, 2025 rates, 2026 status, multi-state Schedule A mechanics
- [`references/deposits-and-due-dates.md`](./references/deposits-and-due-dates.md) — the $500 rule, quarterly liability, Part 5, deposit and filing dates for 2025 and 2026 returns, penalties
- [`references/common-mistakes.md`](./references/common-mistakes.md) — frequent errors with authority and fix
- [`filing.md`](./filing.md) — e-file through a 94x provider, paper addresses, payment voucher, amended returns, consent and security rules

## Examples

- [`examples/texas-landscaper-2026.md`](./examples/texas-landscaper-2026.md) — 14 employees in one state, health and employer 401(k) exemptions, cumulative liability crosses $500 in Q2, Part 5
- [`examples/california-nevada-credit-reduction-2025.md`](./examples/california-nevada-credit-reduction-2025.md) — multi-state employer with a California credit reduction, an employee transferred between states, Schedule A, fourth-quarter deposit
- [`examples/scorp-officer-florida-2025.md`](./examples/scorp-officer-florida-2025.md) — S corporation with a shareholder-officer and one employee, 2% shareholder health insurance on line 4, state tax paid late but before the Form 940 due date, and the line 10 worksheet for two what-if cases

## Sources

Re-verify every source for the tax year being filed.

- [Form 940 (2025)](https://www.irs.gov/pub/irs-pdf/f940.pdf) and [Instructions for Form 940 (2025)](https://www.irs.gov/pub/irs-pdf/i940.pdf)
- [Schedule A (Form 940) (2025)](https://www.irs.gov/pub/irs-pdf/f940sa.pdf), including its page 2 instructions and the 2025 credit reduction rates
- 2026 drafts: [Form 940](https://www.irs.gov/pub/irs-dft/f940--dft.pdf), [Instructions](https://www.irs.gov/pub/irs-dft/i940--dft.pdf), [Schedule A](https://www.irs.gov/pub/irs-dft/f940sa--dft.pdf)
- [About Form 940](https://www.irs.gov/forms-pubs/about-form-940)
- [IRS: FUTA credit reduction](https://www.irs.gov/businesses/small-businesses-self-employed/futa-credit-reduction)
- [U.S. Department of Labor: FUTA credit reductions](https://oui.doleta.gov/unemploy/futa_credit.asp) (historical table and potential 2026 list dated Jan 15, 2026)
- [Publication 15 (2026), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf), sections 2, 3, 5, 11, 12, 14, 15
- [Publication 926 (2026), Household Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p926.pdf) (household employees on business returns)
- [E-file employment tax forms](https://www.irs.gov/businesses/e-file-employment-tax-forms) and [MeF for employment taxes FAQ](https://www.irs.gov/e-file-providers/modernized-e-file-mef-for-employment-taxes-frequently-asked-questions)
- IRC §3301 (6% rate), §3302 (credits; 90% limit for late contributions; credit reduction), §3306(a) (employer tests), §3306(b)(1) ($7,000 wage base), §3306(c)(5) (family employment); Treas. Reg. §31.6302(c)-3 ($500 deposit rule); IRC §6656 (failure to deposit), §6651 (failure to file or pay)
- Announcement 92-16 (2% shareholder health insurance excluded from FUTA wages, as cited in Pub. 15 section 5)
- [Companion guide](https://jupid.com/blog/form-940-instructions-futa-2026) for human readers

## Disclaimer

This skill encodes the mechanics of Form 940 from public IRS forms, instructions, and publications. It is not tax advice and does not create a CPA-client relationship. The agent should tell the user that the draft is a starting point and that multi-state payroll, successor-employer credits, officer exclusions, amended returns, and penalty situations deserve review by a CPA or enrolled agent.
