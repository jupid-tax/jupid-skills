# Schedule B Decision Rules and the Small-Partnership Exception

How to answer the Schedule B questions on pages 2-4 of the 2025 Form 1065 that change what the partnership must attach or complete. Rules come from the Instructions for Form 1065 (2025), pages 25-31, unless another source is named. Question 33 (election out of the centralized audit regime) has its own file: [`bba-audit-and-penalties.md`](./bba-audit-and-penalties.md).

Every question needs an explicit Yes or No (or a count). Do not leave a question blank because "it obviously does not apply"; the instructions for question 30 say outright "Don't leave the question unanswered." When a fact is missing, ask the user the question in plain words and record the answer in the draft.

---

## Question 1 — Entity type

Check the box that matches the state-law entity, not the tax classification:

| State-law entity | Box |
|------------------|-----|
| General partnership (no filing with the state, or a general partnership filing) | a |
| Limited partnership (LP certificate filed) | b |
| Limited liability company with two or more members, no Form 8832 corporate election | c |
| Limited liability partnership (LLP filing) | d |
| Partnership not created or organized in the United States | e |
| Anything else (state the type) | f |

A multi-member LLC checks box c. Checking box a for an LLC is a common error.

---

## Questions 2a and 2b — 50% owners (Schedule B-1)

Test at the **end of the tax year**, using the **maximum** of the owner's profit, loss, and capital percentages under the partnership agreement (Instructions p. 25).

- 2a asks about corporations, partnerships (including entities taxed as partnerships), trusts, tax-exempt organizations, and foreign governments.
- 2b asks about individuals and estates.

Constructive ownership (Instructions pp. 25-26):

- Section 267(c) applies, excluding section 267(c)(3). An interest owned by an entity is treated as owned proportionately by its owners.
- Family attribution reaches only a spouse, brothers, sisters, ancestors, and lineal descendants, and runs to a person only if that person also owns an interest directly or through an entity. Example from the instructions: A owns 50% directly; A's daughter B owns nothing directly or through an entity, so A's interest is not attributed to B; the partnership answers 2b "Yes" because of A.
- Add direct and indirect percentages. Example from the instructions: Corporation A owns 15% of Partnership C directly and 50% of Partnership B, which owns 70% of C. A owns 15% + 35% = 50% of C, so C answers 2a "Yes".

A two-member 50/50 LLC owned by two individuals answers 2b "Yes" (each owns 50%, which is "50% or more") and attaches Schedule B-1, Part II for both.

Ask when needed: "At year end, did any member's spouse, parent, child, grandchild, or sibling also hold an interest, directly or through an entity?" Do not assume family ownership is zero.

---

## Questions 3a and 3b — What the partnership owns

List each corporation in which the partnership owns directly 20% or more, or directly or indirectly 50% or more, of the voting power (3a), and each partnership or trust in which it owns directly 20% or more, or directly or indirectly 50% or more, of profit, loss, capital, or beneficial interest (3b). For an entity owned through a disregarded entity, list the owned entity, not the DE (Instructions p. 26).

---

## Question 4 — The four-condition small-partnership test

Answer "Yes" only if **all four** conditions hold (Form 1065, page 2):

| Condition | Test | Definition (Instructions p. 26) |
|-----------|------|-------------------------------|
| (a) | Total receipts for the tax year less than $250,000 | Gross receipts or sales (page 1, line 1a) + all other income (page 1, lines 4-7) + income on Schedule K, lines 3a, 5, 6a, and 7 + income or net gain on Schedule K, lines 8, 9a, 10, and 11 + income or net gain on Form 8825, lines 2, 21, and 22a |
| (b) | Total assets at year end less than $1 million | The amount that would be reported in item F, on the books' accounting method |
| (c) | Schedules K-1 filed with the return and furnished to the partners on or before the due date (including extensions) | A K-1 furnished late, or a return filed after the due date, fails this condition |
| (d) | Not filing and not required to file Schedule M-3 | M-3 tests: total assets or adjusted total assets of $10 million or more, total receipts of $35 million or more, or a 50% reportable entity partner (Instructions pp. 18-19) |

Computation notes:

- Use line 1a (before returns and allowances), not line 1c.
- Portfolio income on Schedule K counts: bank interest on line 5 adds to total receipts even though it never touches page 1.
- Use "income or net gain" amounts for lines 8, 9a, 10, 11 and the Form 8825 lines: a net loss on one of those lines adds zero, it does not reduce receipts.

What "Yes" excuses (Form 1065, page 2; Instructions pp. 17-18, 34, 62):

- Schedule L, Schedule M-1, Schedule M-2 (page 6)
- Item F (total assets) on page 1
- Item L (capital account analysis) on every Schedule K-1
- Schedules K-2 and K-3, under the small partnership filing exception (see below)

What "Yes" does **not** excuse:

- The Analysis of Net Income (Loss) per Return at the top of page 6
- Schedule K and every other item and box of the K-1, including items J and K1
- The partners' own duty to track the adjusted basis of their interests (Instructions p. 34: "Each partner is responsible for maintaining a record of the adjusted tax basis in its partnership interest")

Trap: condition (c) is judged when the K-1s actually go out. A partnership that files late, or files on time but furnishes even one K-1 after the due date, must answer "No" and complete Schedules L, M-1, M-2, item F, and item L. When the return is late, build page 6 before telling the user the return is "simple".

Optional use: "If 'Yes,' the partnership is not required to complete" those items. A partnership may still complete them; ask the user whether they want the balance sheet included (some lenders and state returns ask for it).

### Small partnership exception for Schedules K-2 and K-3 (new for 2025)

The 2025 Partnership Instructions for Schedules K-2 and K-3 (p. 3) add a filing exception tied to question 4: a partnership that meets all four question 4 conditions is excepted from completing Schedules K-2 and K-3, provided that:

1. The partners receive a notification, at the latest when the K-1s are furnished, stating that partners will not receive Schedule K-3 unless they request it (an attachment to the K-1 is acceptable).
2. No partner requests Schedule K-3 information on or before the "1-month date" (1 month before the date the partnership files Form 1065; for calendar-year 2025 partnerships that extend, the latest 1-month date is August 17, 2026).

If a partner requests on or before the 1-month date, the partnership must file Schedules K-2 and K-3 for the requested parts and furnish K-3 to that partner. A request after the 1-month date requires furnishing the completed K-3 to that partner within 1 month of the request, without filing K-2/K-3 for the others.

When the exception applies, check Schedule K, line 16b ("Check this box if you qualified for an exception to filing Schedule K-2").

The separate **domestic filing exception** (four criteria: no or limited foreign activity with no more than $300 of creditable foreign taxes shown on a payee statement; all direct partners are U.S. citizen or resident individuals, domestic estates and trusts with U.S. beneficiaries, S corporations, single-member LLCs owned by those persons, or domestic partnerships owned by them; partner notification; no request by the 1-month date) is described in [`k1-allocation-and-capital.md`](./k1-allocation-and-capital.md).

---

## Questions 5-7

- **5** Publicly traded partnership under section 469(k)(2): interests traded on an established securities market or readily tradable on a secondary market. Almost always "No" for a closely held business.
- **6** Debt canceled, forgiven, or modified to reduce principal: "Yes" means cancellation of debt income is separately stated on Schedule K and K-1 (the partners apply section 108). Ask about forgiven loans, settled vendor balances, and modified bank notes.
- **7** Form 8918 material advisor disclosure: "Yes" only if the partnership filed or must file Form 8918.

---

## Question 8 — Foreign financial accounts (FBAR)

Answer "Yes" if, at any time during calendar year 2025, the partnership had an interest in or signature or other authority over a foreign bank, securities, or other financial account, **and** the combined value exceeded $10,000 at any time during the calendar year, and the accounts were not at a U.S. military banking facility; or the partnership owns more than 50% of the stock of a corporation that would answer "Yes" (Instructions p. 27). If "Yes", enter the country or countries and file FinCEN Form 114 electronically at BSAefiling.fincen.gov.

Ask: "Did the business hold any account at a bank, broker, or payment platform outside the United States during 2025, and what was the highest combined balance?"

---

## Question 9 — Foreign trusts

"Yes" if the partnership transferred property to a foreign trust, is treated as owner of part of one, or received a distribution, loan, or use of property from one. Form 3520 may be required (Instructions p. 27).

---

## Questions 10a-10d — Section 754 and basis adjustments

- **10a** "Yes" if the partnership is making, or made and has not revoked, a section 754 election; enter its effective date. The election is made by a statement filed with the timely filed return (including extensions) for the year of the distribution or transfer, containing the partnership's name and address and a declaration that it elects under section 754 to apply sections 734(b) and 743(b). Regulations section 301.9100-2 gives an automatic 12-month extension if corrective action is taken within 12 months of the original deadline. Revocation uses Form 15254 (Instructions p. 10).
- **10b/10c** Enter the aggregate net positive and net negative section 743(b) or 734(b) adjustments made this year and attach the computation statement.
- **10d** Mandatory adjustments for a substantial built-in loss or substantial basis reduction.

Ask whether any partner sold or inherited an interest, or whether any distribution of property occurred during the year; either fact can make section 754 relevant. Whether to make the election is a judgment call for the user and their CPA; this skill records the decision, it does not make it.

---

## Questions 11-15

- **11** Checkbox: like-kind exchange replacement property distributed (or contributed to a non-DE entity) in the current year, when the exchange happened in the current or prior year.
- **12** "Yes" if the partnership distributed tenancy-in-common or other undivided interests in its property.
- **13a** Count of Forms 8858 attached (foreign disregarded entities and foreign branches).
- **14** "Yes" if the partnership had any foreign partner at any time in the year; enter the number of Forms 8805 filed. Effectively connected income allocable to foreign partners can require section 1446 withholding and Forms 8804, 8805, and 8813 (Instructions p. 28). Stop and refer the user to a CPA if foreign partners have effectively connected income; that withholding regime is out of scope.
- **15** Count of Forms 8865 attached.

---

## Questions 16a and 16b — Forms 1099

16a: "Yes" if the partnership made any payment in 2025 that requires a Form 1099. 16b: whether the partnership filed or will file them. Determine the obligation under the Form 1099 instructions for the payment year (see [`../../form-1099-nec/SKILL.md`](../../form-1099-nec/SKILL.md) and [`../../form-1099-misc/SKILL.md`](../../form-1099-misc/SKILL.md)); do not hard-code a dollar threshold here, because the threshold depends on the calendar year of payment.

A "Yes" to 16a with "No" to 16b is a truthful answer the IRS can act on. Do not change 16b to "Yes" unless the user confirms the forms were or will be filed.

---

## Questions 17-29 (mostly international, interest, and special regimes)

| Q | Answer "Yes" when | Consequence |
|---|-------------------|-------------|
| 17 | Forms 5471 attached (count) | Foreign corporation reporting |
| 18 | Partners that are foreign governments (count) | Section 892 |
| 19 | Payments made, or received allocable to foreign partners, requiring Forms 1042/1042-S | Chapter 3 or 4 withholding |
| 20 | The partnership is a specified domestic entity required to file Form 8938 | Attach Form 8938 |
| 21 | Section 721(c) partnership | Regulations section 1.721(c)-1(b)(14) |
| 22 | Interest or royalties disallowed to partners under section 267A | Enter the disallowed total |
| 23 | An election under section 163(j) for a real property or farming business is in effect | Irrevocable; requires ADS depreciation for certain property |
| 24 | (a) owns a pass-through with excess business interest expense; (b) prior 3-year average annual gross receipts above $31 million with business interest expense; (c) tax shelter with business interest expense | Attach Form 8990 |
| 25 | Self-certifying as a qualified opportunity fund | Attach Form 8996 |
| 26 | Foreign partners subject to section 864(c)(8) (count) | Schedule K-3, Part XIII |
| 27 | Transfers subject to Regulations section 1.707-8 disclosure | |
| 28 | Foreign acquisition with section 7874 ownership above 50% | Enter percentages |
| 29a/b | Form 7208 required (stock repurchase excise tax) | |

Tax shelter for question 24(c) includes a syndicate: a partnership that allocates more than 35% of its losses to limited partners or limited entrepreneurs (Instructions p. 7). A loss year can therefore flip question 24 to "Yes" for an LP or LLC with passive members.

---

## Question 30 — Digital assets

"Yes" if at any time during 2025 the partnership received digital assets as payment, reward, or award (including mining, staking, or a hard fork), or sold, exchanged, or otherwise disposed of a digital asset or a financial interest in one. Holding, moving between the partnership's own wallets, or buying with U.S. dollars alone does not require "Yes" (Instructions p. 30). Ask: "Did the business accept, earn, sell, or swap any crypto, stablecoins, or NFTs during 2025?"

---

## Question 32 — Election out of subchapter K (section 761(a))

Only for a qualifying investing, operating, or similar arrangement electing to be excluded from all of subchapter K. Requires a statement naming every member with identifying numbers, the qualification under Regulations section 1.761-2(a), the members' election, and where the agreement can be obtained. Calendar-year filers make it on a Form 1065 filed by March 15 following the first year (subject to extensions) (Instructions p. 30). Operating businesses do not qualify; refer anything else to a CPA.
