# IRS Number Catalog for Form 720

The IRS Number is a 2–3 digit code identifying each excise tax category on Form 720. The agent uses this catalog to answer "which line does this user's tax go on?" and to confirm rate and base.

**Always verify rates against the latest Pub. 510 and Form 720 instructions** — rates change by statute, especially fuel taxes during transportation funding bill cycles.

---

## How to use this catalog

1. The user describes their excise tax obligation in plain English (e.g., "I sell fishing rods").
2. The agent locates the relevant IRS Number(s) below.
3. The agent confirms the IRC section, base, and rate from the latest IRS guidance.
4. The agent populates Part I (or Part II for PCORI/specials) of the SKILL.md output template.

---

## Part I — Excise taxes (most common)

### Communications and air transportation

| IRS No. | Category | Base | Rate (verify) | IRC § |
|---------|----------|------|---------------|-------|
| 14 | Local telephone service / teletypewriter exchange | Amount paid | 3% | §4251 |
| 22 | Air transportation of persons (domestic) | Amount paid + segment fee | 7.5% + segment fee per segment ($5.20 in 2025) | §4261 |
| 26 | Air transportation of property | Amount paid | 6.25% | §4271 |
| 27 | International air travel facilities (departure) | Per passenger | $22.20 (2025; verify for 2026) | §4261(c) |
| 28 | Use of facilities — Hawaii/Alaska air | Per passenger | $11.10 (2025) | §4261(c)(3) |
| 29 | Transportation by water (passenger ships) | Per passenger | $5.00 | §4471 |

### Fuel taxes (the largest dollar category)

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 35 | Diesel-water fuel emulsions | Per gallon | $0.198 (verify) | §4081 |
| 51 | LUST tax (Leaking UST) | Per gallon | $0.001 | §4081(a)(2)(B) |
| 60 | Gasoline (rack rate) | Per gallon | $0.184 (basic) + $0.001 LUST | §4081 |
| 62 | Gasoline (retail) | Per gallon | $0.184 + LUST | §4081 |
| 64 | Inland waterways fuel | Per gallon | $0.29 + LUST | §4042 |
| 71 | Aviation gasoline | Per gallon | $0.194 (verify) | §4081 |
| 79 | Diesel fuel (rack rate) | Per gallon | $0.244 + LUST | §4081 |
| 105 | Kerosene (rack rate) | Per gallon | $0.244 + LUST | §4081 |

Fuel tax rates have specific quirks: rate differs for clear vs dyed, blended vs pure, used on-highway vs off-highway. Load `references/fuel-taxes.md` for the deep dive.

### Manufacturer's excise

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 41 | Sport fishing equipment (rods, reels, etc.) | Sales price | 10% | §4161(a)(1) |
| 42 | Fishing tackle boxes | Sales price | 3% | §4161(a)(1)(A) |
| 110 | Electric outboard motors | Sales price | 3% | §4161(a)(1)(B) |
| 44 | Bows ≥ 30 lb draw weight | Sales price | 11% | §4161(b)(1) |
| 106 | Arrows (per shaft, not assembled arrows) | Per arrow shaft | $0.59 (verify) | §4161(b)(2)(A) |
| 119 | Quivers, broadheads, points (archery) | Sales price | 11% | §4161(b)(2)(B) |
| 8 | Truck, trailer, semitrailer chassis & bodies | Sales price | 12% | §4051 |

The 12% retail tax on heavy trucks (IRS No. 8) is significant and has a $1,000 small-purchase floor. Often filed by dealers and reported on Form 720.

### Foreign insurance (§4371)

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 104 | Casualty/indemnity foreign insurance | Premium | 4% | §4371(1) |
| 105 (Part II) | Life/sickness/accident foreign insurance | Premium | 1% | §4371(2) |
| 107 | Foreign reinsurance | Premium | 1% | §4371(3) |

Note: tax-treaty exemptions may apply (Bermuda, UK, Switzerland, etc.). Check the relevant treaty before applying §4371.

### Environmental and chemical

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 18 | Petroleum (Superfund) | Per barrel | varies (reinstated under IRA 2022) | §4611 |
| 53 | Coal — underground | Per ton | varies | §4121 |
| 54 | Coal — surface | Per ton | varies | §4121 |
| 121 | Vaccines | Per dose | $0.75 per disease per dose | §4131 |
| 125 | Ozone-depleting chemicals (ODC) | Per pound | varies by chemical | §4681 |
| 17 | Chemicals subject to chapter 38 (Superfund) | Per ton | varies (reinstated under IRA) | §4661 |

The Inflation Reduction Act of 2022 reinstated/updated several chemical and petroleum excises. Verify rates against post-2022 IRS guidance.

### Tobacco (limited Form 720 applicability)

Tobacco excise tax is generally filed on **Form 5000.24** (TTB form) by manufacturers and importers, NOT on Form 720. Form 720 IRS No. 19 is rarely the right line for tobacco. Verify before filing.

### Wagering — different forms

Wagering excise (Form 730) and occupational wagering tax (Form 11-C) are NOT Form 720 categories. Redirect to those forms.

---

## Part II — Other excise taxes

### PCORI fee

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 133 | PCORI fee (Patient-Centered Outcomes Research Institute) | Average covered lives | $3.22/life for plan years ending Oct 1, 2024 – Sep 30, 2025 (Notice 2024-83); rate for plan years ending after Oct 1, 2025 set by IRS notice — verify | §4375, §4376 |

The PCORI fee is the most commonly asked-about Form 720 item for small businesses. Load `references/pcori-fee.md` for the deep dive.

### Patient-Centered Fees (other)

There are no other PCORI-like fees on Form 720 currently. The "Annual fee on health insurance providers" (former IRS No. 132) was repealed effective 2021. Don't confuse with current PCORI.

### Special fuel and waterways

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 30 | Inland waterways fuel use | Per gallon | $0.29 | §4042 |

### Indoor tanning

| IRS No. | Category | Base | Rate | IRC § |
|---------|----------|------|------|-------|
| 140 | Indoor tanning services | Amount paid | 10% | §5000B |

**Status note**: §5000B has been the subject of repeal proposals. As of Apr 2026, the agent must verify the tax is still in effect for the quarter being filed. The IRS Form 720 instructions are the authoritative current-status indicator. If repealed, IRS No. 140 should NOT be filed.

---

## How to find an obscure category

If the user describes an excise tax not listed above:

1. Search Pub. 510 (https://www.irs.gov/pub/irs-pdf/p510.pdf) by category name
2. Confirm the IRS Number against the current Form 720 instructions
3. Verify the rate is current — fuel and chemical rates change by statute periodically
4. If the category isn't on Form 720 at all, check whether it's on:
   - Form 11-C (wagering occupational tax)
   - Form 730 (wagering excise)
   - Form 2290 (HVUT)
   - Form 8849 (refund-only claims)
   - Form 5000.24 (TTB tobacco)
   - State excise (varies by state)

---

## Statutory authority pyramid (when in doubt)

1. **IRS Form 720 instructions** (i720.pdf) — operational rules per quarter
2. **Pub. 510 (Excise Taxes)** — comprehensive overview
3. **IRC Subtitle D** (§§4001–5891) — statutory authority
4. **Treasury Regulations** (26 CFR Part 40, 41–53) — interpretive
5. **IRS Notices** (e.g., 2024-83 for PCORI) — annual rate-setting
6. **Revenue Procedures / Rulings** — specific situations

The agent always cites the most specific authority that supports the position taken on the form.
