# Example: Sarah, S-Corp Owner Drops Equipment Business Use (§179 Recapture, Part IV)

End-to-end Form 4797 for a Part IV §179 recapture scenario where business use drops without a sale.

---

## Facts

- **Filer:** Sarah, sole shareholder of S-corp consulting practice (Form 1120-S)
- **Asset:** 2023 GPU workstation and server equipment (computers and peripheral equipment, 5-year MACRS property). Not listed property: computers placed in service after 2017 are not listed property (2025 Form 4562 instructions, Lines 26 and 27), so Part IV column (a) applies, not column (b)
- **Date placed in service:** 03/15/2023
- **Business use 2023:** 100% — full-year business use
- **§179 deduction taken in 2023:** $80,000 (the entire cost; within the 2023 §179 limit of $1,160,000 under Rev. Proc. 2022-38). The S-corp elected §179 on its 2023 Form 4562 and passed the deduction through on Schedule K, Line 11; Sarah deducted it on her 2023 Schedule E, Part II, column (j)
- **Original cost:** $80,000
- **2024 business use:** 80% (still above 50% threshold)
- **2025 business use:** 40% (DROPPED below 50%; the equipment is now mostly used for personal projects)
- **Current year:** 2025 (the year of the business-use drop)
- **Equipment still owned, NOT sold**

(Why not a vehicle? A heavy SUV would have been capped at the §179(b)(5) SUV limit, $28,900 for 2023, and a vehicle is listed property, which uses Part IV column (b) and a straight-line ADS recomputation instead of the steps below. Do not reuse this example for a vehicle.)

---

## Step 1 — Trigger identification

When a §179 property's business use drops to **50% or less** in any tax year before the end of the recovery period (5 years for this equipment), recapture is triggered under IRC §179(d)(10) and Reg. §1.179-1(e). This is the case here:

- 2025 business use = 40% ≤ 50% → **Part IV recapture required**

Note: The equipment is NOT sold. There is no gain or loss disposition. Part I, Part II, Part III are NOT used. Only Part IV.

---

## Step 2 — Compute "what depreciation would have been" under MACRS

Figure the depreciation that would have been allowable on the §179 amount, starting with the year placed in service and including the year of recapture, at each year's business-use percentage (Pub. 946 (2025), chapter 2, "Figuring the recapture amount"). Regular MACRS 5-year, half-year convention, Table A-1:

| Year | MACRS % | Depreciation |
|------|---------|----------------------------|
| 2023 | 20% | $80,000 × 20% × 100% biz use = $16,000 |
| 2024 | 32% | $80,000 × 32% × 80% biz use = $20,480 |
| 2025 (year of recapture, full table %) | 19.2% | $80,000 × 19.2% × 40% biz use = $6,144 |
| **Total recomputed depreciation through 2025** | | **$42,624** |

Pub. 946's own example applies the full table percentage in the year of recapture, multiplied by that year's business-use percentage; it does not halve it.

---

## Step 3 — Compute Part IV (on Sarah's Form 4797)

| Line | Field | (a) Section 179 | (b) Section 280F(b)(2) |
|------|-------|-------------|---------------------|
| 33 | Section 179 expense deduction or depreciation allowable in prior years | $80,000 | blank (not listed property) |
| 34 | Recomputed depreciation | $42,624 | blank |
| 35 | Recapture amount (Line 33 − Line 34) | **$37,376** | blank |

The $37,376 is ordinary income.

---

## Step 4 — Where the recapture goes

Per the 2025 Form 4797 instructions for Line 35, the recapture amount is reported as "other income" on the same form or schedule on which the deduction was taken.

- The S-corp did not deduct the §179 itself: it passed the $80,000 through on Schedule K, Line 11 (Form 1120-S), and Sarah deducted it on her own return.
- For 2025, the S-corp reports the recapture information on Sarah's Schedule K-1 (Form 1120-S), **Box 17, code L** ("Recapture of section 179 deduction"): her share of the original basis and depreciation allowed or allowable (not counting §179), and the §179 amount passed through with the year it was passed through (2025 Instructions for Form 1120-S, Schedule K, code L; 2025 Shareholder's Instructions for Schedule K-1, code L).
- Sarah completes Part IV of **her own** Form 4797 with those figures and reports the $37,376 as other income on Schedule E, Part II, on the S-corp's row, the schedule where she took the deduction.

---

## Step 5 — Basis adjustment

The $37,376 recaptured amount adds back to the equipment's basis for future depreciation. Going forward:

```
Original cost:                      $80,000
§179 deducted (2023):              ($80,000)
Recapture in 2025:                  +$37,376
Adjusted basis after 2025 recapture: $37,376

Equivalently: $80,000 − $42,624 recomputed MACRS = $37,376
```

The equipment can continue to be depreciated on the restored basis over the rest of the MACRS recovery period (2026, 2027, 2028 at 11.52% / 11.52% / 5.76%), at each year's business-use percentage. With business use at or below 50%, confirm the method with a CPA before taking those deductions.

If business use drops further in subsequent years (e.g., to 0% in 2026), there is no additional Part IV recapture (Part IV applies only in the year business use first drops to 50% or less, not in subsequent years), but depreciation deductions cease.

---

## Step 6 — What the forms look like

The S-corp's 2025 return: no Form 4797 Part IV entry for this property; Schedule K-1 Box 17, code L carries the recapture information to Sarah.

Sarah's 2025 Form 4797:

| Section | Lines used | Lines NOT used |
|---------|-----------|----------------|
| Part I (§1231) | None | All |
| Part II (Ordinary) | None on 4797 | All |
| Part III (Recapture on disposition) | None | All |
| **Part IV (§179/§280F recapture)** | **Lines 33-35, column (a)** | Column (b) |

Only Part IV is completed. The recapture amount flows OUT of Form 4797 (to Schedule E, Part II), not through Form 4797 Part II.

---

## Step 7 — Required attachments and downstream forms

- [x] Sarah's Form 4797 with Part IV, column (a) completed
- [x] Schedule K-1 (Form 1120-S) Box 17, code L statement (from the S-corp)
- [x] Schedule E, Part II: $37,376 recapture as other income on the S-corp's row
- [ ] No Schedule D entries (no disposition)
- [ ] No Schedule 1 Line 4 entry (Part II of Form 4797 was not used)

---

## Step 8 — Tax impact

Sarah's 2025 ordinary federal bracket: 32%

```
Federal ordinary tax on $37,376 × 32%:           $11,960
SE tax on this amount:                            $0  (not SE income — passes through S-corp)
Net Investment Income Tax (NIIT):                 $0  (NIIT does not apply to active business income)
State tax (varies):                              ~$1,869 (assume 5% state)
Total tax cost of the business-use drop:        ~$13,829
```

The $37K recapture is a tax cost of using the equipment less for business. It reverses the timing benefit Sarah got from §179 in 2023. The "recapture" gives back the difference between §179 (immediate full expensing) and MACRS (slower).

---

## Step 9 — What if Sarah's S-corp had sold instead?

If the S-corp had SOLD the equipment in 2025 instead of Sarah dropping business use, the analysis would shift to Part III §1245 recapture, not Part IV §179 recapture. Specifically:

- Asset is fully depreciated (basis = $0 after §179 in 2023)
- Sales price (whatever it is) is 100% gain
- Gain is fully §1245 ordinary recapture (limited by depreciation taken = $80K, which always exceeds gain)
- Reported on Part III (Line 31) → Part II Line 13; for property whose §179 was passed through, follow the 2025 Form 4797 instructions' worksheet for partners and S corporation shareholders

The "drop business use" path (Part IV) and the "sell" path (Part III) are mutually exclusive — you don't do both for the same year. If a sale happens, it supersedes the business-use drop logic.

---

## Lessons from this example

1. **Part IV is not for sales.** It is the rare case of recapture-without-disposition, triggered by IRC §179(d)(10) when business use of a §179 asset drops to ≤50% before recovery period ends.

2. **Recapture flows BACK to the original deduction's form.** Not to Part II Line 13. For a §179 deduction passed through an S-corp, this means K-1 Box 17 code L → the shareholder's Form 4797 Part IV → Schedule E, Part II.

3. **Basis is restored by the recapture amount.** The asset can resume MACRS depreciation on the recaptured basis.

4. **Listed property + §280F.** Part IV column (b) covers §280F(b)(2) for listed property whose business use drops. The recomputation there uses straight-line ADS (Pub. 946, chapter 5), not the regular MACRS table used above.

5. **This rule is the "gotcha" of generous expensing.** §179 and bonus depreciation are timing benefits, not permanent ones. Aggressive expensing today means recapture risk if business circumstances change.
