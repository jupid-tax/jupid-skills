# Fuel Taxes on Form 720

Federal fuel excise tax is the largest single category on Form 720 by dollar volume. The structure is complex: rates differ by fuel type, by who's selling (manufacturer vs distributor), by use (on-highway vs off-highway), by additive content (clear vs dyed diesel), and by location in the distribution chain (terminal rack vs retail).

This file covers the high-level structure. For deep computation, the IRS Pub. 510 and Form 720 instructions are the authoritative references.

---

## Fuel categories on Form 720

### Gasoline (§4081)

| IRS No. | Category | Rate (verify Pub. 510) |
|---------|----------|------------------------|
| 60 | Gasoline removed at terminal rack | $0.184/gal + $0.001 LUST = $0.185 |
| 62 | Gasoline (retail/blending) | Same as above |
| 71 | Aviation gasoline | $0.194/gal (verify) |

The basic federal gasoline tax has been $0.184/gal since 1993 (NOT inflation-adjusted). The Highway Trust Fund collects the bulk of this; LUST adds $0.001.

### Diesel (§4081)

| IRS No. | Category | Rate |
|---------|----------|------|
| 60 / 79 | Diesel (rack rate) | $0.244/gal + $0.001 LUST |
| 35 | Diesel-water emulsions | $0.198/gal |

Dyed diesel (red diesel for off-highway use) is **not** subject to §4081 at the rack — but if dyed diesel is later used on-highway, it triggers the tax.

### Kerosene

| IRS No. | Category | Rate |
|---------|----------|------|
| 105 | Kerosene (rack) | $0.244/gal + $0.001 LUST |
| 35 | Kerosene for use in aviation (commercial) | $0.044/gal (verify) |
| 77 | Kerosene for use in non-commercial aviation | $0.219/gal (verify) |

### Alternative fuels

| IRS No. | Category | Rate (verify) |
|---------|----------|---------------|
| 117 | Compressed natural gas (CNG) | $0.183/GGE (gallon-gas-equivalent) |
| 120 | Liquefied natural gas (LNG) | $0.243/gal |
| 78 | Propane | $0.183/gal |

### Inland waterways fuel (§4042)

| IRS No. | Category | Rate |
|---------|----------|------|
| 64 | Inland waterways fuel use | $0.29/gal + LUST = $0.291 |

This applies to fuel consumed by vessels on certain inland waterways (Mississippi, Ohio, Tennessee, Columbia, etc., per a list maintained in §4042). Operators must self-report based on gallon consumption.

---

## The distribution chain (who pays first)

Federal motor fuel tax is collected at the **terminal rack** — the point where fuel leaves the bulk distribution system and enters the retail/wholesale chain. The "position holder" at the terminal is liable.

```
Refinery → Pipeline/Vessel → Terminal (TANK) → RACK → Truck → Distributor → Retailer → Consumer
                                                  ↑
                                       Federal tax collected here (§4081)
```

**Position holder** = the entity that holds the inventory at the terminal at the time of removal. Usually a major oil company; sometimes a smaller distributor.

**Terminal operator** = the entity that operates the terminal facility (often different from the position holder). Files Schedule T of Form 720.

The terminal-rack tax model means:
- A small retail gas station does NOT file Form 720 for fuel tax — it pays the tax embedded in wholesale price.
- A position holder (major oil company / large distributor) files Form 720 quarterly with semi-monthly Schedule A reporting and EFTPS deposits.
- A truck-fleet operator paying fuel tax via wholesale price doesn't file Form 720 — they may file refund claims on Form 8849 if eligible.

---

## Refund and credit claims (Schedule C of Form 720)

Many fuel users are eligible for refunds because the §4081 tax is collected at terminal removal regardless of end use. Common claims:

| CRN | Type of claim | IRC | Common claimant |
|-----|---------------|-----|-----------------|
| 360 | Nontaxable use of gasoline | §6421 | Off-highway business use, farming |
| 362 | Nontaxable use of aviation gasoline | §6421(c) | Foreign trade |
| 346 | Nontaxable use of diesel fuel | §6427 | Farming, off-highway |
| 347 | Nontaxable use of kerosene | §6427 | Off-highway, aviation outside commercial |
| 309 | Biodiesel mixture credit | §6426 | Blender of biodiesel B100 + diesel mix |
| 310 | Renewable diesel mixture credit | §6426 | Blender of renewable diesel |
| 396 | Alternative fuel credit | §6426 | Operator using LPG, LNG, CNG |
| 397 | Alternative fuel mixture credit | §6426 | Blender of alt fuel mix |
| 415 | Sustainable aviation fuel (SAF) credit | §6426/IRA-2022 | SAF blender (verify post-IRA implementation) |

Each claim row on Schedule C requires:
- CRN (3-digit code)
- Type of claim description
- Period covered (start/end dates within the quarter)
- Number of gallons (or other base)
- Rate per gallon
- Total amount claimed
- Form 637 registration letter (if applicable)

### Form 637 registration

Many alternative-fuel claims require a current **Form 637 registration**. Activity letters relevant to Schedule C claims:

| Letter | Activity |
|--------|----------|
| M | Alternative fuel mixture |
| AL | Alternative fueler |
| AB | Alternative fuel mixture blender |
| H | Heating use (claims for diesel used for heating) |
| K | Kerosene blender |
| Y | Hospitals, nursing homes (off-highway use) |

A claim filed without current Form 637 registration is denied. The agent must verify the user's registration status before populating Schedule C.

---

## Semi-monthly deposits and Schedule A

For fuel tax filers above the §6011(a) threshold (typically > $2,500 in liability per quarter), deposits are required twice per month via EFTPS. Schedule A reports the liability incurred during each semi-monthly period:

```
Period 1: Day 1 – 15 of month 1
Period 2: Day 16 – end of month 1
Period 3: Day 1 – 15 of month 2
Period 4: Day 16 – end of month 2
Period 5: Day 1 – 15 of month 3
Period 6: Day 16 – end of month 3
```

Deposit due date: **14 calendar days after the end of each semi-monthly period**.

Failure to deposit on time triggers §6656 penalties:

| Days late | Penalty rate |
|-----------|-------------|
| 1–5 days | 2% |
| 6–15 days | 5% |
| 16+ days | 10% |
| After IRS demand | 15% |

The agent flags any deposit-timing risk in the validation summary.

---

## Common fuel-tax scenarios

### Small farm tractor — refund only

A farmer buys 1,000 gallons of gasoline for tractor use during 2026. The gas station charged the federal tax (~$0.184/gal embedded). Farmer files Schedule C of Form 720 (or Form 8849 Schedule 1) with CRN 360, claiming refund of $184.

The farmer does NOT file Part I/II of Form 720 — they're not a position holder. Just a refund claimant.

### Commercial trucking — embedded tax, no Form 720 unless claim

A trucking company pays diesel tax via wholesale fuel purchases. They don't file Form 720 unless:
- They have an HVUT credit (Form 2290 prorated) — file Schedule C with CRN 365
- They use diesel for off-highway equipment (e.g., reefer units, generators) — file Schedule C with CRN 346

### Biodiesel blender — credit claim

A blender that mixes B99 biodiesel + 1% petroleum diesel files Schedule C of Form 720 with CRN 309 to claim the §6426 biodiesel mixture credit ($1.00/gal of biodiesel content). Requires Form 637 letter AB or M.

The blender must also file Form 720 Part I/II if they're a position holder; otherwise the Schedule C claim alone is acceptable on Form 720 (or use Form 8849 for refund-only filings).

### Position holder at a terminal — full filing

A position holder at a fuel terminal files Form 720 quarterly:
- Part I Lines 60, 79, 105 with gallons removed from rack × rate
- Schedule A semi-monthly liability tracking
- Schedule C if any nontaxable-use refund claims by their direct customers
- Schedule T if they're also the terminal operator

This is the most complex Form 720 filer profile and typically managed by tax software / professional preparers.

---

## Why this skill keeps fuel tax at the reference level only

Fuel tax filings span thousands of lines per quarter for major position holders, with industry-specific terminology (rack, blender, position holder, terminal operator) and Form 637 registration management. A skill cannot fully automate this without provider-specific tooling.

For users with complex fuel-tax obligations, the agent should:
1. Confirm the IRS Numbers and rates from the catalog
2. Surface the Schedule A and deposit-timing requirements
3. Identify any Schedule C claims they're entitled to
4. **Hand off to a CPA or excise-tax specialist** for the actual filing — this is not a do-it-yourself category

For small-volume claimants (farmer with off-highway gasoline, occasional alternative fuel mixer), the skill can produce a workable Schedule C entry. For position-holder filings, treat this skill as an outline only.
