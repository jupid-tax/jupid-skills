---
name: form-8959
description: >
  Use this skill when an individual filer with high wages, self-employment income,
  or railroad retirement (RRTA) compensation needs to compute and report the
  0.9% Additional Medicare Tax. Triggers on phrases like "Additional Medicare
  Tax", "fill out Form 8959", "0.9% Medicare surtax", "high income Medicare",
  "extra Medicare tax", "Medicare surtax on wages", "Additional Medicare Tax on
  self-employment", or any request to reconcile Medicare tax withheld in W-2
  Box 6 against the 0.9% surtax owed at filing. Do NOT use for the regular
  1.45% Medicare tax on wages (handled inside payroll / W-2 itself), the
  employer-side Medicare match (employer's payroll obligation), or the 3.8%
  Net Investment Income Tax — that is a different tax under IRC §1411 reported
  on Form 8960.
form: Form 8959 (Additional Medicare Tax)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8959.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8959.pdf
---

# Form 8959 — Additional Medicare Tax

This skill produces an audit-grade draft of Form 8959 from the user's wages, self-employment income, RRTA compensation, filing status, and any Additional Medicare Tax already withheld by an employer. It walks through Parts I–V line by line, applies the IRC §1401(b)(2) and §3101(b)(2) surtax rules, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form.

The 0.9% Additional Medicare Tax is mechanically simple — a flat surtax above a status-based threshold — but it is easy to get wrong because **the threshold does not phase, does not adjust for inflation, and is split unevenly across income types**. Employer withholding kicks in only at $200,000 of wages from a single employer regardless of filing status, so MFJ couples with two earners under $200K each will under-withhold and owe at filing. The agent's job is to catch that gap and produce the reconciliation cleanly.

**Companion guide for end users:** [Form 8959: Who Pays the 0.9% Additional Medicare Tax (2026) + AI Agent Skill](https://jupid.com/blog/form-8959-additional-medicare-tax-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision:** the line map in this skill was verified against the **2025 Form 8959** ("Created 4/30/25") and the **2025 Instructions for Form 8959** (Aug 7, 2025), filed with 2025 returns in 2026. The next revision must be re-checked before use: https://www.irs.gov/forms-pubs/about-form-8959.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 8959, "Additional Medicare Tax", or the 0.9% Medicare surtax
- The user has W-2 wages above the threshold for their filing status (see Prerequisites) — single/HoH/QSS at $200,000; MFJ at $250,000; MFS at $125,000
- The user has self-employment income and wages combined above their threshold
- The user has Box 6 (Medicare tax withheld) on a W-2 that exceeds 1.45% of Box 5 (Medicare wages) — that excess is Additional Medicare Tax already withheld by the employer and must reconcile on Form 8959 Part V
- The user has RRTA compensation (railroad retirement) with similar high-income exposure
- A return is being assembled and Schedule 2 Line 11 needs a number

Form 8959 must be filed if any of these apply (2025 Instructions for Form 8959, "Who Must File"): Medicare wages and tips on any single W-2 (box 5) are more than $200,000; RRTA compensation on any single W-2 (box 14) is more than $200,000; total Medicare wages and tips plus self-employment income (including the spouse's if MFJ) are more than the filing-status threshold; or total RRTA compensation (including the spouse's if MFJ) is more than the threshold. The first test means an MFJ filer whose one employer withheld the 0.9% must file Form 8959 to claim credit for that withholding even if the household owes nothing.

Do **not** engage this skill when:

- The question is about the regular **1.45% Medicare tax** on every dollar of Medicare wages — that is computed and withheld by the employer on the W-2 and does not require Form 8959
- The question is about the **employer-side 1.45% Medicare match** — that is a payroll tax obligation reported on Form 941, not the employee's Form 8959
- The question is about the **3.8% Net Investment Income Tax (NIIT)** — that is a different tax under IRC §1411 reported on **Form 8960** (sister surtax, often confused)
- The user's wages are exempt from Medicare tax altogether (for example certain nonresident alien students and scholars) — out of scope; refer to a tax professional. Otherwise the instructions say there are no special Additional Medicare Tax rules for nonresident aliens or U.S. citizens living abroad

If the user says "Medicare surtax" without specifying which one, ask: "Are you asking about the 0.9% Additional Medicare Tax on earned income (Form 8959) or the 3.8% Net Investment Income Tax on investment income (Form 8960)?" They are different taxes, computed on different bases, with the same threshold dollar amounts but different rules.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 8959 thresholds are statutory and have not changed since the tax took effect in 2013 ("The threshold amounts below aren't indexed for inflation," 2025 Instructions for Form 8959), but the form revision and Schedule 2 line number can change — verify the current tax year's form before transcribing.
2. **Filing status** — Single / Head of Household / Qualifying Surviving Spouse / Married Filing Jointly / Married Filing Separately. The threshold depends on this:
   - Single, HoH, QSS: **$200,000**
   - MFJ: **$250,000**
   - MFS: **$125,000**
   These are statutory under IRC §1401(b)(2) and §3101(b)(2). Do not invent or interpolate.
3. **W-2 Medicare wages** — the sum of **Box 5** ("Medicare wages and tips") from every W-2 the filer received. If MFJ, sum across both spouses for Part I.
4. **W-2 Medicare tax withheld** — the sum of **Box 6** from every W-2. Used in Part V to identify whether the employer already withheld any Additional Medicare Tax (any amount above 1.45% × Box 5).
5. **Self-employment net earnings** — the figure from **Schedule SE Part I, Line 6** (net earnings from self-employment, after the 92.35% multiplier per IRC §1402(a)(12)). If the filer has both wages and SE income, the threshold is reduced by wages before applying to SE income (see Workflow Step 4).
6. **RRTA compensation** — only if the filer has Tier 1 Medicare RRTA compensation (almost no one does outside the railroad industry). Most filers: zero. If non-zero, ask for both compensation and Medicare tax withheld on it.
7. **Filing-status-specific spouse data** — if MFJ, both spouses' wages, SE income, and RRTA compensation are combined at the household level. If MFS, only the filing spouse's amounts are used and the threshold is $125,000.
8. **Unreported tip income** (Form 4137 line 6 → Form 8959 line 2), **misclassified-worker wages** (Form 8919 line 6 → line 3), and **uncollected Medicare tax on tips or on group-term life insurance over $50,000 for former employees** (W-2 box 12 codes B and N → added to Part V line 19; not codes for uncollected RRTA Medicare tax). Most filers: zero. Ask whether the user has Form 4137, Form 8919, or any W-2 box 12 code B or N.

If the user does not know any of these, do not guess. Ask. The threshold logic depends on every input.

---

## Workflow

Execute these steps in order. Don't skip ahead.

### Step 1 — Confirm filing status and threshold

Confirm the filer's filing status. Look up the statutory threshold:

| Filing status | Threshold (IRC §3101(b)(2), §1401(b)(2)) |
|---------------|------------------------------------------|
| Single | $200,000 |
| Head of Household | $200,000 |
| Qualifying Surviving Spouse | $200,000 |
| Married Filing Jointly | $250,000 |
| Married Filing Separately | $125,000 |

Record the threshold. Every part of the form uses the same threshold for the same filer.

### Step 2 — Sum wages (Part I)

Sum Box 5 of every W-2 received by the filer (and spouse if MFJ). This is **Line 1** of Form 8959. Form 4137 line 6 (unreported tips) goes on **Line 2** and Form 8919 line 6 (misclassified-worker wages) on **Line 3**, each including the spouse's form if MFJ. Do not fold them into Line 1.

### Step 3 — Compute Part I (wage-only Additional Medicare Tax)

```
Line 1 = total Medicare wages and tips from W-2 Box 5 (all W-2s; both spouses if MFJ)
Line 2 = unreported tips from Form 4137 line 6
Line 3 = wages from Form 8919 line 6
Line 4 = Line 1 + Line 2 + Line 3
Line 5 = threshold for filing status (from Step 1)
Line 6 = Line 4 − Line 5  (zero if Line 4 ≤ Line 5)
Line 7 = Line 6 × 0.9%  (the wage Additional Medicare Tax)
```

**Always re-read the current-year form and instructions before transcribing.** If Line 4 ≤ Line 5, Line 7 is zero — but the form still must be filed if any other Part has a non-zero result or a "Who Must File" test applies.

### Step 4 — Compute Part II (self-employment Additional Medicare Tax)

The threshold for SE income is **reduced by total wages from Part I Line 4** (not by the 92.35% SE multiplier figure — by gross wages). This is the key trick: a filer with $150,000 of wages and $80,000 of SE earnings does not get a fresh $200,000 threshold for SE income.

```
Line 8  = self-employment income from Schedule SE Part I Line 6 (enter -0- if a loss; combine if more than one Schedule SE)
Line 9  = threshold for filing status (same as Line 5)
Line 10 = wages from Part I Line 4
Line 11 = Line 9 − Line 10  (zero if Line 10 ≥ Line 9; the wage side already exhausted the threshold)
Line 12 = Line 8 − Line 11  (zero if Line 8 ≤ Line 11)
Line 13 = Line 12 × 0.9%  (the SE Additional Medicare Tax)
```

If the filer has only wages, Lines 8–13 are zero. If only SE income, Lines 1–7 are zero and the threshold flows fully to Line 11.

### Step 5 — Compute Part III (RRTA compensation)

Only fill if the filer has RRTA compensation (almost never applicable). If zero, leave Lines 14–17 blank or zero and move on. Otherwise:

```
Line 14 = RRTA compensation and tips from W-2 box 14 (all W-2s; both spouses if MFJ)
Line 15 = threshold for filing status (the full threshold — NOT reduced by wages)
Line 16 = Line 14 − Line 15  (zero if negative)
Line 17 = Line 16 × 0.9%
```

RRTA compensation is compared to the threshold separately; wages do not reduce the RRTA threshold and RRTA compensation does not reduce the self-employment threshold (2025 Instructions for Form 8959, "Additional Medicare Tax" and Examples 6–7).

### Step 6 — Total Additional Medicare Tax (Part IV)

```
Line 18 = Line 7 + Line 13 + Line 17
```

This is the total Additional Medicare Tax owed for the year. Line 18 flows to **Schedule 2 Line 11** (2025 Schedule 2; Form 1040-SS filers use Part I line 5) and from there to Form 1040 Line 23.

### Step 7 — Reconcile employer withholding (Part V)

This is the part most often skipped. Employers must withhold an extra 0.9% on wages **above $200,000 paid by that single employer**, per IRC §3102(f). The employer withholds without regard to filing status — so two-earner MFJ couples both under $200K each will have *zero* Additional Medicare Tax withheld even though they may owe it at filing.

```
Line 19 = Medicare tax withheld from W-2 Box 6 (all W-2s; both spouses if MFJ), plus any
          uncollected Medicare tax on tips (box 12 code B) and on group-term life insurance
          (box 12 code N), excluding uncollected RRTA Medicare tax
Line 20 = the amount from Line 1
Line 21 = Line 20 × 1.45%  (regular Medicare tax withholding on Medicare wages)
Line 22 = Line 19 − Line 21  (zero if negative) — Additional Medicare Tax withheld on wages
Line 23 = Additional Medicare Tax withheld on RRTA compensation (W-2 box 14) — usually zero
Line 24 = Line 22 + Line 23
```

**Line 24 is included with federal income tax withholding on Form 1040 Line 25c** ("Other forms"; Form 1040-SS filers use Part I line 11a) — it's a *withholding credit* the filer takes against total tax. W-2 box 2 withholding stays on Line 25a. Without Line 24 on Line 25c, a filer who had Additional Medicare Tax withheld by a high-paying employer pays it twice (owes again on Schedule 2 Line 11 without credit for what was already withheld).

The reconciliation:
- **What the employer withheld** = Line 24 (already paid through payroll)
- **What is owed** = Line 18
- **Net at filing** = Line 18 − Line 24 (positive = owe; negative = refund of over-withholding flows through normal Form 1040 totals)

### Step 8 — Run validation checks

See **Validation** below. Run every check.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next forms the filer's return needs:

- **Schedule 2 Line 11** — Line 18 from Form 8959 flows here (see [`../schedule-2/SKILL.md`](../schedule-2/SKILL.md))
- **Form 1040 Line 23** — Schedule 2 line 21 total flows here, including Line 11
- **Form 1040 Line 25c** — Line 24 from Form 8959 (Additional Medicare Tax withheld by employer) is included here as a withholding credit
- **Form 1040-ES** — if the user expects to owe Additional Medicare Tax next year and is not having extra withheld, flag quarterly estimated tax obligations (see `references/employer-withholding-rules.md` and [`../form-1040-es/SKILL.md`](../form-1040-es/SKILL.md)); the instructions say estimated payments can't be designated specifically for Additional Medicare Tax
- **Form W-4** — recommend an updated W-4 with extra income tax withholding if a recurring under-withholding pattern is identified (see [`../form-w4/SKILL.md`](../form-w4/SKILL.md)); the employee can't request withholding specifically for Additional Medicare Tax

### Step 11 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains the FFFF / paid software / paper decision tree and field-by-field mapping for Form 8959 specifically. If the user only wants a draft and will file themselves, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name(s) shown on return** — exactly as on Form 1040 (both names if MFJ)
- **Your social security number** — must match the return; if MFJ, the first SSN that appears on the return

### Part I — Additional Medicare Tax on Medicare Wages (Lines 1–7)

| Line | What goes here |
|------|----------------|
| 1 | Total Medicare wages — sum of Box 5 across all W-2s (filer + spouse if MFJ) |
| 2 | Unreported tips from Form 4137 Line 6 |
| 3 | Wages from Form 8919 Line 6 (uncollected SS/Medicare on misclassified worker) |
| 4 | Sum of Lines 1, 2, 3 |
| 5 | Threshold ($200K / $250K / $125K based on filing status) |
| 6 | Line 4 − Line 5 (floor at zero) |
| 7 | Line 6 × 0.009 |

### Part II — Additional Medicare Tax on Self-Employment Income (Lines 8–13)

| Line | What goes here |
|------|----------------|
| 8 | Schedule SE Part I Line 6 (net earnings from self-employment after 92.35% multiplier); -0- if a loss |
| 9 | Threshold (same as Line 5) |
| 10 | Wages from Part I Line 4 |
| 11 | Line 9 − Line 10 (floor at zero — the "remaining threshold" for SE income) |
| 12 | Line 8 − Line 11 (floor at zero — the SE income above the remaining threshold) |
| 13 | Line 12 × 0.009 |

### Part III — Additional Medicare Tax on Railroad Retirement (RRTA) Compensation (Lines 14–17)

Almost always zero outside the railroad industry. Line 14 = RRTA compensation and tips (W-2 box 14); Line 15 = full threshold (not reduced by wages); Line 16 = Line 14 − Line 15 (floor zero); Line 17 = Line 16 × 0.9%. See `references/line-by-line.md`, Part III.

### Part IV — Total Additional Medicare Tax (Line 18)

```
Line 18 = Line 7 + Line 13 + Line 17
```

Flows to Schedule 2 Line 11 (2025 Schedule 2) → Form 1040 Line 23.

### Part V — Withholding Reconciliation (Lines 19–24)

Reconciles what the employer already withheld against what is owed. Line 19 = W-2 box 6 total (+ box 12 codes B and N); Line 20 = Line 1; Line 21 = Line 20 × 1.45%; Line 22 = Line 19 − Line 21 (floor zero); Line 23 = RRTA Additional Medicare Tax withheld; Line 24 = Line 22 + Line 23 → included on Form 1040 Line 25c as a withholding credit.

---

## Validation

Run every check. Surface failures — don't silently fix.

### Math checks

- [ ] Line 4 = Line 1 + Line 2 + Line 3
- [ ] Line 5 matches the statutory threshold for the declared filing status ($200,000 / $250,000 / $125,000)
- [ ] Line 6 = max(Line 4 − Line 5, 0)
- [ ] Line 7 = Line 6 × 0.009 (rounded per IRS conventions — usually nearest dollar)
- [ ] Line 11 = max(Line 9 − Line 10, 0)
- [ ] Line 12 = max(Line 8 − Line 11, 0)
- [ ] Line 13 = Line 12 × 0.009
- [ ] Line 18 = Line 7 + Line 13 + Line 17
- [ ] Line 16 = max(Line 14 − Line 15, 0), with Line 15 = the full threshold
- [ ] Line 17 = Line 16 × 0.009
- [ ] Line 20 = Line 1
- [ ] Line 21 = Line 20 × 0.0145
- [ ] Line 22 = max(Line 19 − Line 21, 0)  (Line 19 < Line 21 → flag, see Sanity)
- [ ] Line 24 = Line 22 + Line 23

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] **Filing status mismatch with threshold**: e.g., the deliverable says "Single" but Line 5 = $250,000 → wrong threshold; recompute
- [ ] **MFJ couple with two earners both under $200K each but combined over $250K**: confirm the user knows employer withholding is zero in this scenario and the full Additional Medicare Tax will be owed at filing
- [ ] **Line 19 < Line 21** (W-2 Box 6 less than 1.45% of Box 5): possible W-2 reporting error; ask the user to confirm Box 5 and Box 6 with the employer before filing
- [ ] **Filer is MFS**: confirm — MFS threshold is $125,000 (the lowest), and many filers default to "married = $250K"; this is a frequent error
- [ ] **Both wages and SE income, with wages > threshold**: Line 11 = 0, so all SE income above zero is taxed; double-check the user understands the threshold is single, not stacked
- [ ] **Line 18 > $0 but Line 24 = $0**: filer owes the full Additional Medicare Tax at filing with no employer withholding offset; flag estimated tax obligation for next year
- [ ] **Line 24 > Line 18**: employer withheld more than the filer owes (typical case: MFJ, one spouse's employer paid over $200,000, combined household wages under $250,000); the excess is credited via Form 1040 Line 25c and refunded through normal channels

### Cross-form checks

- [ ] If Line 18 > $0, ensure Schedule 2 Line 11 carries the same number
- [ ] If Line 24 > $0, ensure Form 1040 Line 25c includes it (W-2 box 2 stays on Line 25a)
- [ ] If Form 8919 is filed, Line 3 = Form 8919 line 6; if Form 4137 is filed, Line 2 = Form 4137 line 6
- [ ] If filer also has investment income > the threshold for filing status, confirm whether **Form 8960** (NIIT) is also required — different tax, same income brackets
- [ ] If the filer's net Additional Medicare Tax liability is large and recurring, recommend updated Form W-4 (additional withholding) or Form 1040-ES (quarterly estimates)

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 8959 or paste into tax software. Format:

```markdown
# Form 8959 — DRAFT for tax year YYYY

## Header
Name(s) shown on return:    <filer name(s)>
Your social security number: <SSN>
Filing status:               <Single | HoH | QSS | MFJ | MFS>
Threshold (Line 5):          $<200,000 | 250,000 | 125,000>

## Part I — Additional Medicare Tax on Medicare Wages
 1. Medicare wages (W-2 Box 5 total):              $X,XXX,XXX
 2. Unreported tips (Form 4137 Line 6):            $X,XXX
 3. Wages from Form 8919 Line 6:                   $X,XXX
 4. Add Lines 1, 2, 3:                             $X,XXX,XXX
 5. Threshold for filing status:                   $XXX,XXX
 6. Subtract Line 5 from Line 4 (floor zero):      $X,XXX,XXX
 7. Additional Medicare Tax on wages (Line 6 × 0.9%): $X,XXX

## Part II — Additional Medicare Tax on Self-Employment Income
 8. Self-employment income (Schedule SE Line 6):   $X,XXX,XXX
 9. Threshold for filing status:                   $XXX,XXX
10. Wages from Part I Line 4:                      $X,XXX,XXX
11. Subtract Line 10 from Line 9 (floor zero):     $X,XXX,XXX
12. Subtract Line 11 from Line 8 (floor zero):     $X,XXX,XXX
13. Additional Medicare Tax on SE income (Line 12 × 0.9%): $X,XXX

## Part III — RRTA Compensation
14. RRTA compensation:                             $X,XXX  (or 0)
15. Threshold:                                     $XXX,XXX
16. Subtract Line 15 from Line 14 (floor zero):    $X,XXX
17. Additional Medicare Tax on RRTA (Line 16 × 0.9%): $X,XXX  (or 0)

## Part IV — Total Additional Medicare Tax
18. Total Additional Medicare Tax (Lines 7 + 13 + 17): $X,XXX
    → flows to Schedule 2 Line 11 → Form 1040 Line 23

## Part V — Withholding Reconciliation
19. Medicare tax withheld (W-2 Box 6 total, + box 12 codes B, N): $XX,XXX
20. Amount from Line 1:                            $X,XXX,XXX
21. Regular Medicare withholding (Line 20 × 1.45%): $XX,XXX
22. Additional Medicare Tax withheld on wages (Line 19 − Line 21, floor zero): $X,XXX
23. RRTA Additional Medicare Tax withheld (W-2 box 14): $X,XXX  (or 0)
24. Total Additional Medicare Tax withholding (Line 22 + Line 23): $X,XXX
    → included on Form 1040 Line 25c

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Net at filing: Line 18 − Line 24 = $X,XXX  (positive = owe; negative = refund through normal totals)
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 8959 (tax year of the revision used; 2025 form created 4/30/25)
- IRS Instructions for Form 8959 (tax year; 2025 instructions dated Aug 7, 2025)
- IRC §1401(b)(2) (Additional Medicare Tax on self-employment income)
- IRC §3101(b)(2) (Additional Medicare Tax on wages)
- IRC §3102(f) (employer withholding obligation at $200K wage threshold)
- IRS Schedule 2 (tax year) — flow target for Line 18
```

Show every line including zeros. The deliverable is a starting point — the user still has to enter it into Form 1040 e-file software or paper Form 8959.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8959 line with examples and edge cases
- [`references/thresholds-and-statuses.md`](./references/thresholds-and-statuses.md) — Statutory thresholds, MFJ/MFS interaction, why the threshold doesn't inflate
- [`references/wage-vs-se-interaction.md`](./references/wage-vs-se-interaction.md) — How wages reduce the SE threshold; worked examples
- [`references/employer-withholding-rules.md`](./references/employer-withholding-rules.md) — IRC §3102(f) employer obligation, why MFJ couples under-withhold, multiple-employer cases
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 8959 alongside Form 1040 via FFFF, paper, or generic tax software

## Examples

End-to-end worked Form 8959 drafts. Use these as patterns when the user's situation is similar.

- [`examples/single-high-earner.md`](./examples/single-high-earner.md) — Single filer with $262,400 of Medicare wages from one employer, employer withheld correctly above $200K
- [`examples/mfj-two-earners.md`](./examples/mfj-two-earners.md) — MFJ couple with two W-2s ($186,500 + $98,300 Medicare wages), under each individual employer's withholding trigger but over the MFJ filing threshold
- [`examples/se-consultant.md`](./examples/se-consultant.md) — Solo consultant with $350,000 Schedule C net earnings, no W-2 wages, no employer withholding, full obligation at filing

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 8959: Who Pays the 0.9% Additional Medicare Tax (2026) + AI Agent Skill](https://jupid.com/blog/form-8959-additional-medicare-tax-2026) — Jupid's narrative companion
- [Form 8959 (2025)](https://www.irs.gov/pub/irs-pdf/f8959.pdf) — the form itself (line map verified against the 2025 revision)
- [Instructions for Form 8959 (2025)](https://www.irs.gov/pub/irs-pdf/i8959.pdf) — Who Must File, thresholds (not indexed), line instructions, Examples 1–7
- [About Form 8959](https://www.irs.gov/forms-pubs/about-form-8959) — IRS landing page with archive of past revisions
- [Form 8960](https://www.irs.gov/pub/irs-pdf/f8960.pdf) — Net Investment Income Tax (sister surtax under IRC §1411; do not confuse)
- [Schedule 2 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) — flow target for Form 8959 Line 18 (line 11)
- [Form 1040](https://www.irs.gov/pub/irs-pdf/f1040.pdf) — Line 25c receives Form 8959 Line 24
- [Form 8919](https://www.irs.gov/pub/irs-pdf/f8919.pdf) — line 6 feeds Form 8959 Line 3 (see [`../form-8919/SKILL.md`](../form-8919/SKILL.md))
- [Schedule SE (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) — Part I line 6 feeds Form 8959 Line 8 (see [`../schedule-se/SKILL.md`](../schedule-se/SKILL.md))
- [Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) — quarterly estimated tax for filers under-withheld for Additional Medicare Tax
- [Form 4137](https://www.irs.gov/pub/irs-pdf/f4137.pdf) — Social Security and Medicare Tax on Unreported Tip Income (feeds Line 2)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (chapter on Additional Medicare Tax planning)
- IRC §1401(b)(2) — Additional Medicare Tax on self-employment income, 0.9%, threshold by filing status
- IRC §3101(b)(2) — Additional Medicare Tax on wages, 0.9%, threshold by filing status
- IRC §3102(f) — Employer withholding obligation: 0.9% on wages above $200,000 from a single employer regardless of filing status
- IRC §1411 — Net Investment Income Tax (the *other* surtax, 3.8% — do not confuse with this skill)
- T.D. 9645 (2013-51 I.R.B.) — final regulations; Additional Medicare Tax added by §9015 of P.L. 111-148, amended by §10906 and by §1402(b) of P.L. 111-152

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and IRC sections. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations — multiple jobs, RRTA compensation, mid-year filing-status changes — warrant a licensed tax professional's review.
