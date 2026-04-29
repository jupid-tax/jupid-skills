# Coordinating Form 1116 with Form 2555

US citizens and resident aliens working abroad have two main mechanisms for relieving double taxation:

- **Form 2555 — Foreign Earned Income Exclusion (FEIE)**: exclude up to $130,000 (2025; 2026 figure announced fall 2025) of foreign earned income from US tax
- **Form 1116 — Foreign Tax Credit (FTC)**: credit foreign income tax paid (dollar-for-dollar reduction of US tax)

They are NOT mutually exclusive — but they cannot apply to the same dollar of income.

## Decision framework: which to use

The filer typically picks one PRIMARY mechanism. Coordination matters when the filer has multiple income types.

### Use Form 2555 (FEIE) when:

- Foreign earned income (wages, SE income) is below or near the $130,000 cap
- The foreign country has a low income tax rate (e.g., UAE = 0%, Hong Kong territorial system, Singapore tier rates)
- The filer qualifies under the bona fide residence or physical presence test
- There's no significant unused FTC carryforward to use

If foreign tax is low, FEIE is usually better — it eliminates US tax entirely on the excluded income. FTC would only credit a small foreign tax against larger US tax, leaving residual US tax owed.

### Use Form 1116 (FTC) when:

- Foreign country has a high income tax rate (Germany ~42%, France progressive to 45%, UK 40%+)
- Foreign earned income exceeds the $130,000 FEIE cap (the excess needs FTC anyway)
- The filer has substantial passive income (dividends, interest) — FEIE doesn't apply to passive at all
- The filer has unused FTC carryforward they want to use up
- The filer wants to keep IRA / Roth contribution room (FEIE removes the income from the "compensation" basis, but FTC doesn't)

### Use both (coordination):

- Foreign earned income above $130,000 → FEIE the first $130K, FTC the excess
- Foreign earned income (FEIE) + foreign passive income (FTC general approach: FTC the passive)
- Foreign earned income with a housing exclusion (Form 2555 Part VI) plus foreign tax on residual income (Form 1116)

## The "no double dip" rule

A filer cannot claim both:
- FEIE (excluding income) AND
- FTC (crediting tax) on **the same dollar of income**

When using both, the foreign tax allocable to the **excluded** portion of income is NOT creditable on Form 1116. Only foreign tax on the **non-excluded** portion is creditable.

### Mechanic — allocating foreign tax when both are used

Allocation formula (Pub 514 / Reg. §1.911-6):

```
FTC-eligible foreign tax = Total foreign tax × (Non-excluded foreign earned income / Total foreign earned income)
```

**Worked example**: Filer earns $180,000 in Germany, pays $58,000 in German tax.

- FEIE excludes $130,000 (2025 cap)
- Non-excluded portion: $180,000 − $130,000 = $50,000
- Allocation ratio: $50,000 / $180,000 = 0.2778
- FTC-eligible German tax: $58,000 × 0.2778 = $16,111
- The remaining $41,889 of German tax is NOT creditable (allocable to the excluded $130,000)

The excluded income is gone from US tax (zero US tax on it), so there's no US tax to credit against. The non-excluded $50,000 has US tax owed, and the $16,111 of FTC offsets it.

### Mechanic — Form 1116 Line 1a when FEIE is used

On Form 1116 Line 1a (gross foreign-source income), include ONLY the non-excluded foreign earned income — not the excluded portion. The excluded portion never appears on Form 1116.

Example continued: on Form 1116 (general basket), Line 1a = $50,000, NOT $180,000.

## The FEIE election is binding (with cost to revoke)

Once a filer elects FEIE on Form 2555, the election applies to all subsequent years until revoked. To revoke:

- File a return for the year of revocation without claiming FEIE
- Once revoked, the filer cannot re-elect FEIE for **5 years** without IRS consent (Form 3115 or letter ruling)

**Why this matters**: a filer in a high-tax country (Germany) using FTC may be tempted to "switch back" to FEIE if they move to a low-tax country (UAE). The 5-year wait is real. Plan ahead.

## Decision tree

```
Is foreign earned income > $0?
├── No → Use Form 1116 only (passive income, etc.)
└── Yes
    ├── Is foreign tax rate > US effective rate?
    │   ├── Yes → Form 1116 (FTC fully offsets US tax; FEIE wastes the excess foreign tax)
    │   └── No
    │       ├── Is foreign earned income ≤ FEIE cap?
    │       │   ├── Yes → Form 2555 (FEIE) likely better
    │       │   └── No
    │       │       └── Use BOTH: FEIE first $130K, FTC for excess + passive
    │       └── (passive income only)
    │           └── Use Form 1116 only (FEIE doesn't apply to passive)
    └── (also has passive foreign income)
        └── Form 1116 for passive (separate basket) regardless of FEIE choice for earned
```

## Side-by-side comparison: Germany expat earning $120K wages, $45K German tax

### Option A: Form 2555 (FEIE) only

- $120,000 < $130,000 cap → entire $120K excluded
- US tax on $120K wages = $0
- German tax = $45,000 (paid to Germany; not recoverable from US)
- US tax on remaining income (e.g., $5K US-source interest) computed normally
- **Net out-of-pocket: $45,000 to Germany, $0 (or close to $0) to US**
- IRA contribution: BLOCKED on the excluded $120K (no compensation for IRA purposes)
- Standard deduction: still applies

### Option B: Form 1116 (FTC) only

- $120,000 fully taxable in US (general basket)
- Tentative US tax on $120K wages (single, std deduction $14,600 for 2024) ≈ $20,000
- German tax = $45,000
- §904 limitation: foreign-source taxable income / total taxable income × US tax. If all income is foreign, fraction ≈ 1.0; limitation ≈ $20,000
- FTC = lesser of $45,000 or $20,000 = $20,000
- Unused FTC: $25,000 carries back 1 year, forward 10 years
- US tax on $120K = $0 (after FTC)
- **Net out-of-pocket: $45,000 to Germany, $0 to US, plus $25K carryforward as future-year asset**
- IRA contribution: ALLOWED ($120K is compensation)

For this scenario: **Option B (FTC) is better**. Same net cash result, but the filer keeps IRA contribution eligibility and accumulates carryforward.

### Option C: Low-tax country (UAE) expat earning $120K wages, $0 UAE tax

- FEIE: $120K excluded, US tax on wages = $0
- FTC: no foreign tax to credit. US tax on wages = ~$20,000 (regular rates).
- **FEIE wins decisively** in zero-tax countries.

## What the agent should do

When the filer has foreign earned income and asks about credit OR exclusion:

1. **Ask** about the foreign country's tax rate on their wages (or the actual tax paid)
2. **Compute** Option A (FEIE only), Option B (FTC only), and Option C (both, if income > FEIE cap)
3. **Surface** the differential — both the current-year tax and the value of unused FTC carryforward (if any)
4. **Note** the IRA contribution implication if relevant
5. **Note** that the FEIE election, once made, has a 5-year wait to re-elect after revocation

The default heuristic: high-tax country → FTC; low-tax country → FEIE; mixed → both.

## When to escalate to CPA

- Filer is changing residence mid-year (qualification tests get tricky)
- Filer has both a US-located rental property AND foreign earned income (passive activity rules)
- Filer has GILTI inclusion or PFIC investments
- Filer is dual-resident under treaty tie-breaker
- Filer's spouse is a non-resident alien (Section 6013(g) election interacts)
- Filer's foreign earned income is mostly or entirely SE income with self-employment tax implications (Totalization Agreement matters)
