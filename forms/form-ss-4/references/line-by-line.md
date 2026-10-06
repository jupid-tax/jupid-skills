# Form SS-4 Line-by-Line Reference

Every line of Form SS-4 (Rev. December 2025), built from the text of the form and the Instructions for Form SS-4 (Rev. December 2025). Before use, confirm at https://www.irs.gov/forms-pubs/about-form-ss-4 that December 2025 is still the current revision.

General rule from the instructions ("Specific Instructions"): enter "N/A" on lines that don't apply. Lines 7b, 10, 16, and 17 always need an entry ("An entry is required" / "A selection is required" / "You must check a box").

## Which lines a situation requires (Form SS-4, page 2, "Do I Need an EIN?")

| If the applicant... | And... | Complete lines |
|---|---|---|
| Started a new business | has (and expects) no employees | 1, 2, 4a–8a, 8b–c (if applicable), 9a, 9b (if applicable), 10–14, 16–18 |
| Hired or will hire employees, including household employees | has no EIN | 1, 2, 4a–6, 7a–b, 8a, 8b–c (if applicable), 9a, 9b (if applicable), 10–18 |
| Opened a bank account | needs an EIN for banking only | 1–5b, 7a–b, 8a, 8b–c (if applicable), 9a, 9b (if applicable), 10, 18 |
| Changed type of organization | legal character or ownership changed | 1–18 as applicable |
| Purchased a going business | has no EIN | 1–18 as applicable |
| Created a trust | other than a grantor trust or IRA trust | 1–18 as applicable |
| Created a pension plan as plan administrator | needs an EIN for reporting | 1, 3, 4a–5b, 7a–b, 9a, 10, 18 |
| Is a foreign person needing an EIN for IRS withholding regulations | for a Form W-8 (other than W-8ECI), to avoid withholding on portfolio assets, or to claim treaty benefits | 1–5b, 7a–b (SSN or ITIN as applicable), 8a, 8b–c (if applicable), 9a, 9b (if applicable), 10, 18 |
| Is administering an estate | reports estate income on Form 1041 | 1–7b, 9a, 10–12, 13–17 (if applicable), 18 |
| Is a withholding agent for nonwage income paid to an alien | files Form 1042 | 1, 2, 3 (if applicable), 4a–5b, 7a–b, 8a, 8b–c (if applicable), 9a, 9b (if applicable), 10, 18 |
| Is a state or local agency | reporting agent for public assistance recipients (Rev. Proc. 80-4) | 1, 2, 4a–5b, 7a–b, 9a, 10, 18 |
| Is a single-member LLC | needs an EIN for Form 8832, employment or excise returns, state reporting, or Form 5472 as a foreign-owned U.S. disregarded entity | 1–18 as applicable |
| Is an S corporation | needs an EIN to file Form 2553 | 1–18 as applicable |

## Header

| Field | Rule | Source |
|---|---|---|
| EIN box (top right) | Leave blank; the IRS assigns the number. Telephone applicants write the number they are given in the upper right corner of their copy | Instructions, "Apply by telephone" |
| Form revision | Use Rev. December 2025 | About Form SS-4 |

## Lines 1 to 3 — Names

| Line | Field | What goes here | Notes |
|---|---|---|---|
| 1 | Legal name of entity (or individual) | Exact legal name from the social security card, charter, or other legal document. Required | Individuals: first name, middle initial, last name; no nicknames or abbreviations. Sole proprietor: individual name, business name on line 2. Trust: name on the trust instrument. Estate: estate name, or decedent's name followed by "Estate". Partnership: name in the partnership agreement. Corporation: name in the charter including suffix (Inc., Corp., PC). Plan administrator: administrator's name (use an existing EIN if it has one). Indian tribal government or enterprise: legal name |
| 2 | Trade name of business | DBA only if different from line 1 | Use the line 1 name on all returns; if the trade name is chosen instead, use it on all returns |
| 3 | Executor, administrator, trustee, "care of" name | Trustee (trusts); executor, administrator, personal representative, or other fiduciary (estates); designated person to receive tax information | First name, middle initial, last name |

IRS online-system character rules (Employer identification number page, "Business Name & Address Rules"): only letters A–Z, numbers 0–9, hyphens, and ampersands. Spell out or replace symbols such as +, @, and periods ("Jones.Com" becomes "Jones Dot Com" or "Jones Com"); replace slashes with a hyphen; remove apostrophes without adding a space.

## Lines 4a to 6 — Addresses and location

| Line | Field | What goes here | Notes |
|---|---|---|---|
| 4a | Mailing address | Room, suite, street, or P.O. box for entity correspondence | If line 3 is completed, use the executor's, trustee's, or "care of" person's address. If applying only to obtain an EIN for Form 8832, use the address where the acceptance or nonacceptance letter should go. Generally used on all returns |
| 4b | City, state, ZIP (or foreign) | Foreign: city, province or state, postal code, full country name, not abbreviated | |
| 5a | Street address (if different) | Physical address; no P.O. box | Only if different from 4a |
| 5b | City, state, ZIP | Same foreign-address rules as 4b | |
| 6 | County and state where principal business is located | The entity's primary physical location | Instructions give no separate rule for entities located outside the U.S.; ask the user where the business is physically run |

The IRS allows 35 characters for street addresses online; use USPS standard abbreviations (Employer identification number page). Later address changes go on Form 8822-B.

## Lines 7a and 7b — Responsible party

| Line | Field | What goes here | Notes |
|---|---|---|---|
| 7a | Name of responsible party | Full name (first, middle initial, last) of the individual who ultimately owns or controls the entity or exercises ultimate effective control | Must be a natural person unless the applicant is a government entity. Not a nominee |
| 7b | SSN, ITIN, or EIN | SSN or ITIN of the 7a person. EIN only for a government entity applicant | If the person has no SSN or ITIN and is ineligible to obtain one, enter "foreign" or "N/A". An entry is required |

Full rules: [`responsible-party.md`](./responsible-party.md).

## Lines 8a to 8c — LLC information

| Line | Field | What goes here |
|---|---|---|
| 8a | Is this application for an LLC (or a foreign equivalent)? | Yes or No |
| 8b | Number of LLC members | If 8a is Yes. Spouses owning the LLC in a community property state who choose disregarded treatment enter "1" |
| 8c | Was the LLC organized in the United States? | If 8a is Yes. Yes or No |

## Line 9a — Type of entity (check only one box)

| Box | Use when | Write-in |
|---|---|---|
| Sole proprietor (SSN) | Schedule C or F filer with a qualified plan, or required to file excise, employment, alcohol, tobacco, or firearms returns, or a payer of gambling winnings | SSN or ITIN; nonresident alien with no effectively connected income enters "N/A" |
| Partnership | Partnership; domestic LLC with 2+ members keeping partnership classification; disregarded entity that gained an owner and became a partnership by default | — |
| Corporation | Any corporation other than a personal service corporation; LLC that will file Form 8832 (corporate) or Form 2553 (S corporation) | Income tax form number (1120, 1120-S, etc.). Single-member LLC electing: "Single-member" plus 1120 or 1120-S |
| Personal service corporation | Principal activity is personal services (accounting, actuarial science, architecture, consulting, engineering, health, law, performing arts) performed substantially by employee-owners who own at least 10% of the stock by FMV on the last day of the testing period | — |
| Church or church-controlled organization | Church | — |
| Other nonprofit organization (specify) | Nonprofit other than a church, including a nonprofit corporation | Type of nonprofit; 4-digit GEN if covered by a group exemption letter; section 527 organizations write "Section 527 organization" |
| Estate (SSN of decedent) | Estate | Decedent's SSN or ITIN |
| Plan administrator (TIN) | Plan administrator | Administrator's TIN if an individual |
| Trust (TIN of grantor) | Trust | Grantor's TIN |
| Military/National Guard, State/local government, Federal government, Indian tribal governments/enterprises | As named | — |
| Farmers' cooperative | As named | — |
| REMIC | Entity elected REMIC status | — |
| Other (specify) | Anything not listed, including disregarded entities, household employers, withholding agents, QSubs | Entity type and return to be filed; never "N/A" |

Disregarded-entity write-ins (Instructions, "Disregarded entities"):

| Purpose of the EIN | Box | Write-in |
|---|---|---|
| Employment or excise taxes, or non-federal purposes such as a state requirement | Other | "Disregarded entity" |
| Filing Form 5472 for a U.S. disregarded entity wholly owned by a foreign person | Other | "Foreign-owned U.S. disregarded entity-Form 5472" |
| Filing Form 8832 to elect corporate classification or Form 2553 to elect S status | Corporation | "Single-member" and form 1120 or 1120-S |
| Gained additional owners; now a partnership by default (Reg. 301.7701-3(f)) | Partnership | — |
| Foreign eligible entity filing Form 8832 to elect disregarded status | Other | "foreign disregarded entity" |

Other write-ins: "Household employer" with SSN; "Household employer agent" (also check State/local government if applicable); "QSub"; "Withholding agent"; "Created a pension plan" (with line 10 Created a pension plan). Line 9a is not a classification election (Instructions, Line 9a caution). If 1120-S is entered, Form 2553 must be filed no later than the 15th day of the 3rd month of the tax year the election takes effect; until received and approved, the entity is a Form 1120 filer.

## Line 9b — State or foreign country of incorporation

| Field | Rule |
|---|---|
| State / Foreign country | "If a corporation". No further instruction text. Ask the user for the state or country of organization when line 9a is Corporation |

## Line 10 — Reason for applying (check only one box)

| Box | Use when | Specify |
|---|---|---|
| Started new business | Starting a new business that requires an EIN. Not for adding a place of business to an existing EIN | Type of business |
| Hired employees | Existing business without an EIN now hiring. Not if it already has an EIN | Also see line 13 |
| Banking purpose | EIN needed for banking only | Purpose (e.g., investment club) |
| Changed type of organization | Sole proprietorship incorporated or became a partnership, and similar | "From ... to ..." |
| Purchased going business | Bought an existing business; don't use the seller's EIN unless you became owner of a corporation by acquiring its stock | — |
| Created a trust | Trust created | Type of trust; certain grantor trusts need no EIN |
| Created a pension plan | Plan needs an EIN for reporting | Type of plan; also check Other on 9a and write "Created a pension plan" |
| Compliance with IRS withholding regulations | Foreign person needing an EIN for withholding documentation | — |
| Other (specify) | Anything else. Foreign-owned U.S. disregarded entity: "Foreign-owned U.S. disregarded entity filing Form 5472". New state government entity: "Newly formed state government entity" | Reason |

"N/A" is not allowed on line 10.

## Lines 11 and 12 — Dates and tax year

| Line | Field | Rule |
|---|---|---|
| 11 | Date business started or acquired | New business: start date. Acquired operating business: acquisition date. Foreign applicants: date the business began or was acquired in the U.S. Change of ownership form: date the new entity began. Trusts: date funded (or date required to obtain an EIN under Reg. 301.6109-1(a)(2)). Estates: date of death or date legally funded |
| 12 | Closing month of accounting year | Last month of the tax year. Individuals: generally calendar year. Partnerships: majority-partner year, principal-partners year, least aggregate deferral, or other in certain cases. REMICs: calendar year. Personal service corporations: calendar year unless business purpose or section 444 election. Trusts: calendar year except tax-exempt, charitable, and grantor-owned trusts |

## Lines 13 to 15 — Employees

| Line | Field | Rule |
|---|---|---|
| 13 | Highest number of employees expected in next 12 months | Each box (Agricultural, Household, Other), including -0-. If none expected, skip line 14 |
| 14 | Form 944 election box | Check only if employment tax liability is expected to be $1,000 or less in a full calendar year. Generally true if total wages subject to social security, Medicare, and federal income tax withholding are $5,000 or less; $6,536 or less in wages for employers in U.S. territories. If not checked, file Form 941 every quarter. Once checked, keep filing Form 944 until the IRS instructs otherwise |
| 15 | First date wages or annuities were paid | Date payroll began. Foreign applicants: date wages began in the U.S. Withholding agents: date income (including annuities) is first paid to a nonresident alien (also individuals filing Form 1042 for alimony to a nonresident alien). "N/A" if no employees planned |

Employers must make electronic deposits of depository taxes using EFTPS (Instructions, Line 10 caution).

## Lines 16 to 18 — Activity and prior EIN

| Line | Field | Rule |
|---|---|---|
| 16 | Principal activity (one box) | Construction; Real estate; Rental & leasing (also equity REITs); Manufacturing; Transportation & warehousing; Finance & insurance; Health care & social assistance; Accommodation & food service; Wholesale—agent/broker; Wholesale—other; Retail; Other (specify). Mortgage REITs check Real estate. A box is required |
| 17 | Principal line of merchandise, construction work, products, or services | Required. More detail than line 16, e.g., "General contractor for residential buildings". REITs: mortgage REIT, or the property type for equity REITs |
| 18 | Has the applicant entity ever applied for and received an EIN? | Yes or No; if Yes, write the previous EIN |

## Third Party Designee

| Field | Rule |
|---|---|
| Designee's name, address and ZIP, telephone, fax | Complete only if the applicant authorizes this individual to receive the EIN and answer questions about the form |
| Validity | The signature area must be completed for the authorization to be valid |
| Duration | Authority ends when the EIN is assigned and released to the designee |
| Delivery | EIN released to the designee by the method used (online, telephone, or fax); the EIN notice is mailed to the taxpayer |
| Same contact details | If the designee's address or telephone number matches the taxpayer's, the application must be mailed or faxed |

## Signature block

| Applicant | Who signs |
|---|---|
| Individual | The individual |
| Corporation | President, vice president, or other principal officer |
| Partnership, government entity, or other unincorporated organization | A responsible and duly authorized member or officer with knowledge of its affairs |
| Trust or estate | The fiduciary |
| Foreign applicant | Any duly authorized person (for example, a division manager) |

Also enter name and title, applicant's telephone (and fax if faxing), and date. The declaration is under penalties of perjury.
