# Form W-9 — TIN selection (Part I)

When to use SSN vs EIN. Loaded by SKILL.md Step 4.

The TIN goes in Part I of Form W-9. The form has separate boxes for SSN (XXX-XX-XXXX) and EIN (XX-XXXXXXX). Fill exactly one — leave the other blank.

---

## Decision rule

The TIN type follows from Line 3a (federal tax classification):

| Line 3a | TIN type | Boxes used |
|---------|----------|-----------|
| Individual/sole proprietor (incl. SMLLC disregarded) | SSN (or ITIN); a sole prop may instead use its own EIN | SSN boxes (EIN boxes if using the EIN) |
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

**Default rule:** SMLLC with no corporate election → use the **owner's SSN** (or the owner's own EIN, if the owner has one), never the LLC's EIN (W-9 Part I: "enter the owner's SSN (or EIN, if the owner has one)").

**Why:** Under federal tax law, a default SMLLC is "disregarded" — treated as if the LLC doesn't exist. The owner files Schedule C with their Form 1040 using their SSN. The LLC's EIN is only used for federal employment tax, certain excise taxes, and bank-account-opening — NOT for income tax matching.

When the requestor files the year-end 1099, the IRS matches:
- The 1099 payee name (Line 1 of W-9) → owner's name
- Against the IRS database for the TIN (Part I of W-9) → must be the owner's SSN

If Part I has the LLC's EIN, the match fails. Result: the IRS sends the requestor a CP2100 / "B" notice, the requestor sends the user a request for a corrected W-9, and during the gap, the requestor may apply 24% backup withholding.

**Exceptions to the SMLLC = SSN rule:**

1. **SMLLC with Form 2553 (S-corp) election** → use the LLC's EIN. The S-corp election makes the LLC a separate taxpayer for federal income tax.
2. **SMLLC with Form 8832 (C-corp) election** → use the LLC's EIN. Same reasoning.
3. **SMLLC owned by another LLC or by a corporation** → the first owner that is not disregarded goes on line 1, with its EIN (W-9 chart item 8).
4. **SMLLC owned by a foreign person** → not a W-9 case; the foreign owner gives a Form W-8, even if it has a US TIN (W-9 instructions, Line 1).

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

**Per IRS instructions:** "If you are a sole proprietor and you have an EIN, you may enter either your SSN or EIN." The chart note adds: "You may use either your SSN or EIN (if you have one), but the IRS encourages you to use your SSN." Line 1 is still the owner's individual name either way.

**Practical reality:** Using the sole-proprietor EIN keeps the SSN off vendor files; it is allowed. Ask the user which they prefer.

---

## EIN application (form-ss-4 skill)

If the user needs an EIN before they can complete the W-9, they apply via:

- IRS EIN application (online): https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online (EIN issued at the end of the session; hours Mon–Fri 6:00 a.m.–1:00 a.m. ET, Sat 6:00 a.m.–9:00 p.m., Sun 6:00 p.m.–midnight)
- Form SS-4 (paper): https://www.irs.gov/pub/irs-pdf/fss4.pdf (by mail about 4 weeks; by fax about 4 business days)
- See [`../../form-ss-4/SKILL.md`](../../form-ss-4/SKILL.md) for the full application workflow

EINs are free. There are scam websites that charge for EIN applications — these are not affiliated with the IRS.

---

## Validation rules for the agent

When the agent enters Part I of the draft, verify:

- [ ] Exactly one TIN type is filled (not both)
- [ ] TIN length is exactly 9 digits
- [ ] SSN format: XXX-XX-XXXX (3-2-4)
- [ ] EIN format: XX-XXXXXXX (2-7)
- [ ] If SSN starts with `9`, flag as ITIN (and confirm the filer is still a US person for W-9 purposes; if non-resident alien, redirect to form-w8ben)
- [ ] EIN prefix is valid: the first two digits must be one of 01–06, 10–16, 20–27, 30–48, 50–68, 71–77, 80–88, 90–95, 98, 99 (irs.gov, "How EINs are assigned and valid EIN prefixes"); 00, 07–09, 17–19, 28–29, 49, 69–70, 78–79, 89, 96–97 are not issued
- [ ] TIN matches Line 3a (sole prop = SSN or own EIN; corp/partnership/trust/LLC with C, S, or P = EIN)
- [ ] If filer described an SMLLC default and is using the LLC's EIN, raise a sanity warning ("The IRS expects your SSN here, not the LLC's EIN — confirm before signing")
