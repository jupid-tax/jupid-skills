# Example: Marcus, Sole-Prop Landscaper Sells a Truck

End-to-end Form 4797 for a §1245 personal property disposition with full ordinary recapture.

---

## Facts

- **Filer:** Marcus, sole-prop landscaping business (Schedule C)
- **Asset:** 2021 Ford F-250 truck
- **Date acquired:** 01/05/2021
- **Date sold:** 08/14/2025
- **Original cost:** $35,000
- **Business use:** 100% from acquisition through sale
- **Accumulated depreciation:** $28,000 (combination of §179 in year 1, bonus depreciation, and MACRS through year of sale)
- **Sales price:** $22,000 (sold to a used-car dealer)
- **Selling expenses:** $0
- **Prior 5 years of §1231 history:** No prior §1231 gains or losses (verified by reviewing 2020-2024 returns)

---

## Step 1 — Classification

The Ford F-250 is **§1245 property** (depreciable personal property used in business). Held more than 1 year (4 years 7 months) → eligible for §1231 treatment. Goes through Part III first; residual lands in Part I via Line 6.

---

## Step 2 — Compute Part III

### Part III, Column A: 2021 Ford F-250

| Line | Field | Value |
|------|-------|-------|
| 19 | Description | 2021 Ford F-250 (business vehicle) |
| 20 | Gross sales price | $22,000 |
| 21 | Cost or other basis | $35,000 |
| 22 | Depreciation allowed or allowable | $28,000 |
| 23 | Adjusted basis (21 − 22) | $7,000 |
| 24 | Total gain (20 − 23) | **$15,000** |

### §1245 recapture computation (Lines 25a/b)

| Line | Field | Value |
|------|-------|-------|
| 25a | Depreciation allowed for §1245 | $28,000 |
| 25b | Recapture = lesser of Line 24 or 25a | **$15,000** |

The entire $15,000 gain is §1245 recapture (ordinary). Depreciation taken ($28,000) exceeds the realized gain ($15,000), so 100% of the gain is ordinary. No residual §1231 gain.

### Part III rollup

| Line | Field | Value |
|------|-------|-------|
| 30 | Column A total recapture | $15,000 |
| 31 | Sum across columns | $15,000 |
| 32 | To Part II Line 13 | **$15,000** |

Residual §1231 gain (Line 24 − Line 32) = $15,000 − $15,000 = **$0** → no entry on Part I Line 6.

---

## Step 3 — Part I (no entry)

Because the residual §1231 gain is $0, nothing flows to Part I Line 6 from this disposition. Marcus has no other §1231 transactions this year, so:

| Line | Value |
|------|-------|
| 2 | (no entries) |
| 6 | $0 |
| 7 | $0 |
| 8 | $0 (no prior §1231 losses) |
| 9 | $0 |

No Schedule D Line 11 entry from this Form 4797.

---

## Step 4 — Part II rollup

| Line | Field | Value |
|------|-------|-------|
| 10 | Ordinary (≤1 year) | $0 |
| 11 | Net §1231 loss from Part I | $0 |
| 12 | §1231 gain recharacterized by lookback | $0 |
| 13 | Recapture from Part III Line 32 | **$15,000** |
| 14 | Other ordinary | $0 |
| 18 | Total ordinary (Lines 10-17) | **$15,000** |

The $15,000 flows to **Schedule 1 Line 4** ("Other gains or losses — from Form 4797") → **Form 1040 Line 8**.

---

## Step 5 — Tax impact

Marcus's other 2025 income:
- Schedule C net profit: $65,000
- W-2 spouse income: $40,000
- Total household income before §4797 gain: $105,000
- Filing status: MFJ
- Marginal federal bracket: 22%

**Tax on the §1245 recapture:**

```
Federal ordinary tax on $15,000 × 22% = $3,300
SE tax on $15,000:                       $0  (Form 4797 gains NOT SE income per Reg §1.1402(a)-6)
State tax (varies):                      ~$1,100 (assuming 7% state)
Total:                                  ~$4,400
```

**What if the filer had reported it on Form 8949 instead?**

Wrong, but illustrative: $15,000 LTCG at 15% bracket = $2,250 vs. $3,300 ordinary. The IRS would catch the misclassification (cross-reference of Form 4562 prior depreciation) and assess the additional $1,050 plus interest.

---

## Step 6 — Schedule C interactions

Marcus's Schedule C for 2025 already correctly stops depreciating the truck on the date of sale. No "phantom" depreciation in 2025 for the truck after 08/14/2025. The pro-rated 2025 depreciation through sale date is included in the $28,000 accumulated total on Form 4797 Line 22.

There is **no** entry on Schedule C Line 6 (Other income) from this disposition — that line is only used for §179 / §280F recapture (Part IV), not for sale-of-asset recapture (Part II).

---

## Step 7 — Required attachments and downstream forms

- [x] Form 4562 prior-year history (referenced, not attached)
- [ ] Form 6252 — N/A (not an installment sale)
- [ ] Form 4684 — N/A (not casualty/theft)
- [ ] Form 8824 — N/A (not a like-kind exchange)
- [x] Schedule 1 Line 4: $15,000
- [x] Form 1040 Line 8: includes $15,000

---

## Lessons from this example

1. **§1245 recapture often consumes the entire gain.** When depreciation taken (especially with §179 + bonus) exceeds the realized gain, 100% is ordinary recapture — no §1231 LTCG benefit at all.

2. **Form 4797 gains are not SE income.** Marcus saves 15.3% × $15,000 = $2,295 vs. if this were a Schedule C ordinary income item.

3. **No need for Part I detail when Part III consumes the full gain.** Marcus's Form 4797 Part I has zero entries; everything flows through Part III → Part II.

4. **Truck sales are the most common §1245 disposition for solo filers.** Anyone who took §179 or bonus on a vehicle should expect substantial recapture at sale.
