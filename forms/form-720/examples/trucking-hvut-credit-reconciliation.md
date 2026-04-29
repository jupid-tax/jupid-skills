# Example — Trucking Company HVUT Credit Reconciliation on Form 720 Schedule C

A small trucking company paid the Heavy Highway Vehicle Use Tax (HVUT) on Form 2290 for the full tax period, then sold and destroyed vehicles mid-period. It claims a partial-year HVUT credit on Form 720 Schedule C, IRS No. 365.

---

## Taxpayer facts

- **Entity**: Ridgeline Hauling, LLC (S-corp election, EIN 33-9876543)
- **Fleet**: 8 tractor-trailers, all over 55,000 lbs gross weight (HVUT-taxable)
- **HVUT period**: July 1, 2025 – June 30, 2026 (the standard HVUT tax period)
- **Form 2290 filing**: Filed August 25, 2025 for the full tax period
- **HVUT paid**: $4,400 total ($550 per vehicle × 8 vehicles for the full year)
- **Mid-period events**:
  - **November 12, 2025**: Vehicle #3 destroyed in I-80 collision (insurance write-off, salvage value zero)
  - **February 8, 2026**: Vehicle #7 sold to an unrelated buyer (ownership transfer registered with state DMV)
  - **No replacement vehicles** added to the fleet during the tax period

The CFO needs to recover the unused portion of HVUT for the destroyed and sold vehicles by claiming a credit on Form 720 Schedule C, IRS No. 365.

---

## When to use Form 720 Schedule C vs Form 8849

Two paths exist for HVUT recovery on partial-year vehicles:

| Path | When to use |
|------|-------------|
| **Form 720, Schedule C, IRS No. 365** | When the trucking company files Form 720 for OTHER reasons in the same period (e.g., owes other excise tax). Credit offsets that other liability. |
| **Form 8849 Schedule 6** | When the trucking company has NO other Form 720 obligation. Form 8849 is a refund claim filed standalone. |

Ridgeline does NOT have other Form 720 liabilities (no fuel-tax issues, no manufacturer's tax). For a pure refund without offset, Form 8849 is technically the cleaner path. But the user explicitly asked about Form 720 Schedule C, so this example assumes Ridgeline IS filing Form 720 for another reason — for instance, it has a small fuel-tax liability under §4081 from a tank farm operation, OR it wants to use Schedule C to apply the credit to a future excise liability.

For this scenario, assume Ridgeline files Q1 2026 Form 720 (covering Jan-Mar 2026) for an unrelated **kerosene retail tax** of $1,200 (IRS No. 105) and uses Schedule C to credit the HVUT recovery against that liability.

---

## HVUT credit computation

The HVUT credit is prorated based on the months remaining in the tax period after the disposition event. The HVUT tax period runs **July 1 to June 30**. Months are counted as the **full calendar months remaining after the disposition month**.

### Vehicle #3 (destroyed November 12, 2025)

- HVUT paid for full year: $550
- Months in tax period: 12 (July 2025 – June 2026)
- Months "used" before destruction: July, August, September, October, November = 5 months
- Months remaining (creditable): December, January, February, March, April, May, June = 7 months
- Credit = $550 × (7 / 12) = **$320.83**

Per IRS Form 2290 instructions, the disposition month itself counts toward the "used" portion (not the remaining). So November = used.

### Vehicle #7 (sold February 8, 2026)

- HVUT paid for full year: $550
- Months in tax period: 12
- Months "used" before sale: July through February = 8 months
- Months remaining: March, April, May, June = 4 months
- Credit = $550 × (4 / 12) = **$183.33**

### Total HVUT credit

```
Vehicle #3: $320.83
Vehicle #7: $183.33
Total:      $504.16
```

Round to **$504** for Form 720 reporting.

---

## Form 720 — Schedule C, IRS No. 365

Schedule C of Form 720 is the credits/claims schedule. **IRS No. 365** specifically covers HVUT credits for sold, destroyed, or stolen vehicles.

| Line | Field | Value |
|------|-------|-------|
| Schedule C, Line 5 — IRS No. 365 | Description | HVUT credit — vehicles destroyed/sold mid-period |
| | Vehicle #3 — VIN 1HGCM82633A123456 — destroyed Nov 12, 2025 — credit | $321 |
| | Vehicle #7 — VIN 1HGBH41JXMN654321 — sold Feb 8, 2026 — credit | $183 |
| | **Total Schedule C Line 5 credit** | **$504** |

---

## Form 720 — Q1 2026 full picture

| Line | Field | Value |
|------|-------|-------|
| Quarter | 1 | Q1 2026 |
| Filer name | | Ridgeline Hauling, LLC |
| EIN | | 33-9876543 |
| Part I — IRS No. 105 (kerosene) | Tax | $1,200 |
| Schedule C — IRS No. 365 (HVUT credit) | Credit | $504 |
| Part III — net balance due | | $1,200 − $504 = **$696** |

---

## Documentation required (Schedule C support)

For each HVUT credit claim under IRS No. 365, the following must accompany Form 720 (or be retained for IRS request):

### Vehicle #3 — destroyed

- Police accident report (I-80 collision, November 12, 2025)
- Insurance settlement document showing total loss / write-off
- Salvage disposition record (or statement of zero salvage)
- Original Form 2290 Schedule 1 stamped copy showing the vehicle's VIN and HVUT paid
- Calculation worksheet showing months remaining and credit math

### Vehicle #7 — sold

- Bill of sale to the unrelated buyer
- State DMV title transfer record showing date of transfer
- Buyer's name, address, and (if known) EIN — required because the IRS may pursue the buyer for any HVUT going forward (the buyer typically files a new Form 2290 for the remaining period)
- Original Form 2290 Schedule 1 stamped copy
- Calculation worksheet

The agent must remind Ridgeline that the buyer of Vehicle #7 has a Form 2290 obligation starting from the month following purchase. Ridgeline can be cooperative by providing copies of the original Form 2290 and the bill of sale.

---

## Filing channel

Ridgeline files Q1 2026 Form 720 by **April 30, 2026**.

Channel: e-file via an IRS-authorized MeF provider that supports Form 720 with Schedule C. Most truck-tax-focused providers (ExpressTruckTax, J.J. Keller, TaxBandits) support combined Form 720 + Schedule C filings.

Payment: $696 owed, paid via EFTPS or check with paper Form 720.

---

## Common errors avoided

1. **Confusing Form 720 with Form 2290**: The original HVUT is reported on Form 2290 (annual). The credit for partial-year disposition is claimed on Form 720 Schedule C OR Form 8849 — never on Form 2290 itself.
2. **Wrong proration**: counting the disposition month as "remaining" instead of "used" overstates the credit. Per IRS instructions, the disposition month is counted as used.
3. **Missing VIN**: Schedule C IRS No. 365 requires the VIN of each vehicle. Without VIN, the IRS cannot match to the original Form 2290 and may deny the credit.
4. **Claiming credit before disposition documented**: the disposition (sale, destruction, theft) must be documented and dated. Without third-party evidence (bill of sale, insurance write-off, police report), the IRS may deny.
5. **Stolen vehicles — separate treatment**: stolen vehicles require a police report and proof the vehicle was not recovered. The proration is the same, but documentation differs.
6. **Pickup-truck disposition**: HVUT only applies to vehicles ≥ 55,000 lbs gross weight. Pickup-truck dispositions are not Form 2290 / Form 720 issues; they have no excise-tax credit.
7. **Filing Schedule C without other Part I or Part II liability**: if Ridgeline had ZERO other excise liability, it would use Form 8849 Schedule 6 instead. Filing a Form 720 with only a Schedule C credit (negative balance) is administratively allowed but unusual; Form 8849 is the cleaner refund path.

---

## Output for the user

The agent delivers to Ridgeline:

1. **Q1 2026 Form 720 filing summary**: kerosene tax $1,200, HVUT credit $504, net owed $696, due April 30, 2026
2. **HVUT credit worksheet**: per-vehicle proration math with VINs, disposition dates, and supporting documentation list
3. **Documentation checklist**: police report (Vehicle #3), bill of sale + DMV transfer (Vehicle #7), original Form 2290 stamps
4. **Process note**: if Ridgeline acquires replacement vehicles before June 30, 2026, they need a new Form 2290 for those vehicles (prorated for partial year)
5. **Future-quarter reminder**: track each vehicle's status on the next Form 2290 (July 2026 filing for the 2026-2027 tax period); only the 6 surviving vehicles will be on that filing
