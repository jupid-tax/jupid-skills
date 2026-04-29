# Form 8824 Timing Rules

The 45-day identification deadline and 180-day acquisition deadline are the most-litigated rules in §1031. They are statutory (IRC §1031(a)(3)) — there is no extension, no good-faith exception, no waiver for natural disasters except in narrow IRS-declared disaster relief notices.

Miss either deadline by one day and the entire deferral fails.

---

## The 45-day identification rule (IRC §1031(a)(3)(A))

The user has **45 calendar days** from the date the relinquished property is transferred (Form 8824 Line 4) to identify the replacement property in writing.

### What "identify in writing" means

Per Treas. Reg. §1.1031(k)-1(c):
- **Written**: a signed document (paper or signed PDF; email is acceptable if signed)
- **Unambiguous description**: legal description (preferred) or street address; for unbuilt property, a clear lot number / parcel ID
- **Delivered to a person involved in the exchange other than the user or a related party**: typically the Qualified Intermediary (QI). Cannot be delivered to the user's own attorney if that attorney represents only the user — must go to QI or seller.
- **Delivered by midnight of the 45th day**

### Day counting

Day 1 = the day after Line 4 (the transfer day). Day 45 = the 45th day after Line 4.

Example:
- Line 4 = March 1
- Day 1 = March 2
- Day 45 = April 15

Identification must be delivered no later than April 15.

**No weekend / holiday extension.** If Day 45 falls on a Saturday, Sunday, or federal holiday, the deadline is **not** pushed to the next business day. Plan ahead.

### The three-property rule

The user can identify up to **three replacement properties** of any value. They can ultimately acquire one, two, or all three.

This is the most-used identification approach.

### The 200% rule

If the user wants to identify more than three properties, they may — but the **aggregate FMV** of all identified properties cannot exceed **200% of the FMV of the relinquished property**.

Example: relinquished FMV is $500,000. User can identify any number of properties as long as their total FMV is ≤ $1,000,000.

### The 95% rule

If the user identifies more than three properties AND their total FMV exceeds 200% of relinquished FMV, the user must acquire properties whose aggregate FMV is **at least 95% of all identified properties' FMV** to satisfy §1031.

Failure to acquire 95% disqualifies the entire exchange. This rule is rarely useful.

### Revocation

Identification can be revoked in writing before the 45th day. After Day 45, identification is locked.

### Constructive identification

If the replacement property was actually acquired within the 45-day window (Line 6 ≤ Line 4 + 45 days), it is automatically deemed identified — no separate written notice needed. This is rare in delayed exchanges but common in simultaneous exchanges.

---

## The 180-day acquisition rule (IRC §1031(a)(3)(B))

The user must receive the replacement property by the **earlier** of:

1. **180 calendar days** after the date the relinquished property was transferred (Line 4), OR
2. **The due date of the user's tax return** (with extensions) for the year the relinquished property was transferred.

### Why "earlier of"

The IRS's reasoning: the exchange must be reported on the tax return for the year of relinquished transfer. If the return is due (April 15 + 6-month extension = October 15) before 180 days have passed, the user must complete the exchange by the return due date or file an extension.

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

- The EAT parks the replacement title for up to **180 days**.
- During this period, the user must:
  - Identify the property to be relinquished within **45 days** of the EAT's acquisition
  - Complete the disposition (relinquished sale) within **180 days** of the EAT's acquisition

If the user fails either deadline, the safe harbor of Rev. Proc. 2000-37 is broken and the IRS may reclassify the EAT's holdings as taxable to the user.

### Reverse-exchange Form 8824 reporting

The exchange is reported on Form 8824 in the year the **relinquished property is transferred** (Line 4), NOT the year the replacement was acquired. This often confuses first-time reverse-exchange filers.

---

## Disaster relief

The IRS occasionally issues notices extending §1031 deadlines for taxpayers in federally-declared disaster areas. Examples:
- Hurricane-related extensions (multiple notices per year in affected zones)
- COVID-19 relief: Notice 2020-23 extended deadlines falling between April 1 and July 15, 2020 to July 15, 2020

These are notice-driven, not statutory. Always check **IRS Disaster Relief** at https://www.irs.gov/newsroom/tax-relief-in-disaster-situations for the user's specific date range and ZIP code.

---

## Common timing mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Counted business days instead of calendar days | Missed 45 or 180-day deadline | Recompute using calendar days; if missed, recognize gain currently |
| Identified by phone, not in writing | Identification invalid; exchange fails | Must be written and signed; cannot be cured retroactively |
| Identified to user's own attorney (not QI or seller) | Identification invalid | Must be delivered to QI or seller |
| Did not file Form 4868 extension when relinquished in late November | 180-day deadline truncated to April 15 return due date | Always file extension if relinquished after October 18-20 (depending on weekend) |
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
- [ ] Identification was in writing, signed, delivered to QI (not user/related party)
- [ ] If reverse exchange, EAT-related dates are within 45/180 windows from EAT's acquisition

If any of these fail, **stop and inform the user**. The §1031 deferral does not apply, and Form 8824 should not be filed for this transaction. Recognize the gain on Schedule D / Form 4797 normally.

---

## Sources

- IRC §1031(a)(3) — 45-day and 180-day deadlines
- Treas. Reg. §1.1031(k)-1(b) through (k) — qualified intermediary, identification, deferred-exchange rules
- Rev. Proc. 2000-37 — reverse exchange safe harbor
- Rev. Proc. 2003-39 — IRS modifications to §1031(k)-1
- Pub. 544 (Sales and Other Dispositions of Assets) — narrative explanation
- Form 8824 instructions, current revision
- IRS Disaster Relief portal: https://www.irs.gov/newsroom/tax-relief-in-disaster-situations
