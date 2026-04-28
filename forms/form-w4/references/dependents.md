# Step 3 — Dependents Reference

Step 3 reduces federal withholding by the expected Child Tax Credit (CTC) and Credit for Other Dependents (ODC). It only applies if total household income is below the phaseout.

## The Math

```
Qualifying children under 17 with SSN  × $2,000  = $___
Other dependents                       × $500    = $___
Other expected credits                           = $___  (usually $0)
                                                  ━━━━━━
Total — enter on Step 3                          = $___
```

## Phaseout: When Step 3 Must Be $0

| Filing status | Phaseout begins at AGI |
|---------------|------------------------|
| Single, HoH, MFS | $200,000 |
| MFJ, QSS | $400,000 |

**Above the phaseout**, the CTC reduces by $50 per $1,000 of AGI above the threshold (IRC §24(b)).

For a household at $250K AGI single (50K above threshold): CTC reduces by 50 × $50 = $2,500 per child. So a $2,000 CTC for one child would actually phase out completely.

**Rule of thumb:** If you're within $50,000 of the phaseout, leave Step 3 blank and claim the credit on your tax return instead. Better to have slightly higher withholding than under-withhold and owe a penalty.

## Who Is a Qualifying Child? (CTC at $2,000)

All FIVE tests must pass (IRC §152(c)):

### 1. Relationship test

The child must be your:
- Son, daughter, stepchild, eligible foster child
- Brother, sister, half-brother/sister, step-brother/sister
- Or descendant of any (grandchild, niece, nephew)

Adopted children are treated the same as biological.

### 2. Age test

Under age 17 at the end of the tax year. A child who turned 17 on December 31 does NOT qualify for CTC — they qualify for the $500 ODC instead.

This is the most common dependents mistake — parents claim a 17-year-old high-schooler under CTC. Wrong; it's ODC.

### 3. Residency test

Lived with you more than half the year (more than 183 days). Exceptions for:
- Temporary absence (school, illness, vacation, military service, business)
- Children of divorced parents (custodial parent gets CTC unless Form 8332 signed)
- Kidnapped children (special rules under IRC §152(f))

### 4. Support test

The child did NOT provide more than half of their own support. For most kids this is trivially satisfied.

### 5. SSN test (NEW since TCJA 2017)

The child must have a valid SSN issued before the return's due date (including extensions).

- ITIN does NOT qualify for CTC (only ODC)
- ATIN (adoption taxpayer identification number) does NOT qualify
- Newborn without SSN yet at filing → file extension (Form 4868) and apply for SSN ASAP

## Who Is "Other Dependent"? (ODC at $500)

Anyone who's a "qualifying child" failing the age test (17+) or a "qualifying relative" passing all of:

### Qualifying relative tests (IRC §152(d))

1. **Not a qualifying child** of you or anyone else
2. **Relationship**: Either a relative listed in IRC §152(d)(2) (parent, sibling, in-law, etc.) OR a member of your household for the full year
3. **Gross income**: Their gross income for the year is below the exemption amount (~$5,200 for 2025; check Pub 501 for current year)
4. **Support**: You provided more than half their total support
5. **Joint return**: They are not filing a joint return with their spouse (with limited exceptions)

### Common ODC scenarios

- **17-year-old high schooler still living at home** — qualifying child failing age test → $500 ODC
- **20-year-old college student** — must be a "qualifying child" if a full-time student and under age 24, otherwise must qualify under the $5,200 income test. Full-time student under 24 → still qualifies as "qualifying child" for dependency purposes BUT not for CTC ($500 ODC instead since they're 17+)
- **Elderly parent you support** — qualifying relative if their income is below ~$5,200 and you pay more than half their costs. Doesn't have to live with you. → $500 ODC
- **Adult disabled child** — qualifying child regardless of age IF permanently and totally disabled → still $500 ODC (over 17)
- **Boyfriend/girlfriend's child** — not your qualifying child (no relationship); only if they live with you full year + you support them → $500 ODC

## Coordination Rules

### MFJ — only ONE spouse claims dependents on Step 3

Higher-paying spouse claims them so the credit reduces withholding from a higher-bracket paycheck. Other spouse leaves Step 3 blank.

### Divorced/separated parents

The custodial parent gets CTC by default (IRC §152(e)). The non-custodial parent can only claim CTC if the custodial parent signs **Form 8332** releasing the claim for that year.

Common error: both parents claim the same child on their respective W-4s. Tax return e-file then rejects the second-filed return for "duplicate dependent."

### Multiple W-4s in same household

If user has TWO jobs themselves AND a working spouse with a job:
- All Step 3 credits go on the highest-paying W-4 of the three
- The other two W-4s leave Step 3 at $0

## Other Credits Field

Step 3 has a sub-line for "expected other credits" — education credits, foreign tax credit, residential energy credit, etc.

**Default this to $0.** Reasons:
- These credits are notoriously hard to predict mid-year
- Better to claim them on the tax return than reduce withholding upfront
- If you're wrong, you under-withhold and owe a penalty

The exception: if you're certain about a large refundable credit (e.g., American Opportunity Credit for education, $2,500 max per student), you can include it. But verify with last year's return.

## Edge Cases

### Newborn during the year

If a child is born during the year, they count for the full year for CTC (IRC §24(c)). Submit an updated W-4 to claim the credit on remaining paychecks. Note: the child must have an SSN by the return due date (apply at the hospital or via SSA after birth).

### Child turns 17 during the year

A child who turned 17 in 2026 does NOT qualify for CTC for tax year 2026 — IRS uses age at end of year, not start. If your previous W-4 included CTC for that child, update the W-4 to drop them to $500 ODC.

### Death of a dependent during the year

A dependent who died during the year can still be claimed as a dependent for that full year if they would have qualified before death. CTC eligibility is based on age at death (under 17 → CTC, 17+ → ODC).

### Kidnapped child

Under IRC §152(f)(6), a kidnapped child can still be claimed as a dependent if specific conditions are met. Rare; consult Pub 501.

### Shared custody, neither parent the "majority"

If custody is exactly 50/50, the parent with higher AGI gets the dependency claim (IRC §152(c)(4)(C)) — and therefore CTC.

## Validation: How to Sanity-Check Step 3

Run these checks against the user's stated Step 3:

| Check | Action |
|-------|--------|
| Step 3 = (kids × $2,000) + (other deps × $500)? | Verify math |
| All children claimed have SSNs? | Confirm with user |
| All children are under 17? | Confirm ages |
| Total household income below phaseout? | Confirm |
| Step 3 only on highest-paying W-4? | Confirm coordination |
| User the only one claiming these dependents (vs ex-spouse)? | Confirm; flag if shared custody |
