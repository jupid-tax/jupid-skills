# Timing Rules for Form 2553

The deadline math is the #1 source of voided elections. This file decomposes every timing scenario, with the explicit calculations, plus the late-relief mechanics under Rev. Proc. 2013-30.

---

## The core deadline rule (IRC §1362(b))

Form 2553 must be filed **either**:

- **No more than 2 months and 15 days after the start of the tax year** in which the election is to take effect, OR
- **Any time during the tax year preceding** the election year

For calendar-year filers: 2 months and 15 days from January 1 lands on **March 15**. March 15, 2026 was a Sunday, so a calendar-2026 election was due **Monday, March 16, 2026** (IRC §7503).

The IRS treats "2 months and 15 days" as date arithmetic, *not* as 75 days. Rule (Instructions for Form 2553, "When To Make the Election"): the 2-month period begins on the day the tax year begins and ends with the close of the day **before** the numerically corresponding day of the second calendar month following; if there is no corresponding day, it ends on the last day of that month. Then add 15 days. The instructions' own examples: January 7 → March 21; November 8 → January 22.

| Tax year start | 2-month period ends | Deadline |
|----------------|---------------------|----------|
| January 1 | February 28 | March 15 |
| January 7 | March 6 | March 21 |
| February 1 | March 31 | April 15 |
| March 1 | April 30 | May 15 |
| April 1 | May 31 | June 15 |
| July 1 | August 31 | September 15 |
| October 1 | November 30 | December 15 |

If the deadline falls on a Saturday, Sunday, or legal holiday, it shifts to the next business day (IRC §7503). Do not plan on the shift: file earlier.

---

## Decision tree: when does the clock start?

```
Is the election meant to start with the entity's FIRST tax year in existence?

  NO → Existing-entity case.
    The deadline is 2 months 15 days from the start of the tax year for which
    the election is to take effect.
    Example: calendar-year LLC operating since 2023 wants S-corp for 2026.
             Deadline = March 15, 2026.

  YES → New-entity case.
    The first tax year begins on the EARLIEST of (Reg. §1.1362-6(a)(2)(ii)(C);
    Instructions, "Item E"):
      (a) the date the entity first had shareholders/members
      (b) the date the entity first had assets
      (c) the date the entity began doing business
    The deadline is 2 months 15 days after that date. An election filed
    before that date is not valid, because the entity has no prior tax year.

    ASK about each event; any one can start the clock:
      - members admitted / stock issued
      - money deposited in an entity bank account, or any property contributed
      - first contract, sale, hire, or lease
    The state filing date (articles accepted) is item B, not automatically
    item E; the clock starts at the FIRST of (a)-(c).
```

### Worked example — new entity

```
ABC Consulting, LLC
  03/01/2026 — Articles of organization accepted by Delaware
  03/01/2026 — Single member admitted (Event A: shareholders)
  03/05/2026 — LLC opens business bank account (Event C: began doing business)
  03/10/2026 — LLC signs first client contract (Event C confirmed)

  Earliest event: 03/01/2026 (Event A)
  2-month period ends: 04/30/2026
  Deadline: 04/30/2026 + 15 days = 05/15/2026 (a Friday)

  To be an S-corp from 03/01/2026, Form 2553 must be filed by 05/15/2026.
```

### Worked example — existing entity

```
XYZ Software, Inc.
  Incorporated in California on 06/15/2022
  Operating as C-corp 2022-2025
  Wants to elect S-corp starting 2026

  Calendar year, so 2026 starts 01/01/2026.
  Deadline: 01/01/2026 + 2 months 15 days = 03/15/2026, a Sunday,
            so 03/16/2026 under IRC §7503.

  Form 2553 must be filed by 03/16/2026 to be effective for tax year 2026.
  (Could also have filed any time during 2025.)
```

---

## What if the deadline is missed?

If the form is filed after the deadline, the election generally is effective for the **following** tax year (Instructions, "Relief for a Late S Corporation Election Filed by a Corporation"), UNLESS the filer qualifies for late-election relief under Rev. Proc. 2013-30. The standard is reasonable cause plus diligent action once the mistake was found (§4.02(4)).

---

## Rev. Proc. 2013-30 — late-election relief mechanics

Rev. Proc. 2013-30, 2013-36 I.R.B. 173 (effective September 3, 2013) modifies and supersedes Rev. Procs. 2003-43, 2004-48, and 2007-62, supersedes Situation 1 and obsoletes Situation 2 of Rev. Proc. 97-48, and replaces sections 4.01-4.03 of Rev. Proc. 2004-49 (§9). It provides relief without a letter ruling for late S elections that missed the §1362(b) deadline.

### Eligibility — all must be true

1. **Entity intended to be classified as an S-corp** as of the intended effective date (item E) (§4.02(1))
2. **Failure to qualify was solely because the election was not timely filed**: the only defect is lateness, not eligibility (§4.02(3))
3. **Reasonable cause** for the late filing, and the entity **acted diligently** to correct the mistake once discovered (§4.02(4))
4. **Request made within 3 years and 75 days** of the intended effective date (§4.02(2)). Exception: a corporation (not seeking classification relief) that filed every return as an S corporation, whose first Form 1120-S was filed at least 6 months ago with no IRS notice of a problem within 6 months, can file later (§5.04)
5. **Consistent reporting:** every person who was a shareholder from the effective date to the filing date states they reported income consistently with S status for every affected year (§5.02; the column K consent text covers this). An LLC that also needs classification relief must make Part IV representation 5: all required returns timely filed consistent with S status and no inconsistent returns (5a), or no return yet filed for the first year because its due date has not passed (5b) (§5.03(5))

### The 3-year-75-day window

```
Intended effective date: 01/01/2024
Window opens:            01/01/2024
Window closes:           01/01/2024 + 3 years 75 days
                       = 01/01/2027 + 75 days
                       = 03/17/2027

Form 2553 with Rev. Proc. 2013-30 relief can be filed any time between
01/01/2024 and 03/17/2027.
```

If the user is past 3 years 75 days (and §5.04 does not apply), Rev. Proc. 2013-30 is unavailable. The remaining option is a letter ruling under §1362(b)(5) (with Reg. §301.9100-3 for a late classification election). User fee under Rev. Proc. 2026-1, Appendix A (A)(3)(c)(i): $14,500, reduced to $3,450 for gross income under $400,000 or $9,775 for gross income under $10 million (A)(4); plus professional fees. Outside the scope of this skill. Refer to a CPA or tax attorney.

### Mechanics of filing late under Rev. Proc. 2013-30

1. Complete Form 2553 normally (Part I, Part II if applicable, Part III if QSST)
2. **In the top margin of page 1**, write or print: **"FILED PURSUANT TO REV. PROC. 2013-30"** (§4.03(1))
3. **Item I**: state the reasonable cause and the diligent actions, or attach a statement that does so and carries the §4.03(3) penalties-of-perjury declaration, signed by an authorized officer
4. **Column K**: consents from everyone who was a shareholder at any time from the item E date to the filing date (§5.01)
5. **Part IV**: only if the entity is an eligible entity (LLC) without a timely Form 8832; all five representations must be true (§5.03)
6. File by one of the three routes in §4.03(2): (a) attach to the current-year Form 1120-S if all Forms 1120-S since the effective date have been filed; (b) attach to the late-filed Form 1120-S for the year including the effective date, with all other delinquent Forms 1120-S filed at the same time; or (c) send Form 2553 directly to the service center. Routes (a) and (b): write "INCLUDES LATE ELECTION(S) FILED PURSUANT TO REV. PROC. 2013-30" at the top of the Form 1120-S. All routes must be completed within 3 years 75 days; extending the 1120-S does not extend that window

### Acceptable reasonable-cause language

The IRS has historically accepted these patterns:

> "The entity owners were unaware of the requirement to file Form 2553 within 2 months and 15 days of the intended effective date. Upon learning of the requirement on [date], owners promptly engaged a tax professional and prepared this election."

> "The entity's prior accountant agreed to prepare and file Form 2553 but failed to do so before disengaging in [month/year]. The owner discovered the failure on [date] when reviewing tax records and is filing this election immediately upon discovery."

> "The entity owner believed (incorrectly) that filing the LLC operating agreement designating S-corp tax treatment automatically triggered the federal election. Upon being advised by a CPA on [date] that a separate Form 2553 filing was required, the owner is filing this form."

### Unacceptable reasonable-cause language

These do not show reasonable cause and risk a CP264 notice (Form 2553 denied):

- "We wanted to wait and see how the year went before electing." (willful, not inadvertent)
- "We elected at our convenience." (no cause)
- "We were too busy to file." (insufficient diligence)

The reasonable-cause statement should be **2-4 sentences**, factual, dated, and signed by an authorized officer under the §4.03(3) penalties-of-perjury declaration.

### Consistent-treatment requirement

Every late election needs the §5.02 statements (all shareholders reported consistently with S status); an LLC relying on the deemed classification election also needs Part IV representation 5. ASK which returns have already been filed for each year from the item E date, then:

| Entity status | Result |
|---------------|--------|
| No return of any kind filed yet for the first intended S year, and its due date has not passed | LLC: Part IV representation 5b can be made. Corporation: no Part IV; shareholders' column K consents carry the §5.02 statement |
| LLC; every return since the effective date was a timely Form 1120-S and no inconsistent return was filed | Part IV representation 5a can be made |
| LLC; the owner already reported an intended S year on Schedule C, or the LLC filed Form 1065 for it | Representation 5a cannot be made as written ("no inconsistent tax or information returns ... filed by or with respect to the entity"). Stop: refer to a CPA (a letter ruling may be required) |
| LLC; first-year Form 1120-S due date passed with no return filed | Neither 5a nor 5b is true. Stop: refer to a CPA |
| Corporation that filed Form 1120 (C-corp) for an intended S year | No Part IV; shareholders must be able to give the §5.02 statement. How to replace the filed Form 1120 is a CPA question: refer |

The easiest path, when it is still open: file Form 2553 under Rev. Proc. 2013-30 BEFORE any return for the first intended S year is due or filed, then file Form 1120-S on time.

---

## Special timing case: Form 8832 already filed

If an LLC already elected corporate classification on Form 8832, it is a corporation for Form 2553 purposes and needs no deemed classification election (and no Part IV). If the S election is meant to start on the Form 8832 effective date (its first tax year as a corporation), use the new-entity deadline counted from that date; if it starts in a later year, use the existing-entity window for that year.

For LLCs going **directly** to S-corp without Form 8832, a timely Form 2553 is itself the deemed election to be classified as a corporation (Reg. §301.7701-3(c)(1)(v)(C); Rev. Proc. 2013-30 §4.01(1); Form 2553 instructions, "Purpose of Form"). For a new LLC, item E can be its first day (earliest of members, assets, or business).

---

## §444 election (fiscal year)

If the entity wants a non-calendar tax year that isn't a natural business year or ownership tax year, it can elect under §444 a year with a deferral period of no more than 3 months (Form 1120-S instructions, "Electing a tax year under section 444") by making the **required payment** under IRC §7519. Mechanics:

1. Check item F box (2) (fiscal year ending month/day) on Form 2553
2. Complete Part II: item O, then R1 (or Q1 with a Q2 back-up §444 election)
3. File **Form 8716** (Election To Have a Tax Year Other Than a Required Tax Year), attached or separately
4. Compute and pay the required payment annually on Form 8752

Most small entities should not elect §444: the required payment offsets most of the deferral, and the compliance overhead is significant. Default to calendar year.

---

## Quick reference: timing decision matrix

```
| Scenario                                         | Filing window                              | Relief?                   |
|--------------------------------------------------|--------------------------------------------|---------------------------|
| Calendar-year existing entity, 2026 election     | 1/1/2025 - 3/16/2026 (3/15 was a Sunday)   | None needed               |
| Calendar-year, missed 3/16/2026                  | After 3/16/2026, by 3/17/2029              | Rev. Proc. 2013-30        |
| New entity, first event 3/1/2026                 | 3/1/2026 - 5/15/2026                       | None needed               |
| New entity, first event 3/1/2026, missed 5/15    | 5/16/2026 - 5/15/2029                      | Rev. Proc. 2013-30        |
| Calendar-year, missed by >3 years 75 days        | After 3/17/2029 (for 1/1/2026 effective)   | §1362(b)(5) letter ruling, unless §5.04 applies |
```

## Cross-references

- Form mechanics: [`line-by-line.md`](./line-by-line.md)
- Eligibility: [`eligibility.md`](./eligibility.md)
- Common timing mistakes: [`common-mistakes.md`](./common-mistakes.md)
- Filing channel and CP261 follow-up: [`../filing.md`](../filing.md)
- Authority sources: IRC §1362(b) and (b)(5), IRC §7503, Reg. §1.1362-6(a)(2)(ii)(C), Rev. Proc. 2013-30, Rev. Proc. 2006-46 (natural business year), Rev. Proc. 2026-1 (user fees), Reg. §301.9100-3
