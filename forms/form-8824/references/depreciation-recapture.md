# Form 8824 Depreciation Recapture

When the relinquished property had depreciation taken on it (almost every rental), the §1031 deferral does NOT shield the recapture portion to the extent of boot received, and for §1245 property it may not shield it even without boot.

This file explains §1245 vs. §1250 and how recapture flows through Form 8824. Verified on 2026-10-06 against the 2025 Instructions for Form 8824 (Line 21 and the Taylor/Finley examples) and the 2025 Schedule D instructions.

---

## §1245 vs. §1250

### §1245 property

Depreciable personal property and certain other property listed in §1245(a)(3). A cost segregation study can put part of a building's basis into §1245 classes; some of those components are still real property for §1031 under Treas. Reg. §1.1031(a)-3 ("§1245 real property" in the Form 8824 instructions).

- Recapture under §1245 is **ordinary income** up to the lesser of:
  - All depreciation taken, OR
  - The gain
- Reported on Form 4797 Part III, then flowed to Part II

In §1031 exchanges, §1245 recapture appears on **Form 8824 Line 21**. It is the smaller of (1) the depreciation allowed or allowable (up to the Line 19 gain) or (2) the Line 20 gain **plus the FMV of non-§1245 like-kind property received** (IRC §1245(b)(4); 2025 instructions, Line 21). So when §1245 real property is exchanged for a building that is all §1250 property, the full §1245 recapture is recognized even if there is little or no boot. Pre-TCJA §1245 recapture was common (vehicles, equipment); post-TCJA it arises mainly from cost-segregated components.

Qualified improvement property (QIP) is §1250 property, not §1245; the instructions' Finley example treats QIP as "section 1250 qualified improvement property".

### §1250 property

Depreciable real property — buildings, structural components, residential and commercial real estate.

- §1250 "additional depreciation" recapture (depreciation in excess of straight-line) is ordinary income and goes on Line 21. Buildings depreciated under MACRS since 1986 use straight-line, so this arises mainly from accelerated or bonus depreciation on §1250 components such as QIP or 15-year land improvements (the Finley example: $35,000 of excess depreciation on QIP).
- In an exchange, §1250 recapture on Line 21 is the smaller of (1) the additional-depreciation ordinary income a sale would have produced or (2) the larger of the Line 20 gain or the excess of (1) over the FMV of §1250 property received (IRC §1250(d)(4); 2025 instructions, Line 21).
- **Unrecaptured §1250 gain** is the part of the gain attributable to straight-line depreciation (IRC §1(h)(6)). Taxed at a maximum federal rate of **25%** (IRC §1(h)(1)(E)).
- Figured on the Schedule D **Unrecaptured Section 1250 Gain Worksheet** (2025 Schedule D instructions, line 19).

In §1031 exchanges, unrecaptured §1250 gain on the boot-attributable portion sits inside Form 8824 Line 22, flows through Form 4797 line 5, and is split out on Schedule D as 25%-rate gain.

---

## Recapture in §1031 — the sequencing rule

Per the 2025 Form 8824 instructions (Lines 21 and 22) and IRC §1(h)(6):

When boot triggers gain recognition, the **recapture is recognized first**:

1. First, ordinary recapture on Line 21 (§1245, or §1250 additional depreciation)
2. Then the rest (Line 22); for a depreciated building, it is unrecaptured §1250 gain up to the straight-line depreciation taken
3. Anything left is regular long-term gain (taxed at 0/15/20%) if held > 1 year

Example:
- Relinquished property had $100,000 of straight-line §1250 depreciation taken
- Realized gain (Line 19) = $295,000
- Boot received = $50,000
- Recognized gain (Line 23) = $50,000 (Line 21 = $0, Line 22 = $50,000)

Of the $50,000 recognized:
- All $50,000 is unrecaptured §1250 gain (taxed at up to 25%) — because all $50,000 ≤ $100,000 of accumulated depreciation
- $0 is regular long-term capital gain at this point

The remaining $50,000 of accumulated depreciation (and $245,000 of total deferred gain) carries into the replacement property's basis, preserving the recapture potential for the next sale.

---

## Form 8824 Line 21 specifically

Line 21 — "Ordinary income under recapture rules. Enter here and on Form 4797, line 16."

Line 21 captures **ordinary** recapture: §1245, §1250 additional depreciation, and §1252/1254/1255. It does NOT capture unrecaptured §1250 gain (which is capital gain taxed at up to 25%).

For most rental real-estate §1031 exchanges with a straight-line building and no cost segregation, Line 21 = **$0**. The recapture, if any, is unrecaptured §1250 gain, reflected on Line 22 and split out via Schedule D's worksheet.

When §1245 or §1250 ordinary recapture applies (cost segregation, bonus or accelerated depreciation on QIP or land improvements):

- Compute the recapture a sale would produce per Form 4797 Part III rules
- Apply the exchange limit: §1245(b)(4) (Line 20 gain + FMV of non-§1245 like-kind property received) or §1250(d)(4) (larger of Line 20 gain or recapture minus FMV of §1250 property received)
- Enter the result on Line 21 — it can exceed Line 20 (instructions' Taylor example: $50,000 on Line 21 against a $40,000 Line 20)
- Line 22 = max(Line 20 − Line 21, 0); Line 23 = Line 21 + Line 22

---

## Carryover of recapture potential

Even after a §1031 exchange, the recapture potential is preserved in the replacement property's basis:

- The replacement property inherits the relinquished property's holding period (per IRC §1223(1))
- Accumulated depreciation flows through: when the user later sells the replacement, depreciation taken on **both** the old and the new property is subject to recapture
- For tax purposes, the user maintains a "depreciation history" tied to the replacement property

This is a long-term recordkeeping obligation. The agent should remind the user to keep:
- Original closing statement and basis records of the relinquished property
- Depreciation schedule showing all depreciation taken on relinquished
- Form 8824 from the year of exchange
- Replacement closing statement and any subsequent improvements

---

## Cost segregation interaction

If the user did a cost segregation study on the relinquished property, portions of basis were allocated to 5/7/15-year MACRS (§1245 property) instead of 27.5/39-year §1250.

In a §1031 exchange:
- §1245 real property of the relinquished can be exchanged for §1245 property in the replacement; Line 25b then carries that part of the basis
- §1245 real property of the relinquished exchanged for a replacement that is §1250 property → §1245 recapture is recognized up to the FMV of the non-§1245 property received (IRC §1245(b)(4); Treas. Reg. §1.1245-4(d))
- Components that are personal property (not real property under Treas. Reg. §1.1031(a)-3) are not like-kind at all: report them on Lines 12-14 as other property given up

This is complex. If the user did a cost segregation study, **flag for CPA review** before finalizing Form 8824. The general skill scope does not cover this nuance.

---

## State conformity

Most states conform to federal §1031, but state recapture rules may differ:
- Some states have no preferential capital gains rate, so unrecaptured §1250 gain is taxed at ordinary state rate
- California and others have "clawback" rules requiring annual reporting (Form 3840) until the deferred gain is recognized

---

## Worked examples

### Example A: Pure §1250 property, full deferral

- Relinquished: residential rental, $500k FMV, $200k adjusted basis, $100k accumulated depreciation
- Replacement: commercial rental, $500k FMV
- No boot, no debt change

- Realized gain = 500k − 200k = $300k
- Boot received = $0
- Recognized gain (Line 23) = $0
- Deferred gain = $300k
- Replacement basis = $200k

The $100k of depreciation history carries into the replacement. When eventually sold, it will be unrecaptured §1250 gain at up to 25%.

### Example B: §1250 property with cash boot

- Relinquished: residential rental, $500k FMV, $200k basis, $100k accumulated depreciation
- Replacement: $450k FMV
- Cash boot received: $50k

- Realized gain = $295k (after $5k exchange expenses, simplified)
- Boot received (Line 15) = $45k (after $5k expenses)
- Recognized gain (Line 23) = $45k (all on Line 22)
- Of the $45k, all $45k is unrecaptured §1250 gain (taxed at up to 25%) — because $45k ≤ $100k accumulated depreciation
- Line 21 (§1245 ordinary recapture) = $0
- Schedule D unrecaptured §1250 gain worksheet = $45k

User pays federal tax on $45k at up to 25% rate.

### Example C: Mixed §1245/§1250 with cost segregation

- Relinquished: $1M FMV, $400k basis, $200k accumulated depreciation
  - Of $200k depreciation: $50k from cost-seg-allocated 5-year property (§1245), $150k from §1250 building
- Replacement: $1M FMV, no cost seg study
- No boot

- If the 5-year components are §1245 real property under Treas. Reg. §1.1031(a)-3 and the replacement is all §1250 property: Line 21 = smaller of $50k depreciation or ($0 Line 20 gain + $1M FMV of non-§1245 property received) = **$50k ordinary income**, even with no boot; Line 22 = $0; Line 23 = $50k
- If the 5-year components are personal property (e.g., furniture, appliances), they are not like-kind: they belong on Lines 12-14 as other property given up
- This is complex; flag for CPA

---

## Validation

- [ ] If relinquished property had depreciation, accumulated depreciation amount is documented
- [ ] If §1245 or §1250 ordinary recapture applies, computed per Form 4797 Part III rules and limited per §1245(b)(4) / §1250(d)(4) (not simply capped at Line 20)
- [ ] Line 21 contains ordinary recapture only (§1245, §1250 additional depreciation, §1252/1254/1255) and matches Form 4797 line 16
- [ ] Unrecaptured §1250 gain is reflected on Line 22 and on Schedule D's worksheet
- [ ] Replacement property's depreciation follows Treas. Reg. §1.168(i)-6: carryover basis over the remaining recovery period of the relinquished property, excess basis as newly placed in service, unless the user elects out under §1.168(i)-6(i) on a timely filed return (2025 Instructions for Form 4562). Total basis = Form 8824 Line 25
- [ ] If cost segregation was used on relinquished, flagged for CPA review

---

## Sources

- IRC §1245 (recapture of depreciation on certain depreciable property — ordinary income)
- IRC §1250 (recapture of depreciation on real property — true recapture for accelerated portion)
- IRC §1(h)(1)(E) — 25% maximum rate on unrecaptured §1250 gain; IRC §1(h)(6) — definition
- IRC §1245(b)(4), §1250(d)(4) — exchange limits on recapture
- Treas. Reg. §1.1245-4(d) — §1245 in like-kind exchanges
- Treas. Reg. §1.1250-3(d) — §1250 in like-kind exchanges
- Treas. Reg. §1.1031(d)-1, §1.1031(d)-2 — basis of replacement
- 2025 Instructions for Form 8824, Line 21 and the Taylor/Finley examples
- Form 4797 instructions — Part III recapture computation
- Schedule D instructions — Unrecaptured §1250 Gain Worksheet
- Pub. 544 (Sales and Other Dispositions of Assets), Chapter 3 — recapture interaction with §1031
