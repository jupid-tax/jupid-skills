# Form 2553 Line-by-Line Reference

Complete lookup for every box on Form 2553 Parts I-IV. Use this when the agent needs to confirm what goes in a specific field, what triggers an attachment, or what an unusual checkbox means.

The form is 4 pages. Page 1 holds Part I (entity info + most shareholder consents). Page 2 continues consents and contains Parts II-III. Page 3 is reserved for additional shareholders if needed. Page 4 of the **instructions** (not the form) contains the service-center addresses and fax numbers.

---

## Part I — Election Information

### Line A — Name of corporation (or other entity)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Exact legal name as registered with the state and as on IRS EIN records | Must match character-for-character — including commas, "Inc.", "LLC", "Corp." |

**Common pitfall**: an LLC files articles as "Smith Consulting, LLC" but applies for EIN as "Smith Consulting LLC" (no comma). The IRS uses whichever appeared first. Pull the EIN confirmation letter (147C) before completing this field. Mismatch is the #1 cause of CP262 rejection.

### Line B — Address

| Field | What goes here | Notes |
|-------|----------------|-------|
| Number, street, room/suite | Current mailing address | PO Box acceptable |
| City, state, ZIP | Current mailing city/state/ZIP | Foreign addresses: enter country in city field |

This becomes the IRS's address of record for the entity until Form 8822-B is filed to change it.

### Line C — Employer Identification Number (EIN)

| Field | What goes here | Notes |
|-------|----------------|-------|
| EIN | 9-digit IRS EIN, format XX-XXXXXXX | **Mandatory.** Form 2553 cannot be filed without an EIN. |

If the entity has no EIN, apply at https://www.irs.gov/EIN (online application, EIN issued immediately for U.S.-based responsible parties with valid SSN/ITIN). Foreign responsible parties must apply by Form SS-4 fax, which takes 4-6 weeks — plan accordingly.

### Line D — Date incorporated

| Field | What goes here | Notes |
|-------|----------------|-------|
| Date | Date the state accepted articles of incorporation (corp) or articles of organization (LLC) | The "date filed" stamp on the state filing receipt |

This is the entity's birth date. For LLCs, this is the date on the state's certificate of formation, not the date the operating agreement was signed.

### Line E — State of incorporation

| Field | What goes here | Notes |
|-------|----------------|-------|
| State | Two-letter postal abbreviation of the state where the entity was formed | e.g., "DE", "CA", "TX" |

For entities formed outside the U.S. but doing business in the U.S., enter the foreign country name. These are uncommon for S-corp elections — non-U.S. entities are usually ineligible.

### Line F — Election effective date

**The single most consequential field on the form.**

| Field | What goes here | Notes |
|-------|----------------|-------|
| Effective date | The first day of the tax year the entity wants S-corp treatment to start | Format: MM/DD/YYYY |

Rules:

- **Calendar-year filer continuing from prior year**: January 1 of intended year (e.g., 01/01/2026 to be S-corp for 2026)
- **New entity**: typically the date the entity began doing business OR the date of formation, whichever was later in the same tax year
- **New entity that wants S-corp from day 1**: the date the entity had shareholders / acquired assets / began doing business — whichever was earliest

This date triggers the 2-month-15-day deadline calculation. See [`timing-rules.md`](./timing-rules.md) for the full decision tree.

A common mistake: entering January 1 of the *current* year on a form being filed in October. That makes the form 8+ months late, requiring Part IV (Rev. Proc. 2013-30 relief). The agent should verify Line F is consistent with the user's stated intent.

### Line G — Name and address of person to be contacted for more information

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Officer, member, or paid preparer | Must be a real person — not "any officer" |
| Address | Where the IRS should send correspondence about this election | Often same as Line B |
| Telephone | Daytime phone | IRS may call to clarify questions |

This is *not* a power-of-attorney designation. For POA, file Form 2848 separately.

### Line H — If the entity is changing its name (with the IRS)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name change checkbox | Check only if the entity's name on Line A is different from the name on its prior IRS records | Most filers leave blank |

A new entity electing for the first time leaves this blank — there's no prior IRS name to change.

### Line I — Tax year

The entity's tax year selection. Check exactly **one**:

| Box | Meaning | When to use |
|-----|---------|-------------|
| (1) Calendar year | Jan 1 – Dec 31 | Default for ~99% of small entities; Part II not required |
| (2) Fiscal year ending | Last day of month other than December | Requires Part II |
| (3) 52-53 week year ending with reference to month [____] | A 52-53 week year referenced to a specific month | Rare; requires Part II |
| (4) Other | Specifies a tax year not above | Requires Part II + explanation |

For an S-corp, the IRS strongly prefers calendar year. Non-calendar elections require business-purpose justification or a §444 election (with required-payment buy-in). See [`timing-rules.md`](./timing-rules.md) for §444 mechanics.

### Line J — Officer signature, title, date

| Field | What goes here | Notes |
|-------|----------------|-------|
| Signature | Original signature of an officer (corp) or member/manager with authority (LLC) | Wet-ink or qualifying e-signature per Reg. §1.1362-6(b)(3) |
| Title | "President", "CEO", "Member", "Manager", "Sole Member" | Must be a real title with signing authority |
| Date | Date the officer signed | Must be on or before the filing date |

For single-member LLCs: the sole member signs as "Sole Member" or "Member". For multi-member LLCs: any member with authority per the operating agreement signs.

---

## Shareholder Consent Statement (page 1, bottom + page 2)

Each shareholder must complete one row. Up to 5 shareholders fit on page 1; additional shareholders go on page 2 or a continuation sheet.

### Column J — Name and address of each shareholder

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Full legal name | Match SSN records |
| Address | Current mailing address | Where IRS would mail correspondence |

For community-property states (AZ, CA, ID, LA, NV, NM, TX, WA, WI), the **non-owner spouse** of a married shareholder must also be listed and sign. Enter the spouse on a separate row with the same shares as 0 (or as their community-property half, depending on state interpretation) — but they sign Column K and provide SSN in Column N. Failure to obtain spouse signature is the #2 cause of voided elections.

### Column K — Signature

| Field | What goes here | Notes |
|-------|----------------|-------|
| Signature | Original signature of the shareholder | Or qualifying e-signature per Reg. §1.1362-6(b)(3); must be the actual shareholder, not a proxy |

Powers of attorney are not sufficient unless the POA explicitly authorizes signing tax-election documents. Default Form 2848 POAs do *not* cover this — the POA must be customized.

### Column L — Date

| Field | What goes here | Notes |
|-------|----------------|-------|
| Date signed | Date of shareholder signature | Must be on or before the filing date |

Shareholders can sign at different times. The latest signature date must still be on or before the form transmission date.

### Column M — Stock owned or percentage of ownership

| Field | What goes here | Notes |
|-------|----------------|-------|
| Number of shares (corp) OR % interest (LLC) | Numeric ownership at the effective date | Total across all shareholders must equal 100% (or total issued shares for a corp) |
| Dates acquired | When each shareholder acquired their stock/interest | MM/DD/YYYY for each block |

**Sanity check**: Column M sums must reconcile. For a 50/50 two-member LLC, both members enter "50%". If the operating agreement has economic terms that don't match pro-rata ownership (waterfalls, preferred returns), the entity violates the one-class-of-stock rule and is ineligible — see [`eligibility.md`](./eligibility.md).

### Column N — Social Security Number or Employer Identification Number

| Field | What goes here | Notes |
|-------|----------------|-------|
| SSN/ITIN/EIN | Individual: SSN or ITIN; Trust: EIN; Estate: EIN | No exceptions |

ITIN holders (resident aliens without SSN) are eligible shareholders provided they're U.S. tax residents. Non-resident aliens are *not* eligible — listing one voids the entire election.

---

## Part II — Selection of Fiscal Tax Year

Skip if Line I Box 1 (calendar year) is checked. Required if Box 2, 3, or 4.

### Box O (Box P in older revisions) — Selection rationale

Check exactly one:

| Box | Meaning | Documentation required |
|-----|---------|------------------------|
| Natural business year | ≥25% of gross receipts in the last 2 months for each of last 3 years | Schedule of receipts attached |
| Ownership tax year | Majority shareholders share a tax year | Statement of shareholder tax years |
| Business purpose | Documented non-tax business purpose | Detailed statement; user fee may apply |
| §444 election | "Required payment" tax year | Must also file Form 8716; required-payment computation |

The IRS denies most §444 elections for small filers because the tax-deferral benefit is captured by the required payment. Most small entities should default to calendar year and skip Part II entirely.

### Box Q — Year-end requested

| Field | What goes here | Notes |
|-------|----------------|-------|
| Month and day | Last day of the requested fiscal year | e.g., 06/30 for a year ending June 30 |

### Box R — Statement of business purpose (if Box 3)

If business-purpose is the basis, attach a separate statement explaining:
- The natural seasonality of the business
- Why a calendar year creates accounting hardship
- How the proposed year-end matches operational reality

### Box S — §444 information (if Box 4)

If §444, also file Form 8716 separately, and prepare to make the required payment annually.

---

## Part III — Qualified Subchapter S Trust (QSST) Election

Required only if a Qualified Subchapter S Trust is among the shareholders. Most LLCs and small corporations have no trust shareholders — skip this part.

### Box T — Income beneficiary

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Beneficiary's full legal name | Must be a single individual (no joint beneficiaries) |
| SSN | Beneficiary's SSN | |
| Address | Beneficiary's mailing address | |

### Box U — Trust information

| Field | What goes here | Notes |
|-------|----------------|-------|
| Trust name | Full legal name of the trust | |
| Trust EIN | Trust's EIN | Required |
| Date stock transferred to trust | When the S-corp stock was transferred into the trust | |

### Box V — Income beneficiary's QSST election signature

| Field | What goes here | Notes |
|-------|----------------|-------|
| Signature | Original signature of the income beneficiary (or legal representative) | The beneficiary, not the trustee, makes the QSST election |
| Date | Date of signature | |

---

## Part IV — Late Corporate Classification Election Representations

Required only if filing late under Rev. Proc. 2013-30. See [`timing-rules.md`](./timing-rules.md) for late-relief eligibility.

If using Part IV, also write **"FILED PURSUANT TO REV. PROC. 2013-30"** across the top of page 1.

### Box 1

> The corporation intended to be classified as an S corporation as of the effective date entered on Line E.

Always check this box if filing late and intending S-corp treatment.

### Box 2

> The corporation has reasonable cause for its failure to make the timely election.

Always check this box if claiming late relief. Attach a separate statement (2-4 sentences) explaining the reasonable cause. See [`timing-rules.md`](./timing-rules.md) for acceptable vs. unacceptable reasonable-cause language.

### Box 3

> The corporation and all of its shareholders have reported their income for the period since the effective date in a manner consistent with S corporation status.

This means: no shareholder filed Schedule C, Form 1065, or Form 1120 for the period since the intended effective date. If anyone did, those returns must be amended before late relief will be granted.

For a brand-new entity that has not yet filed any tax return, Box 3 is automatically satisfied — just check it.

### Reasonable-cause statement (attached separately)

The agent helps the user draft this. Acceptable patterns:

> "Entity owners were unaware of the requirement to file Form 2553 within 2 months and 15 days of the intended effective date. Upon learning of the requirement on [date], owners promptly engaged counsel and prepared this election. The entity has at all times intended to operate as an S-corporation."

> "The entity's prior accountant agreed to prepare and file Form 2553 but failed to do so before disengaging in [month]. The owner discovered the failure on [date] when reviewing tax records and is filing this election immediately upon discovery."

Unacceptable:

> "We wanted to wait and see how the year went before electing." (willful, not inadvertent)

> "We elected at our convenience." (no reasonable cause)

---

## Cross-references

- Eligibility (who can be a shareholder, one class of stock, ineligible corporation classes): [`eligibility.md`](./eligibility.md)
- Timing rules (deadline calculation, Rev. Proc. 2013-30, §444): [`timing-rules.md`](./timing-rules.md)
- Reasonable salary (the post-election compliance challenge): [`reasonable-salary.md`](./reasonable-salary.md)
- State-level S-corp election (separate state forms): [`state-conformity.md`](./state-conformity.md)
- Common mistakes that void elections: [`common-mistakes.md`](./common-mistakes.md)
- Filing channel (fax vs mail): [`../filing.md`](../filing.md)
