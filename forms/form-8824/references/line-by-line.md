# Form 8824 Line-by-Line Reference

Complete lookup for every line on Form 8824. Use this when the agent needs to confirm where a number belongs or what a line means.

---

## Header

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name(s) shown on return | Filer's legal name | Match the 1040 / 1065 / 1120-S |
| (top) | Identifying number | SSN, EIN, or ITIN | Match the parent return |

A separate Form 8824 must be filed for **each** like-kind exchange (or each multi-asset exchange group). If the user did two exchanges in the same year, they file two Form 8824s.

---

## Part I — Information on the Like-Kind Exchange

### Line 1 — Description of like-kind property given up

Plain English description of the relinquished property. Best practice: include the address and short asset type.

Examples:
- "Single-family rental home at 123 Main Street, Phoenix, AZ 85001"
- "Commercial warehouse at 456 Industrial Blvd, Reno, NV 89501"
- "Undeveloped 5-acre parcel at parcel #12-345-678, Travis County, TX"

Avoid vague entries like "rental property" — the IRS uses Line 1 to match the relinquished property to the seller's prior depreciation schedule.

### Line 2 — Description of like-kind property received

Same format as Line 1, for the replacement property. Both must be **real property** held for productive use in a trade or business or for investment (post-TCJA, exchanges completed after 2017-12-31).

### Line 3 — Date like-kind property given up was originally acquired

The date the user originally acquired the relinquished property — not the exchange date. Format MM/DD/YYYY.

This sets the holding period for prior depreciation and §1250 recapture analysis.

### Line 4 — Date you actually transferred your property given up

The date the deed or title transferred to the third-party buyer (in a delayed exchange) or to the swap counterparty (in a simultaneous exchange).

**This is the start of the 45-day and 180-day clocks.**

### Line 5 — Date like-kind property received was identified

The date the user delivered written identification of replacement property to the QI (or seller, in simultaneous exchanges).

Identification rules (IRC §1031(a)(3)(A) + Treas. Reg. §1.1031(k)-1(c)):
- Must be in writing
- Must be signed
- Must be delivered to a person involved in the exchange (typically QI), NOT to a related party of the user
- Must unambiguously describe the property (legal description or street address)

The "three-property", "200%", and "95%" identification rules govern how many properties can be identified. See [`timing-rules.md`](./timing-rules.md).

**If Line 5 minus Line 4 > 45 days, the exchange fails. Stop and recognize gain normally.**

### Line 6 — Date you actually received the like-kind property

The date title to the replacement property transferred to the user (or to the QI, who then conveyed to the user).

**Must be ≤ 180 days after Line 4 OR ≤ the due date of the user's tax return (including extensions) for the year of Line 4 — whichever is earlier.**

Practical note: a transfer in late November (Line 4) gives a 180-day deadline of late May. A transfer in early November of an extension-filer's year may be limited by the October 15 extension date. Always compute both and use the earlier.

### Line 7 — Was the exchange of property given up or received made with a related party?

Yes/No.

"Related party" per IRC §1031(f)(3) → IRC §267(b) and §707(b)(1):
- Family members: spouse, ancestors (parents, grandparents), lineal descendants (children, grandchildren), siblings (full or half-blood)
- Controlled entity: a corporation in which the user (and their family) owns more than 50% of the stock by value
- Partnership in which the user owns more than 50% of capital or profits
- Trusts where the user is grantor/beneficiary in certain configurations
- Other family-controlled or constructive-ownership relationships

If Yes → Part II is required.

NOT related: in-laws (except spouse), step-relatives, friends, business partners (unless partnership ≥50%-owned), unrelated tenants in common.

---

## Part II — Related-Party Exchange Information

### Line 8 — Related party's name, address, and identifying number

Full legal name, mailing address, and SSN (for individuals) or EIN (for entities). The IRS uses this to track both sides of the exchange against the 2-year rule.

### Line 9 — Relationship to you

Specify the relationship: "father", "wholly-owned LLC", "controlled corporation (75% ownership)", etc.

### Line 10 — During this tax year, did the related party sell or dispose of any part of the like-kind property received in the exchange? Did you sell or dispose of any part of the like-kind property received from the related party?

Yes/No.

If Yes — and the disposition was within 2 years of the exchange — the §1031 deferral is **un-done**: gain recognized in the current year on the original exchange. See [`related-party.md`](./related-party.md).

### Line 11 — If "Yes" on Line 10, complete one of these exception boxes

Three exceptions to the 2-year rule (IRC §1031(f)(2)):
- Death of either party (a) — automatic
- Compulsory or involuntary conversion (b) — §1033 governs the new property; deferral preserved
- Establish to the satisfaction of the IRS that neither the original exchange nor the disposition had as one of its principal purposes the avoidance of federal income tax (c) — high bar; needs supporting documentation

If none of these applies and Line 10 is Yes within 2 years, recognize the deferred gain on this year's return.

---

## Part III — Realized Gain or (Loss), Recognized Gain, and Basis of Like-Kind Property Received

### Line 12 — FMV of OTHER (non-like-kind) property given up

Used only when the user gave up additional property along with the like-kind real estate. Examples:
- Stock or bonds bundled into the deal
- Vehicles or equipment thrown in
- Personal property (furniture, equipment) included with a building sale that wasn't separately allocated

Most §1031 exchanges have $0 here. Post-TCJA, any non-like-kind property given up is fully recognized — there's no shielding.

### Line 13 — Adjusted basis of OTHER property given up

The user's adjusted basis in the non-like-kind property given up. Original cost + improvements − depreciation taken.

### Line 14 — Gain or (loss) on OTHER property given up

Line 12 − Line 13. **Always recognized**, regardless of §1031 status of the rest of the deal. Reported on Schedule D / Form 4797 / Form 1040 according to character of the asset.

### Line 15 — Cash received, FMV of other property received, plus net liabilities assumed by other party

This is **boot received**. Components:
- Cash received from QI (after replacement was acquired) → cash boot
- FMV of any non-like-kind property received from the other party → other boot
- Net liabilities assumed by other party (mortgage on relinquished that the other party now owes − mortgage on replacement that you assumed). If net is negative (you assumed more debt), enter $0; you don't get mortgage boot for paying down debt.
- LESS exchange expenses paid out of the exchange proceeds (QI fees, escrow, etc.)

Boot received triggers gain recognition up to the amount of realized gain (Line 19).

### Line 16 — FMV of like-kind property you received

The fair market value of the replacement real property at the time of receipt.

### Line 17 — Add Lines 15 and 16

Total value received in the exchange.

### Line 18 — Adjusted basis of like-kind property you gave up + net amounts paid + exchange expenses

Components:
- Adjusted basis of relinquished property (original cost + improvements − depreciation taken)
- PLUS cash you paid to other party (cash boot paid)
- PLUS net liabilities you assumed (debt on replacement − debt on relinquished, if positive; else $0)
- PLUS exchange expenses paid (the portion not netted against boot received in Line 15)

This represents the "give" side — what the user contributed to the exchange.

### Line 19 — Realized gain or (loss)

Line 17 − Line 18.

- Positive → realized gain. §1031 will defer some/all.
- Negative → realized loss. §1031 disallows loss recognition; the loss is deferred into basis of replacement.

### Line 20 — Smaller of Line 15 or Line 19, but not less than zero

Recognized gain attributable to boot received.

- If Line 15 (boot) is $0, Line 20 is $0 (full deferral, no boot triggered gain).
- If Line 15 > Line 19 (boot exceeds realized gain — rare), Line 20 = Line 19 (recognize all realized gain).
- If Line 19 < 0 (realized loss), Line 20 = 0 (no loss recognized via boot).

### Line 21 — Ordinary income under recapture rules

Depreciation recapture under IRC §1245 (rare for real property) or §1250.

Most §1031 real property has §1250 unrecaptured gain (up to 25% federal rate) which is **not** ordinary income — Line 21 stays $0 for most real-property exchanges. Line 21 captures *only* §1245 ordinary recapture (e.g., short-life depreciable improvements with accelerated MACRS).

For unrecaptured §1250 gain on the boot-attributable portion, character flows through Line 22 and is reported on Schedule D's unrecaptured §1250 gain worksheet. See [`depreciation-recapture.md`](./references/depreciation-recapture.md).

### Line 22 — Recognized gain

Add Line 21 + (Line 20 − Line 21 if positive, else 0).

In plain terms: total gain you must recognize this year = ordinary recapture + boot-attributable capital gain.

This number flows to:
- Form 4797 if the relinquished property was held for productive use in a trade or business (the typical §1031 case — rentals)
- Schedule D + Form 8949 if the property was held for investment only and not in a trade or business

### Line 23 — Recognized gain

Equal to Line 22. (Line 23 is a checkpoint that re-states recognized gain for Line 25's basis calculation.)

### Line 24 — Deferred gain or (loss)

Line 19 − Line 23. The portion of realized gain (or loss) pushed into the basis of replacement and deferred.

### Line 25 — Basis of like-kind property received

Line 18 + Line 23 − Line 15.

Algebraic equivalent: Line 25 = FMV of replacement − Deferred gain (or + Deferred loss).

This is the **carryover basis** that reduces the user's basis in the replacement below its FMV. When the replacement is later sold, the deferred gain is recognized.

---

## Part IV — Federal Conflict-of-Interest Exchanges

For federal officers required to divest under a Certificate of Divestiture from the Office of Government Ethics. Out of scope for typical filers. Do not engage unless the user explicitly invokes this category.

---

## Worked numerical example (full deferral, no boot)

User exchanges Property A for Property B via QI:

- Property A adjusted basis: $200,000
- Property A FMV at exchange: $500,000
- Property B FMV at exchange: $500,000
- No boot, no debt assumed/relieved, exchange expenses $10,000 paid out of escrow

| Line | Computation | Value |
|------|-------------|-------|
| 12 | Other property given up | 0 |
| 13 | Basis of other property | 0 |
| 14 | (12 − 13) | 0 |
| 15 | Cash + other received + net debt relief − expenses | 0 − 10,000 = −10,000 → enter 0 (not below 0) |
| 16 | FMV of like-kind received | 500,000 |
| 17 | (15 + 16) | 500,000 |
| 18 | Basis given up + cash paid + net debt assumed + expenses | 200,000 + 0 + 0 + 10,000 = 210,000 |
| 19 | Realized gain (17 − 18) | 290,000 |
| 20 | Smaller of (15, 19), ≥ 0 | 0 |
| 21 | Ordinary recapture | 0 |
| 22 | Recognized gain | 0 |
| 23 | (= 22) | 0 |
| 24 | Deferred gain (19 − 23) | 290,000 |
| 25 | Basis of replacement (18 + 23 − 15) | 210,000 |

User pays $0 federal tax this year; basis in Property B is $210,000 (carrying $290,000 deferred gain). On a future sale of Property B at $600,000, the user would recognize $390,000 gain ($290k deferred + $100k new appreciation).

---

## Worked numerical example (with cash boot)

User exchanges Property A for Property B via QI; user takes $50,000 cash out at closing:

- Property A adjusted basis: $200,000
- Property A FMV at exchange: $500,000
- Property B FMV at exchange: $450,000
- Cash boot received: $50,000
- Exchange expenses: $5,000 (paid from boot)

| Line | Computation | Value |
|------|-------------|-------|
| 15 | Boot received: 50,000 cash − 5,000 exchange expenses | 45,000 |
| 16 | FMV of like-kind received | 450,000 |
| 17 | (15 + 16) | 495,000 |
| 18 | Basis given up + 0 + 0 | 200,000 |
| 19 | Realized gain (17 − 18) | 295,000 |
| 20 | Smaller of (15=45,000; 19=295,000), ≥ 0 | 45,000 |
| 21 | Ordinary recapture | 0 (assume straight-line §1250) |
| 22 | Recognized gain | 45,000 |
| 23 | (= 22) | 45,000 |
| 24 | Deferred gain (19 − 23) | 250,000 |
| 25 | Basis of replacement (18 + 23 − 15) | 200,000 + 45,000 − 45,000 = 200,000 |

User recognizes $45,000 capital gain (long-term if held > 1 year, possibly with 25% unrecaptured §1250 rate); basis in Property B is $200,000 (carrying $250,000 deferred gain).

See [`examples/delayed-exchange-with-boot.md`](../examples/delayed-exchange-with-boot.md) for full persona walkthrough.
