# Example: Sarah, S-Corp Owner Drops Vehicle Business Use (§179 Recapture, Part IV)

End-to-end Form 4797 for a Part IV §179 recapture scenario where business use drops without a sale.

---

## Facts

- **Filer:** Sarah, sole shareholder of S-corp consulting practice (Form 1120-S)
- **Asset:** 2023 Tesla Model X (over 6,000 lbs, qualifies for §179 vehicle expensing)
- **Date placed in service:** 03/15/2023
- **Business use 2023:** 100% — full-year business use
- **§179 deduction taken in 2023:** $80,000 (the entire cost of the vehicle, within §179 limit and Heavy SUV cap rules in effect at the time)
- **Original cost:** $80,000
- **2024 business use:** 80% (still above 50% threshold)
- **2025 business use:** 40% (DROPPED below 50%)
- **Current year:** 2025 (the year of the business-use drop)
- **Vehicle still owned, NOT sold**

---

## Step 1 — Trigger identification

When a §179 property's business use drops to **50% or less** in any tax year before the end of the recovery period (5-year MACRS for vehicles), recapture is triggered under IRC §179(d)(10) and §280F(b)(2). This is the case here:

- 2025 business use = 40% ≤ 50% → **Part IV recapture required**

Note: The vehicle is NOT sold. There is no gain or loss disposition. Part I, Part II, Part III are NOT used. Only Part IV.

---

## Step 2 — Compute "what depreciation would have been" under MACRS

If Sarah had NOT taken §179 and had instead depreciated under regular MACRS 5-year half-year convention (assuming 100% business use 2023 and 80% in 2024 — though luxury auto §280F caps would also apply, simplified here):

| Year | MACRS % | Depreciation (no §280F cap) |
|------|---------|----------------------------|
| 2023 | 20% | $80,000 × 20% = $16,000 |
| 2024 | 32% | $80,000 × 32% × 80% biz use = $20,480 |
| 2025 (year of drop, half-year) | 19.2% × 50% | $80,000 × 9.6% × 40% biz use = $3,072 |
| **Total recomputed depreciation through 2025** | | **$39,552** |

(In a real filing, §280F luxury auto annual caps would typically reduce these amounts further. This example uses simplified MACRS for clarity. For an actual return, use the §280F first-year, second-year, and subsequent-year caps — see Pub 946 Table B-1 and the §280F annual depreciation cap table.)

---

## Step 3 — Compute Part IV

| Line | Field | §179 Column | §280F(b)(2) Column |
|------|-------|-------------|---------------------|
| 33 | Section 179 deduction or §280F deduction taken in prior years | $80,000 | $0 (no §280F listed-property deductions claimed separately) |
| 34 | Recomputed depreciation under MACRS | $39,552 | $0 |
| 35 | Recapture amount (Line 33 − Line 34) | **$40,448** | $0 |

The $40,448 is ordinary income.

---

## Step 4 — Where the recapture goes

Per Form 4797 instructions, the Part IV recapture amount goes back to the form/schedule where the original deduction was claimed:

- Sarah's S-corp claimed §179 in 2023 on Form 1120-S Line 12 (Officer compensation/general deduction tracked through Form 4562). The S-corp's Form 4562 in 2023 elected §179 on Line 12.
- The recapture in 2025 is reported on **Form 1120-S Line 5 (Other income)** at the corporate level, OR passed through to the shareholder's Schedule K-1 Line 17V (depending on whether the S-corp made the §179 election at entity vs shareholder level).

For most S-corps, §179 elections flow through to shareholders, so the recapture also flows through. Sarah's K-1 will show:
- Schedule K-1 Line 17V (Other items): "§179 recapture under §1.179-1(e): $40,448"

She reports this on her individual Form 1040 Schedule 1 Line 8 (Other income) with a label.

---

## Step 5 — Basis adjustment

The $40,448 recaptured amount adds back to the vehicle's basis for future depreciation. Going forward:

```
Original cost:                      $80,000
§179 deducted (2023):              ($80,000)
MACRS depreciation 2023-2025:      ($39,552)  (recomputed amount)
Recapture in 2025:                  +$40,448
Basis at start of 2026:             $0  (full §80K cost has now been depreciated through MACRS only)

OR equivalently:
  Adjusted basis after 2025 recapture = $80,000 − $39,552 = $40,448
```

Sarah can continue depreciating the remaining $40,448 over the rest of the MACRS recovery period (years 2026, 2027, 2028 at 11.52% / 11.52% / 5.76%, applied to remaining basis with year-of-drop business-use percentage).

If business use drops further in subsequent years (e.g., to 0% in 2026), there is no additional Part IV recapture (Part IV applies only in the year business use first drops below 50%, not in subsequent years), but depreciation deductions cease.

---

## Step 6 — What Form 4797 looks like

Sarah's S-corp 2025 Form 4797:

| Section | Lines used | Lines NOT used |
|---------|-----------|----------------|
| Part I (§1231) | None | All |
| Part II (Ordinary) | None on 4797 | All |
| Part III (Recapture on disposition) | None | All |
| **Part IV (§179/§280F recapture)** | **Lines 33-35** | — |

Only Part IV is completed. The recapture amount flows OUT of Form 4797 (to Form 1120-S Line 5 or Schedule K-1), not through Form 4797 Part II.

---

## Step 7 — Required attachments and downstream forms

- [x] Form 4797 with Part IV completed
- [x] Form 1120-S Schedule K-1 Line 17V (passes recapture to Sarah)
- [x] Form 4562 — current-year (2025) depreciation showing MACRS catch-up (rather than §179)
- [ ] No Schedule D entries (no disposition)
- [ ] No Schedule 1 Line 4 entry (Part II of Form 4797 was not used)

Sarah's 1040 picks up the $40,448 on Schedule 1 Line 8 (with a description noting "§179 recapture from K-1 Line 17V").

---

## Step 8 — Tax impact

Sarah's 2025 ordinary federal bracket: 32%

```
Federal ordinary tax on $40,448 × 32%:           $12,943
SE tax on this amount:                            $0  (not SE income — passes through S-corp)
Net Investment Income Tax (NIIT):                 $0  (NIIT does not apply to active business income)
State tax (varies):                              ~$2,000 (assume 5% state)
Total tax cost of the business-use drop:        ~$14,943
```

The $40K recapture is a tax cost of using the vehicle less for business. It reverses the timing benefit Sarah got from §179 in 2023. The "recapture" gives back the difference between §179 (immediate full expensing) and MACRS (slower).

---

## Step 9 — What if Sarah had sold instead?

If Sarah had SOLD the vehicle in 2025 instead of just dropping business use, the analysis would shift to Part III §1245 recapture, not Part IV §179 recapture. Specifically:

- Asset is fully depreciated (basis = $0 after §179 in 2023)
- Sales price (whatever it is) is 100% gain
- Gain is fully §1245 ordinary recapture (limited by depreciation taken = $80K, which always exceeds gain)
- Reported on Part III → Part II Line 13

The "drop business use" path (Part IV) and the "sell" path (Part III) are mutually exclusive — you don't do both for the same year. If a sale happens, it supersedes the business-use drop logic.

---

## Lessons from this example

1. **Part IV is not for sales.** It is the rare case of recapture-without-disposition, triggered by IRC §179(d)(10) when business use of a §179 asset drops to ≤50% before recovery period ends.

2. **Recapture flows BACK to the original deduction's form.** Not to Part II Line 13. For S-corps, this means K-1 → Schedule 1 Line 8.

3. **Basis is restored by the recapture amount.** The asset can resume MACRS depreciation on the recaptured basis.

4. **Listed property + §280F.** Part IV also covers §280F(b)(2) for listed property whose business use drops. The mechanics are similar; the column labels are different on the form.

5. **This rule is the "gotcha" of generous expensing.** §179 and bonus depreciation are timing benefits, not permanent ones. Aggressive expensing today means recapture risk if business circumstances change.
