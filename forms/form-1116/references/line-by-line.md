# Form 1116 Line-by-Line Reference

Complete lookup for every line on Form 1116. Use when the agent needs to confirm where a number belongs or what a line means. One Form 1116 covers exactly one income category (basket); separate forms for each basket the user has.

Verified against the **2025 Form 1116** (created 9/16/25) and the **2025 Instructions for Form 1116** (Dec 23, 2025). Line numbers change between revisions; re-check the current form at https://www.irs.gov/forms-pubs/about-form-1116 before using this map for a later year.

## Header

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name | Filer's legal name | Match Form 1040 |
| (top) | Identifying number | SSN/ITIN as shown on the return | Or trust/estate EIN if Form 1041 |
| a | Section 951A category income | Checkbox | GILTI inclusions of US shareholders of CFCs |
| b | Foreign branch category income | Checkbox | Business profits attributable to QBUs in foreign countries |
| c | Passive category income | Checkbox | Most income behind foreign tax in 1099-DIV box 7 / 1099-INT box 6 |
| d | General category income | Checkbox | Wages, SE, active business income |
| e | Section 901(j) income | Checkbox | Sanctioned countries; 2025 list in Pub. 514: Iran, Libya (waiver), North Korea, Sudan, Syria |
| f | Certain income re-sourced by treaty | Checkbox | Separate Form 1116 per treaty country |
| g | Lump-sum distributions | Checkbox | Foreign-source pension lump sum taxed using Form 4972 |
| h | Resident of (name of country) | Country name | The filer's country of residence (United States for a US-resident investor) |

Only one of a-g is checked per Form 1116. If the filer has income in multiple baskets, file one Form 1116 per basket. Paid/Accrued is not in the header: it is the (j)/(k) checkbox in Part II.

---

## Part I — Taxable income or loss from sources outside the US (for the category checked)

### Line i — Foreign country or US territory

One column (A, B, C) per country or territory; attach additional sheets for more than three. The "Total" column adds A, B, and C. Special labels from the instructions:

- **RIC** — income passed through from a mutual fund or other regulated investment company, totaled in one column
- **863(b)** — section 863(b) income (partly US, partly foreign), one column
- **951A** — section 951A inclusions, one column
- **HTKO** — high-taxed passive income moved to another category (negative on the passive form, positive on the other form)
- **909 income** — income from a prior-year foreign tax credit splitting event

### Line 1a — Gross income from sources within the country shown

Gross income in this category, from that country, in USD, even if the foreign country doesn't tax it. Identify the type on the dotted line ("Wages", "Dividends").

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Foreign wages (general basket), not excluded on Form 2555 | Earned income excluded on Form 2555 (never on line 1a) |
| Foreign dividends, interest (passive) | US-source dividends from a US company (no FTC) |
| Foreign rents and royalties (usually passive) | Income re-sourced by treaty (basket f, separate 1116) |
| Foreign capital gains (passive), after any rate adjustment | Foreign capital losses (line 5) |
| Foreign SE / business gross receipts less cost of goods sold (general) | |

Foreign qualified dividends and capital gain distributions go on line 1a after the rate adjustment (× 0.4054 at 15%, × 0.5405 at 20%, omitted at 0%) unless the filer uses the adjustment exception. See [`qualified-dividend-adjustment.md`](./qualified-dividend-adjustment.md).

### Line 1b — Alternative-basis checkbox

A checkbox, not an amount. Check it only if **all** apply: line 1a is compensation for services as an employee; total employee compensation from all sources is $250,000 or more; and an alternative basis (Pub. 514) was used to source it. Attach the statement the instructions require (name/SSN, items, basis, computation, comparison with the time basis).

### Line 2 — Expenses definitely related to line 1a

Attach a statement listing them. No interest expense on line 2 (interest goes on 4a/4b).

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Business expenses of foreign SE income (supplies, travel for the foreign engagement) | Expenses of US-source income (not on Form 1116 at all) |
| State and local income taxes related to foreign-source income | Interest expense (lines 4a/4b) |
| Investment expenses tied to the foreign income | Deductions related to Form 2555-excluded income |

### Line 3a — Certain itemized deductions or standard deduction

If itemizing: medical expenses (Schedule A line 4), general sales taxes, real estate taxes for the home, and state and local personal property taxes. Don't include more state and local tax than Schedule A line 5e allows. If not itemizing: the standard deduction.

### Line 3b — Other deductions

Deductions not definitely related to any specific income, e.g., Schedule 1 (Form 1040) Part II adjustments. Do not include the Schedule 1-A line 37 senior deduction. The Schedule 1-A line 30 car loan interest deduction goes on line 4b instead. Attach a statement.

### Line 3c — Add lines 3a and 3b

### Line 3d — Gross foreign source income

Gross foreign-source income in this category. Include foreign earned income excluded on Form 2555; exclude other exempt income. Use amounts before any qualified dividend / capital gain adjustment. "Gross income" means gross receipts less cost of goods sold, gains before losses, and other income before deductions.

### Line 3e — Gross income from all sources

Worldwide gross income, US and foreign, all categories, same definition as 3d (including Form 2555-excluded income). The same amount goes on line 3e of every Form 1116 the filer files. Nonresident aliens include non-effectively-connected income on both 3d and 3e.

### Line 3f — Divide line 3d by line 3e

Round to at least four decimal places (0.8756782 → 0.8757). Not more than 1.

### Line 3g — Multiply line 3c by line 3f

### Line 4a — Home mortgage interest

If gross foreign-source income (including Form 2555-excluded income) is $5,000 or less, all interest can be allocated to US-source income and lines 4a/4b are 0. Otherwise use the Worksheet for Home Mortgage Interest: (gross foreign-source income of this type, excluding Form 2555 income) ÷ (gross income from all sources, excluding Form 2555 income), at least four decimals, × Schedule A line 8e.

### Line 4b — Other interest expense

Investment interest, trade or business interest, passive activity interest, student loan interest, and qualified passenger vehicle loan interest, apportioned by the **asset method** (adjusted basis of assets producing foreign vs. US income). Same $5,000 threshold as line 4a for US citizens, resident aliens, and domestic estates. Example from the instructions: $2,000 of investment interest, $60,000 of $100,000 asset basis produces foreign income → $1,200 on line 4b.

### Line 5 — Losses from foreign sources

Foreign-source losses in this category, including foreign capital losses after the Worksheet A/B adjustments.

### Line 6 — Add lines 2, 3g, 4a, 4b, and 5

### Line 7 — Subtract line 6 from line 1a

Enter here and on line 15.

---

## Part II — Foreign taxes paid or accrued

Check one box: **(j) Paid** or **(k) Accrued**. A cash-basis filer can choose accrued only on a timely filed original return, never on an amended return, and must then credit taxes in the year they accrue on all future returns.

| Column | What goes here |
|--------|---------------|
| Country line A/B/C | Same order as the Part I columns |
| (l) Date paid or accrued | Payment or accrual date; "1099 taxes" when the tax is reported in USD on a 1099; "909 taxes" for released splitter taxes |
| (m) Dividends, (n) Rents and royalties, (o) Interest — foreign currency | Taxes withheld at source, in the foreign currency |
| (p) Other foreign taxes paid or accrued — foreign currency | e.g., income tax on wages or business profits |
| (q)–(t) | The same four items in US dollars |
| (u) Total | Add columns (q) through (t) |

### Line 8 — Add lines A through C, column (u)

Enter here and on line 9. Translation rules: taxes paid use the rate on the date paid (or withheld); accrued taxes use the average rate for the year to which they relate, with the exceptions in [`currency.md`](./currency.md). Attach an explanation of the conversion.

**Foreign taxes that do NOT go on Line 8** (2025 i1116, "Foreign Taxes Not Eligible for a Credit"):

- Interest and penalties
- Tax not legally owed or eligible for refund (including withholding above the treaty rate)
- Withholding on US-source income
- Taxes paid to sanctioned countries
- Taxes on dividends or other income that fail the 16-day holding period, or for which related payments must be made
- Foreign value-added tax (VAT, GST) and other non-income taxes (Reg. §1.901-2)
- Foreign social security tax covered by a totalization agreement

See [`non-creditable-taxes.md`](./non-creditable-taxes.md) for the full list. Taxes on Form 2555-excluded income are entered here but removed on line 12.

---

## Part III — Figuring the credit

### Line 9 — Enter the amount from line 8

### Line 10 — Carryover and carrybacks

Carryover from Schedule B (Form 1116), line 3, column (xiv), plus any carryback to this year. Attach Schedule B for the category if there is a carryover in or a new carryover generated this year; if an amount is entered but Schedule B isn't required, check the box. Leave blank for section 951A category income (no carryovers). Carryback 1 year, carryforward 10 years (IRC §904(c)).

### Line 11 — Add lines 9 and 10

### Line 12 — Reduction in foreign taxes (enter as a negative)

- Taxes allocable to foreign earned income and housing amounts excluded on Form 2555 (fraction in the instructions)
- Taxes on Puerto Rico income exempt from US tax; American Samoa income excluded on Form 4563
- Combined foreign oil and gas income; foreign mineral income with percentage depletion
- 10% reduction for failure to file Form 5471 or Form 8865
- Taxes specifically attributable to international boycott operations (otherwise use line 34)
- Taxes related to a foreign tax credit splitting event (§909)

### Line 13 — Taxes reclassified under high tax kickout

Negative on the passive category form, positive on the other category's form.

### Line 14 — Combine lines 11, 12, and 13

Total foreign taxes available for credit.

### Line 15 — Enter the amount from line 7

If zero or a loss, the category generally has no credit, but line 16 must still be completed.

### Line 16 — Adjustments to line 15

In this order, with an attached computation: (1) §461(l) disallowed business loss; (2) allocation of foreign losses among categories; (3) allocation of a US-source loss; (4) recapture of overall foreign loss accounts; (5) recapture of separate limitation loss accounts; (6) recapture of overall domestic loss accounts. Usually 0 for filers without losses.

### Line 17 — Combine lines 15 and 16

If zero or less, skip line 18 and enter 0 on line 19.

### Line 18 — Taxable income for the limitation

Individuals: Form 1040 (or 1040-SR/1040-NR) line 11b minus line 14, plus Schedule 1-A line 37 (the senior deduction is added back for 2025-2028). Estates and trusts: taxable income without the exemption deduction. If zero or less, enter 0 on lines 18 and 19. If the filer has qualified dividends or capital gains and line 5 of the Qualified Dividends and Capital Gain Tax Worksheet is greater than zero while line 23 is less than line 24, use the Worksheet for Line 18 unless the adjustment exception applies.

### Line 19 — Divide line 17 by line 18

"1" if line 17 is more than line 18; "0" if line 18 is zero.

### Line 20 — Regular tax against which the credit is allowed

Individuals: Form 1040 line 16 plus Schedule 2 (Form 1040) line 1z, less any Form 4972 tax on line 16. Regular tax only (IRC §26(b)(1)); no SE tax, no NIIT. Form 1041: Schedule G lines 1a and 1d. Category g uses the lump-sum worksheet; category e leaves line 20 blank. Adjust for Form 8978 if filed.

### Line 21 — Multiply line 20 by line 19 (maximum credit)

### Line 22 — Increase in limitation (§960(c))

Only for distributions of previously taxed CFC earnings with an excess limitation account. Usually 0.

### Line 23 — Add lines 21 and 22

### Line 24 — Smaller of line 14 or line 23

The credit for this category; enter on the matching line of Part IV. If line 23 is smaller than line 14, the excess is a carryback/carryover (Schedule B).

---

## Part IV — Summary of separate credits from Parts III

For 2025, Part IV must be completed even when filing only one Form 1116. With several forms, complete it on the one with the largest line 24 (not on a category e or g form, unless the only forms are e and g), and attach the others.

| Line | Content |
|------|---------|
| 25 | Credit for taxes on section 951A category income |
| 26 | Credit for taxes on foreign branch category income |
| 27 | Credit for taxes on passive category income |
| 28 | Credit for taxes on general category income |
| 29 | Credit for taxes on section 901(j) income |
| 30 | Credit for taxes on certain income re-sourced by treaty |
| 31 | Credit for taxes on lump-sum distributions |
| 32 | Add lines 25 through 31 |
| 33 | Smaller of line 20 or line 32 |
| 34 | Reduction for international boycott operations (factor method) |
| 35 | Line 33 − line 34: the foreign tax credit → Schedule 3 (Form 1040) line 1; Form 1041 Schedule G line 2a; Form 990-T Part III line 1a |

---

## Schedules B and C (Form 1116)

- **Schedule B (Form 1116), Rev. December 2022** — Foreign Tax Carryover Reconciliation; one per category with a carryover; line 3 column (xiv) feeds Form 1116 line 10.
- **Schedule C (Form 1116), Rev. December 2025** — Foreign Tax Redeterminations that occurred this year and relate to prior years; one per category. Also filed annually while a provisional credit for contested taxes (Form 7204) is open.

---

## Special situations

### High-tax kickout (HTK)

Passive income is "high-taxed" when the foreign taxes on it (after allocating expenses) exceed the highest US tax that could be imposed on it (Reg. §1.904-4(c)). That income moves to the other category: enter it in an "HTKO" column on line 1a (negative on the passive form, positive on the other form), move the related deductions on line 6 the same way, and move the related taxes on line 13. The agent should ask whether any foreign passive income bore foreign tax above the top US rate; if so, evaluate HTK.

### Look-through rules for CFC payments

Dividends, interest, rents, and royalties from a CFC in which the filer is a 10%-or-more US shareholder are passive only to the extent attributable to the CFC's passive income (Reg. §1.904-5). Route to a CPA.

### §904(f) and §904(g) loss accounts

Foreign losses that offset US income create overall foreign loss accounts; US losses that offset foreign income create overall domestic loss accounts. Both are recaptured through line 16 in later years. Out of scope for this skill; CPA referral.

### Estate / trust filers

Form 1116 attaches to Form 1041. Line 18 is taxable income without the exemption deduction; line 20 is Schedule G lines 1a and 1d; line 35 goes to Schedule G line 2a. The no-Form-1116 election is not available to estates or trusts.
