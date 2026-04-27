# Example: Freelance Graphic Designer (Service Business, Home Office)

A complete walkthrough of Schedule C for a service business with no inventory, a small home office, and occasional client travel. This is the canonical "knowledge worker freelancer" pattern.

## The filer

- **Name**: Maya Lopez
- **Business**: Freelance graphic design (logos, brand identity, web mockups)
- **Entity**: Single-member LLC formed in California, taxed as a disregarded entity
- **First Schedule C year**: No (third year)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Income

| Source | Type | Amount |
|--------|------|--------|
| Acme Brand (largest client) | 1099-NEC | $42,000 |
| Other agency clients (5 total) | 1099-NEC | $16,400 |
| Stripe direct invoices | 1099-K | $24,300 |
| Two cash payments from local clients | cash | $1,800 |
| **Line 1 Gross receipts** | | **$84,500** |

No returns or refunds. Line 2 = $0. Line 3 = $84,500. Service business → Line 4 = $0, Line 5 = $84,500. Maya earned $35 in business savings account interest. Line 6 = $35. **Line 7 = $84,535**.

### Expenses

Maya's bookkeeping app exported these transactions for the year. Each has been mapped to a Schedule C line:

| Original transaction | Mapped to | Amount |
|---------------------|-----------|--------|
| Google Ads + Meta Ads | Line 8 (Advertising) | $2,400 |
| 1,800 business miles × $0.70 | Line 9 (Car & truck) | $1,260 |
| Stripe processing fees (2.9% of $84,500) | Line 10 (Commissions/fees) | $2,452 |
| Subcontracted illustrator (one project) | Line 11 (Contract labor) | $1,800 |
| Section 179: new $2,200 laptop | Line 13 (Depreciation) via Form 4562 | $2,200 |
| Professional liability insurance | Line 15 (Insurance) | $720 |
| Business credit card interest | Line 16b (Interest, other) | $180 |
| CPA + Jupid subscription | Line 17 (Legal & professional) | $640 |
| Printer ink, paper, USB drives | Line 18 (Office expense) | $310 |
| Wacom tablet, color-calibration tools (each <$2,500) | Line 22 (Supplies) | $1,440 |
| DBA filing renewal | Line 23 (Taxes & licenses) | $95 |
| Conference travel: flight + hotel for one out-of-state client visit | Line 24a (Travel) | $1,250 |
| Client lunches × 50% | Line 24b (Meals) | $385 |
| Adobe CC, Figma, Notion, ChatGPT (each itemized in Part V) | Line 27a (Other expenses) | $1,820 |

### Home office

- 120 sq ft dedicated office in a 1,400 sq ft apartment (renter)
- Used exclusively and regularly
- Maya picks **simplified method** for record-keeping ease
- Calculation: 120 × $5 = $600

### Vehicle (Part IV details)

- Maya's car was first used for business on January 8, 2025 (start of tax year)
- 2,400 total miles for the year
  - 1,800 business
  - 0 commuting (Maya works from home)
  - 600 personal
- She has a separate vehicle her partner uses
- She kept a contemporaneous log via her phone calendar

## The Form 4562 entry (Line 13)

Maya bought a $2,200 MacBook Pro on March 14, 2025. She uses it 100% for design work. She elects §179 on Form 4562:

- Form 4562 Part I, Line 6: $2,200 (cost) × 100% (business use) = $2,200
- Section 179 within annual limit ($1,250,000 for 2025)
- Form 4562 Line 12 (carryover) = $0; Line 13 → flows to Schedule C Line 13

Her Section 179 is well within her business income, so no carryover.

## The completed Schedule C draft

```markdown
# Schedule C — DRAFT for tax year 2025

## Header
A. Principal business: Freelance graphic design
B. Business code: 541430 (Graphic design services)
C. Business name: Maya Lopez Design LLC
D. EIN: 87-XXXXXXX
E. Address: Same as Form 1040
F. Accounting method: Cash
G. Material participation: Yes
H. Started this year: No
I. Paid any individual $600+: Yes (subcontracted illustrator)
J. Will file required 1099-NEC: Yes

## Part I — Income
1.  Gross receipts:                $84,500
2.  Returns and allowances:        $0
3.  Subtract line 2 from 1:        $84,500
4.  Cost of goods sold:            $0       (service business; no Part III)
5.  Gross profit:                  $84,500
6.  Other income:                  $35      (business savings interest)
7.  Gross income:                  $84,535

## Part II — Expenses
 8. Advertising:                   $2,400
 9. Car and truck:                 $1,260   (1,800 mi × $0.70 — see Part IV)
10. Commissions and fees:          $2,452   (Stripe 2.9%)
11. Contract labor:                $1,800   (illustrator subcontractor)
12. Depletion:                     $0
13. Depreciation + §179:           $2,200   (laptop, Form 4562 attached)
14. Employee benefit programs:     $0
15. Insurance (other than health): $720     (professional liability)
16a. Mortgage interest:            $0
16b. Other interest:               $180
17. Legal and professional:        $640
18. Office expense:                $310
19. Pension/profit-sharing:        $0
20a. Rent (vehicles, machinery):   $0
20b. Rent (other):                 $0
21. Repairs and maintenance:       $0
22. Supplies:                      $1,440
23. Taxes and licenses:            $95
24a. Travel:                       $1,250
24b. Deductible meals (50%):       $385
25. Utilities:                     $0       (home office, captured in Line 30)
26. Wages:                         $0
27a. Other expenses (Part V):      $1,820
28. Total expenses:                $16,952

## Part II totals
29. Tentative profit:              $67,583
30. Home office (simplified):      $600     (120 sq ft × $5)
31. Net profit:                    $66,983

## Part III — COGS
   N/A (service business)

## Part IV — Vehicle
43. Date placed in service:        01/08/2025
44a. Business miles:               1,800
44b. Commuting miles:              0
44c. Other miles:                  600
45. Available for personal use:    Yes
46. Another vehicle available:     Yes (partner's vehicle)
47a. Have evidence:                Yes (contemporaneous log)
47b. Written:                      Yes (phone calendar entries)

## Part V — Other Expenses (detail of Line 27a)
| Description                              | Amount  |
|-------------------------------------------|---------|
| Adobe Creative Cloud (annual)             | $720    |
| Figma Pro (annual)                        | $144    |
| Notion (annual)                           | $96     |
| ChatGPT Plus + Claude Pro                 | $480    |
| iCloud + Google One storage (business %)  | $144    |
| Industry publications (Communication Arts)| $96     |
| Bank service charges                      | $140    |
| **Total (Line 48 = Line 27a)**            | $1,820  |

## Required attachments
- [x] Form 4562 (Line 13 = $2,200)
- [ ] Form 8829 — Not required; using simplified home office method
- [x] Schedule SE — required (profit > $400)

## Validation summary
- Math: all checks passed
- Sanity:
  - Expense ratio: 20% — typical for service business solo
  - Line 27a ratio: 11% of total expenses — within normal range
  - Business mileage 1,800 — modest; consistent with Maya's work-from-home setup
- Next steps:
  - File Schedule SE: 92.35% × $66,983 = $61,860 net earnings × 15.3% ≈ $9,464 SE tax
  - Half of SE tax ($4,732) deductible on Schedule 1 Line 15
  - Maya should pay quarterly estimated taxes on Form 1040-ES going forward
  - Adjust 2026 quarterly estimates upward given the income trajectory

## Sources cited in this draft
- IRS Form 1040 Schedule C, Rev. 2025
- IRS Instructions for Schedule C, Rev. 2025
- IRC §162 (ordinary and necessary business expenses)
- IRC §179 + Rev. Proc. 2024-40 (2025 §179 limit $1.25M)
- Notice 2025-5 (2025 standard mileage rate 70¢)
```

## Why each non-obvious choice

**Why simplified home office instead of Form 8829?** Maya rents (no depreciation recapture concern), the office is small (120 sq ft × $5 = $600 is well under the $1,500 cap), and her actual rent + utilities allocation would only exceed $600 if she did regular method. Simplified saves an entire form and several hours of recordkeeping. Net loss < $200/year — fine trade-off.

**Why §179 the laptop instead of MACRS?** Maya's net profit absorbs the $2,200 deduction this year. §179 gives her the full deduction now. MACRS would spread it over 5+ years; with a 22% federal bracket, she'd save $484 in tax this year vs. ~$96/year over 5 years. Time value of money favors §179.

**Why business code 541430 specifically?** The IRS Schedule C instructions list 541430 for "graphic design services." It's specific, matches what Maya actually does, and the IRS expense benchmarks for that code align with her ratios.

**Why didn't Maya put Stripe fees on Line 8 (Advertising)?** Payment processor fees are a cost of being paid, not a marketing cost. Line 10 (Commissions and fees) is the IRS instruction's specific home for them.

**Why is internet in Line 27a as part of "iCloud + Google One storage" instead of Line 25 Utilities?** Maya works from home. Home office utilities (including internet) are inside Line 30 simplified method calculation by design — the simplified method bundles utilities. If she had a separate non-home office, internet there would go on Line 25.

**What if Maya had been audited?** Her audit defense would be:
1. Income matches all 1099s plus documented cash deposits in her business bank account
2. Mileage log substantiates Line 9
3. Business credit card statements substantiate Lines 8, 10, 18, 22, 27a
4. Subcontractor 1099-NEC filed for Line 11
5. Form 4562 attached for Line 13
6. Home office: dedicated 120 sq ft documented with photos showing it's used exclusively for design work
7. Travel: receipts plus calendar entries showing the client meeting
8. Meals: receipts with notes on date, place, attendees, business purpose
