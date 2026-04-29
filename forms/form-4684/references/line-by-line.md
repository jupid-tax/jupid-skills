# Form 4684 Line-by-Line Reference

Complete lookup for every line on Form 4684. Use this when the agent needs to confirm what a line means or where a value goes.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on return | Filer's name as on Form 1040 | Match the 1040 exactly |
| Identifying number | SSN (individuals) or EIN (entities) | |
| FEMA disaster declaration number | Format: "DR-####-XX" or "EM-####-XX" + state | Required for Section A losses post-TCJA. Look up at https://www.fema.gov/disaster/declarations |

The FEMA number must match an actual declaration. If the user reports a loss in an event that was *not* declared, Section A is unavailable (IRC §165(h)(5), effective 2018-2025).

---

## Section A — Personal-Use Property (federally declared disaster only)

Section A is for losses to property held for personal use (home, household goods, personal vehicle). Post-TCJA, deductible only if the loss is attributable to a federally declared disaster.

Each Form 4684 Section A handles up to four properties (A, B, C, D) damaged in **one casualty event**. Multiple events = multiple Forms 4684 (or roll-up at Lines 13-18).

### Per-item detail (Lines 1-9)

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 1 | Description of properties (A, B, C, D) | Plain English: "Single-family home, 123 Main St" | Generic categories like "personal property" |
| 2 | Cost or other basis | Adjusted basis: cost + improvements − prior depreciation | Replacement cost. FMV. Insured value. |
| 3 | Insurance or other reimbursement | Amount received OR reasonably expected | Pending claims with no estimable recovery |
| 4 | Gain (Line 3 − Line 2 if positive) | Triggers gain reporting; consider §1033 deferral | Always zero if reimbursement ≤ basis |
| 5 | FMV before casualty | Pre-loss market value | Original cost |
| 6 | FMV after casualty | Post-loss market value (zero if destroyed) | Salvage value of debris only |
| 7 | Decline in FMV (Line 5 − Line 6) | Auto | |
| 8 | Smaller of Line 2 or Line 7 | Auto: deductible loss before reimbursement | |
| 9 | Subtract Line 3 from Line 8 (≥ 0) | Loss after insurance | If negative, set to zero |

**Critical rule for Line 8**: The loss is the **smaller** of basis (Line 2) or decline-in-FMV (Line 7). This is the "lesser-of" rule from Reg. §1.165-7(b)(1). For appreciated property, the deduction is capped at basis. For depreciated property, the deduction is capped at the decline.

### Per-event aggregation (Lines 10-12)

| Line | Field | What goes here |
|------|-------|----------------|
| 10 | Casualty/theft loss | Sum of Line 9 across properties A-D for THIS event |
| 11 | $100 reduction per casualty | Statutory; IRC §165(h)(1). One $100 per event. |
| 12 | Subtract Line 11 from Line 10 | Auto |

**Critical rule for Line 11**: $100 per **casualty event**, not per property. Hurricane Helene damaging both your roof and your car = ONE event = ONE $100 reduction. Two unrelated events (hurricane and a separate fire) = two $100 reductions.

### Roll-up across events (Lines 13-18)

| Line | Field | What goes here |
|------|-------|----------------|
| 13 | Total of Line 12 across all events / forms | If user has multiple Forms 4684, sum here |
| 14 | Total gains from casualty/theft (Line 4 across) | If insurance > basis on any property |
| 15 | Line 14 − Line 13, if positive | Net gain (rare); flows differently |
| 16 | If Line 14 < Line 13, the loss | Net loss before AGI floor |
| 17 | 10% of AGI | IRC §165(h)(2). One floor across the entire return. |
| 18 | Line 16 − Line 17 | Final personal-use casualty loss → Schedule A Line 15 |

If Line 18 ≤ 0, no deduction. Tell the user.

---

## Section B — Business and Income-Producing Property

Section B has no AGI floor and no $100 reduction. The full loss flows through to Form 4797 (business) or Schedule A (income-producing).

Section B is split into two parts and uses two columns within Part I.

### Section B columns

| Column | What it covers |
|--------|----------------|
| (b)(i) Trade or business | Property used in the user's trade/business (Schedule C, F, partnership, S-corp). Loss is ordinary on Form 4797. |
| (b)(ii) Income-producing | Property held for investment or rental, not in a trade/business. Loss flows to Schedule A Line 16. |

### Part I — Casualty or Theft Gain or Loss (Lines 19-27)

| Line | Field | What goes here |
|------|-------|----------------|
| 19 | Description of properties | Plain English |
| 20 | Cost or other basis | Adjusted basis (cost − prior depreciation) |
| 21 | Insurance/reimbursement | Received or reasonably expected |
| 22 | Gain (Line 21 − Line 20 if pos) | Triggers gain reporting |
| 23 | FMV before | |
| 24 | FMV after | |
| 25 | Decline (Line 23 − Line 24) | Auto |
| 26 | Smaller of Line 20 or Line 25 | Auto |
| 27 | Subtract Line 21 from Line 26 (≥ 0) | Loss after insurance |

**Important difference from Section A**: For business property that is *totally destroyed*, the loss is the full adjusted basis even if FMV before was less than basis (Reg. §1.165-7(b)(1)). The "smaller of" rule still applies for partial destruction.

### Part II — Roll-up (Lines 28-39)

The roll-up separates short-term vs. long-term holding period and pushes the totals to Form 4797 or Schedule A.

| Line | Field | What goes here |
|------|-------|----------------|
| 28 | Casualty/theft loss totals (by holding period) | Sum of Line 27, separated by ≤1yr / >1yr |
| 29-31 | (continuation of Line 28) | |
| 32 | Total gains | Sum of Line 22 |
| 33-34 | (continuation of Line 32) | |
| 35-37 | Loss roll-ups | |
| 38 | Net loss (trade/business) → Form 4797 Line 14 | Ordinary loss |
| 39 | Net loss (income-producing) → Schedule A Line 16 | Itemized deduction (not subject to 2% floor under TCJA carve-out for §165(c)(2) losses; verify against current instructions) |

If Section B nets to a gain, the gain may qualify for §1033 deferral if reinvested. Out of scope for this skill.

---

## Section C — Theft Loss Deduction for Ponzi-Type Investment Fraud

Section C is for theft losses qualifying under the Rev. Proc. 2009-20 safe harbor for fraudulent investment schemes (Madoff-style frauds).

| Line | Field | What goes here |
|------|-------|----------------|
| 40-41 | Initial investment + subsequent contributions | Cost basis |
| 42 | Income reported in prior years | Add to basis |
| 43 | Withdrawals | Subtract from basis |
| 44 | Discoveries / recoveries | |
| 45 | Computed deductible theft loss | Auto, applying the safe-harbor percentage (95% if no third-party recovery pursued; 75% if pursuing) |

Most filers will not need Section C. If the user qualifies, the safe harbor sidesteps the per-event $100 floor and 10% AGI floor for Section A — but only because Section C is itself a special path. Consult Pub 547 + Rev. Proc. 2009-20 carefully.

---

## Section D — Election to Deduct Federally Declared Disaster Loss in Preceding Year

A check-the-box election allowing the user to claim a federally declared disaster loss in the **year before** the year of the loss. IRC §165(i).

To elect:
- Check the Section D box
- File Form 4684 with the prior-year return (or Form 1040-X amending it)
- Attach a statement with:
  - "Election under IRC §165(i) to deduct loss in preceding year"
  - FEMA disaster declaration number
  - Date of the loss
  - Property address
  - Filer name and SSN
- Election deadline: generally six months after the original due date of the loss-year return; verify against current Pub 547

Election is **irrevocable** once filed.

When the election makes sense:
- Prior year had higher AGI → 10% floor was lower (relative)
- Prior year had higher tax bracket → bigger marginal benefit
- User wants the refund sooner (amended-return refunds usually arrive in 8-16 weeks)

When it doesn't:
- Loss year has higher tax bracket
- Prior year already had a casualty loss carrying its own 10% floor

---

## Holding period notes

For Section B, holding period determines whether a casualty gain (if any) is short-term or long-term. The casualty loss itself is ordinary regardless of holding period for trade/business property; for income-producing property the character is determined by the asset's character.

- Held ≤ 1 year: short-term
- Held > 1 year: long-term
- Special rules for inherited property (always long-term basis is FMV at date of death)

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
- Year of deduction = year theft is **discovered**, not committed

Insurance fraud / misrepresentation losses sometimes qualify; consult Pub 547.
