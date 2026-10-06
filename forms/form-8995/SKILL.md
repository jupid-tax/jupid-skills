---
name: form-8995
description: >
  Use this skill when a sole proprietor, single-member LLC owner, freelancer,
  K-1 recipient, or REIT/PTP investor needs to claim the 20% Qualified Business
  Income (QBI) deduction under IRC §199A AND their taxable income before the
  deduction is at or below the 2025 threshold ($197,300; $394,600 MFJ). Triggers on phrases like
  "QBI deduction below income threshold", "Form 8995 simplified", "Section 199A
  pass-through deduction", "qualified business income for freelancer/sole prop",
  or any request to compute the 20% pass-through deduction at low to moderate
  income. Do NOT use above the threshold (use form-8995-a), for W-2 employees
  (no QBI), C-corps (no §199A), or SSTB filers in the phase-in range.
form: Form 8995
audience: [solo, freelance, llc1, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8995.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8995.pdf
---

# Form 8995 — Qualified Business Income Deduction Simplified Computation

This skill produces an audit-grade draft of Form 8995 (the simplified §199A computation) from the user's pass-through income data. It applies the §199A regulations at each line, validates the result against the taxable income limit, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The form is mechanical: 17 lines, one page. The judgment is in (a) computing QBI correctly — subtracting the §199A adjustments from Schedule C profit — and (b) confirming the user belongs on Form 8995 rather than 8995-A.

Line map verified against the **2025 Form 8995** (Created 9/12/25) and the **2025 Instructions for Form 8995** (Jan 26, 2026), the revision filed in 2026 for tax year 2025. The 2026 draft Form 8995 (Created 5/1/26) renumbers the end of the form: new line 15 (deduction before the minimum), line 16 (OBBBA $400 minimum deduction for active QBI), line 17 (deduction), lines 18–19 (carryforwards), line 20 (ESBT box). Re-check the final revision before using this skill for a 2026 return: https://www.irs.gov/forms-pubs/about-form-8995

**Companion guide for end users:** [Form 8995 + AI Agent Skill: Simplified QBI Deduction Guide 2026](https://jupid.com/blog/form-8995-qbi-simplified-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **all** of the following are true:

- The user has qualified business income from a pass-through source (Schedule C profit, partnership K-1, S-corp K-1, qualifying rental, REIT dividends, PTP income)
- The user's taxable income before the QBI deduction is at or below the 2025 threshold: **$197,300 single, HOH, QSS and MFS / $394,600 MFJ** (2025 Form 8995 header; Rev. Proc. 2024-40 §2.27). For tax year 2026: $201,750 / $201,775 MFS / $403,500 MFJ (Rev. Proc. 2025-32 §4.26)
- The user is NOT a patron of an agricultural or horticultural cooperative

Trigger phrases:

- "QBI deduction", "Section 199A", "20% pass-through deduction"
- "Form 8995", "qualified business income", "QBI for my Schedule C"
- "How much QBI can I claim", "what's my QBI deduction"
- "Where does QBI go on 1040" (answer: 2025 Form 1040 line 13a, computed on Form 8995 / 8995-A)

Do **not** engage this skill when:

- Taxable income exceeds the threshold → use the [`form-8995-a`](../form-8995-a/SKILL.md) skill
- The user is in the phase-in range (2025: next $50,000 above the threshold, $100,000 MFJ; 2026: $75,000 / $150,000 MFJ under P.L. 119-21 §70105) → also `form-8995-a`
- The user is a Specified Service Trade or Business (SSTB) at any income near the threshold → `form-8995-a` to apply phase-out
- The user has only W-2 wages (no QBI exists)
- The user is a C-corp shareholder (C-corps don't get §199A — they have a flat 21% rate)
- The user is a patron of an agricultural or horticultural cooperative → must use Form 8995-A regardless of income

If the user's taxable income is close to the threshold (within $5K) ask explicitly before proceeding. The threshold can shift if the user has not yet finalized other Schedule 1 adjustments or itemized deductions.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. 2025 thresholds are $197,300 / $394,600 MFJ (Rev. Proc. 2024-40 §2.27). 2026 thresholds are $201,750 / $201,775 MFS / $403,500 MFJ (Rev. Proc. 2025-32 §4.26); 2026 also adds the $400 minimum deduction (IRC §199A(i)), so use the 2026 form revision for a 2026 return.
2. **Filing status** — single, MFJ, MFS, HoH. Determines which threshold applies.
3. **Filer's legal name and SSN** — for the form header.
4. **Schedule C net profit (Line 31)** for sole-prop filers, or the QBI amounts from K-1s. For K-1 sources, the agent must use the QBI specifically labeled in Box 20 code Z (partnership) or Box 17 code V (S-corp), not the total K-1 income.
5. **§199A QBI adjustments** for sole-prop / SE filers:
   - One-half self-employment tax (Schedule SE Line 13)
   - Self-employed health insurance deduction (Schedule 1 Line 17)
   - Self-employed retirement contributions: SEP, SIMPLE, solo 401(k) (Schedule 1 Line 16)
6. **Prior-year QBI loss carryforward** — from line 16 of last year's Form 8995 (or Schedule C (Form 8995-A) line 6 if they used Form 8995-A last year). If first-year filer, 0.
7. **REIT/PTP income** — Section 199A dividends from Form 1099-DIV Box 5, plus any qualified PTP income from PTP K-1s. If none, 0.
8. **Prior-year REIT/PTP loss carryforward** — from line 17 of last year's Form 8995 (or Form 8995-A line 40). If none or first-year, 0.
9. **Form 1040 taxable income before QBI** — 2025 Form 1040 line 11a minus lines 12e and 13b (i8995 2025, Line 11), which equals line 15 plus line 13a once the return is drafted. Line 13b (Schedule 1-A: tips, overtime, car loan interest, seniors) does reduce it.
10. **Net capital gain** — qualified dividends (1040 line 3a) plus net capital gain: the smaller of Schedule D line 15 or 16 (zero if either is zero or less), or 1040 line 7a if Schedule D isn't required (i8995 2025, Line 12).
11. **Qualified tips deducted on Schedule 1-A** that were earned in the business (2025 and later): ask. Those amounts are not QBI (IRC §199A(c)(4)(D); i8995 2025 What's New).

If the user relies on the §199A rental real estate safe harbor (Rev. Proc. 2019-38: 250+ hours of rental services, separate books, contemporaneous records), additionally confirm:
- They have a qualifying enterprise (commercial or residential, kept separate)
- 250+ hours of rental services performed in the year
- Separate books and records for the rental enterprise
- Contemporaneous record of services performed

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm threshold eligibility

Confirm the user's taxable income before the QBI deduction is at or below $197,300 ($394,600 MFJ) for tax year 2025, or $201,750 ($201,775 MFS, $403,500 MFJ) for tax year 2026. If close to the threshold, compute taxable income explicitly before proceeding. If above, redirect to `form-8995-a`.

### Step 2 — Confirm not a co-op patron

Ask: "Are you a patron of an agricultural or horticultural cooperative?" If yes, redirect to `form-8995-a` regardless of income level.

### Step 3 — Identify all QBI sources

Build this internal table:

```
| Source name              | Type           | Raw amount  | §199A adjustments | QBI       |
|--------------------------|----------------|-------------|-------------------|-----------|
| Garcia Design (Sched C)  | sole prop      | $50,000     | $9,232            | $40,768   |
| Acme LLC (K-1)           | partnership    | $12,000 QBI | $0 (asked)        | $12,000   |
| XYZ Corp (K-1)           | S-corp         | $8,000 QBI  | $0 (asked)        | $8,000    |
```

The "raw amount" column is Schedule C Line 31 for sole props, or Box 20 code Z (partnership) / Box 17 code V (S-corp) for K-1 sources. The K-1 statement does not include owner-level deductions attributable to that business: ½ SE tax on partnership self-employment income, the SE health insurance deduction of a partner or more-than-2% S corporation shareholder, retirement contributions based on that income, unreimbursed partnership expenses. Ask whether any apply and subtract them (i8995 2025, "Determining Your Qualified Business Income").

### Step 4 — Apply §199A adjustments to sole-prop QBI

For each Schedule C source:

```
QBI = Schedule C Line 31
    − ½ SE tax allocated to this business
    − SE health insurance allocated to this business
    − SE retirement contributions allocated to this business
```

If the filer has only one Schedule C, allocate 100% of these adjustments to it. If multiple Schedule Cs, allocate proportionally to net profit. Also subtract any qualified tips from this business deducted under §224 on Schedule 1-A (2025 and later). See [`references/qbi-adjustments.md`](./references/qbi-adjustments.md).

### Step 5 — Aggregate REIT and PTP income

Sum:
- Form 1099-DIV Box 5 amounts (Section 199A dividends from REITs)
- Qualified PTP income from PTP K-1s

This goes on Line 6 separately from QBI (income positive, losses negative). REIT/PTP income is not reduced for §199A adjustments — use the gross amount.

### Step 6 — Apply prior-year loss carryforwards

If line 16 from last year's Form 8995 had a number (qualified business loss carryforward), enter it as a negative on Line 3.

If a REIT/PTP loss carryforward exists (last year's line 17), enter it as a negative on Line 7.

### Step 7 — Compute the form mechanically

```
Line 2   = sum of column (c) on rows 1i–1v (can be negative)
Line 4   = Line 2 + Line 3 (if zero or less, enter 0)
Line 5   = Line 4 × 0.20
Line 8   = Line 6 + Line 7 (if zero or less, enter 0)
Line 9   = Line 8 × 0.20
Line 10  = Line 5 + Line 9
Line 13  = Line 11 − Line 12 (if zero or less, enter 0)
Line 14  = Line 13 × 0.20
Line 15  = smaller of Line 10 or Line 14
Line 16  = Line 2 + Line 3 if less than zero, else 0 (QBI loss carryforward)
Line 17  = Line 6 + Line 7 if less than zero, else 0 (REIT/PTP loss carryforward)
```

Line 15 flows to **2025 Form 1040, line 13a** (1040-NR line 13a; Form 1041 line 20).

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next steps:

- **Line 15** flows to Form 1040 line 13a (QBI deduction)
- **If Line 10 > Line 14** (taxable income limit binding): note that future income growth may unlock more deduction
- **If Line 16 is negative**: the loss carries forward to next year's Line 3
- **If Line 17 is negative**: the REIT/PTP loss carries forward to next year's Line 7
- **Form 8995 is attached to Form 1040** — the user does not file it standalone

### Step 11 — File the return (optional)

If the user has authorized agent filing and the agent has browser-automation tooling, follow [`filing.md`](./filing.md). Form 8995 is e-filed as an attachment to Form 1040.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

Filer name(s) and SSN — use the same names/SSN(s) as on Form 1040.

### Line 1, rows i–v: Trade, business, or aggregation

For each QBI source:

- **Column (a)** — Trade, business, or aggregation name. Plain English: "Garcia Design", "Acme LLC partnership", "XYZ S-corp". Aggregation: "Aggregation 1" and leave (b) blank; rental safe harbor: "Enterprise 1"
- **Column (b)** — TIN. The EIN if the business has one (including a single-member LLC's EIN); otherwise SSN or ITIN. EIN of the entity for K-1 sources
- **Column (c)** — QBI or (loss) (after §199A adjustments; for K-1 sources, the statement amount less any owner-level deductions attributable to it). Exclude losses still suspended under other Code sections

Five rows fit on the form (1i–1v). More businesses: attach a statement with name, TIN and amount, and include them in the line 2 total.

### Line 2: Total QBI

Sum of column (c). Can be negative; do not floor it here.

### Line 3: QBI net (loss) carryforward from the prior year

From prior year's Form 8995 line 16 (or Schedule C (Form 8995-A) line 6). Negative number, in parentheses.

### Line 4: Total QBI

Line 2 + Line 3. If zero or less, enter 0.

### Line 5: QBI component

Line 4 × 20%.

### Line 6: Qualified REIT dividends and PTP income or (loss)

REIT Section 199A dividends (1099-DIV Box 5, after the holding-period check) + qualified PTP income or loss. Losses as a negative number.

### Line 7: REIT/PTP (loss) carryforward from the prior year

From prior year's Form 8995 line 17 (or Form 8995-A line 40). Negative number.

### Lines 8–9: REIT/PTP component

Line 8 = Line 6 + Line 7; if zero or less, enter 0. Line 9 = Line 8 × 20%.

### Line 10: QBI deduction before the income limitation

Line 5 + Line 9.

### Line 11: Taxable income before QBI deduction

2025 Form 1040 line 11a minus lines 12e and 13b (1040-NR: line 11a minus lines 12, 13b and 13c).

### Line 12: Net capital gain plus qualified dividends

Qualified dividends (1040 line 3a) + net capital gain: the smaller of Schedule D line 15 or 16 (nothing added if either is zero or less), or 1040 line 7a if Schedule D isn't required.

### Line 13: Line 11 − Line 12

If zero or less, enter 0.

### Line 14: Income limitation

Line 13 × 20%.

### Line 15: Final QBI deduction

Smaller of Line 10 or Line 14. Goes to Form 1040 line 13a.

### Lines 16–17: Carryforwards to next year

Line 16 = Line 2 + Line 3 if negative, else 0 (to next year's Line 3). Line 17 = Line 6 + Line 7 if negative, else 0 (to next year's Line 7).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 2 = sum of column (c) on rows 1i–1v (negative allowed)
- [ ] Line 4 = Line 2 + Line 3, floored at 0
- [ ] Line 5 = Line 4 × 0.20 (within $1 rounding)
- [ ] Line 8 = Line 6 + Line 7, floored at 0
- [ ] Line 9 = Line 8 × 0.20 (within $1 rounding)
- [ ] Line 10 = Line 5 + Line 9
- [ ] Line 13 = Line 11 − Line 12, floored at 0
- [ ] Line 14 = Line 13 × 0.20
- [ ] Line 15 = MIN(Line 10, Line 14)
- [ ] Line 16 = MIN(0, Line 2 + Line 3); Line 17 = MIN(0, Line 6 + Line 7)

### Threshold checks

- [ ] Form 1040 taxable income (before QBI) is at or below threshold for filing status
- [ ] If within $5K of threshold, recompute after pending Schedule 1 adjustments
- [ ] If above threshold, abort and route to form-8995-a

### Sanity checks (warn, don't block)

- [ ] QBI on Line 1 column (c) for a Schedule C source equals Schedule C Line 31 unmodified → likely missing §199A adjustments; surface "Did you subtract ½ SE tax, SE health insurance, and SE retirement?"
- [ ] Line 15 = Line 14 (taxable income limit binding) → note to user that future income growth may unlock more deduction
- [ ] Line 15 < $100 → not worth the form attachment effort; check if user prefers to skip (rare, but legitimate)
- [ ] Line 6 > $0 but no 1099-DIV documentation → confirm Box 5 amount, not Box 1a (ordinary dividends)
- [ ] Line 13 > $0 but Line 12 close to Line 11 → user may be primarily a passive investor; confirm QBI is genuinely from a trade or business

### Cross-form checks

- [ ] Schedule C Line 31 reconciles with the QBI source amount before adjustments
- [ ] ½ SE tax used in QBI adjustment matches Schedule SE Line 13
- [ ] SE health insurance used in QBI adjustment matches Schedule 1 Line 17
- [ ] SE retirement used in QBI adjustment matches Schedule 1 Line 16
- [ ] Line 15 deduction is reflected on Form 1040 line 13a

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 8995 or paste into tax software:

```markdown
# Form 8995 — DRAFT for tax year YYYY (Simplified QBI Computation)

## Header
Name(s): <as on 1040>
SSN: <primary filer SSN>

## Line 1, rows i–v — Trade or Business Information

| (a) Trade/business     | (b) TIN           | (c) QBI/(Loss)   |
|------------------------|-------------------|------------------|
| <name>                 | <SSN/EIN>         | $X,XXX           |
| ...                    | ...               | ...              |

## Lines 2-5 — QBI Component

 2. Total QBI or (loss):                  $X,XXX
 3. QBI net (loss) carryforward:          ($X,XXX)
 4. Total QBI (2 + 3, min 0):             $X,XXX
 5. QBI component (20% of Line 4):        $X,XXX

## Lines 6-9 — REIT/PTP Component

 6. REIT dividends + PTP income/(loss):   $X,XXX
 7. REIT/PTP (loss) carryforward:         ($X,XXX)
 8. Total REIT/PTP (6 + 7, min 0):        $X,XXX
 9. REIT/PTP component (20% of Line 8):   $X,XXX

## Lines 10-15 — Income Limit and Final Deduction

10. QBI deduction before income limit (5 + 9): $X,XXX
11. Taxable income before QBI:            $X,XXX
12. Net capital gain + qualified dividends: $X,XXX
13. Line 11 − Line 12 (min 0):            $X,XXX
14. Income limitation (20% of Line 13):   $X,XXX
15. **Smaller of Line 10 or Line 14:**    **$X,XXX**

## Lines 16-17 — Carryforwards to next year
16. QBI (loss) carryforward:              ($X,XXX) or 0
17. REIT/PTP (loss) carryforward:         ($X,XXX) or 0

## Result
- Final QBI deduction: $X,XXX
- Flows to: Form 1040, line 13a
- Limiting factor: <QBI itself / taxable income limit>

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Threshold: confirmed at or below $197,300 ($394,600 MFJ) for 2025
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 8995 (revision date YYYY)
- IRS Instructions for Form 8995 (revision date YYYY)
- IRC §199A
- Rev. Proc. 2024-40 §2.27 (2025 thresholds)
- Treas. Reg. §1.199A-3 (QBI computation)
- (any other authority used)
```

The draft is **not** the final filed form. It is a worksheet the user transcribes to e-file software or paper Form 8995 attached to Form 1040.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8995 line with examples
- [`references/qbi-adjustments.md`](./references/qbi-adjustments.md) — How to compute QBI from Schedule C with §199A adjustments
- [`references/k1-qbi.md`](./references/k1-qbi.md) — Reading partnership and S-corp K-1 Section 199A statements
- [`references/reit-ptp.md`](./references/reit-ptp.md) — Section 199A dividends from REITs and PTP income
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: filing Form 8995 as an attachment to Form 1040 via e-file software, Free File Fillable Forms, or paper (loaded only when filing is authorized)

## Examples

End-to-end worked Form 8995 deliverables.

- [`examples/freelance-designer.md`](./examples/freelance-designer.md) — Single sole prop, Schedule C source, taxable income limit binding
- [`examples/k1-recipient.md`](./examples/k1-recipient.md) — S-corp shareholder with K-1 QBI, no Schedule C
- [`examples/multi-source.md`](./examples/multi-source.md) — Schedule C plus REIT dividends plus prior-year loss carryforward

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 8995 + AI Agent Skill: Simplified QBI Deduction Guide 2026](https://jupid.com/blog/form-8995-qbi-simplified-2026) — Jupid's narrative companion
- [Form 8995 (latest)](https://www.irs.gov/pub/irs-pdf/f8995.pdf) — the form itself
- [Instructions for Form 8995 (latest)](https://www.irs.gov/pub/irs-pdf/i8995.pdf) — line-by-line IRS guidance
- [About Form 8995](https://www.irs.gov/forms-pubs/about-form-8995) — IRS landing page
- [Form 8995-A (above-threshold version)](https://www.irs.gov/pub/irs-pdf/f8995a.pdf) — for filers above the income threshold
- [2026 draft Form 8995](https://www.irs.gov/pub/irs-dft/f8995--dft.pdf) — new lines 15–20 for tax year 2026 (draft, do not file)
- IRC §199A — Qualified Business Income Deduction (made permanent by OBBBA, P.L. 119-21 §70105; §199A(i) $400 minimum deduction and $75,000 / $150,000 phase-in range for tax years beginning after 2025; §199A(c)(4)(D) qualified tips excluded from QBI, P.L. 119-21 §70201(d), tax years beginning after 2024)
- Treas. Reg. §1.199A-3 — QBI computation rules
- Treas. Reg. §1.199A-5 — SSTB definitions
- Rev. Proc. 2024-40 §2.27 — 2025 thresholds ($197,300 / $394,600 MFJ)
- Rev. Proc. 2025-32 §4.26 — 2026 thresholds ($201,750 / $201,775 MFS / $403,500 MFJ) and §2.12 (the $400 / $1,000 minimum deduction amounts)
- Rev. Proc. 2019-38 — §199A safe harbor for rental real estate (Publication 535 is discontinued; its last revision was for 2022)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations warrant a licensed tax professional's review.
