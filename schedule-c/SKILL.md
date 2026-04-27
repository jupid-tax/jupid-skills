---
name: schedule-c
description: >
  Use this skill when a sole proprietor, single-member LLC owner, freelancer,
  independent contractor, or gig worker (Uber, DoorDash, Etsy, Upwork, etc.)
  needs to fill out IRS Schedule C (Form 1040). Triggers on phrases like
  "fill out schedule c", "schedule c for my business", "where does X go on
  schedule c", "1040 schedule c", "schedule c help", or any request to
  categorize self-employment income and expenses for tax filing. Do NOT use
  for partnerships (Form 1065), S-corps (Form 1120-S), or C-corps (Form 1120).
form: Schedule C (Form 1040)
audience: [solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-04-27
official_form: https://www.irs.gov/pub/irs-pdf/f1040sc.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040sc.pdf
---

# Schedule C (Form 1040) — Profit or Loss From Business

This skill produces an audit-grade draft of Schedule C from the user's income, expenses, and business facts. It walks through the form line by line, applies the IRS rules at each line, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The math is mechanical. The judgment is in *where things go* and *when a rule depends on a fact the user hasn't mentioned*. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Schedule C (Form 1040) Instructions: Complete Line-by-Line Guide 2026](https://jupid.com/blog/schedule-c-instructions-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule C, "1040 schedule c", or "schedule c form"
- The user describes self-employment income: 1099-NEC, 1099-K, freelance income, gig earnings (Uber/Lyft/DoorDash/Instacart/Amazon Flex), Etsy or Shopify revenue, consulting fees, etc.
- The user is a sole proprietor or single-member LLC (treated as a disregarded entity by default) trying to file taxes
- The user asks "where does X go on my taxes" *and* X is a business expense

Do **not** engage this skill when:

- The user is a partner in a partnership → use the (forthcoming) `form-1065` skill
- The user is an S-corp shareholder → use the (forthcoming) `form-1120-s` skill
- The user has formed an LLC and *elected* to be taxed as an S-corp (filed Form 2553) → also `form-1120-s`
- The user is a C-corp owner → use the (forthcoming) `form-1120` skill
- The user is reporting rental real estate income → that goes on Schedule E, not Schedule C (unless they're a real estate dealer)
- The user is a farmer → that goes on Schedule F, not Schedule C

If the user's entity status is ambiguous, ask before proceeding. The most common confusion: a single-member LLC owner who thinks they need a separate business return — they don't, they file Schedule C.

---

## Prerequisites

Before producing anything, the agent must have these eight inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Schedule C for tax year 2025 is filed in 2026; for tax year 2024, in 2025. Numbers (mileage rate, Section 179, de minimis safe harbor) depend on this.
2. **Filer's legal name and SSN/ITIN.** Used in the Schedule C header. Do not invent.
3. **Business name** (if different from filer's name) — Line C
4. **Principal business or profession** — Line A. A short description like "Freelance graphic design", "Rideshare driving", "Online sales of handmade jewelry".
5. **NAICS / business code** — Line B. Six-digit code. If the user doesn't know it, propose 2-3 candidates from [`references/naics-codes.md`](./references/naics-codes.md) and let them pick.
6. **Accounting method** — Line F. Cash or accrual. Default for solo filers is cash; only switch to accrual if the user explicitly says they use it or they have inventory and revenue ≥ $30M (which they don't, given they file Schedule C).
7. **Income data**, structured as: a list of income sources with amounts, source type (1099-NEC, 1099-K, cash, check), and whether returns/refunds were given.
8. **Expense data**, structured as: a list of business expenses with amounts and rough category descriptions. The agent will map descriptions to Schedule C lines using [`references/line-by-line.md`](./references/line-by-line.md).

For the home office deduction (Line 30), additionally ask:
- Does the user have a dedicated, regularly-used home office?
- Square footage of the office?
- Total square footage of the home?
- Will they use the simplified method ($5/sq ft, max 300 sq ft = $1,500) or the regular method (Form 8829)?

For vehicle expenses (Line 9), additionally ask:
- Total business miles driven in the year
- Whether they want to use the standard mileage rate or actual expenses
- Whether they have a contemporaneous mileage log (required to defend the deduction in an audit)

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filing status

Confirm the user is filing as a sole proprietor or disregarded-entity SMLLC. If they describe partners or shareholders, redirect to the right skill.

### Step 2 — Collect and structure the income data

Ask for income broken down by source. Produce this internal table:

```
| Source                     | Type    | Amount   |
|----------------------------|---------|----------|
| Acme Corp invoices         | 1099-NEC| $42,000  |
| Stripe (direct clients)    | 1099-K  | $18,500  |
| Cash payments not on 1099  | cash    | $1,200   |
```

Sum becomes Line 1 (Gross receipts or sales).

If the user gave returns/refunds separately, that's Line 2. If they didn't mention any, set Line 2 = 0 and confirm.

### Step 3 — Determine if Part III (COGS) applies

Ask: "Does your business sell physical products you make or resell?" If yes, gather inventory data and compute COGS using [`references/cogs.md`](./references/cogs.md). If no, Line 4 = 0 and skip Part III.

For a service business, this saves significant time and removes the largest source of mistakes.

### Step 4 — Map expenses to Schedule C lines

Walk every expense line item from the user's data and assign it to the correct Schedule C line using [`references/line-by-line.md`](./references/line-by-line.md). If an item doesn't fit a labeled line (8-26), it goes to Line 27a (Other Expenses) and gets itemized in Part V.

When you're not sure where an item belongs:
- **Ask the user** with a tight question: "Was the $1,200 Adobe Creative Cloud charge a software subscription you used the whole year? If yes it goes on Line 27a as 'Software subscriptions'."
- **Don't silently guess**. The wrong line can trigger an IRS notice or just look sloppy in an audit.

For mixed-use items (cell phone, internet, vehicle), you must apply the business-use percentage. Ask for the percentage if not given. Don't default to 100% — the IRS expects this to be substantiated.

### Step 5 — Compute Line 13 (Depreciation + Section 179)

If the user bought any business asset over $2,500 this year, it might belong on Line 13:
- Items costing **≤$2,500** can be expensed under the de minimis safe harbor (IRS Reg. §1.263(a)-1(f)). Put them on Line 18 (Office expense), Line 22 (Supplies), or Line 27a depending on type. No Form 4562 needed.
- Items costing **>$2,500** must be depreciated or expensed under Section 179. Both flow through Form 4562 → Line 13.

For Section 179 in tax year 2025, the limit is $1,250,000 (Rev. Proc. 2024-40). For 2026, the limit is set by inflation adjustment — check the most recent Revenue Procedure before filing. Bonus depreciation rates change yearly under the OBBBA / TCJA phase-down; consult [`references/depreciation.md`](./references/depreciation.md) for the year-specific table.

### Step 6 — Compute Line 30 (Home office)

If the user has a qualifying home office:
- **Simplified method**: square footage (capped at 300) × $5. Max deduction $1,500. Calculation goes directly on Line 30.
- **Regular method**: complete Form 8829. The output of Form 8829 goes on Line 30. This is a separate skill (forthcoming `form-8829`); for now, ask the user if they have a Form 8829 calculation already and use that number, or default to simplified.

The home office deduction **cannot create a loss**. If the deduction would push Line 31 (Net profit) below zero, cap it at the amount that brings Line 31 to zero. Carry the unused portion forward (regular method only — simplified method has no carryforward).

### Step 7 — Compute the bottom line

```
Line 7  = Line 5 + Line 6                    (Gross income)
Line 28 = sum of Lines 8 through 27a         (Total expenses)
Line 29 = Line 7 − Line 28                   (Tentative profit/loss)
Line 31 = Line 29 − Line 30                  (Net profit/loss)
```

### Step 8 — Run validation checks

See **Validation** below. Run every check. Don't skip checks even if the math looks clean.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next forms the user will need:

- **Profit > $400** → Schedule SE (self-employment tax) is required
- **Any profit** → flows to Schedule 1 Line 3 → Form 1040
- **Vehicle expenses claimed on Line 9** → Part IV of Schedule C must be completed
- **Section 179 or depreciation on Line 13** → Form 4562 must be attached
- **Home office regular method on Line 30** → Form 8829 must be attached
- **Quarterly estimated tax payments** for next year → Form 1040-ES if profit ≥ ~$5,000

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header (Lines A-J)

- **A** — Plain-English description of what the business does
- **B** — NAICS code; see [`references/naics-codes.md`](./references/naics-codes.md)
- **C** — Business name; blank if filer uses their personal name
- **D** — EIN; blank if the filer uses their SSN
- **E** — Business address; if same as Form 1040 address, leave blank and check the box
- **F** — Cash (default for solo) or Accrual
- **G** — "Yes" if the filer materially participated (for solos this is almost always yes)
- **H** — Check only if this is the first Schedule C for this business
- **I/J** — "Yes" on Line I if the filer paid any contractor $600+; "Yes" on J if they (will) file the required 1099-NEC

### Part I — Income (Lines 1-7)

- **Line 1** — All gross receipts including cash, checks, 1099-NEC totals, 1099-K totals, and any income the filer collected without a 1099. Do *not* exclude income just because no 1099 was issued.
- **Line 2** — Returns and allowances (refunds to customers, allowances for damaged goods)
- **Line 3** — Line 1 minus Line 2
- **Line 4** — Cost of Goods Sold (from Part III, Line 42). Service businesses: 0.
- **Line 5** — Line 3 minus Line 4 (Gross profit)
- **Line 6** — Other income: business interest, scrap sales, recovered bad debts, fuel tax credit
- **Line 7** — Line 5 plus Line 6 (Gross income)

### Part II — Expenses (Lines 8-27)

The agent must map each user expense to exactly one of these lines. Hot lines:

| Line | Category | What goes here | What does NOT go here |
|------|----------|----------------|------------------------|
| 8 | Advertising | Online ads, print ads, business cards, website costs | Customer gifts (use 27a, "Gifts to clients" — capped $25/recipient/year) |
| 9 | Car & truck | Standard mileage × IRS rate, OR actual vehicle expenses × business-use % | Personal commute miles. Lease payments if using standard mileage. |
| 10 | Commissions and fees | Sales commissions, payment processor fees (Stripe 2.9%, Square, PayPal), platform seller fees (Etsy, Amazon) | Contract labor for non-sales work (use Line 11) |
| 11 | Contract labor | Bookkeeper, VA, subcontractor, freelance designer | Sales commissions (use Line 10). Wages to W-2 employees (use Line 26). |
| 13 | Depreciation + Section 179 | Form 4562 total | Items ≤$2,500 (use Line 18, 22, or 27a as applicable) |
| 14 | Employee benefit programs | Health insurance for *employees*, group life, dependent care | Filer's own health insurance (Schedule 1 Line 17, not Schedule C) |
| 15 | Insurance (other than health) | Business liability, E&O, property, business interruption | Vehicle insurance (already in Line 9 actual or mileage). Health insurance for self (Schedule 1). |
| 16a / 16b | Mortgage / other interest | Business mortgage interest / business loan interest, business credit card interest | Personal interest. Vehicle loan interest if using standard mileage. |
| 17 | Legal & professional services | Attorney, CPA, bookkeeping, tax prep (business portion), Jupid subscription, professional consultants | Personal tax prep (not deductible) |
| 18 | Office expense | Paper, pens, printer ink, postage, small office equipment under $2,500 | Computer >$2,500 (use Line 13) |
| 19 | Pension and profit-sharing plans | Plans for *employees* | Filer's own SEP-IRA / solo 401(k) (Schedule 1 Line 16) |
| 20a / 20b | Rent (vehicle/equipment) / Rent (other) | Equipment leases / office space, coworking, storage | Vehicle leases if using standard mileage |
| 21 | Repairs and maintenance | Equipment repairs, computer repair, building maintenance | Improvements that increase asset value (those are depreciated, Line 13) |
| 22 | Supplies | Project materials, cleaning supplies, small tools | Inventory (goes to Part III) |
| 23 | Taxes and licenses | Business licenses, state/local business tax, employer payroll tax, professional license | Federal income tax. Self-employment tax. Personal property tax. |
| 24a | Travel | Flights, hotels, rental cars while away from home overnight for business | Local taxis to a regular workplace (commuting) |
| 24b | Deductible meals (50%) | Client meals, meals during business travel, conference meals | Personal meals. Entertainment (no longer deductible since TCJA). |
| 25 | Utilities | Electric/gas/water/internet for a *separate* business location | Home office utilities (those are inside Line 30 simplified, or Form 8829 if regular) |
| 26 | Wages | Gross W-2 wages | Contractor payments (use Line 11) |
| 27a | Other expenses | Software subscriptions, professional memberships, education, bank fees, business portion of cell/internet | Anything that fits Lines 8-26 |

Line 27a items must be itemized in Part V (Line 48). The agent should produce the Part V breakdown, not just the total.

### Lines 28-32 — Net profit calculation

- **Line 28** = sum of Lines 8 through 27a
- **Line 29** = Line 7 − Line 28
- **Line 30** = Home office (simplified) or Form 8829 result
- **Line 31** = Line 29 − Line 30 (this is the bottom line)
- **Line 32** = If Line 31 is a loss, check 32a if all investment is at risk (most solo filers), 32b otherwise. If 32b, attach Form 6198.

### Part III — Cost of Goods Sold (Lines 33-42)

Only for product businesses. See [`references/cogs.md`](./references/cogs.md). Formula:

```
COGS = Beginning inventory + Purchases + Cost of labor + Materials/supplies + Other costs − Ending inventory
```

### Part IV — Vehicle Information (Lines 43-47)

Required only if Line 9 has a vehicle expense. Don't fill this in if the user used a hired/leased fleet exclusively.

- **Line 43** — Date the vehicle was first used for business (not when purchased; when first used)
- **Line 44a/b/c** — Business / commuting / other miles. The three should sum to the vehicle's total annual miles.
- **Line 45-47** — Yes/no questions about vehicle usage and recordkeeping

The most-flunked question is Line 47b ("Do you have written evidence?"). The user must keep a contemporaneous mileage log. If they don't, they should still answer truthfully — but the deduction becomes very hard to defend in an audit.

### Part V — Other Expenses (Line 48)

Itemized list of everything aggregated into Line 27a. Each row: description + amount. Total at the bottom matches Line 27a.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 3 = Line 1 − Line 2
- [ ] Line 5 = Line 3 − Line 4
- [ ] Line 7 = Line 5 + Line 6
- [ ] Line 28 = sum of Lines 8 through 27a
- [ ] Line 29 = Line 7 − Line 28
- [ ] Line 31 = Line 29 − Line 30
- [ ] Part V (Line 48) total = Line 27a
- [ ] If Part III used: Line 4 = Line 42; Line 40 = Lines 35+36+37+38+39; Line 42 = Line 40 − Line 41
- [ ] If Part IV used: Line 44a + 44b + 44c is plausible (matches odometer if known)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Total expenses (Line 28) > Gross income (Line 7) → indicates a loss; user should be aware of hobby-loss rules (IRC §183) if this is the third loss in five years
- [ ] Line 9 (vehicle) without Part IV completed
- [ ] Line 13 (depreciation) without Form 4562 attached
- [ ] Line 30 regular method without Form 8829 attached
- [ ] Line 27a > 30% of Line 28 → suggests miscategorization; user should review whether items belong on Lines 8-26 instead
- [ ] Line 24b (meals) > Line 24a (travel) by 2× → unusual; user should confirm
- [ ] Section 179 amount > Line 31 (net profit before §179) → §179 deduction is limited to taxable income; excess carries forward
- [ ] Vehicle business-use % is exactly 100% → very rare; user should confirm they have a separate personal vehicle
- [ ] Line 11 (contract labor) > $600 to any single payee with no 1099-NEC filed → trigger reminder about 1099 obligations and Lines I/J

### Cross-form checks

- [ ] If profit > $400, ensure Schedule SE is on the user's to-do list
- [ ] If Section 179 used, ensure user knows about recapture if business use drops below 50% in later years
- [ ] If home office used, confirm user knows about depreciation recapture on the home if sold

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Schedule C or paste into tax software. Format:

```markdown
# Schedule C — DRAFT for tax year YYYY

## Header
A. Principal business: <description>
B. Business code: <NAICS>
C. Business name: <name or blank>
D. EIN: <EIN or "Use SSN">
E. Address: <address or "Same as 1040">
F. Accounting method: Cash | Accrual
G. Material participation: Yes
H. Started this year: Yes | No
I. Paid any individual $600+: Yes | No
J. (If I=Yes) Will file required 1099s: Yes | No

## Part I — Income
1.  Gross receipts:                $X,XXX
2.  Returns and allowances:        $X,XXX
3.  Subtract line 2 from 1:        $X,XXX
4.  Cost of goods sold:            $X,XXX
5.  Gross profit:                  $X,XXX
6.  Other income:                  $X,XXX
7.  Gross income:                  $X,XXX

## Part II — Expenses
 8. Advertising:                   $X,XXX
 9. Car and truck:                 $X,XXX
10. Commissions and fees:          $X,XXX
... (every line, including zeros)
27a. Other expenses (Part V):      $X,XXX
28. Total expenses:                $X,XXX

## Part II totals
29. Tentative profit/loss:         $X,XXX
30. Home office:                   $X,XXX
31. Net profit/loss:               $X,XXX
32. (If loss) At-risk:             32a | 32b

## Part III — COGS  (or "N/A — service business")
35. Beginning inventory:           $X,XXX
36. Purchases:                     $X,XXX
37. Cost of labor:                 $X,XXX
38. Materials and supplies:        $X,XXX
39. Other costs:                   $X,XXX
40. Total:                         $X,XXX
41. Ending inventory:              $X,XXX
42. COGS (= Line 4):               $X,XXX

## Part IV — Vehicle
43. Date placed in service:        MM/DD/YYYY
44a. Business miles:               X,XXX
44b. Commuting miles:              X,XXX
44c. Other miles:                  X,XXX
45. Available for personal use:    Yes
46. Another vehicle available:     Yes | No
47a. Have evidence:                Yes
47b. Written:                      Yes

## Part V — Other Expenses (detail of Line 27a)
| Description                       | Amount  |
|-----------------------------------|---------|
| Software subscriptions            | $X,XXX  |
| Professional memberships          | $X,XXX  |
| ...                               | ...     |
| **Total (Line 48 = Line 27a)**    | $X,XXX  |

## Required attachments
- [ ] Form 4562 (if Line 13 > 0)
- [ ] Form 8829 (if Line 30 used regular method)
- [ ] Schedule SE (if Line 31 > $400)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 1040 Schedule C (revision date YYYY-MM-DD)
- IRS Instructions for Schedule C (revision date YYYY-MM-DD)
- IRC §162, §179, §280A
- Rev. Proc. 2024-40 (Section 179 limit for tax year 2025)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Schedule C. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Schedule C line with examples and edge cases
- [`references/naics-codes.md`](./references/naics-codes.md) — Common NAICS codes for solo / freelance businesses
- [`references/cogs.md`](./references/cogs.md) — Cost of Goods Sold computation for product businesses
- [`references/depreciation.md`](./references/depreciation.md) — Section 179, bonus depreciation, MACRS, year-by-year limits
- [`references/home-office.md`](./references/home-office.md) — Simplified method vs. regular method (Form 8829)
- [`references/vehicle.md`](./references/vehicle.md) — Standard mileage vs. actual expenses, recordkeeping requirements
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 filer mistakes with examples and fixes

## Examples

End-to-end worked Schedule Cs. Use these as patterns when the user's situation is similar.

- [`examples/freelance-designer.md`](./examples/freelance-designer.md) — Service business, no inventory, home office, occasional vehicle
- [`examples/rideshare-driver.md`](./examples/rideshare-driver.md) — Heavy vehicle expenses, multiple platforms, low overhead
- [`examples/ecommerce-seller.md`](./examples/ecommerce-seller.md) — Etsy/Shopify with inventory (Part III), payment processor fees, shipping

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [Schedule C Instructions: Complete Line-by-Line Guide 2026](https://jupid.com/blog/schedule-c-instructions-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1040 Schedule C (latest)](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf) — the form itself
- [Instructions for Schedule C (latest)](https://www.irs.gov/pub/irs-pdf/i1040sc.pdf) — line-by-line IRS guidance
- [About Schedule C (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-c-form-1040) — IRS landing page with archive of past revisions
- [Publication 334](https://www.irs.gov/publications/p334) — Tax Guide for Small Business (Sole Proprietor)
- [Publication 463](https://www.irs.gov/publications/p463) — Travel, Gift, and Car Expenses
- [Publication 535](https://www.irs.gov/publications/p535) — Business Expenses
- [Publication 587](https://www.irs.gov/publications/p587) — Business Use of Your Home
- [Publication 946](https://www.irs.gov/publications/p946) — How to Depreciate Property
- [Standard Mileage Rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) — annual rates
- [Schedule C NAICS Code Lookup](https://www.census.gov/naics/) — Census Bureau NAICS reference
- IRC §162 (trade or business expenses), §179 (Section 179 deduction), §183 (hobby loss), §263A (UNICAP), §280A (business use of home)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025 (Section 179 limit, mileage, etc.)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's review.
