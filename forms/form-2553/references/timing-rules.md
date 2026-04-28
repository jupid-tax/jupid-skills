# Timing Rules for Form 2553

The deadline math is the #1 source of voided elections. This file decomposes every timing scenario, with the explicit calculations, plus the late-relief mechanics under Rev. Proc. 2013-30.

---

## The core deadline rule (IRC §1362(b))

Form 2553 must be filed **either**:

- **No more than 2 months and 15 days after the start of the tax year** in which the election is to take effect, OR
- **Any time during the tax year preceding** the election year

For calendar-year filers: 2 months and 15 days from January 1 lands on **March 15**. To be an S-corp for tax year 2026, Form 2553 must be filed (faxed or postmarked) on or before **March 15, 2026**.

The IRS treats "2 months and 15 days" as date arithmetic — *not* as 75 days. So:

| Tax year start | Deadline |
|----------------|----------|
| January 1 | March 15 |
| February 1 | April 16 (Feb 1 + 2 months = April 1; + 15 days = April 16) |
| April 1 | June 16 |
| July 1 | September 15 |
| October 1 | December 16 |

If the deadline falls on a weekend or federal holiday, the deadline shifts to the next business day (per IRC §7503).

---

## Decision tree: when does the clock start?

```
Has the entity ever filed a U.S. federal tax return as an entity (not Schedule C
on the owner's 1040)?

  YES → Existing-entity case.
    The deadline is 2 months 15 days from the start of the tax year for which
    the election is to take effect.
    Example: calendar-year LLC operating since 2023 wants S-corp for 2026.
             Deadline = March 15, 2026.

  NO → New-entity case.
    The deadline is 2 months 15 days from the EARLIEST of:
      (a) the date the entity first had shareholders/members
      (b) the date the entity first acquired assets
      (c) the date the entity first began doing business

    "Began doing business" is interpreted broadly:
      - opened a bank account in the entity's name
      - hired an employee
      - signed a lease or vendor contract
      - accepted any payment
      - filed a state tax return
    The IRS does NOT use the date of state filing (articles of incorporation /
    organization) as the trigger if business activity started later. The clock
    starts at the FIRST operational event.
```

### Worked example — new entity

```
ABC Consulting, LLC
  03/01/2026 — Articles of organization accepted by Delaware
  03/01/2026 — Single member admitted (Event A: shareholders)
  03/05/2026 — LLC opens business bank account (Event C: began doing business)
  03/10/2026 — LLC signs first client contract (Event C confirmed)

  Earliest event: 03/01/2026 (Event A)
  Deadline: 03/01/2026 + 2 months 15 days = 05/16/2026

  To be an S-corp for tax year 2026, Form 2553 must be filed by 05/16/2026.
```

### Worked example — existing entity

```
XYZ Software, Inc.
  Incorporated in California on 06/15/2022
  Operating as C-corp 2022-2025
  Wants to elect S-corp starting 2026

  Calendar year, so 2026 starts 01/01/2026.
  Deadline: 01/01/2026 + 2 months 15 days = 03/15/2026.

  Form 2553 must be filed by 03/15/2026 to be effective for tax year 2026.
  (Could also have filed any time during 2025.)
```

---

## What if the deadline is missed?

If the form is filed after the deadline, the IRS treats the election as effective for the **following** tax year — UNLESS the filer qualifies for late-election relief under Rev. Proc. 2013-30.

The good news: Rev. Proc. 2013-30 grants relief generously for filers who acted in good faith. The bar is "reasonable cause," not "extraordinary circumstances."

---

## Rev. Proc. 2013-30 — late-election relief mechanics

Rev. Proc. 2013-30 (effective September 3, 2013, supersedes Rev. Proc. 2003-43, 2007-62, 2004-48, 97-48) provides simplified relief for late S-corp elections that would otherwise miss the §1362(b) deadline.

### Eligibility — all five must be true

1. **Entity intended to be classified as an S-corp** as of the intended effective date (Line F)
2. **Entity failed to qualify as an S-corp solely because the election was not timely filed** — i.e., the only defect is the lateness, not eligibility
3. **Entity has reasonable cause** for the late filing
4. **Less than 3 years and 75 days** have passed since the intended effective date (with limited exceptions for entities that had already filed all returns consistent with S-corp treatment for the period)
5. **Entity (and shareholders) have reported all income consistently with S-corp treatment** for the period from the intended effective date — OR the entity has not yet filed a return for that period (most-common new-entity case)

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

If the user is past 3 years 75 days, Rev. Proc. 2013-30 is unavailable. The remaining option is a Private Letter Ruling under Reg. §301.9100-3 — expensive ($12,600 user fee as of 2026, plus CPA/attorney fees) and outside the scope of this skill. Refer to a tax attorney.

### Mechanics of filing late under Rev. Proc. 2013-30

1. Complete Form 2553 normally (Parts I, II if applicable, III if QSST)
2. **Across the top of page 1**, write or print: **"FILED PURSUANT TO REV. PROC. 2013-30"**
3. Complete **Part IV** — check Boxes 1, 2, 3
4. **Attach a reasonable-cause statement** as a separate page — see acceptable language below
5. Get all shareholder signatures (same as on-time filing)
6. Either fax to the appropriate service center OR attach to the first Form 1120-S being filed and mail with that 1120-S

### Acceptable reasonable-cause language

The IRS has historically accepted these patterns:

> "The entity owners were unaware of the requirement to file Form 2553 within 2 months and 15 days of the intended effective date. Upon learning of the requirement on [date], owners promptly engaged a tax professional and prepared this election."

> "The entity's prior accountant agreed to prepare and file Form 2553 but failed to do so before disengaging in [month/year]. The owner discovered the failure on [date] when reviewing tax records and is filing this election immediately upon discovery."

> "The entity owner believed (incorrectly) that filing the LLC operating agreement designating S-corp tax treatment automatically triggered the federal election. Upon being advised by a CPA on [date] that a separate Form 2553 filing was required, the owner is filing this form."

### Unacceptable reasonable-cause language

These do NOT qualify and will result in CP262 rejection:

- "We wanted to wait and see how the year went before electing." (willful, not inadvertent)
- "We elected at our convenience." (no cause)
- "We were too busy to file." (insufficient diligence)

The reasonable-cause statement should be **2-4 sentences**, factual, dated, and signed (typically by the same officer signing Line J).

### Consistent-treatment requirement

Box 3 of Part IV requires that the entity and shareholders have reported income consistent with S-corp treatment since the intended effective date. In practice:

| Entity status | Action required |
|---------------|-----------------|
| New entity, no returns filed yet | Box 3 satisfied automatically; just check it |
| LLC that filed Schedule C (single member) | Owner must amend Form 1040 to remove Schedule C and report S-corp income via Schedule K-1 from Form 1120-S |
| LLC that filed Form 1065 (multi-member) | File a "final" 1065 for the period before effective date; file 1120-S from effective date forward; partners amend their 1040s |
| Corporation that filed Form 1120 (C-corp) | File 1120-S retroactively from effective date; if 1120 was already filed, may need to file a 1120-X (amended C-corp return showing zero) for the period |

Most new entities take the easy path: file Form 2553 with Rev. Proc. 2013-30 relief BEFORE filing any return for the year. Then file 1120-S directly. No amendments needed.

---

## Special timing case: Form 8832 already filed

Some LLCs first file Form 8832 (Entity Classification Election) to be taxed as a C-corp, then later decide to be an S-corp. The 2-month-15-day clock for Form 2553 starts at the **8832 effective date**, not the original LLC formation date — because the entity was a partnership-taxed LLC before, and only became a "small business corporation" eligible for S-election when 8832 took effect.

For LLCs going **directly** to S-corp without an intervening C-corp period, Form 2553 alone makes the combined election (per Rev. Proc. 2013-30). The 2-month-15-day clock starts at the *desired* S-corp effective date, which can be the LLC's original formation date for a new entity.

---

## §444 election (fiscal year)

If the entity wants a non-calendar tax year that isn't a "natural business year" or "ownership year," it can elect under §444 to use a fiscal year by making a **required payment** under IRC §7519. Mechanics:

1. Check Line I Box 4 ("Other") on Form 2553
2. Complete Part II
3. Also file **Form 8716** (Election to Have a Tax Year Other Than a Required Tax Year)
4. Annually compute and pay the required payment via Form 8752

Most small entities should not elect §444 — the required payment captures most of the deferral benefit, and the compliance overhead is significant. Default to calendar year.

---

## Quick reference: timing decision matrix

```
| Scenario                                              | Filing window                          | Relief?            |
|-------------------------------------------------------|----------------------------------------|--------------------|
| Calendar-year existing entity, 2026 election          | 1/1/2025 - 3/15/2026                  | None needed        |
| Calendar-year, missed 3/15/2026                       | After 3/15/2026, before 3/16/2029     | Rev. Proc. 2013-30 |
| New entity formed 3/1/2026                            | 3/1/2026 - 5/16/2026                  | None needed        |
| New entity formed 3/1/2026, missed 5/16/2026          | 5/16/2026 - 5/15/2029                 | Rev. Proc. 2013-30 |
| Calendar-year, missed by >3 years 75 days             | Beyond 3/16/2029 (for 2026 effective)  | §301.9100-3 PLR    |
```

---

## Cross-references

- Form mechanics: [`line-by-line.md`](./line-by-line.md)
- Eligibility: [`eligibility.md`](./eligibility.md)
- Common timing mistakes: [`common-mistakes.md`](./common-mistakes.md)
- Filing channel and CP261 follow-up: [`../filing.md`](../filing.md)
- Authority sources: IRC §1362(b), Rev. Proc. 2013-30, Rev. Proc. 2006-46 (natural business year), Reg. §301.9100-3 (PLR relief)
