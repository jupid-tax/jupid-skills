---
name: form-8829
description: >
  Use this skill when a sole proprietor or single-member LLC owner who files
  Schedule C wants to deduct actual expenses for business use of their home on
  IRS Form 8829, or wants to compare Form 8829 with the simplified home office
  method. Triggers on phrases like "fill out form 8829", "home office deduction
  regular method", "actual expense method home office", "form 8829 line 11
  worksheet", "home office depreciation", "home office carryover", "daycare
  home office percentage", "schedule c line 30 form 8829". Do NOT use for W-2
  employees working from home (not deductible; explain and stop), for partners
  or Schedule F farmers (Pub. 587 worksheet, not Form 8829), for renting part
  of a home to a tenant (use schedule-e), for the rest of Schedule C (use
  schedule-c), for depreciating business equipment (use form-4562), or for
  selling the home (use form-8949 / schedule-d, or form-4797 for a separate
  business structure).
form: Form 8829 (Expenses for Business Use of Your Home)
audience: [solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8829.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8829.pdf
---

# Form 8829 — Expenses for Business Use of Your Home

This skill produces an audit-grade draft of Form 8829 for one home: the business percentage (Part I), the allowable deduction with the gross income limit and carryovers (Part II), depreciation of the home for owners (Part III), and the carryovers to next year (Part IV). It ends with the amount for Schedule C line 30 and a side-by-side figure for the simplified method.

The arithmetic is short. The judgment sits in four places: whether the space qualifies at all (exclusive and regular use plus a qualifying purpose), which expenses go in which tier and column (itemizer vs standard deduction, direct vs indirect), the order in which the income limit cuts expenses off, and the depreciation basis. Each depends on facts the agent must ask for.

Line map verified against the **2025 Form 8829** (footer "Created 10/2/25") and the **2025 Instructions for Form 8829** (dated Mar 4, 2026), the revision filed in 2026 for tax year 2025. Before using this skill for a later tax year, download the new revision from https://www.irs.gov/forms-pubs/about-form-8829 and re-check every line number, the line 41 percentage table, and the Line 11 Worksheet thresholds.

**Companion guide for end users:** [Form 8829 Instructions: Home Office Deduction Guide 2026](https://jupid.com/blog/form-8829-instructions-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user names Form 8829, "regular method" or "actual expense method" for a home office, or Schedule C line 30 with actual expenses
- The user files Schedule C, works from home, and asks how much of their rent, mortgage interest, utilities, insurance, or home depreciation they can deduct
- The user has a home office carryover from a prior Form 8829 (lines 43–44) or a prior Simplified Method Worksheet (lines 6a–6b)
- The user runs a licensed home daycare, or stores inventory at home as their only fixed business location, and asks about deducting home costs
- The [schedule-c skill](../schedule-c/SKILL.md) hands off line 30 with the regular method

Do **not** engage this skill when:

- The user is an **employee** working from home (W-2, no Schedule C for that work) → explain that the expense is not deductible on the personal return (2025 Instructions for Form 8829; IRC §67(h) as amended by P.L. 119-21 §70110) and stop. Do not suggest workarounds.
- The user is a **partner** claiming home expenses, or a **Schedule F** farmer → the Pub. 587 worksheet applies, not Form 8829; partners report through [schedule-e](../schedule-e/SKILL.md). Say so and stop.
- The user rents part of the home to a tenant → [schedule-e](../schedule-e/SKILL.md) (rental use cannot use the simplified method and is not Form 8829 space).
- The user wants only the simplified method with no comparison → compute it inside the [schedule-c skill](../schedule-c/SKILL.md) (Schedule C line 30 and its Simplified Method Worksheet); this skill is still useful for frozen carryovers.
- The user is depreciating furniture, computers, or equipment → [form-4562](../form-4562/SKILL.md).
- The user is selling the home → [form-8949](../form-8949/SKILL.md) and [schedule-d](../schedule-d/SKILL.md); a separate business structure may need [form-4797](../form-4797/SKILL.md); a seller-financed sale → [form-6252](../form-6252/SKILL.md). This skill supplies only the cumulative depreciation history.
- The business is an S corporation or partnership that reimburses the owner → entity skills ([form-1120-s](../form-1120-s/SKILL.md), [form-1065](../form-1065/SKILL.md)); Form 8829 attaches only to Schedule C.

Boundaries with siblings: Schedule C line 29 comes from [schedule-c](../schedule-c/SKILL.md); the personal share of mortgage interest and real estate taxes goes to [schedule-a](../schedule-a/SKILL.md); first-year home depreciation is also reported on [form-4562](../form-4562/SKILL.md) line 19j; the resulting Schedule C line 31 feeds [schedule-se](../schedule-se/SKILL.md) and [form-8995](../form-8995/SKILL.md).

---

## Prerequisites

Collect every item before computing. If any item is missing, ask a tight question and stop until the user answers. Never default.

1. **Tax year** and whether this is the first year the home was used for business. The skill's tables are for tax year 2025 returns.
2. **Filer status**: sole proprietor or single-member LLC filing Schedule C. Ask: "Is the work you do at home for your own business reported on Schedule C, or for an employer?"
3. **Qualification facts** (see [references/qualification-tests.md](./references/qualification-tests.md)):
   - "Is the space used only for business? Does anyone use it for anything else?"
   - "What do you do there: billing, scheduling, bookkeeping, client meetings, production work?"
   - "Do you have any other fixed location where you do substantial administrative work for this business?"
   - Daycare: "Do you hold, or have you applied for, a state daycare license, certification, or registration, or are you exempt?" Inventory storage: "Is your home the only fixed location of the business?"
4. **Areas**: square feet of the business area and of the whole home (or another reasonable measure). For daycare: hours used and days available; whether any room is used only for daycare.
5. **Period of use**: the full year, or start/stop dates. Part-year use limits expenses to the business period.
6. **Schedule C line 29** for this business, plus any gain or loss from business use of the home on Form 8949/Schedule D or Form 4797, and whether any gross income comes from another business location.
7. **Itemize or standard deduction** for the year. If itemizing: deductible mortgage interest under the Pub. 936 limits, and state and local income (or sales), real estate, and personal property taxes for the Line 11 Worksheet; if MAGI could exceed $500,000 ($250,000 MFS), say the worksheet may need iteration and flag CPA review.
8. **Expenses** for the business period, each labeled as whole-home (indirect) or business-area-only (direct): mortgage interest, real estate taxes, casualty losses (and whether from a federally declared disaster), insurance, rent, repairs, utilities, other. Ask whether any item is an improvement rather than a repair.
9. **Owners only**: month and year of first business use; purchase price; improvements before business use; FMV of the home on the first-business-use date; land basis and land FMV on that date; improvements placed in service after business use began (dates, costs); depreciation claimed in earlier years.
10. **Carryovers**: prior Form 8829 lines 43 and 44, or the Simplified Method Worksheet lines 6a and 6b from a simplified-method year. Ask: "Did you file Form 8829 for any earlier year? What is on lines 43 and 44 of the most recent one?"
11. **Other homes and businesses**: more than one home used during the year (one Form 8829 each; simplified method for at most one), or more than one business in the same home (line 36 allocation).

---

## Workflow

### Step 1 — Gate the filer

Confirm Schedule C filer and not an employee, partner, or Schedule F filer. Any "no" ends the skill with an explanation and the right sibling.

### Step 2 — Run the qualification tests

Apply exclusive-and-regular use, then one qualifying purpose (principal place of business, client meetings, separate structure, inventory storage, daycare) from [references/qualification-tests.md](./references/qualification-tests.md). Record the user's answers verbatim in the draft. If the space fails, stop and explain; do not compute a smaller "partial" area on your own.

### Step 3 — Figure Part I

Line 1 ÷ line 2 → line 3. Daycare not used exclusively: lines 4–6 (line 5 = 8,760, or 24 × days available when daycare started or stopped during the year), line 7 = line 6 × line 3. Mixed exclusive and part-time daycare rooms: the three-step special computation with an attached statement. Round percentages to two decimals and line 6 to four decimals; state the convention.

### Step 4 — Owners: complete Part III before Part II

Line 30 needs line 42. Compute lines 37–42 with [references/home-depreciation.md](./references/home-depreciation.md): smaller of adjusted basis or FMV (both including land) on the first-business-use date, minus land, times line 7, times the line 41 percentage. Add the improvements statement. Note Form 4562 line 19j when first use or improvements fall in the tax year. Renters: Part III is N/A.

### Step 5 — Sort every expense into tier, line, and column

Use [references/line-by-line.md](./references/line-by-line.md). Itemizers: lines 9–11 (Line 11 Worksheet when total SALT exceeds $10,000, $5,000 MFS); standard-deduction filers: mortgage interest to line 16(b), real estate taxes to line 17(b). Direct expenses in column (a); indirect in column (b); a differing business percentage goes in column (a) as the business part only. Daycare direct expenses × line 6 first. Remove non-home expenses (supplies, phone line, advertising) and send them back to the Schedule C lines.

### Step 6 — Apply the limit in form order

Line 8 → Tier 1 (lines 12–14) → line 15 → Tier 2 (lines 23–27) → line 28 → Tier 3 (lines 29–33) → lines 34–36. Never let Tier 2 or Tier 3 exceed its cap. See [references/limits-and-carryovers.md](./references/limits-and-carryovers.md).

### Step 7 — Carryovers

Line 43 = line 26 − line 27; line 44 = line 32 − line 33 (not below zero). Write both in the draft as next year's lines 25 and 31.

### Step 8 — Simplified-method comparison

Compute the Simplified Method Worksheet figure ($5 per square foot, at most 300 square feet, limited by the gross income limitation; reduced rate and monthly averaging for daycare or part-year use) and show it next to line 36, with what moves where: Tier 1 items stay on Schedule A under the simplified method; carryovers freeze; no home depreciation. Do not recommend a method. If the user asks, say the choice is theirs or their CPA's and that the simplified election for a year is irrevocable once made on a timely original return.

### Step 9 — Validate

Run every check in **Validation**. Surface failures; do not silently fix.

### Step 10 — Produce the deliverable and the hand-offs

Fill the **Output format** template. Hand-offs: Schedule C line 30 (line 36) to [schedule-c](../schedule-c/SKILL.md); personal mortgage interest and real estate taxes to [schedule-a](../schedule-a/SKILL.md); Form 4562 line 19j row to [form-4562](../form-4562/SKILL.md); Form 4684 line 27 if line 35 > 0. Owners: include the sentence about depreciation at sale.

### Step 11 — Filing (only if the user asks the agent to file)

Follow [filing.md](./filing.md): channel choice, attachment order, mailing addresses, consent and security rules.

---

## Line-by-line guidance

Full map with every caption: [references/line-by-line.md](./references/line-by-line.md). Rules that decide the result:

### Part I (lines 1–7)

- Line 1 counts only area used regularly and exclusively for business, regularly for daycare, or for storage of inventory or product samples. Exclude area whose costs are already allocated to inventory (Schedule C Part III).
- Line 7 = line 3, except daycare not used exclusively (line 6 × line 3) or the special three-step daycare computation.

### Part II (lines 8–36)

- **Line 8** = Schedule C line 29 + gain from business use of the home − business losses not from the home's use. With another business location, allocate gross income to the home first.
- **Lines 9–11** only for itemizers (plus net qualified disaster losses for standard-deduction filers). Mortgage interest is never column (a), even for a separate structure.
- **Line 11**: total SALT ≤ $10,000 ($5,000 MFS) → all real estate taxes in column (b). Otherwise the Line 11 Worksheet: its line 10 in column (a) of line 11, its line 11 in column (a) of line 17. The 2025 worksheet uses the $40,000 ($20,000 MFS) overall limit, reduced above $500,000 ($250,000 MFS) of MAGI but not below $10,000 ($5,000 MFS).
- **Line 15** = line 8 − line 14, not below zero. It caps Tiers 2 and 3.
- **Lines 16–17**: standard-deduction filers put all acquisition mortgage interest and all real estate taxes here; itemizers only the Schedule A-disallowed excess.
- **Lines 18–22**: insurance (current-year coverage only), rent, repairs (not improvements), utilities, other home operating expenses.
- **Line 25 / line 31**: prior-year carryovers, from the last Form 8829 or the Simplified Method Worksheet lines 6a/6b.
- **Line 27** = smaller of line 15 or line 26. **Line 33** = smaller of line 28 or line 32. Depreciation is absorbed last.
- **Line 35** casualty portion → Form 4684 line 27 ("See Form 8829"). **Line 36** → Schedule C line 30; allocate among businesses using the same home.

### Expense routing table

| Expense the user reports | Form 8829 line and column | Not here |
|---|---|---|
| Rent for the home | 19(b) | Office rent elsewhere → Schedule C line 20b |
| Mortgage interest, itemizer | 10(b) (deductible amount); 16(b) only the Schedule A-disallowed excess on acquisition debt | Home equity interest not used for the home |
| Mortgage interest, standard deduction | 16(b) | Lines 10, 11 |
| Real estate taxes | 11(b), or Line 11 Worksheet → 11(a) and 17(a), or 17(b) for standard deduction | Schedule A line 5b for the business share |
| Homeowner's or renter's insurance | 18(b), current-year coverage only | Business liability insurance → Schedule C line 15 |
| Electricity, gas, water, trash, cleaning service | 21(b); a separately estimated business part → 21(a) only | Second business phone line, business long-distance → Schedule C line 25 |
| Painting or repair of the office only | 20(a) (× line 6 for daycare not used exclusively) | Improvements → Part III statement |
| Whole-home repair (furnace, roof patch) | 20(b) | Roof replacement, new HVAC → depreciation |
| Security system maintenance and monitoring (Pub. 587), pest control | 22(b) | |
| Casualty loss, federally declared disaster, itemizer | 9(b) via worksheet Form 4684; excess on 29 | |
| Office furniture, computer, printer | Not on Form 8829 | Form 4562 / Schedule C line 13 or 22 |
| Food for daycare children | Not on Form 8829 | Schedule C |

When the user cannot say whether an item is direct or indirect, ask: "Did this cost benefit only the business room, or the whole home?" When the user cannot say whether it was a repair or an improvement, ask what was done and whether it replaced a major component; improvements are never entered on lines 18–22.

### Part III (lines 37–42)

- Lines 37–38 fixed at the first-business-use date: smaller of adjusted basis or FMV (with land); land at the smaller of its basis or FMV.
- Line 41: 2025 first use → month table (January 2.461% … December 0.107%); after May 12, 1993 and before 2025 → 2.564%; other cases → Pub. 946 / Pub. 534.
- Line 42 → line 30. Improvements after business use began: separate statement, included in line 42.

### Part IV (lines 43–44)

- Carry to next year's lines 25 and 31, subject to that year's limit even in a different home.

---

## Validation

Run every check. Report each failure in the validation summary; do not change user data to make a check pass.

### Math checks

- [ ] Line 3 = line 1 ÷ line 2; line 7 = line 3, or line 6 × line 3 for daycare not used exclusively
- [ ] Line 6 = line 4 ÷ line 5; line 5 = 8,760 or 24 × days available
- [ ] Line 12 = lines 9 + 10 + 11 per column; line 13 = line 12(b) × line 7; line 14 = line 12(a) + line 13
- [ ] Line 15 = max(0, line 8 − line 14)
- [ ] Line 23 = lines 16–22 per column; line 24 = line 23(b) × line 7; line 26 = line 23(a) + line 24 + line 25
- [ ] Line 27 = min(line 15, line 26); line 28 = line 15 − line 27
- [ ] Line 32 = lines 29 + 30 + 31; line 33 = min(line 28, line 32)
- [ ] Line 34 = lines 14 + 27 + 33; line 36 = line 34 − line 35
- [ ] Line 39 = line 37 − line 38; line 40 = line 39 × line 7; line 42 = line 40 × line 41 (+ improvements statement); line 30 = line 42
- [ ] Line 43 = max(0, line 26 − line 27); line 44 = max(0, line 32 − line 33)
- [ ] Line 11 Worksheet: lines 5, 6, 7a, 8, 9, 10, 11 recomputed

### Sanity checks (warn, do not block)

- [ ] Line 7 above 50% for an office in a residence → confirm measurements and exclusivity
- [ ] Line 37 equals the purchase price exactly → confirm FMV comparison and pre-use improvements
- [ ] Line 38 is zero for an owned home → land missing
- [ ] Line 41 = 2.564% with first use in 2025, or a month rate with first use before 2025
- [ ] Any line 9–22 item also appears elsewhere on Schedule C (utilities, insurance, phone) → double count
- [ ] Mortgage interest or real estate taxes on lines 10–11 for a standard-deduction filer, or full amounts also on Schedule A
- [ ] Full-year expenses with part-year business use
- [ ] Lines 25/31 zero although the user filed Form 8829 before → ask for the last lines 43/44
- [ ] Line 36 plus other Schedule C expenses produce a loss larger than the Tier 1 amount → Tier 2/3 cap broken
- [ ] Owner with no depreciation claimed in prior years → explain allowed-or-allowable and refer to a CPA
- [ ] MAGI near $500,000 ($250,000 MFS) with the Line 11 Worksheet → iteration needed; flag CPA review

### Cross-form checks

- [ ] Schedule C line 30 = line 36 (or this business's allocated share); square-footage spaces on Schedule C line 30 left blank
- [ ] Form 4562 line 19j filled when first use or improvements fall in the tax year; not on Schedule C line 13
- [ ] Schedule A shows only the personal share of mortgage interest and real estate taxes (line 5b excludes Line 11 Worksheet line 6)
- [ ] Form 4684 line 27 equals line 35 when nonzero
- [ ] Schedule SE uses Schedule C line 31 after line 30

---

## Output format

Deliver this markdown draft. Every line appears with its number, including zeros and N/A.

```markdown
# Form 8829 — DRAFT for tax year YYYY (home: <address or "main home">)

Revision used: 2025 Form 8829 (Created 10/2/25); Instructions dated Mar 4, 2026
Rounding: percentages 2 decimals, line 6 4 decimals, whole dollars

## Qualification (user's answers)
- Filer: Schedule C, <business>; not an employee/partner/Schedule F use
- Exclusive and regular use: <answer>
- Qualifying purpose: principal place of business | client meetings | separate structure | inventory storage | daycare (license: <status>)
- Period of business use: <dates>

## Part I
1. Business area: <n>          2. Total area: <n>          3. <x.xx>%
4. Daycare hours: <n | N/A>    5. Hours available: <n | N/A>   6. <.xxxx | N/A>
7. Business percentage: <x.xx>%

## Part II                                   (a) Direct   (b) Indirect
8.  Line 8 amount:                                           $X
9.  Casualty losses:                         $X           $X
10. Deductible mortgage interest:            $X           $X
11. Real estate taxes:                       $X           $X
12. Lines 9–11:                              $X           $X
13. Line 12(b) × line 7:                                     $X
14. Line 12(a) + line 13:                                    $X
15. Line 8 − line 14:                                        $X
16. Excess mortgage interest:                $X           $X
17. Excess real estate taxes:                $X           $X
18. Insurance:                               $X           $X
19. Rent:                                    $X           $X
20. Repairs and maintenance:                 $X           $X
21. Utilities:                               $X           $X
22. Other expenses (list):                   $X           $X
23. Lines 16–22:                             $X           $X
24. Line 23(b) × line 7:                                     $X
25. Prior-year operating carryover:                          $X
26. Line 23(a) + 24 + 25:                                    $X
27. Allowable operating expenses:                            $X
28. Line 15 − line 27:                                       $X
29. Excess casualty losses:                                  $X
30. Depreciation (line 42):                                  $X
31. Prior-year casualty/depreciation carryover:              $X
32. Lines 29–31:                                             $X
33. Allowable excess casualty/depreciation:                  $X
34. Lines 14 + 27 + 33:                                      $X
35. Casualty portion → Form 4684 line 27:                    $X
36. Allowable expenses → Schedule C line 30:                 $X

## Part III (owners; "N/A — renter" otherwise)
37. Smaller of adjusted basis or FMV:  $X   (basis $X; FMV $X on MM/YYYY)
38. Land:                              $X
39. Building basis:                    $X
40. Business basis:                    $X
41. Depreciation percentage:           x.xxx%
42. Depreciation allowable:            $X   (+ improvements statement $X)

## Part IV
43. Operating expense carryover to next year:        $X
44. Casualty/depreciation carryover to next year:    $X

## Line 11 Worksheet (if used): lines 1–11 with amounts

## Method comparison
| | Simplified | Form 8829 |
| Schedule C line 30 | $X | $X |
| Tier 1 items | Schedule A / not deductible | Schedule C |
| Home depreciation | none | $X |
| Carryovers | frozen | lines 43–44 |

## Hand-offs
- Schedule C line 30: $X
- Schedule A personal share: mortgage interest $X; real estate taxes (line 5b) $X
- Form 4562 line 19j: (b) MM/YYYY (c) $X (g) $X | not required
- Form 4684 line 27: $X | none
- Sale note (owners): depreciation allowed or allowable after May 6, 1997 is not excludable under §121 and is taxed as unrecaptured section 1250 gain when the home is sold

## Validation summary
- Math: all checks passed | <failures>
- Sanity: <warnings>
- Open questions for the user or CPA: <list>

## Sources cited in this draft
- 2025 Form 8829 and 2025 Instructions for Form 8829 (sections used)
- Pub. 587 (2025) sections used
- 2025 Instructions for Schedule C, Line 30 / Simplified Method Worksheet
- IRC §280A(c)(1), (c)(4), (c)(5) as applicable; IRC §67(h) if the employee rule was explained
```

The draft is not a filed form. Remind the user that complex facts (mixed employee and business use of a room, iteration near the SALT phase-down, missed depreciation, a home sale) need a licensed tax professional's review.

---

## References

- [references/line-by-line.md](./references/line-by-line.md) — every Form 8829 line (1–44), the Line 11 Worksheet, the line 41 table, who cannot use the form
- [references/qualification-tests.md](./references/qualification-tests.md) — employee/partner/farmer gate, exclusive and regular use, principal place of business, client meetings, separate structure, inventory storage, daycare time-use computation
- [references/limits-and-carryovers.md](./references/limits-and-carryovers.md) — the three tiers, itemizer vs standard deduction placement, the Pub. 587 limit example, carryovers, simplified method rules and the comparison table
- [references/home-depreciation.md](./references/home-depreciation.md) — Part III inputs, basis rules, 39-year mid-month percentages, improvements, Form 4562 line 19j, allowed or allowable, sale boundary
- [references/common-mistakes.md](./references/common-mistakes.md) — 17 mistakes with detection and fix
- [filing.md](./filing.md) — channel decision tree, Free File Fillable Forms, paper assembly and mailing addresses, consent and security rules

## Examples

- [examples/renter-consultant.md](./examples/renter-consultant.md) — renter, full year, no depreciation, simplified comparison
- [examples/homeowner-income-limit.md](./examples/homeowner-income-limit.md) — owner who itemizes, Line 11 Worksheet, prior-year carryovers, income limit binds, depreciation carryover
- [examples/daycare-provider.md](./examples/daycare-provider.md) — licensed daycare started mid-year, time-use percentage, prorated line 5, first-year March depreciation and Form 4562 line 19j

---

## Sources

Re-verify each source for the tax year being prepared; the IRS revises the form, instructions, and Pub. 587 every year.

- [Form 8829 Instructions: Home Office Deduction Guide 2026](https://jupid.com/blog/form-8829-instructions-guide-2026) — companion guide for human readers
- [Form 8829 (2025)](https://www.irs.gov/pub/irs-pdf/f8829.pdf) — Created 10/2/25
- [Instructions for Form 8829 (2025)](https://www.irs.gov/pub/irs-pdf/i8829.pdf) — dated Mar 4, 2026
- [About Form 8829](https://www.irs.gov/forms-pubs/about-form-8829) — check for the next revision
- [Publication 587 (2025), Business Use of Your Home](https://www.irs.gov/publications/p587) — dated Feb 27, 2026
- [Instructions for Schedule C (2025)](https://www.irs.gov/pub/irs-pdf/i1040sc.pdf) — Line 30, Simplified Method Worksheet
- [Form 4562 (2025)](https://www.irs.gov/pub/irs-pdf/f4562.pdf) — line 19j, nonresidential real property
- [Publication 523 (2025), Selling Your Home](https://www.irs.gov/publications/p523) — home office and depreciation at sale
- [Publication 946, How To Depreciate Property](https://www.irs.gov/publications/p946) — MACRS tables for older or interrupted use
- [Publication 936, Home Mortgage Interest Deduction](https://www.irs.gov/publications/p936) — limits applied on line 10
- [Rev. Proc. 2013-13](https://www.irs.gov/irb/2013-06_IRB) — simplified method
- [IRC §280A](https://www.law.cornell.edu/uscode/text/26/280A) — business use of home; (c)(1) qualifying uses, (c)(2) storage, (c)(4) daycare, (c)(5) income limit
- [IRC §67](https://www.law.cornell.edu/uscode/text/26/67) — §67(h): no miscellaneous itemized deductions for tax years beginning after 2017, as amended by P.L. 119-21 §70110
- IRC §1(h)(1)(E) — 25% maximum rate on unrecaptured section 1250 gain; IRC §121 — home sale exclusion
- [2025 Instructions for Form 1040](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — "Where Do You File?" addresses used in filing.md

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions, and publications. It is not tax advice and does not create a CPA-client relationship. When producing a draft, the agent reminds the user that it is a starting point and that a licensed tax professional should review complex situations.
