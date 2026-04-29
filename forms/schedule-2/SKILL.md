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
  8959, 8960, 4137, 8919, 5329, 8606, 965-A and routes totals to Form
  1040 Lines 17 and 23. Do NOT use for Schedule 1 (additional income
  and adjustments — different schedule), Schedule 3 (additional credits
  and payments — different schedule), Form 5405 (first-time homebuyer
  credit repayment — has its own form), or any business-entity return.
form: Schedule 2 (Form 1040) — Additional Taxes
audience: [individual]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f1040s2.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
---

# Schedule 2 (Form 1040) — Additional Taxes

This skill produces an audit-grade draft of Schedule 2 by aggregating results from upstream tax forms (6251, 8962, Schedule SE, 8959, 8960, 4137, 8919, 5329, 8606, 965-A) and routing the totals to the right Form 1040 lines. Schedule 2 itself does almost no computation; it is a transcription and totaling exercise. The judgment is in identifying *which* upstream forms a filer needs and ensuring each upstream form is computed correctly before its number lands on Schedule 2.

The agent should not synthesize the upstream forms inside this skill. It should ask the user (or invoke the dedicated skill) for the result of each upstream form, then place that number on the right line.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule 2, "1040 Schedule 2", or "additional taxes" on the 1040
- The user has computed (or owes) any of: AMT (Form 6251), excess advance premium tax credit repayment (Form 8962), self-employment tax (Schedule SE), Additional Medicare Tax (Form 8959), Net Investment Income Tax (Form 8960), unreported social security/Medicare tax on tip or wage income (Form 4137 or 8919), additional 10% tax on early distributions from IRAs/qualified plans (Form 5329), or Section 965 deferred foreign income transition tax (Form 965-A)
- The user asks "where does my SE tax go on the 1040", "where does my Form 8962 repayment go", "where does AMT show up on the 1040"

Do **not** engage this skill when:

- The user is asking about Schedule 1 (additional income or above-the-line adjustments) — different schedule, use the `schedule-1` skill
- The user is asking about Schedule 3 (additional credits or payments such as Form 8962 *refundable* PTC, foreign tax credit, education credits, fuel tax credit, withholding) — different schedule, use the `schedule-3` skill (forthcoming)
- The user owes the first-time homebuyer credit repayment — that flows on Schedule 2 Line 10 from Form 5405; treat as a single-line input item, do not re-derive
- The user is filing a business entity return (Form 1065, 1120, 1120-S) — Schedule 2 is for Form 1040 only

If the user is unsure whether their tax belongs on Schedule 2 or Schedule 3, ask: "Is the amount you owe a tax (Schedule 2) or a credit/payment that reduces tax (Schedule 3)?" Schedule 2 is exclusively *taxes the filer owes in addition to regular income tax*.

For the upstream forms, prefer the dedicated skills when they exist:

- Self-employment tax → `schedule-se` skill (forthcoming)
- Additional Medicare Tax → `form-8959` skill
- Excess advance Premium Tax Credit repayment → `form-8962` skill
- Additional tax on IRAs and other qualified plans → `form-5329` skill
- AMT → `form-6251` skill (forthcoming)
- NIIT → `form-8960` skill (forthcoming)

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Schedule 2 line numbering and which lines are populated has been stable since the 2021 redesign; verify against the current-year form revision.
2. **Filer's legal name and SSN/ITIN.** Used in the Schedule 2 header. Do not invent.
3. **Whether the filer is subject to AMT** (Form 6251). If the filer's income, ISO exercises, large state-tax deductions, or large miscellaneous deductions trigger AMT, the result of Form 6251 Line 11 goes on Schedule 2 Line 1. Ask: "Have you computed Form 6251 (AMT)? If not, do you have ISO exercises, large state-and-local taxes, or AMT preference items?"
4. **Whether the filer received advance Premium Tax Credit (APTC)** for marketplace health insurance (Form 1095-A received). If yes, Form 8962 must be completed; the excess-APTC repayment from Form 8962 Line 29 goes on Schedule 2 Line 2. Ask: "Did you receive Form 1095-A from a Health Insurance Marketplace?"
5. **Whether the filer has self-employment income ≥ $400** (net earnings). If yes, Schedule SE is required; Schedule SE Line 12 goes on Schedule 2 Line 4.
6. **Whether the filer's Medicare wages + SE income exceeded the Additional Medicare Tax threshold** for their filing status. Thresholds are statutory under IRC §3101(b)(2): $200,000 single / HoH / QSS, $250,000 MFJ, $125,000 MFS. If exceeded, Form 8959 result goes on Schedule 2 Line 11.
7. **Whether the filer has investment income and MAGI above the NIIT threshold** under IRC §1411. Thresholds: $200,000 single / HoH / QSS, $250,000 MFJ / QSS, $125,000 MFS. If so, Form 8960 result goes on Schedule 2 Line 12.
8. **Whether the filer received tip income that wasn't reported to the employer** (Form 4137) or had wages from an employer who failed to withhold FICA when the filer should have been an employee (Form 8919). If yes, Form 4137 / 8919 results go on Schedule 2 Line 13.
9. **Whether the filer took early distributions from an IRA, 401(k), HSA, ABLE, MSA, Coverdell, or 529** (Form 5329) or made excess contributions or missed an RMD. If yes, Form 5329 result goes on Schedule 2 Line 8.
10. **Whether the filer has any of the less-common items** — Section 965 net tax (Form 965-A, Line 17a), HSA distribution recapture (Line 17c), recapture of various credits (Lines 17a–17z), look-back interest (Line 17g), etc. The instructions list ~20 specific items under Lines 17a–17z. Ask only if the filer mentions a triggering event.

For each upstream form result:
- Confirm the agent has either the completed upstream form OR explicit user-provided number plus source citation.
- Do not estimate. If the user says "I think I owe about $3,000 in SE tax" without a Schedule SE, redirect to the `schedule-se` skill first.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filer is filing Form 1040 (not 1040-NR or business return)

Schedule 2 attaches only to Form 1040, 1040-SR, or 1040-NR. Confirm filing the right return.

### Step 2 — Identify which Part I lines apply (Lines 1, 1a, 1b, 1c, 1d, 1e, 1f, 1g, 1h, 1m, 1n, 1q, 1y, 1z, 2, 3)

Part I covers two categories: **Tax (Line 1, AMT)** and **Excess advance premium tax credit repayment (Line 2)**. Line 3 totals Part I and flows to Form 1040 Line 17.

For Line 1 (AMT), if the user has Form 6251 with a positive amount on Line 11, transcribe that amount to Schedule 2 Line 1.

For Line 2 (Excess APTC repayment), if the user has Form 8962 Line 29 > 0, transcribe that amount to Schedule 2 Line 2. Note: the *refundable* PTC (Form 8962 Line 26) goes on Schedule 3 Line 9, not Schedule 2.

For 2026, post-OBBBA additions on Lines 1a–1h, 1m–1z (e.g., excess deferral recapture for QOZ, IRC §965(h) installment, etc.) — check the current-year form revision and instructions for the exact list.

Compute Line 3 = sum of Lines 1 and 2 (and any sub-lines specified by the current-year form).

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
| 10 | Repayment of first-time homebuyer credit | Form 5405 | "Did you claim the 2008 first-time homebuyer credit and now owe the annual installment?" |
| 11 | Additional Medicare Tax | Form 8959 | "Did your wages + SE income exceed your filing-status threshold?" |
| 12 | Net Investment Income Tax | Form 8960 | "Is your MAGI above the NIIT threshold and do you have investment income?" |
| 13 | Section 965 deferred foreign income — net tax | Form 965-A | "Do you have a Section 965 transition tax installment due?" |
| 14 | Interest on tax due on installment income from sale of certain residential lots and timeshares | (compute) | rare |
| 15 | Interest on the deferred tax on gain from certain installment sales > $150,000 | (compute) | rare |
| 16 | Recapture of low-income housing credit | Form 8611 | rare |
| 17 | Other additional taxes (list of ~25 sub-items 17a–17z) | various | ask only if triggered |
| 18 | Total of Lines 17a–17z | (computed) | — |
| 19 | Reserved for future use | — | leave blank |
| 20 | Section 965 net tax liability installment from Form 965-A | Form 965-A | rare |
| 21 | Total Part II = Lines 4 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 18 (do NOT include Line 20 in this total) | (computed) | flows to Form 1040 Line 23 |

For each "yes" answer, fetch the upstream form's result and place on the corresponding Schedule 2 line.

### Step 4 — Detail Line 17 (Other additional taxes) if applicable

Line 17 has subparts 17a–17z (some lines reserved). Each subpart corresponds to a specific recapture or additional tax. Common ones:

| Sub-line | Tax | Trigger |
|----------|-----|---------|
| 17a | Recapture of other credits (list each on the dotted line) | claimed a credit subject to recapture |
| 17c | HSA distribution not used for qualified medical expense (additional 20% tax) | non-qualified HSA distribution |
| 17d | Additional tax on Archer MSA distributions | rare |
| 17e | Additional tax on Medicare Advantage MSA distributions | rare |
| 17f | Recapture of charitable contribution deduction related to fractional interest in tangible personal property | rare |
| 17g | Income from look-back interest on installment sales | rare |
| 17h | Look-back interest under IRC §167(g) or §460(b) (long-term contracts) | rare |
| 17i | Interest on §72(p) loan from qualified plan | rare |
| 17j | Interest charge on accumulated income — undistributed capital gains of REITs/RICs | rare |
| 17k | ABLE account additional tax | non-qualified ABLE distribution |
| 17l | Recapture of federal mortgage subsidy | rare |
| 17m | Additional tax from Form 8889 (HSA) Line 17b | non-qualified HSA distribution |
| 17n | Recapture of Indian employment credit | rare |
| 17o–17z | Other items per current-year instructions (verify list) | — |

If the user identifies any item, transcribe the upstream amount and a 1-line description on the dotted line. Sum Lines 17a–17z to Line 18.

### Step 5 — Compute the totals

```
Line 3  = Line 1 + Line 2 (+ any 1a–1z sub-lines per current-year form)
            → flows to Form 1040 Line 17

Line 7  = Line 5 + Line 6
Line 18 = sum of Lines 17a–17z
Line 21 = Line 4 + Line 7 + Line 8 + Line 9 + Line 10 + Line 11 + Line 12
          + Line 13 + Line 14 + Line 15 + Line 16 + Line 18
            → flows to Form 1040 Line 23
```

Line 20 (Section 965 installment) reports separately and does not roll into Line 21 — it is paid via Form 965-A but tracked on the schedule. Verify against current-year form before including.

### Step 6 — Run validation checks

See **Validation** below.

### Step 7 — Produce the deliverable

See **Output format** below.

### Step 8 — Hand off downstream

State the next action items:

- **Line 3 amount** must be transcribed to **Form 1040 Line 17**
- **Line 21 amount** must be transcribed to **Form 1040 Line 23**
- **Each upstream form** (6251, 8962, SE, 8959, 8960, 5329, 4137, 8919, 8611, 965-A, etc.) must be **attached** to the return
- If the agent has not yet completed an upstream form, route the user to the dedicated skill for that form before finalizing Schedule 2

### Step 9 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md). Schedule 2 is filed as part of the Form 1040 return; it does not file separately.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name** — Filer's legal name as shown on Form 1040 (not business name)
- **SSN** — Filer's SSN or ITIN (matches Form 1040)

### Part I — Tax (Lines 1–3)

- **Line 1** — Alternative Minimum Tax. From Form 6251 Line 11. Zero if Form 6251 not required.
- **Line 1a–1z** — Sub-categories per current-year form revision (verify against the f1040s2 PDF)
- **Line 2** — Excess advance premium tax credit repayment. From Form 8962 Line 29.
- **Line 3** — Total. Sum of Line 1 (and any sub-lines) + Line 2. Flows to Form 1040 Line 17.

### Part II — Other Taxes (Lines 4–21)

- **Line 4** — SE tax. From Schedule SE Line 12.
- **Line 5** — SS/Medicare on unreported tips. From Form 4137 Line 13.
- **Line 6** — Uncollected SS/Medicare on wages. From Form 8919 Line 13.
- **Line 7** — Sum of Lines 5 + 6.
- **Line 8** — Additional tax on early/excess retirement plan transactions. From Form 5329 (Parts I, III, IV, V, VI, VII, VIII, IX as applicable).
- **Line 9** — Household employment taxes. From Schedule H.
- **Line 10** — Repayment of first-time homebuyer credit. From Form 5405. Taxpayers who bought before 2009 do not owe this; only 2008 buyers under the original credit.
- **Line 11** — Additional Medicare Tax. From Form 8959 Line 18.
- **Line 12** — Net Investment Income Tax. From Form 8960 Line 17.
- **Line 13** — Section 965 deferred foreign income net tax. From Form 965-A.
- **Line 14** — Interest on installment sales of residential lots and timeshares (IRC §453(l)(3)). Rare.
- **Line 15** — Interest on deferred tax on installment sales > $150,000 (IRC §453A). Rare.
- **Line 16** — Recapture of low-income housing credit. From Form 8611.
- **Line 17a–17z** — Other additional taxes (recaptures, HSA non-qualified distribution, ABLE non-qualified distribution, look-back interest, etc.). See Step 4 above and current-year instructions for the full list.
- **Line 18** — Sum of Lines 17a–17z.
- **Line 19** — Reserved.
- **Line 20** — Section 965 installment from Form 965-A (separate tracking).
- **Line 21** — Total Part II = Line 4 + Line 7 + Line 8 + Line 9 + Line 10 + Line 11 + Line 12 + Line 13 + Line 14 + Line 15 + Line 16 + Line 18. Flows to Form 1040 Line 23.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 3 = Line 1 + sub-lines of Line 1 + Line 2 (per current-year form)
- [ ] Line 7 = Line 5 + Line 6
- [ ] Line 18 = sum of Lines 17a through 17z
- [ ] Line 21 = Line 4 + Line 7 + Line 8 + Line 9 + Line 10 + Line 11 + Line 12 + Line 13 + Line 14 + Line 15 + Line 16 + Line 18
- [ ] Line 3 matches the amount transcribed on Form 1040 Line 17
- [ ] Line 21 matches the amount transcribed on Form 1040 Line 23

### Cross-form checks

- [ ] If Line 1 > 0 → Form 6251 attached
- [ ] If Line 2 > 0 → Form 8962 attached AND Form 1095-A is in the filer's records
- [ ] If Line 4 > 0 → Schedule SE attached
- [ ] If Line 5 > 0 → Form 4137 attached
- [ ] If Line 6 > 0 → Form 8919 attached
- [ ] If Line 8 > 0 → Form 5329 attached
- [ ] If Line 9 > 0 → Schedule H attached
- [ ] If Line 10 > 0 → Form 5405 attached
- [ ] If Line 11 > 0 → Form 8959 attached
- [ ] If Line 12 > 0 → Form 8960 attached
- [ ] If Line 13 > 0 or Line 20 > 0 → Form 965-A attached
- [ ] If Line 16 > 0 → Form 8611 attached

### Sanity checks (warnings, not blockers)

- [ ] Line 4 (SE tax) without any Schedule C, F, or partnership K-1 with self-employment earnings → confirm SE income source
- [ ] Line 11 (Additional Medicare Tax) with wages below $200,000 single → likely a calculation error; verify Form 8959
- [ ] Line 12 (NIIT) with no Schedule B/D investment income → verify the Form 8960 inputs
- [ ] Line 2 (excess APTC) and Schedule 3 Line 9 (refundable PTC) both > 0 → impossible; only one can be nonzero per filer
- [ ] Line 8 (Form 5329) without any IRA or pension income on Form 1040 → verify the trigger event
- [ ] Line 1 (AMT) very large compared to regular tax → confirm AMT was actually triggered, not just a worksheet artifact

---

## Output format

The agent's deliverable is a **filled draft** of Schedule 2 the user can transcribe to Form 1040 e-file software or paper. Format:

```markdown
# Schedule 2 (Form 1040) — DRAFT for tax year YYYY

## Header
Name(s) shown on Form 1040: <filer name>
Your social security number: <SSN>

## Part I — Tax
 1.  Alternative minimum tax. Attach Form 6251:           $X,XXX
 2.  Excess advance premium tax credit repayment.
     Attach Form 8962:                                    $X,XXX
 3.  Add lines 1 and 2. Enter here and on Form 1040,
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
10.  Repayment of first-time homebuyer credit.
     Attach Form 5405 if required:                        $X,XXX
11.  Additional Medicare Tax. Attach Form 8959:           $X,XXX
12.  Net investment income tax. Attach Form 8960:         $X,XXX
13.  Section 965 net tax liability. From Form 965-A:      $X,XXX
14.  Interest on tax due on installment income from sale
     of certain residential lots and timeshares:          $X,XXX
15.  Interest on the deferred tax on gain from certain
     installment sales > $150,000:                        $X,XXX
16.  Recapture of low-income housing credit.
     Attach Form 8611:                                    $X,XXX
17.  Other additional taxes:
   17a. Recapture of other credits (list):                $X,XXX
   17c. HSA distributions (Form 8889):                    $X,XXX
   17k. ABLE account distributions:                       $X,XXX
   17m. Form 8889 — HSA additional 20%:                   $X,XXX
   <other 17x lines as triggered>:                        $X,XXX
18.  Total Other Additional Taxes (sum of 17a–17z):       $X,XXX
19.  Reserved for future use:                             —
20.  Section 965 net tax liability installment from
     Form 965-A (does not roll into Line 21):             $X,XXX
21.  Add lines 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
     and 18. Enter here and on Form 1040, 1040-SR, or
     1040-NR, line 23:                                    $X,XXX

## Form 1040 routing
Form 1040 Line 17 (from Schedule 2 Line 3):               $X,XXX
Form 1040 Line 23 (from Schedule 2 Line 21):              $X,XXX

## Required upstream forms attached
- [ ] Form 6251 (if Line 1 > 0)
- [ ] Form 8962 + 1095-A in records (if Line 2 > 0)
- [ ] Schedule SE (if Line 4 > 0)
- [ ] Form 4137 (if Line 5 > 0)
- [ ] Form 8919 (if Line 6 > 0)
- [ ] Form 5329 (if Line 8 > 0)
- [ ] Schedule H (if Line 9 > 0)
- [ ] Form 5405 (if Line 10 > 0)
- [ ] Form 8959 (if Line 11 > 0)
- [ ] Form 8960 (if Line 12 > 0)
- [ ] Form 965-A (if Line 13 or Line 20 > 0)
- [ ] Form 8611 (if Line 16 > 0)
- [ ] Form 8889 (if Line 17c or 17m > 0)

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
- [`references/line-17-subitems.md`](./references/line-17-subitems.md) — Full list of Line 17a–17z sub-items with triggers and citations
- [`references/amt-and-niit-thresholds.md`](./references/amt-and-niit-thresholds.md) — AMT exemption amounts, NIIT thresholds, Additional Medicare Tax thresholds (year-aware)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 8–12 audit-trip mistakes filers make on Schedule 2

## Examples

End-to-end worked Schedule 2s. Use these as patterns when the user's situation is similar.

- [`examples/high-earner-amt.md`](./examples/high-earner-amt.md) — High-income filer with ISO exercise triggering AMT (Line 1)
- [`examples/freelancer-se-and-add-medicare.md`](./examples/freelancer-se-and-add-medicare.md) — Sole prop with SE tax + Additional Medicare Tax (Lines 4 + 11)
- [`examples/aca-excess-aptc.md`](./examples/aca-excess-aptc.md) — Marketplace enrollee whose income spiked, owing excess APTC repayment (Line 2)

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

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
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025 (AMT exemption, etc.); verify the 2026 successor Revenue Procedure before filing 2026 returns

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
