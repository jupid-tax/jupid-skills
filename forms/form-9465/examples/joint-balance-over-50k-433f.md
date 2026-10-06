# Example: Joint Balance Over $50,000, Payment Below Line 10, Form 433-F Required

A married couple owes on two years of joint returns. The balance is over $50,000 and the payment they can afford is below the line 10 benchmark, so Form 433-F is required twice over, and the arithmetic shows the agreement may not pay in full before the collection statute ends (a possible partial payment installment agreement). The agent fills Part I, then stops and collects the Form 433-F data from the couple instead of estimating anything.

Sources used: Form 9465 (Rev. 9-2020); Instructions for Form 9465 (Rev. 7-2024), sections "Streamlined installment agreement", "Partial payment installment agreement (PPIA)", "Line 11a", "Line 11b", "Lines 21 and 22", "Where To File"; Form 433-F (Rev. 7-2024); irs.gov payment plans page.

## The users

- **Names**: Marcus and Elena Whitfield (fictional), married filing jointly
- **State**: California (Sacramento), a community property state
- **Household**: two children; family unit size 4
- **Income**: Marcus W-2; Elena self-employed consultant reporting on Schedule C
- **Returns**: 2023 and 2024 joint Forms 1040 filed on time; 2025 joint return filed on time and fully paid
- **Prior installment agreement**: none in the last 12 months

## Balances (from the notices and their account transcripts)

| Year | Form | Balance on most recent notice | Tax assessed (transcript) |
|---|---|---|---|
| 2023 | 1040 | $41,207.66 | 05/27/2024 |
| 2024 | 1040 | $22,915.08 | 06/09/2025 |

Line 6: they confirm no other balances. Line 8: no payment with the request.

## Line math

```
Line 5  = 41,207.66 + 22,915.08 = 64,122.74
Line 6  = 0.00
Line 7  = 64,122.74
Line 8  = 0.00
Line 9  = 64,122.74
Line 10 = 64,122.74 ÷ 72.0 = 890.59
Line 11a = 650.00 < 890.59
Line 11b: asked "Can you raise the payment to $890.59?" → No → leave 11b blank, check the box
Line 9 > 50,000 → Form 433-F required (independently of the 11b box)
```

## Why this may be a partial payment agreement

i9465 says a proposed payment that does not pay the balance in full by the Collection Statute Expiration Date (CSED) may be considered for a PPIA, which needs a financial statement and is reviewed periodically.

The agent computes only what the transcript supports and leaves interest out:
- CSED for 2023 is normally 10 years from assessment: 05/27/2034, unless suspended or extended (i9465; the transcript did not show suspension events, but the agent tells them the IRS's CSED controls).
- From 10/06/2026 to 05/27/2034 there are about 91.7 months, so 91 full monthly payments.
- 91 × $650 = $59,150, which is less than $64,122.74 **before any interest or penalty**.

So even ignoring interest, $650 a month does not clear the balance before the earliest CSED. The draft says: the IRS may treat this as a PPIA; the IRS will analyze Form 433-F and may set a different payment. Because a balance that cannot be paid within the collection period is also where an offer in compromise gets considered, the agent mentions `../../form-656/SKILL.md` and recommends a CPA or enrolled agent compare the two. It does not recommend either.

## Fee and channel

- OPA is not available for long-term plans over $50,000 combined (irs.gov OPA page). Form 9465 by mail.
- They chose direct debit: **$107** (irs.gov payment plans page, phone/mail column).
- Low-income check: 2025 joint AGI $96,410, family unit size 4 → above the $82,500 Form 13844 (Rev. 2-2026) amount for four people in the 48 contiguous states. Not low-income.

## The Part I draft

```markdown
# Form 9465 — DRAFT (Rev. September 2020)

This request is for Form(s): 1040
Tax year(s) or period(s): 2023 and 2024

## Part I
1a. Your name: Marcus Whitfield             SSN: •••-••-6630
    Spouse: Elena Whitfield                  Spouse SSN: •••-••-1958
    (same order as on the 2023 and 2024 returns)
    Address: 7902 Riverbend Way, Sacramento, CA 95831
    Foreign address fields: (blank)
1b. New address since last return: [ ] (not checked)
2.  Business name (no longer operating) / EIN: (blank — Elena's consulting is operating;
    balances are income tax)
3.  Home phone: (916) 555-0124   Best time: evenings
4.  Work phone: (916) 555-0171  Ext. 30   Best time: 12–1 pm
5.  Total owed per return(s)/notice(s):        $64,122.74
6.  Additional balances not on line 5:         $0.00
7.  Line 5 + line 6:                            $64,122.74
8.  Payment with this request:                  $0.00
9.  Amount owed (line 7 − line 8):              $64,122.74
10. Line 9 ÷ 72.0:                              $890.59
11a. Monthly payment:                           $650.00
11b. Revised monthly payment:                   (blank — cannot increase)
     [X] Can't increase to line 10; Form 433-F attached
12. Payment day each month:                     5
13a. Routing number:                            •••••0016 (users write the full number)
13b. Account number:                            •••••2284 (users write the full number)
13c. Low-income, unable to pay electronically:  [ ] (not checked)
14. Payroll deduction (Form 2159 attached):     [ ] (not checked)

Signature: Marcus Whitfield (wet signature)   Date: (date signed)
Spouse's signature: Elena Whitfield (wet signature)   Date: (date signed)
(Joint return: both must sign; the direct debit is not approved without both signatures.)

## Part II — not required (no default in the last 12 months; and line 9 exceeds $50,000,
## where Form 433-F is the required statement)

## Attachments
- [ ] Form 433-F (Rev. 7-2024), completed and signed — PENDING (see below)
```

## Where the agent stops

Form 433-F is a full financial statement. The agent does not estimate any figure on it. It sends the couple this list and waits:

1. **Section A, accounts and lines of credit**: every checking, savings, online/mobile (for example PayPal), money market, and investment account, with institution and current balance; and lines of credit.
2. **Section B, real estate**: each property, market value, loan balances, monthly payment.
3. **Section C, other assets**: vehicles (year, make, model, value, loan balance); whole-life insurance cash value; other assets.
4. **Section D, credit cards**: issuer, limit, balance, minimum payment.
5. **Section E, business information**: Elena's consulting — current-year profit and loss statement, monthly gross and net.
6. **Section F, employment**: Marcus's employer and gross and net pay per period; a current pay stub.
7. **Section G, non-wage household income**: Elena's net self-employment income per month (cash expenses only; Form 433-F says not to deduct depreciation), and any other income.
8. **Section H, monthly necessary living expenses**: actual amounts. For box 1 (food, housekeeping supplies, clothing, personal care, miscellaneous) and box 4 (medical), the Form 433-F instructions say to enter the IRS allowable standard, or the actual amount if it exceeds the standard; the standards are at https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards (effective June 29, 2026; re-check). Substantiation may be requested for amounts over the standards.

Community property note: California is a community property state, so even a non-liable spouse's income can count (i9465 "Lines 21 and 22"). Here both spouses are liable on joint returns, so both incomes go on Form 433-F anyway.

## Where it goes (after Form 433-F is complete)

Standalone request; Elena's Schedule C is on both returns in the request, so use the Schedule C, E, or F table. California is in the Ogden row:

```
Department of the Treasury
Internal Revenue Service
P.O. Box 9941
Stop 5500
Ogden, UT 84409
```

## Validation summary

- Math: lines 5, 7, 9, 10 recomputed; 91 × $650 = $59,150 vs $64,122.74 checked.
- 11a < line 10 and cannot increase → box checked. Pass.
- Line 9 > $50,000 → Form 433-F listed as required attachment. Pass (pending data).
- Joint return → names and SSNs in return order; two signatures. Pass.
- Address: Schedule C table, California → Ogden. Pass.
- Draft status: **NOT READY TO FILE** until Form 433-F is completed and signed.

## Sources cited in this draft

- Form 9465 (Rev. 9-2020) and Instructions (Rev. 7-2024)
- Form 433-F (Rev. 7-2024) and its instructions
- IRS payment plans page (fees updated March 3, 2026); IRS OPA page ($50,000 online limit)
- IRS Collection Financial Standards page
- Form 13844 (Rev. 2-2026) low-income table
