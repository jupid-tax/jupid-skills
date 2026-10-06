# Personal-Use vs. Business / Income-Producing Property

The single most important classification on Form 4684. It determines:
- Which Section (A, B, or both) to file
- Whether the §165(h)(5) disaster restriction applies (Section A only; tax years beginning after 2017, made permanent by P.L. 119-21 §70109)
- Whether the $100 per-event floor and 10% AGI floor apply (Section A only)
- Where the loss flows on the return (Schedule A vs. Form 4797)

Get this wrong and the entire form is wrong. Ask the user explicitly when classification is ambiguous.

---

## The three classifications

### 1. Personal-use property → Section A

Property held for personal use, not used in any business or income-producing activity.

Examples:
- Primary residence
- Second home (if not rented to others)
- Personal vehicle (not used for business commute or rideshare)
- Furniture, appliances, electronics in the home
- Personal clothing and jewelry
- Personal art collection (not held for investment)
- Boats, RVs used only personally

**Disaster restriction (IRC §165(h)(5))**: For tax years beginning after 2017, personal-use casualty/theft losses are deductible **only** if attributable to a federally declared disaster (for tax years beginning after 2025, also a State declared disaster), except to the extent of personal casualty gains. A house fire that destroys your home is NOT deductible if the fire wasn't part of a declared disaster. A theft of personal property is generally not deductible, because a theft is rarely attributable to a declared disaster; it can only offset personal casualty gains (line 14, Worksheet 1-1).

The Section A floors:
- $100 per casualty event (Line 11); $500 for a qualified disaster loss
- 10% of AGI floor across all Section A losses (Line 17); none for a qualified disaster loss

The line 18 result flows to **Schedule A Line 15** (itemized deduction). If the user takes the standard deduction, a line 18 loss gives NO tax benefit. A net qualified disaster loss (line 15) goes to Schedule A line 16 and can be added to the standard deduction.

### 2. Trade, business, rental, or royalty property → Section B, column (b)(i)

Column (b)(i) of Section B Part II is "Trade, business, rental, or royalty property":
- Schedule C business assets (laptop used 100% for self-employment, business vehicle, equipment)
- Inventory (special rules: deduct either through cost of goods sold or separately as a casualty loss, not both; Pub. 547, "Loss of inventory")
- Rental real estate and royalty property (Schedule E), including a vacation home rented out part of the year (rental part only)
- Farm equipment (Schedule F filers)
- Partnership / S-corp business assets passed through to the user

The (b)(i) loss flows through Section B line 31 or 38a to **Form 4797 Line 14** as an ordinary loss (or Schedule 1 line 4 if Form 4797 is not otherwise required). No floors. No AGI threshold. A rental or passive-activity loss may still be limited by Form 8582 (instructions, "Property Used in a Passive Activity").

### 3. Income-producing property → Section B, column (b)(ii)

Property held for investment, not used in a trade or business or rented out. The instructions' examples: stocks, notes, bonds, gold, silver, vacant lots, and works of art. Also:
- A collector car held purely for investment (rare)
- Funds lost in a Ponzi-type scheme or a financial scam entered into for profit

The Section B income-producing loss flows through line 32 or 38b to **Schedule A Line 16** ("other itemized deductions"; the 2025 Schedule A instructions list casualty and theft losses of income-producing property from Form 4684 lines 32 and 38b there). It is not a miscellaneous itemized deduction, so the termination of those deductions does not reach it. It helps only a user who itemizes.

### 4. Mixed-use property (special rules)

If property is used partly for business and partly for personal:

- The business-use portion follows Section B rules (no floor).
- The personal-use portion follows Section A rules (federally-declared-disaster restriction, $100 floor, 10% AGI floor).
- Allocate by business-use percentage.

Example: Home with a 200 sq ft home office in a 2,000 sq ft house = 10% business use. A $100,000 loss to the structure is split as $10,000 business (Section B, deductible loss figured on Form 8829 for a Schedule C filer) and $90,000 personal (Section A, only if a declared disaster). If the user figured the home office deduction with the simplified method, the whole home goes in Section A (instructions, "Which Sections To Complete").

Example: Vehicle used 60% for business and 40% personal = 60% Section B, 40% Section A.

### 5. Employee property (not deductible)

Property used in performing services as an employee (employee tools, work clothing, etc.). Before 2018 this was a miscellaneous itemized deduction subject to the 2% AGI floor. Miscellaneous itemized deductions are no longer allowed (P.L. 119-21 §70110 made the TCJA suspension permanent), and the 2025 instructions (Section B caution) say business casualty and theft losses of property used as an employee cannot be deducted or used in the netting process. Do not enter them. If the user says they are a qualified performing artist, fee-basis government official, armed forces reservist, or eligible educator, refer the question to a CPA rather than guessing.

---

## The classification questionnaire

Ask the user these questions in order:

1. **"Was this property used in a business you operate (Schedule C, F, partnership, S-corp)?"**
   - Yes → Section B, trade/business
   - No → continue

2. **"Was this property rented out, or held for investment or another profit-seeking purpose?"**
   - Rental or royalty property → Section B, column (b)(i)
   - Investment property (stocks, vacant land, collectibles held for investment, scam or Ponzi losses) → Section B, column (b)(ii)
   - No → continue

3. **"Was this your home, personal vehicle, or other personal-use property?"**
   - Yes → Section A
   - No → unusual; investigate (might be employee property → see Section 5 above)

4. **For Section A only: "Was the property in a FEMA-declared federal disaster area when the loss occurred?"** (For 2026 and later tax years, also ask about a State declared disaster.)
   - Yes → continue with Section A; record the DR- or EM- number and whether it was a major disaster (DR) with an incident period in the qualified window
   - No → loss is deductible only against personal casualty gains; with no gains, STOP

5. **For mixed-use (home office, business vehicle): "What percentage was business use?"**
   - Allocate; split between Sections.

---

## Common classification mistakes

| Mistake | Why it's wrong | Correct treatment |
|---------|----------------|-------------------|
| Filing Section A for a non-disaster house fire (tax years after 2017) | §165(h)(5) bars it | Loss not deductible unless offsetting personal casualty gains; otherwise do not file Form 4684 |
| Filing Section A for theft of personal property | A theft is rarely attributable to a declared disaster | Not deductible beyond personal casualty gains; see if any business-use portion qualifies for Section B |
| Filing Section B for a personal vehicle stolen during a business trip | Personal-use property; the trip's purpose doesn't change classification | Section A (deductible only if attributable to a declared disaster or against personal casualty gains) |
| Filing Section A for a rental property loss | Rental property is Section B property | Section B column (b)(i), "trade, business, rental, or royalty property" |
| Filing Section A for a vehicle used 80% for Uber driving | 80% business → Section B | 80% Section B (b)(i), 20% Section A |
| Deducting inventory destruction twice | Inventory loss can go through COGS or be deducted separately, not both (Pub. 547, "Loss of inventory") | If taken through COGS, include reimbursement in income and skip Form 4684; if deducted separately, reduce opening inventory or purchases |
| Claiming employee tool loss on Section B | Employee-property casualty losses cannot be deducted (2025 instructions, Section B caution) | Not deductible; do not enter |

---

## Federally declared disaster — definitions

A "federally declared disaster" is an event the President has declared as a major disaster (FEMA-DR) or emergency (FEMA-EM) under the Stafford Act.

- Major disasters: typically hurricanes, wildfires, floods, tornadoes
- Emergencies: typically narrower, time-limited federal response
- Both are federally declared disasters for §165(h)(5) and §165(i) (2025 instructions, "Definitions"; Reg. §1.165-11(b)(1)). Only a major disaster can be a qualified disaster.

The "disaster area" is the geographic area covered by the declaration. The user's property must be **in** the declared area, and the loss must be **caused by** the declared disaster.

A "qualified disaster loss" gets enhanced treatment: $500 reduction instead of $100, no 10% AGI floor, and deductible without itemizing (added to the standard deduction). The 2025 instructions cover major disasters declared January 1, 2020 – September 2, 2025 with an incident period beginning December 28, 2019 – July 4, 2025 and ending by August 3, 2025. P.L. 119-108 (Sept. 11, 2026) replaced that window for tax years beginning after December 31, 2024 with IRC §165(h)(6): any Stafford Act §401 major disaster whose incident period begins on or after December 28, 2019 and before January 1, 2027.

Lookup tools:
- FEMA disaster page: https://www.fema.gov/disaster/declarations
- IRS tax relief in disaster situations: https://www.irs.gov/newsroom/tax-relief-in-disaster-situations

Check https://www.irs.gov/forms-pubs/about-form-4684 and https://www.irs.gov/DisasterTaxRelief for IRS guidance issued after the 2025 instructions (Dec 19, 2025), including guidance implementing P.L. 119-108.
