# Form 2553 Line-by-Line Reference

Complete lookup for every item on Form 2553, Parts I-IV. Use this when the agent needs to confirm what goes in a specific field, what triggers an attachment, or what an unusual checkbox means.

**Revision:** built on 2026-10-06 from the text of Form 2553 (Rev. December 2017) and the Instructions for Form 2553 (Rev. December 2020), the current revisions. The form is not annual. Before use, check https://www.irs.gov/forms-pubs/about-form-2553 for a newer revision; a new revision can re-letter the items.

The form has 4 pages:

| Page | Contents |
|------|----------|
| 1 | Part I: name and address, items A-I, officer signature |
| 2 | Part I continued: shareholder consents, columns J-N (use extra copies of page 2 for more rows) |
| 3 | Part II: Selection of Fiscal Tax Year, items O-R |
| 4 | Part III: QSST election; Part IV: Late Corporate Classification Election Representations |

Service-center addresses and fax numbers are on **page 3 of the instructions**, and on https://www.irs.gov/filing/where-to-file-your-taxes-for-form-2553.

---

## Part I — Election Information (page 1)

### Name and address (no item letter)

| Field | What goes here | Source |
|-------|----------------|--------|
| Name | The corporation's (entity's) true name as stated in the charter or other legal document creating it | Instructions, "Name and Address" |
| C/O | If the mailing address is someone else's (for example a shareholder's), enter "C/O" and that person's name after the entity name | Same |
| Number, street, room or suite | Street address including suite or room number. Use a P.O. box only if the Post Office does not deliver to the street address | Same |
| City, state or province, country, ZIP | Mailing city, state, ZIP (country and foreign postal code if foreign) | Form text |

**Practical check (not an IRS rule):** pull the EIN assignment notice (CP575) or a Letter 147C and copy the name exactly as the IRS has it, including commas and "LLC" / "Inc.". A mismatch slows processing. Letter 147C can be requested from the Business & Specialty Tax Line, 800-829-4933.

### Item A — Employer identification number

| Field | What goes here | Notes |
|-------|----------------|-------|
| EIN | 9-digit EIN, XX-XXXXXXX | If the entity has no EIN it must apply (online at IRS.gov/EIN, or Form SS-4 by fax or mail). If the EIN has not been received by the time the election is due, enter "Applied For" and the date applied (Instructions, "Item A") |

### Item B — Date incorporated

The date the state accepted the articles of incorporation (corporation) or articles of organization / certificate of formation (LLC).

### Item C — State of incorporation

State (or, if applicable, country) under whose law the entity was formed. A foreign entity is not eligible (Who May Elect, test 1).

### Item D — Name or address change

Check "name" and/or "address" if the entity changed its name or address **after applying for the EIN shown in item A** (Instructions, "Name and Address"). A brand-new entity whose details match its EIN application leaves both blank.

### Item E — Effective date of election

**The single most consequential field on the form.** Enter the beginning date (month, day, year) of the tax year for which the election is to be effective.

| Situation | What to enter (Instructions, "Item E") |
|-----------|-----------------------------------------|
| First tax year in existence | The earliest of: the date the entity first had shareholders (owners), first had assets, or began doing business. This usually is not January 1 |
| Existing entity keeping its tax year | The beginning date of the first tax year for which the election is to be effective (for a calendar-year entity, January 1 of the election year) |
| Existing entity changing its tax year, wanting S status for the short year | The beginning date of the short tax year |
| Existing entity changing its tax year, not wanting S status for the short year | The beginning date of the tax year after the short year; file Form 1128 and write "Form 1128" on the dotted line to the left of item E |

Form 2553 generally must be filed no later than 2 months and 15 days after the date entered in item E. See [`timing-rules.md`](./timing-rules.md) for the date arithmetic and late relief.

Common mistake: entering January 1 of the current year on a form filed in October. The election is then late and needs Rev. Proc. 2013-30 relief (item I statement, and Part IV for an LLC relying on the deemed classification election). Confirm item E against the user's stated intent.

### Item F — Selected tax year

Check exactly **one**:

| Box | Form text | Part II? |
|-----|-----------|----------|
| (1) | Calendar year | No |
| (2) | Fiscal year ending (month and day) | Yes |
| (3) | 52-53-week year ending with reference to the month of December | No |
| (4) | 52-53-week year ending with reference to the month of ____ | Yes |

"If box (2) or (4) is checked, complete Part II" (form text). Most small entities check box (1).

### Item G — More than 100 shareholders

Check only if more than 100 shareholders are listed in column J and treating members of a family as one shareholder results in no more than 100 shareholders (Who May Elect, test 2; IRC §1361(c)(1)). Almost always blank.

### Item H — Contact

Name and title of the officer or legal representative whom the IRS may call for more information, and that person's telephone number. This is not a power of attorney; use Form 2848 for that.

### Item I — Late election declaration and explanation

Leave blank for a timely election. For a late election, the officer declares reasonable cause and, if the entity is an eligible entity also making a late classification election, that the Part IV representations are true. The space (or an attached statement) must explain why the election was not made on time **and** describe the diligent actions taken to correct the mistake once discovered (form text; Rev. Proc. 2013-30 §4.03(1)). An attached statement must carry the penalties-of-perjury declaration in Rev. Proc. 2013-30 §4.03(3) and be signed.

### Signature

| Field | What goes here | Notes |
|-------|----------------|-------|
| Signature of officer | Signed by the president, vice president, treasurer, assistant treasurer, chief accounting officer, or any other corporate officer (such as tax officer) authorized to sign | Instructions, "Signature". If Form 2553 isn't signed, it won't be considered timely filed |
| Title | Officer title; for an LLC, the member or manager title the operating agreement gives signing authority | |
| Date | Date signed | |

Use a handwritten signature. Form 2553 is not on the IRS list of forms that accept electronic or digital signatures (IRM 10.10.1, Exhibit 10.10.1-2, checked 2026-10-06).

---

## Part I continued — Shareholder consents (page 2, columns J-N)

Use additional copies of page 2 for more rows, or attach a continuation sheet / separate consent statement with the entity's name, address, and EIN and the information in columns J through N.

### Who must consent (Instructions, "Item E" and "Column K")

- Election filed **before** the item E date: only shareholders who own stock on the day the election is made.
- Election filed **on or after** the item E date (every late election): all shareholders and former shareholders who owned stock at any time from the item E date to the day the election is made. Rev. Proc. 2013-30 §5.01 states the same for late elections.

### Column J — Name and address of each shareholder or former shareholder required to consent

| Situation | Enter |
|-----------|-------|
| Individual | Full name and address |
| Stock held by a nominee, guardian, custodian, or agent | Name and address of the person for whom the stock is held |
| Shareholder is a disregarded single-member LLC | The owner's name and address (the owner must be an eligible shareholder) |

### Column K — Shareholder's consent statement (signature and date)

Each shareholder signs and dates here (or on a separate consent statement). The printed consent also declares, for a late election, that the shareholder reported income on all affected returns consistent with the S election (Rev. Proc. 2013-30 §5.02). Special rules (Instructions, "Column K"; Reg. §1.1362-6(b)(2)):

- Community property: if an individual and spouse have a community interest in the stock or its income, **both** consent.
- Each tenant in common, joint tenant, and tenant by the entirety consents.
- Minor: the minor, the legal representative, or a natural or adoptive parent if no legal representative has been appointed.
- Estate: the executor or administrator.
- ESBT: the trustee and, if a grantor trust, the deemed owner.
- QSST: the deemed owner of the trust.
- Other trust: the person treated as the shareholder under §1361(c)(2)(B).

A timely election missing a consent can be saved under Reg. §1.1362-6(b)(3)(iii) (reasonable cause, consents filed within the extended period); for a community-property spouse who was a shareholder only because of state law, see Rev. Proc. 2004-35.

Signatures must be handwritten (see Signature above). A power of attorney signing for a shareholder is outside this skill; refer to a CPA.

### Column L — Stock owned or percentage of ownership

Number of shares each shareholder owns on the date the election is filed, and the date(s) acquired. Enter -0- for former shareholders listed in column J. An entity without stock (an LLC) enters the percentage of ownership and date(s) acquired.

**Sanity check:** current holders should sum to 100% (or to total issued shares). If the operating agreement gives members economic rights that differ from these percentages (waterfalls, preferred returns), the one-class-of-stock rule is at risk; see [`eligibility.md`](./eligibility.md).

### Column M — Social security number or employer identification number

SSN of each individual in column J; EIN of each estate, qualified trust, or exempt organization. A resident alien without an SSN uses an ITIN. A nonresident alien is not an eligible shareholder (Who May Elect, test 4).

### Column N — Shareholder's tax year ends (month and day)

Usually 12/31 for individuals. If a shareholder is changing tax year, enter the new year and attach an explanation of the present year and the basis for the change.

---

## Part II — Selection of Fiscal Tax Year (page 3)

Complete only if item F box (2) or (4) is checked. "All corporations using this part must complete item O and item P, Q, or R" (form text).

### Item O — Status

| Box | Meaning |
|-----|---------|
| 1 | A new corporation adopting the tax year entered in item F |
| 2 | An existing corporation retaining the tax year entered in item F |
| 3 | An existing corporation changing to the tax year entered in item F |

### Item P — Automatic approval under Rev. Proc. 2006-46

| Box | Representation | Attachment |
|-----|----------------|------------|
| P1 Natural Business Year | The year qualifies as a natural business year (section 5.07 of Rev. Proc. 2006-46) | Statement of gross receipts for each month of the most recent 47 months. A corporation without 47 months of receipts cannot use P1 |
| P2 Ownership Tax Year | Shareholders holding more than half the shares on the first day of the year have the same tax year or are concurrently changing to it (section 5.08) | None listed |

P1/P2 are not available automatically to a corporation under examination, before an appeals office, or before a federal court without meeting section 7.03 of Rev. Proc. 2006-46.

### Item Q — Business purpose (prior approval, Rev. Proc. 2002-39)

| Box | Meaning |
|-----|---------|
| Q1 | Request the fiscal year based on business purpose; attach a statement of facts (and gross receipts if relying on a natural-business-year test: 47 months for the 25% test; short period plus 3 prior years for the annual business cycle or seasonal test). Answer Yes/No for a conference if the IRS proposes to disapprove |
| Q2 | Make a back-up §444 election if the business purpose request is not approved (Form 8716) |
| Q3 | Agree to adopt or change to a December 31 year if needed for the S election to be accepted |

Q1 user fee: $5,750 under Rev. Proc. 2026-1, Appendix A (A)(3)(a)(ii), reduced to $3,450 for gross income under $400,000 (A)(4)(a). The instructions still show $6,200 "subject to change by Rev. Proc. 2021-1 or its successor"; the 2026 revenue procedure controls. Do not pay with the form; the IRS sends a notice. Allow about 90 more days for acceptance when Q1 is checked.

### Item R — Section 444 election

| Box | Meaning |
|-----|---------|
| R1 | The corporation will make, if qualified, a §444 election for the item F year; complete Form 8716 and attach it or file it separately |
| R2 | Agree to adopt or change to a December 31 year if the corporation is ultimately not qualified for §444 |

If a back-up or R1 §444 election fails and the corporation files a calendar-year return, it writes "Section 444 Election Not Made" in the top left corner of the first calendar-year Form 1120-S (Instructions, "Boxes Q3 and R2"). A §444 year requires the §7519 required payment (Form 8752).

---

## Part III — Qualified Subchapter S Trust (QSST) Election Under Section 1361(d)(2) (page 4)

Use Part III only if stock was transferred to the trust on or before the date the corporation makes its S election; otherwise the QSST election is made and filed separately. Form 2553 can't be filed with only Part III completed. One copy of page 4 (or a separate statement with the same information) per QSST.

| Field | What goes here |
|-------|----------------|
| Income beneficiary's name and address | The current income beneficiary |
| Social security number | Beneficiary's SSN |
| Trust's name and address | Trust |
| Employer identification number | Trust's EIN |
| Date on which stock was transferred to the trust | MM/DD/YYYY |
| Signature | Income beneficiary, or legal representative / other qualified person making the election, with date; certifies the trust meets §1361(d)(3) |

The deemed owner of the QSST must also consent in column K. Late QSST elections: Rev. Proc. 2013-30.

---

## Part IV — Late Corporate Classification Election Representations (page 4)

Use **only** when an eligible entity (typically an LLC with no timely Form 8832) makes a late S election whose classification election was intended to be effective on the same date. A corporation (Inc./Corp.) filing late leaves Part IV blank and relies on item I plus the column K consents. Form text and Rev. Proc. 2013-30 §5.03:

1. The requesting entity is an eligible entity as defined in Regulations section 301.7701-3(a);
2. The requesting entity intended to be classified as a corporation as of the effective date of the S corporation status;
3. The requesting entity fails to qualify as a corporation solely because Form 8832 was not timely filed under Regulations section 301.7701-3(c)(1)(i), or Form 8832 was not deemed to have been filed under Regulations section 301.7701-3(c)(1)(v)(C);
4. The requesting entity fails to qualify as an S corporation on the effective date solely because the S corporation election was not timely filed pursuant to section 1362(b); and
5a. The requesting entity timely filed all required federal tax returns and information returns consistent with its requested classification as an S corporation for all of the years the entity intended to be an S corporation and no inconsistent tax or information returns have been filed by or with respect to the entity during any of the tax years, **or**
5b. The requesting entity has not filed a federal tax or information return for the first year in which the election was intended to be effective because the due date has not passed for that year's federal tax or information return.

If neither 5a nor 5b is true (for example, the owner already reported the intended S year on Schedule C, or the first-year Form 1120-S due date passed with no return), the Rev. Proc. 2013-30 route is not available as written. Stop and refer the user to a CPA.

### Late-election header

For any late election, write "FILED PURSUANT TO REV. PROC. 2013-30" in the top margin of page 1. If the form is attached to Form 1120-S, also write "INCLUDES LATE ELECTION(S) FILED PURSUANT TO REV. PROC. 2013-30" in the top margin of page 1 of the 1120-S (Instructions, "Relief for Late Elections").

### Reasonable-cause statement (item I or attachment)

The agent helps the user draft the facts; it does not invent them. Patterns that state cause and diligence:

> "The owners were unaware of the requirement to file Form 2553 within 2 months and 15 days of the intended effective date. On [date] their CPA told them of the requirement, and they prepared and filed this election on [date]. The entity has operated on the basis that it is an S corporation since [item E date]."

> "The entity's prior accountant agreed to file Form 2553 but did not do so before disengaging in [month]. The owner discovered this on [date] while reviewing tax records and filed this election immediately."

Not reasonable cause: "We wanted to wait and see how the year went before electing."

---

## Cross-references

- Eligibility (who can be a shareholder, one class of stock, ineligible corporation classes): [`eligibility.md`](./eligibility.md)
- Timing rules (deadline calculation, Rev. Proc. 2013-30, §444): [`timing-rules.md`](./timing-rules.md)
- Reasonable salary (the post-election compliance question): [`reasonable-salary.md`](./reasonable-salary.md)
- State follow-up after the federal election: [`state-conformity.md`](./state-conformity.md)
- Common mistakes that void elections: [`common-mistakes.md`](./common-mistakes.md)
- Filing channel (fax vs mail): [`../filing.md`](../filing.md)
