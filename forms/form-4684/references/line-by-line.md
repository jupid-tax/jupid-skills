# Form 4684 Line-by-Line Reference

Complete lookup for every line on Form 4684. Use this when the agent needs to confirm what a line means or where a value goes.

Verified against the 2025 Form 4684 ("Created 9/26/25") and the 2025 Instructions for Form 4684 (Dec 19, 2025). Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-4684.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on return | Filer's name as on Form 1040 | Match the 1040 exactly |
| Identifying number | SSN (individuals) or EIN (entities) | |
| Federally declared disaster box (above line 1) | Check if the loss is attributable to a federally declared disaster | |
| FEMA disaster declaration number | "DR-" or "EM-" plus four digits, e.g. "DR-4865" (instructions example) | Look up at https://www.fema.gov/disaster/declarations. Also enter the ZIP code of the most affected property on line 1, Property A. |

The FEMA number must match an actual declaration. If the user reports a personal-use loss in an event that was *not* declared, the loss can only offset personal casualty gains (line 14, Worksheet 1-1). IRC §165(h)(5) applies to tax years beginning after 2017; P.L. 119-21 §70109 made it permanent and adds State declared disasters for tax years beginning after 2025.

---

## Section A — Personal-Use Property

Section A is for losses to property not used in a trade or business or for income-producing purposes (home, household goods, personal vehicle). It also covers the home-office part of a home when the user figured the home office deduction with the simplified method (instructions, "Which Sections To Complete"). Deductible only if the loss is attributable to a federally declared disaster (or, for 2026 and later, a State declared disaster), except to the extent of personal casualty gains.

Use a separate Form 4684 through line 12 for each casualty or theft event. Each event has four property columns (A, B, C, D); for more than four items, attach additional sheets in the format of lines 1 through 9. Lines 13 through 18 are completed on one Form 4684 only.

### Per-item detail (Lines 1-9)

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 1 | Description of properties (A, B, C, D) | Type, location (city, state, ZIP), date acquired. If the FEMA box is checked, ZIP of the most affected property on the Property A line | Generic categories like "personal property" |
| 2 | Cost or other basis | Cost + improvements, minus any postponed gain from a previous main home sale | Replacement cost. FMV. Insured value. |
| 3 | Insurance or other reimbursement | Received or expected, whether or not a claim was filed (instructions for line 3) | Grants with no conditions on use |
| 4 | Gain from casualty or theft | Line 3 − Line 2 if line 3 is larger; then skip lines 5-9 for that column. Only reimbursement actually claimed counts toward a gain | |
| 5 | FMV before casualty or theft | Pre-loss market value | Original cost |
| 6 | FMV after casualty or theft | Post-loss market value (zero if destroyed or stolen and not recovered) | |
| 7 | Line 5 − Line 6 | Decline in FMV. With a Rev. Proc. 2018-08 safe harbor, leave 5 and 6 blank and enter the safe-harbor decline here, with an attached statement naming the method | |
| 8 | Smaller of Line 2 or Line 7 | | |
| 9 | Line 8 − Line 3 (if zero or less, enter -0-) | Loss after insurance | |

**Critical rule for Line 8**: The loss is the **smaller** of basis (Line 2) or decline-in-FMV (Line 7). This is the "lesser-of" rule from Reg. §1.165-7(b)(1). For appreciated property, the deduction is capped at basis. For depreciated property, the deduction is capped at the decline. For personal-use real estate, measure the decline for the property as a whole (land, building, trees, shrubs as one item; Reg. §1.165-7(b)(2)(ii)).

### Per-event aggregation (Lines 10-12)

| Line | Field | What goes here |
|------|-------|----------------|
| 10 | Casualty or theft loss | Sum of Line 9 across properties A-D for THIS event |
| 11 | $100 per casualty ($500 if qualified disaster loss rules apply) | IRC §165(h)(1). $500 only when the event is a qualified disaster and line 10 is larger than the total of line 4 on all Forms 4684 (instructions for line 11) |
| 12 | Line 10 − Line 11 (if zero or less, enter -0-) | |

**Critical rule for Line 11**: $100 per **casualty event**, not per property. A hurricane damaging both your home and your car = ONE event = ONE reduction. Two unrelated events = two reductions (Reg. §1.165-7(b)(4)(ii); Pub. 547 Table 2).

**Qualified disaster losses.** The 2025 instructions define them as losses attributable to a major disaster declared January 1, 2020 – September 2, 2025 with an incident period that began December 28, 2019 – July 4, 2025 and ended by August 3, 2025 (plus older listed disasters; not COVID-19-only declarations). P.L. 119-108 (Sept. 11, 2026) added IRC §165(h)(6) for tax years beginning after December 31, 2024: a major disaster declared under Stafford Act §401 whose incident period begins on or after December 28, 2019 and before January 1, 2027. Emergency (EM) declarations and State declared disasters are not qualified disasters.

### Roll-up across events (Lines 13-18, one Form 4684 only)

| Line | Field | What goes here |
|------|-------|----------------|
| 13 | Add line 4 of all Forms 4684 | Total personal casualty gains |
| 14 | Add line 12 of all Forms 4684 | Total losses. If any loss is not attributable to a federally declared disaster, use Worksheet 1-1: disaster losses + smaller of (non-disaster losses or line 13) |
| 15 | Net gain, zero, or net qualified disaster loss | If 13 > 14: difference → Schedule D (short-term to line 4, long-term to line 11), stop. If equal: 0, stop. If 13 < 14 with no qualified disaster losses: 0, go to 16. If 13 < 14 with qualified disaster losses: smaller of (14 − 13) or line 12 of the qualified-disaster Form 4684 → Schedule A line 16, "Net Qualified Disaster Loss"; stop if all losses are qualified |
| 16 | Line 14 − (Line 13 + Line 15) | Net loss subject to the AGI floor |
| 17 | 10% of AGI | Form 1040, 1040-SR, or 1040-NR line 11b. IRC §165(h)(2). One floor across the entire return |
| 18 | Line 16 − Line 17 (if zero or less, enter -0-) | → Schedule A (Form 1040) line 15, or Schedule A (Form 1040-NR) line 6 |

If Line 18 is zero and line 15 is zero, no deduction. Tell the user.

A net qualified disaster loss on line 15 can be claimed without itemizing: enter it on the dotted line next to Schedule A line 16 as "Net Qualified Disaster Loss", enter the standard deduction there as "Standard Deduction Claimed With Qualified Disaster Loss", and carry the total to Schedule A line 16 and Form 1040 line 12e (instructions, "Increased standard deduction reporting").

---

## Section B — Business and Income-Producing Property

Section B has no AGI floor and no $100 reduction. Use one Part I (lines 19-28) for each casualty or theft and one Part II (lines 29-39) to summarize all of them.

### Part I — Casualty or Theft Gain or Loss (Lines 19-28)

| Line | Field | What goes here |
|------|-------|----------------|
| 19 | Description of properties | Type, location, date acquired. For a fraud loss not using Section C: name, TIN (if known), and address of the person or entity |
| 20 | Cost or adjusted basis | Cost + improvements − depreciation allowed or allowable (including §179), amortization, depletion |
| 21 | Insurance/reimbursement | Received or expected (same rules as line 3) |
| 22 | Gain (Line 21 − Line 20 if line 21 is larger) | Enter here and on line 29 or 34, column (c) (or line 33 if recapture applies); skip lines 23-27 for that column |
| 23 | FMV before | |
| 24 | FMV after | |
| 25 | Line 23 − Line 24 | |
| 26 | Smaller of Line 20 or Line 25 | If the property was totally destroyed or stolen, enter the line 20 amount |
| 27 | Line 26 − Line 21 (if zero or less, enter -0-) | Loss after insurance. Home used for business: deductible loss from Form 8829 line 35 or a §280A(c)(5) statement |
| 28 | Casualty or theft loss | Sum of line 27 (or Section C line 51); allocate between line 29 (held 1 year or less) and line 34 (more than 1 year) |

**Important difference from Section A**: For business or income-producing property that is *totally destroyed*, the loss is the full adjusted basis even if FMV before was less than basis (Reg. §1.165-7(b)(1); form note on line 26). The "smaller of" rule still applies for partial damage. Figure each item separately: a building and trees on the same lot are separate items (Reg. §1.165-7(b)(2)(i)).

### Part II — Summary of Gains and Losses (Lines 29-39)

Columns: (a) identify the casualty or theft; (b)(i) trade, business, rental, or royalty property; (b)(ii) income-producing property (investment property such as stocks, notes, bonds, gold, silver, vacant lots, works of art); (c) gains includible in income.

| Line | Field | What goes here |
|------|-------|----------------|
| 29 | Property held 1 year or less | One line per event: losses in (b)(i)/(b)(ii), gains in (c) |
| 30 | Totals of line 29 | |
| 31 | Line 30 (b)(i) + (c) | Net gain or loss → Form 4797 line 14. If Form 4797 is not otherwise required: Schedule 1 (Form 1040) line 4, check "4684" |
| 32 | Line 30 (b)(ii) | Individuals → Schedule A line 16 (not employee property). Estates/trusts: "Other deductions"; partnerships: Form 1065 Sch. K line 13e; S corps: Form 1120-S Sch. K line 12e |
| 33 | Casualty or theft gains from Form 4797 line 32 | Use when depreciation recapture applies (Form 4797 Part III), instead of line 34 |
| 34 | Property held more than 1 year | One line per event |
| 35 | Total losses (line 34 (b)(i) and (b)(ii)) | |
| 36 | Total gains (line 33 + line 34 column (c)) | |
| 37 | Line 35 (b)(i) + (b)(ii) | |
| 38a | If the loss on 37 is more than the gain on 36: line 35 (b)(i) + line 36 | → Form 4797 line 14 (or Schedule 1 line 4 if Form 4797 is not otherwise required) |
| 38b | Same condition: line 35 (b)(ii) | Individuals → Schedule A line 16 |
| 39 | If the loss on 37 is less than or equal to the gain on 36: line 36 + line 37 | → Form 4797 line 3 (§1231). Partnerships: Form 1065 Sch. K line 11 |

Income-producing losses on lines 32 and 38b are Schedule A line 16 "other itemized deductions" (2025 Schedule A instructions list them there), so they help only an itemizer. Employee-use property losses cannot be deducted or used in this netting (instructions, Section B caution).

If Section B nets to a gain, the gain may qualify for §1033 postponement if reinvested. Out of scope for this skill beyond flagging it.

---

## Section C — Theft Loss Deduction for Ponzi-Type Investment Scheme (Rev. Proc. 2009-20)

Section C is for theft losses where the user qualifies for and chooses the Rev. Proc. 2009-20 safe harbor (as modified by Rev. Proc. 2011-58). It replaces Appendix A of Rev. Proc. 2009-20.

| Line | Field | What goes here |
|------|-------|----------------|
| 40 | Initial investment | Cash or basis of property first invested |
| 41 | Subsequent investments | Including reinvested amounts |
| 42 | Income reported on returns for years before the discovery year | Net income from the arrangement included in income, even closed years |
| 43 | Lines 40 + 41 + 42 | |
| 44 | Withdrawals for all years | Income or principal |
| 45 | Line 43 − Line 44 | Total qualified investment |
| 46 | 0.95 or 0.75 | 0.95 if no potential third-party recovery; 0.75 if pursuing one |
| 47 | Line 46 × Line 45 | |
| 48 | Actual recovery | Received from any source |
| 49 | Potential insurance/SIPC recovery | |
| 50 | Line 48 + Line 49 | Total recovery |
| 51 | Line 47 − Line 50 | Deductible theft loss → Section B line 28; skip lines 19-27; complete Section B Part II |

Part II of Section C holds the required declarations (name, TIN, address of the person or entity; qualified-investor status under Rev. Proc. 2009-20 §4.03; no third-party recovery if 0.95 was used). The user agrees to them by signing the return.

A theft loss from a transaction entered into for profit is not a personal casualty loss, so the $100 and 10% AGI rules do not apply (Pub. 547, "Deduction Limits": losses on business and income-producing property aren't subject to these rules; see also Rev. Rul. 2009-9). Victims of other financial scams use Section B Part I (instructions, "Losses From Financial Scams").

---

## Section D — Election To Deduct Federally Declared Disaster Loss in Preceding Tax Year

Part I is the §165(i) election statement; Part II revokes a prior election. Section D goes on the **preceding year's** Form 4684 (for a 2025 disaster-year loss, the 2024 Form 4684), attached to that year's original or amended return.

| Line | Field | What goes here |
|------|-------|----------------|
| 52 | Name or description of the federally declared disaster | e.g., the FEMA disaster title and DR number |
| 53 | Date or dates of the loss (mm/dd/yyyy) | |
| 54 | Address of the damaged property | City or town, county or parish, state, ZIP |
| 55 | (Revocation) Disaster and property address for the prior election | |
| 56 | (Revocation) Date the prior election was filed | |
| 57 | (Revocation) Payment or arrangement to repay the credit or refund from the prior election | |

Rules (Reg. §1.165-11; Rev. Proc. 2016-53):
- Due date: 6 months after the regular due date (without extensions) of the disaster-year return. For a 2025 disaster-year loss of a calendar-year individual: October 15, 2026.
- The election covers the entire loss from that disaster for the disaster year (Reg. §1.165-11(c)).
- Revocation: on an amended preceding-year return, on or before 90 days after the election due date, and before filing the disaster-year return that claims the loss (Reg. §1.165-11(d), (g)).
- Do not claim the same loss in both years (Reg. §1.165-11(d)).

When the election makes sense:
- Prior year had a higher marginal rate → bigger benefit
- Prior year had lower AGI → smaller 10% floor (not relevant to qualified disaster losses, which have no floor)
- User wants the refund sooner

When it doesn't:
- Loss year has the higher marginal rate
- The loss would lose qualified-disaster treatment in the prior year (P.L. 119-108 applies only to tax years beginning after December 31, 2024)

---

## Holding period notes

For Section B, the holding period decides whether an item goes on line 29 (1 year or less) or line 34 (more than 1 year). Count from the day after you received the property and include the day of the casualty or theft (instructions for line 15).

- Held 1 year or less: lines 29-32
- Held more than 1 year: lines 33-39
- Inherited property is generally treated as held more than 1 year

For Section A, a net gain on line 15 is split into short-term (Schedule D line 4) and long-term (Schedule D line 11) by the same holding-period test.

---

## What "casualty" means (for line entries)

Sudden, unexpected, or unusual event. From Pub 547:

| Qualifies as casualty | Does NOT qualify |
|-----------------------|-------------------|
| Hurricane, tornado, earthquake | Gradual decline / wear and tear |
| House fire (sudden) | Termite damage (gradual) |
| Vandalism | Mold caused by progressive water damage |
| Sonic boom, terrorist action | Drought (typically gradual; some exceptions) |
| Mine cave-in (sudden) | Stock market loss (no physical damage) |
| Vehicle accident not caused by willful act | Lost or misplaced property |

If the event doesn't fit, the loss is not deductible on Form 4684. Tell the user.

---

## What "theft" means

The taking of property with the intent to deprive the owner of it, illegal under state law. From Pub 547:

- Larceny, robbery, embezzlement, blackmail, extortion, kidnap-for-ransom (rare)
- Must be intentional, illegal under state law where it occurred
- Police report strongly recommended (not required by IRS but expected)
- Mysterious disappearance (lost wallet, missing jewelry with no evidence of theft) does NOT qualify as theft
- Year of deduction = year theft is **discovered**, not committed (Reg. §1.165-1(d)(3))

Insurance fraud / misrepresentation losses sometimes qualify; consult Pub 547.
