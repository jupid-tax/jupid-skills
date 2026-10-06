# Common Schedule E Mistakes

Each entry: the mistake, what the rule says (with source), and what the agent does about it. Sources are the 2025 Instructions for Schedule E unless noted; Pub. 527 and Pub. 925 are the 2025 editions.

## 1. Depreciating the land, or skipping depreciation

**Mistake.** Running the whole purchase price through 27.5 years, or claiming no depreciation at all.

**Rule.** Land is not depreciable; split cost by relative FMV, or by assessed values if FMV is uncertain (Line 18). Basis must be reduced by depreciation you could have deducted even if you did not claim it (Pub. 527, Claiming the Correct Amount of Depreciation).

**Agent action.** Ask for the closing statement and the assessor's land/building split. Compute line 18 from the building only. If prior years were skipped, do not "catch up" on this year's line 18; tell the user that Pub. 527 points to Form 1040-X or an accounting method change and recommend a CPA.

## 2. Deducting an improvement as a repair

**Mistake.** A roof replacement, new HVAC system, or kitchen remodel on line 14.

**Rule.** Repairs keep property in ordinarily efficient operating condition; amounts that better, restore, or adapt the property must generally be capitalized and depreciated (Line 14).

**Agent action.** For each line 14 item over a few hundred dollars, ask what was done and why. Move improvements to Form 4562 (`../../form-4562/SKILL.md`), which also covers the de minimis safe harbor election (Treas. Reg. §1.263(a)-1(f)).

## 3. Treating a security deposit as income when received, or forgetting the part kept

**Rule.** A deposit you plan to return is not income; any part you keep becomes income that year; a deposit to be used as final rent is advance rent, income when received (Pub. 527 ch. 1). Advance rent is income when received regardless of the period covered.

**Agent action.** Ask: "How much in deposits did you collect, return, and keep in 2025? Was any deposit applied as the last month's rent?"

## 4. Ignoring personal-use days

**Mistake.** Reporting 0 personal days for a vacation property the family used, or treating rent from a relative at a discount as fair rent.

**Rule.** Personal use includes family use (unless fair-rent main home), below-fair-rent days, and swap arrangements; expenses must be divided; personal use above the greater of 14 days or 10% of fair-rental days makes the unit a home (Line 2; Pub. 527 ch. 5).

**Agent action.** Load `personal-use-and-vacation-homes.md` and ask the day-count questions there. Never fill line 2 from an estimate.

## 5. Claiming a loss on a unit used as a home

**Rule.** If used as a home and rented 15 days or more, rental expenses beyond rental income are limited by Worksheet 5-1 and carried forward; the unit is not a passive activity (Pub. 527 ch. 5).

**Agent action.** Run Worksheet 5-1 in the draft. Line 21 for that column cannot be negative except for the fully deductible 2a–2d amounts exceeding rent.

## 6. Reporting rent from a home rented fewer than 15 days

**Rule.** Used as a home and rented fewer than 15 days: do not report the rent and deduct no rental expenses (Line 2; Pub. 527).

**Agent action.** Leave the property off Schedule E. Route deductible mortgage interest and taxes to `../../schedule-a/SKILL.md`.

## 7. Short-term rental with services filed on the wrong schedule, or assumed passive

**Rule.** Significant services such as maid service: Schedule C (Line 3). Pub. 527 ch. 3 lists regular cleaning, changing linen, or maid service primarily for the tenant's convenience as substantial services; heat and light, cleaning of public areas, and trash collection are not. Separately, an average customer stay of 7 days or less (or 30 days or less with significant personal services) means the activity is not a rental activity for the passive rules; material participation then decides passive vs nonpassive, and the $25,000 allowance does not apply (Pub. 925; Instructions for Form 8582).

**Agent action.** Compute the average stay from the booking export. Ask what services are provided during stays. If the facts point both ways, present both schedules and send the user to a CPA.

## 8. Assuming the $25,000 allowance applies

**Mistake.** MFS filer living with spouse claims $12,500; filer with MAGI over $150,000 claims a rental loss; limited partner claims the allowance; filer with 5% ownership claims active participation.

**Rule.** MFS living together at any time: $0. Allowance reduced by 50% of MAGI over $100,000 ($50,000 MFS living apart). Active participation requires at least 10% ownership; limited partners generally do not actively participate (Pub. 925; Instructions, Active participation).

**Agent action.** Compute MAGI with the Form 8582 line 6 adjustments and show the phase-out arithmetic in the draft.

## 9. Skipping Form 8582 when it is required

**Rule.** Form 8582 can be skipped only if every condition of the Exception for Certain Rental Real Estate Activities holds, including MAGI $100,000 or less, net loss $25,000 or less, and no prior-year unallowed passive losses (General Instructions).

**Agent action.** Check each condition in the draft, one by one. Any "No" means Form 8582 worksheet.

## 10. Losing suspended passive losses

**Rule.** Unallowed passive losses carry forward and are released when the entire interest is disposed of in a fully taxable transaction to an unrelated person (Pub. 925).

**Agent action.** Ask for last year's Form 8582 (Parts VII–IX). Put the carryforward per property in the draft's "carry to next year" block.

## 11. Netting PYA or UPE amounts into current K-1 numbers

**Rule.** Prior-year basis/at-risk losses now allowed, prior-year passive losses not reported on Form 8582, and unreimbursed partnership expenses each go on their own line with "PYA" or "UPE" in column (a) (Line 27).

**Agent action.** Answer line 27 "Yes" and use separate lines. Never combine with the entity's current ordinary income line.

## 12. S corporation column (e) not checked

**Rule.** Loss, distribution, stock disposition, or loan repayment from an S corporation: check column (e) and attach Form 7203 (form note; Instructions, Basis rules for S corporations).

**Agent action.** Ask about distributions on every S corporation K-1 (box 16, code D). Any distribution means column (e) is checked even if the K-1 shows income.

## 13. Telling the user Schedule E income is never subject to self-employment tax

**Rule.** Rental real estate income generally is not net earnings from self-employment, but a partner's share of partnership business income may be: K-1 (Form 1065) box 14, code A goes to Schedule SE (Instructions, Domestic Partnerships; QJV section). Rentals with substantial services on Schedule C may owe SE tax (Pub. 527 ch. 3).

**Agent action.** Route any box 14 code A amount to `../../schedule-se/SKILL.md`.

## 14. Wrong mileage rate or mileage plus actual costs

**Rule.** 2025: 70 cents a mile (Line 6). Standard mileage excludes lease payments, depreciation and actual auto expenses for that vehicle; you can use it only if you used it the first year the owned vehicle was placed in service (or for the whole lease). Any auto expense requires Form 4562 Part V (Line 6). For 2026 the IRS rate is 72.5 cents (Jan. 1–June 30) and 76 cents (July 1–Dec. 31) (irs.gov/tax-professionals/standard-mileage-rates; IR-2025-128, IR-2026-29).

**Agent action.** Ask for the mileage log and which method was used in the vehicle's first rental year.

## 15. Mortgage interest from a loan not used for the rental

**Rule.** Interest follows the use of loan proceeds (tracing); a home equity loan spent on personal items is not rental interest (Lines 12 and 13).

**Agent action.** Ask what each loan funded. Put only traced rental interest on lines 12–13.
