# Filing Form 1065

How an agent takes a validated Form 1065 draft (from `SKILL.md`) to a filed return and delivered Schedules K-1. Sources: Instructions for Form 1065 (2025), pp. 5-10; Treasury Regulations section 301.6011-3; Instructions for Form 7004 (Rev. December 2025). Load this file only after the draft has passed validation and the user has said they want to file.

---

## Pre-flight checklist

Do not start any filing channel until every item is true:

- [ ] The draft passed every check in SKILL.md **Validation**, with no open "ask the user" items
- [ ] Every partner's K-1 is complete, and K-1 boxes sum to Schedule K
- [ ] Attachments are ready: Form 1125-A, Form 4562, Form 8825, Schedule D, Form 4797, line 7/line 21/line 20c statements, Schedule B-1, Schedule B-2, Statement A, K-3 notice, section 754 statement (whichever apply)
- [ ] A partner or LLC member is available to sign; the return "isn't considered to be a return unless it's signed by a partner or LLC member" (Instructions p. 6)
- [ ] The partnership representative fields are complete, or Schedule B-2 is attached with question 33 "Yes"
- [ ] The user has confirmed the filing channel and given explicit consent to file

---

## Channel decision tree

```
Is today after the due date (15th day of the 3rd month after year end, next business day
if it falls on a weekend or legal holiday) and no valid Form 7004 was filed by that date?
  → The return is late. File as soon as possible by any allowed channel below.
    Do not file Form 7004 now: it must be filed by the regular due date (Instructions p. 5).
    Estimate the IRC §6698 penalty (references/bba-audit-and-penalties.md) and tell the user.

Is the return not ready, and the due date has not passed?
  → File Form 7004 (form code 09 for Form 1065) by the due date for an automatic 6-month
    extension (Instructions for Form 7004, Extension Period). Use ../form-7004/SKILL.md.
    The extension also moves the K-1 furnishing deadline, since K-1s are due when the
    return is required to be filed.

Was the partnership required to file 10 or more returns of any type during the calendar
year ending with or within its tax year (income tax, employment tax, excise tax, and
information returns such as Forms W-2 and 1099; Schedules K-1 do not count), or did it
have more than 100 partners during the tax year?
  → E-filing is mandatory (Regulations section 301.6011-3(a), (d)(5)-(6); Instructions p. 5).
    Use Section 1. Paper is allowed only with a hardship waiver or the religious exemption
    (Section 3).

Otherwise
  → The user chooses: e-file (Section 1) or paper (Section 2).
```

Counting example: for a calendar-year 2025 return, count the returns the partnership was required to file during calendar 2025 (for example the 2024 Form 1065 filed in 2025, Forms W-2 and 1099 for 2024 filed in early 2025, and the Forms 941 and 940 filed during 2025). Ask the user for the list; do not estimate it.

---

## Section 1 — Electronic filing (Modernized e-File)

Form 1065 is e-filed through software from an authorized IRS e-file provider using the Modernized e-File (MeF) system (Instructions p. 5). The IRS lists providers at https://www.irs.gov/e-file-providers/1065-mef-providers. References: Pub. 4163 (MeF information for authorized e-file providers for business returns), Form 8879-PE (e-file authorization for Form 1065), Form 8453-PE (e-file declaration). e-Help Desk: 866-255-0654.

Generic flow (provider screens differ; follow on-screen labels, not remembered layouts):

1. Create the 2025 Form 1065 for the partnership's EIN and tax year.
2. Enter page 1, Schedule B, Schedule K, page 6, and each K-1 from the draft. Where the software computes a line (lines 1c, 3, 8, 16c, 22, 23; Analysis line 1; M-1 line 9; M-2 line 9), compare its number to the draft. If they differ, stop: one of them is wrong. Do not override.
3. Attach the required forms and statements (Form 1125-A, Form 4562, Schedule B-1, Schedule B-2, line 21 statement, Statement A, section 754 statement if any).
4. Run the software's diagnostics and clear every error.
5. Signature: a partner or LLC member signs Form 8879-PE (the provider's process controls how). Keep the signed Form 8879-PE with the partnership's records as the provider instructs.
6. Transmit only after the user confirms, in this session, that they authorize transmission now.
7. Record the submission ID and the acknowledgment (accepted or rejected). On rejection, read the reject code, fix the cause, and retransmit; never change numbers just to clear a reject without understanding it.
8. Item C on each K-1 reads "e-file".

---

## Section 2 — Paper filing

### Assembly order (Instructions p. 10)

1. Form 1065, pages 1-6
2. Schedule F (Form 1040), if required
3. Form 8825, if required
4. Schedule D (Form 1065), if required
5. Form 4797, if required
6. Form 8949, if required
7. Form 8996, if required
8. Form 1125-A, if required
9. Form 8941, if required
10. Form 3800, if required
11. Form 6252, if required
12. Form 8997, if required
13. Form 8283, if required
14. Schedule A (Form 8936), if required
15. Form 4255, if required
16. Schedules K-1 (Form 1065)
17. Form 8938, if required
18. Any other schedules in alphabetical order, including Schedules K-2 and K-3
19. Any other forms in numerical order

Complete every entry space; do not write "See attached" in place of an entry. Supporting statements go at the end, same size as the printed forms, each with the partnership's name and EIN (Instructions p. 10). A partner or LLC member signs page 1 in ink.

### Where to file (Instructions p. 6, Where To File table, 2025)

| Principal business, office, or agency in | Total assets at year end (item F) | Address |
|-------------------------------------------|-----------------------------------|---------|
| Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin | Less than $10 million and Schedule M-3 not filed | Department of the Treasury, Internal Revenue Service Center, Kansas City, MO 64999-0011 |
| Same states | $10 million or more, or less than $10 million and Schedule M-3 filed | Department of the Treasury, Internal Revenue Service Center, Ogden, UT 84201-0011 |
| Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Texas, Utah, Washington, Wyoming | Any amount | Department of the Treasury, Internal Revenue Service Center, Ogden, UT 84201-0011 |
| A foreign country or U.S. territory | Any amount | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 |

If Schedule M-3 is filed, the return goes to Ogden regardless of state. When Schedule B, question 4 is "Yes" and item F is blank, use the books' year-end total assets to pick the row. Re-check this table in the instructions for the year being filed; service center assignments change.

### Mailing

- Timely mailing counts as timely filing when the envelope is mailed by U.S. Postal Service or an IRS-designated private delivery service (PDS) by the due date. Current PDS list: https://www.irs.gov/pds. PDS street addresses: https://www.irs.gov/pdsstreetaddresses. A PDS cannot deliver to a P.O. box (Instructions p. 5).
- Use USPS Certified Mail with return receipt, or a designated PDS service, so the user keeps proof of the mailing date.
- Keep a complete copy of the signed return and all attachments.

---

## Section 3 — Waivers and exemptions from mandatory e-filing (Instructions p. 5)

- **Hardship waiver**: written request in the manner prescribed by the Ogden Submission Processing Center, mailed to Internal Revenue Service, Ogden Submission Processing Center, Attn: Form 1065 e-file Waiver Request, Stop 1057, Ogden, UT 84201; by overnight delivery to Internal Revenue Service, Ogden Submission Processing Center, Attn: Form 1065 e-file Waiver Request, Stop 1056, 1973 N. Rulon White Blvd., Ogden, UT 84404; or by fax to 877-477-0575. Guidance: https://www.irs.gov/e-file-providers/guidance-on-waivers-for-partnerships-unable-to-meet-e-file-requirements. Request it well before the due date; the waiver does not extend the due date.
- **Religious exemption**: if e-filing technology conflicts with the partners' religious beliefs, file on paper and write "Religious Exemption" at the top of page 1.
- Bankruptcy returns and returns with pre-computed penalty and interest are excluded from the e-file requirement.

---

## Section 4 — Delivering Schedules K-1 (and K-3)

- Furnish each K-1 to the partner on or before the day the return is required to be filed, including extensions (Instructions p. 32; Schedule B, question 4(c)).
- Include the Partner's Instructions for Schedule K-1 (Form 1065) or item-by-item instructions (Instructions p. 31).
- When relying on the domestic filing exception or the small partnership exception for Schedules K-2 and K-3, include the notice that the partner will not receive Schedule K-3 unless they request it.
- The partner's copy may show a truncated SSN or EIN; the IRS copy may not (Instructions p. 33).
- Any copy of the full Form 1065 given to a partner is marked "Duplicate Copy" (Instructions p. 18).
- If the partnership elected out of the centralized audit regime, send each partner notice of the election within 30 days (Regulations section 301.6221(b)-1(c)(3)).

---

## Section 5 — Payments (uncommon)

Most partnerships owe nothing with Form 1065. If line 31 shows an amount owed (look-back interest, a BBA AAR imputed underpayment, or other taxes), pay electronically through https://www.irs.gov/payments (Direct Pay, debit or credit card, digital wallet, or the IRS business tax account) (Instructions p. 25). BBA AAR imputed underpayment checks go to Internal Revenue Service, Ogden Service Center, Ogden, UT 84201-0011, as described in [`references/bba-audit-and-penalties.md`](./references/bba-audit-and-penalties.md).

---

## Section 6 — After filing

1. Save the acknowledgment (e-file) or the mailing receipt (paper), and the full return as filed.
2. Records supporting the return are kept for as long as they may be needed; generally at least 3 years from the later of the due date or filing date, and also 3 years from the later of each partner's return due date or filing date; basis records for as long as the basis matters (Instructions p. 9).
3. State returns are separate. For a California LLC, see [`../ca-form-568/SKILL.md`](../ca-form-568/SKILL.md); otherwise point the user to the state's partnership return.
4. Partner handoffs: box 1 and box 4 to the partner's Schedule E, Part II ([`../schedule-e/SKILL.md`](../schedule-e/SKILL.md)); box 14 to Schedule SE ([`../schedule-se/SKILL.md`](../schedule-se/SKILL.md)); box 20, code Z to Form 8995 or 8995-A ([`../form-8995/SKILL.md`](../form-8995/SKILL.md), [`../form-8995-a/SKILL.md`](../form-8995-a/SKILL.md)).
5. Errors found later: follow the AAR or amended-return route in [`references/bba-audit-and-penalties.md`](./references/bba-audit-and-penalties.md).
6. Address or responsible-party changes after filing: Form 8822-B (Instructions p. 18).

---

## Consent and security rules

1. **Explicit consent at submission.** Capture the user's statement that they authorize filing this return through the named channel now. Consent given for drafting is not consent to file.
2. **The signer is a partner or LLC member.** The agent never signs, never enters a partner's signature PIN, and never completes Form 8879-PE on the signer's behalf.
3. **Protect identifiers.** Do not store SSNs, EINs of individual partners, bank account and routing numbers (line 32b-32d), or e-file PINs in logs, memory, or transcripts beyond what the filing step needs. Use truncated SSNs on partner copies.
4. **No placeholders.** Do not file with "TBD" in the PR designation, partner TINs, or addresses. An incomplete return can be penalized as a failure to file a complete return (Instructions p. 7).
5. **Stop on disagreement.** If the software's computed figure differs from the draft, or an acknowledgment is a rejection the agent does not understand, stop and report to the user.
6. **Identity checks and CAPTCHAs** are for the user to complete. Do not bypass them.
