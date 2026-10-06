# Example: Small Business Owner Excluding $200K of Discharged Commercial Real Property Debt (QRPBI)

A complete walkthrough of Form 982 Box 1d — qualified real property business indebtedness under §108(a)(1)(D) and §108(c). Pattern: a sole proprietor with a workout on a commercial mortgage; basis of depreciable real property reduced on line 4; election made by checking box 1d on a timely filed return; the taxable remainder goes to Schedule C. Lines follow Form 982 (Rev. March 2018) and its Instructions (Rev. December 2021).

## The filer

- **Name**: Priya Shah
- **Filing status**: Married filing jointly (spouse W-2 only)
- **Tax year**: 2025 (filing in 2026)
- **Business**: Shah Auto Body — sole proprietorship, Schedule C
- **Property**: Commercial repair shop in Tucson, AZ; held in Priya's individual name; used 100% in the auto-body trade
- **Event**: Lender (regional bank) agreed to a $200,000 principal reduction on the commercial mortgage in August 2025 after a long workout. Priya remained personally liable, kept the property, and continued operating
- **1099-C received**: Box 2 = $200,000; Box 1 = 08/22/2025; Box 6 code = F (agreement)

Priya is solvent immediately before the discharge: the Pub. 4681 Insolvency Worksheet, with the full $815,000 shop loan counted as a liability, shows total liabilities of $1,118,000 (line 15) and total assets of $1,458,200 (line 37), so line 38 is −$340,200. Bankruptcy was never filed. Priya wants to exclude under QRPBI rather than recognize $200K of ordinary income.

## Step 1 — Verify the 1099-C

- Box 2: $200,000 ✓
- Box 3: $0 (interest separately handled; not in Box 2)
- Box 4: "Commercial mortgage, 4521 W Industrial Ave, Tucson AZ"
- Box 5: Yes (recourse — Priya was personally liable)
- Box 6: F (by agreement)
- Box 7: blank (box 7 is for a foreclosure, abandonment, or short sale; Priya kept the property; Instructions for Forms 1099-A and 1099-C)

The 1099-C is correct. Priya confirms the principal balance was reduced from $815,000 to $615,000 by recorded modification dated 08/22/2025. An independent appraisal puts the shop (land and building) at $640,000 FMV immediately before the discharge.

## Step 2 — Identify exclusion

Walk the §108(a) menu:

- (A) Bankruptcy: no Title 11 case → skip
- (B) Insolvency: the Insolvency Worksheet shows Priya solvent → skip
- (E) Principal residence: this is commercial real property, not the home → skip
- (C) Farm: not a farmer → skip
- (D) **QRPBI**: real property used in a trade or business, debt secured by it, debt was acquisition indebtedness → eligible

Priya satisfies §108(c)(3):
- Property is real (land + building)
- Used in a trade or business (Schedule C auto-body shop, not investment / not personal-use; not held for sale to customers)
- Debt secured by the property (recorded mortgage)
- Debt was incurred to acquire the property in 2014: a $1,037,700 acquisition loan on a $1,153,000 purchase (land $168,000, building $985,000). Post-1992 debt qualifies as qualified acquisition indebtedness (§108(c)(3)(B), (c)(4))
- Priya is not a C corporation (sole proprietor) — §108(a)(1)(D)

Priya makes the election by checking Box 1d and completing Form 982 on her timely filed 2025 return, including extensions (Pub. 4681 "How to elect the qualified real property business debt exclusion"); she attaches the §1017 basis-reduction description the Part II header requires.

## Step 3 — Compute the QRPBI cap

§108(c)(2) imposes two caps. The excludable amount is the LESSER of:

### Cap 1 — Excess of debt over property's FMV (immediately before discharge)

```
Outstanding principal immediately before discharge:  $815,000
- FMV of property immediately before discharge:       $640,000
  (no other QRPBI secured by the shop reduces the FMV)
= Excess of debt over FMV (Cap 1):                    $175,000
```

### Cap 2 — Adjusted basis of depreciable real property

Priya's basis records (accumulated depreciation through Dec. 31, 2025, from her depreciation schedule; the Form 982 instructions measure this limit as of the first day of the next tax year, i982 Line 1d):

| Asset | Original cost | Accumulated depreciation | Adjusted basis |
|-------|---------------|--------------------------|----------------|
| Land (4521 W Industrial Ave) | $168,000 | $0 (land not depreciable) | $168,000 |
| Building | $985,000 | ($291,510) | $693,490 |
| Other depreciable real property used in business | $0 | $0 | $0 |

Land basis is **excluded** from Cap 2 — only DEPRECIABLE real property counts under §108(c)(2)(B).

```
Adjusted basis of depreciable real property (building only): $693,490
```

### Excluded amount

```
Lesser of:
  - Cap 1 (excess of debt over FMV):  $175,000
  - Cap 2 (depreciable real basis):   $693,490
  - Discharged amount (Box 2):        $200,000
= Excludable under QRPBI:             $175,000
```

**Excluded amount: $175,000** (Form 982 Line 2)
**Included in income on Schedule C Line 6** (business debt of a nonfarm sole proprietorship; Pub. 4681): $200,000 − $175,000 = **$25,000** (ordinary income)

The $25,000 above the QRPBI cap is taxable. Insolvency could cover it only if Priya were insolvent; the worksheet says no, so the $25,000 is ordinary income. It flows through Schedule C Line 31 to Schedule 1 Line 3 and Schedule SE Line 2 (2025 Schedule C, line 31).

## Step 4 — Basis reduction (§1017(b)(3)(F))

The $175,000 excluded under QRPBI reduces the basis of depreciable real property only (§108(c)(1); §1017(b)(3)(F)(i)). Priya's only depreciable real property is the building that secured the loan, so it absorbs the whole reduction (Form 982 line 4).

```
Building adjusted basis before reduction:  $693,490
- §108(c) basis reduction (line 4):       ($175,000)
= Building adjusted basis after:           $518,490
```

The reduction is recorded as of the first day of the tax year FOLLOWING the discharge year (§1017(a) timing) — i.e., 1/1/2026 for a discharge in 2025 — or immediately before a sale if Priya disposed of the building first (§1017(b)(3)(F)(iii); Pub. 4681). Depreciation for 2025 is unaffected; depreciation for 2026 onward is computed against the reduced basis.

Land basis ($168,000) is unchanged. Land is not depreciable real property and is outside the §108(c) basis-reduction scope.

## Step 5 — Recapture risk on future sale

§1017(d)(1) treats the $175,000 basis reduction as a deduction allowed for depreciation for §§1245 and 1250, and §1017(d)(2) figures §1250 straight-line depreciation as if there had been no reduction. So if Priya later sells the building at a gain, the part of the gain due to the $175,000 reduction is ordinary income under the recapture rules (Pub. 4681 "Recapture of basis reductions"). Priya must track this in fixed-asset records until the building is sold.

## Step 6 — §108(b)(5) election

Line 5 on Form 982 (the §108(b)(5) election) is available only when box 1a, 1b, or 1c is checked (i982 Part II "Basis Reduction"). Priya checks only 1d, and QRPBI already mandates basis reduction by its own statutory mechanism in §108(c): **Line 5 = $0**. Line 3 (the §1017(b)(3)(E) election for real property held for sale) doesn't apply to QRPBI (i982 Line 3): **No**.

## The completed Form 982 draft

```markdown
# Form 982 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Priya Shah and Raj Shah
Identifying number: XXX-XX-XXXX (Priya, the QRPBI obligor)

## Part I — General Information

| Line | Description | Value |
|------|-------------|-------|
| 1a | Discharge in a Title 11 case | [ ] |
| 1b | Discharge to extent insolvent | [ ] |
| 1c | Discharge of qualified farm indebtedness | [ ] |
| 1d | Discharge of qualified real property business indebtedness | [x] |
| 1e | Discharge of qualified principal residence indebtedness | [ ] |
| 2 | Total amount of discharged indebtedness excluded from gross income | $175,000 |
| 3 | Elect to treat §1221(a)(1) real property as depreciable property? | No (doesn't apply to QRPBI) |

## Part II — Reduction of Tax Attributes (amount excluded applied)

| Line | Attribute | Amount |
|------|-----------|--------|
| 4 | QRPBI applied to reduce basis of depreciable real property (building) | $175,000 |
| 5 | §108(b)(5) election | $0 (not available with 1d alone) |
| 6 | NOL | $0 (QRPBI reduces only depreciable real property basis) |
| 7 | General business credit | $0 |
| 8 | Minimum tax credit | $0 |
| 9 | Net capital loss + carryover | $0 |
| 10a | Basis of nondepreciable and depreciable property | $0 |
| 10b | Basis of principal residence | $0 |
| 11a–11c | Farm debt basis | $0 |
| 12 | Passive activity loss + credit | $0 |
| 13 | Foreign tax credit carryover | $0 |

Line 4 $175,000 = Line 2 $175,000 ✓

## Part III
Blank (corporations only)

## QRPBI cap calculation (Pub. 4681 / §108(c))

| Item | Value |
|------|-------|
| Outstanding debt immediately before discharge | $815,000 |
| FMV of property immediately before discharge | $640,000 |
| Cap 1 — Excess of debt over FMV | $175,000 |
| Adjusted basis of depreciable real property (building) | $693,490 |
| Cap 2 — Depreciable real basis | $693,490 |
| Box 2 (discharged amount) | $200,000 |
| Excluded amount = lesser of $200K, $175K, $693,490 | $175,000 |
| Residual ordinary income (Schedule C Line 6) | $25,000 |

## Required attachments / off-form items
- [x] Form 1099-C (kept with records)
- [x] §1017 basis-reduction statement attached to return (Form 982 Part II header): describes the 08/22/2025 workout, identifies the building, basis before ($693,490) and after ($518,490) the reduction
- [x] Updated fixed-asset register: building basis $693,490 → $518,490 effective 1/1/2026; depreciation schedule recomputed
- [x] Insolvency Worksheet (kept; confirms not insolvent — explains why (B) not chosen)
- [x] Schedule C Line 6: $25,000 (residual ordinary income)
- [x] Schedule C (auto-body shop): Line 6 includes the $25,000 for 2025; 2025 depreciation unchanged; 2026 depreciation reflects reduced basis
- [ ] Bankruptcy discharge order (N/A)
- [ ] Principal residence basis record (N/A)

## Validation summary
- Math: all checks passed
  - Cap 1 = $815,000 − $640,000 = $175,000 ✓
  - Cap 2 = $693,490 (building only; land excluded) ✓
  - Excluded = lesser of $200K, $175K, $693,490 = $175,000 ✓
  - Line 4 = $175,000 = Line 2 ✓
  - Schedule C Line 6 = $200,000 − $175,000 = $25,000 ✓
- Sanity:
  - Box 1d only (Priya not insolvent; no title 11 case)
  - Land basis EXCLUDED from Cap 2 (correct — only depreciable real property)
  - Election made by checking 1d on the timely filed 2025 return; §1017 statement attached
  - §1017(d) recapture flag set in fixed-asset records (future ordinary-income recapture of the $175K reduction)
  - Property used in the trade or business (required for QRPBI)
- §108(b)(5) election: NOT made (Line 5 not available with 1d alone)
- Next steps:
  - File Form 982 with the timely 2025 return (if left off, the 1d election can still be made on an amended return within 6 months of the due date, excluding extensions, marked "Filed pursuant to section 301.9100-2")
  - Update fixed-asset register effective 1/1/2026
  - Recompute 2026 depreciation against $518,490 building basis
  - Track §1017(d) recapture potential until property sold
  - Report $25,000 residual on Schedule C Line 6

## Sources cited in this draft
- IRS Form 982 (Rev. March 2018)
- IRS Instructions for Form 982 (Rev. December 2021), When To File, Line 1d, Line 3, Part II
- IRS Pub. 4681 (2025) (Canceled Debts, Foreclosures, Repossessions, and Abandonments), QRPBI sections and examples
- 2025 Schedule C (Form 1040), lines 6 and 31
- IRC §61(a)(11) (discharge of indebtedness as gross income)
- IRC §108(a)(1)(D) (QRPBI exclusion; taxpayers other than C corporations)
- IRC §108(c) (basis reduction; caps)
- IRC §108(c)(3) (definition of qualified real property business indebtedness)
- IRC §1017(b)(3)(F) (basis reduction allocation for §108(c))
- IRC §1017(d) (recapture of basis reduction as ordinary income at sale)
- Form 1099-C from regional bank dated 08/22/2025
```

## Why each non-obvious choice

**Why QRPBI instead of insolvency?** The Insolvency Worksheet shows Priya is solvent (assets > liabilities). Insolvency caps the exclusion at the insolvency amount, which is zero (or minimal) here. QRPBI applies on facts (real property, business use, acquisition debt) without requiring insolvency. For solvent business owners with secured commercial debt workouts, QRPBI is usually the only path.

**Why is land basis excluded from Cap 2?** §108(c)(2)(B) limits the basis cap to "depreciable real property". Land is real property but not depreciable. Many filers incorrectly include the full real-estate basis (land + building) and overstate Cap 2. Including land here would not change the answer ($861,490 still > $175K), but the principle matters in tighter cases.

**Why does Cap 1 match the excluded amount exactly?** Pure coincidence of facts. If the discharge had been only $150,000, the excluded amount would be the lesser of $150K and $175K = $150K. If the discharge had been $400,000, the excluded amount would be $175,000 (Cap 1) — and $225,000 would land on Schedule C Line 6.

**Why is the basis reduction effective 1/1/2026 and not 8/22/2025?** §1017(a) applies the reduction to property held at the beginning of the tax year FOLLOWING the discharge year. Depreciation for the discharge year (2025) is computed against pre-reduction basis. For QRPBI property sold before then, the reduction is made immediately before the sale (§1017(b)(3)(F)(iii)).

**Why track §1017(d) recapture?** When Priya eventually sells the building at a gain, the part of the gain due to the $175,000 basis reduction is ordinary income: §1017(d)(1) treats the reduction as depreciation, and §1017(d)(2) figures §1250 straight-line depreciation as if there had been no reduction (Pub. 4681 "Recapture of basis reductions"). Without explicit tracking, the recapture is easy to miss at sale.

**What if Priya were a C-corp?** The QRPBI exclusion is unavailable to C corporations: §108(a)(1)(D) applies only "in the case of a taxpayer other than a C corporation". A C-corp would use §108(a)(1)(A) (bankruptcy), (B) (insolvency), or (C) (farm) only. An S corporation applies §108 at the corporate level (§108(d)(7)).

**What if the property had been rental real estate (Schedule E, no Schedule C)?** §108(c)(3)(A) requires real property used in a trade or business. Pub. 4681 says residential rental property generally qualifies as real property used in a trade or business unless the user also uses the dwelling as a home (see Pub. 527). Land held for investment and real property held primarily for sale to customers do not qualify. Taxable cancellation of rental-property debt goes on Schedule E Line 3 (Pub. 4681). Confirm the facts before electing.

**What documentation does Priya retain?**
1. Form 1099-C from the lender
2. Recorded mortgage modification document (08/22/2025)
3. Independent appraisal supporting $640,000 FMV at discharge
4. Original closing statements for 2014 acquisition (basis substantiation)
5. Depreciation schedules 2014-2025
6. §1017 basis-reduction statement (filed with return; copy retained)
7. Updated fixed-asset register reflecting reduced basis
8. Schedule C records confirming continuous business use

Retain until the period of limitations expires for the year the building is sold — the basis records and §1017(d) recapture flag matter until then (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records).
