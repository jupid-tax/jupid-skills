# W-9 vs W-8BEN vs W-8BEN-E — Quick reference

When the user is unsure which form to give to a requestor.

---

## The three forms

| Form | Used by | Purpose |
|------|---------|---------|
| **W-9** | US persons | Provide TIN to a US payor |
| **W-8BEN** | Non-resident alien individuals | Certify foreign status; claim treaty benefits if applicable |
| **W-8BEN-E** | Foreign entities (non-US corporations, partnerships, trusts) | Certify foreign status; claim treaty benefits if applicable |
| (Other W-8s exist for specific cases — W-8ECI, W-8EXP, W-8IMY — out of scope here) |

---

## Decision rule

```
Is the filer a US person?
  Yes → W-9
  No → ask: individual or entity?
    Individual → W-8BEN
    Entity → W-8BEN-E
```

### Who is a "US person" for W-9 purposes?

US person = ANY of:
- US citizen
- US resident alien (green card holder OR substantial-presence test)
- US partnership (formed under US law)
- US corporation (formed under US law)
- US LLC (formed in any US state)
- US estate or domestic trust (defined under §7701(a)(31))

### Who is a "non-resident alien" for W-8BEN purposes?

Non-resident alien = an individual who is NOT a US citizen AND fails BOTH:
- Green card test (no lawful permanent resident status)
- Substantial presence test (didn't spend enough days in the US — calculated via a formula in IRS Pub 519)

### Who is a "foreign entity" for W-8BEN-E purposes?

Foreign entity = a corporation, partnership, trust, or other entity formed under the laws of a country OTHER than the US (or a US territory).

---

## Consequences of using the wrong form

### US person sends W-8BEN (wrong)

The requestor treats the user as a non-resident alien. Result:

- **NRA tax withholding (IRC §1441)** — the requestor withholds 30% from gross payments (not 24% BUW)
- **The user gets a 1042-S, not a 1099-NEC**, at year-end
- **The user has to file Form 1040-NR or amend to a US return** to recover the over-withholding — cumbersome process
- **Treaty benefits don't apply** — most US-tax treaties require the claimant to actually be a tax resident of the treaty country, which a US person is not

This mistake is rare but happens with dual citizens, recent green-card holders, or US persons living abroad who confuse "I live abroad" with "I'm a non-resident alien."

### Non-resident alien sends W-9 (wrong)

The requestor treats the user as a US person. Result:

- **Backup withholding may apply** at 24% if the requestor's system flags the SSN/ITIN as missing or mismatched
- **The user gets a 1099, not a 1042-S** — IRS database mismatch likely
- **The user files US tax return as if a US person** — incorrect filing status
- **Possible criminal liability** for false certification (the W-9 Part II certifies "I am a US person")

The W-9 is a sworn declaration. A non-US person signing a W-9 commits perjury. This mistake is also serious for visa-holders whose work authorization depends on accurate tax classification.

---

## Borderline cases

Cases where the agent should NOT proceed without the user clarifying their tax residency:

1. **Recent green-card holder** — green card means they ARE a US resident alien; W-9. But if the W-9 is for a payment made before the green card was issued, the user was an NRA at the time and W-8BEN would have been correct. Going forward (post-green-card): W-9.

2. **Dual citizen (US + another country)** — US citizenship makes them a US person regardless of where they live; W-9.

3. **F-1 / J-1 visa holder** — usually NRA in their first 5 calendar years (per substantial-presence rules carving out students); W-8BEN. After 5 years they may pass substantial presence; switch to W-9.

4. **H-1B / L-1 visa holder** — usually NRA in year 1 of US presence, often becomes resident alien in year 2+ via substantial presence; depends on days present in US. Verify before completing.

5. **US LLC owned by a foreign person** — LLC itself is a US entity, but if it's an SMLLC default-disregarded, the IRS treats payments as going to the foreign owner. This requires W-8BEN (not W-9), because the disregarded entity transparency means the foreign owner is the actual recipient. SMLLC + S-corp election = entity is taxed as a corporation and gives W-9 (LLC name + LLC's EIN).

6. **US person living abroad full-time** — STILL a US person if US citizen or green-card holder. W-9 (not W-8BEN), regardless of residence.

7. **Person who recently became a US resident** — date matters. If the W-9 covers payments made before residency, those were NRA payments and W-8BEN would have been correct. Use the form that matches the user's status at the time of payment.

---

## What the agent does in borderline cases

1. **Ask explicitly:** "Are you a US citizen, green-card holder, or have you spent enough days in the US under the substantial-presence test to be a US resident alien for tax purposes?"

2. **If unsure:** Pause and recommend the user check with a CPA or look at their last tax return — were they filing as a US person (Form 1040) or NRA (Form 1040-NR)?

3. **If still unsure:** Don't guess. Wrong form has tax + legal consequences. Recommend professional advice.

---

## Form W-8BEN (when applicable)

If the user is a non-resident alien individual, redirect to the (forthcoming) `form-w8ben` skill. The W-8BEN:

- IRS form: https://www.irs.gov/pub/irs-pdf/fw8ben.pdf
- Used to certify foreign status for IRC §1441 withholding purposes
- May be used to claim a reduced withholding rate under a tax treaty
- Valid for 3 years from signing (W-9 has no expiration but is often re-collected annually)

## Form W-8BEN-E (when applicable)

If the user is a foreign entity, redirect to the (forthcoming) `form-w8bene` skill. The W-8BEN-E:

- IRS form: https://www.irs.gov/pub/irs-pdf/fw8bene.pdf
- 8 pages, much more complex than W-9 or W-8BEN
- Required for FATCA classification of foreign entities
- Filed to certify status as a beneficial owner under Chapter 3 and Chapter 4 (FATCA) regimes

---

## Sources

- IRS Form W-9 — https://www.irs.gov/forms-pubs/about-form-w-9
- IRS Form W-8BEN — https://www.irs.gov/forms-pubs/about-form-w-8-ben
- IRS Form W-8BEN-E — https://www.irs.gov/forms-pubs/about-form-w-8-ben-e
- IRS Publication 519 — US Tax Guide for Aliens (substantial presence test, residency rules)
- IRC §1441 — Withholding of tax on nonresident aliens
- IRC §3406 — Backup withholding
- IRC §6109 — TIN furnishing requirement
- IRC §7701(a)(31) — Definition of US person and foreign person
