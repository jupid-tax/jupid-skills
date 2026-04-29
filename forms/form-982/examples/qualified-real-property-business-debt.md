# Example: Small Business Owner Excluding $200K of Discharged Commercial Real Property Debt (QRPBI)

A complete walkthrough of Form 982 Box 1d — qualified real property business indebtedness under §108(a)(1)(D) and §108(c). Pattern: a sole proprietor with a workout on a commercial mortgage; basis of depreciable real property reduced; election made on Form 982.

## The filer

- **Name**: Priya Shah
- **Filing status**: Married filing jointly (spouse W-2 only)
- **Tax year**: 2025 (filing in 2026)
- **Business**: Shah Auto Body — sole proprietorship, Schedule C
- **Property**: Commercial repair shop in Tucson, AZ; held in Priya's individual name; used 100% in the auto-body trade
- **Event**: Lender (regional bank) agreed to a $200,000 principal reduction on the commercial mortgage in August 2025 after a long workout. Priya remained personally liable, kept the property, and continued operating
- **1099-C received**: Box 2 = $200,000; Box 1 = 08/22/2025; Box 6 code = F (agreement)

Priya is solvent at the time of the discharge (Worksheet 2 shows assets > liabilities by ~$110K once the $200K reduction is excluded from the snapshot). Bankruptcy was never filed. Priya wants to exclude under QRPBI rather than recognize $200K of ordinary income.

## Step 1 — Verify the 1099-C

- Box 2: $200,000 ✓
- Box 3: $0 (interest separately handled; not in Box 2)
- Box 4: "Commercial mortgage, 4521 W Industrial Ave, Tucson AZ"
- Box 5: Yes (recourse — Priya was personally liable)
- Box 6: F (debt relief from probable workout / agreement)
- Box 7: $640,000 (FMV of property at discharge)

The 1099-C is correct. Priya confirms the principal balance was reduced from $815,000 to $615,000 by recorded modification dated 08/22/2025.

## Step 2 — Identify exclusion

Walk the §108(a) menu:

- (A) Bankruptcy: no Title 11 case → skip
- (B) Insolvency: Worksheet 2 shows Priya solvent → skip (or only partial)
- (E) Principal residence: this is commercial real property, not the home → skip
- (C) Farm: not a farmer → skip
- (D) **QRPBI**: real property used in a trade or business, debt secured by it, debt was acquisition indebtedness → eligible

Priya satisfies §108(c)(3):
- Property is real (land + building)
- Used in a trade or business (Schedule C auto-body shop, not investment / not personal-use)
- Debt secured by the property (recorded mortgage)
- Debt was incurred to acquire the property in 2014 (acquisition indebtedness, post-1992 — qualifies under the second prong of §108(c)(3)(A))
- Priya is a non-corporate taxpayer (sole proprietor)

Priya makes the §108(c) election by checking Box 1d on Form 982 and attaching the basis-reduction statement.

## Step 3 — Compute the QRPBI cap

§108(c)(2) imposes two caps. The excludable amount is the LESSER of:

### Cap 1 — Excess of debt over property's FMV (immediately before discharge)

```
Outstanding principal immediately before discharge:  $815,000
- FMV of property immediately before discharge:       $640,000
= Excess of debt over FMV (Cap 1):                    $175,000
```

### Cap 2 — Adjusted basis of depreciable real property

Priya's basis records (after prior depreciation):

| Asset | Original cost | Accumulated depreciation | Adjusted basis |
|-------|---------------|--------------------------|----------------|
| Land (4521 W Industrial Ave) | $90,000 | $0 (land not depreciable) | $90,000 |
| Building | $560,000 | ($148,000) | $412,000 |
| Other depreciable real property used in business | $0 | $0 | $0 |

Land basis is **excluded** from Cap 2 — only DEPRECIABLE real property counts under §108(c)(2)(B).

```
Adjusted basis of depreciable real property (building only): $412,000
```

### Excluded amount

```
Lesser of:
  - Cap 1 (excess of debt over FMV):  $175,000
  - Cap 2 (depreciable real basis):   $412,000
  - Discharged amount (Box 2):        $200,000
= Excludable under QRPBI:             $175,000
```

**Excluded amount: $175,000** (Form 982 Line 2)
**Included on Schedule 1 Line 8c**: $200,000 − $175,000 = **$25,000** (ordinary income)

The $25,000 above the QRPBI cap is taxable. Priya cannot stack QRPBI with insolvency for the residual unless Priya is also insolvent — Worksheet 2 says no, so the $25,000 is ordinary income.

## Step 4 — Basis reduction (§1017(b)(3)(F))

The $175,000 excluded under QRPBI reduces the basis of depreciable real property. Per §1017 ordering for §108(c) discharges, the reduction goes specifically to the depreciable real property securing (or otherwise associated with) the discharged debt — here, the building.

```
Building adjusted basis before reduction:  $412,000
- §108(c) basis reduction:                ($175,000)
= Building adjusted basis after:           $237,000
```

The reduction is recorded as of the first day of the tax year FOLLOWING the discharge year (§1017(a) timing) — i.e., 1/1/2026 for a discharge in 2025. Depreciation for 2025 is unaffected; depreciation for 2026 onward is computed against the reduced basis.

Land basis ($90,000) is unchanged. Land is not depreciable real property and is outside the §108(c) basis-reduction scope.

## Step 5 — Recapture risk on future sale

§1017(d) recharacterizes the $175,000 of basis reduction as §1245 / §1250 ordinary-income recapture potential at future sale. If Priya sells the building for more than the reduced basis at a future date, the gain up to $175,000 is treated as ordinary income (subject to §1250 unrecaptured-gain rules). Priya must track this in fixed-asset records permanently.

## Step 6 — §108(b)(5) election

Box 3 on Form 982 (the §108(b)(5) election) does NOT apply to QRPBI. §108(b)(5) is an election available only for bankruptcy / insolvency exclusions, to apply attribute reduction to basis FIRST. QRPBI already mandates basis reduction by its own statutory mechanism in §108(c). Leave Line 3 unchecked.

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
| 3 | Election under §108(b)(5) | [ ] (N/A for QRPBI) |

## Part II — Reduction of Tax Attributes

| Line | Attribute | Amount reduced |
|------|-----------|----------------|
| 4 | Basis reduction under §108(c) (QRPBI) — depreciable real property | $175,000 |
| 5 | NOL (current + carryover) | $0 (N/A for QRPBI) |
| 6 | General business credit | $0 |
| 7 | Minimum tax credit | $0 |
| 8 | Net capital loss + carryover | $0 |
| 9 | Basis of other property | $0 |
| 10 | Passive activity loss + credit | $0 |
| 11 | Foreign tax credit carryover | $0 |
| | **Total Line 4-11** | **$175,000 = Line 2** ✓ |

## QRPBI cap calculation (Pub 4681 / §108(c))

| Item | Value |
|------|-------|
| Outstanding debt immediately before discharge | $815,000 |
| FMV of property immediately before discharge | $640,000 |
| Cap 1 — Excess of debt over FMV | $175,000 |
| Adjusted basis of depreciable real property (building) | $412,000 |
| Cap 2 — Depreciable real basis | $412,000 |
| Box 2 (discharged amount) | $200,000 |
| Excluded amount = lesser of $200K, $175K, $412K | $175,000 |
| Residual ordinary income (Schedule 1 Line 8c) | $25,000 |

## Required attachments / off-form items
- [x] Form 1099-C (kept with records)
- [x] §108(c) election statement attached to return: identifies the property, the debt, the FMV at discharge, basis before reduction, and basis after reduction
- [x] Updated fixed-asset register: building basis $412,000 → $237,000 effective 1/1/2026; depreciation schedule recomputed
- [x] Worksheet 2 (kept; confirms not insolvent — explains why (B) not chosen)
- [x] Schedule 1 Line 8c: $25,000 (residual ordinary income)
- [x] Schedule C (auto-body shop): unchanged for 2025; 2026 depreciation deduction reflects reduced basis
- [ ] Bankruptcy discharge order (N/A)
- [ ] Principal residence basis record (N/A)

## Validation summary
- Math: all checks passed
  - Cap 1 = $815,000 − $640,000 = $175,000 ✓
  - Cap 2 = $412,000 (building only; land excluded) ✓
  - Excluded = lesser of $200K, $175K, $412K = $175,000 ✓
  - Lines 4-11 sum = $175,000 = Line 2 ✓
  - Schedule 1 Line 8c = $200,000 − $175,000 = $25,000 ✓
- Sanity:
  - Box 1d checked once; no other Line 1 boxes
  - Land basis EXCLUDED from Cap 2 (correct — only depreciable real property)
  - §108(c) election statement attached (required)
  - §1017(d) recapture flag set in fixed-asset records (future ordinary-income recapture up to $175K)
  - Property remains used in trade/business throughout 2025 (required for QRPBI)
- §108(b)(5) election: NOT made (irrelevant to QRPBI)
- Next steps:
  - File §108(c) election statement with return
  - Update fixed-asset register effective 1/1/2026
  - Recompute 2026 depreciation against $237,000 building basis
  - Track §1017(d) recapture potential until property sold
  - Report $25,000 residual on Schedule 1 Line 8c

## Sources cited in this draft
- IRS Form 982, 2025 revision
- IRS Instructions for Form 982, 2025 revision
- IRS Pub 4681 (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRC §61(a)(11) (discharge of indebtedness as gross income)
- IRC §108(a)(1)(D) (QRPBI exclusion)
- IRC §108(c) (basis reduction election; caps)
- IRC §108(c)(3) (definition of qualified real property business indebtedness)
- IRC §1017(b)(3)(F) (basis reduction allocation for §108(c))
- IRC §1017(d) (recapture of basis reduction as ordinary income at sale)
- Form 1099-C from regional bank dated 08/22/2025
```

## Why each non-obvious choice

**Why QRPBI instead of insolvency?** Worksheet 2 shows Priya is solvent (assets > liabilities). Insolvency caps the exclusion at the insolvency amount, which is zero (or minimal) here. QRPBI applies on facts (real property, business use, acquisition debt) without requiring insolvency. For solvent business owners with secured commercial debt workouts, QRPBI is usually the only path.

**Why is land basis excluded from Cap 2?** §108(c)(2)(B) limits the basis cap to "depreciable real property". Land is real property but not depreciable. Many filers incorrectly include the full real-estate basis (land + building) and overstate Cap 2. Including land here would not change the answer ($502K still > $175K), but the principle matters in tighter cases.

**Why does Cap 1 match the excluded amount exactly?** Pure coincidence of facts. If the discharge had been only $150,000, the excluded amount would be the lesser of $150K and $175K = $150K. If the discharge had been $400,000, the excluded amount would be $175,000 (Cap 1) — and $225,000 would land on Schedule 1 Line 8c.

**Why is the basis reduction effective 1/1/2026 and not 8/22/2025?** §1017(a) says basis reductions under §108 are taken into account on the FIRST DAY of the tax year FOLLOWING the discharge year. Depreciation for the discharge year (2025) is computed against pre-reduction basis. This timing rule is universal across §108 basis reductions.

**Why track §1017(d) recapture?** When Priya eventually sells the building, gain up to the $175,000 of prior basis reduction is recharacterized as §1245-style ordinary income (notwithstanding §1250's normal treatment of real property). Without explicit tracking, the recapture is easy to miss at sale, and the IRS will reconstruct it from the §108(c) election statement on file.

**What if Priya were a C-corp?** §108(c) is unavailable to C-corporations. A C-corp would use §108(a)(1)(B) (insolvency) or §108(a)(1)(A) (bankruptcy) only. The "non-corporate" requirement in §108(c)(3)(C) is a hard gate.

**What if the property had been investment real estate (rental held passively, no Schedule C)?** Investment property generally does not qualify — §108(c)(3)(A) requires use "in a trade or business". A pure rental of real property may or may not rise to a §162 trade or business; the analysis is fact-intensive (frequency, services provided, scale). Most small-scale rentals reported on Schedule E without §162 status DO NOT qualify. Confirm before electing.

**What documentation does Priya retain?**
1. Form 1099-C from the lender
2. Recorded mortgage modification document (08/22/2025)
3. Independent appraisal supporting $640,000 FMV at discharge
4. Original closing statements for 2014 acquisition (basis substantiation)
5. Depreciation schedules 2014-2025
6. §108(c) election statement (filed with return; copy retained)
7. Updated fixed-asset register reflecting reduced basis
8. Schedule C records confirming continuous business use

Retain permanently — the basis records and §1017(d) recapture flag matter until the property is sold.
