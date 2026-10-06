# Example: One-Owner Personal Service Corporation Under the $250,000 Test

A calendar-year 2025 Form 1120 for a small engineering consulting corporation. Total receipts and total assets are both under $250,000, so Schedule K question 13 is "Yes" and Schedules L, M-1, and M-2 are skipped, with distributions entered on the question 13 line. The prior-year estimated tax safe harbor applies, a small balance is due, and the corporation may file on paper because it filed fewer than 10 returns in calendar 2025. All arithmetic was checked in Python before writing.

---

## The corporation

- **Name:** Quillon Engineering Studio, Inc. (Oregon corporation, incorporated 2021), principal office Portland, Oregon
- **Owner:** Wren Lindqvist, licensed structural engineer, 100% shareholder, president, sole employee
- **Tax year:** calendar 2025, cash method
- **Personal service corporation:** yes. Its principal activity is engineering, performed by its employee-owner (Instructions, Item A, Personal Service Corporation). Check item A box 3. The tax rate is the same 21% (Schedule J line 1a instructions).

## Facts the agent asked for, and the answers

| Question | User's answer |
|----------|---------------|
| Wren's W-2 wages for 2025? | $118,000 per the payroll provider's annual report |
| Total assets on the December 31, 2025 balance sheet? | $61,240 |
| Distributions to Wren during 2025 (not payroll)? | $9,500 cash; no property |
| 2024 Form 1120 tax, and was it a full 12-month return? | $3,141; yes |
| Estimated payments? | $786 on April 15, June 16, September 15, December 15, 2025 |
| Passive or rental activities? | None (no Form 8810 needed) |
| Returns required in calendar 2025? | 2024 Form 1120, 4 Forms 941, 1 Form 940, 1 Form W-2, 1 Form 1099-NEC (drafting contractor) = 8 |

The agent did not evaluate whether $118,000 is reasonable compensation. It recorded the payroll figure and noted that reasonableness questions go to a CPA.

## Page 1

| Line | Description | Amount |
|------|-------------|-------:|
| 1a | Gross receipts or sales | 214,780 |
| 1b | Returns and allowances | 0 |
| 1c | Balance | 214,780 |
| 2 | Cost of goods sold | 0 |
| 3 | Gross profit | 214,780 |
| 4 | Dividends and inclusions | 0 |
| 5 | Interest (business savings) | 318 |
| 6–10 | Rents, royalties, capital gains, Form 4797, other | 0 |
| 11 | Total income | 215,098 |
| 12 | Compensation of officers (Form 1125-E not required: total receipts under $500,000) | 118,000 |
| 13 | Salaries and wages | 0 |
| 14 | Repairs and maintenance | 0 |
| 15 | Bad debts | 0 |
| 16 | Rents (studio space) | 14,400 |
| 17 | Taxes and licenses (employer payroll taxes, Oregon licenses and fees) | 10,214 |
| 18 | Interest | 0 |
| 19 | Charitable contributions | 0 |
| 20 | Depreciation (Form 4562) | 2,968 |
| 21 | Depletion | 0 |
| 22 | Advertising | 3,150 |
| 23 | Pension, profit-sharing (401(k) employer contribution) | 11,800 |
| 24 | Employee benefit programs (health insurance) | 9,636 |
| 25 | Energy efficient commercial buildings deduction | 0 |
| 26 | Other deductions (statement) | 29,364 |
| 27 | Total deductions | 199,532 |
| 28 | Taxable income before NOL and special deductions | 15,566 |
| 29a | NOL deduction | 0 |
| 29b | Special deductions | 0 |
| 29c | Add 29a and 29b | 0 |
| 30 | Taxable income | 15,566 |
| 31 | Total tax (Schedule J line 12) | 3,269 |
| 32 | Section 1062 first installment | 0 |
| 33 | Total payments (Schedule J line 23) | 3,144 |
| 34 | Estimated tax penalty | 0 |
| 35 | Amount owed | 125 |
| 36 | Overpayment | 0 |
| 37a | Credited to 2026 estimated tax | 0 |
| 37b | Refunded | 0 |

**Line 26 statement:** software subscriptions 6,312; professional liability insurance 3,480; accounting and legal 4,250; contract labor 9,900; travel 2,876; meals (50% deductible portion) 612; phone and internet 1,934. Total 29,364.

## Schedule C

All lines 0. No dividends.

## Schedule J

1a $15,566 × 21% = $3,268.86 → 3,269 · 1b–1z 0 · 2 3,269 · 3 0 · 4 3,269 · 5a–5f 0 · 6 0 · 7 3,269 · 8 0 · 9a–9z 0 · 10 0 · 11a 3,269 · 11b 0 · 11c 0 · **12 3,269** · 13 0 · 14 3,144 · 15 0 · 17 0 · 18 0 · **19 3,144** · 20a–20z 0 · 21 0 · 22a 0 · 22b 0 · **23 3,144**.

**Estimated tax penalty check:** the 2024 return covered 12 months and showed $3,141 of tax, and the corporation is not a large corporation, so Method 2 applies: 25% × $3,141 = $785.25 per installment (Pub. 542). Each $786 payment was on time and at least that amount, so no penalty: line 34 = 0, no Form 2220. Method 1 would have required $817.25 per installment (25% × $3,269); the smaller Method 2 amount governs.

**Balance due:** $3,269 − $3,144 = $125, paid by electronic funds transfer by April 15, 2026.

## Schedule K (every question)

1 cash · 2a/2b/2c 541330 (Engineering Services, from the instructions' code list), engineering services, structural engineering consulting · 3 No · 4a No · 4b **Yes** (Wren 100%) → Schedule G Part II · 5a No · 5b No · 6 No · 7 No · 8 No · 9 $0 · 10: 1 shareholder · 11 not checked · 12 $0 · **13 Yes**: total receipts $215,098 (line 1a $214,780 + line 5 $318) and total assets $61,240 are both under $250,000; enter distributions **$9,500** · 14 No · 15a Yes · 15b Yes · 16 No · 17 No · 18 No · 19 No · 20 No · 21 No · 22 No · 23 No · 24 No · 25 No · 26 No · 27 No · 28 No · 29a No → 29b skipped → 29c Yes · 30a/30b/30c No · 31 No.

## Schedules L, M-1, M-2

Not required: Schedule K question 13 = Yes. Item D is still completed: **$61,240** (Instructions, Item D).

## Validation summary

- Math: 1c, 3, 11, 27, 28, 30 tie; J1a = 30 × 21%; J12 = 31; J23 = 33; 35 = 31 − 33 = 125. All pass.
- Sanity: item A box 3 checked with a calendar year (required for a personal service corporation absent an exception); the $9,500 distribution is not on page 1; officer pay recorded from payroll, not estimated.
- Cross-form: line 12 ties to Wren's Form W-2 and the four Forms 941; one Form 1099-NEC issued for the $9,900 of contract labor.
- Attachments: Form 4562, Schedule G, line 26 statement. No Form 1125-E (receipts under $500,000), no Form 2220.

## Filing

The corporation was required to file 8 returns during calendar 2025, fewer than 10, so e-file is not mandatory (Reg. §301.6011-5(a)(1), (d)(5)). If Wren chooses paper: an Oregon corporation mails to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0012 (Instructions for Form 1120 (2025), Where To File), signed by Wren as president, and pays the $125 through EFTPS or the IRS business tax account by April 15, 2026. E-file through approved software remains available and is the default recommendation in filing.md.

## 2026 estimated tax handoff

Method 2 for 2026: 25% × $3,269 = $817.25 per installment, due April 15, June 15, September 15, and December 15, 2026. If 2026 tax is expected to fall below $500, no installments are required (Instructions for Form 1120, Estimated Tax Payments).

Sources: Form 1120 (2025); Instructions for Form 1120 (2025), Item A (Personal Service Corporation), Item D, Line 12, Schedule J, Schedule K question 13, Where To File; Pub. 542 (Rev. January 2024); Treasury Reg. §301.6011-5.
