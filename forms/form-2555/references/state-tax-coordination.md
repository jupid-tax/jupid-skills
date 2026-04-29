# Form 2555 — State Tax Coordination

The Foreign Earned Income Exclusion (FEIE) is a **federal** tax benefit under IRC §911. It reduces federal taxable income on Form 1040 via a Schedule 1 negative adjustment. Most states **decouple** from §911 either fully or partially, meaning the excluded income reappears on the state return.

This is the single most-overlooked item in expat tax planning. A filer who saves $20,000 on federal tax via FEIE may still owe $8,000+ to California on the same income. Always check state treatment before treating FEIE as a complete answer.

---

## The general framework

States fall into three buckets:

1. **Conformity states** — start state taxable income from federal AGI or federal taxable income. Because FEIE reduces federal AGI on Schedule 1, these states effectively honor FEIE without a state-level add-back.
2. **Decoupled / add-back states** — start from federal AGI but add back the FEIE amount on the state return. The income is fully state-taxable.
3. **No state income tax** — Alaska, Florida, Nevada, New Hampshire (interest/dividends only post-2025), South Dakota, Tennessee, Texas, Washington, Wyoming. FEIE coordination is moot for residents.

The bucket a state falls into depends on how its tax base is computed (AGI conformity, taxable income conformity, separate calculation) and any state-specific decoupling statute.

---

## California — does NOT honor FEIE

California is the most-cited example because it's where many digital nomads and tech expats remain "domiciled" while abroad.

**Mechanic**: California computes state taxable income on a **separate** basis (Form 540 starts from federal AGI but applies California adjustments). Schedule CA (540) Part I, Section A, Line 1h **adds back** the FEIE amount excluded on federal Schedule 1.

**Result**: California taxes worldwide income for residents, including income excluded under FEIE for federal purposes. A California resident excluding $130,000 under FEIE federally still reports the full $130,000 on Form 540 and pays California tax (up to 13.3% top rate, 9.3% on income in the $70K-$375K range for single filers — verify current brackets).

**Citation**: California Rev. & Tax. Code §17024.5(b)(1) provides general IRC conformity but explicitly does **not** conform to §911. FTB Pub. 1031 (Guidelines for Determining Resident Status) and FTB Pub. 1100 (Taxation of Nonresidents and Individuals Who Change Residency) confirm this.

### How to escape California taxation while abroad

The only way for a Californian abroad to stop owing California tax on worldwide income is to **change domicile** away from California. This is a facts-and-circumstances test (FTB calls it the "closest connections" test) involving:

- Selling or renting out California home long-term
- Surrendering California driver's license; getting one in new state/country
- Registering vehicles elsewhere
- Moving bank accounts, voter registration, professional licenses
- Filing as a nonresident or part-year resident on Form 540NR for the year of departure
- Spending less time in California than in the new domicile
- Having intent to remain elsewhere indefinitely

Until domicile changes, California treats the filer as a resident subject to tax on all income. The 546-day "safe harbor" (RTC §17014(d)) provides that an individual outside California under an employment contract for at least 546 consecutive days is treated as a nonresident — but this requires meeting strict conditions (no more than 45 days in California per year during the period, intangibles income < $200K), and the FTB scrutinizes safe-harbor claims.

---

## Other notable decoupled states

| State | Treatment | Notes |
|-------|-----------|-------|
| **California** | Decouples — full add-back of FEIE | RTC §17024.5; Schedule CA add-back |
| **Pennsylvania** | Decouples — PA has its own taxable-income calculation; foreign wages taxable to PA residents | PA does not start from federal AGI |
| **New Jersey** | Decouples — NJ has its own gross income calculation; foreign wages taxable | NJ-1040 starts from NJ-defined gross income, not federal AGI |
| **Alabama** | Decouples — AL has its own gross income; FEIE not honored | Al. Code §40-18-14 |
| **Arkansas** | Decouples — AR-specific calculation | Verify current Arkansas instructions |
| **Mississippi** | Decouples — MS taxes residents on worldwide income | MS-specific calculation |
| **Hawaii** | Partial conformity — verify against current HRS §235 | Hawaii has updated conformity dates |

States that are **AGI-conformity** (start from federal AGI without add-back) generally honor FEIE because the exclusion already happened at the AGI level. Examples: New York (mostly), Illinois, Massachusetts, Virginia, Maryland, Colorado, Georgia. **Always verify against the current state instructions** — states change conformity rules in their annual budget bills.

---

## Massachusetts — partial trap

Massachusetts conforms to federal AGI as a starting point, but Massachusetts has its own definition of Massachusetts gross income under M.G.L. c. 62 §2. For tax years where Massachusetts has updated its IRC conformity date past §911, the FEIE flows through. For older years or specific decouplings, an add-back may apply. Verify with current DOR Form 1 instructions — Massachusetts is the state most likely to surprise filers due to lagging conformity.

---

## New York — generally honors FEIE for residents abroad

New York starts from federal AGI on Form IT-201 / IT-203, and there is no §911 add-back. A New York State resident abroad excludes FEIE on the federal return; that exclusion flows through to New York taxable income.

**However**: New York City and Yonkers residents are taxed separately, and New York applies a strict **domicile** test similar to California. A New Yorker who keeps a New York apartment, has family in New York, or maintains "permanent place of abode" in New York may still be a NY resident for tax purposes despite being abroad — and would owe NY tax on the residual non-excluded income (passive, US-source) at NY rates. Truly leaving New York requires changing domicile.

---

## Nonresident state filing for expats with US ties

An expat may have moved abroad but still have US-source income or US ties that trigger nonresident state filing:

- Rental property in California → California nonresident return (Form 540NR) on the rental income
- Consulting work performed in client's New York office during US business trip → NY nonresident filing on the NY-source wages
- US LLC pass-through income sourced to a state → nonresident filing in that state
- W-2 from US employer for work performed in the US (e.g., 30 days in office) → state nonresident filing for those wages

FEIE doesn't apply to these because the income wasn't earned IN a foreign country — even though the filer's tax home was abroad, the services were physically performed in the US. The "foreign-earned" requirement is about WHERE services were performed, not where the worker is domiciled.

---

## Impact on state estimated tax

Expats often forget state estimated tax. Mechanics:

- **Resident states** (where filer is still domiciled): if FEIE is fully honored federally but state decouples, state estimated tax may be substantial. Pay quarterly via state vouchers (e.g., California Form 540-ES).
- **Nonresident state filings**: estimated tax may be required if state-source income exceeds the state's threshold (varies — typically $1,000+ in tax owed).
- **Withholding from US employer**: if a US employer continues to withhold California state tax on wages paid to an employee abroad, the withholding may be excessive (if the employee has changed domicile). File state return claiming refund; update employer's W-4-equivalent state form.

The agent should ask about state of domicile before declaring an FEIE plan complete. State tax can wipe out half the federal savings.

---

## Decision tree

```
Filer's state of domicile?
  ├── No state income tax (AK, FL, NV, NH, SD, TN, TX, WA, WY)
  │   → No state coordination needed
  ├── California
  │   → FEIE NOT honored. Add back full FEIE on Schedule CA (540) or 540NR.
  │   → Consider domicile change if abroad long-term.
  ├── Pennsylvania, New Jersey, Alabama, Arkansas, Mississippi
  │   → FEIE NOT honored (state has separate income calculation).
  │   → Foreign wages taxable to state residents.
  ├── Massachusetts
  │   → Verify against current year's IRC conformity date.
  │   → Likely partial honor; check Form 1 instructions.
  └── Most other states (NY, IL, VA, MD, GA, CO, etc.)
      → FEIE generally honored via AGI conformity.
      → Verify no state-specific add-back was added in current year's budget.
```

For any state classified as "verify," load the current state's resident return instructions and search for "§911", "foreign earned income", or "FEIE" in the adjustment schedule.

---

## Citations

- IRC §911 — Foreign earned income exclusion (federal)
- California Rev. & Tax. Code §17024.5(b)(1) — California's selective IRC conformity, excluding §911
- FTB Pub. 1031 — Guidelines for Determining Resident Status
- FTB Pub. 1100 — Taxation of Nonresidents and Individuals Who Change Residency
- M.G.L. c. 62 §2 — Massachusetts gross income definition
- N.Y. Tax Law §612 — New York adjusted gross income (starts from federal AGI)
- Pub. 54 — IRS Tax Guide for U.S. Citizens and Resident Aliens Abroad (federal context only; does not address state)
- Each state's current resident and nonresident return instructions (re-verify annually — states change conformity dates in budget bills)
