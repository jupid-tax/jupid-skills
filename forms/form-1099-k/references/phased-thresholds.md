# 1099-K Threshold History — ARPA, Notice 2024-85, OBBBA, State Variations

Use this when the user is confused about why the 1099-K threshold "changed three times" or asks why they did or didn't receive a 1099-K below $20,000. Also use when reviewing prior-year forms (2022, 2023, 2024, 2025) where the threshold rules differed.

---

## Federal threshold timeline

### Pre-2022 (the original threshold)

IRC §6050W as enacted in 2008 required a 1099-K only if **both**:

- Gross payments **exceed $20,000**, AND
- Number of transactions **exceeds 200**

This held for tax years through 2021.

### 2022 — American Rescue Plan Act (ARPA) tried to lower it

The American Rescue Plan Act of 2021 amended IRC §6050W to drop the threshold to:

- Gross payments **exceed $600**
- No transaction minimum

This was scheduled to take effect tax year 2022. The change would have generated tens of millions of new 1099-K filings. The IRS, facing operational concerns, **delayed enforcement** for tax year 2022 — Notice 2023-10 kept the original $20,000 / 200 in place.

### 2023 — Second delay

IRS Notice 2023-74 again delayed enforcement, keeping $20,000 / 200 for tax year 2023.

Notice 2023-74 also clarified the **personal-item resale at a loss** rule: gross payments for personal items sold at a loss are not taxable income, and the user can offset the 1099-K amount via Schedule 1 Line 8z + Line 24z to net $0. This guidance survives the OBBBA changes — see [`personal-vs-business.md`](./personal-vs-business.md).

### 2024 — Phased rollout begins

IRS Notice 2024-85 (December 2024) replaced the all-or-nothing transition with a phased rollout:

- Tax year 2024: $5,000 threshold (no transaction minimum)
- Tax year 2025: $2,500 threshold (no transaction minimum)
- Tax year 2026: $600 threshold (no transaction minimum) — would have been the ARPA target
- Tax year 2027 and beyond: $600 threshold

Some PSEs began issuing 1099-Ks at the lower phased thresholds during 2024 and 2025.

### 2025 — OBBBA reverses the phased rollout

The One, Big, Beautiful Bill Act (OBBBA), signed into law July 4, 2025, repealed the ARPA threshold change in IRC §6050W and restored the original $20,000 / 200 threshold permanently.

Key effects:

- **Tax year 2025 onward**: $20,000 / 200 with both conditions required (AND, not OR)
- Notice 2024-85's phased rollout is **superseded** — the $5,000 / $2,500 / $600 schedule no longer applies
- IRS Form 1099-K FAQs were updated November 17, 2025 to reflect the OBBBA reversal: "the dollar limit reverts to $20,000"

### 2026 — current state

For tax year 2026 federal reporting:

- A PSE is required to file 1099-K only if gross payments **exceed $20,000 AND** transactions **exceed 200**
- Both conditions must be met (AND, not OR)
- PSEs may voluntarily issue 1099-Ks below the threshold (some always do; some don't)
- All income remains taxable regardless of whether a 1099-K was issued

Source: [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs) (last updated November 17, 2025), [IRS Fact Sheet FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf), OBBBA Section 112202.

---

## State thresholds (lower than federal)

Several states have their own 1099-K reporting requirements that are lower than the federal $20,000 / 200. PSEs must file 1099-K with the state taxing authority and the recipient if the state threshold is met, even if federal isn't.

| State | Threshold | Transaction minimum |
|-------|-----------|---------------------|
| Rhode Island | $100 | None |
| Massachusetts | $600 | None |
| Maryland | $600 | None |
| Virginia | $600 | None |
| Vermont | $600 | None |
| Montana | $600 | None |
| North Carolina | $600 | None |
| District of Columbia | $600 | None |
| Illinois | $1,000 + 4 transactions | 4 |
| New Jersey | $1,000 | None |
| Arkansas | $2,500 | None |
| Missouri | $1,200 | None |

If the user lives or does business in one of these states, they may receive a 1099-K from a PSE despite being below the federal threshold. The federal reporting on Schedule C / Schedule 1 is the same regardless — the state-trigger 1099-K just means there's documentation.

State thresholds can change year to year. Verify the user's state at the time of filing if it's not on this list.

---

## Voluntary reporting below the threshold

Some PSEs issue 1099-K forms to recipients even when neither the federal nor state threshold is met. Reasons:

- Conservative compliance posture (they'd rather over-issue than under-issue)
- Internal policy of issuing for any account with material activity
- Operational simplification (cheaper to issue all than to filter)

If the user receives a 1099-K below the federal threshold, they still reconcile and report normally. The form's existence isn't determinative — the underlying income's taxability is.

---

## What if the user got a 1099-K they shouldn't have?

If the user received a 1099-K when no threshold (federal or state) was met, the form is correct (PSE issued voluntarily) and just needs to be reconciled like any other 1099-K. There's no "rejection" path.

If the user received a 1099-K with the wrong gross amount, request a corrected form from the PSE. See `reconciliation.md` Section "Corrected forms."

---

## What if the user did NOT get a 1099-K but had reportable income?

All business income is taxable regardless of 1099-K issuance. Two common scenarios:

1. **User was below the federal threshold** ($20,000 / 200 not met) and the PSE didn't voluntarily issue. The user reports all platform income on Schedule C Line 1 from their own records — no 1099-K is required to file, just to document.
2. **User should have received a 1099-K and didn't** (PSE error, lost in mail). The user reports income from their own records and notes the missing 1099-K in their files. If the IRS later sends a CP2000 alleging income reported on a 1099-K the user never saw, the user requests a copy from the PSE and reconciles.

---

## Sources

- IRC §6050W (returns relating to payment card and third-party network transactions)
- IRC §6050W(e) as amended by ARPA (lowered threshold) and OBBBA Section 112202 (reversed)
- IRS Notice 2023-10 (first delay of ARPA threshold)
- IRS Notice 2023-74 (second delay; personal-item resale guidance)
- IRS Notice 2024-85 (phased rollout; superseded by OBBBA)
- OBBBA Section 112202 (restoration of $20,000 / 200)
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs) (Nov 2025 update)
- [IRS Fact Sheet FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf)
