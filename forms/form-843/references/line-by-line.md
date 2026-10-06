# Form 843 Line-by-Line Reference

Complete map of every field on Form 843 (Rev. December 2024), built from the text of the official PDF (https://www.irs.gov/pub/irs-pdf/f843.pdf) and the Instructions for Form 843 (Rev. December 2024) (https://www.irs.gov/pub/irs-pdf/i843.pdf). The form has two pages: page 1 holds the reason checkboxes, the identity block, and lines 1–4; page 2 holds lines 5–8, the signatures, and the paid preparer block.

Form 843 is not revised every year. Before using this map, open https://www.irs.gov/forms-pubs/about-form-843 and confirm the current revision is still "Rev. December 2024". If it changed, rebuild this map from the new PDF text.

---

## Reason checkboxes (top of page 1)

The instructions say: "You must check one box above the name block at the top of the form to indicate your reason for filing Form 843. Do not check more than one box." Exactly one box, always.

### Group "Tax"

| Box (label on the form) | Use when |
|---|---|
| Abatement or refund of tax other than income, estate, or gift tax | A non-income tax was over-assessed or overpaid and no other form applies. Employers cannot use it for FICA, RRTA, or income tax withholding |
| Abatement or refund of tax that can't be claimed on any form except Form 843 | The tax has no dedicated amended return or claim form |
| Refund to employee of excess social security, Medicare, or RRTA tax withheld by any one employer, but only if your employer will not adjust the overcollection | One employer over-withheld and refuses to fix it |
| Refund to employee of excess tier 2 RRTA tax when, for the year, you had more than one railroad employer and your total tier 2 RRTA tax withheld or paid exceeds the tier 2 limit | Multiple railroad employers |
| Refund to employee of social security, Medicare, or RRTA tax withheld in error, but only if your employer will not adjust the overcollection | Tax withheld from pay that was not subject to it (nonresident aliens: follow Pub. 519) |
| Abatement or refund of tier 1 RRTA tax for an employee representative | Employee representatives only |

### Group "Penalty"

| Box | Use when |
|---|---|
| Abatement or refund of a penalty or addition to tax due to reasonable cause or other reason allowed under the law | Failure-to-file, failure-to-pay, failure-to-deposit, accuracy-related and similar penalties. The instructions say this includes the section 6676 penalty (20% of an excessive refund claim) where the claim was due to reasonable cause. This is the box for most penalty relief requests, including First Time Abate |
| Abatement or refund of penalty imposed under section 6672 ... (Trust Fund Recovery Penalty) | TFRP. Before a refund claim, pay the divisible portion: one employee's share (employment taxes) or one transaction (excise) |
| Refund of penalty imposed under section 6695A for misstatements due to incorrect appraisals | Appraisers |
| Refund of penalty imposed under section 6715 for misuse of dyed fuel | Dyed fuel |
| Abatement or refund under section 6404(f) of a penalty or addition to tax attributable to erroneous written advice by the IRS | The IRS gave written advice in response to a specific written request and the penalty resulted from relying on it |

### Group "Interest"

| Box | Use when |
|---|---|
| Abatement or refund of interest due to IRS error or delay under section 6404(e)(1) | Interest accrued because of an unreasonable IRS error or delay in a ministerial or managerial act |
| Request for net interest rate of zero under Rev. Proc. 2000-26 | The taxpayer owed underpayment interest and was owed overpayment interest for the same period (IRC §6621(d)) |

### Group "Other"

| Box | Use when |
|---|---|
| Abatement or refund of assessed penalties, interest, or additions to tax because you were unable to read and timely respond to a standard print notice from the IRS | Visual impairment or disability. Line 8 must describe the disability, the notice and its date, when the taxpayer learned of the issue, and any request for an alternative format |
| Refund of branded prescription drug fee | Letter 4658 recipients |
| Refund of annual fee on health insurance providers | Letter 5067C recipients |
| Other (specify) | Anything not listed. Do NOT use it when a different form is required (see the routing rules in `wrong-form-routing.md`) |

**Interest on a penalty is not a separate box.** When a penalty is abated, the IRS removes the interest charged on that penalty automatically (https://www.irs.gov/payments/penalty-relief-for-reasonable-cause, "Interest relief").

---

## Identity block (page 1)

| Field | What goes here |
|---|---|
| Name of person requesting the refund or abatement | The taxpayer's name as on the related return. An entity uses its legal name |
| Social security number (SSN) | SSN, or ITIN wherever an SSN is requested |
| Name of spouse if filing Form 843 relating to a joint return | Spouse's name from the related joint return. Both spouses must then sign |
| Spouse's social security number (SSN) | Spouse's SSN or ITIN from that joint return |
| Address, Apt./room/suite no. | Current mailing address. P.O. box only if the post office does not deliver to the home |
| City, State, ZIP code | Current |
| Employer ID number (EIN) | Entities (partnership, corporation, estate, trust) enter the EIN instead of an SSN |
| Foreign country name / province / postal code | Foreign addresses only; do not abbreviate the country |
| Name and address shown on return if different from above | The name and address on the return the claim relates to, if either changed |
| Daytime telephone number | A number the IRS can call |

If the taxpayer moves after filing, Form 8822 (individuals) or Form 8822-B (businesses) updates the address (i843, "Address change").

---

## Line 1 — Tax period or fee year

"Enter the tax period or fee year. Prepare a separate Form 843 for each tax period or fee year."

| Situation | Beginning date | Ending date |
|---|---|---|
| Calendar-year Form 1040, 1120, 1065, 1120-S, 940 | 01/01/YYYY | 12/31/YYYY |
| Fiscal-year return | First day of the fiscal year | Last day of the fiscal year |
| Quarterly Form 941 (for example Q2 2025) | 04/01/2025 | 06/30/2025 |
| Branded prescription drug fee | Fee year on the beginning-date line | Blank |
| Net interest rate of zero request | Leave line 1 blank | Leave blank |

Copy the period from the IRS notice or account transcript. Never infer it.

## Line 2 — Amount to be refunded or abated

"Enter the dollar amount for which you are requesting a refund or an abatement."

- Penalty: the assessed penalty amount shown on the notice or transcript for that period. If several penalties on the same period are requested (for example failure to file and failure to pay), line 2 is their total and line 8 itemizes them.
- Interest under §6404(e): the interest attributable to the IRS error or delay, with the computation in line 8.
- Net interest rate of zero: line 2 may be left blank or filled.
- The failure-to-pay penalty keeps accruing on unpaid tax (IRS FTA page comparison table: "May continue to accrue until the tax is fully paid"). Enter the amount on the notice and ask in line 8 for abatement of any further accruals of the same penalty for the period.

## Line 3 — Date(s) of payment(s)

"Date(s) of payment(s) for which you are requesting a refund (MM/DD/YYYY)." Twelve slots, a through l; attach a sheet if more are needed.

- Fill only when asking for a refund of an amount already paid.
- Leave blank for an abatement of an unpaid assessment.
- Each date matters for the refund lookback under IRC §6511(b)(2). See `refund-and-interest-rules.md`.
- Skip line 3 for excess tier 2 RRTA and branded prescription drug fee claims; do not complete it for net-interest-zero requests.

## Line 4 — Type of tax or fee

"Check the box(es) with the type of tax or fee for which you are asking a refund or abatement. Or check the box(es) with the type of tax or fee to which the interest, penalty, or addition to tax is related. Check only one box unless an exception applies."

Boxes: a Employment, b Estate, c Gift, d Excise, e Income, f Fee, g Civil penalty.

- A late-filing penalty on Form 1040 relates to income tax: box e.
- A failure-to-deposit penalty on Form 941 relates to employment tax: box a.
- Box g "Civil penalty" exists for penalties that do not relate to one of the listed tax types. The instructions do not define it further; when unsure which box applies, ask the user or their CPA instead of guessing.
- Exceptions allowing more than one box: net interest rate of zero, and one §6404(e) error affecting several tax types.

## Line 5 — Type of fee or return

"Indicate the type of fee or return, if any, filed to which the tax, interest, penalty, or addition to tax relates. Check only one box unless an exception applies."

Boxes: a 706, b 709, c 940, d 941, e 943, f 944, g 945, h 990-PF, i 1040, j 1120, k 4720, l CT-2, m Branded Prescription Drug (BPD) Fee, n Other (specify).

- Box i "1040" also covers Form 1040-SR, 1040-NR, and 1040 (sp) (i843, Line 5).
- The form has no 1065 or 1120-S box. The instructions do not say which box to use for them; use n "Other (specify)" and write the exact form number (for example "1120-S") so the request cannot be routed to the wrong return. Tell the user this is the agent's reading, not an IRS rule.
- More than one box only for net-interest-zero requests and the multi-type §6404(e) exception.

## Line 6 — Internal Revenue Code section of the penalty

"If the claim or request involves a penalty, enter the Internal Revenue Code section on which the penalty is based." The instructions add: "Generally, you can find the Code section on the Notice of Assessment you received from the IRS."

Common entries (confirm against the notice):

| Penalty | IRC section |
|---|---|
| Failure to file a return | 6651(a)(1) |
| Failure to pay tax shown on the return | 6651(a)(2) |
| Failure to pay tax not shown, after notice and demand | 6651(a)(3) |
| Failure to file a partnership return | 6698(a)(1) |
| Failure to file an S corporation return | 6699(a)(1) |
| Failure to deposit | 6656 |
| Accuracy-related penalty | 6662 |
| Erroneous claim for refund | 6676 |
| Trust Fund Recovery Penalty | 6672 |

Leave blank when the request is only about interest or tax. Skip for excess tier 2 RRTA and BPD fee claims.

## Line 7 — Reason for the request (check one)

| Box | Text on the form | Use for |
|---|---|---|
| a | Interest was assessed as a result of IRS errors or delays | §6404(e)(1) interest abatement |
| b | A penalty or addition to tax was the result of erroneous written advice from the IRS | §6404(f); attach the written request, the IRS advice, and any report of adjustments |
| c | Reasonable cause or other reason allowed under the law can be shown | Reasonable cause, statutory exceptions, and administrative waivers such as First Time Abate |
| d | None of the above reasons apply | Anything else |

The instructions do not name First Time Abate. Box c ("other reason allowed under the law") is the closest wording for an administrative waiver; some preparers use box d. Either way, write "First Time Abate" in line 8. The IRS says taxpayers "don't need to specify FTA as the relief sought" and reviews eligibility from its own records (https://www.irs.gov/payments/penalty-relief-due-to-first-time-abate-or-other-administrative-waiver). Tell the user which box you chose and why.

Do not complete line 7 for net-interest-zero requests, excess tier 2 RRTA claims, or branded prescription drug fee claims.

## Line 8 — Explanation and computation

"Explain why you believe this claim or request should be allowed and show how you computed the amount shown on line 2. If you need more space, attach additional sheets."

Required content (i843, Line 8):
- The reasons in detail.
- The computation of the amount on line 2.
- Supporting evidence attached.
- On every attached sheet: name and SSN, ITIN, or EIN.

Situation-specific content:
- §6404(e) interest: type of tax; date of first written IRS notice about the deficiency or payment; the specific period for which abatement is requested; the circumstances; why failing to abate would be grossly unfair (i843, "How to request abatement of interest on a tax").
- Net interest rate of zero: the six items listed in i843 under "Requesting Net Interest Rate of Zero", and a statement that the overlapping period has been used only once for a §6621(d) request.
- Visual impairment: the four items listed under "Taxpayers With Visual Impairments and Disabilities".
- Excess tier 2 RRTA: identify the claim as "Excess tier 2 RRTA" and attach Forms W-2.
- BPD fee: identify as "Branded prescription drug fee", attach Form 8947, state whether anyone filed a previous claim for the same amount.

---

## Signature block (page 2)

| Field | Rule |
|---|---|
| Signature, title if applicable, date | The taxpayer. Corporations: a corporate officer authorized to sign, with title. Estates and trusts: the fiduciary |
| Spouse signature, date | Required when Form 843 relates to a joint return. "Both you and your spouse must sign" |
| Identity Protection PIN (taxpayer, spouse) | Enter the six-digit IP PIN only if the IRS issued one for that person. Ask the user; do not store it after the draft |
| Declaration | Signed under penalties of perjury |

Representatives: an authorized representative may file Form 843 only with Form 2848 attached (original or copy), signed by the taxpayer and covering this matter (i843, "Who Can File").

Decedents: a legal representative attaches a statement that they filed the decedent's return and still act as representative, or certified letters testamentary or administration, plus Form 1310 (i843, "Who Can File").

## Paid Preparer Use Only

A paid preparer signs and completes: printed name, signature, date, PTIN, self-employed checkbox, firm's name, firm's EIN, firm's address, phone. Someone who prepares Form 843 without charging does not sign this block (i843, "Paid Tax Return Preparer"). An AI agent never signs as preparer.

---

## Separate form rule

"Generally, you must file a separate Form 843 for each tax period or fee year or type of tax or fee" (i843, "Separate Form Required"). Exceptions:

1. Net interest rate of zero: one form can cover several periods.
2. §6404(e): one form when a single managerial or ministerial IRS act caused interest on several years or tax types; check the applicable line 4 boxes and explain in line 8.

Three years of late-filing penalties on Form 1040 means three Forms 843.
