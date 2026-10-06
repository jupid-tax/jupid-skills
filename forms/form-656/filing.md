# Submitting an Offer in Compromise

How an agent takes a reviewed Form 656 package from draft to submission, and what to tell the user about the months that follow. Load this only after the draft has passed validation and the user has reviewed it. The taxpayer signs under penalties of perjury; the agent never signs, never submits without explicit consent, and never pays without the user's authorization.

Sources: Form 656-B booklet (Rev. 4-2026), https://www.irs.gov/pub/irs-pdf/f656b.pdf (pages 3 to 6 and checklist page 29); Form 656 (Rev. 4-2026) Sections 5 to 8; Form 656-L (Rev. 7-2026); IRS offer in compromise page, https://www.irs.gov/payments/offer-in-compromise; IRC §6331(k), §7122(f).

---

## Channel decision tree

```
Is the offer doubt as to liability (Form 656-L)?
  Yes → Channel D (mail to the Brookhaven DATL Unit; no fee, no payment)
  No  → continue

Is the taxpayer an individual (including sole proprietor), and can they sign in to
an IRS Individual Online Account?
  Yes → Channel A (Individual Online Account): prepare forms, compute, pay, and submit online
  No  → continue

Is it a business entity (corporation, partnership, LLC)?
  Yes → Channel C (mail Form 656 + Form 433-B (OIC); payments may be made through the
        Business Tax Account or EFTPS)
  No  → Channel B (mail to the COIC unit for the taxpayer's state)
```

If the package was already submitted online, do not mail a duplicate (checklist, page 29).

---

## Channel A — Individual Online Account (IOLA)

Form 656-B, page 4 ("Apply Online"): individuals may use their Individual Online Account to prepare all necessary forms, calculate the potential offer, make all required payments, and submit electronically. Sign-in: IRS.gov/OLA.

Pre-flight:

- Draft validated; user has reviewed every line and attachment.
- User completes identity verification themselves. Do not handle the user's credentials.
- Supporting documents scanned (pay stubs, three months of personal bank statements, six months per business account, investment and retirement statements, loan statements, court orders, special-circumstances documentation).
- Payment option chosen; Low-Income Certification decided.

Do not automate the identity-verification flow or the final submit. Walk the user through it, or prepare the entries for them to type.

---

## Channel B — Mail to a Centralized Offer in Compromise (COIC) unit

Mail Form 656, Form 433-A (OIC) and/or Form 433-B (OIC), and copies of supporting documents (not originals) to the unit for the taxpayer's state of residence (Form 656-B, page 29):

| If you reside in | Mail your application to |
|---|---|
| AL, AZ, CA, CO, GA, HI, ID, KY, LA, MD, MS, ND, NM, NV, OK, OR, SD, TN, TX, UT, VA, WA | Memphis IRS Center COIC Unit, P.O. Box 30803, AMC, Memphis, TN 38130-0803 — 844-398-5025 |
| AK, AR, CT, DC, DE, FL, IA, IL, IN, KS, MA, ME, MI, MN, MO, MT, NC, NE, NH, NJ, NY, OH, PA, PR, RI, SC, VT, WI, WV, WY, or a foreign address | Brookhaven IRS Center COIC Unit, P.O. Box 9007, Holtsville, NY 11742-9007 — 844-805-4980 |

Addresses change between revisions; use the table printed in the current booklet. Keep a complete copy of the package (page 5, Step 7). Recommend a mailing method with proof of delivery; the 24-month deemed-acceptance period runs from receipt by the correct site (Form 656, Section 7(b)).

If the user is already working with an IRS employee (for example a revenue officer), tell that employee an offer is being sent (page 6).

## Channel C — Business entity

The IRS offer page: business taxpayers can pay the offer online through the Business Tax Account (https://www.irs.gov/businesses/business-tax-account) and must mail Form 656 and Form 433-B (OIC) to the address shown in the booklet (use the Channel B table by the business's state). Low-Income Certification never applies to entities; the $205 fee and initial payment are always due.

## Channel D — Doubt as to liability (Form 656-L)

Mail to: Brookhaven Internal Revenue Service, DATL Unit, P.O. Box 9008, Stop 681-D, Holtsville, NY 11742-9008 (Form 656-L (Rev. 7-2026) checklist). Do not send any payment. Include the written explanation and supporting documentation. A Form 656 offer must not be pending at the same time.

---

## Payments

| Item | Rule | Source |
|---|---|---|
| Application fee | $205 per Form 656, unless Low-Income Certification applies | Form 656-B, pages 3 to 4 |
| Lump-sum initial payment | 20% of the offer | Form 656, Section 4 |
| Periodic initial payment | First proposed monthly payment; then keep paying monthly while pending | Form 656, Section 4 |
| Electronic payment | EFTPS, or the Individual Online Account for individuals; allowed even if the offer is mailed; must be made the same date the offer is mailed or filed; record the 15-digit EFT numbers in Section 5 | Form 656-B, page 5 (Step 6); Form 656, Section 5 |
| Paper payment | Separate personal check, cashier's check, or money order for the fee and for each payment; payable to "United States Treasury"; U.S. dollars; attached to the front of Form 656; no cash | Form 656-B, page 5; Form 656, Section 6 |
| Low-Income Certification | Send no fee and no payment; payments sent anyway are kept | Form 656-B, page 5 reminder; Form 656 page 2 |
| Returned/insufficient payment | Offer returned | Form 656, Section 6 |

Payments are applied to the tax and generally not returned if the offer is rejected, returned, or withdrawn (Form 656, Section 7(c)). The fee is kept unless the offer is not accepted for processing; it reduces the compromised liability (IRC §7122(c)(2)(B)). The payer may designate the period in Section 5.

Never ask the user for card numbers or bank login credentials. If the user wants the agent to schedule EFTPS payments, the user enters payment details themselves.

---

## Representation

Attach Form 2848 (representation and confidential information) or Form 8821 (confidential information only; cannot represent in a collection matter) if someone else will deal with the IRS. List all years and forms in the offer and the current tax year (Form 656, page 7; Form 433-A (OIC) attachment list).

---

## After submission

| Event | What it means | Source |
|---|---|---|
| IRS official signs the offer | Offer becomes pending as of that date | Form 656, Section 7(j) |
| Before that signature | IRS may still levy and keep proceeds | Form 656-B, page 3; Section 7(g) |
| While pending, 30 days after rejection, during an appeal | No levy | IRC §6331(k)(1) |
| While pending, 30 days after rejection, during Appeals | Collection statute suspended; assessment period extended by pending time plus one year if the offer fails | Form 656, Section 7(p) |
| Periodic offer | Keep making monthly payments until a final decision or the offer is returned without appeal | Form 656, Section 4 |
| Existing approved installment agreement | Payments not required while pending; reinstated if the offer fails and no new debt arose | Form 656-B, page 3 |
| Penalties and interest | Continue to accrue | Form 656-B, page 2 |
| Refunds | Offset for periods assessed before acceptance; do not count toward the offer | Form 656-B, page 1 |
| Information requests | Reply by the deadline; failure returns the offer without appeal | Form 656-B, page 6 |
| No decision within 24 months of receipt | Offer deemed accepted (judicial-dispute periods excluded) | IRC §7122(f); Form 656, Section 7(b) |
| Rejection | Appeal within 30 days using Form 13711, Request for Appeal of Offer in Compromise | IRS offer in compromise page; Form 656, Section 7(k) |
| Return (not rejection) | No appeal | Form 656-B, page 2 |
| Acceptance | Pay per the terms; five years of compliance; lien released generally within 45 days after the final payment is received and verified; public inspection for one year | Form 656, Section 7(l), 7(q), 7(v) |

Publication 5 (Rev. 4-2021) sets the appeal format: a small case request is available when the total for each period is $25,000 or less (for an offer, the unpaid tax, penalty, and interest); above that a formal written protest is required. Confirm against the rejection letter.

---

## Consent and security rules

1. **Explicit consent at each irreversible step:** submitting the offer, paying the fee, making the initial payment, and signing the waiver in Section 7(p) by signing the form. Restate the amounts and the five-year terms before asking.
2. **No signatures by the agent.** The taxpayer (and spouse for a joint offer, or the corporate officer) signs Form 656, Form 433-A (OIC) or 433-B (OIC), and any attachment titled "Attachment to Form 656".
3. **No invented data.** Every figure on the forms traces to a user answer or a document the user supplied. If a value is missing, the form is not ready.
4. **Data minimization.** Do not store SSNs, ITINs, EINs, bank account numbers, EFT numbers, statements, or the signed package in agent logs or memory after the session. Redact identifiers in any summary.
5. **No credentials.** Do not ask for or type IRS online account, ID verification, bank, or EFTPS credentials.
6. **Surface, do not retry.** If the IRS returns the offer, requests information, or rejects it, show the user the notice and the deadline; do not resubmit on your own.
7. **Paid help.** If the user is paying a firm that promises a settlement amount before seeing the financial statement, point out that the minimum offer is set by the Form 433-A (OIC) computation, and suggest the free IRS Pre-Qualifier (https://irs.treasury.gov/oic_pre_qualifier/) or a Low Income Taxpayer Clinic.
