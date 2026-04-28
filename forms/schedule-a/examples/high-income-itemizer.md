# Example: High-Income Itemizer ($400K AGI, Large Mortgage and Charity)

A complete walkthrough of Schedule A for a high-earning couple with a large mortgage near the $750K cap, substantial state and local taxes triggering the SALT high-income phaseout (at $400K they're below it but close), and significant annual charitable giving via a donor-advised fund. This is the canonical "tax-aware professional" pattern.

## The filers

- **Names**: Daniel and Anya Sharma
- **Filing status**: Married Filing Jointly
- **State**: New York (NYC residents, subject to state and city income tax)
- **Tax year**: 2025 (filing in 2026)
- **AGI** (Form 1040 Line 11): $400,000
- **MAGI**: $400,000
- **Standard deduction MFJ 2025**: $30,000

Daniel is a tech product manager (W-2). Anya is a hospital physician (W-2 + a small 1099 consulting practice on Schedule C, separately).

## Inputs gathered

### Medical (Lines 1-4)

A relatively healthy year:

| Item | Amount |
|------|--------|
| Out-of-pocket dental work | $3,200 |
| Prescription medications | $400 |
| Annual physicals (deductibles only) | $600 |
| Vision (LASIK for Daniel — qualifies) | $4,500 |
| **Total Line 1** | **$8,700** |

7.5% × $400,000 = $30,000 floor. Line 4 = max(0, $8,700 − $30,000) = **$0**.

Even with $8,700 of real out-of-pocket spending, the 7.5% floor wipes the deduction out entirely. This is typical for high-AGI filers without major medical events.

### SALT (Lines 5-7)

| Item | Amount |
|------|--------|
| NY state income tax (W-2 box 17 + estimates) | $24,000 |
| NYC personal income tax (W-2 box 19) | $13,500 |
| Real estate (property) tax on Brooklyn co-op | $9,000 |
| Personal property tax | $0 |
| **Sum Line 5d** | **$46,500** |

SALT cap for 2025 = $40,000. MAGI $400,000 < $500,000 threshold → no phaseout.

Line 5e = min($46,500, $40,000) = **$40,000**.

The couple loses $6,500 of SALT deductibility to the cap. (Pre-OBBBA cap of $10K would have lost them $36,500; OBBBA saved them $30,000 of deduction — worth roughly $9,600 at their 32% federal bracket.)

### Mortgage interest (Lines 8-10)

| Item | Amount |
|------|--------|
| Form 1098 box 1 (interest paid) | $32,400 |
| Form 1098 box 6 (points) | $0 |
| Form 1098 box 5 (PMI) | $0 (no PMI; LTV <80% at origination) |
| Loan origination date | 2021-08-22 (post-12/15/2017, $750K cap applies) |
| Loan original principal | $740,000 |
| Loan current balance Jan 1, 2025 | $695,000 |

Loan is within the $750K cap throughout the year — full $32,400 deductible on Line 8a.

If the loan had been $850,000 average balance:

```
Deductible % = $750,000 / $850,000 = 88.24%
Deductible interest = $32,400 × 88.24% = $28,590
$3,810 of interest would be non-deductible.
```

But Daniel and Anya are well within the cap.

No HELOC, no investment interest.

### Charity (Lines 11-14)

The couple makes a planned bunching contribution to a Donor-Advised Fund this year, intending to distribute over the next 4 years:

| Item | Amount |
|------|--------|
| Cash to DAF (Fidelity Charitable) | $30,000 |
| Cash to local food bank | $1,500 |
| Non-cash: appreciated stock (Anya's old employer, held 3 years; FMV at donation) to alma mater | $12,000 |
| Carryover from prior year | $0 |
| **Raw total Line 14** | **$43,500** |

For 2025, no 0.5% AGI floor applies — full $43,500 deducts (subject to AGI ceilings).

### AGI ceiling check

- Cash to public charity (DAF + food bank = $31,500): 60% AGI ceiling = $240,000. Within ceiling. ✓
- Non-cash, long-term capital gain to public charity ($12,000 stock to alma mater): 30% AGI ceiling = $120,000. Within ceiling. ✓

Total well within ceilings; no carryover triggered.

### Form 8283 required?

Yes — non-cash > $500 ($12,000 of appreciated stock).
- Section A: stock is publicly traded, no appraisal required
- Just enter the description, date acquired, FMV, and how FMV was determined

### Casualty (Line 15)

None.

### Other (Line 16)

None.

## The completed Schedule A draft

```markdown
# Schedule A — DRAFT for tax year 2025

## Filing context
Filing status: Married Filing Jointly
AGI (Form 1040 Line 11): $400,000
MAGI: $400,000
Standard deduction MFJ 2025: $30,000
SALT cap applicable: $40,000 (no phaseout; MAGI < $500,000)
Federal marginal bracket: 32%

## Lines 1-4 — Medical and Dental
1. Medical and dental expenses:        $8,700
2. AGI:                              $400,000
3. 7.5% × AGI:                        $30,000
4. Deductible medical (Line 1 − Line 3, ≥ 0): $0   (floor wipes out)

## Lines 5-7 — Taxes
5a. State + local income tax (NY + NYC, W-2 boxes 17+19): $37,500
5b. Real estate taxes (Brooklyn co-op):  $9,000
5c. Personal property taxes:                 $0
5d. Sum 5a+5b+5c:                       $46,500
5e. SALT capped (smaller of 5d or $40K cap): $40,000
6.  Other taxes:                             $0
7.  Total taxes:                        $40,000

## Lines 8-10 — Interest
8a. Mortgage interest (Form 1098):      $32,400
8b. Mortgage interest not on 1098:           $0
8c. Points not on 1098:                      $0
8d. Mortgage insurance premiums:             $0  (Line 8d not available 2025)
8e. Sum 8a-8d:                          $32,400
9.  Investment interest:                     $0
10. Total interest:                     $32,400

## Lines 11-14 — Charity
11. Cash contributions ($30K DAF + $1.5K food bank): $31,500
12. Non-cash contributions (publicly traded stock to alma mater): $12,000
13. Carryover from prior year:               $0
14. Total charitable:                   $43,500
    Raw total: $43,500
    AGI ceiling check: cash 60% = $240K ✓; non-cash LT 30% = $120K ✓
    0.5% AGI floor (2026+ only): N/A for 2025
    Effective Line 14: $43,500

## Line 15 — Casualty and theft
15. Casualty/theft (Form 4684):              $0

## Line 16 — Other
16. Other itemized deductions:               $0

## Line 17 — Total itemized deductions
17. Total: Sum Lines 4+7+10+14+15+16: $115,900

## Standard-vs-itemized comparison
Itemized (Line 17):     $115,900
Standard deduction MFJ:  $30,000
Recommendation: ITEMIZE
Difference: $85,900 of additional deduction

Federal tax savings at 32% bracket: ~$27,488
(Plus state savings if NY mirrors federal itemized — verify state-by-state)

## Required attachments
- [ ] Form 8283 Section A — REQUIRED (Line 12 = $12,000 > $500)
  - Description: 100 shares MSFT (publicly traded, donated 2025-11-15)
  - Date acquired: 2022-04-10
  - Acquisition cost basis: $4,800
  - FMV at donation: $12,000
  - Method of FMV determination: average of high/low on donation date
- [ ] Form 8283 Section B — NOT required (no single non-cash item > $5K requiring appraisal; publicly traded exempt)
- [ ] Form 4684 — NOT required (Line 15 = $0)
- [ ] Form 4952 — NOT required (Line 9 = $0)
- [ ] DAF acknowledgment letter (CWA) — required since contribution > $250
- [ ] Food bank acknowledgment letter (CWA) — required since contribution > $250
- [ ] Alma mater stock-donation acknowledgment letter (CWA) — required since contribution > $250

## Validation summary
- Math: all checks passed
- Sanity: 
  - Line 17 ($115,900) > standard deduction ($30,000) ✓
  - Line 8d = 0 (correct for 2025) ✓
  - SALT cap $40K applied (correct for 2025 under OBBBA) ✓
  - Effective SALT cap = full $40K (MAGI $400K < $500K phaseout threshold) ✓
  - 7.5% medical floor wipes out medical deduction (expected for high-AGI filer) ✓
  - Charity within AGI ceilings (cash 60%, non-cash LT 30%) ✓
- Next steps: Schedule A attaches to Form 1040; Line 17 flows to 1040 Line 12

## Sources cited in this draft
- IRS Form 1040 Schedule A (2025 revision)
- IRS Form 8283 (2025 revision)
- IRC §163(h) (mortgage interest, $750K cap permanent under OBBBA)
- IRC §164(b)(6) (SALT cap as amended by OBBBA 2025)
- IRC §170(b)(1)(G) (60% cash AGI ceiling) and §170(b)(1)(C) (30% non-cash LT AGI ceiling)
- IRC §213 (medical, 7.5% AGI floor)
- Rev. Proc. 2024-40 (2025 inflation adjustments)
- Pub 502, 526, 561, 936
```

## Strategic observations for this filer

### 1. Bunching with a DAF was strategically optimal

By contributing $30,000 to the DAF in 2025 (instead of $7,500/year over 4 years), Daniel and Anya:
- Capture the full $30,000 deduction in 2025 against 32% marginal bracket = $9,600 of federal tax savings
- Avoid the new 0.5% AGI floor entirely (floor doesn't apply for 2025; would apply for 2026+ if they bunched then)
- Distribute to charities over multiple years from the DAF, decoupling timing from tax benefit

If they had spread the $30K over 4 years starting 2026:

| Year | Contribution | 0.5% Floor | Deductible |
|------|--------------|-----------|------------|
| 2026 | $7,500 | $2,000 | $5,500 |
| 2027 | $7,500 | $2,020 | $5,480 |
| 2028 | $7,500 | $2,040 | $5,460 |
| 2029 | $7,500 | $2,060 | $5,440 |
| **Total deduction over 4 years** | **$30,000** | | **$21,880** |

vs the bunched 2025 scenario: $30,000 deduction now, no floor.

The bunching saves roughly $8,120 of *additional deduction value* worth $2,598 at 32%. In addition, capturing it in 2025 (32% bracket) is more valuable than spreading into years where the bracket might be lower. This is why DAF bunching is a high-leverage move post-OBBBA.

### 2. Donating appreciated stock is more efficient than cash + selling

Anya's $12,000 of appreciated MSFT (basis $4,800, gain $7,200 long-term):

**If she sold first and donated cash**:
- Capital gain tax: $7,200 × 23.8% (20% federal LTCG + 3.8% NIIT) = $1,714
- Net donation: $12,000 cash → $12,000 deduction at 32% = $3,840 federal savings
- Net tax benefit: $3,840 − $1,714 = $2,126

**Donating the stock directly**:
- No capital gain recognized
- $12,000 FMV deduction at 32% = $3,840 federal savings
- Net tax benefit: $3,840

Direct donation saves $1,714 vs sell-then-donate. Always donate appreciated long-term securities directly when possible.

### 3. SALT high-income phaseout is approaching

At $400K MAGI, no phaseout applies. But if Daniel and Anya's AGI rose to $500K+ (e.g., from a bonus, RSU vesting, or capital gain sale), the phaseout kicks in:

| Hypothetical MAGI | Phaseout | Effective cap | Lost SALT deduction (vs $40K) |
|--------------------|----------|----------------|--------------------------------|
| $500,000 | $0 | $40,000 | $0 |
| $550,000 | $15,000 | $25,000 | $15,000 (worth ~$5,250 at 35%) |
| $600,000 | $30,000 | $10,000 (floor) | $30,000 (worth ~$10,500 at 35%) |
| $700,000 | $60,000 | $10,000 (floor) | $30,000 (worth ~$10,500) |

Strategies to manage MAGI near the $500K threshold:
- Maximize 401(k) contributions (Anya likely already maxed; check Daniel)
- HSA contributions if available
- Backdoor Roth IRA does NOT lower MAGI
- Defer RSU vesting if possible (rarely controllable)
- Charitable QCDs from IRA (if 70½+; not applicable yet)
- State Pass-Through Entity Tax (PTET) election if Anya's Schedule C generates substantial income — converts uncapped SALT (deductible at federal level) into entity-level deduction

### 4. New York PTET election

If Anya's Schedule C consulting generates $50K+ of net income, she could form an LLC and elect S-corp taxation, then opt into NY's PTET regime — paying NY state tax at the entity level (uncapped federal deduction) instead of personal level (subject to SALT cap). This is a significant planning lever for high-AGI filers in PTET states (NY, CA, NJ, CT, MA, etc.). Outside the scope of Schedule A but worth flagging to the user.

## Filing channel

Daniel and Anya use a CPA who files via professional tax software. The CPA will:

1. Receive their W-2s, 1099s, Form 1098, year-end DAF statement, charitable acknowledgments, K-1s, and 1099-B for the donated stock (showing FMV at donation, with notes that it was a charitable transfer not a sale)
2. Run the standard-vs-itemized comparison
3. File Schedule A with attached Form 8283 Section A
4. E-file return; provide acceptance confirmation

If they were using FFFF instead, follow `filing.md` Section 1 — this is a moderate-complexity return that's still feasible deterministically.

## Records to retain

- Form 1098 (3 years)
- W-2 (3 years)
- Form 8283 + DAF/charity acknowledgment letters (7 years recommended given non-cash > $5K threshold; required at least 3 years)
- Stock cost-basis records for the donated MSFT shares (kept indefinitely until donated; now may discard)
- Form 1099-B for the year of donation showing the transfer (3 years)

## Common variations to watch for

- **Investment interest on Line 9**: if Daniel had margin interest on a brokerage account used to buy taxable securities, Form 4952 would apply
- **Casualty loss in a federally declared disaster**: would add to Line 15
- **HELOC used for kitchen remodel**: would increase Line 8a if traced; not present here
- **Crypto donation > $5,000**: would require qualified appraisal (publicly traded securities exemption does NOT apply to crypto per CCA 202302012)
- **Spouse becomes self-employed**: SE health insurance deductible on Schedule 1 Line 17, not Schedule A
