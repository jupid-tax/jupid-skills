# Form W-9 — Backup withholding (IRC §3406)

When a requestor must withhold 24% from payments to the W-9 payee, why, and how to stop it.

---

## What backup withholding is

Backup withholding (BUW) is a federal tax-withholding mechanism authorized by IRC §3406. It applies a flat 24% withholding rate to certain reportable payments (compensation reportable on 1099-NEC, 1099-MISC, 1099-K, interest reported on 1099-INT, dividends on 1099-DIV, etc.) when the payee hasn't furnished a correct TIN or, for interest and dividends, the IRS has flagged underreporting.

The withheld amount is sent to the IRS in the requestor's name (the payor) on Form 945 and credited to the payee's tax account. The payee gets the money back when they file their tax return — but only if they file.

**Rate:** 24% (IRC §3406(a)(1): the fourth lowest rate under §1(c), which is 24% under §1(j)(2)(C)).

**Mechanism:** The requestor reduces each payment by 24%, deposits the withholding under the Form 945 deposit rules (monthly or semiweekly; Pub. 15), and reports the year's total on Form 945 line 2. At year-end, the requestor reports the BUW amount in **Box 4 of Form 1099** (federal income tax withheld). The payee credits this amount on Form 1040 Line 25b (2025 form).

---

## When BUW applies

A requestor must apply backup withholding when ANY of these is true (IRC §3406(a)(1)):

1. **No TIN provided** — the payee never gave a W-9 and the requestor has no other valid TIN on file.
2. **Wrong TIN provided** — the IRS has notified the requestor that the TIN on file doesn't match IRS records (CP2100 / CP2100A notice).
3. **IRS notification of payee under-reporting** — interest and dividend payments only: the IRS has notified the requestor that the payee under-reported interest or dividends (§3406(a)(1)(C)).
4. **Payee fails to certify** — interest and dividend accounts only: the payee didn't certify that they are not subject to BUW (§3406(a)(1)(D)); for those accounts opened after 1983, an unsigned W-9 triggers BUW (W-9 "Signature requirements" item 2).

**Most common scenario:** Case 1 — the user delayed sending the W-9 and the requestor started withholding 24%.

**Threshold link (P.L. 119-21 §70433(d)):** for payments reportable under §6041 or §6041A (rents, services, medical, etc.), backup withholding applies only once the year's payments to the payee reach the §6041(a) amount — $600 for 2025, $2,000 for 2026 (IRC §3406(b)(6)). For third party network payments, only once the $20,000 / 200-transaction 1099-K test is met (IRC §3406(b)(8), calendar years after 2024).

---

## What BUW looks like in practice

Example: Maya Garcia, single-member LLC owner (Garcia Design LLC), bills a client $5,000 for a project. She hasn't sent the W-9 yet.

**Without BUW (W-9 on file):**
- Client pays Maya $5,000
- Year-end: client files 1099-NEC reporting $5,000 in Box 1a (2026 form)
- Maya pays income tax + self-employment tax on the $5,000

**With BUW (no W-9):**
- Client pays Maya $5,000 × 76% = $3,800 (after 24% withholding)
- Client remits $1,200 to IRS via Form 945
- Year-end: client files 1099-NEC reporting $5,000 in Box 1a, $1,200 in Box 4
- Maya files her tax return: reports $5,000 income, claims $1,200 BUW credit on Form 1040 Line 25b, gets the money back via refund or applied to her tax bill

The money is not lost — but it's frozen with the IRS until tax filing. For a freelancer with cash-flow concerns, that's effectively a 24% interest-free loan to the federal government.

---

## How to stop backup withholding once it's started

If the user is currently subject to BUW because of Case 1 (no W-9 on file):

1. **Send a properly completed W-9** to the requestor. Include valid TIN that matches IRS records.
2. **Confirm receipt** with the requestor's AP team — make sure the W-9 is logged in their vendor system.
3. **Going forward**, the requestor stops BUW on future payments.
4. **For payments already withheld** in the current year: the user claims the BUW credit on Form 1040 Line 25b at year-end. A payor may, at its option, refund or adjust over-withheld amounts within the same calendar year (IRS FS-2025-08 Q9 describes this for 1099-K payors); otherwise the user gets them via the year-end credit.

If the user is subject to BUW because of Case 2 (TIN mismatch — CP2100 notice):

1. The requestor sends the user a "B" notice asking for a corrected, signed W-9.
2. The requestor must start BUW on payments made after 30 business days from its receipt of the IRS notice unless the user has supplied a corrected TIN by then (Pub. 1099 (2026), part N; Reg. §31.3406(d)-5). Respond quickly.
3. After a second notice for the same account within 3 years, a new W-9 is not enough: the user must have the SSA (SSN) or IRS (EIN, e.g., Letter 147C) validate the TIN (Pub. 1281).
4. The IRS TIN Matching Program is for payers, not payees. The user checks the name and TIN against the Social Security card or the IRS EIN notice (CP 575 / 147C) before sending the corrected W-9.

If the user is subject to BUW because of Case 3 (IRS notification of under-reporting):

1. The IRS has sent the user a notice (CP2000 or similar) that they previously under-reported interest or dividend income.
2. BUW continues until the IRS determines it should stop (IRC §3406(c)(2): no underreporting, underreporting corrected, undue hardship, or a bona fide dispute). Follow the notice's instructions; filing or paying for the missed income may be part of it.
3. Once resolved, the IRS notifies the payer (and the user); the user can then give the requestor a fresh W-9 without striking item 2.

---

## The "Item 2" decision in W-9 Part II

Part II of W-9 has the certification:

> "I am not subject to backup withholding because: (a) I am exempt from BUW, OR (b) I have not been notified by the IRS that I am subject to BUW for failing to report all interest or dividends, OR (c) the IRS has notified me that I am no longer subject to BUW."

By signing without modification, the user attests that one of (a), (b), or (c) is true.

**If the user is currently subject to BUW per Case 3** (IRS has notified them, they have NOT yet been told they're no longer subject), they must **strike through Item 2** before signing. This puts the requestor on notice to apply BUW.

**If the user is subject to BUW per Case 1 or Case 2**, that's a different mechanism — Item 2 is about *under-reporting* notifications specifically, not about TIN issues. For Case 1 / 2, the user does NOT strike Item 2.

In practice, very few filers strike Item 2. If the user can't recall ever receiving an IRS notice about under-reported interest or dividends, they should leave Item 2 unstruck.

---

## Exempt payees (Line 4 — exempt payee codes)

Certain payees are exempt from BUW under IRC §3406(g) and the W-9 instructions. They enter an exempt payee code on Line 4. Common codes:

- **Code 1** — §501(a) tax-exempt orgs, IRAs, §403(b)(7) custodial accounts
- **Code 2** — US government and instrumentalities
- **Code 3** — State, DC, US commonwealth, political subdivisions
- **Code 5** — Corporations (most C-corps and S-corps are exempt from BUW on most payments — note exceptions for legal services and medical services)
- **Code 11** — Banks and §581 financial institutions

**Individuals, sole proprietors, and disregarded single-member LLCs are generally not exempt from BUW** (W-9 instructions, "Exempt payee code"). An LLC that elected S or C corporation status gives its own W-9 and may enter Code 5 where the W-9 chart allows — not for card / third-party network settlements, attorneys' fees or gross proceeds, or medical payments reportable on 1099-MISC, and an S corporation never for broker transactions.

---

## OBBBA and the new 1099 threshold

For payments made after December 31, 2025, P.L. 119-21 §70433 raised the §6041(a) / §6041A reporting threshold from $600 to $2,000 (indexed from 2027). The same section amended IRC §3406(b)(6), so backup withholding on these payments is tied to the same amount: it applies only once the year's payments to the payee reach $2,000 (2026).

A requestor who pays a contractor $1,500 in total in 2026 doesn't file a 1099-NEC and has no backup withholding duty on those payments, W-9 or not. Many requesters still collect a W-9 up front because they can't know the year's total in advance.

---

## Validation for the agent

When the agent finishes a W-9 draft for a user who is currently subject to BUW:

- [ ] Confirm whether Item 2 should be struck — explicit yes/no from the user
- [ ] If user is subject to BUW per Case 3 (under-reporting), Item 2 IS struck
- [ ] If user is subject to BUW per Case 1 / 2 (TIN issues), Item 2 is NOT struck — fixing those cases is via providing a valid W-9, not via the certification
- [ ] If user has received an IRS BUW notice they don't fully understand, advise consulting a tax pro before completing the W-9 — wrong handling of Item 2 leads to perjury risk on the certification

---

## Sources

- IRC §3406 — Backup withholding requirements
- IRS Topic No. 307 — Backup Withholding (https://www.irs.gov/taxtopics/tc307)
- IRS Publication 1281 — Backup Withholding for Missing and Incorrect Name/TIN(s) (https://www.irs.gov/pub/irs-pdf/p1281.pdf)
- IRS TIN Matching Program — https://www.irs.gov/tax-professionals/taxpayer-identification-number-tin-matching
- Form 945 — Annual Return of Withheld Federal Income Tax (the form requestors use to remit BUW to IRS)
- Form 1099-NEC Box 4 — Federal income tax withheld (where BUW shows up on the year-end form)
- Form 1040 Line 25b — Federal income tax withheld from Form(s) 1099 (2025 form; where the user credits BUW on their return)
- IRC §3406(b)(6) and (b)(8) as amended by P.L. 119-21 §§70432–70433
- Pub. 1099 (2026), part N; Reg. §31.3406(d)-5 (B-notice timing)
- Form W-9 (Rev. March 2024), "Exempt payee code" and "Signature requirements"
