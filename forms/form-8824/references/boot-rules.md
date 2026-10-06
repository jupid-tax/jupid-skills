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

If the liabilities the other party assumes (debt on the relinquished property) exceed what the user puts in on the other side, the **net relief** is mortgage boot received. Per the 2025 Form 8824 instructions, Line 15, the user's offsets are liabilities the user assumed, cash the user paid, and the FMV of other property the user gave up:

```
Mortgage boot received = max(0, liabilities assumed by other party
                               − liabilities assumed by user
                               − cash paid by user
                               − FMV of other property given up by user)
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
| Non-like-kind property given | Offsets cash boot received? **No** | Its own gain or loss is a separate sale (Line 12-14) |
| Non-like-kind property given | Offsets mortgage boot received? **Yes** | Its FMV reduces net liabilities assumed by the other party (Line 15 instructions) |

The cleanest mental model: **netting works for mortgage relief, not for cash**. Cash boot received goes into Line 15 fully; mortgage boot is netted before Line 15.

### Practical formula for Line 15

```
Line 15 = Cash received
        + FMV of non-like-kind property received
        + max(0, debt relieved − debt assumed − cash paid
                 − FMV of other property given)    [net liabilities assumed by other party]
        − ALL exchange expenses
        (floor at $0; never below zero)
```

Cash paid sits inside the max(), so it can only cancel mortgage relief, never cash received. Exchange expenses that cannot be used because Line 15 hits $0 go on Line 18, as does the net amount paid (2025 instructions, Lines 15 and 18).

---

## Exchange expenses

Costs of the exchange reduce boot received first; whatever cannot be used there increases the basis side.

Per the 2025 Form 8824 instructions (Lines 15 and 18) and Pub. 544 ("The limit of recognized gain"):
- **All exchange expenses**, however paid → reduce Line 15 (boot received), but not below zero
- **The unused remainder** → add to Line 18 (give side, increasing basis)

The agent should ask the user for every closing cost on both closing statements, then sort them into exchange expenses and other items (below). How they were paid does not change the line they go on.

### What counts as an exchange expense

Pub. 544 (2025), "Exchange expenses": closing costs paid on the disposition of the property given up, such as brokerage commissions, attorney fees, and deed preparation fees, and closing costs paid on the acquisition of the replacement property. In practice this covers:
- Real estate broker commissions
- QI fees
- Escrow / closing fees
- Recording fees and transfer taxes
- Attorney and deed preparation fees

Not exchange expenses:
- Property taxes, rent prorations, security deposits, and repairs shown on the closing statement (Pub. 544)
- Loan costs on the replacement (points, origination fees, lender-required appraisal, mortgage insurance) → capitalized as costs of getting a loan and deducted over the loan term, not added to property basis (Pub. 551, "Settlement costs")
- Property repairs or improvements pre-sale → adjust basis of relinquished

---

## Worked examples

### Example 1: Cash boot only

User receives $50,000 cash; no debt relief.

- Cash received: $50,000
- Exchange expenses: $5,000
- Line 15 = 50,000 − 5,000 = **$45,000**

If realized gain (Line 19) ≥ $45,000, recognized gain (Line 23) = $45,000.

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

- Net liabilities assumed by other party: max(0, 200,000 − 250,000 − 40,000) = $0 (user assumed more debt)
- Cash received: $50,000
- Cash paid: $40,000
- Cash paid does NOT offset cash received (rule above)
- Line 15 = 50,000 + 0 + 0 (cash paid does not offset cash received) = **$50,000**
- Line 18 (your "give" side) includes: basis given up + net amount paid of (250,000 + 40,000) − 200,000 = $90,000

### Example 5: Mortgage boot received, cash paid to offset

User had $200k mortgage on relinquished, $0 mortgage on replacement (paid all cash). User paid $50k cash at replacement closing.

- Liabilities assumed by other party: $200,000
- Cash paid: $50,000 → **offsets mortgage boot** per the offset rules
- Line 15 = max(0, 200,000 − 0 − 50,000) = **$150,000**

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

Ordinary recapture goes on Line 21 and the rest of the recognized gain on Line 22; Line 23 is their total. Line 21 can exceed the boot-attributable gain on Line 20 when §1245 property is given up for §1250 property (IRC §1245(b)(4)). Within Line 22, gain on a depreciated building is unrecaptured §1250 gain up to the straight-line depreciation taken (IRC §1(h)(6)).

---

## Validation

Before finalizing Line 15:

- [ ] Cash received correctly identified (excluding amounts that flow to QI for replacement purchase)
- [ ] Mortgage boot computed as max(0, debt relieved − debt assumed − cash paid − FMV of other property given) — net, not gross
- [ ] All exchange expenses reduce Line 15 (not below zero); only the unused remainder is on Line 18
- [ ] If non-like-kind property received, FMV included in Line 15 and described on Line 15a; its basis is its FMV. (Lines 12-13 are for non-like-kind property GIVEN UP.)
- [ ] If cash paid offsets mortgage boot received, applied correctly per offset matrix
- [ ] Line 15 is ≥ 0 (floor at zero; if negative computation, "boot paid" instead)

---

## Sources

- IRC §1031(b) — gain recognized to extent of boot
- IRC §1031(d) — basis of replacement property
- Treas. Reg. §1.1031(b)-1, §1.1031(d)-1, §1.1031(d)-2 — boot characterization, basis computation
- 2025 Instructions for Form 8824, Lines 15, 15a, 18, and the Taylor/Finley example under "Figuring amounts for lines 15 through 20"
- Pub. 544 (2025) (Sales and Other Dispositions of Assets), Chapter 1 — "Exchange expenses", "Partially Nontaxable Exchanges"
- Pub. 551 (Rev. December 2025), "Settlement costs" — loan costs are not basis
