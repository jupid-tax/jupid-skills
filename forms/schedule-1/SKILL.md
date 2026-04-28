---
name: schedule-1
description: |
  Use this skill when a taxpayer needs to fill out Schedule 1 (Form 1040) — Additional Income and Adjustments to Income — for tax year 2026. Triggers: "fill out Schedule 1", "report side income", "claim student loan interest deduction", "report unemployment income", "self-employed health insurance deduction", "HSA deduction on tax return", "above-the-line deductions", "where do I report my Etsy 1099-K", "report jury duty pay", "report gambling winnings".

  Do NOT use for: a return without any non-W-2 income or adjustments (Schedule 1 is not needed); business income reporting itself (use schedule-c skill); SE tax (use schedule-se skill); itemized deductions (use schedule-a skill); rental real estate income reporting (use schedule-e skill); farm income (use schedule-f skill).
form: Schedule 1 (Form 1040)
audience: [individual, solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1040s1.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
---

# Schedule 1 (Form 1040) — Additional Income and Adjustments to Income

This skill produces an audit-grade draft of Schedule 1 from the user's income sources, adjustments, and supporting forms. It walks through the form line by line, applies IRS rules at each line, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

Schedule 1 is mostly mechanical aggregation: amounts that originate on other schedules (C, E, F, SE) and forms (8889, 1098-E, 1099-G) get summed in two places — Line 10 (additional income) and Line 26 (adjustments). The judgment is in **whether** an item belongs here at all and **which sub-line** it goes on. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Schedule 1 (Form 1040) 2026: Additional Income & Adjustments Guide](https://jupid.com/blog/schedule-1-additional-income-adjustments-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule 1, "Schedule 1 form 1040", "additional income", or "above-the-line deduction"
- The user describes income that's not W-2 wages, ordinary interest, or dividends: 1099-G unemployment, 1099-K (personal), prize money, jury duty, hobby income, gambling winnings, alimony received, cancellation of debt, digital assets received as ordinary income
- The user describes an above-the-line adjustment: student loan interest paid (1098-E), HSA contribution (Form 8889), self-employed health insurance, SEP-IRA / SIMPLE / solo 401(k) contribution, half of SE tax, alimony paid (pre-2019 decree), educator expenses
- The user has filed Schedule C, E, F, or SE and needs to know where the result flows (answer: Schedule 1 Lines 3, 5, 6, and 15 respectively)
- The user received a 1099-K and isn't sure if/where to report it

Do **not** engage this skill when:

- The user has only W-2 wages and standard interest/dividends, no side income, no above-the-line adjustments → Schedule 1 isn't needed
- The user is filling out Schedule C itself → use the `schedule-c` skill (Schedule 1 receives the result, but the work happens in `schedule-c`)
- The user is computing self-employment tax → use the `schedule-se` skill (half of SE tax flows to Schedule 1 Line 15, but the calc is on Schedule SE)
- The user is claiming itemized deductions → use the `schedule-a` skill (those go below the line, not on Schedule 1)
- The user is reporting rental real estate or partnership income → use the `schedule-e` skill (result flows to Schedule 1 Line 5)
- The user is a farmer → use the `schedule-f` skill (result flows to Schedule 1 Line 6)

If the user's situation is ambiguous, ask before proceeding. The most common confusion: a freelancer with one 1099-NEC who thinks they fill out Schedule 1 directly — they don't. Schedule C captures the freelance income and expenses; Schedule 1 receives only the net result on Line 3.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Schedule 1 for tax year 2026 is filed in 2027. Numbers (HSA caps, SEP-IRA cap, student loan phaseout) depend on this.
2. **Filer's legal name and SSN/ITIN** as shown on Form 1040. Used in the Schedule 1 header. Do not invent.
3. **Whether each Part I income source applies**, with amounts and supporting forms:
   - Taxable refund from prior year (only if itemized last year)
   - Alimony received (only pre-2019 decrees)
   - Schedule C net profit/loss (request schedule-c skill output)
   - Form 4797 / 4684 gains or losses
   - Schedule E net result
   - Schedule F net result
   - Unemployment 1099-G Box 1 amount
   - Each Line 8 sub-type the user has (jury duty, gambling, prizes, hobby, cancellation of debt, digital assets, etc.)
4. **Whether each Part II adjustment applies**, with amounts and supporting forms:
   - Educator expenses (and 900-hour eligibility)
   - HSA contribution outside payroll (and Form 8889)
   - Half of SE tax (request schedule-se skill output)
   - SEP-IRA / SIMPLE / solo 401(k) contribution amount
   - SE health insurance premiums paid (and employer-coverage disqualifier check)
   - Alimony paid (only pre-2019 decrees)
   - Traditional IRA contribution (and active-plan-participant test)
   - Student loan interest paid (1098-E Box 1)
   - Each Line 24 sub-type the user has

For mixed-W-2-and-self-employment filers, also confirm: **was the filer eligible for an employer-subsidized health plan for any month**? This disqualifies them from claiming SE health insurance for that month on Line 17.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm Schedule 1 is needed

If the user has only W-2 wages, standard 1099-INT/1099-DIV, and no side income or adjustments, Schedule 1 is not required and you should tell them so. If they have **any** Part I income or **any** Part II adjustment, proceed.

### Step 2 — Collect Part I inputs

Walk through each Line 1-7 in turn:

- **Line 1** — Did the user get a state/local tax refund this year? Did they itemize last year (Schedule A) and get a tax benefit from the state income tax deduction? If both yes, use the IRS Pub 525 worksheet to compute the taxable portion.
- **Line 2a** — Alimony received under a pre-2019 decree only.
- **Line 3** — Schedule C net profit/loss. If the user hasn't done Schedule C yet, redirect to the `schedule-c` skill first.
- **Line 4** — Form 4797 / 4684 results (rare for solo filers).
- **Line 5** — Schedule E net result.
- **Line 6** — Schedule F net result.
- **Line 7** — Unemployment 1099-G Box 1.

### Step 3 — Collect Line 8 sub-line inputs

For each Line 8 sub-line (8a-8z), ask whether the user has anything to report. The 22 sub-lines are listed in [`references/line-by-line.md`](./references/line-by-line.md). Common entries for solo filers: 8b (gambling), 8c (cancellation of debt), 8h (jury duty), 8i (prizes/awards), 8j (hobby income), 8v (digital assets received as ordinary income).

**1099-K handling:** if the user received a 1099-K for personal items sold at a loss or in error, that amount goes on the line at the top of Schedule 1 (above Part I), not on Line 8. If the 1099-K is for a trade or business, it's already inside Schedule C (Line 3), don't double-count.

### Step 4 — Sum Part I

```
Line 9  = Sum of Lines 8a through 8z (some are negatives — 8a NOL, 8d Form 2555 exclusion, 8s Medicaid waiver)
Line 10 = Lines 1 + 2a + 3 + 4 + 5 + 6 + 7 + 9
```

### Step 5 — Collect Part II inputs

Walk through each Line 11-23 in turn:

- **Line 11** — Educator expenses (cap $300 for 2025; verify 2026 cap)
- **Line 12** — Reservist / performing artist / fee-basis official expenses (Form 2106)
- **Line 13** — HSA deduction (Form 8889)
- **Line 14** — Armed Forces moving expenses (Form 3903)
- **Line 15** — Half of SE tax (from Schedule SE Line 13)
- **Line 16** — Self-employed retirement plan contribution
- **Line 17** — SE health insurance (eligibility check: no employer-subsidized plan during covered period)
- **Line 18** — Penalty on early withdrawal of savings (1099-INT Box 2)
- **Line 19a** — Alimony paid (pre-2019 decree)
- **Line 20** — Traditional IRA deduction
- **Line 21** — Student loan interest (cap $2,500; phaseout based on MAGI)
- **Line 23** — Archer MSA deduction (rare — most filers use HSAs)

Then walk Line 24 sub-lines (24a-24z). For most solo filers, these are blank.

### Step 6 — Sum Part II

```
Line 25 = Sum of Lines 24a through 24z
Line 26 = Lines 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19a + 20 + 21 + 23 + 25
```

(Note: Line 22 is "reserved for future use" and is always blank.)

### Step 7 — Run validation checks

See **Validation** below. Run every check. Don't skip checks even if the math looks clean.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next forms the user will need:

- **Line 10 → Form 1040 Line 8** (additional income)
- **Line 26 → Form 1040 Line 10** (adjustments to income)
- **Line 13 used → Form 8889** must be attached
- **Line 14 used → Form 3903** must be attached
- **Line 15 used → Schedule SE** must be attached
- **Line 12 used → Form 2106** must be attached
- **Line 23 used → Form 8853** must be attached
- **Line 19a used → recipient SSN must be included on 19b**

### Step 10 — File the return (optional, if user wants the agent to file)

If the user authorizes filing, follow [`filing.md`](./filing.md). Schedule 1 is filed as part of Form 1040; the agent can't e-file Schedule 1 in isolation.

---

## Line-by-line guidance

For the complete reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Additional Income (Lines 1-10)

| Line | Field | Source / What goes here |
|------|-------|--------------------------|
| 1 | Taxable refunds, credits, or offsets of state and local income taxes | Form 1099-G Box 2, only if itemized prior year and got a benefit |
| 2a | Alimony received | Pre-2019 divorce decree only; post-2018 not taxable |
| 2b | Date of original divorce decree | Date field, not a number |
| 3 | Business income or (loss) | Schedule C Line 31 (net profit/loss) |
| 4 | Other gains or (losses) | Form 4797 / 4684 |
| 5 | Rental real estate, royalties, partnerships, S-corps, trusts | Schedule E result |
| 6 | Farm income or (loss) | Schedule F result |
| 7 | Unemployment compensation | 1099-G Box 1 |
| 8a | Net operating loss | Negative — carryforward from prior years |
| 8b | Gambling | Gross winnings (W-2G + cash); losses go on Schedule A only |
| 8c | Cancellation of debt | 1099-C amount unless exception applies |
| 8d | Foreign earned income exclusion | Negative — from Form 2555 |
| 8e | Income from Form 8853 | Archer MSA / LTC distributions |
| 8f | Income from Form 8889 | Non-qualified HSA distributions |
| 8g | Alaska Permanent Fund dividends | Annual dividend |
| 8h | Jury duty pay | Pay for jury service (offset by Line 24a if turned over to employer) |
| 8i | Prizes and awards | Game show, raffle, contest |
| 8j | Activity not engaged in for profit (hobby) | Gross hobby revenue (no expense offset) |
| 8k | Stock options | Non-statutory options not on W-2 |
| 8l | Income from rental of personal property (not a business) | Rare — occasional, not a trade |
| 8m | Olympic and Paralympic medals and USOC prize money | (offset by Line 24c if income limit met) |
| 8n | Section 951(a) inclusion (Subpart F) | CFC income |
| 8o | Section 951A(a) inclusion (GILTI) | Global intangible low-taxed income |
| 8p | Section 461(l) excess business loss adjustment | Add-back if losses exceeded threshold |
| 8q | Taxable distributions from an ABLE account | ABLE excess distributions |
| 8r | Scholarship and fellowship grants not on W-2 | Taxable portion |
| 8s | Nontaxable Medicaid waiver payments | Negative — backs out wages already on Form 1040 |
| 8t | Pension or annuity from nonqualified deferred comp / nongovt §457 plan | Distribution |
| 8u | Wages earned while incarcerated | Per IRS rule |
| 8v | Digital assets received as ordinary income | Crypto received as payment (not on Schedule C), NFT royalties, mining/staking |
| 8z | Other income — list type and amount | Catchall, label clearly |
| 9 | Total other income | Sum 8a through 8z |
| 10 | Additional income | Lines 1 + 2a + 3 + 4 + 5 + 6 + 7 + 9 → Form 1040 Line 8 |

### Part II — Adjustments to Income (Lines 11-26)

| Line | Field | Source / What goes here |
|------|-------|--------------------------|
| 11 | Educator expenses | Up to $300 for 2025; K-12 with 900+ hours |
| 12 | Reservist / performing artist / fee-basis gov't official expenses | Form 2106 |
| 13 | HSA deduction | Form 8889 (non-payroll contributions only) |
| 14 | Armed Forces moving expenses | Form 3903 |
| 15 | Deductible part of self-employment tax | Schedule SE Line 13 |
| 16 | SEP-IRA / SIMPLE / qualified plans | Owner's contribution only (not employees) |
| 17 | Self-employed health insurance | Premiums for self/spouse/dependents/children <27; capped at Schedule C profit |
| 18 | Penalty on early withdrawal of savings | 1099-INT Box 2 |
| 19a | Alimony paid | Pre-2019 decree only |
| 19b | Recipient's SSN | Required if 19a > 0 |
| 19c | Date of original divorce decree | Date field |
| 20 | IRA deduction | Traditional IRA only; phaseout if active-plan-participant |
| 21 | Student loan interest deduction | Up to $2,500; MAGI phaseout |
| 22 | Reserved for future use | Always blank |
| 23 | Archer MSA deduction | Form 8853; rare — closed to most new entrants |
| 24a-24z | Other adjustments | Specific items listed in [`references/above-the-line-deductions.md`](./references/above-the-line-deductions.md) |
| 25 | Total other adjustments | Sum 24a through 24z |
| 26 | Total adjustments | Lines 11+12+13+14+15+16+17+18+19a+20+21+23+25 → Form 1040 Line 10 |

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 9 = Sum of 8a through 8z (with negatives applied)
- [ ] Line 10 = Lines 1 + 2a + 3 + 4 + 5 + 6 + 7 + 9
- [ ] Line 25 = Sum of 24a through 24z
- [ ] Line 26 = Lines 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19a + 20 + 21 + 23 + 25
- [ ] Line 22 is blank (always)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 3 (Schedule C net profit) is on Schedule 1 but Schedule SE is not on the user's to-do list and Line 3 > $400 → SE tax is owed
- [ ] Line 17 (SE health insurance) > Line 3 (Schedule C net profit) → exceeds the IRC §162(l) cap
- [ ] Line 17 used but user was eligible for an employer-subsidized plan for any month → Line 17 must be reduced for those months
- [ ] Line 21 (student loan interest) > $2,500 → cap is statutory; entry must be capped
- [ ] Line 21 used but user's MAGI exceeds phaseout ceiling → Line 21 must be reduced or zeroed
- [ ] Line 1 (state refund) > 0 but user took standard deduction last year → state refund is not taxable, Line 1 should be 0
- [ ] Line 2a or 19a > 0 but decree date is 2019 or later → TCJA rules apply, alimony is neither income nor deduction
- [ ] Line 7 (unemployment) > 0 but no 1099-G provided → ask user for 1099-G to confirm amount
- [ ] Line 8j (hobby income) > 0 — confirm user understands hobby expenses are NOT deductible
- [ ] Line 13 (HSA) > 0 but user not on a qualifying HDHP → not eligible
- [ ] Line 16 (SEP/SIMPLE) > 0 but user has no Schedule C net profit → SEP/SIMPLE require earned SE income
- [ ] Line 8v (digital assets) > 0 — confirm whether the activity was a trade or business (would belong on Schedule C instead)

### Cross-form checks

- [ ] If Line 3 > $400, Schedule SE is required
- [ ] If Line 13 > 0, Form 8889 is attached
- [ ] If Line 14 > 0, Form 3903 is attached
- [ ] If Line 15 > 0, Schedule SE is attached
- [ ] If Line 19a > 0, recipient SSN on 19b and decree date on 19c
- [ ] If Line 23 > 0, Form 8853 is attached

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Schedule 1 or paste into tax software. Format:

```markdown
# Schedule 1 — DRAFT for tax year YYYY

## Header
Name(s): <filer name>
SSN: <SSN>
1099-K reported in error or for personal items sold at a loss: $X,XXX (or 0)

## Part I — Additional Income
 1. Taxable refunds:                          $X,XXX
 2a. Alimony received:                        $X,XXX
 2b. Date of original decree:                 MM/DD/YYYY (if 2a > 0)
 3. Business income (Schedule C):             $X,XXX
 4. Other gains (Form 4797/4684):             $X,XXX
 5. Rental, royalties, partnerships (Sch E):  $X,XXX
 6. Farm income (Sch F):                      $X,XXX
 7. Unemployment compensation:                $X,XXX
 8. Other income:
    8a. Net operating loss:                   ($X,XXX)
    8b. Gambling:                             $X,XXX
    8c. Cancellation of debt:                 $X,XXX
    ... (every sub-line, including zeros)
    8z. Other (list):                         $X,XXX
 9. Total other income (sum of 8a-8z):        $X,XXX
10. ADDITIONAL INCOME (= Form 1040 Line 8):   $X,XXX

## Part II — Adjustments to Income
11. Educator expenses:                        $X,XXX
12. Reservist/artist/fee-basis (Form 2106):   $X,XXX
13. HSA deduction (Form 8889):                $X,XXX
14. Armed Forces moving (Form 3903):          $X,XXX
15. Half of SE tax (Schedule SE):             $X,XXX
16. SEP/SIMPLE/qualified plans:               $X,XXX
17. SE health insurance:                      $X,XXX
18. Early withdrawal penalty:                 $X,XXX
19a. Alimony paid:                            $X,XXX
19b. Recipient SSN:                           XXX-XX-XXXX (if 19a > 0)
19c. Date of original decree:                 MM/DD/YYYY (if 19a > 0)
20. IRA deduction:                            $X,XXX
21. Student loan interest:                    $X,XXX
22. Reserved for future use:                  (blank)
23. Archer MSA deduction:                     $X,XXX
24. Other adjustments:
    24a. Jury duty pay turned over:           $X,XXX
    ... (every sub-line, including zeros)
    24z. Other (list):                        $X,XXX
25. Total other adjustments:                  $X,XXX
26. ADJUSTMENTS TO INCOME (= Form 1040 Line 10): $X,XXX

## Required attachments
- [ ] Form 8889 (if Line 13 > 0)
- [ ] Form 3903 (if Line 14 > 0)
- [ ] Schedule SE (if Line 15 > 0)
- [ ] Form 2106 (if Line 12 > 0)
- [ ] Form 8853 (if Line 23 > 0)
- [ ] Schedule C, E, F (whichever feed Lines 3, 5, 6)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 9>

## Sources cited in this draft
- IRS Schedule 1 (Form 1040) revision date YYYY
- IRS Form 1040 General Instructions (revision date YYYY)
- IRC §61, §62, §162(l), §164(f), §221, §223
- Rev. Proc. 2024-25 (HSA limits for 2025)
- Rev. Proc. 2024-40 (other inflation adjustments for 2025)
- Rev. Proc. 2025-XX (2026 inflation adjustments — verify before filing)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Schedule 1. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on the user's situation:

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Schedule 1 line with examples and edge cases
- [`references/additional-income-types.md`](./references/additional-income-types.md) — Deep guidance on each Line 8 sub-type
- [`references/above-the-line-deductions.md`](./references/above-the-line-deductions.md) — Eligibility tests for each Part II adjustment
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`references/state-refund-taxability.md`](./references/state-refund-taxability.md) — When a prior-year state refund is taxable on Line 1
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files a completed Schedule 1 as part of Form 1040

## Examples

End-to-end worked Schedule 1s. Use these as patterns when the user's situation is similar:

- [`examples/freelance-designer-side-gig.md`](./examples/freelance-designer-side-gig.md) — Maya, freelance designer with Etsy 1099-K, student loan interest, SE health insurance, SEP-IRA contribution
- [`examples/gig-driver-with-unemployment.md`](./examples/gig-driver-with-unemployment.md) — Uber driver who received unemployment compensation early in the year, then started driving
- [`examples/consultant-with-hsa-and-sep.md`](./examples/consultant-with-hsa-and-sep.md) — Solo consultant with HSA contributions, SEP-IRA, SE health insurance, half of SE tax

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed:

- [Schedule 1 (Form 1040) 2026: Additional Income & Adjustments Guide](https://jupid.com/blog/schedule-1-additional-income-adjustments-2026) — Jupid's narrative companion to this skill, written for human readers
- [Schedule 1 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) — the form itself
- [Form 1040 General Instructions](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — covers Schedule 1 line-by-line
- [About Schedule 1 (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-1-form-1040) — IRS landing page
- [Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (For Individuals)
- [Publication 525](https://www.irs.gov/publications/p525) — Taxable and Nontaxable Income
- [Publication 521](https://www.irs.gov/publications/p521) — Moving Expenses
- [Publication 535](https://www.irs.gov/publications/p535) — Business Expenses
- [Publication 969](https://www.irs.gov/publications/p969) — Health Savings Accounts and Other Tax-Favored Health Plans
- [Publication 970](https://www.irs.gov/publications/p970) — Tax Benefits for Education
- [Form 8889](https://www.irs.gov/pub/irs-pdf/f8889.pdf) — Health Savings Accounts
- [Form 3903](https://www.irs.gov/pub/irs-pdf/f3903.pdf) — Moving Expenses
- [Form 1098-E](https://www.irs.gov/forms-pubs/about-form-1098-e) — Student Loan Interest Statement
- IRC §61 (gross income), §62 (above-the-line adjustments), §71 (alimony, pre-TCJA), §162(l) (SE health insurance), §164(f) (half of SE tax), §221 (student loan interest), §223 (HSA), §274(n) (50% meals)
- Rev. Proc. 2024-25 — HSA contribution limits for 2025
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025
- Notice 2024-80 — retirement plan contribution limits for 2025

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
