# Example: Multi-Member LLC Taxed as a Partnership (Form 1065, code 09)

A calendar-year partnership with no entity-level tax. Lines 6 to 8 are zero; the judgment is in the code, the deadline, the paper address, the partner count, and telling the members to extend their own returns.

## The filer

- **Entity**: Harbor & Pine Studio LLC, an Oregon LLC with default partnership classification
- **Return**: Form 1065 for calendar year 2026
- **Members during 2026**: 4 persons. Three current members; a fourth member was redeemed out on June 30, 2026.
- **Name on the 2025 Form 1065**: Harbor & Pine Studio LLC
- **Principal business location**: Portland, Oregon
- **Total assets at the end of 2026**: $412,860
- **Foreign partners**: none (so no Form 8804 and no second Form 7004)
- **Books kept**: in the United States (so line 4 does not apply)
- **Filing channel the user picked**: paper, because their bookkeeper does not e-file extensions
- **Date of drafting**: February 26, 2027

## Questions the agent asked, and the answers

| Question | Answer | Effect |
|---|---|---|
| Is the LLC taxed as a partnership, or did it elect S or C corporation status? | Partnership; no Form 8832 or 2553 ever filed | Code 09 |
| Will the 2026 Form 1065 show look-back interest, an imputed underpayment, or other taxes on lines 24 to 27? | No | Line 6 = -0- |
| Any partner who is a nonresident alien or foreign entity? | No | No Form 8804 / code 31 application |
| Were the partnership's books and records kept outside the U.S. and Puerto Rico? | No | Line 4 unchecked |
| Is the tax year 12 months? | Yes | Line 5b blank |
| Did the LLC's name change since the 2025 return? | No | Use current name |

## Deadlines

- Original due date: 15th day of the 3rd month after December 31, 2026 = Monday, March 15, 2027 (IRC §6072(b); 2025 Instructions for Form 1065, When To File). This is the Form 7004 deadline.
- Extended due date: 6 months = Wednesday, September 15, 2027 (i7004; Treas. Reg. §1.6081-2(a)). Schedules K-1 are due to partners by the day the return is required to be filed "(determined with regard to extensions)" (Treas. Reg. §1.6031(b)-1T(b)), so the extension moves them too.

## Where to mail

Oregon is in the western state group. For Form 1065 filers in those states, i7004 gives one address regardless of total assets:

```
Department of the Treasury
Internal Revenue Service
Ogden, UT 84201-0045
```

The $10 million asset test only splits the Kansas City state group. Mail by USPS Certified Mail or an IRS-designated private delivery service so the postmark or PDS record proves the date (IRC §7502). Note the i7004 caution: if the return will later be e-filed, a paper Form 7004 may not be processed before the return, which can trigger a penalty notice. The agent tells the user to keep the mailing receipt.

## The completed Form 7004 draft

```markdown
# Form 7004 — DRAFT for Harbor & Pine Studio LLC (tax year 2026)

## Filing summary
- Return extended: Form 1065 (code 09)
- Tax year: calendar year 2026
- Form 7004 due: Monday, March 15, 2027 (postmark)
- Extended return and K-1s due: Wednesday, September 15, 2027
- Channel: paper, USPS Certified Mail
- Mail to: Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045
- Payment due with this form: $0

## Identification
Name: Harbor & Pine Studio LLC  (matches 2025 Form 1065)
Identifying number: 9X-XXXXXXX
Address: <street>, Portland, OR <ZIP>

## Part I
1. Form code: 09

## Part II
2. Foreign corporation without U.S. office: ☐
3. Common parent of consolidated group: ☐
4. Qualifies under Reg. §1.6081-5: ☐
5a. Calendar year 2026 (entry after the preprinted "20": 26)
5b. Short tax year: N/A
6. Tentative total tax:            -0-
7. Total payments and credits:     -0-
8. Balance due:                    -0-
```

No signature is required (i7004).

## The penalty the extension prevents

If the LLC filed no Form 7004 and filed its 2026 Form 1065 on August 20, 2027:

```
Months or part of a month after March 15, 2027:
  Mar 16–Apr 15, Apr 16–May 15, May 16–Jun 15, Jun 16–Jul 15, Jul 16–Aug 15, Aug 16–Aug 20  = 6
Persons who were partners at any time in 2026                                           = 4
Amount for returns required to be filed in 2027 (Rev. Proc. 2025-32 §4.55)              = $260
Penalty: 4 × 6 × $260                                                                   = $6,240
Cap at 12 months: 4 × 12 × $260                                                         = $12,480
```

The redeemed member counts. The 2025 Instructions for Form 1065 multiply by "the total number of persons who were partners in the partnership during any part of the partnership's tax year." Separate per-K-1 penalties for late Schedules K-1 can also apply (IRC §6722); they are outside this skill.

## Handoff to the members

The partnership extension does not extend any member's Form 1040 or the time to pay a member's tax (Treas. Reg. §1.6081-2(e)). The agent tells the user:

- Each of the 4 persons who will get a 2026 K-1 and expects it after April 15, 2027 files Form 4868 by Thursday, April 15, 2027 and pays an estimate of their own tax with it (see [`form-1040`](../../form-1040/SKILL.md)).
- Calendar September 15, 2027 for the Form 1065 and all K-1s, including the redeemed member's final K-1.

## Why each non-obvious choice

**Why code 09 and not 12?** The LLC files Form 1065 under its default classification. Code 12 would extend a Form 1120 it does not file (i7004: the extension applies "only to the specific return identified on Part I, line 1").

**Why -0- and not blank?** i7004, Line 6: "If you expect this amount to be zero, enter -0-."

**Why not line 4?** Line 4 covers partnerships that keep books and records outside the United States and Puerto Rico (Treas. Reg. §1.6081-5(a)(1)). This LLC does not.

## Sources cited in this example

- Form 7004 (Rev. December 2025) and Instructions for Form 7004 (Rev. December 2025): line 1 codes, line 6 "-0-", Where To File, paper/e-file caution, no signature
- 2025 Instructions for Form 1065: When To File; Late Filing of Return
- IRC §6072(b), §6698, §7502
- Treas. Reg. §1.6081-2(a), (e); §1.6081-5(a)(1); §1.6031(b)-1T(b)
- Rev. Proc. 2025-32 §4.55 ($260 for returns required to be filed in 2027)
