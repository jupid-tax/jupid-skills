# Form 8832 Line-by-Line Reference

Complete lookup for every field on Form 8832 (Rev. December 2013, current as of 2026-04-29). Use this when the agent needs to confirm what a line means or what the IRS expects.

The instructions for Form 8832 are **printed inside the form PDF** (pages 3-6). There is no separate i8832.pdf — the IRS combined form and instructions in 2007. When the agent needs the canonical instruction text, fetch <https://www.irs.gov/pub/irs-pdf/f8832.pdf> and read pages 3-6.

---

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name of eligible entity making election | Full legal name as filed with state of formation (or country, for foreign entities) | Match the EIN application Form SS-4 exactly |
| Employer Identification Number (EIN) | 9 digits, format XX-XXXXXXX | Required. If no EIN, obtain at <https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online> before filing |
| Number, street, and room or suite no. | Principal place of business | Where IRS mails CP277/CP278 |
| City, state, and ZIP code | Same as above | Foreign entities use country and foreign postal code |
| ☐ Check if address change | Box at top of form | Check only if address is different from prior IRS records (last return filed, EIN application) |

---

## Part I — Election Information

### Line 1 — Type of election

Check exactly one box:

- **(a) Initial classification by a newly-formed entity. Skip lines 2a and 2b.** — The entity has never made a classification election since formation. Default classification was in effect; this is the first deviation.
- **(b) Change in current classification.** — The entity has made a prior election OR is changing from default to elected, more than once. Lines 2a and 2b apply.

**Edge case**: a brand-new LLC that elects on day 1 of formation checks (a). If the LLC operated for 6 months on default classification and *then* elects, it still checks (a) — the default-to-first-election change is "initial classification" because the default is not an election.

### Line 2a — Has the entity filed an entity classification election within the last 60 months?

Yes / No.

The 60-month limitation in 26 CFR §301.7701-3(c)(1)(iv): once an eligible entity makes an election to change its classification, it generally cannot elect again for 60 months following the effective date of the prior election.

"Filed an election" means a Form 8832 was previously submitted and accepted. Default classification (without a prior 8832) does not count.

### Line 2b — If "Yes" to 2a, was the prior election an election by a newly-formed entity effective on the date of formation?

Yes / No.

If Yes, the 60-month rule does **not** block the current election — the prior "initial" election does not count as a "change" for purposes of §301.7701-3(c)(1)(iv).

If No, the 60-month rule blocks unless one of two exceptions applies:

- IRS waiver on showing of "more than 50% change in ownership" since the prior effective date
- The current change is being made within the same regulatory framework that originally permitted the prior election (rare; consult counsel)

If blocked, the entity must wait until 60 months have elapsed from the prior effective date before re-electing.

### Line 3 — Does the eligible entity have more than one owner?

Yes / No.

This determines which Box 6 options are available:

- **Yes (multi-owner)**: Box 6(a) association, Box 6(b) partnership, Box 6(d) foreign association, Box 6(e) foreign partnership available. Boxes 6(c) and 6(f) (disregarded) not available — disregarded requires single owner.
- **No (single owner)**: Box 6(a) association, Box 6(c) disregarded, Box 6(d) foreign association, Box 6(f) foreign disregarded available. Boxes 6(b) and 6(e) (partnership) not available — partnership requires multi-owner.

**Edge case**: spouses in a community-property state can be treated as a single owner (Rev. Proc. 2002-69) for a "qualified entity" they jointly own. This is single-owner for Form 8832 purposes — Box 6(c)/(f) is available.

### Line 4 — If the eligible entity is owned by one person, provide the following information

- Name of owner
- Identifying number of owner (SSN if individual, EIN if entity)

Required only if Line 3 = No.

### Line 5 — If the eligible entity is owned by one or more affiliated corporations that file a consolidated return, provide the name and EIN of the parent corporation

Used in consolidated-group structures where the eligible entity is a subsidiary. Most solo / SMB filers leave this blank.

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

Required only if Box 6(d), (e), or (f) is checked. Use the country name in English (e.g., "United Kingdom", "Germany", "Cayman Islands").

If the foreign entity is on the per-se corporation list in 26 CFR §301.7701-2(b)(8), Form 8832 cannot be filed — the entity is permanently classified as a corporation. See [`eligibility.md`](./eligibility.md) for the full list.

### Line 8 — Election is to be effective beginning (month, day, year)

The desired effective date. Constraints:

- Cannot be more than **75 days before** the date Form 8832 is filed (USPS postmark / PDS mark date)
- Cannot be more than **12 months after** the date Form 8832 is filed
- If left blank, the effective date defaults to the filing date

If the user wants an effective date more than 75 days back, complete Part II (Late Election Relief). Up to 3 years and 75 days back is permitted under Rev. Proc. 2009-41.

**Edge case**: if the desired effective date falls on the entity's formation date but Form 8832 is mailed more than 75 days later, the election is "late" and Part II is required even if the user assumed the formation-date effective date would carry through automatically.

### Line 9 — Name and title of contact person whom the IRS may call for more information / Contact person's telephone number

Single contact person. The IRS calls this person if a clarification is needed. Usually the filer or their tax pro. Phone number with area code.

### Line 10 — If the entity is electing to be classified differently than its current classification, also indicate whether the entity has been issued a determination letter relating to a request to change its classification

This is a checkbox / attachment field used **only** if relying on regulatory automatic relief under Reg §301.9100-1, NOT Rev. Proc. 2009-41 (which uses Part II).

§301.9100-1 relief is a different mechanism — it allows extensions of time to make regulatory elections in certain circumstances, generally requiring a private letter ruling. Most late-relief filings should use Part II / Rev. Proc. 2009-41 instead, which is automatic and free.

### Line 11 (Part I) — Consent Statement and Signatures

Each member/owner with an interest in the entity on the effective date must sign. Format per signer:

- Signature
- Date
- Printed name
- Title (if applicable)

Alternative: an officer, manager, or member who is authorized under the entity's operating agreement or state law to make the election on behalf of all owners may sign. If using this alternative, attach evidence of authority (operating agreement excerpt, board/manager resolution, citation to state statute).

The IRS prefers all-owner signatures because authority disputes can void the election. Default to collecting all signatures.

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

If any of these is false, the entity must seek a private letter ruling under Rev. Proc. 2025-1 (annually updated) — not Form 8832 Part II.

### Line 11 (Part II) — Explanation

Reasonable-cause statement. The IRS expects:

- Specific facts (not boilerplate)
- Why the election was intended at the requested effective date
- Why Form 8832 was not timely filed (illness, professional reliance, change in law, oversight on a known-but-niche rule)
- What the entity has done since discovering the issue
- Statement that no inconsistent returns have been filed (or commitment to amend)

Common reasonable-cause patterns the IRS has accepted:

- "Filer reasonably relied on tax professional [name] who advised that the election would be auto-filed but did not file. Filer discovered the omission on [date] when reviewing prior returns."
- "Filer was unaware of the entity classification election requirement at formation. Filer discovered the requirement upon engaging a CPA on [date]."
- "Owner died on [date] and successor was unaware of pending entity classification election. Successor filed promptly upon discovery on [date]."

Boilerplate that the IRS rejects: "We forgot." "It was an oversight." "The form was lost." Without specific facts, no reasonable cause.

### Line 12 (Part II) — Statement of consistent returns

Signed declaration under penalties of perjury that all returns filed for affected years are consistent with the requested classification, OR all inconsistent returns will be amended.

If inconsistent returns have been filed and the entity is unwilling to amend, Part II relief is not available — private letter ruling required.

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
- Cancellation of debt income if liabilities exceed basis
- Built-in gains tax (BIG) if subsequently electing S-corp under IRC §1374
- Loss of basis or holding-period attributes

Always recommend a CPA review the deemed-transaction consequences *before* mailing Form 8832. Once filed, the deemed transactions are baked in.

### EIN persistence

Filing Form 8832 does NOT require a new EIN. The entity keeps its existing EIN through the classification change. However:

- If electing C-corp and changing the entity's name as part of the strategy, file Form 8822-B (change of address / responsible party) to update IRS records
- If the deemed liquidation is treated as a complete liquidation followed by formation of a new entity for state-law purposes, the new entity may need a new EIN

### State conformity

State-level entity classification varies:

- **Conforming states** (most): the federal classification election flows through to state tax purposes
- **Non-conforming states**: separate state-level election may be required (e.g., New York, New Jersey, California for some elections)
- **Some states** require a copy of Form 8832 to be filed with the state taxing authority within a window after federal filing

This skill does not handle state filings. After Form 8832 is mailed, surface the state-conformity question to the user and recommend they confirm with their state's department of revenue.
