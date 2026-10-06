# Officer Compensation on Form 1120-S (Lines 7 and 8)

How to place officer and shareholder pay on the 2025 Form 1120-S, what to reconcile it to, and which questions to ask. The agent never chooses, estimates, or suggests a salary amount. Reasonable compensation is a fact the corporation must establish with its own evidence and, where in doubt, a CPA. The agent's job is to report what was actually paid, tie it to payroll filings, and surface the risk when the facts look wrong.

Sources: 2025 Instructions for Form 1120-S, lines 7, 8, 17, 18; Form 1125-E (Rev. October 2016); IRS page "S Corporation Compensation and Medical Insurance Issues" (https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues); IRC §1366(e); IRC §3111.

---

## The rule in the instructions

The 2025 instructions print this caution at lines 7 and 8:

> "Distributions and other payments by an S corporation to a corporate officer must be treated as wages to the extent the amounts are reasonable compensation for services rendered to the corporation."

And: "If a shareholder or a member of the family of one or more shareholders of the corporation renders services or furnishes capital to the corporation for which reasonable compensation isn't paid, the IRS may make adjustments in the items taken into account by such individuals to reflect the value of such services or capital. See section 1366(e)."

The IRS compensation page adds that S corporations "must pay reasonable compensation to a shareholder-employee in return for services that the employee provides to the corporation before non-wage distributions may be made," and that the amount "will never exceed the amount received by the shareholder either directly or indirectly."

---

## Which line

| Person | Wages | Health insurance and other fringe benefits |
|---|---|---|
| Officer (state-law definition) owning more than 2% | Line 7 | Line 7, and in W-2 box 1 |
| Officer owning 2% or less | Line 7 | Line 18 |
| Non-officer employee owning more than 2% | Line 8 | Line 8, and in W-2 box 1 |
| Non-officer employee owning 2% or less | Line 8 | Line 18 |
| Anyone, wages included in cost of goods sold | Form 1125-A, not lines 7/8 | — |

More-than-2% means owning on any day of the tax year more than 2% of outstanding stock or of combined voting power, with §318 attribution (Instr., line 18). Elective 401(k) deferrals, salary-reduction SEP and SIMPLE IRA contributions are excluded from lines 7 and 8 (Instr., lines 7 and 8); employer plan contributions go on line 17.

Health insurance for a more-than-2% shareholder (including spouse, dependents, children under 27): reported in W-2 box 1, and per the IRS compensation page not in boxes 3 and 5 when paid under a plan for all or a class of employees; reported as an information item in W-2 box 14 (Instr., lines 7 and 8). The shareholder may deduct it on Schedule 1 (Form 1040), line 17. Employer FICA on line 12 is figured on box 3/box 5 wages, so it does not apply to that premium amount.

---

## Form 1125-E

Required when total receipts are $500,000 or more. Total receipts = page 1 line 1a + lines 4 and 5 + income on Schedule K lines 3a, 4, 5a, 6 + income or net gain on Schedule K lines 7, 8a, 9, 10 + income or net gain on Form 8825 lines 2, 21, 22a (Instr., lines 7 and 8).

Form 1125-E columns, per officer: (a) name, (b) SSN, (c) percent of time devoted to business, (d) percent of common stock owned, (e) percent of preferred stock owned, (f) amount of compensation. Line 2 = total; line 3 = officer compensation claimed on Form 1125-A or elsewhere; line 4 = line 2 − line 3 → Form 1120-S, line 7.

---

## Questions to ask (in this order)

1. "Who are the corporation's officers under its bylaws or state law, and what percent of the stock does each own?"
2. "For each officer, what were the total Form W-2 box 1, box 3 and box 5 amounts for the year?" Ask for the W-2s or the payroll year-end report.
3. "Did the corporation pay health insurance premiums for any shareholder who owns more than 2%? Was that amount included in their W-2 box 1?"
4. "Do the four Forms 941 for the year agree with those W-2 totals?" If the user has not filed Forms 941, stop: the payroll filings come first ([`../../form-941/SKILL.md`](../../form-941/SKILL.md)).
5. "Did any shareholder who works in the business receive distributions but no W-2 wages?" If yes, ask question 6.
6. "What services did that shareholder perform, roughly how many hours, and how did the corporation decide what to pay them?" Record the answer verbatim in the open items. Do not convert it into a salary number.

If the user asks the agent what salary to pay, answer with the factors below and refer to a CPA. Do not name a figure, a percentage of profit, or a "rule of thumb".

---

## Factors the IRS lists (for the user's own analysis)

From the IRS compensation page: training and experience; duties and responsibilities; time and effort devoted to the business; dividend history; payments to non-shareholder employees; timing and manner of paying bonuses to key people; what comparable businesses pay for similar services; compensation agreements; the use of a formula to determine compensation.

The same page frames the analysis by the source of gross receipts: services of the shareholder, services of non-shareholder employees, and capital and equipment. Receipts generated by the shareholder's personal services (and administrative work supporting other income producers) point toward wage treatment.

Court cases the IRS page cites: *Joly v. Commissioner*, T.C. Memo. 1998-361, aff'd 211 F.3d 1269 (6th Cir. 2000); *Veterinary Surgical Consultants, P.C. v. Commissioner*, 117 T.C. 141 (2001); *Joseph M. Grey Public Accountant, P.C. v. Commissioner*, 119 T.C. 121 (2002); *David E. Watson, P.C. v. United States*, 668 F.3d 1008 (8th Cir. 2012).

---

## Reconciliation the draft must show

```
Officer W-2 box 1 totals (incl. >2% shareholder health)     = Form 1120-S line 7 (+ officer wages in COGS)
Non-officer W-2 box 1 totals (incl. >2% shareholder health) = Form 1120-S line 8 (+ wages in COGS)
W-2 box 5 totals (all employees)                             = Forms 941 line 5c totals for the 4 quarters
Employer social security + Medicare (7.65% of box 3/box 5 wages, IRC §3111(a),(b)) is part of line 12
```

Differences are listed in the validation summary with the dollar gap. Common causes: elective deferrals (excluded from lines 7/8), wages capitalized in inventory, a bonus paid after year end (accrual-method related-party rule: deductible only in the year includible by the shareholder, §267), and fringe benefits placed on line 18 by mistake.

---

## Red flags to surface (warn; do not fix by picking numbers)

- Line 7 is zero while K line 16d shows distributions to an officer who worked in the business
- W-2 wages exist in the books but no Forms 941 or W-2 were filed
- The officer's "salary" was booked as owner draws and never ran through payroll
- More-than-2% shareholder health insurance deducted on line 18
- Officer wages placed on line 8 to avoid Form 1125-E (the form follows total receipts, not the line used)

For each flag write one line: what the books show, why it matters (quote the instruction), and the question pending with the user.
