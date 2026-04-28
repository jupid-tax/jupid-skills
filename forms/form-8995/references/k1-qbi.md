# Reading Section 199A Information from Partnership and S-corp K-1s

Filers with QBI from a partnership (Form 1065) or S-corp (Form 1120-S) receive a Schedule K-1 with Section 199A information reported separately from total entity income.

This reference covers how to read those statements, what to put in Form 8995 Lines 1a-1e column (iii), and common pitfalls.

---

## Partnership K-1 (Schedule K-1, Form 1065)

### Where to find QBI

**Box 20: Other information** — code Z is "Section 199A information"

The partnership preparer must attach a separate statement detailing Section 199A items. The K-1 itself just has "STMT" in Box 20 next to code Z, pointing to the statement.

### What the statement contains

For each trade or business of the partnership, the statement should report:

- Partner's allocable share of QBI (or loss)
- Partner's allocable share of W-2 wages from the trade or business
- Partner's allocable share of unadjusted basis immediately after acquisition (UBIA) of qualified property
- Whether the trade or business is an SSTB (specified service trade or business)
- §199A REIT dividends (if the partnership received any)
- §199A PTP income (if the partnership received any)

For Form 8995 (simplified), only the **QBI amount** matters at low income levels — W-2 wages and UBIA are only relevant above the threshold (Form 8995-A).

### What to put on Form 8995 Line 1 column (iii)

The QBI amount from the Section 199A statement. **Not** the total partnership distributive share, **not** Box 1 ordinary business income.

Example:

K-1 statement (simplified):
```
Section 199A Information
Trade or business: Acme Marketing LLC
Partner's QBI: $15,000
Partner's W-2 wages: $4,000   (ignore for Form 8995)
Partner's UBIA: $0            (ignore for Form 8995)
SSTB: No
```

Form 8995:
- Line 1b (i): "Acme Marketing LLC"
- Line 1b (ii): partnership EIN (from K-1 header)
- Line 1b (iii): $15,000

### When the partnership has multiple trades or businesses

A partnership may operate multiple trades or businesses. The Section 199A statement reports each separately. Each separate trade or business gets its own row in Lines 1a-1e on Form 8995.

Exception: if the partnership made an aggregation election under Treas. Reg. §1.199A-4 and reported the aggregated amount, treat it as a single row.

### Guaranteed payments

Guaranteed payments to partners (Box 4 of K-1) are **not** QBI. They are treated as compensation for services and excluded from §199A. The partnership should reduce QBI by guaranteed payments before reporting QBI on the Section 199A statement — verify by spot-checking that the QBI in the statement is less than Box 1 ordinary business income by at least the amount of guaranteed payments.

### Section 707(c) payments

Section 707(c) payments (deductible payments to partners for use of capital or services) are also not QBI. Same treatment as guaranteed payments — the partnership should net these out before reporting QBI.

---

## S-corp K-1 (Schedule K-1, Form 1120-S)

### Where to find QBI

**Box 17: Other information** — code V is "Section 199A information"

Like partnership K-1, Box 17 typically just shows "STMT" with the detail in an attached statement.

### What the statement contains

Same fields as partnership Section 199A statement: shareholder's QBI, W-2 wages, UBIA, SSTB status, §199A REIT dividends, §199A PTP income.

### What to put on Form 8995 Line 1 column (iii)

The QBI amount from the Section 199A statement. **Not** Box 1 ordinary business income.

Example:

K-1 statement:
```
Section 199A Information
Trade or business: XYZ Consulting Inc.
Shareholder's QBI: $20,000
Shareholder's W-2 wages: $50,000   (ignore for Form 8995)
Shareholder's UBIA: $5,000         (ignore for Form 8995)
SSTB: No
```

Form 8995:
- Line 1c (i): "XYZ Consulting Inc."
- Line 1c (ii): S-corp EIN
- Line 1c (iii): $20,000

### Reasonable compensation reduces QBI

S-corp shareholders who perform services for the corporation must take reasonable compensation as W-2 wages. That W-2 amount is **not** QBI — it's wages. The S-corp's QBI on the Section 199A statement is computed after subtracting reasonable compensation paid to all shareholder-employees.

If the S-corp paid no reasonable compensation but the shareholder worked for the business, the IRS may reclassify distributions as wages, which changes the QBI computation. This is a separate issue from Form 8995 — the K-1 figure is what it is.

---

## Trust and estate K-1s (Schedule K-1, Form 1041)

### Where to find QBI

**Box 14: Other information** — code I is "Section 199A information"

Same statement structure as partnership/S-corp K-1.

### What to put on Form 8995

The QBI amount from the Section 199A statement, with the trust/estate name and EIN.

---

## Common pitfalls

### Pitfall 1: Using K-1 Box 1 instead of the Section 199A QBI

Box 1 (partnership ordinary income / S-corp ordinary income) often includes guaranteed payments, interest, dividends, and other items that don't qualify for §199A. The Section 199A statement strips these out. **Always use the statement's QBI figure, not Box 1.**

### Pitfall 2: K-1 has no Section 199A statement

If the K-1 has "STMT" in the Section 199A box but no attached statement, request one from the entity. Do not estimate or use Box 1 as a substitute. Filing without proper Section 199A info risks an IRS notice and potential disallowance.

### Pitfall 3: SSTB status is "Yes" and filer is below threshold

Below the threshold, SSTB status doesn't matter — every QBI source qualifies fully. Use the QBI figure as-is. Above the threshold, SSTB triggers phase-out (use Form 8995-A).

### Pitfall 4: Negative QBI on K-1

If the K-1 reports a QBI loss (negative QBI), enter it as a negative number in Column (iii) of Form 8995. It will reduce the total QBI on Line 2. If the total Line 2 is negative, enter 0 on Line 2 and carry the loss to next year's Line 3.

### Pitfall 5: K-1 reports QBI from multiple sources but only one row was provided

Some preparers report aggregate QBI as one number even when the entity has multiple trades or businesses. If the K-1 statement breaks them out, enter each on a separate row of Form 8995. If not, ask for a corrected statement — aggregation requires a formal §1.199A-4 election.

### Pitfall 6: Final K-1 (entity dissolved)

If the K-1 is a final K-1 because the partnership/S-corp dissolved during the year, QBI is reported through the date of dissolution. The QBI amount in the Section 199A statement reflects this. No special Form 8995 treatment — file as normal.

---

## When to flag for §1.199A-4 aggregation

If the filer has multiple K-1s from related entities (e.g., a real estate operating company and a real estate property-holding company both flowing to the same person), an aggregation election may be beneficial. Aggregation matters above the threshold (W-2 wage and UBIA limits combine across the aggregated group). Below the threshold, aggregation is irrelevant.

If the filer is below the threshold, do not pursue aggregation — it adds compliance burden with no benefit.
