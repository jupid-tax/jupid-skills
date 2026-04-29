# Corporate Exception — Box 6 (Medical) and Box 10 (Attorney) Special Rules

The general rule for 1099 reporting is that payments to corporations (C-corp, S-corp) are **exempt** from 1099 reporting. This is in Reg. §1.6041-3(c).

But there are two exceptions where corporate payees ARE reportable on 1099-MISC:

1. **Box 6 — Medical and health-care payments**
2. **Box 10 — Gross proceeds paid to attorneys**

This file explains why, when, and how to apply each exception.

---

## Why these exceptions exist

The IRS wants visibility into payments to medical providers and attorneys regardless of entity type because:

- **Medical providers** receive substantial payments from employers, insurance, and government programs. The IRS uses 1099-MISC data to cross-check provider income reporting.
- **Attorney settlements** flow through trust accounts and can obscure who got what. Box 10 (gross proceeds) reports the entire settlement amount to the IRS, allowing the IRS to track downstream taxability to plaintiffs.

Both exceptions are codified in regulations:
- Box 6 medical exception: Reg. §1.6041-3(c) (corporate exemption) is *limited* by §6041(a)(1) and elaborated in IRS instructions. The instructions specifically state medical and health-care payments to corporations are reportable.
- Box 10 attorney exception: **Reg. §1.6041-1(d)(2)** explicitly carves out attorneys from the general corporate exemption.

---

## Box 6 — Medical and health-care payments

### Who is a "medical or health-care provider"?

Per IRS instructions for Form 1099-MISC and Pub. 535:

- Physicians (MD, DO)
- Dentists, orthodontists, periodontists
- Hospitals (corporate or not — REPORTABLE)
- Outpatient clinics, ambulatory surgery centers
- Diagnostic centers, laboratories
- Nursing homes, assisted-living facilities
- Physical therapy, occupational therapy
- Mental-health practitioners (psychiatrists, psychologists, counselors, therapists)
- Chiropractors
- Acupuncturists
- Veterinarians (for business animals)
- Suppliers of durable medical equipment (when payment is for services + supply, not pure sale)

### What payments are included?

Payments for services rendered. Examples:
- Doctor's office visit fee
- Hospital bill for an inpatient stay
- Lab work invoice
- Mental health session fee
- Veterinary services for a guard dog (business animal)

### What payments are excluded?

- **Insurance premiums** — those are paid to insurance carriers and reported separately
- **Pharmacy / prescription** — sale of goods, not services
- **Employee health plan contributions** — flow through payroll system, not 1099
- **HRA / FSA reimbursements to employees** — payroll-side
- **Pure goods sales** (e.g., buying medical equipment from a non-service vendor) — sale of goods is not 1099 reportable

### Threshold

$600 per provider per calendar year, aggregated across all payments.

### Common scenarios

**Scenario 1: Business pays a doctor for an executive's annual physical**
- The business pays the doctor's office (a corporate professional medical group LLC taxed as S-corp)
- $1,200 paid in the year
- Box 6 reportable: **YES** (corporate exemption does not apply)

**Scenario 2: Workers' compensation payment to physical therapist**
- Self-insured employer pays a corporate PT clinic $3,400 for treatment of an injured worker
- Box 6 reportable: **YES**

**Scenario 3: Pharmacy charges**
- Same employer pays a pharmacy chain $2,800 for prescriptions reimbursed under a workers' comp plan
- Box 6 reportable: **No** (sale of goods, not services)

**Scenario 4: Health insurance premium**
- Employer pays Blue Cross $80,000 in premiums
- Box 6 reportable: **No** (insurance premiums are excluded)

---

## Box 10 — Gross proceeds paid to attorney

### Who is an "attorney"?

Any individual or entity practicing law and admitted to the bar, regardless of entity structure:
- Solo practitioner attorney
- Law firm partnership
- Law firm professional corporation (PC), professional LLC (PLLC)
- Law firm corporation (some states allow)

### What payments are included in Box 10?

**Gross proceeds** = the entire amount of a settlement, judgment, or other payment that passed through the attorney's trust account, **before** the attorney deducts their fee.

This is unique. The attorney is essentially a conduit; Box 10 reports the amount that landed in the conduit, not what the attorney kept.

Example: $50,000 settlement.
- Attorney keeps $20,000 as their fee (1/3 contingency).
- Attorney remits $30,000 to plaintiff.
- Box 10 to attorney: **$50,000** (gross — the full pass-through amount)

### What payments are NOT in Box 10?

Box 10 is for *gross proceeds*. Payments for the attorney's *services* (their fee component) go on **1099-NEC Box 1** if the attorney is an individual / SMLLC / partnership, or are exempt if the attorney is a corporation (since 1099-NEC follows the standard corporate exemption — only Box 10 has the special anti-exemption rule).

So for the same $50,000 settlement above:
- Attorney is an SMLLC: 1099-MISC Box 10 = $50,000; 1099-NEC Box 1 = $20,000
- Attorney is a PC (professional corporation): 1099-MISC Box 10 = $50,000; 1099-NEC = NOT issued (corporate exemption applies to 1099-NEC; only Box 10 exception is in 1099-MISC)

### Threshold

$600 per attorney per year.

### Common scenarios

**Scenario 1: Insurance company pays settlement to plaintiff via plaintiff's attorney**
- Liberty Insurance pays $75,000 settlement to attorney's trust account on behalf of plaintiff Jane.
- Attorney's contingency fee: $25,000. Disbursed to plaintiff: $50,000.
- Liberty issues:
  - 1099-MISC to attorney, **Box 10 = $75,000** (gross proceeds)
  - 1099-MISC to Jane, **Box 3 = $50,000** (plaintiff's portion, taxable as "Other income"; NOT excluded under §104 if not for personal physical injury)
  - 1099-NEC to attorney, **Box 1 = $25,000** (attorney's fee for services) — only if attorney is non-corporate

If the entire settlement was for personal physical injury, Jane's portion may be excluded from income under IRC §104(a)(2) — but Liberty still issues the 1099-MISC to the attorney for Box 10 (the gross proceeds reporting is independent of the recipient's tax treatment).

**Scenario 2: Business settles a commercial dispute, pays plaintiff directly**
- ABC Corp pays $40,000 directly to plaintiff (no attorney trust account involved)
- Plaintiff has an attorney but the attorney didn't receive the funds
- 1099-MISC to plaintiff, Box 3 = $40,000
- No Box 10 to attorney (because attorney didn't receive the funds)

**Scenario 3: Business pays attorney for legal services (not settlement-related)**
- ABC Corp pays its corporate attorney (a professional corp) $15,000 for ongoing legal work — drafting contracts, regulatory filings
- 1099-MISC Box 10: **No** (this isn't a settlement; no "gross proceeds")
- 1099-NEC: **No** (attorney is a corporation, exempt from 1099-NEC)
- Net: no 1099 issued. The attorney reports the income on the corporation's return.

---

## How to verify entity status without falling into the corporate exemption trap

### Step 1: Get the W-9

Always request a current W-9 (Form W-9, Request for Taxpayer Identification Number and Certification). The W-9 has Line 3 entity-type checkboxes. Save it.

### Step 2: Read W-9 Line 3 carefully

| W-9 Line 3 box | Standard 1099-NEC reporting? | Box 6 (medical) reporting? | Box 10 (attorney) reporting? |
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
- 1099-NEC = nothing (corporation, exempt from NEC)

---

## Common mistakes

1. **Excluding hospital from Box 6 because hospital is a corporation** — wrong; hospitals (and any medical / health-care provider) are reportable on Box 6 regardless of entity.
2. **Putting attorney's fee on Box 10 instead of just gross proceeds** — Box 10 is gross. The fee portion (if non-corporate) goes on 1099-NEC. If the entire $50K passed through the attorney trust, Box 10 = $50K (the full $50K), not just the $20K fee.
3. **Skipping 1099-MISC for medical because "we already 1099 nothing for our corporate vendors"** — the rule is different for medical and attorney. Don't apply the standard corporate exemption blindly.
4. **Treating insurance premiums as Box 6** — premiums go to the insurer, not to a medical provider. Insurance premiums are not 1099-MISC reportable to the insurance carrier under standard rules.
5. **Issuing 1099-NEC instead of 1099-MISC Box 10 for a settlement** — settlement gross proceeds go on Box 10 of 1099-MISC, not Box 1 of 1099-NEC. The fee portion may go on 1099-NEC separately, but the gross is always Box 10.
