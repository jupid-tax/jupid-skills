---
name: form-1040-x
description: >
  Use this skill when an individual needs to correct a Form 1040, 1040-SR, or
  1040-NR that was already filed and accepted: missed income (a late W-2 or
  1099), a missed deduction or credit, a wrong filing status, dependents added
  or removed, or a claim for refund for a prior year. Triggers on phrases like
  "amend my tax return", "Form 1040-X", "amended return", "I forgot a 1099",
  "I missed a deduction last year", "claim a refund for 2023", "file a 1040-X",
  "where's my amended return", "can I still amend 2022". Do NOT use for: an
  original return that was never filed or was rejected in e-file (use
  form-1040); a refund of only penalties or interest (use form-843); a business
  return (Form 1120, 1120-S, or 1065 have their own amendment mechanics, use
  form-1120, form-1120-s, or form-1065); a payment plan for the balance (use
  form-9465); a CP2000 notice you fully agree with and have nothing else to
  change (follow the notice, no 1040-X).
form: Form 1040-X (Amended U.S. Individual Income Tax Return)
audience: [individual, solo, freelance, llc1, nonresident]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040x.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040x.pdf
---

# Form 1040-X — Amended U.S. Individual Income Tax Return

This skill produces an audit-grade draft of Form 1040-X: every line 1 through 23 in columns A (original or as previously adjusted), B (net change), and C (correct amount), the Part I dependent list when dependents change, a Part II explanation a reviewer can follow, the list of corrected schedules to attach, a refund-statute check, and a filing-channel decision.

The arithmetic on Form 1040-X is simple. The judgment sits in four places: deciding whether to amend at all (many errors are fixed by the IRS without one), building column A from the return *as the IRS currently has it*, recomputing every downstream item the change touches using the amended year's own rules, and checking that a refund claim is still inside the IRC §6511 window and lookback cap. The agent asks for the dates and documents those steps need; it never assumes them.

**Verified against:** Form 1040-X (Rev. December 2025) and Instructions for Form 1040-X (Rev. December 2025, dated Feb 27, 2026). Form 1040-X is a continuous-use form, not an annual one: the same revision is used to amend any year until the IRS replaces it. Before using this skill, open [About Form 1040-X](https://www.irs.gov/forms-pubs/about-form-1040x) and confirm the current revision; if it is later than December 2025, re-check the line map in [`references/line-by-line.md`](./references/line-by-line.md). The substance of the correction (brackets, standard deduction, credits, schedules) always comes from the forms and instructions **for the year being amended**, not from the current year.

**Companion guide for end users:** [Amended Tax Return 2026: Form 1040-X, Deadlines, and Refund Tracking](https://jupid.com/blog/amended-tax-return-form-1040-x-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions Form 1040-X, an amended return, or correcting a filed individual return.
- The user received a W-2, W-2c, 1099, 1099-R, K-1, or corrected statement **after** filing, and it changes income, withholding, or credits.
- The user finds a deduction, credit, or dependent they missed, or claimed one they were not entitled to.
- The user wants to change filing status (subject to the MFJ-to-MFS restriction below).
- The user asks whether a prior-year refund can still be claimed ("is it too late to amend 2022?").
- The user filed Form 1040-NR and should have filed Form 1040, or the reverse. Form 1040-X covers that switch (Instructions for Form 1040-X, "Resident and nonresident aliens").
- The user filed a 2025 return without a Schedule 1-A deduction they qualify for. The IRS notes that the final occupation list for the "no tax on tips" deduction (Treas. Reg. §1.224-1) may make an amended 2025 return worthwhile ([About Form 1040-X](https://www.irs.gov/forms-pubs/about-form-1040x), recent development dated 04-May-2026).

Do **not** engage this skill when:

- **No original return was filed, or the e-filed original was rejected.** A rejected return is not filed; correct and retransmit it, or file it on paper. Use [`../form-1040/SKILL.md`](../form-1040/SKILL.md). The instructions say to file Form 1040-X "only after you have filed your original return".
- **Only a refund of penalties, interest, or an addition to tax is wanted.** Use Form 843: [`../form-843/SKILL.md`](../form-843/SKILL.md).
- **Only an injured spouse allocation is wanted.** Form 8379 (it can ride along on an e-filed 1040-X, but no amendment is needed for it alone).
- **The user is amending a business return** (C corporation, S corporation, partnership). Use [`../form-1120/SKILL.md`](../form-1120/SKILL.md), [`../form-1120-s/SKILL.md`](../form-1120-s/SKILL.md), or [`../form-1065/SKILL.md`](../form-1065/SKILL.md). A sole proprietor's Schedule C is part of the individual return, so a Schedule C correction *does* come here.
- **The user received a CP2000 and agrees with it with nothing else to change.** Follow the notice; the IRS says no amendment is needed. See [`references/when-not-to-amend.md`](./references/when-not-to-amend.md).
- **The user only needs a payment plan for an existing balance.** Use [`../form-9465/SKILL.md`](../form-9465/SKILL.md).

Boundaries with sibling skills:

- The corrected Form 1040 itself is built with [`../form-1040/SKILL.md`](../form-1040/SKILL.md) and the schedule skills ([`../schedule-c/SKILL.md`](../schedule-c/SKILL.md), [`../schedule-se/SKILL.md`](../schedule-se/SKILL.md), [`../schedule-1/SKILL.md`](../schedule-1/SKILL.md), [`../schedule-a/SKILL.md`](../schedule-a/SKILL.md), [`../form-8995/SKILL.md`](../form-8995/SKILL.md)). This skill reconciles the corrected figures onto Form 1040-X.
- A corrected Form 1040-NR is built with [`../form-1040-nr/SKILL.md`](../form-1040-nr/SKILL.md); this skill wraps it.
- If the original return is lost, reconstruct column A from an IRS transcript: [`../form-4506-t/SKILL.md`](../form-4506-t/SKILL.md).
- State amended returns are out of scope. A federal change may require one; tell the user to contact the state tax agency and never attach a state return to the federal 1040-X (irs.gov, [File an amended return](https://www.irs.gov/filing/file-an-amended-return)).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any is missing, **ask for it explicitly and stop until answered**. Do not default.

1. **Tax year being amended** (calendar or fiscal). One Form 1040-X per year.
2. **The return as filed**: a copy of the filed Form 1040/1040-SR/1040-NR with every schedule and form. If unavailable, an IRS account or return transcript (see [`../form-4506-t/SKILL.md`](../form-4506-t/SKILL.md)), and tell the user a transcript may not show every attachment.
3. **Every IRS change since filing**: math-error notices, CP2000 results, audit reports, prior Forms 1040-X. Ask: "Has the IRS sent you any notice about this return, or have you amended it before?" Column A must reflect those changes.
4. **What changed and the document behind it**: the late W-2/1099, the receipt, Form 5498, the corrected K-1, and so on.
5. **Filing status on the original and on the amended return.** If the original was married filing jointly and the user wants married filing separately, ask whether the original due date has passed; in general the switch is not allowed after it (Form 1040-X, filing status caution).
6. **Dates for the statute check** (refund claims only): the date the original was filed or accepted, whether an extension was filed, and the date and amount of every payment (withholding, estimates, amount paid with the return, later payments). See [`references/refund-statute.md`](./references/refund-statute.md).
7. **How the original was filed** (e-file or paper) and in which calendar year, for the channel decision in [`filing.md`](./filing.md).
8. **Original refund status** if claiming an additional refund: has the original refund been received? The IRS advises waiting for it before filing for more ([Amending a return](https://www.irs.gov/newsroom/amending-a-return-youtube-video-text-script)).
9. **Current mailing address**, and the state of residence (paper mailing address depends on it).

For a dependent change, also ask for each dependent: name, SSN/ITIN/ATIN, relationship, months lived with the taxpayer, and which credit is claimed. For a retroactive child tax credit claim, ask when the child's SSN was issued; it must have been issued, valid for employment, before the due date (including extensions) of the return being amended (Instructions for Form 1040-X, line 7 and line 15).

---

## Workflow

Execute these steps in order.

### Step 1 — Decide whether an amendment is the right tool

Run the decision table in [`references/when-not-to-amend.md`](./references/when-not-to-amend.md). Stop and redirect if the case is a math error the IRS already corrected, a missing form the IRS accepted or asked for, a rejected e-file, a CP2000 the user fully agrees with, a penalty-only refund (Form 843), or a pre-due-date superseding return. Tell the user which branch applied and why.

### Step 2 — Check the deadline before doing the work

For a refund or credit, run the date procedure in [`references/refund-statute.md`](./references/refund-statute.md): deemed filing date, 3-year window, 2-year window, and the lookback cap on the refundable amount. If the claim is out of time, say so and stop unless a special period applies (bad debt, worthless security, foreign tax credit, carryback, disaster, combat zone, financial disability). For a correction that increases tax there is no claim deadline, but interest has run from the original due date; tell the user to file and pay promptly.

### Step 3 — Build column A from the return as currently adjusted

Copy each Form 1040-X line 1–23 amount from the filed return, then overlay every IRS adjustment and prior amendment. Example from the instructions: if the IRS added $10,000 of income making taxable income $100,000, column A shows $100,000, not the original figure. If original taxable income was $0 but the real figure was negative, column A line 5 shows the negative amount in parentheses.

### Step 4 — Prepare the corrected return for the amended year

Using that year's forms and instructions, rebuild every affected schedule: income lines, adjustments, the deduction (standard or Schedule A), QBI deduction, tax method, credits, other taxes (SE tax, Additional Medicare Tax, NIIT), and payments. Trace each change downstream. An AGI change can move charitable limits, taxable Social Security, credits with AGI phase-outs, and the premium tax credit (Instructions for Form 1040-X, line 1). A Schedule C change moves Schedule SE, the deductible half of SE tax, and QBI.

For paper filing the completed, updated Form 1040/1040-SR/1040-NR itself must be attached behind the 1040-X (new requirement in the December 2025 revision). For e-filing the software submits the full corrected return.

### Step 5 — Fill columns B and C

Column B = C − A for each changed line; enter decreases in parentheses. For an unchanged line, column C equals column A. Use the "which lines to complete" chart in [`references/line-by-line.md`](./references/line-by-line.md) to decide which lines to fill.

### Step 6 — Compute tax and the refund-or-owe section

Line 6 is the tax on line 5 column C using the method for that year (Tax Table, Tax Computation Worksheet, QDCGTW, Schedule D Tax Worksheet, Schedule J, Form 8615, FEITW), with the method code written on the dotted line. Then lines 7–23 per the line-by-line reference. Lines 18–21 reconcile against the original overpayment so dollars already refunded are not claimed twice.

### Step 7 — Complete Part I (dependents) if anything about dependents changed

Lines 25 and 27 counts in A/B/C; line 30 lists **all** dependents claimed on the amended return, including those already on the original.

### Step 8 — Write Part II

One paragraph per change: what changed, the line(s), the amount, why, and the attached schedule or document. Use the template in **Output format**. A vague explanation ("fixing my taxes") invites correspondence.

### Step 9 — Validate

Run every check in **Validation**. Surface failures; do not silently fix.

### Step 10 — Produce the deliverable

Fill the **Output format** template, including the attachment list and the statute result.

### Step 11 — Hand off to filing

Follow [`filing.md`](./filing.md) for the channel decision (e-file vs paper), the paper mailing address, payment of any balance, tracking with Where's My Amended Return, and consent and security rules. Remind the user to check whether the state return also needs amending.

---

## Line-by-line guidance

The full map is in [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

### Header

- **Year**: the calendar year (or fiscal year end) of the return being amended.
- **Names and SSNs**: same order as the original joint return. If changing from separate to joint and the spouse did not file, the filer's name goes first.
- **Address**: current address, even if it changed since filing.
- **Presidential Election Campaign**: a box can be checked only if no $3 designation was made before; allowed within 20½ months after the original due date; a prior designation cannot be undone.
- **Filing status**: check one box even if unchanged. Generally no change from joint to separate after the original due date. If MFS, enter the spouse's name (write "NRA" if the spouse has and needs no SSN/ITIN), unless amending a Form 1040-NR.

### Lines 1–5 (income and deductions)

- **Line 1**: AGI. Check the box if an NOL carryback is included.
- **Line 2**: itemized total or standard deduction for the amended year and filing status (age/blindness add-ons included).
- **Line 3**: line 1 − line 2.
- **Line 4a**: QBI deduction (Form 8995/8995-A for that year).
- **Line 4b**: Schedule 1-A deductions (tips, overtime, car loan interest, seniors). Schedule 1-A exists only from tax year 2025; enter 0 for earlier years. Attach Schedule 1-A when claiming.
- **Line 5**: line 3 − (4a + 4b). Columns A and B can be negative; column C is never below 0.

### Lines 6–11 (tax liability)

- **Line 6**: tax on line 5 column C; include Schedule 2 line 3 amounts; write the method code (Table, TCW, Sch D, Sch J, QDCGTW, FEITW, F8615).
- **Line 7**: nonrefundable credits (check the box if a general business credit carryback is included). Refigure credits when lines 1–6 changed.
- **Line 8**: line 6 − line 7, not below 0.
- **Line 9**: reserved. Leave blank.
- **Line 10**: other taxes (the Schedule 2 total for the year).
- **Line 11**: line 8 + line 10.

### Lines 12–17 (payments)

- **Line 12**: federal withholding plus excess Social Security/tier 1 RRTA. Attach new or corrected W-2s and any 1099-R showing withholding to the front.
- **Line 13**: estimated payments plus prior-year overpayment applied, plus any Form 1040-C balance paid.
- **Line 14**: earned income credit.
- **Line 15**: other refundable credits; check the boxes (Schedule 8812, 2439, 4136, 8863, 8885, 8962) and name others.
- **Line 16**: amount paid with an extension request, with the original return, and after filing. **Exclude interest, penalties, and card convenience fees.** Instructions example: $1,500 check that included a $100 estimated tax penalty → enter $1,400.
- **Line 17**: lines 12–15 column C plus line 16.

### Lines 18–23 (refund or amount owed)

- **Line 18**: overpayment shown on the original (plus any additional overpayment from an IRS change). Include it even if it was refunded or applied to next year's estimates.
- **Line 19**: line 17 − line 18. If negative, treat it as positive and add it to line 11 to get line 20.
- **Line 20**: amount owed = line 11 column C − line 19 when line 11 is larger.
- **Line 21**: overpayment on this amendment = line 19 − line 11 column C when line 19 is larger.
- **Line 22**: portion of line 21 refunded (sent separately from any original refund; paper 1040-X refunds come by check).
- **Line 23**: portion of line 21 applied to next year's estimated tax (irrevocable; no interest paid on it).

### Part I, Part II, Part III, signature

- Lines 24, 26, 28, 29 are reserved. Line 25 = children who lived with the filer more than half the year; line 27 = other dependents; line 30 = full dependent list.
- Part II is mandatory on every Form 1040-X.
- Part III (direct deposit, lines 31–33) exists only on the e-filed Form 1040-X for tax year 2021 and later; it is not on the paper PDF.
- Both spouses sign an amended joint return. Paper requires a handwritten signature. Enter the current IP PIN if one was issued.

### Amending a Form 1040-NR on paper

Per the instructions: enter name, current address, and SSN/ITIN on page 1 and nothing else on page 1; skip Part I; explain in Part II; complete a new or corrected return, write "Amended" across its top, and attach it behind the 1040-X. If e-filing a 1040-X for a 1040-NR, complete the 1040-X in full.

### Special situations from the instructions

- **Only information changes, no dollar amounts** (for example a dependent's details): complete the header, Presidential Election Campaign if applicable, Part I if a dependent changes, and Part II. Lines 1–23 stay blank.
- **Separate returns to a joint return**: column A = the filer's return as filed or adjusted; column B = the spouse's return amounts (or, if the spouse did not file, the spouse's income, deductions, credits, and taxes) plus any other changes; column C = A ± B; both spouses sign; Part II says "Changing the filing status".
- **Carryback claim** (NOL, credits, section 1256 losses): write "Carryback Claim" at the top of page 1; attach the computations listed in the instructions (for an NOL, Schedules A and B of Form 1045). A refund based on an NOL does not include self-employment tax on line 10. Form 1045 is the alternative, but it must be filed within 1 year after the end of the year in which the loss or credit arose.
- **Deceased taxpayer**: write "Deceased", the name, and the date of death across the top; a surviving spouse on a joint return signs and writes "Filing as surviving spouse"; any other claimant attaches Form 1310.
- **Household employment taxes**: attach a corrected Schedule H and give the date the error was discovered in Part II; changed wages also need Forms W-2c and W-3c filed with the SSA.
- **Additional Medicare Tax** changes: attach a corrected Form 8959 and the W-2 or W-2c.
- **Reportable transaction**: attach Form 8886.
- **BBA partner modification amended return**: write "BBA Partner Modification Amended Return" at the top and attach the statement the instructions require (source partnership name, TIN, audit control number). Refer this to a CPA.

Every special situation still requires the normal line entries unless the instructions say otherwise, and the IRS returns a Form 1040-X that is missing required forms or schedules.

---

## Validation

Run all checks. Surface failures to the user; never silently fix them.

### Math checks

- [ ] For every line: column C = column A + column B (decreases in parentheses).
- [ ] Line 3 = line 1 − line 2 (each column).
- [ ] Line 5 = line 3 − line 4a − line 4b; column C not below 0.
- [ ] Line 8 = line 6 − line 7, not below 0; line 11 = line 8 + line 10.
- [ ] Line 6 column C matches the tax method for the amended year (Tax Table row or worksheet), recomputed from line 5 column C.
- [ ] Line 17 = lines 12–15 column C + line 16.
- [ ] Line 19 = line 17 − line 18.
- [ ] Exactly one of line 20 or line 21 is positive (or both zero), and line 20 or line 21 equals |line 11 C − line 19|.
- [ ] Line 22 + line 23 = line 21.
- [ ] Cross-check: change in amount owed or refunded equals the change in total tax (line 11 B) minus the change in payments (lines 12–16 B), with the original overpayment accounted for on line 18.

### Sanity checks

- [ ] Column A matches the return as currently adjusted, not only the original PDF (ask about notices).
- [ ] The corrected Form 1040/1040-SR/1040-NR agrees line by line with column C.
- [ ] Every schedule the change touches was recomputed (SE tax, half-SE deduction, QBI, credits with AGI limits, taxable Social Security, Additional Medicare Tax).
- [ ] The amended year's rules were used (brackets, standard deduction, credit amounts), not the current year's.
- [ ] Line 16 contains no interest, penalty, or convenience fee.
- [ ] Line 18 includes the original overpayment even if it was applied to estimated tax.
- [ ] Filing status change is permitted (no MFJ → MFS after the due date).
- [ ] Retroactive CTC/EIC claims meet the SSN-issued-by-due-date rule.
- [ ] If line 21 > 0: the statute check passed and the refund requested on lines 22/23 does not exceed the lookback cap.
- [ ] Part II is specific and references attachments.
- [ ] Only one tax year per Form 1040-X.

### Cross-form checks

- [ ] State return impact flagged to the user.
- [ ] If the change affects next year (carryforwards, basis, estimated payments applied), the user is told which later return may also need amending.
- [ ] If tax increases, the user knows interest runs from the original due date and the IRS bills it separately (do not put it on the form).

---

## Output format

```markdown
# Form 1040-X — DRAFT amending tax year YYYY
Form revision used: Form 1040-X (Rev. December 2025)

## Header
Tax year amended: YYYY
Name(s) / SSN(s): <as on original, same order>
Current address: <address>
Presidential Election Campaign: <no change | You | Spouse>
Amended return filing status: <status> (original: <status>)

## Lines 1–23
| Line | Description | A. Original / as adjusted | B. Net change | C. Correct |
|---|---|---:|---:|---:|
| 1 | Adjusted gross income | | | |
| 2 | Itemized or standard deduction | | | |
| 3 | Line 1 − line 2 | | | |
| 4a | QBI deduction | | | |
| 4b | Schedule 1-A deductions | | | |
| 5 | Taxable income | | | |
| 6 | Tax (method: <Table/TCW/...>) | | | |
| 7 | Nonrefundable credits | | | |
| 8 | Line 6 − line 7 | | | |
| 9 | Reserved | — | — | — |
| 10 | Other taxes | | | |
| 11 | Total tax | | | |
| 12 | Withholding + excess SS/RRTA | | | |
| 13 | Estimated tax payments | | | |
| 14 | Earned income credit | | | |
| 15 | Refundable credits (<forms>) | | | |
| 16 | Paid with extension/original/after filing | | | (single amount) |
| 17 | Total payments | | | (single amount) |
| 18 | Overpayment on original / as adjusted | | | (single amount) |
| 19 | Line 17 − line 18 | | | (single amount) |
| 20 | Amount you owe | | | (single amount) |
| 21 | Overpayment on this return | | | (single amount) |
| 22 | Refunded to you | | | (single amount) |
| 23 | Applied to YYYY estimated tax | | | (single amount) |

## Part I — Dependents (or "No change")
## Part II — Explanation of changes
<Item 1: what changed, which lines, amount, reason, attached schedule/document>
<Item 2 ...>

## Statute check (refund claims)
- Original filed: <date> → deemed filed: <date> (reason)
- 3-year window ends: <date> | 2-year window from last payment ends: <date>
- Tax paid within lookback period: $X → maximum refundable: $X
- Result: timely / out of time / capped at $X

## Attachments
- Completed, updated Form <1040/1040-SR/1040-NR> for YYYY (paper: behind the 1040-X)
- Changed schedules/forms in attachment-sequence order: <list>
- Front of 1040-X: <new or corrected W-2/W-2c/1099-R with withholding/1042-S, if any>

## Filing channel
<e-file through software | paper to <address>> — reason per filing.md

## Validation summary
- Math: all checks passed | <failures>
- Sanity: <warnings>
- Next steps: pay balance / track at Where's My Amended Return after ~3 weeks / review state return

## Sources cited in this draft
- Form 1040-X (Rev. December 2025) and Instructions (Rev. December 2025)
- Form 1040 instructions for tax year YYYY (tax method and amounts)
- IRC §6511, §6513 (if a refund is claimed)
- <any other authority used>
```

The draft is not the filed form. Its value is that every line is traceable to the corrected return and every date in the statute check is sourced from the user's records.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Every header field, line 1–33, Part I–III, signature, the "which lines to complete" chart, and column rules, from the Rev. December 2025 PDF and instructions
- [`references/refund-statute.md`](./references/refund-statute.md) — IRC §6511/§6513 date math, lookback cap, special periods, and the procedure the agent runs
- [`references/when-not-to-amend.md`](./references/when-not-to-amend.md) — Decision table: math errors, missing forms, rejected e-files, CP2000, Form 843, Form 8379, superseding returns, carrybacks, state returns
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Frequent errors with the rule that prevents each
- [`filing.md`](./filing.md) — E-file vs paper decision tree, mailing addresses, payment, Where's My Amended Return tracking, consent and security rules

## Examples

- [`examples/missed-1099-nec-2024.md`](./examples/missed-1099-nec-2024.md) — 2024 return, late Form 1099-NEC: Schedule C, Schedule SE, and QBI recomputed; additional tax owed; e-filed in 2026
- [`examples/senior-deduction-refund-2025.md`](./examples/senior-deduction-refund-2025.md) — 2025 joint return that skipped the Schedule 1-A enhanced deduction for seniors; line 4b; refund by direct deposit
- [`examples/statute-cap-2022.md`](./examples/statute-cap-2022.md) — 2022 return already adjusted by a CP2000; 3-year window closed; 2-year window and §6511(b)(2)(B) cap limit the refund; paper filing

## Sources

Re-verify each item against irs.gov before relying on it; the form is continuous-use and the IRS pages change.

- [Amended Tax Return 2026: Form 1040-X, Deadlines, and Refund Tracking](https://jupid.com/blog/amended-tax-return-form-1040-x-2026) — companion guide for human readers
- [Form 1040-X (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/f1040x.pdf)
- [Instructions for Form 1040-X (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i1040x.pdf)
- [About Form 1040-X](https://www.irs.gov/forms-pubs/about-form-1040x) — revision check
- [File an amended return](https://www.irs.gov/filing/file-an-amended-return) — reviewed 30-Sep-2026
- [Amended return frequently asked questions](https://www.irs.gov/filing/amended-return-frequently-asked-questions) — e-file scope, three e-filed amendments, Form 8879, direct deposit; reviewed 02-Sep-2026
- [Where's My Amended Return?](https://www.irs.gov/filing/wheres-my-amended-return) — reviewed 02-Sep-2026
- [Topic No. 308, Amended returns](https://www.irs.gov/taxtopics/tc308) — reviewed 24-Sep-2026
- [Understanding your CP2000 notice](https://www.irs.gov/individuals/understanding-your-cp2000-notice) — reviewed 14-Jul-2026
- [Amending a return (video script)](https://www.irs.gov/newsroom/amending-a-return-youtube-video-text-script) — wait for the original refund; reviewed 14-Sep-2026
- [Publication 556](https://www.irs.gov/publications/p556) — claims for refund, financial disability
- [IRM 3.42.5.14.6](https://www.irs.gov/irm/part3/irm_03-042-005r) — perfection period for rejected e-filed returns
- [IRC §6511](https://www.law.cornell.edu/uscode/text/26/6511), [IRC §6513](https://www.law.cornell.edu/uscode/text/26/6513) — refund claim period and deemed filing/payment dates
- [Treas. Reg. §1.6664-2](https://www.law.cornell.edu/cfr/text/26/1.6664-2) — qualified amended return (accuracy-penalty context; refer to a CPA)
- Forms 1040 and instructions for the year being amended: [prior-year forms](https://www.irs.gov/prior-year-forms-and-instructions)

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions, and the Internal Revenue Code. It is not tax advice and does not create a CPA-client relationship. Remind the user that the draft is a starting point; statute questions, filing-status changes, carrybacks, and penalty relief warrant review by a licensed tax professional.
