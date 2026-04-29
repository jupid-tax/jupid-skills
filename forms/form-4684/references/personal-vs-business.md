# Personal-Use vs. Business / Income-Producing Property

The single most important classification on Form 4684. It determines:
- Which Section (A, B, or both) to file
- Whether the §165(h)(5) federally-declared-disaster restriction applies (Section A only, post-TCJA, through 2025)
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

**Post-TCJA restriction (IRC §165(h)(5))**: For tax years 2018-2025, personal-use casualty/theft losses are deductible **only** if attributable to a federally declared disaster. A house fire that destroys your home is NOT deductible if the fire wasn't part of a declared disaster. A theft of personal property is NOT deductible at all (no theft is part of a federally declared disaster).

The Section A floors:
- $100 per casualty event (Line 11)
- 10% of AGI floor across all Section A losses (Line 17)

The deductible result flows to **Schedule A Line 15** (itemized deduction). If the user takes the standard deduction, there is NO tax benefit from a Section A casualty loss.

### 2. Trade or business property → Section B, column (b)(i)

Property used in a trade or business that the user actively operates:
- Schedule C business assets (laptop used 100% for self-employment, business vehicle, equipment)
- Inventory (special rules — usually deducted via Schedule C COGS, not Form 4684)
- Rental real estate IF the user is a real-estate dealer or active real-estate professional under §469(c)(7) (otherwise income-producing, see below)
- Farm equipment (Schedule F filers)
- Partnership / S-corp business assets passed through to the user

The Section B trade/business loss flows to **Form 4797 Part II Line 14** as an ordinary loss. No floors. No AGI threshold.

### 3. Income-producing property → Section B, column (b)(ii)

Property held for the production of income but NOT used in a trade or business:
- Rental real estate (most rentals — passive activity)
- Investment property held for appreciation
- A car held purely for investment (rare)
- A vacation home rented out part of the year

The Section B income-producing loss flows to **Schedule A Line 16**. Under TCJA, miscellaneous itemized deductions subject to the 2% floor are suspended through 2025 — but a §165(c)(2) loss from a transaction entered into for profit is NOT a 2%-floor item. It's deductible without the 2% floor. Verify against current Schedule A instructions before filing.

### 4. Mixed-use property (special rules)

If property is used partly for business and partly for personal:

- The business-use portion follows Section B rules (no floor).
- The personal-use portion follows Section A rules (federally-declared-disaster restriction, $100 floor, 10% AGI floor).
- Allocate by business-use percentage.

Example: Home with a 200 sq ft home office in a 2,000 sq ft house = 10% business use. A $100,000 loss to the structure is split as $10,000 business (Section B) and $90,000 personal (Section A, only if FEMA disaster).

Example: Vehicle used 60% for business and 40% personal = 60% Section B, 40% Section A.

### 5. Employee property (post-TCJA: usually not deductible)

Property used in employment (employee tools, work clothing, etc.). Pre-TCJA, deductible as a miscellaneous itemized deduction subject to 2% AGI floor. Post-TCJA (2018-2025), the 2%-floor miscellaneous deductions are suspended. A casualty loss to employee property generally provides no current deduction.

Exception: certain qualified performing artists, fee-basis state/local government officials, and reservists can still deduct unreimbursed employee expenses above the line. If the user is in one of those narrow categories, treat as Section B income-producing (verify with the current Form 4684 instructions).

---

## The classification questionnaire

Ask the user these questions in order:

1. **"Was this property used in a business you operate (Schedule C, F, partnership, S-corp)?"**
   - Yes → Section B, trade/business
   - No → continue

2. **"Was this property held for rental, investment, or other profit-seeking purpose?"**
   - Yes → Section B, income-producing
   - No → continue

3. **"Was this your home, personal vehicle, or other personal-use property?"**
   - Yes → Section A
   - No → unusual; investigate (might be employee property → see Section 5 above)

4. **For Section A only: "Was the property in a FEMA-declared federal disaster area when the loss occurred?"**
   - Yes → continue with Section A; record the FEMA-DR number
   - No → loss is NOT deductible (post-TCJA, through 2025); STOP

5. **For mixed-use (home office, business vehicle): "What percentage was business use?"**
   - Allocate; split between Sections.

---

## Common classification mistakes

| Mistake | Why it's wrong | Correct treatment |
|---------|----------------|-------------------|
| Filing Section A for a non-disaster house fire (2018-2025) | §165(h)(5) bars it | Loss not deductible; do not file Form 4684 |
| Filing Section A for theft of personal property | No theft is "federally declared disaster" | Loss not deductible (Section A); see if any business-use portion qualifies for Section B |
| Filing Section B for a personal vehicle stolen during a business trip | Personal-use property; the trip's purpose doesn't change classification | Section A (and only if FEMA disaster, which a theft never is) |
| Filing Section A for a rental property loss | Rentals are income-producing | Section B column (b)(ii) |
| Filing Section A for a vehicle used 80% for Uber driving | 80% business → Section B | 80% Section B (b)(i), 20% Section A |
| Treating inventory destruction as Form 4684 | Inventory loss flows through COGS | Adjust Schedule C Lines 35-42 (purchases / inventory); not Form 4684 |
| Claiming employee tool loss on Section B | TCJA suspended unreimbursed employee expenses | Generally not deductible (2018-2025); confirm against Pub 547 |

---

## Federally declared disaster — definitions

A "federally declared disaster" is an event the President has declared as a major disaster (FEMA-DR) or emergency (FEMA-EM) under the Stafford Act.

- Major disasters: typically hurricanes, wildfires, floods, tornadoes
- Emergencies: typically narrower, time-limited federal response
- Both qualify for §165(h)(5) treatment (verify in current Pub 547 — there have been distinctions in some years)

The "disaster area" is the geographic area covered by the declaration. The user's property must be **in** the declared area, and the loss must be **caused by** the declared disaster.

A "qualified disaster loss" (different from any federally declared disaster) gets enhanced treatment — Congress periodically passes laws elevating specific disasters to qualified status (no 10% AGI floor, simpler election, etc.). The list changes over time; check Pub 547 for the current qualified-disaster list.

Lookup tools:
- FEMA disaster page: https://www.fema.gov/disaster/declarations
- IRS tax relief in disaster situations: https://www.irs.gov/newsroom/tax-relief-in-disaster-situations

The IRS publishes notices when Congress designates qualified disasters; the agent should search "IRS [year] qualified disaster" before filing.
