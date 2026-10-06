---
name: schedule-2
description: >
  Use this skill when an individual filer needs to complete IRS Schedule 2
  (Form 1040), Additional Taxes. Triggers on phrases like "Schedule 2",
  "additional taxes on tax return", "where do I put AMT on 1040", "where
  does SE tax go on 1040", "Form 8962 result on 1040", "Form 8959
  result on 1040", "NIIT line on 1040", "additional tax on early IRA
  withdrawal", "excess advance premium tax credit repayment". Schedule 2
  is a router: it aggregates results from Forms 6251, 8962, Schedule SE,
  8959, 8960, 4137, 8919, 5329, 8889, 965-A and routes totals to Form
  1040 Lines 17 and 23. Do NOT use for Schedule 1 (additional income
  and adjustments — different schedule), Schedule 3 (additional credits
  and payments — different schedule), Form 5405 (first-time homebuyer
  credit repayment — has its own form), or any business-entity return.
form: Schedule 2 (Form 1040) — Additional Taxes
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040s2.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
---

# Schedule 2 (Form 1040) — Additional Taxes

This skill produces an audit-grade draft of Schedule 2 by aggregating results from upstream tax forms (6251, 8962, Schedule SE, 8959, 8960, 4137, 8919, 5329, 8889, 965-A) and routing the totals to the right Form 1040 lines. Schedule 2 itself does almost no computation; it is a transcription and totaling exercise. The judgment is in identifying *which* upstream forms a filer needs and ensuring each upstream form is computed correctly before its number lands on Schedule 2.

The agent should not synthesize the upstream forms inside this skill. It should ask the user (or invoke the dedicated skill) for the result of each upstream form, then place that number on the right line.

**Companion guide for end users:** [Schedule 2 (Form 1040) 2026: Additional Taxes Explained Line by Line](https://jupid.com/blog/schedule-2-additional-taxes-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule 2, "1040 Schedule 2", or "additional taxes" on the 1040
- The user has computed (or owes) any of: AMT (Form 6251), excess advance premium tax credit repayment (Form 8962), self-employment tax (Schedule SE), Additional Medicare Tax (Form 8959), Net Investment Income Tax (Form 8960), unreported social security/Medicare tax on tip or wage income (Form 4137 or 8919), additional 10% tax on early distributions from IRAs/qualified plans (Form 5329), or Section 965 deferred foreign income transition tax (Form 965-A)
- The user asks "where does my SE tax go on the 1040", "where does my Form 8962 repayment go", "where does AMT show up on the 1040"

Do **not** engage this skill when:

- The user is asking about Schedule 1 (additional income or above-the-line adjustments) — different schedule, use the `schedule-1` skill
- The user is asking about Schedule 3 (additional credits or payments such as Form 8962 *refundable* PTC, foreign tax credit, education credits, fuel tax credit, withholding) — different schedule, use the `schedule-3` skill (forthcoming)
- The user says they owe a first-time homebuyer credit repayment — Line 10 is "Reserved for future use" on the 2025 Schedule 2; the last annual installment of the 2008 credit was reported on 2024 returns (Form 5405, Rev. November 2024, points to the 2024 Schedule 2 line 10). Stop and refer the user to a CPA rather than placing an amount
- The user is filing a business entity return (Form 1065, 1120, 1120-S) — Schedule 2 is for Form 1040 only

If the user is unsure whether their tax belongs on Schedule 2 or Schedule 3, ask: "Is the amount you owe a tax (Schedule 2) or a credit/payment that reduces tax (Schedule 3)?" Schedule 2 is exclusively *taxes the filer owes in addition to regular income tax*.

For the upstream forms, prefer the dedicated skills when they exist:

- Self-employment tax → [`schedule-se`](../schedule-se/SKILL.md) skill
- Additional Medicare Tax → `form-8959` skill
- Excess advance Premium Tax Credit repayment → `form-8962` skill
- Additional tax on IRAs and other qualified plans → `form-5329` skill
- AMT → `form-6251` skill (forthcoming)
- NIIT → `form-8960` skill (forthcoming)

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. This skill's line map is verified against the **2025 Schedule 2 (Form 1040), filed in 2026**: Part I = lines 1a–1f, 1y, 1z (additions to tax), 2 (AMT), 3; Part II = lines 4–21, with line 10 reserved, line 13 = uncollected social security and Medicare or RRTA tax on tips or group-term life insurance (Form W-2 box 12), and line 19 = recapture of net EPE from Form 4255. Re-check the next revision at https://www.irs.gov/forms-pubs/about-schedule-2-form-1040 before use.
2. **Filer's legal name and SSN/ITIN.** Used in the Schedule 2 header. Do not invent.
3. **Whether the filer is subject to AMT** (Form 6251). If the filer's income, ISO exercises, large state-tax deductions, or large miscellaneous deductions trigger AMT, the result of Form 6251 Line 11 goes on Schedule 2 Line 2. Ask: "Have you computed Form 6251 (AMT)? If not, do you have ISO exercises, large state-and-local taxes, or AMT preference items?"
4. **Whether the filer received advance Premium Tax Credit (APTC)** for marketplace health insurance (Form 1095-A received). If yes, Form 8962 must be completed; the excess-APTC repayment from Form 8962 Line 29 goes on Schedule 2 Line 1a. For 2025 returns the repayment is capped by Table 5 of the Form 8962 instructions when household income is under 400% of the federal poverty line; for tax years after 2025 there is no repayment cap (P.L. 119-21; IRS Premium Tax Credit Q&A, Q31). Ask: "Did you receive Form 1095-A from a Health Insurance Marketplace?"
5. **Whether the filer has self-employment income ≥ $400** (net earnings). If yes, Schedule SE is required; Schedule SE Line 12 goes on Schedule 2 Line 4.
6. **Whether the filer's Medicare wages + SE income exceeded the Additional Medicare Tax threshold** for their filing status. Thresholds are statutory under IRC §3101(b)(2): $200,000 single / HoH / QSS, $250,000 MFJ, $125,000 MFS. If exceeded, Form 8959 result goes on Schedule 2 Line 11.
7. **Whether the filer has investment income and MAGI above the NIIT threshold** under IRC §1411. Thresholds: $200,000 single / HoH, $250,000 MFJ / QSS, $125,000 MFS. If so, Form 8960 result goes on Schedule 2 Line 12.
8. **Whether the filer received tip income that wasn't reported to the employer** (Form 4137) or had wages from an employer who failed to withhold FICA when the filer should have been an employee (Form 8919). If yes, Form 4137 goes on Schedule 2 Line 5 and Form 8919 on Line 6. Uncollected social security and Medicare (or RRTA) tax on tips or group-term life insurance shown in Form W-2 box 12 (codes A and B, or M and N) goes on Line 13.
9. **Whether the filer took an early distribution from an IRA or other qualified plan, a taxable distribution from a Coverdell ESA, 529 plan, or ABLE account, made excess contributions to an IRA, Coverdell ESA, Archer MSA, HSA, or ABLE account, or missed an RMD** (Form 5329). If yes, Form 5329 result goes on Schedule 2 Line 8. The 20% additional tax on a non-qualified HSA distribution is NOT Line 8: it comes from Form 8889 line 17b and goes on Line 17c.
10. **Whether the filer has any of the less-common items** — clean vehicle credit transferred to a dealer that must be repaid (Lines 1b/1c), elective payment election items from Form 4255 (Lines 1d–1f, 1y, 19), Section 965 installment (Form 965-A, Line 20), HSA additional taxes (Lines 17c/17d), recapture of other credits (Line 17a), look-back interest (Line 17n), etc. The 2025 instructions list 17a–17q plus 17z. Ask only if the filer mentions a triggering event.

For each upstream form result:
- Confirm the agent has either the completed upstream form OR explicit user-provided number plus source citation.
- Do not estimate. If the user says "I think I owe about $3,000 in SE tax" without a Schedule SE, redirect to the `schedule-se` skill first.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filer is filing Form 1040 (not 1040-NR or business return)

Schedule 2 attaches only to Form 1040, 1040-SR, or 1040-NR. Confirm filing the right return.

### Step 2 — Identify which Part I lines apply (Lines 1a, 1b, 1c, 1d, 1e, 1f, 1y, 1z, 2, 3)

Part I covers **additions to tax (Lines 1a–1z)** and the **alternative minimum tax (Line 2)**. Line 3 totals Part I and flows to Form 1040 Line 17.

| Line | Item | Source |
|------|------|--------|
| 1a | Excess advance premium tax credit repayment | Form 8962 Line 29 |
| 1b | Repayment of new clean vehicle credit transferred to a registered dealer | Schedule A (Form 8936), Part II (amount from Part I line 4a) |
| 1c | Repayment of previously owned clean vehicle credit transferred to a registered dealer | Schedule A (Form 8936), Part IV |
| 1d | Recapture of net elective payment election (EPE) | Form 4255, line 2a, column (l) |
| 1e | Excessive payments (EPs) on gross EPE (check the box for the Form 4255 line) | Form 4255, column (n)(1) |
| 1f | 20% EP (check the box) | Form 4255, column (n)(3) |
| 1y | Other additions to tax (e.g., "ARPCR" recapture of the alternative fuel vehicle refueling property credit from Form 8911; Form 8933 / Form 4255 items) | Per 2025 Schedule 2 instructions |
| 1z | Add Lines 1a through 1y | Computed |
| 2 | Alternative minimum tax | Form 6251 Line 11 |

For Line 1a, if the user has Form 8962 Line 29 > 0, transcribe that amount. Note: the *net* PTC (Form 8962 Line 26) goes on Schedule 3 Line 9, not Schedule 2.

For Line 2 (AMT), if the user has Form 6251 with a positive amount on Line 11, transcribe that amount to Schedule 2 Line 2.

Compute Line 3 = Line 1z + Line 2.

### Step 3 — Identify which Part II lines apply (Lines 4–21)

Part II covers all "other taxes". Walk each line with a yes/no question:

| Line | Tax | Source form | Question to ask |
|------|-----|-------------|-----------------|
| 4 | Self-employment tax | Schedule SE Line 12 | "Did you have self-employment income ≥ $400 net?" |
| 5 | Social security and Medicare tax on unreported tip income | Form 4137 | "Did you receive tip income that you didn't report to your employer?" |
| 6 | Uncollected SS and Medicare on wages | Form 8919 | "Were you treated as an independent contractor when you should have been an employee?" |
| 7 | Total of Lines 5 + 6 | (computed) | — |
| 8 | Additional tax on IRAs / other qualified retirement plans | Form 5329 | "Did you take an early distribution, miss an RMD, or make an excess contribution to an IRA, 401(k), HSA, MSA, Coverdell, or 529?" |
| 9 | Household employment taxes | Schedule H | "Did you pay a household employee (nanny, housekeeper, eldercare worker) ≥ the FICA wage threshold?" |
| 10 | Reserved for future use (2025 revision) | — | leave blank |
| 11 | Additional Medicare Tax | Form 8959 | "Did your wages + SE income exceed your filing-status threshold?" |
| 12 | Net Investment Income Tax | Form 8960 | "Is your MAGI above the NIIT threshold and do you have investment income?" |
| 13 | Uncollected social security and Medicare or RRTA tax on tips or group-term life insurance | Form W-2 box 12, codes A and B or M and N | "Does your W-2 box 12 show code A, B, M, or N?" |
| 14 | Interest on tax due on installment income from sale of certain residential lots and timeshares | (compute) | rare |
| 15 | Interest on the deferred tax on gain from certain installment sales > $150,000 | (compute) | rare |
| 16 | Recapture of low-income housing credit | Form 8611 | rare |
| 17 | Other additional taxes (sub-items 17a–17q and 17z) | various | ask only if triggered |
| 18 | Total of Lines 17a–17z | (computed) | — |
| 19 | Recapture of net EPE (Form 3468 Part IV credit) | Form 4255, line 1d, column (l) | rare |
| 20 | Section 965 net tax liability installment from Form 965-A | Form 965-A | rare |
| 21 | Total Part II = Lines 4 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 18 + 19 (Line 10 is reserved; do NOT include Line 20) | (computed) | flows to Form 1040 Line 23 (1040-NR Line 23b) |

For each "yes" answer, fetch the upstream form's result and place on the corresponding Schedule 2 line.

### Step 4 — Detail Line 17 (Other additional taxes) if applicable

Line 17 has subparts 17a–17q and 17z on the 2025 form. Each subpart corresponds to a specific recapture or additional tax:

| Sub-line | Tax | Source / trigger |
|----------|-----|---------|
| 17a | Recapture of other credits (list type and amount) | Form 4255 items, new markets credit (Form 8874), employer-provided childcare facilities credit (Form 8882), §6418(g)(3) amounts |
| 17b | Recapture of federal mortgage subsidy | Form 8828; home sold in the year |
| 17c | Additional 20% tax on HSA distributions | Form 8889 line 17b |
| 17d | Additional tax on an HSA because the user didn't remain an eligible individual | Form 8889 line 21 |
| 17e | Additional tax on Archer MSA distributions | Form 8853 line 9b |
| 17f | Additional tax on Medicare Advantage MSA distributions | Form 8853 line 13b |
| 17g | Recapture of a charitable contribution deduction (fractional interest in tangible personal property) | Pub. 526 |
| 17h | Nonqualified deferred compensation that fails §409A (20% + interest) | W-2 box 12 code Z or Form 1099-MISC box 15 |
| 17i | Nonqualified deferred compensation under §457A (20% + interest) | rare |
| 17j | §72(m)(5) excess benefits tax | Pub. 560 |
| 17k | Golden parachute payments (20% excise) | W-2 box 12 code K or 20% of Form 1099-NEC box 3 |
| 17l | Tax on accumulation distribution of trusts | Form 4970 |
| 17m | Excise tax on insider stock compensation from an expatriated corporation | §4985 |
| 17n | Look-back interest under §167(g) or §460(b) | Form 8697 or 8866 |
| 17o | Tax on non-effectively connected income for any part of the year as a nonresident alien | Form 1040-NR |
| 17p | Interest from Form 8621, line 16f (§1291 fund) | Form 8621 |
| 17q | Interest from Form 8621, line 24 | Form 8621 |
| 17z | Any other taxes (list type and amount; e.g., PWA penalties from Form 4255, negative Form 8978 adjustment) | 2025 Schedule 2 instructions |

If the user identifies any item, transcribe the upstream amount and a 1-line description on the dotted line. Sum Lines 17a–17z to Line 18.

### Step 5 — Compute the totals

```
Line 1z = Lines 1a through 1y
Line 3  = Line 1z + Line 2
            → flows to Form 1040 Line 17

Line 7  = Line 5 + Line 6
Line 18 = sum of Lines 17a–17z
Line 21 = Line 4 + Lines 7 through 16 + Line 18 + Line 19
          (Line 10 is reserved and blank on the 2025 form)
            → flows to Form 1040 Line 23 (Form 1040-NR Line 23b)
```

Line 20 (Section 965 installment) is reported separately and does not roll into Line 21 (2025 Schedule 2, line 21 instruction: "Add lines 4, 7 through 16, 18, and 19").

### Step 6 — Run validation checks

See **Validation** below.

### Step 7 — Produce the deliverable

See **Output format** below.

### Step 8 — Hand off downstream

State the next action items:

- **Line 3 amount** must be transcribed to **Form 1040 Line 17**
- **Line 21 amount** must be transcribed to **Form 1040 Line 23**
- **Each upstream form** (6251, 8962, SE, 8959, 8960, 5329, 4137, 8919, 8611, 8889, 965-A, etc.) must be **attached** to the return
- If the agent has not yet completed an upstream form, route the user to the dedicated skill for that form before finalizing Schedule 2

### Step 9 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md). Schedule 2 is filed as part of the Form 1040 return; it does not file separately.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name** — Filer's legal name as shown on Form 1040 (not business name)
- **SSN** — Filer's SSN or ITIN (matches Form 1040)

### Part I — Tax (Lines 1a–3)

- **Line 1a** — Excess advance premium tax credit repayment. From Form 8962 Line 29.
- **Lines 1b–1c** — Repayment of clean vehicle credits transferred to a dealer. From Schedule A (Form 8936), Parts II and IV.
- **Lines 1d–1f** — Elective payment election recapture and excessive payments. From Form 4255.
- **Line 1y** — Other additions to tax listed in the instructions. **Line 1z** — Add Lines 1a through 1y.
- **Line 2** — Alternative Minimum Tax. From Form 6251 Line 11. Zero if Form 6251 not required.
- **Line 3** — Total. Line 1z + Line 2. Flows to Form 1040 Line 17.

### Part II — Other Taxes (Lines 4–21)

- **Line 4** — SE tax. From Schedule SE Line 12.
- **Line 5** — SS/Medicare on unreported tips. From Form 4137 Line 13.
- **Line 6** — Uncollected SS/Medicare on wages. From Form 8919 Line 13.
- **Line 7** — Sum of Lines 5 + 6.
- **Line 8** — Additional tax on early/excess retirement plan transactions. From Form 5329 (Parts I, III, IV, V, VI, VII, VIII, IX as applicable).
- **Line 9** — Household employment taxes. From Schedule H.
- **Line 10** — Reserved for future use on the 2025 revision (it carried the first-time homebuyer credit repayment through 2024 returns). Leave blank.
- **Line 11** — Additional Medicare Tax. From Form 8959 Line 18.
- **Line 12** — Net Investment Income Tax. From Form 8960 Line 17.
- **Line 13** — Uncollected social security and Medicare or RRTA tax on tips or group-term life insurance. From Form W-2 box 12, codes A and B or M and N.
- **Line 14** — Interest on installment sales of residential lots and timeshares (IRC §453(l)(3)). Rare.
- **Line 15** — Interest on deferred tax on installment sales > $150,000 (IRC §453A). Rare.
- **Line 16** — Recapture of low-income housing credit. From Form 8611 line 14.
- **Line 17a–17z** — Other additional taxes (credit recaptures, HSA additional taxes, §409A/§457A, golden parachute, look-back interest, Form 8621 interest, etc.). See Step 4 above and [`references/line-17-subitems.md`](./references/line-17-subitems.md).
- **Line 18** — Sum of Lines 17a–17z.
- **Line 19** — Recapture of net EPE from Form 4255, line 1d, column (l).
- **Line 20** — Section 965 net tax liability installment from Form 965-A (not added to Line 21).
- **Line 21** — Total Part II = Line 4 + Lines 7 through 16 + Line 18 + Line 19. Flows to Form 1040 Line 23.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 1z = sum of Lines 1a through 1y
- [ ] Line 3 = Line 1z + Line 2
- [ ] Line 7 = Line 5 + Line 6
- [ ] Line 18 = sum of Lines 17a through 17z
- [ ] Line 21 = Line 4 + Line 7 + Line 8 + Line 9 + Line 10 + Line 11 + Line 12 + Line 13 + Line 14 + Line 15 + Line 16 + Line 18 + Line 19 (Line 10 blank; Line 20 excluded)
- [ ] Line 3 matches the amount transcribed on Form 1040 Line 17
- [ ] Line 21 matches the amount transcribed on Form 1040 Line 23

### Cross-form checks

- [ ] If Line 1a > 0 → Form 8962 attached AND Form 1095-A is in the filer's records
- [ ] If Line 1b or 1c > 0 → Form 8936 and Schedule A (Form 8936) attached
- [ ] If any of Lines 1d–1f or 19 > 0 → Form 4255 attached
- [ ] If Line 2 > 0 → Form 6251 attached
- [ ] If Line 4 > 0 → Schedule SE attached
- [ ] If Line 5 > 0 → Form 4137 attached
- [ ] If Line 6 > 0 → Form 8919 attached
- [ ] If Line 8 > 0 → Form 5329 attached
- [ ] If Line 9 > 0 → Schedule H attached
- [ ] Line 10 is blank (reserved on the 2025 form)
- [ ] If Line 11 > 0 → Form 8959 attached
- [ ] If Line 12 > 0 → Form 8960 attached
- [ ] If Line 13 > 0 → Form W-2 box 12 shows codes A/B or M/N
- [ ] If Line 20 > 0 → Form 965-A attached
- [ ] If Line 16 > 0 → Form 8611 attached
- [ ] If Line 17c or 17d > 0 → Form 8889 attached

### Sanity checks (warnings, not blockers)

- [ ] Line 4 (SE tax) without any Schedule C, F, or partnership K-1 with self-employment earnings → confirm SE income source
- [ ] Line 11 (Additional Medicare Tax) with wages below $200,000 single → likely a calculation error; verify Form 8959
- [ ] Line 12 (NIIT) with no Schedule B/D investment income → verify the Form 8960 inputs
- [ ] Line 1a (excess APTC) and Schedule 3 Line 9 (net PTC) both > 0 → impossible; only one can be nonzero per filer
- [ ] Line 8 (Form 5329) without any IRA or pension income on Form 1040 → verify the trigger event
- [ ] Line 2 (AMT) very large compared to regular tax → confirm AMT was actually triggered, not just a worksheet artifact

---

## Output format

The agent's deliverable is a **filled draft** of Schedule 2 the user can transcribe to Form 1040 e-file software or paper. Format:

```markdown
# Schedule 2 (Form 1040) — DRAFT for tax year YYYY

## Header
Name(s) shown on Form 1040: <filer name>
Your social security number: <SSN>

## Part I — Tax
 1a. Excess advance premium tax credit repayment.
     Attach Form 8962:                                    $X,XXX
 1b. Repayment of new clean vehicle credit(s):            $X,XXX
 1c. Repayment of previously owned clean vehicle
     credit(s):                                           $X,XXX
 1d. Recapture of net EPE from Form 4255:                 $X,XXX
 1e. Excessive payments (EPs) on gross EPE:               $X,XXX
 1f. 20% EP from Form 4255:                               $X,XXX
 1y. Other additions to tax (type):                       $X,XXX
 1z. Add lines 1a through 1y:                             $X,XXX
 2.  Alternative minimum tax. Attach Form 6251:           $X,XXX
 3.  Add lines 1z and 2. Enter here and on Form 1040,
     1040-SR, or 1040-NR, line 17:                        $X,XXX

## Part II — Other Taxes
 4.  Self-employment tax. Attach Schedule SE:             $X,XXX
 5.  Social security and Medicare tax on unreported
     tip income. Attach Form 4137:                        $X,XXX
 6.  Uncollected social security and Medicare tax on
     wages. Attach Form 8919:                             $X,XXX
 7.  Total additional social security and Medicare tax.
     Add lines 5 and 6:                                   $X,XXX
 8.  Additional tax on IRAs or other tax-favored accounts.
     Attach Form 5329 if required:                        $X,XXX
 9.  Household employment taxes. Attach Schedule H:       $X,XXX
10.  Reserved for future use:                             —
11.  Additional Medicare Tax. Attach Form 8959:           $X,XXX
12.  Net investment income tax. Attach Form 8960:         $X,XXX
13.  Uncollected social security and Medicare or RRTA
     tax on tips or group-term life insurance (W-2
     box 12):                                             $X,XXX
14.  Interest on tax due on installment income from sale
     of certain residential lots and timeshares:          $X,XXX
15.  Interest on the deferred tax on gain from certain
     installment sales > $150,000:                        $X,XXX
16.  Recapture of low-income housing credit.
     Attach Form 8611:                                    $X,XXX
17.  Other additional taxes:
   17a. Recapture of other credits (list):                $X,XXX
   17c. Additional tax on HSA distributions (Form 8889):  $X,XXX
   17d. HSA — not remaining an eligible individual:       $X,XXX
   <other 17x lines as triggered>:                        $X,XXX
18.  Total additional taxes (sum of 17a–17z):             $X,XXX
19.  Recapture of net EPE from Form 4255, line 1d:        $X,XXX
20.  Section 965 net tax liability installment from
     Form 965-A (does not roll into Line 21):             $X,XXX
21.  Add lines 4, 7 through 16, 18, and 19. Enter here
     and on Form 1040 or 1040-SR, line 23 (1040-NR,
     line 23b):                                           $X,XXX

## Form 1040 routing
Form 1040 Line 17 (from Schedule 2 Line 3):               $X,XXX
Form 1040 Line 23 (from Schedule 2 Line 21):              $X,XXX

## Required upstream forms attached
- [ ] Form 8962 + 1095-A in records (if Line 1a > 0)
- [ ] Form 6251 (if Line 2 > 0)
- [ ] Schedule SE (if Line 4 > 0)
- [ ] Form 4137 (if Line 5 > 0)
- [ ] Form 8919 (if Line 6 > 0)
- [ ] Form 5329 (if Line 8 > 0)
- [ ] Schedule H (if Line 9 > 0)
- [ ] Form 8959 (if Line 11 > 0)
- [ ] Form 8960 (if Line 12 > 0)
- [ ] Form 965-A (if Line 20 > 0)
- [ ] Form 8611 (if Line 16 > 0)
- [ ] Form 8889 (if Line 17c or 17d > 0)

## Validation summary
- Math: all checks passed | <list failures>
- Cross-form: <list missing attachments>
- Sanity: <list warnings raised>

## Sources cited in this draft
- IRS Form 1040 Schedule 2 (revision date YYYY-MM-DD)
- IRS Instructions for Form 1040 and 1040-SR (revision date YYYY-MM-DD), Schedule 2 section
- IRC §55 (AMT), §1401 (SE tax), §1411 (NIIT), §3101(b)(2) (Additional Medicare Tax), §36B (PTC), §72(t) (early distribution additional tax), §965 (transition tax)
- (any other authority used for upstream forms)
```

The draft is a transcription tool. Every nonzero line has a corresponding upstream form attachment. The deliverable's value is that every line is sourced and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Schedule 2 line with source form, statutory citation, and edge cases
- [`references/upstream-forms.md`](./references/upstream-forms.md) — Decision tree for which upstream forms a filer needs and how each result lands on Schedule 2
- [`references/line-17-subitems.md`](./references/line-17-subitems.md) — Full list of Line 17a–17q and 17z sub-items with triggers and citations
- [`references/amt-and-niit-thresholds.md`](./references/amt-and-niit-thresholds.md) — AMT exemption amounts, NIIT thresholds, Additional Medicare Tax thresholds (year-aware)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 8–12 audit-trip mistakes filers make on Schedule 2

## Examples

End-to-end worked Schedule 2s. Use these as patterns when the user's situation is similar.

- [`examples/high-earner-amt.md`](./examples/high-earner-amt.md) — High-income filer with ISO exercise triggering AMT (Line 2)
- [`examples/freelancer-se-and-add-medicare.md`](./examples/freelancer-se-and-add-medicare.md) — Sole prop with SE tax + Additional Medicare Tax (Lines 4 + 11)
- [`examples/aca-excess-aptc.md`](./examples/aca-excess-aptc.md) — Marketplace enrollee whose income spiked, owing excess APTC repayment (Line 1a)

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [Schedule 2 (Form 1040) 2026: Additional Taxes Explained Line by Line](https://jupid.com/blog/schedule-2-additional-taxes-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1040 Schedule 2 (latest)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) — the form itself
- [Instructions for Form 1040 and 1040-SR (includes Schedule 2 instructions)](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — line-by-line IRS guidance
- [About Schedule 2 (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-2-form-1040) — IRS landing page with archive of past revisions
- [Form 6251 Instructions](https://www.irs.gov/pub/irs-pdf/i6251.pdf) — AMT
- [Form 8962 Instructions](https://www.irs.gov/pub/irs-pdf/i8962.pdf) — Premium Tax Credit
- [Schedule SE Instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf) — Self-employment tax
- [Form 8959 Instructions](https://www.irs.gov/pub/irs-pdf/i8959.pdf) — Additional Medicare Tax
- [Form 8960 Instructions](https://www.irs.gov/pub/irs-pdf/i8960.pdf) — NIIT
- [Form 5329 Instructions](https://www.irs.gov/pub/irs-pdf/i5329.pdf) — Additional taxes on qualified plans
- [Form 4137](https://www.irs.gov/pub/irs-pdf/f4137.pdf) — Unreported tips
- [Form 8919](https://www.irs.gov/pub/irs-pdf/f8919.pdf) — Uncollected SS/Medicare on wages
- [Form 5405](https://www.irs.gov/pub/irs-pdf/f5405.pdf) — First-time homebuyer credit repayment
- [Schedule H Instructions](https://www.irs.gov/pub/irs-pdf/i1040sh.pdf) — Household employment taxes
- IRC §55 (AMT), §59 (AMT-related), §1401 (SE tax rate), §1411 (NIIT), §36B (PTC), §3101(b)(2) (Additional Medicare Tax), §72(t) (early distribution additional tax), §965 (transition tax), §453(l)(3), §453A (installment sale interest)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025 (AMT exemption, etc.); Rev. Proc. 2025-32 — tax year 2026 (AMT exemption $90,100 / $140,200, phaseout from $500,000 / $1,000,000)
- [IRS Questions and answers on the Premium Tax Credit](https://www.irs.gov/affordable-care-act/individuals-and-families/questions-and-answers-on-the-premium-tax-credit) — no excess-APTC repayment cap for tax years after 2025 (Q31)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
