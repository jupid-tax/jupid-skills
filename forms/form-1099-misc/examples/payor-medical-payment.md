# Example: Business Paying Medical Provider — Box 6 Corporate Exception

A complete walkthrough of a small business that paid $2,450 to a corporate medical provider for executive physicals, illustrating that the corporate exemption does NOT apply to Box 6 medical payments, and that the 2026 threshold is $2,000.

## The setup

- **Payer**: Trail Bend Provisions LLC (multi-member LLC taxed as partnership; outdoor gear retailer)
- **EIN**: 92-7104XXX
- **Address**: 905 Cascade Way, Bend, OR 97702
- **Tax year**: 2026

## The recipient

- **Name**: Mountain View Medical Group, P.C.
- **Entity**: Professional corporation (PC) — a corporation under federal tax classification
- **TIN**: EIN 91-3852XXX
- **Address**: 2100 Medical Pkwy, Bend, OR 97702
- **W-9 status**: Mountain View provided W-9 (Rev. March 2024) indicating "C corporation" on Line 3a (a PC organized as a C-corp)

## The transaction

Trail Bend's CEO Carla Reyes had her annual executive physical at Mountain View Medical Group on March 15, 2026, and the CFO had his on September 9, 2026. Trail Bend (as the employer) paid Mountain View directly by ACH: $1,200 on April 2, 2026 and $1,250 on September 24, 2026, under the company's executive health benefit policy (not a health FSA or HRA).

Total paid in 2026: **$2,450**.

## Decision: 1099-MISC Box 6 required?

### Step 1: Categorize the payment

This is a **medical / health-care payment** for services rendered (an annual physical). Falls under Box 6.

### Step 2: Apply the threshold

Box 6 threshold for 2026 payments: $2,000 (P.L. 119-21 §70433; Instructions, Rev. December 2026, Box 6). $2,450 ≥ $2,000 → threshold met.

Had Trail Bend paid only the CEO's $1,200, no 1099-MISC would be required for 2026 ($1,200 < $2,000), although the same $1,200 paid in 2025 would have been reportable ($600 threshold).

### Step 3: Apply entity classification rules

Standard rule: payments to corporations are exempt from 1099 reporting (Reg. §1.6041-3(p)(1)).

**BUT** — Box 6 medical payments have a SPECIAL RULE: corporate exemption does NOT apply. From the Instructions for Forms 1099-MISC and 1099-NEC, Box 6: "The exemption from issuing Form 1099-MISC to a corporation does not apply to payments for medical or health care services provided by corporations, including professional corporations."

Mountain View is a corporation (and not a tax-exempt or government hospital), so Box 6 reporting is required.

### Step 4: Trade-or-business

Trail Bend is paying in the course of its trade-or-business (employer paying for employee benefit). Reportable.

**Conclusion**: Trail Bend issues 1099-MISC to Mountain View with Box 6 = $2,450.

## The completed 1099-MISC

```
FORM 1099-MISC (Rev. December 2026), calendar year 2026

PAYER: Trail Bend Provisions LLC
  EIN: 92-7104XXX
  905 Cascade Way
  Bend, OR 97702

RECIPIENT: Mountain View Medical Group, P.C.
  TIN (truncated on Copy B): XX-XXX1234
  Address: 2100 Medical Pkwy, Bend, OR 97702

Account number: TB-MED-2026

Box 1 — Rents:                            $0
Box 2 — Royalties:                        $0
Box 3 — Other income:                     $0
Box 4 — Federal income tax withheld:      $0
Box 5 — Fishing boat proceeds:            $0
Box 6 — Medical / health-care payments:   $2,450.00
Box 7 — Direct sales ≥$5,000:             ☐
Box 8 — Substitute payments:              $0
Box 9 — Crop insurance:                   $0
Box 10 — Gross proceeds to attorney:      $0
(other boxes: $0 / blank)
Box 16 — State tax withheld:              $0
Box 17 — State / Payer's state no.:       OR / <Oregon-assigned payer ID, not the EIN>
Box 18 — State income:                    $2,450
```

## Filing checklist

- [x] Recipient Copy B mailed to Mountain View by **February 1, 2027** (January 31 is a Sunday)
- [x] Copy A filed with IRS via IRIS by **March 31, 2027** (electronic deadline)
- [x] State copy: ask whether Oregon requires a direct filing; check the Oregon Department of Revenue rule instead of assuming CF/SF forwarding covers it
- [x] Records retained: W-9 from Mountain View, ACH transaction record, Mountain View invoice, 1099-MISC Copy C, IRIS submission ID
- [x] No Form 945 needed (no backup withholding)

## How Mountain View reports this

Mountain View Medical Group, P.C. is a C-corp. The $2,450 is professional services revenue, reported on the corporation's **Form 1120** (corporate income tax return) as gross receipts.

The 1099-MISC Box 6 is informational — it cross-checks that Mountain View is reporting the income. Without the 1099-MISC, the IRS would have less visibility into payments to medical corporations.

## What if Trail Bend had skipped the 1099-MISC?

Common error: payer thinks "Mountain View is a PC, so it's a corporation, so I don't issue a 1099." Skipping triggers:

- Penalty under IRC §6721 for returns due in 2027: $60 (corrected within 30 days), $130 (by August 1), $340 (later or never) per form (Rev. Proc. 2025-32 §4.57)
- A separate penalty under IRC §6722 for failure to furnish to the recipient
- Intentional disregard: at least $690 per form, no cap (Rev. Proc. 2025-32 §4.57)

If Trail Bend skips, the IRS's matching system doesn't have the cross-check between Trail Bend's deduction and Mountain View's gross receipts. Mountain View still has to report it (income is taxable regardless), but the IRS loses audit visibility.

## What payments would NOT require a Box 6?

Within Trail Bend's broader medical-related spending, here's what would NOT trigger Box 6:

1. **Health insurance premiums to Blue Cross**: Trail Bend pays $80,000/year in premiums for employee health insurance. NOT Box 6 reportable. Insurance premiums go to the insurance carrier, not directly for medical services. Coverage reporting runs on its own forms (1095-B from insurers; 1094-C / 1095-C from applicable large employers).

2. **Pharmacy purchases**: an employee's prescription refill paid through a pharmacy benefits manager. NOT Box 6 — the instructions say payments to pharmacies for prescription drugs are not required.

3. **Medical equipment purchase**: Trail Bend buys an AED for the office from a medical supply company. NOT Box 6 — sale of goods. Also corporate seller likely.

4. **Health FSA / HRA payments**: NOT Box 6 — exempt from §6041 reporting (Instructions, Box 6 caution).

5. **Payments to a 501(c)(3) tax-exempt or government-owned hospital**: NOT Box 6 (Reg. §1.6041-3(p)(1)).

6. **Payments for medical services to employees as wages**: if the medical benefit is taxable to the employee (rare; certain executive benefits), it would be on the employee's W-2, not on a 1099-MISC.

## What if Mountain View had been a sole-prop physician?

Same outcome on Box 6 ($2,450). The corporate exemption doesn't cover medical providers — Box 6 is reportable to corporations and individuals alike. So the entity type doesn't change the Box 6 conclusion.

The only difference: a sole-prop physician's TIN would be SSN, not EIN. The 1099-MISC would still be issued.

## Why each non-obvious choice

**Why Box 6 instead of Box 3 (other income)?** Box 6 is the dedicated box for medical / health-care services. Box 3 is the catch-all for income that doesn't fit elsewhere. Specific boxes always take priority over Box 3.

**Why not 1099-NEC?** 1099-NEC is for nonemployee compensation in general. But medical / health-care services have their own dedicated box on 1099-MISC (Box 6). Use the more specific form.

**What about the corporate exemption?** Reg. §1.6041-3(p)(1) provides a general exemption for payments to corporations, but carves out corporations providing medical and health care services (and attorneys' fees). The instructions list Boxes 6, 8, 10 and 11 as reportable to corporations. The carve-out is the rule that catches most filers.

**What if a filing platform warns that the recipient is a corporation?** Proceed: Box 6 is correctly reportable to a corporate medical provider.

**What if the executive paid out-of-pocket and Trail Bend reimbursed?** Then Trail Bend isn't paying Mountain View directly — Trail Bend is reimbursing the executive. The reimbursement flows through payroll (taxable to executive if not a qualifying medical reimbursement plan; non-taxable if under an HRA / qualifying plan). NOT Box 6 from Trail Bend to Mountain View. The executive paid Mountain View directly and, as an individual paying a personal medical expense (not in a trade or business), has no 1099-MISC obligation at any amount.

## Sources cited
- IRS Form 1099-MISC, Rev. December 2026 (https://www.irs.gov/pub/irs-pdf/f1099msc.pdf)
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026 (https://www.irs.gov/pub/irs-pdf/i1099mec.pdf), Box 6 and "Reportable payments to corporations"
- IRC §6041 ($2,000 for payments after 2025, P.L. 119-21 §70433; $600 before)
- Reg. §1.6041-3(p)(1) (corporate exemption and its medical-provider exception)
- Rev. Proc. 2025-32 §4.57 (§6721 penalty amounts for returns due in 2027)
