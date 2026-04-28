---
name: form-8995-a
description: >
  Use this skill when a sole proprietor, S-corp shareholder, partnership member,
  or REIT/PTP investor needs to compute the Qualified Business Income (QBI)
  deduction under IRC §199A AND their taxable income before QBI exceeds the
  threshold ($241,950 single / $483,900 MFJ for 2025) OR they have any income
  from a Specified Service Trade or Business (SSTB — health, law, accounting,
  consulting, athletes, performing arts, financial services, brokerage,
  investing). Triggers on phrases like "Form 8995-A", "QBI deduction over
  income threshold", "Section 199A SSTB", "qualified business income deduction
  high income", "QBI for consultant/lawyer/doctor", "phase-in QBI", "W-2 wage
  limit QBI". Do NOT use for filers below the threshold with no SSTB issues
  (use the simplified form-8995 skill), W-2 employees (no QBI), or C-corp
  shareholders (no QBI).
form: Form 8995-A
audience: [solo, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f8995a.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8995a.pdf
---

# Form 8995-A — Qualified Business Income Deduction (Full Version)

This skill produces an audit-grade draft of Form 8995-A, including any required Schedules A, B, C, and D, from the user's QBI sources, W-2 wage data, UBIA records, taxable income, and SSTB classification. It walks through the form line by line, applies the §199A rules at each step, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The math is mechanical once the inputs are clean. The judgment is in (1) whether to use Form 8995-A vs. the simplified Form 8995, (2) which businesses are SSTBs, (3) whether to aggregate, (4) the SE-tax / SE-HI / SE-retirement adjustments to QBI, and (5) the W-2 / UBIA limit interaction with the SSTB phase-in. This skill optimizes for those — the agent should ask, not guess, when any input is ambiguous.

**Companion guide for end users:** [Form 8995-A + AI Agent Skill: Full QBI Deduction Guide 2026](https://jupid.com/blog/form-8995-a-qbi-deduction-full-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **all** of the following are true:

- The user has at least one source of qualified business income: Schedule C, S-corp K-1, partnership K-1, qualifying Schedule E rental, qualified REIT dividends, or qualified PTP income, AND
- Either (a) their taxable income BEFORE the QBI deduction exceeds the §199A threshold for their filing status, OR (b) they have any income from a Specified Service Trade or Business (SSTB) and are in or above the phase-in zone

Quick threshold check (2025 figures from Rev. Proc. 2024-40; verify 2026 figures against the latest Rev. Proc.):

- **Single / HoH / MFS**: threshold $241,950, phase-in top $291,950
- **MFJ / QSS**: threshold $483,900, phase-in top $583,900

Do **not** engage this skill when:

- Taxable income before QBI is at or below the threshold AND no SSTB issues → use the simpler `form-8995` skill (forthcoming)
- The user is a W-2 employee with no business income → wages are not QBI; nothing to compute
- The user is a C-corp shareholder → C-corp income is taxed at the corporate rate, not §199A
- The user's only income is capital gains, ordinary dividends, or interest → not QBI
- The user has only foreign-source income that doesn't rise to a US trade or business

If the user's threshold position or SSTB status is ambiguous, **ask before proceeding**. The most common confusion: a consultant who thinks software development counts as "consulting" (it doesn't — software is explicitly carved out by Treas. Reg. §1.199A-5(b)(2)).

---

## Prerequisites

Before producing anything, the agent must have these eight inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 8995-A for tax year 2025 is filed in 2026; thresholds depend on the year.

2. **Filing status** — Single, HoH, MFS, MFJ, or QSS. Determines threshold and phase-in width.

3. **Taxable income BEFORE the QBI deduction.** This is Form 1040 Line 11 (AGI) minus Line 12 (standard or itemized deduction). Do NOT subtract Line 13 (the deduction we're computing). Required to determine threshold position and SSTB phase-in percentage.

4. **For each trade or business**:
   - Business name
   - Whether it's an SSTB (see [`references/sstb-classification.md`](./references/sstb-classification.md))
   - QBI: net of all §199A-eligible income, gain, deduction, loss, allocable to that business
   - W-2 wages paid by the business (calendar year ending in the tax year)
   - UBIA of qualified property (depreciable tangible property within its depreciable period)
   - For S-corps: how much of K-1 box 1 is reasonable comp paid to the owner (this is NOT QBI but IS W-2 wages)

5. **Net capital gains** from Form 1040 Line 3a (qualified dividends) + Schedule D Line 16 (net LTCG). Required for Part IV Line 34 (overall cap).

6. **REIT dividends and PTP income** (from 1099-DIV Box 5 and K-1 box 17/20). These are NOT subject to the W-2/UBIA limit but DO appear on Part IV.

7. **Carryforward from prior years**: any §199A loss carryforward (negative QBI from prior year) or REIT/PTP loss carryforward (negative qualified REIT/PTP from prior year).

8. **For Schedule C filers**: the deductible portion of SE tax (½ SE tax), self-employed health insurance, and SE retirement contributions allocable to each business. These reduce QBI per Treas. Reg. §1.199A-3(b)(1)(vi).

For aggregation (Schedule B), additionally ask:
- Common ownership ≥50% across all businesses?
- Same tax year for all?
- None of them is an SSTB?
- Two of three sharing factors (same products/services, shared facilities, operating coordination)?

For cooperative patrons (Schedule D), additionally ask:
- Did the user receive Section 199A(g) information from a co-op (Form 1099-PATR Box 6)?

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm Form 8995-A is the right form

Compute taxable income before QBI. Compare to threshold. If under threshold AND no SSTB → redirect to the simplified `form-8995` skill. If over threshold OR any SSTB → continue.

### Step 2 — Classify each business

For each trade or business, decide SSTB or not using [`references/sstb-classification.md`](./references/sstb-classification.md). Ask the user to confirm any borderline classification. The 11 SSTB categories per IRC §199A(d)(2)(A) are: health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage, investing/investment management, and trading/dealing in securities/partnerships/commodities — plus the "reputation or skill" catch-all.

### Step 3 — Compute QBI per business

For Schedule C filers: QBI = Schedule C Line 31 net profit MINUS (½ SE tax allocable + SE health insurance allocable + SE retirement contribution allocable). All allocable to that specific business.

For S-corp K-1: QBI = K-1 Box 1 ordinary business income MINUS reasonable compensation paid to the owner (the owner's W-2 from the S-corp).

For partnership K-1: QBI = K-1 Box 1 ordinary income (do NOT subtract guaranteed payments — they're already excluded from Box 1).

For qualifying Schedule E rental: QBI = net rental income, only if the rental rises to a §162 trade or business OR meets the §1.199A-1(b)(14) safe harbor (250+ hours of rental services, separate books, contemporaneous records).

See [`references/qbi-computation.md`](./references/qbi-computation.md) for full mechanics including state tax adjustments and trader vs. investor distinctions.

### Step 4 — Check threshold position for SSTB businesses

For each SSTB:
- Below threshold → would use Form 8995 (out of scope here)
- In phase-in zone → complete Schedule A (apply applicable percentage to QBI, W-2, UBIA before the W-2/UBIA limit)
- Above phase-in top → SSTB QBI deduction = $0; report the SSTB in Part I but its contribution to Line 27 is zero

For non-SSTB businesses above threshold → no Schedule A, but the W-2/UBIA limit applies in full.

### Step 5 — Decide whether to aggregate

If multiple non-SSTB businesses with shared ownership and operations, consider Schedule B aggregation when one business has high QBI but low W-2 wages (would otherwise be limited) and another has high W-2 wages. See [`references/aggregation.md`](./references/aggregation.md).

**Aggregation is a binding multi-year election** (Treas. Reg. §1.199A-4(c)(1)). Confirm with the user.

### Step 6 — Compute Part II for each business

For each business, complete Lines 2-13 of Part II:
- L2: QBI
- L3: 20% of QBI
- L4: W-2 wages
- L5: 50% × W-2
- L6: 25% × W-2
- L7: UBIA
- L8: 2.5% × UBIA
- L9: L6 + L8
- L10: greater of L5 or L9 (the W-2/UBIA limit)
- L11: smaller of L3 or L10
- L12: phase-in reduction from Schedule A (if applicable)
- L13: L11 − L12 (adjusted QBI for this business)

### Step 7 — Loss netting (Schedule C of Form 8995-A)

If any business has negative QBI, complete Schedule C to net losses against positive-QBI businesses proportionally. If aggregate is still negative, the full loss carries forward; this year's QBI component is $0.

### Step 8 — Complete Part IV

- L27: sum of all businesses' L13 (or net result from Schedule C of Form 8995-A)
- L28-31: REIT/PTP component (qualified REIT divs + qualified PTP income) × 20%, with prior-year loss carryforward netting
- L32: L27 + L31
- L33: taxable income before QBI deduction
- L34: net capital gains (LTCG + qualified dividends)
- L35: L33 − L34
- L36: 20% × L35 (overall cap)
- L37: smaller of L32 or L36
- L38-39: cooperative patron reduction (Schedule D), if applicable
- L39: final QBI deduction → Form 1040 Line 13

### Step 9 — Run validation checks

See **Validation** below. Run every check.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next steps:

- The Line 39 result flows to **Form 1040 Line 13**
- If any QBI loss carries forward, note the amount and the 2026 / 2027 line where it'll be reported
- If aggregation was elected, note that this is binding for future years and the same aggregation must be used
- For S-corp owners: confirm reasonable comp documentation (the wage-vs-distribution decision interacts with both QBI and SS/Medicare)

### Step 12 — File the return (optional)

If the user wants the agent to e-file, follow [`filing.md`](./filing.md). Form 8995-A is attached to Form 1040; it's not filed separately.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Trade, business, or aggregation information

- **L1(a)** — Name of each business or aggregation
- **L1(b)** — Check box if SSTB
- **L1(c)** — EIN or SSN

### Part II — Adjusted QBI per business

(See Step 6 above for line-by-line.)

Critical:
- L2 (QBI) must reflect SE-tax / SE-HI / SE-retirement adjustments for Schedule C filers and reasonable-comp removal for S-corp owners
- L4 (W-2 wages) must use the calendar year ending in the tax year, not a fiscal year
- L7 (UBIA) excludes land and intangibles; only depreciable tangible property within its depreciable period
- L10 (W-2/UBIA limit) is the GREATER of the two formulas — choose the more favorable

### Part III — Phased-in reduction

Used for SSTBs in the phase-in zone. The Schedule A computation produces the L12 reduction. See [`references/sstb-phase-in.md`](./references/sstb-phase-in.md) for the full math.

### Part IV — QBI deduction

- L27: sum of all L13 from Part II
- L28-30: REIT/PTP component (no W-2/UBIA limit applies)
- L32: total before overall cap
- L33-36: overall cap = 20% × (taxable income − net capital gains)
- L37: smaller of L32 or L36
- L39: final → Form 1040 Line 13

### Schedule A — SSTB phase-in

Lines 1-13 compute the applicable percentage and the resulting reduction. See [`references/sstb-phase-in.md`](./references/sstb-phase-in.md).

### Schedule B — Aggregation

Lists the businesses being aggregated and confirms eligibility. See [`references/aggregation.md`](./references/aggregation.md).

### Schedule C — Loss netting

If any business has negative QBI, allocates the loss across positive-QBI businesses proportionally. See [`references/loss-netting.md`](./references/loss-netting.md).

### Schedule D — Cooperative patrons

Only for farmers and other §199A(g) DPAD patrons. Skip if not applicable.

---

## Validation

Before declaring the form ready, run these checks. Surface any failure — don't silently fix.

### Math checks

- [ ] Each Part II row: L3 = 0.20 × L2; L5 = 0.50 × L4; L6 = 0.25 × L4; L8 = 0.025 × L7; L9 = L6 + L8
- [ ] L10 = max(L5, L9)
- [ ] L11 = min(L3, L10)
- [ ] L13 = L11 − L12
- [ ] If Schedule A used: L7 (Schedule A) = 1 − L6 (Schedule A)
- [ ] L27 = sum of all Part II Line 13s (or Schedule C result)
- [ ] L31 = 0.20 × L30
- [ ] L32 = L27 + L31
- [ ] L35 = L33 − L34
- [ ] L36 = 0.20 × L35
- [ ] L37 = min(L32, L36)
- [ ] L39 ≥ 0 (deduction can never be negative)

### Sanity checks

Surface a warning, do not block:

- [ ] Taxable income before QBI ≤ threshold AND no SSTB → user should file Form 8995, not 8995-A
- [ ] Filer is S-corp owner AND K-1 box 1 was used as QBI without subtracting reasonable comp → ask
- [ ] Filer is Schedule C AND QBI = Line 31 net profit (no SE-tax / SE-HI / SE-retirement reduction) → ask
- [ ] UBIA includes any line item described as "land" → must be excluded
- [ ] L4 W-2 wages > Schedule C Line 26 wages by more than 10% → reconciliation needed
- [ ] L7 UBIA exceeds total depreciable basis in service per Form 4562 → ask
- [ ] SSTB above phase-in top → confirm $0 contribution; the deduction is gone
- [ ] Net capital gains > taxable income before QBI → unusual; double-check the input

### Cross-form checks

- [ ] L39 matches what's entered on Form 1040 Line 13
- [ ] If aggregating, the same aggregation must appear on next year's Form 8995-A
- [ ] S-corp owner's W-2 from the corp matches Form 1040 Line 1z and the Box 1 figure on the W-2

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
Threshold for status: $<241,950 | 483,900 | etc.>
Phase-in top: $<amount>
Position: <below threshold | in phase-in | above phase-in top>

## Part I — Trades or Businesses
| (a) Name | (b) SSTB | (c) EIN/SSN |
|----------|----------|--------------|
| <name 1> | Yes/No   | <id>         |
| <name 2> | Yes/No   | <id>         |

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
12. Phase-in reduction (Sch A): $X,XXX
13. Adjusted QBI:             $X,XXX

(repeat for each business)

## Schedule A — SSTB Phase-In  (or "N/A — no SSTB in phase-in zone")
 1. Trade name:               <name>
 2. Taxable income before QBI: $X,XXX
 3. Threshold:                $X,XXX
 4. Excess (L2 − L3):         $X,XXX
 5. Phase-in range:           $50,000 | $100,000
 6. Phase-in % (L4 / L5):     0.XXXX
 7. Applicable % (1 − L6):    0.XXXX
 8-12. Reduced QBI / W-2 / UBIA computation
13. Phase-in reduction → Part II L12: $X,XXX

## Schedule B — Aggregation  (or "N/A")
List of businesses aggregated, with eligibility factors confirmed.

## Schedule C — Loss Netting  (or "N/A — no QBI losses")
Allocation of negative QBI across positive-QBI businesses.

## Schedule D — Cooperative Patron  (or "N/A")
§199A(g) DPAD computation if applicable.

## Part IV — QBI Deduction
27. Total QBI component:       $X,XXX
28. Qualified REIT/PTP income: $X,XXX
29. Prior-year REIT/PTP loss carryforward: $X,XXX
30. L28 + L29 (≥ 0):           $X,XXX
31. 20% × L30:                 $X,XXX
32. L27 + L31:                 $X,XXX
33. Taxable income before QBI: $X,XXX
34. Net capital gains:         $X,XXX
35. L33 − L34:                 $X,XXX
36. 20% × L35:                 $X,XXX
37. Smaller of L32 or L36:     $X,XXX
38. Patron reduction:          $X,XXX (or 0)
39. **Final QBI deduction:**   $X,XXX  → Form 1040 Line 13

## Loss carryforwards to 2026
- QBI loss carryforward:        $X,XXX (or 0)
- REIT/PTP loss carryforward:   $X,XXX (or 0)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 8995-A (revision date YYYY-MM-DD)
- IRS Instructions for Form 8995-A (revision date YYYY-MM-DD)
- IRC §199A
- Treas. Reg. §1.199A-1 through §1.199A-6
- Rev. Proc. 2024-40 (2025 thresholds)
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
- [Tax Topic 651 — Qualified Business Income Deduction](https://www.irs.gov/taxtopics/tc651) — IRS plain-language overview
- [QBI FAQ](https://www.irs.gov/newsroom/qualified-business-income-deduction) — IRS Q&A on common §199A issues
- IRC §199A — Qualified Business Income Deduction
- Treas. Reg. §1.199A-1 (operational rules), §1.199A-2 (W-2 wages and UBIA), §1.199A-3 (QBI definition), §1.199A-4 (aggregation), §1.199A-5 (SSTB), §1.199A-6 (cooperatives)
- Rev. Proc. 2024-40 — 2025 thresholds and phase-in widths
- One Big Beautiful Bill Act of 2025 — Made §199A permanent

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and regulations. It is not tax advice. SSTB classification in particular has been the subject of multiple PLRs and FAQs that interpret edge cases (e.g., the "reputation or skill" provision); when a borderline case arises, the agent should flag it for human review rather than proceed silently. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
