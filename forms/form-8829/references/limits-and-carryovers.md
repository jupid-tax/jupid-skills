# Gross Income Limit, Deduction Ordering, Carryovers, and the Simplified Method

How Form 8829 caps the deduction, in what order expenses absorb the cap, what carries to next year, and how the simplified method interacts with all of it. Sources: 2025 Form 8829 lines 8–36 and 43–44; 2025 Instructions for Form 8829; Pub. 587 (2025), "Deduction Limit" and "Using the Simplified Method"; 2025 Instructions for Schedule C, Line 30 and the Simplified Method Worksheet; Rev. Proc. 2013-13; IRC §280A(c)(5).

## The limit in one sentence

Home expenses that are deductible only because of business use (operating costs, then depreciation) cannot exceed the gross income from the business use of the home minus (1) the business part of expenses deductible anyway (mortgage interest, real estate taxes, qualifying casualty losses) and (2) the business expenses not related to the home. Line 8 already nets out (2) because it starts from Schedule C line 29, which is after all other Schedule C expenses.

## The three tiers, in form order

| Tier | Lines | What | Limited by |
|---|---|---|---|
| 1 | 9–14 | Business share of casualty losses (federally declared disasters), deductible mortgage interest, real estate taxes, for filers who itemize | Not limited by line 8; they reduce the room for Tiers 2 and 3 (line 15 = line 8 − line 14, not below zero) |
| 2 | 16–27 | Operating expenses: excess mortgage interest, excess real estate taxes, insurance, rent, repairs, utilities, other, plus the prior-year operating carryover (line 25) | Line 27 = smaller of line 15 or line 26 |
| 3 | 28–33 | Excess casualty losses, depreciation of the home, plus the prior-year excess casualty/depreciation carryover (line 31) | Line 33 = smaller of line 28 (= line 15 − line 27) or line 32 |

Total deduction: line 34 = line 14 + line 27 + line 33; line 36 = line 34 − line 35 (casualty portion, which goes to Form 4684 line 27).

Consequences the agent must state in the draft:
- Depreciation is absorbed last (Pub. 587: "with depreciation of your home taken last").
- Tier 1 amounts are included in line 34 even when line 15 is zero. That is why Schedule C line 31 can still show a loss after Form 8829 when Tier 1 is large: those amounts would have been deductible on Schedule A anyway.
- Tiers 2 and 3 cannot push Schedule C line 31 below zero (they are capped at line 15).
- Do not count one-half of SE tax as a business expense in this computation (Pub. 587, Deduction Limit).

### Where Tier 1 items go depends on itemizing

| Filer | Mortgage interest | Real estate taxes | Casualty losses |
|---|---|---|---|
| Itemizes on Schedule A | Deductible amount (Pub. 936 limits) on line 10(b); any disallowed interest on acquisition debt on line 16(b) | All on line 11(b) if total SALT ≤ $10,000 ($5,000 MFS); otherwise Line 11 Worksheet: line 10 → line 11(a), line 11 → line 17(a) | Line 9(b) from the worksheet version of Form 4684 (federally declared disaster); excess on line 29 |
| Standard deduction | All acquisition interest on line 16(b) | All on line 17(b) | Line 29 (unless the standard deduction is increased by a net qualified disaster loss: then line 9) |

The standard-deduction filer moves these items into Tier 2, where line 15 limits them. The instructions add a TIP that the filer "may prefer to itemize ... to claim amounts on lines 9, 10, and 11, even if your total personal deductions are less than the standard deduction." Do not choose for the user; show both results if the line 15 limit binds, and say a CPA should confirm.

Personal remainder on Schedule A (itemizers only): mortgage interest = deductible interest − line 13's share of it (i8829 example: business 30% → 70% of line 10(b) on Schedule A); real estate taxes on Schedule A line 5b exclude the business portion, including Line 11 Worksheet line 6. Hand the personal amounts to [../../schedule-a/SKILL.md](../../schedule-a/SKILL.md).

## Pub. 587 deduction-limit example (use as a self-test)

20% business use, itemizer, no SALT or mortgage limits:

```
Gross income from business                                  $6,000
− Mortgage interest and real estate taxes (20%)              3,000
− Business expenses not related to the home                  2,000
= Deduction limit                                           $1,000
− Maintenance, insurance, utilities (20%)                      800
= Room left for depreciation                                   200
Depreciation allowed (20% of $1,600)                           200
Depreciation carryover to next year ($1,600 − $200)         $1,400
```

On Form 8829 terms: line 8 = $4,000 (Schedule C line 29 after the $2,000 of other expenses), line 14 = $3,000, line 15 = $1,000, line 27 = $800, line 28 = $200, line 32 = $1,600, line 33 = $200, line 44 = $1,400.

## Carryovers

- Line 43 (operating) → next year's line 25. Line 44 (excess casualty and depreciation) → next year's line 31.
- The carryover is subject to the next year's limit "whether or not you live in the same home during that year" (i8829, Part IV).
- If the user skipped Form 8829 last year, look for the most recent Form 8829 filed, or line 6a/6b of the Simplified Method Worksheet for a simplified-method year (i8829, Lines 25 and 31). Ask the user for those documents; never assume zero without asking "Did you file Form 8829 in any earlier year? If yes, what is on lines 43 and 44 of the most recent one?"
- Business portion of mortgage interest and real estate taxes not deductible this year carries over to a later actual-expense year (Pub. 587, Where To Deduct).

## The simplified method

Authority: Rev. Proc. 2013-13; Pub. 587 "Using the Simplified Method"; Schedule C instructions Line 30 and the Simplified Method Worksheet.

| Rule | Detail |
|---|---|
| Rate and area | $5 per square foot (Simplified Method Worksheet line 3a), area capped at 300 square feet, so at most $1,500 for one home |
| Where it goes | Schedule C line 30, with the square-footage entry spaces filled; no Form 8829 for that home |
| Gross income limitation | Worksheet line 5 = smaller of the gross income limitation (line 1: Schedule C line 29 + home-use gains − non-home losses) and line 4 (area × rate). Zero or less → zero |
| No carryover from a simplified year | Any excess over the limit is lost; nothing carries |
| Prior actual-expense carryovers | Cannot be used in a simplified year; they stay frozen (worksheet lines 6a and 6b) and resume the next year Form 8829 is used |
| Depreciation | None for the home in a simplified year; allowable depreciation is deemed zero. Later actual-expense years use the MACRS optional table. Depreciation and §179 on furniture and equipment remain available on Form 4562 / Schedule C line 13 |
| Mortgage interest, real estate taxes, casualty losses | Treated as personal; itemizers claim them in full on Schedule A |
| Election | Made by using the method on a timely filed, original return for that year; "an election for a year, once made, is irrevocable." Switching between methods from one year to the next is not a change in accounting method and needs no consent |
| One home per year | If the filer used more than one home in the year, the simplified method applies to only one; others use Form 8829 |
| More than one business in the home | The election covers all qualified uses of that home; 300 square feet total, allocated reasonably |
| Shared home | Each person elects separately but cannot use the same square feet |
| Qualified joint venture | Spouses split the area the way they split other tax attributes |
| Part-year use or area change | Average monthly allowable square footage: sum each month's allowable area (max 300 per month; 0 for a month with fewer than 15 days of qualified use) ÷ 12 (Pub. 587 Examples: 420 sq ft from July 20 → 125; 100 then 330 sq ft → 150) |
| Daycare not used exclusively | Rate reduced to $5 × (hours used for daycare ÷ hours available); worksheet line 3c rounded to two decimals. If at least 300 square feet were used regularly and exclusively for daycare, no reduction |
| Rental use | Simplified method does not apply |

### Choosing a method: what the agent produces

Compute both whenever the user qualifies and has the data, then present:

| Item | Simplified | Form 8829 |
|---|---|---|
| Schedule C line 30 | $5 × allowable sq ft, limited by worksheet line 1 | Form 8829 line 36 |
| Business share of mortgage interest and real estate taxes | Stays on Schedule A (itemizers) or is lost (standard deduction) | Moves to Schedule C (reduces SE tax as well as income tax) |
| Depreciation of the home | None; nothing to recapture for that year | Line 42; reduces basis and is taxed on sale (see [home-depreciation.md](./home-depreciation.md)) |
| Carryover of excess | None | Lines 43–44 |
| Prior-year Form 8829 carryovers | Frozen | Used, subject to the limit |

State the arithmetic; do not recommend. "Which method should I use?" beyond the arithmetic is a CPA question. If the user asks the agent to choose, compute both and ask the user to pick.
