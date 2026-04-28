---
name: form-1040
description: |
  Use this skill when a US individual taxpayer needs to fill out Form 1040 for tax year 2026. Triggers: "fill out Form 1040", "file my federal income tax return", "individual tax return", "tax return for self-employed/W-2/freelancer".

  Do NOT use for: non-resident aliens (Form 1040-NR), amended returns (Form 1040-X), trusts/estates (Form 1041), corporations (Form 1120 or 1120-S).
form: Form 1040
audience: [individual, solo, freelance, llc1, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1040.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
---

# Form 1040 — U.S. Individual Income Tax Return

This skill produces an audit-grade draft of Form 1040 from the user's income, deductions, credits, payments, and dependent facts. It walks through every line on page 1 and page 2, applies the IRS rules at each line, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

Form 1040 is the cover sheet for the entire US individual return. Most of the heavy lifting happens on the schedules — Schedule 1, 2, 3, A, B, C, D, E, SE, and dozens of supporting forms. The 1040 itself is the single page (front and back) that pulls all of those into one number: refund or balance due. The math is mechanical. The judgment is in *which schedules apply*, *which credits the user qualifies for*, and *when a rule depends on a fact the user hasn't mentioned*. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Form 1040 (2026): Complete Individual Tax Return Guide](https://jupid.com/blog/form-1040-individual-tax-return-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1040, "1040", "individual tax return", "federal income tax return"
- The user describes filing for themselves (W-2 employee, self-employed, retired, mixed) for tax year 2025 or 2026
- The user wants a draft assembled from W-2s, 1099s, and supporting schedules they've already computed
- The user asks "how much tax do I owe" or "what's my refund" and is filing as an individual

Do **not** engage this skill when:

- The user is a non-resident alien → use Form 1040-NR (out of scope for this skill)
- The user is amending a prior-year return → use Form 1040-X (out of scope; different line numbers and reconciliation logic)
- The user is filing for a trust, estate, or fiduciary → use Form 1041
- The user is filing for a C-corporation → use Form 1120
- The user is filing for an S-corporation → use the (forthcoming) `form-1120-s` skill
- The user is filing a partnership return → Form 1065 (out of scope)

If the user's residency status is ambiguous (e.g., dual-status, recent green card holder, F-1 student), ask before proceeding. Resident aliens file Form 1040; non-resident aliens file Form 1040-NR; dual-status taxpayers file both with attached statements.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer. Do not default.

1. **Tax year** the return covers. Form 1040 for tax year 2025 is filed by April 15, 2026; for tax year 2026, by April 15, 2027. Numbers (standard deduction, brackets, CTC) depend on this.
2. **Filer's legal name and SSN/ITIN.** Must match the Social Security card exactly. Do not invent.
3. **Spouse's legal name and SSN/ITIN** if filing jointly or separately while married.
4. **Filing status** — Single, Married Filing Jointly (MFJ), Married Filing Separately (MFS), Head of Household (HoH), or Qualifying Surviving Spouse. See [`references/filing-status.md`](./references/filing-status.md). If user says "I'm married" without specifying joint or separate, ask which.
5. **Mailing address** as of the filing date.
6. **Dependents** — for each: name, SSN, relationship, months lived with taxpayer, and whether the dependent qualifies for CTC (under 17 at year-end + valid SSN) or ODC (other dependents). See [`references/dependents.md`](./references/dependents.md).
7. **Digital assets answer** — Yes if the user sold, exchanged, or otherwise disposed of crypto/NFTs/digital assets during the year; No if they only held.
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
10. **Standard or itemized deduction decision** — see [`references/line-by-line.md`](./references/line-by-line.md) Line 12. If itemizing, need Schedule A inputs.
11. **QBI inputs** — for Schedule C / Schedule E passthrough / K-1 income, the qualified business income amount and whether the user is in a Specified Service Trade or Business (SSTB).
12. **Credits the user might qualify for** — CTC, EITC, AOTC/LLC, Saver's Credit, foreign tax credit, dependent care, residential energy. See [`references/credits-overview.md`](./references/credits-overview.md).
13. **Payments already made** — W-2 federal withholding (box 2), 1099 withholding (box 4), quarterly estimated tax payments, prior-year overpayment applied.
14. **Refund routing** if expecting a refund — bank routing number, account number, account type (checking or savings). The agent should not store these — collect at filing time only.

If the user mentions they have a Schedule C / SE / E / D, treat those as separate skills (`schedule-c`, `schedule-se`, etc.) and import the bottom-line numbers.

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
| Vanguard brokerage    | 1099-DIV/1099-B | 1040 L3a/3b/7, Schedule D    |
| Traditional IRA RMD   | 1099-R        | 1040 Line 4a/4b               |
| Social Security       | SSA-1099      | 1040 Line 6a/6b               |
```

If any source is on a schedule the user hasn't computed yet (Schedule C, D, E, SE), pause and run the appropriate sibling skill first: `schedule-c`, `form-8949`, `schedule-se`. Do not invent the bottom-line numbers.

### Step 3 — Identify required schedules

Form 1040 is short; the schedules carry the weight. Identify which apply:

- **Schedule 1** — additional income (Schedule C profit, rentals, K-1, unemployment, COD) and above-the-line adjustments
- **Schedule 2** — additional taxes (SE tax, AMT, NIIT, Additional Medicare Tax, advance PTC repayment)
- **Schedule 3** — non-refundable credits (foreign tax, dependent care, education, retirement savings) and refundable payments (PTC, fuel credits)
- **Schedule A** — itemized deductions (only if itemizing instead of standard)
- **Schedule B** — if interest + dividends > $1,500 OR foreign accounts
- **Schedule C** — sole proprietor / SMLLC business income → use `schedule-c` skill
- **Schedule D + Form 8949** — capital gains → use `form-8949` skill
- **Schedule E** — rental, royalty, K-1 passthrough income
- **Schedule SE** — self-employment tax → use `schedule-se` skill
- **Form 8995 / 8995-A** — Qualified Business Income deduction
- **Schedule 8812** — refundable Child Tax Credit
- **Form 2441** — child and dependent care credit
- **Form 8863** — education credits (AOTC, LLC)
- **Form 8889** — HSA → use `form-8889` skill

For each schedule that applies, list it as a required attachment in the deliverable.

### Step 4 — Compute Page 1 income (Lines 1-9)

Walk lines 1a through 1z (wages). Then Lines 2a/2b (interest), 3a/3b (dividends), 4a/4b (IRA), 5a/5b (pensions), 6a/6b/6c (Social Security), 7 (capital gains from Schedule D), 8 (Schedule 1 additional income).

Sum to Line 9 (Total Income).

For Line 6b (taxable Social Security), use the Social Security Benefits Worksheet from the 1040 instructions. If combined income (AGI before SS + tax-exempt interest + half of SS) is below $25,000 single / $32,000 MFJ, none of SS is taxable. Above the second threshold ($34,000 single / $44,000 MFJ), up to 85% is taxable.

### Step 5 — Compute adjustments and AGI (Lines 10-11)

Line 10 = Schedule 1 Line 26 (above-the-line adjustments). Line 11 = Line 9 − Line 10 = **AGI**. Flag AGI explicitly in the deliverable — it's the base for many phaseouts and downstream calculations (IRMAA, FAFSA, Roth eligibility).

### Step 6 — Decide standard vs itemized (Line 12)

For 2025 (Rev. Proc. 2024-40):
- Single / MFS: $15,000
- MFJ / Qualifying Surviving Spouse: $30,000
- Head of Household: $22,500
- Additional for 65+ or blind: $1,600 each (MFJ/QSS); $2,000 each (Single/HoH)

For 2026, verify against the latest IRS Revenue Procedure (typically Rev. Proc. 2025-XX, announced October–November 2025). If the user has not provided 2026 figures, **ask** and reference the official source rather than estimating.

If the user has potential itemized deductions (large mortgage, high state tax, major medical, large charitable), run Schedule A and compare. Pick the larger of standard or itemized for Line 12.

### Step 7 — Compute QBI deduction (Line 13)

If the user has Schedule C profit, Schedule E passthrough income, qualifying REIT dividends, or PTP income:

- Below the income threshold ($241,950 single / $383,900 MFJ for 2025; verify 2026), use Form 8995 (simplified)
- Above threshold, use Form 8995-A (full) — SSTB phaseouts and W-2 wage / UBIA limits apply
- QBI deduction = lesser of (20% × QBI) or (20% × (taxable income before QBI − net capital gains))
- For self-employed filers, QBI is approximately Schedule C profit minus the deductible half SE tax, SE health insurance, and qualified retirement contributions

If the user qualifies but hasn't computed QBI, ask to run Form 8995 first.

### Step 8 — Compute taxable income (Lines 14-15)

Line 14 = Line 12 + Line 13. Line 15 = Line 11 − Line 14. If negative, enter 0. Line 15 is **taxable income** — the number tax is calculated on.

### Step 9 — Compute tax (Line 16)

Use the right method per [`references/tax-computation.md`](./references/tax-computation.md):
- Taxable income < $100,000 → Tax Tables (look up bracket)
- Taxable income ≥ $100,000 → Tax Computation Worksheet
- Has qualified dividends or net long-term capital gains → Qualified Dividends and Capital Gain Tax Worksheet (uses preferential 0/15/20% LTCG rates)
- Has 28%-rate gain (collectibles) or unrecaptured §1250 gain → Schedule D Tax Worksheet
- Has lump-sum SS election, foreign earned income exclusion, etc. → other worksheets

Show the worksheet used and the math.

### Step 10 — Apply credits and other taxes (Lines 17-23)

- Line 17 = Schedule 2 Line 3 (AMT, excess advance PTC, NIIT, Additional Medicare Tax)
- Line 18 = Line 16 + Line 17
- Line 19 = CTC / ODC non-refundable portion (from Schedule 8812)
- Line 20 = Schedule 3 Line 8 (other non-refundable credits)
- Line 21 = Line 18 − (Line 19 + Line 20), floored at 0
- Line 22 = Schedule 2 Line 21 (SE tax + other additional taxes)
- Line 23 = Line 21 + Line 22 — **total federal tax liability**

For self-employed filers, Line 22 is usually the largest line on page 2 (SE tax = 15.3% × 92.35% × Schedule C profit, up to the SS wage base).

### Step 11 — Compute payments and refundable credits (Lines 25-33)

- Lines 25a/25b/25c — federal income tax withheld from W-2s, 1099s, and other forms
- Line 26 — quarterly estimated tax payments + prior-year overpayment applied
- Line 27 — EITC (refundable; from EIC tables)
- Line 28 — Additional Child Tax Credit (refundable portion; from Schedule 8812)
- Line 29 — refundable AOTC (40% of AOTC, up to $1,000 per student)
- Line 31 — Schedule 3 Line 15 (refundable PTC, fuel credits, withholding excess)
- Line 32 = Lines 27 + 28 + 29 + 31
- Line 33 = Lines 25a + 25b + 25c + 26 + 32 — **total payments**

### Step 12 — Refund or balance due (Lines 34-38)

If Line 33 > Line 23: refund. Line 34 = Line 33 − Line 23. Lines 35a/b/c/d for direct deposit; Line 36 to apply to next year's estimated tax.

If Line 23 > Line 33: balance due. Line 37 = Line 23 − Line 33. Pay by April 15.

Line 38 = estimated tax penalty (Form 2210). Leave blank for the IRS to calculate, OR compute on Form 2210 if claiming the annualized income exception or wanting to verify the number.

### Step 13 — Run validation checks

See **Validation** below. Run every check.

### Step 14 — Produce the deliverable

See **Output format** below.

### Step 15 — Hand off downstream

State the next forms the user will need:

- All schedules used must be attached
- Schedule SE if self-employment net earnings > $400
- Form 1040-V payment voucher if mailing a payment
- Form 4868 if extending past April 15
- Form 1040-ES for next year's estimated tax payments

### Step 16 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree to pick a filing channel (FFFF, paid software, paper, IRS Direct File)
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
- **Digital assets question** — Yes if sold/exchanged/disposed of any crypto/NFT in the year; No if only held or received as gift/inheritance.
- **Standard deduction checkboxes** — check if (a) someone can claim the filer as a dependent, (b) spouse itemizes on a separate return, or (c) dual-status alien.
- **Age/blindness boxes** — increase the standard deduction.
- **Dependents grid** — name, SSN, relationship, CTC vs ODC checkbox per dependent. See [`references/dependents.md`](./references/dependents.md).

### Page 1 income (Lines 1-9)

- **1a-1z** — Wages and earned income. 1a is W-2 box 1 sum. 1z is total of 1a-1h.
- **2a/2b** — Tax-exempt and taxable interest.
- **3a/3b** — Qualified and ordinary dividends.
- **4a/4b**, **5a/5b** — Gross and taxable IRA / pension distributions.
- **6a/6b/6c** — Gross and taxable Social Security.
- **7** — Capital gain or loss (Schedule D).
- **8** — Schedule 1 additional income.
- **9** — Total income (sum of 1z + 2b + 3b + 4b + 5b + 6b + 7 + 8).

### AGI to taxable income (Lines 10-15)

- **10** — Schedule 1 Line 26 adjustments (above-the-line).
- **11** — AGI.
- **12** — Standard deduction or Schedule A itemized.
- **13** — QBI deduction (Form 8995 or 8995-A).
- **14** — Sum of 12 + 13.
- **15** — Taxable income.

### Page 2 tax + credits + payments (Lines 16-38)

- **16** — Tax computed from Line 15.
- **17–23** — Credits applied; SE tax and other taxes added; total tax liability.
- **25–33** — Payments tallied.
- **34–37** — Refund or balance due.
- **38** — Estimated tax penalty (optional self-compute).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails.

### Math checks

- [ ] Line 1z = sum of 1a + 1b + 1c + 1d + 1e + 1f + 1g + 1h
- [ ] Line 9 = 1z + 2b + 3b + 4b + 5b + 6b + 7 + 8
- [ ] Line 11 = Line 9 − Line 10
- [ ] Line 14 = Line 12 + Line 13
- [ ] Line 15 = Line 11 − Line 14 (floored at 0)
- [ ] Line 16 matches the tax computation method used (Tax Tables, Tax Computation Worksheet, or QDCG Worksheet)
- [ ] Line 18 = Line 16 + Line 17
- [ ] Line 21 = Line 18 − (Line 19 + Line 20), floored at 0
- [ ] Line 23 = Line 21 + Line 22
- [ ] Line 32 = Lines 27 + 28 + 29 + 31
- [ ] Line 33 = Lines 25a + 25b + 25c + 26 + 32
- [ ] Either Line 34 or Line 37 is populated, not both
- [ ] Line 34 (if refund) = Line 33 − Line 23
- [ ] Line 37 (if owed) = Line 23 − Line 33

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filing status is HoH but no qualifying person listed in dependents → likely wrong status
- [ ] Filing status is MFJ but only one SSN provided → missing spouse SSN
- [ ] Schedule C exists in inputs but Line 8 (Schedule 1 income) is 0 → Schedule C profit didn't flow through
- [ ] Schedule SE exists but Line 22 (other taxes) is 0 → SE tax didn't flow through
- [ ] Self-employment income but no Schedule 1 Line 15 (half SE tax adjustment) → missing the deduction
- [ ] Self-employed but no QBI on Line 13 → likely missed the 20% deduction
- [ ] Standard deduction taken but Schedule A items mentioned → consider itemizing
- [ ] HoH or single with > 1 dependent but no CTC/ODC on Line 19 → check if dependents are correctly flagged
- [ ] Digital assets question left blank → must be answered Yes or No
- [ ] AGI > $200K single / $400K MFJ but no Additional Medicare Tax on Line 17 → check Form 8959
- [ ] AGI > $200K single / $250K MFJ with investment income but no NIIT on Line 17 → check Form 8960
- [ ] No quarterly estimates (Line 26 = 0) and Line 23 > $5,000 → likely underpayment penalty (Line 38)
- [ ] EITC claimed but earned income / AGI exceeds the EITC limit for the filer's status and number of children

### Cross-form checks

- [ ] If Schedule C profit > $400, Schedule SE must be attached and Line 22 must include SE tax
- [ ] If Schedule A used, Line 12 = Schedule A Line 17 (not the standard deduction)
- [ ] If Form 8995 used, Line 13 = Form 8995 Line 15
- [ ] If Schedule 8812 used, Line 19 ≤ Schedule 8812 Line 14 (non-refundable cap) and Line 28 = Schedule 8812 Line 27 (refundable)

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 1040 or paste into tax software. Format:

```markdown
# Form 1040 — DRAFT for tax year YYYY

## Header
Filing status: <Single | MFJ | MFS | HoH | QSS>
Filer name: <Legal Name>     SSN: <XXX-XX-XXXX>
Spouse name (if MFJ/MFS): <Legal Name>     SSN: <XXX-XX-XXXX>
Address: <Street, City, State, ZIP>
Digital assets question: <Yes | No>
Someone can claim you as dependent: <Yes | No>
Spouse itemizes on separate return: <Yes | No>
You 65+: <Yes | No>     Spouse 65+: <Yes | No>
You blind: <Yes | No>    Spouse blind: <Yes | No>

Dependents:
| Name | SSN | Relationship | CTC | ODC |
|------|-----|--------------|-----|-----|
| ...  | ... | ...          | [x] | [ ] |

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
4a. IRA distributions:                $X,XXX
4b. Taxable IRA distributions:        $X,XXX
5a. Pensions and annuities:           $X,XXX
5b. Taxable pensions:                 $X,XXX
6a. Social Security benefits:         $X,XXX
6b. Taxable SS:                       $X,XXX
6c. Lump-sum election:                [ ]
7. Capital gain/loss (Sch D):         $X,XXX
8. Schedule 1 additional income:      $X,XXX
9. TOTAL INCOME:                      $X,XXX

10. Adjustments (Schedule 1 L26):     $X,XXX
11. AGI:                              $X,XXX
12. Standard | Itemized deduction:    $X,XXX
13. QBI deduction (Form 8995):        $X,XXX
14. Sum of 12 + 13:                   $X,XXX
15. TAXABLE INCOME:                   $X,XXX

## Page 2 — Tax, Credits, Payments
16. Tax (method: <Tax Tables | TCW | QDCG WS | Sch D WS>):    $X,XXX
17. Other taxes (Sch 2 L3):           $X,XXX
18. Sum:                              $X,XXX
19. CTC / ODC (Sch 8812):             $X,XXX
20. Other credits (Sch 3 L8):         $X,XXX
21. Subtract:                         $X,XXX
22. Other taxes (Sch 2 L21):          $X,XXX
23. TOTAL TAX:                        $X,XXX

25a. W-2 withholding:                 $X,XXX
25b. 1099 withholding:                $X,XXX
25c. Other withholding:               $X,XXX
26. Estimated tax payments + prior overpayment: $X,XXX
27. EITC:                             $X,XXX
28. Additional CTC (Sch 8812):        $X,XXX
29. Refundable AOTC:                  $X,XXX
31. Sch 3 L15 refundable:             $X,XXX
32. Sum (27 + 28 + 29 + 31):          $X,XXX
33. TOTAL PAYMENTS:                   $X,XXX

34. Overpayment (refund):             $X,XXX
35a. Refunded directly:               $X,XXX
35b. Routing #:                       <to be entered at filing>
35c. Account type:                    <Checking | Savings>
35d. Account #:                       <to be entered at filing>
36. Applied to next year:             $X,XXX
37. Amount you owe:                   $X,XXX
38. Estimated tax penalty:            $X,XXX (or "leave blank")

## Required attachments
- [ ] Schedule 1 (additional income / adjustments)
- [ ] Schedule 2 (additional taxes)
- [ ] Schedule 3 (credits and payments)
- [ ] Schedule A (if itemizing)
- [ ] Schedule B (if interest + dividends > $1,500 or foreign accounts)
- [ ] Schedule C (if self-employed; uses `schedule-c` skill)
- [ ] Schedule D + Form 8949 (capital gains; uses `form-8949` skill)
- [ ] Schedule E (rentals, K-1)
- [ ] Schedule SE (if SE earnings > $400; uses `schedule-se` skill)
- [ ] Form 8995 / 8995-A (QBI)
- [ ] Schedule 8812 (CTC)
- [ ] Form 2441 (dependent care)
- [ ] Form 8863 (education)
- [ ] Form 8889 (HSA; uses `form-8889` skill)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 15>

## Sources cited in this draft
- IRS Form 1040 (revision date YYYY-MM-DD)
- IRS Instructions for Form 1040 (revision date YYYY-MM-DD)
- IRC §1, §63, §24, §32, §151–152, §199A, §221
- Rev. Proc. 2024-40 (inflation adjustments for tax year 2025)
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
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files the completed Form 1040 via FFFF, paper, or generic tax software (loaded only when the user authorizes filing)

## Examples

End-to-end worked Form 1040s. Use these as patterns when the user's situation is similar.

- [`examples/solo-consultant-with-schedule-c.md`](./examples/solo-consultant-with-schedule-c.md) — Single freelance consultant, $84,500 Schedule C, SEP-IRA, SE health insurance
- [`examples/w2-employee-with-side-hustle.md`](./examples/w2-employee-with-side-hustle.md) — W-2 day job + 1099-NEC freelance side income
- [`examples/married-filing-jointly-with-kids.md`](./examples/married-filing-jointly-with-kids.md) — MFJ with two qualifying children, CTC, dependent care credit

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [Form 1040 (2026): Complete Individual Tax Return Guide](https://jupid.com/blog/form-1040-individual-tax-return-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1040 (latest)](https://www.irs.gov/pub/irs-pdf/f1040.pdf) — the form itself
- [Instructions for Form 1040 (latest)](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — line-by-line IRS guidance with worksheets, Tax Tables, and EIC tables
- [About Form 1040](https://www.irs.gov/forms-pubs/about-form-1040) — IRS landing page with archive of past revisions
- [Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (taxpayer's complete reference)
- [Publication 501](https://www.irs.gov/publications/p501) — Dependents, Standard Deduction, and Filing Information
- [Publication 505](https://www.irs.gov/publications/p505) — Tax Withholding and Estimated Tax
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses
- [Publication 596](https://www.irs.gov/publications/p596) — Earned Income Credit
- [Publication 970](https://www.irs.gov/publications/p970) — Tax Benefits for Education
- IRC §1 (tax brackets), §24 (CTC), §32 (EITC), §63 (standard deduction), §151–152 (dependents), §199A (QBI), §221 (student loan interest), §6011/6012 (filing requirement)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025 (standard deduction, brackets, CTC, EITC)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-state returns, AMT, foreign income, large estates, recent law changes) warrant a licensed tax professional's review.
