# Corporate Exception — Box 6 (Medical) and Box 10 (Attorney) Special Rules

The general rule for 1099 reporting is that payments to corporations (C-corp, S-corp, LLC taxed as either) are **exempt** from 1099 reporting. This is in Reg. §1.6041-3(p)(1).

The Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026, "Reportable payments to corporations") list four 1099-MISC boxes that ARE reportable to corporations:

1. **Box 6 — Medical and health-care payments**
2. **Box 8 — Substitute payments in lieu of dividends or tax-exempt interest**
3. **Box 10 — Gross proceeds paid to attorneys**
4. **Box 11 — Cash payments for fish purchased for resale**

Separately, **attorneys' fees for legal services** are reportable to corporations on **1099-NEC box 1a** ("The exemption from reporting payments made to corporations does not apply to payments for legal services").

This file explains why, when, and how to apply the medical and attorney exceptions, which are the ones small businesses hit.

---

## Why these exceptions exist

The IRS wants visibility into payments to medical providers and attorneys regardless of entity type because:

- **Medical providers** receive substantial payments from employers, insurance, and government programs. The IRS uses 1099-MISC data to cross-check provider income reporting.
- **Attorney settlements** flow through trust accounts and can obscure who got what. Box 10 (gross proceeds) reports the entire settlement amount to the IRS, allowing the IRS to track downstream taxability to plaintiffs.

Both exceptions are codified in regulations:
- Reg. §1.6041-3(p)(1) exempts payments to corporations "except with respect to payments made to a corporation after December 31, 1997 for attorneys' fees, and except a corporation engaged in providing medical and health care services or engaged in the billing and collecting of payments in respect to the providing of medical and health care services." It then excludes tax-exempt (501(c)(3)) and government-owned hospitals and extended care facilities.
- Gross proceeds paid to attorneys are reported under IRC §6045(f) and Reg. §1.6045-5, which apply whatever the attorney's entity type.

---

## Box 6 — Medical and health-care payments

### Who is a "medical or health-care provider"?

Per the Instructions for Forms 1099-MISC and 1099-NEC, Box 6 ("each physician or other supplier or provider of medical or health care services"). Typical providers:

- Physicians (MD, DO)
- Dentists, orthodontists, periodontists
- Hospitals (corporate or not — REPORTABLE), except 501(c)(3) tax-exempt and government-owned hospitals and extended care facilities
- Outpatient clinics, ambulatory surgery centers
- Diagnostic centers, laboratories
- Nursing homes, assisted-living facilities
- Physical therapy, occupational therapy
- Mental-health practitioners (psychiatrists, psychologists, counselors, therapists)
- Chiropractors
- Acupuncturists
- Suppliers of medical or health-care services whose charges include drugs, injections, dentures and similar items (the entire payment is reportable)

### What payments are included?

Payments for services rendered. Examples:
- Doctor's office visit fee
- Hospital bill for an inpatient stay
- Lab work invoice
- Mental health session fee
- Payments by a health insurer to a provider under a health, accident, or sickness program

### What payments are excluded?

- **Insurance premiums** — not payments for medical services
- **Payments to pharmacies for prescription drugs** — the instructions say these are not required
- **Payments to 501(c)(3) or government-owned hospitals and extended care facilities** — Reg. §1.6041-3(p)(1)
- **Health FSA / HRA payments** — exempt from §6041 reporting (Instructions, Box 6 caution)
- **Pure goods sales** (e.g., buying medical equipment from a non-service vendor) — payments for merchandise are not reportable (Reg. §1.6041-3(c))

### Threshold

$600 per provider for 2025 payments; $2,000 for 2026 payments (P.L. 119-21 §70433), aggregated across all payments in the calendar year.

### Common scenarios

**Scenario 1: Business pays a doctor for an executive's annual physical**
- The business pays the doctor's office (a corporate professional medical group LLC taxed as S-corp)
- $1,200 paid in the year
- Box 6 reportable: **YES for 2025 payments** (≥ $600; corporate exemption does not apply); **No for 2026 payments** ($1,200 < $2,000)

**Scenario 2: Workers' compensation payment to physical therapist**
- Self-insured employer pays a corporate PT clinic $3,400 for treatment of an injured worker
- Box 6 reportable: **YES** (above both years' thresholds)

**Scenario 3: Pharmacy charges**
- Same employer pays a pharmacy chain $2,800 for prescriptions reimbursed under a workers' comp plan
- Box 6 reportable: **No** (payments to pharmacies for prescription drugs are not required)

**Scenario 4: Health insurance premium**
- Employer pays Blue Cross $80,000 in premiums
- Box 6 reportable: **No** (insurance premiums are excluded)

---

## Box 10 — Gross proceeds paid to attorney

### Who is an "attorney"?

The instructions: "The term 'attorney' includes a law firm or other provider of legal services," regardless of entity structure:
- Solo practitioner attorney
- Law firm partnership
- Law firm professional corporation (PC), professional LLC (PLLC)
- Law firm corporation (some states allow)

### What payments are included in Box 10?

**Gross proceeds** = payments made to an attorney in the course of the payer's trade or business in connection with legal services, but **not for the attorney's services to the payer** — for example, a settlement paid to the claimant's attorney — **before** the attorney deducts their fee (IRC §6045(f); Reg. §1.6045-5).

The attorney is essentially a conduit; Box 10 reports the amount paid to the attorney, not what the attorney kept.

Example: $50,000 settlement.
- Attorney keeps $20,000 as their fee (1/3 contingency).
- Attorney remits $30,000 to plaintiff.
- Box 10 to attorney: **$50,000** (gross — the full pass-through amount)

### What payments are NOT in Box 10?

Box 10 is for *gross proceeds*. Fees the payer pays an attorney for legal services provided **to the payer** go on **1099-NEC box 1a** ($600 for 2025, $2,000 for 2026 payments), **including when the law firm is a corporation**.

When the payer pays a settlement to the claimant's attorney, the payer does **not** report the claimant's attorney's fees at all: "Generally, you are not required to report the claimant's attorney's fees" (Instructions, "Gross proceeds paid to attorneys").

So for the same $50,000 settlement above, whatever the firm's entity type:
- 1099-MISC to the attorney: Box 10 = $50,000
- No 1099-NEC to the attorney for the $20,000 fee
- 1099-MISC to the claimant: Box 3 = $50,000 if the damages are taxable (none if they are non-punitive personal physical injury damages)

### Threshold

$600 per attorney per year, for both 2025 and 2026 payments (§6045(f) was not changed by P.L. 119-21).

### Common scenarios

**Scenario 1: Insurance company pays settlement to plaintiff via plaintiff's attorney**
- Liberty Insurance pays $75,000 settlement to attorney's trust account on behalf of plaintiff Jane.
- Attorney's contingency fee: $25,000. Disbursed to plaintiff: $50,000.
- Liberty issues:
  - 1099-MISC to attorney, **Box 10 = $75,000** (gross proceeds)
  - 1099-MISC to Jane, **Box 3 = $75,000** if the damages are taxable (the full amount, not Jane's $50,000 net; Reg. §1.6045-5(f), Example 3 and Reg. §1.6041-1(f))
  - No 1099-NEC to the attorney for the $25,000 fee

If the entire settlement was for personal physical injury (no punitive damages), Jane's damages are excluded under IRC §104(a)(2) and Liberty files **no** return for Jane — but still issues the 1099-MISC to the attorney for Box 10 (Reg. §1.6045-5(f), Example 2).

**Scenario 2: Business settles a commercial dispute, pays plaintiff directly**
- ABC Corp pays $40,000 directly to plaintiff (no attorney trust account involved)
- Plaintiff has an attorney but the attorney didn't receive the funds
- 1099-MISC to plaintiff, Box 3 = $40,000
- No Box 10 to attorney (because attorney didn't receive the funds)

**Scenario 3: Business pays attorney for legal services (not settlement-related)**
- ABC Corp pays its corporate attorney (a professional corp) $15,000 for ongoing legal work — drafting contracts, regulatory filings
- 1099-MISC Box 10: **No** (these are fees for services to ABC, not gross proceeds)
- 1099-NEC box 1a: **YES, $15,000** — the corporate exemption does not apply to payments for legal services (above both the $600 (2025) and $2,000 (2026) thresholds)

---

## How to verify entity status without falling into the corporate exemption trap

### Step 1: Get the W-9

Always request a current W-9 (Form W-9, Request for Taxpayer Identification Number and Certification, Rev. March 2024). The W-9 has Line 3a entity-type checkboxes. Save it.

### Step 2: Read W-9 Line 3a carefully

| W-9 Line 3a box | Standard 1099-NEC reporting? | Box 6 (medical) reporting? | Box 10 (attorney) reporting? |
|----------------|------------------------------|----------------------------|------------------------------|
| Individual / sole prop / SMLLC | Yes | Yes (if medical provider) | Yes (if attorney) |
| C Corp | No | **Yes** | **Yes** |
| S Corp | No | **Yes** | **Yes** |
| Partnership | Yes | Yes (if medical) | Yes (if attorney) |
| Trust / estate | Yes | Yes | Yes |
| LLC taxed as C, S, or P | Follows the underlying classification | **Yes** for medical or attorney regardless | **Yes** for medical or attorney regardless |

### Step 3: Apply the right form / box

For a corporate medical provider paid $5,000:
- 1099-MISC Box 6 = $5,000 ✓
- 1099-NEC = nothing (corporate exemption applies to NEC; only MISC Box 6 has the special rule)

For a corporate law firm receiving $50,000 in settlement gross proceeds:
- 1099-MISC Box 10 = $50,000 ✓
- 1099-NEC = nothing (the payer does not report the claimant's attorney's fees)

For a corporate law firm paid $15,000 in fees for legal work done for the payer:
- 1099-NEC box 1a = $15,000 ✓ (no corporate exemption for legal services)

---

## Common mistakes

1. **Excluding hospital from Box 6 because hospital is a corporation** — wrong; hospitals (and any medical / health-care provider) are reportable on Box 6 regardless of entity, unless the hospital is 501(c)(3) tax-exempt or government-owned.
2. **Putting only the attorney's fee on Box 10** — Box 10 is gross. If $50K was paid to the claimant's attorney, Box 10 = $50K, not the $20K fee, and the payer issues no 1099-NEC for the fee.
3. **Skipping 1099-MISC for medical because "we already 1099 nothing for our corporate vendors"** — the rule is different for medical and attorney. Don't apply the standard corporate exemption blindly.
4. **Treating insurance premiums as Box 6** — premiums go to the insurer, not to a medical provider. Insurance premiums are not 1099-MISC reportable to the insurance carrier under standard rules.
5. **Issuing 1099-NEC instead of 1099-MISC Box 10 for a settlement** — settlement gross proceeds go on Box 10 of 1099-MISC, not box 1a of 1099-NEC.
6. **Skipping 1099-NEC for the payer's own corporate law firm** — fees for legal services provided to the payer are reportable on 1099-NEC box 1a even when the firm is a corporation.
