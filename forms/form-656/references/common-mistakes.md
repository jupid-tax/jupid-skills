# Form 656 and Form 433-A (OIC) — Common Mistakes

Errors that get offers returned (no appeal) or rejected, each with the fix and the source. Sources are the Form 656-B booklet (Rev. 4-2026), Form 656 and Form 433-A (OIC) (Rev. 4-2026), Form 656-L (Rev. 7-2026), and IRM 5.8.5 (effective 04-23-2026).

## 1. Submitting with a missing return or without a bill

**What happens:** the IRS applies the initial payment to the debt and returns the offer and fee; no appeal (Form 656-B, page 1). Without a bill for at least one listed debt, the offer and fee may be returned and the payment applied (page 2).

**Fix:** confirm every required return is filed and at least one bill was received. Include a complete copy of any return filed within 10 weeks of the offer (Form 656, Section 6).

## 2. Skipping current-year estimated payments or employer deposits

**What happens:** ineligible under the booklet's pre-checks (page 1), and failure to stay current while the offer is pending can get it returned (page 2).

**Fix:** bring 2026 estimated payments and the current and two prior quarters of deposits current before submission; keep them current until a decision.

## 3. Offering a round number instead of the computed minimum

**What happens:** the offer must be at least the Form 433-A (OIC) / 433-B (OIC) amount (Form 656-B, page 5, Step 5). A lower offer without documented special circumstances draws a request to raise it or a rejection.

**Fix:** carry the Section 8 figure to Form 656 Section 4 exactly. If the user cannot pay it, describe the special circumstances in Section 3 and attach evidence (checklist, page 29).

## 4. Estimating allowable expenses

**What happens:** Box E is wrong, so Box F and the offer are wrong. The IRS recomputes with the Collection Financial Standards and asks for a higher offer.

**Fix:** enter the full National Standard on lines (39) and (45) from the table effective June 29, 2026 (https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards); enter actual amounts on the other lines and flag any above the local standard. If the table cannot be read, stop.

## 5. Claiming expenses the IRS does not allow

**What happens:** removed during review; offer rises.

**Fix:** leave out private school and college tuition, charitable contributions, unsecured debt and credit card payments (Form 656-B, page 5; IRM 5.8.5.22.4), voluntary retirement contributions and investment-type savings (IRM 5.8.5.23). Allow only expenses the user actually pays and can document (IRM 5.8.5.22.4).

## 6. Keeping depreciation in self-employment income

**What happens:** net business income understated.

**Fix:** add back depreciation and other non-cash expenses (Form 433-A (OIC), line (36) note; IRM 5.8.5.26).

## 7. Applying the $3,450 allowance to a second car on a single offer

**What happens:** Box A understated.

**Fix:** line (6b) always subtracts $3,450 from the first vehicle; line (6d) subtracts it from the second vehicle only on a joint offer (Form 433-A (OIC), Section 3).

## 8. Leaving out assets

**What happens:** the IRS checks third-party records; concealment lets it reopen or terminate an accepted offer (Form 656, Section 7(o)). Section 9 asks about transfers over $10,000 for less than full value in the past 10 years, trusts, safe deposit boxes, and foreign assets.

**Fix:** walk the user through every Section 3 and Section 9 category and record "none" explicitly. Include foreign accounts and digital assets.

## 9. Using the allowances when the user can full pay

**What happens:** the $1,000 and $3,450 allowances and the 12/24 multipliers do not apply if the user can pay in full within the collection period (Form 656-B, page 1; Form 433-A (OIC) Section 8 note).

**Fix:** run the full-pay screen without the allowances first (`rcp-calculation.md`). If the user can full pay, route to an installment agreement.

## 10. Missing a periodic payment while the offer is pending

**What happens:** the offer is returned with no appeal rights, and the payments already made are kept (Form 656, Section 4; Form 656-B, page 3; IRC §7122(c)(1)(B)(ii)).

**Fix:** set the payment day (1 to 28) to fit the user's pay cycle and recommend EFTPS or IOLA scheduled payments.

## 11. Sending money with a Low-Income Certification

**What happens:** voluntary payments are applied to the debt and not returned (Form 656, page 2; Section 7(d)).

**Fix:** if the user checks a Low-Income Certification box, send no fee and no payment.

## 12. One package for individual and business debts

**What happens:** the offer cannot be processed as filed.

**Fix:** separate Form 656 packages for individual and business debts, each with its own financial statement, fee, and payment (Form 656-B, page 4).

## 13. Filing DATL and DATC together

**What happens:** the Form 656 (DATC) offer is returned and its payment kept (Form 656-L, page 4).

**Fix:** resolve the liability dispute first (Form 656-L or the notice process), then file Form 656 if the debt still cannot be paid.

## 14. Combining the fee and the initial payment in one check

**What happens:** may delay processing (Form 656, Section 6). An offer is returned if the fee and payment are not made at submission or a payment bounces.

**Fix:** two separate payments (EFTPS, IOLA, or two checks payable to "United States Treasury"). Electronic payments made the same date the offer is mailed or filed, with the 15-digit EFT numbers in Section 5.

## 15. Filing an amended return while the offer is pending

**What happens:** may be grounds for termination (Form 656, Section 7(e)).

**Fix:** settle any amended-return question before submitting.

## 16. Ignoring an information request

**What happens:** offer returned without appeal rights (Form 656-B, page 6).

**Fix:** calendar every IRS deadline; respond in full by the date given.

## 17. Treating acceptance as the end

**What happens:** a late return or unpaid balance within five years after acceptance can default the offer and revive the original debt less payments, plus accrued penalties and interest (Form 656, Section 7(l), 7(o); Form 656-B, page 6).

**Fix:** set up next year's estimated payments ([`../../form-1040-es/SKILL.md`](../../form-1040-es/SKILL.md)) or withholding before the offer is accepted.
