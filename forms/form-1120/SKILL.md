---
name: form-1120
description: >
  Use this skill when a domestic C corporation, or an LLC that elected on Form 8832 to be
  taxed as a corporation, must prepare its annual federal income tax return on Form 1120.
  Triggers on phrases like "Form 1120", "fill out 1120", "C corp tax return", "corporate
  income tax return", "21% corporate tax", "1120 schedule C dividends received deduction",
  "1120 schedule J", "1120 schedule K question 13", "NOL deduction on 1120", "LLC taxed as a
  corporation return", "personal service corporation return". Do NOT use for an S corporation
  (use form-1120-s), a partnership or multi-member LLC without a corporate election (use
  form-1065), a sole proprietor or single-member LLC (use schedule-c), the entity election
  itself (use form-8832 or form-2553), an extension only (use form-7004), a pro forma 1120 for
  a foreign-owned disregarded entity (use form-5472), an amended return (Form 1120-X, no skill
  yet), or special returns (1120-F, 1120-H, 1120-REIT, 1120-RIC, 1120-L, 1120-PC, 1120-C).
form: Form 1120 (U.S. Corporation Income Tax Return)
audience: [ccorp, llc1, llcm]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1120.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1120.pdf
---

# Form 1120 — U.S. Corporation Income Tax Return

This skill produces an audit-grade draft of Form 1120: page 1 (income, deductions, taxable income, tax and payments), Schedule C (dividends and the dividends-received deduction), Schedule J (tax at 21%, credits, payments), the Schedule K questions, and Schedules L, M-1 and M-2 when the $250,000 test requires them. Every line is listed with its number, including zeros, with a validation summary and a sources list a CPA can check without redoing the math.

The arithmetic is simple. The judgment sits in five places: the dividends-received deduction and its taxable-income limit, the 80% cap on post-2017 net operating losses, the charitable contribution limit, the Schedule K question 13 test that decides whether Schedules L, M-1 and M-2 are required, and the estimated-tax handoff. Each depends on facts only the user has. Ask; do not assume.

**Revision:** Line map verified against the 2025 Form 1120 (form created 9/26/25) and the 2025 Instructions for Form 1120 (dated Jan 15, 2026), filed in 2026. The IRS revises both every year. Re-check the 2026 revision before use: https://www.irs.gov/forms-pubs/about-form-1120

**Companion guide for end users:** [Form 1120 Instructions 2026: Line by Line for C Corporations, the $250,000 Schedule K Test, the 21% Rate, and What OBBBA Changed](https://jupid.com/blog/form-1120-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.


---

## When to invoke

Engage this skill when any of these is true:

- The user names Form 1120, a "C corp return", or a "corporate income tax return".
- The entity is a state-law corporation with no accepted S election (C corporation is the default for a corporation).
- The entity is an LLC that filed Form 8832 electing association (corporate) classification. The instructions require a copy of Form 8832 attached to Form 1120 for the year of the election (Instructions, Who Must File).
- The entity's S election terminated or was revoked and it now files as a C corporation.
- The user asks about Schedule C (Form 1120) dividends, Schedule J, Schedule K (Form 1120) questions, or the NOL deduction on line 29a.

Do not engage this skill when:

- The corporation has an accepted S election → [`../form-1120-s/SKILL.md`](../form-1120-s/SKILL.md).
- The entity is a multi-member LLC that never elected corporate treatment → [`../form-1065/SKILL.md`](../form-1065/SKILL.md).
- The entity is a sole proprietorship or a single-member LLC that never elected → [`../schedule-c/SKILL.md`](../schedule-c/SKILL.md).
- The user is still deciding or making the classification election → [`../form-8832/SKILL.md`](../form-8832/SKILL.md) or [`../form-2553/SKILL.md`](../form-2553/SKILL.md).
- The user only needs more time to file → [`../form-7004/SKILL.md`](../form-7004/SKILL.md) (Form 1120 is form code 12 on Form 7004).
- The entity is a foreign-owned single-member LLC filing a pro forma Form 1120 with Form 5472 → [`../form-5472/SKILL.md`](../form-5472/SKILL.md).
- The user wants to correct a filed Form 1120 → Form 1120-X (Instructions, Other Forms and Statements). No skill exists yet; say so and stop.
- The entity must file a special return instead of Form 1120: 1120-F (foreign corporation), 1120-H (homeowners association), 1120-REIT, 1120-RIC, 1120-L, 1120-PC, 1120-C (cooperative), 1120-POL, 990-T (Instructions, Special Returns for Certain Organizations). Stop and redirect.

Boundaries inside a Form 1120 job (flag and hand off, do not compute):

- Consolidated returns (item A, box 1a, Form 851), life-nonlife groups (box 1b).
- Corporate alternative minimum tax (Schedule J line 3, Form 4626), base erosion minimum tax (line 1f, Form 8991, gross receipts of $500 million or more in any of the 3 preceding years per Schedule K question 22), personal holding company tax (line 8, Schedule PH).
- Foreign items: Schedule C lines 13 through 18 and 22 (section 245A, subpart F, GILTI, section 250), Forms 5471, 1118, 8992, 8993.
- Section 382 limits after an ownership change, section 384, section 1062 farmland installment election (line 32, Schedule J line 22b).
- Section 1202 (qualified small business stock). The exclusion belongs to the selling shareholder; Form 1120 has no line for it. If the user asks, say the corporation's records (gross assets, active business) matter to shareholders later and refer them to a CPA.

---

## Prerequisites

Collect these before drafting. If any item is missing, ask a specific question and stop until it is answered. Never fill a gap with a typical value.

1. **Tax year.** Calendar or fiscal; the year-end month. The 2025 form covers calendar 2025 and fiscal years that begin in 2025 (Instructions, Period Covered).
2. **Identity.** Legal name as in the charter, EIN, date incorporated, principal office address (not the registered agent's address), principal business activity code from the instructions' code list.
3. **Return status.** Initial, final, name change, address change (item E). Consolidated or not (item A, box 1a). Personal service corporation (box 3): ask whether the principal activity is accounting, actuarial science, architecture, consulting, engineering, health, law, or performing arts, substantially performed by employee-owners (Instructions, Item A).
4. **Accounting method** (Schedule K question 1) and average annual gross receipts for the 3 prior years. Above $31 million the corporation is not a small business taxpayer (Instructions, Accounting Methods; section 448(c)).
5. **Books for the year.** Trial balance or profit and loss statement with each income and expense account, plus cost of goods sold detail for Form 1125-A if the corporation sells inventory.
6. **Officer compensation.** Each officer's name, ownership percentage, and amount paid through payroll. Ask the user for the amounts on the officers' Forms W-2 and the payroll reports. Never choose or suggest a salary figure. For a C corporation the question is deductibility: compensation is deductible only as a reasonable allowance for services (IRC §162(a)(1)), and an excessive amount paid to a shareholder-officer can be treated as a nondeductible dividend. If the user asks what is reasonable, refer them to a CPA.
7. **Dividends received.** For each payer: domestic or foreign, the corporation's ownership percentage by vote and by value, whether the stock was debt-financed, and whether the holding-period test was met (46 days in the 91-day window; 91 days in the 181-day window for certain preferred stock). See [`references/schedule-c-dividends.md`](./references/schedule-c-dividends.md).
8. **Net operating loss carryovers.** Each loss year and amount, split between losses that arose in tax years beginning before January 1, 2018 and after December 31, 2017. Ask whether any ownership change (section 382) occurred. Ask for the prior-year return to confirm the carryover.
9. **Charitable contributions.** Amount paid in the year, unused carryovers from the prior 5 years, and, for an accrual-method corporation, any contribution authorized by the board during the year and paid by the 15th day of the 4th month after year end.
10. **Payments.** Each estimated tax payment with its date, prior-year overpayment credited, Form 7004 deposit, any Form 4466 refund, backup withholding.
11. **Prior-year return.** Total tax shown, whether the return covered 12 months, and taxable income for each of the 3 prior years (large-corporation test for Form 2220).
12. **Ownership.** Each shareholder owning 20% or more directly, or 50% or more of the vote directly or indirectly (Schedule G). Any foreign person owning 25% or more by vote or value (question 7, Form 5472). Number of shareholders at year end if 100 or fewer (question 10).
13. **Size tests.** Total receipts (page 1 line 1a plus lines 4 through 10) and total assets at year end. These decide Schedule K question 13 and Form 1125-E.
14. **Balance sheet and retained earnings** (if question 13 is "No"): beginning and ending balance sheet per books, book net income, federal income tax expense per books, distributions by type.
15. **Distributions to shareholders.** Cash and the book value of property distributed. Distributions never go on page 1.
16. **Other forms the facts trigger:** Form 4562 assets placed in service, Form 4797 sales of business property, capital gains (Schedule D (Form 1120), which is the corporate schedule, not the individual [`../schedule-d/SKILL.md`](../schedule-d/SKILL.md)), Forms 1099 issued, digital asset activity (question 27).

### Question bank (ask in these words when the fact is missing)

| Fact | Question to ask | Why it matters |
|------|-----------------|----------------|
| Officer pay | "What did each officer receive in W-2 wages this year, per the payroll reports? I will not estimate it." | Line 12 and Form 1125-E |
| Dividend ownership | "What percentage of the paying corporation's stock, by vote and by value, did the corporation own when each dividend was paid?" | 50% vs 65% vs 100% (Schedule C lines 1, 2, 11) |
| Holding period | "Was each stock held at least 46 days during the 91-day period that began 45 days before the ex-dividend date?" | Fails → no deduction; dividend moves to line 20 |
| NOL vintage | "List each loss year and amount. Did any loss arise in a tax year beginning before January 1, 2018?" | 80% limit applies only to post-2017 losses |
| Ownership change | "Did ownership of more than 50% of the stock change hands during the last three years, including through a financing round?" | Section 382 boundary |
| Contribution timing | "Was each contribution paid during the year? If accrual-method, did the board authorize any unpaid contribution during the year, and when was it paid?" | Line 19 timing election |
| Prior-year tax | "What total tax did last year's return show, and did that return cover a full 12 months?" | Estimated-tax Method 2 |
| Large corporation | "Was taxable income $1 million or more in any of the three prior years?" | Method 2 limited to the first installment |
| Size tests | "What are total receipts on line 1a plus lines 4 through 10, and total assets on the year-end balance sheet?" | Question 13 and Form 1125-E |
| Foreign owner | "Did any one foreign person own 25% or more of the vote or value at any time this year?" | Question 7 and Form 5472 |
| Research costs | "Did the corporation capitalize domestic research costs in 2022–2024, and which Rev. Proc. 2025-28 transition option did it adopt?" | Section 174A treatment |
| E-file count | "How many returns of any type (income tax, Forms 941, 940, W-2, 1099, excise) were the corporation and any controlled-group members required to file during the calendar year ending with or within this tax year?" | 10 or more → e-file required (Reg. §301.6011-5) |

---

## Workflow

### Step 1 — Confirm the return type

Confirm the entity is a domestic corporation with no S election in effect for the year, or an LLC with an effective corporate election. If the LLC's Form 8832 took effect this year, list a copy of Form 8832 as a required attachment. If anything points to a special return or an S election, stop and redirect per **When to invoke**.

### Step 2 — Fix the due dates

- Due date: the 15th day of the 4th month after year end; a calendar-year 2025 return is due April 15, 2026 (Instructions, When To File).
- A June 30 year end files by the 15th day of the 3rd month under the 2025 instructions. Form 7004 instructions (Rev. December 2025) give June 30 years that begin before January 1, 2026 a 7-month extension and years beginning in 2026 a 6-month extension; confirm the 2026 instructions for June 30 years beginning in 2026.
- A weekend or legal holiday moves the date to the next business day. Form 7004 extends filing, not payment.

### Step 3 — Build income, lines 1a through 11

Map every income account. Gross receipts on 1a, returns and allowances on 1b, cost of goods sold from Form 1125-A line 8 on line 2. Dividends go to Schedule C first and land on line 4 from Schedule C line 23. Taxable interest on line 5 (tax-exempt interest goes to Schedule K item 9 and Schedule M-1 line 7, never page 1). Capital gain net income from Schedule D (Form 1120) on line 8. Ordinary gain from Form 4797 Part II line 17 on line 9 ([`../form-4797/SKILL.md`](../form-4797/SKILL.md)). Everything else on line 10 with a statement.

### Step 4 — Build deductions, lines 12 through 27

Officer compensation on line 12 from the amounts the user provided. If total receipts are $500,000 or more, complete Form 1125-E and carry its line 4 to line 12 (Instructions, Line 12). Map the rest using [`references/line-by-line.md`](./references/line-by-line.md). Section 179 and depreciation both come from Form 4562 to line 20 ([`../form-4562/SKILL.md`](../form-4562/SKILL.md)). Charitable contributions go on line 19 only after the limit in Step 6.

### Step 5 — Schedule C and the dividends-received deduction

Classify each dividend by ownership and holding period, compute column (c), apply the section 246(b) taxable-income limit with the instructions' worksheet, and carry line 23 to page 1 line 4 and line 24 to page 1 line 29b. Procedure and worksheet: [`references/schedule-c-dividends.md`](./references/schedule-c-dividends.md).

### Step 6 — Charitable contributions and the NOL deduction

Apply the charitable limit (10% of taxable income figured without the contribution deduction, special deductions, NOL carrybacks and capital loss carrybacks; with an NOL carryover the limit uses taxable income after the NOL deduction) and the NOL limit (post-2017 losses up to 80% of taxable income figured without the NOL, section 199A and section 250 deductions). If both limits bind in the same year, stop: the two computations depend on each other; ask the user to confirm the figure with the CPA or software. Details: [`references/taxable-income-to-tax-due.md`](./references/taxable-income-to-tax-due.md).

### Step 7 — Taxable income and Schedule J

Line 28 = line 11 − line 27. Line 29c = 29a + 29b. Line 30 = line 28 − line 29c. Schedule J line 1a = line 30 × 21% (Instructions, Schedule J line 1a). Add other chapter 1 taxes, subtract credits, add other taxes, then payments on lines 13 through 23. Carry Schedule J line 12 to page 1 line 31 and line 23 to page 1 line 33.

### Step 8 — Estimated tax penalty check

Compare each installment paid against the required installment (25% of the smaller of current-year tax or prior-year tax, subject to the prior-year and large-corporation conditions). If an installment was short or late, flag Form 2220. Attach Form 2220 when the annualized or adjusted seasonal method was used, or when a large corporation based its first installment on the prior year's tax (Instructions, Line 34). Form 1120-W is historical; Pub. 542 (Rev. January 2024) states the 2022 revision was the last.

### Step 9 — Balance due or overpayment

Line 35 or 36 from lines 31 through 34. Ask how much of any overpayment to credit to next year's estimated tax (37a) and how much to refund (37b); the 37a election cannot be changed later (Instructions, Line 37a). Collect direct deposit details only at filing time (filing.md).

### Step 10 — Schedule K questions

Answer every question 1 through 31 (32 is reserved). Each "Yes" that adds a form is listed in [`references/schedules-k-l-m.md`](./references/schedules-k-l-m.md).

### Step 11 — Question 13 and Schedules L, M-1, M-2

Total receipts = line 1a + lines 4 through 10. If both total receipts and year-end total assets are under $250,000, answer "Yes", skip Schedules L, M-1 and M-2, and enter total cash distributions plus the book value of property distributions on the question 13 line. Otherwise complete all three. Item D (total assets) is required either way. Total assets of $10 million or more require Schedule M-3 instead of M-1: flag and hand off.

### Step 12 — Validate

Run every check in **Validation**. Surface failures; do not fix silently.

### Step 13 — Produce the deliverable

Fill the **Output format** template, every line with its number, zeros included.

### Step 14 — Hand off to filing

Load [`filing.md`](./filing.md) for channel choice (CPA, approved e-file software, or paper), the e-file mandate, Form 8879-C, payment by electronic funds transfer, Form 7004, and the mailing addresses. Remind the user of next year's estimated tax installments and the related returns this year produced (Forms 941, 940, W-2, 1099, 1099-DIV for dividends paid).

---

## Line-by-line guidance

Full map of every line: [`references/line-by-line.md`](./references/line-by-line.md). Rules the agent applies most often:

### Header

- **Item A boxes:** 1a consolidated (Form 851), 1b life-nonlife, 2 personal holding company (Schedule PH), 3 personal service corporation, 4 Schedule M-3 attached.
- **Item D:** total assets from the books at year end; from Schedule L line 15 column (d) when Schedule L is completed; enter -0- if none.
- **Item E:** initial, final, name change, address change. Use Form 8822-B for changes after filing.

### Income (lines 1a–11)

- Line 1a takes gross receipts from all business operations except amounts reported on lines 4 through 10.
- Line 5: taxable interest only. Do not net interest expense against it.
- Line 10: ordinary income from a partnership Schedule K-1, recoveries of deducted bad debts, refunds of previously deducted taxes, positive section 481(a) adjustments. Partnership ordinary losses go on line 26, not netted on line 10.

### Deductions (lines 12–27)

- **Line 12:** officers only. Form 1125-E at total receipts of $500,000 or more.
- **Line 13:** other employees' wages less employment credits. Exclude amounts in cost of goods sold.
- **Line 17:** never federal income tax.
- **Line 18:** business interest; if the corporation is not a small business taxpayer ($31 million average gross receipts test), Form 8990 applies (section 163(j): business interest income + 30% of adjusted taxable income + floor plan interest).
- **Line 19:** paid contributions plus carryovers, limited to 10% of taxable income computed under the instructions; excess carries forward 5 years. For tax years beginning after December 31, 2025, IRC §170(b)(2)(A) as amended by P.L. 119-21 §70426 allows contributions only to the extent they exceed 1% and do not exceed 10% of taxable income. Recheck the 2026 instructions.
- **Line 20:** depreciation and section 179 from Form 4562, net of amounts in cost of goods sold. For tax years beginning in 2025 the section 179 limit is $2,500,000, reduced above $4,000,000 of section 179 property placed in service, and qualified property acquired after January 19, 2025 qualifies for the 100% special allowance (2025 Instructions for Form 4562).
- **Line 26:** attach a statement by type: amortization (Form 4562 Part VI), start-up and organizational costs (limited deduction, remainder over 180 months per sections 195 and 248), insurance, legal and professional fees, supplies, utilities, travel, the deductible 50% of meals, partnership ordinary losses, negative section 481(a) adjustments.
- **Domestic research costs:** deductible under section 174A(a) for tax years beginning after December 31, 2024, or amortizable over at least 60 months by election under section 174A(c). For unamortized 2022–2024 amounts, ask which transition option under Rev. Proc. 2025-28 the corporation chose; do not choose one.

### Lines 28–37

- 28 = 11 − 27. 29a NOL (attach computation; complete Schedule K item 12). 29b = Schedule C line 24. 30 = 28 − 29c.
- 31 = Schedule J line 12. 32 = Form 1062 line 15 (section 1062 election only). 33 = Schedule J line 23. 34 = estimated tax penalty (check the box if Form 2220 is attached).
- 35 = amount owed if line 33 < lines 31 + 32 + 34; 36 = overpayment otherwise; 37a + 37b = 36.

### Schedule C (summary)

| Line | Dividend type | Column (b) |
|------|---------------|-----------|
| 1 | Less-than-20%-owned domestic corporations (not debt-financed) | 50 |
| 2 | 20%-or-more-owned domestic corporations (not debt-financed) | 65 |
| 3 | Debt-financed stock (section 246A) | See instructions |
| 4 / 5 | Certain preferred stock of public utilities, under 20% / 20% or more owned | 23.3 / 26.7 |
| 6 / 7 / 8 | Foreign corporations under 20% / 20% or more owned / wholly owned subsidiaries | 50 / 65 / 100 |
| 9 | Subtotal of lines 1–8; column (c) limited by the section 246(b) worksheet | See instructions |
| 10 / 11 / 12 | Small business investment company / affiliated group members / certain FSCs | 100 |
| 13–18, 22 | Foreign and CFC items, section 250 | Boundary: hand off |
| 19 / 20 | IC-DISC dividends not on lines 1–3 / other dividends (REITs, non-qualifying RIC dividends, dividends failing the holding period) | None |

The 20% test uses voting power and value of the stock (Instructions, Schedule C). Line 23 = column (a) lines 9 through 20 → page 1 line 4. Line 24 = column (c) lines 9 through 22 → page 1 line 29b.

### Schedule J

- 1a = line 30 × 21%. Lines 1b–1z other chapter 1 taxes. 2 = sum of 1a–1z. 3 = CAMT from Form 4626 (boundary). 4 = 2 + 3. 5a–5f credits; 6 = sum. 7 = 4 − 6. 8 = PHC tax (boundary). 9a–9z other taxes; 10 = sum. 11a = 7 + 8 + 10. 12 = 11a − (11b + 11c).
- 13 prior-year overpayment credited; 14 current estimated payments; 15 Form 4466 refund (entered in parentheses, subtracts); 16 reserved; 17 Form 7004 deposit; 18 withholding; 19 = 13 + 14 − 15 + 17 + 18. 20a–20z refundable credits; 21 = sum. 22a Form 3800 elective payment; 22b section 1062 net tax liability. 23 = 19 + 21 + 22a + 22b.

### Schedule K and Schedules L, M-1, M-2

Questions, triggers, and the L/M-1/M-2 rules: [`references/schedules-k-l-m.md`](./references/schedules-k-l-m.md).

---

## Validation

### Math checks (block until resolved)

- [ ] 1c = 1a − 1b; 3 = 1c − 2; 11 = 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
- [ ] 27 = sum of 12 through 26; 28 = 11 − 27
- [ ] 29c = 29a + 29b; 30 = 28 − 29c
- [ ] Line 4 = Schedule C line 23 (column (a) lines 9 through 20); line 29b = Schedule C line 24 (column (c) lines 9 through 22)
- [ ] Schedule C line 9 column (c) ≤ worksheet line 29 (section 246(b) limit), unless the NOL exception applies
- [ ] 29a ≤ the NOL limit (pre-2018 carryovers + lesser of post-2017 carryovers or 80% of the excess of taxable income without NOL/199A/250 deductions over pre-2018 carryovers) and ≤ taxable income after special deductions
- [ ] Schedule J: 1a = 30 × 21%; 2 = 1a through 1z; 4 = 2 + 3; 6 = 5a through 5f; 7 = 4 − 6; 10 = 9a through 9z; 11a = 7 + 8 + 10; 12 = 11a − 11b − 11c
- [ ] Schedule J: 19 = 13 + 14 − 15 + 17 + 18; 21 = 20a through 20z; 23 = 19 + 21 + 22a + 22b
- [ ] 31 = J12; 33 = J23; exactly one of 35 or 36 is nonzero; 37a + 37b = 36
- [ ] Line 12 = Form 1125-E line 4 when Form 1125-E is required; line 2 = Form 1125-A line 8
- [ ] If Schedules L, M-1, M-2 are completed: L line 15 = L line 28 for each column; item D = L line 15 column (d); M-1 line 10 = page 1 line 28; M-2 line 8 = L line 25 column (d); M-2 line 1 = L line 25 column (b)
- [ ] Schedule K item 9 = M-1 line 7 tax-exempt interest; Schedule K item 12 = NOL available before this year's deduction

### Sanity checks (warn, do not block)

- [ ] Line 17 includes federal income tax → remove it; it belongs on M-1 line 2 only
- [ ] Shareholder distributions appear anywhere on page 1 → move to M-2 line 5 or the question 13 line
- [ ] Total receipts ≥ $500,000 and no Form 1125-E
- [ ] Line 12 is zero while officers worked in the business, or officer pay is unusually high relative to profit → ask the user to confirm the payroll records; do not change the number
- [ ] Line 29a equals the full carryover while line 28 is positive → recheck the 80% limit
- [ ] Line 19 > 10% of the computed base → recompute the limit and carry the excess forward
- [ ] Item A box 3 checked and the year is not a calendar year → personal service corporations must use a calendar year unless an exception applies (Instructions, Personal Service Corporation)
- [ ] Question 7 "Yes" with no Forms 5472 counted
- [ ] Question 13 "Yes" but total receipts or total assets is $250,000 or more
- [ ] Total assets ≥ $10 million → Schedule M-3 required; stop and hand off
- [ ] Each estimated payment is below the required installment → Form 2220 penalty exposure

### Cross-form checks

- [ ] Line 12 + line 13 (+ wages in cost of goods sold) reconcile to the four Forms 941 and Form W-3 ([`../form-941/SKILL.md`](../form-941/SKILL.md))
- [ ] Question 15a "Yes" → Forms 1099 filed ([`../form-1099-nec/SKILL.md`](../form-1099-nec/SKILL.md))
- [ ] Dividends paid to shareholders → Forms 1099-DIV
- [ ] LLC in its first corporate year → Form 8832 copy attached

---

## Output format

```markdown
# Form 1120 — DRAFT for tax year YYYY (form revision: 2025 Form 1120)

## Header
Name / EIN / Address:            <...>
A. 1a Consolidated: No | 1b Life-nonlife: No | 2 PHC: No | 3 PSC: Yes/No | 4 Sch. M-3: No
B. EIN:                          XX-XXXXXXX
C. Date incorporated:            MM/DD/YYYY
D. Total assets:                 $X
E. Initial / Final / Name change / Address change: <checked boxes or none>

## Income
1a Gross receipts or sales       $X     1b Returns and allowances  $X     1c Balance  $X
2  Cost of goods sold (1125-A)   $X     3  Gross profit            $X
4  Dividends and inclusions      $X     5  Interest                $X
6  Gross rents                   $X     7  Gross royalties         $X
8  Capital gain net income       $X     9  Form 4797 gain (loss)   $X
10 Other income (statement)      $X     11 Total income            $X

## Deductions
12 Officers (1125-E: yes/no)     $X     13 Salaries and wages      $X
14 Repairs and maintenance       $X     15 Bad debts               $X
16 Rents                         $X     17 Taxes and licenses      $X
18 Interest                      $X     19 Charitable (after limit) $X
20 Depreciation (4562)           $X     21 Depletion               $X
22 Advertising                   $X     23 Pension, profit-sharing $X
24 Employee benefit programs     $X     25 Energy efficient bldgs  $X
26 Other deductions (statement)  $X     27 Total deductions        $X

## Taxable income, tax, payments
28 TI before NOL and special ded. $X    29a NOL deduction          $X
29b Special deductions (Sch C 24) $X    29c Add 29a and 29b        $X
30 Taxable income                 $X    31 Total tax (Sch J 12)    $X
32 Section 1062 first installment $X    33 Payments (Sch J 23)     $X
34 Estimated tax penalty          $X    (Form 2220 attached: yes/no)
35 Amount owed                    $X    36 Overpayment             $X
37a Credited to next year         $X    37b Refunded               $X

## Schedule C (lines 1–24, columns (a), (b) %, (c)); show the §246(b) worksheet if line 9 is limited
## Schedule J (lines 1a–23, every line)
## Schedule K (questions 1–31: Yes/No and every required entry)
## Schedule L (lines 1–28, columns (a)–(d)) | or "Not required: Schedule K question 13 = Yes"
## Schedule M-1 (lines 1–10) | M-2 (lines 1–8) | or "Not required: question 13 = Yes; distributions entered: $X"

## Statements
- Line 10 other income: <type: amount>
- Line 26 other deductions: <type: amount> ... total = line 26
- Line 29a NOL computation: <loss year, original amount, used, available, deduction, carryforward>
- Charitable limit computation: <base, 10% limit, deduction, carryover>

## Required attachments
- [ ] Form 1125-A  - [ ] Form 1125-E  - [ ] Form 4562  - [ ] Form 4797  - [ ] Schedule D (Form 1120) / Form 8949
- [ ] Schedule G  - [ ] Form 5472 (count: N)  - [ ] Form 8990  - [ ] Form 2220  - [ ] Form 8832 copy
- [ ] Schedule O  - [ ] Schedule UTP  - [ ] Form 4626 (or question 29c safe harbor)

## Validation summary
- Math: all checks passed | <failures>
- Sanity: <warnings>
- Boundaries flagged for CPA: <list or none>
- Estimated tax next year: <installment dates and amounts, method used>

## Sources cited in this draft
- 2025 Form 1120 (created 9/26/25); 2025 Instructions for Form 1120 (Jan 15, 2026)
- IRC §§ 11(b), 170, 172, 243, 246, 246A, 6655; <others used>
- Pub. 542 (Rev. January 2024); Instructions for Form 2220 (2025); <others used>
```

The draft is not the filed return. The corporation's officer signs the return; e-filing goes through an authorized provider or the corporation's tax professional (filing.md).

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md): every line of the 2025 Form 1120: header, page 1, Schedules C, J, K, L, M-1, M-2
- [`references/schedule-c-dividends.md`](./references/schedule-c-dividends.md): dividends-received deduction percentages, ownership and holding-period tests, debt-financed stock, the section 246(b) worksheet and its NOL exception
- [`references/taxable-income-to-tax-due.md`](./references/taxable-income-to-tax-due.md): NOL deduction and the 80% limit, charitable limit (2025 and 2026 rules), Schedule J, estimated tax, Form 2220 and Form 4466, CAMT/BEAT/PHC and section 1202 boundaries
- [`references/schedules-k-l-m.md`](./references/schedules-k-l-m.md): Schedule K questions and the forms they trigger, question 13, Schedules L, M-1, M-2, Schedule M-3 boundary
- [`references/common-mistakes.md`](./references/common-mistakes.md): errors to catch before the draft goes out
- [`filing.md`](./filing.md): filing channels, e-file mandate, signature, payment, Form 7004, mailing addresses, consent and security rules

## Examples

- [`examples/saas-nol-80-percent-cap.md`](./examples/saas-nol-80-percent-cap.md): software company with a post-2017 NOL limited to 80%, charitable limit check, section 174A transition question, Schedules L/M-1/M-2
- [`examples/distributor-dividends-received-deduction.md`](./examples/distributor-dividends-received-deduction.md): distributor with 65% and 50% dividends, the section 246(b) limit binding, Form 4466 refund, Schedules L/M-1/M-2
- [`examples/small-psc-under-250k.md`](./examples/small-psc-under-250k.md): one-owner personal service corporation answering question 13 "Yes", prior-year estimated tax safe harbor, small balance due

## Sources

Re-verify each source for the tax year being filed; amounts and line numbers change.

- [Form 1120 Instructions 2026 (Jupid blog)](https://jupid.com/blog/form-1120-instructions-2026): narrative companion for human readers
- [Form 1120 (2025)](https://www.irs.gov/pub/irs-pdf/f1120.pdf) and [Instructions for Form 1120 (2025)](https://www.irs.gov/pub/irs-pdf/i1120.pdf)
- [About Form 1120](https://www.irs.gov/forms-pubs/about-form-1120): revision history and updates
- [Instructions for Form 2220 (2025)](https://www.irs.gov/pub/irs-pdf/i2220.pdf): underpayment penalty, large corporation definition
- [Publication 542, Corporations (Rev. January 2024)](https://www.irs.gov/pub/irs-pdf/p542.pdf): estimated tax methods, Form 1120-W historical, Form 4466
- [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf): extension periods; Form 7004 code 12
- [Instructions for Form 4562 (2025)](https://www.irs.gov/pub/irs-pdf/i4562.pdf): section 179 limits and the 100% special allowance after January 19, 2025
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf): penalty amounts for returns due in 2027; section 6041 reporting threshold of $2,000 for payments after December 31, 2025
- [Quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates): underpayment rate used by Form 2220
- IRC §§ 11(b) (21% rate), 163(j), 170(b)(2) and (d)(2), 172, 174A, 179, 243, 245, 246(b) and (c), 246A, 448(c), 6072, 6651, 6655; Treasury Reg. §301.6011-5 (e-file mandate)
- P.L. 119-21 (One Big Beautiful Bill Act), §70426 (corporate 1% charitable floor, tax years beginning after December 31, 2025)
- Rev. Proc. 2025-28 — section 174A transition for 2022–2024 research costs
- [`../../workflows/irs-evidence-research/SKILL.md`](../../workflows/irs-evidence-research/SKILL.md): how to re-verify a number against primary IRS sources

## Disclaimer

This skill encodes the mechanics of Form 1120 from the IRS form, instructions, and cited authorities. It is not tax advice and creates no CPA-client relationship. Remind the user that the draft is a starting point; consolidated groups, foreign ownership or subsidiaries, ownership changes, net operating losses that interact with other limits, and the corporate alternative minimum tax call for a licensed tax professional.
