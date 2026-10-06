# Refund Claim Deadlines and the Lookback Cap (IRC §6511, §6513)

A Form 1040-X that claims a refund or credit is a claim under IRC §6511. Two separate tests apply, and both must be run:

1. **Timeliness**: was the claim filed inside the claim period?
2. **Amount**: how much tax was paid inside the lookback period that matches the claim? The refund cannot exceed that amount, even when the claim itself is timely.

A Form 1040-X that only **increases** tax has no claim deadline; the IRS's assessment period is a separate question (refer to a CPA if the user asks about it). Interest on additional tax runs from the original due date regardless.

---

## The rules

### Claim period — IRC §6511(a)

"Claim for credit or refund of an overpayment ... shall be filed by the taxpayer within 3 years from the time the return was filed or 2 years from the time the tax was paid, whichever of such periods expires the later." (IRC §6511(a), https://www.law.cornell.edu/uscode/text/26/6511)

The Instructions for Form 1040-X (Rev. December 2025, "When To File") restate it: within 3 years (including extensions) after the date the original return was filed, or within 2 years after the date the tax was paid, whichever is later.

### Lookback cap — IRC §6511(b)(2)

- **(A) Claim filed within the 3-year period**: the refund cannot exceed the tax paid within 3 years before the claim, **plus the period of any extension of time to file**.
- **(B) Claim not filed within the 3-year period**: the refund cannot exceed the tax paid within the 2 years immediately before the claim.

The instructions call this the "lookback period" ("Filing limits due to lookback period").

### Deemed filing date — IRC §6513(a)

A return filed **before** its due date is treated as filed on the due date, determined **without** extensions. Instructions examples:

- Filed early (for example March 1 for a calendar-year return) → considered filed on the due date (generally April 15).
- Had an extension to October 15 but the IRS received the return July 1 → considered filed July 1.

### Deemed payment dates — IRC §6513(b)

- Income tax **withheld** during the year is deemed paid on the 15th day of the fourth month after the tax year ends (§6513(b)(1)).
- **Estimated tax** is deemed paid on the last day prescribed for filing the return, without extensions (§6513(b)(2)).
- Tax withheld at source under chapter 3 or 4 (Form 1042-S, nonresidents) is deemed paid on the return due date without extensions (§6513(b)(3)).
- The instructions summarize: "Income tax withheld and estimated tax are considered paid on the due date of the return (generally April 15th for calendar-year taxpayers)."

Payments made **after** the due date (balance due paid late, an installment payment, a payment after a CP2000 or audit) are paid on the date actually paid. Those later payments are what keep a 2-year window open.

### Special periods (Instructions for Form 1040-X, "When To File" and "Special Situations")

| Situation | Period | Source |
|---|---|---|
| Bad debt or worthless security | Generally 7 years after the due date of the return for the year the debt or security became worthless | Instructions ("see section 6511") |
| Foreign tax credit (claiming it, or switching from deduction to credit) | Generally 10 years from the due date (without extensions) of the return for the year the foreign tax was paid or accrued | Instructions; Pub. 514 |
| Foreign tax **deduction** (or switching credit → deduction) | Normal 3-year/2-year rule | Instructions |
| NOL, capital loss, or credit carryback on Form 1040-X | Generally 3 years after the due date (including extensions) of the return for the year the loss or unused credit arose (10 years for a foreign tax credit, without extensions). Write "Carryback Claim" at the top | Instructions |
| Carryback on Form 1045 instead | Within 1 year after the end of the year the loss, credit, or claim-of-right adjustment arose | Instructions; Instructions for Form 1045 |
| Federally declared disaster or qualified State-declared disaster | Possibly more time. For claims filed after December 26, 2025, a §7508A postponement is treated as an extension, so the 3-year lookback is extended by the postponement period (Disaster Related Extension of Deadlines Act). State-declared disaster rule applies to declarations made after July 24, 2025 | Instructions, "Federally declared disasters", "State-declared disasters", "Special rules for certain claims filed after December 26, 2025" |
| Combat zone or contingency operation | Deadline may be automatically extended | Instructions; Pub. 3 |
| Physically or mentally unable to manage financial affairs (financial disability) | The claim period can be suspended | Instructions; Pub. 556 |
| Qualified wildfire relief payments, tax years 2022–2025 | Until the §6511(a) period for the year expires (2020–2021 claims had until the later of December 12, 2025 or the §6511 expiration) | Instructions, What's New |
| Section 174A election for 2022–2024 R&E expenditures (small business taxpayers) | Election deadline July 6, 2026 (Rev. Proc. 2025-28) | Instructions, What's New |
| Casualty loss from a federally declared disaster deducted in the prior year | Election made on the prior-year return or amendment no later than 6 months after the due date (without extensions) of the loss-year return | Instructions, "Casualty loss from a federally declared disaster"; Rev. Proc. 2016-53 |

If any special period may apply, collect the facts and route the user to a CPA; do not compute a special-period deadline from memory.

---

## Procedure the agent runs

Ask for each input; do not assume it.

1. **Original return**: "On what date did you file (or the IRS accept) the original return for YYYY? Did you file an extension (Form 4868)?" Get the e-file acceptance email or the certified-mail receipt if possible. If the user does not know, an IRS account transcript shows the return received date ([`../../form-4506-t/SKILL.md`](../../form-4506-t/SKILL.md)).
2. **Due date of the original**: take it from that year's Form 1040 instructions (it is not always April 15; the 2022 return was due April 18, 2023 because of the Emancipation Day holiday, per the 2022 Instructions for Form 1040).
3. **Deemed filing date** = the later of the actual filing date and the due date without extensions (§6513(a)).
4. **3-year window end** = deemed filing date + 3 years. (If a deadline falls on a Saturday, Sunday, or legal holiday, IRC §7503 moves it to the next business day; flag this, don't rely on it to rescue a late claim without a CPA.)
5. **Payments**: list every payment for the year with its date and amount: withholding (deemed paid per §6513(b)(1)), estimates (deemed paid per §6513(b)(2)), the amount paid with the return (paid on that date, or the due date if earlier — §6513(a)), extension payments, later payments, and any payment made after an IRS notice. **Exclude interest and penalties**; they are not tax.
6. **2-year window end** = date of the latest tax payment + 2 years.
7. **Timeliness**: the claim is timely if the planned filing date is on or before the later of the two window ends.
8. **Lookback cap**:
   - If filing inside the 3-year window: cap = tax paid within 3 years (plus any extension period) before the planned filing date. For a return filed on time with withholding, this usually covers everything.
   - Otherwise: cap = tax paid within the 2 years before the planned filing date.
9. **Compare**: if Form 1040-X line 21 exceeds the cap, the excess cannot be refunded or credited. Show the computed line 21, state the cap and the barred amount in the deliverable, and ask the user to have a CPA confirm how to present lines 22–23 and Part II (see the worked case in [`../examples/statute-cap-2022.md`](../examples/statute-cap-2022.md)). The 20% erroneous refund claim penalty in the instructions is a reason to get this right.
10. **Record** every date and its source in the "Statute check" block of the deliverable.

### Worked date checks

| Case | Deemed filed | 3-year window ends | Notes |
|---|---|---|---|
| 2025 return e-filed February 21, 2026, no extension | April 15, 2026 (due date per 2025 Instructions for Form 1040) | April 15, 2029 (a Sunday; §7503 moves it to the next day that is not a weekend or DC legal holiday) | Withholding deemed paid April 15, 2026, inside the lookback |
| 2024 return filed March 3, 2025 | April 15, 2025 (due date per 2024 Instructions for Form 1040) | April 15, 2028 | |
| 2022 return filed February 27, 2023 | April 18, 2023 (due date per 2022 Instructions for Form 1040) | April 18, 2026 — passed as of October 2026 | Only a 2-year window from a later payment can remain |
| Return on extension, received July 1 | July 1 (instructions example) | July 1 + 3 years | Lookback under §6511(b)(2)(A) adds the extension period |

---

## What the user must keep

- Proof of the original filing date (e-file acknowledgment or mailing receipt).
- Proof of every payment date (bank records, IRS account transcript).
- Proof of the Form 1040-X filing date: e-file acceptance, or certified mail / IRS-designated private delivery service receipt for paper (the "timely mailing as timely filing" rule; current PDS list at IRS.gov/PDS, per the Instructions for Form 1040-X).
