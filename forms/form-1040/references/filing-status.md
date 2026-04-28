# Filing Status Reference

The five filing statuses on Form 1040, with eligibility rules. Filing status controls standard deduction, tax brackets, EITC eligibility, and dozens of phaseout thresholds.

**Legal basis**: IRC §1(a)-(d) (rate schedules by status), IRC §2 (definition of HoH and surviving spouse), IRC §7703 (married for tax purposes).

---

## 1. Single

**Eligibility (any of these on December 31)**:
- Never married
- Divorced under a final decree of divorce or separate maintenance
- Legally separated under a state court decree
- Widowed and not eligible for QSS

If you got divorced or legally separated on December 31, you're considered single for the entire year. Same for marriage on December 31 — you're considered married for the entire year.

**Standard deduction (2025)**: $15,000.

**Brackets (2025)**: 10% up to $11,925 → 12% up to $48,475 → 22% up to $103,350 → 24% up to $197,300 → 32% up to $250,525 → 35% up to $626,350 → 37% above.

---

## 2. Married Filing Jointly (MFJ)

**Eligibility**:
- Married on December 31 (or spouse died during the year and you didn't remarry)
- Both spouses agree to file jointly
- Both spouses sign the return

A common-law marriage recognized by the state where the relationship began counts as married for federal tax. Same-sex marriage is recognized federally regardless of state. Domestic partnerships and civil unions are NOT marriage for federal tax purposes.

**Standard deduction (2025)**: $30,000 (double the single amount).

**Brackets (2025)**: 10% up to $23,850 → 12% up to $96,950 → 22% up to $206,700 → 24% up to $394,600 → 32% up to $501,050 → 35% up to $751,600 → 37% above.

**Joint and several liability**: each spouse is fully liable for the entire tax, including any errors or omissions by the other. If concerned about a spouse's reporting, consider Innocent Spouse Relief (Form 8857) or filing MFS.

**Almost always lower tax than MFS** — the joint brackets are wider, and many credits phase out faster or aren't available at all on MFS.

---

## 3. Married Filing Separately (MFS)

**Eligibility**:
- Married on December 31
- Choose to file separately rather than jointly

Both spouses must use the same deduction method (both standard or both itemized). If one itemizes, the other cannot take the standard deduction — they must itemize too, even if their itemized deductions are $0.

**Standard deduction (2025)**: $15,000 (same as single, but if spouse itemizes, must itemize).

**Brackets (2025)**: same as MFJ but at half the thresholds — 10% up to $11,925 → 12% up to $48,475 → etc.

**When MFS makes sense**:
- One spouse has large medical expenses and the AGI floor (7.5% of AGI) is lower on a separate return
- Liability concerns (one spouse's tax issues / fraud / non-payment shouldn't bind the other)
- Income-driven student loan repayment plan (lower individual AGI = lower monthly payment, though TCJA made this less common)
- Separated but not legally divorced and don't want to file jointly

**Restrictions on MFS**:
- Cannot claim EITC
- Cannot claim Saver's Credit
- Cannot deduct student loan interest
- Cannot exclude US Savings Bond interest used for education
- Cannot take the dependent care credit (in most cases)
- Cannot take the AOTC or Lifetime Learning Credit
- Roth IRA contribution phaseout starts at $0 (vs. $146,000 single) for MFS who lived with spouse during the year
- IRA deduction phaseout extremely tight if covered by retirement plan
- 85% of Social Security is taxable starting at $0 combined income (vs. $32,000 MFJ) for MFS who lived with spouse

Run the math both ways before choosing MFS — it rarely beats MFJ.

---

## 4. Head of Household (HoH)

**Eligibility — ALL three must be true**:

1. **Unmarried** on December 31, OR considered unmarried (= married but lived apart from spouse for the last 6 months of the year, paid more than half the cost of keeping up a home that was the main home for the filer's qualifying child, and is not filing jointly).
2. **Paid more than half the cost** of keeping up a home for the year. "Cost of keeping up a home" = rent or mortgage interest, property tax, home insurance, utilities, food eaten in the home, household repairs.
3. **A qualifying person lived with the filer more than half the year** (or, for a dependent parent, the parent doesn't have to live with the filer — the filer must just pay more than half the cost of the parent's main home).

**Qualifying person for HoH**:
- Qualifying child (most common)
- Qualifying relative (only certain ones — not all dependents qualify)
- Mother or father (dependent parent)
- Brother, sister, half-sibling, step-sibling, niece, nephew (if the dependent meets the qualifying relative test)

**NOT a qualifying person for HoH**: cousins, aunts/uncles, unrelated dependents (e.g., a friend you support).

**Standard deduction (2025)**: $22,500 (between Single and MFJ).

**Brackets (2025)**: 10% up to $17,000 → 12% up to $64,850 → 22% up to $103,350 → 24% up to $197,300 → 32% up to $250,525 → 35% up to $626,350 → 37% above. Wider than Single brackets in the lower tiers.

**Audit risk**: HoH is the most-misclaimed filing status. The IRS audits incorrect HoH claims often. Common errors:
- 50/50 custody — only ONE parent can claim HoH (typically the higher-AGI parent absent agreement)
- Married but not "considered unmarried" — still married = MFJ or MFS
- No qualifying person — a roommate or non-relative dependent doesn't qualify
- Nephew/cousin lived with filer but doesn't meet qualifying relative test

When in doubt, run the qualifying person test from `dependents.md` before claiming HoH.

---

## 5. Qualifying Surviving Spouse (QSS)

**Eligibility (all must be true)**:
- Spouse died during one of the two preceding tax years (i.e., 2023 or 2024 deaths qualify for tax year 2025 QSS)
- Filer has not remarried before December 31
- Filer has a dependent child (son, daughter, stepchild, adopted child) who lived with filer all year, except for temporary absences
- Filer paid more than half the cost of keeping up the home that was the main home of that child for the entire year
- Filer could have filed jointly with the deceased spouse in the year of death

The year the spouse dies, the filer can file MFJ. The two following years, if the conditions are met, the filer can file QSS (uses MFJ brackets). After that, filer typically files HoH (if dependent qualifying child still in home) or Single.

**Standard deduction (2025)**: $30,000 (same as MFJ).

**Brackets (2025)**: same as MFJ (most favorable).

---

## Decision tree

```
Spouse died in last 2 years AND have dependent child living with you?
  → QSS (uses MFJ brackets — most favorable)

Married on Dec 31?
  → MFJ usually better than MFS. Run both. MFS only if specific reasons.

Unmarried + paid > half cost of home + qualifying person lived with you > half year?
  → HoH

Otherwise unmarried?
  → Single
```

---

## Edge cases

**Divorced mid-year**: filing status as of December 31. Divorced on Dec 31 = Single (or HoH if qualifying person). Married on Dec 31 = MFJ or MFS.

**Death of spouse mid-year**: in the year of death, surviving spouse can file MFJ (if conditions met). The next two years may qualify for QSS.

**Innocent spouse**: filed MFJ but want to limit liability for spouse's errors → Form 8857 Innocent Spouse Relief or Form 8379 Injured Spouse Allocation.

**Resident alien spouse, nonresident alien spouse**: can elect to treat NRA spouse as resident alien for tax purposes (Section 6013(g) election) and file MFJ. Otherwise file MFS or HoH (if qualifying person).

**Same-sex marriage**: recognized federally regardless of state. File MFJ or MFS like any married couple.

**Domestic partnership / civil union**: NOT marriage for federal tax purposes, even if state recognizes. File Single or HoH.

**Common-law marriage**: recognized federally if recognized by the state where the relationship began (typically AL, CO, IA, KS, MT, NH, OK, RI, SC, TX, UT). File MFJ or MFS.

---

## Sources

- IRC §1(a)-(d) — rate schedules by filing status
- IRC §2(a) — definition of QSS
- IRC §2(b) — definition of HoH
- IRC §7703 — determination of marital status
- [Publication 501](https://www.irs.gov/publications/p501) — Dependents, Standard Deduction, and Filing Information (the canonical IRS reference)
- Rev. Proc. 2024-40 — 2025 brackets and standard deductions
