# Recipient Routing — Where Each 1099-MISC Box Goes on the Return

For a recipient of Form 1099-MISC, the most important question is: where does each box go on my federal return? "1099-MISC = Schedule C" is a common but wrong assumption. Each box has its own destination.

This file is the routing lookup. Use it after the recipient has the form in hand.

## Master routing table

| Box | Default destination | Alternative destinations |
|-----|---------------------|--------------------------|
| Box 1 (Rents) | **Schedule E** Part I | Schedule C if real estate dealer or equipment rental as trade-or-business |
| Box 2 (Royalties) | **Schedule E** Part I | Schedule C if creating IP as trade-or-business |
| Box 3 (Other income) | **Schedule 1 Line 8z** ("Other income — type") | Schedule C if part of trade-or-business |
| Box 4 (Federal tax withheld) | **Form 1040 Line 25b** | (always Form 1040, irrespective of source) |
| Box 5 (Fishing boat proceeds) | **Schedule C** | (commercial fishing as trade-or-business) |
| Box 6 (Medical / health-care) | **Schedule C** | (the recipient is a healthcare provider; this is their business income) |
| Box 7 (Direct sales ≥$5,000) | **Schedule C** | (direct sales of consumer products is a trade-or-business) |
| Box 8 (Substitute payments) | **Schedule B** Part I (treat as interest/dividend) | Schedule 1 if not interest/dividend in nature |
| Box 9 (Crop insurance) | **Schedule F** (farming) | |
| Box 10 (Attorney gross proceeds) | **Schedule C** (attorney's law practice) | Note: gross proceeds includes amounts disbursed to clients — those are NOT the attorney's income; deduct as fiduciary disbursement |
| Box 12 (§409A deferrals) | **Form 1040 Line 8t** | Plus 20% additional tax under §409A(a)(1)(B) |
| Box 14 (Excess golden parachute) | **Form 1040 Line 1h** | Plus 20% excise tax under §4999 |
| Box 15 (Nonqualified deferred comp inclusions) | **Form 1040 Line 1h** | |
| Boxes 16-18 (State info) | **State return** | |

---

## Box 1 — Rents → Schedule E

### Default: Schedule E Part I

For most recipients of rent (landlords), Box 1 income goes on **Schedule E Part I**:

- Line 3 (Rents received) — combine across all rental properties; itemize each property in columns A, B, C
- Subtract operating expenses (Lines 5-19) — repairs, mortgage interest, depreciation, taxes, etc.
- Net to Line 21 → Schedule 1 Line 5

The activity is treated as **rental real estate** for tax purposes:
- Generally **passive** under §469 (passive activity loss rules)
- Subject to depreciation under MACRS (27.5 years residential, 39 years commercial)
- Material participation rules apply for the special $25,000 active rental real estate exception (§469(i))

### Alternative: Schedule C

In rare cases, rental income goes on Schedule C instead of Schedule E:
- **Real estate dealer** — buying and selling real estate as inventory (e.g., flippers). The income is ordinary, not passive.
- **Hotel / motel / short-term rental with substantial services** — provides daily housekeeping, on-site management, meals; treated as a trade-or-business under Reg. §1.469-1T(e)(3)(ii)(A). Average rental period ≤ 7 days.
- **Equipment rental as a regular business** — renting equipment (cranes, cars, generators) on a regular basis with substantial services (operators, maintenance, delivery).

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

## Box 3 — Other income → Schedule 1 Line 8z (default)

### Default: Schedule 1 Line 8z

Most "other income" — prizes, awards, taxable damages, settlement portions — goes on **Schedule 1 Line 8z** with a description ("Lawsuit settlement", "Game-show prize", "Award from XYZ").

This income is:
- **Taxable** (unless excluded under §104 personal physical injury)
- **Not subject to SE tax** (it's not a trade or business)
- **Not deductible expenses** post-TCJA (the misc 2% itemized deductions are suspended through 2025)

### Alternative: Schedule C

If the prize / award is part of a trade or business:
- Game-show winnings for a professional contestant who appears regularly
- Award paid to a professional speaker for a keynote
- Settlement of a business dispute (lost-profits damages connected to the business)

Then Schedule C; subject to SE tax; offsetting expenses deductible.

### Settlement-specific: §104 exclusion

If the Box 3 amount is plaintiff's portion of a settlement for personal physical injury, IRC §104(a)(2) excludes it from gross income. The recipient:
- Does NOT include on Schedule 1 Line 8 or anywhere
- May attach an explanatory statement noting the §104 exclusion (especially if Box 3 was issued anyway)

For mixed claims (some physical, some non-physical), allocate per the settlement agreement. Only the non-§104 portion is includable.

## Box 4 — Federal income tax withheld → Form 1040 Line 25b

Always Form 1040 Line 25b (federal income tax withheld from forms 1099). No exceptions. This is treated identically to W-2 Line 25a withholding — credited against total federal tax liability.

If the recipient has multiple 1099 forms with Box 4, sum them and report the total on Line 25b.

## Box 5 — Fishing boat proceeds → Schedule C

Schedule C Line 1 (gross receipts). Subject to SE tax. The recipient is a commercial fisher / crew member treating the activity as a trade-or-business.

## Box 6 — Medical / health-care payments → Schedule C

The recipient is a medical / health-care provider; Box 6 income is their business income.

Schedule C Line 1. Subject to SE tax (unless the provider is incorporated, in which case Box 6 is reported on the corporation's return, e.g., Form 1120 / 1120-S).

## Box 7 — Direct sales → Schedule C (or 1099-NEC reporting)

Box 7 is a checkbox indicating direct sales ≥$5,000. The actual income comes from the recipient's own records, not from Box 7 (which is informational).

Recipient reports total direct-sales income on Schedule C.

## Box 8 — Substitute payments → Schedule B

Substitute payments in lieu of dividends or interest report on:
- **Schedule B Part I** if treated as interest
- **Schedule B Part II** if treated as dividends (but rare; usually treated as interest)
- Otherwise Schedule 1 Line 8

The character of the substitute payment depends on the underlying security. The broker / borrower typically classifies on the form.

## Box 9 — Crop insurance proceeds → Schedule F

Schedule F (farm income) Line 6a (Crop insurance proceeds and federal crop disaster payments received). The recipient is a farmer.

Special election under IRC §451(g): farmers may elect to defer crop insurance proceeds for one year if the loss occurred in the year of payment and they would have sold the crop in the following year.

## Box 10 — Attorney gross proceeds → Schedule C

The recipient is an attorney. Box 10 reports the **gross proceeds** that passed through the attorney's trust account. But this is NOT all the attorney's income.

The attorney's actual income is the **fee portion**, not the gross. The gross includes amounts disbursed to clients, which is a fiduciary disbursement, not the attorney's income.

Reconciliation on the attorney's Schedule C:
- Schedule C Line 1: total fee income earned in the year (NOT the Box 10 amount; Box 10 is a gross-proceeds reporting figure that includes client disbursements)
- The fee income is independently reported on 1099-NEC Box 1 if the attorney is non-corporate; for corporate attorneys, no 1099-NEC is issued and the corporation reports total fee receipts on its own return

The attorney's office records distribute as:
- Total trust-account inflows (matches Box 10): $X
- Disbursements to clients: $X − fee
- Fee retained: $X − client disbursement = the attorney's actual income

Box 10 is informational reporting for IRS visibility; the attorney's tax return follows their actual fee income, not Box 10's gross.

## Box 12 — §409A deferrals → Form 1040 Line 8t

§409A(a)(1)(B) failure: deferrals into a noncompliant nonqualified deferred compensation plan are taxable currently. The recipient pays:
- Regular income tax on the deferral
- Plus an additional 20% tax under §409A(a)(1)(B)
- Plus interest at the underpayment rate + 1%

Form 1040 Line 8t (additional tax from Schedule 2 Line 17e or per Form 1040 instructions) and Form 1040 Line 1 wages section.

## Box 14 — Excess golden parachute → Form 1040 Line 1h

Excess parachute payments under §280G are subject to a 20% excise tax under IRC §4999 (paid by the recipient, in addition to regular income tax on the parachute). Routes via Schedule 2 Line 17.

## Box 15 — Nonqualified deferred comp inclusions → Form 1040 Line 1h

Similar to Box 12 but for income inclusions of previously-deferred amounts. Routes to Form 1040 wages line.

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
