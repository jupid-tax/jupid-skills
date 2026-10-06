---
name: form-1120-s
description: >
  Use this skill when a corporation or LLC with an accepted S election must
  prepare its annual federal return, Form 1120-S, including Schedules B, K,
  L, M-1, M-2 and a Schedule K-1 for each shareholder. Triggers on phrases
  like "Form 1120-S", "1120S", "S corp tax return", "S corporation return",
  "file my S corp taxes", "Schedule K-1 for my S corp", "officer compensation
  line 7", "AAA Schedule M-2", "do I need Schedule L", "S corp distributions
  on the return", "K-2 K-3 domestic filing exception". Do NOT use for a C
  corporation return (use form-1120), a partnership or multi-member LLC
  without an S election (use form-1065), a sole proprietor or single-member
  LLC without an S election (use schedule-c), making or fixing the S election
  itself (use form-2553), the shareholder's own reporting of a K-1 on Form
  1040 (use schedule-e and form-1040), payroll returns (use form-941), or an
  extension only (use form-7004).
form: Form 1120-S (U.S. Income Tax Return for an S Corporation)
audience: [scorp, llc1, llcm]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1120s.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1120s.pdf
---

# Form 1120-S — U.S. Income Tax Return for an S Corporation

This skill produces an audit-grade draft of Form 1120-S: page 1 (lines 1a–28e), Schedule B, Schedule K, Schedules L, M-1 and M-2 when required, and one Schedule K-1 per shareholder, with a validation summary and a list of sources. The arithmetic is simple. The judgment concentrates in five places: officer compensation on line 7 (a fact the agent must ASK for, never choose), separating page 1 income from separately stated Schedule K items, the Schedule B question 11 test, the AAA roll-forward on Schedule M-2, and the per-share, per-day allocation onto each K-1.

Line map verified against the **2025 Form 1120-S** (form created 4/7/25), the **2025 Instructions for Form 1120-S** (dated Jan 15, 2026) and the **2025 Schedule K-1 (Form 1120-S)**, which are the revisions filed in 2026. Re-check the 2026 revision before using this skill for a 2026 tax year: https://www.irs.gov/forms-pubs/about-form-1120-s

**Companion guide for end users:** [Form 1120-S Instructions 2026: Line by Line for S Corporations, Officer Compensation, Schedule K-1, and Which Schedules You Can Skip](https://jupid.com/blog/form-1120-s-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when any of the following is true:

- The user mentions Form 1120-S, "1120S", "S corp return", or Schedule K-1 (Form 1120-S) from the corporation's side
- The entity filed Form 2553, the IRS accepted it, and the user needs the annual return for a tax year on or after the election's effective date
- An LLC elected S status (Form 2553 alone, or Form 8832 plus Form 2553) and asks which return to file
- The user asks how to report officer salary, distributions, the AAA, or K-1 allocations for an S corporation

Do not engage this skill when:

- The entity is a C corporation, or the S election has not taken effect for the year → use [`form-1120`](../form-1120/SKILL.md). The instructions say not to file Form 1120-S "for any tax year before the year the election takes effect"
- The entity is a partnership or multi-member LLC that never elected S status → use [`form-1065`](../form-1065/SKILL.md)
- The owner is a sole proprietor or a single-member LLC without an S election → use [`schedule-c`](../schedule-c/SKILL.md)
- The user needs to make the election, or relief for a late election → use [`form-2553`](../form-2553/SKILL.md). Late-election relief is claimed on Form 2553, not on Form 1120-S
- The user is a shareholder reporting a K-1 on a personal return → use [`schedule-e`](../schedule-e/SKILL.md) and [`form-1040`](../form-1040/SKILL.md)
- The user needs quarterly payroll returns for the officer's wages → use [`form-941`](../form-941/SKILL.md)
- The user only needs more time → use [`form-7004`](../form-7004/SKILL.md) (form code 25 for Form 1120-S)
- The user needs a state S corporation return. This skill covers the federal return only; say so

If the entity's status is unclear, ask: "Do you have the IRS letter accepting Form 2553, and what effective date does it show?" Stop until answered.

---

## Prerequisites

Collect these before drafting. If any item is missing, ask for it with the tight question shown and stop until it is answered. Do not fill gaps with defaults.

1. **Tax year and revision.** Calendar or fiscal year. Use the 2025 form for calendar 2025 and fiscal years that begin in 2025.
2. **Identity.** Legal name as in the charter, EIN, principal office address (not the registered agent's address), date incorporated, S election effective date (item A), business activity code (item B; code list in the instructions).
3. **Shareholder register for every day of the year.** Name, SSN or EIN, address, shares held at the start of the year, and every change with its date. Ask: "Did any shareholder buy, sell, gift or redeem shares during the year? Give the date and number of shares for each change." Item G percentages depend on this.
4. **Officer compensation facts.** Ask: "Which shareholders are officers under your state's law, what W-2 box 1 wages did the corporation pay each officer for the year, and what did it pay for each more-than-2% shareholder's health insurance?" Use the amounts the user gives, tied to Forms W-2 and 941. Never propose, estimate, or default a salary figure. See [`references/officer-compensation.md`](./references/officer-compensation.md).
5. **Trial balance or books** for the year: receipts, returns, cost of goods sold inputs (if inventory), every expense account, interest and dividend income, rents, asset purchases and sales, loans to or from shareholders, distributions by date and recipient.
6. **Prior-year return** (or opening balances): beginning AAA, other adjustments account, accumulated earnings and profits (AE&P), beginning balance sheet, carryovers.
7. **History screen.** Ask: "Was the corporation ever a C corporation, or did it acquire assets from a C corporation in a tax-free transaction? Did it use LIFO before the election?" A "Yes" activates the boundary flags in Step 2.
8. **Payments.** Estimated tax payments and any deposit with Form 7004, each with date and amount.
9. **Foreign items.** Ask: "Did the corporation pay foreign taxes, earn foreign-source income, or own any foreign entity, branch or account?" Drives Schedule K line 14 and Schedules K-2/K-3.

---

## Workflow

### Step 1 — Confirm the return applies

Confirm the IRS accepted Form 2553 and the effective date is on or before the first day of the tax year (or that this is the first S year). If the user says the election was filed late or never acknowledged, stop and route to [`form-2553`](../form-2553/SKILL.md). Record item G: "Yes" only if the corporation is electing S status beginning with this tax year.

### Step 2 — Run the boundary screen

Screen for each item below. Compute only the screen arithmetic shown in [`references/schedules-l-m1-m2.md`](./references/schedules-l-m1-m2.md), section 6 (for example, the 25% passive income test); never compute an entity-level tax or make an election. Each failed screen goes into the validation summary as a boundary flag with a referral to a CPA, and the dependent lines are marked "PENDING — CPA" or "PROVISIONAL":

- Former C corporation or C-corporation assets acquired with carryover basis → possible built-in gains tax (line 23b; Schedule D (Form 1120-S), Part III; 5-year recognition period under §1374(d)(7)) and Schedule B question 8 entry
- AE&P at year end plus passive investment income above 25% of gross receipts → possible excess net passive income tax (line 23a) and, after 3 consecutive years, termination of the election (§1362(d)(3))
- LIFO recapture installments (line 23a)
- Total assets of $10 million or more → Schedule M-3 instead of M-1 (instructions, Schedule M-1)
- Foreign activity that fails the domestic filing exception → Schedules K-2 and K-3
- Section 1377(a)(2) terminating election or §1.1368-1(g)(2) qualifying-disposition election (all affected shareholders must consent; statement attached)
- More than one at-risk or passive activity, rental real estate (Form 8825), oil and gas, credits with recapture

Detail for each flag: [`references/schedules-l-m1-m2.md`](./references/schedules-l-m1-m2.md) (entity-level taxes) and [`references/schedule-k-and-k1.md`](./references/schedule-k-and-k1.md) (allocation elections, K-2/K-3).

### Step 3 — Classify every book item

Assign each trial-balance amount to exactly one destination:

| Item | Destination |
|---|---|
| Trade or business receipts and expenses | Page 1, lines 1a–20 |
| Interest, dividends, royalties not from the ordinary course of business | Schedule K, lines 4, 5a, 6 |
| Capital gains and losses | Schedule D (Form 1120-S) → Schedule K, lines 7, 8a |
| Section 1231 gains and losses | Form 4797 → Schedule K, line 9 |
| Ordinary gain from sale of business property | Form 4797, Part II, line 17 → page 1, line 4 |
| Section 179 expense | Schedule K, line 11 (never page 1) |
| Charitable contributions | Schedule K, lines 12a/12b (never page 1) |
| Rental real estate | Form 8825 → Schedule K, line 2 |
| Tax-exempt income; nondeductible expenses | Schedule K, lines 16a/16b; 16c |
| Distributions to shareholders | Schedule K, line 16d (never a deduction) |

Ask about any item that does not fit. Example question: "Was the $1,083 of interest earned on the operating bank account, or charged to customers on overdue invoices?" Bank interest is portfolio income (Schedule K, line 4); interest on receivables in the ordinary course of business is page 1, line 5.

### Step 4 — Officer compensation (line 7) and wages (line 8)

Follow [`references/officer-compensation.md`](./references/officer-compensation.md). In short: line 7 holds compensation of officers as defined by state law; line 8 holds wages of non-officers; fringe benefits (including health insurance) for any more-than-2% shareholder go on line 7 or 8, whichever applies, and into that person's W-2 box 1, not on line 18. Reconcile line 7 plus line 8 (plus any wages in cost of goods sold) to the Forms W-2 and the four Forms 941. Attach Form 1125-E when total receipts are $500,000 or more.

If an officer-shareholder performed services and line 7 is zero (or the user describes wages that never ran through payroll), stop and ask before continuing. Do not supply a wage figure; record the issue as an open item.

### Step 5 — Page 1 income and deductions

Compute lines 1a–22 per [`references/line-by-line.md`](./references/line-by-line.md). Attach Form 1125-A if line 2 is used and Form 4562 if property was placed in service or listed property is claimed. Keep line 20 itemized in a statement. Line 22 flows to Schedule K, line 1.

### Step 6 — Tax and payments (lines 23a–28e)

Lines 23a–23c are entity-level taxes. Enter zero only after Step 2 found no flags. If a flag is open, mark the lines "PENDING — CPA" and say why. Then enter payments (24a–24d), the Form 2220 penalty (25), and compute line 26 or 27; split any overpayment between 28a (credit to 2026 estimated tax, irrevocable) and 28b (refund), with direct deposit on 28c–28e.

### Step 7 — Schedule B

Answer all 17 items (item 17 is reserved). Questions 3, 4a/4b, 9, 10, 11, 12, 14a/14b and 16 are the ones a small corporation most often gets wrong; see the line-by-line reference.

### Step 8 — Schedule K

Total every separately stated item for the corporation. Compute line 18: lines 1 through 10 combined, minus lines 11 through 12e and 16f. Line 17d carries coded statements: code V (Section 199A, Statement A) for every corporation with a trade or business, code AC (gross receipts for §448(c)) when needed.

### Step 9 — Schedule B question 11 and Schedules L, M-1, M-2

Total receipts = line 1a + lines 4 and 5 + Schedule K lines 3a, 4, 5a, 6 + income or net gain on Schedule K lines 7, 8a, 9, 10 + Form 8825 lines 2, 21, 22a. If total receipts are under $250,000 and year-end total assets are under $250,000, answer "Yes": Schedules L and M-1 are not required. Item F (total assets) is required either way. Schedule M-2 is not excused by question 11; complete the AAA column every year. Mechanics: [`references/schedules-l-m1-m2.md`](./references/schedules-l-m1-m2.md).

### Step 10 — Schedules K-1

For each person who was a shareholder at any time during the year, compute item G (current-year allocation percentage, weighted by days held) and multiply each Schedule K amount by it. Report distributions (16d) and loan repayments (16e) to the shareholder who actually received them. Attach Statement A for code V. Apply the K-2/K-3 domestic filing exception or the small S corporation exception, or flag. Tell each shareholder to complete Form 7203 when they claim a loss, receive a non-dividend distribution, dispose of stock, or receive a loan repayment. See [`references/schedule-k-and-k1.md`](./references/schedule-k-and-k1.md).

### Step 11 — Validate

Run every check under **Validation**. Surface failures; do not silently fix them.

### Step 12 — Produce the deliverable and hand off to filing

Emit the draft in the **Output format** below. If the user wants help filing, follow [`filing.md`](./filing.md): e-file through an authorized provider (mandatory when the corporation is required to file 10 or more returns of any type during the calendar year ending with or within its tax year), or paper to the address in the instructions. Never submit without explicit consent at submission time.

---

## Line-by-line guidance

Full map of every line: [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

### Key numbers (2025 revision, filed in 2026; year-dependent values flagged)

| Item | Value | Source |
|---|---|---|
| Due date | 15th day of the 3rd month after year end; calendar 2025 returns due March 16, 2026 (March 15 was a Sunday) | Instructions, When To File; IRC §6072(b) |
| Extension | Form 7004 by the original due date, code 25; 6 months; does not extend payment of line 23c tax | Form 7004 and its instructions (Rev. Dec. 2025) |
| Late or incomplete return (§6699) | $255 × shareholders during the year × months late (max 12), returns required to be filed in 2026; $260 for returns required to be filed in 2027 (year-dependent) | Instructions, Late filing of return; Rev. Proc. 2025-32 §4.56 |
| If tax is due | plus 5% of unpaid tax per month (max 25%); minimum for a return more than 60 days late is the smaller of the tax due or $525 (2026 filings; $535 for 2027 filings) | Instructions; IRC §6651(a); Rev. Proc. 2025-32 §4.52 |
| Late payment | 0.5% of unpaid tax per month, max 25% | Instructions, Late payment of tax |
| K-1 not furnished or wrong | $340 per K-1; $680 or 10% if intentional (year-dependent) | Instructions, Failure to furnish information timely; IRC §6722 |
| Skip Schedules L and M-1 | Schedule B, question 11: total receipts AND year-end total assets both under $250,000 | Form 1120-S, page 2 |
| Form 1125-E | Total receipts of $500,000 or more | Instructions, lines 7 and 8 |
| Schedule M-3 | Total assets of $10 million or more at year end | Instructions, Schedule M-1 |
| E-file mandate | Required to file 10 or more returns of any type (income, employment, excise, information returns) during the calendar year ending with or within the tax year | Instructions, Electronic Filing; Reg. §301.6037-2(a)(1), (d)(5) |
| Estimated tax (entity taxes only) | Built-in gains, excess net passive income and investment credit recapture taxes totaling $500 or more; due 15th day of months 4, 6, 9, 12 | Instructions, Estimated Tax Payments |

### Header (items A–J)

- **A** S election effective date from the IRS acceptance letter. **B** principal business activity code. **C** check only if Schedule M-3 is attached. **D** EIN ("Applied for" plus date only on a paper return; e-file requires the EIN). **E** date incorporated. **F** total assets per books at year end; equals Schedule L, line 15, column (d) when Schedule L is completed; enter -0- if none.
- **G** "Yes" only if the corporation is electing S status beginning with this tax year (attach Form 2553 if not already filed; a Form 2553 filed with the return is generally late).
- **H** (1) final return (also "Final K-1" on each K-1), (2) name change, (3) address change, (4) amended return (attach a statement of each changed line; check "Amended K-1"), (5) S election termination.
- **I** number of persons who were shareholders during any part of the year. This count also drives the §6699 late-filing penalty.
- **J** aggregation for §465 or grouping for §469, only when the corporation actually made that choice.

### Income (lines 1a–6)

Only trade or business income. No rental income, no portfolio income, no tax-exempt income on lines 1a–5. Line 2 comes from Form 1125-A, line 8. Line 4 is ordinary gain or loss from Form 4797, Part II, line 17. Line 5 carries other business income (interest on customer receivables, recoveries of bad debts, §280F recapture, positive §481(a) adjustments) with a statement.

### Deductions (lines 7–22)

- **7 / 8** See Step 4. Elective 401(k), salary-reduction SEP and SIMPLE IRA contributions are not included on lines 7 or 8 (instructions, lines 7 and 8).
- **12** Taxes and licenses: employer payroll taxes, state and local taxes, licenses. Never federal income tax (except the portion of built-in gains tax allocable to ordinary income).
- **13** Business interest only; interest allocable to rental activities, investment property or debt-financed distributions goes elsewhere. §163(j) applies unless the corporation is a small business taxpayer (average annual gross receipts of $31 million or less for the 3 prior years, not a tax shelter).
- **14** Depreciation from Form 4562, excluding section 179 (passes through on Schedule K, line 11). For 2025, 100% special depreciation applies to certain property acquired after January 19, 2025 (Instructions for Form 4562, 2025).
- **18** Fringe benefits only for employees owning 2% or less.
- **20** Other deductions with a statement: amortization, start-up and organizational costs, insurance, legal and professional fees, supplies, utilities, travel, 50% of meals. Lobbying, fines, and expenses related to tax-exempt income are Schedule K, line 16c items.

### Tax and payments (lines 23a–28e)

- **23a** Excess net passive income tax (worksheet, 21% rate) or LIFO recapture installment. **23b** built-in gains tax from Schedule D (Form 1120-S), line 23. **23c** = 23a + 23b plus Form 4255 and look-back interest items noted to the left of the entry.
- **24a** estimated payments and prior overpayment credited; **24b** Form 7004 deposit; **24c** Form 4136; **24d** elective payment election amount from Form 3800; **24z** total.
- **25** Form 2220 penalty (check the box if attached). **26** amount owed = (23c + 25) − 24z when positive; pay electronically. **27** overpayment; **28a/28b** split; **28c–28e** routing (9 digits), account type, account number.

### Schedule B (items 1–17)

- **1** accounting method; changing it needs Form 3115. **2** activity and product or service (same code list as item B).
- **3** any shareholder that is a disregarded entity, trust, estate, or nominee → "Yes" requires Schedule B-1.
- **4a / 4b** ownership of 20% directly or 50% directly or indirectly of a corporation or partnership (§267(c) attribution) → list each.
- **8** net unrealized built-in gain less prior net recognized built-in gain; former C corporations only (boundary flag).
- **9 / 10** §163(j): real property or farming election in effect; Form 8990 conditions (pass-through excess interest, gross receipts above $31 million with business interest, tax shelter).
- **11** the $250,000 test (Step 9). **12** non-shareholder debt canceled or modified (amount). **13** QSub election terminated or revoked.
- **14a / 14b** payments requiring Forms 1099 in the tax year, and whether they were or will be filed. **15** Qualified Opportunity Fund (Form 8996). **16** digital assets received or disposed of; must be answered "Yes" or "No".

### Schedules K and K-1

Schedule K is the corporation's total; each K-1 is one shareholder's share. Allocation when ownership changed during the year (Instructions, item G):

```
Item G % = Σ over periods ( % of shares held in period × days in period ) ÷ days in tax year
K-1 amount = Schedule K amount × Item G %   (round; put any $1 rounding difference on one shareholder and say so)
```

A shareholder who disposes of stock counts as a shareholder on the day of disposition. The closing-of-the-books alternatives need consent of all affected shareholders and a statement attached to a timely return. Distributions on line 16d are not income and not a deduction; they reduce AAA and stock basis. Dividend distributions from AE&P go on line 17c and Form 1099-DIV, not on any K-1. S corporation income is not self-employment income (Shareholder's Instructions for Schedule K-1 (Form 1120-S), 2025).

### Schedules L, M-1, M-2

Schedule L per books, beginning and end. Schedule M-1 line 8 must equal Schedule K, line 18. Schedule M-2 column (a) is the AAA; distributions cannot reduce it below zero, and the year's net negative adjustment is applied after distributions.

---

## Validation

### Math checks (block the draft on any failure)

- [ ] 1c = 1a − 1b; 3 = 1c − 2; 6 = 3 + 4 + 5
- [ ] 21 = sum of lines 7 through 20; 22 = 6 − 21
- [ ] 23c = 23a + 23b (+ itemized additions); 24z = 24a + 24b + 24c + 24d
- [ ] Exactly one of line 26 or line 27 is non-zero (or both zero); 28a + 28b = 27
- [ ] Line 2 = Form 1125-A, line 8; line 7 = Form 1125-E, line 4 when 1125-E is required
- [ ] Line 20 = total of the attached statement
- [ ] Schedule K, line 1 = page 1, line 22
- [ ] Schedule K, line 18 = lines 1 through 10 − (lines 11 through 12e + 16f)
- [ ] Item G percentages across all K-1s total 100%; each K-1 box total across shareholders equals the Schedule K line (after rounding adjustment)
- [ ] Sum of K-1 box 16 code D amounts = Schedule K, line 16d
- [ ] If Schedule L completed: line 15 (d) = item F; line 27 = line 15 in both columns; line 19 reconciles to the sum of K-1 item I
- [ ] If Schedule M-1 completed: line 8 = Schedule K, line 18
- [ ] Schedule M-2 column (a): line 6 = lines 1 + 2 + 3 − 4 − 5; line 8 = 6 − 7; line 7 does not create a negative balance

### Sanity checks (warn, do not block)

- [ ] Officer-shareholder performed services and line 7 is zero or far below distributions on line 16d → ask; record as open item
- [ ] Line 7 + line 8 (+ wages in COGS) differs from W-2 and Form 941 totals
- [ ] More-than-2% shareholder health insurance on line 18 instead of line 7/8
- [ ] Section 179 or charitable contributions on page 1
- [ ] Bank interest or dividends on page 1
- [ ] Distributions not proportional to shares on each distribution date (one-class-of-stock risk under Reg. §1.1361-1(l)); ask and refer to a CPA
- [ ] Total receipts ≥ $500,000 and no Form 1125-E
- [ ] Question 11 answered "Yes" but either total exceeds $249,999
- [ ] Loss on line 22 or distributions above AAA → remind shareholders of basis limits and Form 7203
- [ ] Any Step 2 flag still open

### Cross-form checks

- [ ] Forms W-2/W-3 and four Forms 941 filed for officer wages
- [ ] Forms 1099 filed if Schedule B, question 14a is "Yes"
- [ ] K-1s (and K-3s when required) furnished to shareholders by the return due date
- [ ] Form 7004 filed by the original due date if the return will be late

---

## Output format

```markdown
# Form 1120-S — DRAFT for tax year YYYY (2025 revision)
Corporation: <name> | EIN: <EIN> | Calendar / fiscal <dates>

## Header
A S election effective date: MM/DD/YYYY     B Activity code: <code>
C Schedule M-3 attached: No                 D EIN: <EIN>
E Date incorporated: MM/DD/YYYY             F Total assets: $X
G Electing S beginning this year: Yes | No
H Boxes checked: none | (1)…(5)             I Number of shareholders: N
J Aggregation/grouping: none

## Page 1 (every line, including zeros)
1a $X  1b $X  1c $X | 2 $X | 3 $X | 4 $X | 5 $X | 6 $X
7 $X  8 $X  9 $X  10 $X  11 $X  12 $X  13 $X  14 $X  15 $X
16 $X  17 $X  18 $X  19 $X  20 $X (statement attached) | 21 $X | 22 $X
23a $X  23b $X  23c $X | 24a $X  24b $X  24c $X  24d $X  24z $X
25 $X | 26 $X | 27 $X | 28a $X  28b $X  28c <routing>  28d <type>  28e <acct, masked>

## Line 20 statement | Form 1125-A summary | Form 1125-E table (if required)

## Schedule B (items 1–17, Yes/No and entries)

## Schedule K (every line 1–18 with amount or 0; codes for 10, 12d/e, 13, 15, 16, 17d)

## Schedule B question 11 test
Total receipts: $X (components listed) | Year-end total assets: $X | Answer: Yes | No

## Schedule L / Schedule M-1 (or "Not required — Schedule B, question 11 = Yes")

## Schedule M-2 (columns a–d, lines 1–8)

## Schedules K-1 (one block per shareholder)
Items A–I | Item G calculation (shares × days) | Boxes 1–17 with codes | Statement A summary
Form 7203 reminder: yes/no and why

## Required attachments
- [ ] Form 1125-A  - [ ] Form 1125-E  - [ ] Form 4562  - [ ] Form 4797  - [ ] Schedule D (1120-S)
- [ ] Form 8825    - [ ] Schedule B-1  - [ ] Statement A  - [ ] K-2/K-3 or exception statement

## Validation summary
Math: pass | <failures>   Sanity: <warnings>   Boundary flags: <open items>   Open questions: <list>

## Sources cited in this draft
- Form 1120-S (2025) and Instructions for Form 1120-S (2025), with page/line references
- Schedule K-1 (Form 1120-S) (2025) and Shareholder's Instructions (2025)
- IRC sections and Rev. Procs. relied on
```

Mask SSNs, EINs of shareholders and bank account numbers in any shared draft except the copy the user files.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of Form 1120-S (header, page 1, Schedules B, K, L, M-1, M-2) and Schedule K-1 items A–I and boxes 1–19, from the 2025 PDF text
- [`references/officer-compensation.md`](./references/officer-compensation.md) — line 7 versus line 8, more-than-2% shareholder fringe benefits, Form 1125-E, payroll reconciliation, and the reasonable-compensation questions to ask
- [`references/schedule-k-and-k1.md`](./references/schedule-k-and-k1.md) — Schedule K totals, per-share per-day allocation, §1377(a)(2) and qualifying-disposition elections, coded items and Statement A, K-2/K-3 exceptions, Form 7203 handoff
- [`references/schedules-l-m1-m2.md`](./references/schedules-l-m1-m2.md) — the $250,000 test, Schedule L, M-1, M-2 and AAA ordering, M-3 boundary, built-in gains and excess net passive income flags
- [`references/common-mistakes.md`](./references/common-mistakes.md) — the errors that most often break a Form 1120-S, with fixes
- [`filing.md`](./filing.md) — channel decision tree, e-file mandate, mailing addresses, payments, consent and security rules

## Examples

- [`examples/single-owner-design-studio.md`](./examples/single-owner-design-studio.md) — one shareholder-officer, cash basis, under the $250,000 test, health insurance on line 7, AAA roll-forward, Form 7203 handoff
- [`examples/three-shareholder-retailer.md`](./examples/three-shareholder-retailer.md) — inventory, accrual basis, mid-year share sale with daily allocation, Form 1125-E, Schedules L and M-1, section 179 and charitable items on Schedule K
- [`examples/former-c-corp-flags.md`](./examples/former-c-corp-flags.md) — converted C corporation with AE&P and a built-in gain sale; the agent drafts what it can and stops lines 23a–23c at boundary flags

## Sources

Re-verify each source for the tax year being filed.

- [Form 1120-S (2025)](https://www.irs.gov/pub/irs-pdf/f1120s.pdf) and [Instructions for Form 1120-S (2025)](https://www.irs.gov/pub/irs-pdf/i1120s.pdf)
- [About Form 1120-S](https://www.irs.gov/forms-pubs/about-form-1120-s) — current and prior revisions
- [Schedule K-1 (Form 1120-S) (2025)](https://www.irs.gov/pub/irs-pdf/f1120ssk.pdf) and [Shareholder's Instructions for Schedule K-1 (Form 1120-S) (2025)](https://www.irs.gov/pub/irs-pdf/i1120ssk.pdf)
- [S Corporation Instructions for Schedules K-2 and K-3 (Form 1120-S) (2025)](https://www.irs.gov/pub/irs-pdf/i1120s23.pdf)
- [Instructions for Schedule D (Form 1120-S) (2025)](https://www.irs.gov/pub/irs-pdf/i1120ssd.pdf) — built-in gains tax, Part III
- [Form 1125-E (Rev. October 2016)](https://www.irs.gov/pub/irs-pdf/f1125e.pdf); [Instructions for Form 7203](https://www.irs.gov/pub/irs-pdf/i7203.pdf); [Instructions for Form 4562 (2025)](https://www.irs.gov/pub/irs-pdf/i4562.pdf); [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf)
- [IRS: S Corporation Compensation and Medical Insurance Issues](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues)
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — §6699 amount for returns required to be filed in 2027; §6041 reporting threshold for payments after 2025
- [Rev. Proc. 2019-11](https://www.irs.gov/pub/irs-drop/rp-19-11.pdf) — methods for figuring W-2 wages for §199A
- IRC §§1361, 1362, 1363(d), 1366, 1367, 1368, 1374, 1375, 1377, 3111, 6037, 6651, 6699, 6722
- Treas. Reg. §§1.1361-1(l), 1.1368-1(g)(2), 1.1377-1(b), 301.6037-2

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions and publications. It is not tax or legal advice and does not create a CPA-client relationship. Remind the user that the draft is a starting point; former C corporations, mid-year ownership changes, multiple activities, foreign items and any open boundary flag call for a licensed tax professional's review.
