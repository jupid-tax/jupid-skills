# Student Loan Discharge — IRC §108(f)

Federal tax treatment of canceled student loans is layered: a few **permanent** exclusions exist for specific situations, a **temporary, broad** exclusion under ARPA covered discharges after Dec. 31, 2020 and before Jan. 1, 2026, and for discharges **after 2025** P.L. 119-21 (One Big Beautiful Bill Act) §70119 rewrote §108(f)(5) as a permanent exclusion for death and total and permanent disability discharges only.

Sources checked on 2026-10-06: IRC §108(f) text and notes (law.cornell.edu); Pub. 4681 (2025), "Student Loans"; Instructions for Forms 1099-A and 1099-C (Rev. April 2025), What's New; Notice 2022-1.

This file maps each sub-rule, lists the 1099-C handling for each, and flags the date-dependent items.

---

## Exclusions that don't depend on the discharge year

If the discharge fits one of these, the canceled amount is excluded. **No Form 982** — Form 982 is for §108(a) exclusions, and Pub. 4681 treats student loans under "Exceptions".

### §108(f)(1) — Work-requirement cancellation (e.g., PSLF)

**Scope:** The loan was made by a qualified lender (U.S. or a state agency, certain tax-exempt public-benefit hospitals, or an educational organization under the conditions in Pub. 4681) and its terms cancel all or part of it if the borrower works for a certain period, in certain professions, for any of a broad class of employers (Pub. 4681). Public Service Loan Forgiveness fits this pattern.

**Not covered:** cancellation by an educational organization or 501(c)(3) organization because of services the borrower performed for that organization (§108(f)(3); Pub. 4681 caution).

**Treatment:** Excluded from income. The borrower simply does not report the canceled amount.

**Practical note:** If a 1099-C is issued for a qualifying discharge, the borrower can claim the exclusion and keep the program documentation, or ask the servicer for a corrected 1099-C.

### §108(f)(4) — Student loan repayment assistance

Payments made to the borrower under the National Health Service Corps Loan Repayment Program, a state education loan repayment program eligible for funds under the Public Health Service Act, or any other state loan repayment or forgiveness program intended to increase health services in underserved or shortage areas (Pub. 4681). Interest paid with those payments isn't deductible.

### Death or total and permanent disability (TPD)

**Scope:** Discharge on account of the death or total and permanent disability of the student — under HEA §437(a) or (d) or the parallel Part D benefit, §464(c)(1)(F), or otherwise — of a student loan or a private education loan (§108(f)(5) as amended by P.L. 119-21 §70119).

**Treatment:**
- Discharges in 2018–2025: excluded (TCJA rule, then the broader ARPA rule).
- Discharges **after Dec. 31, 2025**: excluded under the rewritten §108(f)(5), **but only if the taxpayer's SSN is on the return**; the SSN must be valid for employment and issued before the return due date (§108(f)(5)(C); Pub. 4681 What's New).

---

## ARPA broad exclusion — discharges after 2020 and before 2026

The **American Rescue Plan Act of 2021** (P.L. 117-2, §9675) made a broad range of education-loan discharges federally tax-free if the discharge happened **after Dec. 31, 2020 and before Jan. 1, 2026**.

### Scope

Per Pub. 4681 and Notice 2022-1, the rule covered:

- Loans for postsecondary educational expenses made, insured, or guaranteed by the United States, a state or territory (or political subdivision), or an eligible educational institution — whether provided through the school or directly to the borrower
- Private education loans (as defined in the Truth in Lending Act)
- Loans from an educational organization described in §170(b)(1)(A)(ii)
- Loans from a §501(a) tax-exempt organization to refinance a student loan

The reason for the discharge didn't matter (income-driven repayment forgiveness, closed school, borrower defense, settlements), subject to the exception for discharges for services to the lender.

### Treatment

Excluded from federal income. **No Form 982.** Notice 2022-1 told lenders and servicers not to file Form 1099-C for these discharges; if one arrived anyway, the borrower excludes the amount and keeps the discharge notice.

### Discharges after 2025

The broad rule expired: the Instructions for Forms 1099-A and 1099-C (Rev. April 2025) say the §108(f)(5) student loan relief "expires on December 31, 2025", and P.L. 119-21 replaced §108(f)(5) with the death/TPD rule only. For a discharge on or after Jan. 1, 2026 that isn't work-requirement (§108(f)(1)), repayment-assistance (§108(f)(4)), or death/TPD:

1. Treat it as canceled-debt income (Schedule 1 Line 8c for a personal loan)
2. Test §108(a)(1)(B) insolvency — borrowers getting student-loan relief are often insolvent
3. Test §108(a)(1)(A) bankruptcy if there was a title 11 discharge
4. Re-check https://www.irs.gov/forms-pubs/about-form-982 and IRS.gov for later legislation before filing

---

## State tax treatment

State conformity to federal §108(f) varies, and some states tax canceled student loans that are federally excluded. Rules change often. The agent should:

1. Identify the borrower's state of residence
2. Check whether the state conforms to §108(f) for the year of discharge (state revenue department)
3. If the state does not conform, the canceled amount may be reportable on the state return even if federally excluded

This reference is federal-focused. For state analysis, refer the user to a state-tax practitioner or the state's department of revenue.

---

## How to claim — by category

| Sub-rule | Form 982 needed? | Where it shows |
|----------|------------------|----------------|
| §108(f)(1) work requirement (e.g., PSLF) | No | Not reported |
| §108(f)(4) repayment assistance | No | Not reported |
| Death / TPD, discharged 2021–2025 | No | Not reported |
| Death / TPD, discharged after 2025 | No | Not reported; SSN must be on the return |
| ARPA broad rule, discharged after 2020 and before 2026 | No | Not reported |
| §108(a)(1)(B) insolvency fallback | Yes | Form 982 box 1b; Line 2 capped by insolvency |
| §108(a)(1)(A) bankruptcy fallback | Yes | Form 982 box 1a; Line 2 = discharged amount |

---

## 1099-C handling

For 2021–2025 discharges under the ARPA rule, lenders were directed not to file a 1099-C (Notice 2022-1). A 1099-C received for such a discharge is likely an error; the amount is still excluded.

For discharges after 2025 that aren't covered by §108(f), expect a 1099-C from the lender if the amount is $600 or more, and report or exclude it under the general §108 rules.

---

## Workflow for a student loan 1099-C

1. **Identify the loan type** — federal, state, school, private education loan, refinance?
2. **Identify the discharge category** — work requirement (PSLF), repayment assistance, death/TPD, other (IDR forgiveness, closed school, borrower defense, settlement)?
3. **Check the discharge date** — before Jan. 1, 2026 (ARPA rule available) or after 2025 (only §108(f)(1), (4), and death/TPD)?
4. **Map to the right exclusion** — see the table above
5. **Federal handling** — claim the exclusion (no Form 982) or fall back to insolvency / bankruptcy (Form 982)
6. **State handling** — flag for the user; refer to the state's revenue department

---

## Common mistakes

1. **Treating all student loan discharges as taxable** — the 2021–2025 ARPA rule and the permanent sub-rules exclude many discharges.
2. **Assuming the ARPA rule covers a 2026 discharge** — it applies only to discharges before Jan. 1, 2026.
3. **Omitting the SSN for a post-2025 death/TPD exclusion** — the rewritten §108(f)(5) requires it.
4. **Attaching Form 982 for a §108(f) exclusion** — Form 982 is for §108(a); §108(f) exclusions need none.
5. **Ignoring state tax** — some states tax canceled student loans even when federally excluded. Flag this.

---

## Sources

- IRC §108(f)(1), (3), (4), (5) — student loan rules; §108(f)(5) as amended by P.L. 119-21 §70119 (effective for discharges after Dec. 31, 2025)
- ARPA 2021 (P.L. 117-2), §9675 — broad rule for discharges after Dec. 31, 2020 and before Jan. 1, 2026
- [Notice 2022-1](https://www.irs.gov/pub/irs-drop/n-22-01.pdf) — no 1099-C for ARPA-excluded discharges
- [Publication 4681 (2025)](https://www.irs.gov/publications/p4681) — "Student Loans" (exceptions), What's New (SSN requirement)
- [Instructions for Forms 1099-A and 1099-C (Rev. April 2025)](https://www.irs.gov/pub/irs-pdf/i1099ac.pdf) — What's New
- HEA §437 (20 U.S.C. §1087) — death and disability discharge authority
- [Federal Student Aid: Loan Forgiveness](https://studentaid.gov/manage-loans/forgiveness-cancellation)

**Year-aware:** for any discharge after 2025, re-check §108(f) for later legislation before filing.
