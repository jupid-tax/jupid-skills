# Form 8824 Common Mistakes

The 10 most common audit-trip mistakes on Form 8824, with citations and fixes.

---

## 1. Treating a vehicle or equipment exchange as §1031

**Mistake**: User trades a business truck for a newer truck and reports it on Form 8824.

**Why it's wrong**: Post-TCJA (exchanges completed after Dec 31, 2017), IRC §1031 applies **only to real property** (TCJA §13303, codified at IRC §1031(a)(1)). Vehicles, equipment, livestock, art, machinery — none qualify.

**Fix**: Recognize the gain (or loss, if applicable) on Form 4797 normally. Trade-ins are still allowed under §1245 / §1250 dispositions; they just don't get §1031 deferral. The new equipment's basis is its cost (cash + trade-in value if any).

**Citation**: IRC §1031(a)(1) (post-TCJA); TCJA §13303 (Public Law 115-97).

---

## 2. No Qualified Intermediary in a delayed exchange

**Mistake**: User sells rental property directly to a buyer, holds the proceeds in their personal account, then uses those proceeds to buy a new rental within 180 days. Reports it on Form 8824.

**Why it's wrong**: The user was in **constructive receipt** of the proceeds (Treas. Reg. §1.1031(k)-1(f)). Once the user touches the cash, the exchange fails — even if the timing of replacement acquisition is within 180 days.

**Fix**: A QI must be in place **before** the relinquished sale closes. The QI takes title to the proceeds; the user never has access. There is no retroactive cure.

If the exchange already failed, recognize the gain on Form 4797 / Schedule D.

**Citation**: Treas. Reg. §1.1031(k)-1(f); §1.1031(k)-1(g)(4) (qualified intermediary safe harbor).

---

## 3. Identifying replacement property to the user's own attorney

**Mistake**: User signs a written identification document, but delivers it only to their personal attorney instead of the QI.

**Why it's wrong**: Per Treas. Reg. §1.1031(k)-1(c), identification must be delivered to "a person involved in the exchange other than the taxpayer or a related party of the taxpayer." The user's own attorney representing only the user is treated as a related party of the user for these purposes.

**Fix**: Re-deliver to the QI before Day 45. If past Day 45, the exchange fails — recognize gain.

**Citation**: Treas. Reg. §1.1031(k)-1(c)(2) (designation of replacement property).

---

## 4. Counting business days instead of calendar days

**Mistake**: User assumes the 45-day clock excludes weekends and federal holidays.

**Why it's wrong**: IRC §1031(a)(3) refers to calendar days. Day 45 falling on a Saturday is still Day 45.

**Fix**: Always recompute deadlines in calendar days. If Day 45 is a Saturday, plan to identify by Friday. If the user already missed it because they thought it would push to Monday, the exchange fails.

**Citation**: IRC §1031(a)(3); Form 8824 instructions.

---

## 5. Late-year relinquished without filing extension

**Mistake**: User relinquishes property in November. They have 180 days to acquire replacement (until May), but their tax return is due April 15. They file the return on April 15 without extension, before completing the exchange. Then close on replacement in late April.

**Why it's wrong**: IRC §1031(a)(3)(B) caps the 180-day window at the **earlier** of 180 days or the return due date (with extensions). By filing without an extension, the user shortened their own window.

**Fix**: File Form 4868 (automatic 6-month extension) BEFORE April 15. This pushes the deadline to October 15, preserving the full 180 days. The user still pays any estimated tax owed by April 15.

**Citation**: IRC §1031(a)(3)(B); Form 4868 instructions.

---

## 6. Including primary residence as relinquished property

**Mistake**: User exchanges their primary residence for a rental property, claiming §1031.

**Why it's wrong**: Primary residences are personal-use property, not "held for productive use in a trade or business or for investment." They don't qualify under §1031.

The right framework for primary residence sales is **IRC §121** — up to $250,000 ($500,000 MFJ) of gain excluded if held and used as principal residence ≥2 of last 5 years. That's a separate rule with no Form 8824.

**Fix**: Use §121 if eligible. If gain exceeds the §121 exclusion, the excess is recognized on Schedule D. There is no §1031 path for personal residences.

Edge case: a former primary residence converted to rental and held as a rental for some period CAN later be §1031 exchanged if the rental use was substantive. Rev. Proc. 2008-16 provides a safe harbor (must be rented at FMV ≥14 days/yr for 2 years and personal use ≤14 days/yr or 10% of rental days, whichever is greater).

**Citation**: IRC §121; IRC §1031(a)(1) ("held for productive use"); Rev. Proc. 2008-16.

---

## 7. Vacation home that fails the rental safe harbor

**Mistake**: User exchanges a beach house they've used personally and rented occasionally, treating it as §1031-eligible because it had some rental income.

**Why it's wrong**: To qualify for §1031, the property must be "held for productive use in a trade or business or for investment." Personal use disqualifies. Rev. Proc. 2008-16 sets a safe harbor:

For both relinquished and replacement property, in each of the **two 12-month periods** before/after the exchange:
- Property must be rented at fair rental value to others for **at least 14 days**
- Personal use must not exceed **the greater of 14 days or 10% of the days the property was rented at FMV**

If the user fails the safe harbor, the IRS may still allow §1031 based on facts and circumstances, but the burden is on the user.

**Fix**: Have the user document rental days, FMV rent received, and personal use days for the prior and (if known) future 12-month periods. If safe harbor fails and facts/circumstances are weak, the exchange likely fails — recognize gain.

**Citation**: Rev. Proc. 2008-16.

---

## 8. Misidentifying mortgage boot direction

**Mistake**: User had $300k mortgage on relinquished and assumed $400k mortgage on replacement. They report $400k as mortgage boot received.

**Why it's wrong**: Mortgage boot received is the **net debt RELIEF**, not the gross debt assumed. Here:
- Debt relieved (relinquished): $300k
- Debt assumed (replacement): $400k
- Net relief: $300k − $400k = −$100k → **$0 mortgage boot received**

The user assumed more debt than they were relieved of, which is "boot paid" — it goes into Line 18 (give side), increasing basis of replacement.

**Fix**: Recompute Line 15 with the netting formula: max(0, debt relieved − debt assumed). If negative, the excess goes to Line 18.

**Citation**: Treas. Reg. §1.1031(b)-1; Form 8824 instructions, Line 15 worksheet.

---

## 9. Forgetting the 2-year holding rule in related-party exchanges

**Mistake**: User exchanges with a sibling, completes Form 8824 for the year of exchange, then 18 months later sells the received property — and doesn't realize this triggers gain recognition on the original §1031 exchange.

**Why it's wrong**: IRC §1031(f) requires both parties to hold for 2 years. Disposition by either party within 2 years undoes the deferral.

**Fix**: When the user files Form 8824 with Line 7 = Yes, the agent should:
1. Highlight the 2-year obligation in the deliverable's Next Steps
2. Recommend a calendar reminder for the 2-year date
3. Remind the user to file Form 8824 in any subsequent year showing a disposition (Line 10 = Yes)

In the year of disqualifying disposition: file an updated Form 8824 with the original exchange details (Lines 1-9), Line 10 = Yes, Line 11 reflecting any exception (or none → recognize), and report recognized gain on Form 4797 / Schedule D.

**Citation**: IRC §1031(f); Form 8824 instructions, Part II.

---

## 10. Using a "disqualified person" as Qualified Intermediary

**Mistake**: User's CPA, attorney, real estate broker, or family member acts as the QI for the exchange.

**Why it's wrong**: Treas. Reg. §1.1031(k)-1(k) lists disqualified persons:
- The user's agent (anyone who has acted as the user's employee, attorney, accountant, investment banker, broker, or real estate agent or broker within the 2 years before the exchange)
- A person who bears a relationship described in §267(b) or §707(b) to the user (related parties)

If a disqualified person serves as QI, the safe harbor is broken and the exchange fails (constructive receipt).

**Fix**: Use an independent professional QI from the start. Major QIs include national title-company affiliates (First American Exchange, Investors Title, IPX1031, etc.) and specialized boutique firms. Verify the QI is not a §267(b)/§707(b) related party AND has not provided services to the user in the prior 2 years.

If the exchange already used a disqualified person, the §1031 deferral fails — recognize gain.

**Citation**: Treas. Reg. §1.1031(k)-1(k); IRC §267(b), §707(b).

---

## How the agent should use this list

When producing a draft, the agent should:

1. Cross-check the user's facts against each common mistake
2. Surface any matches as warnings in the deliverable's "Validation summary" → Sanity warnings section
3. If a mistake invalidates the exchange (Numbers 1-7), **stop and recommend recognizing gain normally**, not filing Form 8824
4. If a mistake is recoverable (Numbers 8, 9), guide the user to the correct computation

The agent should not silently fix substantive errors. The user (or their CPA) needs to be aware of and consent to any change in characterization.

---

## Sources

- IRC §1031(a)(1) — held for productive use; real property only post-TCJA
- IRC §1031(a)(3) — 45-day / 180-day deadlines
- IRC §1031(b) — gain to extent of boot
- IRC §1031(f) — related-party 2-year rule
- IRC §121 — primary residence exclusion
- IRC §267(b), §707(b) — related parties
- Treas. Reg. §1.1031(k)-1 — qualified intermediary, identification, deferred-exchange rules
- Treas. Reg. §1.1031(b)-1 — boot rules
- TCJA §13303 (Public Law 115-97) — restricting §1031 to real property
- Rev. Proc. 2000-37 — reverse exchange safe harbor
- Rev. Proc. 2008-16 — vacation home safe harbor
- Form 8824 instructions, current revision
- Pub. 544 — Sales and Other Dispositions of Assets
