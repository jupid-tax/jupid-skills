# Example: First Time Abate Refund of Penalties Already Paid

A freelancer filed her 2023 Form 1040 late, paid the tax with the return, then paid the penalty notice. Two years later she learns about First Time Abate. The penalties are paid, so this is a refund claim, and the IRC §6511 window decides whether money can come back.

All figures below were checked in Python (failure-to-file and failure-to-pay arithmetic, month counts, and the §6511 dates).

## The filer

- **Name:** Priya Raman, single, freelance UX researcher (Schedule C)
- **State:** Colorado
- **Return:** 2023 Form 1040, due 04/15/2024, no extension filed
- **Filed:** 08/19/2024, with full payment of the balance due
- **Today:** 10/06/2026; she plans to mail on 10/13/2026

## Inputs the agent collected (by asking)

```
Notice: CP14-type balance notice dated 09/16/2024 (user read it aloud)
  Failure to file penalty, IRC 6651(a)(1), period ending 12/31/2023:   $1,444.05
  Failure to pay penalty,  IRC 6651(a)(2), period ending 12/31/2023:   $160.45
  Interest on penalties and late payment: shown separately
Payments:
  08/19/2024  tax balance $6,418.00 paid with the return
  10/02/2024  penalties and interest paid in full per the notice ($1,604.50 penalties)
Return facts (from her copy of the return):
  Total tax $9,912.00; estimated payments $3,494.00; balance due $6,418.00
Prior three years, same return (Form 1040):
  2020, 2021, 2022: filed on time, no penalties, no IRS letters about penalties
Prior penalty relief: none ever
Reason for lateness: "I lost track of the deadline while moving apartments."
Representative: none
IP PIN: not issued
```

## Step 1 — Is Form 843 the right vehicle?

The charges are penalties on income tax, not income tax itself, and not the §6654 estimated tax penalty. Form 843 applies (i843, Purpose of Form). Line 4 will be box e (Income).

## Step 2 — Should relief already have happened?

- Account error? No: she confirms the return went in on 08/19/2024.
- AEP? No: AEP starts with 2025 tax year returns. This is a 2023 return.

## Step 3 — Relief ground

Her stated reason (forgot the deadline while moving) is a "mistake or oversight," which the IRS reasonable cause page says generally does not qualify. So the agent checks FTA instead.

FTA lookback worksheet:

```
Penalized period: 12/31/2023   Return type: Form 1040
2022: filed on time, no penalty
2021: filed on time, no penalty
2020: filed on time, no penalty
Penalty types: 6651(a)(1) and 6651(a)(2) — both FTA-eligible
Event-based return? No
=> Likely eligible for First Time Abate (IRS checks its own records)
```

## Step 4 — Channel

She has no open notice to call about; the penalties were paid two years ago. A refund requires a claim filed inside the §6511 period, so the agent drafts Form 843 rather than relying on a phone call. (A call to 800-829-1040 is an option she may also try; the written claim protects the deadline.)

## Step 5 — Timing (§6511)

```
A. Return filed (late, actual date):           08/19/2024
B. 3-year deadline (A + 3 years):              08/19/2027
C. Planned claim date:                         10/13/2026
D. C on or before B?                           Yes → 3-year rule, §6511(b)(2)(A)
E. Lookback start (C − 3 years, no extension): 10/13/2023
F. Penalty payment 10/02/2024 $1,604.50        inside lookback: yes
G. Maximum refund:                             $1,604.50
```

## Cross-check of the notice amounts (optional consistency check)

The agent uses the notice figures. As a sanity check it recomputes them from the IRS rules (https://www.irs.gov/payments/failure-to-file-penalty, https://www.irs.gov/payments/failure-to-pay-penalty):

```
Unpaid tax at due date:  $9,912.00 − $3,494.00 = $6,418.00
Months late (each month or part): 04/16–05/15, 05/16–06/15, 06/16–07/15,
  07/16–08/15, 08/16–08/19 → 5
Failure to pay: 0.5% × 5 × $6,418.00 = $160.45
Failure to file: (5% − 0.5%) × 5 × $6,418.00 = 4.5% × 5 × $6,418.00 = $1,444.05
  (reduced by the FTP amount for months both apply)
Minimum FTF for returns due in 2024 and over 60 days late: $485 (126 days late) → $1,444.05 exceeds it
Total penalties: $1,604.50 — matches the notice
```

## Completed Form 843 draft

```markdown
# Form 843 — DRAFT (Rev. December 2024)

## Routing decision
- Channel: Form 843 by mail (refund claim)
- Relief ground: First Time Abate
- FTA lookback: likely eligible (2020–2022 Forms 1040 timely, no penalties)
- §6511 check: return filed 08/19/2024; 3-year deadline 08/19/2027; claim date 10/13/2026;
  lookback from 10/13/2023; refundable payments $1,604.50

## Reason box (one)
[x] Abatement or refund of a penalty or addition to tax due to reasonable cause or other reason allowed under the law

## Identity
Name: Priya Raman                 SSN: XXX-XX-XXXX
Spouse: (blank — not a joint return)
Address: <current Colorado address>   EIN: (blank)
Name/address on return if different: (blank — unchanged)
Daytime phone: <phone>

## Lines
1. Tax period: 01/01/2023 to 12/31/2023
2. Amount to be refunded or abated: $1,604.50
3. Payment dates: a 10/02/2024
4. Type of tax: e Income
5. Type of return: i 1040
6. IRC section: 6651(a)(1) and 6651(a)(2)
7. Reason: c
8. Explanation:
   I request a refund of the failure-to-file penalty under IRC 6651(a)(1) ($1,444.05)
   and the failure-to-pay penalty under IRC 6651(a)(2) ($160.45) assessed for tax
   period ending 12/31/2023, total $1,604.50, under the First Time Abate
   administrative waiver, together with the interest charged on these penalties.
   Compliance history: I filed Form 1040 on time for 2020, 2021, and 2022, with no
   penalties assessed for those years, and I have not received penalty relief before.
   I filed the 2023 return on 08/19/2024 and paid the full balance of tax that day.
   I paid the penalties on 10/02/2024 after the notice dated 09/16/2024.
   Computation of line 2: $1,444.05 + $160.45 = $1,604.50, as shown on the notice.
   Attachments: copy of the notice dated 09/16/2024; proof of the 10/02/2024 payment.

## Signatures
Taxpayer: ______________________  Date: __________  IP PIN: (none issued)
Spouse: (not applicable)
Paid preparer: (blank)

## Attachments
- [ ] Copy of notice dated 09/16/2024 (name and SSN on each page)
- [ ] Bank record of the 10/02/2024 payment (name and SSN written on it)

## Validation summary
- Math: line 2 = $1,444.05 + $160.45 = $1,604.50 ✓; matches notice ✓; within lookback ✓
- Form: one reason box ✓; one period ✓; line 4 one box ✓; line 5 one box ✓; line 6 filled ✓; line 7 one box ✓
- Warnings: line 7 box c is the agent's reading for an FTA request (instructions do not name FTA)

## Mailing
Address: the IRS service center where a current-year Form 1040 from Colorado is filed
  without a payment (i843 "for penalties ... the service center where you would be
  required to file a current year tax return"); look it up live at
  https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment
Method: certified mail, return receipt requested; keep a full copy

## Sources cited in this draft
- Form 843 and Instructions (Rev. December 2024)
- IRM 20.1.1.3.3.2.1 (03-29-2023); IRS FTA/AEP page (14-Jul-2026)
- IRC 6511(a), 6511(b)(2)(A), 6651(a)(1), 6651(a)(2)
```

## Reasoning notes

- **Why not reasonable cause:** a forgotten deadline is a mistake or oversight; the IRS page says those generally do not qualify. FTA needs no excuse.
- **Why one form:** both penalties belong to the same period and the same return; line 2 totals them.
- **Why line 3 has one date:** only the penalty payment of 10/02/2024 is refunded. The 08/19/2024 payment was tax, which is not being refunded.
- **Interest:** the IRS removes interest on abated penalties automatically. The line 8 sentence mentions it so the refund includes it, but line 2 stays at the penalty total because interest on penalties is not a separate claim.
- **What the agent did not do:** promise approval, pick a mailing address from memory, or add a reasonable-cause story the user did not give.
