---
name: form-ss-4
description: >
  Use this skill when a business, LLC, corporation, partnership, trust, estate,
  household employer, withholding agent, or a foreign-owned U.S. LLC needs an
  Employer Identification Number (EIN) and must prepare Form SS-4 or the
  answers for the IRS online EIN application. Triggers on phrases like
  "Form SS-4", "apply for an EIN", "get an EIN for my LLC", "EIN for a
  foreign-owned LLC", "EIN without an SSN", "responsible party on the EIN
  application", "which box on line 9a", "do I need a new EIN", "fax SS-4",
  "international EIN phone number". Do NOT use for: an individual ITIN (use
  ../form-w7/SKILL.md); a Social Security number (SSA Form SS-5); a preparer
  PTIN (Form W-12); making the entity classification election itself (use
  ../form-8832/SKILL.md); making the S corporation election (use
  ../form-2553/SKILL.md); filing employment tax returns after the EIN is
  issued (use ../form-941/SKILL.md); Form 5472 for a foreign-owned LLC (use
  ../form-5472/SKILL.md).
form: Form SS-4 (Application for Employer Identification Number)
audience: [solo, llc1, llcm, scorp, ccorp, partnership, employer, household-employer, nonresident]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/fss4.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/iss4.pdf
---

# Form SS-4 — Application for Employer Identification Number

This skill produces a completed Form SS-4 draft (every line 1 through 18, the third party designee block, and the signature block) plus a channel decision: IRS online application, international telephone line, fax, or mail. The same draft doubles as the answer sheet for the online application, which asks the same questions.

There is almost no arithmetic on Form SS-4. The judgment concentrates in four places: who the responsible party is (lines 7a and 7b), which box to check on line 9a for an LLC (the box follows the federal tax classification and the reason for the EIN, not the word "LLC"), which single reason to check on line 10, and which channel the applicant is allowed to use. Each of these depends on facts the agent must ask for. Do not pick defaults.

**Companion guide for end users:** [Form SS-4 (2026): How to Complete the EIN Application Line by Line](https://jupid.com/blog/form-ss-4-ein-application-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Revision verified:** the line map in this skill was built from the text of Form SS-4 (Rev. December 2025) and the Instructions for Form SS-4 (Rev. December 2025). Form SS-4 is revised by date, not by tax year. Before using this skill, open [About Form SS-4](https://www.irs.gov/forms-pubs/about-form-ss-4) and confirm the "Current revision" is still December 2025. If a newer revision exists, re-check every line number and every phone, fax, and address in this skill against it.

**Key values used by this skill** (re-verify on each use; irs.gov pages change without a form revision):

| Item | Value | Source |
|---|---|---|
| EIN fee | None; the IRS never charges for an EIN | Get an EIN page |
| Daily limit | 1 EIN per responsible party per day, all channels | Instructions, General Instructions caution; Get an EIN page |
| Online application | U.S. or territory applicants only; issued at end of session | Instructions, "Apply for an EIN online" |
| International phone | 267-941-1099, not toll free, 6 a.m. to 11 p.m. ET, Monday to Friday | Instructions, "Apply by telephone" |
| Fax (50 states + DC) | 855-641-6935, generally within 4 business days | Instructions, "Apply by fax" |
| Fax (no presence in any state or DC) | 855-215-1627 inside the U.S.; 304-707-9471 outside the U.S. | Instructions, "Apply by fax" |
| Mail | Internal Revenue Service, Attn: EIN Operation (or EIN International Operation), Cincinnati, OH 45999; approximately 4 weeks | Instructions, "Apply by mail" |
| Responsible party change | Report on Form 8822-B within 60 days | Instructions, "Reminders"; Reg. 301.6109-1(d)(2)(ii) |
| Form 944 line 14 test | $1,000 or less liability; generally $5,000 or less in wages ($6,536 in U.S. territories) | Instructions, Line 14 |

---

## When to invoke

Engage this skill when any of the following is true:

- The user mentions Form SS-4, an EIN application, or the IRS online EIN assistant
- The user formed (or is about to form) an LLC, corporation, or partnership and needs a federal tax ID for a bank account, payroll, state registration, or a tax return
- The user hired or will hire employees, including household employees, and has no EIN
- A foreign person owns a U.S. single-member LLC and needs an EIN so the LLC can file Form 5472 with a pro forma Form 1120
- A trust, estate, pension plan administrator, or withholding agent (Form 1042 filer) needs an EIN
- The user asks whether a change (incorporating, adding a member, converting, buying a business) requires a new EIN
- The user's responsible party has no SSN or ITIN and the online application rejected them

Do not engage this skill when:

- The person needs an individual taxpayer number and is not eligible for an SSN → `../form-w7/SKILL.md` (ITIN). An EIN never replaces an SSN or ITIN on an individual return (Instructions for Form SS-4, "Purpose of Form").
- The person needs an SSN → Social Security Administration, Form SS-5, not the IRS
- The person is a paid preparer who needs a PTIN → Form W-12
- The user already has an EIN and wants to elect corporate or disregarded classification → `../form-8832/SKILL.md`
- The user already has an EIN and wants S corporation status → `../form-2553/SKILL.md` (an existing corporation keeps its EIN; Form SS-4, page 2, footnote 9)
- The user already has an EIN and needs to file Form 941 → `../form-941/SKILL.md`
- The user only changed the business name, address, or responsible party → no new EIN; Form 8822-B reports address and responsible-party changes (Instructions for Form SS-4, "Reminders")

Boundary with sibling skills: this skill stops when the EIN is assigned. If the applicant will also file Form 8832 or Form 2553, the SS-4 answers on line 9a must match that plan, so confirm the plan first (see Step 3) and then hand off.

---

## Prerequisites

Before drafting anything, collect these inputs. If any are missing, ask for them explicitly and stop until you have an answer.

1. **Legal name of the entity** exactly as on the state formation document, trust instrument, or partnership agreement. For a sole proprietor, the individual's name (line 1) and the business name separately (line 2).
2. **Entity type and federal tax classification intent.** Ask: "Is this an LLC? How many members? Will it keep the default classification, elect to be taxed as a C corporation (Form 8832), or elect S corporation status (Form 2553)?" Do not assume. The line 9a box depends on the answer.
3. **Where the entity was organized** (U.S. state, or a foreign country). Feeds line 8c and line 9b.
4. **Principal place of business** (physical location, county and state) and whether the entity has a legal residence, principal place of business, or principal office or agency in the United States or a U.S. territory. This decides which channels are available.
5. **Responsible party**: full name and whether that person has an SSN or ITIN. Ask: "Who ultimately owns or controls this entity and its funds? Does that person have a U.S. Social Security number or ITIN?" The responsible party must be an individual except for government entities.
6. **Reason for applying** (one only), and the start or acquisition date.
7. **Employees expected in the next 12 months** (agricultural, household, other), expected total wages, and the first wage date. Needed for lines 13 to 15.
8. **Principal activity** in plain words (line 16 box and line 17 description).
9. **Prior EIN**: has this entity ever applied for and received an EIN? (line 18)
10. **Third party designee**, if someone other than the applicant will receive the EIN: name, address, phone, fax, and the applicant's willingness to sign the authorization.
11. **Mailing address and, if different, street address**, plus a fax number if the applicant will fax.
12. **Accounting year end** (line 12). Ask; do not assume December for a trust, partnership, or personal service corporation (Instructions, Line 12).

Collect identifying numbers (SSN, ITIN) only at the moment they are needed for submission, and never store them in logs or notes. See `filing.md`.

---

## Workflow

Execute in order. Each step is a discrete decision.

### Step 1 — Confirm an EIN is needed and that one does not already exist

Use the "Do I Need an EIN?" table on page 2 of Form SS-4 and the IRS [Get an EIN](https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number) page. Ask whether the entity ever received an EIN. Do not apply for a new EIN when the existing entity only changed its name, elected a different classification on Form 8832, or had a partnership terminate because at least 50% of capital and profits interests were sold within 12 months (Form SS-4, page 2, footnote 2; Regulations section 301.6109-1(d)(2)(iii)). For changes in ownership or structure, use [`references/entity-type-and-reason.md`](./references/entity-type-and-reason.md), section "When a new EIN is needed".

Also confirm the entity is already formed with the state. The IRS asks corporations and LLCs to form with the secretary of state before applying; applying first may delay the application (Get an EIN page).

### Step 2 — Identify the responsible party

Apply the definition in [`references/responsible-party.md`](./references/responsible-party.md). The responsible party owns or controls the entity or exercises ultimate effective control, must be a natural person (unless a government entity), and cannot be a nominee such as a formation-service employee. If more than one person qualifies, ask the user which one the IRS should recognize (IRS "Responsible parties and nominees" page).

Record whether the responsible party has an SSN or ITIN. If not, line 7b gets "foreign" or "N/A" (Instructions, Lines 7a–7b TIP), and the online application is unavailable.

### Step 3 — Fix the federal tax classification, then choose the line 9a box

Use the decision table in [`references/entity-type-and-reason.md`](./references/entity-type-and-reason.md). Key rules from the instructions:

- Single-member LLC that stays disregarded, EIN needed for employment or excise tax or state purposes: **Other**, write "Disregarded entity"
- Foreign-owned U.S. single-member LLC that needs an EIN to file Form 5472: **Other**, write "Foreign-owned U.S. disregarded entity-Form 5472"
- Single-member LLC that will file Form 8832 or Form 2553: **Corporation**, write "Single-member" and the return form number (1120 or 1120-S)
- Multi-member domestic LLC keeping partnership treatment: **Partnership**
- Domestic LLC that will elect corporate or S corporation treatment: **Corporation**, write 1120 or 1120-S
- Disregarded entity that gained an owner and became a partnership by default: **Partnership**

If the user has not decided between default classification and an election, stop and say the decision belongs with their tax adviser; this skill does not recommend a classification.

### Step 4 — Choose one reason on line 10

Exactly one box; "N/A" is not allowed (Instructions, Line 10). Map the user's facts with the line 10 table in [`references/entity-type-and-reason.md`](./references/entity-type-and-reason.md). A foreign-owned disregarded entity filing Form 5472 checks **Other** and writes "Foreign-owned U.S. disregarded entity filing Form 5472".

### Step 5 — Complete the remaining lines

Walk lines 1 through 18 with [`references/line-by-line.md`](./references/line-by-line.md). Use the page 2 table of Form SS-4 to decide which lines the applicant's situation requires, and enter "N/A" on lines that do not apply (Instructions, "Specific Instructions": "Generally, enter 'N/A' on the lines that don't apply"). Exceptions: lines 7b, 10, 16, and 17 require an entry.

### Step 6 — Employment lines 13, 14, 15

Enter the highest number of employees expected in the next 12 months in each box, including -0- (Instructions, Line 13). If no employees are expected, skip line 14. For line 14, apply the IRS rule of thumb: employment tax liability is generally $1,000 or less if total wages subject to social security, Medicare, and federal income tax withholding are $5,000 or less ($6,536 or less for employers in the U.S. territories) (Instructions, Line 14). Ask before checking the box; once checked, the employer files Form 944 until the IRS says otherwise.

### Step 7 — Third party designee and signature

Complete the designee block only if the applicant authorizes a named person to receive the EIN and answer questions; the signature block must be completed for the authorization to be valid, and the designee's authority ends when the EIN is assigned and released (Instructions, Line 18 / Third-party designee). If the designee's address or phone matches the taxpayer's, the application must be mailed or faxed, not filed online or by phone. Identify the correct signer by entity type (Instructions, "Signature").

### Step 8 — Pick the channel

Apply the decision tree in [`filing.md`](./filing.md). Summary:

- **Online**: domestic entity, principal place of business in the U.S. or a territory, responsible party has an SSN or ITIN, not applying with an EIN as the responsible party's number (unless a government entity). EIN issued at the end of the session.
- **Telephone 267-941-1099**: only applicants with no legal residence, principal place of business, or principal office or agency in the U.S. or U.S. territories.
- **Fax**: anyone; generally within 4 business days.
- **Mail**: anyone; approximately 4 weeks.

### Step 9 — Validate

Run every check under **Validation**. Do not submit with an open failure.

### Step 10 — Produce the deliverable and hand off

Emit the draft in the **Output format** below. Then state the next steps that depend on the answers:

- Line 9a Corporation with 1120-S → Form 2553 deadline (`../form-2553/SKILL.md`)
- Line 9a Corporation with 1120 for an LLC → Form 8832 (`../form-8832/SKILL.md`)
- Foreign-owned disregarded entity → pro forma Form 1120 with Form 5472 (`../form-5472/SKILL.md`); if the owner has U.S. effectively connected income, the owner's own return (`../form-1040-nr/SKILL.md`) and possibly an ITIN (`../form-w7/SKILL.md`)
- Employees on line 13 → Form 941 quarterly or Form 944 annually (`../form-941/SKILL.md`), Form 940 (`../form-940/SKILL.md`)
- Household employer → Schedule H (`../schedule-h/SKILL.md`)
- Any later change of responsible party or address → Form 8822-B within 60 days

If the user wants the agent to submit, follow [`filing.md`](./filing.md), including its consent and security rules.

---

## Line-by-line guidance

The full map is in [`references/line-by-line.md`](./references/line-by-line.md). The rules that cause most errors:

### Lines 1 to 3 — Names

- **Line 1**: exact legal name, required. Individuals enter first name, middle initial, last name; a sole proprietor enters the individual name here and the business name on line 2. Corporations include the suffix (Inc., Corp., PC). Estates with no legal name: decedent's name followed by "Estate".
- **Line 2**: trade name (DBA) only if different. Use the line 1 name (or, if chosen, the line 2 name) consistently on every return.
- **Line 3**: trustee for a trust, executor or other fiduciary for an estate, or a designated "care of" person.
- The IRS online system accepts only letters, numbers, hyphens, and ampersands in business names and 35 characters for street addresses (Get an EIN / Employer identification number page, "Business Name & Address Rules"). Spell out symbols.

### Lines 4a to 6 — Addresses and location

- **4a–4b**: mailing address for IRS correspondence. Foreign addresses: city, province or state, postal code, full country name, no abbreviation.
- **5a–5b**: street address only if different; no P.O. box.
- **6**: county and state of the entity's primary physical location.

### Lines 7a and 7b — Responsible party

- Natural person (except government entities), not a nominee.
- 7b: SSN or ITIN; government entities may enter an EIN. If the person has no SSN or ITIN and is ineligible to obtain one, enter "foreign" or "N/A". An entry is required.

### Lines 8a to 8c — LLC questions

- 8a Yes for an LLC or foreign equivalent. 8b member count; spouses owning an LLC in a community property state who choose disregarded treatment enter "1". 8c whether the LLC was organized in the United States.

### Line 9a — Entity type (check one box)

The box records the classification and purpose; it is not itself an election (Instructions, Line 9a caution). See the decision table in Step 3. Additional rules:

- **Sole proprietor**: only for a Schedule C or F filer with a qualified plan, or required to file excise, employment, alcohol, tobacco, or firearms returns, or a payer of gambling winnings. Enter SSN or ITIN; a nonresident alien with no effectively connected income enters "N/A".
- **Corporation**: enter the income tax form number to be filed. A nonprofit corporation that is not a church checks "Other nonprofit organization" instead.
- **Personal service corporation**: principal activity is personal services performed substantially by employee-owners who own at least 10% of the stock by fair market value on the last day of the testing period.
- **Other**: always specify the entity type and the return to be filed; never "N/A". Household employer: "Household employer" plus SSN. Withholding agent: "Withholding agent". QSub: "QSub".
- **Estate**: decedent's SSN or ITIN. **Trust**: grantor's TIN. **Plan administrator**: administrator's TIN.

### Line 9b — State or country of incorporation

Complete when line 9a is Corporation. The instructions have no separate line 9b text. For an LLC that will be taxed as a corporation, ask the user to confirm the state (or foreign country) under whose law the entity was organized and enter that; flag the entry for the user's adviser because the line text says "incorporated".

### Line 10 — Reason for applying

One box. Started new business (specify type); Hired employees (existing business without an EIN only); Banking purpose (EIN needed only for banking); Changed type of organization (specify old and new type); Purchased going business; Created a trust (specify type); Created a pension plan (specify type, and check Other on 9a with "Created a pension plan"); Compliance with IRS withholding regulations; Other (specify).

### Lines 11 and 12 — Dates

- **11**: start or acquisition date. Foreign applicants: date the business began or was acquired in the United States. Trusts: date funded. Estates: date of death or date legally funded.
- **12**: closing month of the tax year. Partnerships, REMICs, personal service corporations, and trusts have restrictions (see line-by-line reference).

### Lines 13 to 15 — Employees

See Step 6. Line 15 is the first date wages or annuities were paid; withholding agents enter the date income will first be paid to a nonresident alien; "N/A" if no employees are planned.

### Lines 16 to 18 — Activity and prior EIN

- **16**: check exactly one box; "Other" requires a description.
- **17**: required; describe the principal line of merchandise, construction work, products, or services.
- **18**: Yes and the prior EIN if this entity ever received one.

---

## Validation

Run every check. Surface failures; do not silently fix them.

### Completeness checks

- [ ] Line 1 matches the formation document character for character (after applying IRS character rules)
- [ ] Lines 7a and 7b name one natural person; 7b holds an SSN or ITIN, or "foreign"/"N/A" only when the person has neither and is ineligible
- [ ] Line 7a person is not a nominee, formation service, registered agent, or another entity
- [ ] Line 8a answered; if Yes, 8b and 8c answered
- [ ] Exactly one box on line 9a; "Other" entries specify type and return
- [ ] Line 9a consistent with 8b and the classification plan (one member and Partnership is a contradiction; two members and "Disregarded entity" is a contradiction unless the spouses community property rule applies)
- [ ] Line 9b completed when line 9a is Corporation
- [ ] Exactly one box on line 10, with the required specification
- [ ] Line 11 date is the real start or acquisition date, not the application date by default
- [ ] Lines 13 to 15 consistent: zero employees means line 14 skipped and line 15 "N/A"
- [ ] Line 16 has one box; line 17 has a description
- [ ] Signature block names the correct signer for the entity type, with title, phone, and date

### Channel checks

- [ ] Online chosen only if every eligibility condition in `filing.md` is met
- [ ] Phone chosen only for applicants with no legal residence, principal place of business, or principal office or agency in the U.S. or U.S. territories
- [ ] Fax number matches the applicant's location category
- [ ] Mail address matches: "EIN Operation" (50 states and DC) or "EIN International Operation" (no presence in any state or DC)
- [ ] No other EIN request for the same responsible party on the same day (one EIN per responsible party per day)
- [ ] If a designee is named: authorization signed; designee address and phone differ from the taxpayer's, or the channel is fax or mail

### Sanity checks (warn, do not block)

- [ ] Sole proprietor with no employees, no excise returns, and no qualified plan → may not need an EIN; confirm the reason (Form SS-4, page 2, footnote 1)
- [ ] Single-member LLC with no employees and no excise tax that wants an EIN only for a bank → confirm the bank requires it; the owner's existing sole proprietor EIN may already serve (IRS "When to get a new EIN" page)
- [ ] Line 9a Corporation with 1120-S → remind that the entity is a Form 1120 filer until Form 2553 is received and approved (Instructions, Line 9a caution)
- [ ] Line 14 checked while expected wages exceed $5,000 → probably ineligible for Form 944
- [ ] Applying before state formation is complete → may delay the application

### Cross-form checks

- [ ] Line 9a "Single-member" + 1120 or 1120-S → Form 8832 or Form 2553 is on the user's to-do list with its own deadline
- [ ] Foreign-owned disregarded entity → pro forma Form 1120 with Form 5472 is on the to-do list (filing triggers in `../form-5472/SKILL.md`)
- [ ] Line 13 above zero → payroll setup, Form 941 or 944, Form 940, and EFTPS enrollment are on the to-do list
- [ ] Line 1 legal name will be used identically on every later return (Instructions, Line 2 TIP)

---

## Output format

```markdown
# Form SS-4 — DRAFT (Rev. December 2025)

## Applicant summary
- Entity: <legal name>, <entity type>, organized in <state/country> on <date>
- Federal classification plan: <default disregarded / partnership / Form 8832 to 1120 / Form 2553 to 1120-S / other>
- Channel: <Online / Phone 267-941-1099 / Fax <number> / Mail <address>>

## Lines
1.  Legal name:                         <...>
2.  Trade name:                         <... or N/A>
3.  Executor/trustee/"care of":         <... or N/A>
4a. Mailing address:                    <...>
4b. City, state, ZIP (or foreign):      <...>
5a. Street address (if different):      <... or N/A>
5b. City, state, ZIP:                   <... or N/A>
6.  County and state:                   <...>
7a. Responsible party:                  <full name>
7b. SSN/ITIN/EIN:                       <[collected at submission] / foreign / N/A>
8a. LLC?                                Yes | No
8b. Number of members:                  <n or N/A>
8c. Organized in the U.S.?              Yes | No | N/A
9a. Entity type:                        <box> — "<write-in text>"
9b. State/foreign country:              <... or N/A>
10. Reason:                             <box> — "<specification>"
11. Date started/acquired:              MM/DD/YYYY
12. Closing month:                      <month>
13. Employees expected:                 Agricultural <n>  Household <n>  Other <n>
14. Form 944 box:                       Checked | Not checked | Skipped (no employees)
15. First wages date:                   MM/DD/YYYY | N/A
16. Principal activity:                 <box> (Other: "<text>")
17. Principal line of business:         <text>
18. Prior EIN?                          No | Yes: <EIN>
Third party designee:                   <name, address, phone, fax> | None
Signature:                              <name, title>, phone <...>, date <...>

## Validation summary
- Completeness: <all passed / failures>
- Channel: <eligibility reasoning>
- Warnings: <sanity flags>

## Next steps
- <Form 2553 / Form 8832 / Form 5472 / Form 941 or 944 / Form 8822-B items>
- EIN usable immediately for a bank account; allow up to 2 weeks before e-filing, TIN matching, or electronic deposits

## Sources cited in this draft
- Form SS-4 (Rev. December 2025) and Instructions for Form SS-4 (Rev. December 2025)
- IRS Get an EIN and Employer identification number pages (reviewed <date>)
- (any other authority used)
```

The draft is not the filed application. The applicant (or a signed-authorized designee) still submits it. Every line is traceable to the instructions.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of Form SS-4, the designee block, and the signature rules, from the Rev. December 2025 text
- [`references/responsible-party.md`](./references/responsible-party.md) — who qualifies by entity type, nominees, applicants without an SSN or ITIN, one EIN per day, Form 8822-B
- [`references/entity-type-and-reason.md`](./references/entity-type-and-reason.md) — lines 8a to 10, the line 9a decision table for LLCs, Form 8832 and Form 2553 interplay, when a new EIN is needed
- [`references/common-mistakes.md`](./references/common-mistakes.md) — frequent errors and how to prevent them
- [`filing.md`](./filing.md) — channel decision tree, phone, fax, and mail details, timing, consent and security rules

## Examples

- [`examples/us-single-member-llc.md`](./examples/us-single-member-llc.md) — U.S. resident forms a single-member LLC that stays disregarded; online application
- [`examples/foreign-owned-llc-5472.md`](./examples/foreign-owned-llc-5472.md) — non-U.S. owner with no SSN or ITIN; Form 5472 purpose; international phone line
- [`examples/two-member-llc-s-election.md`](./examples/two-member-llc-s-election.md) — two-member LLC that will elect S corporation status; employees; third party designee

## Sources

Re-verify each source before use; Form SS-4 changes by revision, and irs.gov pages change without notice.

- [Form SS-4 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/fss4.pdf)
- [Instructions for Form SS-4 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/iss4.pdf)
- [About Form SS-4](https://www.irs.gov/forms-pubs/about-form-ss-4) — current revision and recent developments
- [Get an employer identification number](https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number) — online application eligibility, hours, daily limit
- [Employer identification number](https://www.irs.gov/businesses/employer-identification-number) — ways to apply, international applicants, when the EIN can be used, name rules
- [Responsible parties and nominees](https://www.irs.gov/businesses/small-businesses-self-employed/responsible-parties-and-nominees)
- [When to get a new EIN](https://www.irs.gov/businesses/small-businesses-self-employed/when-to-get-a-new-ein)
- [Instructions for Form 2553](https://www.irs.gov/pub/irs-pdf/i2553.pdf) — election timing
- [Form 8832 and instructions](https://www.irs.gov/forms-pubs/about-form-8832) — entity classification
- [Publication 1635, Understanding Your EIN](https://www.irs.gov/pub/irs-pdf/p1635.pdf)
- [Publication 15 (Circular E)](https://www.irs.gov/publications/p15) — employment taxes after the EIN is issued
- IRC §6109; Regulations section 301.6109-1 (including (d)(2)(ii) on responsible-party changes and (d)(2)(iii) on partnership terminations); Regulations section 301.7701-2 and -3 (entity classification)

## Disclaimer

This skill encodes procedural guidance from publicly available IRS forms, instructions, and web pages. It is not tax or legal advice and does not choose an entity's tax classification. The agent should remind the user that the draft is a starting point and that classification choices, foreign ownership, and trust or estate applications warrant review by a qualified tax professional.
