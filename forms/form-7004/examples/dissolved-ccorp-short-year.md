# Example: Dissolved C Corporation, Short Final Year (Form 1120, code 12, line 5a/5b)

A C corporation that dissolved mid-year and needs time for its final return. The hard parts are the due date for a dissolved corporation, the short-year boxes on lines 5a and 5b, and the Kansas City address with the asset test.

## The filer

- **Entity**: Larkspur Analytics Corp., a Massachusetts corporation, principal office in Worcester, Massachusetts
- **Return**: final Form 1120 for the short tax year January 1, 2026 to July 22, 2026
- **Dissolution**: articles of dissolution effective July 22, 2026
- **Name on the 2025 Form 1120**: Larkspur Analytics Corp.
- **Total assets at the end of the short year**: $38,415 (cash held for final expenses)
- **Filing channel**: the user's preparer will e-file the final return in spring 2027, so the agent recommends e-filing Form 7004 too; the user wants a paper fallback address in the draft
- **Date of drafting**: October 6, 2026

## Questions the agent asked, and the answers

| Question | Answer | Effect |
|---|---|---|
| On what date did the corporation dissolve? | July 22, 2026 | Due date runs from this date |
| Is the year short because the corporation stopped existing, or because of a change in accounting period? | Stopped existing | Line 5b "Final return"; no Form 1128 question |
| Is the corporation part of a consolidated group or a controlled group? | No | Line 3 unchecked; one Form 7004 |
| Projected taxable income for January 1 to July 22, 2026? | $41,973 | Line 6 |
| Credits or other Schedule J taxes? | None | Line 6 = income tax only |
| Estimated tax payments for 2026? | $2,350 on April 15 and $2,350 on June 15, 2026 | Line 7 = $4,700 |
| Prior-year overpayment credited? | None | — |

## Deadlines

- Original due date: "A corporation that has dissolved must generally file by the 15th day of the 4th month after the date it dissolved" (2025 Instructions for Form 1120, When To File). Four months after July 2026 is November 2026; November 15, 2026 is a Sunday, so the deadline is **Monday, November 16, 2026** (IRC §7503).
- Extension length: 6 months. The short year ends July 22, not in June, so the 7-month June 30 rule does not apply (i7004, Extension Period, Note).
- Extended due date: 6 months after the statutory date November 15, 2026 = May 15, 2027, a Saturday, so **Monday, May 17, 2027** (Treas. Reg. §1.6081-3(a); IRC §7503).
- e-file timing: the IRS will not accept an e-filed Form 7004 "filed before end of tax period" (https://www.irs.gov/Efile7004). The short period ended July 22, 2026, so e-filing in October 2026 is allowed.

## Line 6, step by step

```
Income tax: $41,973 × 21%          = $8,814.33     (IRC §11(b))
Credits                            −     $0.00
Tentative total tax                = $8,814.33
Rounded                            = $8,814        (i7004, Rounding)
```

The short year here comes from the corporation ceasing to exist, not from a change in annual accounting period, so the annualization rule of IRC §443(b), which applies to a short period caused by a change in accounting period, is not used. If the user's preparer disagrees on the facts, stop and ask.

## Lines 7 and 8

```
Line 7: $2,350 + $2,350             = $4,700
Line 8: $8,814 − $4,700             = $4,114   pay by Monday, November 16, 2026
```

## Paper fallback address

Massachusetts is in the Kansas City state group. For Form 1120 in that group, i7004 splits by total assets at the end of the tax year:

- Less than $10 million → Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0019
- $10 million or more → Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045

Total assets of $38,415 → **Kansas City, MO 64999-0019**.

## The completed Form 7004 draft

```markdown
# Form 7004 — DRAFT for Larkspur Analytics Corp. (short final year 2026)

## Filing summary
- Return extended: Form 1120 (code 12), final return
- Tax year: January 1, 2026 to July 22, 2026 (short year)
- Form 7004 due: Monday, November 16, 2026
- Extended return due: Monday, May 17, 2027
- Channel: e-file (MeF) recommended; paper fallback: Department of the Treasury,
  Internal Revenue Service, Kansas City, MO 64999-0019
- Payment due with this form: $4,114 by November 16, 2026 (EFTPS or EFW)

## Identification
Name: Larkspur Analytics Corp.  (matches 2025 Form 1120)
Identifying number: 0X-XXXXXXX
Address: <street>, Worcester, MA <ZIP>

## Part I
1. Form code: 12

## Part II
2. Foreign corporation without U.S. office: ☐
3. Common parent of consolidated group: ☐
4. Qualifies under Reg. §1.6081-5: ☐
5a. Tax year beginning 01/01, 2026, and ending 07/22, 2026
5b. Short tax year: ☒ Final return
6. Tentative total tax:                 $8,814
7. Total payments and credits:          $4,700
8. Balance due:                         $4,114
```

## Validation the agent ran

- Line 8 = $8,814 − $4,700 = $4,114 ✔
- Line 5a dates span less than 12 months and line 5b has exactly one box checked ✔
- Filing date (October 2026) is before the November 16, 2026 deadline and after the short period ended ✔
- Paper address chosen from the Kansas City state group with the asset test applied ✔
- Mailing address: if the corporation's address changes after dissolution (for example, to an officer's address), Form 7004 does not update IRS records; Form 8822-B does (i7004, Address) ✔ flagged to the user

## Why each non-obvious choice

**Why November and not April?** A calendar-year corporation that stays in existence files by April 15. A dissolved corporation's final return is due the 15th day of the 4th month after the date it dissolved (2025 Instructions for Form 1120).

**Why "Final return" and not "Other"?** Line 5b lists "Final return" as its own reason. "Other" requires an attached explanation (i7004, Line 5a, Periods and Methods).

**Why compute the extended date from November 15, not November 16?** The regulation grants the 6 months "after the date prescribed for filing the return" (Treas. Reg. §1.6081-3(a)); §7503 only makes a next-business-day filing timely.

## Sources cited in this example

- Form 7004 (Rev. December 2025) and Instructions for Form 7004 (Rev. December 2025): lines 5a, 5b, 6 to 8, Rounding, Where To File, Address
- 2025 Instructions for Form 1120, When To File (dissolved corporations)
- IRS e-file page for Form 7004 (https://www.irs.gov/Efile7004): early-filed applications
- IRC §11(b), §443(b), §7503
- Treas. Reg. §1.6081-3(a)
