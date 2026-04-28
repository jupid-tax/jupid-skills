# §1245 Recapture — Personal Property

§1245 property is depreciable personal property — equipment, vehicles, machinery, computers, furniture, livestock other than real-estate-fixed structures, and most amortizable intangibles. When you dispose of §1245 property at a gain, the depreciation portion comes back as **fully ordinary income** (no 25% cap, no LTCG rate).

This is asymmetric: you got ordinary deductions while you depreciated, and you give back ordinary income at sale. The "preference" for business owners is the timing — deducting now, paying tax later — not a rate difference.

---

## What is §1245 property?

IRC §1245(a)(3) defines §1245 property as:

- **Tangible personal property** — equipment, vehicles, machinery, livestock, furniture
- **Other tangible property** used as an integral part of manufacturing, production, extraction, or furnishing transportation, communications, electricity, gas, water, sewage services, or research/storage facilities — including buildings or structural components if the building's use is integral to one of those activities
- **Real property with a class life ≤ 15 years** — e.g., land improvements like fences, parking lots, signs (15-year MACRS land improvements ARE §1245 property)
- **Single-purpose agricultural / horticultural structures**
- **Storage facilities used for distribution of petroleum or its primary products**
- **Amortizable §197 intangibles** — goodwill, going-concern value, customer lists, etc.

What is NOT §1245 property: residential rental real estate, commercial buildings, raw land. Those are §1250 property (or non-depreciable).

---

## The §1245 recapture formula

```
§1245 recapture = lesser of:
  (a) Realized gain (Sales price − Adjusted basis)
  (b) Depreciation allowed or allowable (cumulative)

Residual §1231 gain = Realized gain − §1245 recapture
```

Three scenarios illustrate this:

### Scenario 1: Gain is less than depreciation taken (most common for vehicles/equipment)

```
Original cost:           $50,000
Accumulated dep:         $40,000
Adjusted basis:          $10,000
Sales price:             $35,000
Realized gain:           $25,000

§1245 recapture = min($25,000, $40,000) = $25,000  ← all ordinary
§1231 gain      = $25,000 − $25,000 = $0
```

The entire gain is ordinary income because the gain is less than depreciation taken. This is the typical outcome for a depreciating asset sold below original cost.

### Scenario 2: Gain exceeds depreciation taken (asset appreciated above original cost)

```
Original cost:           $30,000
Accumulated dep:         $20,000
Adjusted basis:          $10,000
Sales price:             $50,000
Realized gain:           $40,000

§1245 recapture = min($40,000, $20,000) = $20,000  ← ordinary
§1231 gain      = $40,000 − $20,000 = $20,000     ← LT capital gain
```

The depreciation portion ($20,000) is ordinary; the appreciation portion ($20,000) above original cost gets §1231 treatment (LTCG if there's a net §1231 gain after Part I netting).

### Scenario 3: Loss

```
Original cost:           $30,000
Accumulated dep:         $5,000
Adjusted basis:          $25,000
Sales price:             $20,000
Realized loss:          ($5,000)

§1245 recapture = $0 (no gain)
§1231 loss      = ($5,000)  ← ordinary loss via Part I → Part II Line 11
```

A loss never triggers §1245 recapture. The loss is §1231, which becomes ordinary if Part I nets to a loss for the year.

---

## §179 interaction

Section 179 is treated as depreciation for §1245 recapture purposes. So:

- A §179 deduction in the year of purchase counts toward Line 22 / Line 25a depreciation
- Bonus depreciation (§168(k)) also counts
- "Allowed or allowable" applies

If you took a $40,000 §179 deduction on a $40,000 truck (100% expensed in year 1), your accumulated depreciation is $40,000, your adjusted basis is $0, and ANY sale price is fully ordinary §1245 recapture.

---

## §280F listed property

If the §1245 asset is "listed property" under §280F (passenger autos, certain trucks, computers used outside an office, certain telecommunications equipment), additional rules apply:

- Annual depreciation is capped (e.g., 2024 first-year cap on passenger autos: $20,400 with bonus, $12,400 without)
- If business use drops ≤50% in a year before recovery period ends → Part IV recapture even without sale
- §179 cannot be claimed on assets used 50% or less for business

---

## Cost segregation interaction

If a real estate owner did a **cost segregation study** to accelerate depreciation by reclassifying components of a building into 5-, 7-, or 15-year MACRS lives (instead of 27.5- or 39-year real property life), those reclassified components become §1245 property.

At sale:
- Real property components remaining as §1250 → §1250 treatment (typically 25% cap on depreciation portion)
- Cost-segregated 5/7/15-year components → §1245 treatment (full ordinary recapture)

This is a critical complication — a $2M building sale where $400K was cost-segregated produces meaningfully different tax than $2M without cost segregation. The agent should ALWAYS ask if cost segregation was done before treating a building as pure §1250.

---

## Goodwill and §197 intangibles

§197 intangibles (purchased goodwill, going-concern value, workforce in place, customer lists, licenses, covenants not to compete) are §1245 property. When sold:

- Amortization taken (15-year straight-line under §197) is recaptured as ordinary
- Residual gain is §1231

Self-created goodwill (built up over years of operating the business) is generally NOT amortizable and NOT §197 intangible. Sale of self-created goodwill is generally a §1231 gain (no recapture, since no amortization was taken). Form 8594 allocation determines how proceeds split across asset classes in a business sale.

---

## Common §1245 traps

1. **Forgot the §179 in basis.** Filer took §179 in year 1, then computed gain at sale assuming basis = original cost. Wrong: basis = $0 after §179, so the entire sales price is gain.

2. **Assumed a "trade-in" defers gain.** Pre-2018 §1031 like-kind exchange could defer gain on equipment trade-ins. Post-TCJA, §1031 is real-estate only — equipment trade-ins are taxable §1245 dispositions in full.

3. **Ignored business-use percentage at disposition.** A truck that was 100% business in year 1 but dropped to 60% in years 2-4 has different §1245 recapture math (and may also trigger Part IV §280F recapture in the year of the drop).

4. **Treated §197 goodwill amortization as non-recapturable.** Filer sold their consulting practice including purchased goodwill — and forgot that the amortization on the purchased goodwill recaptures as §1245 ordinary income at sale.
