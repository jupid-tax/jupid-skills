# Step 3 — Dependents Reference

Step 3 reduces federal withholding by the expected Child Tax Credit (CTC) and Credit for Other Dependents (ODC). It only applies if total income will be $200,000 or less ($400,000 or less MFJ) (2026 Form W-4, Step 3; verified 2026-10-06 against the 2026 form and the 2025 Instructions for Schedule 8812).

## The Math

```
Qualifying children under 17 with SSN  × $2,200  = $___
Other dependents                       × $500    = $___
Other expected credits                           = $___  (ask the user)
                                                  ━━━━━━
Total — enter on Step 3                          = $___
```

## Phaseout: When Step 3 Must Be Blank

| Filing status | Step 3 applies if total income is | Credit reduction starts above modified AGI of |
|---------------|------------------------|------|
| Single, HoH, MFS, QSS | $200,000 or less | $200,000 |
| MFJ | $400,000 or less | $400,000 |

QSS shares the MFJ box in Step 1(c), but the $400,000 threshold applies to joint returns only (Instructions for Schedule 8812 (2025): "All other filing statuses – $200,000").

**Above the threshold**, the combined CTC and ODC is reduced by $50 for each $1,000 (or fraction) of modified AGI over the threshold (IRC §24(b)(1), thresholds in §24(h)(3); Instructions for Schedule 8812 (2025), "Limits on the CTC and ODC"). The reduction applies to the total credit, not per child.

For a single filer at $250,000 modified AGI ($50,000 over): the total credit drops by 50 × $50 = $2,500. One child's $2,200 CTC is gone entirely; two children's $4,400 drops to $1,900.

**Near the threshold:** the form gives no Step 3 instruction above the threshold. If the user's total income is close to or above it, ask and recommend the Estimator rather than entering a full Step 3 amount.

## Who Is a Qualifying Child? (CTC at $2,200)

All of these must be true (IRC §152(c) tests, the §24(c) age limit and citizenship rule, and the §24(h)(7) SSN rule, as applied in the 2025 Instructions for Schedule 8812 and the Form 1040 instructions):

### 1. Relationship test

The child must be your:
- Son, daughter, stepchild, eligible foster child
- Brother, sister, half-brother/sister, step-brother/sister
- Or descendant of any (grandchild, niece, nephew)

Adopted children are treated the same as biological.

### 2. Age test

Under age 17 at the end of the tax year. A child who turned 17 on or before December 31 does NOT qualify for CTC — they qualify for the $500 ODC instead (Instructions for Schedule 8812 (2025), Example 1: a child who turned 17 on December 30 cannot be used for the CTC).

This is the most common dependents mistake — parents claim a 17-year-old high-schooler under CTC. Wrong; it's ODC.

### 3. Residency test

Lived with you more than half the year (more than 183 days). Exceptions for:
- Temporary absence (school, illness, vacation, military service, business)
- Children of divorced parents (custodial parent gets CTC unless Form 8332 signed)
- Kidnapped children (special rules under IRC §152(f))

### 4. Support test

The child did NOT provide more than half of their own support. For most kids this is trivially satisfied.

### 5. Dependent, joint return, and citizenship tests

The child must be claimed as your dependent, must not file a joint return (other than only to claim a refund), and must be a U.S. citizen, U.S. national, or U.S. resident alien.

### 6. SSN tests

- **Child:** an SSN valid for employment, issued before the return's due date (including extensions).
  - ITIN or ATIN does NOT qualify for CTC; such a child may still qualify for the $500 ODC
  - Newborn without SSN yet at filing → file extension (Form 4868) and apply for SSN ASAP
- **Taxpayer (new for 2025 and later, OBBBA):** you, or at least one spouse on a joint return, must have an SSN valid for employment issued by the due date; the other spouse needs an SSN or ITIN issued by the due date (Instructions for Schedule 8812 (2025), What's New). The 2026 Form W-4 repeats this caution in Step 1(c) and on page 2. If the user has no such SSN, Step 3 must not include the CTC.

## Who Is "Other Dependent"? (ODC at $500)

Anyone who's a "qualifying child" failing the age test (17+) or a "qualifying relative" passing all of:

### Qualifying relative tests (IRC §152(d))

1. **Not a qualifying child** of you or anyone else
2. **Relationship**: Either a relative listed in IRC §152(d)(2) (parent, sibling, in-law, etc.) OR a member of your household for the full year
3. **Gross income**: Their gross income for the year is less than $5,300 for 2026 (Rev. Proc. 2025-32 §4.23; $5,200 for 2025, Rev. Proc. 2024-40 §2.24)
4. **Support**: You provided more than half their total support
5. **Joint return**: They are not filing a joint return with their spouse (with limited exceptions)

### Common ODC scenarios

- **17-year-old high schooler still living at home** — qualifying child failing age test → $500 ODC
- **20-year-old college student** — a qualifying child for dependency purposes if a full-time student under age 24; otherwise must qualify as a qualifying relative (2026 gross income under $5,300). Either way not for CTC ($500 ODC instead since they're 17+)
- **Elderly parent you support** — qualifying relative if their 2026 gross income is under $5,300 and you provide more than half their support. Doesn't have to live with you. → $500 ODC
- **Adult disabled child** — qualifying child regardless of age IF permanently and totally disabled → still $500 ODC (over 17)
- **Boyfriend/girlfriend's child** — not your qualifying child (no relationship); only if they live with you the full year as a member of your household, you provide more than half their support, they pass the gross income test, and they are not the qualifying child of another taxpayer (such as the parent) → $500 ODC

## Coordination Rules

### MFJ — only ONE W-4 carries Step 3

Steps 3 through 4(b) go on only one W-4; withholding is most accurate on the highest-paying job's (2026 Form W-4, Step 2 note). Other spouse leaves Step 3 blank.

### Divorced/separated parents

The custodial parent gets CTC by default (IRC §152(e)). The non-custodial parent can only claim CTC if the custodial parent signs **Form 8332** releasing the claim for that year.

Common error: both parents claim the same child on their respective W-4s. Tax return e-file then rejects the second-filed return for "duplicate dependent."

### Multiple W-4s in same household

If user has TWO jobs themselves AND a working spouse with a job:
- All Step 3 credits go on the highest-paying W-4 of the three
- The other two W-4s leave Step 3 at $0

## Other Credits Field

Step 3's total line includes "the amount for other credits." The form names "the foreign tax credit and the education tax credits" as examples (2026 Form W-4, page 2).

**Ask the user; do not pick a number.** Points to raise:
- These credits are hard to predict mid-year; an overestimate means under-withholding
- Including them increases the paycheck and reduces the refund (form text)
- If the user wants to include one, base it on last year's return (e.g., the American Opportunity Credit is at most $2,500 per student, IRC §25A)

## Edge Cases

### Newborn during the year

A child born during the year is treated as having lived with you more than half the year if your home was the child's home for more than half the time the child was alive (Pub. 501 residency test), so the child can count for the CTC for that year. Submit an updated W-4 to claim the credit on remaining paychecks. Note: the child must have an SSN valid for employment by the return due date (apply at the hospital or via SSA after birth).

### Child turns 17 during the year

A child who turned 17 in 2026 does NOT qualify for CTC for tax year 2026 — IRS uses age at end of year, not start. If your previous W-4 included CTC for that child, update the W-4 to drop them to $500 ODC.

### Death of a dependent during the year

A dependent who died during the year can still be claimed for that year if the tests were met while the dependent was alive (Pub. 501). If a qualifying child was born and died in the same year without an SSN, the return must attach a birth certificate, death certificate, or hospital records showing a live birth (Instructions for Schedule 8812 (2025)). Ask before entering such a child on Step 3.

### Kidnapped child

Under IRC §152(f)(6), a kidnapped child can still be claimed as a dependent if specific conditions are met. Rare; consult Pub 501.

### Shared custody, neither parent the "majority"

If parents who don't file jointly both claim the child and the child lived with each for the same amount of time, the parent with the higher AGI gets the claim (IRC §152(c)(4)(B)(ii)) — and therefore CTC.

## Validation: How to Sanity-Check Step 3

Run these checks against the user's stated Step 3:

| Check | Action |
|-------|--------|
| Step 3 = (kids × $2,200) + (other deps × $500)? | Verify math |
| All children claimed have SSNs valid for employment? | Confirm with user |
| User (or one spouse if MFJ) has an SSN valid for employment? | Confirm with user |
| All children are under 17? | Confirm ages |
| Total household income below phaseout? | Confirm |
| Step 3 on only one W-4 (highest-paying for accuracy)? | Confirm coordination |
| User the only one claiming these dependents (vs ex-spouse)? | Confirm; flag if shared custody |
