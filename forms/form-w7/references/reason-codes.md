# Reason Codes (a-h) — Decision Tree

The "Reason for submitting Form W-7" box is the single most consequential field on the W-7. Picking the wrong code is the #1 rejection cause per IRS data. Each code has specific eligibility criteria, required supporting evidence, and processing implications.

The agent's job: walk the applicant through the decision tree and identify the exact code.

---

## The decision tree

```
Is the applicant a nonresident alien?
  (Nonresident = does not meet substantial presence test or green card test under §7701(b))

  YES
    ↓
    Is the applicant claiming a tax treaty benefit?
      ↓
      YES → Box (a)
      NO  ↓
        Is the applicant a student / professor / researcher?
          ↓
          YES → Box (f)
          NO  ↓
            Is the applicant a dependent or spouse of an NRA visa holder?
              ↓
              YES → Box (g)
              NO  ↓
                Is the applicant filing their own 1040-NR?
                  ↓
                  YES → Box (b)
                  NO  ↓
                    Is the applicant submitting under an exception (FIRPTA, etc.)?
                      ↓
                      YES → Box (h) — explain
                      NO → SKIP (W-7 may not be needed)

  NO  (i.e., U.S. resident alien — meets substantial presence test or has green card)
    ↓
    Is the applicant filing their own U.S. tax return?
      ↓
      YES → Box (c)
      NO  ↓
        Is the applicant being claimed as a dependent on another's return?
          ↓
          YES → Box (d)
          NO  ↓
            Is the applicant the spouse of a U.S. citizen / resident alien filing MFJ?
              ↓
              YES → Box (e)
              NO  ↓
                Is the applicant submitting under an exception?
                  ↓
                  YES → Box (h) — explain
                  NO → SKIP
```

---

## Box-by-box detail

### Box (a) — Nonresident alien claiming a tax treaty benefit

**Who**: Nonresident alien who needs an ITIN to claim a benefit under a U.S. income tax treaty. Examples:
- Canadian researcher claiming Article XX exemption
- German performer claiming Article 18 (independent personal services)
- Indian student claiming Article 21 (students and apprentices)

**Required evidence**:
- Treaty article number must be entered at the top of the W-7 (treaty country and article)
- Form 8233 (Exemption from Withholding on Compensation) OR Form W-8BEN typically attached
- The W-7 may be filed **without a 1040** if filing under Exception 1 or 2 (passive income or treaty-exempt scholarship)

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

**Common pitfalls**:
- Some applicants conflate (a) and (b). (a) is for treaty claimants; (b) is for taxable filers without treaty claim.
- "Required to file" is determined by the threshold rules in IRC §6012 — verify the applicant actually has a filing obligation.

### Box (c) — U.S. resident alien filing a tax return

**Who**: Person who meets the substantial presence test (IRC §7701(b)(3)) — present in the U.S. for at least 31 days in the current year and 183 days over a 3-year weighted period — but is not eligible for SSN. Examples:
- Long-term undocumented resident with U.S. income
- Resident alien on a visa that doesn't authorize work (rare)

**Required evidence**:
- Form 1040 attached (not 1040-NR — resident aliens file 1040)
- Documents establishing presence (passport stamps, lease records, etc.) — not strictly required on the W-7 but support the residence claim

**Common pitfalls**:
- Confusing nonresident alien (1040-NR, box b) with resident alien (1040, box c). The substantial presence test determines this.
- DACA recipients and individuals with EAD cards are typically SSN-eligible — do not use box (c) for them; redirect to SSA.

### Box (d) — Dependent of U.S. citizen or resident alien

**Who**: Person being claimed as a dependent on someone else's U.S. tax return. Examples:
- Foreign-born child of a U.S. citizen
- Foreign parent being claimed as dependent
- Stepchild who is not a U.S. citizen

**Required evidence**:
- Primary filer's full name and SSN listed on the W-7
- Supporting tax return (the primary filer's 1040) attached
- For dependents under 18: photo on at least one identification document
- For dependents who are U.S. citizens but lacking SSN (e.g., adopted child still in process): different rules apply — verify

**Common pitfalls**:
- Dependent test changed under TCJA (2018+). Some dependents (e.g., Mexican / Canadian dependents under the old "qualifying relative" test) are no longer eligible. Verify against current §152.
- Children who are U.S. citizens (born to U.S.-citizen parents abroad) should apply for SSN, not ITIN.

### Box (e) — Spouse of U.S. citizen or resident alien

**Who**: Foreign spouse of a U.S. citizen or resident alien who needs an ITIN to file MFJ. Most common case.

**Required evidence**:
- Primary filer's full name and SSN listed on the W-7
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
- Visa type and expiration on Line 6c
- Form I-20 (for F students) or DS-2019 (for J exchange visitors) — may be requested
- Form 1040-NR or treaty-related forms (8233, W-8BEN) attached

**Common pitfalls**:
- F-1 / J-1 students may be SSN-eligible if they have on-campus employment authorization or CPT/OPT — they must apply for SSN, not ITIN.
- Verify SSN ineligibility before using box (f).

### Box (g) — Dependent / spouse of nonresident alien holding U.S. visa

**Who**: Family members (spouse, children) of an NRA visa holder. Examples:
- F-2 spouse of F-1 student
- J-2 dependent of J-1 visitor
- H-4 dependent of H-1B

**Required evidence**:
- Primary visa holder's name, visa type, ITIN
- Supporting tax return (if the family is filing) or evidence of nonresident status

**Common pitfalls**:
- F-2 / J-2 / H-4 dependents may be eligible for SSN if they have work authorization (rare for F-2; possible for J-2 and H-4 with specific conditions). Verify SSA eligibility first.
- This box is rarely used; most family members fall under (d) or (e) instead.

### Box (h) — Other (specify)

**Who**: Catchall for situations not fitting (a)-(g). Common examples:
- Foreign seller of U.S. real estate (FIRPTA, IRC §1445) — Exception 4 — no 1040 required
- Beneficiary of a U.S. trust receiving distributions
- Foreign person receiving U.S. mortgage interest reporting (IRC §6045) — Exception 3
- Foreign-owned U.S. corporation reporting under §6038A — Exception 5
- Person needing ITIN for non-tax purposes (limited circumstances; mostly rejected)

**Required evidence**:
- A clear written explanation in the "Other" box
- Supporting evidence specific to the exception (e.g., FIRPTA closing statement for Exception 4)

**Common pitfalls**:
- Box (h) is the easiest to misuse. If a more specific box (a-g) applies, use that.
- If claiming under an Exception (1-5), reference the exception number in the W-7 explanation.

---

## Quick reference: which box for which scenario

| Scenario | Box | Tax return attached? |
|----------|-----|----------------------|
| Foreign owner of U.S. rental, files 1040-NR | (b) | 1040-NR |
| Foreign student with treaty claim | (a) or (f) | 1040-NR + 8233/W-8BEN |
| Foreign spouse, MFJ filing | (e) | 1040 (primary filer's) |
| Foreign-born child of U.S. citizen | (d) | 1040 (primary filer's) |
| Resident alien (substantial presence) without SSN | (c) | 1040 |
| Foreign seller of U.S. real estate, FIRPTA | (h), Exception 4 | NO 1040; FIRPTA closing docs |
| Foreign trust beneficiary | (h) | varies |
| F-1 / J-1 student needing SSN-eligibility | NOT W-7 | redirect to SSA Form SS-5 |
| DACA recipient | NOT W-7 | redirect to SSA |

---

## Citation summary

- IRC §6109 — TIN requirements
- IRC §7701(b) — Resident vs. nonresident alien
- IRC §6012 — Filing obligation thresholds
- IRC §1445 — FIRPTA
- IRC §6038A — Foreign-owned U.S. corporations
- IRC §6045 — Mortgage interest reporting
- Pub 519 — U.S. Tax Guide for Aliens (residency rules and treaty cross-references)
- Pub 1915 — Understanding Your IRS ITIN
- Form W-7 instructions — current revision
