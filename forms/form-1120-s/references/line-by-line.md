# Form 1120-S Line-by-Line Reference (2025 revision)

Every line of the 2025 Form 1120-S (form created 4/7/25) and the 2025 Schedule K-1 (Form 1120-S), built from the text of the IRS PDFs and the 2025 Instructions for Form 1120-S (dated Jan 15, 2026). Line numbers change between revisions: confirm against the current form at https://www.irs.gov/forms-pubs/about-form-1120-s before use.

Conventions: "Instr." = 2025 Instructions for Form 1120-S. "K" = Schedule K. Amounts are whole dollars (round all amounts or none; Instr., Rounding Off to Whole Dollars).

---

## Page 1 header

| Field | What goes here | Source / notes |
|---|---|---|
| Tax year line | Calendar 2025, or fiscal year beginning in 2025 | Fill dates only for fiscal or short years (Instr., Period Covered) |
| Name, address | True name per charter; principal office address, not the registered agent | Instr., Name and Address. "C/O" for third-party mail |
| A | S election effective date | From the IRS acceptance of Form 2553 |
| B | Business activity code number | Principal Business Activity Codes list at the end of the Instr.; nonstore retailers select by primary product |
| C | Check if Schedule M-3 attached | Required at $10 million+ total assets; optional below (Instr., Item C) |
| D | Employer identification number | "Applied for" + date only on a paper return; e-file requires an EIN (Instr., Item D) |
| E | Date incorporated | From the charter or state filing |
| F | Total assets | Per books at year end; = Schedule L, line 15, column (d) when Schedule L is completed; -0- if none (Instr., Item F) |
| G | Electing S beginning with this tax year? | "Yes" → attach Form 2553 if not already filed; generally a late election (Instr., Item G) |
| H(1)–(5) | Final return; name change; address change; amended return; S election termination | Final → also "Final K-1"; amended → statement of changed lines and "Amended K-1" (Instr., Item H; Amended Return) |
| I | Number of shareholders during any part of the tax year | Also the multiplier for the §6699 penalty |
| J(1) / J(2) | Aggregated activities for §465 / grouped activities for §469 | Only if the corporation made that choice |

Caution printed on the form: include only trade or business income and expenses on lines 1a through 22.

---

## Page 1 — Income

| Line | Description | How to compute / what to include |
|---|---|---|
| 1a | Gross receipts or sales | All trade or business receipts except amounts on lines 4 and 5. No rental, portfolio or tax-exempt income (Instr., Line 1a) |
| 1b | Less returns and allowances | Cash and credit refunds, rebates, allowances |
| 1c | Balance | 1a − 1b |
| 2 | Cost of goods sold | Form 1125-A, line 8 (attach) |
| 3 | Gross profit | 1c − 2 |
| 4 | Net gain (loss) from Form 4797, Part II, line 17 | Ordinary gains/losses on business assets only; not rental assets; not property for which §179 was passed through (that goes to K-1 box 17 code K) |
| 5 | Other income (loss) | Statement required. Interest on business receivables, bad-debt recoveries, insurance proceeds, §280F recapture, positive §481(a) adjustment, ordinary income from a partnership/estate/trust K-1 (not PTP income, not portfolio or rental items) |
| 6 | Total income (loss) | 3 + 4 + 5 |

## Page 1 — Deductions

| Line | Description | How to compute / what to include |
|---|---|---|
| 7 | Compensation of officers | Officers as defined by state law. From Form 1125-E, line 4 when total receipts ≥ $500,000. Includes fringe benefits (health insurance) of officers owning more than 2%. Excludes elective 401(k), salary-reduction SEP and SIMPLE IRA contributions and wages in COGS |
| 8 | Salaries and wages (less employment credits) | Non-officer wages; more-than-2% shareholder non-officers' fringe benefits go here; reduce by wage credits claimed |
| 9 | Repairs and maintenance | Not improvements that must be capitalized (Reg. §1.263(a)-3) |
| 10 | Bad debts | Business debts that became worthless; cash-method corporations only for amounts previously included in income |
| 11 | Rents | Business property and vehicle leases (Form 4562, Part V for vehicles; lease inclusion amount may apply). No rent for a dwelling used by a shareholder |
| 12 | Taxes and licenses | Employer payroll taxes, state/local taxes, licenses. Not federal income tax (except built-in gains tax allocable to ordinary income), not creditable foreign taxes (K line 16f), not taxes on rental or investment property |
| 13 | Interest | Business interest only. Rental interest → Form 8825 / K line 3b; investment interest → K line 12c; interest on debt allocated to distributions → K line 12e, K-1 box 12 code AC. §163(j) limit via Form 8990 unless a small business taxpayer |
| 14 | Depreciation from Form 4562 not claimed elsewhere | Excludes §179 (K line 11) and depreciation in COGS |
| 15 | Depletion | Not oil and gas (shareholders figure it); timber → Form T |
| 16 | Advertising | |
| 17 | Pension, profit-sharing, etc., plans | Employer contributions to qualified plans, SEP, SIMPLE; Form 5500 series may be required |
| 18 | Employee benefit programs | Only for employees owning 2% or less (health, up to $50,000 group-term life, employer-convenience meals and lodging) |
| 19 | Energy efficient commercial buildings deduction | Attach Form 7205 (§179D) |
| 20 | Other deductions | Statement listing type and amount: amortization, start-up and organizational costs, insurance, legal and professional fees, supplies, travel, 50% of meals, utilities, negative §481(a) adjustments. Not lobbying, fines, or expenses of tax-exempt income (K line 16c) |
| 21 | Total deductions | Sum of lines 7 through 20 |
| 22 | Ordinary business income (loss) | 6 − 21 → K line 1. Not used to figure the line 23a/23b taxes |

## Page 1 — Tax and Payments

| Line | Description | How to compute / what to include |
|---|---|---|
| 23a | Excess net passive income or LIFO recapture tax | Excess Net Passive Income Tax Worksheet (line 11 = line 10 × 21%); LIFO installment written "LIFO tax" to the left. Former C corporations only (boundary flag) |
| 23b | Tax from Schedule D (Form 1120-S) | Built-in gains tax, Schedule D (Form 1120-S), line 23 (boundary flag) |
| 23c | Add lines 23a and 23b | Plus Form 4255 amounts ("From Form 4255"), Form 8697 and Form 8866 look-back interest, each noted to the left |
| 24a | Current year's estimated tax payments and preceding year's overpayment credited | |
| 24b | Tax deposited with Form 7004 | |
| 24c | Credit for federal tax paid on fuels | Attach Form 4136 |
| 24d | Elective payment election amount from Form 3800 | Form 3800, Part III, line 6, column (h); also K line 16b tax-exempt income |
| 24z | Add lines 24a through 24d | Include a §643(g) trust credit as "T" to the left |
| 25 | Estimated tax penalty | Check the box if Form 2220 attached |
| 26 | Amount owed | If 24z < 23c + 25: (23c + 25) − 24z. Pay electronically. Online installment agreement if ≤ $25,000 and payable in 24 months |
| 27 | Overpayment | If 24z > 23c + 25: 24z − (23c + 25) |
| 28a | Credited to 2026 estimated tax | Irrevocable once made |
| 28b | Refunded | |
| 28c | Routing number | 9 digits; first two 01–12 or 21–32 |
| 28d | Type: Checking / Savings | Check exactly one |
| 28e | Account number | Up to 17 characters, include hyphens, no spaces |
| Signature | Officer signature, date, title; "May the IRS discuss" box | President, VP, treasurer, assistant treasurer, chief accounting officer or other authorized officer |
| Paid preparer | Name, signature, date, PTIN, firm name, EIN, address, phone | Blank if prepared by an employee or without charge |

---

## Schedule B — Other Information (pages 2–3)

| Item | Question | Notes |
|---|---|---|
| 1 | Accounting method: (a) cash (b) accrual (c) other | Tax shelters cannot use cash; inventory rules for non-small business taxpayers |
| 2 | (a) Business activity (b) Product or service | From the Principal Business Activity Codes list |
| 3 | Any shareholder a disregarded entity, trust, estate, nominee or similar person? | "Yes" → attach Schedule B-1 |
| 4a | At year end, own directly 20%+ or directly/indirectly 50%+ of any corporation? | "Yes" → (i) name (ii) EIN (iii) country (iv) % owned (v) date of QSub election if 100% |
| 4b | At year end, own directly 20%+ or directly/indirectly 50%+ of profit, loss or capital of any partnership or beneficial interest of a trust? | "Yes" → (i)–(v), including maximum % owned |
| 5a | Restricted stock outstanding at year end? | (i) restricted shares (ii) non-restricted shares |
| 5b | Stock options, warrants or similar instruments outstanding? | (i) shares outstanding (ii) shares if all executed |
| 6 | Filed or required to file Form 8918 (material advisor)? | |
| 7 | Issued publicly offered debt with OID? | Form 8281 may be required |
| 8 | Net unrealized built-in gain reduced by prior net recognized built-in gain | Former C corporations or carryover-basis C assets only; statement per asset pool |
| 9 | §163(j) real property or farming election in effect? | Irrevocable election; ADS required |
| 10 | Satisfies 10a, 10b or 10c (pass-through excess interest; 3-year average gross receipts > $31 million with business interest; tax shelter with business interest)? | "Yes" → Form 8990 |
| 11 | (a) Total receipts < $250,000 AND (b) year-end total assets < $250,000? | "Yes" → Schedules L and M-1 not required. Total receipts defined below |
| 12 | Non-shareholder debt canceled, forgiven or modified to reduce principal? | Enter principal reduction; PPP forgiveness disregarded |
| 13 | QSub election terminated or revoked during the year? | Reg. §1.1361-5 |
| 14a | Made payments requiring Form(s) 1099? | For payments made in 2025, under the rules for 2025 (base §6041(a) threshold rises to $2,000 for payments made after December 31, 2025: Rev. Proc. 2025-32 §2.15) |
| 14b | If "Yes," did or will the corporation file them? | |
| 15 | Intends to self-certify as a Qualified Opportunity Fund? | Attach Form 8996; enter line 15 amount |
| 16 | Received, sold, exchanged or otherwise disposed of a digital asset? | Must check Yes or No; holding or self-transfers alone are "No" |
| 17 | Reserved for future use | |

**Total receipts for question 11 and Form 1125-E** (Instr., Question 11; lines 7 and 8): page 1 line 1a + lines 4 and 5 + income on K lines 3a, 4, 5a, 6 + income or net gain on K lines 7, 8a, 9, 10 + income or net gain on Form 8825 lines 2, 21, 22a.

---

## Schedule K — Shareholders' Pro Rata Share Items (pages 3–4)

| Line | Item | Source |
|---|---|---|
| 1 | Ordinary business income (loss) | Page 1, line 22 |
| 2 | Net rental real estate income (loss) | Form 8825 |
| 3a / 3b / 3c | Other gross rental income / expenses / net (3a − 3b) | Statement for 3b |
| 4 | Interest income | Portfolio interest |
| 5a / 5b | Ordinary dividends / qualified dividends | 5b is a subset of 5a |
| 6 | Royalties | |
| 7 | Net short-term capital gain (loss) | Schedule D (Form 1120-S), line 7 |
| 8a / 8b / 8c | Net long-term capital gain (loss) / collectibles (28%) / unrecaptured §1250 gain | Schedule D (Form 1120-S), line 15; statement for 8c |
| 9 | Net section 1231 gain (loss) | Form 4797 |
| 10 | Other income (loss) | With type code |
| 11 | Section 179 deduction | Form 4562; never on page 1 |
| 12a / 12b | Cash / noncash charitable contributions | Form 8283 if required |
| 12c | Investment interest expense | |
| 12d | Section 59(e)(2) expenditures | With type |
| 12e | Other deductions | With type code |
| 13a–13g | Credits (low-income housing, rehabilitation, other rental, biofuel, other) | With codes |
| 14a | Check if reporting items of international tax relevance (attach Schedule K-2) | |
| 14b | Check if qualified for an exception to filing Schedule K-2 | Attach statement |
| 15a–15f | AMT items (post-1986 depreciation adjustment, adjusted gain or loss, depletion, oil/gas/geothermal gross income and deductions, other) | Complete for all shareholders |
| 16a | Tax-exempt interest income | Increases stock basis |
| 16b | Other tax-exempt income | Includes EPE and §6418 transfer amounts |
| 16c | Nondeductible expenses | Decreases stock basis |
| 16d | Distributions | Cash plus FMV of property, excluding dividends on line 17c; statement for property |
| 16e | Repayment of loans from shareholders | |
| 16f | Foreign taxes paid or accrued | |
| 17a / 17b | Investment income / investment expenses | From K lines 4, 5a, 6, 10 / line 12e |
| 17c | Dividend distributions paid from accumulated E&P | Report on Form 1099-DIV, not on K-1 |
| 17d | Other items and amounts | Statement; codes include V (§199A, Statement A), AC (gross receipts for §448(c)), BA (domestic research or experimental expenditures, new for 2025), ZZ |
| 18 | Income (loss) reconciliation | Lines 1 through 10 combined, minus lines 11 through 12e and 16f; must equal Schedule M-1, line 8 (or M-3, Part II, line 26(d)) |

---

## Schedule L — Balance Sheets per Books (page 4)

Columns: (a)/(b) beginning of tax year, (c)/(d) end of tax year. Not required if Schedule B, question 11 = "Yes".

| Line | Assets |
|---|---|
| 1 | Cash |
| 2a / 2b | Trade notes and accounts receivable / less allowance for bad debts |
| 3 | Inventories |
| 4 | U.S. government obligations |
| 5 | Tax-exempt securities (state/local obligations; RIC stock paying exempt-interest dividends) |
| 6 | Other current assets (statement) |
| 7 | Loans to shareholders |
| 8 | Mortgage and real estate loans |
| 9 | Other investments (statement) |
| 10a / 10b | Buildings and other depreciable assets / less accumulated depreciation |
| 11a / 11b | Depletable assets / less accumulated depletion |
| 12 | Land (net of any amortization) |
| 13a / 13b | Intangible assets (amortizable only) / less accumulated amortization |
| 14 | Other assets (statement) |
| 15 | Total assets (column (d) → item F) |

| Line | Liabilities and Shareholders' Equity |
|---|---|
| 16 | Accounts payable |
| 17 | Mortgages, notes, bonds payable in less than 1 year |
| 18 | Other current liabilities (statement) |
| 19 | Loans from shareholders (reconciles to the sum of K-1 item I) |
| 20 | Mortgages, notes, bonds payable in 1 year or more |
| 21 | Other liabilities (statement) |
| 22 | Capital stock |
| 23 | Additional paid-in capital |
| 24 | Retained earnings |
| 25 | Adjustments to shareholders' equity (statement) |
| 26 | Less cost of treasury stock |
| 27 | Total liabilities and shareholders' equity (= line 15) |

---

## Schedule M-1 — Reconciliation of Income (Loss) per Books With Income (Loss) per Return (page 5)

Not required if question 11 = "Yes"; replaced by Schedule M-3 at $10 million+ total assets.

| Line | Description |
|---|---|
| 1 | Net income (loss) per books |
| 2 | Income included on K lines 1, 2, 3c, 4, 5a, 6, 7, 8a, 9, 10 not recorded on books this year (itemize) |
| 3a | Expenses recorded on books not included on K lines 1–12e and 16f: depreciation |
| 3b | Same: travel and entertainment (nondeductible meals, entertainment, QTFs, gifts over $25, club dues, etc.) |
| 4 | Add lines 1 through 3 |
| 5a | Income recorded on books not included on K lines 1–10: tax-exempt interest (and other, itemized) |
| 6a | Deductions included on K lines 1–12e and 16f not charged against book income: depreciation (and other, itemized) |
| 7 | Add lines 5 and 6 |
| 8 | Income (loss) (Schedule K, line 18): line 4 − line 7 |

---

## Schedule M-2 — AAA, PTEP, AE&P, Other Adjustments Account (page 5)

Columns: (a) accumulated adjustments account, (b) shareholders' undistributed taxable income previously taxed (only if a balance existed at the start of 2025), (c) accumulated earnings and profits, (d) other adjustments account.

| Line | Description |
|---|---|
| 1 | Balance at beginning of tax year (= prior year line 8) |
| 2 | Ordinary income from page 1, line 22 |
| 3 | Other additions (separately stated income, including K lines 4, 5a, 6, gains; tax-exempt income goes in column (d)) |
| 4 | Loss from page 1, line 22 (column (a), in parentheses) |
| 5 | Other reductions (separately stated losses and deductions, nondeductible expenses other than those related to tax-exempt income; parentheses in columns (a) and (d)) |
| 6 | Combine lines 1 through 5 |
| 7 | Distributions (ordering rules in schedules-l-m1-m2.md) |
| 8 | Balance at end of tax year: line 6 − line 7 |

---

## Schedule K-1 (Form 1120-S) (2025)

Top boxes: "Final K-1", "Amended K-1"; tax year dates for fiscal or short years.

### Part I — Information About the Corporation

| Item | Content |
|---|---|
| A | Corporation's EIN |
| B | Corporation's name, address, city, state, ZIP |
| C | IRS Center where the corporation filed its return ("e-file" if filed electronically) |
| D | Corporation's total number of shares, beginning and end of tax year (LLC: units or equivalent; round to the nearest whole number, not below zero; 0.6315 rounds to 1) |

### Part II — Information About the Shareholder

| Item | Content |
|---|---|
| E | Shareholder's identifying number (may be truncated on the copy furnished to the shareholder, never on the IRS copy) |
| F1 | Shareholder of record's name and address |
| F2 | If the shareholder of record is a disregarded entity, trust, estate, nominee or similar person: TIN and name of the person responsible for reporting (rules by trust type in Instr., Item F2) |
| F3 | Type of entity of the shareholder of record |
| G | Current year allocation percentage (weighted by days when holdings changed) |
| H | Shareholder's number of shares, beginning and end of tax year |
| I | Loans from shareholder, beginning and end of tax year (direct debt only; not guarantees) |

### Part III — Shareholder's Share of Current Year Income, Deductions, Credits, and Other Items

| Box | Item | Matches Schedule K line |
|---|---|---|
| 1 | Ordinary business income (loss) | 1 |
| 2 | Net rental real estate income (loss) | 2 |
| 3 | Other net rental income (loss) | 3c |
| 4 | Interest income | 4 |
| 5a / 5b | Ordinary / qualified dividends | 5a / 5b |
| 6 | Royalties | 6 |
| 7 | Net short-term capital gain (loss) | 7 |
| 8a / 8b / 8c | Net long-term capital gain (loss) / collectibles (28%) / unrecaptured §1250 gain | 8a / 8b / 8c |
| 9 | Net section 1231 gain (loss) | 9 |
| 10 | Other income (loss) (code) | 10 |
| 11 | Section 179 deduction | 11 |
| 12 | Other deductions (codes; e.g., A cash contributions) | 12a–12e |
| 13 | Credits (codes) | 13a–13g |
| 14 | Schedule K-3 is attached if checked | 14a |
| 15 | AMT items (codes A–F) | 15a–15f |
| 16 | Items affecting shareholder basis (codes A tax-exempt interest, B other tax-exempt income, C nondeductible expenses, D distributions, E repayment of loans from shareholders, F foreign taxes) | 16a–16f |
| 17 | Other information (codes, e.g., A investment income, B investment expenses, V §199A, AC gross receipts) | 17a, 17b, 17d |
| 18 | More than one activity for at-risk purposes (check; statement) | — |
| 19 | More than one activity for passive activity purposes (check; statement) | — |

In boxes 10, 12, 13 and 15–17 enter a code in the left column; use an asterisk and "STMT" when the detail is on an attached statement (Instr., Codes; Attached statements).
