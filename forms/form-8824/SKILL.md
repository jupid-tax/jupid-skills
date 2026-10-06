---
name: form-8824
description: >
  Use this skill when an individual taxpayer or a single-member LLC owner
  needs to report a like-kind exchange of REAL PROPERTY under IRC §1031 on
  Form 8824. Triggers on phrases like "1031 exchange", "like-kind exchange",
  "Form 8824", "defer real estate gain", "Qualified Intermediary 1031",
  "delayed exchange", "reverse exchange", "swap one rental for another".
  Related-party exchanges are in scope (Part II, plus the Form 8824 filed for
  each of the 2 following years).
  Do NOT use for: vehicle, equipment, or personal-property exchanges (post-2017
  no longer eligible — recognize gain on Form 4797 instead); §1033 involuntary
  conversions (different rules — use the form-4684 skill); exchanges of
  partnership interests (also ineligible); §1043 conflict-of-interest sales
  (Part IV) beyond the line map.
form: Form 8824 (Like-Kind Exchanges)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8824.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8824.pdf
---

# Form 8824 — Like-Kind Exchanges

This skill produces an audit-grade draft of Form 8824 from the user's facts about a §1031 like-kind exchange. It walks the form line by line, applies the strict timing and boot rules, computes deferred gain and recognized gain, and emits a deliverable the user can transcribe to their return with confidence.

The math has discrete edge cases (boot received, mortgage relief, related-party 2-year holds, mixed-basis property). The judgment is in *whether the exchange even qualifies* and *which rule controls when a fact is missing*. The agent should ask, not assume — a single missed timing date or related-party flag can invalidate the entire deferral.

**Form revision.** The line map in this skill was verified on 2026-10-06 against the **2025 Form 8824** (created 8/19/25) and the **2025 Instructions for Form 8824** (Dec 2, 2025), filed with 2025 returns in 2026. Before using it for a later tax year, re-check the current revision at https://www.irs.gov/forms-pubs/about-form-8824.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions "1031", "Section 1031", "like-kind exchange", or "Form 8824"
- The user describes selling a rental property and buying another with the proceeds, mediated by a Qualified Intermediary (QI)
- The user describes a "swap" of two real properties between parties
- The user mentions a "Qualified Intermediary", "Exchange Accommodation Titleholder" (EAT), "45-day identification" or "180-day deadline"
- The user asks "how do I defer the gain on selling my rental"

Do **not** engage this skill when:

- The exchange involves a vehicle, equipment, livestock, artwork, machinery, or any personal property — IRC §1031 (post-TCJA, exchanges completed after Dec 31, 2017) covers REAL PROPERTY only. Recognize gain on the disposition normally (Form 4797 or Schedule D).
- The transaction is an involuntary conversion (insurance proceeds, condemnation, casualty) — that is IRC §1033, not §1031, and uses different forms and rules. Use [`../form-4684/SKILL.md`](../form-4684/SKILL.md).
- The property exchanged is a partnership interest, stock, bonds, notes, certificates of trust or other beneficial interest, or choses in action — never real property for §1031 purposes (Treas. Reg. §1.1031(a)-3; 2025 Form 8824 instructions, "Intangible property that is never real property").
- The user holds the property as inventory or primarily for sale (e.g., a real-estate dealer who flips homes) — excluded by IRC §1031(a)(2) ("real property held primarily for sale").
- A related party sold the replacement property into the exchange (directly or through a QI) for cash or other non-like-kind property and none of the line 11 exceptions applies — the instructions say not to file Form 8824; report the disposition of the property given up as a sale (2025 Form 8824, Note under line 7; IRC §1031(f)(4); Rev. Rul. 2002-83).
- The user is considering a Delaware Statutory Trust (DST) interest as replacement property — DST interests can qualify, but the qualification analysis is more involved than this skill covers; loop in a CPA / 1031 attorney.

Related-party exchanges otherwise stay in this skill: Part II is completed in the exchange year and in each of the 2 following years, and a disposition within 2 years is reported through Part III of that year's Form 8824. See [`references/related-party.md`](./references/related-party.md).

If the user's situation is ambiguous, ask before proceeding. The most common confusion: a taxpayer sold a rental in November and bought a new one in February without using a Qualified Intermediary — that is **not** a §1031 exchange, it's two separate taxable events.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer. No defaults for ambiguous facts.

1. **Tax year** the exchange is reported in. The exchange is reported in the year the relinquished property was transferred — not the year the replacement was acquired (per Form 8824 instructions). Confirm this date with the user.
2. **Filer's legal name and SSN/ITIN** (or EIN for an entity filer). Used in the Form 8824 header.
3. **Description of relinquished property** — Line 1. Address and brief description (e.g., "Single-family rental at 123 Main St, Phoenix AZ").
4. **Description of replacement property** — Line 2. Address and brief description.
5. **Date relinquished property was originally acquired** — Line 3.
6. **Date relinquished property was transferred to other party** — Line 4. This starts the 45/180-day clock.
7. **Date replacement property was identified in writing** — Line 5. Must be ≤ 45 days after Line 4 per IRC §1031(a)(3)(A). If the replacement was received within the 45 days, enter the receipt date (2025 instructions, Line 5 Note).
8. **Date replacement property was received** — Line 6. Must be ≤ 180 days after Line 4 (or the due date of the return for the year of transfer, including extensions, whichever is earlier) per IRC §1031(a)(3)(B).
9. **Was the exchange between related parties, directly or indirectly?** — Line 7. If yes, ask for the related party's name, relationship, identifying number, and address (Line 8), whether either party disposed of the property during the year (Lines 9 and 10), and walk the 2-year holding rule per IRC §1031(f).
10. **Property fair market values and bases**:
    - Adjusted basis of relinquished property (original cost + improvements − depreciation taken)
    - Fair market value (FMV) of relinquished property at the time of transfer
    - FMV of replacement property at the time of receipt
    - Cash boot received (if any)
    - Cash boot paid (if any)
    - Liabilities ASSUMED BY OTHER PARTY (mortgage relief on relinquished — treated as boot received)
    - Liabilities ASSUMED BY USER (debt on replacement — netted against mortgage relief; net relief is boot)
    - Exchange expenses (closing costs on both sides: brokerage commissions, QI fees, escrow, attorney and deed fees, recording fees) — they first reduce Line 15 (not below zero); any remainder goes on Line 18 (Pub. 544, "Exchange expenses"; 2025 instructions, Lines 15 and 18). Prorated property taxes, rent prorations, security deposits, and repairs on the closing statement are not exchange expenses.
    - For depreciable replacement property: how much of the replacement's FMV is §1250 property, §1245 property, or intangible real property (Lines 25a–25c)

For multi-asset exchanges (more than one group of like-kind properties, or cash or other non-like-kind property on either side), the instructions say not to complete lines 12–18; attach a statement showing how realized and recognized gain were figured and enter lines 19–25 (2025 instructions, "Reporting of multi-asset exchanges"; Treas. Reg. §1.1031(j)-1). Personal property received with the real estate is non-like-kind property (boot) for gain recognition, even when it is "incidental" for the QI rules (Pub. 544, "Disregard incidental property").

For depreciable property (most rentals), there are recapture considerations under IRC §1245 / §1250 even within a §1031 exchange — flag if the user took accelerated depreciation. See [`references/depreciation-recapture.md`](./references/depreciation-recapture.md).

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm post-TCJA real-property test

Confirm both relinquished and replacement properties are real property held for productive use in a trade or business or for investment. If either is personal property, vehicles, equipment, machinery, art, crypto, or inventory, **stop**: §1031 does not apply to that exchange. Recognize gain normally on Form 4797 (business assets) or Schedule D (investment assets).

### Step 2 — Confirm structure: simultaneous, delayed, or reverse

Three patterns:

- **Simultaneous (rare today)**: The two properties trade hands on the same day. No QI strictly required, but most parties still use one to avoid constructive receipt issues.
- **Delayed / forward (most common)**: The user sells the relinquished property to a third-party buyer, the proceeds go to a Qualified Intermediary (QI), the user identifies replacement within 45 days, and the QI uses the funds to acquire replacement within 180 days. Without a QI, the user is in constructive receipt of the proceeds and the deferral fails.
- **Reverse**: The user (via an Exchange Accommodation Titleholder, "EAT") acquires the replacement property *before* selling the relinquished. Governed by the Rev. Proc. 2000-37 safe harbor as modified by Rev. Proc. 2004-51. Timing runs from the transfer of the replacement to the EAT: 45 days to identify the property to be relinquished, 180 days to complete the transfers, and the property may not be held in the arrangement longer than 180 days in total. Property the user owned within 180 days before its transfer to the EAT cannot be replacement property (Rev. Proc. 2004-51; 2025 instructions, "Exchanges Using a QEAA").

Confirm which pattern applies. The pattern affects how the dates on Form 8824 lines 3–6 are read.

### Step 3 — Verify the 45-day and 180-day deadlines

Compute days between Line 4 (relinquished transfer) and:
- Line 5 / written identification: must be ≤ 45 calendar days. The period "ends at midnight on the 45th day" (Treas. Reg. §1.1031(k)-1(b)(2)(i)); do not roll a weekend or holiday deadline forward.
- Line 6 / replacement receipt: must be ≤ 180 calendar days OR the due date of the return for the year of transfer (with extensions), whichever is **earlier** (Treas. Reg. §1.1031(k)-1(b)(2)(ii)).

The only extension is a federally declared disaster postponement under Rev. Proc. 2018-58, section 17 (120 days or the end of the disaster relief period, whichever is later, but never past the return due date with extensions or 1 year). If a deadline looks missed, ask whether the user, the property, or a party to the exchange was in a covered disaster area before concluding.

If either deadline was missed, **stop**: the exchange does not qualify for deferral. Recognize the entire gain in the year of the relinquished transfer. Surface this clearly to the user before continuing.

### Step 4 — Apply related-party rule (if applicable)

If the exchange was with a related party (per IRC §267(b) or §707(b)(1) — siblings, spouse, ancestors, lineal descendants, controlled entities, etc.):

- Both parties must hold their received property for **at least 2 years** after the date of the last transfer in the exchange.
- If either party disposes within 2 years, the original §1031 deferral is **un-done** for the user: the deferred gain or loss from Line 24 is reported in the year of the disqualifying disposition (IRC §1031(f)(1)).
- Exceptions (Line 11): disposition after the death of either party; involuntary conversion where the threat of conversion arose after the exchange; or the user establishes to the IRS's satisfaction that neither the exchange nor the disposition had tax avoidance as a principal purpose (attach an explanation) (IRC §1031(f)(2)).

File Form 8824 for the exchange year and for each of the 2 following years (2025 instructions, "When To File"). In a following year, complete Parts I and II; if Lines 9 and 10 are both "No", stop there. The agent should warn the user that a future disposition within 2 years will reopen the gain.

### Step 5 — Compute realized gain or loss

```
Realized gain = FMV of replacement property received
              + Cash and other boot received
              + Liabilities assumed by other party (mortgage relief)
              − Adjusted basis of relinquished property
              − Cash and other boot paid
              − Liabilities assumed by user
              − Exchange expenses
```

This is the gross gain economically realized. Without §1031, all of it would be taxable.

### Step 6 — Compute recognized gain (boot rule)

```
Recognized gain = LESSER OF:
  (a) Realized gain, OR
  (b) Boot received (cash boot + net mortgage relief, less exchange expenses paid out of boot)
```

- Cash boot received is fully recognized up to the realized gain.
- **Mortgage boot**: liabilities assumed by the other party count as boot only to the extent they exceed the total of (a) liabilities the user assumed, (b) cash the user paid, and (c) FMV of other property the user gave up (2025 instructions, Line 15). If the user assumes more debt than the other party, there is no mortgage boot.
- Cash paid and debt assumed by the user offset mortgage relief, but liabilities the user assumed never offset cash the user received. See [`references/boot-rules.md`](./references/boot-rules.md) for the offset matrix.
- All exchange expenses reduce Line 15 (not below zero), regardless of how they were paid; the unused remainder goes on Line 18.
- If realized loss occurred and boot was received, **no loss is recognized** under §1031 (boot does not trigger loss recognition; the loss is deferred into basis of replacement property).

### Step 7 — Compute basis of replacement property

```
Basis of replacement = Adjusted basis of relinquished
                     + Boot paid (cash + liabilities assumed by user)
                     − Boot received (cash + FMV of other property
                       + liabilities assumed by other party, before expenses)
                     + Recognized gain
                     + All exchange expenses
```

On the form this is Line 25 = Line 18 + Line 23 − Line 15, which also equals Line 16 − Line 24. Allocate Line 25 on Lines 25a (§1250 property), 25b (§1245, 1252, 1254, 1255 property), and 25c (intangible real property) in proportion to FMV (2025 instructions, "Lines 25a, 25b, and 25c"). Non-like-kind property received takes a basis equal to its FMV.

This basis carries forward. The deferred gain is preserved in this lower-than-FMV basis and will be taxed when the replacement property is eventually sold (unless it's exchanged again under §1031).

### Step 8 — Map computed values to Form 8824 lines

Use [`references/line-by-line.md`](./references/line-by-line.md) for the full mapping. High-level:

- **Part I (Lines 1-7)**: Property descriptions and dates
- **Part II (Lines 8-11)**: Related-party information (only if applicable)
- **Part III (Lines 12-25c)**: Realized gain/loss, recognized gain, basis of replacement
- **Part IV (Lines 26-38)**: §1043 conflict-of-interest sales by federal executive-branch officers, employees, and judicial officers (rare; do not engage unless user is in this category)

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms the user will need:

- **Line 21** (ordinary income under recapture rules) goes on Form 4797, line 16 (printed on the form).
- **Line 22** (the rest of the recognized gain) flows to:
  - Form 4797, line 5 (§1231 gain from like-kind exchanges, property held more than 1 year) or line 16 (ordinary, held 1 year or less) for real property used in a trade or business, including rentals (2025 instructions, Line 22; 2025 Form 4797 lines 5 and 16). See [`../form-4797/SKILL.md`](../form-4797/SKILL.md).
  - Schedule D, line 4 (short-term) or line 11 (long-term) for a capital asset such as investment land; no Form 8949 entry (2025 Schedule D lines 4 and 11). See [`../schedule-d/SKILL.md`](../schedule-d/SKILL.md).
  - Form 6252 if the installment method applies (§453(f)(6)). See [`../form-6252/SKILL.md`](../form-6252/SKILL.md).
- **Depreciation recapture**: Line 21 can exceed the boot-attributable gain on Line 20 when §1245 property is exchanged for §1250 property — see [`references/depreciation-recapture.md`](./references/depreciation-recapture.md).
- **Depreciation of the replacement** (Form 4562): depreciate the carryover basis over the remaining recovery period of the relinquished property with the same method and convention, and treat any excess basis as newly placed in service; or elect out under Treas. Reg. §1.168(i)-6(i) on a timely filed return (2025 Instructions for Form 4562, "Property acquired in a like-kind exchange or involuntary conversion"). Residential rental (27.5-year) and nonresidential (39-year) buildings are not "qualified property" for the special depreciation allowance, which requires a MACRS recovery period of 20 years or less; for qualified property received (for example 15-year components), the OBBBA 100% allowance applies to property acquired after January 19, 2025 (2025 Instructions for Form 4562, What's New and "Qualified property"). The new §168(n) qualified production property allowance is outside this skill. See [`../form-4562/SKILL.md`](../form-4562/SKILL.md).
- **State return**: many states conform to §1031, but California has a "clawback" — if California-source property is exchanged for out-of-state property, FTB Form 3840 must be filed annually until the deferred gain is recognized. Other states have variations. Flag for the user.
- **Future sale of replacement**: the deferred gain is embedded in the carryover basis. Set a reminder in the user's tax records that this property has a tax basis lower than its FMV by the deferred gain amount. Keep the records for both the old and the new property until the period of limitations expires for the year the new property is disposed of (irs.gov, "How long should I keep records?").

### Step 12 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). Form 8824 is supported on most paid tax software and on IRS Free File Fillable Forms (FFFF lists it as available from 01/26/2026 for tax year 2025; FFFF closes Oct. 15, 2026). IRS Direct File was not offered in the 2026 filing season; do not offer it as a channel.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level summary below.

### Part I — Information on the Like-Kind Exchange (Lines 1-7)

- **Line 1** — Description of like-kind property given up (relinquished). Include address and brief description ("rental SFH at 123 Main St, Phoenix AZ").
- **Line 2** — Description of like-kind property received (replacement). Same format.
- **Line 3** — Date like-kind property given up was originally acquired (MM/DD/YYYY).
- **Line 4** — Date you actually transferred property given up (MM/DD/YYYY).
- **Line 5** — Date like-kind property you received was identified in writing (MM/DD/YYYY). Must be ≤ 45 days after Line 4. If the replacement was received before the 45-day period ended, enter the receipt date.
- **Line 6** — Date you actually received like-kind property (MM/DD/YYYY). Must be ≤ 180 days after Line 4 and no later than the return due date with extensions.
- **Line 7** — Was the exchange of property given up or received made with a related party, directly or indirectly (such as through an intermediary)? Yes/No. If Yes, complete Part II; if No, go to Part III.

### Part II — Related Party Exchange Information (Lines 8-11)

Only fill if Line 7 is Yes. Asks for:
- **Line 8** — Related party's name, relationship to you, identifying number, and address
- **Line 9** — During this tax year (and before 2 years after the last transfer), did the related party sell or dispose of any part of the like-kind property received from you? Yes/No
- **Line 10** — During this tax year (and before 2 years after the last transfer), did you sell or dispose of any part of the like-kind property you received? Yes/No
- If Lines 9 and 10 are both "No": in the exchange year go to Part III; in a later year, stop. If either is "Yes": complete Part III and report the Line 24 deferred gain or (loss) this year unless a Line 11 exception applies.
- **Line 11** — Exception boxes: 11a disposition after the death of either related party; 11b involuntary conversion where the threat of conversion occurred after the exchange; 11c no tax-avoidance principal purpose (attach an explanation).

### Part III — Realized Gain or (Loss), Recognized Gain, and Basis of Like-Kind Property Received (Lines 12-25)

Highest-friction part. Lines 12-14 handle "non-like-kind" property GIVEN UP (rare under the post-TCJA real-property-only rule, but possible if part of the deal was personal property bundled with the real estate); complete them only in that case, otherwise go to Line 15. Lines 15-25c are the core §1031 math.

- **Line 12** — FMV of OTHER (non-like-kind) property given up. **Line 12a** — its description (on the form itself, including e-filed returns since 2024).
- **Line 13** — Adjusted basis of OTHER property given up
- **Line 14** — Gain or loss on OTHER property given up (Line 12 − Line 13). This portion is **always recognized**; report it as if the exchange had been a sale.
- **Line 15** — Cash received, FMV of other property received, plus net liabilities assumed by other party, reduced (but not below zero) by any exchange expenses you incurred. (This is "boot received".) **Line 15a** — description of the other property received (e.g., "cash").
- **Line 16** — FMV of like-kind property you received
- **Line 17** — Add Lines 15 + 16
- **Line 18** — Adjusted basis of like-kind property given up, plus the net amount paid to the other party (excess of liabilities you assumed + cash you paid + FMV of other property you gave up over liabilities the other party assumed), plus exchange expenses not used on Line 15 (the user's "give" side)
- **Line 19** — Realized gain or (loss). Subtract Line 18 from Line 17. If a §121 exclusion applies, write "Section 121 exclusion" and the amount in the entry space; do not reduce Line 19 (2025 What's New).
- **Line 20** — Smaller of Line 15 or Line 19, but not less than zero. (This is recognized gain attributable to boot received.)
- **Line 21** — Ordinary income under recapture rules (§1245, §1250 additional depreciation, §1252/1254/1255). Enter here and on Form 4797, line 16. Can exceed Line 20. See [`references/depreciation-recapture.md`](./references/depreciation-recapture.md).
- **Line 22** — Line 20 − Line 21; if zero or less, enter -0-. If more than zero, report on Form 4797 (line 5 or 16) or Schedule D (line 4 or 11), unless the installment method applies.
- **Line 23** — Recognized gain. Line 21 + Line 22.
- **Line 24** — Deferred gain or (loss). Line 19 − Line 23; if Line 19 is a loss, enter the loss. This is the gain pushed into the basis of replacement.
- **Line 25** — Basis of like-kind property received. Line 18 + Line 23 − Line 15. **Lines 25a / 25b / 25c** — the part of Line 25 allocated to like-kind §1250 property / §1245, 1252, 1254, 1255 property / intangible real property received, in proportion to FMV.

### Part IV — Section 1043 Conflict-of-Interest Sales (Lines 26-38)

Do not engage unless the user is an officer or employee of the federal executive branch or a federal judicial officer (or a spouse, minor or dependent child, or trustee covered by §1043) selling under a certificate of divestiture from the Office of Government Ethics or the Judicial Conference. Part IV is used only when the cost of replacement property bought within 60 days exceeds the basis of the divested property. Out of scope for the typical filer; the line map is in [`references/line-by-line.md`](./references/line-by-line.md).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 5 minus Line 4 ≤ 45 days (IRC §1031(a)(3)(A) identification deadline)
- [ ] Line 6 minus Line 4 ≤ 180 days (IRC §1031(a)(3)(B) acquisition deadline)
- [ ] Line 6 minus Line 4 ≤ due date of return for year of relinquished transfer (including extensions) — whichever is earlier than 180 days
- [ ] Line 14 = Line 12 − Line 13
- [ ] Line 17 = Line 15 + Line 16
- [ ] Line 19 = Line 17 − Line 18 (could be negative — that's a realized loss)
- [ ] Line 20 = lesser of (Line 15, Line 19), but ≥ 0
- [ ] Line 22 = max(Line 20 − Line 21, 0)
- [ ] Line 23 = Line 21 + Line 22
- [ ] Line 24 = Line 19 − Line 23 (deferred gain or loss)
- [ ] Line 25 = Line 18 + Line 23 − Line 15, and Line 25 = Line 16 − Line 24
- [ ] Lines 25a + 25b + 25c = Line 25 when any of them is used, each in proportion to FMV

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Realized loss (Line 19 negative) AND boot was received → user should know the loss is **deferred into replacement basis**, not recognized currently
- [ ] Replacement FMV substantially higher than relinquished FMV with no cash boot paid → confirm with user; usually the user paid additional cash, which is boot **paid** (good — it adds to basis)
- [ ] Mortgage relief (debt assumed by other party) > debt user assumed on replacement → net mortgage boot received; flag for inclusion in Line 15
- [ ] Property was held < 1 year before exchange → §1031 still applies if held for investment/business use, but a holding-period question may arise; inform the user
- [ ] Property given up was used solely as the user's personal residence at the time of the exchange → §1031 does not apply; §121 may. Stop and redirect. If it was used partly or formerly as a main home, follow "Property Used as Home" in the instructions (two worksheet Forms 8824, Line 19 write-in; Rev. Proc. 2005-14).
- [ ] Replacement is held for personal use (vacation home not rented) → fails §1031 "held for productive use in trade or business or for investment" requirement. Rev. Proc. 2008-16 provides a safe harbor for dwelling units: owned 24 months before (relinquished) or after (replacement) the exchange, and in each of the two 12-month periods rented at a fair rental for 14 days or more, with personal use not exceeding the greater of 14 days or 10% of the days rented at a fair rental.
- [ ] Exchange was with a related party → Form 8824 is due for this year and each of the next 2 years; flag Lines 9 and 10 for those years
- [ ] Depreciation taken on relinquished property exceeded straight-line, or a cost segregation study allocated basis to §1245 property → Line 21 recapture likely; see [`references/depreciation-recapture.md`](./references/depreciation-recapture.md)

### Cross-form checks

- [ ] If Line 21 > 0, Form 4797 line 16 shows the same amount
- [ ] If Line 22 > 0, Form 4797 (line 5 or 16) or Schedule D (line 4 or 11) shows the same amount, or Form 6252 if the installment method applies
- [ ] If user took depreciation on relinquished property, check Line 21 (§1245 recapture for §1245 real property, §1250 recapture for depreciation in excess of straight-line) and the unrecaptured §1250 gain in any Line 22 amount
- [ ] State return: California requires Form 3840 if relinquished was CA-source and replacement is non-CA. Other states with "clawback" rules: Oregon, Massachusetts, Montana — verify per-state at filing.
- [ ] If cash boot was received, the user owes federal tax on Line 23 and possibly state tax — surface for estimated-tax planning.

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 8824 or paste into tax software.

```markdown
# Form 8824 — DRAFT for tax year YYYY

## Header
Name(s) on return: <legal name>
Identifying number: <SSN/EIN>

## Part I — Information on the Like-Kind Exchange
1. Description of property given up:    <addr / description>
2. Description of property received:    <addr / description>
3. Date property given up was originally acquired:  MM/DD/YYYY
4. Date you actually transferred property given up: MM/DD/YYYY
5. Date like-kind property received was identified: MM/DD/YYYY
   (Days from Line 4 to Line 5: NN — must be ≤ 45)
6. Date you actually received like-kind property:   MM/DD/YYYY
   (Days from Line 4 to Line 6: NN — must be ≤ 180)
7. Related-party exchange?  Yes | No

## Part II — Related-Party Exchange Information (if Line 7 = Yes)
8. Name, relationship, identifying number, address of related party
9. Related party disposed of property received from you this year?  Yes | No
10. You disposed of property you received this year?  Yes | No
11. Exception (if Line 9 or 10 = Yes): 11a death | 11b involuntary conversion | 11c no tax-avoidance purpose (explanation attached) | none → report Line 24 now

## Part III — Realized Gain, Recognized Gain, and Basis
12. FMV of OTHER (non-like-kind) property given up:  $X,XXX
12a. Description of other property given up:        <text>
13. Adjusted basis of OTHER property given up:       $X,XXX
14. Gain/(loss) on OTHER property (Line 12 − 13):    $X,XXX  (always recognized)
15. Cash + FMV of other property received + net liabilities assumed by other party
    less exchange expenses, not below 0 (boot received): $X,XXX
15a. Description of other property received:         <text>
16. FMV of like-kind property you received:           $X,XXX
17. Add lines 15 and 16:                              $X,XXX
18. Adjusted basis of like-kind property given up + net amount paid
    + exchange expenses not used on line 15:          $X,XXX
19. Realized gain/(loss) (Line 17 − Line 18):         $X,XXX
20. Smaller of Line 15 or Line 19 (≥ 0):              $X,XXX  (boot-attributable gain)
21. Ordinary income under recapture rules:            $X,XXX  → Form 4797, line 16
22. Line 20 − Line 21 (≥ 0):                          $X,XXX  → Form 4797 line 5/16 or Sch D line 4/11
23. Recognized gain (Line 21 + Line 22):              $X,XXX
24. Deferred gain/(loss) (Line 19 − Line 23):         $X,XXX
25. Basis of like-kind property received
    (Line 18 + Line 23 − Line 15):                    $X,XXX
25a. Basis of like-kind §1250 property received:      $X,XXX
25b. Basis of like-kind §1245/1252/1254/1255 property: $X,XXX
25c. Basis of like-kind intangible property received: $X,XXX

## Required attachments
- [ ] Form 4797 (if Line 21 or Line 22 > 0 and property was used in a trade or business, including rentals)
- [ ] Schedule D (if Line 22 > 0 and property was a capital asset held for investment)
- [ ] Line 11c explanation, if checked
- [ ] State 1031 form (e.g., CA FTB 3840 — verify state rules)
- [ ] QI exchange agreement and identification notice (retain for records, not filed)

## Validation summary
- 45-day check: Day NN ≤ 45  ✓ | ✗
- 180-day check: Day NN ≤ 180 ✓ | ✗
- Math: all checks passed | <list failures>
- Sanity warnings: <list>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 8824 (tax year YYYY revision)
- IRS Instructions for Form 8824 (tax year YYYY revision)
- IRC §1031 (post-TCJA, real-property-only rule effective for exchanges after 2017-12-31)
- IRC §1031(a)(3) (45-day / 180-day deadlines)
- IRC §1031(f) (related-party 2-year rule)
- Rev. Proc. 2000-37, as modified by Rev. Proc. 2004-51 (reverse exchange safe harbor)
- Rev. Proc. 2008-16 (dwelling-unit safe harbor)
- Treas. Reg. §1.1031(a)-3 (definition of real property), §1.1031(d)-2 (liabilities), §1.1031(k)-1 (deferred exchanges, qualified intermediary rules)
- Pub. 544 (Sales and Other Dispositions of Assets)
```

The draft is **not** the final filed form. The user still has to attach it to their Form 1040 (or 1065 / 1120-S / 1041) and carry Line 21 and Line 22 to the appropriate gain-recognition form (4797 or Schedule D).

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8824 line with examples and edge cases
- [`references/timing-rules.md`](./references/timing-rules.md) — 45-day identification rules (3-property, 200%, 95% rules), 180-day deadline interaction with return due date, weekends/holidays handling
- [`references/boot-rules.md`](./references/boot-rules.md) — Cash boot, mortgage boot, the offset matrix, exchange expenses
- [`references/depreciation-recapture.md`](./references/depreciation-recapture.md) — §1245 vs. §1250, unrecaptured §1250 gain in §1031 exchanges
- [`references/related-party.md`](./references/related-party.md) — IRC §1031(f), 2-year holding rule, exceptions, Part II reporting
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 10 audit-trip mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Form 8824 via Free File Fillable Forms, paper, or generic tax software (loaded only when the user authorizes filing)

## Examples

End-to-end worked Form 8824 walkthroughs. Use these as patterns when the user's situation is similar.

- [`examples/delayed-exchange-no-boot.md`](./examples/delayed-exchange-no-boot.md) — Rental SFH for rental SFH, equal values via QI, no boot, full deferral
- [`examples/delayed-exchange-with-boot.md`](./examples/delayed-exchange-with-boot.md) — Replacement worth less than relinquished; user receives $50,000 cash boot; exchange expenses reduce it to $38,000 of recognized gain
- [`examples/reverse-exchange.md`](./examples/reverse-exchange.md) — Replacement closed first; Exchange Accommodation Titleholder (EAT) parks title under Rev. Proc. 2000-37 safe harbor; more debt and cash in, full deferral

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed.

- [Form 8824 (latest)](https://www.irs.gov/pub/irs-pdf/f8824.pdf) — the form itself
- [Instructions for Form 8824 (latest)](https://www.irs.gov/pub/irs-pdf/i8824.pdf) — line-by-line IRS guidance
- [About Form 8824](https://www.irs.gov/forms-pubs/about-form-8824) — IRS landing page with archive of past revisions
- [Publication 544](https://www.irs.gov/pub/irs-pdf/p544.pdf) — Sales and Other Dispositions of Assets
- IRC §1031 (like-kind exchanges of real property)
- IRC §1031(a)(2) (exclusion for real property held primarily for sale)
- IRC §1031(a)(3) (45-day / 180-day timing rules for delayed exchanges)
- IRC §1031(b) (gain recognized to extent of boot)
- IRC §1031(d) (basis of replacement property)
- IRC §1031(f) (related-party 2-year holding rule)
- IRC §1245, §1250 (depreciation recapture)
- TCJA §13303 (Public Law 115-97), restricting §1031 to real property for exchanges completed after Dec 31, 2017
- Rev. Proc. 2000-37, as modified by Rev. Proc. 2004-51 (reverse exchange safe harbor)
- Rev. Proc. 2005-14 (§121 and §1031 on the same property)
- Rev. Proc. 2008-16 (dwelling-unit safe harbor)
- Rev. Proc. 2018-58, section 17 (disaster postponement of the 45/180-day deadlines)
- Rev. Rul. 2002-83 (related-party exchanges through a QI)
- Treas. Reg. §1.1031(a)-3 (definition of real property), §1.1031(d)-2 (liabilities), §1.1031(j)-1 (multi-asset exchanges), §1.1031(k)-1 (deferred exchanges, qualified intermediaries, exchange periods)
- Treas. Reg. §1.168(i)-6 and the 2025 Instructions for Form 4562 (depreciation of replacement property)
- [Instructions for Form 4797](https://www.irs.gov/pub/irs-pdf/i4797.pdf) and [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) (where Lines 21 and 22 are reported)
- [Free File Fillable Forms available-forms list](https://www.irs.gov/e-file-providers/list-of-available-free-file-fillable-forms) (re-check each season)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. §1031 exchanges are highly fact-dependent — a single missed deadline, related-party flag, or improper QI structure can invalidate the deferral and trigger immediate gain. The agent invoking this skill should remind the user that the output is a starting point and that any §1031 exchange warrants review by a CPA or 1031-experienced tax attorney before the relinquished transfer date, not after.
