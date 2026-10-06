---
name: form-1065
description: >
  Use this skill when a partnership or a multi-member LLC taxed as a
  partnership needs to prepare IRS Form 1065 and the partners' Schedules K-1.
  Triggers on phrases like "Form 1065", "partnership tax return", "file our
  multi-member LLC return", "K-1s for my partners", "Schedule K-1 (Form 1065)",
  "guaranteed payments to a partner", "Schedule B question 4", "do we need
  Schedules L, M-1, M-2", "partner capital accounts tax basis", "partnership
  representative", "elect out of the BBA audit regime", "Schedule B-2",
  "1065 late filing penalty", "K-2 K-3 domestic filing exception".
  Do NOT use for: a single-member LLC or sole proprietor (use schedule-c); an
  LLC or corporation with an S election (use form-1120-s); a C corporation or
  an LLC that elected corporate treatment (use form-1120); a partner reporting
  a K-1 they received on their own return (use schedule-e, schedule-se,
  form-1040); only requesting an extension (use form-7004); changing the
  entity's classification (use form-8832); spouses electing qualified joint
  venture status (use schedule-c); California Form 568 (use ca-form-568).
form: Form 1065 (U.S. Return of Partnership Income)
audience: [llcm, partnership]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1065.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1065.pdf
---

# Form 1065 — U.S. Return of Partnership Income

This skill produces an audit-grade draft of Form 1065 (all six pages) and one Schedule K-1 per partner from the partnership's books and the partners' facts. It classifies every item as page 1 trade or business income, a separately stated Schedule K item, or a nondeductible or capital item, allocates Schedule K to the partners, builds the tax-basis capital accounts, answers Schedule B, and hands off filing.

The arithmetic is simple. The judgment sits in six places: what a payment to a partner is (guaranteed payment, distribution, or neither), whether Schedule B, question 4 lets the partnership skip Schedules L, M-1, M-2, item F, and K-1 item L, how each partner's self-employment earnings are treated, which box 19 code a distribution gets, whether the partnership can and wants to elect out of the centralized audit regime, and the penalty when the return is late. Where a rule turns on a fact the user has not given, ask; never default.

**Companion guide for end users:** [Form 1065 Instructions 2026: Line by Line, Schedule B Questions, Schedules K and K-1, and When You Can Skip L, M-1, and M-2](https://jupid.com/blog/form-1065-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Revision this skill was verified against:** the 2025 Form 1065 (PDF footer "Created 11/25/25"), the 2025 Instructions for Form 1065 (dated Jan 14, 2026), the 2025 Schedule K-1 (Form 1065), Schedule B-1 (Rev. August 2019), Schedule B-2 (Rev. December 2018), and the 2025 Partnership Instructions for Schedules K-2 and K-3, filed in 2026. The 2025 form covers calendar year 2025 and fiscal years beginning in 2025. Before using this skill for a 2026 tax year return (filed in 2027), re-check every line number, threshold, and penalty amount against the new revision at https://www.irs.gov/forms-pubs/about-form-1065.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions Form 1065, a partnership return, or Schedules K-1 they must issue to partners
- The user has a domestic LLC with two or more members and no Form 8832 or Form 2553 on file; under the default rules it is a partnership (Instructions p. 3)
- The user has a general partnership, limited partnership, or LLP, including an informal arrangement where two or more people carry on a business and share profits (Instructions p. 3)
- The user asks how to pay a partner, how to report draws, how to fill item L, or whether they can skip Schedules L, M-1, and M-2
- The user asks about the partnership representative, Schedule B-2, or the late-filing penalty for a partnership

Do **not** engage this skill when:

- The business has one owner: a single-member LLC is disregarded; use [`../schedule-c/SKILL.md`](../schedule-c/SKILL.md)
- The entity has an accepted S election: use [`../form-1120-s/SKILL.md`](../form-1120-s/SKILL.md)
- The entity is a corporation or elected to be taxed as one: use [`../form-1120/SKILL.md`](../form-1120/SKILL.md)
- The user is a partner who received a K-1 and is filing their own return: use [`../schedule-e/SKILL.md`](../schedule-e/SKILL.md), [`../schedule-se/SKILL.md`](../schedule-se/SKILL.md), and [`../form-1040/SKILL.md`](../form-1040/SKILL.md)
- The user only needs more time: use [`../form-7004/SKILL.md`](../form-7004/SKILL.md) (form code 09)
- The user wants to change the entity's classification: use [`../form-8832/SKILL.md`](../form-8832/SKILL.md)
- Spouses who are the only owners of an unincorporated business not held in a state-law entity, both materially participating and filing jointly, want qualified joint venture treatment: that replaces Form 1065 with two Schedules C (Instructions p. 3); use [`../schedule-c/SKILL.md`](../schedule-c/SKILL.md)
- The partnership is foreign, is a publicly traded partnership, a REMIC (Form 1066), a qualified derivatives dealer, or has foreign partners with effectively connected income: state that the skill does not cover it and refer the user to a CPA

If ownership is ambiguous ("my brother helps out and we split profits"), ask whether there is a written or oral agreement to share profits and losses before deciding. A joint undertaking merely to share expenses, or mere co-ownership of rented property without services, is not a partnership (Instructions pp. 3-4).

---

## Prerequisites

Collect these before drafting. If any item is missing, ask for it with a specific question and **stop until it is answered**.

### About the partnership

1. **Tax year**: calendar or fiscal (begin and end dates), and whether this is a first, final, or short-year return.
2. **Legal name, EIN, address, date business started.** If the EIN was applied for but not received, it is entered as "Applied for" with the date (Instructions p. 18). Never invent an EIN.
3. **State-law entity type** (Schedule B, question 1) and confirmation that no Form 8832 or Form 2553 was filed.
4. **Principal business activity, product or service, and six-digit business code** (items A, B, C). Offer two or three candidates from the code list in the instructions and let the user choose.
5. **Accounting method** (cash, accrual, other) as used on the books.
6. **The partnership agreement's allocation terms**: profit, loss, and capital percentages; any special allocations; the liquidation clause; how varying interests are handled (proration or interim closing of the books).

### About each person who was a partner at any time during the year

7. Name, address, and TIN; for a single-member LLC member, the owner's name and TIN plus the LLC's name and EIN; entity type (individual, C corporation, S corporation, partnership, trust, estate, exempt organization, IRA, nominee); domestic or foreign.
8. General partner, LLC member-manager, limited partner, or other member (item G); dates of entry or exit; beginning and ending profit, loss, and capital percentages (item J).
9. **Self-employment treatment** of each individual member who is not clearly a general or limited partner under state law (ask; see Step 8).
10. Prior-year ending tax-basis capital account (from last year's K-1 item L) and contributions during the year (cash; adjusted basis and liabilities of contributed property).
11. Share of liabilities (nonrecourse, qualified nonrecourse, recourse) and any guarantees, as determined by the user's CPA under Regulations section 1.752-2.

### About the money

12. Books for the year: income and expenses by category, cost of goods sold (Form 1125-A), fixed-asset list with depreciation (Form 4562) and any section 179 election, rental activities (Form 8825), portfolio income, gains and losses.
13. **Every payment to a partner**, with type: fixed payment for services, fixed return on capital, medical insurance, retirement contribution, or draw of profits.
14. Year-end balance sheet (and prior year-end), if Schedule B, question 4 may be "No".
15. Facts for Schedule B: 50% owners (including family holdings), interests in other entities, foreign accounts, foreign partners, Form 1099 obligations, digital assets, section 754 status, canceled debt.

### About filing

16. Whether Form 7004 was filed by the original due date, and the planned filing date.
17. The list of returns the partnership was required to file during the calendar year ending with or within its tax year (e-file test).
18. The partners' decision on the centralized audit regime: elect out (if eligible) or designate a partnership representative (name, U.S. street address, U.S. phone; a designated individual if the PR is an entity).

---

## Workflow

Execute in order. Do not skip ahead.

### Step 1 — Confirm the return is a Form 1065

Confirm two or more owners, no corporate or S election, and that the entity is not a disregarded single-member LLC or a qualified joint venture. Redirect if not.

### Step 2 — Fix the year, due date, and status

Due date: the 15th day of the 3rd month after the tax year ends; if that day falls on a Saturday, Sunday, or legal holiday, the next business day. Calendar-year 2025 returns were timely through March 16, 2026 (Instructions p. 5). Form 7004 filed by that date gives an automatic 6-month extension (Instructions for Form 7004). Compute whether the return is on time, extended, or late, and state it at the top of the draft. If late, run Step 13.

### Step 3 — Build the partner roster

List every person who was a partner at any time in the year: item I (number of K-1s) and the section 6698 penalty multiplier both use this count. Record items E through J for each.

### Step 4 — Classify every item

For each book item, decide one destination: page 1 (trade or business only), a Schedule K line (portfolio income, rental activity, section 179, contributions, investment interest, credits, foreign taxes, tax-exempt income), line 18c (nondeductible), Form 8825 (rental real estate), or capitalized. Use [`references/line-by-line.md`](./references/line-by-line.md). When the destination depends on a fact (for example, whether interest was earned on customer receivables or on a bank deposit), ask.

### Step 5 — Separate payments to partners

Map every payment to a partner: guaranteed payment for services (line 10, Schedule K line 4a), for capital (line 10, line 4b), partner medical insurance (line 10, line 4a, and line 13e code M), partner retirement contribution (box 13 code R), or distribution (line 19). Nothing paid to a partner goes on line 9. See [`references/k1-allocation-and-capital.md`](./references/k1-allocation-and-capital.md).

### Step 6 — Complete page 1

Lines 1a through 23, then lines 24 through 32 if any tax or payment item applies. Attach the line 7 and line 21 statements.

### Step 7 — Answer Schedule B

Answer every question. Compute question 4 total receipts and total assets exactly as defined (Instructions p. 26), and test condition (c) against the actual K-1 delivery date. Use [`references/schedule-b-and-small-partnership.md`](./references/schedule-b-and-small-partnership.md).

### Step 8 — Self-employment and Schedule K

Fill Schedule K lines 1 through 21. Run the self-employment worksheet for line 14a. For each LLC member, use the self-employment treatment the user confirmed in Prerequisites item 9; if it is missing, ask now:

> "For self-employment tax, should [member]'s share of ordinary income be treated like a general partner's or like a limited partner's? Does [member] work in the business, and what management rights does the operating agreement give them?"

### Step 9 — Allocate to Schedules K-1

Allocate each Schedule K line per the agreement (special allocations to the named partners; varying interests by the method the user named). Round to whole dollars so each Schedule K line equals the sum of the K-1 boxes. Apply the 2025 box 19 codes (A, B, C, D, F, G). Prepare Statement A for box 20, code Z with the W-2 wage and UBIA figures the user supplies.

### Step 10 — Page 6

Always complete the Analysis of Net Income (Loss) per Return. If question 4 is "No", complete Schedule L, Schedule M-1 (or M-3 if required), Schedule M-2, item F, and item L on every K-1 using the tax-basis method.

### Step 11 — Audit regime and K-2/K-3

Check eligibility to elect out (100 or fewer, counting S corporation shareholders; only eligible partner types for the whole year; timely return). Record the user's decision: Schedule B-2 with question 33 "Yes", or question 33 "No" with a complete PR designation. Test the K-2/K-3 domestic filing exception and small partnership exception; check line 16b and prepare the partner notice if one applies. See [`references/bba-audit-and-penalties.md`](./references/bba-audit-and-penalties.md).

### Step 12 — Validate

Run every check in **Validation**. Fix arithmetic; surface judgment issues to the user.

### Step 13 — Penalty check (late returns only)

Months late (each month or part of a month from the due date, including any valid extension, up to 12) × persons who were partners at any time in the year × $255 for returns required to be filed in 2026 (Instructions p. 7; Rev. Proc. 2024-40) or $260 for returns required to be filed in 2027 (Rev. Proc. 2025-32). Add the K-1 exposure ($340 per late or incorrect K-1 for 2026). Run the Rev. Proc. 84-35 screen and report which criteria are met; do not promise relief.

### Step 14 — Produce the draft and hand off

Produce the deliverable in **Output format**. Then list the downstream items: Form 7004 if not filed and still before the due date ([`../form-7004/SKILL.md`](../form-7004/SKILL.md)); Forms 1099 for the year ([`../form-1099-nec/SKILL.md`](../form-1099-nec/SKILL.md)); state partnership return (California: [`../ca-form-568/SKILL.md`](../ca-form-568/SKILL.md)); partner-side forms ([`../schedule-e/SKILL.md`](../schedule-e/SKILL.md), [`../schedule-se/SKILL.md`](../schedule-se/SKILL.md), [`../form-8995/SKILL.md`](../form-8995/SKILL.md)).

### Step 15 — File (only if the user asks the agent to file)

Follow [`filing.md`](./filing.md): channel decision (mandatory e-file test, paper addresses by state and asset size), K-1 delivery, consent and security rules. If the user will file through their own preparer, stop after Step 14.

---

## Line-by-line guidance

Full map: [`references/line-by-line.md`](./references/line-by-line.md). The rules that cause most errors:

### Header

- **F** total assets at year end; blank when question 4 is "Yes"; equals Schedule L, line 14(d) otherwise.
- **G(5)** checks for an amended return or an e-filed administrative adjustment request (AAR).
- **I** counts every person who was a partner at any time during the year.
- **J** only when Schedule M-3 is filed (total assets or adjusted total assets of $10 million or more, total receipts of $35 million or more, or a 50% reportable entity partner; Instructions pp. 18-19).

### Page 1 income and deductions

- Lines 1a-8 and 9-21 are trade or business only. Rental activity goes to Form 8825 or Schedule K, line 3; portfolio income to Schedule K, lines 5-11 (Instructions pp. 19-20).
- **Line 2** = Form 1125-A, line 8.
- **Line 9** excludes anything paid to partners.
- **Line 10** guaranteed payments, including partner medical insurance; never draws.
- **Lines 16a-16c** exclude section 179 (Schedule K, line 12). Attach Form 4562 when property was placed in service this year or for listed property (Instructions p. 23).
- **Line 18** is for employees' plans only; partners' contributions go to box 13, code R.
- **Line 21** needs a statement by type and amount; meals at 50%, the other 50% to line 18c.
- **Line 23** = line 8 minus line 22; carries to Schedule K, line 1.
- **Lines 24-32** are blank for most small partnerships. Line 26 is the BBA AAR imputed underpayment; lines 32b-32d (new for 2025) take direct deposit details for an overpayment.

### Schedule B

- **Q1**: an LLC checks box c.
- **Q2a/2b**: 50% or more of profit, loss, or capital at year end, with constructive ownership; "Yes" attaches Schedule B-1. A 50/50 two-individual LLC answers 2b "Yes".
- **Q4**: all of total receipts under $250,000, total assets under $1 million, K-1s filed and furnished by the due date including extensions, and no Schedule M-3. "Yes" removes Schedules L, M-1, M-2, item F, and item L, and opens the K-2/K-3 small partnership exception. It never removes the Analysis of Net Income.
- **Q8**: foreign accounts above $10,000 in aggregate at any time in calendar 2025 trigger FinCEN Form 114.
- **Q10a**: section 754 election status; the election itself is a statement filed with a timely return.
- **Q16a/16b**: Forms 1099 obligations under the 1099 instructions for the payment year.
- **Q30**: digital assets; must be answered.
- **Q33**: election out under section 6221(b) with Schedule B-2, or "No" with the PR designation.

### Schedule K and K-1

- **Line 4a/4b/4c**: services, capital, total.
- **Line 14a**: worksheet line 5; box 14, code A only for individuals (general-partner share of ordinary income plus guaranteed payments for services; limited partners only guaranteed payments for services).
- **Line 16a/16b**: K-2 attached, or exception claimed.
- **Line 18c**: nondeductible expenses, including the disallowed half of meals.
- **Line 19a** = box 19 codes A + D + F; **19b** = codes B + C + G (2025 codes; F and G for partners who perform services).
- **Line 20c, code Z**: Statement A for section 199A.
- **Item L**: tax-basis transactional method; guaranteed payments and section 743(b) adjustments excluded; transferee picks up the transferor's capital as "other increase".

### Page 6

- **Analysis of Net Income line 1** = Schedule K lines 1-11 minus lines 12-13e and 21. LLC members go on the limited partners row (Instructions p. 61).
- **Schedule M-1 line 3** = guaranteed payments other than health insurance; **line 4b** = nondeductible meals and other section 274 items; **line 9** = Analysis line 1.
- **Schedule M-2**: line 3 = Analysis line 1; line 7 removes guaranteed payment income and nondeductible expenses; line 9 = sum of ending item L.

---

## Validation

Run every check. Fix arithmetic errors; report judgment issues to the user rather than silently changing them.

### Math checks

- [ ] 1c = 1a − 1b; 3 = 1c − 2; 8 = 3 + 4 + 5 + 6 + 7
- [ ] 16c = 16a − 16b; 22 = 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16c + 17 + 18 + 19 + 20 + 21; 23 = 8 − 22
- [ ] Line 21 statement total = line 21; line 7 statement total = line 7
- [ ] 28 = 24 + 25 + 26 + 27; 31 or 32a consistent with 28, 29, 30
- [ ] Schedule K line 1 = page 1 line 23; 4c = 4a + 4b; 3c = 3a − 3b
- [ ] Each Schedule K line = sum of the matching K-1 box across all partners
- [ ] Self-employment worksheet line 5 = Schedule K line 14a = sum of box 14, code A
- [ ] Line 19a = codes A + D + F; 19b = codes B + C + G
- [ ] Analysis line 1 = K lines 1 through 11 − (12 through 13e + 21); line 2 total = line 1
- [ ] If page 6 required: Schedule L line 14 = line 22 at both dates; item F = L line 14(d); M-1 line 9 = Analysis line 1; M-2 line 1 = sum of beginning item L; M-2 line 9 = sum of ending item L
- [ ] Each item L: beginning + contributed + current year income + other − withdrawals = ending
- [ ] Item J percentages: each category totals 100% (excluding beginning % of new partners and ending % of departed partners); none negative
- [ ] Schedule B-2 line 3 = line 1 + line 2 ≤ 100 if question 33 is "Yes"

### Sanity checks (warn, do not block)

- [ ] Any payment to a partner on line 9
- [ ] Section 179, contributions, or investment interest on page 1
- [ ] Bank interest, dividends, or capital gains on page 1
- [ ] Question 4 "Yes" while the return is late or a K-1 went out late
- [ ] Box 14 blank for an individual member who works in the business, or filled for a corporation, trust, or estate partner
- [ ] All distributions coded A although partners performed services
- [ ] Question 33 "Yes" with a single-member LLC, trust, partnership, or nominee partner, or on a late return
- [ ] PR designation missing a U.S. street address or U.S. phone number
- [ ] Item L ending capital negative (allowed, but confirm with the user)
- [ ] Line 23 loss in a partnership with limited partners: question 24(c) syndicate test (more than 35% of losses to limited partners)
- [ ] Partner medical insurance on line 19 instead of line 10 with box 13, code M

### Cross-form checks

- [ ] Form 1125-A attached if line 2 > 0; Form 4562 if required; Form 8825 if line 2 of Schedule K is used; Schedule D and Form 4797 when gains are reported
- [ ] Schedule B-1 attached if 2a or 2b is "Yes"
- [ ] Statement A attached to every K-1 with code Z
- [ ] K-3 notice prepared if a K-2/K-3 exception is claimed
- [ ] E-file test result recorded; filing channel consistent with it

---

## Output format

Deliver this markdown, filled in. Show every line, including zeros. Mark any value the user supplied without documents as "(user-stated)".

```markdown
# Form 1065 — DRAFT for tax year YYYY
<Partnership name>   EIN <XX-XXXXXXX>   <city, state>
Status: on time | extended (Form 7004 filed MM/DD/YYYY) | late (due MM/DD/YYYY)

## Header
A. Principal business activity: ...
B. Principal product or service: ...
C. Business code: ...
D. EIN: ...
E. Date business started: MM/DD/YYYY
F. Total assets: $X or "blank (Schedule B Q4 = Yes)"
G. Boxes checked: ...
H. Accounting method: Cash | Accrual | Other
I. Number of Schedules K-1: N
J. Schedules C and M-3 attached: Yes | No
K. Aggregated / grouped: ...

## Page 1 (lines 1a through 32d, every line)
1a ... 23  (with line 7 and line 21 statements)
24 ... 32d

## Schedule B (questions 1 through 33, every answer)
... PR designation or Schedule B-2 Part III total

## Schedule K (lines 1 through 21, every line)
Self-employment worksheet (lines 1a through 5)

## Page 6
Analysis of Net Income (Loss) per Return, lines 1 and 2
Schedule L | M-1 | M-2, or "Not required (Schedule B Q4 = Yes)"

## Schedules K-1 (one column per partner)
Items E-N; boxes 1-23 with codes; Statement A summary

## Required attachments
- [ ] Form 1125-A / Form 4562 / Form 8825 / Schedule D / Form 4797
- [ ] Statements: line 7, line 21, line 20c, section 754
- [ ] Schedule B-1 / Schedule B-2
- [ ] Statement A per K-1; K-3 notice

## Validation summary
- Math: all checks passed | list of failures
- Sanity warnings: ...
- Open questions for the user or their CPA: ...
- Penalty exposure (if late): months × partners × $ amount = $X

## Filing plan
Channel: e-file (mandatory | elective) | paper to <address>
Due date: MM/DD/YYYY   K-1 delivery date: MM/DD/YYYY
Signer: <partner or LLC member>

## Sources cited in this draft
- Form 1065 (2025) and Instructions for Form 1065 (2025)
- Schedule K-1 (Form 1065) (2025); Partner's Instructions for Schedule K-1 (2025)
- Schedules B-1 (Rev. 8-2019), B-2 (Rev. 12-2018); Partnership Instructions for Schedules K-2 and K-3 (2025)
- IRC §§ 6031, 6072, 6221(b), 6698, 707(c), 1402(a)(13), 199A; Regulations §§ 301.6011-3, 301.6221(b)-1
- Rev. Proc. 2024-40 (§6698 amount for returns due in 2026); Rev. Proc. 2025-32 (returns due in 2027)
```

The draft is not the filed return. The user or their preparer still enters it in e-file software or on the paper form, and a partner or LLC member signs.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of Form 1065 pages 1-6, Schedule K-1 items and boxes, Schedules B-1 and B-2, from the PDF text
- [`references/schedule-b-and-small-partnership.md`](./references/schedule-b-and-small-partnership.md) — Schedule B decision rules, constructive ownership, the question 4 test and what it excuses, K-2/K-3 small partnership exception
- [`references/k1-allocation-and-capital.md`](./references/k1-allocation-and-capital.md) — allocations, guaranteed payments, self-employment worksheet and box 14, 2025 distribution codes, items J and K1, item L and Schedule M-2 tax-basis capital, Statement A, K-2/K-3 domestic filing exception
- [`references/bba-audit-and-penalties.md`](./references/bba-audit-and-penalties.md) — centralized audit regime, partnership representative, election out under section 6221(b), AARs and amended returns, section 6698 and K-1 penalties, Rev. Proc. 84-35 screen
- [`references/common-mistakes.md`](./references/common-mistakes.md) — sixteen recurring errors with the rule that fixes each
- [`filing.md`](./filing.md) — e-file test, MeF and paper channels, where-to-file table, K-1 delivery, consent and security rules

## Examples

- [`examples/two-member-llc-small.md`](./examples/two-member-llc-small.md) — two-member LLC, question 4 "Yes", guaranteed payment, PR designation, paper filing
- [`examples/limited-partnership-full-schedules.md`](./examples/limited-partnership-full-schedules.md) — LP with full page 6, guaranteed payments for services and capital, S corporation partner, election out with Schedule B-2
- [`examples/late-filed-llc-with-de-member.md`](./examples/late-filed-llc-with-de-member.md) — late return, question 4 lost, disregarded-entity member, penalty estimate and Rev. Proc. 84-35 screen

## Sources

Re-verify each source for the year being filed.

- [Form 1065 Instructions 2026 (Jupid blog)](https://jupid.com/blog/form-1065-instructions-2026) — narrative companion for human readers
- [Form 1065 (2025)](https://www.irs.gov/pub/irs-pdf/f1065.pdf) and [Instructions for Form 1065 (2025)](https://www.irs.gov/pub/irs-pdf/i1065.pdf); HTML: https://www.irs.gov/instructions/i1065
- [About Form 1065](https://www.irs.gov/forms-pubs/about-form-1065) — revision history and updates
- [Schedule K-1 (Form 1065) (2025)](https://www.irs.gov/pub/irs-pdf/f1065sk1.pdf) and [Partner's Instructions for Schedule K-1 (2025)](https://www.irs.gov/pub/irs-pdf/i1065sk1.pdf)
- [Schedule B-1 (Rev. August 2019)](https://www.irs.gov/pub/irs-pdf/f1065sb1.pdf); [Schedule B-2 (Rev. December 2018)](https://www.irs.gov/pub/irs-pdf/f1065sb2.pdf)
- [Partnership Instructions for Schedules K-2 and K-3 (2025)](https://www.irs.gov/pub/irs-pdf/i1065s23.pdf)
- [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf) — 6-month automatic extension
- [Instructions for Schedule SE (2025)](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf) — partner's share of gross nonfarm income
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf), section 2.56 — $255 for partnership returns required to be filed in 2026
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf), section 4.55 — $260 for partnership returns required to be filed in 2027
- [Treas. Reg. §301.6221(b)-1](https://www.ecfr.gov/current/title-26/section-301.6221(b)-1) — election out, eligible partners, 30-day partner notice
- [Treas. Reg. §301.6011-3](https://www.ecfr.gov/current/title-26/section-301.6011-3) — mandatory e-filing for partnerships
- [IRM 20.1.2](https://www.irs.gov/irm/part20/irm_20-001-002r), section 20.1.2.4.3.1 — Rev. Proc. 84-35 small-partnership relief criteria
- [BBA centralized partnership audit regime](https://www.irs.gov/businesses/partnerships/bba-centralized-partnership-audit-regime); [About Form 8979](https://www.irs.gov/forms-pubs/about-form-8979); [About Form 1065-X](https://www.irs.gov/forms-pubs/about-form-1065-x)
- [1065 MeF providers](https://www.irs.gov/e-file-providers/1065-mef-providers); [e-file waiver guidance](https://www.irs.gov/e-file-providers/guidance-on-waivers-for-partnerships-unable-to-meet-e-file-requirements)
- IRC §§ 199A(c)(4)(B), 704, 706(d), 707(c), 752, 754, 1402(a)(13), 6031, 6072(b), 6221-6241, 6698, 6722

## Disclaimer

This skill encodes procedural guidance from IRS forms, instructions, regulations, and revenue procedures. It is not tax advice and does not create a CPA-client relationship. Allocations, self-employment treatment of LLC members, liability sharing, section 754 and audit-regime elections, and penalty relief involve judgment; the agent should tell the user that the draft is a starting point to be reviewed by a licensed tax professional before filing.
