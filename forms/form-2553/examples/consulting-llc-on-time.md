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
Deadline:        01/01/2026 + 2 months 15 days = 03/15/2026 (a Sunday,
                 so 03/16/2026 under IRC §7503; plan on 03/13/2026)
Today:           01/15/2026
Status:          On time (59 days to 03/15/2026)
```

Timely election: no Rev. Proc. 2013-30 header, item I blank, Part IV blank.

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
May 2025 OEWS national median:  $135,980 (BLS series OEUN000000000000015125213)
Geographic:     Delaware, mid-cost — no upward adjustment
Hours/week:     ~45 (down-adjust from full 40hr baseline by 12.5%? No, no adjustment for working > 40)
Experience:     12 years senior — modest upward adjustment but offset by:
Mix:            ~60% billable consulting, 40% sales/admin/non-billable
                Pure billable rate × hours would imply $135-150K wage equivalent;
                non-billable mix reduces effective comp basis
Documented final salary: $80,000

Defense:
- Below national BLS median by ~$56K. Note: this cuts both ways; the memo
  must explain why $80K is what an unrelated firm would pay for his mix of
  duties (IRS reasonable-compensation factors)
- Documented hours/role split
- Non-coastal mid-tier client base (lower billable rates)
- Memo signed and dated 12/15/2025, before 2026 starts

Distribution:   $70,000 (= $150K profit − $80K salary)
```

Marcus signs the reasonable-comp memo and keeps it in his records.

---

## Step 5 — Form 2553 draft

```
HEADER: none (timely election)

PART I — ELECTION INFORMATION (Form 2553, Rev. December 2017)

Name:                                 Chen Consulting, LLC
Address:                              1234 Market Street, Suite 200
                                      Wilmington, DE 19801
A. Employer identification number:    12-3456789
B. Date incorporated:                 06/15/2023
C. State of incorporation:            DE
D. Name/address changed after EIN:    (blank, no change)
E. Effective for tax year beginning:  01/01/2026
F. Selected tax year:
   [X] (1) Calendar year
   [ ] (2) Fiscal year ending
   [ ] (3) 52-53-week year, December
   [ ] (4) 52-53-week year, other month
G. >100 shareholders box:             (blank)
H. Contact: Marcus Chen, Sole Member, (302) 555-1234
I. Late election explanation:         (blank, timely)

Signature of officer:  Marcus Chen (handwritten)
Title:                 Sole Member
Date:                  01/15/2026

PAGE 2 — SHAREHOLDERS' CONSENTS

| # | J. Name & address     | K. Signature / date   | L. Ownership / acquired | M. SSN      | N. Tax yr ends |
|---|-----------------------|-----------------------|-------------------------|-------------|----------------|
| 1 | Marcus Chen           | M. Chen / 01/15/2026  | 100% / 06/15/2023       | XXX-XX-1234 | 12/31          |
|   | 1234 Market St, #200  |                       |                         |             |                |
|   | Wilmington, DE 19801  |                       |                         |             |                |

(Marcus is single, not in a community-property state: no spouse consent required.)

PART II — Selection of Fiscal Tax Year:    Skip (item F box 1)
PART III — QSST Election:                  Skip (no trust shareholder)
PART IV — Late Classification Reps:        Skip (timely; no late classification election)
```

---

## Step 6 — Validation

```
□ Eligibility: PASS
□ Timing: ON TIME (59 days of cushion)
□ Consents: 1 of 1 shareholders signed
□ Math: 100% ownership confirmed
□ Sanity warnings: Salary at $80K is 53% of net profit; IRS factors documented
                   in the memo
□ Form completeness: name, address, A-F and H complete; F box (1) checked;
                     G and I blank; Parts II-IV blank; officer signature present
```

Ready to file.

---

## Step 7 — Filing

Marcus chooses **fax** to Kansas City service center (DE is east-coast).

```
Service center:   Kansas City, MO (855-887-7734) — DE is in Kansas City zone
Date faxed:       01/16/2026, 10:42 AM
Pages sent:       4 (all form pages; pages 3-4 blank)
Fax confirmation: SUCCESSFUL — saved as PDF in records
```

Marcus does not also mail. He keeps the original signed form and the fax report; the CP261 will be the proof of acceptance (a fax report is not on the instructions' list of acceptable proof of filing).

---

## Step 8 — Wait for CP261

```
Day 1   (01/16): Filed via fax
Day 30  (02/15): No CP261 yet — normal, keep waiting
Day 52  (03/09): CP261 acceptance notice received in mail
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
□ DE state unemployment (SUTA): rate and wage base set by the Delaware
  Division of Unemployment Insurance; ASK the user for the assigned rate
□ Quarterly Form 941 filings (Apr 30, Jul 31, Oct 31, Jan 31)
□ Annual Form 940 (Jan 31, 2027)
□ W-2 to Marcus (Jan 31, 2027)
□ Form 1120-S annual return (Mar 15, 2027) — replaces Schedule C
□ Schedule K-1 to Marcus: box 1 ordinary business income (profit after his
  $80K wages and the employer payroll taxes) and box 16 code D distributions;
  the $80K wages go on his W-2, not the K-1
□ Marcus's 2026 Form 1040 reports K-1 income on Schedule E (not Schedule C)
```

---

## Step 10 — State conformity

Delaware automatically conforms to federal S-corp election. No separate state form required.

DE does impose a $300 annual tax on LLCs (not S-corp specific); Marcus pays this regardless of tax election.

If Marcus had been in NY or AR, a separate state election would be required; NJ needs a registration and consent step (see [`../references/state-conformity.md`](../references/state-conformity.md)).

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

1. **Filed early** (about two months before the deadline) — no time pressure, no late-relief paperwork
2. **Reasonable-salary memo prepared in advance** — IRS factors documented before any payroll began
3. **Single channel chosen** (fax) — clean confirmation, no duplicate-filing risk
4. **CP261 saved** — proof of S-corp status for future state, banking, and audit interactions
5. **Post-election setup queued** — payroll provider, quarterly filings, annual 1120-S all on calendar
