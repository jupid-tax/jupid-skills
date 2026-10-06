# Example: Reasonable-Cause Abatement After a Hospital Stay (FTA Already Used)

A sole proprietor was hospitalized across the 2025 filing deadline and filed 55 days late. He used First Time Abate in 2022, so FTA is closed to him. The failure-to-file penalty is unpaid, so this is an abatement request, not a refund. The agent also has to decide, with the user, whether the hospital facts cover the failure-to-pay penalty. They only partly do.

Arithmetic checked in Python (day count, month count, penalty amount).

## The filer

- **Name:** Marco Bellini, single, owner of a single-member LLC taxed as a sole proprietorship (Schedule C, cabinet installation)
- **Return:** 2024 Form 1040, due 04/15/2025, no extension filed
- **Filed:** 06/09/2025, paid $5,000 with the return
- **Notice:** CP14-type balance notice dated 07/14/2025; return address printed on it; penalty unpaid

## Inputs the agent collected (by asking)

```
Penalties on the notice (period ending 12/31/2024):
  Failure to file, IRC 6651(a)(1):   $1,011.24
  Failure to pay,  IRC 6651(a)(2):   accruing (amount shown as of notice date)
Unpaid tax at the due date:          $11,236.00
Paid with return 06/09/2025:         $5,000.00; balance still owed
Prior relief: penalty removed for 2022 with a letter saying "This type of penalty
  removal is only available one time" (user read the letter)
Events:
  03/24/2025  admitted to hospital (emergency surgery, complications)
  05/12/2025  discharged; doctor's letter restricts work and travel through 05/30/2025
  06/09/2025  return filed (10 days after the restriction ended)
Records: hospital admission and discharge summary; doctor's letter dated 05/12/2025
Funds: "My business account had about $6,000 in April. After I got out, I paid
  hospital bills first, so I only had $5,000 for the IRS in June."
Representative: none.  IP PIN: not issued
```

## Step 1 — Vehicle

Penalties on income tax → Form 843, line 4 box e. Not the estimated tax penalty.

## Step 2 — Should relief already have happened?

- Account error: no. AEP: the 2024 tax year is before AEP (2025 returns onward).

## Step 3 — Relief ground

FTA lookback for period 12/31/2024 covers 2021, 2022, 2023. The 2022 penalty was removed under FTA (the letter wording matches the IRM 20.1.1.3.3.2.1 notification text). A penalty removed under FTA in the lookback blocks FTA. Ground: **reasonable cause** (serious illness of the taxpayer, listed on https://www.irs.gov/payments/penalty-relief-for-reasonable-cause).

## Step 3a — Which penalty do the facts cover?

The agent asks each penalty separately (IRM 20.1.1: each penalty is a different failure).

- **Failure to file:** hospitalized from 03/24/2025 through the 04/15/2025 deadline; medically restricted until 05/30/2025; filed 06/09/2025. The facts connect the illness to the late filing and show prompt compliance after it ended. Request it.
- **Failure to pay:** in April he had about $6,000 against $11,236 owed, so he could not have paid in full even without the illness; after discharge he chose to pay medical bills first. The IRS page says lack of funds by itself is generally not reasonable cause. The agent explains this and asks whether to include the failure-to-pay penalty. **User decision: request the failure-to-file penalty only.** The agent records that the failure-to-pay penalty and interest keep accruing on the unpaid $6,236 and points him to `../../form-9465/SKILL.md` for a payment plan (an installment agreement in effect lowers the FTP rate to 0.25% per month for a timely filed return, IRC §6651(h); his return was late, so that reduction does not apply to him).

## Cross-check of the notice amount

```
Days late: 04/15/2025 → 06/09/2025 = 55 days (under 60, so the $510 minimum for
  returns due in 2025 does not apply)
Months late (each month or part): 04/16–05/15, 05/16–06/15 → 2
Failure to file: 4.5% × 2 × $11,236.00 = $1,011.24 — matches the notice
```

## Channel

The IRS reasonable cause page allows a phone request. Marco prefers paper because the evidence is documents. Mail to the return address on the notice (i843 Where To File: "in response to an IRS notice ... the return address from which the notice was sent").

## Completed Form 843 draft

```markdown
# Form 843 — DRAFT (Rev. December 2024)

## Routing decision
- Channel: Form 843 by mail to the notice return address
- Relief ground: Reasonable cause (serious illness)
- FTA lookback: not eligible — penalty removed under FTA for 2022 (inside 2021–2023 lookback)
- §6511 check: not applicable (abatement of an unpaid penalty)

## Reason box (one)
[x] Abatement or refund of a penalty or addition to tax due to reasonable cause or other reason allowed under the law

## Identity
Name: Marco Bellini           SSN: XXX-XX-XXXX
Spouse: (blank)
Address: <current address>    EIN: (blank — the LLC is disregarded; the penalty is on his Form 1040)
Name/address on return if different: (blank)
Daytime phone: <phone>

## Lines
1. Tax period: 01/01/2024 to 12/31/2024
2. Amount to be refunded or abated: $1,011.24
3. Payment dates: (blank — abatement of an unpaid penalty)
4. Type of tax: e Income
5. Type of return: i 1040
6. IRC section: 6651(a)(1)
7. Reason: c
8. Explanation:
   I request abatement of the failure-to-file penalty under IRC 6651(a)(1) of
   $1,011.24 for the tax period ending 12/31/2024, shown on the notice dated
   07/14/2025, for reasonable cause.
   On 03/24/2025 I was admitted to <hospital> for emergency surgery and remained
   hospitalized until 05/12/2025 because of complications. My physician restricted
   me from work and travel until 05/30/2025 (letter attached). I was hospitalized on
   the 04/15/2025 due date and could not gather my business records or prepare the
   return. I filed the return on 06/09/2025, ten days after the restriction ended.
   Computation of line 2: failure-to-file penalty as shown on the notice, $1,011.24.
   Attachments: hospital admission and discharge summary (03/24/2025–05/12/2025);
   physician's letter dated 05/12/2025; copy of the notice dated 07/14/2025.

## Signatures
Taxpayer: ______________________  Date: __________  IP PIN: (none issued)
Paid preparer: (blank)

## Attachments
- [ ] Hospital admission and discharge summary (name and SSN on each page)
- [ ] Physician's letter dated 05/12/2025 (name and SSN added)
- [ ] Copy of the notice dated 07/14/2025

## Validation summary
- Math: line 2 = $1,011.24, matches notice ✓
- Form: one box ✓; one period ✓; line 3 blank for abatement ✓; line 6 filled ✓; line 7 c ✓
- Warnings: failure-to-pay penalty not requested (user decision; lack of funds alone is
  generally not reasonable cause); FTP and interest continue on the $6,236 balance

## Mailing
Address: the return address printed on the notice dated 07/14/2025
Method: certified mail, return receipt requested; keep a full copy

## Next steps
- Consider a payment plan for the $6,236 balance (form-9465)
- If denied (Letter 854C): appeal within the period stated, generally 30 days;
  the balance is under $25,000, so a small case request is available (Publication 5)
```

## Reasoning notes

- **Why the agent asked about the 2022 letter:** a prior FTA inside the lookback is the most common reason an FTA request fails. The letter text "only available one time" identifies it.
- **Why only one penalty:** the hospital facts explain the late filing. They do not explain the shortfall of funds, which existed before the illness. Mixing both would weaken the filing request.
- **Why the medical details stay short:** the IRS needs dates and the link to the failure, not a medical history. The user decides what medical detail to disclose.
- **What the agent did not do:** draft a failure-to-pay argument the user did not choose, or describe the illness beyond the user's own words.
