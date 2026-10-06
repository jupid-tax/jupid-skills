---
name: schedule-h
description: >
  Use this skill when an individual (or an estate or trust) pays a household
  employee such as a nanny, babysitter, housekeeper, cook, private nurse, caregiver,
  driver, or yard worker, and must figure Social Security, Medicare, Additional
  Medicare, withheld federal income tax, and federal unemployment (FUTA) tax on
  Schedule H (Form 1040), plus the related Forms W-2 and W-3. Triggers on phrases
  like "Schedule H", "nanny tax", "household employment taxes", "I pay a nanny",
  "pay my housekeeper on the books", "caregiver taxes", "household employee W-2",
  "do I owe FUTA for my babysitter", "Schedule 2 household employment taxes",
  "file Schedule H by itself". Do NOT use for: business employees — use form-941
  and form-940; a business owner who chooses to report the household employee on
  Form 941/944/943 and Form 940 — use form-941 and form-940; workers who are
  self-employed or controlled by an agency — no Schedule H; contractors paid by a
  business — use form-1099-nec; getting the EIN — use form-ss-4; assembling the
  rest of Schedule 2 — use schedule-2; state household payroll filings — state
  forms, out of scope.
form: Schedule H (Form 1040) (Household Employment Taxes)
audience: [household-employer, individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040sh.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040sh.pdf
---

# Schedule H (Form 1040) — Household Employment Taxes

This skill produces an audit-grade draft of Schedule H, the matching Forms W-2 and W-3 entries, and a plan for paying the tax during the year. The arithmetic is two multiplications and a sum. The judgment sits in who counts: which workers are household employees, which relatives and minors are excluded from the Social Security test but not from FUTA, which quarter crossed $1,000, and whether state unemployment contributions were paid on time and in a credit reduction state. The agent asks for each of those facts instead of assuming.

**Revision verified.** The line map was built from the text of the **2025 Schedule H (Form 1040)** (Created 4/15/25; filed in 2026) and the **2025 Instructions for Schedule H** (dated Dec 1, 2025), and compared with the **2026 draft Schedule H** (Created 5/8/26) and **2026 draft instructions** (dated Aug 19, 2026). Line numbers are identical. What changes for 2026: the line A test rises from $2,800 to $3,000, the quarter test looks at 2025 or 2026, state contributions are due April 15, 2027, and the destination on the 2026 draft Schedule 2 moves from line 9 to line 17a. Re-check the final 2026 Schedule H, Schedule 2, and the final 2026 credit reduction rates at [About Schedule H (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-h-form-1040) and IRS.gov/DraftForms before use.

**Companion guide for end users:** [Schedule H Instructions 2026: Line-by-Line Guide to Household Employment Taxes](https://jupid.com/blog/schedule-h-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when any of the following is true:

- The user mentions Schedule H, the "nanny tax", or household employment taxes.
- The user pays someone to work in or around their home and controls how the work is done (babysitter, nanny, housekeeper, cleaning person, cook, caretaker, health aide, private nurse, driver, yard worker, maid, butler).
- The user withheld federal income tax from a household worker at the worker's request.
- The user asks whether a household worker's pay crossed $2,800 (2025) or $3,000 (2026), or whether a quarter crossed $1,000.
- The user needs Forms W-2 and W-3 for a household employee.
- The user owes household employment taxes and has no Form 1040 filing requirement (stand-alone Schedule H).

Do not engage, and route instead, when:

- The worker runs an independent business with their own tools and offers services to the public, or an agency controls who does the work and how → not the user's employee; no Schedule H (Instructions for Schedule H, "Workers who aren't your employees"; Pub. 926 (2026), "Workers who aren't your employees").
- A worker provides childcare in the worker's own home → generally not the user's employee (Pub. 926 (2026)).
- The workers are business employees → [`../form-941/SKILL.md`](../form-941/SKILL.md) and [`../form-940/SKILL.md`](../form-940/SKILL.md).
- The user owns a business or farm and chooses to report the household employee with business employees on Form 941, 944, or 943 and Form 940 → those skills; do not also file Schedule H (Pub. 926 (2026), "Payment option for business employers" and "Business employment tax returns").
- A government agency or a Form 2678 agent reports and pays the employment taxes for a home care recipient → no Schedule H for those wages (Instructions for Schedule H, TIP under "Did you have a household employee?").
- The user needs an EIN → [`../form-ss-4/SKILL.md`](../form-ss-4/SKILL.md).
- The user is assembling Schedule 2 → [`../schedule-2/SKILL.md`](../schedule-2/SKILL.md) takes line 26 from this skill.
- Puerto Rico household employers (Schedule H-PR, Form 499R-2/W-2PR) → out of scope; say so.

---

## Prerequisites

Collect these before drafting. If any is missing, ask the question shown and stop until it is answered.

1. **Tax year.** "Which calendar year are these wages for?" The thresholds, wage base, due dates, and Schedule 2 line depend on it.
2. **Return type.** "Will you file Form 1040 (or 1040-SR, 1040-NR, 1040-SS, or a Form 1041) for that year?" If not, Schedule H is filed by itself with Part IV.
3. **Employer identity.** Name exactly as on the return, SSN (not on Form 1041), and EIN. "Do you have an employer identification number? If you applied, on what date?" Never put an SSN in the EIN field.
4. **For each worker:**
   - Relationship to the user (spouse, child, parent, other relative, unrelated).
   - Age at any time during the year, and whether the worker was a student.
   - Where and how the work is done: in the user's home, under the user's direction? Through an agency that controls the work? In the worker's own home? Their own business?
   - Cash wages paid in each calendar quarter of the current year and the prior year. The instructions define cash wages as "wages paid by check, money order, etc."; treat cash, bank transfers, and app transfers of money the same way, and ask if a payment form is unclear. Use dates paid, not dates earned.
   - Noncash items (meals, lodging, clothing, transit passes) and any cash given in place of them.
   - Whether the employee's 7.65% share was withheld or the user paid it from their own funds.
   - Whether the worker gave a Form W-4 and federal income tax was withheld, and how much.
   - State disability plan payments the employee received, if the state sent a notice.
5. **State unemployment.** Every state the user paid unemployment contributions to; total contributions for the year; the date of each payment; assigned experience rate(s) and rate periods; taxable state wages. Exclude amounts withheld from the employee, penalties, interest, special administrative taxes, and voluntary contributions.
6. **For a parent employee:** "Does your parent care for your child who lives with you and is under 18 (or needs adult care for at least 4 continuous weeks in the quarter)? Are you divorced and not remarried, widowed, or married to a spouse whose condition prevented them from caring for the child for at least 4 continuous weeks in the quarter?"
7. **For a worker under 18:** "Was household work this person's principal occupation?" A student's never is.
8. **Business owner option:** "Do you own a business or farm with its own payroll, and do you want the household employee on that payroll instead?"
9. **Payment planning (for the penalty discussion):** prior-year tax, prior-year AGI, current withholding from the user's wages or pension, and estimated payments made.

---

## Workflow

### Step 1 — Classify each worker

Confirm each worker is a household employee (control test, work in or around the private home). Drop agency-controlled and self-employed workers and say why. See [`references/who-and-what-counts.md`](./references/who-and-what-counts.md).

### Step 2 — Build the quarterly cash-wage table

```
| Worker | Relationship | Age/student | Q1 | Q2 | Q3 | Q4 | Year total | Counts for line A? | Counts for line C / line 15? |
```

Include the prior year's quarters for the line C test.

### Step 3 — Answer lines A, B, C

- **Line A:** any one employee's countable cash wages ≥ $2,800 (2025) / $3,000 (2026)? Leave out spouse, child under 21, parent (unless the parent exception applies), and anyone under 18 at any time in the year (unless household work is their principal occupation; never for a student). Yes → line 1.
- **Line B:** any federal income tax withheld from any household employee? Yes → line 7.
- **Line C:** total cash wages to all household employees of $1,000 or more in any calendar quarter of the current or prior year, leaving out spouse, child under 21, and parent? Yes → line 10. No → stop; no Schedule H.

Decision patterns (2026 values; each row follows from the line A and line C text and the exclusions in Pub. 926 (2026)):

| Facts | A | B | C | Result |
|---|---|---|---|---|
| Unrelated adult nanny, $640 a week all year | Yes | — | — | Part I and Part II (her quarters exceed $1,000) |
| Unrelated adult cleaner, $2,700 for the year (about $675 per quarter), no withholding, no 2025 quarter at $1,000 | No | No | No | No Schedule H |
| Same cleaner, but $1,200 in one quarter | No | No | Yes | FUTA only: line 25 = 0 |
| Unrelated adult paid $1,500, income tax withheld at her request | No | Yes | — | Part I line 7 only; line 9 decides Part II; W-2 boxes 1 and 2 only |
| 16-year-old student sitter, $4,000 over the summer, $2,800 in one quarter | No | No | Yes | FUTA only on $4,000 |
| User's own 19-year-old child, $6,000 | No | No | No (child under 21 excluded) | No Schedule H |
| User's mother, $10,000, user widowed, grandchild under 18 at home | Yes | — | — | Part I; mother excluded from Part II |

### Step 4 — Part I (lines 1–9)

Lines 1 and 3 take every cash dollar paid in the year to each employee who passed line A, including the first dollars; line 1 is capped per employee at the Social Security wage base. Line 5 takes each employee's wages above $200,000. Line 7 is the income tax actually withheld. Line 9 repeats the line C test.

If the user did not withhold the employee's 7.65%, the Schedule H amounts do not change; the employer owes both shares, and the gross-up affects only W-2 box 1 (Instructions for Schedule H, Part I and "Employee's portion of taxes paid by employer"). If a state disability plan paid the employee and withheld her share, follow the line 8 adjustment in [`references/line-by-line.md`](./references/line-by-line.md).

### Step 5 — Part II (lines 10–24)

Lines 10–12 decide Section A or Section B. Section A: line 15 × 0.006. Section B: line 17 columns, then Worksheet 1 for late contributions and Worksheet 2 for credit reduction states. See [`references/futa-section-b-worksheets.md`](./references/futa-section-b-worksheets.md).

### Step 6 — Part III (lines 25–27)

Line 25 = line 8 (zero if line C was answered Yes). Line 26 = line 16 or 24, plus line 25. Line 27 routes the total to the right return line.

### Step 7 — Forms W-2 and W-3

Prepare W-2 entries for each employee who had Social Security and Medicare wages at or above the test, or federal income tax withheld (Pub. 926 (2026), "Form W-2"):

- Box 1: cash wages plus taxable noncash wages, plus any employee share of Social Security and Medicare the employer paid instead of withholding (add boxes 3, 4, and 6, or 4, 5, and 6 if box 5 exceeds box 3).
- Box 2: line 7 amount for that employee.
- Boxes 3 and 5: the employee's line 1 and line 3 amounts. Boxes 4 and 6: the employee share withheld or paid for the employee, never the employer share.
- Below the test with income tax withheld: boxes 1 and 2 only; boxes 3–6 blank or the SSA rejects the form.
- Form W-3 box b: "Hshld. emp." Due to the employee and the SSA by February 2, 2026 (2025 forms) or February 1, 2027 (2026 forms).

No W-2 is due for an employee with no Social Security or Medicare wages and no withholding (for example, a FUTA-only teenage sitter); suggest a receipt instead (Pub. 926 (2026)).

### Step 8 — Payment plan and penalty check

Household employment taxes are added to the user's income tax and count for the estimated tax penalty (IRC §3510(b)(1)), unless the user has no withholding at all and would not otherwise owe estimated tax (IRC §3510(b)(2)). Compute:

```
Projected total tax = income tax + Schedule H line 26
Required payments   = lesser of 90% of projected total tax, or 100% of prior-year tax
                      (110% if prior-year AGI > $150,000; $75,000 if married filing separately)   [IRC §6654(d)]
Shortfall           = required payments − (withholding to date + projected withholding + estimates paid)
```

If there is a shortfall, propose extra withholding on Form W-4 (wages) or W-4P (pension), which counts as paid evenly through the year (IRC §6654(g)(1)), or Form 1040-ES installments. Show the per-paycheck amount and the count of remaining paychecks. Ask the user for prior-year tax and AGI; do not estimate them. See [`references/paying-and-correcting.md`](./references/paying-and-correcting.md).

### Step 9 — Validate

Run every check in **Validation**.

### Step 10 — Produce the deliverable

Use **Output format**, with every line shown, including zeros and blanks.

### Step 11 — Hand off and file

State where line 26 goes, due dates for W-2/W-3 and Schedule H, and state filings to check. If the user authorizes filing, follow [`filing.md`](./filing.md).

---

## Line-by-line guidance

Full map from the PDF text: [`references/line-by-line.md`](./references/line-by-line.md).

### Key figures (year-dependent; re-verify each year)

| Item | 2025 Schedule H (filed 2026) | 2026 Schedule H (filed 2027) | Source |
|---|---|---|---|
| Line A cash-wage test per employee | $2,800 | $3,000 | 2025 form line A; 2026 draft line A; Pub. 926 (2026); SSA domestic employee coverage threshold |
| Line C / line 9 quarter test | $1,000 in any quarter of 2024 or 2025 | $1,000 in any quarter of 2025 or 2026 | Schedule H lines C and 9; IRC §3306(a)(3) |
| Social Security wage base (line 1 cap) | $176,100 | $184,500 | 2025 instructions; Pub. 926 (2026); SSA |
| Social Security rate (line 2) | 12.4% | 12.4% | Schedule H line 2 |
| Medicare rate (line 4) | 2.9%, no cap | 2.9%, no cap | Schedule H line 4 |
| Additional Medicare (lines 5–6) | 0.9% of wages over $200,000, employee only | Same | Schedule H lines 5–6 |
| FUTA (Section A) | 0.6% of first $7,000 per employee | Same | Schedule H line 16 |
| State contributions due for full credit | April 15, 2026 | April 15, 2027 | Schedule H line 11 |
| Credit reduction (Worksheet 2) | CA 0.012, VI 0.045 | CA and VI listed as "0.0XX" on the draft | 2025 instructions Worksheet 2; 2026 draft instructions |
| Destination of line 26 (Form 1040/1040-SR/1040-NR) | Schedule 2 line 9 | Schedule 2 line 17a (draft) | Schedule H line 27; Schedule 2 (2025); 2026 draft Schedule 2 |
| W-2/W-3 due | February 2, 2026 | February 1, 2027 | Instructions for Schedule H; Pub. 926 (2026) |
| Schedule H due | April 15, 2026 with the return (extension applies) | April 15, 2027 | Instructions; Pub. 926 (2026); IRC §3510(a) |
| Transit/parking monthly exclusion | $325 each | $340 each | Instructions (2025 and 2026 draft); Pub. 926 (2026) |

The 2026 test is the SSA's computation $1,000 × 69,846.57 ÷ 23,132.67 = $3,019.39, rounded down to $3,000 (SSA, "Determination of Employment Coverage Thresholds"; IRC §3121(x)).

### Header

Name of employer (must match the return; only two Schedules H per Form 1040, one per spouse), SSN (Form 1041 filers leave blank), EIN (or "Applied For" and the date). "Calendar year taxpayers having no household employees in [year] don't have to complete this form."

### Part I — Social Security, Medicare, and Federal Income Taxes

| Line | Entry |
|---|---|
| 1 | Cash wages paid in the year to each employee who met the line A test; only the first $176,100 (2025) / $184,500 (2026) per employee |
| 2 | Line 1 × 12.4% (0.124) |
| 3 | Same employees' cash wages, no cap |
| 4 | Line 3 × 2.9% (0.029) |
| 5 | Each employee's cash wages above $200,000 |
| 6 | Line 5 × 0.9% (0.009) |
| 7 | Federal income tax withheld, if any |
| 8 | Lines 2 + 4 + 6 + 7 |
| 9 | $1,000 quarter test; No → line 8 to the Schedule 2 line and stop (Part IV if no Form 1040); Yes → line 10 |

The employer owes both halves of Social Security and Medicare whether or not the employee's share was withheld (Instructions for Schedule H, Part I).

### Part II — FUTA

| Line | Entry |
|---|---|
| 10 | Contributions paid to only one state? Check "No" if that state is a credit reduction state |
| 11 | All state contributions for the year paid by April 15 of the next year? (Fiscal-year filers: by the return due date without extensions) |
| 12 | All FUTA-taxable wages also taxable for state unemployment tax? |
| 13–16 | Section A (all Yes): state code; contributions paid (or "0% rate"); line 15 = first $7,000 of each employee's cash wages, including employees under 18 and employees paid under $1,000, excluding spouse, child under 21, and parent; line 16 = line 15 × 0.006 |
| 17–24 | Section B (any No): columns (a)–(h) per state and rate period; 18 totals; 19 = (g) + (h); 20 = FUTA wages; 21 = 20 × 6.0%; 22 = 20 × 5.4%; 23 = smaller of 19 or 22, or the Worksheet 1/2 result (check the box); 24 = 21 − 23 |

### Part III and Part IV

Line 25 = line 8 (or 0 if line C was Yes). Line 26 = line 16 (or 24) + line 25. Line 27: Form 1040, 1040-SR, or 1040-NR → Schedule 2 line 9 (2025) / line 17a (2026 draft); 1040-SS → Part I, line 4; 1041 → Schedule G, Part I, line 7; none of these → complete Part IV (address and signature; paid preparer block only when the schedule is not attached to one of those returns).

---

## Validation

### Math checks

- [ ] Line 1 = Σ countable cash wages of line-A employees, each capped at the wage base
- [ ] Line 2 = line 1 × 0.124; line 4 = line 3 × 0.029; line 6 = line 5 × 0.009 (to the cent)
- [ ] Line 3 ≥ line 1; line 5 = Σ max(0, employee cash wages − $200,000)
- [ ] Line 8 = 2 + 4 + 6 + 7
- [ ] Line 15 (or 20) = Σ min($7,000, FUTA-countable cash wages) per employee
- [ ] Section A: line 16 = line 15 × 0.006
- [ ] Section B: (e) = (b) × 0.054; (f) = (b) × (d); (g) = max(0, e − f); 19 = Σg + Σh; 21 = 20 × 0.06; 22 = 20 × 0.054; 24 = 21 − 23
- [ ] Worksheets recomputed line by line when used
- [ ] Line 25 = line 8 unless line C was Yes (then 0)
- [ ] Line 26 = line 16 or 24, plus line 25

### Sanity checks (warn)

- [ ] Line A "No" but any employee's countable cash wages reached the test → recheck exclusions
- [ ] Wages of a spouse, child under 21, or parent on line 15 → remove (no FUTA exception for parents)
- [ ] An under-18 student on line 1 → remove; keep on line 15
- [ ] Line 7 > 0 without a Form W-4 on file → confirm the withholding agreement
- [ ] Section A used while a state payment was made after April 15 or the state is a credit reduction state → switch to Section B
- [ ] Line 16 or 24 > $42 per FUTA employee although contributions were paid on time and no credit reduction state applies → recheck
- [ ] Line 7 > 0 but no W-2 planned for that employee → a W-2 is required whenever income tax is withheld
- [ ] Noncash items included on lines 1, 3, or 15 → remove (they go in W-2 box 1 only)
- [ ] User paid the employee's share but W-2 box 1 equals box 3 → apply the gross-up
- [ ] Line C answered Yes but lines 1–9 filled in → line C Yes skips Part I; line 25 is 0
- [ ] Household wages also deducted on Schedule C or F → not allowed (Pub. 926 (2026))

### Cross-form checks

- [ ] W-2 box 3 total = line 1 and box 5 total = line 3 (for employees with W-2s); box 2 total = line 7
- [ ] W-2 boxes 3–6 blank for an employee below the test who had income tax withheld
- [ ] Line 26 appears on the correct Schedule 2 line for the year (or the 1040-SS / 1041 line)
- [ ] EIN on Schedule H = EIN on W-2 and W-3

---

## Output format

```markdown
# Schedule H (Form 1040) — DRAFT for tax year YYYY

Form revision used: Schedule H (YYYY), Created M/D/YY [final | 2026 DRAFT — re-check]

## Header
Name of employer: <as on return>
SSN: <masked> | (Form 1041: blank)
EIN: XX-XXXXXXX | Applied For <date>

## Worker classification
| Worker | Relationship | Age/student | Household employee? | Line A wages | Line C/15 wages | Notes |

## Filing questions
A. One employee ≥ $X,XXX cash wages?  Yes | No
B. Federal income tax withheld?       Yes | No | (skipped)
C. $1,000 in any quarter of YYYY−1 or YYYY? Yes | No | (skipped)

## Part I
1. Cash wages subject to social security tax:       $X
2. Social security tax (× 0.124):                     $X
3. Cash wages subject to Medicare tax:               $X
4. Medicare tax (× 0.029):                            $X
5. Cash wages subject to Additional Medicare:         $X
6. Additional Medicare Tax withholding (× 0.009):     $X
7. Federal income tax withheld:                       $X
8. Total (2 + 4 + 6 + 7):                             $X
9. $1,000 quarter test: Yes | No

## Part II
10. Only one state?  Yes | No     11. Paid by April 15?  Yes | No     12. All wages state-taxable?  Yes | No
Section A: 13 <state>  14 $X  15 $X  16 $X
Section B: line 17 table (a)–(h); 18; 19; 20; 21; 22; 23 [box checked if worksheet]; 24
Worksheet 1 / Worksheet 2 detail (keep)

## Part III
25. $X
26. Total household employment taxes: $X
27. Required to file Form 1040? Yes → Schedule 2, line <9 | 17a> | No → Part IV

## Forms W-2 / W-3 (per employee)
Box 1 | Box 2 | Box 3 | Box 4 | Box 5 | Box 6 ; W-3 box b "Hshld. emp." checked; due <date>

## Payment plan
Total tax with household taxes: $X; withholding + estimates so far: $X; proposed W-4/W-4P or 1040-ES amounts and dates

## Validation summary
- Math: <pass | failures>
- Sanity: <warnings>
- Year check: thresholds and Schedule 2 line match the tax year

## Sources cited in this draft
- Schedule H (YYYY) and Instructions for Schedule H (YYYY)
- Pub. 926 (YYYY)
- SSA coverage threshold and contribution and benefit base for YYYY
- IRC §§3121, 3306, 3510, 6654
```

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of Schedule H from the 2025 PDF text with 2026 draft values side by side
- [`references/who-and-what-counts.md`](./references/who-and-what-counts.md) — household employee test, family and under-18 exclusions for line A versus FUTA, cash versus noncash wages, W-2/W-3 and EIN rules
- [`references/futa-section-b-worksheets.md`](./references/futa-section-b-worksheets.md) — Section A versus B, line 17 columns, Worksheet 1 (late contributions), Worksheet 2 (credit reduction)
- [`references/paying-and-correcting.md`](./references/paying-and-correcting.md) — paying through withholding or estimated tax, IRC §3510 and §6654, business-owner option, stand-alone filing, corrections, records
- [`references/common-mistakes.md`](./references/common-mistakes.md) — frequent errors with authority and fix
- [`filing.md`](./filing.md) — filing with Form 1040, stand-alone paper filing and addresses, W-2/W-3 to the SSA, consent and security rules

## Examples

- [`examples/full-time-nanny-2025.md`](./examples/full-time-nanny-2025.md) — full-time nanny with income tax withholding, Section A, W-2, and an extra-withholding plan
- [`examples/widowed-parent-and-teen-sitter-2026.md`](./examples/widowed-parent-and-teen-sitter-2026.md) — parent exception for a grandmother-caregiver, a 17-year-old student sitter counted only for FUTA, an agency cleaner excluded (2026 draft form)
- [`examples/california-caregiver-late-state-tax-2025.md`](./examples/california-caregiver-late-state-tax-2025.md) — California caregiver, state contributions paid late, Section B with Worksheets 1 and 2

## Sources

Re-verify each source for the tax year being filed.

- [Schedule H (Form 1040) (2025)](https://www.irs.gov/pub/irs-pdf/f1040sh.pdf) and [Instructions for Schedule H (2025)](https://www.irs.gov/pub/irs-pdf/i1040sh.pdf)
- 2026 drafts: [Schedule H](https://www.irs.gov/pub/irs-dft/f1040sh--dft.pdf), [Instructions](https://www.irs.gov/pub/irs-dft/i1040sh--dft.pdf), [Schedule 2](https://www.irs.gov/pub/irs-dft/f1040s2--dft.pdf)
- [Schedule 2 (Form 1040) (2025)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf)
- [About Schedule H (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-h-form-1040)
- [Publication 926 (2026), Household Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p926.pdf)
- [Publication 15 (2026), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf), sections 3 and 14
- [SSA: Determination of Employment Coverage Thresholds](https://www.ssa.gov/oact/cola/covthreshdet.html) and [Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html)
- [U.S. Department of Labor: FUTA credit reductions](https://oui.doleta.gov/unemploy/futa_credit.asp)
- IRC §3121(a)(7)(B) and §3121(x) (domestic cash-wage threshold), §3121(b)(3) (family employment, parent exception), §3121(b)(21) (under-18 domestic service), §3306(a)(3) and §3306(c)(2) ($1,000 quarter test), §3306(c)(5) (family employment for FUTA), §3510 (household taxes collected with income tax; no deposits; estimated tax treatment), §6654 (estimated tax penalty; withholding timing in §6654(g))
- [Companion guide](https://jupid.com/blog/schedule-h-instructions-2026) for human readers

## Disclaimer

This skill encodes the mechanics of Schedule H from public IRS forms, instructions, and publications. It is not tax or legal advice and does not create a CPA-client relationship. Worker classification, state unemployment and disability rules, and penalty situations can be fact-specific; the agent should tell the user that the draft is a starting point and recommend a CPA or enrolled agent for anything unusual.
