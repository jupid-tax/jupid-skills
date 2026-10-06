# IRS Number Catalog for Form 720

The IRS No. is a 2- or 3-digit code preprinted next to each tax line on Form 720. The agent uses this catalog to answer "which line does this user's tax go on?" and to confirm the rate, the base, and whether the line is in Part I or Part II.

**Revision:** every IRS No. and rate below was checked against the text of Form 720 (Rev. June 2026) and the Instructions for Form 720 (Rev. June 2026) on 2026-10-06. Rates for later quarters can change by statute or annual inflation adjustment (arrow shafts, air transportation). Check https://www.irs.gov/forms-pubs/about-form-720 for a newer revision before relying on this table.

**Why Part I vs Part II matters:** Part I taxes go on Schedule A and are generally deposited semimonthly (no deposit if the quarter's Part I net liability is $2,500 or less). Part II taxes (other than the ODC floor stocks tax) are paid with the return and never go on Schedule A (i720 "Payment of Taxes"; Form 720 Schedule A note).

---

## How to use this catalog

1. The user describes their excise tax obligation in plain English (e.g., "I import fishing rods").
2. The agent locates the IRS No. below and notes whether it is Part I or Part II.
3. The agent confirms the IRC section, base, and rate against the current Form 720 PDF.
4. The agent populates Part I or Part II of the SKILL.md output template.

---

## Part I — Environmental taxes (figure on Form 6627, attach it)

| IRS No. | Category | IRC § |
|---------|----------|-------|
| 53 | Domestic petroleum superfund tax | §4611 |
| 16 | Imported petroleum products superfund tax | §4611 |
| 54 | Chemicals (other than ODCs) | §4661 |
| 17 | Imported chemical substances | §4671 |
| 98 | Ozone-depleting chemicals (ODCs) | §4681 |
| 19 | ODC tax on imported products | §4681 |

The superfund petroleum tax is $0.18 per barrel for 2026 (Pub. 510, Rev. Dec. 2025, "What's New"). The oil spill liability taxes (former IRS Nos. 18 and 21) expired after 2025; their rows are "Reserved for future use" (i720 "What's New").

## Part I — Communications and air transportation

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 22 | Local telephone service and teletypewriter exchange service | Amount paid | 3% | §4251 |
| 26 | Transportation of persons by air | Amount paid + per domestic segment | 7.5% + $5.30 per segment (2026); $5.20 (2025) | §4261(a)–(b) |
| 28 | Transportation of property by air | Amount paid | 6.25% | §4271 |
| 27 | Use of international air travel facilities | Per person | $23.40 (2026), $22.90 (2025); Alaska/Hawaii departures $11.70 (2026), $11.40 (2025) | §4261(c) |

Sources: Rev. Proc. 2024-40 §2.45 (2025), Rev. Proc. 2025-32 §4.44 (2026), i720 "What's New".

## Part I — Fuel taxes

| IRS No. | Category | Rate per gallon | IRC § |
|---------|----------|-----------------|-------|
| 60 | Diesel: (a) rack removal, (b) other events, (c) biodiesel mixture not at rack | $.244 | §4081 |
| 104 | Diesel-water fuel emulsion | $.198 | §4081(a)(2)(D) |
| 105 | Dyed diesel, LUST tax | $.001 | §4081 |
| 107 | Dyed kerosene, LUST tax | $.001 | §4081 |
| 119 | LUST tax, other exempt removals | $.001 | §4081 |
| 35 | Kerosene: (a) rack removal, (b) other events | $.244 | §4081 |
| 69 | Kerosene for use in aviation | $.219 | §4081(a)(2)(C) |
| 77 | Kerosene for use in commercial aviation (other than foreign trade) | $.044 | §4081(a)(2)(C) |
| 111 | Kerosene for use in aviation, LUST tax on nontaxable uses | $.001 | §4081 |
| 79 | Other fuels (rate table in i720) | $.0925–$.244 | §4041 |
| 62 | Gasoline: (a) rack removal, (b) other events | $.184 | §4081 |
| 13 | Surtax on fuel used in a fractional ownership program aircraft | $.141 | §4043 |
| 14 | Aviation gasoline | $.194 | §4081 |
| 112 | LPG | $.183 per GGE | §4041 |
| 118 | "P Series" fuels | $.184 | §4041 |
| 120 | CNG | $.183 per GGE | §4041 |
| 121 | Liquefied hydrogen | $.184 | §4041 |
| 122 | Fischer-Tropsch liquid fuel from coal | $.244 | §4041 |
| 123 | Liquid fuel derived from biomass | $.244 | §4041 |
| 124 | LNG | $.243 per DGE | §4041 |

Fuel tax rules depend on the event (rack removal vs other) and the fuel. Load `references/fuel-taxes.md` for the deep dive.

## Part I — Retail, ship passenger, other, foreign insurance, manufacturers

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 33 | Truck, trailer, and semitrailer chassis and bodies, and tractors (first retail sale; parts installed within 6 months) | Sale price | 12% | §4051 |
| 29 | Transportation by water (ship passengers) | Per passenger | $3 | §4471 |
| 31 | Obligations not in registered form | Principal × years | $.01 | §4701 |
| 155 | Remittance transfers (after Dec 31, 2025) | Amount transferred | 1% | §4475 |
| 30 | Policies issued by foreign insurers | Premiums paid | 4% casualty and indemnity bonds; 1% life, sickness, accident, annuity; 1% reinsurance | §4371 |
| 36 / 37 | Coal, underground mined | Tons / sale price | $1.10 per ton / 4.4% | §4121 |
| 38 / 39 | Coal, surface mined | Tons / sale price | $.55 per ton / 4.4% | §4121 |
| 108 / 109 / 113 | Taxable tires | Max rated load over 3,500 lb | $.0945 / $.04725 / $.0945 per 10 lb | §4071 |
| 40 | Gas guzzler (Form 6197) | Form 6197 | Form 6197 | §4064 |
| 97 | Vaccines | Doses | $.75 per taxable vaccine | §4131 |

The IRS No. 33 retail tax applies to truck chassis and bodies for vehicles over 33,000 lb GVW, trailer chassis and bodies over 26,000 lb GVW, and highway tractors (except tractors of 19,500 lb GVW or less with gross combined weight of 33,000 lb or less). The §4051(b) tax on parts and accessories installed within 6 months of placing the vehicle in service applies only if their total price, including installation, exceeds $1,000; idling reduction devices and qualifying insulation are exempt (i720 "Retail Tax"; Pub. 510 ch. 6). The $1,000 test applies only to §4051(b) parts and accessories, not to the vehicle sale. The retail tax terminates on Oct 1, 2028 (§4051(c)).

Foreign insurance: the person who pays the premium to the foreign insurer (or to a nonresident person such as a foreign broker) pays the tax and files. Treaty-based exemptions require a disclosure statement (Form 8833 or equivalent) filed with the first-quarter Form 720 (i720 "Foreign Insurance Taxes").

---

## Part II

### PCOR fee

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 133 | Patient-centered outcomes research fee: specified health insurance policies (rows a, b) and applicable self-insured health plans (rows c, d) | Average covered lives | $3.47 for policy/plan years ending Oct 1, 2024 – Sep 30, 2025 (Notice 2024-83); $3.84 for years ending Oct 1, 2025 – Sep 30, 2026 (Notice 2025-61) | §4375, §4376 |

The PCOR fee is the most commonly asked-about Form 720 item for small businesses. It applies to plan years ending before Oct 1, 2029 (§4376(e)). Load `references/pcori-fee.md` for the deep dive.

There is no other fee of this type on Form 720. Don't confuse it with the ACA health insurance providers fee, which was repealed after 2020 and has no line on Form 720 (Rev. June 2026).

### Sport fishing and archery (manufacturers taxes)

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 41 | Sport fishing equipment (other than rods and poles) | Sale price | 10% | §4161(a)(1)(A) |
| 110 | Fishing rods and fishing poles | Sale price | 10%, max $10 per article | §4161(a)(1)(B) |
| 42 | Electric outboard motors | Sale price | 3% | §4161(a)(2) |
| 114 | Fishing tackle boxes | Sale price | 3% | §4161(a)(3) |
| 44 | Bows (peak draw weight 30 lb or more), parts and accessories, quivers, broadheads, points | Sale price | 11% | §4161(b)(1) |
| 106 | Arrow shafts | Per shaft | $.65 (2026), $.63 (2025) | §4161(b)(2) |

Pub. 510 (Rev. Dec. 2025, ch. 5): "Pay this tax with Form 720. No tax deposits are required." Load `references/sport-fishing-archery.md`.

### Indoor tanning

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 140 | Indoor tanning services | Amount paid | 10% | §5000B |

The tax is paid by the customer and collected by the provider; if the provider doesn't collect it, the provider is liable. The line is on Form 720 (Rev. June 2026) and the tax is described in i720 "Indoor Tanning Services Tax".

### Other Part II taxes

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 64 | Inland waterways fuel use tax | Gallons | $.29 | §4042 |
| 125 | LUST tax on inland waterways fuel use | Gallons | $.001 | §4042 |
| 51 | Section 40 fuels (second generation biofuel recapture) | Gallons | Credit rate ($1.01) | §40(d)(3)(D) |
| 117 | Biodiesel sold as but not used as fuel (recapture) | Gallons | Credit rate | §40A(d)(3) |
| 20 | ODC floor stocks tax (Form 6627) | Form 6627 | Form 6627 | §4682(h) |
| 150 | Repurchase of corporate stock (Form 7208) | Form 7208 | 1% | §4501 |
| 142 | Sales of designated drugs during statutory periods | Sales | §5000D | §5000D |

---

## Not on Form 720

- Alcohol, tobacco, and firearms excise taxes are TTB taxes, filed on TTB forms (e.g., TTB F 5000.24), not Form 720.
- Wagering excise (Form 730) and occupational tax on wagering (Form 11-C).
- Heavy Highway Vehicle Use Tax and HVUT credits (Form 2290; refunds on Form 8849 Schedule 6).

---

## How to find an obscure category

If the user describes an excise tax not listed above:

1. Search Pub. 510 (https://www.irs.gov/pub/irs-pdf/p510.pdf) by category name
2. Confirm the IRS No. against the current Form 720 and instructions
3. Verify the rate is current; fuel, chemical, and inflation-adjusted rates change
4. If the category isn't on Form 720 at all, check whether it's on:
   - Form 11-C (wagering occupational tax)
   - Form 730 (wagering excise)
   - Form 2290 (HVUT)
   - Form 8849 or Form 4136 (refund-only claims)
   - TTB forms (alcohol, tobacco, firearms)
   - State excise (varies by state)

---

## Statutory authority pyramid (when in doubt)

1. **IRS Form 720 and its instructions** (f720.pdf, i720.pdf) — the lines and rates for the quarter
2. **Pub. 510 (Excise Taxes)** — overview; not updated annually
3. **IRC Subtitle D** — statutory authority
4. **Treasury Regulations** (26 CFR Parts 40, 46, 48, 49) — procedure and definitions
5. **IRS Notices** (e.g., 2025-61 for the PCOR fee) and **Revenue Procedures** (e.g., 2025-32 for inflation adjustments)
6. **Revenue Rulings** — specific situations

The agent always cites the most specific authority that supports the position taken on the form.
