# Form 8824 Boot Rules

"Boot" is anything received in a like-kind exchange that is **not** like-kind property. Cash, debt relief, and non-like-kind property are all boot. Boot triggers gain recognition up to the boot's value.

The cardinal rule: **gain is recognized to the extent of boot received, but never more than realized gain.**

---

## Types of boot

### Cash boot

Cash the user receives at closing (after the QI uses sale proceeds to acquire replacement and any leftover proceeds are paid to the user). Includes:
- Cash from QI after replacement acquisition
- Promissory notes received from the other party
- Securities (stocks, bonds) received

Cash boot received → recognized gain dollar-for-dollar, up to realized gain.

### Mortgage boot (debt relief)

If the user's debt on the relinquished property is greater than the user's debt on the replacement property, the **net relief** is mortgage boot received.

```
Mortgage boot received = max(0, debt on relinquished − debt on replacement)
```

Example:
- Relinquished property had $300,000 mortgage (assumed by buyer)
- Replacement property has $200,000 mortgage (user assumes)
- Net relief = $300,000 − $200,000 = $100,000 mortgage boot received

If the user assumes more debt than they were relieved of (e.g., relinquished $200k, replacement $300k), there is **no mortgage boot** — the excess assumed debt is **boot paid**, not received.

### Non-like-kind property boot

Property received that isn't real estate (or isn't held for trade/business/investment use). Examples:
- Vehicles, equipment, machinery thrown into the deal
- Inventory
- Personal-use property
- Stocks, bonds

The FMV of non-like-kind property received is boot.

Post-TCJA, this is rare in real-estate exchanges since the deal structure usually carves these out — but watch for "FF&E" (furniture, fixtures, equipment) bundled into a commercial real estate sale.

---

## The boot offset matrix

Different types of boot received and given can offset each other to varying degrees. The offset rules:

| Given by user | Offsets boot received? | Notes |
|---------------|------------------------|-------|
| Cash boot paid | Offsets cash boot received? **No** (rare situation) | Cash flows in opposite directions on the same exchange are uncommon |
| Cash boot paid | Offsets mortgage boot received? **Yes** | User pays cash to reduce mortgage relief |
| Net debt assumed (more debt on replacement than relinquished) | Offsets cash boot received? **No** | Excess debt assumed does NOT offset cash boot received |
| Net debt assumed | Offsets mortgage boot received? **N/A** | Mortgage boot received only exists when debt was relieved |
| Non-like-kind property given | Offsets cash boot received? **No** | Treated as a separate sale (Line 12-14) |

The cleanest mental model: **netting works for mortgage relief, not for cash**. Cash boot received goes into Line 15 fully; mortgage boot is netted before Line 15.

### Practical formula for Line 15

```
Line 15 = Cash received
        + FMV of non-like-kind property received
        + max(0, debt relieved − debt assumed)        [net mortgage boot]
        − Cash paid (offsets mortgage boot only)
        − Exchange expenses paid out of exchange proceeds
        (floor at $0; never below zero)
```

If the formula produces a negative, enter $0 — the excess "boot paid" instead reduces realized gain by going into Line 18 (basis-side adjustment).

---

## Exchange expenses

Costs of the exchange (QI fees, escrow fees, recording fees, transfer taxes, attorney fees specific to the exchange) reduce boot received (if paid out of boot) and increase the basis of replacement (if paid out of pocket).

Per Form 8824 instructions:
- **Exchange expenses paid out of cash received** → reduce Line 15 (boot received)
- **Exchange expenses paid out of pocket / from non-exchange funds** → add to Line 18 (give side, increasing basis)

The agent should ask the user how exchange expenses were paid.

### What counts as an exchange expense

Per IRS audit guidelines and case law:
- QI fees
- Escrow / closing fees
- Title insurance for the replacement
- Recording fees
- Transfer taxes (state stamp tax, deed tax)
- Attorney fees specific to the exchange

Not exchange expenses (these are different):
- Loan origination / financing fees on replacement → capitalized into basis of replacement separately, not netted against boot
- Property repairs or improvements pre-sale → adjust basis of relinquished
- Real estate broker commissions → reduce amount realized on relinquished

---

## Worked examples

### Example 1: Cash boot only

User receives $50,000 cash; no debt relief.

- Cash received: $50,000
- Exchange expenses paid out of boot: $5,000
- Line 15 = 50,000 − 5,000 = **$45,000**

If realized gain (Line 19) ≥ $45,000, recognized gain (Line 22) = $45,000.

### Example 2: Mortgage boot only

User had $300k mortgage on relinquished, took $200k mortgage on replacement; no cash exchanged.

- Net debt relief: 300,000 − 200,000 = $100,000
- Cash received: $0
- Line 15 = **$100,000** mortgage boot

If realized gain ≥ $100,000, recognized gain = $100,000.

### Example 3: Both cash and mortgage boot

User receives $30k cash and is relieved of $80k net mortgage relief.

- Line 15 = 30,000 + 80,000 = **$110,000**

### Example 4: Cash paid offsets mortgage boot received

User receives $50k cash. User pays $40k cash at replacement closing. User had $200k mortgage on relinquished, took $250k mortgage on replacement.

- Net debt relief: 200,000 − 250,000 = −$50,000 → $0 mortgage boot received (user assumed more debt; excess goes to Line 18)
- Cash received: $50,000
- Cash paid: $40,000
- Cash paid does NOT offset cash received (rule above)
- Line 15 = 50,000 + 0 + 0 (cash paid does not offset cash received) = **$50,000**
- Line 18 (your "give" side) includes: basis given up + $40,000 cash paid + $50,000 net debt assumed

### Example 5: Mortgage boot received, cash paid to offset

User had $200k mortgage on relinquished, $0 mortgage on replacement (paid all cash). User paid $50k cash at replacement closing.

- Net debt relief: 200,000 − 0 = $200,000 → mortgage boot received
- Cash paid: $50,000 → **offsets mortgage boot** per the offset rules
- Line 15 = 200,000 − 50,000 (cash offset) = **$150,000**

---

## Loss with boot received

If the realized loss (Line 19 negative) and the user received boot:

- **No loss is recognized** under §1031.
- The boot received is just a return of basis; it's not a recognition trigger.
- The loss is fully deferred into the basis of replacement.

This is unusual but possible when relinquished property has significantly declined in value relative to its adjusted basis.

---

## Recapture and boot

If the relinquished property had depreciation taken on it (most rentals), boot received can trigger §1245 ordinary recapture or §1250 unrecaptured gain (taxed at up to 25%) — see [`depreciation-recapture.md`](./depreciation-recapture.md).

The recapture is recognized **first** out of the boot, so the character of the recognized gain (Line 22) is mostly recapture before any preferential capital gains rate applies.

---

## Validation

Before finalizing Line 15:

- [ ] Cash received correctly identified (excluding amounts that flow to QI for replacement purchase)
- [ ] Mortgage boot computed as max(0, debt relieved − debt assumed) — net, not gross
- [ ] Exchange expenses correctly attributed: out-of-boot reduces Line 15, out-of-pocket adds to Line 18
- [ ] If non-like-kind property received, FMV included in Line 15 (and basis in Line 12-13)
- [ ] If cash paid offsets mortgage boot received, applied correctly per offset matrix
- [ ] Line 15 is ≥ 0 (floor at zero; if negative computation, "boot paid" instead)

---

## Sources

- IRC §1031(b) — gain recognized to extent of boot
- IRC §1031(d) — basis of replacement property
- Treas. Reg. §1.1031(b)-1, §1.1031(d)-1, §1.1031(d)-2 — boot characterization, basis computation
- Form 8824 instructions, current revision (Line 15 detailed worksheet)
- Pub. 544 (Sales and Other Dispositions of Assets), Chapter 1 — boot examples
