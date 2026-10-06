# California Form 568 Line-by-Line Reference

Complete lookup for every line on Form 568 Side 1, the Side 2–3 questions, Schedule IW, Schedule K (568), Schedule T, and the supporting schedules. Use this when the agent needs to confirm where a value belongs or what a line means.

Verified against the **2025 Form 568** (taxable year 2025, filed in 2026; https://www.ftb.ca.gov/forms/2025/2025-568.pdf) and the **2025 Form 568 Booklet** (https://www.ftb.ca.gov/forms/2025/2025-568-booklet.pdf). Re-check the next revision at <https://www.ftb.ca.gov/forms/> before using these line numbers for taxable year 2026.

Form layout: Side 1 (identification, lines 1–17), Side 2 (lines 18–21, Questions J–BB), Side 3 (Questions CC–KK, Single Member LLC Information and Consent, signature), Side 4 (Schedule A, Schedule B, Schedule T), Side 5 (Schedule K), Side 6 (Schedules L, M-1, M-2, O), Side 7 (Schedule IW).

---

## Side 1 — Identification items

| Item | What goes here | Notes |
|------|----------------|-------|
| (name block) | LLC legal name, additional information, address, PMB | Use the legal name filed with the SOS; "Additional information" is only for owner/representative/attention lines (booklet, Specific Instructions) |
| A | California SOS file number | Required (booklet: "Before mailing, make sure entries have been made for... California SOS file number") |
| B | FEIN | Required, including for single-member LLCs |
| E | Accounting method | (1) Cash, (2) Accrual, (3) Other (attach explanation) |
| F | Date business started in California | mm/dd/yyyy |
| G | Total assets at end of year | Complete only if Schedule L is required (see Schedule L below); enter $0 if no assets |
| H | Return type | (1) Initial return, (2) FINAL RETURN (attach a statement explaining the termination; check "final" on each K-1 (568)), (3) Amended return, (4) Protective claim |
| I(1)–I(3) | Change in control / ownership of entities owning or leasing California real property; transfers of property excluded from reassessment under R&TC §62(a)(2) | All LLCs answer all three. "Yes" to both parts of a question requires form BOE-100-B with the Board of Equalization within 90 days of the event |

There are no Items C or D on the 2025 Form 568. Federal classification is reported through Question U (disregarded) and, for an election year, by attaching a copy of federal Form 8832 (booklet, General Information S).

---

## Side 1 — Tax, fee, payments (lines 1–17) and Side 2 lines 18–21

Complete Schedule IW (Side 7) first; it feeds line 1. Whole dollars only.

| Line | 2025 label | What goes here | What does NOT go here |
|------|-----------|----------------|------------------------|
| 1 | Total income from Schedule IW | Schedule IW line 17; may not be negative | Federal gross receipts or profit |
| 2 | Limited Liability Company fee | $0 / $900 / $2,500 / $6,000 / $11,790 from line 1; $0 under the deployed-military exemption; see [`llc-fee-tiers.md`](./llc-fee-tiers.md) | The $800 (line 3) |
| 3 | 2025 annual Limited Liability Company tax | $800 (paid with the 2025 FTB 3522 by the 15th day of the 4th month); $0 under the deployed-military exemption | The fee (line 2) |
| 4 | Pass-through entity elective tax | FTB 3804, Part I, line 3, only if the LLC elected | Nonresident member tax |
| 5 | Nonconsenting nonresident members' tax liability | Schedule T total; see [`nonresident-members.md`](./nonresident-members.md) | 7% withholding on distributions (that is Form 592-Q / 592-PTE, not this line) |
| 6 | Partnership level tax | Only if the IRS concluded a centralized partnership audit for the year; usually on an amended return. Otherwise leave blank | Ordinary income tax |
| 7 | Total tax and fee | Lines 2 + 3 + 4 + 5 + 6 | |
| 8 | Amount paid with FTB 3537 and 2025 FTB 3522 and FTB 3536 | Every 2025 payment: the $800, the June estimate, any fee balance, extension payments; plus K-1 line 15e amounts if this LLC is itself a nonconsenting nonresident member of another LLC (capped at line 5) | PTE elective tax payments (line 9) |
| 9 | Amounts paid for pass-through entity elective tax | FTB 3893 and electronic elective-tax payments for 2025 | |
| 10 | Overpayment from prior year allowed as a credit | The 2024 overpayment the LLC elected to apply | New payments |
| 11 | Withholding (Form 592-B and/or 593) | Withholding on the LLC by another payer that the LLC claims (not more than total tax and fee); attach the 592-B / 593 | Withholding the LLC did on its members |
| 12 | Total payments | Lines 8 + 9 + 10 + 11 | |
| 13 | Use tax | From the booklet's Use Tax Worksheet; not a total line | |
| 14 | Payments balance | Line 12 − line 13, if line 12 is more | |
| 15 | Use tax balance | Line 13 − line 12, if line 13 is more | |
| 16 | Tax and fee due | Line 7 − line 14, if line 7 is more | |
| 17 | Overpayment | Line 14 − line 7, if line 14 is more | |
| 18 | Amount of line 17 to be credited to 2026 tax or fee | Portion applied forward | |
| 19 | Refund | Line 17 − line 18 | |
| 20 | Penalties and interest | Late-payment, late-filing, estimated-fee penalties and interest (booklet, General Information G) | |
| 21 | Total amount due | Lines 15 + 16 + 18 + 20, minus line 17 | |

---

## Side 2 and Side 3 — Questions

| Item | Question | Notes |
|------|----------|-------|
| J | Principal business activity code, business activity, product or service | Six-digit code from the booklet chart; "Do not leave blank" |
| K | Maximum number of members at any time during the year | Multi-member: number of Schedules K-1 (568) attached must equal K |
| L | Investment partnership? | Booklet General Information O |
| M(1) | Apportioning or allocating income to California using Schedule R? | |
| M(2) | If "No": registered in California without earning California-source income? | The "SB 1106 Filing" case: write "SB 1106 Filing" at the top of Side 1 |
| N | Distribution of property or transfer of an LLC interest? | If "Yes", see federal §754 instructions |
| P(1)–P(3) | Foreign nonresident members? Domestic nonresident members? Forms 592, 592-A, 592-B, 592-F, 592-PTE filed? | |
| Q | Any members that are LLCs or partnerships? | |
| R | Under IRS audit now or in a prior year? | |
| S | Member/partner in another multi-member LLC or partnership? | If "Yes", Schedule EO Part I |
| T | Publicly traded partnership under §469(k)(2)? | |
| U(1)–U(3) | Disregarded entity? Credits attributable to it? California income less than total income? | "Yes" to U(1): complete Sides 1, 2, 3, 7 (and Schedules B, K if the $3M test is met) |
| V | Reportable or listed transaction? | Attach federal Form 8886 |
| W, X | Filed federal Schedule M-3? Direct owner of an entity that did? | |
| Y | Beneficial interest in or grantor of a trust? | Attach schedule |
| Z | Owns a disregarded entity? | If "Yes", Schedule EO Part II |
| AA, BB | Related members / trusts for related persons (§267(c)(4)) | |
| CC, DD | Deferring income from asset dispositions; reporting previously deferred income (installment, §1031, §1033, other) | |
| EE | "Doing business as" name | |
| FF | Operated as another entity type in the past five years? | Give prior FEINs, names, entity types |
| GG(1), GG(2) | Previously operated outside California? First year doing business in California? | |
| HH, II | §721(c) partnership? Disclosed transfers under Reg. §1.707-8? | |
| JJ | Aggregated activities (§465) / grouped activities (§469) | Check boxes |
| KK | Unclaimed property Holder Remit Report filed with the State Controller? Date and amount of last report | Do not round cents |

**Single Member LLC Information and Consent** (Side 3, disregarded LLCs only): sole owner's name, TIN (SSN/FEIN/CA corp no./SOS file no.), address, owner entity type — (1) Individual, (2) C Corporation, (3) Pass-Through, (4) Estate/Trust, (5) Exempt Organization — and the owner's signed consent to California's jurisdiction. A nonresident owner who does not sign is treated like a nonconsenting nonresident member (Schedule T).

**Signature**: authorized member or manager; paid preparer block; "May the FTB discuss this return with the preparer?"

Critical: if the user marks "Final return", confirm the SOS cancellation (Form LLC-4/7, plus Form LLC-3 Certificate of Dissolution for a domestic LLC) will be filed within 12 months of the timely final return, and that the LLC does no business in California after the final year. Otherwise another $800 can be assessed (booklet, General Information Q).

---

## Schedule IW — LLC Income Worksheet (Side 7)

California amounts only; income and gains, never losses. An LLC wholly within California assigns everything to California. A disregarded LLC that does not meet the $3M test for Schedules B and K still completes Schedule IW from the owner's federal Schedules B, C, D, E, F.

| Line | What goes here |
|------|----------------|
| 1a | Total California income from Form 568 Schedule B, line 3 (gross profit) |
| 1b | California cost of goods sold from Schedule B line 2 and federal Schedule F, tied to receipts on lines 1a and 4 (not negative) |
| 2a | If Question U(1) is "Yes": the disregarded entity's gross income not included on lines 1 and 8–16 |
| 2b | Cost of goods sold of disregarded entities tied to line 2a receipts (not negative) |
| 3a | LLC's distributive share of ordinary income from pass-through entities |
| 3b | Distributive share of cost of goods sold from other pass-through entities (Schedule K-1 (565) Table 3, line 1a) |
| 3c | Distributive share of deductions from other pass-through entities (Table 3, line 1b) |
| 4 | Gross farm income from federal Schedule F (California amounts) |
| 5 | Other income (not loss) from Schedule B, line 10 |
| 6 | Gains (not losses) from Schedule B, line 8 |
| 7 | Add lines 1a through 6 |
| 8a | Rental real estate income from federal Form 8825, line 20a |
| 8b | Gross rents from all Schedules K-1 (565), Table 3, line 2 |
| 8c | Add lines 8a and 8b |
| 9a | Other rentals from Schedule K (568), line 3a |
| 9b | Other rentals from Schedules K-1 (565), Table 3, line 3 |
| 9c | Add lines 9a and 9b |
| 10 | California interest (Schedule K, line 5) |
| 11 | California dividends (Schedule K, line 6) |
| 12 | California royalties (Schedule K, line 7) |
| 13 | California capital gains (not losses) from Schedule K, lines 8 and 9 |
| 14 | California §1231 gains (not losses) from Schedule K, line 10a |
| 15 | Other portfolio income (not loss) from Schedule K, line 11a |
| 16 | Other income (not loss) not on line 5, from Schedule K, line 11b |
| 17 | Total California income: lines 7 + 8c + 9c + 10 + 11 + 12 + 13 + 14 + 15 + 16; if less than zero enter 0 → Side 1, line 1 |

Do not include amounts already subject to the LLC fee at another LLC (R&TC §17942(b)(1)(A)). For multi-state LLCs, assign each item using R&TC §§25135–25136 (services: where the customer receives the benefit; tangible goods: destination; real property and rentals: location). See [`llc-fee-tiers.md`](./llc-fee-tiers.md).

**Common error**: entering profit, or gross profit without line 1b / 2b. Line 17 is built from gross income **plus** cost of goods sold, so a reseller's cost of goods sold does not reduce it.

---

## Schedule B — Income and Deductions (Side 4)

Trade or business items only, under California law: 1a–1c gross receipts less returns, 2 cost of goods sold (Schedule A line 8), 3 gross profit, 4–5 ordinary income/loss from other LLCs, partnerships, fiduciaries, 6–7 farm profit/loss, 8–9 gains/losses from Schedule D-1 Part II line 17, 10–11 other income/loss, 12 total income, 13 salaries and wages (other than to members), 14 guaranteed payments, 15 bad debts, 16 deductible interest, 17a–17c depreciation and amortization (FTB 3885L) less amounts reported elsewhere, 18 depletion (not oil and gas), 19 retirement plans, 20 employee benefit programs, 21 other deductions, 22 total deductions, 23 ordinary income (loss). §179 is not deducted here; it passes through on Schedule K line 12.

Schedule A (cost of goods sold): lines 1–8 and the 9a–9d inventory questions, mirroring federal Form 1125-A.

---

## Schedule K (568) — Members' Shares of Income, Deductions, Credits (Side 5)

Columns: (a) distributive share item, (b) amounts from federal K (1065), (c) California adjustments, (d) totals under California law. Lines: 1 ordinary income, 2 rental real estate, 3a–3c other rentals, 4a–4c guaranteed payments, 5 interest, 6 dividends, 7 royalties, 8–9 short- and long-term capital gain (Schedule D (568)), 10a–10b §1231 gain/loss, 11a–11c other portfolio income, other income, other loss, 12 §179 expense, 13a–13f contributions, investment interest, §59(e), portfolio deductions, other deductions, 15a–15f withholding and credits (15e = nonconsenting nonresident members' tax paid by the LLC), 17a–17f AMT items, 18a–18c tax-exempt income and nondeductible expenses, 19a–19b distributions, 20a–20c investment income/expenses and other information, 21a total distributive income/payment items, 21b analysis by member type.

Key California adjustments versus federal (2025 FTB 3885L; 2025 booklet):

| Federal item | California treatment |
|--------------|----------------------|
| §168(k) bonus depreciation | Not allowed; depreciate under California rules on FTB 3885L |
| §179 expense | Limit $25,000, reduced dollar for dollar above $200,000 of §179 property placed in service; federal 2025 limit is $2,500,000 / $4,000,000 |
| §174 research expenditures | California does not conform to the federal §174 modifications |
| §199A deduction | Member-level federal deduction; not on Schedule K (568) |
| OBBBA changes generally | California generally does not conform |

For the full list, see [`california-adjustments.md`](./california-adjustments.md).

---

## Schedule K-1 (568) — Member's Share

One per member (multi-member LLCs only; single-member LLCs never issue one). Shows the member's share of every Schedule K (568) line, the member's resident status, and California-source amounts. Nonresident members' withholding appears through Form 592-B, and Schedule T tax paid for a member appears on line 15e.

---

## Schedules L, M-1, M-2 (Side 6)

Not required, along with Item G on Side 1 and Item K on Schedule K-1 (568), if Questions 4a through 4c on federal Form 1065 Schedule B are all "Yes" and the LLC has 10 or fewer members (booklet, Schedule L). Federal Question 4a: total receipts under $250,000; 4b: total assets under $1 million; 4c: K-1s filed and furnished on time (2025 Form 1065). Otherwise follow the federal Schedule L rules; Schedule M-1 uses worldwide amounts under California law (line 4c lists the annual LLC tax as a book expense not on Schedule K). Schedule M-2 should equal the totals of the members' K-1 capital account columns.

---

## Schedule T — Nonconsenting Nonresident Members' Tax Liability (Side 4)

List each nonresident member who has not signed FTB 3832, and a nonresident single owner who has not signed the Side 3 consent.

| Column | What goes here |
|--------|----------------|
| (a) | Member's name |
| (b) | SSN, ITIN, or FEIN |
| (c) | Distributive share of income |
| (d) | Tax rate: 12.3% individual, partnership, LLC, estate, or trust; 8.84% C corporation; 1.5% S corporation |
| (e) | Member's total tax due = (c) × (d) |
| (f) | Amount withheld by this LLC on this member, reported on Form 592-B |
| (g) | Member's net tax due = (e) − (f), not less than zero |

Total of column (g) → Side 1, **line 5**. (The caption under Schedule T on the 2025 form says "Side 1, line 4"; the Side 1 label "Nonconsenting nonresident members' tax liability from Schedule T" is line 5, and the booklet's line 5 instruction says to enter the Schedule T total there. Use line 5 and flag the caption.) Due by the original due date of the return. The member still files a California return and claims the payment.

---

## Schedule O (Side 6)

Amounts from liquidation used to capitalize the LLC. Complete only if the Initial return box (H(1)) is checked and the LLC was capitalized with liquidation proceeds of another entity.

---

## Schedule R — Apportionment

A separate schedule, attached when the LLC has income inside and outside California (Question M(1) "Yes"). California apportions business income with the single-sales-factor formula (R&TC §25128.7). Schedule R does not replace Schedule IW: the fee base is still assigned item by item on Schedule IW. Out of scope for this skill: §25137 industry rules, combined reports — redirect to a CPA.

---

## Where common items go (quick lookup)

| Item | Where on Form 568 |
|------|-------------------|
| $800 annual LLC tax owed | Line 3 |
| LLC fee owed (tiered) | Line 2 |
| $800 already paid with FTB 3522 / Web Pay | Line 8 |
| Estimated fee and fee balance paid with FTB 3536 | Line 8 |
| Extension payment with FTB 3537 | Line 8 |
| PTE elective tax | Line 4 (tax), line 9 (payments) |
| Nonresident member who didn't sign FTB 3832 | Schedule T → line 5 |
| Withholding on the LLC by others (592-B / 593 received) | Line 11 |
| Withholding the LLC did on its members | Not on Form 568; Form 592-Q / 592-PTE / 592-B |
| Federal §168(k) bonus depreciation | Schedule K col. (c) adjustment via FTB 3885L |
| Federal §179 over $25,000 | Schedule K line 12 col. (c); the excess basis is depreciated on FTB 3885L |
| Multi-state assignment of the fee base | Schedule IW (item by item); Schedule R for income apportionment |
