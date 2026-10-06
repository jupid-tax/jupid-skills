# Effectively Connected Income vs Schedule NEC Income

How to place each U.S. income item of a nonresident alien. Sources: Instructions for Form 1040-NR (2025), "How To Report Income on Form 1040-NR", Schedule 1 and Schedule NEC instructions; Pub. 519 (2025) chapters 2–4; IRC §§864, 871, 897.

The three kinds of income (Instructions, "Kinds of Income"):

1. **Effectively connected with a U.S. trade or business (ECI)**: taxed at the graduated rates that apply to citizens and residents, after allowable deductions. Form 1040-NR page 1.
2. **U.S.-source income not effectively connected**: taxed at **30%** unless a treaty sets a lower rate; no deductions. Schedule NEC.
3. **Exempt income**: treaty-exempt → Schedule OI item L and line 1k; exempt by statute → not reported.

Foreign-source income of a nonresident is generally not on the return. It becomes ECI only in limited cases that require a U.S. office or fixed place of business to which it is attributable (Instructions, "Foreign Income Taxed by the United States"; Pub. 519 ch. 4). If a user describes foreign-source income routed through a U.S. office, ask and flag for CPA review.

---

## Step A — Was the user engaged in a U.S. trade or business?

Pub. 519 chapter 4 tests. Ask the matching question for each:

| Activity | Default answer | Question to ask |
|---|---|---|
| Personal services performed in the U.S. (employee or contractor) | Usually engaged | "How many days did you work while physically in the U.S., and who paid you?" |
| Pay from a foreign employer for short U.S. visits | Not U.S.-source and exempt only if all three: employer is a foreign person not engaged in U.S. business (or a foreign office of a U.S. person); present 90 days or fewer in the year; pay for the U.S. services $3,000 or less | "Was your total pay for the U.S. days more than $3,000?" (over $3,000 → all of it is ECI) |
| F, J, M, or Q student with taxable U.S. scholarship or fellowship | Treated as engaged; the taxable U.S.-source part is ECI | "Which part of the grant paid for tuition, fees, books, and required equipment?" |
| Owning and operating a business selling services, products, or merchandise in the U.S. | Usually engaged | "Does the business have a U.S. office, warehouse, employees, or an agent who signs contracts in the U.S.?" |
| Member of a partnership engaged in U.S. business at any time | Engaged | "Did the partnership send a Schedule K-3 or Form 8805?" |
| Beneficiary of an estate or trust engaged in U.S. business | Engaged | |
| Trading stocks, securities, commodities through a U.S. broker for own account | Not engaged (not for dealers; not with a U.S. office through which trades are directed) | "Do you have a U.S. office from which you direct the trading?" |

Being engaged has two consequences: Form 1040-NR is required even with no income (Table A item 1), and U.S.-source income from the business (and certain investment income under the asset-use and business-activities tests) is ECI.

### Foreign-owned single-member LLC

A domestic single-member LLC owned by a nonresident is disregarded for income tax: its income is the owner's. The owner reports the LLC's ECI on Schedule C → Schedule 1 line 3 → Form 1040-NR line 8 (Schedule 1 line 3 instructions: only ECI income and expenses). Pub. 519 ch. 7: the LLC itself must file a pro forma Form 1120 with Form 5472 by the due date, and the foreign owner includes the LLC's reportable items on Form 1040-NR. Hand the LLC filing to [`../../form-5472/SKILL.md`](../../form-5472/SKILL.md); never fold it into this return.

Ask, in this order: "Does the LLC have any U.S. office, employees, inventory, or dependent agents?", "Who performs the services, and where are they physically when they do?", "Has the LLC filed Form 8832 or 2553?" (If it elected corporate status, it is a corporation and this skill only covers dividends or wages the owner received from it.)

### Self-employment tax

A nonresident pays SE tax only if an international social security (totalization) agreement places them under the U.S. system (Instructions, Items To Note; Schedule 2 line 4 instructions). Then SE tax goes on Schedule 2 line 4 (→ line 23b), half on Schedule 1 line 15, with Schedule SE. Otherwise there is no SE tax. Ask: "Which country's social security system covers your self-employment, and do you have a certificate of coverage?" Agreements: SSA, U.S. international social security agreements page.

---

## Step B — Classify each item

| Item | Where it goes | Notes |
|---|---|---|
| Wages for U.S. work | Line 1a | Days-based sourcing when work is split: U.S. workdays ÷ total workdays × pay; housing/education fringes by principal place of work; $250,000+ compensation with an alternative method → item K and statement |
| Treaty-exempt wages | Line 1k + item L | Form 8233 or a substitute statement |
| Taxable scholarship not on W-2 | Schedule 1 line 8r → line 8 | Degree candidates include only amounts used for non-qualified expenses (room, board, travel); attach Form 1042-S |
| Business profit (ECI) | Schedule C → Schedule 1 line 3 → line 8 | ECI income and expenses only |
| Rental income, no §871(d) election | Schedule NEC line 6, 30% or treaty rate on gross rents | No deductions |
| Rental income with §871(d) election | Schedule E → Schedule 1 line 5 → line 8 | Net basis; Schedule OI item M |
| Portfolio dividends from U.S. corporations | Schedule NEC line 1a, column by rate | Form 1042-S box 10 → line 25g |
| Interest on U.S. bank deposits | Not reported | Exempt from the 30% tax (§871(i)); not on line 2b |
| Portfolio interest on registered obligations issued after July 18, 1984 | Not reported | Foreign bearer obligations issued on or after March 19, 2012 don't qualify |
| Interest-related dividends; short-term capital gain dividends | Generally exempt | STCG dividends exempt only if present fewer than 183 days |
| Capital gains on stock (not ECI) | Schedule NEC lines 16–18 → line 9 | Taxable only if present 183 days or more in the year (IRC §871(a)(2)); no loss carryover; net loss → 0 |
| U.S. real property interest dispositions | Schedule D → line 7a; withholding on Form 8288-A → line 25f | Treated as ECI automatically (FIRPTA, IRC §897); may trigger AMT |
| U.S. pensions | ECI part (post-1986 U.S. services) lines 5a/5b; rest Schedule NEC line 7 | Example in the instructions: 10 years worked, 3 after 1986 → 30% on line 5a, 70% on NEC line 7 |
| U.S. social security | Schedule NEC line 8: 85% of SSA-1042S box 5 | 30% unless a treaty exempts or reduces |
| Gambling winnings (not a gambling business) | NEC line 11 (winnings only); Canada residents NEC line 10 (net) | Treaty-exempt → column (d) 0% |
| Royalties | NEC lines 3–5 | |
| Gain on sale of personal property | NEC line 12 | |
| Pre-2019 U.S.-source alimony | NEC line 12 | Not Schedule 1 line 2a |
| Gifts or bequests from a foreign person | Not income | Schedule 1 line 8z exception |
| 4% transportation tax | Line 23c | Rare |

---

## Step C — Schedule NEC rate column

1. Start at **30%**, column (c).
2. If a treaty reduces the rate and the user is a resident of that country under the treaty with no U.S. permanent establishment the income is attributable to, use the treaty rate: column (a) 10%, (b) 15%, or (d) with the rate written in (including 0%).
3. Find the rate in IRS Tax Treaty Table 1 (Rev. May 2023) and confirm in the treaty text; Table 1 warns it is not a complete statement of eligibility (limitation on benefits, ownership tests).
4. Compare to Form 1042-S: if the payer withheld at the right rate and the user has no other filing trigger, no return is needed for that income. If the payer over-withheld, report all income of that type and claim the difference through line 25g.

Example rates from Table 1 for dividends paid by U.S. corporations, general column: Germany 15, India 25, Spain 15, United Kingdom 15. Always re-read the current table; rates differ for direct-investment dividends and RIC/REIT dividends (see the table's footnotes).

---

## Step D — The §871(d) real property election

A nonresident can elect to treat all income from U.S. real property held for the production of income (and interests in it) as ECI, so rents are taxed net of expenses at graduated rates instead of 30% of gross (Instructions, "Income You Can Elect To Treat as Effectively Connected"; Pub. 519 ch. 4).

- Applies to all such property and income: rents, natural resource royalties, gains on timber, coal, or iron ore with a retained interest. Dispositions of U.S. real property interests are already ECI without the election.
- Does not make the person engaged in a U.S. trade or business.
- Made by attaching a statement for the election year containing all eight items: (1) that the election is made; (2) complete list of U.S. real property and interests with location (legal identification for timber, coal, iron ore); (3) extent of ownership; (4) description of substantial improvements; (5) income from the property; (6) dates owned; (7) whether under §871(d) or a treaty; (8) prior elections and revocations.
- Schedule OI item M(1) for the first year, M(2) for later years.
- Stays in effect until revoked with IRS consent; after a revocation, a new election cannot be made until after the fifth year in which the revocation occurs.
- Deductions require a timely return (16-month rule, Treas. Reg. §1.874-1(b)). A late return can leave the user taxed on gross rents with no deductions.

Ask before recommending: "Do you want rents taxed net of expenses from now on, knowing the election covers all your U.S. rental property and can only be revoked with IRS consent?" Then show both computations (30% of gross vs graduated on net) so the user and a CPA can decide.

---

## Step E — Deductions allowed against ECI

- Schedule A (Form 1040-NR) only: state and local income taxes on ECI, gifts to U.S. charities, federally declared disaster casualty losses, and the listed line 7 items. No standard deduction except India Art. 21(2) students and business apprentices.
- Adjustments on Schedule 1 Part II only where related to ECI (educator expenses, reservist/performing artist expenses, etc.).
- QBI deduction (line 13a) only for ECI from a qualified trade or business.
- Deductions and credits only on a timely, true, and accurate return (IRC §874(a); Treas. Reg. §1.874-1(b)). If the user is unsure whether some income is ECI, a protective return can be filed by the due date to preserve deductions (Pub. 519 ch. 7).
