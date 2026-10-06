---
name: form-8995-a
description: >
  Use this skill when a sole proprietor, S-corp shareholder, partnership member,
  or REIT/PTP investor needs to compute the Qualified Business Income (QBI)
  deduction under IRC §199A AND their taxable income before QBI exceeds the
  threshold ($197,300; $394,600 MFJ for 2025) OR they are a patron of an
  agricultural or horticultural cooperative. Above the threshold it applies the
  W-2 wage / UBIA limit and the Specified Service Trade or Business (SSTB —
  health, law, accounting, consulting, athletes, performing arts, financial
  services, brokerage, investing) phase-out. Triggers on phrases like "Form 8995-A", "QBI deduction over
  income threshold", "Section 199A SSTB", "qualified business income deduction
  high income", "QBI for consultant/lawyer/doctor", "phase-in QBI", "W-2 wage
  limit QBI". Do NOT use for filers at or below the threshold who are not
  cooperative patrons, even with an SSTB (use the simplified form-8995 skill),
  W-2 employees (no QBI), or C-corp shareholders (no QBI).
form: Form 8995-A
audience: [solo, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8995a.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8995a.pdf
---

# Form 8995-A — Qualified Business Income Deduction (Full Version)

This skill produces an audit-grade draft of Form 8995-A, including any required Schedules A, B, C, and D, from the user's QBI sources, W-2 wage data, UBIA records, taxable income, and SSTB classification. It walks through the form line by line, applies the §199A rules at each step, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The math is mechanical once the inputs are clean. The judgment is in (1) whether to use Form 8995-A vs. the simplified Form 8995, (2) which businesses are SSTBs, (3) whether to aggregate, (4) the SE-tax / SE-HI / SE-retirement adjustments to QBI, and (5) the W-2 / UBIA limit interaction with the SSTB phase-in. This skill optimizes for those — the agent should ask, not guess, when any input is ambiguous.

Line map verified against the **2025 Form 8995-A** (Created 9/12/25), **2025 Schedule A (Form 8995-A)** (Created 12/12/25), **Schedules B, C and D (Form 8995-A) (Rev. December 2022)**, and the **2025 Instructions for Form 8995-A** (Jan 26, 2026), the revision filed in 2026 for tax year 2025. The 2026 draft Form 8995-A (https://www.irs.gov/pub/irs-dft/f8995a--dft.pdf) changes the threshold and phase-in amounts and renumbers the end of Part IV: line 39 (deduction before the minimum), line 40 (OBBBA $400 minimum deduction), line 41 (total), line 42 (REIT/PTP carryforward), line 43 (ESBT box). Re-check the final revision before use: https://www.irs.gov/forms-pubs/about-form-8995-a

**Companion guide for end users:** [Form 8995-A + AI Agent Skill: Full QBI Deduction Guide 2026](https://jupid.com/blog/form-8995-a-qbi-deduction-full-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **all** of the following are true:

- The user has at least one source of qualified business income: Schedule C, S-corp K-1, partnership K-1, qualifying Schedule E rental, qualified REIT dividends, or qualified PTP income, AND
- Either (a) their taxable income BEFORE the QBI deduction exceeds the §199A threshold for their filing status, OR (b) they are a patron of an agricultural or horticultural cooperative (2025 Instructions for Form 8995-A, "Who Can Take the Deduction")

Quick threshold check (2025: Rev. Proc. 2024-40 §2.27; 2026: Rev. Proc. 2025-32 §4.26):

- **2025, all returns other than MFJ**: threshold $197,300, phase-in top $247,300 (range $50,000)
- **2025, MFJ**: threshold $394,600, phase-in top $494,600 (range $100,000)
- **2026**: single/HOH $201,750 → $276,750; MFS $201,775 → $276,775; MFJ $403,500 → $553,500 (range $75,000 / $150,000 under P.L. 119-21 §70105)

Do **not** engage this skill when:

- Taxable income before QBI is at or below the threshold and the user is not a cooperative patron → use the [`form-8995`](../form-8995/SKILL.md) skill (an SSTB at or below the threshold is treated as a qualified trade or business)
- The user is a W-2 employee with no business income → wages are not QBI; nothing to compute
- The user is a C-corp shareholder → C-corp income is taxed at the corporate rate, not §199A
- The user's only income is capital gains, ordinary dividends, or interest → not QBI
- The user has only foreign-source income that doesn't rise to a US trade or business

If the user's threshold position or SSTB status is ambiguous, **ask before proceeding**. The most common confusion: a developer who calls the work "consulting". Software development is not a listed SSTB field, and consulting means advice and counsel; it does not include the performance of services other than advice and counsel (Treas. Reg. §1.199A-5(b)(2)(vii)). Ask what the client pays for: written code or advice.

---

## Prerequisites

Before producing anything, the agent must have these eight inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 8995-A for tax year 2025 is filed in 2026; thresholds depend on the year.

2. **Filing status** — Single, HoH, MFS, MFJ, or QSS. Determines threshold and phase-in width.

3. **Taxable income BEFORE the QBI deduction.** For 2025 this is Form 1040 line 11a (AGI) minus line 12e (standard or itemized deduction) minus line 13b (Schedule 1-A deductions). Do NOT subtract line 13a (the deduction we're computing). Source: 2025 Instructions for Form 8995-A, "Taxable income before QBI deduction". Required to determine threshold position and SSTB phase-in percentage.

4. **For each trade or business**:
   - Business name
   - Whether it's an SSTB (see [`references/sstb-classification.md`](./references/sstb-classification.md))
   - QBI: net of all §199A-eligible income, gain, deduction, loss, allocable to that business
   - W-2 wages paid by the business (calendar year ending in the tax year)
   - UBIA of qualified property (depreciable tangible property within its depreciable period)
   - For S-corps and partnerships: the Section 199A statement (S-corp box 17 code V; partnership box 20 code Z) with QBI, W-2 wages, UBIA and SSTB status. The owner's S-corp wages are not QBI but are part of the corporation's W-2 wages; K-1 box 1 is already after the corporation's wage deduction

5. **Net capital gain** for Part IV Line 34: Form 1040 line 3a (qualified dividends) plus the smaller of Schedule D line 15 or 16 (nothing if either is zero or less), or Form 1040 line 7a if Schedule D isn't required (2025 i8995-A, Line 34).

6. **REIT dividends and PTP income** (from 1099-DIV Box 5 and K-1 box 17/20). These are NOT subject to the W-2/UBIA limit but DO appear on Part IV.

7. **Carryforward from prior years**: QBI net loss carryforward (prior-year Schedule C (Form 8995-A) line 6, or Form 8995 line 16) and REIT/PTP loss carryforward (prior-year Form 8995-A line 40, or Form 8995 line 17).

8. **Owner-level deductions attributable to each business**: the deductible portion of SE tax (½ SE tax), self-employed health insurance, and SE retirement contributions, for Schedule C filers and for partners with SE income. These reduce QBI per Treas. Reg. §1.199A-3(b)(1)(vi). Also ask about qualified tips deducted under §224 (Schedule 1-A, 2025 and later): they are not QBI and not W-2 wages for the limitation (2025 i8995-A).

For aggregation (Schedule B), additionally ask:
- Common ownership ≥50% across all businesses?
- Same tax year for all?
- None of them is an SSTB?
- Two of three sharing factors (same products/services, shared facilities, operating coordination)?

For cooperative patrons (Schedule D), additionally ask:
- Form 1099-PATR (Rev. April 2025) box 7 (qualified payments, §199A(b)(7)) → Schedule D patron reduction; box 6 (section 199A(g) deduction) → Part IV line 38; boxes 8–9 (§199A(a) qualified items / SSTB items)

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm Form 8995-A is the right form

Compute taxable income before QBI. Compare to threshold. If at or below the threshold AND not a cooperative patron → redirect to the simplified `form-8995` skill. If over threshold OR a cooperative patron → continue.

### Step 2 — Classify each business

For each trade or business, decide SSTB or not using [`references/sstb-classification.md`](./references/sstb-classification.md). Ask the user to confirm any borderline classification. The 11 SSTB categories per IRC §199A(d)(2)(A) are: health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage, investing/investment management, and trading/dealing in securities/partnerships/commodities — plus the "reputation or skill" catch-all.

### Step 3 — Compute QBI per business

For Schedule C filers: QBI = Schedule C Line 31 net profit MINUS (½ SE tax allocable + SE health insurance allocable + SE retirement contribution allocable + qualified tips deducted under §224). All allocable to that specific business.

For S-corp K-1: QBI = the QBI on the box 17 code V statement. Do NOT subtract the owner's W-2 again: the corporation already deducted it in computing box 1 and the statement's QBI (Treas. Reg. §1.199A-3(b)(2)(ii)(H)). Subtract owner-level items such as a >2% shareholder's SE health insurance deduction.

For partnership K-1: QBI = the QBI on the box 20 code Z statement. Guaranteed payments (box 4) are not QBI and are already deducted in box 1. Subtract partner-level items (½ SE tax on partnership SE income, unreimbursed partnership expenses).

For qualifying Schedule E rental: QBI = net rental income, only if the rental rises to a §162 trade or business OR meets the Rev. Proc. 2019-38 safe harbor (250+ hours of rental services, separate books, contemporaneous records, statement attached).

See [`references/qbi-computation.md`](./references/qbi-computation.md) for full mechanics including state tax adjustments and trader vs. investor distinctions.

### Step 4 — Check threshold position for SSTB businesses

For each SSTB:
- Below threshold → would use Form 8995 (out of scope here)
- In phase-in zone → complete Schedule A: applicable percentage (line 10) times QBI, W-2 wages and UBIA; enter the results on Form 8995-A lines 2, 4 and 7 (or on Schedule C (Form 8995-A) for loss netting)
- Above phase-in top → the SSTB's QBI, W-2 wages and UBIA are not taken into account at all (2025 i8995-A, "SSTBs excluded…")

For non-SSTB businesses: no Schedule A. In the phase-in range, the W-2/UBIA limit itself is phased in through Part III; above the phase-in top it applies in full.

### Step 5 — Decide whether to aggregate

If multiple non-SSTB businesses with shared ownership and operations, consider Schedule B aggregation when one business has high QBI but low W-2 wages (would otherwise be limited) and another has high W-2 wages. See [`references/aggregation.md`](./references/aggregation.md).

**Aggregation is a binding multi-year election** (Treas. Reg. §1.199A-4(c)(1)). Confirm with the user.

### Step 6 — Loss netting (Schedule C of Form 8995-A) before Part I

If any business has a qualified business loss this year, or there is a QBI net loss carryforward, complete Schedule C (Form 8995-A) first (2025 i8995-A). It apportions losses to the businesses with positive QBI in proportion to their QBI; column (c) feeds Part II line 2. A business whose adjusted QBI is zero or less reports zero W-2 wages and UBIA. If the total is still negative, line 6 carries forward and this year's QBI component is $0.

### Step 7 — Compute Parts II and III for each business

For each business (columns A–C), complete Part II:
- L2: QBI (after Schedule A and Schedule C, if used)
- L3: 20% of L2 (at or below the threshold, skip lines 4–12 and enter L3 on L13)
- L4: W-2 wages (after Schedule A, if used)
- L5: 50% × L4
- L6: 25% × L4
- L7: UBIA (after Schedule A, if used)
- L8: 2.5% × L7
- L9: L6 + L8
- L10: greater of L5 or L9 (the W-2/UBIA limit)
- L11: smaller of L3 or L10
- L12: phased-in reduction = Part III line 26, if any
- L13: greater of L11 or L12
- L14: patron reduction (Schedule D line 6)
- L15: L13 − L14
- L16: total of all L15 amounts

Part III (lines 17–26) only when taxable income is above the threshold but not above the phase-in top AND line 10 < line 3: L17 = L3; L18 = L10; L19 = L17 − L18; L20 taxable income before QBI; L21 threshold; L22 = L20 − L21; L23 phase-in range; L24 = L22 ÷ L23; L25 = L19 × L24; L26 = L17 − L25 (→ L12).

### Step 8 — Complete Part IV

- L27: line 16
- L28: qualified REIT dividends and PTP income or (loss) (include Schedule A line 24 for SSTB PTPs)
- L29: prior-year REIT/PTP loss carryforward (negative)
- L30: L28 + L29 (if less than zero, 0); L31: 20% × L30
- L32: L27 + L31
- L33: taxable income before QBI deduction
- L34: net capital gain plus qualified dividends
- L35: L33 − L34 (if zero or less, 0)
- L36: 20% × L35 (income limitation)
- L37: smaller of L32 or L36
- L38: §199A(g) DPAD allocated from a cooperative (1099-PATR box 6); not more than L33 − L37
- L39: L37 + L38 → 2025 Form 1040 line 13a
- L40: L28 + L29 if negative (REIT/PTP loss carryforward), else 0

### Step 9 — Run validation checks

See **Validation** below. Run every check.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next steps:

- The Line 39 result flows to **Form 1040 line 13a** (2025)
- If any QBI loss carries forward (Schedule C (Form 8995-A) line 6) or REIT/PTP loss carries forward (line 40), note the amount and the next-year line (Schedule C line 2 / Form 8995 line 3; Form 8995-A line 29 / Form 8995 line 7)
- If aggregation was elected, note that this is binding for future years and the same aggregation must be used
- For S-corp owners: confirm reasonable comp documentation (the wage-vs-distribution decision interacts with both QBI and SS/Medicare)

### Step 12 — File the return (optional)

If the user wants the agent to e-file, follow [`filing.md`](./filing.md). Form 8995-A is attached to Form 1040; it's not filed separately.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Trade, business, or aggregation information

- **L1(a)** — Name of each business, or "Aggregation 1, 2, 3" for a Schedule B aggregation
- **L1(b)** — Check if specified service (SSTB)
- **L1(c)** — Check if aggregation
- **L1(d)** — TIN: EIN (a disregarded single-member LLC's EIN), else SSN/ITIN; leave blank for an aggregation
- **L1(e)** — Check if patron of an agricultural or horticultural cooperative

Three rows (A, B, C) fit on the form; with four or more businesses, attach a statement with Parts I–III for the extra ones (2025 i8995-A, Line 2).

### Part II — Adjusted QBI per business

(See Step 7 above for line-by-line.)

Critical:
- L2 (QBI) must reflect owner-level deductions (½ SE tax, SE health insurance, SE retirement) and come from the Section 199A statement for K-1 sources; never subtract an S-corp owner's wages from box 1 a second time
- L4 (W-2 wages) uses Forms W-2 for the calendar year ending with or within the tax year, under one of the three methods in the instructions (unmodified box, modified box 1, tracking wages); excludes amounts deducted under §224
- L7 (UBIA) excludes land and intangibles; only depreciable tangible property within its depreciable period
- L10 (W-2/UBIA limit) is the GREATER of the two formulas
- L13 is the GREATER of L11 or L12 (L12 comes from Part III)

### Part III — Phased-in reduction

Only when taxable income is in the phase-in range and line 10 is less than line 3. Phases in the W-2/UBIA limitation for SSTBs and non-SSTBs alike. Result (line 26) goes to line 12. See [`references/sstb-phase-in.md`](./references/sstb-phase-in.md) for the full math.

### Part IV — QBI deduction

- L27: line 16
- L28-31: REIT/PTP component (no W-2/UBIA limit applies)
- L32: total before the income limitation
- L33-36: income limitation = 20% × (taxable income − net capital gain)
- L37: smaller of L32 or L36
- L38: §199A(g) DPAD from a cooperative
- L39: L37 + L38 → Form 1040 line 13a
- L40: REIT/PTP loss carryforward

### Schedule A — SSTB applicable percentage

Part I (lines 1a–13) for SSTBs other than PTPs: applicable percentage (line 10 = 100% − (line 7 ÷ line 8)) times QBI (line 11 → Form 8995-A line 2 or Schedule C), W-2 wages (line 12 → line 4) and UBIA (line 13 → line 7). Part II (lines 14–24) for SSTB PTP income (line 24 → Form 8995-A line 28). See [`references/sstb-phase-in.md`](./references/sstb-phase-in.md).

### Schedule B — Aggregation

Description of each aggregation and the factors met, changes from the prior year, and per-business QBI, W-2 wages and UBIA with totals (line 4) that go to Schedule C or Part II. See [`references/aggregation.md`](./references/aggregation.md).

### Schedule C — Loss netting and carryforward

Allocates losses (and the prior-year carryforward, line 2) across positive-QBI businesses in proportion to their QBI; line 6 is the carryforward to next year. See [`references/loss-netting.md`](./references/loss-netting.md).

### Schedule D — Cooperative patrons

Patron reduction = smaller of 9% of QBI allocable to qualified payments (line 3) or 50% of W-2 wages allocable to them (line 5); line 6 → Form 8995-A line 14. Skip if not a patron.

---

## Validation

Before declaring the form ready, run these checks. Surface any failure — don't silently fix.

### Math checks

- [ ] Each Part II column: L3 = 0.20 × L2; L5 = 0.50 × L4; L6 = 0.25 × L4; L8 = 0.025 × L7; L9 = L6 + L8
- [ ] L10 = max(L5, L9)
- [ ] L11 = min(L3, L10)
- [ ] If Part III used: L19 = L17 − L18; L24 = L22 ÷ L23; L25 = L19 × L24; L26 = L17 − L25 = L12
- [ ] L13 = max(L11, L12); L15 = L13 − L14 (not below 0); L16 = sum of L15
- [ ] If Schedule A used: line 10 = 100% − (line 7 ÷ line 8); lines 11–13 = lines 2–4 × line 10, carried to Form 8995-A lines 2, 4, 7
- [ ] L27 = L16
- [ ] L30 = max(0, L28 + L29); L31 = 0.20 × L30
- [ ] L32 = L27 + L31
- [ ] L35 = max(0, L33 − L34)
- [ ] L36 = 0.20 × L35
- [ ] L37 = min(L32, L36); L39 = L37 + L38
- [ ] L39 ≥ 0 (deduction can never be negative); L40 = min(0, L28 + L29)

### Sanity checks

Surface a warning, do not block:

- [ ] Taxable income before QBI ≤ threshold AND not a cooperative patron → user should file Form 8995, not 8995-A
- [ ] Filer is S-corp owner AND the owner's wages were subtracted from box 1 (double subtraction) or box 1 was used instead of the code V statement QBI → ask
- [ ] Filer is Schedule C AND QBI = Line 31 net profit (no SE-tax / SE-HI / SE-retirement reduction) → ask
- [ ] UBIA includes any line item described as "land" → must be excluded
- [ ] L4 W-2 wages > Schedule C Line 26 wages by more than 10% → reconciliation needed
- [ ] L7 UBIA exceeds total depreciable basis in service per Form 4562 → ask
- [ ] SSTB above phase-in top → confirm its QBI, W-2 wages and UBIA were left out entirely
- [ ] Net capital gains > taxable income before QBI → unusual; double-check the input

### Cross-form checks

- [ ] L39 matches what's entered on Form 1040 line 13a
- [ ] If aggregating, the same aggregation must appear on next year's Form 8995-A (Schedule B every year)
- [ ] S-corp owner's W-2 from the corp is included in Form 1040 line 1a and in the corporation's W-2 wages on L4

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 8995-A or paste into tax software. Format:

```markdown
# Form 8995-A — DRAFT for tax year YYYY

## Filing Information
Taxpayer: <name>
SSN/ITIN: <provided>
Filing status: <Single | HoH | MFS | MFJ | QSS>
Taxable income before QBI: $<amount>
Threshold for status: $<197,300 | 394,600 (2025)>
Phase-in top: $<amount>
Position: <below threshold | in phase-in | above phase-in top>

## Part I — Trades or Businesses
| (a) Name | (b) SSTB | (c) Aggregation | (d) TIN | (e) Patron |
|----------|----------|-----------------|---------|------------|
| <name 1> | Yes/No   | Yes/No          | <id>    | Yes/No     |
| <name 2> | Yes/No   | Yes/No          | <id>    | Yes/No     |

## Part II — Adjusted QBI per Business
### Business 1: <name>
 2. QBI:                      $X,XXX
 3. 20% × L2:                 $X,XXX
 4. W-2 wages:                $X,XXX
 5. 50% × L4:                 $X,XXX
 6. 25% × L4:                 $X,XXX
 7. UBIA:                     $X,XXX
 8. 2.5% × L7:                $X,XXX
 9. L6 + L8:                  $X,XXX
10. Greater of L5 or L9:      $X,XXX
11. Smaller of L3 or L10:     $X,XXX
12. Phased-in reduction (Part III L26): $X,XXX
13. Greater of L11 or L12:    $X,XXX
14. Patron reduction (Sch D): $X,XXX
15. QBI component (L13 − L14): $X,XXX
16. Total of all L15:         $X,XXX

(repeat lines 2-15 for each business)

## Part III — Phased-in Reduction  (or "N/A — not in phase-in range, or L10 ≥ L3")
17. L3: $X,XXX   18. L10: $X,XXX   19. L17 − L18: $X,XXX
20. Taxable income before QBI: $X,XXX
21. Threshold: $X,XXX   22. L20 − L21: $X,XXX
23. Phase-in range: $50,000 | $100,000 (2025)
24. L22 ÷ L23: XX.XX%
25. L19 × L24: $X,XXX
26. L17 − L25 → L12: $X,XXX

## Schedule A — SSTB  (or "N/A — no SSTB in phase-in range")
 1a/1b. Trade name / TIN:     <name> / <id>
 2. QBI:                      $X,XXX
 3. W-2 wages:                $X,XXX
 4. UBIA:                     $X,XXX
 5. Taxable income before QBI: $X,XXX
 6. Threshold:                $X,XXX
 7. L5 − L6:                  $X,XXX
 8. Phase-in range:           $50,000 | $100,000 (2025)
 9. L7 ÷ L8:                  0.XXXXX
10. Applicable % (100% − L9): XX.XXX%
11. L2 × L10 → Form 8995-A L2 (or Sch C): $X,XXX
12. L3 × L10 → Form 8995-A L4: $X,XXX
13. L4 × L10 → Form 8995-A L7: $X,XXX

## Schedule B — Aggregation  (or "N/A")
List of businesses aggregated, with eligibility factors confirmed.

## Schedule C — Loss Netting  (or "N/A — no QBI losses")
Allocation of negative QBI across positive-QBI businesses.

## Schedule D — Cooperative Patron  (or "N/A")
Patron reduction: smaller of 9% × QBI allocable to qualified payments or 50% × allocable W-2 wages → Part II L14.

## Part IV — QBI Deduction
27. Total QBI component (L16): $X,XXX
28. Qualified REIT/PTP income or (loss): $X,XXX
29. Prior-year REIT/PTP loss carryforward: ($X,XXX)
30. L28 + L29 (≥ 0):           $X,XXX
31. 20% × L30:                 $X,XXX
32. L27 + L31:                 $X,XXX
33. Taxable income before QBI: $X,XXX
34. Net capital gain + qualified dividends: $X,XXX
35. L33 − L34 (≥ 0):           $X,XXX
36. 20% × L35:                 $X,XXX
37. Smaller of L32 or L36:     $X,XXX
38. DPAD under §199A(g):       $X,XXX (or 0)
39. **Total QBI deduction (L37 + L38):** $X,XXX  → Form 1040 line 13a
40. REIT/PTP loss carryforward: ($X,XXX) or 0

## Loss carryforwards to next year
- QBI loss carryforward (Schedule C (Form 8995-A) line 6): $X,XXX (or 0)
- REIT/PTP loss carryforward (line 40): $X,XXX (or 0)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 8995-A (revision date YYYY-MM-DD)
- IRS Instructions for Form 8995-A (revision date YYYY-MM-DD)
- IRC §199A
- Treas. Reg. §1.199A-1 through §1.199A-6
- Rev. Proc. 2024-40 §2.27 (2025 thresholds)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 8995-A. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8995-A line including all four schedules
- [`references/sstb-classification.md`](./references/sstb-classification.md) — The 11 SSTB categories with examples and edge cases
- [`references/sstb-phase-in.md`](./references/sstb-phase-in.md) — Schedule A computation with worked numbers
- [`references/qbi-computation.md`](./references/qbi-computation.md) — How QBI is computed for Schedule C, S-corp, partnership, rental
- [`references/aggregation.md`](./references/aggregation.md) — Schedule B aggregation rules under Treas. Reg. §1.199A-4
- [`references/loss-netting.md`](./references/loss-netting.md) — Schedule C of Form 8995-A loss allocation rules
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 8995-A as part of Form 1040 via FFFF, paid software, or paper

## Examples

End-to-end worked Form 8995-As. Use these as patterns when the user's situation is similar.

- [`examples/sstb-physician-phase-in.md`](./examples/sstb-physician-phase-in.md) — Single physician sole proprietor in SSTB phase-in zone
- [`examples/scorp-software-consultant.md`](./examples/scorp-software-consultant.md) — MFJ S-corp software consultant above threshold (non-SSTB)
- [`examples/multi-business-aggregation.md`](./examples/multi-business-aggregation.md) — Common-ownership rental + property management businesses with aggregation election

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 8995-A + AI Agent Skill: Full QBI Deduction Guide 2026](https://jupid.com/blog/form-8995-a-qbi-deduction-full-2026) — Jupid's narrative companion to this skill
- [Form 8995-A (latest)](https://www.irs.gov/pub/irs-pdf/f8995a.pdf) — the form itself
- [Instructions for Form 8995-A (latest)](https://www.irs.gov/pub/irs-pdf/i8995a.pdf) — line-by-line IRS guidance
- [About Form 8995-A](https://www.irs.gov/forms-pubs/about-form-8995-a) — IRS landing page with archive of past revisions
- [Form 8995](https://www.irs.gov/pub/irs-pdf/f8995.pdf) — Simplified version (below threshold, no SSTB)
- [Qualified business income deduction](https://www.irs.gov/newsroom/qualified-business-income-deduction) — IRS overview page
- [2026 draft Form 8995-A](https://www.irs.gov/pub/irs-dft/f8995a--dft.pdf) — 2026 thresholds and new lines 39–43 (draft, do not file)
- IRC §199A — Qualified Business Income Deduction
- Treas. Reg. §1.199A-1 (operational rules), §1.199A-2 (W-2 wages and UBIA), §1.199A-3 (QBI definition), §1.199A-4 (aggregation), §1.199A-5 (SSTB), §1.199A-6 (cooperatives)
- Rev. Proc. 2024-40 §2.27 — 2025 thresholds ($197,300 / $394,600 MFJ) and phase-in ($247,300 / $494,600)
- Rev. Proc. 2025-32 §4.26 — 2026 thresholds ($201,750 / $201,775 MFS / $403,500 MFJ) and phase-in ($276,750 / $276,775 / $553,500); §2.12 — $400 minimum deduction
- Rev. Proc. 2019-38 — rental real estate safe harbor
- One Big Beautiful Bill Act, P.L. 119-21 — §70105 made §199A permanent, widened the phase-in range to $75,000 / $150,000 and added the §199A(i) $400 minimum deduction (tax years beginning after 2025); §70201(d) excluded §224 qualified tips from QBI (tax years beginning after 2024)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and regulations. It is not tax advice. SSTB classification in particular has been the subject of multiple PLRs and FAQs that interpret edge cases (e.g., the "reputation or skill" provision); when a borderline case arises, the agent should flag it for human review rather than proceed silently. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
