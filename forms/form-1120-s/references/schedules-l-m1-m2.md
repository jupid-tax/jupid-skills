# Schedules L, M-1, M-2, the $250,000 Test, and Entity-Level Tax Flags (Form 1120-S)

Covers Schedule B question 11, the balance sheet (Schedule L), the book-to-return reconciliation (Schedule M-1, and when Schedule M-3 replaces it), the accumulated adjustments account and the other Schedule M-2 columns, distribution ordering, and the three entity-level taxes that the agent screens for but does not compute. Sources: 2025 Form 1120-S, pages 2–5; 2025 Instructions for Form 1120-S (Question 11; Schedule L; Schedule M-1; Schedule M-2; Distributions; lines 23a–23c; Estimated Tax Payments); 2025 Instructions for Schedule D (Form 1120-S), Part III; 2025 S Corporation Instructions for Schedules K-2 and K-3.

---

## 1. Schedule B, question 11: the $250,000 test

Question 11 asks whether both are true:

- (a) total receipts for the tax year were less than $250,000, and
- (b) total assets at the end of the tax year were less than $250,000.

**Total receipts** (Instr., Question 11) = page 1 line 1a + page 1 lines 4 and 5 + income reported on Schedule K lines 3a, 4, 5a, 6 + income or net gain reported on Schedule K lines 7, 8a, 9, 10 + income or net gain reported on Form 8825 lines 2, 21, 22a. Use gross receipts on line 1a (before returns and allowances). Add only income or net gains on the K lines; a net loss on line 7, 8a, 9 or 10 adds nothing.

**Total assets** = year-end total assets per the books (the same figure as item F).

| Answer | Consequence |
|---|---|
| "Yes" | Schedules L and M-1 not required (form text). Schedules K-2 and K-3 also not required (Small S Corporation Filing Exception, K-2/K-3 Instructions, 2025) |
| "No" | Complete Schedules L and M-1 (or M-3) |
| Either | Item F is still required. Schedule M-2 is still on the form; question 11 does not excuse it. Complete column (a) every year so next year's AAA is not a guess |

Work the test as a table in the draft:

```
Line 1a gross receipts                         $_____
Lines 4 + 5                                    $_____
Schedule K 3a, 4, 5a, 6                         $_____
Schedule K 7, 8a, 9, 10 (income or net gain)   $_____
Form 8825 lines 2, 21, 22a                     $_____
Total receipts                                 $_____   < $250,000?  Y/N
Year-end total assets (item F)                 $_____   < $250,000?  Y/N
Question 11                                    Yes only if both Y
```

The same total-receipts figure decides Form 1125-E (required at $500,000 or more).

---

## 2. Schedule L — balance sheets per books

- Agree to the corporation's books and records, beginning and end of year. The beginning columns equal last year's ending columns; if they do not, ask why (restatement, prior-year error, first year).
- Line 15, column (d) = item F on page 1.
- Line 27 = line 15 in both the beginning and ending columns.
- Line 19 (loans from shareholders) reconciles to the sum of item I on all K-1s. Line 7 (loans to shareholders) deserves a question: "Is there a signed note with interest and repayments? If not, the IRS may treat the balance as a distribution." Record the answer; do not reclassify.
- Line 24 retained earnings is a book figure. It is not the AAA. If the S election terminated during the year, see the Instructions for which short year's balance sheet to use.

---

## 3. Schedule M-1 — book income to Schedule K, line 18

| Line | What goes here | Typical small-corporation items |
|---|---|---|
| 1 | Net income (loss) per books | From the income statement |
| 2 | Income on K lines 1, 2, 3c, 4, 5a, 6, 7, 8a, 9, 10 not on the books | Rare for small corporations |
| 3a | Book expense not on K lines 1–12e or 16f: depreciation | Book depreciation above tax depreciation |
| 3b | Travel and entertainment | Nondeductible 50% of meals, entertainment, QTFs, gifts over $25, club dues |
| 4 | Lines 1 + 2 + 3 | |
| 5a | Book income not on K lines 1–10: tax-exempt interest | Also other tax-exempt income, itemized |
| 6a | K deductions not charged against book income: depreciation | Section 179 and bonus depreciation above book depreciation |
| 7 | Lines 5 + 6 | |
| 8 | Line 4 − line 7 | Must equal Schedule K, line 18 |

If line 8 does not equal Schedule K, line 18, list the difference and stop. Do not plug.

**Schedule M-3 boundary.** Corporations with total assets of $10 million or more at year end file Schedule M-3 (Form 1120-S) instead of M-1, and check item C. A corporation required to file M-3 with less than $50 million of total assets (or a voluntary filer) may complete M-3 Part I and Schedule M-1 instead of M-3 Parts II and III, with M-1 line 1 equal to M-3 Part I line 11 (Instr., Schedule M-1). Treat any M-3 return as outside this skill's scope: draft page 1 and Schedule K, flag M-3 for a CPA, and use the Ogden address in `filing.md`.

---

## 4. Schedule M-2 — the four columns

### Column (a): accumulated adjustments account (AAA)

The AAA starts at zero on the first day of the first S year (Instr., Schedule M-2). Corporations with AE&P must maintain it; the Instructions recommend that every S corporation maintain it. Adjust at year end in this order (Instr., Column (a)):

1. Increase by income (other than tax-exempt income), and excess depletion over basis.
2. Decrease by deductible losses and expenses, nondeductible expenses (other than those related to tax-exempt income), and oil and gas depletion. If these decreases exceed the increases in (1), the excess is a "net negative adjustment": do not take it into account here.
3. Decrease (not below zero) by distributions other than dividend distributions from AE&P.
4. Decrease by any net negative adjustment. The AAA may end negative (§1368(e)).

Mapping to the form lines:

```
Line 1  Beginning AAA (prior year line 8, column (a))
Line 2  Page 1, line 22 income
Line 3  Other additions: K lines 2 (if income), 3c, 4, 5a, 6, 7, 8a, 9, 10 income items
Line 4  Page 1, line 22 loss (in parentheses)
Line 5  Other reductions: K 11, 12a–12e, 16c (except expenses of tax-exempt income), 16f, separately stated losses
Line 6  Lines 1 + 2 + 3 − 4 − 5
Line 7  Distributions charged to AAA (not more than line 6 figured without the net negative adjustment, and not below zero)
Line 8  Line 6 − line 7
```

When total distributions exceed the AAA available, the AAA is allocated pro rata among the year's distributions (§1368; Instr., Distributions). Hand any such year to a CPA if the corporation has AE&P (part of the excess may be a dividend).

### Column (b): shareholders' undistributed taxable income previously taxed (PTEP)

Only for corporations that had a balance at the start of the 2025 tax year (pre-1983 S corporation history). No additions; reduced only for §1375(d) (pre-1983) distributions. Flag if present.

### Column (c): accumulated earnings and profits (AE&P)

Only for former C corporations or corporations that absorbed a C corporation in a tax-free reorganization. Carry the balance forward; it changes only for dividend distributions, redemptions and reorganizations, and investment credit recapture (Instr., Distributions, item 3; §1371(c)). Estimates based on retained earnings are acceptable when computing it (Instr., Column (c)). Any AE&P balance is a boundary flag: it enables the excess net passive income tax and changes distribution taxation.

### Column (d): other adjustments account (OAA)

Adjusted for tax-exempt income (and related expenses) and federal taxes attributable to a C corporation year; then reduced for distributions (Instr., Column (d)).

### Instructions example (no PTEP, no AE&P)

Page 1 line 22 income $10,000; K line 2 loss ($3,000); K line 4 $4,000; K line 5a $16,000; K line 12a $24,000; K line 12e $3,000; K line 16a tax-exempt interest $5,000; K line 16c $6,000; K line 16d distributions $65,000. Column (a): line 1 $0; line 2 $10,000; line 3 $20,000; line 5 ($36,000); line 6 ($6,000) is a net negative adjustment, so distributions cannot reduce the AAA (line 7 $0) and line 8 is ($6,000). Column (d): line 3 $5,000; line 7 $5,000; line 8 $0. The remaining $60,000 of distributions is not entered on Schedule M-2 (Instr., Schedule M-2 Example).

---

## 5. Distribution ordering (for the draft's notes, not for elections)

General rule (Instr., Distributions; §1368):

1. AAA (figured without the year's net negative adjustment; not below zero)
2. PTEP (§1375(d) as in effect before 1983)
3. AE&P → dividend, reported on Schedule K line 17c and Form 1099-DIV, not on K-1
4. Other adjustments account
5. Remaining shareholders' equity accounts

For a corporation with no AE&P, distributions are not dividends; each shareholder applies them against stock basis (box 16, code D; Form 7203).

Elections that change the order (distribute AE&P first; deemed dividend; forgo PTEP) require the consent of all affected shareholders and a statement attached to a timely filed return (Instr., Elections relating to source of distributions; Reg. §1.1368-1(f)). They are tax planning decisions: list them as options for the CPA, never make them.

---

## 6. Entity-level taxes: screen, compute the screen, then stop

These taxes generally reach only corporations that were C corporations or acquired C-corporation assets with carryover basis (Instr., line 23a; Schedule D (Form 1120-S) Instructions, Part III). The agent runs the screen, shows its arithmetic, and marks the tax lines "PENDING — CPA" when a screen is failed. It never enters a computed built-in gains or excess net passive income tax as final.

### Screen 1 — Excess net passive income tax (line 23a)

Applies only if, at the close of the tax year, the corporation has AE&P AND passive investment income exceeds 25% of gross receipts (Instr., line 23a). Worksheet lines 1–3:

```
1. Gross receipts for the tax year (see §1362(d)(3)(B) for capital asset sales)
2. Passive investment income (§1362(d)(3)(C))
3. Line 1 × 25%   → if line 2 is less than line 3, stop: no tax
```

If line 2 exceeds line 3 and there is AE&P, flag: the tax is line 10 × 21% after worksheet lines 4–10 and a taxable-income computation using Form 1120 lines 1–28, and three consecutive such years terminate the election (§1362(d)(3); Instr., Termination of Election). Passive investment income passed through is reduced by its share of this tax (§1366(f)(3)).

### Screen 2 — Built-in gains tax (line 23b)

Applies when the corporation disposes of an asset held on the first day of its first S year (or acquired from a C corporation with carryover basis) during the 5-year recognition period beginning on that day or the acquisition date (Schedule D (Form 1120-S) Instructions, Part III). Ask: "Did the corporation sell or dispose of any asset this year that it held when it converted from a C corporation (or acquired from a C corporation)? What was its fair market value and adjusted basis on the conversion date?"

Schedule D (Form 1120-S), Part III structure: line 16 recognized built-in gains over losses; line 17 taxable income; line 18 smallest of line 16, line 17, or Schedule B line 8; line 19 §1374(b)(2) deduction; line 20 = 18 − 19; line 21 = 21% of line 20; line 22 C-year credit carryforwards; line 23 tax → page 1 line 23b. Also complete Schedule B, item 8 (net unrealized built-in gain reduced by prior net recognized built-in gain).

What the agent may show: the inputs, the gain recognized on each asset, the built-in gain at conversion, and an upper bound of 21% × the lesser of those two amounts, labeled "upper bound before limitations; CPA to compute". The portion of the tax allocable to ordinary income is deductible on line 12 (Instr., line 12), so line 12, line 22 and every K-1 are provisional until the CPA fixes line 23b.

### Screen 3 — LIFO recapture (line 23a)

Applies if the corporation used LIFO in its last C year (or received LIFO inventory from a C corporation). The tax is figured for the last C year and paid in four equal installments; the S corporation pays the remaining three with its next three Forms 1120-S, noted as "LIFO tax" to the left of line 23a (Instr., line 23a). Ask for the installment schedule; enter only the amount the user documents.

### Estimated tax for entity-level taxes

Required when the built-in gains, excess net passive income and investment credit recapture taxes total $500 or more; four installments due the 15th day of the 4th, 6th, 9th and 12th months (for calendar 2026: April 15, June 15, September 15, December 15), paid by electronic funds transfer; Form 2220 for any penalty (Instr., Estimated Tax Payments). Flag for the CPA whenever a screen fails.
