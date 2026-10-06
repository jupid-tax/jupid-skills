# Submitting Form SS-4 (channel playbook)

How an agent takes a completed Form SS-4 draft from `SKILL.md` and gets the EIN issued. There are four channels: the IRS online application, the international telephone line, fax, and mail. Which ones the applicant may use depends on where the applicant is located and whether the responsible party has an SSN or ITIN.

Sources: Instructions for Form SS-4 (Rev. December 2025), "How To Apply for an EIN" and "Third-party designee"; IRS [Get an employer identification number](https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number) page (reviewed 19-Aug-2026); IRS [Employer identification number](https://www.irs.gov/businesses/employer-identification-number) page (reviewed 17-Jul-2026). Phone and fax numbers "may change without notice" (Instructions, Apply by fax): re-check both pages before every submission.

Produce the complete draft first. Then pick a channel. Then follow the channel section.

---

## Channel decision tree

```
Does the applicant have a legal residence, principal place of business, or
principal office or agency in the U.S. or a U.S. territory?
│
├── YES
│   ├── Is the entity a domestic organization (formed in the U.S. or a territory),
│   │   with its principal place of business in the U.S. or a territory,
│   │   and does the responsible party have an SSN or ITIN,
│   │   and is the applicant NOT applying with an EIN as the responsible party's
│   │   number (government entities excepted)?
│   │   ├── YES → ONLINE (Section 1). EIN at the end of the session.
│   │   └── NO  → FAX (Section 3) or MAIL (Section 4).
│   └── Telephone is NOT available ("The IRS no longer issues EINs by
│       telephone for domestic taxpayers").
│
└── NO (international applicant)
    ├── Online is NOT available.
    ├── TELEPHONE 267-941-1099 (Section 2): EIN during the call.
    ├── FAX 855-215-1627 (from within the U.S.) or 304-707-9471 (from
    │   outside the U.S.) (Section 3): generally within 4 business days.
    └── MAIL to EIN International Operation (Section 4): about 4 weeks.

Third party designee whose address or phone matches the taxpayer's?
  → Online and telephone are out; the application must be mailed or faxed.
```

Rules that apply to every channel:

- **One EIN per responsible party per day**, online, telephone, fax, or mail (Instructions, General Instructions caution).
- **Use only one method for each entity** so the entity does not receive two EINs (Instructions, How To Apply).
- **No fee.** "You never have to pay a fee for an EIN" (Get an EIN page). A third-party service may charge for its own work; the IRS does not.
- **Form the entity with the state first** (Get an EIN page).

---

## Section 1 — Online application

Start from https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number and follow its "Apply for an EIN" link. Do not use third-party sites that imitate the IRS application.

### Eligibility (all must be true; Get an EIN page, "Who can use this tool")

- Domestic organization, formed or created in the United States or U.S. territories
- Principal place of business in the U.S. or U.S. territories
- The person applying is the responsible party or its authorized representative (a third party designee needs signed authorization)
- The applicant has the responsible party's SSN or ITIN
- Not applying with an EIN (unless a government entity)

### Session rules (Get an EIN page)

- Complete in one session; it cannot be saved.
- Expires after 15 minutes of inactivity; the applicant must start over.
- Available (Eastern time): Monday to Friday 6:00 a.m. to 1:00 a.m. (next day); Saturday 6:00 a.m. to 9:00 p.m.; Sunday 6:00 p.m. to 12:00 a.m.
- If approved, the EIN is issued immediately online. Print or save the EIN confirmation letter at the end of the session (Instructions: applicants "have an option to view, print, and save their EIN assignment notice at the end of the session").

### Agent flow

1. Confirm eligibility against the list above. If any item fails, switch to fax or mail.
2. Have the full SS-4 draft open; the online questions follow the same fields.
3. Get explicit consent from the user to submit on their behalf at this moment (see Consent and security).
4. Ask the user to enter, or read aloud for entry, the responsible party's SSN or ITIN at the point the page asks for it. Do not store it.
5. Answer the entity-type questions to match line 9a of the draft. Stop if the page offers a choice that does not match the draft.
6. At the confirmation screen, save the EIN confirmation letter to the user's own storage. Record the EIN in the deliverable.
7. If the session errors out, do not immediately retry: ask the user to call 800-829-4933 to verify whether a number was assigned before any second attempt (one EIN per responsible party per day).

---

## Section 2 — Telephone (international applicants only)

- **Number:** 267-941-1099 (not toll free)
- **Hours:** 6:00 a.m. to 11:00 p.m. Eastern time, Monday through Friday
- **Who may use it:** applicants with no legal residence, principal place of business, or principal office or agency in the U.S. or U.S. territories (Instructions, "Apply by telephone"; Employer identification number page, "International EIN applicants")

Agent flow:

1. Complete the SS-4 draft before the call. The IRS representative uses it to establish the account.
2. The caller must be authorized to receive the EIN and answer questions about the form. That is the applicant, or a third party designee named and authorized in the signed designee block.
3. The agent does not place the call. The user (or the authorized designee) calls; the agent supplies the draft as a script.
4. Write the EIN in the upper right corner of the form, then sign and date it; keep the copy.
5. If the representative asks, mail or fax the signed Form SS-4 (including any designee authorization) within 24 hours to the address the representative gives.

---

## Section 3 — Fax (Fax-TIN)

| Applicant location | Fax number | Source |
|---|---|---|
| Legal residence, principal place of business, or principal office or agency in one of the 50 states or DC | 855-641-6935 | Instructions, Apply by fax; Employer identification number page |
| None of the above in any state or DC (U.S. territory or international), faxing from within the U.S. | 855-215-1627 | Instructions, Apply by fax |
| Same, faxing from outside the U.S. | 304-707-9471 | Instructions, Apply by fax |

- Timing: EIN generally faxed back within 4 business days, if the applicant provides a return fax number (Instructions; the irs.gov page says "about 4 business days" and that the IRS faxes a cover sheet with the EIN, no longer the notated Form SS-4).
- Fax-TIN numbers are only for EIN applications and are available 24 hours a day, 7 days a week. Long-distance charges may apply.
- The fillable SS-4 downloaded from irs.gov is suitable for faxing.

Agent flow: fill the fillable PDF from the draft, include the applicant's fax number in the signature area, have the authorized signer sign and date, and let the user send it. Record the send date and the expected reply date (4 business days later).

---

## Section 4 — Mail

| Applicant location | Address | Source |
|---|---|---|
| Legal residence, principal place of business, or principal office or agency in one of the 50 states or DC | Internal Revenue Service, Attn: EIN Operation, Cincinnati, OH 45999 | Instructions, Apply by mail |
| None of the above in any state or DC (U.S. territory or international) | Internal Revenue Service, Attn: EIN International Operation, Cincinnati, OH 45999 | Instructions, Apply by mail |

- Mail the form at least 4 to 5 weeks before the EIN is needed; the EIN arrives by mail in approximately 4 weeks (Instructions).
- Status of a mailed application, or verification of a number: 800-829-4933 (Instructions).
- The irs.gov page notes that high inventory may delay processing and points to the IRS "Processing status for tax forms" page. Check it before promising a date.

---

## After submission

| Need | When the EIN works | Source |
|---|---|---|
| Open a bank account, apply for business licenses, file a paper return | Immediately | Employer identification number page |
| Pass the IRS TIN Matching Program, e-file a return, make tax deposits and pay electronically | Allow up to 2 weeks | Employer identification number page |

- **Return due before the EIN arrives:** write "Applied For" and the application date in the EIN space. Don't show an SSN as the EIN (Instructions, Reminders).
- **Deposit due before the EIN arrives:** the instructions say to send the payment to the Internal Revenue Service Center for your filing area shown in the instructions for the return you are filing, with a check or money order payable to "United States Treasury", showing the name as on Form SS-4, address, type of tax, period covered, and the date you applied (Instructions, Reminders). The irs.gov EIN page states the payee as "Internal Revenue Service". Use the payee in the instructions for the specific return and tell the user about the inconsistency.
- **Confirmation later:** an Entity transcript, a digital CP575 downloaded by eligible Business Tax Account users, or Letter 147C requested at 800-829-4933 (Employer identification number page, "EIN confirmation").
- **Changes later:** Form 8822-B within 60 days for a responsible-party change; also for address and location changes (Instructions, Reminders).

---

## Consent and security rules

These are not optional.

1. **Explicit consent at submission.** Before the agent submits online, or prepares a fax or mail package for the user to send, capture the user's statement that they authorize this application now, for this entity, through this channel.
2. **Never store SSNs or ITINs.** Collect the responsible party's number only at the moment of entry, use it, and discard it. Do not write it into the draft file, logs, memory, or a vector store. In saved drafts, line 7b reads "[collected at submission]".
3. **The responsible party or an authorized representative applies.** The agent acts only as the user's tool. A third party designee needs the signed authorization in the designee block, and the authority ends when the EIN is assigned (Instructions, Third-party designee). Nominees cannot apply (Responsible parties and nominees page).
4. **No workarounds.** Do not use another person's SSN or ITIN to pass online eligibility. Do not apply through more than one channel for the same entity.
5. **Identity checks and CAPTCHAs** are for the user to complete. Pause and hand control back.
6. **Save confirmations under the user's account**, not the agent's: the online confirmation letter, the fax return sheet, or the mailed notice.
7. **Stop on anything unexpected.** If the online application asks a question the draft does not answer, or a phone representative's instruction conflicts with the draft, stop and surface it to the user.
