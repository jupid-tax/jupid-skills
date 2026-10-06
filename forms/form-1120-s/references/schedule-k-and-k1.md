# Schedule K and Schedules K-1 (Form 1120-S)

How to total the separately stated items on Schedule K, allocate them to each shareholder on Schedule K-1, decide whether Schedules K-2 and K-3 are required, and hand basis tracking to the shareholder (Form 7203). Built from the 2025 Instructions for Form 1120-S, the 2025 Schedule K-1 (Form 1120-S), the 2025 Shareholder's Instructions for Schedule K-1 (Form 1120-S), the 2025 S Corporation Instructions for Schedules K-2 and K-3 (Form 1120-S), and the Instructions for Form 7203.

---

## 1. What belongs on Schedule K instead of page 1

The corporation reports on page 1 only trade or business income and deductions. Everything a shareholder must apply their own limits to is separately stated on Schedule K:

| Item | Schedule K line | Why separate |
|---|---|---|
| Ordinary business income (loss) | 1 (from page 1, line 22) | Base item |
| Rental real estate | 2 (Form 8825) | Passive activity rules at shareholder level |
| Other rental | 3a–3c | Same |
| Interest, dividends, royalties (portfolio) | 4, 5a/5b, 6 | Portfolio income is never passive income (Instr., Portfolio Income) |
| Capital gains and losses | 7, 8a–8c | Shareholder's capital loss limits and rates |
| Section 1231 gain (loss) | 9 | Netted at shareholder level |
| Section 179 deduction | 11 | Each shareholder applies the §179 limits; the corporation still reduces asset basis by the full amount elected (Instr., line 14) |
| Charitable contributions | 12a, 12b | Individual percentage limits |
| Investment interest | 12c | Form 4952 at shareholder level |
| Credits | 13a–13g | Shareholder-level credit limits |
| AMT items | 15a–15f | Complete for all shareholders |
| Tax-exempt income, nondeductible expenses | 16a, 16b, 16c | Basis adjustments |
| Distributions | 16d | Basis and AAA |
| Loan repayments to shareholders | 16e | Debt basis |

Schedule K, line 18 = lines 1 through 10 combined, minus lines 11 through 12e and 16f. It must equal Schedule M-1, line 8 when M-1 is completed.

---

## 2. Allocation: per share, per day

Rule (IRC §1377(a)(1); Instr., Shareholder's Pro Rata Share Items): items are allocated on a daily basis according to the number of shares held on each day. A shareholder who disposes of stock is treated as the shareholder for the day of disposition; a deceased shareholder is the shareholder for the day of death.

**No change in ownership during the year.** Item G = percentage of total stock owned. Each K-1 box = Schedule K line × item G.

**Ownership changed.** Weight each period:

```
Item G (shareholder) = Σ [ % of outstanding shares held during period × days in period ] ÷ days in tax year
```

Instruction example (Item G): A and B each hold 50% for half the year; then A, B and C hold 40%, 40%, 20% for the other half. Item G: A 45%, B 45%, C 10%.

Worked arithmetic for a 365-day year, 1,000 shares, a sale of 150 shares from L to P on April 30 (L holds them through April 30; P from May 1):

```
Period 1: Jan 1–Apr 30 = 120 days   D 50%  L 30%  P 20%
Period 2: May 1–Dec 31 = 245 days   D 50%  L 15%  P 35%
L: (30 × 120 + 15 × 245) ÷ 365 = 72.75 ÷ 365 × 100 = 19.9315%
P: (20 × 120 + 35 × 245) ÷ 365 = 109.75 ÷ 365 × 100 = 30.0685%
D: 50.0000%                                          Total 100.0000%
```

Rounding: compute each K-1 amount to the dollar, then assign any $1 difference so the K-1s sum exactly to Schedule K, and state where the difference went.

**Exceptions to daily proration** (both require a statement attached to a timely filed original or amended return):

| Election | When available | Consent | Marking |
|---|---|---|---|
| Terminating election, §1377(a)(2), Reg. §1.1377-1(b) | A shareholder terminates their entire interest | Corporation and all affected shareholders | "Section 1377(a)(2) Election Made" at the top of each affected K-1 |
| Qualifying disposition, Reg. §1.1368-1(g)(2) | Disposition of 20%+ of outstanding stock in a 30-day period; redemption of 20%+ treated as an exchange; issuance of 25%+ of previously outstanding stock to new shareholders in a 30-day period | Each shareholder who held stock during the year | Statement describes the facts |

Ask: "Did any shareholder sell, gift or redeem shares, or did the corporation issue new shares, during the year? On what date and how many?" If an election might apply, list it as an open item for the CPA; do not make it on the user's behalf.

---

## 3. Items reported only to the shareholder who received them

- **Distributions (K line 16d → K-1 box 16, code D):** report on the K-1 of the shareholder who actually received each distribution. Property distributions at FMV with a statement (date acquired, date distributed, FMV, corporation's basis).
- **Loan repayments (K line 16e → box 16, code E):** to the shareholder repaid.
- **Item I:** debt owed directly to the shareholder at the beginning and end of the year; the sum across K-1s reconciles to Schedule L, line 19. Exclude guarantees and co-borrowed debt.

Sanity check on distributions: for each distribution date, divide each shareholder's amount by their shares on that date. Unequal per-share amounts are a one-class-of-stock question (Reg. §1.1361-1(l)); ask the user about the governing documents and refer to a CPA. Do not reallocate distributions yourself.

---

## 4. Coded items the agent most often needs

| Box / code | Item | Notes (Instr.) |
|---|---|---|
| 12, code A (or B) | Cash contributions (60%) (or 30% limit) | From K line 12a |
| 12, code AC | Interest expense allocated to debt-financed distributions | From K line 12e |
| 16, codes A–F | Tax-exempt interest; other tax-exempt income; nondeductible expenses; distributions; repayment of loans; foreign taxes | Basis items |
| 17, codes A/B | Investment income / expenses | From K lines 17a/17b |
| 17, code V | Section 199A information | Use "V*" and "STMT"; attach Statement A per trade or business: QBI items, W-2 wages, UBIA of qualified property, qualified PTP items, §199A dividends, SSTB status, aggregations (Statement B). Do not add the amounts into one number |
| 17, code AC | Gross receipts for §448(c) | When shareholders need it for their own tests |
| 17, code AJ | Excess business loss limitation | Statement of aggregate business gross income and deductions |
| 17, code BA | Domestic research or experimental expenditures | New for 2025 (§174A) |
| 17, code K | Disposition of property with §179 deductions passed through | Reported instead of using Form 4797 |

W-2 wages for Statement A: figure under Rev. Proc. 2019-11. Under the unmodified box method, W-2 wages are the lesser of total box 1 or total box 5 of the Forms W-2 filed (Rev. Proc. 2019-11, §5.01). Then keep only wages properly allocable to QBI.

---

## 5. Schedules K-2 and K-3

Schedule K line 14a: check and attach Schedule K-2 when reporting items of international tax relevance. Line 14b: check if the corporation qualifies for an exception to filing Schedule K-2, with a statement. Each K-1 box 14 is checked when a K-3 is attached.

**Small S corporation filing exception (new for 2025).** If the corporation meets both conditions of Schedule B, question 11 (total receipts under $250,000 and year-end total assets under $250,000), it is excepted from completing Schedules K-2 and K-3 (K-2/K-3 Instructions, Small S Corporation Filing Exception).

**Domestic filing exception.** No K-2 filed and no K-3 furnished (except on a late request) if all three are met for tax year 2025:

1. No foreign activity, or foreign activity limited to passive category foreign income with not more than $300 of creditable foreign income taxes, shown on a payee statement (for example, Form 1099) furnished to the corporation. Foreign activity includes foreign taxes, foreign-source income or loss, and any interest in a foreign partnership, foreign corporation, foreign branch or foreign disregarded entity.
2. Shareholders are notified, no later than when the K-1 is furnished (an attachment to the K-1 works), that they will not receive Schedule K-3 unless they request it.
3. No shareholder requests K-3 information on or before the "1-month date" (one month before the corporation files Form 1120-S; for calendar 2025 returns on extension, the latest 1-month date is August 17, 2026). A request after that date still requires furnishing the K-3 to that shareholder within one month of the request.

A shareholder must request K-3 information each year or ask for subsequent years. If neither exception applies (or a shareholder asked in time), flag the return for a CPA: K-2/K-3 preparation is outside this skill.

Draft notification text for the K-1 attachment:

> "The corporation qualifies for the domestic filing exception for tax year 2025 and will not furnish Schedule K-3 unless you request it. To request Schedule K-3 information, contact the corporation in writing."

---

## 6. Basis is the shareholder's job: Form 7203 handoff

The corporation does not compute shareholder basis on Form 1120-S. The Shareholder's Instructions for Schedule K-1 state that the shareholder is responsible for keeping the information needed to figure basis, and generally should use Form 7203.

Form 7203 is filed by shareholders who (Instructions for Form 7203, Who Must File):
- claim a deduction for their share of an aggregate loss (including a loss carried over because of basis limits),
- received a non-dividend distribution,
- disposed of stock, or
- received a loan repayment from the corporation.

Basis ordering the shareholder applies (Shareholder's Instructions, Basis Limitations): (1) increase for all income including tax-exempt income; (2) decrease for distributions (box 16, code D), not below zero; (3) decrease for nondeductible expenses; (4) decrease for losses and deductions. An election under Reg. §1.1367-1(g) can move (4) before (3). Distributions do not reduce loan basis; guarantees do not create loan basis.

What the agent produces: for each shareholder, a one-paragraph handoff stating whether Form 7203 appears required this year and why, and the K-1 amounts that feed it (boxes 1–12, 16A–16F). If the shareholder supplies a beginning basis, the agent may show the arithmetic as an illustration labeled "shareholder-level, not part of Form 1120-S". If distributions exceed the shareholder's stated beginning basis plus current increases, flag possible gain and refer to a CPA.

---

## 7. Delivery and penalties

- Furnish each K-1 (and K-3 when required) "on or before the day on which the corporation's Form 1120-S is required to be filed" (Instr., Specific Instructions (Schedule K-1 Only), General Information).
- Give each shareholder the Shareholder's Instructions for Schedule K-1 or item-specific instructions.
- Failure to furnish a correct K-1 (or K-3): $340 per schedule; $680 or, if greater, 10% of the items required to be reported when the failure is intentional (2025 Instr., Failure to furnish information timely; IRC §§6722, 6724). Year-dependent: re-check the instructions for the year filed.
- Substitute K-1s need no approval if they are exact copies of the IRS schedule (Pub. 1167).
