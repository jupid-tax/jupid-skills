# Form 8824 Timing Rules

The 45-day identification deadline and 180-day acquisition deadline are the most-litigated rules in §1031. They are statutory (IRC §1031(a)(3)) — there is no extension, no good-faith exception, and no waiver except the federally declared disaster postponement described below.

Verified on 2026-10-06 against IRC §1031(a)(3), Treas. Reg. §1.1031(k)-1 (eCFR), Pub. 544 (2025), and the 2025 Instructions for Form 8824.

Miss either deadline by one day and the entire deferral fails.

---

## The 45-day identification rule (IRC §1031(a)(3)(A))

The user has **45 calendar days** from the date the relinquished property is transferred (Form 8824 Line 4) to identify the replacement property in writing.

### What "identify in writing" means

Per Treas. Reg. §1.1031(k)-1(c):
- **Written**: a signed document (paper or signed PDF; email is acceptable if signed)
- **Unambiguous description**: legal description (preferred) or street address; for unbuilt property, a clear lot number / parcel ID
- **Sent to the right person**: either the person obligated to transfer the replacement property to the user (even if that person is a disqualified person), or any other person involved in the exchange other than the user or a disqualified person — typically the Qualified Intermediary (QI) (Treas. Reg. §1.1031(k)-1(c)(2)). The user's own attorney, accountant, broker, or real estate agent who acted for the user in the prior 2 years is a disqualified person (§1.1031(k)-1(k)), so delivery only to that person does not count.
- **Delivered by midnight of the 45th day** (Treas. Reg. §1.1031(k)-1(b)(2)(i))

### Day counting

Day 1 = the day after Line 4 (the transfer day). Day 45 = the 45th day after Line 4.

Example:
- Line 4 = March 1
- Day 1 = March 2
- Day 45 = April 15

Identification must be delivered no later than April 15.

**No weekend / holiday extension.** The identification period "ends at midnight on the 45th day" (Treas. Reg. §1.1031(k)-1(b)(2)(i)). If Day 45 falls on a Saturday, Sunday, or federal holiday, do not push it to the next business day. Plan ahead.

If the user transferred more than one relinquished property on different dates as part of the same transaction, both the 45-day and 180-day periods start on the date of the earliest transfer (Pub. 544, "Identification requirement").

### The three-property rule

The user can identify up to **three replacement properties** of any value. They can ultimately acquire one, two, or all three.

This is the most-used identification approach.

### The 200% rule

If the user wants to identify more than three properties, they may — but the **aggregate FMV** of all identified properties at the end of the identification period cannot exceed **200% of the FMV of all relinquished property on the date of transfer** (Pub. 544, "Identifying alternative and multiple properties").

Example: relinquished FMV is $500,000. User can identify any number of properties as long as their total FMV is ≤ $1,000,000.

### The 95% rule

If the user identifies more than three properties AND their total FMV exceeds 200% of relinquished FMV, the user must acquire properties whose aggregate FMV is **at least 95% of all identified properties' FMV** to satisfy §1031.

Failure to acquire 95% disqualifies the entire exchange. This rule is rarely useful.

### Revocation

Identification can be revoked by a signed written document, delivered the same way, at any time before the end of the identification period. After Day 45, identification is locked.

### Constructive identification

If the replacement property was actually acquired within the 45-day window (Line 6 ≤ Line 4 + 45 days), it is automatically deemed identified — no separate written notice needed. This is rare in delayed exchanges but common in simultaneous exchanges.

---

## The 180-day acquisition rule (IRC §1031(a)(3)(B))

The user must receive the replacement property by the **earlier** of:

1. **180 calendar days** after the date the relinquished property was transferred (Line 4), OR
2. **The due date of the user's tax return** (with extensions) for the year the relinquished property was transferred.

### Why "earlier of"

The statute caps the exchange period at the due date (with extensions) of the return for the year of the relinquished transfer (IRC §1031(a)(3)(B)(ii)). If the unextended return is due (April 15 for a calendar-year individual) before 180 days have passed, the user must either complete the exchange by that date or extend the return (Form 4868 extends to October 15).

### Example calculations

**Scenario A — relinquished early in year**:
- Line 4 = March 1, 2025
- 180 days = August 28, 2025
- Return due (without extension) = April 15, 2026
- Earlier date = August 28, 2025 → that's the deadline

**Scenario B — relinquished late in year**:
- Line 4 = November 15, 2025
- 180 days = May 14, 2026
- Return due without extension = April 15, 2026
- Earlier date = April 15, 2026 → if the user wants the full 180 days, **they must file Form 4868 for an extension** to push their return due date to October 15, 2026

This is a frequent trap. Always check.

### What "receive" means

The replacement property must be transferred to the user (or to the QI for the user's benefit) by the deadline. "Receive" = title closes / deed records.

A signed contract with closing scheduled after Day 180 does **not** satisfy the rule. The closing must occur by Day 180.

### Identification → acquisition flow

```
Day 0:  Line 4 (relinquished transfer)
Days 1-45:  Window to deliver written identification → Line 5
Days 1-180:  Window to close on replacement → Line 6
              (subject to the "or return due date" cap)
```

Line 5 and Line 6 deadlines run concurrently from Day 0, not sequentially. The user does not get 45 + 180 = 225 days.

---

## Reverse exchange timing (Rev. Proc. 2000-37)

In a reverse exchange, the user (through an Exchange Accommodation Titleholder, EAT) acquires the replacement BEFORE relinquishing the original. The timing rules invert:

- The user and the EAT must sign a written qualified exchange accommodation agreement (QEAA) no later than 5 business days after the replacement is transferred to the EAT.
- The user must identify the property to be relinquished within **45 days** after the transfer of the replacement to the EAT.
- Within **180 days** after that transfer, the replacement must be transferred to the user (directly or through a QI) or the relinquished property must be transferred to someone other than the user or a disqualified person.
- The combined time the relinquished and replacement property are held in the QEAA cannot exceed **180 days**.
- Rev. Proc. 2004-51: property the user owned within 180 days before its transfer to the EAT cannot be treated as replacement property.

(Rev. Proc. 2000-37, as modified by Rev. Proc. 2004-51; Pub. 544 (2025), "Like-Kind Exchanges Using Qualified Exchange Accommodation Arrangements".)

If the user fails any of these, the safe harbor is broken and the IRS may treat the user as the owner of the property the EAT holds.

### Reverse-exchange Form 8824 reporting

The exchange is reported on Form 8824 in the year the **relinquished property is transferred** (Line 4), NOT the year the replacement was acquired. This often confuses first-time reverse-exchange filers.

---

## Disaster relief

When the IRS announces relief for a federally declared disaster, Rev. Proc. 2018-58, section 17 postpones the last day of the 45-day identification period and the 180-day exchange period (and the Rev. Proc. 2000-37 reverse-exchange periods) that fall on or after the disaster date by **120 days or to the end of the general disaster extension period, whichever is later** — but never beyond the due date (with extensions) of the return for the year of transfer, and never more than 1 year. The user qualifies only if the relinquished property was transferred (or, in a reverse exchange, title went to the EAT) on or before the disaster date and the user is an "affected taxpayer" or had difficulty meeting a deadline because of the disaster (e.g., a property, the QI, a lender, or a title insurer was in the covered area).

Example of a broad notice: COVID-19 relief in Notice 2020-23 extended deadlines falling between April 1 and July 15, 2020 to July 15, 2020.

Relief is announcement-driven. Always check **IRS Disaster Relief** at https://www.irs.gov/newsroom/tax-relief-in-disaster-situations for the user's specific date range and county.

---

## Common timing mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Counted business days instead of calendar days | Missed 45 or 180-day deadline | Recompute using calendar days; if missed, recognize gain currently |
| Identified by phone, not in writing | Identification invalid; exchange fails | Must be written and signed; cannot be cured retroactively |
| Identified only to user's own attorney (a disqualified person) | Identification invalid | Must be delivered to the QI or another non-disqualified party, or to the replacement seller |
| Did not file Form 4868 extension when relinquished in late November | 180-day deadline truncated to April 15 return due date | Extend the return if the 180th day falls after the unextended due date (for a 2025 transfer and an April 15, 2026 due date: any transfer after October 17, 2025) |
| Closed on replacement after Day 180 due to title issues | Exchange fails | No relief except IRS disaster notice; recognize gain |
| Took possession of cash from sale (constructive receipt) | No QI involvement = no §1031 deferral, even if a replacement was bought | Must use QI from the start; cannot retroactively constitute one |
| Used a related party as QI | QI is disqualified per Treas. Reg. §1.1031(k)-1(k); exchange fails | Use an independent QI (not your attorney, accountant, or family) |

---

## Validation the agent must run

Before submitting Form 8824:

- [ ] (Line 5 date) − (Line 4 date) ≤ 45 calendar days
- [ ] (Line 6 date) − (Line 4 date) ≤ 180 calendar days
- [ ] (Line 6 date) ≤ user's tax return due date for the year of Line 4 (with extensions if filed)
- [ ] If user filed Form 4868 to push return due date, confirm extension date
- [ ] Identification was in writing, signed, delivered to the replacement seller or to a party who is not the user or a disqualified person (usually the QI)
- [ ] If reverse exchange, EAT-related dates are within 45/180 windows from EAT's acquisition, the QEAA was signed within 5 business days, and the user did not own the replacement within the 180 days before the EAT took title
- [ ] If any deadline looks missed, ask whether a federally declared disaster postponement applies before concluding

If any of these fail, **stop and inform the user**. The §1031 deferral does not apply, and Form 8824 should not be filed for this transaction. Recognize the gain on Schedule D / Form 4797 normally.

---

## Sources

- IRC §1031(a)(3) — 45-day and 180-day deadlines
- Treas. Reg. §1.1031(k)-1(b) through (k) — qualified intermediary, identification, deferred-exchange rules
- Rev. Proc. 2000-37 — reverse exchange safe harbor
- Rev. Proc. 2004-51 — modifies Rev. Proc. 2000-37 (180-day prior-ownership bar)
- Rev. Proc. 2018-58, section 17 — disaster postponement of §1031 deadlines
- Pub. 544 (Sales and Other Dispositions of Assets) — narrative explanation
- Form 8824 instructions, current revision
- IRS Disaster Relief portal: https://www.irs.gov/newsroom/tax-relief-in-disaster-situations
