# Form 8824 Line-by-Line Reference

Complete lookup for every line on Form 8824. Use this when the agent needs to confirm where a number belongs or what a line means.

Verified on 2026-10-06 against the 2025 Form 8824 (created 8/19/25) and the 2025 Instructions for Form 8824 (Dec 2, 2025). Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-8824 before use.

---

## Header

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name(s) shown on return | Filer's legal name | Match the 1040 / 1065 / 1120-S |
| (top) | Identifying number | SSN, EIN, or ITIN | Match the parent return |

Each like-kind exchange is reported separately. If the user made more than one exchange, the instructions allow either one Form 8824 per exchange or a summary Form 8824 (name and identifying number, "Summary" on line 1, total recognized gain on line 23, total basis of like-kind property received on line 25) with an attached statement giving all Form 8824 information for each exchange (2025 instructions, "Multiple exchanges").

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
- Must be sent to the person obligated to transfer the replacement property (even if that person is a disqualified person) or to any other person involved in the exchange other than the user or a disqualified person (typically the QI) (Treas. Reg. §1.1031(k)-1(c)(2))
- Must unambiguously describe the property (legal description, street address, or distinguishable name)
- If the replacement was received before the 45-day period ended, it is treated as identified; enter the receipt date on Line 5 (2025 instructions, Line 5 Note)

The "three-property", "200%", and "95%" identification rules govern how many properties can be identified. See [`timing-rules.md`](./timing-rules.md).

**If Line 5 minus Line 4 > 45 days, the exchange fails. Stop and recognize gain normally.**

### Line 6 — Date you actually received the like-kind property

The date title to the replacement property transferred to the user (or to the QI, who then conveyed to the user).

**Must be ≤ 180 days after Line 4 OR ≤ the due date of the user's tax return (including extensions) for the year of Line 4 — whichever is earlier.**

Practical note: for a calendar-year individual, a transfer after October 17, 2025 (Line 4) has a 180th day after April 15, 2026, so the unextended return due date cuts the period short unless the user files Form 4868. A transfer in late November gives a 180-day deadline in late May only if the return is extended. Always compute both and use the earlier.

### Line 7 — Was the exchange of property given up or received made with a related party?

Yes/No.

"Related party" per IRC §1031(f)(3) → IRC §267(b) and §707(b)(1):
- Family members: spouse, ancestors (parents, grandparents), lineal descendants (children, grandchildren), siblings (full or half-blood)
- Controlled entity: a corporation in which the user (and their family) owns more than 50% of the stock by value
- Partnership in which the user owns more than 50% of capital or profits
- Trusts where the user is grantor/beneficiary in certain configurations
- Other family-controlled or constructive-ownership relationships

Includes indirect exchanges: through an intermediary (QI or EAT), or by a disregarded entity (such as a single-member LLC) owned by the user or a related party (2025 instructions, Line 7).

If Yes → Part II is required. If No → go to Part III.

NOT related: in-laws (except spouse), step-relatives, friends, business partners (unless partnership ≥50%-owned), unrelated tenants in common.

---

## Part II — Related Party Exchange Information

File Part II in the exchange year and in each of the 2 following years (2025 instructions, "When To File").

### Line 8 — Name of related party, relationship to you, related party's identifying number, and address

Full legal name, relationship (e.g., "father", "wholly-owned LLC", "controlled corporation (75% ownership)"), SSN or EIN, and mailing address. The IRS uses this to track both sides of the exchange against the 2-year rule.

### Line 9 — During this tax year (and before 2 years after the last transfer), did the related party sell or dispose of any part of the like-kind property received from you (or an intermediary)?

Yes/No.

### Line 10 — During this tax year (and before 2 years after the last transfer), did you sell or dispose of any part of the like-kind property you received?

Yes/No.

Form instruction after Line 10: if both Lines 9 and 10 are "No" and this is the year of the exchange, go to Part III; if both are "No" and this is not the year of the exchange, stop. If either is "Yes", complete Part III and report the deferred gain or (loss) from Line 24 on this year's return unless a Line 11 exception applies. See [`related-party.md`](./related-party.md).

### Line 11 — Exceptions (check the applicable box)

Three exceptions to the 2-year rule (IRC §1031(f)(2)):
- 11a — The disposition was after the death of either of the related parties
- 11b — The disposition was an involuntary conversion, and the threat of conversion occurred after the exchange
- 11c — The user can establish to the satisfaction of the IRS that neither the exchange nor the disposition had tax avoidance as one of its principal purposes; attach an explanation

If one applies in a later year, check the box, attach any required explanation, and stop. If none applies and Line 9 or 10 is Yes, complete Part III and report the deferred gain on this year's return.

The 2-year period is suspended while the holder's risk of loss is substantially diminished (IRC §1031(g); 2025 instructions, "Tolling of holding period").

---

## Part III — Realized Gain or (Loss), Recognized Gain, and Basis of Like-Kind Property Received

### Line 12 — FMV of OTHER (non-like-kind) property given up

Complete Lines 12-14 only if the user gave up property that was not like-kind; otherwise go to Line 15. Examples:
- Stock or bonds bundled into the deal
- Vehicles or equipment thrown in
- Personal property (furniture, equipment) included with a building sale that wasn't separately allocated

Most §1031 exchanges have $0 here. Post-TCJA, any non-like-kind property given up is fully recognized — there's no shielding.

### Line 12a — Description of other property given up

Required on the form itself, including e-filed returns, since the 2024 revision (no separate attachment).

### Line 13 — Adjusted basis of OTHER property given up

The user's adjusted basis in the non-like-kind property given up. Original cost + improvements − depreciation taken.

### Line 14 — Gain or (loss) on OTHER property given up

Line 12 − Line 13. **Always recognized**, regardless of §1031 status of the rest of the deal. Report the gain or (loss) as if the exchange had been a sale (Schedule D or Form 4797 according to the character of the asset). If the property given up was used previously or partly as a home, see "Property Used as Home" in the instructions.

### Line 15 — Cash received, FMV of other property received, plus net liabilities assumed by other party

This is **boot received**. Components (2025 instructions, Lines 15 and 15a):
- Any cash paid to the user by the other party (including cash from the QI) → cash boot
- FMV of any non-like-kind property received → other boot
- Net liabilities assumed by the other party: the excess, if any, of liabilities (including mortgages) the other party assumed over the total of (a) liabilities the user assumed, (b) cash the user paid, and (c) FMV of other property the user gave up. If there is no excess, this component is $0.
- REDUCE the sum (but not below zero) by any exchange expenses the user incurred, whether paid from exchange funds or out of pocket. Exchange expenses are closing costs on the disposition (brokerage commissions, attorney fees, deed preparation fees) and on the acquisition; prorated taxes, rent prorations, security deposits, and repairs are not exchange expenses (Pub. 544, "Exchange expenses").

Liability rules: a recourse liability is assumed by the party that agreed to and is expected to pay it; a nonrecourse liability is generally assumed by the party receiving the property subject to it (2025 instructions, Line 15; Treas. Reg. §1.1031(d)-2).

Boot received triggers gain recognition up to the amount of realized gain (Line 19).

### Line 15a — Description of other property received

E.g., "cash" or "liabilities and cash". On the form itself since the 2024 revision.

### Line 16 — FMV of like-kind property you received

The fair market value of the replacement real property at the time of receipt.

### Line 17 — Add Lines 15 and 16

Total value received in the exchange.

### Line 18 — Adjusted basis of like-kind property you gave up, net amounts paid to other party, plus any exchange expenses not used on line 15

Components (2025 instructions, Line 18):
- Adjusted basis of relinquished real property (original cost + improvements − depreciation taken)
- PLUS the net amount paid to the other party: the excess, if any, of (a) liabilities the user assumed, (b) cash the user paid, and (c) FMV of other property the user gave up, over liabilities the other party assumed
- PLUS exchange expenses not used to reduce Line 15

This represents the "give" side — what the user contributed to the exchange.

### Line 19 — Realized gain or (loss)

Line 17 − Line 18.

- Positive → realized gain. §1031 will defer some/all.
- Negative → realized loss. §1031 disallows loss recognition; the loss is deferred into basis of replacement.
- If a §121 exclusion applies (property used as a main home), write "Section 121 exclusion" and the amount in the entry space (now available on e-filed forms too); do not reduce Line 19 (2025 What's New; "Property Used as Home").

### Line 20 — Smaller of Line 15 or Line 19, but not less than zero

Recognized gain attributable to boot received. If a §121 exclusion applies, use the "Property Used as Home" steps instead (Line 20 = smaller of Line 15 minus the exclusion, or Line 19).

- If Line 15 (boot) is $0, Line 20 is $0 (full deferral, no boot triggered gain).
- If Line 15 > Line 19 (boot exceeds realized gain — rare), Line 20 = Line 19 (recognize all realized gain).
- If Line 19 < 0 (realized loss), Line 20 = 0 (no loss recognized via boot).

### Line 21 — Ordinary income under recapture rules

Printed on the form: "Enter here and on Form 4797, line 16." Figure it per the 2025 instructions, Line 21:

- **§1245 real property** (property depreciated as §1245 property that is real property for §1031, e.g. from a cost segregation study): the smaller of (1) total depreciation and amortization allowed or allowable (up to the Line 19 gain), or (2) the Line 20 gain plus the FMV of non-§1245 like-kind property received (IRC §1245(b)(4)).
- **§1250 property**: the smaller of (1) the ordinary income from additional depreciation (depreciation in excess of straight-line) that a sale would have produced (Form 4797 instructions, line 26), or (2) the larger of the Line 20 gain or the excess of (1) over the FMV of §1250 property received (IRC §1250(d)(4)).
- **§1252, 1254, 1255 property**: similar to §1245 (Treas. Reg. §§1.1252-2(d), 1.1254-2(d); Temp. Reg. §16A.1255-2(c)).

Line 21 **can exceed Line 20**. In the instructions' example, Taylor's §1245 recapture is $50,000 against a $40,000 Line 20 gain, so Line 21 = $50,000 and Line 22 = $0.

For a building depreciated straight-line (27.5-year residential or 39-year nonresidential MACRS) with no §1245 components, Line 21 is $0. The unrecaptured §1250 gain (taxed at up to 25%) inside any Line 22 amount is not ordinary income; it is figured on the Schedule D Unrecaptured Section 1250 Gain Worksheet. See [`depreciation-recapture.md`](./depreciation-recapture.md).

If the installment method applies, see the Line 21 instructions (Form 6252 lines 25/36 and Form 4797 line 15).

### Line 22 — Subtract Line 21 from Line 20

If zero or less, enter -0-. If more than zero, enter here and on Schedule D or Form 4797, unless the installment method applies:
- Real property used in a trade or business, including rentals (and other noncapital assets) → Form 4797, line 5 (§1231 gain from like-kind exchanges) or line 16 (ordinary gain from like-kind exchanges, property held 1 year or less)
- Capital assets (e.g., land held for investment) → Schedule D, line 4 (short-term) or line 11 (long-term) as the Schedule D instructions direct; no Form 8949 entry
- Installment method → Form 6252 (IRC §453(f)(6))

Use the date of the exchange as the date for reporting the gain (2025 instructions, Line 22).

### Line 23 — Recognized gain

Line 21 + Line 22. This is the total gain recognized this year and feeds Line 24 and Line 25.

### Line 24 — Deferred gain or (loss)

Line 19 − Line 23. If Line 19 is a loss, enter the loss. The portion of realized gain (or loss) pushed into the basis of replacement and deferred. For related-party exchanges, a later disqualifying disposition makes this amount reportable in that later year (see Part II).

### Line 25 — Basis of like-kind property received

Line 18 + Line 23 − Line 15.

Algebraic equivalent: Line 25 = Line 16 (FMV of replacement) − Line 24 (deferred gain), or + a deferred loss.

This is the **carryover basis** that reduces the user's basis in the replacement below its FMV. When the replacement is later sold, the deferred gain is recognized. Basis in any non-like-kind property received is its FMV. If a §121 exclusion applies, follow "Property Used as Home" (add the exclusion to Line 25).

### Lines 25a, 25b, 25c — Allocation of Line 25

Complete whichever apply when the like-kind property received includes §1250 property, §1245/1252/1254/1255 property, or intangible property treated as real property (2025 instructions, "Lines 25a, 25b, and 25c"):
- 25a — part of Line 25 allocated to like-kind §1250 property received
- 25b — part allocated to like-kind §1245, 1252, 1254, and 1255 property received
- 25c — part allocated to like-kind intangible property received

The amounts must be proportionate to FMV. Instructions example: Finley receives a $220,000 building with $165,000 of §1250 property and $55,000 of §1245 property; Line 25 of $175,000 is split $131,250 (25a) and $43,750 (25b). When the replacement contains only §1250 property, the instructions' example puts the whole Line 25 on 25a. Since 2024 these lines are on the e-filed form (no attachment).

---

## Part IV — Deferral of Gain From Section 1043 Conflict-of-Interest Sales

Only for officers or employees of the federal executive branch or federal judicial officers (and certain spouses, minor or dependent children, and trustees described in §1043) who sell property under a certificate of divestiture from the Office of Government Ethics or the Judicial Conference. Use Part IV only if the cost of replacement property is more than the basis of the divested property and the user elects to defer. Do not engage unless the user explicitly invokes this category.

| Line | Text on the 2025 form |
|------|----------------------|
| 26 | Number from the upper right corner of the certificate of divestiture (do not attach the certificate) |
| 27 | Description of divested property |
| 28 | Description of replacement property |
| 29 | Date divested property was sold |
| 30 | Sales price of divested property (amount received minus selling expenses) |
| 31 | Basis of divested property |
| 32 | Realized gain (Line 30 − Line 31) |
| 33 | Cost of replacement property purchased within 60 days after date of sale |
| 34 | Line 30 − Line 33; if zero or less, enter -0- |
| 35 | Ordinary income under recapture rules (Form 4797 Part III used as a worksheet); also enter on Form 4797, line 10 |
| 36 | Line 34 − Line 35; if more than zero, enter on Schedule D or Form 4797 |
| 37 | Deferred gain: Line 32 − (Line 35 + Line 36) |
| 38 | Basis of replacement property: Line 33 − Line 37 |

---

## Worked numerical example (full deferral, no boot)

User exchanges Property A for Property B via QI:

- Property A adjusted basis: $200,000
- Property A FMV at exchange: $500,000
- Property B FMV at exchange: $500,000
- No boot, no debt assumed/relieved, exchange expenses $10,000 (paid by the user outside escrow, so the QI's full $500,000 buys Property B)

| Line | Computation | Value |
|------|-------------|-------|
| 12 | Other property given up | 0 |
| 13 | Basis of other property | 0 |
| 14 | (12 − 13) | 0 |
| 15 | Cash + other received + net debt relief − expenses | 0 − 10,000 = −10,000 → enter 0 (not below 0) |
| 16 | FMV of like-kind received | 500,000 |
| 17 | (15 + 16) | 500,000 |
| 18 | Basis given up + net amount paid + expenses not used on Line 15 | 200,000 + 0 + 10,000 = 210,000 |
| 19 | Realized gain (17 − 18) | 290,000 |
| 20 | Smaller of (15, 19), ≥ 0 | 0 |
| 21 | Ordinary recapture | 0 |
| 22 | max(20 − 21, 0) | 0 |
| 23 | Recognized gain (21 + 22) | 0 |
| 24 | Deferred gain (19 − 23) | 290,000 |
| 25 | Basis of replacement (18 + 23 − 15) | 210,000 |
| 25a | §1250 property received (all of Line 25 if Property B has no §1245 or intangible components) | 210,000 |

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
| 22 | max(20 − 21, 0) | 45,000 |
| 23 | Recognized gain (21 + 22) | 45,000 |
| 24 | Deferred gain (19 − 23) | 250,000 |
| 25 | Basis of replacement (18 + 23 − 15) | 200,000 + 45,000 − 45,000 = 200,000 |

User recognizes $45,000. For a rental held more than 1 year it goes on Form 4797, line 5 as §1231 gain, and the part covered by prior depreciation is unrecaptured §1250 gain taxed at up to 25%; for investment land it goes on Schedule D, line 11. Basis in Property B is $200,000 (carrying $250,000 deferred gain).

See [`examples/delayed-exchange-with-boot.md`](../examples/delayed-exchange-with-boot.md) for full persona walkthrough.
