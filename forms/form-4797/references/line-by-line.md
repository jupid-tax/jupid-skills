# Form 4797 — Line by Line Reference

Complete reference for every line on Form 4797. Load this file when the user is filling out a specific line and needs detailed guidance.

---

## Header

- **Name(s) shown on return** — Match Form 1040 (or entity return) header exactly. For joint filers, both spouses' names.
- **Identifying number** — SSN for individuals, EIN for entities.

---

## Part I — Sales or Exchanges of Property Used in a Trade or Business and Involuntary Conversions From Other Than Casualty or Theft (Most Property Held More Than 1 Year)

### Line 1 — Year and 1099-S info

Enter:
- Total gross proceeds reported on Forms 1099-S during the tax year (real estate transactions reported to IRS by closing agents)
- The year the property was sold

This is informational, used for IRS matching against 1099-S transmittals from title companies.

### Line 2 — Per-property §1231 gains and losses

For each non-depreciable §1231 asset (or depreciable asset whose recapture computation in Part III produces zero recapture):

| Column | What to enter |
|--------|---------------|
| (a) Description | Plain description (e.g., "20 head breeding cattle", "Land at 456 Oak Ave") |
| (b) Date acquired | MM/DD/YYYY |
| (c) Date sold | MM/DD/YYYY |
| (d) Gross sales price | Sale price net of selling expenses |
| (e) Depreciation allowed or allowable | Cumulative depreciation through date of sale ("allowed or allowable" rule per IRC §1016(a)(2)) |
| (f) Cost or other basis | Original basis plus capitalized improvements |
| (g) Gain or loss | (d) + (e) − (f) |

**Depreciable §1245 / §1250 property does NOT go directly on Line 2.** It goes through Part III first; the residual gain (after recapture) comes back to Part I via Line 6.

### Line 3 — Installment sale §1231 gain

If you have a §1231 installment sale from a prior year (Form 6252), the current-year recognized gain comes here.

### Line 4 — Form 4684 §1231 gain

Casualty/theft of business property held more than 1 year, after working through Form 4684. The §1231 portion lands here.

### Line 5 — §1231 gain from §1031 with boot

If the user did a like-kind exchange of §1231 real property and received boot (cash, debt relief, non-like-kind property), the recognized gain is computed on Form 8824 and the §1231 portion comes here.

### Line 6 — §1231 gain from Part III (Line 32 residual)

Residual gain from depreciable §1231 assets in Part III, after subtracting the recapture amount (Line 32). This is typically the largest entry on Part I for filers with depreciable real estate or equipment.

### Line 7 — Net §1231 result

Combine Lines 2 through 6. This is your net §1231 result for the year.

- If Line 7 is **net gain (positive)**: continue to Line 8 lookback
- If Line 7 is **net loss (negative)**: enter the loss on Part II Line 11 (treated as ordinary loss); skip Lines 8 and 9

### Line 8 — 5-year non-recaptured §1231 loss

Look back at the prior 5 tax years. Sum any net §1231 losses (Part I Line 7 negative amount in those years). Subtract any portion already recharacterized as ordinary in intervening years.

The remainder is your "non-recaptured net §1231 loss" — enter it on Line 8.

If current Line 7 is a §1231 gain, this lookback amount converts gain to ordinary. The ordinary portion goes to Part II Line 12.

### Line 9 — Long-term capital gain to Schedule D Line 11

If Line 7 > Line 8, the excess is long-term capital gain — enter it here. This amount flows to **Schedule D Line 11** for individuals (or the equivalent line on entity returns).

If Line 7 ≤ Line 8, all of the Line 7 gain is recharacterized as ordinary on Line 12; Line 9 = $0.

---

## Part II — Ordinary Gains and Losses

### Line 10 — Property held 1 year or less

For each disposition of business property held 1 year or less, enter:
- Description, dates, sales price, depreciation, basis, gain/loss

Short-held property does not qualify for §1231 treatment. The gain or loss is fully ordinary.

### Line 11 — Net §1231 loss from Part I

If Part I Line 7 is a net loss, enter the loss amount here as ordinary.

### Line 12 — §1231 gain recharacterized as ordinary by lookback

If Part I Line 7 is a gain and Line 8 has prior unrecaptured losses, the lesser of (Line 7) or (Line 8) is recharacterized — enter that amount here.

### Line 13 — Recapture from Part III Line 32

§1245 / §1250 / §1252 / §1254 / §1255 recapture amounts flow here as ordinary.

### Lines 14-17 — Other ordinary gains and losses

| Line | What goes here |
|------|----------------|
| 14 | Ordinary gain/loss from Form 4684 (casualty/theft, ordinary portion) |
| 15 | Ordinary loss from §1244 small business stock |
| 16 | Ordinary gain from §1244 stock recapture (rare) |
| 17 | Combined |

### Line 18 — Total ordinary

Combine Lines 10 through 17. This total flows to:
- **Schedule 1 Line 4** for individuals → Form 1040 Line 8
- Equivalent line on entity returns

---

## Part III — Gain From Disposition of Property Under Sections 1245, 1250, 1252, 1254, and 1255

Up to 4 properties per page in columns A, B, C, D. Use multiple pages if needed.

### Line 19 — Description

Description of the property. Match to Form 4562 prior-year listings if possible.

### Line 20 — Gross sales price

Sale proceeds net of selling expenses (commissions, closing costs).

### Line 21 — Cost or other basis

Original cost basis plus capitalized improvements. For inherited property, stepped-up FMV at decedent's date of death (IRC §1014).

### Line 22 — Depreciation allowed or allowable

Cumulative depreciation, §179, and bonus depreciation through date of sale. **"Allowed or allowable"** — if the user should have depreciated but didn't, the IRS treats it as if they did. Recommend Form 3115 catch-up before filing if there's a gap.

### Line 23 — Adjusted basis

Line 21 − Line 22.

### Line 24 — Total gain

Line 20 − Line 23.

### Line 25 — §1245 Recapture (Personal Property)

For §1245 property only (equipment, vehicles, machinery, furniture, amortizable intangibles).

| Sub-line | What to enter |
|----------|---------------|
| 25a | Depreciation allowed or allowable for §1245 property = Line 22 for §1245 assets |
| 25b | Lesser of Line 24 or Line 25a |

Line 25b is the §1245 recapture amount — fully ordinary.

### Line 26 — §1250 Recapture (Real Property)

For §1250 property only (buildings, structural components, real property improvements).

| Sub-line | What to enter |
|----------|---------------|
| 26a | Additional depreciation after 1975 (depreciation in excess of straight-line). For post-1986 property under MACRS straight-line, this is generally $0. |
| 26b | Applicable percentage × Line 26a (post-1969 properties) |
| 26c | Subtract Line 26b from Line 26a |
| 26d | Additional depreciation after 1969 and before 1976 |
| 26e | Applicable percentage × the smaller of Line 24 or 26d |
| 26f | Section 291 amount (corporations only — extra 20% recapture for §1250 property) |
| 26g | §1250 recapture (sum of recapture-portion lines) |
| 26h | Combine recapture amounts |

For most post-1986 residential or commercial real estate under MACRS straight-line, **Line 26g is $0**. The depreciation portion is tracked separately as **unrecaptured §1250 gain** on Schedule D Line 19 (computed via Schedule D's Unrecaptured §1250 Gain Worksheet, capped at 25%).

### Line 27 — §1252 Recapture (Farmland)

If farmland was held less than 10 years and the user took deductions for soil/water/land-clearing expenses under §175 or §182, recapture applies. Most filers have $0 here.

### Line 28 — §1254 Recapture (Oil, Gas, Geothermal, Mineral)

If the user took intangible drilling costs (IDC), depletion, or other §263(c)/§616/§617 deductions, recapture applies on disposition. Most non-energy filers have $0.

### Line 29 — §1255 Recapture (Cost-Share Payments)

If the user excluded cost-share payments from income under §126 (USDA conservation programs), recapture applies. Mostly farmers.

### Line 30 — Total recapture per column

Sum of Lines 25b, 26g, 27, 28, 29 for each column.

### Line 31 — Total recapture across columns

Sum of Line 30 across all columns (and across multiple Part III pages if applicable).

### Line 32 — Recapture sent to Part II Line 13

Generally Line 31. Reduce by any portion attributable to other forms (e.g., Form 6252 for installment sales — recapture is recognized in full in year 1 even if gain is spread across years).

---

## Part IV — Recapture Amounts Under Sections 179 and 280F(b)(2) When Business Use Drops to 50% or Less

This part is NOT for sales — it's for situations where the property is still owned but business use has dropped.

### Line 33 — Section 179 deduction or §280F deduction taken

Cumulative §179 + §280F amounts taken on the property in prior years.

### Line 34 — Recomputed depreciation

What depreciation would have been under MACRS (or straight-line for §280F listed property) through the year of the business-use drop. Use [Pub 946](https://www.irs.gov/publications/p946) for MACRS schedules.

### Line 35 — Recapture amount

Line 33 − Line 34. This is ordinary income.

**Where Line 35 goes (NOT Part II of Form 4797):**

- For sole proprietors: Schedule C Line 6 ("Other income")
- For partnerships: distribute to partners on Schedule K-1
- For S-corps: distribute on Schedule K-1
- For C-corps: Form 1120 Line 10
- For employees with §280F listed property: Form 1040 Schedule 1 Line 8z

The recaptured amount adds back to the basis of the property — you can re-depreciate it under MACRS going forward (over the remaining recovery period).
