---
name: form-1040
description: |
  Use this skill when a US individual taxpayer needs to fill out Form 1040 in the 2026 filing season (the 2025 return). Triggers: "fill out Form 1040", "file my federal income tax return", "individual tax return", "tax return for self-employed/W-2/freelancer".

  Do NOT use for: non-resident aliens (Form 1040-NR, use form-1040-nr), amended returns (Form 1040-X, use form-1040-x), trusts/estates (Form 1041), corporations (Form 1120 or 1120-S, use form-1120 or form-1120-s).
form: Form 1040
audience: [individual, solo, freelance, llc1, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
---

# Form 1040 — U.S. Individual Income Tax Return

This skill produces an audit-grade draft of Form 1040 from the user's income, deductions, credits, payments, and dependent facts. It walks through every line on page 1 and page 2, applies the IRS rules at each line, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

Form 1040 is the cover sheet for the entire US individual return. Most of the heavy lifting happens on the schedules — Schedule 1, 2, 3, A, B, C, D, E, SE, and dozens of supporting forms. The 1040 itself is the single page (front and back) that pulls all of those into one number: refund or balance due. The math is mechanical. The judgment is in *which schedules apply*, *which credits the user qualifies for*, and *when a rule depends on a fact the user hasn't mentioned*. This skill optimizes for the latter — the agent should ask, not guess.

**Form revision.** The line map in this skill was verified against the **2025 Form 1040 (filed in 2026)** and the 2025 Instructions for Form 1040. The 2025 revision split several lines (1a–1i/1z, 6a–6d, 7a/7b, 11a/11b, 12a–12e, 13a/13b, 27a–27c) and added Line 30 (refundable adoption credit) and Line 38 (estimated tax penalty) alongside the new Schedule 1-A. Before using this skill for a later year, re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1040.

**Companion guide for end users:** [Form 1040 + AI Agent Skill: Complete US Tax Return Guide 2026](https://jupid.com/blog/form-1040-individual-tax-return-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1040, "1040", "individual tax return", "federal income tax return"
- The user describes filing for themselves (W-2 employee, self-employed, retired, mixed) for tax year 2025 or 2026
- The user wants a draft assembled from W-2s, 1099s, and supporting schedules they've already computed
- The user asks "how much tax do I owe" or "what's my refund" and is filing as an individual

Do **not** engage this skill when:

- The user is a non-resident alien → use Form 1040-NR ([`form-1040-nr`](../form-1040-nr/SKILL.md))
- The user is amending a prior-year return → use Form 1040-X ([`form-1040-x`](../form-1040-x/SKILL.md); different line numbers and reconciliation logic)
- The user is filing for a trust, estate, or fiduciary → use Form 1041 (no skill in this repo)
- The user is filing for a C-corporation → use Form 1120 ([`form-1120`](../form-1120/SKILL.md))
- The user is filing for an S-corporation → use Form 1120-S ([`form-1120-s`](../form-1120-s/SKILL.md))
- The user is filing a partnership return → use Form 1065 ([`form-1065`](../form-1065/SKILL.md))

If the user's residency status is ambiguous (e.g., dual-status, recent green card holder, F-1 student), ask before proceeding. Resident aliens file Form 1040; non-resident aliens file Form 1040-NR; dual-status taxpayers file both with attached statements.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer. Do not default.

1. **Tax year** the return covers. Form 1040 for tax year 2025 is filed by April 15, 2026; for tax year 2026, by April 15, 2027. Numbers (standard deduction, brackets, CTC) depend on this. This skill's line map is the 2025 revision; for a 2026 return, re-check the 2026 form first.
2. **Filer's legal name and SSN/ITIN.** Must match the Social Security card exactly. Do not invent.
3. **Spouse's legal name and SSN/ITIN** if filing jointly or separately while married.
4. **Filing status** — Single, Married Filing Jointly (MFJ), Married Filing Separately (MFS), Head of Household (HoH), or Qualifying Surviving Spouse. See [`references/filing-status.md`](./references/filing-status.md). If user says "I'm married" without specifying joint or separate, ask which.
5. **Mailing address** as of the filing date, and whether the main home (and the spouse's, if joint) was in the U.S. for more than half the year (new 2025 checkbox). Ask whether either spouse died before filing (Deceased box and date).
6. **Dependents** — for each: first and last name, SSN, relationship, whether they lived with the taxpayer more than half the year and whether that was in the U.S. (row 5), full-time student or permanently and totally disabled (row 6), and whether the dependent qualifies for CTC (under 17 at year-end, SSN valid for employment issued by the return due date) or ODC (row 7). For CTC/ACTC the filer (or at least one spouse on a joint return) also needs an SSN valid for employment issued by the due date, including extensions; the other spouse needs an SSN or ITIN. See [`references/dependents.md`](./references/dependents.md).
7. **Digital assets answer** — Yes if during the year the user (a) received a digital asset as a reward, award, or payment for property or services, or (b) sold, exchanged, or otherwise disposed of one; No if they only bought with real currency, held, or moved it between their own wallets.
8. **Income data**, structured by source:
   - W-2s (each employer's box 1 wages, box 2 federal withholding, box 3/4/5/6 SS+Medicare, box 12 codes if relevant)
   - 1099-NEC, 1099-MISC, 1099-K (self-employment — flows through Schedule C)
   - 1099-INT, 1099-DIV (interest, dividends)
   - 1099-R (retirement distributions)
   - 1099-B / Form 8949 (capital gains)
   - SSA-1099 (Social Security)
   - K-1s (partnership, S-corp, trust)
   - Other income (unemployment, gambling, alimony pre-2019, COD, etc.)
9. **Adjustments to income** — half SE tax, SEP/SIMPLE/Solo 401(k), self-employed health insurance, HSA, student loan interest, educator expenses, alimony paid (pre-2019). Compute each on Schedule 1.
10. **Standard or itemized deduction decision** — see [`references/line-by-line.md`](./references/line-by-line.md) Lines 12a–12e. If itemizing, need Schedule A inputs.
11. **QBI inputs** — for Schedule C / Schedule E passthrough / K-1 income, the qualified business income amount and whether the user is in a Specified Service Trade or Business (SSTB).
12. **Schedule 1-A inputs** (new for 2025, Form 1040 Line 13b) — qualified tips, qualified overtime premium pay, interest on a loan secured by a first lien on a new (original use), U.S.-assembled personal-use vehicle bought in 2025, with the VIN, and whether the user or spouse was born before January 2, 1961. Ask about each; these apply whether or not the user itemizes.
13. **Credits the user might qualify for** — CTC, EITC, AOTC/LLC, Saver's Credit, foreign tax credit, dependent care, residential energy, adoption. See [`references/credits-overview.md`](./references/credits-overview.md).
14. **Payments already made** — W-2 federal withholding (box 2), 1099 withholding (box 4), W-2G and other withholding, Additional Medicare Tax withheld (Form 8959 line 24), quarterly estimated tax payments, prior-year overpayment applied, and the prior year's total tax and AGI (needed for the Line 38 penalty test).
15. **Refund routing** if expecting a refund — bank routing number, account number, account type (checking or savings). The agent should not store these — collect at filing time only.

If the user mentions they have a Schedule C / SE / E / D, treat those as separate skills ([`schedule-c`](../schedule-c/SKILL.md), [`schedule-se`](../schedule-se/SKILL.md), [`schedule-e`](../schedule-e/SKILL.md), [`schedule-d`](../schedule-d/SKILL.md)) and import the bottom-line numbers.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filing status and residency

Confirm the user is a US citizen, resident alien, or otherwise required to file Form 1040 (not 1040-NR). Confirm filing status using [`references/filing-status.md`](./references/filing-status.md). If MFJ, confirm both spouses agree to file jointly.

### Step 2 — Inventory income sources

Walk every source of income the user received in the tax year. Map each to a Form 1040 line or schedule:

```
| Source                | Tax document  | Goes to                       |
|-----------------------|---------------|-------------------------------|
| Acme Corp salary      | W-2           | 1040 Line 1a                  |
| Stripe (consulting)   | 1099-K        | Schedule C → Schedule 1 → 1040 L8 |
| Wells Fargo savings   | 1099-INT      | 1040 Line 2b                  |
| Vanguard brokerage    | 1099-DIV/1099-B | 1040 L3a/3b/7a, Schedule D   |
| Traditional IRA RMD   | 1099-R        | 1040 Line 4a/4b               |
| Social Security       | SSA-1099      | 1040 Line 6a/6b               |
```

If any source is on a schedule the user hasn't computed yet (Schedule C, D, E, SE), pause and run the appropriate sibling skill first: `schedule-c`, `form-8949`, `schedule-se`. Do not invent the bottom-line numbers.

### Step 3 — Identify required schedules

Form 1040 is short; the schedules carry the weight. Identify which apply:

- **Schedule 1** — additional income (Schedule C profit, rentals, K-1, unemployment, COD) and above-the-line adjustments → [`schedule-1`](../schedule-1/SKILL.md)
- **Schedule 1-A** — new for 2025: no tax on tips, no tax on overtime, car loan interest, enhanced deduction for seniors (flows to Line 13b)
- **Schedule 2** — additional taxes: Part I (excess advance PTC repayment, AMT → Line 17) and Part II (SE tax, Additional Medicare Tax, NIIT, other → Line 23) → [`schedule-2`](../schedule-2/SKILL.md)
- **Schedule 3** — non-refundable credits (foreign tax, dependent care, education, retirement savings) and refundable payments (PTC, fuel credits)
- **Schedule A** — itemized deductions (only if itemizing instead of standard) → [`schedule-a`](../schedule-a/SKILL.md)
- **Schedule B** — if taxable interest is over $1,500, ordinary dividends are over $1,500, OR the user had a foreign account or foreign trust (each test separately; 2025 Instructions for Form 1040, lines 2b and 3b)
- **Schedule C** — sole proprietor / SMLLC business income → use `schedule-c` skill
- **Schedule D + Form 8949** — capital gains → use `form-8949` skill
- **Schedule E** — rental, royalty, K-1 passthrough income
- **Schedule SE** — self-employment tax → use `schedule-se` skill
- **Form 8995 / 8995-A** — Qualified Business Income deduction
- **Schedule 8812** — Child Tax Credit / Credit for Other Dependents (Line 19) and refundable Additional Child Tax Credit (Line 28) → [`schedule-8812`](../schedule-8812/SKILL.md)
- **Form 2441** — child and dependent care credit
- **Form 8863** — education credits (AOTC, LLC)
- **Form 8889** — HSA → [`form-8889`](../form-8889/SKILL.md)

For each schedule that applies, list it as a required attachment in the deliverable.

### Step 4 — Compute Page 1 income (Lines 1-9)

Walk lines 1a through 1i and 1z (wages and other earned income). Then Lines 2a/2b (interest), 3a/3b/3c (dividends), 4a/4b/4c (IRA), 5a/5b/5c (pensions), 6a/6b/6c/6d (Social Security), 7a/7b (capital gain from Schedule D), 8 (Schedule 1 additional income).

Sum to Line 9 (Total Income) = 1z + 2b + 3b + 4b + 5b + 6b + 7a + 8.

For Line 6b (taxable Social Security), use the Social Security Benefits Worksheet from the 1040 instructions. If combined income (AGI before SS + tax-exempt interest + half of SS) is not more than $25,000 single/HOH/QSS ($32,000 MFJ), none of SS is taxable. Above the second threshold ($34,000 / $44,000), up to 85% is taxable. MFS who lived with the spouse at any time in the year have a $0 base; MFS who lived apart all year check Line 6d.

### Step 5 — Compute adjustments and AGI (Lines 10-11b)

Line 10 = Schedule 1 Line 26 (above-the-line adjustments). Line 11a = Line 9 − Line 10 = **AGI**; Line 11b at the top of page 2 repeats Line 11a. Flag AGI explicitly in the deliverable — it's the base for many phaseouts and downstream calculations (IRMAA, FAFSA, Roth eligibility).

### Step 6 — Decide standard vs itemized (Lines 12a–12e)

Lines 12a–12d are checkboxes: 12a someone can claim you / your spouse as a dependent, 12b spouse itemizes on a separate MFS return, 12c dual-status alien, 12d born before January 2, 1961 / blind (you and spouse). Line 12e is the deduction amount.

For 2025 (P.L. 119-21 §70102, shown in the 2025 Instructions for Form 1040, line 12e):
- Single / MFS: $15,750
- MFJ / Qualifying Surviving Spouse: $31,500
- Head of Household: $23,625
- Additional for each 12d box: $1,600 (MFJ/QSS/MFS); $2,000 (Single/HOH)
- 12b or 12c checked: standard deduction is zero; 12a checked: use the Standard Deduction Worksheet for Dependents (greater of $1,350 or earned income + $450, capped at the regular amount)

For 2026 (Rev. Proc. 2025-32 §4.14): $16,100 single/MFS, $32,200 MFJ/QSS, $24,150 HOH; additional $1,650 ($2,050 single/HOH); dependent $1,350 or earned income + $450.

If the user has potential itemized deductions (large mortgage, high state tax, major medical, large charitable), run Schedule A and compare. The 2025 SALT cap is $40,000 ($20,000 MFS), reduced when MAGI is over $500,000 ($250,000 MFS) but not below $10,000 ($5,000 MFS). Pick the larger of standard or itemized for Line 12e.

### Step 7 — Compute QBI deduction (Line 13a) and Schedule 1-A deductions (Line 13b)

If the user has Schedule C profit, Schedule E passthrough income, qualifying REIT dividends, or PTP income:

- If 2025 taxable income before the QBI deduction is at or below $197,300 ($394,600 MFJ), use Form 8995 (simplified); for 2026 the thresholds are $201,750 / $403,500 (Rev. Proc. 2025-32 §4.26)
- Above the threshold, use Form 8995-A (full) — SSTB phaseouts and W-2 wage / UBIA limits apply
- QBI deduction = lesser of (20% × QBI) or (20% × (taxable income before QBI − net capital gain)); Form 8995 line 15 → Line 13a
- For self-employed filers, QBI is Schedule C profit minus the deductible half SE tax, SE health insurance, and qualified retirement contributions attributable to the business

If the user qualifies but hasn't computed QBI, ask to run [`form-8995`](../form-8995/SKILL.md) first.

Line 13b = Schedule 1-A line 38. For 2025: qualified tips up to $25,000; qualified overtime up to $12,500 ($25,000 MFJ), both reduced above $150,000 MAGI ($300,000 MFJ); qualified passenger vehicle loan interest up to $10,000 (new vehicle, final assembly in the U.S., VIN required), reduced above $100,000 ($200,000 MFJ); enhanced senior deduction $6,000 per person born before January 2, 1961, reduced above $75,000 ($150,000 MFJ). Married filers must file jointly for the tips, overtime, and senior deductions (2025 Instructions for Form 1040, What's New). Ask the user for the inputs; do not assume zero.

### Step 8 — Compute taxable income (Lines 14-15)

Line 14 = Line 12e + Line 13a + Line 13b. Line 15 = Line 11b − Line 14. If zero or less, enter 0. Line 15 is **taxable income** — the number tax is calculated on.

### Step 9 — Compute tax (Line 16)

Use the right method per [`references/tax-computation.md`](./references/tax-computation.md):
- Taxable income < $100,000 → Tax Tables (look up bracket)
- Taxable income ≥ $100,000 → Tax Computation Worksheet
- Has qualified dividends or net long-term capital gains → Qualified Dividends and Capital Gain Tax Worksheet (uses preferential 0/15/20% LTCG rates)
- Has 28%-rate gain (collectibles) or unrecaptured §1250 gain (Schedule D line 18 or 19 > 0 with gains on lines 15 and 16) → Schedule D Tax Worksheet
- Child with unearned income over $2,700 → Form 8615; foreign earned income exclusion → Foreign Earned Income Tax Worksheet; Form 8814 / Form 4972 → check the matching Line 16 box

Show the worksheet used and the math.

### Step 10 — Apply credits and other taxes (Lines 17-24)

- Line 17 = Schedule 2 Line 3 (Part I only: excess advance PTC repayment and other additions on lines 1a–1z, plus AMT on line 2)
- Line 18 = Line 16 + Line 17
- Line 19 = CTC / ODC (Schedule 8812 line 14)
- Line 20 = Schedule 3 Line 8 (other non-refundable credits)
- Line 21 = Line 19 + Line 20
- Line 22 = Line 18 − Line 21, floored at 0
- Line 23 = Schedule 2 Line 21 (Part II: SE tax, Additional Medicare Tax, NIIT, additional tax on IRAs, household employment taxes, and other taxes)
- Line 24 = Line 22 + Line 23 — **total tax**

For self-employed filers, Line 23 is usually the largest line on page 2 (Schedule SE: 12.4% on net earnings up to the Social Security wage base plus 2.9% on all net earnings, where net earnings = 92.35% of Schedule C profit).

### Step 11 — Compute payments and refundable credits (Lines 25-33)

- Lines 25a/25b/25c — federal income tax withheld from W-2s (box 2), 1099s (box 4; SSA-1099 box 6), and other forms (W-2G, Form 8959 line 24 Additional Medicare Tax withheld, Schedule K-1, 1042-S, 8805, 8288-A); Line 25d = 25a + 25b + 25c
- Line 26 — estimated tax payments + prior-year overpayment applied (enter a former spouse's SSN if joint estimates were made before a 2025 divorce)
- Line 27a — EIC (refundable; from EIC worksheets and tables). 27b = clergy filing Schedule SE checkbox; 27c = check if the user does not want to (or cannot) claim the EIC
- Line 28 — Additional Child Tax Credit (Schedule 8812 line 27); checkbox if the user does not want to claim the ACTC
- Line 29 — refundable AOTC (Form 8863 line 8; 40% of AOTC, up to $1,000 per student)
- Line 30 — refundable adoption credit (Form 8839 line 13; up to $5,000 per child for 2025)
- Line 31 — Schedule 3 Line 15 (net PTC, extension payment, excess SS/RRTA withheld, fuel credit, other)
- Line 32 = Lines 27a + 28 + 29 + 30 + 31
- Line 33 = Lines 25d + 26 + 32 — **total payments**

### Step 12 — Refund or balance due (Lines 34-38)

If Line 33 > Line 24: refund. Line 34 = Line 33 − Line 24. Lines 35a/b/c/d for direct deposit (check the 35a box if Form 8888 splits the refund); Line 36 to apply to next year's estimated tax (this election cannot be changed later).

If Line 24 > Line 33: balance due. Line 37 = Line 24 − Line 33. Pay by April 15 (electronic payment is recommended; Form 1040-V only with a mailed check).

Line 38 = estimated tax penalty (Form 2210). The user may owe it if Line 37 is at least $1,000 and more than 10% of the tax shown, or if estimated payments were short on any due date. No penalty if Lines 25d + 26 + Schedule 3 line 11 are at least 100% of the prior year's tax (110% if prior-year AGI was over $150,000, $75,000 MFS) and estimates were paid on time, or if the prior year showed no tax (2025 Instructions for Form 1040, line 38). Leave Line 38 blank for the IRS to calculate, OR compute on Form 2210 if claiming the annualized income exception or wanting to verify the number; a computed penalty is also added to Line 37.

### Step 13 — Run validation checks

See **Validation** below. Run every check.

### Step 14 — Produce the deliverable

See **Output format** below.

### Step 15 — Hand off downstream

State the next forms the user will need:

- All schedules used must be attached
- Schedule SE if net earnings from self-employment are $400 or more
- Form 1040-V payment voucher if mailing a payment
- Form 4868 if extending past April 15
- Form 1040-ES for next year's estimated tax payments

### Step 16 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree to pick a filing channel (IRS Free File, Free File Fillable Forms, paid software, paper; IRS Direct File was not offered for the 2026 filing season)
- Field-by-field mapping from this skill's draft to FFFF form labels
- Submission state machine and security/consent rules

If the user only wants a draft and will file themselves, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). Highlights below.

### Header

- **Filing status box** — exactly one. See [`references/filing-status.md`](./references/filing-status.md).
- **Names + SSNs** — must match Social Security cards. Wrong middle initials trigger e-file rejection.
- **Address** — current as of filing date. The IRS mails refunds and notices here unless direct deposit specified.
- **Digital assets question** — Yes if the user received a digital asset as a reward, award, or payment, or sold, exchanged, or otherwise disposed of one in the year; No if only bought with real currency, held, or moved between own wallets.
- **Main home in the U.S.** — new 2025 checkbox: main home (and spouse's, if joint) in the U.S. for more than half the year.
- **Deceased** — check and enter the date of death for a taxpayer or spouse who died before filing.
- **Dependents section** — numbered rows (1) first name, (2) last name, (3) SSN, (4) relationship, (5)(a) lived with you more than half the year and (5)(b) in the U.S., (6) full-time student / permanently and totally disabled, (7) CTC or ODC checkbox; check the box for more than four dependents and attach a statement. See [`references/dependents.md`](./references/dependents.md).

### Page 1 income (Lines 1-11a)

- **1a-1z** — Wages and earned income. 1a is W-2 box 1 sum. 1z is total of 1a-1h (1i is not added).
- **2a/2b** — Tax-exempt and taxable interest.
- **3a/3b/3c** — Qualified and ordinary dividends; 3c flags a child's dividends included via Form 8814.
- **4a/4b/4c**, **5a/5b/5c** — Gross and taxable IRA / pension distributions; 4c/5c checkboxes for rollover, QCD/PSO, other.
- **6a/6b/6c/6d** — Social Security (SSA-1099 box 5) and taxable amount; 6c lump-sum election; 6d MFS who lived apart all year.
- **7a/7b** — Capital gain or loss (Schedule D line 16 or capital gain distributions); 7b boxes "Schedule D not required" and "Includes child's capital gain or (loss)".
- **8** — Schedule 1 additional income.
- **9** — Total income (sum of 1z + 2b + 3b + 4b + 5b + 6b + 7a + 8).
- **10** — Schedule 1 Line 26 adjustments (above-the-line).
- **11a** — AGI.

### Page 2 deductions to taxable income (Lines 11b-15)

- **11b** — AGI repeated from 11a.
- **12a–12d** — Dependent, spouse-itemizes, dual-status, and age/blindness checkboxes.
- **12e** — Standard deduction or Schedule A itemized (Schedule A line 17).
- **13a** — QBI deduction (Form 8995 or 8995-A line 15/39).
- **13b** — Schedule 1-A line 38 (tips, overtime, car loan interest, seniors).
- **14** — Sum of 12e + 13a + 13b.
- **15** — Taxable income (11b − 14, not below zero).

### Page 2 tax + credits + payments (Lines 16-38)

- **16** — Tax computed from Line 15 (boxes for Form 8814, Form 4972, other).
- **17–24** — Schedule 2 Part I taxes, credits (19–21), tax after credits (22), Schedule 2 Part II taxes (23), total tax (24).
- **25a–33** — Withholding (25d total), estimates (26), refundable credits (27a–31), totals (32, 33).
- **34–37** — Refund or balance due.
- **38** — Estimated tax penalty (optional self-compute).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails.

### Math checks

- [ ] Line 1z = sum of 1a + 1b + 1c + 1d + 1e + 1f + 1g + 1h (1i not added)
- [ ] Line 9 = 1z + 2b + 3b + 4b + 5b + 6b + 7a + 8
- [ ] Line 11a = Line 9 − Line 10; Line 11b = Line 11a
- [ ] Line 14 = Line 12e + Line 13a + Line 13b
- [ ] Line 15 = Line 11b − Line 14 (floored at 0)
- [ ] Line 16 matches the tax computation method used (Tax Table under $100,000, Tax Computation Worksheet, QDCG Worksheet, Schedule D Tax Worksheet)
- [ ] Line 18 = Line 16 + Line 17
- [ ] Line 21 = Line 19 + Line 20
- [ ] Line 22 = Line 18 − Line 21, floored at 0
- [ ] Line 24 = Line 22 + Line 23
- [ ] Line 25d = 25a + 25b + 25c
- [ ] Line 32 = Lines 27a + 28 + 29 + 30 + 31
- [ ] Line 33 = Lines 25d + 26 + 32
- [ ] Either Line 34 or Line 37 is populated, not both
- [ ] Line 34 (if refund) = Line 33 − Line 24; Line 35a + Line 36 = Line 34
- [ ] Line 37 (if owed) = Line 24 − Line 33 (plus Line 38 if a penalty was computed)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filing status is HoH but no qualifying person listed in dependents → likely wrong status
- [ ] Filing status is MFJ but only one SSN provided → missing spouse SSN
- [ ] Schedule C exists in inputs but Line 8 (Schedule 1 income) is 0 → Schedule C profit didn't flow through
- [ ] Schedule SE exists but Line 23 (other taxes) is 0 → SE tax didn't flow through
- [ ] Self-employment income but no Schedule 1 Line 15 (half SE tax adjustment) → missing the deduction
- [ ] Self-employed but no QBI on Line 13a → likely missed the 20% deduction
- [ ] User mentioned tips, overtime, a 2025 car loan, or was born before January 2, 1961, but Line 13b is 0 → check Schedule 1-A
- [ ] Standard deduction taken but Schedule A items mentioned → consider itemizing
- [ ] HoH or single with > 1 dependent but no CTC/ODC on Line 19 → check if dependents are correctly flagged
- [ ] Digital assets question left blank → must be answered Yes or No
- [ ] Medicare wages (W-2 box 5) plus SE earnings over $200,000 single/HOH/QSS, $250,000 MFJ, $125,000 MFS, but no Additional Medicare Tax → check Form 8959 (Schedule 2 line 11 → Line 23)
- [ ] MAGI over $200,000 single/HOH, $250,000 MFJ/QSS, $125,000 MFS with investment income but no NIIT → check Form 8960 (Schedule 2 line 12 → Line 23)
- [ ] Line 37 is at least $1,000 and more than 10% of the tax shown, and the prior-year safe harbor is not met → Line 38 penalty likely (Form 2210)
- [ ] EITC claimed but earned income / AGI exceeds the EITC limit for the filer's status and number of children

### Cross-form checks

- [ ] If Schedule C net earnings from self-employment are $400 or more, Schedule SE must be attached and Line 23 must include SE tax (Schedule SE line 12 → Schedule 2 line 4 → Schedule 2 line 21)
- [ ] If Schedule A used, Line 12e = Schedule A Line 17 (not the standard deduction)
- [ ] If Form 8995 used, Line 13a = Form 8995 Line 15 (Form 8995-A line 39)
- [ ] If Schedule 1-A used, Line 13b = Schedule 1-A Line 38
- [ ] If Schedule 8812 used, Line 19 = Schedule 8812 Line 14 and Line 28 = Schedule 8812 Line 27

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 1040 or paste into tax software. Format:

```markdown
# Form 1040 — DRAFT for tax year YYYY (form revision: 2025 Form 1040)

## Header
Filing status: <Single | MFJ | MFS | HoH | QSS>
Filer name: <Legal Name>     SSN: <XXX-XX-XXXX>
Spouse name (if MFJ/MFS): <Legal Name>     SSN: <XXX-XX-XXXX>
Address: <Street, City, State, ZIP>
Main home in the U.S. more than half the year: <Yes | No>
Deceased (filer / spouse): <No | date of death>
Digital assets question: <Yes | No>

Dependents:
| # | First name | Last name | SSN | Relationship | (5a) Lived with you > half year | (5b) In the U.S. | (6) Student / Disabled | (7) CTC / ODC |
|---|------------|-----------|-----|--------------|------|------|------|------|
| 1 | ...        | ...       | ... | ...          | [x]  | [x]  | [ ] / [ ] | [x] / [ ] |

## Page 1 — Income
1a. Total W-2 wages:                  $X,XXX
1b. Household employee wages:         $X,XXX
1c. Tip income:                       $X,XXX
1d. Medicaid waiver payments:         $X,XXX
1e. Taxable dependent care benefits:  $X,XXX
1f. Adoption benefits:                $X,XXX
1g. Form 8919 wages:                  $X,XXX
1h. Other earned income:              $X,XXX
1i. Nontaxable combat pay election:   $X,XXX
1z. Sum of 1a-1h:                     $X,XXX

2a. Tax-exempt interest:              $X,XXX
2b. Taxable interest:                 $X,XXX
3a. Qualified dividends:              $X,XXX
3b. Ordinary dividends:               $X,XXX
3c. Child's dividends included:       [ ] 1 (3a)  [ ] 2 (3b)
4a. IRA distributions:                $X,XXX
4b. Taxable IRA distributions:        $X,XXX
4c. [ ] Rollover  [ ] QCD  [ ] Other
5a. Pensions and annuities:           $X,XXX
5b. Taxable pensions:                 $X,XXX
5c. [ ] Rollover  [ ] PSO  [ ] Other
6a. Social Security benefits:         $X,XXX
6b. Taxable SS:                       $X,XXX
6c. Lump-sum election:                [ ]
6d. MFS, lived apart all year:        [ ]
7a. Capital gain/loss (Sch D):        $X,XXX
7b. [ ] Schedule D not required  [ ] Includes child's capital gain or (loss)
8. Schedule 1 additional income:      $X,XXX
9. TOTAL INCOME:                      $X,XXX

10. Adjustments (Schedule 1 L26):     $X,XXX
11a. AGI:                             $X,XXX

## Page 2 — Deductions, Tax, Credits, Payments
11b. AGI (from 11a):                  $X,XXX
12a. Someone can claim: [ ] You  [ ] Your spouse
12b. Spouse itemizes on a separate return: [ ]   12c. Dual-status alien: [ ]
12d. You: [ ] born before Jan 2, 1961 [ ] blind   Spouse: [ ] born before Jan 2, 1961 [ ] blind
12e. Standard | Itemized deduction:   $X,XXX
13a. QBI deduction (Form 8995/8995-A): $X,XXX
13b. Schedule 1-A deductions (L38):   $X,XXX
14. Sum of 12e + 13a + 13b:           $X,XXX
15. TAXABLE INCOME:                   $X,XXX

16. Tax (method: <Tax Table | TCW | QDCG WS | Sch D WS>; boxes 8814/4972/other): $X,XXX
17. Schedule 2 Part I (Sch 2 L3):     $X,XXX
18. Sum (16 + 17):                    $X,XXX
19. CTC / ODC (Sch 8812 L14):         $X,XXX
20. Other credits (Sch 3 L8):         $X,XXX
21. Sum (19 + 20):                    $X,XXX
22. Line 18 − Line 21 (not below 0):  $X,XXX
23. Other taxes (Sch 2 L21):          $X,XXX
24. TOTAL TAX:                        $X,XXX

25a. W-2 withholding:                 $X,XXX
25b. 1099 withholding:                $X,XXX
25c. Other withholding:               $X,XXX
25d. Total withholding:               $X,XXX
26. Estimated tax payments + prior overpayment: $X,XXX
27a. EIC:                             $X,XXX   (27b clergy [ ]; 27c no EIC [ ])
28. Additional CTC (Sch 8812 L27):    $X,XXX   (decline box [ ])
29. Refundable AOTC (Form 8863 L8):   $X,XXX
30. Refundable adoption credit (Form 8839 L13): $X,XXX
31. Sch 3 L15:                        $X,XXX
32. Sum (27a + 28 + 29 + 30 + 31):    $X,XXX
33. TOTAL PAYMENTS (25d + 26 + 32):   $X,XXX

34. Overpayment (refund):             $X,XXX
35a. Refunded directly:               $X,XXX   (Form 8888 box [ ])
35b. Routing #:                       <to be entered at filing>
35c. Account type:                    <Checking | Savings>
35d. Account #:                       <to be entered at filing>
36. Applied to next year:             $X,XXX
37. Amount you owe:                   $X,XXX
38. Estimated tax penalty:            $X,XXX (or "leave blank")

## Required attachments
- [ ] Schedule 1 (additional income / adjustments)
- [ ] Schedule 1-A (tips, overtime, car loan interest, seniors)
- [ ] Schedule 2 (additional taxes)
- [ ] Schedule 3 (credits and payments)
- [ ] Schedule A (if itemizing)
- [ ] Schedule B (taxable interest over $1,500, ordinary dividends over $1,500, or foreign account / foreign trust)
- [ ] Schedule C (if self-employed; uses `schedule-c` skill)
- [ ] Schedule D + Form 8949 (capital gains; uses `schedule-d` and `form-8949` skills)
- [ ] Schedule E (rentals, K-1)
- [ ] Schedule SE (if net earnings from self-employment are $400 or more; uses `schedule-se` skill)
- [ ] Form 8995 / 8995-A (QBI)
- [ ] Schedule 8812 (CTC / ODC / ACTC)
- [ ] Form 2441 (dependent care)
- [ ] Form 8863 (education)
- [ ] Form 8889 (HSA; uses `form-8889` skill)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 15>

## Sources cited in this draft
- 2025 Form 1040 and 2025 Instructions for Form 1040
- IRC §1, §63, §24, §32, §151–152, §199A, §221
- Rev. Proc. 2024-40 (inflation adjustments for tax year 2025) and P.L. 119-21 (2025 standard deduction, CTC, Schedule 1-A)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 1040. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line on Form 1040 page 1 + page 2 with rules, examples, and edge cases
- [`references/filing-status.md`](./references/filing-status.md) — Five filing statuses with eligibility tests
- [`references/dependents.md`](./references/dependents.md) — Qualifying child and qualifying relative tests, CTC vs ODC
- [`references/tax-computation.md`](./references/tax-computation.md) — Tax Tables, Tax Computation Worksheet, QDCG Worksheet, Schedule D Tax Worksheet
- [`references/credits-overview.md`](./references/credits-overview.md) — CTC, EITC, AOTC, LLC, Saver's Credit, foreign tax credit
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Filing playbook: channel decision tree (Free File, FFFF, software, paper), FFFF field map for the 2025 form, paper assembly order and where to look up mailing addresses, consent and security rules (loaded only when the user authorizes filing)

## Examples

End-to-end worked Form 1040s. Use these as patterns when the user's situation is similar.

- [`examples/solo-consultant-with-schedule-c.md`](./examples/solo-consultant-with-schedule-c.md) — Single freelance consultant, $84,500 Schedule C, SEP-IRA, SE health insurance
- [`examples/w2-employee-with-side-hustle.md`](./examples/w2-employee-with-side-hustle.md) — W-2 day job + 1099-NEC freelance side income
- [`examples/married-filing-jointly-with-kids.md`](./examples/married-filing-jointly-with-kids.md) — MFJ with two qualifying children, CTC, dependent care credit

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [Form 1040 + AI Agent Skill: Complete US Tax Return Guide 2026](https://jupid.com/blog/form-1040-individual-tax-return-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1040 (2025 revision as of 2026-10-06)](https://www.irs.gov/pub/irs-pdf/f1040.pdf) — the form itself
- [Instructions for Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — line-by-line IRS guidance with worksheets, Tax Table (p. 68), Tax Computation Worksheet (p. 80), EIC tables, Schedule 1-A instructions, mailing addresses (p. 126)
- [About Form 1040](https://www.irs.gov/forms-pubs/about-form-1040) — IRS landing page with archive of past revisions
- [Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (taxpayer's complete reference)
- [Publication 501](https://www.irs.gov/publications/p501) — Dependents, Standard Deduction, and Filing Information
- [Publication 505](https://www.irs.gov/publications/p505) — Tax Withholding and Estimated Tax
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses
- [Publication 596](https://www.irs.gov/publications/p596) — Earned Income Credit
- [Publication 970](https://www.irs.gov/publications/p970) — Tax Benefits for Education
- IRC §1 (tax brackets), §24 (CTC), §32 (EITC), §63 (standard deduction), §151–152 (dependents), §199A (QBI), §221 (student loan interest), §6011/6012 (filing requirement)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025 (brackets, EITC, QBI thresholds); its 2025 standard deduction was superseded by P.L. 119-21 §70102
- P.L. 119-21 (One Big Beautiful Bill Act, July 4, 2025) — 2025 standard deduction, $2,200 CTC and SSN rules, SALT cap $40,000, Schedule 1-A deductions, refundable adoption credit
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — inflation adjustments for tax year 2026
- [IRS Free File](https://www.irs.gov/e-file-do-your-taxes-for-free) and [Free File Fillable Forms](https://www.irs.gov/e-file-providers/free-file-fillable-forms) — filing channels and season dates

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-state returns, AMT, foreign income, large estates, recent law changes) warrant a licensed tax professional's review.
