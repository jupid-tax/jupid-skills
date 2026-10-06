# Example: Rental Condo Owner Making the §871(d) Election (First Return, Form W-7)

A Brazilian resident who owns a Miami condo rented to a long-term tenant. She is not otherwise engaged in a U.S. trade or business. Shows the choice between 30% of gross rents on Schedule NEC and the §871(d) net-basis election, the eight-item election statement, Schedule OI item M, a refund of 30% withholding from Form 1042-S, the 16-month rule, and a paper filing with Form W-7. Tax year 2025, filed in 2026. All amounts were checked with a Python script (Tax Table row 5,300–5,350 Single = $533 verified against the 2025 Tax Table; MACRS rate from Pub. 946 Table A-6).

## The filer

- **Name**: Camila Duarte (single)
- **Citizenship / tax residence**: Brazil / Brazil. The U.S. has no income tax treaty with Brazil (Brazil does not appear in IRS Tax Treaty Table 1, Rev. May 2023), so no treaty rate applies.
- **Property**: condo in Miami, Florida, bought for cash in December 2024 for $318,000 (land $67,000, building $251,000 per the county assessor's allocation); ready and available for rent and leased from January 2025; managed by a local property manager for 8% of rent
- **Visa**: B-1/B-2 visa; never applied for a green card
- **Identifying number**: none (no SSN, no ITIN)
- **Prior returns**: none

## Inputs gathered

| Item | Amount | Source |
|---|---|---|
| Gross rents ($2,650 × 12) | $31,800 | Manager's year-end statement |
| HOA dues | $6,420 | Statement |
| Miami-Dade property tax paid November 2025 | $5,118 | Tax receipt |
| Insurance | $2,286 | Policy |
| Repairs | $1,375 | Invoices |
| Management fee (8% × $31,800) | $2,544 | Statement |
| Depreciation: $251,000 × 3.485% (27.5-year, mid-month, placed in service January; Pub. 946 Table A-6) | $8,747 | Computed through [`../../schedule-e/SKILL.md`](../../schedule-e/SKILL.md) |
| Form 1042-S from the manager: gross rents January–March, 30% withheld (box 10) | $2,385 | Form 1042-S |

The manager withheld 30% on gross rents until April 2025, when she gave the manager Form W-8ECI with a statement of her intent to make the §871(d) election for 2025 (Form W-8ECI instructions). Withholding-agent mechanics are outside this skill; the agent records only the Form 1042-S figure.

Days present (item G): 01/03/25–01/17/25 and 07/20/25–08/09/25 = 15 + 21 = **36**. 2024: 29. 2023: 41.

## Step 2 — Residency

Substantial presence: 36 + 29/3 + 41/6 = 36 + 9.67 + 6.83 = **52.5** → not met. Green card: no. **Nonresident alien for all of 2025.**

## Step 3 — Filing requirement and due date

- Not engaged in a U.S. trade or business (rental through a manager, no other U.S. activity; the election does not make her engaged).
- Schedule NEC-type income on which not all tax was withheld (April–December rents had no withholding) → must file (Table A item 2). Making the election and claiming deductions also require a timely return.
- No wages → due **June 15, 2026**. This is the first year a return is required, so deductions survive only if the return is filed within 16 months: by **October 15, 2027** (Treas. Reg. §1.874-1(b)).

## Step 4 — The two computations shown to the user

| | No election (Schedule NEC line 6) | §871(d) election (Schedule E → Schedule 1 line 5 → line 8) |
|---|---|---|
| Tax base | Gross rents $31,800 | Net rents $31,800 − $26,490 = $5,310 |
| Rate | 30%, column (c) | Graduated, Single |
| Tax | **$9,540** | **$533** |

Expenses on the election side: 6,420 + 5,118 + 2,286 + 1,375 + 2,544 + 8,747 = $26,490.

Agent question asked before drafting: "The election covers all your U.S. rental property now and in future years, and it can only be revoked with IRS consent; after a revocation you can't elect again until after the fifth year. Do you want to make it for 2025?" She said yes. The agent recommended a CPA review of the election statement.

## Step 5 — The election statement (attached to the 2025 return)

The Instructions for Form 1040-NR list eight required items. Draft:

1. Camila Duarte elects under section 871(d) to treat all income from real property located in the United States, and from any interest in such property, as income effectively connected with the conduct of a U.S. trade or business, beginning with tax year 2025.
2. Property: one residential condominium unit, [street address], Miami, Florida [ZIP]. No U.S. timber, coal, or iron ore interests.
3. Ownership: 100%.
4. Substantial improvements: none since acquisition in December 2024.
5. 2025 income from the property: gross rents $31,800.
6. Dates owned: December 2024 through the date of this return.
7. The election is made under section 871(d) (not under a treaty).
8. Previous elections and revocations: none.

Schedule OI item M(1) is checked.

## The completed draft

```markdown
# Form 1040-NR — DRAFT for tax year 2025 (filed in 2026)

## Residency determination
- Green card test: No
- Substantial presence: 36 + 29/3 + 41/6 = 52.5 (31-day test: pass) → not met
- Conclusion: Nonresident alien for all of 2025
- Due date: June 15, 2026 (no wages); 16-month deadline: October 15, 2027

## Header
Name: Camila Duarte   Identifying number: left blank — Form W-7 attached (reason (a))
Filing status: Single   Special boxes: none   Digital assets: No
Dependents: none

## Page 1 — Effectively connected income
1a–1h. $0 each   1i, 1j. Reserved   1k. $0   1z. $0
2a. $0   2b. $0   3a. $0   3b. $0   4a/4b. $0 / $0   5a/5b. $0 / $0   6. Reserved   7a. $0
8.   Schedule 1, line 10 (line 5, Schedule E rental under §871(d)): $5,310
9.   Total effectively connected income:      $5,310
10.  Adjustments:                             $0
11a. AGI:                                     $5,310

## Page 2 — Tax and payments
11b. AGI:                                     $5,310
12.  Itemized deductions:                     $0  (no state income tax, no U.S. charitable gifts;
                                                   property tax is a Schedule E expense, not a Schedule A item)
13a. $0   13b. —   13c. $0
14.  Add 12–13c:                              $0
15.  Taxable income:                          $5,310
16.  Tax (Tax Table, row 5,300–5,350, Single): $533
17.  $0   18. $533   19. $0   20. $0   21. $0   22. $533
23a. Schedule NEC tax:                        $0
23b. $0   23c. $0   23d. $0
24.  Total tax:                               $533
25a–25d. $0   25e. $0   25f. $0
25g. Form 1042-S withholding:                 $2,385
26.  $0   27. Reserved   28–32. $0
33.  Total payments:                          $2,385
34.  Overpaid:                                $1,852
35a. Refund:                                  $1,852 (paper check)
35e. Mail refund to: [São Paulo address] (same as page 1, so blank)
36.  $0   37. $0   38. $0

## Schedule NEC
Not filed: rents are ECI under the §871(d) election; no other U.S.-source income.

## Schedule A (Form 1040-NR)
Not filed: no allowable itemized deductions.

## Schedule OI
A. Brazil   B. Brazil   C. No   D1. No   D2. No   E. B-2   F. No
G. 01/03/25 entered; 01/17/25 departed; 07/20/25 entered; 08/09/25 departed
H. 2023: 41   2024: 29   2025: 36
I. No   J. No   K. No   L. none
M(1). Checked — first year of the section 871(d) election (statement attached)

## Attachments and companion filings
- [x] Form W-7 on top, with identification documents (see ../../form-w7/SKILL.md)
- [x] Form 1042-S (front of return)
- [x] Schedule 1; Schedule E with Form 4562; §871(d) election statement
- [ ] 2026: give the manager an updated Form W-8ECI if any information changes; Form 1040-ES (NR) if tax will be owed

## Validation summary
- Math: all checks passed (Schedule E net 31,800 − 26,490 = 5,310; 9 = 8; 15 = 11b − 14;
  24 = 22; 33 = 25g; 34 = 33 − 24)
- Classification: all rents ECI under the election; nothing on Schedule NEC
- Sanity: deductions depend on the return being filed by October 15, 2027; W-7 package must be paper filed

## Sources cited in this draft
- 2025 Form 1040-NR, Schedule OI; Instructions for Form 1040-NR (2025): Income You Can Elect To Treat
  as Effectively Connected, Schedule 1 line 5, Schedule NEC line 6, Schedule OI item M
- 2025 Instructions for Form 1040 (Tax Table); Pub. 946 Table A-6; Pub. 519 (2025) ch. 4 and ch. 7
- IRC §871(d), §874(a), §6072(c); Treas. Reg. §1.874-1(b)
- Instructions for Form W-7 (Rev. December 2024); Instructions for Form W-8ECI; IRS Tax Treaty Table 1 (Rev. May 2023)
```

## Why each non-obvious choice

**Why not leave the rents on Schedule NEC?** Without the election the 30% tax applies to gross rents with no deductions: $9,540 against $533 on the net basis. The election is a choice, so the agent showed both numbers and asked.

**Why is the property tax not on Schedule A?** Schedule A (Form 1040-NR) has no property tax line; only state and local income taxes are deductible there. The property tax is a rental expense on Schedule E because the election makes the rental income ECI.

**Why a 16-month warning?** Deductions for a nonresident exist only on a timely, true, and accurate return. If this return were filed after October 15, 2027, the IRS could tax the $31,800 of gross rents with no expenses.

**Why paper?** She has no ITIN. The return goes behind Form W-7 to the IRS ITIN Operation, and a return using an ITIN can't be e-filed in the calendar year the ITIN is assigned (Instructions for Form W-7). Mail the package to Internal Revenue Service, ITIN Operation, P.O. Box 149342, Austin, TX 78714-9342, not to the Form 1040-NR address ([`../filing.md`](../filing.md)).

**What happens when she sells?** A sale of a U.S. real property interest is ECI automatically (FIRPTA), reported on Schedule D and line 7a, with the buyer's withholding credited from Form 8288-A on line 25f.
