# Reconciling Form 5498 Against the Tax Return

The agent's job after receiving a Form 5498 is to verify it agrees with
what the user reported on Form 1040, Schedule 1, Form 8606, and any
1099-Rs. This reference catalogs every reconciliation pattern.

---

## Pattern 1 — Traditional IRA contribution (Box 1)

### What the 5498 says

```
Box 1 (IRA contributions): $7,000
Box 5 (FMV 12/31): $48,200
Box 7 (IRA type): IRA
```

### What the return should say

If the user is **deductible-eligible** (not covered by an employer
retirement plan, OR covered but MAGI below phaseout):

- **Schedule 1 Line 20** (IRA deduction): up to $7,000

If the user is **partially deductible** (covered by employer plan and
MAGI in phaseout):

- **Schedule 1 Line 20**: pro-rata deductible amount
- **Form 8606 Line 1**: the nondeductible portion (basis)

If the user is **fully nondeductible** (covered by plan and MAGI above
phaseout):

- **Schedule 1 Line 20**: $0
- **Form 8606 Line 1**: $7,000 (full contribution as basis)

### Reconciliation status

- ✓ Match if Schedule 1 Line 20 + Form 8606 Line 1 = $7,000
- ✗ Mismatch otherwise — investigate

### MAGI phaseouts for traditional IRA deduction (2025)

Per Notice 2024-80 (verify 2026):

**Active participant in employer plan**:
- Single/HoH: $79,000-$89,000 MAGI
- MFJ (filer is participant): $126,000-$146,000 MAGI
- MFJ (spouse is participant, filer is not): $236,000-$246,000 MAGI

**Not active participant**: No phaseout — fully deductible regardless
of MAGI (subject to earned income limit).

---

## Pattern 2 — Roth IRA contribution (Box 10)

### What the 5498 says

```
Box 10 (Roth IRA contributions): $7,000
Box 5 (FMV 12/31): $63,800
Box 7 (IRA type): Roth IRA
```

### What the return should say

**Nothing**. Roth contributions are not deductible. The 5498 is the
record of contribution; the return is silent on it.

### Reconciliation status

- ✓ Match if Roth contribution was within MAGI phaseout
- ✗ Mismatch (excess contribution) if user's MAGI > phaseout
  - Hand off to `form-5329` Part IV

### MAGI phaseouts for Roth IRA contribution (2025)

Per Notice 2024-80 (verify 2026):
- Single/HoH: $150,000-$165,000 MAGI
- MFJ: $236,000-$246,000 MAGI
- MFS: $0-$10,000 MAGI

If user's MAGI is in the phaseout, allowed contribution is reduced
linearly. If above the upper limit, allowed contribution = $0.

---

## Pattern 3 — Direct rollover from 401(k) to Traditional IRA (Box 2)

### What the 5498 says

```
Box 2 (Rollover contributions): $50,000
Box 5 (FMV 12/31): $50,300
Box 7 (IRA type): IRA
```

### What the corresponding 1099-R says

Issued by the 401(k) plan sponsor:
```
Box 1 (gross distribution): $50,000
Box 2a (taxable amount): $0 (or blank)
Box 7 (distribution code): G (direct rollover)
```

### What the return should say

- **Form 1040 Line 5a** (gross 401(k) distribution): $50,000
- **Form 1040 Line 5b** (taxable amount): $0
- "Rollover" written in the margin or via the appropriate
  e-file code/indicator

### Reconciliation status

- ✓ Match if 5498 Box 2 = 1099-R Box 1 = Form 1040 Line 5a (gross)
- ✓ Match if Form 1040 Line 5b = $0
- ✗ Mismatch if Line 5b ≠ $0 (user mis-reported the rollover as
  taxable; amend per `filing.md` Section 3 Scenario D)

### Edge case — partial 60-day rollover

User received $50,000 from 401(k) (no direct rollover; check sent to
user), held it 30 days, deposited $40,000 into IRA within 60-day window,
kept $10,000.

- 1099-R Box 1 (gross): $50,000
- 1099-R Box 7 (code): 1 (early distribution, no known exception) or
  similar
- 5498 Box 2 (rolled over): $40,000
- Form 1040 Line 5a: $50,000
- Form 1040 Line 5b: $10,000 (the $10K not rolled is taxable)
- If user is under 59½, the $10K may also trigger Form 5329 Part I
  10% additional tax

---

## Pattern 4 — Roth conversion (Box 3)

### What the 5498 says

```
Box 3 (Roth conversion amount): $25,000
Box 5 (FMV 12/31, Roth IRA): $145,000
Box 7 (IRA type): Roth IRA
```

(There's also a corresponding 5498 for the *traditional* IRA showing
the distribution out — but that's via a 1099-R, not the 5498. The
sending IRA's 5498 typically just shows reduced Box 5.)

### What the corresponding 1099-R says

Issued by the traditional IRA custodian:
```
Box 1 (gross distribution): $25,000
Box 2a (taxable amount): $25,000 (or blank if user has basis — let
   8606 compute)
Box 7 (distribution code): 2 (early distribution, exception applies —
   the IRA-to-Roth conversion is a §72(t) exception) or 7 (normal
   distribution if user 59½+)
```

### What the return should say

- **Form 1040 Line 4a** (gross IRA distribution): $25,000
- **Form 1040 Line 4b** (taxable amount): computed via Form 8606 Part II

If user has no nondeductible basis in any traditional IRA: Line 4b =
$25,000 (full conversion is taxable).

If user has basis (prior nondeductible contributions on Form 8606):
- **Form 8606 Part II Line 16** (gross Roth conversion): $25,000
- **Form 8606 Part II Line 17** (basis applied via pro-rata rule):
  computed as basis ÷ aggregate traditional IRA value × conversion
- **Form 8606 Part II Line 18** (taxable portion): Line 16 − Line 17
- This goes to Form 1040 Line 4b

### Reconciliation status

- ✓ Match if 5498 Box 3 = 1099-R Box 1 = Form 1040 Line 4a
- ✓ Match if Form 1040 Line 4b = Form 8606 Part II Line 18 (with
  any basis applied)
- ✗ Mismatch if user has prior basis but Form 8606 was not filed

### Pro-rata rule reminder

Form 8606's pro-rata rule treats all the user's traditional / SEP /
SIMPLE IRAs as a single pool for basis-tracking. If the user has
multiple traditional IRAs, sum their year-end values (Box 5 across all
relevant 5498s) for the denominator.

---

## Pattern 5 — Recharacterization (Box 4)

### What the 5498 says

Two 5498s involved:

**Source IRA (e.g., Roth)**:
```
Box 4 (Recharacterized): $7,000
Box 10 (Roth contribution): $0  (the contribution was recharacterized out)
```

**Destination IRA (e.g., traditional)**:
```
Box 1 (IRA contribution): $7,000
Box 4 (Recharacterized): $7,000  (or blank — verify custodian's reporting)
```

### What the return should say

The contribution is reported as having been to the **destination** IRA
type. So if the user originally contributed $7,000 to Roth and
recharacterized to traditional:

- Schedule 1 Line 20 (deductible IRA): up to $7,000 if eligible
- Form 8606 Line 1 (nondeductible basis): $7,000 if not eligible to
  deduct
- Box 10 of the Roth 5498: $0 (the contribution is no longer there)
- Box 1 of the traditional 5498: $7,000

### Reconciliation status

- ✓ Match if both 5498s consistently show the recharacterized round
  trip
- ✗ Mismatch if the source 5498 still shows the contribution in Box
  10/1 — custodian error; request correction

---

## Pattern 6 — Required minimum distribution (Box 11 + 12)

### What the 5498 says

```
Box 5 (FMV 12/31): $230,000
Box 7 (IRA type): IRA
Box 11 (RMD required next year): ✓
Box 12a (RMD date): 12/31/[next year]
Box 12b (RMD amount): $9,389
```

(The RMD amount is an estimate from the custodian; user verifies.)

### What the return should say

The 5498 is for the *contribution* year (call it Year N). The RMD it
flags is for Year N+1. Reconciliation against Year N's return:

- The 5498 doesn't directly affect Year N's return
- Year N+1's return should include the RMD as taxable on Form 1040
  Line 4a/4b (or 5a/5b for 401(k))
- Year N+1's 1099-R (received January of Year N+2) will document the
  actual RMD distribution

### Reconciliation status

For Year N: N/A (5498 is informational about future RMD)

For Year N+1: confirm via the 1099-R that the actual RMD was taken in
the correct amount (≥ Box 12b from the prior-year 5498)

If the RMD was missed or short: hand off to `form-5329` Part IX

---

## Pattern 7 — Multiple IRAs at one custodian (multiple 5498s)

### What the 5498s say

User has both a traditional IRA and a Roth IRA at Fidelity. Receives
two 5498s.

**Traditional IRA 5498**:
```
Box 1 (IRA contributions): $4,000
Box 5 (FMV 12/31): $76,500
Box 7 (IRA type): IRA
```

**Roth IRA 5498**:
```
Box 10 (Roth contributions): $3,000
Box 5 (FMV 12/31): $42,000
Box 7 (IRA type): Roth IRA
```

### Aggregate check

- Total IRA contributions for the year: $4,000 + $3,000 = $7,000
- 2025 limit: $7,000 (or $8,000 age 50+)
- ✓ Within limit; no excess

### Return reconciliation

- Schedule 1 Line 20 (or Form 8606 Line 1): $4,000 (the traditional
  contribution; deductible status depends on MAGI)
- Roth contribution: not on return, but eligibility (MAGI) must be
  verified
- Total = $7,000, within annual limit

---

## Pattern 8 — Multiple IRAs at multiple custodians

### What the 5498s say

User has IRAs at Fidelity, Vanguard, and Schwab. Receives three 5498s.

**Fidelity Traditional**:
```
Box 1: $3,000
Box 5: $58,000
```

**Vanguard Traditional**:
```
Box 1: $2,000
Box 5: $32,000
```

**Schwab Roth**:
```
Box 10: $4,000
Box 5: $19,500
```

### Aggregate check

- Total contributions: $3,000 + $2,000 + $4,000 = $9,000
- 2025 limit: $7,000 (assume user under 50)
- ✗ Excess: $9,000 − $7,000 = $2,000

The excess could be in any of the contributions; the user must decide
which to correct. Hand off to `form-5329` Part III/IV.

### Aggregate check for RMD (when applicable)

If user is 73+, traditional IRAs aggregate for RMD:
- Aggregate traditional FMV (12/31): $58,000 + $32,000 = $90,000
- RMD = $90,000 ÷ distribution period factor for user's age
- The RMD can be taken from any traditional IRA in any combination;
  total must be at least the aggregate RMD

Roth IRA does not aggregate for RMD (Roth has no lifetime RMD for the
original owner).

---

## Common reconciliation issues and fixes

### Issue: Box 1 on 5498 differs from Schedule 1 Line 20 by exactly the catch-up amount

User is 50+ and contributed $8,000 ($7,000 base + $1,000 catch-up). The
5498 should show Box 1 = $8,000. If Schedule 1 Line 20 shows $7,000,
the user forgot to claim the catch-up. Amend to add the $1,000.

### Issue: Box 1 includes a contribution the user already withdrew (return of excess)

If user contributed $7,000 in February, then in October realized it was
excess and withdrew $3,000 + earnings, the 5498 may still show Box 1 =
$7,000 (depending on custodian timing) and a 1099-R may show the
withdrawal with code 8 or P. The reconciliation:
- Form 1040 Schedule 1 Line 20: $4,000 (the contribution that
  remained after correction)
- 5498 Box 1: $7,000 (gross before correction)
- 1099-R Box 1: $3,000 + earnings
- 1099-R Box 7: code 8 (excess return for current year) or P (excess
  return for prior year)

The 5498 and Schedule 1 differ by the corrected amount; this is a
*correct* mismatch, not an error.

### Issue: Box 2 includes a 60-day rollover that's outside the 60-day window

If the user thought they made a 60-day rollover but actually the
deposit was 65 days after distribution, the rollover is invalid:
- The original distribution is fully taxable (and may trigger 10%
  early-distribution tax)
- The "rollover" deposit is a new contribution subject to annual
  limits — likely creating excess

Custodians don't typically validate the 60-day window; the user does.
Surface this if the dates suggest a problem.

### Issue: Box 3 on the Roth 5498 doesn't match Box 1 on the traditional 1099-R

The conversion amount should match. Off-by-a-few-dollars usually means
fees or sweep-account interest accrued between distribution and
deposit. Off-by-a-larger-amount means a custodian error or a partial
conversion that the user didn't realize was partial. Investigate.
