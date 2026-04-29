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
- Gain is recognized on the original exchange in the year of the disqualifying disposition
- Reported on Form 8824 of the year of disposition (with a note explaining the recognition)

### "Date of last transfer"

In a delayed exchange, this is the later of Line 4 (relinquished transfer) or Line 6 (replacement received). The 2-year clock starts on whichever is later.

### Three exceptions (IRC §1031(f)(2))

1. **Death of either party** — natural causes during the 2-year window do not trigger recognition. Estate continues to hold the inherited property with stepped-up basis.
2. **Compulsory or involuntary conversion** — if the received property is condemned, destroyed, or otherwise involuntarily converted, §1033 governs the new property and §1031 deferral is preserved.
3. **No tax-avoidance purpose** — if the user can establish to the IRS's satisfaction that neither the original exchange nor the disposition had as one of its principal purposes the avoidance of federal income tax. This is a high evidentiary bar; relies on documentation, business reasons, and timing.

---

## Form 8824 reporting requirements

When Line 7 = Yes (related-party exchange), Part II becomes mandatory:

- **Line 8** — Name, address, and SSN/EIN/ITIN of related party
- **Line 9** — Relationship to user
- **Line 10** — Yes/No: did either party dispose of the received property during this tax year?
- **Line 11** — If Line 10 = Yes, check the applicable exception (death, involuntary conversion, no tax-avoidance) or recognize gain currently

### Annual reporting requirement

The IRS expects Form 8824 to be filed in the year of original exchange AND, if appropriate, in any year of subsequent disposition during the 2-year window.

If a subsequent disposition triggers recognition under §1031(f), the user files an updated Form 8824 in the year of disposition with:
- Same exchange details (Lines 1-9 from prior year)
- Line 10 = Yes
- Line 11 = exception or recognized gain

---

## Special situations

### Indirect related-party exchange via QI

IRS Letter Ruling 9748006 and subsequent guidance: if the user uses a QI to exchange with what appears to be an unrelated party, but the QI then arranges for the replacement to come from a related party, the 2-year rule still applies (substance-over-form).

This includes "swap-and-drop" structures and similar techniques. The IRS scrutinizes them.

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
- Form 8824 filed for 2025: Line 7 = Yes, Part II completed, Line 10 = No
- No further Form 8824 required (assuming both continue holding past 2027)

### Example B: Brother-to-brother, one disposes within 2 years

- Same setup, but Brother A sells the Tucson property in October 2026 (≈ 19 months after exchange)
- Brother A's 2026 return: Form 8824 with Line 7 = Yes, Line 10 = Yes, Line 11 = no exception
- Brother A recognizes the entire deferred gain from 2025 in 2026 (in addition to any new gain from the 2026 sale)
- Brother B's deferral may also be unwound depending on the structure — file Form 8824 to recognize for his side as well, if applicable

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
- [ ] If a disposition occurred within 2 years, Line 10 = Yes and gain is recognized (or one of the three exceptions checked on Line 11)
- [ ] Constructive ownership applied per IRC §267(c) — family ownership is aggregated

---

## Practical recommendation for the agent

If the exchange is between related parties, surface the 2-year obligation prominently in the deliverable's "Next steps" section. Phrase it as:

> ⚠ Related-party exchange flag: §1031(f) requires both you and [related party] to hold the received properties for at least 2 years (until [date]). Any disposition before that date — by either party — generally un-does the deferral and triggers gain recognition on the original exchange in the year of disposition. Exceptions: death, involuntary conversion, or non-tax-avoidance disposition (the third requires IRS approval).

The user should set a calendar reminder for the 2-year date.

---

## Sources

- IRC §1031(f) — related-party 2-year rule
- IRC §267(b) — definition of related parties
- IRC §707(b)(1) — partnership related parties
- IRC §267(c) — constructive ownership
- IRC §1031(f)(2) — exceptions (death, involuntary conversion, non-tax-avoidance)
- Form 8824 instructions, Part II
- IRS Letter Ruling 9748006 — indirect related-party exchanges
- Pub. 544 — narrative explanation
