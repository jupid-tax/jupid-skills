---
name: schedule-se
description: >
  Use this skill when a sole proprietor, single-member LLC owner, freelancer,
  independent contractor, gig worker, or any filer with net self-employment
  earnings of $400 or more needs to compute self-employment tax on Schedule SE
  (Form 1040). Triggers on phrases like "self-employment tax", "Schedule SE",
  "SE tax calc", "1099 freelance tax", "freelance Social Security Medicare",
  "net earnings from self-employment", "how much SE tax do I owe", or any
  request to compute the 15.3% SE tax on Schedule C / Schedule F income.
  Do NOT use for: W-2 employees (FICA already withheld via Form W-2 box 4/6);
  S-corp shareholder distributions (no SE tax — but the shareholder must take
  reasonable W-2 wages reported on Form 941); church employees with Form 4361
  exemption; partners in a partnership (use the SE earnings line from Schedule
  K-1 box 14 instead of Schedule C); or filers with net SE earnings under $400
  (no SE tax owed and Schedule SE not required).
form: Schedule SE (Form 1040)
audience: [solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f1040sse.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040sse.pdf
---

# Schedule SE (Form 1040) — Self-Employment Tax

This skill produces an audit-grade draft of Schedule SE from the user's net self-employment earnings. It walks through the form line by line, applies the IRS rules at each line, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The math is mostly mechanical — multiply by 0.9235, then by 0.153 (or split into 12.4% Social Security + 2.9% Medicare with a wage-base cap on the SS portion). The judgment is in *whether the income is SE-eligible*, *whether the user has W-2 wages that consume part of the Social Security wage base*, and *whether the optional methods apply*. This skill optimizes for those decisions — the agent should ask, not guess.

**Companion guide for end users:** [Schedule SE Instructions: Complete Self-Employment Tax Guide 2026](https://jupid.com/blog/schedule-se-instructions-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule SE, "SE tax", "self-employment tax"
- The user has filed (or is filing) Schedule C with **Line 31 net profit ≥ $400**
- The user has filed Schedule F (farm) with **Line 34 net profit ≥ $400**
- The user is a partner in a partnership and has **Schedule K-1 (Form 1065) Box 14 Code A self-employment earnings ≥ $400**
- The user asks "how much do I owe in Social Security and Medicare on my freelance income"
- The user is computing quarterly estimated taxes and needs the SE-tax component (Form 1040-ES)

Do **not** engage this skill when:

- The user is a W-2 employee only — FICA is withheld at source; no Schedule SE
- The user is an S-corp shareholder receiving distributions — distributions are not SE earnings; the shareholder takes reasonable W-2 compensation reported on Form W-2 (the corp files Form 941 quarterly)
- The user is a member of a religious order or has filed Form 4361 (clergy housing exemption) or Form 4029 (Amish / Mennonite) — different rules, redirect to the IRS Pub 517 / Pub 51
- The user's net SE earnings are below $400 and the user is not using the optional methods to claim Social Security credits — no SE tax due and Schedule SE not required (IRC §1402(b))
- The user is a foreign national exempt from SE tax under a totalization agreement — see the relevant treaty

If the user's situation is ambiguous (e.g., LLC with multiple members, S-corp election filed mid-year), ask before proceeding. The most common confusion: a solo filer who incorporated as an S-corp and thinks they still owe SE tax — they don't on the K-1 distribution; they owe FICA via the W-2 the S-corp pays them.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Schedule SE for tax year 2025 is filed in 2026; for tax year 2024, in 2025. The Social Security wage base, optional method dollar thresholds, and form revision change yearly.
2. **Filer's legal name and SSN.** Used in the Schedule SE header. If a joint return has SE income from both spouses, each spouse files a separate Schedule SE.
3. **Net SE earnings source.** One or more of:
   - Schedule C Line 31 net profit (most common)
   - Schedule F Line 34 net profit
   - Schedule K-1 (Form 1065) Box 14 Code A (general partner / LLC member share of SE earnings)
   - Church employee income (Form W-2 Box 1 with Box 14 noted as church wages — see Part II Section B)
4. **W-2 wages received in the same year.** Needed because Form W-2 Box 3 (Social Security wages) consumes the SS wage base. If the user has both a W-2 job AND self-employment income, the SS portion of SE tax is reduced (or eliminated) by the wages already subject to FICA. Ask: "Did you also receive a W-2 in [tax year]? If yes, what's in Box 3 (Social Security wages)?"
5. **Optional method election.** Ask only if Schedule C / F income is unusually low and the user wants to qualify for or maintain Social Security credit accrual: "Do you want to use the farm or non-farm optional method to elect into a higher SE tax base for Social Security credit purposes? Most filers say no."
6. **Prior-year self-employment.** Only relevant for the non-farm optional method — the user must have had net SE earnings of at least $400 in 2 of the prior 3 years to qualify (IRC §1402(l)).
7. **Church employee income (Form W-2 with no FICA withheld).** Rare — applies to certain religious organizations that have elected out of FICA under IRC §3121(w). If the user has W-2 wages from such an employer, those go to Part II Section B and use a separate computation.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the user owes SE tax

Confirm net SE earnings are ≥ $400 (after the 0.9235 multiplier). Below that threshold, Schedule SE is not required and no SE tax is owed (IRC §1402(b)). Exception: the user is electing the non-farm or farm optional method to keep accruing Social Security credits — then Schedule SE is filed even with zero or low earnings.

If the user is below $400 and not electing an optional method, stop and tell them Schedule SE is not required; remind them that Schedule C / F still gets filed and the income still flows to Form 1040.

### Step 2 — Gather all SE income sources

Sum every SE income source for this filer (one Schedule SE per spouse):

```
Schedule C Line 31 net profit:           $X,XXX
Schedule F Line 34 net profit:           $X,XXX
K-1 Box 14 Code A (general partner):     $X,XXX
Church employee W-2 income (Sec B):      $X,XXX  (handled separately)
```

Sum of the first three goes to Part I Line 2 (or Line 1a/1b for farmers).

### Step 3 — Determine if Part I Section A short form or Section B long form applies

The 2020 Schedule SE redesign merged the short and long forms into a single form, but the structure still distinguishes scenarios:

- **Part I** — standard SE tax computation (almost everyone)
- **Part II Section A** — farm optional method (farm income < $9,840 for 2025; verify 2026 threshold)
- **Part II Section B** — non-farm optional method (non-farm income < $7,103 for 2025; verify 2026 threshold) AND church employee income computation

Pick Part I for the typical solo / freelance filer.

### Step 4 — Compute Part I Line 3 (sum of SE earnings)

```
Line 1a = Schedule F Line 34 net farm profit (or 0)
Line 1b = Conservation Reserve Program payments excluded from SE under IRC §1402(a)(1) (rare; usually 0)
Line 2  = Schedule C Line 31 + K-1 Box 14 Code A
Line 3  = Line 1a + Line 1b + Line 2
```

### Step 5 — Apply the 0.9235 multiplier (Line 4a)

```
Line 4a = Line 3 × 0.9235
```

The 0.9235 factor (= 1 − 0.0765) approximates removing the "employer's share" of FICA from the SE base. It mathematically gives the self-employed filer parity with W-2 employees, who only pay FICA on 100% of their wage but whose employer pays a separate 7.65%. See IRC §1402(a)(12).

If Line 4a is **less than $400**, no SE tax is due. Stop and document. Otherwise continue.

### Step 6 — Add optional method amounts if elected (Lines 4b, 4c, 5a, 5b)

If the user elected farm or non-farm optional method (Step 1), add the elected amount per Part II Section A or B. Most filers skip this; if you do skip, Line 4c = Line 4a.

### Step 7 — Compute Line 7 (SS wage base for the year)

For tax year 2025, Line 7 prints "$176,100" — this is the Social Security wage base set by SSA each fall (verify the 2026 figure when the SSA announces it, typically late October 2025; the 2026 figure prints on the form itself once revised).

The 2026 Schedule SE form will state the 2026 wage base on Line 7 directly. **Always read it from the form**, do not hardcode.

### Step 8 — Subtract W-2 SS wages already subject to FICA (Line 8a + 8b + 8c)

```
Line 8a = Total W-2 Social Security wages (W-2 Box 3) for the same filer this year
Line 8b = Unreported tips subject to SS tax (from Form 4137; usually 0)
Line 8c = Wages subject to SS tax from Form 8919 (uncollected SS on misclassified worker; usually 0)
Line 8d = 8a + 8b + 8c
Line 9  = Line 7 − Line 8d   (remaining SS base available for SE earnings)
```

If Line 8d ≥ Line 7, Line 9 = 0 and the SS portion of SE tax is zero (the W-2 job already maxed out the SS wage base).

### Step 9 — Compute the Social Security portion (Line 10)

```
Line 10 = min(Line 6, Line 9) × 0.124
```

(Line 6 is total SE earnings post-0.9235 plus any optional method amount.) The 12.4% factor combines the 6.2% employee + 6.2% employer SS rate (IRC §1401(a)).

### Step 10 — Compute the Medicare portion (Line 11)

```
Line 11 = Line 6 × 0.029
```

Medicare has **no wage base cap** on Schedule SE. The 2.9% combines 1.45% employee + 1.45% employer (IRC §1401(b)).

(Note: high earners may also owe **Additional Medicare Tax** of 0.9% on the portion above $200K single / $250K MFJ — that's computed on **Form 8959**, not Schedule SE. Flag this for the user as a follow-up if Line 6 + W-2 wages exceeds the threshold.)

### Step 11 — Compute total SE tax (Line 12)

```
Line 12 = Line 10 + Line 11
```

This is the SE tax owed, reported on Schedule 2 Line 4 → Form 1040 Line 23.

### Step 12 — Compute the deductible half (Line 13)

```
Line 13 = Line 12 × 0.5
```

Half of SE tax is deductible on **Schedule 1 Line 15** (adjustment to income). This is the IRC §164(f) deduction — the self-employed filer's parity with employees, who don't pay tax on the employer's FICA share.

### Step 13 — Run validation checks

See **Validation** below. Run every check.

### Step 14 — Produce the deliverable

See **Output format** below.

### Step 15 — Hand off downstream

State the next forms the user will need:

- **Line 12** → flows to Schedule 2 Line 4 → Form 1040 Line 23 (other taxes)
- **Line 13** → flows to Schedule 1 Line 15 (adjustment to income, deductible)
- **Line 6 + W-2 wages > $200K (single) / $250K (MFJ) / $125K (MFS)** → Form 8959 (Additional Medicare Tax) is required
- **Quarterly estimated tax payments** for current year → Form 1040-ES; the SE tax is part of the quarterly estimate

### Step 16 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). Schedule SE travels with Form 1040; it is not e-filed independently.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- Filer's legal name and SSN. **Each spouse with SE income files a separate Schedule SE.** A joint return can have two Schedule SEs attached.

### Part I — Self-Employment Tax

| Line | Field | Source |
|------|-------|--------|
| 1a | Net farm profit | Schedule F Line 34 |
| 1b | CRP payments excluded | IRC §1402(a)(1); usually 0 |
| 2 | Net non-farm profit | Schedule C Line 31 + K-1 Box 14 Code A |
| 3 | Sum (Line 1a + 1b + 2) | Computed |
| 4a | Line 3 × 0.9235 | Computed |
| 4b | Optional method amount (farm) | Part II Section A; 0 if not elected |
| 4c | Combined (4a + 4b) | Computed |
| 5a | Church employee income | Form W-2 (church-electing-out-of-FICA only) |
| 5b | Line 5a × 0.9235 | Computed |
| 6 | Net earnings from SE (4c + 5b) | Computed |
| 7 | SS wage base for the year | Pre-printed on form (verify each year) |
| 8a | W-2 SS wages | W-2 Box 3 |
| 8b | Unreported tip income subject to SS | Form 4137; usually 0 |
| 8c | Wages subject to SS from Form 8919 | Usually 0 |
| 8d | 8a + 8b + 8c | Computed |
| 9 | Line 7 − Line 8d | Computed |
| 10 | min(Line 6, Line 9) × 0.124 | Computed (SS portion) |
| 11 | Line 6 × 0.029 | Computed (Medicare portion) |
| 12 | Line 10 + Line 11 | Total SE tax → Schedule 2 Line 4 |
| 13 | Line 12 × 0.5 | Deductible half → Schedule 1 Line 15 |

### Part II — Optional Methods + Church Employee Income

Three sections, all opt-in:

**Section A — Farm Optional Method.** Available if (gross farm income < $9,840 OR net farm profit < $7,103) for 2025; verify thresholds for the year being filed. Filer reports the lesser of $6,560 or 2/3 of gross farm income as Line 4b. Used to maintain Social Security credits when farm income is too low to otherwise generate them.

**Section B — Non-Farm Optional Method.** Available if (net non-farm earnings < $7,103) for 2025; verify thresholds. Requires net SE earnings ≥ $400 in 2 of the prior 3 years (IRC §1402(l)). Limit: can be elected at most 5 times in a lifetime. Filer reports 2/3 of gross non-farm income (cap $6,560 for 2025) as Line 4b.

**Section B (also) — Church Employee Income.** For W-2 wages from a church that has elected out of FICA under IRC §3121(w). Different from the optional methods. The wages go on Line 5a, get multiplied by 0.9235 on Line 5b, and flow to Line 6.

See [`references/optional-methods.md`](./references/optional-methods.md) for the threshold table and election rules.

### Special filers (foreign earned income, partnership, multi-state)

See [`references/special-filers.md`](./references/special-filers.md) for:
- Foreign earned income exclusion (Form 2555) — the exclusion does NOT reduce SE tax (IRC §911(d)(4))
- Partnership earnings — only general partner / LLC manager-member share is SE; limited partner share is not (IRC §1402(a)(13))
- Multi-state — SE tax is federal; state SE / city SE rules vary (NYC UBT, etc.)

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 3 = Line 1a + Line 1b + Line 2
- [ ] Line 4a = Line 3 × 0.9235 (rounded to nearest dollar)
- [ ] Line 4c = Line 4a + Line 4b
- [ ] Line 5b = Line 5a × 0.9235 (or 0)
- [ ] Line 6 = Line 4c + Line 5b
- [ ] Line 8d = Line 8a + Line 8b + Line 8c
- [ ] Line 9 = max(0, Line 7 − Line 8d)
- [ ] Line 10 = min(Line 6, Line 9) × 0.124
- [ ] Line 11 = Line 6 × 0.029
- [ ] Line 12 = Line 10 + Line 11
- [ ] Line 13 = Line 12 × 0.5

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 4a < $400 → Schedule SE not required (no SE tax) unless using an optional method
- [ ] Line 8a > Line 7 → user already exceeded SS wage base from W-2; Line 9 should be 0; Line 10 should be 0
- [ ] User has W-2 wages AND SE income totaling > $200K (single) / $250K (MFJ) / $125K (MFS) → Form 8959 (Additional Medicare Tax) is required and not handled by Schedule SE
- [ ] Schedule C Line 31 differs from Line 2 input → reconcile (the agent should pull from Schedule C, not re-enter)
- [ ] Optional method elected with net non-farm earnings ≥ $7,103 → ineligible; remove the election
- [ ] Optional method (non-farm) elected for 5th lifetime time → election no longer available
- [ ] Joint return with SE income from both spouses but only one Schedule SE drafted → second spouse needs a separate Schedule SE

### Cross-form checks

- [ ] If Line 12 > 0, ensure Schedule 2 Line 4 picks it up
- [ ] If Line 13 > 0, ensure Schedule 1 Line 15 picks it up (deduction)
- [ ] If using farm optional method, Schedule F must be attached
- [ ] If using non-farm optional method, Schedule C must be attached
- [ ] If church employee income on Line 5a, the relevant W-2 must show Box 14 with the church wages

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Schedule SE or paste into tax software. Format:

```markdown
# Schedule SE — DRAFT for tax year YYYY

## Header
Name of person with self-employment income: <legal name>
Social security number: <SSN>

## Part I — Self-Employment Tax
1a. Net farm profit (Schedule F Line 34):        $X,XXX
1b. CRP payments excluded:                       $0
2.  Net non-farm profit (Schedule C Line 31
    + K-1 Box 14 Code A):                        $X,XXX
3.  Combine 1a, 1b, 2:                           $X,XXX
4a. Line 3 × 0.9235:                             $X,XXX
4b. Optional method amount:                      $0  (or amount if elected)
4c. Combine 4a + 4b:                             $X,XXX
5a. Church employee income:                      $0
5b. Line 5a × 0.9235:                            $0
6.  Net earnings from SE (4c + 5b):              $X,XXX

7.  SS wage base for [year]:                     $XXX,XXX  (per IRS form)
8a. Total W-2 SS wages (Box 3):                  $XX,XXX
8b. Unreported tip income:                       $0
8c. Wages from Form 8919:                        $0
8d. Sum 8a + 8b + 8c:                            $XX,XXX
9.  Line 7 − Line 8d:                            $XXX,XXX

10. SS portion: min(Line 6, Line 9) × 0.124:     $X,XXX
11. Medicare portion: Line 6 × 0.029:            $X,XXX
12. Total SE tax (10 + 11):                      $X,XXX
13. Deductible half (12 × 0.5):                  $X,XXX

## Part II — Optional Methods (only if elected)
Section A — Farm Optional Method:                Not elected
Section B — Non-Farm Optional Method:            Not elected

## Required attachments
- [ ] Schedule C (if Line 2 from Schedule C)
- [ ] Schedule F (if Line 1a from Schedule F)
- [ ] Schedule K-1 (Form 1065) (if Line 2 includes partnership SE)
- [ ] Form 8959 (if combined wages + SE > Additional Medicare Tax threshold)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps:
  - Schedule 2 Line 4: $X,XXX (SE tax)
  - Schedule 1 Line 15: $X,XXX (deductible half)
  - Form 1040 Line 23 picks up Schedule 2 Line 4
  - Form 1040-ES quarterly estimates for next year if SE income continues

## Sources cited in this draft
- IRS Schedule SE (Form 1040), Rev. <YYYY>
- IRS Instructions for Schedule SE, Rev. <YYYY>
- IRC §1401 (rates), §1402 (definition of SE earnings), §164(f) (deductible half)
- SSA wage base announcement for [year]
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Schedule SE. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Schedule SE line with rules and edge cases
- [`references/optional-methods.md`](./references/optional-methods.md) — Farm and non-farm optional methods: thresholds, elections, lifetime limit
- [`references/wage-base-and-rates.md`](./references/wage-base-and-rates.md) — SS wage base history, FICA rate composition, 0.9235 factor derivation
- [`references/special-filers.md`](./references/special-filers.md) — Partners, church employees, clergy with Form 4361, foreign earned income, multi-state
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top audit-trip mistakes with citations and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Schedule SE with Form 1040

## Examples

End-to-end worked Schedule SEs. Use these as patterns when the user's situation is similar.

- [`examples/freelancer-50k.md`](./examples/freelancer-50k.md) — Straightforward freelancer with $50,000 Schedule C net profit, no W-2 wages
- [`examples/high-earner-250k.md`](./examples/high-earner-250k.md) — Consultant with $250,000 net profit; SS portion caps at the wage base, Medicare keeps applying, Additional Medicare Tax flagged
- [`examples/part-time-gig-4800.md`](./examples/part-time-gig-4800.md) — Part-time gig worker with $4,800 SE income; over the $400 threshold, no W-2 wages, modest SE tax owed

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises the form and the SS wage base each cycle.

- [Schedule SE Instructions: Complete Self-Employment Tax Guide 2026](https://jupid.com/blog/schedule-se-instructions-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Schedule SE (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) — the form itself
- [Instructions for Schedule SE](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf) — line-by-line IRS guidance
- [About Schedule SE (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-se-form-1040) — IRS landing page with archive of past revisions
- [Publication 334](https://www.irs.gov/publications/p334) — Tax Guide for Small Business (Sole Proprietor)
- [Publication 533](https://www.irs.gov/publications/p533) — Self-Employment Tax (legacy; now folded into Pub 334 and the Schedule SE instructions)
- [Self-Employment Tax overview](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) — IRS topic page
- [Social Security Administration — Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html) — annual wage base announcements
- IRC §1401 (SE tax rates), §1402 (definition of SE earnings), §1402(a)(12) (0.9235 factor), §1402(a)(13) (limited-partner exclusion), §1402(b) ($400 threshold), §1402(l) (non-farm optional method), §164(f) (deductible half), §3121(w) (church FICA election)
- Form 8959 — Additional Medicare Tax (separate skill / form for high earners)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-state operations, foreign income, partnership SE allocation disputes) warrant a licensed tax professional's review.
