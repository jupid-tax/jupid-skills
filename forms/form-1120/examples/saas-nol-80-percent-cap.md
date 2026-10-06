# Example: SaaS C Corporation Using an NOL Carryforward Under the 80% Cap

A calendar-year 2025 Form 1120 for a venture-backed software company in its first profitable year. Shows the 80% NOL limit, the charitable limit checked both ways, the section 174A transition question, Form 1125-E, Schedules L, M-1, and M-2, and next year's estimated tax. All arithmetic was checked in Python before writing.

---

## The corporation

- **Name:** Larkspur Data Systems, Inc. (Delaware corporation, incorporated March 6, 2023)
- **Principal office:** Austin, Texas
- **Tax year:** calendar 2025, accrual method, no S election
- **Shareholders (4):** Priya Raman 46%, Daniel Okafor 24%, two U.S. individual angel investors 15% each
- **Employees:** 14 W-2 employees plus 2 officers; contractors paid and reported on Forms 1099-NEC

## Facts the agent asked for, and the answers

| Question | User's answer |
|----------|---------------|
| Officer W-2 wages per payroll reports? | Priya Raman (CEO) $168,000; Daniel Okafor (CTO) $144,000. Both full time. |
| NOL carryovers by year? | 2023 loss $258,940; 2024 loss $153,440; none used yet. Both arose after December 31, 2017. |
| Any ownership change of more than 50 percentage points (section 382)? | No. The 2024 seed round sold 30% to the two angels; company counsel confirmed no ownership change. |
| Research costs in 2022–2024 and the Rev. Proc. 2025-28 transition choice? | 2023–2024 domestic research costs were capitalized under former section 174. The CPA chose to keep amortizing the remaining balance; 2025 amortization is $31,624 (Form 4562, Part VI). 2025 domestic research costs are deducted currently under section 174A(a) inside wages and cost of goods sold. |
| Research credit (Form 6765) for 2025? | Not claimed. |
| Charitable contributions? | $4,180 paid in cash to a 501(c)(3) coding school in 2025; acknowledgment letter on file. No carryovers. |
| Estimated tax paid? | $3,100 each on April 15, June 16, September 15, and December 15, 2025 via EFTPS. |
| 2024 return tax? | Zero (loss year). |
| Total assets at year end? | $2,086,164 per the balance sheet. |
| Foreign owners? | None. |
| Returns required in calendar 2025? | 2024 Form 1120, 4 Forms 941, 1 Form 940, 16 Forms W-2, 5 Forms 1099-NEC: e-file is mandatory. |

## Page 1

| Line | Description | Amount |
|------|-------------|-------:|
| 1a | Gross receipts or sales | 2,846,315 |
| 1b | Returns and allowances (customer refunds and credits) | 18,240 |
| 1c | Balance | 2,828,075 |
| 2 | Cost of goods sold (Form 1125-A: hosting, data licenses, support staff) | 412,906 |
| 3 | Gross profit | 2,415,169 |
| 4 | Dividends and inclusions | 0 |
| 5 | Interest (Treasury money market fund) | 14,382 |
| 6 | Gross rents | 0 |
| 7 | Gross royalties | 0 |
| 8 | Capital gain net income | 0 |
| 9 | Form 4797 gain (loss) | 0 |
| 10 | Other income | 0 |
| 11 | Total income | 2,429,551 |
| 12 | Compensation of officers (Form 1125-E line 4) | 312,000 |
| 13 | Salaries and wages | 1,104,775 |
| 14 | Repairs and maintenance | 3,118 |
| 15 | Bad debts (specific accounts written off) | 9,460 |
| 16 | Rents (office lease) | 96,600 |
| 17 | Taxes and licenses (employer payroll taxes, Texas franchise tax, Delaware franchise tax) | 118,431 |
| 18 | Interest | 0 |
| 19 | Charitable contributions (limit check below) | 4,180 |
| 20 | Depreciation (Form 4562: 100% special allowance $36,915 on laptops and servers acquired after January 19, 2025, plus $4,372 MACRS on earlier assets) | 41,287 |
| 21 | Depletion | 0 |
| 22 | Advertising | 88,914 |
| 23 | Pension, profit-sharing (401(k) match) | 37,206 |
| 24 | Employee benefit programs | 96,128 |
| 25 | Energy efficient commercial buildings deduction | 0 |
| 26 | Other deductions (statement) | 258,289 |
| 27 | Total deductions | 2,170,388 |
| 28 | Taxable income before NOL and special deductions | 259,163 |
| 29a | NOL deduction | 207,330 |
| 29b | Special deductions | 0 |
| 29c | Add 29a and 29b | 207,330 |
| 30 | Taxable income | 51,833 |
| 31 | Total tax (Schedule J line 12) | 10,885 |
| 32 | Section 1062 first installment | 0 |
| 33 | Total payments (Schedule J line 23) | 12,400 |
| 34 | Estimated tax penalty | 0 |
| 35 | Amount owed | 0 |
| 36 | Overpayment | 1,515 |
| 37a | Credited to 2026 estimated tax (user's choice) | 1,515 |
| 37b | Refunded | 0 |

**Line 26 statement:** software subscriptions 71,402; contract labor 38,500; insurance 28,950; legal and professional fees 54,300; travel 19,876; meals (50% deductible portion) 6,137; utilities and telecom 7,500; amortization of 2023–2024 research costs (Form 4562, Part VI) 31,624. Total 258,289.

**Form 1125-E:** total receipts are $2,860,697 (line 1a $2,846,315 + line 5 $14,382), which is $500,000 or more, so Form 1125-E is required. Priya Raman, CEO, 100% of time, 46% common, $168,000; Daniel Okafor, CTO, 100% of time, 24% common, $144,000. Line 4 = $312,000 → page 1 line 12.

## The NOL deduction

- Available post-2017 carryover: $258,940 + $153,440 = $412,380 (Schedule K item 12).
- 80% × line 28: 0.80 × $259,163 = $207,330.40, rounded to $207,330. No section 199A or 250 deduction, no special deductions, no pre-2018 NOLs.
- Deduction = lesser of $412,380 or $207,330 = **$207,330**.
- Carryforward to 2026: $412,380 − $207,330 = **$205,050** (2023 loss used first: $207,330 of $258,940; remaining $51,610 of the 2023 loss and all $153,440 of the 2024 loss).

| Loss year | Vintage | Original | Used before 2025 | Available | Deducted 2025 | Carried forward |
|-----------|---------|---------:|-----------------:|----------:|--------------:|----------------:|
| 2023 | Post-2017 | 258,940 | 0 | 258,940 | 207,330 | 51,610 |
| 2024 | Post-2017 | 153,440 | 0 | 153,440 | 0 | 153,440 |
| Total | | 412,380 | 0 | 412,380 | 207,330 | 205,050 |

## The charitable limit, checked both ways

- Way A (NOL computed on line 28 as drafted): base = $259,163 + $4,180 − $207,330 = $56,013; 10% = $5,601.30.
- Way B (NOL computed before the contribution): NOL = 80% × $263,343 = $210,674 (rounded); base = $263,343 − $210,674 = $52,669; 10% = $5,266.90.
- The $4,180 contribution is under the limit either way, so the full amount stays on line 19 and nothing carries forward. Had it exceeded either figure, the agent would stop and ask the CPA to settle the deduction.

## Schedule J

| Line | Amount |
|------|-------:|
| 1a Income tax: $51,833 × 21% = $10,884.93 | 10,885 |
| 1b–1g, 1z | 0 |
| 2 Total income tax | 10,885 |
| 3 Corporate AMT | 0 |
| 4 | 10,885 |
| 5a–5f Credits | 0 |
| 6 Total credits | 0 |
| 7 | 10,885 |
| 8 PHC tax | 0 |
| 9a–9z, 10 | 0 |
| 11a | 10,885 |
| 11b, 11c | 0 |
| 12 Total tax | 10,885 |
| 13 Prior-year overpayment | 0 |
| 14 Estimated payments (4 × $3,100) | 12,400 |
| 15 Form 4466 refund | 0 |
| 17 Form 7004 deposit | 0 |
| 18 Withholding | 0 |
| 19 Total payments | 12,400 |
| 20a–20z, 21 | 0 |
| 22a, 22b | 0 |
| 23 | 12,400 |

**Estimated tax penalty check:** the 2024 return showed no tax, so the prior-year method is unavailable (Pub. 542). Required installment = 25% × $10,885 = $2,721.25. Each $3,100 payment was on time and above that amount, so line 34 = 0 and Form 2220 is not attached.

## Schedule K (answers that matter)

1 accrual · 2a/2b/2c 513210 (Software Publishers, from the instructions' code list), software publisher, subscription analytics software · 3 No · 4a No · 4b **Yes** (Priya 46%, Daniel 24%) → Schedule G Part II · 5a No · 5b No · 6 No · 7 No · 9 $0 · 10: 4 shareholders · 11 not checked · 12 **$412,380** · 13 **No** (total receipts $2,860,697) · 14 No · 15a Yes · 15b Yes · 16–23 No · 24 No (average gross receipts under $31 million, no interest expense) · 25 No · 26 No · 27 No · 28 No · 29a No → 29c Yes · 30 No · 31 No.

## Schedule L (per books)

| Line | Beginning (b) | End (d) |
|------|--------------:|--------:|
| 1 Cash | 1,410,369 | 1,662,656 |
| 2a/2b Receivables less allowance | 231,640 − 6,200 = 225,440 | 318,905 − 6,200 = 312,705 |
| 6 Other current assets (prepaids) | 38,475 | 44,120 |
| 10a/10b Depreciable assets less accumulated depreciation | 96,410 − 52,880 = 43,530 | 133,325 − 66,642 = 66,683 |
| 15 Total assets | 1,717,814 | 2,086,164 |
| 16 Accounts payable | 61,230 | 74,815 |
| 18 Other current liabilities (deferred revenue + accrued payroll) | 348,902 | 402,377 |
| 22b Common stock | 4,000 | 4,000 |
| 23 Additional paid-in capital | 1,900,000 | 1,900,000 |
| 25 Retained earnings, unappropriated | (596,318) | (295,028) |
| 28 Total liabilities and equity | 1,717,814 | 2,086,164 |

Item D = $2,086,164. Total assets are under $10 million, so Schedule M-1 (not M-3) applies.

## Schedule M-1

| Line | Amount |
|------|-------:|
| 1 Net income per books | 301,290 |
| 2 Federal income tax per books | 10,885 |
| 3, 4 | 0 |
| 5a, 5b | 0 |
| 5c Travel and entertainment (nondeductible 50% of $12,274 meals) | 6,137 |
| 6 Add lines 1–5 | 318,312 |
| 7 Income on books not on return | 0 |
| 8a Depreciation: tax $41,287 − book $13,762 | 27,525 |
| 8 (other) Amortization of 2023–2024 research costs (expensed for books in those years) | 31,624 |
| 9 Add lines 7 and 8 | 59,149 |
| 10 Income (page 1 line 28) | 259,163 |

## Schedule M-2

1 Beginning (596,318) · 2 Net income per books 301,290 · 3 0 · 4 (295,028) · 5a/5b/5c 0 · 6 0 · 7 0 · 8 Ending (295,028) = Schedule L line 25 column (d).

## Validation summary

- Math: 1c, 3, 11, 27, 28, 29c, 30 tie; J1a = 30 × 21%; J12 = 31; J23 = 33; 36 = 33 − 31 = 1,515 = 37a + 37b; L15 = L28 both columns; item D = L15(d); M-1 line 10 = line 28; M-2 line 8 = L25(d). All pass.
- Sanity: 29a is less than the carryover (80% cap applied); line 17 contains no federal income tax; distributions zero.
- Boundaries flagged: section 382 answer recorded as provided by company counsel; section 174A transition choice and amortization amount provided by the CPA.
- Attachments: Form 1125-A, Form 1125-E, Form 4562, Schedule G, NOL statement, line 26 statement.
- Filing: e-file required (more than 10 returns in calendar 2025). Due April 15, 2026.

## 2026 estimated tax handoff

The 2025 return covers 12 months and shows $10,885 of tax, and Larkspur is not a large corporation, so Method 2 gives $2,721.25 per installment, due April 15, June 15, September 15, and December 15, 2026. The $1,515 credited on line 37a counts toward the first installment, leaving $1,206.25 to pay by April 15, 2026. If 2026 tax is expected to be lower, Method 1 (25% of the 2026 tax) gives a smaller installment.

Sources: Form 1120 (2025); Instructions for Form 1120 (2025), Lines 12, 19, 26, 29a, 30, Schedule J, Schedule K; Instructions for Form 4562 (2025); Pub. 542 (Rev. January 2024); IRC §§ 11(b), 170, 172, 174A.
