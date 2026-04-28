# Example: On-Time S-Corp Election for Consulting LLC

End-to-end worked example: single-member LLC consulting business, $150,000 net profit, on-time election for tax year 2026. Demonstrates standard election (no Part IV needed), reasonable-salary analysis, SE tax savings calculation, and post-election compliance setup.

---

## Scenario

**Filer**: Marcus Chen, IT consultant
**Entity**: Chen Consulting, LLC (Delaware single-member LLC, formed 2023)
**EIN**: 12-3456789
**Tax history**: Filed Schedule C on personal 1040 for 2023, 2024, 2025
**Profit projection 2026**: $150,000 net profit
**Goal**: Elect S-corp effective 01/01/2026 to reduce SE tax burden

---

## Step 1 — Eligibility check

```
□ Domestic LLC formed under Delaware law              ✓
□ Not bank/insurance/§936/DISC                        ✓
□ Single shareholder (Marcus, U.S. citizen)           ✓ (well under 100 cap)
□ Marcus is U.S. citizen                              ✓
□ Single-member LLC, one class of "stock" by default  ✓
□ Operating agreement reviewed: no waterfalls,        ✓
  no preferred returns, single member receives 100%
  of distributions
□ EIN issued 2023; matches "Chen Consulting, LLC"     ✓
```

All eligibility checks pass. Proceed.

---

## Step 2 — Deadline calculation

Existing entity (filed Schedule C in prior years), calendar tax year, 2026 election.

```
Tax year start:  01/01/2026
Deadline:        01/01/2026 + 2 months 15 days = 03/15/2026
Today:           01/15/2026
Status:          On time (60 days of cushion)
```

Standard election. Part IV not required.

---

## Step 3 — Break-even check

```
Estimated SE tax savings:
  Sole-prop SE tax on $150,000 = $138,525 × 15.3% (capped at SS base) = $21,194
  S-corp FICA on $80,000 salary               = $80,000 × 15.3% = $12,240
  S-corp FICA on $70,000 distribution         = $0
  Net savings:                                  $21,194 − $12,240 = $8,954

Estimated annual compliance overhead:
  Payroll software (Gusto, OnPay):             $600
  DE state UI (low-rate state):                $200
  Bookkeeping increment:                        $1,200
  Form 1120-S preparation (CPA fee):            $1,500
  Total overhead:                               ~$3,500

Net annual benefit:                              $8,954 − $3,500 ≈ $5,400
```

Decisively in favor of electing. Proceed.

---

## Step 4 — Reasonable-salary analysis

```
Role:           Senior IT consultant (own client work, sales, project management)
BLS SOC code:   15-1252 (Software Developers) — closest match
2024 BLS median (national):  $130,160
Geographic:     Delaware, mid-cost — no upward adjustment
Hours/week:     ~45 (down-adjust from full 40hr baseline by 12.5%? No, no adjustment for working > 40)
Experience:     12 years senior — modest upward adjustment but offset by:
Mix:            ~60% billable consulting, 40% sales/admin/non-billable
                Pure billable rate × hours would imply $130-150K wage equivalent;
                non-billable mix reduces effective comp basis
Documented final salary: $80,000

Defense:
- Below national BLS median by ~$50K — conservative posture
- Documented hours/role split
- Non-coastal mid-tier client base (lower billable rates)
- Memo signed and dated 12/15/2025, before 2026 starts

Distribution:   $70,000 (= $150K profit − $80K salary)
```

Marcus signs the reasonable-comp memo and keeps it in his records.

---

## Step 5 — Form 2553 draft

```
HEADER (no Part IV — on-time election; no banner needed)

PART I — ELECTION INFORMATION

A. Name of corporation:               Chen Consulting, LLC
B. Address:                           1234 Market Street, Suite 200
                                      Wilmington, DE 19801
C. Employer Identification Number:    12-3456789
D. Date incorporated:                 06/15/2023
E. State of incorporation:            DE
F. Election effective date:           01/01/2026
G. Contact: Marcus Chen, 1234 Market Street, Suite 200,
            Wilmington, DE 19801, (302) 555-1234
H. Name change:                       (blank — no change)
I. Tax year:
   [X] (1) Calendar year
   [ ] (2) Fiscal year ending
   [ ] (3) 52-53 week year
   [ ] (4) Other

J. Officer signature:  Marcus Chen
   Title:              Sole Member
   Date:               01/15/2026

SHAREHOLDER CONSENT STATEMENT

| # | J. Name & address     | K. Sig.   | L. Date     | M. Shares & dates  | N. SSN     |
|---|-----------------------|-----------|-------------|---------------------|------------|
| 1 | Marcus Chen           | M. Chen   | 01/15/2026  | 100% from 06/15/2023| XXX-XX-1234|
|   | 1234 Market St, #200  |           |             |                     |            |
|   | Wilmington, DE 19801  |           |             |                     |            |

(Marcus is single, not in community-property state — no spouse signature required.)

PART II — Selection of Fiscal Tax Year:    Skip (calendar year)
PART III — QSST Election:                  Skip (no trust shareholder)
PART IV — Late Election Relief:            Skip (on time)
```

---

## Step 6 — Validation

```
□ Eligibility: PASS
□ Timing: ON TIME (60 days cushion)
□ Consents: 1 of 1 shareholders signed
□ Math: 100% ownership confirmed
□ Sanity warnings: Salary at $80K is 53% of net profit — reasonable
                   (Watson factors documented)
□ Form completeness: A-J complete, Line I Box 1 checked, Parts II-IV blank
```

Ready to file.

---

## Step 7 — Filing

Marcus chooses **fax** to Kansas City service center (DE is east-coast).

```
Service center:   Kansas City, MO (855-887-7734) — DE is in Kansas City zone
Date faxed:       01/16/2026, 10:42 AM
Pages sent:       2 (Form 2553 page 1 + page 2)
Fax confirmation: SUCCESSFUL — saved as PDF in records
```

Marcus does not also mail. The fax confirmation is the proof of filing.

---

## Step 8 — Wait for CP261

```
Day 1   (01/16): Filed via fax
Day 30  (02/15): No CP261 yet — normal, keep waiting
Day 52  (03/09): CP261 acknowledgment letter received in mail
                  S-corp effective 01/01/2026 ✓
                  Marcus saves the CP261 letter permanently
```

---

## Step 9 — Post-election setup

By 01/01/2026 (or as soon as CP261 arrives, whichever is later):

```
□ Set up payroll provider (Gusto) with $80,000 annual salary
□ Configure $80,000 / 26 = $3,077 bi-weekly gross pay
□ Federal income tax withholding via W-4 (Marcus elects standard withholding)
□ FICA: 7.65% employer + 7.65% employee = 15.3% combined on $80K = $12,240/yr
□ Federal unemployment (FUTA): 0.6% on first $7,000 = $42/yr
□ DE state unemployment (SUTA): rate ~ 0.3% on first $14,500 = ~$44/yr
□ Quarterly Form 941 filings (Apr 30, Jul 31, Oct 31, Jan 31)
□ Annual Form 940 (Jan 31, 2027)
□ W-2 to Marcus (Jan 31, 2027)
□ Form 1120-S annual return (Mar 15, 2027) — replaces Schedule C
□ Schedule K-1 to Marcus showing $70K distribution + $80K wages
□ Marcus's 2026 Form 1040 reports K-1 income on Schedule E (not Schedule C)
```

---

## Step 10 — State conformity

Delaware automatically conforms to federal S-corp election. No separate state form required.

DE does impose a $300 annual franchise tax on LLCs (not S-corp specific) — Marcus pays this regardless of tax election.

If Marcus had been in NY, NJ, AR, or LA, a separate state form would be required (see [`../references/state-conformity.md`](../references/state-conformity.md)).

---

## Result

```
2026 SE-equivalent tax under sole prop:    $21,194
2026 SE-equivalent tax under S-corp:       $12,240
Compliance overhead:                        $3,500
Net 2026 benefit:                           ~$5,400

Permanent SE-tax savings each year going forward, as long as profit > ~$80K.
At higher profits, savings grow proportionally (capped at SS wage base).
```

---

## Lessons / what went right

1. **Filed early** (60 days before deadline) — no time pressure, no late-relief paperwork
2. **Reasonable-salary memo prepared in advance** — Watson-factors documented before any payroll began
3. **Single channel chosen** (fax) — clean confirmation, no duplicate-filing risk
4. **CP261 saved** — proof of S-corp status for future state, banking, and audit interactions
5. **Post-election setup queued** — payroll provider, quarterly filings, annual 1120-S all on calendar
