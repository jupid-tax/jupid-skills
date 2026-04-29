---
name: form-8824
description: >
  Use this skill when an individual taxpayer or a single-member LLC owner
  needs to report a like-kind exchange of REAL PROPERTY under IRC §1031 on
  Form 8824. Triggers on phrases like "1031 exchange", "like-kind exchange",
  "Form 8824", "defer real estate gain", "Qualified Intermediary 1031",
  "delayed exchange", "reverse exchange", "swap one rental for another".
  Do NOT use for: vehicle, equipment, or personal-property exchanges (post-2017
  no longer eligible — recognize gain on Form 4797 instead); related-party
  exchanges where the property was held less than 2 years (gain recognized
  in current year per IRC §1031(f)); §1033 involuntary conversions (different
  rules — use the (forthcoming) form-4684 / §1033 skill); exchanges of
  partnership interests (also ineligible).
form: Form 8824 (Like-Kind Exchanges)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f8824.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8824.pdf
---

# Form 8824 — Like-Kind Exchanges

This skill produces an audit-grade draft of Form 8824 from the user's facts about a §1031 like-kind exchange. It walks the form line by line, applies the strict timing and boot rules, computes deferred gain and recognized gain, and emits a deliverable the user can transcribe to their return with confidence.

The math has discrete edge cases (boot received, mortgage relief, related-party 2-year holds, mixed-basis property). The judgment is in *whether the exchange even qualifies* and *which rule controls when a fact is missing*. The agent should ask, not assume — a single missed timing date or related-party flag can invalidate the entire deferral.

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
- The transaction is an involuntary conversion (insurance proceeds, condemnation, casualty) — that is IRC §1033, not §1031, and uses different forms and rules.
- The property exchanged is a partnership interest, stock, bonds, certificates of trust or other beneficial interest, choses in action, or inventory — explicitly excluded by IRC §1031(a)(2).
- The "exchange" is between related parties and either party disposes of the received property within 2 years — gain is recognized in the current year per IRC §1031(f). A different deferral framework applies.
- The user holds the property as inventory (e.g., a real-estate dealer who flips homes) — those properties are §1221(a)(1) inventory, not §1031-eligible.
- The user is considering a Delaware Statutory Trust (DST) interest as replacement property — DST interests can qualify, but the qualification analysis is more involved than this skill covers; loop in a CPA / 1031 attorney.

If the user's situation is ambiguous, ask before proceeding. The most common confusion: a taxpayer sold a rental in November and bought a new one in February without using a Qualified Intermediary — that is **not** a §1031 exchange, it's two separate taxable events.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer. No defaults for ambiguous facts.

1. **Tax year** the exchange is reported in. The exchange is reported in the year the relinquished property was transferred — not the year the replacement was acquired (per Form 8824 instructions). Confirm this date with the user.
2. **Filer's legal name and SSN/ITIN** (or EIN for an entity filer). Used in the Form 8824 header.
3. **Description of relinquished property** — Line 1. Address and brief description (e.g., "Single-family rental at 123 Main St, Phoenix AZ").
4. **Description of replacement property** — Line 2. Address and brief description.
5. **Date relinquished property was originally acquired** — Line 5.
6. **Date relinquished property was transferred to other party** — Line 6. This starts the 45/180-day clock.
7. **Date replacement property was identified in writing** — Line 7. Must be ≤ 45 days after Line 6 per IRC §1031(a)(3)(A).
8. **Date replacement property was received** — Line 8. Must be ≤ 180 days after Line 6 (or the due date of the return for the year of transfer, including extensions, whichever is earlier) per IRC §1031(a)(3)(B).
9. **Was the exchange between related parties?** — Line 7 reverse / Line 9. If yes, ask for the related-party name, address, and SSN/EIN; then walk the 2-year holding rule per IRC §1031(f).
10. **Property fair market values and bases**:
    - Adjusted basis of relinquished property (original cost + improvements − depreciation taken)
    - Fair market value (FMV) of relinquished property at the time of transfer
    - FMV of replacement property at the time of receipt
    - Cash boot received (if any)
    - Cash boot paid (if any)
    - Liabilities ASSUMED BY OTHER PARTY (mortgage relief on relinquished — treated as boot received)
    - Liabilities ASSUMED BY USER (debt on replacement — netted against mortgage relief; net relief is boot)
    - Exchange expenses (QI fees, escrow, recording fees, etc.) — adjust amount realized and basis

For multi-asset exchanges (both real property and incidental personal property bundled together), the agent must split: the personal property portion is taxable, the real property portion uses §1031.

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
- **Reverse**: The user (via an Exchange Accommodation Titleholder, "EAT") acquires the replacement property *before* selling the relinquished. Governed by Rev. Proc. 2000-37 safe harbor. Stricter timing: 45 days to identify the property to be relinquished, 180 days to complete the disposition.

Confirm which pattern applies. The pattern affects which boxes in Form 8824 lines 1–9 must be filled.

### Step 3 — Verify the 45-day and 180-day deadlines

Compute days between Line 6 (relinquished transfer) and:
- Line 7 / written identification: must be ≤ 45 calendar days. No weekends/holidays adjustment per IRC §1031(a)(3)(A) — the deadline is hard.
- Line 8 / replacement receipt: must be ≤ 180 calendar days OR the due date of the return for the year of transfer (with extensions), whichever is **earlier**.

If either deadline was missed, **stop**: the exchange does not qualify for deferral. Recognize the entire gain in the year of the relinquished transfer. Surface this clearly to the user before continuing.

### Step 4 — Apply related-party rule (if applicable)

If the exchange was with a related party (per IRC §267(b) or §707(b)(1) — siblings, spouse, ancestors, lineal descendants, controlled entities, etc.):

- Both parties must hold their received property for **at least 2 years** after the date of the last transfer in the exchange.
- If either party disposes within 2 years, the original §1031 deferral is **un-done**: gain is recognized in the year of the disqualifying disposition, on the original exchange.
- Exceptions: death of either party, involuntary conversion, or non-tax-avoidance disposition (limited).

If the user is filing within the 2-year window, Form 8824 Part II must be completed (Line 9 onward). The agent should warn the user that a future disposition within 2 years will reopen the gain.

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
- **Mortgage boot**: if liabilities assumed by other party > liabilities assumed by user, the **net relief** is boot received. If user assumes more debt than other party, there is no mortgage boot (user does not get mortgage boot for paying off more debt — it's netted, not gross).
- Boot received is offset only by boot given of the **same kind** to a limited extent — cash boot paid by user can offset mortgage boot received, but not vice versa. See [`references/boot-rules.md`](./references/boot-rules.md) for the offset matrix.
- If realized loss occurred and boot was received, **no loss is recognized** under §1031 (boot does not trigger loss recognition; the loss is deferred into basis of replacement property).

### Step 7 — Compute basis of replacement property

```
Basis of replacement = Adjusted basis of relinquished
                     + Boot paid (cash + liabilities assumed by user)
                     − Boot received (cash + liabilities assumed by other party)
                     + Recognized gain
                     − Recognized loss (always 0 under §1031)
                     + Exchange expenses (added to basis if not deducted from boot)
```

This basis carries forward. The deferred gain is preserved in this lower-than-FMV basis and will be taxed when the replacement property is eventually sold (unless it's exchanged again under §1031).

### Step 8 — Map computed values to Form 8824 lines

Use [`references/line-by-line.md`](./references/line-by-line.md) for the full mapping. High-level:

- **Part I (Lines 1-7)**: Property descriptions and dates
- **Part II (Lines 8-11)**: Related-party information (only if applicable)
- **Part III (Lines 12-25)**: Realized gain/loss, recognized gain, basis of replacement
- **Part IV**: Conflict-of-interest exception for federal officers (rare; do not engage unless user is in this category)

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms the user will need:

- **Recognized gain on Line 22** flows to:
  - Schedule D + Form 8949 if the property was a capital asset (rare for §1031, since the property must be held for trade/business or investment use)
  - Form 4797 if the property was business-use real estate (most common for §1031). Specifically Line 22 of Form 8824 enters Form 4797 Part III line 30 or Part I/II as appropriate.
- **Depreciation recapture** under §1250 (real property) is potentially recognized to the extent of boot received — see [`references/depreciation-recapture.md`](./references/depreciation-recapture.md).
- **State return**: many states conform to §1031, but California has a "clawback" — if California-source property is exchanged for out-of-state property, FTB Form 3840 must be filed annually until the deferred gain is recognized. Other states have variations. Flag for the user.
- **Future sale of replacement**: the deferred gain is embedded in the carryover basis. Set a reminder in the user's tax records that this property has a tax basis lower than its FMV by the deferred gain amount.

### Step 12 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). Form 8824 is supported on most paid tax software but **not on IRS Direct File** as of early 2026. IRS Free File Fillable Forms (FFFF) supports it.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level summary below.

### Part I — Information on the Like-Kind Exchange (Lines 1-7)

- **Line 1** — Description of like-kind property given up (relinquished). Include address and brief description ("rental SFH at 123 Main St, Phoenix AZ").
- **Line 2** — Description of like-kind property received (replacement). Same format.
- **Line 3** — Date like-kind property given up was originally acquired (MM/DD/YYYY).
- **Line 4** — Date you actually transferred property given up (MM/DD/YYYY).
- **Line 5** — Date like-kind property you received was identified in writing (MM/DD/YYYY). Must be ≤ 45 days after Line 4.
- **Line 6** — Date you actually received like-kind property (MM/DD/YYYY). Must be ≤ 180 days after Line 4.
- **Line 7** — Was the exchange of property given up or received made with a related party? Yes/No checkbox. If Yes, complete Part II.

### Part II — Related-Party Exchange (Lines 8-11)

Only fill if Line 7 is Yes. Asks for:
- **Line 8** — Related party's name, address, and SSN/EIN/ITIN
- **Line 9** — Relationship (lineal descendant, sibling, controlled corporation, etc.)
- **Line 10** — During this tax year, did either party sell or dispose of the property involved? If Yes and within 2 years of original exchange, the deferral may be undone.
- **Line 11** — If Line 10 is Yes, check exception (death, involuntary conversion, no tax-avoidance purpose) or recognize gain now.

### Part III — Realized Gain or (Loss), Recognized Gain, and Basis of Like-Kind Property Received (Lines 12-25)

Highest-friction part. Lines 12-14 handle "non-like-kind" property received (rare under post-TCJA real-property-only rule, but possible if part of the deal was personal property bundled with the real estate). Lines 15-25 are the core §1031 math.

- **Line 12** — FMV of OTHER (non-like-kind) property given up
- **Line 13** — Adjusted basis of OTHER property given up
- **Line 14** — Gain or loss on OTHER property given up (Line 12 − Line 13). This portion is **always recognized**, regardless of §1031 eligibility for the rest.
- **Line 15** — Cash received, FMV of other property received, plus net liabilities assumed by other party, less exchange expenses paid. (This is "boot received".)
- **Line 16** — FMV of like-kind property you received
- **Line 17** — Add Lines 15 + 16
- **Line 18** — Adjusted basis of like-kind property given up, net amounts paid to other party, plus net liabilities assumed by you, plus other exchange expenses (the user's "give" side)
- **Line 19** — Realized gain or (loss). Subtract Line 18 from Line 17.
- **Line 20** — Smaller of Line 15 or Line 19, but not less than zero. (This is recognized gain attributable to boot received.)
- **Line 21** — Ordinary income under recapture rules (depreciation recapture if applicable). See [`references/depreciation-recapture.md`](./references/depreciation-recapture.md).
- **Line 22** — Recognized gain. Add Line 21 + (Line 20 − Line 21 if positive, else 0). Reported on Schedule D / Form 4797 / Form 8949 as appropriate.
- **Line 23** — Recognized gain. Same as Line 22 (carries the recognized gain).
- **Line 24** — Deferred gain or (loss). Subtract Line 23 from Line 19. This is the gain pushed into the basis of replacement.
- **Line 25** — Basis of like-kind property received. Line 18 − Line 15 + Line 23. (Equivalent algebraic forms exist; the IRS form does it this way.)

### Part IV — Federal Conflict-of-Interest Exchanges

Do not engage unless the user is a federal officer required to divest under a Certificate of Divestiture issued by the Office of Government Ethics. Out of scope for the typical filer.

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
- [ ] Line 22 = Line 20 + Line 21 (with Line 21 being recapture portion, not double-counted)
- [ ] Line 24 = Line 19 − Line 23 (deferred gain or loss)
- [ ] Line 25 (basis of replacement) reconciles: Line 18 + recognized gain − boot received

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Realized loss (Line 19 negative) AND boot was received → user should know the loss is **deferred into replacement basis**, not recognized currently
- [ ] Replacement FMV substantially higher than relinquished FMV with no cash boot paid → confirm with user; usually the user paid additional cash, which is boot **paid** (good — it adds to basis)
- [ ] Mortgage relief (debt assumed by other party) > debt user assumed on replacement → net mortgage boot received; flag for inclusion in Line 15
- [ ] Property was held < 1 year before exchange → §1031 still applies if held for investment/business use, but a holding-period question may arise; inform the user
- [ ] User claims residential primary residence as relinquished property → §121 (home sale exclusion) governs, NOT §1031. Stop and redirect.
- [ ] Replacement is held for personal use (vacation home not rented) → fails §1031 "held for productive use in trade or business or for investment" requirement. Rev. Proc. 2008-16 provides a safe harbor for vacation property: must be rented at FMV at least 14 days/year for 2 years and personal use ≤ 14 days/year or 10% of rental days, whichever is greater.
- [ ] Exchange was with a related party AND user is filing within 2 years of exchange → flag for Part II Line 10 recurring obligation
- [ ] Depreciation taken on relinquished property exceeded straight-line → unrecaptured §1250 gain possibly triggered; see [`references/depreciation-recapture.md`](./references/depreciation-recapture.md)

### Cross-form checks

- [ ] If Line 22 (recognized gain) > 0, Form 4797 (or Schedule D + 8949) must be attached and reflect the same amount
- [ ] If user took depreciation on relinquished property, depreciation recapture under §1245 (rare for real property unless qualified improvement property) or unrecaptured §1250 gain may apply on Line 21
- [ ] State return: California requires Form 3840 if relinquished was CA-source and replacement is non-CA. Other states with "clawback" rules: Oregon, Massachusetts, Montana — verify per-state at filing.
- [ ] If cash boot was received, the user owes federal tax on Line 22 and possibly state tax — surface for estimated-tax planning.

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
8. Name, address, ID of related party
9. Relationship
10. Disposed during this year?  Yes | No
11. Exception (if Line 10 = Yes): death | involuntary conversion | non-tax-avoidance | none → recognize now

## Part III — Realized Gain, Recognized Gain, and Basis
12. FMV of OTHER (non-like-kind) property given up:  $X,XXX
13. Adjusted basis of OTHER property given up:       $X,XXX
14. Gain/(loss) on OTHER property (Line 12 − 13):    $X,XXX  (always recognized)
15. Cash + FMV of other property received + net liabilities assumed by other party
    less exchange expenses (boot received):           $X,XXX
16. FMV of like-kind property you received:           $X,XXX
17. Add lines 15 and 16:                              $X,XXX
18. Adjusted basis of like-kind property given up + net cash/liabilities you paid
    + exchange expenses (your give side):             $X,XXX
19. Realized gain/(loss) (Line 17 − Line 18):         $X,XXX
20. Smaller of Line 15 or Line 19 (≥ 0):              $X,XXX  (boot-attributable gain)
21. Ordinary income under recapture rules:            $X,XXX
22. Recognized gain (Line 21 + max(Line 20 − 21, 0)): $X,XXX  → Form 4797 / Sch D
23. Recognized gain (= Line 22):                      $X,XXX
24. Deferred gain/(loss) (Line 19 − Line 23):         $X,XXX
25. Basis of like-kind property received
    (Line 18 − Line 15 + Line 23):                    $X,XXX

## Required attachments
- [ ] Form 4797 (if Line 22 > 0 and property was business-use real estate)
- [ ] Schedule D + Form 8949 (if Line 22 > 0 and property was investment-use)
- [ ] State 1031 form (e.g., CA FTB 3840 — verify state rules)
- [ ] QI exchange agreement and identification notice (retain for records, not filed)

## Validation summary
- 45-day check: Day NN ≤ 45  ✓ | ✗
- 180-day check: Day NN ≤ 180 ✓ | ✗
- Math: all checks passed | <list failures>
- Sanity warnings: <list>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 8824 (revision date YYYY-MM-DD)
- IRS Instructions for Form 8824 (revision date YYYY-MM-DD)
- IRC §1031 (post-TCJA, real-property-only rule effective for exchanges after 2017-12-31)
- IRC §1031(a)(3) (45-day / 180-day deadlines)
- IRC §1031(f) (related-party 2-year rule)
- Rev. Proc. 2000-37 (reverse exchange safe harbor)
- Rev. Proc. 2008-16 (vacation property safe harbor)
- Treas. Reg. §1.1031(a)-1, §1.1031(b)-1, §1.1031(d)-1, §1.1031(k)-1 (qualified intermediary rules)
- Pub. 544 (Sales and Other Dispositions of Assets)
```

The draft is **not** the final filed form. The user still has to attach it to their Form 1040 (or 1065 / 1120-S / 1041) and reflect Line 22 on the appropriate gain-recognition form (4797 or Schedule D).

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8824 line with examples and edge cases
- [`references/timing-rules.md`](./references/timing-rules.md) — 45-day identification rules (3-property, 200%, 95% rules), 180-day deadline interaction with return due date, weekends/holidays handling
- [`references/boot-rules.md`](./references/boot-rules.md) — Cash boot, mortgage boot, the offset matrix, exchange expenses
- [`references/depreciation-recapture.md`](./references/depreciation-recapture.md) — §1245 vs. §1250, unrecaptured §1250 gain in §1031 exchanges
- [`references/related-party.md`](./references/related-party.md) — IRC §1031(f), 2-year holding rule, exceptions, Part II reporting
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 10 audit-trip mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Form 8824 via FFFF, paper, or generic tax software (loaded only when the user authorizes filing)

## Examples

End-to-end worked Form 8824 walkthroughs. Use these as patterns when the user's situation is similar.

- [`examples/delayed-exchange-no-boot.md`](./examples/delayed-exchange-no-boot.md) — Rental SFH for rental SFH, equal values via QI, no boot, full deferral
- [`examples/delayed-exchange-with-boot.md`](./examples/delayed-exchange-with-boot.md) — Replacement worth less than relinquished; user receives $50,000 cash boot; gain recognized to extent of boot
- [`examples/reverse-exchange.md`](./examples/reverse-exchange.md) — Replacement closed first; Exchange Accommodation Titleholder (EAT) parks title under Rev. Proc. 2000-37 safe harbor

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed.

- [Form 8824 (latest)](https://www.irs.gov/pub/irs-pdf/f8824.pdf) — the form itself
- [Instructions for Form 8824 (latest)](https://www.irs.gov/pub/irs-pdf/i8824.pdf) — line-by-line IRS guidance
- [About Form 8824](https://www.irs.gov/forms-pubs/about-form-8824) — IRS landing page with archive of past revisions
- [Publication 544](https://www.irs.gov/pub/irs-pdf/p544.pdf) — Sales and Other Dispositions of Assets
- IRC §1031 (like-kind exchanges of real property)
- IRC §1031(a)(2) (excluded properties: stocks, bonds, partnership interests, inventory, etc.)
- IRC §1031(a)(3) (45-day / 180-day timing rules for delayed exchanges)
- IRC §1031(b) (gain recognized to extent of boot)
- IRC §1031(d) (basis of replacement property)
- IRC §1031(f) (related-party 2-year holding rule)
- IRC §1245, §1250 (depreciation recapture)
- TCJA §13303 (Public Law 115-97), restricting §1031 to real property for exchanges completed after Dec 31, 2017
- Rev. Proc. 2000-37 (reverse exchange safe harbor)
- Rev. Proc. 2008-16 (vacation-property safe harbor)
- Treas. Reg. §1.1031(a)-1 through §1.1031(k)-1 (qualified intermediary rules, exchange-period rules)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. §1031 exchanges are highly fact-dependent — a single missed deadline, related-party flag, or improper QI structure can invalidate the deferral and trigger immediate gain. The agent invoking this skill should remind the user that the output is a starting point and that any §1031 exchange warrants review by a CPA or 1031-experienced tax attorney before the relinquished transfer date, not after.
