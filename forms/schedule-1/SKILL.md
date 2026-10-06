---
name: schedule-1
description: |
  Use this skill when a taxpayer needs to fill out Schedule 1 (Form 1040) — Additional Income and Adjustments to Income — for the 2025 tax year (filed in 2026). Triggers: "fill out Schedule 1", "report side income", "claim student loan interest deduction", "report unemployment income", "self-employed health insurance deduction", "HSA deduction on tax return", "above-the-line deductions", "where do I report my Etsy 1099-K", "report jury duty pay", "report gambling winnings".

  Do NOT use for: a return without any non-W-2 income or adjustments (Schedule 1 is not needed); business income reporting itself (use schedule-c skill); SE tax (use schedule-se skill); itemized deductions (use schedule-a skill); the 2025 no-tax-on-tips, overtime, car loan interest, or senior deductions (those go on Schedule 1-A, not Schedule 1, and flow to Form 1040 line 13b); rental real estate income reporting (use schedule-e skill); farm income (Schedule F; no skill in this repo yet).
form: Schedule 1 (Form 1040)
audience: [individual, solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040s1.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
---

# Schedule 1 (Form 1040) — Additional Income and Adjustments to Income

This skill produces an audit-grade draft of Schedule 1 from the user's income sources, adjustments, and supporting forms. It walks through the form line by line, applies IRS rules at each line, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

Schedule 1 is mostly mechanical aggregation: amounts that originate on other schedules (C, E, F, SE) and forms (8889, 1098-E, 1099-G) get summed in two places — Line 10 (additional income) and Line 26 (adjustments). The judgment is in **whether** an item belongs here at all and **which sub-line** it goes on. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Schedule 1 (Form 1040) + AI Agent Skill: Additional Income Guide 2026](https://jupid.com/blog/schedule-1-additional-income-adjustments-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision:** the line map was verified on 2026-10-06 against the 2025 Schedule 1 (Form 1040) (created 7/25/25) and the Schedule 1 section of the 2025 Instructions for Form 1040, filed in 2026. Before using this skill for a later tax year, re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1040 (IRS.gov/Schedule1 redirects there).

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
- The user is filling out Schedule C itself → use the [`schedule-c`](../schedule-c/SKILL.md) skill (Schedule 1 receives the result, but the work happens in `schedule-c`)
- The user is computing self-employment tax → use the [`schedule-se`](../schedule-se/SKILL.md) skill (half of SE tax flows to Schedule 1 Line 15, but the calc is on Schedule SE)
- The user is claiming itemized deductions → use the [`schedule-a`](../schedule-a/SKILL.md) skill (those go below the line, not on Schedule 1)
- The user is reporting rental real estate or partnership income → use the [`schedule-e`](../schedule-e/SKILL.md) skill (result flows to Schedule 1 Line 5)
- The user is working the HSA contribution and distribution math → use the [`form-8889`](../form-8889/SKILL.md) skill (the deduction lands on Line 13, income on Line 8f)
- The user is a farmer → Schedule F (no skill in this repo yet; result flows to Schedule 1 Line 6). Tell the user and stop for that part.
- The user asks about the 2025 deductions for qualified tips, qualified overtime, car loan interest, or the enhanced deduction for seniors → those are claimed on **Schedule 1-A** (Form 1040 line 13b), not on Schedule 1. Schedule 1 has no line for them. Source: 2025 Schedule 1-A, line 38; 2025 Form 1040, line 13b.

If the user's situation is ambiguous, ask before proceeding. The most common confusion: a freelancer with one 1099-NEC who thinks they fill out Schedule 1 directly — they don't. Schedule C captures the freelance income and expenses; Schedule 1 receives only the net result on Line 3.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The 2025 Schedule 1 is filed in 2026; a 2026 return (filed in 2027) uses the 2026 revision, which must be re-checked. Numbers (HSA caps, SEP-IRA cap, student loan phaseout) depend on this.
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

- **Line 1** — Did the user get a state/local income tax refund this year? Did they itemize last year (Schedule A) and deduct state income tax (not sales tax)? If both yes, use the State and Local Income Tax Refund Worksheet in the 2025 Form 1040 instructions (or Pub 525 when one of its listed exceptions applies) to compute the taxable portion.
- **Line 2a** — Alimony received under a pre-2019 decree only.
- **Line 3** — Schedule C net profit/loss. If the user hasn't done Schedule C yet, redirect to the `schedule-c` skill first.
- **Line 4** — Form 4797 line 18b (check the 4797 box), or Form 4684 line 31 if Form 4797 isn't otherwise required (check the 4684 box). Rare for solo filers.
- **Line 5** — Schedule E net result.
- **Line 6** — Schedule F net result.
- **Line 7** — Unemployment 1099-G Box 1. If the user repaid a 2025 overpayment in 2025, subtract it, check the line 7 box, and enter the amount repaid.

### Step 3 — Collect Line 8 sub-line inputs

For each Line 8 sub-line (8a-8z), ask whether the user has anything to report. The 22 lettered sub-lines (8a-8v) plus 8z are listed in [`references/line-by-line.md`](./references/line-by-line.md). Common entries for solo filers: 8b (gambling), 8c (cancellation of debt), 8h (jury duty), 8i (prizes/awards), 8j (hobby income), 8v (digital assets received as ordinary income).

**1099-K handling:** if the user received a 1099-K for personal items sold at a loss or in error, that amount goes on the line at the top of Schedule 1 (above Part I), not on Line 8. A personal item sold at a gain goes on Form 8949 / Schedule D. If the 1099-K is for a trade or business, it's already inside Schedule C (Line 3), don't double-count. For 2025, platforms must issue a 1099-K only when payments exceed $20,000 and transactions exceed 200 (2025 Form 1040 instructions, What's New and Schedule 1 "Form(s) 1099-K"); income below that threshold is still reportable.

### Step 4 — Sum Part I

```
Line 9  = Sum of Lines 8a through 8z (some are negatives — 8a NOL, 8d Form 2555 exclusion, 8s Medicaid waiver)
Line 10 = Lines 1 + 2a + 3 + 4 + 5 + 6 + 7 + 9
```

### Step 5 — Collect Part II inputs

Walk through each Line 11-23 in turn:

- **Line 11** — Educator expenses (cap $300 for 2025, $600 if both spouses qualify; $350 for 2026 per Rev. Proc. 2025-32 §4.12)
- **Line 12** — Reservist / performing artist / fee-basis official expenses (Form 2106)
- **Line 13** — HSA deduction (Form 8889)
- **Line 14** — Armed Forces moving expenses (Form 3903; check the line 14 box if claiming only storage fees)
- **Line 15** — Half of SE tax (from Schedule SE Line 13)
- **Line 16** — Self-employed retirement plan contribution
- **Line 17** — SE health insurance (eligibility check: no employer-subsidized plan during covered period)
- **Line 18** — Penalty on early withdrawal of savings (1099-INT Box 2)
- **Line 19a** — Alimony paid (pre-2019 decree)
- **Line 20** — Traditional IRA deduction (check the line 20 box if MFS and lived apart from the spouse all year)
- **Line 21** — Student loan interest (cap $2,500; 2025 MAGI phaseout $85,000–$100,000, $170,000–$200,000 MFJ, not allowed MFS)
- **Line 23** — Archer MSA deduction (rare — most filers use HSAs)

Then walk Line 24 sub-lines (24a-24k). For most solo filers, these are blank. The 2025 instructions say to leave line 24z blank.

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
| 2b | Date of original divorce or separation agreement | Month and year (instructions); attach a statement if more than one agreement |
| 3 | Business income or (loss) | Schedule C Line 31 (net profit/loss) |
| 4 | Other gains or (losses) | Form 4797 line 18b, or Form 4684 line 31; check the matching box |
| 5 | Rental real estate, royalties, partnerships, S-corps, trusts | Schedule E result |
| 6 | Farm income or (loss) | Schedule F result |
| 7 | Unemployment compensation | 1099-G Box 1, less any same-year repayment (check box, enter amount repaid) |
| 8a | Net operating loss | Negative — carryforward from prior years |
| 8b | Gambling | Gross winnings (W-2G + cash); losses go on Schedule A only |
| 8c | Cancellation of debt | 1099-C amount unless exception applies |
| 8d | Foreign earned income exclusion | Negative — Form 2555 line 45 (income and housing exclusion) |
| 8e | Income from Form 8853 | Archer MSA / LTC distributions |
| 8f | Income from Form 8889 | Form 8889 lines 16 and 20 (taxable distributions, testing-period income) |
| 8g | Alaska Permanent Fund dividends | Annual dividend |
| 8h | Jury duty pay | Pay for jury service (offset by Line 24a if turned over to employer) |
| 8i | Prizes and awards | Game show, raffle, contest |
| 8j | Activity not engaged in for profit (hobby) | Gross hobby revenue (no expense offset) |
| 8k | Stock options | Income from exercise of stock options not otherwise reported on Form 1040 line 1h |
| 8l | Income from rental of personal property (not a business) | Rare — occasional, not a trade |
| 8m | Olympic and Paralympic medals and USOC prize money | (offset by Line 24c if income limit met) |
| 8n | Section 951(a) inclusion (Subpart F) | CFC income |
| 8o | Section 951A(a) inclusion (GILTI) | Global intangible low-taxed income |
| 8p | Section 461(l) excess business loss adjustment | Form 461 line 16 |
| 8q | Taxable distributions from an ABLE account | ABLE excess distributions |
| 8r | Scholarship and fellowship grants not on W-2 | Taxable portion |
| 8s | Nontaxable Medicaid waiver payments | Negative — backs out wages already on Form 1040 |
| 8t | Pension or annuity from nonqualified deferred comp / nongovt §457 plan | Distribution |
| 8u | Wages earned while incarcerated | Per IRS rule |
| 8v | Digital assets received as ordinary income | Ordinary income from digital assets not reported elsewhere (e.g., forks, staking, mining when not Schedule C); not gifts or inheritances |
| 8z | Other income — list type and amount | Catchall, label clearly |
| 9 | Total other income | Sum 8a through 8z |
| 10 | Additional income | Lines 1 + 2a + 3 + 4 + 5 + 6 + 7 + 9 → Form 1040 Line 8 |

### Part II — Adjustments to Income (Lines 11-26)

| Line | Field | Source / What goes here |
|------|-------|--------------------------|
| 11 | Educator expenses | Up to $300 for 2025 ($600 MFJ if both qualify); K-12 with 900+ hours |
| 12 | Reservist / performing artist / fee-basis gov't official expenses | Form 2106 |
| 13 | HSA deduction | Form 8889 (non-payroll contributions only) |
| 14 | Armed Forces moving expenses | Form 3903; checkbox for storage-fees-only claims |
| 15 | Deductible part of self-employment tax | Schedule SE Line 13 |
| 16 | SEP-IRA / SIMPLE / qualified plans | Owner's contribution only (not employees) |
| 17 | Self-employed health insurance | Premiums for self/spouse/dependents/children <27; capped at net profit minus Lines 15 and 16 (worksheet in the instructions, or Form 7206) |
| 18 | Penalty on early withdrawal of savings | 1099-INT Box 2 or 1099-OID Box 3 |
| 19a | Alimony paid | Pre-2019 decree only |
| 19b | Recipient's SSN | Required if 19a > 0 |
| 19c | Date of original divorce or separation agreement | Month and year |
| 20 | IRA deduction | Traditional IRA only; phaseout if active-plan-participant; MFS lived-apart checkbox |
| 21 | Student loan interest deduction | Up to $2,500; 2025 MAGI phaseout $85,000–$100,000 ($170,000–$200,000 MFJ) |
| 22 | Reserved for future use | Always blank |
| 23 | Archer MSA deduction | Form 8853; rare — closed to most new entrants |
| 24a-24k | Other adjustments | Specific items listed in [`references/above-the-line-deductions.md`](./references/above-the-line-deductions.md); 2025 instructions: leave 24z blank |
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

- [ ] Line 3 (Schedule C net profit) is on Schedule 1 but Schedule SE is not on the user's to-do list and net earnings from self-employment (Line 3 × 92.35%) are $400 or more → SE tax is owed
- [ ] Line 17 (SE health insurance) > Line 3 minus Lines 15 and 16 → exceeds the IRC §162(l) cap
- [ ] Line 17 used but user (or spouse, dependent, or child under 27) was eligible for an employer-subsidized plan for any month → Line 17 must be reduced for those months
- [ ] Line 17 premiums are for Marketplace coverage with advance premium tax credit → use Pub 974, not the simple worksheet
- [ ] Line 21 (student loan interest) > $2,500 → cap is statutory; entry must be capped
- [ ] Line 21 used but user's MAGI exceeds phaseout ceiling → Line 21 must be reduced or zeroed
- [ ] Line 1 (state refund) > 0 but user took standard deduction last year (or deducted sales tax instead of income tax) → state refund is not taxable, Line 1 should be 0
- [ ] Line 2a or 19a > 0 but decree date is 2019 or later → TCJA rules apply, alimony is neither income nor deduction
- [ ] Line 7 (unemployment) > 0 but no 1099-G provided → ask user for 1099-G to confirm amount
- [ ] Line 8j (hobby income) > 0 — confirm user understands hobby expenses are NOT deductible
- [ ] Line 13 (HSA) > 0 but user not on a qualifying HDHP → not eligible
- [ ] Line 16 (SEP/SIMPLE) > 0 but user has no Schedule C net profit → SEP/SIMPLE require earned SE income
- [ ] Line 8v (digital assets) > 0 — confirm whether the activity was a trade or business (would belong on Schedule C instead)

### Cross-form checks

- [ ] If net earnings from self-employment are $400 or more, Schedule SE is required
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
 2b. Date of original agreement:              MM/YYYY (if 2a > 0)
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
19c. Date of original agreement:              MM/YYYY (if 19a > 0)
20. IRA deduction:                            $X,XXX
21. Student loan interest:                    $X,XXX
22. Reserved for future use:                  (blank)
23. Archer MSA deduction:                     $X,XXX
24. Other adjustments:
    24a. Jury duty pay turned over:           $X,XXX
    ... (every sub-line, including zeros)
    24z. Other adjustments:                   (blank — 2025 instructions)
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
- Rev. Proc. 2024-25 (HSA limits for 2025); Rev. Proc. 2025-19 (2026)
- Rev. Proc. 2024-40 (other inflation adjustments for 2025)
- Notice 2024-80 (2025 retirement plan and IRA limits); Notice 2025-67 (2026)
- Rev. Proc. 2025-32 (2026 inflation adjustments)
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
- [`filing.md`](./filing.md) — Filing playbook: how an agent files a completed Schedule 1 as part of Form 1040

## Examples

End-to-end worked Schedule 1s. Use these as patterns when the user's situation is similar:

- [`examples/freelance-designer-side-gig.md`](./examples/freelance-designer-side-gig.md) — Maya, freelance designer with Etsy 1099-K, student loan interest, SE health insurance, SEP-IRA contribution
- [`examples/gig-driver-with-unemployment.md`](./examples/gig-driver-with-unemployment.md) — Uber driver who received unemployment compensation early in the year, then started driving
- [`examples/consultant-with-hsa-and-sep.md`](./examples/consultant-with-hsa-and-sep.md) — Solo consultant with HSA contributions, SEP-IRA, SE health insurance, half of SE tax

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed:

- [Schedule 1 (Form 1040) + AI Agent Skill: Additional Income Guide 2026](https://jupid.com/blog/schedule-1-additional-income-adjustments-2026) — Jupid's narrative companion to this skill, written for human readers
- [Schedule 1 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) — the form itself
- [Form 1040 General Instructions](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — covers Schedule 1 and Schedule 1-A line-by-line
- [Schedule 1-A (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s1a.pdf) — Additional Deductions (tips, overtime, car loan interest, seniors); not part of Schedule 1
- [About Form 1040](https://www.irs.gov/forms-pubs/about-form-1040) — IRS landing page for Form 1040 and its numbered schedules (IRS.gov/Schedule1 redirects here)
- [Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (For Individuals)
- [Publication 525](https://www.irs.gov/publications/p525) — Taxable and Nontaxable Income
- [Instructions for Form 3903](https://www.irs.gov/pub/irs-pdf/i3903.pdf) — Moving Expenses (Armed Forces)
- [Instructions for Form 7206](https://www.irs.gov/pub/irs-pdf/i7206.pdf) and [Publication 974](https://www.irs.gov/publications/p974) — self-employed health insurance deduction (Pub 535 is no longer revised)
- [Publication 560](https://www.irs.gov/publications/p560) — Retirement Plans for Small Business (SEP, SIMPLE, and Qualified Plans)
- [Publication 590-A](https://www.irs.gov/publications/p590a) — Contributions to IRAs
- [Publication 969](https://www.irs.gov/publications/p969) — Health Savings Accounts and Other Tax-Favored Health Plans
- [Publication 970](https://www.irs.gov/publications/p970) — Tax Benefits for Education
- [Form 8889](https://www.irs.gov/pub/irs-pdf/f8889.pdf) — Health Savings Accounts
- [Form 3903](https://www.irs.gov/pub/irs-pdf/f3903.pdf) — Moving Expenses
- [Form 1098-E](https://www.irs.gov/forms-pubs/about-form-1098-e) — Student Loan Interest Statement
- IRC §61 (gross income), §62 (above-the-line adjustments), §71 (alimony, pre-TCJA), §162(l) (SE health insurance), §164(f) (half of SE tax), §217 (moving expenses; civilian deduction ended permanently by P.L. 119-21 §70113), §221 (student loan interest), §223 (HSA)
- Rev. Proc. 2024-25 — HSA contribution limits for 2025; Rev. Proc. 2025-19 — 2026
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025; Rev. Proc. 2025-32 — 2026
- Notice 2024-80 — retirement plan and IRA limits for 2025; Notice 2025-67 — 2026

Re-verify each year-dependent number against the IRS source for the tax year being filed.

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
