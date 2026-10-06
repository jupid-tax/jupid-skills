# Form SS-4 Common Mistakes

Frequent errors on EIN applications, why each one matters, and the fix. Every rule cites the Instructions for Form SS-4 (Rev. December 2025) or an irs.gov page. Re-check against the current revision at https://www.irs.gov/forms-pubs/about-form-ss-4.

## 1. Checking "Sole proprietor" on line 9a for a single-member LLC

**What happens:** The LLC owner reasons that a one-owner LLC is taxed like a sole proprietorship and checks the Sole proprietor box.

**Rule:** "If you formed a single-member LLC that will be classified as a disregarded entity, check the 'Other' box on line 9a and write 'disregarded entity' in the space provided" (Instructions, Lines 8a–8c TIP). A foreign-owned one writes "Foreign-owned U.S. disregarded entity-Form 5472"; one that will elect corporate or S status checks Corporation and writes "Single-member" and 1120 or 1120-S (Instructions, Disregarded entities).

**Fix:** Use the decision table in [`entity-type-and-reason.md`](./entity-type-and-reason.md).

## 2. Naming a nominee, formation service, or company as the responsible party

**Rule:** The responsible party must be an individual unless the applicant is a government entity (Instructions, Lines 7a–7b caution). "Nominees can't apply for an EIN and shouldn't be listed on Form SS-4" (IRS Responsible parties and nominees page).

**Fix:** Ask who ultimately controls the entity and its funds. If a nominee was already listed, correct it on Form 8822-B.

## 3. Using the online application when not eligible

**What happens:** A foreign owner, or an applicant whose responsible party has no SSN or ITIN, starts the online application and is rejected, or enters someone else's number to get through.

**Rule:** Online is only for applicants with a legal residence, principal place of business, or principal office or agency in the U.S. or U.S. territories, and the responsible party must have an SSN or ITIN (Instructions, "Apply for an EIN online"; Get an EIN page). Line 7b must be the number of the person named on line 7a; the application is signed under penalties of perjury, and the instructions warn that "Providing false information could subject you to penalties" (Privacy Act notice).

**Fix:** Route to telephone (international applicants only), fax, or mail. See `../filing.md`.

## 4. Applying twice for the same entity, or twice in one day

**Rule:** One EIN per responsible party per day across all channels (Instructions, General Instructions caution). "Use only one method for each entity so you don't receive more than one EIN for an entity" (Instructions, How To Apply).

**Fix:** Pick one channel. If a fax or mailed application is pending, do not also apply online. To check status of a mailed application or verify a number, call 800-829-4933 (Instructions, Apply by mail).

## 5. Applying for a new EIN when none is needed

**What happens:** The owner renames the business, moves, changes the responsible party, or files Form 8832 or Form 2553, and requests a new EIN.

**Rule:** No new EIN for a name change, a Form 8832 classification change, or a partnership termination under the 50% sale rule (Form SS-4 page 2, footnote 2). An existing corporation electing or revoking S status keeps its EIN (footnote 9). Address and responsible-party changes go on Form 8822-B (Instructions, Reminders).

**Fix:** Run the "When a new EIN is needed" table in [`entity-type-and-reason.md`](./entity-type-and-reason.md) before drafting.

## 6. Line 1 name that does not match the formation document

**Rule:** Enter the legal name exactly as it appears on the charter or other legal document; corporations include the suffix (Instructions, Line 1). The online system accepts only letters, numbers, hyphens, and ampersands (Employer identification number page, Business Name & Address Rules).

**Fix:** Copy the name from the articles; apply only the IRS character substitutions (spell out symbols, slashes become hyphens, drop apostrophes). Tell the user which characters were changed.

## 7. Leaving line 10 blank or checking two reasons

**Rule:** "Check only one box. Don't enter 'N/A.' A selection is required" (Instructions, Line 10).

**Fix:** Pick the single best fit using the line 10 table. A foreign-owned disregarded entity uses Other with the Form 5472 text.

## 8. Treating the Form 944 box as a default

**Rule:** Check line 14 only if employment tax liability is expected to be $1,000 or less for a full calendar year, generally $5,000 or less in wages ($6,536 in U.S. territories). Once checked, the employer files Form 944 until the IRS instructs it to file Form 941 (Instructions, Line 14).

**Fix:** Ask for expected wages for the next 12 months. If none, skip line 14.

## 9. Applying before the entity exists

**Rule:** The IRS asks corporations and LLCs to form with the secretary of state before applying; otherwise "your EIN application may be delayed" (Get an EIN page).

**Fix:** Confirm the filing date on the state's approval. Enter the real start date on line 11.

## 10. Third party designee with the taxpayer's own address or phone

**Rule:** If the designee's address or telephone number matches the taxpayer's, the application must be mailed or faxed. The authorization is valid only if the signature area is completed, and it ends when the EIN is assigned (Instructions, Third-party designee).

**Fix:** Use the designee's own office address and phone, or switch the channel to fax or mail.

## 11. Missing the follow-on deadlines

- 1120-S on line 9a without filing Form 2553 on time: the entity stays a Form 1120 filer until Form 2553 is received and approved (Instructions, Line 9a caution). Hand off to `../../form-2553/SKILL.md`.
- Responsible-party change not reported within 60 days on Form 8822-B (Instructions, Reminders).
- Return due before the EIN arrives: write "Applied For" and the application date in the EIN space; never put an SSN in the EIN space (Instructions, Reminders).

## 12. Using the new EIN too early for electronic filing

**Rule:** The EIN can be used immediately to open a bank account, apply for licenses, or file a paper return, but allow up to 2 weeks before it passes the IRS TIN Matching Program, can be used to e-file a return, or can be used for electronic payments (Employer identification number page, "When you can use your EIN").

**Fix:** Tell the user the date 2 weeks after assignment and plan EFTPS enrollment and e-filing after it.
