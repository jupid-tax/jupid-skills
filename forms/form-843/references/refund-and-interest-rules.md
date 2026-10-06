# Refund Deadlines and Interest Rules for Form 843

Two timing questions decide whether a Form 843 can succeed: is the refund claim inside the IRC §6511 window, and does the interest request fit IRC §6404(e) or §6621(d)? Load this file whenever line 3 has a payment date or line 7a is checked.

Sources (re-verify each time):
- IRC §6511, https://www.law.cornell.edu/uscode/text/26/6511
- IRC §6513(a), https://www.law.cornell.edu/uscode/text/26/6513
- IRC §6665(a), https://www.law.cornell.edu/uscode/text/26/6665
- IRC §6404, https://www.law.cornell.edu/uscode/text/26/6404
- IRC §6622 (daily compounding), https://www.law.cornell.edu/uscode/text/26/6622
- Instructions for Form 843 (Rev. December 2024), https://www.irs.gov/pub/irs-pdf/i843.pdf
- IRS, Interest abatement (last reviewed 27-Jul-2026), https://www.irs.gov/payments/interest-abatement
- IRS, Quarterly interest rates (last reviewed 10-Sep-2026), https://www.irs.gov/payments/quarterly-interest-rates

---

## 1. Refund versus abatement

- **Abatement** removes an assessed amount that is still unpaid. Line 3 stays blank.
- **Refund** returns an amount already paid. Line 3 lists each payment date. The §6511 limits apply.
- A partly paid penalty is both: abatement of the unpaid part, refund of the paid part. Line 2 is the total; line 8 splits it.

Penalties and additions to tax are treated as "tax" for Title 26 purposes (IRC §6665(a)(2)), so the refund limits for tax apply to paid penalties.

## 2. The §6511 window

IRC §6511(a): a claim must be filed "within 3 years from the time the return was filed or 2 years from the time the tax was paid, whichever of such periods expires the later, or if no return was filed by the taxpayer, within 2 years from the time the tax was paid."

The i843 wording: "Generally, you must file a claim for a credit or refund within 3 years from the date you filed your original return or 2 years from the date you paid the tax, whichever is later."

Early returns: "any return filed before the last day prescribed for the filing thereof shall be considered as filed on such last day" (IRC §6513(a)). A return filed April 1 for an April 15 due date starts the 3-year clock on April 15.

Late returns: the clock starts on the actual filing date.

## 3. The §6511(b)(2) lookback cap

Filing inside the window is not enough; the refund is capped by when the money was paid.

| Claim filed | Refund cannot exceed |
|---|---|
| Within the 3-year period of §6511(a) | Tax paid within the 3 years before the claim, plus any extension of time to file (§6511(b)(2)(A)) |
| After the 3-year period but within 2 years of payment | Tax paid within the 2 years before the claim (§6511(b)(2)(B)) |

Payments made before the due date count as made on the due date for this purpose (§6513(a)).

### Worksheet

```
A. Return for the period filed on (actual date, or due date if filed early): __________
B. 3-year deadline = A + 3 years:                                            __________
C. Planned claim date (date Form 843 will be mailed):                        __________
D. Is C on or before B?                                                      Yes / No
E. If Yes: lookback start = C − 3 years (− extension period, if any):         __________
   If No:  lookback start = C − 2 years:                                      __________
F. Payments of the penalty or interest (dates and amounts, from line 3):
   date ______ amount ______  inside lookback? __
G. Maximum refund = sum of payments dated on or after the lookback start
H. If no payment falls inside the lookback, the refund claim is time-barred.
```

Never stretch a deadline. If C is within 30 days of B or of a 2-year payment deadline, tell the user to mail by certified mail now and keep the receipt.

### Deadlines for other requests

- Erroneous written advice (§6404(f)): request within the period allowed for collecting the penalty, or, if paid, within the refund claim period (i843).
- §6404(e) interest: the IRS interest abatement page lists "File your claim 3 years from when the return was originally filed or 2 years from the payment date of tax, whichever is later."
- Appeal of a penalty relief denial: generally 30 days from the denial letter (https://www.irs.gov/appeals/penalty-appeal).

## 4. Interest on penalties

When a penalty is reduced or removed, the IRS automatically reduces or removes the interest charged on that penalty (IRS reasonable cause and FTA pages, "Interest relief"). Do not file a separate interest claim for it.

Interest on the underlying tax is not removed by penalty relief. It is statutory and compounds daily (IRC §6622(a)). The only Form 843 routes for interest on tax are §6404(e) and the net interest rate of zero.

## 5. Interest abatement for IRS error or delay (§6404(e)(1))

### The six criteria (IRS interest abatement page)

1. Claim filed within 3 years of the original return or 2 years of the tax payment, whichever is later.
2. Interest for tax years beginning after December 31, 1978.
3. Interest on income, estate, gift, and certain excise taxes. "You may not request interest abatement on employment taxes." The i843 adds: interest can be abated only if it relates to taxes for which a notice of deficiency is required.
4. The error or delay occurred after the IRS contacted the taxpayer in writing about the examination, underpayment, or payment (§6404(e)(1), last sentence).
5. Neither the taxpayer nor the representative contributed to the error or delay ("no significant aspect" attributable to the taxpayer).
6. The error or delay was unreasonable and in a ministerial or managerial act.

### Definitions (i843; Treas. Reg. §301.6404-2)

- **Ministerial act:** "a procedural or mechanical act that does not involve the exercise of judgment or discretion and that occurs during the processing of your case after all prerequisites of the act, such as conferences and review by supervisors, have taken place."
- **Managerial act:** "an administrative act that occurs during the processing of your case involving the temporary or permanent loss of records or the exercise of judgment or discretion relating to management of personnel."
- A decision about how to apply federal tax law is neither. A general administrative decision (how to organize return processing, delay in a computer system) is not a managerial act (IRS interest abatement page).

IRS examples that qualify: delay in transferring an approved case to another office; delay in issuing a notice of deficiency once all prerequisites are done; a misplaced case file; a delay caused by sending an agent to training without reassigning cases. Examples that do not: delay while a tax shelter is examined; delay while Chief Counsel advice is requested.

### Amount

"Under IRC 6404(e)(1) we may only abate the amount of interest that accrues during the period in which the unreasonable error or delay occurred." Only interest on the liability the delay affected counts (for an audit delay: interest on the audit deficiency, not on the original balance due).

To estimate line 2:
1. Get the underpayment rate for each quarter from https://www.irs.gov/payments/quarterly-interest-rates.
2. Compound daily (IRC §6622(a)) on the balance (deficiency plus interest accrued so far) through the delay period.
3. The estimate is the difference between interest actually charged through the payment date and interest recomputed with no accrual during the delay period.
4. Label it an estimate; the IRS recomputes. Never invent a rate.

### Form 843 entries for §6404(e)

i843, "How to request abatement of interest on a tax":
- Top box: "Abatement or refund of interest due to IRS error or delay under section 6404(e)(1)".
- Lines 1–4. Line 3: dates of any payments of interest or tax for the period.
- Line 7: box a.
- Line 8: (1) type of tax; (2) when the IRS first notified the taxpayer in writing about the deficiency or payment; (3) the specific period for which abatement is requested; (4) the circumstances; (5) why failing to abate would be grossly unfair.
- One Form 843 may cover several years or tax types when a single IRS act caused the interest; check each applicable line 4 box.

A signed letter is an alternative to Form 843 (IRS interest abatement page).

### Tax Court review (§6404(h))

A taxpayer meeting the net-worth requirements of §7430(c)(4)(A)(ii) may ask the Tax Court to review a failure to abate interest for abuse of discretion. The petition can be filed after the earlier of the IRS final determination or 180 days after the claim was filed, and no later than 180 days after the final determination is mailed. Flag this to the user and recommend a tax professional; do not prepare a Tax Court petition.

## 6. Net interest rate of zero (§6621(d), Rev. Proc. 2000-26)

Use when the same taxpayer owed underpayment interest and was owed overpayment interest for overlapping periods.

Form 843 entries (i843):
- Top box: "Request for net interest rate of zero under Rev. Proc. 2000-26".
- Line 1 blank. Line 2 optional. Lines 4 and 5 completed; more than one box allowed. Lines 3, 6, 7 not completed.
- Line 8: (1) the periods of overpayment and underpayment; (2) when the underpayment was paid, if no longer outstanding; (3) when the refund was received, if no longer outstanding; (4) the overlap period and amount, with background documents; (5) a computation, or an explanation of why one cannot be made; (6) if more than one TIN, why they are the same taxpayer. Include the statement that the overlapping period has been used only once for a §6621(d) request.
- Documentation that the claimant is the taxpayer entitled to the overpayment interest.
- Mail to the service center where the most recent return was filed (i843, Where To File).

## 7. Interest that cannot be abated on Form 843

- Interest on employment taxes or excise taxes other than those requiring a notice of deficiency (i843).
- Interest related to the branded prescription drug fee (i843).
- Interest the taxpayer simply finds unfair, with no IRS ministerial or managerial error after written contact.

## 8. Suspension the IRS applies on its own (§6404(g))

For an individual who filed a timely return, if the IRS does not send a notice stating the liability and its basis within 36 months after the later of the filing date or the due date, interest and certain time-based penalties are suspended from the end of that 36-month period until 21 days after the notice. Exceptions include the §6651 penalties, fraud, tax shown on the return, gross misstatements, certain reportable and listed transactions, and criminal penalties. This is not a Form 843 request; if the user's facts fit and the IRS did not apply it, recommend a tax professional.
