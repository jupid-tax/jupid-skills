# Form 4797 — Line by Line Reference

Complete reference for every line on Form 4797. Load this file when the user is filling out a specific line and needs detailed guidance. Verified against the 2025 Form 4797 and the 2025 Instructions for Form 4797; re-check each new revision at https://www.irs.gov/forms-pubs/about-form-4797.

---

## Header

- **Name(s) shown on return** — Match Form 1040 (or entity return) header exactly. For joint filers, both spouses' names.
- **Identifying number** — SSN for individuals, EIN for entities.

---

## Part I — Sales or Exchanges of Property Used in a Trade or Business and Involuntary Conversions From Other Than Casualty or Theft (Most Property Held More Than 1 Year)

### Lines 1a, 1b, 1c — Gross proceeds and partial dispositions

- **1a**: total gross proceeds from sales or exchanges reported on Forms 1099-B or 1099-S (or substitute statements) for the year that you are including on Line 2, 10, or 20
- **1b**: total gain included on Lines 2, 10, and 24 from partial dispositions of MACRS assets
- **1c**: total loss included on Lines 2 and 10 from partial dispositions of MACRS assets

Line 1a is used for IRS matching against 1099-S/1099-B filings from closing agents and brokers.

### Line 2 — Per-property §1231 gains and losses

For each §1231 asset not reported in Part III: non-depreciable property (land, certain livestock) and depreciable property held more than 1 year that was sold at a loss (2025 Form 4797 instructions, "Where To Make First Entry" table):

| Column | What to enter |
|--------|---------------|
| (a) Description | Plain description (e.g., "20 head breeding cattle", "Land at 456 Oak Ave") |
| (b) Date acquired | MM/DD/YYYY |
| (c) Date sold | MM/DD/YYYY |
| (d) Gross sales price | Gross price (money plus FMV of property received plus debt assumed); do not subtract selling expenses here |
| (e) Depreciation allowed or allowable | Cumulative depreciation through date of sale ("allowed or allowable" rule per IRC §1016(a)(2)) |
| (f) Cost or other basis, plus improvements and expense of sale | Original basis plus capitalized improvements plus selling expenses |
| (g) Gain or loss | (d) + (e) − (f) |

**Depreciable §1245 / §1250 property sold at a gain does NOT go directly on Line 2.** It goes through Part III first; the residual gain (after recapture) comes back to Part I via Line 6. Depreciable property held more than 1 year and sold at a loss goes directly on Line 2.

### Line 3 — Gain from Form 4684, Line 39

Casualty/theft of business property held more than 1 year, after working through Form 4684. The §1231 gain from Form 4684, Line 39 lands here.

### Line 4 — Installment sale §1231 gain

§1231 gain from installment sales, from Form 6252, Line 26 or 37 (current-year recognized gain, including payments on prior-year sales).

### Line 5 — §1231 gain or loss from like-kind exchanges (Form 8824)

If the user did a like-kind exchange of §1231 real property and received boot (cash, debt relief, non-like-kind property), the recognized gain is computed on Form 8824 and the §1231 portion comes here.

### Line 6 — §1231 gain from Part III (Line 32 residual)

Residual gain from depreciable §1231 assets in Part III: Line 32 = Line 30 (total gains) − Line 31 (total recapture), portion other than casualty or theft. This is typically the largest entry on Part I for filers with depreciable real estate or equipment.

### Line 7 — Net §1231 result

Combine Lines 2 through 6. This is your net §1231 result for the year.

- If Line 7 is **net gain (positive)**: continue to Line 8 lookback
- If Line 7 is **net loss (negative)**: enter the loss on Part II Line 11 (treated as ordinary loss); skip Lines 8 and 9
- Partnerships and S corporations: report Line 7 on Schedule K (Form 1065 Line 10; Form 1120-S Line 9) and skip Lines 8, 9, 11, and 12

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

Ordinary gains and losses not included on Lines 11 through 16. For each disposition of business property held 1 year or less, enter:
- Description, dates, sales price, depreciation, basis, gain/loss

Short-held property does not qualify for §1231 treatment. The gain or loss is fully ordinary. Losses on §1244 small business stock also go on Line 10 (2025 Form 4797 instructions, Line 10).

### Line 11 — Net §1231 loss from Part I

If Part I Line 7 is a net loss, enter the loss amount here as ordinary.

### Line 12 — §1231 gain recharacterized as ordinary by lookback

If Part I Line 7 is a gain and Line 8 has prior unrecaptured losses, the lesser of (Line 7) or (Line 8) is recharacterized — enter that amount here.

### Line 13 — Gain from Part III Line 31

§1245 / §1250 / §1252 / §1254 / §1255 recapture amounts (Line 31) flow here as ordinary.

### Lines 14-17 — Other ordinary gains and losses

| Line | What goes here |
|------|----------------|
| 14 | Net gain or loss from Form 4684, Lines 31 and 38a |
| 15 | Ordinary gain from installment sales, Form 6252, Line 25 or 36 |
| 16 | Ordinary gain or loss from like-kind exchanges, Form 8824 |
| 17 | Combine Lines 10 through 16 |

### Line 18 — Total ordinary (18a / 18b)

All returns except individual returns: enter Line 17 on the appropriate line of the return and skip 18a/18b. Individuals:
- **18a**: the part of a Line 11 loss that comes from Form 4684, Line 35, column (b)(ii) (income-producing property) → Schedule A, Line 16
- **18b**: Line 17 redetermined without the 18a loss → **Schedule 1 Line 4** → Form 1040 Line 8

---

## Part III — Gain From Disposition of Property Under Sections 1245, 1250, 1252, 1254, and 1255

Up to 4 properties per page in columns A, B, C, D. Use multiple pages if needed.

### Line 19 — Description

Description of the property. Match to Form 4562 prior-year listings if possible.

### Line 20 — Gross sales price

Money received plus the FMV of other property received plus any mortgage or debt the buyer assumes or takes the property subject to (2025 Form 4797 instructions, Line 20). Do not subtract selling expenses here.

### Line 21 — Cost or other basis plus expense of sale

Original cost basis plus capitalized improvements plus selling expenses (commissions, closing costs). For inherited property, stepped-up FMV at decedent's date of death (IRC §1014).

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
| 26a | Additional depreciation after 1975: actual depreciation (including any special depreciation allowance) in excess of straight-line. For post-1986 property under MACRS straight-line with no bonus, this is $0. |
| 26b | Applicable percentage (generally 100%) × the smaller of Line 24 or Line 26a |
| 26c | Line 24 − Line 26a. If residential rental property, or Line 24 isn't more than Line 26a, skip 26d and 26e |
| 26d | Additional depreciation after 1969 and before 1976 |
| 26e | The smaller of Line 26c or 26d |
| 26f | Section 291 amount (corporations only — 20% of the excess of what would be §1245 recapture over §1250 recapture) |
| 26g | Add Lines 26b, 26e, and 26f (the form says enter -0- here if straight-line was used, except a corporation subject to §291) |

For most post-1986 residential or commercial real estate under MACRS straight-line, **Line 26g is $0**. Exception: if bonus depreciation was claimed on §1250 property (for example, qualified improvement property, 100% bonus if acquired after January 19, 2025), the bonus in excess of straight-line is additional depreciation on Line 26a and is recaptured as ordinary. The depreciation portion is tracked separately as **unrecaptured §1250 gain** on Schedule D Line 19 (computed via Schedule D's Unrecaptured §1250 Gain Worksheet, capped at 25%).

### Line 27 — §1252 Recapture (Farmland)

If farmland was held less than 10 years and the user took deductions for soil/water/land-clearing expenses under §175 or §182, recapture applies. Most filers have $0 here.

### Line 28 — §1254 Recapture (Oil, Gas, Geothermal, Mineral)

If the user took intangible drilling costs (IDC), depletion, or other §263(c)/§616/§617 deductions, recapture applies on disposition. Most non-energy filers have $0.

### Line 29 — §1255 Recapture (Cost-Share Payments)

If the user excluded cost-share payments from income under §126 (USDA conservation programs), recapture applies. Mostly farmers.

### Line 30 — Total gains for all properties

Add property columns A through D, Line 24 (and across multiple Part III pages if applicable).

### Line 31 — Total recapture → Part II Line 13

Add property columns A through D, Lines 25b, 26g, 27c, 28b, and 29b. Enter here and on Part II Line 13. For installment sales, see the Form 6252 instructions before completing Part III (recapture is recognized in full in the year of sale even if the rest of the gain is spread across years).

### Line 32 — Residual §1231 gain → Part I Line 6

Line 30 − Line 31. Enter the portion from casualty or theft on Form 4684, Line 33, and the portion from other than casualty or theft on Form 4797, Line 6.

---

## Part IV — Recapture Amounts Under Sections 179 and 280F(b)(2) When Business Use Drops to 50% or Less

This part is NOT for sales — it's for situations where the property is still owned but business use has dropped.

### Line 33 — Section 179 expense deduction or depreciation allowable in prior years

Column (a), §179 property other than listed property: the §179 deduction claimed when the property was placed in service. Column (b), listed property (§280F(b)(2)): depreciation allowable in prior tax years plus any §179 deduction claimed when placed in service.

### Line 34 — Recomputed depreciation

Column (a): depreciation that would have been allowable on the §179 amount from the year placed in service through (and including) the current year, at each year's business-use percentage (Pub. 946, chapter 2). Column (b): depreciation that would have been allowable had the property not been used more than 50% in a qualified business (straight-line ADS), from the year placed in service up to (but not including) the current year (2025 Form 4797 instructions, Line 34; Pub. 463; Pub. 946).

### Line 35 — Recapture amount

Line 33 − Line 34. This is ordinary income.

**Where Line 35 goes (NOT Part II of Form 4797):**

- For sole proprietors: Schedule C Line 6 ("Other income")
- For partners and S-corp shareholders whose §179 was passed through: the entity reports the recapture information on Schedule K-1 (Form 1120-S Box 17, code L); the owner completes Part IV and reports the recapture on Schedule E, Part II, where the deduction was taken
- For C-corps: Form 1120 Line 10
- For employees with §280F listed property: Form 1040 Schedule 1 Line 8z

The recaptured amount adds back to the basis of the property — you can re-depreciate it under MACRS going forward (over the remaining recovery period).
