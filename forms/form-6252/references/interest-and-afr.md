# Interest on the Note: Stated Interest, Unstated Interest, and the AFR Test

Interest never goes on Form 6252. Lines 5, 21, 23, and 33 all say "Don't include interest, whether stated or unstated," and the instructions add: "Don't report interest received, carrying charges received, original issue discount, or unstated interest on Form 6252" (Form 6252 instructions, "Interest"). This file explains how to separate interest from principal and when part of the stated principal must be recharacterized as interest. Source: Pub. 537 (2025), "Unstated Interest and Original Issue Discount (OID)," pages 14–17, https://www.irs.gov/pub/irs-pdf/p537.pdf.

## 1. Split every payment

Pub. 537: each installment payment usually has three parts: interest income, return of adjusted basis, and gain. Interest comes off first. Only the principal part goes on line 21.

Ask the user for the note's amortization schedule or the buyer's year-end statement showing principal and interest separately. If neither exists, compute the schedule from the note terms and show it to the user for confirmation. Do not split a payment by guesswork.

Interest is ordinary income: Schedule B and Form 1040 for individuals. If the buyer of a home used it as a personal residence and pays on a seller-financed mortgage, the seller lists the buyer's name, address, and SSN on Schedule B line 1 (Pub. 537, "Seller-financed mortgage").

## 2. Is the stated interest adequate?

A contract provides adequate stated interest if the stated principal is less than or equal to the sum of the present values of all payments, discounted at the **test rate**; in general, if the stated rate (on the appropriate compounding period) is at least the test rate (Pub. 537, "Adequate stated interest"). If §483 applies, payments due within 6 months after the sale are taken at face value.

### Test rate

The test rate is the **3-month rate**: the lower of

- the lowest AFR (appropriate compounding period) in effect during the 3-month period ending with the first month in which there is a binding written contract that substantially provides the terms of the sale, and
- the lowest AFR (appropriate compounding period) in effect during the 3-month period ending with the month of the sale.

The term of the note picks the AFR, measured by its **weighted average maturity** (Reg. §1.1273-1(e)(3)):

| Weighted average maturity | AFR |
|---------------------------|-----|
| 3 years or less | Federal short-term rate |
| Over 3 years, not over 9 years | Federal mid-term rate |
| Over 9 years | Federal long-term rate |

The IRS publishes AFRs monthly in a revenue ruling (Table 1, with annual, semiannual, quarterly, and monthly compounding columns): https://www.irs.gov/applicable-federal-rates. **Never assume a rate.** Fetch the revenue rulings for the specific months, read Table 1, and record the Rev. Rul. number, month, term, compounding column, and rate in the draft. Use the compounding column that matches the note (monthly payments → monthly column).

Weighted average maturity: sum over principal payments of (years from sale to payment × payment) ÷ total principal. Compute it from the amortization schedule; an equal-principal note with annual payments over n years has a weighted average maturity of (n + 1) ÷ 2 years.

### Caps on the test rate

| Situation | Cap | Source |
|-----------|-----|--------|
| Seller financing of $7,296,700 or less (2025 figure in Pub. 537; property other than new §38 property) | Test rate not more than 9%, compounded semiannually | Pub. 537, "Seller-financed sales" |
| Certain land transfers between related persons (individual and family: spouse, siblings whole or half, ancestors, lineal descendants, and their spouses) to the extent stated principal of the year's land notes between them does not exceed $500,000 | Test rate not more than 6%, compounded semiannually; §483 governs | Pub. 537, "Certain land transfers between related persons" |

The $7,296,700 figure is inflation-adjusted each year; re-check the current Pub. 537 or the year's revenue ruling under §1274A before using it for another year.

## 3. §1274 or §483?

If interest is inadequate, one of these recharacterizes part of the stated principal (Pub. 537):

**§1274 (OID)** applies to a debt instrument issued for property if any payment is due more than 6 months after the sale and interest is inadequate. It does **not** apply to:

- a cash method debt instrument: stated principal of $5,211,900 or less (2025 figure in Pub. 537, adjusted annually under §1274A), lender on the cash method and not a dealer, and both parties jointly elect cash-method interest;
- a sale for which total payments are $250,000 or less;
- the sale of an individual's main home;
- the sale of a farm for $1 million or less by an individual, estate, testamentary trust, small business corporation (§1244(c)(3)), or a qualifying domestic partnership;
- certain land transfers between related persons (§1274 still applies to the extent stated principal exceeds $500,000, or if any party is a nonresident alien).

**§483 (unstated interest)** applies to an inadequate-interest contract not covered by §1274, except a sale with no payment due more than 1 year after the sale and a sale for $3,000 or less.

**Neither applies** to: assumption of a debt instrument (unless modified into a deemed exchange under Reg. §1.1001-3); publicly traded debt or property; certain patent sales with contingent amounts; certain annuity contracts; §1041 transfers between spouses or incident to divorce; demand loans that are below-market loans under §7872(c)(1); certain below-market loans in sales of personal-use property (holder only).

## 4. Effect on Form 6252

When unstated interest or OID exists, reduce the stated selling price (line 5) and contract price by the recharacterized amount and report it as interest income (Pub. 537, "Rules for the seller"): unstated interest under the seller's regular accounting method; OID over the term under the constant yield method of §1272. The gross profit percentage then uses the reduced price. Do not attempt the OID present-value computation without the full payment schedule; show the inputs and refer the computation to a CPA.

Buyer side (for context only): the recharacterized amount reduces the buyer's basis and becomes interest expense, except for personal-use property, where §483 and §1274 do not apply to the buyer and the buyer cannot deduct it, while the seller still reports it as income.

## 5. Worked checks (from the examples in this skill)

| Example | Contract month / sale month | Term | Compounding | Lowest AFR, contract window | Lowest AFR, sale window | Test rate | Stated | Adequate? |
|---------|----------------------------|------|-------------|------------------------------|-------------------------|-----------|--------|-----------|
| Rental condo | March 2025 / May 2025 | 120 monthly payments, weighted average maturity 5.56 years → mid-term | Monthly | Jan–Mar 2025: 4.16% (Jan) | Mar–May 2025: 4.03% (May) | 4.03% | 6.25% | Yes |
| Lot sold to son | March 2025 / April 2025 | 8 equal annual payments, weighted average maturity 4.5 years → mid-term | Annual | Jan–Mar 2025: 4.24% (Jan) | Feb–Apr 2025: 4.21% (Apr) | 4.21% (below the 6% related-land cap) | 5.25% | Yes |

Rates from Rev. Rul. 2025-1 (January 2025), 2025-5 (February), 2025-6 (March), 2025-8 (April), and 2025-10 (May), Table 1, https://www.irs.gov/pub/irs-drop/rr-25-01.pdf, rr-25-05.pdf, rr-25-06.pdf, rr-25-08.pdf, rr-25-10.pdf.

## 6. Questions to ask

- "What interest rate does the note carry, how is it compounded, and when is it paid?"
- "In what month did you and the buyer sign the binding written contract? In what month did the sale close?"
- "Can you send the note's amortization schedule or the buyer's year-end statement?"
- "Is the buyer a family member, and is the property land?" (6% cap, §483)
- "Does the buyer use the property as a personal residence?" (Schedule B line 1 reporting; buyer-side rules)
