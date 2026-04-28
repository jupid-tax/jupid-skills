# Form W-9 — TIN selection (Part I)

When to use SSN vs EIN. Loaded by SKILL.md Step 4.

The TIN goes in Part I of Form W-9. The form has separate boxes for SSN (XXX-XX-XXXX) and EIN (XX-XXXXXXX). Fill exactly one — leave the other blank.

---

## Decision rule

The TIN type follows from Line 3a (federal tax classification):

| Line 3a | TIN type | Boxes used |
|---------|----------|-----------|
| Individual/sole proprietor (incl. SMLLC disregarded) | SSN (or ITIN) | SSN boxes |
| LLC with S-corp or C-corp election | EIN | EIN boxes |
| Multi-member LLC (partnership default) | EIN | EIN boxes |
| Multi-member LLC with corporate election | EIN | EIN boxes |
| C Corporation | EIN | EIN boxes |
| S Corporation | EIN | EIN boxes |
| Partnership (not LLC) | EIN | EIN boxes |
| Trust/estate | EIN | EIN boxes |

---

## The single-member LLC trap

This is the most-misfiled case. An SMLLC owner often has BOTH an SSN (their personal one) and an EIN (the one they obtained for the LLC to open a business bank account or hire employees).

**Default rule:** SMLLC with no corporate election → use the **owner's SSN**, not the LLC's EIN.

**Why:** Under federal tax law, a default SMLLC is "disregarded" — treated as if the LLC doesn't exist. The owner files Schedule C with their Form 1040 using their SSN. The LLC's EIN is only used for federal employment tax, certain excise taxes, and bank-account-opening — NOT for income tax matching.

When the requestor files the year-end 1099, the IRS matches:
- The 1099 payee name (Line 1 of W-9) → owner's name
- Against the IRS database for the TIN (Part I of W-9) → must be the owner's SSN

If Part I has the LLC's EIN, the match fails. Result: the IRS sends the requestor a CP2100 / "B" notice, the requestor sends the user a request for a corrected W-9, and during the gap, the requestor may apply 24% backup withholding.

**Exceptions to the SMLLC = SSN rule:**

1. **SMLLC with Form 2553 (S-corp) election** → use the LLC's EIN. The S-corp election makes the LLC a separate taxpayer for federal income tax.
2. **SMLLC with Form 8832 (C-corp) election** → use the LLC's EIN. Same reasoning.
3. **SMLLC owned by another LLC or by a corporation** → uses the parent's TIN.

---

## SSN vs ITIN

| Document | Issued to | Format |
|----------|-----------|--------|
| **SSN** | US citizens and certain non-citizen residents authorized to work | XXX-XX-XXXX |
| **ITIN** | US tax filers ineligible for an SSN (resident aliens on visas that don't permit work, dependents/spouses of resident aliens, etc.) | 9XX-XX-XXXX (always starts with 9) |

Both go in the SSN boxes on W-9. ITIN is a substitute for SSN when the filer can't get an SSN.

**Note:** Filers with only an ITIN are still US persons for W-9 purposes if they meet substantial-presence or green-card tests. They use Form W-9, not W-8BEN. If the filer is a non-resident alien (no substantial-presence + no green card), they use W-8BEN — wrong form for this skill.

---

## Sole proprietor with EIN

A sole proprietor (no LLC) can apply for an EIN if they want one (often for opening a business bank account, hiring employees, or for privacy when sharing TIN with a vendor).

**Per IRS instructions:** A sole proprietor with both SSN and EIN should enter the **SSN** on W-9. The IRS prefers SSN for sole-prop tax matching because Schedule C uses the SSN.

**Practical reality:** Some requestors accept EIN from sole props. If the filer wants to use their EIN to avoid sharing the SSN, the IRS instructions tolerate it but it can occasionally cause a TIN-matching failure (the IRS has both records but matches against SSN by default for sole props). Safest to use SSN.

---

## EIN application (forthcoming form-ss4 skill)

If the user needs an EIN before they can complete the W-9, they apply via:

- IRS EIN application (online): https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online (issued instantly, M-F business hours)
- Form SS-4 (paper): https://www.irs.gov/pub/irs-pdf/fss4.pdf (4-week turnaround)

EINs are free. There are scam websites that charge for EIN applications — these are not affiliated with the IRS.

---

## Validation rules for the agent

When the agent enters Part I of the draft, verify:

- [ ] Exactly one TIN type is filled (not both)
- [ ] TIN length is exactly 9 digits
- [ ] SSN format: XXX-XX-XXXX (3-2-4)
- [ ] EIN format: XX-XXXXXXX (2-7)
- [ ] If SSN starts with `9`, flag as ITIN (and confirm the filer is still a US person for W-9 purposes; if non-resident alien, redirect to form-w8ben)
- [ ] EIN does not start with `00` or `07-09` (those are not valid EIN prefixes)
- [ ] TIN matches Line 3a (sole prop = SSN; corp/partnership/trust = EIN)
- [ ] If filer described an SMLLC default and is using the LLC's EIN, raise a sanity warning ("The IRS expects your SSN here, not the LLC's EIN — confirm before signing")
