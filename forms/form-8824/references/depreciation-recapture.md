# Form 8824 Depreciation Recapture

When the relinquished property had depreciation taken on it (almost every rental), the §1031 deferral does NOT shield the recapture portion to the extent of boot received.

This file explains §1245 vs. §1250 and how recapture flows through Form 8824.

---

## §1245 vs. §1250

### §1245 property

Depreciable personal property and certain depreciable real property (e.g., qualified improvement property with 15-year MACRS).

- Recapture under §1245 is **ordinary income** (top federal rate up to 37%) up to the lesser of:
  - All depreciation taken, OR
  - Realized gain
- Reported on Form 4797 Part III, then flowed to Part II

In §1031 exchanges, §1245 recapture appears on **Form 8824 Line 21** (ordinary income under recapture rules) up to the boot received. Pre-TCJA this was common (vehicles, equipment); post-TCJA it's rare for real-property §1031 exchanges, except for:
- Qualified improvement property (QIP) with 15-year MACRS
- Land improvements (15-year MACRS, §1250 but treated as §1245 for some recapture purposes)
- Mixed-asset real estate with carve-outs

### §1250 property

Depreciable real property — buildings, structural components, residential and commercial real estate.

- §1250 "true recapture" (depreciation in excess of straight-line) is ordinary income. Since 1986 most real property uses straight-line MACRS, so true §1250 recapture is **rare**.
- **Unrecaptured §1250 gain** is the lesser of all straight-line depreciation taken or realized gain. Taxed at a maximum federal rate of **25%** (capital gains, but with a higher cap than the 20%/15%/0% long-term capital gains rates).
- Reported on Schedule D's **Unrecaptured Section 1250 Gain Worksheet** (in Schedule D instructions).

In §1031 exchanges, unrecaptured §1250 gain on the boot-attributable portion flows through Form 8824 Line 22 (recognized gain) and is split out on Schedule D as 25%-rate gain.

---

## Recapture in §1031 — the sequencing rule

Per Treas. Reg. §1.1031(d)-1 and Pub. 544:

When boot triggers gain recognition, the **recapture is recognized first**:

1. First, recapture (§1245 ordinary or unrecaptured §1250 capital) up to the recognized gain
2. Then, remaining recognized gain is regular capital gain (long-term if held > 1 year, taxed at 0/15/20%)

Example:
- Relinquished property had $100,000 of straight-line §1250 depreciation taken
- Realized gain (Line 19) = $295,000
- Boot received = $50,000
- Recognized gain (Line 22) = $50,000

Of the $50,000 recognized:
- All $50,000 is unrecaptured §1250 gain (taxed at up to 25%) — because all $50,000 ≤ $100,000 of accumulated depreciation
- $0 is regular long-term capital gain at this point

The remaining $50,000 of accumulated depreciation (and $245,000 of total deferred gain) carries into the replacement property's basis, preserving the recapture potential for the next sale.

---

## Form 8824 Line 21 specifically

Line 21 — "Ordinary income under recapture rules. Enter here and on Form 4797, line 16."

Line 21 captures **§1245 ordinary recapture only**. It does NOT capture unrecaptured §1250 (which is capital, not ordinary).

For most rental real-estate §1031 exchanges, Line 21 = **$0**. The recapture, if any, is unrecaptured §1250 gain, reflected on Line 22 and split out via Schedule D's worksheet.

For rare cases where §1245 recapture applies (e.g., the relinquished property included QIP or had cost-segregation studies allocating part of basis to 5/7/15-year MACRS):

- Compute §1245 recapture per Form 4797 Part III rules
- Cap at recognized gain (Line 20)
- Enter the lesser on Line 21
- Line 22 = Line 21 + (Line 20 − Line 21) — the residual capital gain portion

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
- §1245 portion of relinquished can be exchanged for §1245 portion of replacement (if allocations match)
- §1245 portion of relinquished exchanged for §1250 portion of replacement → §1245 recapture is triggered to the extent of the value mismatch (Treas. Reg. §1.1245-4(d)(1))

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
- Recognized gain (Line 22) = $0
- Deferred gain = $300k
- Replacement basis = $200k

The $100k of depreciation history carries into the replacement. When eventually sold, it will be unrecaptured §1250 gain at up to 25%.

### Example B: §1250 property with cash boot

- Relinquished: residential rental, $500k FMV, $200k basis, $100k accumulated depreciation
- Replacement: $450k FMV
- Cash boot received: $50k

- Realized gain = $295k (after $5k exchange expenses, simplified)
- Boot received (Line 15) = $45k (after $5k expenses)
- Recognized gain (Line 22) = $45k
- Of the $45k, all $45k is unrecaptured §1250 gain (taxed at up to 25%) — because $45k ≤ $100k accumulated depreciation
- Line 21 (§1245 ordinary recapture) = $0
- Schedule D unrecaptured §1250 gain worksheet = $45k

User pays federal tax on $45k at up to 25% rate.

### Example C: Mixed §1245/§1250 with cost segregation

- Relinquished: $1M FMV, $400k basis, $200k accumulated depreciation
  - Of $200k depreciation: $50k from cost-seg-allocated 5-year property (§1245), $150k from §1250 building
- Replacement: $1M FMV, no cost seg study
- No boot

- §1245 portion of relinquished was $50k allocated to short-life property; replacement has no matching §1245 carve-out
- Treas. Reg. §1.1245-4(d)(1) → triggers §1245 recapture to extent of basis allocation mismatch
- This is complex; flag for CPA

---

## Validation

- [ ] If relinquished property had depreciation, accumulated depreciation amount is documented
- [ ] If §1245 recapture applies, computed per Form 4797 Part III rules, capped at Line 20
- [ ] Line 21 contains §1245 ordinary recapture only
- [ ] Unrecaptured §1250 gain is reflected on Line 22 and on Schedule D's worksheet
- [ ] Replacement property's depreciation schedule will inherit relinquished's depreciation history (carryover basis = relinquished basis − boot received + recognized gain)
- [ ] If cost segregation was used on relinquished, flagged for CPA review

---

## Sources

- IRC §1245 (recapture of depreciation on certain depreciable property — ordinary income)
- IRC §1250 (recapture of depreciation on real property — true recapture for accelerated portion)
- IRC §1(h)(1)(E) — 25% maximum rate on unrecaptured §1250 gain
- Treas. Reg. §1.1245-4(d)(1) — §1245 in like-kind exchanges
- Treas. Reg. §1.1250-3(d) — §1250 in like-kind exchanges
- Treas. Reg. §1.1031(d)-1, §1.1031(d)-2 — basis of replacement
- Form 4797 instructions — Part III recapture computation
- Schedule D instructions — Unrecaptured §1250 Gain Worksheet
- Pub. 544 (Sales and Other Dispositions of Assets), Chapter 3 — recapture interaction with §1031
