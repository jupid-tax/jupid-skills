# Fuel Taxes on Form 720

Federal fuel excise tax is the largest single category on Form 720 by dollar volume. The structure is complex: rates differ by fuel type, by the taxable event (removal at the terminal rack vs other events), by use (highway vs nontaxable uses), by dye status (undyed vs dyed diesel and kerosene), and by aviation use.

This file covers the high-level structure. For deep computation, Pub. 510 and the Form 720 instructions are the authoritative references.

**Verified against:** Form 720 (Rev. June 2026), Instructions for Form 720 (Rev. June 2026), Pub. 510 (Rev. Dec. 2025), Form 637 (Rev. Dec. 2025), and the 2025 Form 4136, on 2026-10-06. The rates below are the rates printed on Form 720; they already include the $.001 LUST tax where it applies. Re-check the current Form 720 before each quarter.

---

## Fuel categories on Form 720 (Part I)

### Gasoline (§4081)

| IRS No. | Category | Rate per gallon |
|---------|----------|-----------------|
| 62 | Gasoline: (a) removal at terminal rack, (b) other taxable events (including alcohol blended with taxed gasoline outside the bulk system) | $.184 |
| 14 | Aviation gasoline | $.194 |

The $.184 gasoline rate is not inflation-adjusted. Gallons on 62(a) and 62(b) are combined into one "Tax" entry (i720 "Gasoline (IRS No. 62)").

### Diesel (§4081)

| IRS No. | Category | Rate per gallon |
|---------|----------|-----------------|
| 60 | Diesel: (a) removal at terminal rack, (b) other taxable events, (c) biodiesel blended with taxed diesel outside the bulk transfer/terminal system | $.244 |
| 104 | Diesel-water fuel emulsion (at least 14% water, EPA-registered additive, registered taxpayer) | $.198 |
| 105 | Dyed diesel, LUST tax | $.001 |

Dyed diesel removed for a nontaxable use is exempt from the $.243 portion of the tax but owes the $.001 LUST tax (IRS No. 105). Using dyed fuel in a taxable use triggers the tax and the §6715 penalty.

### Kerosene (§4081)

| IRS No. | Category | Rate per gallon |
|---------|----------|-----------------|
| 35 | Kerosene: (a) removal at terminal rack (not at an airport), (b) other taxable events | $.244 |
| 107 | Dyed kerosene, LUST tax | $.001 |
| 69 | Kerosene for use in aviation (noncommercial aviation, or commercial aviation that doesn't meet the reduced-rate requirements) | $.219 |
| 77 | Kerosene for use in commercial aviation (other than foreign trade), registered "Y" operators only | $.044 |
| 111 | Kerosene for use in aviation, LUST tax on nontaxable uses | $.001 |
| 119 | LUST tax, other exempt removals | $.001 |

### Alternative fuels (§4041) and other fuels

| IRS No. | Category | Rate |
|---------|----------|------|
| 112 | Liquefied petroleum gas (LPG, including propane) | $.183 per gasoline gallon equivalent (5.75 lb or 1.353 gal of LPG) |
| 118 | "P Series" fuels | $.184 per gallon |
| 120 | Compressed natural gas (CNG) | $.183 per GGE (5.66 lb or 123.57 cu ft) |
| 121 | Liquefied hydrogen | $.184 per gallon |
| 122 | Fischer-Tropsch process liquid fuel from coal | $.244 per gallon |
| 123 | Liquid fuel derived from biomass | $.244 per gallon |
| 124 | Liquefied natural gas (LNG) | $.243 per diesel gallon equivalent (6.06 lb or 1.71 gal of LNG) |
| 79 | Other fuels (e.g., qualified ethanol or methanol from coal $.184; ethanol from natural gas $.114; methanol from natural gas $.0925; B-100 $.244; liquefied gas from biomass $.184) | per i720 table |

Alternative fuel tax is owed when the fuel is delivered into the fuel supply tank of a motor vehicle or motorboat, or on certain bulk sales. Example from i720: 10,000 gallons of LNG ÷ 1.71 = 5,848 DGE × $.243 = $1,421.06.

### Inland waterways fuel (§4042, Part II)

| IRS No. | Category | Rate |
|---------|----------|------|
| 64 | Inland waterways fuel use tax | $.29 per gallon |
| 125 | LUST tax on inland waterways fuel use | $.001 per gallon |

IRS No. 64 applies to fuel used by commercial vessels on the inland or intracoastal waterways specified in §4042(d), in addition to all other fuel taxes. IRS No. 125 applies only to fuel not already subject to LUST tax under §4041(d) or §4081 (for example, Bunker C residual fuel oil is reported on both 64 and 125). Both are Part II lines: paid with the return, not deposited.

---

## The distribution chain (who pays first)

Federal motor fuel tax is generally collected at the **terminal rack**: the point where fuel leaves the bulk transfer/terminal system. The **position holder** at the terminal is liable for the tax on removal at the rack.

```
Refinery → Pipeline/Vessel → Terminal (TANK) → RACK → Truck → Distributor → Retailer → Consumer
                                                  ↑
                                       Federal tax collected here (§4081)
```

**Position holder** = the person that holds the inventory position in the fuel at the terminal, as reflected in the terminal operator's records.

**Terminal operator** = the person that operates the terminal. Terminal operators report to the IRS on Form 720-TO, not on Schedule T. Schedule T of Form 720 is used by taxable fuel registrants that receive or deliver fuel in a two-party exchange within a terminal (i720 "Schedule T").

The terminal-rack tax model means:
- A retail gas station generally does NOT file Form 720 for gasoline or diesel tax; the tax is in its purchase price.
- A position holder files Form 720 quarterly with Schedule A and semimonthly EFT deposits (Part I taxes).
- A truck fleet or farm paying fuel tax through the purchase price doesn't file Form 720. Its refund route is Form 8849 or Form 4136, unless it already files Form 720 for another Part I or II liability.

---

## Refund and credit claims (Schedule C of Form 720)

Schedule C is available only to a filer reporting a liability in Part I or II. Others claim on Form 8849 (Schedule 1 for nontaxable use, Schedule 2 for ultimate vendors) or annually on Form 4136 with the income tax return (i720 "Schedule C. Claims").

Common claim lines (rates and CRNs as printed on Form 720, Rev. June 2026):

| Line | Claim | Rate | CRN |
|------|-------|------|-----|
| 1a | Gasoline, nontaxable use (types of use 2, 4, 5, 7, 12) | $.183 | 362 |
| 2b | Aviation gasoline, other nontaxable use | $.193 | 324 |
| 3a | Undyed diesel, nontaxable use (e.g., off-highway business use, type 2) | $.243 | 360 |
| 3b | Undyed diesel used in trains | $.243 | 353 |
| 3c | Undyed diesel used in certain intercity and local buses | $.17 | 350 |
| 3d | Undyed diesel used on a farm for farming purposes | $.243 | 360 |
| 4a / 4c | Undyed kerosene (non-aviation), nontaxable use / farm use | $.243 | 346 |
| 6a–6h | Nontaxable use of alternative fuel | $.183 or $.243 | 419–425, 435 |
| 7a–11b | Registered ultimate vendor sales (state or local government, nonprofit educational organization, buses, blocked pump, aviation) | per form | 350, 355, 360, 362, 324, 346, 347, 369, 417, 418, 433 |

Schedule C lines 12 and 13 are "Reserved for future use". The biodiesel, renewable diesel, and agri-biodiesel mixture credits and the alternative fuel and alternative fuel mixture credits (§6426(c)–(e)) expired for fuel sold or used after Dec 31, 2024, and OBBBA (P.L. 119-21) ended the §6426(k) SAF mixture credit for sales or uses after Sep 30, 2025 (Pub. 510, Rev. Dec. 2025, "What's New" and "Reminders"). Don't claim them unless Congress extends them.

Each Schedule C claim requires (i720 "Schedule C. Claims"):
- "Month your income tax year ends" (MM) and "Period of claim" (MM/DD/YYYY–MM/DD/YYYY)
- Type of use number where the line asks for it, rate, gallons, amount, and CRN
- For ultimate vendor and credit card issuer claims, the Form 637 registration number
- A combined claim of at least $750 for lines 1–6 and 14b–14d for the quarter (or aggregated quarters of the income tax year); otherwise make an annual claim on Form 4136

### Form 637 registration

Form 637 (Rev. Dec. 2025) activity letters relevant to fuel claims and fuel liability include:

| Letter | Activity (abbreviated from Form 637) |
|--------|--------------------------------------|
| M | Blender of gasoline, diesel fuel, or kerosene |
| S | Enterer, position holder, refiner, terminal operator, and others in the bulk system |
| AL | Alternative fueler that sells for use or uses alternative fuel |
| AM | Alternative fueler that produces an alternative fuel mixture |
| K | Buyer of kerosene for a feedstock purpose |
| Y | Buyer of kerosene for its use in commercial aviation |
| UA / UB / UP / UV | Ultimate vendors (kerosene for aviation; undyed diesel or kerosene for buses; kerosene from a blocked pump; gasoline, aviation gasoline, undyed diesel or kerosene for state or local government or nonprofit educational use) |
| CC | Credit card issuer |

A claim that requires registration is disallowed without a current registration number. Check the user's registration letter before filling Schedule C lines 7–11 or 14e.

---

## Semimonthly deposits and Schedule A

Fuel taxes are Part I taxes. Deposits by electronic funds transfer are required semimonthly unless the Part I net liability for the quarter is $2,500 or less (i720 "Payment of Taxes"). Schedule A records the net liability in each semimonthly period:

```
Box A: Day 1 – 15 of month 1      Box B: Day 16 – end of month 1
Box C: Day 1 – 15 of month 2      Box D: Day 16 – end of month 2
Box E: Day 1 – 15 of month 3      Box F: Day 16 – end of month 3
Box G: special rule for September (Q3 only)
```

Deposit due date (regular method): **by the 14th day after the end of each semimonthly period**: generally the 29th of the same month and the 14th of the next month. If the due date is a Saturday, Sunday, or legal holiday, deposit by the preceding business day. September has an additional deposit (in 2026, liability for Sept. 16–26 due Sept. 29).

Failure to deposit on time triggers §6656 penalties:

| Days late | Penalty rate |
|-----------|-------------|
| 1–5 days | 2% |
| 6–15 days | 5% |
| More than 15 days | 10% |
| Not deposited within 10 days after the first IRS delinquency notice, or on notice and demand | 15% |

The agent flags any deposit-timing risk in the validation summary.

---

## Common fuel-tax scenarios

### Farm using taxed gasoline — no Form 720

A farm uses 1,000 gallons of taxed gasoline in tractors on the farm during 2025. It has no Form 720 liability, so it can't use Schedule C, and Schedule C line 1 doesn't list type of use 1 (farm) for gasoline anyway. The farm claims the credit on Form 4136 line 1b (type of use 1, $.183, CRN 362) with its income tax return: 1,000 × $.183 = $183.

### Commercial trucking — embedded tax, no Form 720 unless another liability

A trucking company pays diesel tax through its fuel purchases. It doesn't file Form 720 for fuel tax. Possible claims:
- Undyed diesel used in a separate motor that runs a refrigeration unit is off-highway business use (type of use 2). If the same tank feeds the propulsion motor, the company figures the separate-motor gallons by a reasonable, documented estimate (Pub. 510 "Use in separate motor"). Claim at $.243 per gallon (CRN 360) on Form 8849 Schedule 1 or Form 4136, or on Form 720 Schedule C line 3a only if the company files Form 720 for another liability.
- HVUT credits for vehicles sold, destroyed, or stolen are NOT Form 720 items. They go on Form 2290 line 5 or Form 8849 Schedule 6.

### Former biodiesel blender — credit expired

A blender that mixes biodiesel with petroleum diesel used to claim the §6426(c) biodiesel mixture credit on Schedule C. That credit expired for mixtures sold or used after Dec 31, 2024, and Schedule C line 12 is now reserved. The agent must not compute it for 2025 or 2026 quarters. A blender that produces diesel by blending biodiesel with taxed diesel outside the bulk system still reports the biodiesel gallons on IRS No. 60(c) at $.244.

### Position holder at a terminal — full filing

A position holder files Form 720 quarterly:
- Part I IRS Nos. 60, 62, 35 (and 105, 107, 119 for dyed and exempt removals) with gallons removed at the rack × rate
- Schedule A semimonthly net liability; semimonthly EFT deposits
- Schedule T if it received or delivered gallons in a two-party exchange within a terminal
- Schedule C for its own claims, if any

This is the most complex Form 720 filer profile and is typically handled by professional preparers.

---

## Why this skill keeps fuel tax at the reference level only

Fuel tax filings for position holders involve high volumes, industry terms (rack, blender, position holder, terminal operator), and Form 637 registration management. A skill cannot fully automate this without provider-specific tooling.

For users with complex fuel-tax obligations, the agent should:
1. Confirm the IRS Nos. and rates from the current Form 720
2. Surface the Schedule A and deposit-timing requirements
3. Identify any Schedule C claims they're entitled to (only if they report a Form 720 liability)
4. **Hand off to a CPA or excise-tax specialist** for the actual filing

For small-volume claimants (a farm or fleet with off-highway use), route to Form 4136 or Form 8849 and keep Form 720 out of it unless there is a Form 720 liability. For position-holder filings, treat this skill as an outline only.
