# Example — 65-year-old taking $50K Traditional IRA distribution; opt up via W-4R

## Scenario

**Filer**: Robert Tanaka, age 65, retired

**Distribution**: $50,000 cash withdrawal from his Traditional IRA at Fidelity

**Purpose**: Robert is retired and lives off Social Security ($30,000/year) plus IRA withdrawals. He's withdrawing $50,000 in 2026 to pay for his daughter's wedding. He wants to set the right withholding so he doesn't owe a big tax bill (or get a §6654 underpayment penalty) at filing time.

**Key facts**:
- Robert is 65, so **no §72(t) early-withdrawal penalty** applies (he's past 59½)
- Filing status: Married Filing Jointly (his wife Sarah is 64, also retired, no income)
- Distribution is from a Traditional IRA → **other nonperiodic** under IRC §3405(b)
- **Default withholding: 10%** ($5,000); recipient can choose 0–100%

---

## Step 1 — Classify the payment

Walked the decision tree:

1. Roth qualified distribution? No — Traditional IRA.
2. Direct trustee-to-trustee rollover? No — cash to Robert.
3. Wages? No.
4. Periodic? No — one-time withdrawal.
5. ERD? No — IRA distribution, not from a qualified plan / 403(b) / 457(b) governmental plan.
6. → **Other nonperiodic**. W-4R, default 10%, opt 0–100%.

---

## Step 2 — Estimate marginal bracket and total tax liability

Robert's 2026 income picture:

| Source | Amount |
|--------|--------|
| Social Security (Robert) | $30,000 |
| Social Security (Sarah) | $0 (Sarah filed for benefits but suspended; not yet drawing) |
| IRA distribution (this withdrawal) | $50,000 |
| Other ordinary income | $0 |
| Capital gains / qualified dividends | $1,500 (from a small taxable brokerage account) |
| **Gross income** | **$81,500** |

Social Security taxability: With provisional income of $30,000/2 + $50,000 + $1,500 = $66,500 (above the $44,000 MFJ threshold), up to 85% of SS is taxable. Estimated taxable SS: $25,500 (85% of $30,000).

| Item | Amount |
|------|--------|
| Taxable SS | $25,500 |
| IRA distribution (fully taxable; basis $0) | $50,000 |
| Taxable ordinary dividends | $300 (assumed) |
| Long-term capital gains | $1,200 (qualified, separate rate) |
| **AGI** | **$77,000** |
| Less: 2026 standard deduction (MFJ, both 65+) | $32,300 (estimate; verify against IRS Rev. Proc.) |
| Taxable income (ordinary) | $44,700 |

Federal tax on $44,700 ordinary (MFJ 2026 brackets — estimate):

- 10% on first $23,850 = $2,385
- 12% on next $20,850 = $2,502
- **Ordinary tax: $4,887**

Plus tax on $1,200 LTCG at 0% (MFJ taxable income < $96,700, 2026 estimate) = $0

**Estimated total federal tax: ~$4,887**

Marginal bracket: 12% (on the next dollar of ordinary income).

---

## Step 3 — Determine the withholding rate

Robert's options:

| W-4R rate | Withholding amount | Net to Robert | Tax owed at filing |
|-----------|---------------------|---------------|---------------------|
| 0% | $0 | $50,000 | ~$4,887 |
| 10% (default) | $5,000 | $45,000 | ($4,887 − $5,000) = +$113 refund |
| 12% (matches marginal bracket) | $6,000 | $44,000 | ($4,887 − $6,000) = +$1,113 refund |
| 22% | $11,000 | $39,000 | ($4,887 − $11,000) = +$6,113 refund (over-withheld) |

Robert's preference: he doesn't want to owe at filing AND doesn't want to over-withhold (tying up cash until refund). The **10% default** is close to the right rate.

A more precise calculation: marginal rate is 12%, but average tax rate on the distribution (factoring standard deduction absorption and the 10% bracket) is about 9–10%. The 10% default is well-calibrated.

**Robert chooses: 10% (leaves Line 2 blank, accepting the default).**

Alternatively, if Robert wants to buffer slightly against under-withholding (and accept a small refund), he can enter "12" on Line 2. He goes with the default.

---

## Form W-4R — DRAFT for Robert Tanaka

```
# Form W-4R — DRAFT

## Filing summary
- Recipient:                 Robert Tanaka
- SSN:                       XXX-XX-XXXX
- Payor:                     Fidelity Brokerage Services LLC
- Payment type:              Other nonperiodic (Traditional IRA distribution)
- Distribution amount:       $50,000
- Elected withholding rate:  10% (default; Line 2 blank)
- Default rate that would apply if blank: 10%
- Tax year of distribution:  2026

## Form W-4R (printable)

Withholding Certificate for Nonperiodic Payments and Eligible Rollover Distributions
For tax year 2026

Step 1 — Personal Information
Name:                Robert Tanaka
Social Security number: XXX-XX-XXXX
Address:             [Robert's home address]
City, state, ZIP:    [city, state, ZIP]

Step 2 — Withholding Rate
1a. Payor name:      Fidelity Brokerage Services LLC
1b. Payor address:   [Fidelity's address per Robert's most recent IRA statement]

2.  Rate: ____ %  [LEFT BLANK — default 10% applies]

Step 3 — Sign Here
Signature: Robert Tanaka
Date:      04/15/2026

## Required actions
- [X] Robert signs and dates the form
- [X] Form delivered to Fidelity (via Fidelity's portal, distribution-request workflow)
- [X] Robert retains a copy

## Validation summary
- Classification: PASS — Other nonperiodic
- Rate within allowed range: PASS (blank = 10% default; in 0-100 range)
- Recipient ID matches payor records: PASS

## Estimated tax impact
- Distribution:                            $50,000
- Withholding at 10%:                       $5,000
- After-withholding cash to Robert:        $45,000
- Estimated additional federal tax owed
  at filing given marginal rate ~12%:      ($113) refund (very close to break-even)

## Reminders
- §72(t) 10% early-withdrawal penalty: N/A — Robert is 65 (past 59½)
- State income tax withholding: separate state form via Fidelity
- Form 1099-R issued by Fidelity in January 2027; reconcile on Robert's 2026 Form 1040
- Sarah's 2026 SS suspension: re-evaluate for 2027 (delaying SS to age 66 increases her
  benefit by ~6.7%/year; coordinate with overall retirement income plan)

## Sources cited in this draft
- IRS Form W-4R (2026 revision)
- IRC §3405(b) (other nonperiodic — 10% default)
- IRC §72 (taxation of distributions from retirement accounts)
- IRS Pub. 590-B (Distributions from IRAs)
- IRS Pub. 915 (Social Security and Equivalent Railroad Retirement Benefits)
```

---

## Filing channel

Robert delivers W-4R via Fidelity's participant portal:

1. Logs in at fidelity.com
2. Goes to "Move money" → "Withdraw money"
3. Selects his Traditional IRA → "Withdraw cash"
4. Enters distribution amount: $50,000
5. **Federal tax withholding section**: portal pre-checks "10% default"
6. Robert leaves the default; alternatively could click "Use a different rate"
7. State withholding: Robert lives in CA — CA mandatory state withholding applies; CA default is 1% of distribution but Robert can elect higher. Robert leaves CA default for now.
8. Direct deposit to his linked checking account
9. E-signs (typed name + acknowledgment + 2FA code)
10. Confirmation: distribution scheduled for 4/16/2026; net $44,500 (after $5,000 federal + $500 CA state) to checking

Form 1099-R will be issued in January 2027.

---

## What Robert should also do

- [X] Set a Form 1040 reminder for spring 2027 to reconcile (expects a small refund or near-zero balance)
- [X] If he plans similar IRA withdrawals in future years, evaluate whether to set up automatic 10% withholding on all withdrawals (Fidelity supports this) vs. file W-4R per distribution
- [X] Consider whether IRA withdrawal timing could be optimized — e.g., spreading the $50,000 across two tax years (December 2026 + January 2027) to manage the SS taxable threshold. With $50,000 in one year, 85% of SS is taxable; with $25,000/year split, less SS may be taxable. But the wedding is in 2026, so cash flow drives the decision.

---

## Sources cited in this draft

- IRS Form W-4R (2026 revision)
- IRC §3405(b) (other nonperiodic — 10% default)
- IRC §72 (taxation of distributions)
- IRS Pub. 590-B (IRA Distributions)
- IRS Pub. 915 (Social Security taxation)
- IRC §6654 (estimated tax — N/A here, withholding satisfies safe harbor)
