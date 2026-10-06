# Form 1099-K — Boxes Explained

Every box on Form 1099-K with examples and edge cases. Use this when the user's 1099-K has unusual entries or you need to explain what each number represents.

Verified against Form 1099-K (Rev. December 2026), used for 2026 transactions, and Form 1099-K (Rev. March 2024), used for 2024 and 2025 transactions, plus the Instructions for Form 1099-K (Rev. December 2026). The two revisions share boxes 1a, 1b, 2–4, 5a–5l and 6–8; Rev. December 2026 adds boxes 1c and 1d and splits the address fields. Check the revision printed under the form number before reading boxes. Re-check https://www.irs.gov/forms-pubs/about-form-1099-k for a newer revision.

---

## Filer (top of form, left)

The PSE — payment settlement entity. This is the platform that processed the payments and is required to file under IRC §6050W.

- **Name** — legal name of the PSE (e.g., "PayPal, Inc.", "Stripe Payments Company", "Etsy Payments, Inc.", "Uber Technologies, Inc.")
- **Address** — PSE's mailing address
- **Telephone** — the instructions require a number that reaches someone knowledgeable about the payments; corrections are requested from this filer
- **Filer checkbox** — "Payment settlement entity (PSE)" or "Electronic payment facilitator (EPF)/Other third party". If an EPF filed, the PSE's name and phone appear above the account number at the bottom left. Doesn't change recipient reporting.
- **Transactions reported checkbox** — "Payment card" or "Third party network". A payee with both types gets a separate 1099-K for each type. The $20,000 / 200 de minimis test applies only to third party network transactions; payment card transactions have no minimum (Instructions for Form 1099-K, Box 1a; FS-2025-08).

### Edge case — multiple PSEs from the same parent

A user may receive separate 1099-Ks from sister entities under the same parent (e.g., Square and Cash App, both Block Inc.). Each is a separate PSE. The user reconciles each independently.

### Edge case — international PSE

A user may receive a 1099-K from a non-US-based PSE that has a US filing obligation. The form looks the same; reconciliation is the same.

---

## Filer's federal identification number (top of form)

The PSE's EIN. Useful for identifying the PSE if the user has the form but isn't sure which platform issued it. Cross-reference against IRS / SEC records if needed.

---

## 2nd TIN not. checkbox

Marked by the filer when the IRS notified it twice within 3 calendar years that the payee's TIN was incorrect. If marked, ask the user whether they received a B notice and fix the TIN with the filer.

---

## Recipient's TIN

The user's SSN or EIN as provided on the W-9 to the platform. Must match the user's tax-return filing TIN exactly.

### Edge case — mismatch

If the recipient TIN on the 1099-K is different from the user's actual SSN/EIN, the form is unusable as filed. Two paths:

1. **Mistype on the 1099-K** — request a corrected form from the PSE
2. **User provided wrong TIN on W-9** — update the W-9 with the platform; the next 1099-K will be correct, but the current-year form needs to be corrected

If the TIN was wrong on the W-9, the user may have been subject to backup withholding (24%, IRC §3406) for part of the year — Box 4 will be non-zero in that case.

---

## Recipient's name + address

The user's name + address as provided on the W-9. Should match the user's tax-return name.

### Edge case — name change

If the user got married / divorced / changed their legal name during the year, the 1099-K may show the old name. Not a problem for filing as long as the TIN matches; for next year, update the W-9.

---

## Account number (lower-left)

The platform's internal account ID for the user. Useful for the user's records (helps identify which platform account the form covers if the user has multiple).

---

## Box 1a — Gross amount of payment card / third party network transactions

The headline number. **This is the dollar amount the IRS document-matching system uses.**

Definition (Instructions for Form 1099-K, Rev. December 2026, Box 1a):

> "'Gross amount' means the total dollar amount of total reportable payment transactions for each participating payee without regard to any adjustments for credits, cash equivalents, discount amounts, fees, refunded amounts, shipping amounts, or any other amounts. The dollar amount of each transaction is determined on the date of the transaction."

**Critical**: gross is **before** all deductions. The user does NOT subtract platform fees, processing fees, refunds, chargebacks, or shipping costs from Box 1a. Those are handled as separate Schedule C deductions or Schedule C Line 2 (returns and allowances).

### Edge case — settlement date vs deposit date

Box 1a uses **settlement date**, not deposit date. A transaction settled December 30, 2026 but deposited to the user's bank January 2, 2027 still counts as 2026 gross.

### Edge case — refunds processed in next year

If a user has a $200 sale on December 28, 2026 that the buyer refunds on January 5, 2027, the refund **does not** reduce Box 1a for 2026. The user reports the $200 in 2026 gross and takes the $200 refund as a Schedule C Line 2 (Returns and allowances) deduction in 2027.

### Edge case — currency conversion

For international platforms (Stripe operating in multiple currencies, PayPal cross-border), Box 1a is reported in USD converted at the spot rate on the date of the transaction, or a consistent spot-rate convention such as a monthly average (Instructions for Form 1099-K, "Conversion of amounts paid in foreign currency"). May differ slightly from the user's bank deposit USD due to FX timing.

---

## Box 1b — Card not present transactions

Subset of Box 1a where the card was not present at the time of the transaction or the card number was keyed into the terminal (online, phone, catalog sales). Copy B instructions: if the third party network box is checked, card not present transactions are not reported, so Box 1b is blank on payment-app and marketplace forms.

Informational only. Doesn't change the user's tax computation.

---

## Boxes 1c and 1d — Cash tips and TTOC (Rev. December 2026 only)

- **Box 1c** — total cash tips included in Box 1a (P.L. 119-21 §70201)
- **Box 1d** — up to two Treasury Tipped Occupation Codes; code 000 alone means the tips are not qualified tips

The recipient uses them for the qualified tips deduction in Part II of Schedule 1-A. That deduction is outside this skill. The Rev. March 2024 form used for 2025 has no Box 1c or 1d.

---

## Box 2 — Merchant category code

Four-digit merchant category code (MCC) for payment card transactions. A TPSO, or a filer that uses no industry classification, leaves it blank. Informational.

---

## Box 3 — Number of payment transactions

Count of payment transactions during the year, not including refund transactions.

- Multiple sales to one buyer count as separate transactions
- Refunds are NOT counted

Used to check the federal $20,000 / 200 test on third party network forms. A form with 200 or fewer transactions, or $20,000 or less, may still arrive: payment card forms have no minimum, a TPSO may file voluntarily, and some states set lower thresholds (FS-2025-08, General information Q5).

---

## Box 4 — Federal income tax withheld

Backup withholding under IRC §3406. The amount the PSE withheld (24% of payments) and remitted to the IRS on the user's behalf.

$0 for the vast majority of 1099-Ks. Non-zero only if:

- The user failed W-9 / TIN matching at any point during the year
- The IRS issued a "B" notice (CP2100) and the PSE began withholding

For third party network payments, backup withholding applies only when the $20,000 / 200 test is met (IRC §3406(b)(8), calendar years after 2024).

If Box 4 > 0, the user **claims it on Form 1040 Line 25b** (Form(s) 1099). This is a refundable credit against total tax liability, treated identically to W-2 withholding.

### Edge case — Box 4 surprise

If the user is surprised by a non-zero Box 4, work backward: when did backup withholding start? Usually the PSE sent a notice asking for a corrected W-9; ignoring that notice triggered the 24% withholding. Fix the W-9 to stop future withholding; claim the Box 4 amount on this year's return.

---

## Boxes 5a through 5l — Monthly gross

Box 1a broken out by month:

- Box 5a — January
- Box 5b — February
- Box 5c — March
- Box 5d — April
- Box 5e — May
- Box 5f — June
- Box 5g — July
- Box 5h — August
- Box 5i — September
- Box 5j — October
- Box 5k — November
- Box 5l — December

Sum of Boxes 5a-5l should equal Box 1a (small rounding allowed).

### Use cases

- **Spot timing issues** — December settlements that deposited in January
- **Cross-check against bank deposits** — month-by-month verification
- **Identify seasonal patterns** — useful for the user's own books
- **Detect mid-year account changes** — a sudden drop or jump may flag an account split or merger

---

## Box 6 — State

Abbreviated name of the state the filer reports to. Up to two states per form. Used for state tax reporting.

If the user moved during the year and the W-9 address didn't update, Box 6 may be stale. Doesn't affect federal filing.

---

## Box 7 — State identification number

The filer's identification number assigned by the state. Informational.

---

## Box 8 — State income tax withheld

State income tax the filer withheld, if any. Usually $0. If non-zero, claim on the user's state tax return as state withholding.

---

## Sources

- [Form 1099-K (current)](https://www.irs.gov/pub/irs-pdf/f1099k.pdf)
- [Instructions for Form 1099-K (current)](https://www.irs.gov/pub/irs-pdf/i1099k.pdf)
- IRC §6050W (returns relating to payment card and third-party network transactions)
- IRC §3406 (backup withholding), including §3406(b)(8)
- [IRS Form 1099-K FAQs, FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf)
