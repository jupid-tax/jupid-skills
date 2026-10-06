# Form 8832 Line-by-Line Reference

Complete lookup for every field on Form 8832 (Rev. December 2013, current as of 2026-10-06). Use this when the agent needs to confirm what a line means or what the IRS expects.

The instructions for Form 8832 are **printed inside the form PDF**. There is no separate i8832.pdf. In the current <https://www.irs.gov/pub/irs-pdf/f8832.pdf>, PDF page 1 is the IRS "New Mailing Address" update, the form itself is PDF pages 2-4 (form pages 1-3), and the instructions are PDF pages 5-8 (form pages 4-7).

---

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name of eligible entity making election | Full legal name as filed with state of formation (or country, for foreign entities) | Match the EIN application Form SS-4 exactly |
| Employer Identification Number (EIN) | 9 digits, format XX-XXXXXXX | Required. If no EIN, obtain at <https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online> before filing |
| Number, street, and room or suite no. | Principal place of business | Where IRS mails CP277/CP278 |
| City, state, and ZIP code | Same as above | Foreign entities use country and foreign postal code |
| ☐ Check if address change | Box at top of form | Check only if address is different from prior IRS records (last return filed, EIN application) |
| ☐ Late classification relief sought under Revenue Procedure 2009-41 | Box at top of form | Check when Part II is completed |
| ☐ Relief for a late change of entity classification election sought under Revenue Procedure 2010-32 | Box at top of form | Only for a qualified foreign entity whose owner count was wrong (Rev. Proc. 2010-32); see the "Foreign default rule" instructions |

EIN rules from the instructions: the entity must have received its EIN before filing ("Applied For" is not accepted; an election without an EIN is not accepted), and an entity that already has an EIN keeps it after the classification change.

---

## Part I — Election Information

### Line 1 — Type of election

Check exactly one box:

- **(a) Initial classification by a newly-formed entity. Skip lines 2a and 2b and go to line 3.** — A newly formed entity choosing a classification other than its default from the start.
- **(b) Change in current classification. Go to line 2a.** — The entity is changing its current classification, whether that classification came from a prior election or from the default rules (the instructions' "Who Must File" list includes an entity "electing to change its current classification (even if it is currently classified under the default rule)").

**Edge case**: a brand-new LLC that elects effective on its date of formation checks (a). If the LLC operated for 6 months on its default classification and *then* elects, it checks (b): the election changes its classification, triggers the §301.7701-3(g) deemed transactions, and starts the 60-month clock (Treas. Reg. §301.7701-3(c)(1)(iv); see Example 1 under §301.7701-3(f)(3), which treats an election by an entity that was a default partnership as a change). Exception: a foreign entity whose classification was not relevant (§301.7701-3(d)(1)) before the effective date checks (a) (IRS FAQs for Form 8832 and Foreign Eligible Entities, Q1).

### Line 2a — Has the eligible entity previously filed an entity election that had an effective date within the last 60 months?

Yes → go to line 2b. No → skip line 2b and go to line 3.

The 60-month limitation in 26 CFR §301.7701-3(c)(1)(iv): once an eligible entity makes an election to change its classification, it generally cannot change its classification by election again during the 60 months succeeding the effective date of that election.

Default classification (without a prior Form 8832) does not count. A deemed association election from a timely Form 2553 (§301.7701-3(c)(1)(v)(C)) is also an election; ask the user whether the entity ever had an S election.

### Line 2b — Was the eligible entity's prior election an initial classification election by a newly formed entity that was effective on the date of formation?

Yes → go to line 3. No → the form says "Stop here. You generally are not currently eligible to make the election."

If Yes, the 60-month rule does **not** block the current election — an election by a newly formed entity effective on its formation date "is not considered a change" for purposes of §301.7701-3(c)(1)(iv).

If No, the 60-month rule blocks. The only relief: the IRS may permit the change **by private letter ruling** if more than 50% of the ownership interests in the entity, as of the effective date of the new election, are owned by persons that did not own any interest on the filing date or the effective date of the prior election (§301.7701-3(c)(1)(iv); Form 8832 instructions for lines 2a and 2b). The ruling request goes to the IRS National Office under the current Rev. Proc. 20XX-1 (Rev. Proc. 2026-1 for 2026) with a user fee; it is not claimed on Form 8832.

If blocked, the entity must wait until 60 months have elapsed from the prior effective date before re-electing.

### Line 3 — Does the eligible entity have more than one owner?

Yes / No.

This determines which Box 6 options are available:

- **Yes (multi-owner)**: Box 6(a) association, Box 6(b) partnership, Box 6(d) foreign association, Box 6(e) foreign partnership available. Boxes 6(c) and 6(f) (disregarded) not available — disregarded requires single owner.
- **No (single owner)**: Box 6(a) association, Box 6(c) disregarded, Box 6(d) foreign association, Box 6(f) foreign disregarded available. Boxes 6(b) and 6(e) (partnership) not available — partnership requires multi-owner.

**Edge case**: for a "qualified entity" owned only by spouses as community property, Rev. Proc. 2002-69 §4 lets the spouses treat the entity as either a disregarded entity or a partnership by how they report; the IRS accepts either position, and a change in reporting position is treated as a conversion (§4.03). No Form 8832 is involved in that choice. Ask which position the spouses have been reporting before treating the entity as single-owner.

### Line 4 — If the eligible entity has only one owner, provide the following information

- 4a Name of owner
- 4b Identifying number of owner (SSN, ITIN, or EIN)

Required only if Line 3 = No. If the owner is itself a disregarded entity (or a chain of disregarded entities), enter the first entity up the chain that is not disregarded. If the owner is a foreign person with no U.S. identifying number, enter "none" on line 4b (Form 8832 instructions, Line 4).

### Line 5 — If the eligible entity is owned by one or more affiliated corporations that file a consolidated return, provide the name and EIN of the parent corporation

5a parent name, 5b parent EIN. Used in consolidated-group structures. Most solo / SMB filers leave this blank.

### Line 6 — Type of entity (check only ONE box)

| Box | Domestic / Foreign | Election | Available when |
|-----|---------------------|----------|----------------|
| (a) | Domestic | Association (taxed as C-corporation) | Always (single or multi-owner) |
| (b) | Domestic | Partnership | Multi-owner only |
| (c) | Domestic | Disregarded as separate from its owner | Single-owner only |
| (d) | Foreign | Association (taxed as C-corporation) | Always |
| (e) | Foreign | Partnership | Multi-owner only |
| (f) | Foreign | Disregarded as separate from its owner | Single-owner only |

"Domestic" means formed under US federal or state law. "Foreign" means formed under the law of any other country.

**No-op elections**: Box 6(b) for a multi-member LLC that is already a default partnership is a no-op; no Form 8832 needed unless changing from a prior election. Box 6(c) for a SMLLC that is already a default disregarded entity is also a no-op. Surface no-op elections to the user — they may have meant Box 6(a).

### Line 7 — If the entity is created or organized in a foreign jurisdiction, provide the foreign country of organization

Required whenever the entity is created or organized in a foreign jurisdiction (Box 6(d), (e), or (f)), even if it is also organized under domestic law. Use the country name in English (e.g., "United Kingdom", "Germany", "Cayman Islands").

If the foreign entity is on the per-se corporation list in 26 CFR §301.7701-2(b)(8), Form 8832 cannot be filed — the entity is permanently classified as a corporation. See [`eligibility.md`](./eligibility.md) for the full list.

### Line 8 — Election is to be effective beginning (month, day, year)

The desired effective date. Constraints:

- Cannot be more than **75 days before** the date Form 8832 is filed (USPS postmark / PDS mark date)
- Cannot be more than **12 months after** the date Form 8832 is filed
- If left blank, the effective date defaults to the filing date
- A date more than 75 days back is treated as 75 days before filing; a date more than 12 months forward is treated as 12 months after filing (Treas. Reg. §301.7701-3(c)(1)(iii))

If the user wants an effective date more than 75 days back, complete Part II (Late Election Relief). Up to 3 years and 75 days back is permitted under Rev. Proc. 2009-41.

**Edge case**: if the desired effective date falls on the entity's formation date but Form 8832 is mailed more than 75 days later, the election is "late" and Part II is required even if the user assumed the formation-date effective date would carry through automatically.

### Line 9 — Name and title of contact person whom the IRS may call for more information

Single contact person. The IRS calls this person if a clarification is needed. Usually the filer or their tax pro.

### Line 10 — Contact person's telephone number

Phone number with area code.

### Consent Statement and Signature(s) (unnumbered, below line 10)

Each member who is an owner at the time the election is filed must sign. If the effective date is before the filing date, each person who was an owner between the effective date and the filing date and is not an owner when it is filed must also sign (Treas. Reg. §301.7701-3(c)(2)). Format per signer:

- Signature
- Date
- Printed name
- Title (if applicable)

Alternative: an officer, manager, or member who is authorized under local law or the entity's organizational documents to make the election may sign; the signer represents that authority under penalties of perjury. The form does not require attaching evidence of authority; keep the operating agreement excerpt or resolution in the file.

Authority disputes can undermine the election, so default to collecting all owner signatures. If using a continuation sheet or separate consent statement, it must contain the same information as the form. Do not sign the copy attached to the tax return.

**Penalty of perjury declaration**: signers attest under penalties of perjury that the information is true, correct, and complete.

---

## Part II — Late Election Relief

Used to claim relief under Rev. Proc. 2009-41 when the desired effective date is more than 75 days before the filing date.

### Eligibility for Part II relief (Rev. Proc. 2009-41 § 4)

All four must be true:

1. The entity has failed to obtain its desired classification solely because Form 8832 was not timely filed
2. Either:
   - (a) The entity has not filed a federal tax or information return for the first year in which the election was intended because the due date has not passed, OR
   - (b) The entity has timely filed all required federal tax returns and information returns consistent with its requested classification for all the years the entity intended the requested classification to be in effect AND no inconsistent tax or information returns have been filed by or with respect to the entity during any of the taxable years
3. The entity has reasonable cause for the failure to timely file Form 8832
4. Three years and seventy-five days from the requested effective date of the eligible entity's classification election have not passed

For condition 2(b), a return filed within 6 months after its due date (excluding extensions) counts as timely, and for a change election "consistent" includes reporting the §301.7701-3(g) deemed transactions (Rev. Proc. 2009-41 §4.01(2)(b)). If the entity files no return, each affected person's returns must meet the same test.

If any of these is false, the entity must seek a private letter ruling under Rev. Proc. 2026-1 (annually updated) — not Form 8832 Part II.

Check the top-of-form box "Late classification relief sought under Revenue Procedure 2009-41". (Rev. Proc. 2009-41 §4.02 told filers to write "Filed Pursuant to Rev. Proc. 2009-41" at the top only until the form was revised; the Rev. 12-2013 form has the box, Part II, and the declaration.)

### Line 11 (Part II) — Explanation

Reasonable-cause statement. The IRS expects:

- Specific facts (not boilerplate)
- Why the election was intended at the requested effective date
- Why Form 8832 was not timely filed (illness, professional reliance, change in law, oversight on a known-but-niche rule)
- What the entity has done since discovering the issue
- Statement that no inconsistent returns have been filed

Common reasonable-cause patterns the IRS has accepted:

- "Filer reasonably relied on tax professional [name] who advised that the election would be auto-filed but did not file. Filer discovered the omission on [date] when reviewing prior returns."
- "Filer was unaware of the entity classification election requirement at formation. Filer discovered the requirement upon engaging a CPA on [date]."
- "Owner died on [date] and successor was unaware of pending entity classification election. Successor filed promptly upon discovery on [date]."

Boilerplate that the IRS rejects: "We forgot." "It was an oversight." "The form was lost." Without specific facts, no reasonable cause.

### Part II declaration and signatures (no line 12)

Part II has one numbered line (11). Below it is a pre-printed declaration, under penalties of perjury, that the signers have personal knowledge of the facts and that "the elements required for relief in Section 4.01 of Revenue Procedure 2009-41 have been satisfied." That declaration covers the consistent-returns condition. Part II is signed by an authorized representative of the entity and each affected person (Form 8832 instructions, Part II "Signatures").

If inconsistent returns have been filed, Part II relief is not available, even if the entity offers to amend — private letter ruling required (Rev. Proc. 2009-41 §§3.03, 4.04).

---

## What's NOT on Form 8832 but matters

### Deemed liquidation / contribution under §301.7701-3(g)

When an eligible entity changes classification, the IRS treats the transition as if the following deemed transactions occurred:

| From | To | Deemed transaction |
|------|----|--------------------|
| Disregarded | Association (C-corp) | Owner contributes assets to a newly-formed corporation in exchange for stock; §351 may apply |
| Partnership | Association (C-corp) | Partnership contributes assets to a newly-formed corporation in exchange for stock; partnership liquidates and distributes stock to partners |
| Association | Disregarded | Corporation distributes all assets and liabilities to its single shareholder in complete liquidation; §331/§332 may apply |
| Association | Partnership | Corporation distributes all assets and liabilities to its shareholders in complete liquidation; partners then contribute to a new partnership |

These deemed transactions can trigger:

- Recognized gain on appreciated assets (corp-to-pass-through transitions especially)
- §357(c) gain if liabilities deemed assumed exceed the basis of the deemed-contributed assets (disregarded or partnership → association)
- Built-in gains tax (BIG) if subsequently electing S-corp under IRC §1374
- Loss of basis or holding-period attributes

Always recommend a CPA review the deemed-transaction consequences *before* mailing Form 8832. Once filed, the deemed transactions are baked in.

### EIN persistence

Filing Form 8832 does NOT require a new EIN. The entity keeps its existing EIN through the classification change. However:

- If electing C-corp and changing the entity's name as part of the strategy, report the name change on the return (Form 1120, page 1, item E, box 3) or by a letter signed by an officer if the return is already filed ([IRS: Business name change](https://www.irs.gov/businesses/business-name-change)). Form 8822-B covers only address and responsible-party changes
- The deemed transactions under §301.7701-3(g) are federal tax fictions; they do not create a new state-law entity. Do not apply for a new EIN for an existing entity that already has one. A formerly disregarded entity that never had its own EIN must apply for one (Form SS-4) before filing, and must not use the owner's number (Form 8832 instructions, "Employer identification number")

### State conformity

State-level entity classification varies:

- **Conforming states** (most): the federal classification election flows through to state tax purposes
- **Non-conforming states**: separate state-level election may be required for some elections (e.g., New York, New Jersey). California follows the federal classification by statute (R&TC §23038(b)(2)(B)) but still applies its LLC annual tax and fee to a disregarded LLC
- **Some states** require a copy of Form 8832 to be filed with the state taxing authority within a window after federal filing

This skill does not handle state filings. After Form 8832 is mailed, surface the state-conformity question to the user and recommend they confirm with their state's department of revenue.
