# Example: U.S. Owner, Single-Member LLC That Stays Disregarded (Online)

A U.S. resident forms a one-member LLC, keeps the default disregarded classification, and needs an EIN because the bank will not open the LLC's account without one. This is the most common SS-4 and the one most often filed with the wrong line 9a box.

## The applicant

- **Owner:** Renata A. Okafor, U.S. citizen with an SSN, lives in Columbus, Ohio
- **Entity:** Okafor Studio LLC, organized with the Ohio Secretary of State, effective Monday, September 14, 2026
- **Business:** brand identity and packaging design for food and beverage companies, run from her home studio
- **Employees:** none planned in the next 12 months
- **Classification plan:** default (disregarded); no Form 8832 or Form 2553 planned. The agent asked and Renata confirmed she discussed this with her accountant
- **Why an EIN:** her bank requires an EIN in the LLC's name to open the business account. She has never had a sole proprietor EIN
- **Application date:** Wednesday, September 16, 2026, about 10:30 a.m. Eastern

## Inputs gathered (Prerequisites)

| Input | Answer |
|---|---|
| Legal name on the Ohio articles | Okafor Studio LLC |
| Trade name | None |
| Mailing address | 1187 Neil Ave, Apt 3, Columbus, OH 43201 |
| Physical location | Same; Franklin County, Ohio |
| Responsible party | Renata A. Okafor (sole member; controls all funds) |
| Responsible party has SSN or ITIN? | Yes, SSN (collected only at submission) |
| Members | 1, organized in the U.S. |
| Prior EIN for this entity | No |
| Accounting year | Calendar year |
| Third party designee | None |

## Decisions

1. **Is an EIN needed?** A single-member LLC needs an EIN for employment or excise returns, state reporting, Form 8832, or Form 5472 (Form SS-4, page 2). Renata has none of those yet, but the bank requires one. The instructions treat "non-federal purposes such as a state requirement" as a reason a disregarded entity applies (Instructions, Disregarded entities). The agent tells her that, as of today, she has no federal filing that requires it, and she confirms she still wants it for the bank.
2. **Responsible party:** Renata is the only member and controls the funds. No nominee was used.
3. **Line 9a:** single-member, domestic, staying disregarded, EIN for a non-federal purpose → **Other**, "Disregarded entity" (Instructions, Lines 8a–8c TIP and Disregarded entities). Not "Sole proprietor".
4. **Line 10:** she is starting an operating business, so **Started new business** fits better than **Banking purpose**, which the instructions reserve for an EIN requested "for banking purposes only" (examples given: a bowling league, an investment club).
5. **Channel:** domestic organization, principal place of business in Ohio, responsible party has an SSN, not applying with an EIN → **online** (Get an EIN page). Wednesday 10:30 a.m. is within the Monday to Friday 6:00 a.m. to 1:00 a.m. Eastern window.

## The completed draft

```markdown
# Form SS-4 — DRAFT (Rev. December 2025)

## Applicant summary
- Entity: Okafor Studio LLC, single-member LLC, organized in Ohio on 09/14/2026
- Federal classification plan: default, disregarded entity (no Form 8832 or 2553)
- Channel: Online (IRS Get an EIN page)

## Lines
1.  Legal name:                         Okafor Studio LLC
2.  Trade name:                         N/A
3.  Executor/trustee/"care of":         N/A
4a. Mailing address:                    1187 Neil Ave, Apt 3
4b. City, state, ZIP:                   Columbus, OH 43201
5a. Street address (if different):      N/A
5b. City, state, ZIP:                   N/A
6.  County and state:                   Franklin County, Ohio
7a. Responsible party:                  Renata A. Okafor
7b. SSN/ITIN/EIN:                       [collected at submission]
8a. LLC?                                Yes
8b. Number of members:                  1
8c. Organized in the U.S.?              Yes
9a. Entity type:                        Other — "Disregarded entity"
9b. State/foreign country:              N/A (not a corporation)
10. Reason:                             Started new business — "Graphic design studio"
11. Date started/acquired:              09/14/2026
12. Closing month:                      December
13. Employees expected:                 Agricultural 0  Household 0  Other 0
14. Form 944 box:                       Skipped (no employees)
15. First wages date:                   N/A
16. Principal activity:                 Other — "Graphic design services"
17. Principal line of business:         Brand identity and packaging design for food and beverage companies
18. Prior EIN?                          No
Third party designee:                   None
Signature:                              Renata A. Okafor, Member, phone (614) 555-0136, 09/16/2026

## Validation summary
- Completeness: all checks passed
- Channel: online eligible (domestic LLC, Ohio principal place of business, responsible party has SSN)
- Warnings: EIN requested for a non-federal (banking) purpose; no federal return currently requires it

## Next steps
- Save the EIN confirmation letter at the end of the online session
- EIN usable immediately for the bank account; allow up to 2 weeks (to 09/30/2026) before using it to e-file or pay electronically
- LLC income stays on Renata's Form 1040, Schedule C (see ../../schedule-c/SKILL.md)
- If she hires, the LLC must use its own name and EIN for employment taxes (see ../../form-941/SKILL.md)
- Report any later change of address or responsible party on Form 8822-B within 60 days

## Sources cited in this draft
- Form SS-4 (Rev. December 2025); Instructions for Form SS-4 (Rev. December 2025): Lines 7a–7b, 8a–8c, 9a, Disregarded entities, Line 10
- IRS Get an EIN page (reviewed 19-Aug-2026); Employer identification number page (reviewed 17-Jul-2026)
```

## Why each non-obvious choice

**Why "Other — Disregarded entity" and not "Sole proprietor"?** The instructions say a single-member LLC classified as a disregarded entity checks Other and writes "disregarded entity". The Sole proprietor box is for an individual filing Schedule C or F who needs an EIN for a qualified plan, excise, employment, or ATF returns, or gambling payouts. The LLC, not Renata personally, is the applicant here.

**Why line 8b = 1 when the IRS already treats the LLC as disregarded?** Line 8b reports members, and the disregarded status follows from one member plus no election. Lines 8b and 9a must agree.

**Why lines 14 and 15 are skipped or N/A?** Line 13 shows zero employees, and the instructions say to skip line 14 when no employees are expected and to enter N/A on line 15 if the business doesn't plan to have employees.

**Why Started new business on line 10?** Only one box is allowed, and the business is new. "Banking purpose" is for an EIN requested for banking only, for example an investment club.

**Date checks (Python):** September 14, 2026 is a Monday and September 16, 2026 a Wednesday; September 16 plus 14 days is September 30, 2026.
