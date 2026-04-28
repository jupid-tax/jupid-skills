# Form W-9 — Backup withholding (IRC §3406)

When a requestor must withhold 24% from payments to the W-9 payee, why, and how to stop it.

---

## What backup withholding is

Backup withholding (BUW) is a federal tax-withholding mechanism authorized by IRC §3406. It applies a flat 24% withholding rate to certain payments (compensation reportable on 1099-NEC, 1099-MISC, 1099-K, interest reported on 1099-INT, dividends on 1099-DIV, etc.) when the IRS doesn't trust that the payee will report the income correctly on their tax return.

The withheld amount is sent to the IRS in the requestor's name (the payor) on Form 945 and credited to the payee's tax account. The payee gets the money back when they file their tax return — but only if they file.

**Rate:** 24% (set by IRC §3406; tied to the lowest individual income tax bracket).

**Mechanism:** The requestor reduces each payment by 24% and remits that amount to the IRS quarterly via Form 945. At year-end, the requestor reports the BUW amount in **Box 4 of Form 1099** (federal income tax withheld). The payee credits this amount on Form 1040 Line 25c.

---

## When BUW applies

A requestor must apply backup withholding when ANY of these is true (IRC §3406(a)(1)):

1. **No TIN provided** — the payee never gave a W-9 and the requestor has no other valid TIN on file.
2. **Wrong TIN provided** — the IRS has notified the requestor that the TIN on file doesn't match IRS records (CP2100 / CP2100A notice).
3. **IRS notification of payee under-reporting** — the IRS has notified the payee that they previously under-reported interest or dividends, and the IRS has instructed the requestor to apply BUW.
4. **Payee fails to certify** — the payee didn't sign Part II of the W-9, or struck through item 2 inappropriately (only struck if IRS has notified them they ARE subject to BUW).

**Most common scenario:** Case 1 — the user delayed sending the W-9 and the cautious requestor started withholding 24% as a default.

---

## What BUW looks like in practice

Example: Maya Garcia, single-member LLC owner (Garcia Design LLC), bills a client $5,000 for a project. She hasn't sent the W-9 yet.

**Without BUW (W-9 on file):**
- Client pays Maya $5,000
- Year-end: client files 1099-NEC reporting $5,000 in Box 1
- Maya pays income tax + self-employment tax on the $5,000

**With BUW (no W-9):**
- Client pays Maya $5,000 × 76% = $3,800 (after 24% withholding)
- Client remits $1,200 to IRS via Form 945
- Year-end: client files 1099-NEC reporting $5,000 in Box 1, $1,200 in Box 4
- Maya files her tax return: reports $5,000 income, claims $1,200 BUW credit on Form 1040 Line 25c, gets the money back via refund or applied to her tax bill

The money is not lost — but it's frozen with the IRS until tax filing. For a freelancer with cash-flow concerns, that's effectively a 24% interest-free loan to the federal government.

---

## How to stop backup withholding once it's started

If the user is currently subject to BUW because of Case 1 (no W-9 on file):

1. **Send a properly completed W-9** to the requestor. Include valid TIN that matches IRS records.
2. **Confirm receipt** with the requestor's AP team — make sure the W-9 is logged in their vendor system.
3. **Going forward**, the requestor stops BUW on future payments.
4. **For payments already withheld** in the current year: the user claims the BUW credit on Form 1040 Line 25c at year-end. There is no mechanism to "claw back" already-withheld amounts mid-year — the user gets them via the year-end credit.

If the user is subject to BUW because of Case 2 (TIN mismatch — CP2100 notice):

1. The requestor sends the user a "B" notice asking for a corrected W-9.
2. The user has 30 days to respond with a corrected W-9 (matching name + TIN).
3. If the user fails to respond, BUW continues until they correct.
4. **Verify TIN matching** with the IRS via the TIN Matching Program (https://www.irs.gov/tax-professionals/taxpayer-identification-number-tin-matching) before sending the corrected W-9 — this catches the mismatch before the 30-day clock runs out.

If the user is subject to BUW because of Case 3 (IRS notification of under-reporting):

1. The IRS has sent the user a notice (CP2000 or similar) that they previously under-reported interest or dividend income.
2. The user must resolve the under-reporting before the IRS will notify the requestor that BUW can stop.
3. This typically requires filing an amended return (Form 1040-X) to report the missed income.
4. Once resolved, the IRS sends the user a "no longer subject" notice; the user gives that to the requestor along with a fresh W-9.

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

**Sole proprietors, individuals, and single-member LLCs are NEVER exempt from BUW.** A sole prop / SMLLC owner cannot claim Code 5 even if their LLC has elected S-corp status — the W-9 instructions specifically scope Code 5 to corporations as defined for federal income tax.

---

## OBBBA and the new 1099 threshold

Effective tax year 2026 (per OBBBA Section 112201), the 1099-NEC reporting threshold for ordinary commercial payments rose from $600 to $2,000. This affects whether the requestor must file a 1099 at year-end — but it does **not** change BUW rules.

A requestor who pays $1,500 in 2026 doesn't have to file a 1099-NEC, but they still must apply BUW if there's no W-9 on file. The W-9 obligation is independent of the 1099 reporting threshold.

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
- Form 1040 Line 25c — Other federal income tax withheld (where the user credits BUW on their return)
