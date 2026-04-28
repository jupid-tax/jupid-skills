---
name: form-8995
description: >
  Use this skill when a sole proprietor, single-member LLC owner, freelancer,
  K-1 recipient, or REIT/PTP investor needs to claim the 20% Qualified Business
  Income (QBI) deduction under IRC §199A AND their taxable income is at or below
  the 2025 threshold ($241,950 single / $483,900 MFJ). Triggers on phrases like
  "QBI deduction below income threshold", "Form 8995 simplified", "Section 199A
  pass-through deduction", "qualified business income for freelancer/sole prop",
  or any request to compute the 20% pass-through deduction at low to moderate
  income. Do NOT use above the threshold (use form-8995-a), for W-2 employees
  (no QBI), C-corps (no §199A), or SSTB filers in the phase-in range.
form: Form 8995
audience: [solo, freelance, llc1, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f8995.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8995.pdf
---

# Form 8995 — Qualified Business Income Deduction Simplified Computation

This skill produces an audit-grade draft of Form 8995 (the simplified §199A computation) from the user's pass-through income data. It applies the §199A regulations at each line, validates the result against the taxable income limit, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The form is mechanical: 17 lines, one page. The judgment is in (a) computing QBI correctly — subtracting the §199A adjustments from Schedule C profit — and (b) confirming the user belongs on Form 8995 rather than 8995-A.

**Companion guide for end users:** [Form 8995 + AI Agent Skill: Simplified QBI Deduction Guide 2026](https://jupid.com/blog/form-8995-qbi-simplified-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **all** of the following are true:

- The user has qualified business income from a pass-through source (Schedule C profit, partnership K-1, S-corp K-1, qualifying rental, REIT dividends, PTP income)
- The user's taxable income before the QBI deduction is at or below the 2025 threshold: **$241,950 single / $483,900 MFJ / $241,950 MFS**
- The user is NOT a patron of an agricultural or horticultural cooperative

Trigger phrases:

- "QBI deduction", "Section 199A", "20% pass-through deduction"
- "Form 8995", "qualified business income", "QBI for my Schedule C"
- "How much QBI can I claim", "what's my QBI deduction"
- "Where does QBI go on 1040" (answer: Line 13, computed on Form 8995 / 8995-A)

Do **not** engage this skill when:

- Taxable income exceeds the threshold → use the (forthcoming) `form-8995-a` skill
- The user is in the phase-in range (next $75K above threshold for single, next $100K for MFJ) → also `form-8995-a`
- The user is a Specified Service Trade or Business (SSTB) at any income near the threshold → `form-8995-a` to apply phase-out
- The user has only W-2 wages (no QBI exists)
- The user is a C-corp shareholder (C-corps don't get §199A — they have a flat 21% rate)
- The user is a patron of an agricultural or horticultural cooperative → must use Form 8995-A regardless of income

If the user's taxable income is close to the threshold (within $5K) ask explicitly before proceeding. The threshold can shift if the user has not yet finalized other Schedule 1 adjustments or itemized deductions.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. 2025 thresholds are $241,950 / $483,900 (Rev. Proc. 2024-40). 2026 thresholds typically announced in late 2025 — verify before filing 2026.
2. **Filing status** — single, MFJ, MFS, HoH. Determines which threshold applies.
3. **Filer's legal name and SSN** — for the form header.
4. **Schedule C net profit (Line 31)** for sole-prop filers, or the QBI amounts from K-1s. For K-1 sources, the agent must use the QBI specifically labeled in Box 20 code Z (partnership) or Box 17 code V (S-corp), not the total K-1 income.
5. **§199A QBI adjustments** for sole-prop / SE filers:
   - One-half self-employment tax (Schedule SE Line 13)
   - Self-employed health insurance deduction (Schedule 1 Line 17)
   - Self-employed retirement contributions: SEP, SIMPLE, solo 401(k) (Schedule 1 Line 16)
6. **Prior-year QBI loss carryforward** — from Line 16 of last year's Form 8995 (or Line 4 / Line 9 of 8995-A if they used that form last year). If first-year filer, 0.
7. **REIT/PTP income** — Section 199A dividends from Form 1099-DIV Box 5, plus any qualified PTP income from PTP K-1s. If none, 0.
8. **Prior-year REIT/PTP loss carryforward** — from prior year's Line 9. If none or first-year, 0.
9. **Form 1040 taxable income before QBI** — equal to Form 1040 Line 15 plus the QBI deduction itself. If the 1040 isn't yet drafted, derive from AGI minus standard or itemized deductions.
10. **Net capital gain** — qualified dividends (1040 Line 3a) plus net long-term capital gain (Schedule D Line 16 / 1040 Line 7).

If the user qualifies for the §199A rental real estate safe harbor (Notice 2019-7, 250+ hours of rental services, separate books, contemporaneous records), additionally confirm:
- They have a qualifying enterprise (commercial or residential, kept separate)
- 250+ hours of rental services performed in the year
- Separate books and records for the rental enterprise
- Contemporaneous record of services performed

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm threshold eligibility

Confirm the user's taxable income is at or below $241,950 (single) or $483,900 (MFJ) for tax year 2025. If close to the threshold, compute taxable income explicitly before proceeding. If above, redirect to `form-8995-a`.

### Step 2 — Confirm not a co-op patron

Ask: "Are you a patron of an agricultural or horticultural cooperative?" If yes, redirect to `form-8995-a` regardless of income level.

### Step 3 — Identify all QBI sources

Build this internal table:

```
| Source name              | Type           | Raw amount  | §199A adjustments | QBI       |
|--------------------------|----------------|-------------|-------------------|-----------|
| Garcia Design (Sched C)  | sole prop      | $50,000     | $9,232            | $40,768   |
| Acme LLC (K-1)           | partnership    | $12,000 QBI | reported on K-1   | $12,000   |
| XYZ Corp (K-1)           | S-corp         | $8,000 QBI  | reported on K-1   | $8,000    |
```

The "raw amount" column is Schedule C Line 31 for sole props, or Box 20 code Z (partnership) / Box 17 code V (S-corp) for K-1 sources.

### Step 4 — Apply §199A adjustments to sole-prop QBI

For each Schedule C source:

```
QBI = Schedule C Line 31
    − ½ SE tax allocated to this business
    − SE health insurance allocated to this business
    − SE retirement contributions allocated to this business
```

If the filer has only one Schedule C, allocate 100% of these adjustments to it. If multiple Schedule Cs, allocate proportionally to net profit. See [`references/qbi-adjustments.md`](./references/qbi-adjustments.md).

### Step 5 — Aggregate REIT and PTP income

Sum:
- Form 1099-DIV Box 5 amounts (Section 199A dividends from REITs)
- Qualified PTP income from PTP K-1s

This goes on Line 5 separately from QBI. REIT/PTP income is not reduced for §199A adjustments — use the gross amount.

### Step 6 — Apply prior-year loss carryforwards

If Line 16 from last year's Form 8995 had a number (qualified business loss carryforward), enter as a negative on Line 3.

If REIT/PTP carryforward exists, enter as a negative on Line 6.

### Step 7 — Compute the form mechanically

```
Line 2   = sum of Column (iii) on Lines 1a-1e (positive only; if negative, enter 0 and carry forward)
Line 4   = Line 2 + Line 3 (zero floor)
Line 7   = Line 5 + Line 6 (zero floor)
Line 10  = Line 4 × 0.20
Line 11  = Line 7 × 0.20
Line 12  = Line 10 + Line 11
Line 15  = Line 13 − Line 14
Line 16  = Line 15 × 0.20
Line 17  = lesser of Line 12 or Line 16
```

Line 17 flows to **Form 1040, Line 13**.

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next steps:

- **Line 17** flows to Form 1040 Line 13 (QBI deduction)
- **If Line 12 > Line 16** (taxable income limit binding): note that future income growth may unlock more deduction
- **If Line 4 was zero** because of a current-year loss: note that the loss carries forward to next year's Line 3
- **If REIT/PTP loss exists**: note the carryforward to next year's Line 6
- **Form 8995 is attached to Form 1040** — the user does not file it standalone

### Step 11 — File the return (optional)

If the user has authorized agent filing and the agent has browser-automation tooling, follow [`filing.md`](./filing.md). Form 8995 is e-filed as an attachment to Form 1040.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

Filer name(s) and SSN — use the same names/SSN(s) as on Form 1040.

### Lines 1a-1e: Trade or business information

For each QBI source:

- **Column (i)** — Trade, business, or aggregation name. Plain English: "Garcia Design", "Acme LLC partnership", "XYZ S-corp"
- **Column (ii)** — TIN. SSN for sole prop, EIN for K-1 sources
- **Column (iii)** — QBI amount (after §199A adjustments for sole props; as reported on K-1 for partnership/S-corp shares)

Up to 5 sources fit on the form. More require a continuation statement.

### Line 2: Total QBI

Sum of Column (iii). Floor at 0 if negative — carry the loss to next year's Line 3.

### Line 3: QBI loss carryforward

From prior year's Line 16 (or 8995-A equivalent). Negative number.

### Line 4: Total QBI component

Line 2 + Line 3. Floor at 0.

### Line 5: REIT/PTP income

REIT Section 199A dividends (1099-DIV Box 5) + qualified PTP income.

### Line 6: REIT/PTP loss carryforward

From prior year's Line 9. Negative number.

### Lines 7-9: REIT/PTP component

Line 7 = Line 5 + Line 6. Floor at 0. Lines 8-9 handle further carryforward mechanics — refer to current-year IRS instructions for exact treatment, as line numbering occasionally shifts between revisions.

### Line 10: 20% × QBI component

Line 4 × 0.20.

### Line 11: 20% × REIT/PTP component

Line 7 (or final REIT/PTP figure from Lines 8-9) × 0.20.

### Line 12: Tentative deduction

Line 10 + Line 11.

### Line 13: Taxable income before QBI

Form 1040 Line 15 *plus* the QBI deduction itself (i.e., what taxable income would be without §199A).

### Line 14: Net capital gain

Qualified dividends (1040 Line 3a) + net long-term capital gain (Schedule D Line 16).

### Line 15: Income subject to limit

Line 13 − Line 14.

### Line 16: Taxable income limit

Line 15 × 0.20.

### Line 17: Final QBI deduction

Lesser of Line 12 or Line 16. Goes to Form 1040 Line 13.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 2 = sum of Column (iii) on Lines 1a-1e (or 0 if negative)
- [ ] Line 4 = Line 2 + Line 3, floored at 0
- [ ] Line 7 = Line 5 + Line 6, floored at 0
- [ ] Line 10 = Line 4 × 0.20 (within $1 rounding)
- [ ] Line 11 = Line 7 × 0.20 (within $1 rounding)
- [ ] Line 12 = Line 10 + Line 11
- [ ] Line 15 = Line 13 − Line 14
- [ ] Line 16 = Line 15 × 0.20
- [ ] Line 17 = MIN(Line 12, Line 16)

### Threshold checks

- [ ] Form 1040 taxable income (before QBI) is at or below threshold for filing status
- [ ] If within $5K of threshold, recompute after pending Schedule 1 adjustments
- [ ] If above threshold, abort and route to form-8995-a

### Sanity checks (warn, don't block)

- [ ] QBI on Line 1 column (iii) for a Schedule C source equals Schedule C Line 31 unmodified → likely missing §199A adjustments; surface "Did you subtract ½ SE tax, SE health insurance, and SE retirement?"
- [ ] Line 17 = Line 16 (taxable income limit binding) → note to user that future income growth may unlock more deduction
- [ ] Line 17 < $100 → not worth the form attachment effort; check if user prefers to skip (rare, but legitimate)
- [ ] Line 5 > $0 but no 1099-DIV documentation → confirm Box 5 amount, not Box 1a (ordinary dividends)
- [ ] Line 13 minus Line 14 > $0 but Line 14 close to Line 13 → user may be primarily a passive investor; confirm QBI is genuinely from a trade or business

### Cross-form checks

- [ ] Schedule C Line 31 reconciles with the QBI source amount before adjustments
- [ ] ½ SE tax used in QBI adjustment matches Schedule SE Line 13
- [ ] SE health insurance used in QBI adjustment matches Schedule 1 Line 17
- [ ] SE retirement used in QBI adjustment matches Schedule 1 Line 16
- [ ] Line 17 deduction is reflected on Form 1040 Line 13

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 8995 or paste into tax software:

```markdown
# Form 8995 — DRAFT for tax year YYYY (Simplified QBI Computation)

## Header
Name(s): <as on 1040>
SSN: <primary filer SSN>

## Lines 1a-1e — Trade or Business Information

| (i) Trade/business     | (ii) TIN          | (iii) QBI/(Loss) |
|------------------------|-------------------|------------------|
| <name>                 | <SSN/EIN>         | $X,XXX           |
| ...                    | ...               | ...              |

## Lines 2-4 — Total QBI

 2. Total QBI:                          $X,XXX
 3. Qualified business loss carryforward: ($X,XXX)
 4. Total QBI component (Line 2 + 3):    $X,XXX

## Lines 5-9 — REIT/PTP

 5. REIT dividends + PTP income:          $X,XXX
 6. REIT/PTP loss carryforward:           ($X,XXX)
 7. Total REIT/PTP (5 + 6):               $X,XXX
 8. (continuation, see latest instructions)
 9. REIT/PTP loss carryforward (used):    $X,XXX

## Lines 10-12 — Deduction Before Income Limit

10. 20% of Line 4:                        $X,XXX
11. 20% of Line 7:                        $X,XXX
12. QBI deduction before income limit:    $X,XXX

## Lines 13-17 — Taxable Income Limit and Final Deduction

13. Taxable income before QBI:            $X,XXX
14. Net capital gain (qual div + LTCG):   $X,XXX
15. Line 13 − Line 14:                    $X,XXX
16. 20% of Line 15 (income limit):        $X,XXX
17. **Lesser of Line 12 or Line 16:**     **$X,XXX**

## Result
- Final QBI deduction: $X,XXX
- Flows to: Form 1040, Line 13
- Limiting factor: <QBI itself / taxable income limit>

## Carryforwards to next year
- QBI loss carryforward: $X,XXX (if Line 2 was negative)
- REIT/PTP loss carryforward: $X,XXX (if Line 7 was negative)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Threshold: confirmed below $241,950 single / $483,900 MFJ for 2025
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 8995 (revision date YYYY)
- IRS Instructions for Form 8995 (revision date YYYY)
- IRC §199A
- Rev. Proc. 2024-40 (2025 thresholds)
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
- [`filing.md`](./filing.md) — Browser-automation playbook: filing Form 8995 as an attachment to Form 1040 via FFFF, Direct File, or paid software (loaded only when filing is authorized)

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
- [Publication 535](https://www.irs.gov/publications/p535) — Business Expenses (includes §199A overview)
- IRC §199A — Qualified Business Income Deduction (made permanent by OBBBA 2025, P.L. 119-21)
- Treas. Reg. §1.199A-3 — QBI computation rules
- Treas. Reg. §1.199A-5 — SSTB definitions
- Rev. Proc. 2024-40 — 2025 inflation-adjusted thresholds
- Notice 2019-7 — §199A safe harbor for rental real estate

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations warrant a licensed tax professional's review.
