# Form 1099-K — Boxes Explained

Every box on Form 1099-K with examples and edge cases. Use this when the user's 1099-K has unusual entries or you need to explain what each number represents.

The 2026 form layout follows the post-2022 redesign that added monthly breakdown boxes (5a-5l). Older 1099-Ks (2021 and prior) had a different layout — if the user is asking about a prior-year form, check the form's revision date in the bottom-right corner.

---

## Filer (top of form, left)

The PSE — payment settlement entity. This is the platform that processed the payments and is required to file under IRC §6050W.

- **Name** — legal name of the PSE (e.g., "PayPal, Inc.", "Stripe Payments Company", "Etsy Payments, Inc.", "Uber Technologies, Inc.")
- **Address** — PSE's mailing address
- **Telephone** — PSE's contact number for tax questions (rarely useful in practice; corrections go through the platform's online help center)
- **PSE / EPF indicator** — "Payment Settlement Entity" (PSE) for direct processors; "Electronic Payment Facilitator" (EPF) for sub-processors. Doesn't change recipient reporting.

### Edge case — multiple PSEs from the same parent

A user may receive separate 1099-Ks from sister entities under the same parent (e.g., Square and Cash App, both Block Inc.). Each is a separate PSE. The user reconciles each independently.

### Edge case — international PSE

A user may receive a 1099-K from a non-US-based PSE that has a US filing obligation. The form looks the same; reconciliation is the same.

---

## Filer's federal identification number (top of form)

The PSE's EIN. Useful for identifying the PSE if the user has the form but isn't sure which platform issued it. Cross-reference against IRS / SEC records if needed.

---

## PAYER MADE DIRECT SALES OF $5,000 OR MORE checkbox

Almost never checked on a 1099-K. This box exists primarily for 1099-MISC; on 1099-K it's unused.

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

Definition (from IRS Form 1099-K instructions, January 2025 revision):

> "Enter the gross amount of the total reportable payment transactions for the calendar year through the payment card and third party network. Do not include any adjustments for credits, cash equivalents, discount amounts, fees, refunded amounts, or any other amounts."

**Critical**: gross is **before** all deductions. The user does NOT subtract platform fees, processing fees, refunds, chargebacks, or shipping costs from Box 1a. Those are handled as separate Schedule C deductions or Schedule C Line 2 (returns and allowances).

### Edge case — settlement date vs deposit date

Box 1a uses **settlement date**, not deposit date. A transaction settled December 30, 2026 but deposited to the user's bank January 2, 2027 still counts as 2026 gross.

### Edge case — refunds processed in next year

If a user has a $200 sale on December 28, 2026 that the buyer refunds on January 5, 2027, the refund **does not** reduce Box 1a for 2026. The user reports the $200 in 2026 gross and takes the $200 refund as a Schedule C Line 2 (Returns and allowances) deduction in 2027.

### Edge case — currency conversion

For international platforms (Stripe operating in multiple currencies, PayPal cross-border), Box 1a is reported in USD using the conversion rate at settlement. May differ slightly from the user's bank deposit USD due to FX timing.

---

## Box 1b — Card-not-present transactions

Subset of Box 1a where the card wasn't physically swiped (online-only sellers, almost always equal to Box 1a).

Informational only. Doesn't change the user's tax computation. Used by the IRS to identify online-only vs brick-and-mortar businesses.

---

## Box 2 — Number of payment transactions

Count of separate payment transactions during the year.

- Multiple sales to one buyer count as separate transactions
- One sale to many buyers (impossible in practice) would be one transaction
- Refunds are NOT counted as transactions in the count
- Voided / failed transactions are NOT counted

Used to verify the federal $20,000 / 200 threshold. Most filers are well above 200 transactions if they're getting a 1099-K at all (the dollar threshold usually triggers first).

---

## Box 3 — (currently reserved)

Not used in current revisions. Skip.

---

## Box 4 — Federal income tax withheld

Backup withholding under IRC §3406. The amount the PSE withheld (24% of payments) and remitted to the IRS on the user's behalf.

$0 for the vast majority of 1099-Ks. Non-zero only if:

- The user failed W-9 / TIN matching at any point during the year
- The IRS issued a "B" notice (CP2100) and the PSE began withholding
- The user is subject to a 1099-K-specific backup withholding for unrelated underreporting

If Box 4 > 0, the user **claims it on Form 1040 Line 25c** (Other federal income tax withheld). This is a refundable credit against total tax liability, treated identically to W-2 withholding.

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

Two-letter state code where the recipient is located (per the W-9 address). Used for state tax reporting.

If the user moved during the year and the W-9 address didn't update, Box 6 may be stale. Doesn't affect federal filing.

---

## Box 7 — State identification number

The PSE's state tax ID (varies by state). Informational.

---

## Box 8 — State income tax withheld

State backup withholding, if applicable. Most states don't have backup withholding; this is usually $0. If non-zero, claim on the user's state tax return as state withholding.

---

## Sources

- [Form 1099-K (current)](https://www.irs.gov/pub/irs-pdf/f1099k.pdf)
- [Instructions for Form 1099-K (current)](https://www.irs.gov/pub/irs-pdf/i1099k.pdf)
- IRC §6050W (returns relating to payment card and third-party network transactions)
- IRC §3406 (backup withholding)
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs)
