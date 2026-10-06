# Recipient Routing — Where Each 1099-MISC Box Goes on the Return

For a recipient of Form 1099-MISC, the most important question is: where does each box go on my federal return? "1099-MISC = Schedule C" is a common but wrong assumption. Each box has its own destination.

This file is the routing lookup. Use it after the recipient has the form in hand. Routing follows the "Instructions for Recipient" on Copy B of Form 1099-MISC (Rev. April 2025 for 2025 payments; Rev. December 2026 for 2026 payments) and the 2025 Form 1040 / Schedule 1 / Schedule 2 line numbers.

## Master routing table

| Box | Default destination | Alternative destinations |
|-----|---------------------|--------------------------|
| Box 1 (Rents) | **Schedule E** Part I | Schedule C if significant services to the tenant, real estate sold as a business, or personal property rented as a business (Copy B) |
| Box 2 (Royalties) | **Schedule E** Part I | Schedule C if creating IP as trade-or-business |
| Box 3 (Other income) | **Schedule 1 Line 8i** (prizes and awards) or **Line 8z** ("Other income — type") | Schedule C or F if trade or business income (Copy B) |
| Box 4 (Federal tax withheld) | **Form 1040 Line 25b** | (always Form 1040, irrespective of source) |
| Box 5 (Fishing boat proceeds) | **Schedule C** | (commercial fishing as trade-or-business) |
| Box 6 (Medical / health-care) | **Schedule C** | (the recipient is a healthcare provider; this is their business income) |
| Box 7 (Direct sales ≥$5,000) | **Schedule C** | (direct sales of consumer products is a trade-or-business) |
| Box 8 (Substitute payments) | **Schedule 1** "Other income" line (8z) | Copy B, Box 8 |
| Box 9 (Crop insurance) | **Schedule F** (farming) | |
| Box 10 (Attorney gross proceeds) | **Schedule C** (attorney's law practice), taxable part only | Copy B: "Report only the taxable part as income." Amounts passed to clients are not the attorney's income |
| Box 11 (Fish purchased for resale) | **Schedule C** (commercial fishing) | |
| Box 12 (§409A deferrals) | Informational | Any currently taxable amount is also in Box 15 |
| Box 13a / 13b, 14 (2026 forms only) | Already included in Box 3 | Cash tips / TTOC / overtime for Schedule 1-A deductions; outside this skill |
| Box 14 (2025 form) | Reserved | Excess golden parachute payments are on 1099-NEC box 3 since the April 2025 revision |
| Box 15 (Nonqualified deferred comp, §409A failure) | Income on the return (Copy B) | Plus 20% additional tax and interest on **Schedule 2 line 17h** |
| Boxes 16-18 (State info) | **State return** | |

---

## Box 1 — Rents → Schedule E

### Default: Schedule E Part I

For most recipients of rent (landlords), Box 1 income goes on **Schedule E Part I** (Copy B, Box 1):

- Line 3 (Rents received) — combine across all rental properties; itemize each property in columns A, B, C
- Subtract operating expenses (Lines 5-19) — repairs, mortgage interest, depreciation, taxes, etc.
- Net to Line 21 → Schedule 1 Line 5

The activity is treated as **rental real estate** for tax purposes:
- Generally **passive** under §469 (passive activity loss rules)
- Subject to depreciation under MACRS (27.5 years residential, 39 years commercial)
- The special $25,000 allowance for rental real estate requires **active** participation, not material participation (§469(i))

### Alternative: Schedule C

Copy B names three cases where rents go on Schedule C instead of Schedule E:
- **Significant services to the tenant** — e.g., hotel-like services such as maid service (2025 Schedule E instructions, line 3; Pub. 527)
- **Real estate sold as a business** — real estate dealer (e.g., flippers)
- **Personal property rented as a business** — equipment rental (cranes, cars, generators) as a regular business

Separately, an average rental period of 7 days or less means the activity is not a "rental activity" for the passive-loss rules (Temp. Reg. §1.469-1T(e)(3)(ii)(A)); that changes loss limits, not by itself the schedule.

If unsure, default to Schedule E. Schedule C requires meeting the trade-or-business standard (regular, continuous, profit-motive).

## Box 2 — Royalties → Schedule E

### Default: Schedule E Part I

Royalty income on Schedule E Line 4 (Royalties received). Net of expenses related to the royalty stream (Lines 5-19, applied on a "royalty as one column" basis).

Common: oil/gas royalties, mineral leases, copyright royalties for non-creator recipients.

### Alternative: Schedule C

If the recipient is in the **business of creating** the royalty-generating asset (e.g., a working author, a working musician, a working inventor):
- Royalties are gross receipts of their writing / music / invention business
- Reports on Schedule C
- Subject to SE tax

The IRS factor: did the recipient create the work as part of an active business, or did they passively receive royalties on something they didn't create (or created decades ago)?

## Box 3 — Other income → Schedule 1 (default)

### Default: Schedule 1 Line 8i or 8z

Copy B: "Generally, report this amount on the 'Other income' line of Schedule 1 (Form 1040) and identify the payment." On the 2025 Schedule 1, prizes and awards have their own line, **8i**; taxable damages, settlement amounts, and other items go on **Line 8z** with a description ("Lawsuit settlement", "Award from XYZ").

This income is:
- **Taxable** (unless excluded under §104 personal physical injury)
- **Not subject to SE tax** (it's not a trade or business)
- **Expenses not deductible** as miscellaneous itemized deductions (IRC §67(g), made permanent by P.L. 119-21 §70110). Exception: attorney fees in unlawful-discrimination and certain whistleblower actions are an above-the-line deduction (IRC §62(a)(20)–(21); Schedule 1 line 24h for discrimination claims)

### Alternative: Schedule C

If the prize / award is part of a trade or business:
- Game-show winnings for a professional contestant who appears regularly
- Award paid to a professional speaker for a keynote
- Settlement of a business dispute (lost-profits damages connected to the business)

Then Schedule C; subject to SE tax; offsetting expenses deductible.

### Settlement-specific: §104 exclusion

Box 3 normally shows the **full** taxable damages, including any part the payer sent to the plaintiff's attorney (Reg. §1.6045-5(f), Example 3). The plaintiff reports the full amount; the attorney fee is deductible only in the cases above (or on Schedule C if the claim was business income).

If a Box 3 amount was issued for damages the recipient believes are excluded under IRC §104(a)(2) (personal physical injury, non-punitive), the payer should not have reported it (Instructions, Box 3 item 6a). Ask the payer for a corrected form; if it can't be corrected, Copy B says to attach an explanation to the return and report correctly.

For mixed claims (some physical, some non-physical), allocate per the settlement agreement. Only the non-§104 portion is includable.

## Box 4 — Federal income tax withheld → Form 1040 Line 25b

Always Form 1040 Line 25b (federal income tax withheld from forms 1099). No exceptions. This is treated identically to W-2 Line 25a withholding — credited against total federal tax liability.

If the recipient has multiple 1099 forms with Box 4, sum them and report the total on Line 25b.

## Box 5 — Fishing boat proceeds → Schedule C

Schedule C Line 1 (gross receipts). Subject to SE tax. The recipient is a commercial fisher / crew member treating the activity as a trade-or-business.

## Box 6 — Medical / health-care payments → Schedule C

The recipient is a medical / health-care provider; Box 6 income is their business income.

Copy B: "For individuals, report on Schedule C (Form 1040)." Schedule C Line 1. Subject to SE tax (unless the provider is incorporated, in which case Box 6 is reported on the corporation's return, e.g., Form 1120 / 1120-S).

## Box 7 — Direct sales → Schedule C (or 1099-NEC reporting)

Box 7 is a checkbox indicating direct sales ≥$5,000. The actual income comes from the recipient's own records, not from Box 7 (which is informational).

Recipient reports total direct-sales income on Schedule C.

## Box 8 — Substitute payments → Schedule 1

Copy B, Box 8: substitute payments in lieu of dividends or tax-exempt interest received by your broker because your securities were on loan. "Report on the 'Other income' line of Schedule 1 (Form 1040)" — Line 8z on the 2025 form. They are not qualified dividends and not tax-exempt interest.

## Box 9 — Crop insurance proceeds → Schedule F

Schedule F (farm income) Line 6a (Crop insurance proceeds and federal crop disaster payments received). The recipient is a farmer.

Special election under IRC §451(g): farmers may elect to defer crop insurance proceeds for one year if the loss occurred in the year of payment and they would have sold the crop in the following year.

## Box 10 — Attorney gross proceeds → Schedule C

The recipient is an attorney. Box 10 reports the **gross proceeds** that passed through the attorney's trust account. But this is NOT all the attorney's income.

The attorney's actual income is the **fee portion**, not the gross. Copy B: "Report only the taxable part as income on your return." The gross includes amounts disbursed to clients, which is a fiduciary disbursement, not the attorney's income.

Reconciliation on the attorney's Schedule C:
- Schedule C Line 1: total fee income earned in the year (NOT the Box 10 amount; Box 10 is a gross-proceeds reporting figure that includes client disbursements)
- Fees paid out of settlement proceeds are usually not on any separate 1099-NEC (the payer does not report the claimant's attorney's fees); fees paid by the attorney's own clients for services to them may arrive on 1099-NEC box 1a, including for corporate firms

The attorney's office records distribute as:
- Total trust-account inflows (matches Box 10): $X
- Disbursements to clients: $X − fee
- Fee retained: $X − client disbursement = the attorney's actual income

Box 10 is informational reporting for IRS visibility; the attorney's tax return follows their actual fee income, not Box 10's gross.

## Box 12 — §409A deferrals → informational

Copy B: Box 12 "may show current year deferrals as a nonemployee under a nonqualified deferred compensation (NQDC) plan that is subject to the requirements of section 409A plus any earnings." Deferrals are not income by themselves. Any amount that is currently taxable because the plan fails §409A is also in Box 15.

## Box 14

- 2025 form (Rev. April 2025): "Reserved for future use." Excess golden parachute payments now come on 1099-NEC box 3.
- 2026 form (Rev. December 2026): overtime compensation already included in Box 3 (for the Schedule 1-A overtime deduction; outside this skill).

## Box 15 — Nonqualified deferred comp inclusions → income + Schedule 2 line 17h

Copy B: "Report this amount as income on your tax return. This income is also subject to a substantial additional tax." The additional tax is 20% of the amount plus interest under §409A(a)(1)(B)(ii), reported on **Schedule 2 line 17h** (2025 Form 1040 instructions, Schedule 2 line 17h, which names Form 1099-MISC box 15). Ask a CPA which income line fits the recipient (Schedule C if the deferred pay was for the recipient's business services).

## State boxes 16-18

- Box 16 (state tax withheld) → state return Line for state withholding (Form CA 540 / NY IT-201 / etc.)
- Box 17 (state / payer state ID) → informational; goes on state return for reconciliation
- Box 18 (state income) → state return line for state-source income

For non-resident filers, the state income may be apportioned to the state where services were performed.

## When in doubt: ask the user

If the recipient's classification is ambiguous (trade-or-business vs. one-off, real estate dealer vs. landlord, professional creator vs. passive royalty recipient), ask before routing. The wrong destination can:
- Subject income to SE tax that shouldn't be (or miss SE tax that should be)
- Trigger passive activity rules that shouldn't apply (or miss them)
- Cause a §104 exclusion to be missed

Routing is irreversible without an amended return. Better to ask once than to amend later.
