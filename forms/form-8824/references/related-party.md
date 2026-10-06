# Form 8824 Related-Party Exchanges

IRC §1031(f) imposes a **2-year holding rule** on like-kind exchanges between related parties. Both the user and the related party must hold their respective received properties for 2 years after the last transfer in the exchange. Disposition by either party within 2 years generally un-does the §1031 deferral.

This rule was added to Congress's response to perceived abuse: related parties shifting basis to extract gain at lower tax cost.

---

## Who is "related"

Per IRC §1031(f)(3) → IRC §267(b) and §707(b)(1):

### Family

- Spouse
- Ancestors: parents, grandparents, great-grandparents
- Lineal descendants: children, grandchildren, great-grandchildren (includes legally adopted)
- Siblings, including half-siblings (NOT step-siblings, in-laws, or cousins)

### Entities

- A corporation in which the user (and family, with constructive ownership rules) owns **more than 50%** of the stock by value
- A partnership in which the user owns more than 50% of capital or profits interests
- An estate of which the user is the executor or beneficiary
- A trust where the user (or family) is grantor or beneficiary in certain configurations
- Two corporations in the same controlled group (with reciprocal ownership rules)

### Constructive ownership

Stock or partnership interests owned by family members are attributed to the user under §267(c). So a corporation owned 30% by the user, 25% by the user's spouse, and 5% by their child is treated as 60% owned by the user — over the 50% threshold, hence related.

### NOT related

- In-laws (other than spouse)
- Step-relatives (most contexts)
- First cousins, aunts/uncles, nieces/nephews
- Friends, business associates, unrelated tenants in common
- Partners in a partnership that the user owns ≤50% of

When in doubt, ask the user to describe the relationship and apply §267(b) carefully.

---

## The 2-year rule

If the user exchanges property with a related party AND either party disposes of the received property within **2 years** after the date of the last transfer in the exchange:

- The original §1031 deferral is **un-done**
- Gain or loss on the original exchange is taken into account as of the date of the disqualifying disposition (IRC §1031(f)(1))
- Reported on Form 8824 for the year of disposition: Part II with Line 9 or Line 10 = Yes, then Part III, reporting the deferred gain or (loss) from Line 24 as if the exchange had been a sale
- Either party's disposition triggers recognition for the user: Line 9 covers the related party's disposition, Line 10 the user's own

### "Date of last transfer"

In a delayed exchange, this is the later of Line 4 (relinquished transfer) or Line 6 (replacement received). The 2-year clock starts on whichever is later.

### Three exceptions (IRC §1031(f)(2))

1. **Death of either party** (Line 11a) — a disposition after the death of either related party does not trigger recognition.
2. **Compulsory or involuntary conversion** (Line 11b) — a disposition by involuntary conversion (within §1033) does not count, but only if the exchange occurred before the threat or imminence of the conversion.
3. **No tax-avoidance purpose** (Line 11c) — if the user can establish to the IRS's satisfaction that neither the original exchange nor the disposition had as one of its principal purposes the avoidance of federal income tax. Attach an explanation. The instructions say tax avoidance generally won't be seen as a principal purpose for a disposition in a nonrecognition transaction, an exchange where the related parties get no tax advantage from shifting basis, or an exchange of undivided interests that leaves each party holding a whole property or a larger undivided interest.

The 2-year period is suspended for any period in which the holder's risk of loss is substantially diminished (IRC §1031(g); 2025 instructions, "Tolling of holding period").

---

## Form 8824 reporting requirements

When Line 7 = Yes (related-party exchange, directly or indirectly), Part II becomes mandatory (2025 Form 8824):

- **Line 8** — Name of related party, relationship to you, related party's identifying number, and address
- **Line 9** — Yes/No: during this tax year (and before 2 years after the last transfer), did the related party sell or dispose of any part of the like-kind property received from you (or an intermediary)?
- **Line 10** — Yes/No: during this tax year (and before 2 years after the last transfer), did you sell or dispose of any part of the like-kind property you received?
- **Line 11** — If Line 9 or 10 = Yes, check the applicable exception (11a death, 11b involuntary conversion, 11c no tax-avoidance purpose with explanation) or complete Part III and report the deferred gain now

### Annual reporting requirement

File Form 8824 for the year of the exchange AND for each of the 2 years following the year of a related party exchange (2025 instructions, "When To File").

In each following year:
- Complete Parts I and II (same exchange details on Lines 1-8)
- If Lines 9 and 10 are both "No", stop; Part III is not required
- If Line 9 or 10 is "Yes" and a Line 11 exception applies, check it, attach any required explanation, and stop
- If Line 9 or 10 is "Yes" and no exception applies, complete Part III and report the Line 24 deferred gain or (loss) on this year's return

---

## Special situations

### Indirect related-party exchange via QI

An exchange made with a related party through an intermediary (a QI or EAT), or by a disregarded entity owned by the user or a related party, is a related-party exchange (2025 instructions, Line 7).

An exchange structured to avoid the related-party rules is not a like-kind exchange (IRC §1031(f)(4)). The common case: the user transfers the relinquished property to a QI and receives replacement property that a related party sold into the exchange for cash or other non-like-kind property (Rev. Rul. 2002-83). Unless a Line 11 exception applies, do not file Form 8824 for it; report the disposition of the property given up as a sale (2025 Form 8824, Note under line 7).

### Partnerships and S-corps as related parties

If the user owns >50% of a partnership and exchanges with that partnership, both the partnership and the user are subject to the 2-year rule. The same applies to controlled S-corps and C-corps.

A common structural error: an LLC owned 50/50 by spouses exchanges with one of the spouses individually. The spouse-to-spouse relationship plus the entity's ownership both trigger related-party status.

### Sales between exchanges (basis-shifting concern)

The classic abuse §1031(f) was designed to stop:
1. Related Party A owns Property X (low basis, high FMV)
2. Related Party B owns Property Y (high basis, equal FMV)
3. They exchange under §1031
4. Party A immediately sells Property Y at FMV — recognizing minimal gain due to high basis
5. Party B holds Property X with low basis and high FMV — but maybe never sells

Net effect: family unit extracted cash with little tax. §1031(f) prevents this by undoing the exchange when disposition happens within 2 years.

---

## Worked examples

### Example A: Brother-to-brother exchange, both hold > 2 years

- Brother A owns rental property in Phoenix; Brother B owns rental property in Tucson
- They exchange via QI in March 2025
- Neither disposes within 2 years (i.e., by March 2027)
- Form 8824 filed for 2025: Line 7 = Yes, Part II completed, Lines 9 and 10 = No, Part III completed
- Form 8824 filed again for 2026 and 2027: Parts I and II only, Lines 9 and 10 = No, stop

### Example B: Brother-to-brother, one disposes within 2 years

- Same setup, but Brother A sells the Tucson property in October 2026 (≈ 19 months after exchange)
- Brother A's 2026 return: Form 8824 with Line 7 = Yes, Line 9 = No, Line 10 = Yes, no Line 11 exception; Part III reports his Line 24 deferred gain from 2025 in 2026 (in addition to any new gain from the 2026 sale)
- Brother B's 2026 return: Form 8824 with Line 9 = Yes (the related party disposed), no exception; Part III reports his own deferred gain in 2026 (IRC §1031(f)(1)(C)(i))

### Example C: Death exception

- Father exchanges with son in 2025; father dies in 2026
- Son inherits father's interest (or vice versa); §1031(f)(2)(A) exception applies
- No recognition triggered by the death

### Example D: LLC partner exchange

- User owns 60% of XYZ LLC; LLC and user individually exchange properties
- §1031(f) applies (related entity)
- Both must hold for 2 years post-exchange

---

## Validation

- [ ] If Line 7 = Yes, Part II Lines 8-11 completed in full
- [ ] Related party's SSN/EIN provided (the IRS uses this to track the other side)
- [ ] Relationship correctly characterized (family, controlled entity, partnership, etc.)
- [ ] If user is filing within 2 years of the original exchange, agent reminds user that any disposition before the 2-year mark un-does the deferral
- [ ] Form 8824 is calendared for each of the 2 years after the exchange year
- [ ] If a disposition occurred within 2 years, Line 9 or Line 10 = Yes and the Line 24 deferred gain is reported (or one of the three exceptions checked on Line 11)
- [ ] Constructive ownership applied per IRC §267(c) — family ownership is aggregated

---

## Practical recommendation for the agent

If the exchange is between related parties, surface the 2-year obligation prominently in the deliverable's "Next steps" section. Phrase it as:

> ⚠ Related-party exchange flag: §1031(f) requires both you and [related party] to hold the received properties for at least 2 years (until [date]). Any disposition before that date — by either party — generally un-does the deferral and triggers gain recognition on the original exchange in the year of disposition. Exceptions: death, involuntary conversion, or a disposition you can show had no tax-avoidance purpose (attach an explanation; the IRS decides). Form 8824 is also due with your return for each of the next 2 years.

The user should set a calendar reminder for the 2-year date.

---

## Sources

- IRC §1031(f) — related-party 2-year rule
- IRC §267(b) — definition of related parties
- IRC §707(b)(1) — partnership related parties
- IRC §267(c) — constructive ownership
- IRC §1031(f)(2) — exceptions (death, involuntary conversion, non-tax-avoidance)
- IRC §1031(f)(4) — transactions structured to avoid the rule; IRC §1031(g) — tolling
- 2025 Instructions for Form 8824, "When To File", Line 7, Lines 11a-11c
- Rev. Rul. 2002-83 — related party sells replacement property into the exchange through a QI
- Pub. 544 — narrative explanation
