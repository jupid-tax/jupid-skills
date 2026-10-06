# Example: Distributor With 65% and 50% Dividends and the Section 246(b) Limit

A calendar-year 2025 Form 1120 for a closely held wholesale distributor in a weak operating year. It received dividends from a 25%-owned domestic corporation and from a brokerage portfolio, so Schedule C and the taxable-income limit decide the deduction. It also shows tax-exempt interest, a Form 4466 quick refund, dividends paid to shareholders, and full Schedules L, M-1, and M-2. All arithmetic was checked in Python before writing.

---

## The corporation

- **Name:** Harbor Point Marine Supply, Inc. (Ohio corporation, incorporated 1998), principal office Toledo, Ohio
- **Tax year:** calendar 2025, accrual method, inventory on Form 1125-A
- **Shareholders (2):** Tomas Reyes 50%, Mateo Reyes 50%, both officers
- **Investments:** 25% of Lakeshore Coatings, Inc. (domestic C corporation, held since 2014, not debt-financed); a brokerage account of listed stocks and a REIT; Ohio municipal bonds

## Facts the agent asked for, and the answers

| Question | User's answer |
|----------|---------------|
| Officer W-2 wages? | Tomas $93,000, Mateo $93,000 (payroll reports) |
| Ownership of each dividend payer, by vote and by value? | Lakeshore Coatings: 25% vote and 25% value. Brokerage holdings: each under 1%. |
| Holding period on brokerage dividends? | $1,104 of dividends came from shares bought and sold within a 3-week window around the ex-dividend dates; the other $8,214 met the 46-day test. |
| Any debt used to buy the stock? | No |
| Other dividends? | $1,480 from a REIT |
| Tax-exempt interest? | $2,210 from Ohio municipal bonds |
| Prior-year (2024) tax? | $38,416 on a 12-month return; taxable income under $1 million in 2022, 2023, 2024 |
| Estimated payments? | $9,604 on April 15, June 16, September 15, December 15, 2025 |
| Form 4466? | Filed February 2, 2026 for a $30,000 quick refund |
| Distributions? | $60,000 cash dividends, $30,000 to each brother; Forms 1099-DIV issued |
| Controlled group? | The brothers own no other corporations (user confirmed) |

## Schedule C

| Line | (a) Dividends | (b) % | (c) Special deduction |
|------|--------------:|------:|----------------------:|
| 1 Less-than-20%-owned domestic (portfolio, holding period met) | 8,214 | 50 | 4,107 |
| 2 20%-or-more-owned domestic (Lakeshore Coatings) | 48,600 | 65 | 31,590 |
| 3–8 | 0 | | 0 |
| 9 Subtotal (column (c) limited by the worksheet) | 56,814 | | 33,760 |
| 10–19 | 0 | | 0 |
| 20 Other dividends ($1,104 failed holding period + $1,480 REIT) | 2,584 | | |
| 21, 22 | | | 0 |
| 23 Total dividends → page 1 line 4 | 59,398 | | |
| 24 Total special deductions → page 1 line 29b | | | 33,760 |

### Section 246(b) limit

- Unlimited column (c): $4,107 + $31,590 = $35,697.
- NOL-year exception test: line 28 $52,940 − $35,697 = $17,243. Not a loss, so the limit applies.
- Worksheet: line 1 = 52,940; 2 = 0; 3 = 52,940; 4 = 65% × 52,940 = 34,411; 5 = 31,590; 6 = 0; 7 = 31,590; 8 = 34,411 − 31,590 = 2,821, which is zero or more, so line 8 = 31,590 (the line 5 amount) and lines 9–15 are skipped.
- Line 16 = 48,600; 17 = 52,940 − 48,600 = 4,340; 18 = 2,170; 19 = 4,107; 20 = 0 + 4,107 = 4,107; 21 = 2,170 − 4,107 = −1,937, below zero, so continue.
- Line 22 = 4,107 ÷ 4,107 = 1.000; 23 = 4,107 − 2,170 = 1,937; 24 = 1,937; 25 = 4,107 − 1,937 = 2,170; 26 = 0.000; 27 = 0; 28 = 0.
- Line 29 = 31,590 + 2,170 = **33,760** → Schedule C line 9 column (c). The 65% deduction survives in full; the 50% deduction is cut from $4,107 to $2,170, because taxable income after the Lakeshore dividends is only $4,340.

## Page 1

| Line | Description | Amount |
|------|-------------|-------:|
| 1a | Gross receipts or sales | 3,318,745 |
| 1b | Returns and allowances | 41,920 |
| 1c | Balance | 3,276,825 |
| 2 | Cost of goods sold (Form 1125-A) | 2,276,550 |
| 3 | Gross profit | 1,000,275 |
| 4 | Dividends and inclusions (Schedule C line 23) | 59,398 |
| 5 | Interest (taxable bank and money market) | 6,905 |
| 6–10 | Rents, royalties, capital gains, Form 4797, other | 0 |
| 11 | Total income | 1,066,578 |
| 12 | Compensation of officers (Form 1125-E) | 186,000 |
| 13 | Salaries and wages | 301,448 |
| 14 | Repairs and maintenance | 12,930 |
| 15 | Bad debts | 4,775 |
| 16 | Rents (warehouse) | 84,000 |
| 17 | Taxes and licenses (payroll taxes, Ohio CAT, property tax) | 67,412 |
| 18 | Interest (mortgage and line of credit; small business taxpayer, no Form 8990) | 21,664 |
| 19 | Charitable contributions | 0 |
| 20 | Depreciation (Form 4562: 100% special allowance on $41,800 pallet racking acquired April 2025, plus $17,100 MACRS) | 58,900 |
| 21 | Depletion | 0 |
| 22 | Advertising | 31,205 |
| 23 | Pension, profit-sharing | 18,320 |
| 24 | Employee benefit programs | 46,118 |
| 25 | Energy efficient commercial buildings deduction | 0 |
| 26 | Other deductions (statement) | 180,866 |
| 27 | Total deductions | 1,013,638 |
| 28 | Taxable income before NOL and special deductions | 52,940 |
| 29a | NOL deduction | 0 |
| 29b | Special deductions (Schedule C line 24) | 33,760 |
| 29c | Add 29a and 29b | 33,760 |
| 30 | Taxable income | 19,180 |
| 31 | Total tax (Schedule J line 12) | 4,028 |
| 32 | Section 1062 first installment | 0 |
| 33 | Total payments (Schedule J line 23) | 8,416 |
| 34 | Estimated tax penalty | 0 |
| 35 | Amount owed | 0 |
| 36 | Overpayment | 4,388 |
| 37a | Credited to 2026 estimated tax | 2,000 |
| 37b | Refunded | 2,388 |

**Line 26 statement:** freight-out and delivery 52,360; insurance 38,412; legal and professional fees 21,950; supplies 11,204; utilities 16,890; bank and card processing fees 27,531; travel 6,420; meals (50% deductible portion) 3,412; dues and subscriptions 2,687. Total 180,866.

**Form 1125-E:** total receipts $3,385,048 (line 1a $3,318,745 + line 4 $59,398 + line 5 $6,905). Two officers at $93,000; line 4 = $186,000.

## Schedule J

1a $19,180 × 21% = $4,027.80 → 4,028 · 1b–1z 0 · 2 4,028 · 3 0 · 4 4,028 · 5a–5f 0 · 6 0 · 7 4,028 · 8 0 · 9a–9z 0 · 10 0 · 11a 4,028 · 11b 0 · 11c 0 · **12 4,028** · 13 0 · 14 38,416 · 15 (30,000) · 17 0 · 18 0 · **19 8,416** · 20a–20z 0 · 21 0 · 22a 0 · 22b 0 · **23 8,416**.

**Form 4466 check:** overpayment of estimated tax $38,416 − $4,028 = $34,388, which is at least 10% of the expected $4,028 liability ($402.80) and at least $500, and Form 4466 was filed after year end and before the return. The $30,000 refund goes on Schedule J line 15 in parentheses.

**Estimated tax penalty check:** Method 2 is available (2024 return, 12 months, $38,416 tax; not a large corporation). Each $9,604 payment equals 25% of $38,416 and was on time. Line 34 = 0.

## Schedule K (answers that matter)

1 accrual · 3 No · 4a No · 4b **Yes** (each brother 50%) → Schedule G Part II · 5a **Yes**: Lakeshore Coatings, Inc., its EIN, United States, 25% · 5b No · 6 No · 7 No · **9 $2,210** · 10: 2 shareholders · 12 $0 · 13 **No** · 14 No · 15a Yes · 15b Yes · 16–23 No · 24 No (average gross receipts under $31 million) · 25–27 No · 28 No (user confirmed) · 29a No → 29c Yes · 30, 31 No.

## Schedule L (per books)

| Line | Beginning (b) | End (d) |
|------|--------------:|--------:|
| 1 Cash | 308,645 | 254,578 |
| 2a/2b Receivables less allowance | 402,118 − 8,000 = 394,118 | 371,604 − 8,000 = 363,604 |
| 3 Inventories | 611,904 | 648,337 |
| 5 Tax-exempt securities (Ohio municipal bonds) | 95,000 | 95,000 |
| 6 Other current assets (end includes $4,388 federal tax overpayment receivable) | 34,000 | 36,148 |
| 9 Other investments (Lakeshore Coatings at cost $126,000; brokerage $142,600) | 268,600 | 268,600 |
| 10a/10b Depreciable assets less accumulated depreciation | 448,230 − 261,540 = 186,690 | 490,030 − 283,980 = 206,050 |
| 15 Total assets | 1,898,957 | 1,872,317 |
| 16 Accounts payable | 228,411 | 241,906 |
| 17 Notes payable in less than 1 year | 60,000 | 60,000 |
| 18 Other current liabilities | 71,220 | 66,915 |
| 20 Mortgage payable in 1 year or more | 305,000 | 245,000 |
| 22b Common stock | 10,000 | 10,000 |
| 23 Additional paid-in capital | 40,000 | 40,000 |
| 25 Retained earnings, unappropriated | 1,184,326 | 1,208,496 |
| 28 Total liabilities and equity | 1,898,957 | 1,872,317 |

Item D = $1,872,317. The Lakeshore investment is carried at cost on the books, so book dividend income equals tax dividend income and no M-1 adjustment arises from it.

## Schedule M-1

| Line | Amount |
|------|-------:|
| 1 Net income per books | 84,170 |
| 2 Federal income tax per books | 4,028 |
| 3, 4, 5a, 5b | 0 |
| 5c Nondeductible meals | 3,412 |
| 6 | 91,610 |
| 7 Tax-exempt interest | 2,210 |
| 8a Depreciation: tax $58,900 − book $22,440 | 36,460 |
| 9 | 38,670 |
| 10 Income (page 1 line 28) | 52,940 |

## Schedule M-2

1 Beginning 1,184,326 · 2 Net income per books 84,170 · 3 0 · 4 1,268,496 · 5a Cash distributions 60,000 · 5b 0 · 5c 0 · 6 0 · 7 60,000 · 8 Ending 1,208,496 = Schedule L line 25 column (d).

## Validation summary

- Math: Schedule C line 23 = page 1 line 4; Schedule C line 24 = page 1 line 29b; worksheet line 29 = Schedule C line 9 column (c); J12 = 31; J19 = 14 − 15; J23 = 33; 36 = 37a + 37b; L15 = L28; item D = L15(d); M-1 line 10 = line 28; M-2 line 8 = L25(d); question 9 = M-1 line 7. All pass.
- Sanity: the $60,000 of dividends paid sits only on M-2 line 5a, not on page 1; REIT and short-held dividends are on line 20 with no deduction.
- Cross-form: Forms 1099-DIV ($30,000 each) issued; officer wages tie to Forms 941 and W-3.
- Filing: the corporation was required to file well over 10 returns in calendar 2025 (Forms 941, 940, W-2, 1099, its 2024 Form 1120), so e-file is mandatory. Due April 15, 2026.

## 2026 estimated tax handoff

Method 2 for 2026: 25% × $4,028 = $1,007 per installment, due April 15, June 15, September 15, and December 15, 2026, less the $2,000 line 37a credit applied to the first installment(s). Ask the user for the 2026 profit outlook; if 2026 tax will be higher, Method 2 still protects against the penalty because Harbor Point is not a large corporation.

Sources: Form 1120 (2025) pages 1–6; Instructions for Form 1120 (2025), Schedule C and the Worksheet for Schedule C, Lines 9 and 22, Schedule J line 15, Schedule K questions 5a and 9, Schedules L, M-1; Pub. 542 (Rev. January 2024); IRC §§ 243, 246(b), 246(c), 6655.
