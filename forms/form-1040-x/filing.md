# Filing Form 1040-X (channel, mailing, payment, tracking)

How an agent takes a completed Form 1040-X draft from `SKILL.md` and gets it to the IRS. Form 1040-X can be e-filed through tax software for recent years; older years go on paper. The agent prepares the package and, only with explicit user consent at the moment of submission, helps submit it.

Sources: Instructions for Form 1040-X (Rev. December 2025), "Where To File", "Assembling Your Return", "Sign Your Return", "Tracking Your Amended Return"; irs.gov [Amended return frequently asked questions](https://www.irs.gov/filing/amended-return-frequently-asked-questions) (reviewed 02-Sep-2026); irs.gov [File an amended return](https://www.irs.gov/filing/file-an-amended-return) (reviewed 30-Sep-2026); irs.gov [Where's My Amended Return?](https://www.irs.gov/filing/wheres-my-amended-return) (reviewed 02-Sep-2026). Re-check these pages before each filing season; addresses and e-file scope change.

---

## Channel decision tree

```
Is the return being amended for the current tax period or one of the two prior tax periods?
(In calendar 2026: tax years 2025, 2024, 2023.)
  NO  → PAPER (Section 2). "Any amended ... returns older than the current or prior two tax
        periods cannot be amended electronically." (FAQ)
  YES → Was the original prior-year return filed ON PAPER during the CURRENT processing year?
        (Example from irs.gov: a 2023 return filed on paper in February 2025, amended in 2025.)
          YES → PAPER (Section 2). The FAQ: "the amended return must also be filed on paper."
          NO  → Has the user already had three amended returns accepted electronically for this year?
                  YES → PAPER (a fourth e-filed amendment is rejected; FAQ: "up to three").
                  NO  → Is the user's software able to e-file Form 1040-X for that year?
                          YES → E-FILE (Section 1)
                          NO  → another participating software, a preparer, or PAPER
Is the 1040-X a response to an IRS notice (for example CP2000 marked "CP2000")?
  → Follow the notice's reply channel and address (upload, fax, or mail), not the table below.
```

Forms 1040, 1040-SR, 1040-NR, and 1040-SS can be amended electronically within those limits (FAQ).

---

## Section 1 — E-file

### Pre-flight

The agent must have:

- The completed draft (all lines, Part II, Part I if dependents changed) and the complete corrected return for that year. The FAQ: an e-filed amended return "requires submission of all necessary forms and schedules as if it were the original submission, even if some forms have no adjustments", plus Form 1040-X.
- For a 1040-NR amendment e-filed: Form 1040-X completed in its entirety (the paper shortcut does not apply).
- The user's consent to submit.
- Signature data, collected only at submission: Self-Select PIN (five digits, not all zeros), date of birth, and the prior-year AGI from the originally filed prior-year return (not from an amended return or an IRS math-error correction) or the prior-year PIN; "$0" if no prior-year return was filed or it was only recently processed. Current-year IP PIN if one was issued (a missing IP PIN invalidates the signature and the return rejects).
- If a preparer transmits: a new Form 8879 signed for **each** e-filed amended return (FAQ; File an amended return page).
- Refund by direct deposit (tax year 2021 and later only): routing number, account number, account type, entered in the Form 1040-X Part III fields; account must be in the taxpayer's name. Form 8888 can split the deposit; amended-return refunds can't buy savings bonds.

### Flow (generic; software screens vary by vendor)

1. Open the filed return for that year in the software and choose the amend option (vendors label it differently). If the user changed software, re-create the original first so column A is right.
2. Enter only the changes; confirm the software's Form 1040-X columns A/B/C match the draft line for line. If any number differs, **stop**; one of the two is wrong.
3. Enter the Part II explanation from the draft.
4. Review the attached forms list against the draft's attachment list.
5. At submission, with explicit consent, enter signature data and transmit.
6. Save the submission ID and acceptance acknowledgment. An accepted transmission is the proof of filing; a saved PDF is not.

### Paying a balance with e-file

Authorize a direct debit with the e-filed 1040-X, or pay through IRS Direct Pay, EFTPS, debit/credit card, or digital wallet (Instructions, line 20; https://www.irs.gov/payments). If mailing a check for an e-filed amendment, use Form 1040-V and the address in the Form 1040-V instructions (FAQ).

---

## Section 2 — Paper

### Assemble (Instructions, "Assembling Your Return")

1. **Form 1040-X**, signed by hand (both spouses if joint). Digital or typed signatures are not valid on paper.
2. **Attached to the front of Form 1040-X**: copies of any W-2, W-2c, or Form 2439 supporting the changes; any W-2G or 1099-R supporting the changes, only if tax was withheld; any Form 1042-S, SSA-1042S, RRB-1042S, or 8288-A supporting the changes.
3. **Behind Form 1040-X**: the completed and updated Form 1040, 1040-SR, or 1040-NR with the changes (required since the December 2025 revision).
4. **Behind that return**: new or changed schedules and forms in "Attachment Sequence No." order (upper-right corner of each).
5. **Last**: supporting statements, in the same order as the forms they support.
6. **Back of Form 1040-X**: any Form 8805 supporting the changes.
7. **Enclose, don't attach** a check or money order if paying by check (Line 20).

Don't attach a copy of the original return, correspondence, or other items unless required. For amending a Form 1040-NR on paper: page 1 of 1040-X carries only name, address, and SSN/ITIN; Part I is skipped; the new or corrected return is marked "Amended" across the top and attached behind the 1040-X.

One Form 1040-X per year. When mailing several years, use separate envelopes ([Amending a return video script](https://www.irs.gov/newsroom/amending-a-return-youtube-video-text-script)).

### Where to mail (Instructions for Form 1040-X, Rev. December 2025)

| Situation | Address |
|---|---|
| Filing in response to an IRS notice | The address shown in the notice |
| Filing with Form 1040-NR or 1040-NR-EZ | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 |
| Live in Alabama, Arkansas, Florida, Georgia, Louisiana, Mississippi, Oklahoma, or Texas | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0052 |
| Live in Alaska, Arizona, California, Colorado, Hawaii, Idaho, Iowa, Kansas, Michigan, Montana, Nebraska, Nevada, New Mexico, North Dakota, Ohio, Oregon, South Dakota, Utah, Washington, or Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0052 |
| Live in Connecticut, Delaware, District of Columbia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Minnesota, Missouri, New Hampshire, New Jersey, New York, North Carolina, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, or Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0052 |
| Live in a foreign country or U.S. territory, use an APO or FPO address, file Form 2555 or 4563, or are a dual-status alien | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 (residents of American Samoa, Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Mariana Islands: see Pub. 570) |

Never hardcode these from memory; open the current instructions and match the user's current state of residence.

### Mailing

- Use USPS certified mail or an IRS-designated private delivery service to prove the mailing date ("timely mailing as timely filing"); the PDS list is at IRS.gov/PDS and PDS street addresses at IRS.gov/PDSStreetAddresses. A PDS can't deliver to a P.O. box.
- Keep a complete copy of everything mailed.
- A paper Form 1040-X refund comes as a paper check; direct deposit is available only on e-filed amendments.

---

## Section 3 — Interest, penalties, and payment

- **Don't** put interest or penalties on Form 1040-X; the IRS figures and bills them (Instructions, Purpose of Form; File an amended return page).
- If the original due date (without extensions) has not passed, filing the 1040-X or a corrected Form 1040 and paying by the due date avoids penalties and interest on the additional tax (Topic 308).
- After notice and demand, pay within 21 calendar days (10 business days if $100,000 or more) to avoid the late-payment penalty of 1/2 of 1% per month up to 25% (Instructions, Interest and Penalties).
- If the user can't pay in full, route to [`../form-9465/SKILL.md`](../form-9465/SKILL.md).

---

## Section 4 — Tracking

| Fact | Value | Source |
|---|---|---|
| When the amendment appears in Where's My Amended Return | Up to 3 weeks after submission (mailing or e-file) | Instructions, Tracking Your Amended Return; FAQ |
| Typical processing | 8 to 12 weeks; in some cases up to 16 weeks | Same |
| Tool | https://www.irs.gov/filing/wheres-my-amended-return | |
| Phone | 866-464-2050 (toll-free) | FAQ |
| Inputs | SSN (TIN), date of birth, ZIP or postal code | Instructions; WMAR page |
| Years covered | Current tax year and up to 3 prior years | WMAR page; FAQ |
| Statuses | Received (being processed); Adjusted (account adjusted: refund, balance due, or no change); Completed (processed; details by mail) | FAQ |
| Tool availability | 24 hours except Mondays 12–3 a.m. Eastern and occasional Sundays 1–7 a.m. Eastern | WMAR page |
| Not tracked by the tool | Business returns, carryback applications and claims, injured spouse claims, a Form 1040 marked as amended instead of a 1040-X, amendments with a foreign address, amendments handled by special units (Examination, Bankruptcy) | WMAR page; FAQ |
| When to call | Only if the tool says to | WMAR page |

Reasons processing runs past 12 weeks (FAQ): errors, incomplete or unsigned return, return sent back for information, Form 8379 attached, identity theft or fraud review, routing to a specialized area, bankruptcy clearance, revenue officer review, or an appeal or reconsideration.

The agent should set a reminder for about 3 weeks after submission, then check every few weeks; it should tell the user not to send a second copy.

---

## Security and consent rules

1. **Never submit without explicit consent at the moment of submission**: "I authorize you to e-file (or: I will mail) this Form 1040-X for tax year YYYY now."
2. **Never store** SSNs, dates of birth, PINs, IP PINs, prior-year AGI, or bank account numbers in logs, memory, or transcripts. Collect at submission, use, discard.
3. **Never bypass** identity verification, CAPTCHAs, or MFA; pause and let the user respond.
4. **Stop on disagreement**: if software numbers differ from the draft, or the software flags an error, stop and surface it. Do not override.
5. **Keep proof**: e-file acceptance or mailing receipt, saved under the user's control, with the date. The refund-claim deadline depends on it ([`references/refund-statute.md`](./references/refund-statute.md)).
6. **State return**: remind the user that a separate state amendment may be needed and is not attached to the federal package.
