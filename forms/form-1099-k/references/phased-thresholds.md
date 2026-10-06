# 1099-K Threshold History — ARPA, Notice 2024-85, OBBBA, State Variations

The federal de minimis test below applies only to **third party network transactions** reported by a third party settlement organization (TPSO). **Payment card transactions have no minimum**: a merchant acquirer reports every card payment (Instructions for Form 1099-K, Rev. December 2026, Box 1a; IRS FS-2025-08, Third party filers Q7).

Use this when the user is confused about why the 1099-K threshold "changed three times" or asks why they did or didn't receive a 1099-K below $20,000. Also use when reviewing prior-year forms (2022, 2023, 2024, 2025) where the threshold rules differed.

---

## Federal threshold timeline

### Pre-2022 (the original threshold)

IRC §6050W as enacted in 2008 required a TPSO to file a 1099-K only if **both**:

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

Notice 2023-74 is about the enforcement delay only. The **personal-item resale at a loss** guidance comes from the IRS Form 1099-K FAQs (FS-2024-03, superseded by FS-2025-08) and the Form 1040 instructions: such sales are not income. For 2022 and 2023 returns, the amount was shown on Schedule 1 Line 8z and offset on Line 24z (or as a positive and negative on Line 8z). **For tax years beginning in 2024**, the combined amount goes in the entry space at the top of Schedule 1 (FS-2025-08, Common situations Q6–Q7). See [`personal-vs-business.md`](./personal-vs-business.md).

### 2024 — Phased rollout begins

IRS Notice 2024-85 replaced the all-or-nothing transition with a phased rollout:

- Tax year 2024: $5,000 threshold (no transaction minimum)
- Tax year 2025: $2,500 threshold (no transaction minimum)
- Tax year 2026: $600 threshold (no transaction minimum) — would have been the ARPA target
- Tax year 2027 and beyond: $600 threshold

Some PSEs began issuing 1099-Ks at the lower phased thresholds during 2024 and 2025.

### 2025 — OBBBA reverses the phased rollout

The One, Big, Beautiful Bill Act (OBBBA, P.L. 119-21), signed into law July 4, 2025, rewrote IRC §6050W(e) in §70432(a) and restored the original $20,000 / 200 threshold. The amendment takes effect "as if included in section 9674 of the American Rescue Plan Act," so it is **retroactive** to ARPA's start date (returns for calendar years after 2021).

Key effects:

- **Every year from 2022 on**: $20,000 / 200 with both conditions required (AND, not OR)
- Notice 2024-85's phased rollout is **superseded** — the $5,000 / $2,500 / $600 schedule never applied
- Backup withholding on TPSO payments applies only when the same $20,000 / 200 test is met (IRC §3406(b)(8), added by P.L. 119-21 §70432(b), calendar years after 2024)
- The IRS announced the change in IR-2025-107 and Fact Sheet FS-2025-08 (Oct. 23, 2025): OBBB "retroactively reinstated the reporting threshold in effect prior to the passage of the American Rescue Plan Act of 2021"

### 2026 — current state

For tax year 2026 federal reporting:

- A TPSO is required to file 1099-K for third party network transactions only if gross payments **exceed $20,000 AND** transactions **exceed 200**
- Both conditions must be met (AND, not OR)
- Payment card transactions (merchant acquirers) have no minimum
- TPSOs may voluntarily issue 1099-Ks below the threshold (FS-2025-08, General information Q5)
- All income remains taxable regardless of whether a 1099-K was issued

Source: Instructions for Form 1099-K (Rev. December 2026), "Exception for de minimis payments"; [IRS Fact Sheet FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) (Oct. 23, 2025); IRC §6050W(e) as amended by P.L. 119-21 §70432.

---

## State thresholds (lower than federal)

Several states have their own 1099-K reporting requirements that are lower than the federal $20,000 / 200 (FS-2025-08, General information Q2). A TPSO files with the state and furnishes the payee a copy when the state threshold is met, even if the federal one isn't.

Verified on 2026-10-06 against state revenue department pages:

| State | TPSO threshold | Source |
|-------|----------------|--------|
| Massachusetts | $600 or more, any number of transactions (payee with a Massachusetts address) | mass.gov/info-details/form-1099-filing-requirements; 830 CMR 62C.8.1 |
| Virginia | $600 or more (payee with a Virginia mailing address) | tax.virginia.gov/news/did-you-receive-1099-k-what-you-need-know |
| Illinois | Four or more transactions and cumulative total over $1,000 (payee with an Illinois address) | Illinois Department of Revenue Publication 110 (January 2026) |
| Vermont | $2,000 or more | tax.vermont.gov/business-and-corp/withholding-tax/1099-k (the 2017 rule was $600) |
| North Carolina | No lower threshold; PSEs send NCDOR duplicates of the federal filings | ncdor.gov notice "Important Information for Payment Settlement Entities" (G.S. 105-251.2(c)) |

Other states (for example Maryland, New Jersey, and the District of Columbia) are often listed with lower thresholds; those were not verified here. Ask the user for the state on the form (Box 6) and check that state's revenue department before stating a number.

If the user lives or does business in a lower-threshold state, they may receive a 1099-K despite being below the federal threshold. The federal reporting on Schedule C / Schedule 1 is the same regardless — the state-trigger 1099-K just means there's documentation.

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

If the user received a 1099-K with the wrong gross amount, request a corrected form from the PSE. See `reconciliation.md` section "Corrected 1099-K workflow."

---

## What if the user did NOT get a 1099-K but had reportable income?

All business income is taxable regardless of 1099-K issuance. Two common scenarios:

1. **User was below the federal threshold** ($20,000 / 200 not met) and the PSE didn't voluntarily issue. The user reports all platform income on Schedule C Line 1 from their own records — no 1099-K is required to file, just to document.
2. **User should have received a 1099-K and didn't** (PSE error, lost in mail). The user reports income from their own records and notes the missing 1099-K in their files. If the IRS later sends a CP2000 alleging income reported on a 1099-K the user never saw, the user requests a copy from the PSE and reconciles.

---

## Sources

- IRC §6050W (returns relating to payment card and third-party network transactions)
- IRC §6050W(e) as amended by ARPA §9674 (lowered threshold) and P.L. 119-21 §70432(a) (restored, retroactive)
- IRC §3406(b)(8) (P.L. 119-21 §70432(b))
- IRS Notice 2023-10 (first delay of ARPA threshold)
- IRS Notice 2023-74 (second delay, calendar year 2023)
- IRS Notice 2024-85 (phased rollout; superseded by P.L. 119-21)
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs) and [IRS Fact Sheet FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) (Oct. 23, 2025; IR-2025-107)
- Instructions for Form 1099-K (Rev. December 2026)
- State pages listed in the table above
