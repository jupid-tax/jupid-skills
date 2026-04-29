# Example — Depreciation Error Correction (DCN 7)

A small business discovers in 2026 that a 2022 work truck was misclassified as 7-year MACRS property when it should have been 5-year. Files Form 3115 with DCN 7 to correct the impermissible-to-permissible depreciation method, with §481(a) catch-up.

---

## Taxpayer facts

- **Entity**: Catalyst Plumbing Services LLC (S-corp election, EIN 56-1234987)
- **Calendar fiscal year**
- **Asset in question**: Ford F-350 work truck
  - **Placed in service**: April 2022
  - **Cost basis**: $52,000
  - **Use**: 100% business (plumbing service vehicle)
- **Original treatment**: classified as 7-year MACRS (heavy equipment / general-asset class) by the prior accountant
- **Correct classification**: 5-year MACRS — light general-purpose trucks fall in **Asset Class 00.242** under Rev. Proc. 87-56 (5-year recovery period), not the 7-year machinery class
- **Discovered**: during 2026 fixed-asset review when the new accountant noticed the misclassification
- **Year of change**: 2026

---

## Why DCN 7 (automatic, single-asset depreciation correction)

DCN 7 in Rev. Proc. 2024-23 (or successor) covers changes from an **impermissible** to a **permissible** depreciation method. This includes:
- Wrong recovery period (here: 7-year instead of 5-year)
- Wrong depreciation method (e.g., SL instead of MACRS double-declining-balance)
- Wrong convention (e.g., mid-month instead of half-year)
- Missed depreciation entirely (asset placed in service but never depreciated)

DCN 7 is **automatic consent** — no user fee, deemed consent on filing in duplicate.

Conditions for DCN 7 (verify against current Rev. Proc.):
- The asset was placed in service before the year of change (yes — April 2022, year of change is 2026)
- The change is to a permissible method (yes — 5-year MACRS is the correct, permissible method)
- The taxpayer has used the impermissible method for at least 2 prior tax years (yes — 2022, 2023, 2024, 2025 = 4 prior years)
- Not under IRS examination on this asset (assumed yes for this example)

DCN 7 is the **only** way to correct a multi-year depreciation error. Filing an amended return for one prior year (Form 1120-X) does NOT fix the issue; the IRS treats the impermissible method as "established" once it has been used for 2+ years.

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

Catalyst recognizes the entire **−$7,258** as additional depreciation deduction on the **2026 Form 1120-S**.

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

This goes on Form 1120-S Line 14 (Depreciation) with a separate sub-line or attachment labeled "§481(a) adjustment, DCN 7, depreciation method correction".

---

## Form 3115 — Part I

| Line | Field | Value |
|------|-------|-------|
| 1a | Name of filer | Catalyst Plumbing Services LLC |
| 1b | EIN | 56-1234987 |
| 2 | Tax year of change | January 1, 2026 – December 31, 2026 |
| 3 | Type of return | Form 1120-S (S-corp) |
| 4 | Type of accounting method change | Depreciation (impermissible to permissible) |
| 5 | DCN | 7 |
| 6 | Section 481(a) adjustment | −$7,258 |
| 7 | Spread | 1-year (negative) |

---

## Form 3115 — Schedule E (depreciation)

Schedule E of Form 3115 is specific to depreciation changes. Required entries:

| Line | Field | Value |
|------|-------|-------|
| Asset description | | Ford F-350 work truck (VIN, year, model) |
| Date placed in service | | April 15, 2022 |
| Cost basis | | $52,000 |
| Business use % | | 100% |
| Old method | Recovery period | 7 years |
| Old method | Convention | Half-year |
| Old method | Method | 200% DB switching to SL |
| New method | Recovery period | 5 years |
| New method | Convention | Half-year |
| New method | Method | 200% DB switching to SL |
| Asset class (old) | | (incorrect — 7-year machinery class) |
| Asset class (new) | | 00.242 (light general-purpose trucks) under Rev. Proc. 87-56 |
| Citation for new method | | Rev. Proc. 87-56, Asset Class 00.242 |

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

Citation for asset classification: Rev. Proc. 87-56, Asset Class 00.242
   (light general-purpose trucks, 5-year recovery period under MACRS)
```

---

## Filing logistics

| Task | Date | Detail |
|------|------|--------|
| Year of change | 2026 | Catalyst's 2026 tax year |
| Form 3115 prepared | with 2026 return | Likely Q1 2027 prep cycle |
| Duplicate to Ogden | before/with return filing | Certified mail with return receipt |
| Original attached to | Form 1120-S 2026 | Including extensions, latest September 15, 2027 |
| §481(a) recognized | 2026 return | −$7,258 (full deduction) |
| 2027+ depreciation | 5-year MACRS | $2,995 in 2027 (final year of recovery) |

---

## What this does NOT cover

- **Form 1120-S amendment for 2022-2025**: the taxpayer does NOT amend prior years. DCN 7 is the only path; amended returns for years on an impermissible method are not allowed.
- **Bonus depreciation reconsideration**: if the truck qualified for §168(k) bonus depreciation in 2022 (it did — heavy SUVs/trucks > 6,000 lbs GVW are bonus-eligible), and the taxpayer didn't elect bonus, the §168(k) election is now closed. DCN 7 corrects the recovery period but does not re-open the bonus-depreciation election.
- **State conformity**: state depreciation rules vary. The §481(a) catch-up may have a different value at state level (e.g., states that decoupled from federal bonus depreciation). State Form 3115 equivalents (where they exist) are filed separately.

---

## Common errors avoided

1. **Filing Form 1120-X for prior years**: not allowed. The impermissible method has been "established" by 2+ years of use; only Form 3115 + §481(a) fixes it.
2. **Computing §481(a) only for the years of error**: the §481(a) is **cumulative** through the start of the year of change. For an asset in service since 2022 with a year of change of 2026, the cumulative covers 2022-2025.
3. **Missing the half-year convention**: 5-year MACRS uses a half-year convention by default; mid-quarter applies if > 40% of asset acquisitions in the year were in the last quarter (rare for single-asset cases).
4. **Wrong asset class**: a Ford F-350 work truck used in plumbing services is Asset Class 00.242 (5-year). A heavy duty truck > 13,000 lbs GVW used over the road for hire is Asset Class 00.26 (3-year). Verify the GVW and use case.
5. **Forgetting the duplicate to Ogden**: invalidates DCN 7 consent.

---

## Output for the user

The agent delivers to Catalyst:

1. **Form 3115 draft** (Parts I, IV, Schedule E) with depreciation specifics
2. **§481(a) schedule**: 4-year cumulative comparison with table-based MACRS percentages
3. **2026 deduction summary**: $7,258 catch-up + $5,990 regular depreciation = $13,248 total
4. **Filing checklist**: Ogden mailing, return attachment, retention
5. **Asset classification citation**: Rev. Proc. 87-56 Asset Class 00.242 with rationale
6. **Future-year tracker**: $2,995 deduction in 2027 (final year of MACRS recovery)
