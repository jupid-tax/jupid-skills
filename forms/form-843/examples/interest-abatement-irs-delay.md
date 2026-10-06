# Example: Interest Abatement for an IRS Transfer Delay (§6404(e)(1))

A married couple's audit was approved for transfer to their new local IRS office, then sat untouched for months. They agreed to a deficiency, paid it with interest, and now want back the interest that ran during the delay. The 3-year refund window has already closed; the 2-year-from-payment window has not. The interest amount is an estimate built from the IRS quarterly rates with daily compounding.

All dates and amounts below were computed and checked in Python (daily compounding at the quarterly underpayment rates; §6511 dates). Displayed amounts are rounded to cents; line 2 is the difference of the two rounded totals.

## The filers

- **Names:** Dana and Luis Ortega, married filing jointly
- **Return:** 2022 Form 1040, due 04/18/2023 (2022 Form 1040 instructions); filed early on 04/12/2023
- **Moved:** Arizona to Oregon in March 2024
- **Today:** 10/06/2026; planned mailing 10/13/2026

## Inputs the agent collected (by asking)

```
01/22/2024  IRS examination letter for 2022 (first written IRS contact)
04/08/2024  Ortegas ask in writing to transfer the exam to the office near their new home
04/22/2024  IRS group manager approves; the approval letter says the file will be
            transferred within 14 days
05/06/2024  14 days after approval: transfer not done
11/18/2024  New office acknowledges receipt of the file (letter dated 11/18/2024);
            no exam activity happened between 04/22/2024 and 11/18/2024
03/20/2025  Ortegas agree to a $7,384.00 income tax deficiency (no penalty)
05/12/2025  Deficiency and interest assessed
06/02/2025  Paid in full: $8,675.04 (tax $7,384.00 + interest $1,291.04)
Contributed to delay?  No: they answered every IRS request within the stated time
Representative: none.  IP PINs: none issued
```

## Step 1 — Vehicle and ground

Interest on an income tax deficiency, caused by IRS delay after written contact: IRC §6404(e)(1), Form 843 Interest box, line 7 box a. Income tax deficiencies require a notice of deficiency, so the interest is eligible (i843). Employment tax interest would not be.

## Step 2 — The six IRS criteria (https://www.irs.gov/payments/interest-abatement)

| Criterion | Facts | Met? |
|---|---|---|
| Claim within 3 years of filing or 2 years of payment, whichever is later | See §6511 below | Yes (2-year rule) |
| Tax year after 1978 | 2022 | Yes |
| Income, estate, gift, or certain excise tax | Income tax | Yes |
| Error or delay after IRS written contact | Contact 01/22/2024; delay from 05/06/2024 | Yes |
| Taxpayer did not contribute | User states all responses were on time | Yes (user's statement) |
| Unreasonable delay in a ministerial or managerial act | Transfer after approval is a ministerial act (IRS example 1 on the interest abatement page) | Likely; the IRS decides what is unreasonable |

The agent asked the user to choose the start of the delay period and recommended tying it to the IRS's own 14-day statement. The IRS may pick different dates.

## Step 3 — Timing (§6511)

```
A. Return filed 04/12/2023, before the 04/18/2023 due date → treated as filed 04/18/2023 (IRC 6513(a))
B. 3-year deadline:                       04/18/2026 — PASSED
C. Planned claim date:                    10/13/2026
D. C on or before B?                      No → 2-year rule, §6511(b)(2)(B)
E. Lookback start (C − 2 years):          10/13/2024
F. Payment 06/02/2025 $8,675.04           inside lookback: yes
G. Maximum refund:                        $8,675.04 (far above the claim)
2-year-from-payment deadline:             06/02/2027
```

## Step 4 — Interest estimate

Rates from https://www.irs.gov/payments/quarterly-interest-rates (underpayment, non-corporate): 2023 Q2–Q3 7%, 2023 Q4 8%, 2024 all quarters 8%, 2025 all quarters 7%. Daily compounding (IRC §6622(a)); daily rate = annual rate ÷ 365 (366 in 2024).

```
Deficiency (interest runs from 04/18/2023):          $7,384.00
Balance with interest at 05/06/2024:                 $7,995.25
Balance with interest at 11/18/2024 (196 days later): $8,345.19
Interest that accrued inside the delay period:       $349.94

Interest actually charged 04/18/2023–06/02/2025:     $1,291.04
Interest recomputed with no accrual 05/06–11/18/2024: $927.27
Reduction requested (line 2):                        $363.77
  = $349.94 accrued in the period + $13.83 compounding on it after 11/18/2024
```

The estimate is labeled as such; the IRS recomputes. The agent did not invent any rate.

## Completed Form 843 draft

```markdown
# Form 843 — DRAFT (Rev. December 2024)

## Routing decision
- Channel: Form 843 by mail (a signed letter is also accepted)
- Relief ground: IRS delay in a ministerial act, IRC 6404(e)(1)
- §6511 check: return deemed filed 04/18/2023; 3-year deadline 04/18/2026 passed;
  2-year rule from payment 06/02/2025 applies; lookback from 10/13/2024; refundable payment $8,675.04

## Reason box (one)
[x] Abatement or refund of interest due to IRS error or delay under section 6404(e)(1)

## Identity
Name: Dana Ortega             SSN: XXX-XX-XXXX
Spouse: Luis Ortega           SSN: XXX-XX-XXXX
Address: <current Oregon address>   EIN: (blank)
Name/address on return if different: <Arizona address shown on the 2022 return>
Daytime phone: <phone>

## Lines
1. Tax period: 01/01/2022 to 12/31/2022
2. Amount to be refunded or abated: $363.77
3. Payment dates: a 06/02/2025
4. Type of tax: e Income
5. Type of return: i 1040
6. IRC section: (blank — interest request, not a penalty)
7. Reason: a
8. Explanation:
   Type of tax: individual income tax, Form 1040, tax year 2022.
   First written IRS contact: examination letter dated 01/22/2024.
   Period requested: 05/06/2024 through 11/18/2024 (196 days).
   Circumstances: on 04/08/2024 we asked in writing that the examination be
   transferred to the IRS office near our new home in Oregon. The group manager
   approved the transfer on 04/22/2024, and the approval letter stated the file
   would be transferred within 14 days. The file did not reach the new office until
   11/18/2024 (acknowledgment letter attached). No examination work occurred in that
   period, and we responded to every IRS request on time. Transferring an approved
   case is a ministerial act; the delay after 05/06/2024 was not caused by us.
   Why failure to abate would be grossly unfair: the deficiency was agreed without
   dispute, and the only reason interest ran for these 196 days was the stalled
   transfer of an approved request.
   Computation of line 2 (estimate; IRS to recompute): deficiency $7,384.00,
   interest from 04/18/2023 compounded daily at the IRS underpayment rates
   (7% 2023 Q2–Q3, 8% 2023 Q4 and 2024, 7% 2025). Interest charged through payment
   on 06/02/2025: $1,291.04. Recomputed with no accrual from 05/06/2024 to
   11/18/2024: $927.27. Difference: $363.77 ($349.94 accrued in the period plus
   $13.83 subsequent compounding). We request a refund of this amount.
   Attachments: IRS letters dated 01/22/2024, 04/22/2024, 11/18/2024; our letter of
   04/08/2024; proof of payment 06/02/2025.

## Signatures
Taxpayer: ______________________  Date: __________  IP PIN: (none issued)
Spouse:   ______________________  Date: __________  IP PIN: (none issued)
Paid preparer: (blank)

## Attachments
- [ ] IRS letters dated 01/22/2024, 04/22/2024, 11/18/2024
- [ ] Transfer request dated 04/08/2024
- [ ] Payment record 06/02/2025
  (both names and one SSN on every page)

## Validation summary
- Math: $1,291.04 − $927.27 = $363.77 ✓; line 2 ✓
- Form: one box ✓; one period ✓; line 6 blank (interest) ✓; line 7 a ✓; both spouses sign ✓
- Timing: 3-year window closed; 2-year window open until 06/02/2027 ✓
- Warnings: the IRS decides whether the delay was "unreasonable" and may use a shorter period

## Mailing
Address: the IRS service center where a current-year Form 1040 from Oregon is filed
  without a payment (i843: "for ... any other reason ... the service center where you
  would be required to file a current year tax return"); look up live at
  https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment
Method: certified mail, return receipt requested; keep copies

## Next steps
- If the IRS denies or does not act: appeal rights are in the decision letter; Tax Court
  review of a failure to abate interest is available under IRC 6404(h) for taxpayers who
  meet the IRC 7430(c)(4)(A)(ii) net-worth limits (petition no earlier than the final
  determination or 180 days after this claim, and within 180 days after the final
  determination is mailed). Recommend a tax professional for that step.
```

## Reasoning notes

- **Why the 2-year rule saves the claim:** the early return counts as filed on the due date, so the 3-year window closed 04/18/2026. The payment on 06/02/2025 opens a 2-year window to 06/02/2027, and the refund is capped by payments in the 2 years before the claim. The full payment is inside that cap.
- **Why line 2 includes $13.83 of later compounding:** abating interest for the period lowers the balance on which later interest compounded. The recomputation captures both parts.
- **Why line 6 is blank:** line 6 is for penalty Code sections; this is interest.
- **Why the old Arizona address goes in the "if different" field:** the IRS matches the claim to the 2022 return, which carried the old address.
- **What the agent did not do:** assume the IRS will accept 05/06/2024 as the start, or compute interest with a rate not on the IRS page.
