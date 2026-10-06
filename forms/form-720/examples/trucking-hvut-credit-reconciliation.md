# Example — Trucking Company: HVUT Credit Routing and the 6-Month Parts Tax on Form 720

A small trucking company asks the agent to "claim its HVUT credit on Form 720 Schedule C" for two tractors it lost during the 2025–2026 HVUT period. The agent finds that HVUT credits are not a Form 720 item and routes them to Form 2290 / Form 8849. While collecting facts, it finds one real Form 720 liability: the 12% tax on parts and accessories installed on a new tractor within 6 months of placing it in service (IRS No. 33).

**Verified against:** Form 720 (Rev. June 2026) and instructions (Rev. June 2026), Instructions for Form 2290 (Rev. July 2026) "Line 5" and Partial-Period Tax Tables, Pub. 510 (Rev. Dec. 2025) ch. 6, IRC §§4051, 4481, on 2026-10-06. Math checked in Python.

---

## Taxpayer facts

- **Entity**: Ridgeline Hauling, LLC (S-corp election, EIN 33-9876543)
- **Fleet**: 8 tractors at July 1, 2025, all in HVUT category V (taxable gross weight over 75,000 lb)
- **HVUT period**: July 1, 2025 – June 30, 2026
- **Form 2290**: filed August 25, 2025 for all 8 tractors, first used in July 2025; $550 per vehicle, $4,400 total
- **Mid-period events**:
  - **November 12, 2025**: Tractor #3 destroyed in a collision (insurance total loss; not economical to rebuild)
  - **February 8, 2026**: Tractor #7 sold to an unrelated buyer
- **New tractor #9**: bought from a dealer and placed in service (delivery ticket signed) on **January 14, 2026**. The dealer reported the 12% retail tax on the tractor sale on its own Form 720.
- **Shop work on tractor #9 on February 23, 2026** (invoice from an independent shop):
  - Upgraded fifth wheel slider assembly (an addition, not a replacement): parts $1,640, installation $385
  - Auxiliary power unit that heats and cools the sleeper without the main engine: $10,450 installed. The user supplied documentation that the unit is an idling reduction device as defined in i720 "Retail Tax" (affixed to the tractor and determined by the EPA to reduce idling).
- **Other excise liabilities**: none. Ridgeline has never filed Form 720.

The CFO asks in March 2026, while closing Q1.

---

## Step 1 — HVUT credits are not a Form 720 item

Form 720 Schedule C (lines 1–15) has no Heavy Highway Vehicle Use Tax line, and IRS No. or CRN "365" doesn't exist on the June 2026 form. HVUT credits for a vehicle destroyed, stolen, or sold before June 1 and not used for the rest of the period are claimed on the **next Form 2290 filed (line 5)** or as a refund on **Form 8849 Schedule 6** (Instructions for Form 2290, Rev. July 2026, "Line 5" and "When to make a claim"). The amount on Form 2290 line 5 can't exceed that return's line 4 tax; any excess goes on Form 8849 Schedule 6.

The agent hands this part to the [`form-2290`](../../form-2290/SKILL.md) skill and records a cross-check of the expected credit:

| Tractor | Event | Months of use (first use July 2025 through the event month) | Partial-period tax, category V (i2290 Partial-Period Tax Table) | Credit = $550 − partial-period tax |
|---------|-------|-----|------|------|
| #3 | Destroyed Nov 12, 2025 | 5 (Jul–Nov) | $229.17 | $320.83 |
| #7 | Sold Feb 8, 2026 | 8 (Jul–Feb) | $366.67 | $183.33 |
| | | | **Total** | **$504.16** |

The month of the event counts as a month of use (i2290 "Figuring the credit": count "to the last day of the month in which it was destroyed, stolen, or sold"). For the sold tractor, the claim must include the purchaser's name and address. The new tractor #9 also needs its own Form 2290 for first use in January 2026; that too belongs to the form-2290 skill.

---

## Step 2 — The real Form 720 liability: parts installed within 6 months (IRS No. 33)

IRC §4051(b) imposes a 12% tax on the price of a part or accessory and its installation when the owner, lessee, or operator of a taxable vehicle installs it within 6 months after the vehicle was first placed in service. Exceptions: replacement parts, and an aggregate price (including installation) of $1,000 or less for the vehicle during the 6-month period (§4051(b)(2); Pub. 510 ch. 6 "Separate purchase"). Idling reduction devices are exempt from this tax (i720 "Retail Tax").

| Item | Price incl. installation | Taxable? |
|------|--------------------------|----------|
| Fifth wheel slider upgrade (addition) | $1,640 + $385 = $2,025 | Yes: not a replacement; installed Feb 23, within 6 months of Jan 14 |
| Auxiliary power unit (idling reduction device) | $10,450 | No: exempt idling reduction device |

Taxable parts for tractor #9 so far total $2,025, which is over $1,000, so the tax applies:

```
Tax = 12% × $2,025 = $243.00
```

Ridgeline is the owner and primarily liable; the installing shop is secondarily liable (§4051(b)(3)). Any further non-replacement parts installed on tractor #9 before July 14, 2026 are also taxable and are reported in the quarter of installation.

### Deposits and Schedule A

IRS No. 33 is a Part I tax, so Schedule A is required. Ridgeline's Part I net liability for Q1 2026 is $243.00, which doesn't exceed $2,500, so no semimonthly deposit is required; the tax is paid with the return (i720 "Payment of Taxes"). The liability arose on February 23 (second month, 16th–last day): **box D**.

---

## Form 720 — Q1 2026

| Line | Field | Value |
|------|-------|-------|
| Quarter ending | | March 2026 |
| Filer name | | Ridgeline Hauling, LLC |
| EIN | | 33-9876543 |
| IRS No. 33 — Retail tax, truck, trailer, semitrailer chassis and bodies, tractor | Tax (12% × $2,025) | $243.00 |
| Part I line 1 | | $243.00 |
| Part II line 2 | | $0 |
| Schedule A, line 1, box D (February 16–28) | | $243.00 |
| Schedule A, line 1(b) | | $243.00 |
| Schedule C | | Not used (no Form 720 claims; HVUT credits go on Form 2290 / 8849) |
| Part III line 3 | Total tax | $243.00 |
| Lines 4–9 | | $0 |
| Line 10 | Balance due | $243.00 |
| Final return box | | ASK: check it only if Ridgeline expects no further Form 720 liability (e.g., no more non-replacement parts on tractor #9 before July 14, 2026, and no other new tractors) |

Due date: April 30, 2026 (Thursday).

---

## Documentation required

### Form 720 (IRS No. 33)

- Dealer delivery ticket for tractor #9 showing the January 14, 2026 placed-in-service date
- Shop invoice dated February 23, 2026 separating each part, its price, and installation charges
- Support that the fifth wheel slider was an addition, not a replacement
- EPA documentation for the idling reduction device
- Running log of non-replacement parts installed on tractor #9 through July 14, 2026

### Form 2290 / Form 8849 (handled by the form-2290 skill)

- Police report and insurance total-loss letter for tractor #3
- Bill of sale and title transfer for tractor #7, with the buyer's name and address
- VINs, taxable gross weight category, event dates, and the credit worksheet for each vehicle
- The stamped Schedule 1 from the August 25, 2025 Form 2290

---

## Filing channel

Ridgeline files the Q1 2026 Form 720 by **April 30, 2026**, either by e-file through a provider on https://www.irs.gov/e-file-providers/720-mef-providers (optional) or on paper to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0009. Payment: $243.00 by EFTPS, Direct Pay, electronic funds withdrawal with an e-filed return, or check with Form 720-V.

---

## Common errors avoided

1. **Claiming HVUT on Form 720 Schedule C**: there is no HVUT line. Use Form 2290 line 5 or Form 8849 Schedule 6.
2. **Wrong proration**: the event month counts as a month of use; counting it as "remaining" overstates the credit.
3. **Missing the §4051(b) tax**: owners who add parts to a new heavy tractor or trailer within 6 months owe 12% once the aggregate exceeds $1,000, even though the dealer already paid the retail tax on the vehicle.
4. **Taxing the idling reduction device**: qualifying idling reduction devices are exempt; get the EPA documentation.
5. **Skipping Schedule A because the amount is small**: Schedule A is required for any Part I liability, even under $2,500.
6. **Forgetting future quarters**: having filed for Q1, Ridgeline must keep filing quarterly until it files a final return (i720 "Who Must File"). ASK before checking the final return box.
7. **Assuming the tax continues forever**: the §4051 retail tax terminates on October 1, 2028 (§4051(c)).

---

## Output for the user

The agent delivers to Ridgeline:

1. **Q1 2026 Form 720 draft**: IRS No. 33 $243.00, Schedule A box D $243.00, balance due $243.00, due April 30, 2026
2. **Routing note**: HVUT credits (expected $504.16 total) belong on Form 2290 line 5 or Form 8849 Schedule 6; hand off to the form-2290 skill, which also covers tractor #9's own Form 2290 for January 2026 first use
3. **Parts log**: non-replacement parts on tractor #9 through July 14, 2026
4. **Question for the user**: will there be any more Form 720 liability (final return box)?
