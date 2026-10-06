# Example — Depreciation Error Correction (DCN 7)

A small business discovers in 2026 that a 2022 work truck was misclassified as 7-year MACRS property when it should have been 5-year. Files Form 3115 with DCN 7 to correct the impermissible-to-permissible depreciation method, with §481(a) catch-up.

---

## Taxpayer facts

- **Entity**: Catalyst Plumbing Services LLC (S-corp election, EIN 56-1234987)
- **Calendar tax year**
- **2022 return**: Catalyst attached a statement electing **out** of §168(k) bonus depreciation for all classes of property placed in service in 2022 (§168(k)(7)). The agent confirmed this from the filed 2022 return. Without that election, 100% bonus depreciation was the allowable method for this truck in 2022 and the numbers below change (see "What this does NOT cover")
- **Asset in question**: Ford F-350 work truck
  - **Placed in service**: April 2022
  - **Cost basis**: $52,000
  - **Use**: 100% business (plumbing service vehicle)
- **Original treatment**: classified as 7-year MACRS (heavy equipment / general-asset class) by the prior accountant
- **Correct classification**: 5-year MACRS — light general purpose trucks (actual unloaded weight less than 13,000 pounds) are **Asset Class 00.241** under Rev. Proc. 87-56 (5-year recovery period; Pub. 946, Table B-1), not a 7-year class
- **Discovered**: during 2026 fixed-asset review when the new accountant noticed the misclassification
- **Year of change**: 2026

---

## Why DCN 7 (automatic, single-asset depreciation correction)

DCN 7 (Rev. Proc. 2025-23 §6.01) covers changes from an **impermissible** to a **permissible** method of determining depreciation. This includes:
- Wrong recovery period (here: 7-year instead of 5-year)
- Wrong depreciation method (e.g., SL instead of MACRS double-declining-balance)
- Wrong convention (e.g., mid-month instead of half-year)
- Missed depreciation entirely (asset placed in service but never depreciated)

DCN 7 is **automatic consent** — no user fee, deemed consent on filing in duplicate.

Conditions for DCN 7 (Rev. Proc. 2025-23 §6.01):
- The property was placed in service before the year of change (yes — April 2022, year of change is 2026)
- The change is to a permissible method (yes — 5-year MACRS is the correct, permissible method)
- The impermissible method was used in at least the 2 tax years immediately preceding the year of change (yes — 2022 through 2025)
- The property is not on the §6.01(1)(c) exclusion list (yes)
- No return under examination (confirmed with the user; Form 3115 line 6a "No")

Once the impermissible method has been used on two or more consecutively filed returns, it is a method of accounting (Reg. §1.446-1(e)(2)(ii)(d)(2)); the correction is a Form 3115 change, not amended returns. (An S corporation amends on Form 1120-S with the "amended return" box, not "Form 1120-X".)

---

## §481(a) computation

The §481(a) catch-up captures the depreciation that **should have been** taken under the correct method, less the depreciation **actually taken** under the wrong method.

### Depreciation under the wrong method (7-year MACRS, half-year convention)

7-year MACRS percentages (Table A-1, Rev. Proc. 87-57):

| Year | % | Depreciation on $52,000 |
|------|---|--------------------------|
| 2022 | 14.29% | $7,431 |
| 2023 | 24.49% | $12,735 |
| 2024 | 17.49% | $9,095 |
| 2025 | 12.49% | $6,495 |
| **Cumulative through 2025** | | **$35,756** |

### Depreciation under the correct method (5-year MACRS, half-year convention)

5-year MACRS percentages (Table A-1, Rev. Proc. 87-57):

| Year | % | Depreciation on $52,000 |
|------|---|--------------------------|
| 2022 | 20.00% | $10,400 |
| 2023 | 32.00% | $16,640 |
| 2024 | 19.20% | $9,984 |
| 2025 | 11.52% | $5,990 |
| **Cumulative through 2025** | | **$43,014** |

### §481(a)

```
§481(a) = Cumulative correct − Cumulative actual
        = $43,014 − $35,756
        = −$7,258 (negative)
```

A **negative** §481(a) means the taxpayer **under-depreciated** in prior years and is owed a "catch-up" deduction.

### Spread

Negative §481(a) → **1-year spread** (full deduction in year of change).

Catalyst takes the entire **−$7,258** into account on the **2026 Form 1120-S** as a deduction.

---

## Going forward — 2026 depreciation

After the catch-up, Catalyst applies 5-year MACRS for 2026 onward:

| Year | 5-year MACRS % | Depreciation on $52,000 |
|------|----------------|--------------------------|
| 2026 | 11.52% | $5,990 |
| 2027 | 5.76% | $2,995 |
| **Total remaining** | | **$8,985** |

(5-year MACRS asset is fully depreciated by year 6 — the half-year convention extends recovery into year 6 for the final 5.76%.)

So 2026 deductions on this truck:
- §481(a) catch-up: $7,258
- Regular 2026 depreciation: $5,990
- **Total 2026 deduction**: $13,248

The 2026 depreciation ($5,990) goes on Form 4562 and Form 1120-S line 14. The negative §481(a) adjustment ($7,258) goes on Form 1120-S line 20 (Other deductions) with a statement giving the total adjustment and a description of the change (2025 Instructions for Form 1120-S, Line 20).

---

## Form 3115 (Rev. December 2022) — identification, Part I, Part IV

| Line | Field | Value |
|------|-------|-------|
| Identification | Name of filer / EIN | Catalyst Plumbing Services LLC / 56-1234987 |
| Identification | Tax year of change | 01/01/2026 – 12/31/2026 |
| Identification | Type of applicant | S corporation |
| Identification | Type of change | Depreciation or Amortization |
| 1a | DCN | 7 |
| 2 | Eligibility rules restrict? | No |
| 3 | All required information provided? | Yes |
| 6a | Any return under examination? | No |
| 11a | Change for same item or overall method change within 5 years? | No |
| 25 | Cut-off basis? | No |
| 26 | Section 481(a) adjustment | −$7,258 (decrease in income; statement attached) |
| 28 | Election | None (negative adjustment: year of change) |

---

## Form 3115 — Schedule E (depreciation)

Schedule E of Form 3115 is specific to depreciation changes. Entries:

| Line | Field | Value |
|------|-------|-------|
| 1 | CLADR property? | No |
| 2 | Depreciation capitalized (e.g. §263A)? | No |
| 3 | Elections made for the property | Election out of §168(k) for 2022 property (all classes); no §179 |
| 4a | Property statement | Ford F-350 work truck (VIN, year, model), placed in service April 15, 2022, cost $52,000, 100% business use, no credits or grants |
| 4b / 4c | Residential rental lived in / public utility | No / No |
| 5 | Present treatment | Depreciable property, 7-year MACRS |
| 7a | Code section | §168(a) (present and proposed) |
| 7b | Asset class | Present: 7-year class (incorrect); proposed: 00.241 Light General Purpose Trucks (Rev. Proc. 87-56) |
| 7c | Facts supporting proposed class | Actual unloaded weight under 13,000 lbs; general purpose over-the-road truck |
| 7d | Method | 200% declining balance, §168(b)(1) (present and proposed) |
| 7e | Recovery period | Present 7 years; proposed 5 years |
| 7f | Convention | Half-year (present and proposed) |
| 7g | Bonus depreciation claimed? | No — election out made for 2022 |
| 7h | Account | Single asset account |

---

## §481(a) attachment

```
§481(a) Adjustment Schedule — DCN 7 (Depreciation Method Correction)
Catalyst Plumbing Services LLC, EIN 56-1234987
Tax year of change: January 1, 2026 – December 31, 2026

Asset: Ford F-350 work truck (VIN [redacted])
Placed in service: April 15, 2022
Cost basis: $52,000
Business use: 100%

Old method (impermissible): 7-year MACRS, half-year convention
   2022: $7,431
   2023: $12,735
   2024: $9,095
   2025: $6,495
   Cumulative actual: $35,756

New method (permissible): 5-year MACRS, half-year convention
   2022: $10,400
   2023: $16,640
   2024: $9,984
   2025: $5,990
   Cumulative correct: $43,014

§481(a) = $43,014 − $35,756 = −$7,258 (negative)

Spread: 1-year (default for negative §481(a))
   2026 (year of change): −$7,258 fully deductible

Going-forward depreciation under correct method:
   2026: $5,990
   2027: $2,995

Citation for asset classification: Rev. Proc. 87-56, Asset Class 00.241
   (light general purpose trucks, actual unloaded weight under 13,000 lbs,
   5-year recovery period under MACRS; Pub. 946 Table B-1)
```

---

## Filing logistics

| Task | Date | Detail |
|------|------|--------|
| Year of change | 2026 | Catalyst's 2026 tax year |
| Form 3115 prepared | with 2026 return | Likely Q1 2027 prep cycle |
| Signed copy to Ogden | between 01/01/2026 and the day the return is filed | M/S 6111 by certified mail, or fax 844-249-8134 |
| Original attached to | Form 1120-S 2026 | Including extensions, latest September 15, 2027 |
| §481(a) recognized | 2026 return | −$7,258 (full deduction) |
| 2027+ depreciation | 5-year MACRS | $2,995 in 2027 (final year of recovery) |

---

## What this does NOT cover

- **Form 1120-S amendment for 2022-2025**: the taxpayer does NOT amend prior years; the impermissible method used on 2+ consecutive returns is changed on Form 3115.
- **Bonus depreciation**: bonus depreciation under §168(k) applies unless the taxpayer elects out for the class of property (§168(k)(7)); for property placed in service in 2022 the rate was 100%. If Catalyst had **not** elected out, the allowable depreciation for 2022 was the full $52,000, so the permissible method includes bonus and the §481(a) adjustment would be $35,756 − $52,000 = **−$16,244**, with no 2026 or 2027 regular depreciation left. That is why the agent must read the filed 2022 return (Schedule E line 3, line 7g) before computing. An election out, once made, generally can be revoked only with IRS consent; DCN 7 does not reopen it.
- **State conformity**: state depreciation rules vary. The §481(a) catch-up may have a different value at state level (e.g., states that decoupled from federal bonus depreciation). State Form 3115 equivalents (where they exist) are filed separately.

---

## Common errors avoided

1. **Amending prior-year Forms 1120-S**: not the fix. The impermissible method has been adopted by use on 2+ consecutive returns; Form 3115 + §481(a) fixes it.
2. **Computing §481(a) only for the years of error**: the §481(a) is **cumulative** through the start of the year of change. For an asset in service since 2022 with a year of change of 2026, the cumulative covers 2022-2025.
3. **Missing the half-year convention**: 5-year MACRS uses a half-year convention by default; mid-quarter applies if > 40% of asset acquisitions in the year were in the last quarter (rare for single-asset cases).
4. **Wrong asset class**: a Ford F-350 work truck used in plumbing services (actual unloaded weight under 13,000 lbs) is Asset Class 00.241 (5-year). Heavy general purpose trucks (13,000 lbs or more unloaded) are 00.242, also 5-year; tractor units for use over the road are 00.26 (3-year) (Pub. 946, Table B-1). Verify the unloaded weight and use.
5. **Forgetting the signed copy to Ogden**: the DCN 7 change is not properly filed.
6. **Assuming no bonus depreciation**: confirm whether an election out of §168(k) was made in the placed-in-service year.

---

## Output for the user

The agent delivers to Catalyst:

1. **Form 3115 draft** (Parts I, IV, Schedule E) with depreciation specifics
2. **§481(a) schedule**: 4-year cumulative comparison with table-based MACRS percentages
3. **2026 deduction summary**: $7,258 catch-up + $5,990 regular depreciation = $13,248 total
4. **Filing checklist**: Ogden mailing, return attachment, retention
5. **Asset classification citation**: Rev. Proc. 87-56 Asset Class 00.241 with rationale
6. **Future-year tracker**: $2,995 deduction in 2027 (final year of MACRS recovery)
