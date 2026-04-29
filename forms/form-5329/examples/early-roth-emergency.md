# Example: Emergency Roth IRA Withdrawal at 28

A complete walkthrough of Form 5329 Part I for a young filer who took a
non-qualified Roth IRA distribution that included earnings, with a
partial medical-expense exception. Demonstrates Roth ordering rules,
exception codes, and the interaction with Form 1040.

## The filer

- **Name**: Daniel Reeves
- **Age**: 28 (DOB 06/14/1997)
- **Tax year**: 2025 (filing in 2026)
- **Account**: Roth IRA at Schwab, opened 2019
- **First-year filer for Form 5329?**: Yes

## What happened

In March 2025, Daniel had an unexpected medical emergency — appendicitis,
followed by complications, leading to $14,200 in unreimbursed medical
expenses (his high-deductible health plan did not cover the
out-of-network surgeon).

He took $20,000 from his Roth IRA in April 2025 to cover medical bills
and to bridge a gap in income while recovering.

His Roth IRA records show:

- Total regular contributions over 2019-2024: $24,000
- 2025 contribution (made January 2025): $7,000
- No conversions ever
- Account value at withdrawal in April 2025: $48,000 (so earnings were
  $48,000 − $24,000 − $7,000 = $17,000)
- Account value 12/31/2025 (after the $20,000 withdrawal): $32,500

## Roth ordering rules applied

Per IRC §408A and Pub 590-B, distributions from a Roth IRA come out in
this order:

1. Regular contributions (tax-free, penalty-free, regardless of age or
   5-year rule)
2. Conversions (oldest first; tax-free; penalty-free if 5+ years old)
3. Earnings (taxable if non-qualified; subject to 10% penalty if under
   59½)

Daniel's $20,000 distribution applied to the layers:

| Layer | Available | Used | Remaining |
|-------|-----------|------|-----------|
| Regular contributions ($24,000 prior + $7,000 = $31,000) | $31,000 | $20,000 | $11,000 |
| Conversions | $0 | $0 | $0 |
| Earnings | $17,000 | $0 | $17,000 |

**Result**: Daniel's entire $20,000 distribution was Roth basis. Line 1
on Form 5329 Part I = $0. **No Form 5329 is required.**

## But what if he had taken $35,000 instead?

To illustrate the exception logic, imagine Daniel needed $35,000 (not
$20,000). The layers would be:

| Layer | Available | Used | Remaining |
|-------|-----------|------|-----------|
| Regular contributions ($31,000) | $31,000 | $31,000 | $0 |
| Conversions | $0 | $0 | $0 |
| Earnings | $17,000 | $4,000 | $13,000 |

Now $4,000 of earnings are part of the distribution. These earnings:

- Are includible in income (Form 1040 Line 4b includes the $4,000)
- Are subject to the 10% additional tax under §72(t) — Daniel is 28,
  under 59½

So Form 5329 Part I, Line 1 = $4,000.

### Applying the medical expense exception (code 05)

Daniel's unreimbursed medical expenses were $14,200. His 2025 AGI was
$54,000 (he's a software engineer; the surgery and recovery reduced his
income).

7.5% of AGI = $54,000 × 0.075 = $4,050.

Medical expenses exceeding 7.5% AGI = $14,200 − $4,050 = $10,150.

Daniel can apply this exception against his $4,000 of taxable Roth
earnings. The exception amount caps at the smaller of (the medical
exception) or (the early distribution amount). So Line 2 = $4,000 (the
full taxable earnings; the exception is more than enough to cover them).

Line 3 = Line 1 − Line 2 = $4,000 − $4,000 = $0.
Line 4 = $0 × 10% = $0.

**No additional tax**, even though Daniel was under 59½ and earnings were
distributed.

## The completed Form 5329 draft (hypothetical $35,000 scenario)

```markdown
# Form 5329 — DRAFT for tax year 2025
(Hypothetical: $35,000 withdrawal scenario)

## Header
Name: Daniel Reeves
SSN: XXX-XX-XXXX
Filing standalone? No (attaching to Form 1040)

## Part I — Additional Tax on Early Distributions
1.  Early distributions includible in income:        $4,000
    (Roth earnings portion — basis $31,000 came out tax-free
     under Roth ordering rules)
2.  Exception amount + code:                         $4,000 (code 05)
    (Medical expenses $14,200 − 7.5% × $54,000 AGI
     = $10,150 exception available; capped at $4,000 used)
3.  Amount subject to additional tax (Line 1 − 2):   $0
4.  Additional tax (Line 3 × 10%):                   $0

## Parts II-IX
N/A — no other tax-favored account events for the year

## Total additional tax flowing to Schedule 2 Line 8: $0

## Required attachments
- [ ] Form 1040 (5329 attaches; reports $4,000 earnings on Line 4b)
- [ ] Form 8606 if required for traditional-IRA basis tracking (N/A here)

## Validation summary
- Math: all checks passed
- Sanity:
  - Roth ordering rules applied correctly: basis $31,000 covered first $31,000
    of distribution; remaining $4,000 was earnings
  - Medical exception ($10,150) > earnings amount ($4,000), capped at $4,000
  - User retained medical receipts, AGI computation worksheet, and Schwab
    statements showing 2019-2024 contribution history
- Next steps:
  - $4,000 earnings reported on Form 1040 Line 4b (taxable)
  - $4,000 included in AGI; user already in 22% federal bracket → ~$880 income
    tax on the earnings (separate from §72(t) penalty, which is $0 due to exception)
  - Daniel should consider rebuilding the Roth basis in future years; the $20,000
    actual withdrawal cannot be replaced (Roth IRAs have no rollover-back
    mechanism, only the 60-day rollover for amounts not yet distributed)

## Sources cited in this draft
- IRS Form 5329, Rev. 2025
- IRS Instructions for Form 5329, Rev. 2025
- IRC §72(t)(2)(B) — medical expense exception
- IRC §408A — Roth IRA rules
- IRS Pub 590-B — distributions from IRAs (Roth ordering rules)
- IRC §72(m)(7) — disability standard (not used; for reference)
```

## Why each non-obvious choice

**Why apply Roth ordering before computing Line 1?** The IRS treats Roth
basis as already taxed (it was contributed after-tax). It comes out tax-
and penalty-free. Computing Line 1 on the gross $35,000 would double-
count the basis. Pub 590-B's ordering rules are explicit on this.

**Why is the medical exception based on AGI, not Roth distribution
amount?** §72(t)(2)(B) defines the exception as the amount by which
medical expenses exceed 7.5% of AGI. The user can apply that exception
amount against any early distribution — the cap is the lesser of the
medical-exception amount or the early distribution. Daniel's exception
amount ($10,150) was much larger than his taxable earnings ($4,000), so
the full earnings portion was excepted.

**Why not file Form 5329 in the actual scenario ($20,000 withdrawal)?**
Because Line 1 is $0. The instructions are clear: file Part I only when
there's an early distribution includible in income. Daniel's $20,000 was
all basis. He still reports the $20,000 on Form 1040 Line 4a (gross
distribution) but Line 4b (taxable amount) is $0. No 5329.

**What if Daniel had also made a 2025 Roth contribution after the
distribution?** It wouldn't change Form 5329 unless his MAGI was above the
phaseout (it wasn't — $54,000 AGI is well below the $150,000 single
phaseout threshold for 2025). Just a normal contribution.

**What if Daniel had 1099-R Box 7 code J (early distribution from Roth)?**
He'd still apply Roth ordering. Box 7 codes are the custodian's signal,
not the determining factor. If basis covers the distribution, no Form 5329
needed regardless of Box 7.

**What records should Daniel retain?**

1. Schwab statements showing each year's contribution from 2019-2024
2. The 2019-2024 Form 5498 forms (received from Schwab annually) showing
   contributions
3. Schwab statement showing the April 2025 distribution
4. Medical bills, EOBs, and receipts substantiating the $14,200 in
   unreimbursed medical expenses
5. 2025 Form 1040 showing AGI = $54,000
6. Calculation worksheet for the medical exception:
   $14,200 − ($54,000 × 7.5%) = $10,150

If audited, items 1-2 substantiate the basis layers; items 3 substantiates
the distribution; items 4-6 substantiate the exception.
