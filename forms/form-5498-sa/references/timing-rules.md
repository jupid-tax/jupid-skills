# Form 5498-SA — Timing Rules

The most reconciliation-prone aspects of Form 5498-SA are timing-related. This reference covers the rules in detail.

---

## Calendar year vs. tax year

For HSAs, the **calendar year** and the **tax year** are the same: January 1 through December 31. There's no fiscal year option for an HSA.

5498-SA reports calendar-year activity:

- **Box 2** — Contributions received by the custodian between January 1 and December 31 of the year on the form (whatever year they were designated for)
- **Box 3** — Contributions received January 1–April 15 of the next year and designated for the year on the form
- **Box 5** — Account balance on December 31 of the tax year

---

## The April 15 prior-year contribution window

Under IRC §223(d)(4)(B), which applies the IRA rule of §219(f)(3), an account holder may make a contribution to their HSA for a tax year up until the **unextended filing deadline** for that tax year — April 15 of the following year (April 15, 2026 for 2025). An extension does not extend it; combat-zone service can (2025 Instructions for Form 8889, Line 2).

**Example timeline for tax year 2025:**

```
January 1, 2025 - December 31, 2025
    Calendar-year window for tax year 2025 contributions.
    Contributions received by custodian here → 2025 Form 5498-SA Box 2

January 1, 2026 - April 15, 2026
    Prior-year contribution window. Account holder can contribute
    for tax year 2025 if they designate the contribution as such.
    Contributions received here, designated for 2025 → 2025 Form 5498-SA Box 3
                                                       AND 2026 Form 5498-SA Box 2
    Contributions received here, designated for 2026 → 2026 Form 5498-SA Box 2

April 16, 2026 - December 31, 2026
    Calendar-year window for tax year 2026 contributions only.
```

The 5498-SA reports activity during a calendar year. The Form 8889 reports activity for a tax year. The April 15 window creates a 105-day overlap where the same contribution might affect two different tax years (and two different 5498-SAs).

---

## Custodian crediting rules

When does the custodian "receive" a contribution? The Instructions for Forms 1099-SA and 5498-SA only say "contributions made in" the year; they do not define a posting date. Custodians apply their own rules, typically:

- **Check** — date the check is received by the custodian
- **ACH / wire** — date funds clear to the HSA
- **Payroll deposit** — date the employer's deposit hits the HSA
- **Online transfer** — date the transfer is processed by the custodian's system

ASK the user for the posting date shown in the custodian's history rather than assuming one.

Practically, this means a check mailed December 28 may or may not be a current-year contribution, depending on when the custodian receives it.

To be safe:

- **Mail checks no later than mid-December** for current-year contributions
- **Use ACH or wire** in the last week of December for guaranteed current-year credit
- **Verify in the online portal** that the contribution shows as posted to the correct year before December 31

---

## Designation rules for prior-year contributions

For a contribution between January 1 and April 15 to count for the prior tax year, the account holder must **designate** it explicitly. Custodians offer designation methods:

- **Online portal** — typically a checkbox during the contribution flow ("This contribution is for tax year ____")
- **Paper form** — some custodians require a written election with the deposit
- **Phone call** — possible at most custodians but creates the weakest paper trail

**Default:** Without explicit designation, custodians treat contributions made January 1–April 15 as **current-year** contributions. The instructions tell the custodian to obtain the participant's designation for contributions in that window.

**Reversal:** Custodian policies differ on changing a designation; no IRS rule allows a prior-year designation after April 15. ASK the custodian before promising a change.

---

## December check trap

The most common timing error: writing a check for an HSA contribution in late December that doesn't clear until January.

**Example:**

- December 28, 2025: User mails check for $1,500 to Fidelity HSA
- December 31, 2025: Check has not yet been received by Fidelity (still in USPS)
- January 3, 2026: Fidelity receives the check and posts the deposit
- 5498-SA treatment: The $1,500 is **2026 Box 2**, not 2025 Box 2 — unless the user designated it as a prior-year contribution

If the user files Form 8889 for 2025 with the $1,500 on Line 2 (assuming it was a 2025 contribution because the check was written in December 2025), reconciliation will fail when the 2025 5498-SA shows $1,500 less than expected.

**Fix:** Contact Fidelity, ask them to designate the deposit as a prior-year contribution. If done by April 15, 2026, the $1,500 shows in the **2025 Form 5498-SA Box 3** (and the 2026 Box 2), and **counts toward the 2025 Form 8889**.

---

## January 1 contribution rule

Contributions made on January 1 (or any other January date) without prior-year designation are **current-year** contributions by default. So a January 1 contribution to "max out for the new year" goes into the new year's Box 2, not the prior year's.

To max out the prior year first:

1. Make a contribution between January 1 and April 15
2. Designate it as a prior-year contribution
3. Once the prior-year limit is met, additional contributions count toward the current year

---

## Custodian deadline: May 31 (next business day if a weekend)

The custodian must file Form 5498-SA with the IRS and furnish the participant copy by **May 31** of the year following the tax year, moved to the next business day when May 31 falls on a weekend or legal holiday (Pub. 1099 (2026)). If no contributions were made, a FMV statement furnished by January 31 can replace the participant copy.

**Example:** For tax year 2025, May 31, 2026 is a Sunday, so the 2025 instructions set **June 1, 2026** for both filing and furnishing.

This is a problem for filers because:

- The Form 8889 filing deadline is April 15 (or October 15 with extension)
- The 5498-SA arrives **after** the Form 8889 deadline
- Most filers complete Form 8889 from year-end statements (issued in January) without seeing the 5498-SA at all

The reconciliation must be done **after the fact**, in late May, against the already-filed Form 8889.

---

## CORRECTED 5498-SA timing

If the custodian discovers an error after issuing the original 5498-SA, they issue a **CORRECTED** version. The IRS receives the corrected copy directly; the account holder receives a copy by mail or electronically.

CORRECTED forms can be issued at any time, but most are issued within a few months of the original. If a CORRECTED form arrives **after** the user has filed Form 8889 and the correction changes the deduction, the user must file Form 1040-X.

---

## Statute of limitations interaction

The IRS has 3 years from the filing date of the original return to assess additional tax. The taxpayer has 3 years from the filing date (or 2 years from tax payment, whichever is later) to amend.

**For HSA reconciliation purposes:**

- If 5498-SA reveals an under-reported deduction, file Form 1040-X within 3 years to claim the additional refund
- If 5498-SA reveals an over-reported deduction, the IRS generally has 3 years to assess, and it receives the 5498-SA directly, so a CP2000 is possible
- If the return omitted more than 25% of the gross income it should have reported, the IRS gets 6 years instead of 3 (IRC §6501(e))

Don't sit on a known reconciliation error. Fix it within 3 years of the original filing.
