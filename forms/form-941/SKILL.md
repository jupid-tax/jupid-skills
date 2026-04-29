---
name: form-941
description: >
  Use this skill when an employer (sole proprietor with W-2 employees, single-member
  LLC with payroll, partnership with payroll, S-corp paying shareholder-employee
  reasonable compensation, C-corp, or nonprofit) must file Form 941 — the
  Employer's Quarterly Federal Tax Return — to report federal income tax withheld
  plus the employer and employee shares of FICA (Social Security and Medicare).
  Triggers on phrases like "Form 941", "quarterly payroll tax", "employer payroll
  tax return", "FICA reporting", "withhold federal income tax employees",
  "Schedule B 941", "941 deposit schedule", "S-corp payroll filing", "941-X
  correction". Do NOT use for: agricultural employers (Form 943); annual filers
  who qualified for and elected Form 944 (small employers ≤ $1,000 annual
  liability); household employers (Schedule H attached to Form 1040); state
  payroll tax reporting (state-specific forms); FUTA reporting (Form 940);
  W-2 / W-3 wage statements; 1099-NEC contractor reporting.
form: Form 941 (Employer's Quarterly Federal Tax Return)
audience: [employer, scorp]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f941.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i941.pdf
---

# Form 941 — Employer's Quarterly Federal Tax Return

This skill produces an audit-grade draft of Form 941 from a quarter's payroll data: gross wages, federal income tax withheld, employee and employer FICA, Additional Medicare withheld, sick/family leave (if any), and tax deposits already made. It walks through the form line by line, applies IRS rules, runs validation, and emits a deliverable an employer can transcribe to e-file software or paper.

The math is mechanical once the inputs are correct. The judgment is in *which schedule attaches* (Schedule B for semi-weekly depositors), *whether deposits matched liability* (else Form 945-A), and *when to use 941-X* to fix a prior quarter rather than re-filing. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Payroll Tax Due Dates: Form 941, 940, and Deposits Guide 2026](https://jupid.com/blog/payroll-tax-due-dates-form-941-940-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 941, "quarterly 941", "941 filing", or "941-X"
- The user runs payroll for one or more W-2 employees and is approaching a quarterly due date (April 30, July 31, October 31, January 31)
- The user describes withholding federal income tax from employee paychecks and needs to remit / report it
- An S-corp shareholder-employee is being paid "reasonable compensation" (W-2 wages) and the corporation has not yet filed the quarter's 941
- The user just discovered an error on a previously-filed 941 and asks how to correct it (→ 941-X path)
- The user asks about Schedule B (Form 941) — the daily liability schedule for semi-weekly depositors

Do **not** engage this skill when:

- The user is an agricultural employer paying farmworkers → use Form 943 (separate skill)
- The user qualified for **annual** Form 944 (notified by IRS that annual liability ≤ $1,000) → Form 944 (separate skill). Note: an employer cannot unilaterally pick 944; the IRS assigns it.
- The user is a household employer (nanny, caregiver, household help) → file Schedule H with personal Form 1040 (no 941)
- The user only has 1099 contractors and no W-2 employees → no 941 required
- The user is asking about FUTA (federal unemployment) → Form 940 (separate skill)
- The user is asking about state withholding or state unemployment insurance → state-specific form
- The user needs W-2s / W-3 transmittal at year-end → those go through SSA Business Services Online, not Form 941

If the entity status is ambiguous, ask before proceeding. The most common confusion: a single-member LLC owner who pays themselves "salary" by transferring money from business to personal — that's an owner draw, not W-2 wages. SMLLC owners taxed as disregarded entities cannot put themselves on payroll. They take draws and pay self-employment tax via Schedule SE. Only S-corp / C-corp owners (or LLCs that elected corporate taxation via Form 2553) appear on the company's 941.

For adjacent skills:
- For year-end W-2s and W-3 transmittal → forthcoming `form-w2` skill
- For the parent return (S-corp): see `form-1120-s` (forthcoming)
- For owner self-employment tax (sole prop / SMLLC): see `schedule-c` + Schedule SE

---

## Prerequisites

Before producing anything, the agent must have these eleven inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Quarter and tax year**. Q1 covers Jan–Mar (due Apr 30); Q2 covers Apr–Jun (due Jul 31); Q3 covers Jul–Sep (due Oct 31); Q4 covers Oct–Dec (due Jan 31). Numbers (SS wage base, Additional Medicare threshold) depend on the year.
2. **Employer's legal name and EIN**. Used in the form header. Do not invent. Confirm with the user; an EIN typo can route the deposit to a different employer's account.
3. **Trade name** (DBA) if different from legal name.
4. **Employer's address**. Must match what's on file with the IRS.
5. **Number of employees** who received wages, tips, or other compensation in the pay period that includes March 12, June 12, September 12, or December 12 (Line 1) — the IRS picks the same date each quarter.
6. **Total wages, tips, and other compensation** paid during the quarter (Line 2). Includes taxable fringes, bonuses, commissions, sick pay paid by employer.
7. **Federal income tax withheld** from employee paychecks during the quarter (Line 3). Sum of all Form W-4-driven withholdings.
8. **Wages subject to Social Security tax** (Line 5a) and **Medicare wages** (Line 5c) — these are usually different from Line 2 because:
   - SS wages are capped at the annual wage base ($176,100 for 2025; verify 2026 against [SSA fact sheet](https://www.ssa.gov/oact/cola/cbb.html))
   - Some pretax deductions (401(k), HSA, Section 125 cafeteria plan) reduce federal income tax wages but not FICA wages — or vice versa
9. **Wages subject to Additional Medicare Tax** (Line 5d) — wages paid to any employee exceeding $200,000 in the calendar year. The 0.9% additional withholding starts at $200K regardless of filing status (IRC §3101(b)(2)).
10. **Total tax deposits made during the quarter** (Line 13) — federal tax deposits via EFTPS, broken down by deposit date and amount. Required for the depositor reconciliation and (if semi-weekly) Schedule B daily breakdown.
11. **Deposit schedule status** — monthly or semi-weekly. Determined by the lookback period (July 1 of two years ago through June 30 of last year). If total taxes during lookback > $50,000, semi-weekly. Else monthly. New employers default to monthly until lookback data exists. See [`references/deposit-schedules.md`](./references/deposit-schedules.md).

For S-corp filers with shareholder-employees, additionally ask:
- Shareholder-employee gross W-2 wages for the quarter (subset of Line 2)
- Whether reasonable compensation was assessed against IRS factors (industry, role, hours) — out of scope for this skill but worth a documentation reminder
- Whether shareholder distributions (non-wage) were also paid — those don't appear on 941

For employers with sick or family leave wages (rare post-2021):
- Qualified sick leave wages paid (Line 5a(i)) — only if FFCRA / ARPA credits still apply (they expired Sept 30, 2021; carrying into a 2026 quarter is essentially nil unless a retroactive correction)
- Confirm with the user whether they have any such wages — default to zero

For 941-X corrections, additionally ask:
- Which prior quarter is being corrected (year + quarter)
- The error type: under-reported tax (owe more) or over-reported tax (claim refund / abatement)
- Whether the error is administrative (transposition, misclassification) or substantive
- Date the error was discovered (statute of limitations: generally 3 years from filed date or 2 years from paid date, whichever later — IRC §6511)

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filer status

Confirm the user is the employer required to file 941 (not 943 / 944 / Schedule H). Confirm the quarter and year. If the user describes wages from a prior quarter that are already reported, redirect to the 941-X correction path (Step 11).

### Step 2 — Collect and structure payroll data

Build the master payroll table for the quarter:

```
| Employee | Gross Wages | FIT W/H | SS Wages | Medicare Wages | Add'l Medicare | Pretax 401(k) | Pretax §125 |
|----------|-------------|---------|----------|----------------|----------------|---------------|-------------|
| Smith    | $25,000     | $3,200  | $25,000  | $25,000        | $0             | $1,500        | $300        |
| ...      |             |         |          |                |                |               |             |
| TOTALS   | $X          | $X      | $X       | $X             | $X             | $X            | $X          |
```

The TOTALS row drives Lines 2, 3, 5a, 5c, 5d.

Watch for SS wage base cap: any employee whose YTD SS wages reach $176,100 (2025; verify 2026) stops accruing SS wages mid-year. Their SS wages on Line 5a for that quarter equal the *remaining headroom*, not their gross wages.

### Step 3 — Compute FICA on Line 5

- **Line 5a column 1** = SS wages this quarter
- **Line 5a column 2** = Line 5a column 1 × 0.124 (combined 6.2% employer + 6.2% employee)
- **Line 5b column 1** = Tips subject to SS (rare unless tipped industry); column 2 = × 0.124
- **Line 5c column 1** = Medicare wages (no cap)
- **Line 5c column 2** = Line 5c column 1 × 0.029 (combined 1.45% × 2)
- **Line 5d column 1** = Additional Medicare wages (employee comp > $200K YTD)
- **Line 5d column 2** = Line 5d column 1 × 0.009 (employee-only 0.9%; employer does not match)
- **Line 5e** = sum of column 2 amounts (5a + 5b + 5c + 5d)

Cite IRC §3101 (employee FICA), §3111 (employer FICA), §3101(b)(2) (Additional Medicare).

### Step 4 — Compute Line 6 (total taxes before adjustments)

```
Line 6 = Line 3 (FIT withheld) + Line 5e (total FICA) + Line 5f (Section 3121(q) Notice & Demand, if any)
```

Line 5f is rare — only when the IRS issued a Section 3121(q) Notice and Demand for unreported tip taxes. Default to zero unless user provides.

### Step 5 — Apply Lines 7–9 adjustments

- **Line 7** — Current quarter adjustment for fractions of cents (rounding mismatch between per-paycheck FICA and quarterly aggregate). Usually within ±$1 per quarter. If your payroll system rounds cents inconsistently, this adjusts.
- **Line 8** — Adjustment for sick pay paid by a third party (insurance carrier) where the carrier withheld FICA. Negative entry transfers liability to the carrier.
- **Line 9** — Adjustment for tips and group-term life insurance over $50K coverage paid to former employees.

For most small-employer 941s, Lines 7-9 are all zero. If the user doesn't mention them, set to zero and confirm.

### Step 6 — Compute Line 10 (total taxes after adjustments)

```
Line 10 = Line 6 + Line 7 + Line 8 + Line 9
```

### Step 7 — Apply Lines 11a-11g credits (almost all expired)

Most credits on the 2025 / 2026 941 are residual lines for FFCRA / ARPA sick-leave and family-leave credits, which expired September 30, 2021. For a 2026-quarter filing these are usually zero unless the user is amending a prior quarter via 941-X.

- **Line 11a** — Qualified small business payroll tax credit for increasing research activities (Form 8974). Only applies if the user is a qualified small business that elected to apply the §41 R&D credit against payroll tax. See [`references/r&d-payroll-credit.md`](./references/r-and-d-payroll-credit.md).
- **Line 11b–f** — COVID-era credits, generally zero.
- **Line 11g** — Total nonrefundable credits = sum of 11a-11f (positive value reduces tax).

```
Line 12 = Line 10 − Line 11g
```

### Step 8 — Compute Line 13 (deposits and applied credits)

```
Line 13a = Total deposits made this quarter (per EFTPS records)
Line 13b–13z = Other refundable credits (mostly COVID-era, zero by default)
Line 13g = sum
```

The user must reconcile deposits to liability. Pull EFTPS confirmation numbers if possible. Each deposit needs a date and amount.

### Step 9 — Determine balance due / overpayment (Lines 14–15)

```
If Line 12 > Line 13g:
   Line 14 = Line 12 − Line 13g  (balance due — pay with return or by deposit)
If Line 12 < Line 13g:
   Line 15 = Line 13g − Line 12  (overpayment — apply to next return OR refund)
```

If Line 14 > $2,500 and the user is a monthly depositor, deposits should already have been made (else FTD penalty). If Line 14 > $100 in any deposit period for a semi-weekly depositor, FTD penalty risk.

### Step 10 — Determine which schedule attaches (Part 2)

- **Line 16** — Pick a deposit schedule indicator:
  - **Box 1**: Total quarter liability < $2,500 *and* prior quarter liability was < $2,500 *and* you didn't incur a $100K next-day deposit obligation. No deposit schedule entry needed; pay with return.
  - **Box 2**: Monthly depositor. Fill in the three monthly liability amounts on Line 16. Total must equal Line 12.
  - **Box 3**: Semi-weekly depositor. Attach **Schedule B (Form 941)** showing daily liability for each day of the quarter on which wages were paid.

If Box 3, build Schedule B. See [`references/deposit-schedules.md`](./references/deposit-schedules.md). Schedule B totals must match Line 12.

### Step 11 — Run validation checks

See **Validation** below. Run every check.

### Step 12 — Produce the deliverable

See **Output format** below.

### Step 13 — Hand off downstream

State the next forms / actions:

- **W-2 / W-3 reconciliation at year-end** — sum of all four quarters' Line 2 should equal sum of Box 1 wages on W-2s; sum of Line 3 should equal Box 2 on W-2s. Mismatches trigger CP207 / CP207L notices.
- **Form 940 (FUTA)** — annual federal unemployment, due January 31. Separate from 941.
- **Quarterly state withholding return** — state-specific (e.g., CA Form DE 9, NY NYS-45, IL IL-941). Out of scope.
- **Schedule B** if semi-weekly depositor.
- **941-X** if errors are discovered after filing.

### Step 14 — File the return (optional)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree across e-file channels (IRS Modernized e-File via authorized e-file provider, paid payroll software, paper)
- Field-by-field mapping for the canonical channel
- Pre-flight checklist
- Submission state machine
- Security rules — never store EIN + bank info together; always require explicit consent before submission

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Employer identification number (EIN)**: 9 digits, format XX-XXXXXXX. Cannot be SSN.
- **Name**: Legal name as registered with the IRS (matches SS-4 / EIN application).
- **Trade name**: DBA, if any.
- **Address**: Must match IRS records. Address change → file Form 8822-B separately.
- **Quarter check box**: 1, 2, 3, or 4. Match to filing quarter.

### Part 1 — Quarter taxes (Lines 1–15)

| Line | Field | What goes here |
|------|-------|----------------|
| 1 | Number of employees on pay period including 12th of last month of quarter | Single date snapshot, not average |
| 2 | Wages, tips, other compensation | Box 1-style federal income tax wages this quarter |
| 3 | Federal income tax withheld | Per W-4 + supplemental withholding |
| 4 | (checkbox) | Check if no wages, tips subject to SS/Medicare; skip 5a-5e |
| 5a | Taxable SS wages | Up to wage base; column 2 = ×12.4% |
| 5a(i) | Qualified sick leave wages | Default $0 (FFCRA expired) |
| 5a(ii) | Qualified family leave wages | Default $0 |
| 5b | Taxable SS tips | Tipped industries only |
| 5c | Taxable Medicare wages | All Medicare wages, no cap; ×2.9% |
| 5d | Wages subject to Additional Medicare | Wages > $200K to single employee YTD; ×0.9% |
| 5e | Total = 5a + 5b + 5c + 5d (column 2) | Sum |
| 5f | Section 3121(q) tax on unreported tips | Rare |
| 6 | Total taxes before adjustments | Line 3 + 5e + 5f |
| 7 | Adjustment for fractions of cents | Rounding |
| 8 | Sick pay third-party adjustment | Negative if carrier withheld |
| 9 | Adjustment for tips, group-term life | Rare |
| 10 | Total taxes after adjustments | 6 + 7 + 8 + 9 |
| 11a | Qualified small business R&D payroll credit | Form 8974 |
| 11b–f | COVID credits (residual) | Default $0 |
| 11g | Total nonrefundable credits | Sum |
| 12 | Total taxes after credits | 10 − 11g |
| 13a | Total deposits | EFTPS sum |
| 13b–z | Refundable COVID credits etc. | Default $0 |
| 13g | Total deposits + refundable credits | Sum |
| 14 | Balance due | If 12 > 13g |
| 15 | Overpayment | If 13g > 12 |

### Part 2 — Deposit schedule (Line 16)

Pick exactly one box. If Box 3 (semi-weekly), attach Schedule B.

### Part 3 — Business closure / seasonal (Lines 17–18)

- **Line 17** — If you stopped paying wages this quarter and won't have to file in the future, check and provide final wage-paid date. Triggers final-return processing.
- **Line 18** — Seasonal employer indicator (e.g., resort hotel). Lets the IRS skip dunning notices for off-season quarters.

### Part 4 — Third-party designee

Optional. If the employer authorizes a payroll provider or CPA to discuss the return with the IRS, fill in name + phone + 5-digit PIN.

### Part 5 — Sign here

- Title (e.g., "President", "Owner", "Controller")
- Phone
- Date
- Print name + signature (paper)

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 5a col 2 = Line 5a col 1 × 0.124 (within ±$0.01 rounding)
- [ ] Line 5b col 2 = Line 5b col 1 × 0.124
- [ ] Line 5c col 2 = Line 5c col 1 × 0.029
- [ ] Line 5d col 2 = Line 5d col 1 × 0.009
- [ ] Line 5e = Line 5a col 2 + Line 5b col 2 + Line 5c col 2 + Line 5d col 2
- [ ] Line 6 = Line 3 + Line 5e + Line 5f
- [ ] Line 10 = Line 6 + Line 7 + Line 8 + Line 9
- [ ] Line 12 = Line 10 − Line 11g
- [ ] Line 13g = Line 13a + Line 13b + ... + Line 13z
- [ ] Line 14 OR Line 15 (not both) populated
- [ ] If Box 2 (monthly): three monthly amounts on Line 16 sum to Line 12
- [ ] If Box 3 (semi-weekly): Schedule B daily totals sum to Line 12

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 5a col 1 > Line 2 → SS wages exceed gross wages, which is impossible; check pretax deductions logic
- [ ] Line 5c col 1 < Line 5a col 1 → Medicare wages should be ≥ SS wages (no SS cap on Medicare); check
- [ ] Line 5d > 0 but no employee earned > $200K YTD → recheck threshold
- [ ] Line 3 = 0 but Line 2 > 0 → either all employees claimed exempt on W-4 (rare) or withholding wasn't run; verify
- [ ] Line 14 > 0 and Line 16 Box 2 (monthly): if Line 14 > $100, late deposits likely; FTD penalty risk
- [ ] Line 14 > $2,500: at year-end this means deposits should have been ongoing; check EFTPS
- [ ] Total quarter wages (Line 2) is ~25% of expected annual payroll: confirm seasonality or missing pay periods
- [ ] No FFCRA / ARPA credit lines populated for current 2026 quarters (those credits expired Sept 30, 2021; carrying into 2026 indicates a 941-X correction, not a current 941)
- [ ] Schedule B daily amount > $100,000 → next-day deposit rule was triggered (became semi-weekly automatically)

### Cross-form checks

- [ ] EIN matches what's on Form 940, W-2s, prior 941s
- [ ] Employee headcount on Line 1 is consistent with W-2 issuance plans for year-end
- [ ] Sum of YTD Lines 2 across quarters = sum of Box 1 wages on year-end W-2s (run after Q4)
- [ ] Sum of YTD Lines 5a col 1 across quarters ≤ (wage base × number of employees), capped per employee

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to e-file software or paste into IRS authorized e-file provider screens. Format:

```markdown
# Form 941 — DRAFT for Quarter Q, Tax Year YYYY

## Header
Employer name (legal):       <legal name>
Trade name (if any):         <DBA or blank>
EIN:                         XX-XXXXXXX
Address:                     <street, city, state, ZIP>
Quarter:                     [ ] 1  [ ] 2  [ ] 3  [ ] 4

## Part 1 — Quarter Taxes

 1. Employees on pay period including last 12th:   X
 2. Wages, tips, other compensation:               $X,XXX.XX
 3. Federal income tax withheld:                   $X,XXX.XX
 4. [ ] Check if line 2 wages not subject to SS or Medicare

 5a. Taxable SS wages:           $X,XXX.XX × 0.124 = $X,XXX.XX
 5a(i). Sick leave wages:        $0.00 × 0.062 = $0.00
 5a(ii). Family leave wages:     $0.00 × 0.062 = $0.00
 5b. Taxable SS tips:            $0.00 × 0.124 = $0.00
 5c. Taxable Medicare wages:     $X,XXX.XX × 0.029 = $X,XXX.XX
 5d. Add'l Medicare wages:       $0.00 × 0.009 = $0.00
 5e. Total (5a–5d col 2):                          $X,XXX.XX
 5f. §3121(q) Notice and Demand:                   $0.00
 6.  Total taxes before adjustments:               $X,XXX.XX

 7.  Fractions-of-cents adjustment:                $0.00
 8.  Sick pay third-party adjustment:              $0.00
 9.  Tips & group-term life adjustment:            $0.00
10.  Total taxes after adjustments:                $X,XXX.XX

11a. Qualified small business R&D credit (Form 8974): $0.00
11b–f. (Residual COVID credit lines):              $0.00
11g. Total nonrefundable credits:                  $0.00
12.  Total taxes after credits:                    $X,XXX.XX

13a. Total deposits this quarter:                  $X,XXX.XX
13b–z. (Residual COVID refundable credits):        $0.00
13g. Total:                                        $X,XXX.XX

14.  Balance due (if 12 > 13g):                    $X,XXX.XX  OR
15.  Overpayment (if 13g > 12):                    $X,XXX.XX
     Apply to next return  [ ]   Refund  [ ]

## Part 2 — Deposit Schedule (Line 16)
[ ] Box 1: Liability < $2,500 and no $100K next-day rule
[ ] Box 2: Monthly depositor
       Month 1: $X,XXX.XX
       Month 2: $X,XXX.XX
       Month 3: $X,XXX.XX
       Total = Line 12: $X,XXX.XX
[ ] Box 3: Semi-weekly depositor → Schedule B attached

## Part 3 — Business closure / seasonal
17. [ ] Final return — last wages paid date: __________
18. [ ] Seasonal employer

## Part 4 — Third-party designee
Name: __________  Phone: __________  PIN: _____

## Part 5 — Sign here
Title: __________
Phone: __________
Date: __________
Signature: __________

## Required attachments
- [ ] Schedule B (Form 941) if Line 16 Box 3 (semi-weekly)
- [ ] Form 8974 if Line 11a > 0
- [ ] Form 945-A if month-to-day mismatch on Line 16

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 13>

## Sources cited in this draft
- IRS Form 941, Rev. <month YYYY>
- IRS Instructions for Form 941, Rev. <month YYYY>
- IRC §3101 (employee FICA), §3111 (employer FICA), §3101(b)(2) (Additional Medicare), §3402 (income tax withholding)
- Pub. 15 (Employer's Tax Guide) for the tax year
- SSA Annual Wage Base announcement for the tax year
```

The draft is **not** the final filed form. The user still has to e-file via an authorized provider (IRS doesn't accept direct 941 e-files from the public — must go through an authorized e-file provider) or mail paper. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 941 line with examples and edge cases
- [`references/deposit-schedules.md`](./references/deposit-schedules.md) — Monthly vs. semi-weekly depositor rules, $100K next-day rule, Schedule B mechanics, lookback period calculation
- [`references/941-x-corrections.md`](./references/941-x-corrections.md) — When to file 941-X, how to compute the correction, statute of limitations
- [`references/r-and-d-payroll-credit.md`](./references/r-and-d-payroll-credit.md) — Qualified small business §41 R&D credit applied to payroll tax via Form 8974 (Line 11a)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files via authorized IRS e-file provider, paid payroll software, or paper (loaded only when the user authorizes filing)

## Examples

End-to-end worked Form 941s. Use these as patterns when the user's situation is similar.

- [`examples/small-business-5-employees.md`](./examples/small-business-5-employees.md) — Cash-basis service business with 5 W-2 employees, monthly depositor
- [`examples/scorp-single-shareholder.md`](./examples/scorp-single-shareholder.md) — S-corp paying single shareholder-employee $80,000 reasonable comp + distributions
- [`examples/941-x-correction.md`](./examples/941-x-correction.md) — Employer discovers misclassified contractor and files 941-X to add Q2 wages

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises Form 941 each tax year, often in March.

- [Form 941 (latest)](https://www.irs.gov/pub/irs-pdf/f941.pdf) — the form itself
- [Instructions for Form 941 (latest)](https://www.irs.gov/pub/irs-pdf/i941.pdf) — IRS line-by-line guidance
- [About Form 941](https://www.irs.gov/forms-pubs/about-form-941) — IRS landing page with archive of past revisions
- [Schedule B (Form 941)](https://www.irs.gov/pub/irs-pdf/f941sb.pdf) — daily liability schedule for semi-weekly depositors
- [Instructions for Schedule B (Form 941)](https://www.irs.gov/pub/irs-pdf/i941sb.pdf) — Schedule B IRS guidance
- [Form 941-X (correction)](https://www.irs.gov/pub/irs-pdf/f941x.pdf) — for amending a previously-filed 941
- [Instructions for Form 941-X](https://www.irs.gov/pub/irs-pdf/i941x.pdf) — IRS correction guidance
- [About Form 941-X](https://www.irs.gov/forms-pubs/about-form-941-x) — IRS landing page
- [Publication 15 (Employer's Tax Guide)](https://www.irs.gov/pub/irs-pdf/p15.pdf) — withholding tables, deposit rules, year-aware
- [Publication 15-A (Employer's Supplemental Tax Guide)](https://www.irs.gov/pub/irs-pdf/p15a.pdf) — fringe benefits, sick pay, supplemental wages
- [Publication 15-B (Employer's Tax Guide to Fringe Benefits)](https://www.irs.gov/pub/irs-pdf/p15b.pdf) — taxable / nontaxable fringe rules
- [Employment Taxes landing page](https://www.irs.gov/businesses/small-businesses-self-employed/employment-taxes) — IRS hub
- [Companion blog: Payroll Tax Due Dates Guide 2026](https://jupid.com/blog/payroll-tax-due-dates-form-941-940-guide-2026) — Jupid's narrative companion for human readers
- IRC §3101 (FICA on employee), §3111 (FICA on employer), §3101(b)(2) (Additional Medicare), §3402 (income tax withholding), §3121(q) (tip notice and demand), §6302 (deposit rules), §6511 (statute of limitations on refund / correction)
- SSA — annual contribution and benefit base ($176,100 for 2025; verify 2026 at https://www.ssa.gov/oact/cola/cbb.html)
- Notice 2021-24 (last year of FFCRA / ARPA leave-credit guidance)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and the Internal Revenue Code. It is not tax advice and does not establish a CPA-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations (multi-state payroll, expat employees, shareholder-employee reasonable compensation challenges, prior-quarter underpayments approaching statute of limitations) warrant a licensed CPA or enrolled agent's review.
