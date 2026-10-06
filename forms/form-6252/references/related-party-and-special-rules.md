# Related Parties and Special Rules

Rules that change when or how much installment gain is reported. Sources: 2025 Form 6252 instructions (pages 2–4 of https://www.irs.gov/pub/irs-pdf/f6252.pdf), Pub. 537 (2025) "Other Rules" (https://www.irs.gov/pub/irs-pdf/p537.pdf), IRC §453, §453A, §453B (https://www.law.cornell.edu/uscode/text/26/453, https://www.law.cornell.edu/uscode/text/26/453A).

Ask the user each question below before computing. Do not infer relationships or note events from silence.

---

## 1. Two different related-party rules

| Rule | What it does | Who is related (Pub. 537) | Where |
|------|--------------|---------------------------|-------|
| **Sale and later disposition, §453(e)** | If the related buyer disposes of the property before paying in full and within 2 years of the first sale (no 2-year limit for marketable securities), the seller is treated as receiving the related party's amount realized (or FMV if not sold or exchanged) at the time of the second disposition. | Family (siblings whole or half, spouse, ancestors, lineal descendants); partnership or estate and a partner or beneficiary; trust (other than a §401(a) employees' trust) and a beneficiary; trust and an owner; two corporations in the same controlled group (§267(f)); fiduciaries of two trusts with the same grantor, and the fiduciary and beneficiary of two such trusts; tax-exempt educational or charitable organization and a person (and family) who controls it; individual and a corporation more than 50% owned by value; fiduciary of a trust and a corporation more than 50% owned by the trust or grantor; grantor and fiduciary, and fiduciary and beneficiary, of any trust; two S corporations, or an S and a C corporation, with the same persons owning more than 50% of each; a corporation and a partnership with the same persons owning more than 50% of each; executor and beneficiary of an estate unless the sale satisfies a pecuniary bequest. The Form 6252 instructions summarize this as spouse, child, grandchild, parent, or sibling, or a related corporation, S corporation, partnership, estate, or trust (§453(f)(1)). | Form 6252 Part III, lines 27–37 |
| **Depreciable property to a related person, §453(g)** | The installment method generally is not allowed: all payments to be received are treated as received in the year of sale (noncontingent payments plus FMV of contingent ones). Exception: the seller shows to the IRS's satisfaction that tax avoidance was not a principal purpose (for example, no significant tax deferral benefit). If the FMV of contingent payments cannot be reasonably determined, basis is recovered proportionately. "Depreciable property" means property the buyer can depreciate. | A person and all controlled entities with respect to that person (§1239(c)); a taxpayer and any trust in which the taxpayer or spouse is a beneficiary (unless a remote contingent interest); an executor and a beneficiary of an estate, except a sale in satisfaction of a pecuniary bequest; two or more partnerships in which the same person owns, directly or indirectly, more than 50% of capital or profits. | No Form 6252; report on Form 4797, Form 8949, or Schedule D |

Ask: "Is the buyer a family member, or an entity or trust that you, your spouse, or your family control? Will the buyer depreciate the property?" If the §453(g) rule may apply, stop and refer the user to a CPA before any computation; the exception requires a showing to the IRS.

### Part III mechanics (§453(e))

- Complete Part III for the year of sale and the 2 years after the year of sale, unless the final payment came during the tax year (Form 6252, line 3 and Part III header).
- Line 29 exceptions (skip lines 30–37 if any applies): (a) second disposition more than 2 years after the first (not marketable securities), with the date; (b) the first disposition was a sale or exchange of stock to the issuing corporation; (c) the second disposition was an involuntary conversion and the threat of conversion arose after the first disposition; (d) the second disposition occurred after the death of the original seller or buyer; (e) tax avoidance was not a principal purpose of either disposition, with an attached explanation.
- Box 29e generally fits an involuntary second disposition (foreclosure by the related party's creditor, bankruptcy) or a resale on installment terms substantially equal to or longer than the first sale that does not permit significant deferral (Form 6252 instructions, line 29).
- After a second disposition, later principal payments already counted on line 34 go on line 23, not line 21 (line 21 instructions). They produce no further gain.

### Pub. 537 check figures (Example 1 and 2, "Sale and Later Disposition")

```
2024 sale of farmland to child for $500,000, five equal annual payments; installment sale basis $250,000
Gross profit percentage = 250,000 ÷ 500,000 = 0.50; 2024 payment 100,000 → 50,000 income

Example 1 (child resells in 2025 for $600,000 after paying 2025's $100,000):
  smaller of 600,000 or 500,000                = 500,000
  minus payments 2024 + 2025                   − 200,000
  treated as received                          = 300,000
  plus 2025 payment                            + 100,000
  total for 2025 × 0.50                        = 200,000 income
  2026–2028 payments: no further income

Example 2 (resale for $400,000):
  400,000 − 200,000 = 200,000; + 100,000 = 300,000; × 0.50 = 150,000 income for 2025
  2026 and 2027 payments not taxed; 2028 final $100,000:
  500,000 total − 400,000 already taxed = 100,000 × 0.50 = 50,000 income
```

Reproduce these numbers when testing a Part III implementation.

---

## 2. Electing out of the installment method (§453(d))

- **How:** do not file Form 6252; report the selling price and full gain on Form 4797, Form 8949, or Schedule D on a timely filed return, including extensions (Form 6252 instructions; Pub. 537 "How to elect out").
- **When:** by the due date, including extensions, of the return for the year of sale. A taxpayer who filed on time without electing can elect on an amended return filed within 6 months of the due date of the return, excluding extensions, with "Filed pursuant to section 301.9100-2" at the top (Form 6252 instructions; Pub. 537 "Automatic 6-month extension"). Route the amended return to [`../../form-1040-x/SKILL.md`](../../form-1040-x/SKILL.md).
- **Amount realized when electing out:** for a buyer's note that is a debt instrument, use Reg. §1.1001-1(g); generally the issue price of the note (Pub. 537 "Electing Out"). Pub. 537's example: $50,000 land, $10,000 down, $40,000 note with adequate interest (issue price $40,000), basis $25,000, commission $3,000 → $22,000 gain recognized in the year of sale; later principal payments are not income; interest is.
- **Revocation:** only with IRS approval, retroactive, and not allowed if one purpose is tax avoidance or if the tax year in which any payment was received has closed (Pub. 537).

The decision is tax planning. Present both computations (all gain now versus the installment schedule) and refer the choice to a CPA.

---

## 3. Pledge rule (§453A(d))

If an installment obligation is pledged as security for a debt, the net proceeds of the secured debt are treated as a payment on the obligation (Form 6252 instructions, "Pledge Rule"; Pub. 537).

- Applies to installment sales after 1988 with a sales price over $150,000.
- Does not apply to personal-use property disposed of by an individual, farm property, or timeshares and residential lots (line 1 codes 2, 3, 1).
- Limit: the amount treated as a payment cannot exceed the total contract price minus payments received before the debt was secured (Pub. 537 "Limit").
- For sales after Dec. 16, 1999, a debt is directly secured by the obligation to the extent an arrangement allows the seller to satisfy the debt with the obligation.
- Later payments on the pledged note are not reported until they exceed the amount already reported under the pledge rule (Pub. 537 "Installment payments").
- Refinancing exception for debts outstanding on Dec. 17, 1987 that were secured by the obligation then and continuously after (Form 6252 instructions).

Ask: "Did you borrow money using the buyer's note as collateral?" A "yes" adds a deemed payment to line 21 for the year (and to line 23 later).

---

## 4. Interest on deferred tax (§453A(c))

**Test (both must hold), per the Form 6252 instructions and Pub. 537:**

1. The property had a sales price over **$150,000** (treat all sales that are part of the same transaction as one sale); and
2. The aggregate balance of all nondealer installment obligations **arising during, and outstanding at the close of, the tax year** is more than **$5 million**.

A single sale over $5 million is not the test; a $4.9 million note fails the second prong, and three $2 million notes from the same year pass it. Interest continues in later years while obligations that originally required interest remain outstanding at year end.

**Exceptions:** farm property, personal-use property disposed of by an individual, real property disposed of before 1988, personal property disposed of before 1989 (Form 6252 instructions). Timeshares and residential lots follow §453(l) (their own interest charge, Schedule 2 line 14).

**Computation (Pub. 537 "How to figure interest on deferred tax"; IRC §453A(c)):**

```
Deferred tax liability = unrecognized gain at year end × maximum tax rate for that character
    (IRC §453A(c)(3): maximum rate under §1 or §11; for gain that will be long-term capital gain,
     the maximum rate on net capital gain under §1(h))
Applicable percentage  = (aggregate face of the year's obligations outstanding at year end − $5,000,000)
                         ÷ aggregate face of those obligations     (fixed in the year of sale)
Interest               = deferred tax liability × applicable percentage
                         × underpayment rate under §6621(a)(2) for the month with or within which the tax year ends
```

The interest is not figured on Form 6252. Individuals report it on **2025 Schedule 2, line 15** ("Interest on the deferred tax on gain from certain installment sales with a sales price over $150,000"); attach the computation. See [`../../schedule-2/SKILL.md`](../../schedule-2/SKILL.md).

The underpayment rate is year-dependent: the IRS quarterly interest rates page (https://www.irs.gov/payments/quarterly-interest-rates, reviewed 10-Sep-2026) lists the 4th quarter 2025 underpayment rate (corporate and non-corporate) as 7% (IRB 2025-37). Re-check for the year being prepared.

The maximum rate depends on the seller's entity type and the character of the deferred gain. Ask the CPA to confirm the rate before finalizing; show the formula and the rate used in the draft.

**Pub. 537 check figures (ABC, Inc., a C corporation; $15 million sale of $0-basis property; $500,000 expenses):**

```
2022: obligation 15,000,000 − 1,000,000 = 14,000,000; GPP 0.966670; unrecognized gain 13,533,380
      × 21% = 2,842,010 deferred tax; applicable % = 9,000,000 ÷ 14,000,000 = 64.2857%
      × 6% underpayment rate → $109,620
2023: obligation 9,000,000 × 0.966670 = 8,700,030 × 21% = 1,827,006 × 64.2857% × 8% → $93,960
2024: note paid off → $0
```

---

## 5. Disposing of the note (§453B)

A sale, exchange, gift, cancellation, distribution, or transmission of the installment obligation is generally a disposition that triggers gain or loss (Form 6252 instructions; Pub. 537 "Disposition of an Installment Obligation").

- Basis in the obligation = unpaid balance − (unpaid balance × gross profit percentage).
- Sale or exchange, or accepting less than face in satisfaction: gain or loss = amount realized − basis in the obligation.
- Any other disposition (gift, cancellation): gain or loss = FMV − basis. If the parties are related and the obligation is cancelled, FMV is treated as not less than face value.
- Character follows the original sale (ordinary, capital, or for §1231 property, long-term capital gain or ordinary loss).
- Not dispositions: a reduction of selling price without cancelling the rest of the debt (refigure the percentage instead); a new buyer assuming the obligation; transfer between spouses or incident to divorce (unless the recipient is a nonresident alien); transfer at the seller's death (other than to the buyer).
- Report a taxable §453B disposition on Form 4797, Form 8949, or Schedule D.

Ask: "Did you sell, give away, forgive, or cancel any part of the note this year?"

---

## 6. Repossession

If the seller repossesses the property, separate rules figure gain or loss on the repossession and the basis in the repossessed property (Pub. 537 "Repossession"; personal property and real property are treated differently). Do not compute a repossession with this skill's line map alone; load Pub. 537 "Repossession" and flag the draft for CPA review.

---

## 7. Escrow

If the agreement (or a later agreement) puts the remaining payments into an irrevocable escrow account, the full balance is treated as received when deposited; the sale cannot use the installment method for that balance unless the escrow imposes a substantial restriction serving a bona fide purpose of the buyer (Pub. 537 "Escrow Account").

---

## 8. Contingent payment sales

If the total selling price cannot be determined by the end of the year of sale, answer "No" on line 4 and use Temp. Reg. §15a.453-1(c) for the contract price and gross profit percentage (Pub. 537 "Contingent Payment Sale"). With a stated maximum price, enter the maximum on line 5. Without one, attach a schedule showing the gain computation and enter the taxable part of the payment on line 24 (and line 35 if Part III applies). Earnouts in business sales are the common case; refer the computation to a CPA.

---

## 9. Selling price reduced later (Pub. 537 Worksheet B)

```
New gross profit percentage = (reduced selling price − installment sale basis − installment income already reported)
                              ÷ future installments
```

Pub. 537 check figures: land sold in 2023 for $100,000, basis $40,000, 60% gross profit percentage, $12,000 gain reported in each of 2023 and 2024; in 2025 price reduced to $85,000 with three remaining payments of $15,000. Adjusted gross profit 45,000 − 24,000 reported = 21,000 ÷ 45,000 future installments = 46.67%; $7,000 gain on each $15,000 installment. A price reduction that does not cancel the debt is not a §453B disposition.

---

## 10. Like-kind exchange with an installment note

Like-kind property received is not a payment; the contract price is reduced by the FMV of the like-kind property; gross profit is reduced by gain that can be postponed (Pub. 537 "Like-Kind Exchange"). Since 2018, like-kind treatment applies only to real property not held primarily for sale.

Pub. 537 check figures: installment sale basis $400,000; like-kind property FMV $200,000; installment note $800,000 ($100,000 in 2026, $700,000 in 2027). Selling price $1,000,000; gross profit $600,000; contract price $800,000; percentage 75%. 2025 gain $0; 2026 $75,000; 2027 $525,000. Pair with [`../../form-8824/SKILL.md`](../../form-8824/SKILL.md).

---

## 11. Sale of a business's assets

The installment sale of a whole business is not the sale of one asset (Pub. 537 "Sale of a Business"). Allocate the price and the year-of-sale payments among assets sold at a loss, assets eligible for the installment method, and ineligible assets (inventory, dealer property, stocks and securities). Both buyer and seller use the residual method and each attaches **Form 8594** to the return for the year of sale. Inventory gain is ordinary income in the year of sale. Pub. 537's machine-shop example ($220,000 price, $108,500 eligible, 48% combined gross profit percentage, per-asset 22.95% land, 8.85% building, 16.20% goodwill, 49.3% of each principal payment allocated to the installment part) is the model for the attached schedule.
