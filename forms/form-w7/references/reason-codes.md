# Reason Codes (a-h) — Decision Tree

The "Reason for submitting Form W-7" box is the single most consequential field on the W-7. A code that doesn't match the attached return and documents gets the application suspended or rejected. Each code has specific eligibility criteria, required supporting evidence, and processing implications.

The agent's job: walk the applicant through the decision tree and identify the exact code.

---

## The decision tree

```
Is the applicant claimed as a dependent of a U.S. citizen / resident alien
(for an allowable tax benefit)?
  YES → Box (d)
  NO  ↓
Is the applicant the spouse of a U.S. citizen / resident alien
(e.g., joint return, including a nonresident spouse under the §6013(g) election)?
  YES → Box (e)
  NO  ↓
Is the applicant a dependent or spouse of a nonresident alien holding a U.S. visa?
  YES → Box (g)
  NO  ↓
Is the applicant a nonresident alien?
  (Nonresident = does not meet substantial presence test or green card test under §7701(b))

  YES
    ↓
    Is the applicant a student / professor / researcher filing a return or claiming an exception?
      YES → Box (f)  (+ box h if claiming an exception)
      NO  ↓
        Is the applicant filing their own U.S. return (usually 1040-NR)?
          YES → Box (b)
          NO  ↓
            Does the applicant need the ITIN only to claim a treaty benefit (Exception 1 or 2)?
              YES → Box (a) + box h with the exception designation
              NO  ↓
                Does another exception apply (3 mortgage interest, 4 U.S. real property disposition, 5 T.D. 9363)?
                  YES → Box (h) — enter the exception
                  NO → SKIP (no tax purpose shown; W-7 will be rejected)

  NO  (i.e., U.S. resident alien under the substantial presence test, not SSN-eligible)
    ↓
    Is the applicant filing their own U.S. tax return?
      YES → Box (c)
      NO  ↓
        Is the applicant submitting under an exception?
          YES → Box (h) — enter the exception
          NO → SKIP
```

---

## Box-by-box detail

### Box (a) — Nonresident alien claiming a tax treaty benefit

**Who**: Nonresident alien who needs an ITIN to claim a benefit under a U.S. income tax treaty without filing a return. Examples (designations from the W-7 instructions):
- Nonresident receiving a U.S. pension or annuity at a treaty rate ("Exception 1d-Pension Income")
- Nonresident speaker paid an honorarium, claiming treaty exemption on Form 8233 (Exception 2a)
- Nonresident visitor with gambling winnings claiming a treaty rate through a gaming official acting as Acceptance Agent ("Exception 2d-Gambling Winnings")

Students, professors, and researchers claiming treaty benefits use box (f), not (a). Confirm the treaty article with the user against Pub. 901; do not guess article numbers.

**Required evidence**:
- Treaty country and treaty article number in the entry spaces below box h
- Box h also checked, with the Exception 1 or 2 designation on the dotted line by number, letter, and category (e.g., "Exception 1d-Pension Income", "Exception 2d-Gambling Winnings")
- The documents that exception requires (e.g., withholding agent's letter, the withholding agent's portion of Form 8233, or the Form W-8BEN given to the withholding agent)
- No tax return: box a is for nonresident aliens who need an ITIN for a treaty benefit even though they don't file a return

**Common pitfalls**:
- Treaty article must be specific. "Article XX" or "Article 18" — not just "U.S.-Canada treaty"
- Some treaties have substantive eligibility requirements (e.g., must be a resident of the treaty country at the time of payment)

### Box (b) — Nonresident alien filing a U.S. federal tax return

**Who**: Nonresident alien who has U.S.-source income (rental, business, etc.) and is required to file Form 1040-NR. Examples:
- Foreign owner of U.S. rental property
- Foreign person with U.S. self-employment income
- Foreign person who received gambling winnings or lottery prizes

**Required evidence**:
- Form 1040-NR attached
- Income documents (1042-S, K-1, etc.)
- A complete foreign address on line 3 (for box b, a country name alone is not enough)

**Common pitfalls**:
- Some applicants conflate (a) and (b). (a) is for treaty claimants who don't file a return; (b) is for anyone filing a return, including a 1040-NR that claims a treaty benefit or only a refund.
- "Required to file" is determined by the threshold rules in IRC §6012 — verify the applicant actually has a filing obligation.

### Box (c) — U.S. resident alien filing a tax return

**Who**: Person who meets the substantial presence test (IRC §7701(b)(3)) — present in the U.S. for at least 31 days in the current year and 183 days over a 3-year weighted period — but is not eligible for SSN. Examples:
- Long-term undocumented resident with U.S. income
- Resident alien on a visa that doesn't authorize work (rare)

**Required evidence**:
- Form 1040 attached (not 1040-NR — resident aliens file 1040)
- Date of entry into the United States on line 6d (required for box c)

**Common pitfalls**:
- Confusing nonresident alien (1040-NR, box b) with resident alien (1040, box c). The substantial presence test determines this.
- DACA recipients and individuals with EAD cards are typically SSN-eligible — do not use box (c) for them; redirect to SSA.

### Box (d) — Dependent of U.S. citizen or resident alien

**Who**: Person being claimed as a dependent on someone else's U.S. tax return. Examples:
- Foreign-born child of a U.S. citizen
- Foreign parent being claimed as dependent
- Stepchild who is not a U.S. citizen

**Required evidence**:
- Relationship (parent, child, grandchild, etc.) and the U.S. citizen/resident alien's full name and SSN or ITIN on the dotted lines next to box d
- Supporting tax return (the U.S. person's 1040) attached, listing the dependent and claiming an **allowable tax benefit**: head of household, qualifying surviving spouse, AOTC (Form 8863), PTC (Form 8962), child and dependent care credit (Form 2441), or credit for other dependents (box checked next to the dependent's name). Listing the dependent alone is not enough.
- Date of entry into the United States on line 6d and proof of U.S. residency, unless the dependent is a dependent of U.S. military personnel stationed overseas, or is from Canada or Mexico and claimed for a benefit other than the ODC
- Photo on at least one document unless under 14 (under 18 if a student); original civil birth certificate if under 18 with no passport
- For dependents who are U.S. citizens but lacking SSN (e.g., adopted child still in process): different rules apply (Form W-7A / ATIN) — verify

**Common pitfalls**:
- Since 2018, dependents get an ITIN only if claimed for an allowable tax benefit or filing their own return (personal exemptions are suspended). A dependent claimed for the ODC must be a U.S. resident or U.S. national, so Canada/Mexico dependents claimed only for the ODC must prove U.S. residency.
- Children who are U.S. citizens (born to U.S.-citizen parents abroad) should apply for SSN, not ITIN.

### Box (e) — Spouse of U.S. citizen or resident alien

**Who**: Foreign spouse of a U.S. citizen or resident alien who needs an ITIN to file MFJ. Most common case.

**Required evidence**:
- The U.S. citizen/resident alien's full name and SSN or ITIN on the dotted line next to box e
- Supporting tax return (1040) with MFJ election attached
- Marriage certificate (sometimes requested by IRS, not always)

**Common pitfalls**:
- The MFJ election treats the foreign spouse as a U.S. resident for tax purposes — they must report worldwide income. If the foreign spouse has substantial foreign income, MFJ may not be advantageous. The choice between MFJ (with ITIN) vs. MFS (without spouse's ITIN) is a tax-planning decision; out of scope for this skill but worth flagging.
- If both spouses are foreign and neither has SSN, BOTH need ITINs (two separate W-7s).

### Box (f) — Nonresident alien student, professor, or researcher

**Who**: F, J, M, or Q visa holder (student, exchange visitor, vocational student, cultural exchange) who has U.S. tax obligations or treaty claims. Examples:
- F-1 student with on-campus employment income
- J-1 scholar claiming treaty exemption
- M-1 vocational student with U.S. income

**Required evidence**:
- Lines 6a, 6c, 6d, and 6g completed; passport with a valid U.S. visa (no visa needed if the foreign address is in Canada, Mexico, or Bermuda)
- Form I-20 (for F students) or DS-2019 (for J exchange visitors) — attach copies of I-20/I-94 if held
- Form 1040-NR attached, or, when claiming Exception 2 instead of filing, box h checked with the designation (e.g., "Exception 2b-Scholarship Income and claiming tax treaty benefits", "Exception 2c-Scholarship Income") and the Exception 2 documents
- SSA denial letter, or a letter from the DSO/RO stating the student won't be employed in the U.S.

**Common pitfalls**:
- F-1 / J-1 students may be SSN-eligible if they have on-campus employment authorization or CPT/OPT — they must apply for SSN, not ITIN.
- Verify SSN ineligibility before using box (f).

### Box (g) — Dependent / spouse of nonresident alien holding U.S. visa

**Who**: Family members (spouse, children) of an NRA visa holder. Examples:
- F-2 spouse of F-1 student
- J-2 dependent of J-1 visitor
- H-4 dependent of H-1B

**Required evidence**:
- A copy of the applicant's own U.S. visa attached to the W-7
- Date of entry into the United States on line 6d
- Supporting tax return on which the applicant is claimed as a dependent (for an allowable tax benefit) or files

**Common pitfalls**:
- F-2 / J-2 / H-4 dependents may be eligible for SSN if they have work authorization (rare for F-2; possible for J-2 and H-4 with specific conditions). Verify SSA eligibility first.
- If the visa holder is a U.S. resident alien for tax purposes (substantial presence test), the family member is a dependent or spouse of a resident alien: use (d) or (e) instead.

### Box (h) — Other (specify)

**Who**: Catchall for situations not fitting (a)-(g). Common examples:
- Party to a disposition of a U.S. real property interest by a foreign person (FIRPTA, IRC §1445) — Exception 4 — no 1040 required
- Beneficiary of a U.S. trust receiving distributions
- Individual with a home mortgage loan on U.S. real property subject to Form 1098 reporting (IRC §6050H) — Exception 3
- Non-U.S. representative of a foreign corporation who needs an ITIN for the corporation's e-filing requirement under T.D. 9363 — Exception 5
- Not eligible: a person with no federal tax purpose. Every ITIN request needs a tax purpose, with or without a return (Pub 1915).

**Required evidence**:
- A detailed description of the reason on the dotted line, or the exception designation by number, letter, and category (e.g., "Exception 1a-Partnership Income", "Exception 3-Mortgage Interest", "Exception 5, T.D. 9363")
- The documents the Exceptions Tables require (e.g., Form 8288/8288-A/8288-B plus the sales contract, HUD-1, or Closing Disclosure for Exception 4)

**Common pitfalls**:
- Box (h) is the easiest to misuse. If a more specific box (a-g) applies, use that.
- "Renewing an ITIN" or "ITIN renewal" is not a valid reason (Pub 1915).

---

## Quick reference: which box for which scenario

| Scenario | Box | Tax return attached? |
|----------|-----|----------------------|
| Foreign owner of U.S. rental, files 1040-NR | (b) | 1040-NR |
| Foreign student with treaty claim | (f) (+ h if Exception 2) | 1040-NR, or none under Exception 2 with 8233/W-8BEN docs |
| Nonresident needing ITIN only for treaty-reduced withholding | (a) + (h), Exception 1 or 2 | NO return; exception documents |
| Foreign spouse, MFJ filing | (e) | 1040 (primary filer's) |
| Foreign-born child of U.S. citizen | (d) | 1040 (primary filer's), with the allowable tax benefit claimed |
| Resident alien (substantial presence) without SSN | (c) | 1040 |
| Foreign seller of U.S. real estate, FIRPTA | (h), Exception 4 | NO 1040; Form 8288/8288-A/8288-B + sales contract, HUD-1, or Closing Disclosure |
| Foreign trust beneficiary | (h) | varies |
| F-1 / J-1 student needing SSN-eligibility | NOT W-7 | redirect to SSA Form SS-5 |
| DACA recipient | NOT W-7 | redirect to SSA |

---

## Citation summary

- IRC §6109 — TIN requirements
- IRC §7701(b) — Resident vs. nonresident alien
- IRC §6012 — Filing obligation thresholds
- IRC §1445 — FIRPTA
- T.D. 9363 — e-filing requirement behind Exception 5
- IRC §6050H — Mortgage interest reporting (Form 1098)
- Pub 519 — U.S. Tax Guide for Aliens (residency rules and treaty cross-references)
- Pub 1915 (Rev. 12-2025) — Understanding Your IRS ITIN
- Form W-7 instructions (Rev. December 2024) — "Reason You're Submitting Form W-7" and "Allowable tax benefit"
