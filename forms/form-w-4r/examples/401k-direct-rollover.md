# Example — 401(k) direct rollover to IRA; NO W-4R needed

## Scenario

**Filer**: Aisha Patel, age 45, recently left her job at TechCorp

**Distribution**: $185,000 from her TechCorp 401(k), being **directly rolled over** to a new Traditional IRA at Schwab

**Purpose**: Aisha is moving her retirement savings out of TechCorp's plan into an IRA where she has more investment options. She wants to preserve the full $185,000 in tax-deferred form. She has 60 days to complete a rollover but is choosing the **direct rollover** path to avoid the 20% mandatory withholding.

**Key insight**: For a **direct rollover**, **no W-4R is needed**. The funds move directly from TechCorp's 401(k) to Schwab's IRA custodian without Aisha taking receipt. "There is no withholding" on a direct rollover (Pub. 575 (2025), Table 1; IRC §3405(c)(2)).

This example demonstrates why direct rollovers are almost always preferred over indirect rollovers for ERDs.

---

## Step 1 — Classify the payment

Walked the decision tree:

1. Roth qualified distribution? No — Traditional 401(k).
2. Direct trustee-to-trustee rollover? **YES.** → No withholding. **No W-4R needed.**

The classification short-circuits at step 2. We don't need to go further.

---

## Step 2 — Compare direct rollover vs. indirect rollover

To make sure the direct rollover is truly the right path, contrast the two options:

### Option A — Direct rollover (Aisha's chosen path)

**Mechanics**:
1. Aisha opens a Traditional IRA at Schwab
2. Aisha calls TechCorp's 401(k) recordkeeper (e.g., Fidelity NetBenefits) and requests a "direct rollover to Schwab Traditional IRA"
3. TechCorp's trustee issues a check **payable to "Charles Schwab & Co. FBO Aisha Patel IRA"** OR a wire transfer directly to Schwab
4. Schwab receives the $185,000 and credits Aisha's IRA
5. TechCorp's trustee issues Form 1099-R with **Distribution Code G** (direct rollover) showing:
   - Box 1 (gross distribution): $185,000
   - Box 2a (taxable amount): $0 (direct rollovers are not taxable)
   - Box 4 (federal income tax withheld): $0
   - Box 7 (distribution code): G

**No W-4R needed.** No withholding form is involved because the distribution is not subject to withholding.

**Result**: $185,000 fully transferred to the Traditional IRA. No tax due now. No §72(t) additional tax: the rolled-over amount isn't included in income (Pub. 575 (2025), Table 1: "There is no 10% additional tax").

**How Aisha reports it**: 2025-form line numbers (re-check on the 2026 Form 1040): $185,000 on line 5a, $0 on line 5b, and box 1 ("Rollover") checked on line 5c (Pub. 575 (2025), "How to report").

### Option B — Indirect (60-day) rollover (NOT Aisha's path)

**Mechanics**:
1. Aisha requests a cash distribution from her 401(k), payable to her
2. TechCorp's trustee withholds **20% mandatory federal tax** under IRC §3405(c) → $37,000 sent to IRS
3. Aisha receives a check for **$148,000** (the $185,000 less $37,000 withholding)
4. To complete a tax-free rollover within 60 days, Aisha must deposit the full $185,000 into her IRA (NOT just the $148,000 she received)
5. The $37,000 difference must come from Aisha's non-IRA cash (savings, taxable brokerage, etc.)
6. When Aisha files her 2026 tax return, she reports the $185,000 distribution on Form 1040 line 5a, $0 taxable on line 5b (rolled over within 60 days), checks box 1 ("Rollover") on line 5c, and claims the $37,000 federal withholding on line 25b (2025-form line numbers; Pub. 575 (2025))
7. TechCorp's trustee issues 1099-R with **Distribution Code 7** (normal) or **1** (early) — NOT Code G — showing:
   - Box 1 (gross distribution): $185,000
   - Box 2a (taxable amount): $185,000 (assumed taxable; recipient indicates rollover on Form 1040)
   - Box 4 (federal income tax withheld): $37,000
   - Box 7 (distribution code): 1 or 7

**No W-4R needed unless she wants more than 20%.** This is an ERD: "You can't choose withholding at a rate of less than 20% (including '-0-')... Don't give Form W-4R to your payer unless you want more than 20% withheld" (2026 Form W-4R, page 2). The plan withholds 20% either way.

**Result if successful**: $185,000 in IRA, $37,000 federal withholding refunded at tax filing (~14 months later). Net same as direct rollover but with a 14-month cash flow drag for the $37,000.

**Result if Aisha fails to make whole**: Only $148,000 is rolled over. The $37,000 is a taxable distribution (Pub. 575 (2025), "Rolling over more than amount received"). At an assumed 22% marginal rate, that's $8,140 federal tax + $3,700 §72(t) additional tax (Aisha is 45; she left TechCorp before the year she turns 55, so exception 01 doesn't apply, and no other exception applies) = **$11,840** in tax on money she meant to keep tax-deferred.

---

## Step 3 — Why direct rollover wins

The math:

| Metric | Direct rollover | Indirect rollover (made whole) | Indirect rollover (failed make-whole) |
|--------|------------------|---------------------------------|---------------------------------------|
| Cash from 401(k) | N/A (direct transfer) | $148,000 | $148,000 |
| Cash needed from non-IRA savings to make rollover whole | $0 | $37,000 | $0 |
| Amount in IRA after rollover | $185,000 | $185,000 | $148,000 |
| Federal tax due | $0 | $0 (rolled over) | $8,140 (22% on $37K) |
| §72(t) penalty | $0 | $0 | $3,700 (10% on $37K) |
| Time until $37,000 returned | N/A | ~14 months (refund) | Never |

**Direct rollover is strictly better** when the goal is to keep the money tax-deferred. If Aisha also wanted cash (say $20,000), she could split: direct rollover of $165,000 and a $20,000 cash distribution, which is an ERD with 20% withheld (a W-4R only if she wants more than 20%).

---

## Step 4 — Aisha's actual action

Since Aisha is doing a clean direct rollover, the deliverable is **NOT a W-4R** but rather a **direct rollover request** with her 401(k) recordkeeper.

```
# Direct Rollover Request — DRAFT for Aisha Patel

## Filing summary
- Account holder:           Aisha Patel
- SSN:                      XXX-XX-XXXX
- Source plan:              TechCorp 401(k) Plan
- Source plan administrator: Fidelity NetBenefits
- Distribution amount:      $185,000 (full account balance)
- Receiving custodian:      Charles Schwab & Co. (FBO Aisha Patel IRA)
- Receiving account:        Aisha Patel Traditional IRA, Account # XXX-XXXXXX
- Payment method:           Direct check payable to "Charles Schwab & Co. FBO Aisha Patel IRA"
                            mailed to Schwab's rollover-receiving address
- Federal withholding:      $0 (direct rollover; W-4R not applicable)
- Distribution code:        G (will appear on 1099-R)

## Form W-4R: NOT NEEDED

Direct trustee-to-trustee rollovers are not subject to federal income tax withholding
under IRC §3405. The funds move directly between qualified plans / IRAs without the
participant taking constructive receipt. No W-4R is filed.

## Required actions (Aisha's checklist)
- [X] Open Traditional IRA at Schwab (must be open before initiating rollover)
- [X] Obtain Schwab's rollover-receiving address and account number
- [X] Contact Fidelity NetBenefits (TechCorp's recordkeeper) and request direct rollover
- [X] Provide Schwab's payee instructions to Fidelity
- [X] Confirm with Fidelity: distribution code G will be used on 1099-R
- [X] Track check / wire from Fidelity to Schwab
- [X] Confirm receipt at Schwab and proper crediting to IRA
- [X] Save 1099-R when issued in January 2027 (gross $185K, taxable $0)

## Validation summary
- Classification: PASS — Direct trustee-to-trustee rollover
- W-4R required: NO
- Withholding applied: NONE
- §72(t) early-withdrawal penalty: N/A (direct rollover not treated as distribution)

## Reminders
- The receiving IRA at Schwab should be open before the plan issues the payment,
  so the plan has the receiving account details
- The check must be payable to "Charles Schwab & Co. FBO Aisha Patel IRA" — NOT
  payable to Aisha personally. A payment to Aisha is not a direct rollover: the plan
  must withhold 20%, and she would have 60 days to roll it over (Pub. 575 (2025))

## Sources cited in this draft
- IRC §402(c) (eligible rollover distribution definition)
- IRC §401(a)(31) (direct rollover option)
- IRC §3405(c)(2) (direct rollover NOT subject to 20% mandatory withholding)
- IRC §72(t) (early withdrawal penalty — N/A to direct rollovers)
- IRS Pub. 575 (Pension and Annuity Income)
- IRS Pub. 590-A (IRA Contributions — including rollover treatment)
- Form 1099-R instructions (Distribution Code G for direct rollovers)
```

---

## Process map

```
Aisha's situation: leaving TechCorp, $185K in 401(k), wants tax-deferred rollover

Path: DIRECT ROLLOVER

Step 1: Open Schwab Traditional IRA  →  Schwab issues account number + receiving address
Step 2: Call Fidelity NetBenefits   →  Request "direct rollover to Schwab Traditional IRA"
Step 3: Provide Schwab's instructions →  Fidelity issues check payable to "Schwab FBO Aisha"
Step 4: Fidelity mails check to Schwab →  No federal withholding ($0)
Step 5: Schwab receives, credits IRA →  $185,000 in Traditional IRA
Step 6: Fidelity issues 1099-R Code G →  Aisha files Form 1040 reporting non-taxable rollover

NO W-4R FILED.
```

---

## Contrast — when W-4R WOULD be needed

If Aisha had instead chosen to:

- Take a partial cash withdrawal from her 401(k) ($20K cash, $165K direct rollover) — 20% withheld on the $20K (ERD); W-4R only to ask for more than 20%
- Take all $185K as a cash distribution and roll it over within 60 days — 20% ($37K) withheld (ERD); W-4R only to ask for more; she'd need $37K from other funds to roll over the full amount
- Roll the 401(k) directly to a Roth IRA — no withholding on a direct rollover, but the pre-tax amount is taxable income for 2026 (no 10% additional tax; Pub. 575 (2025), "Rollovers to Roth IRAs"); plan the tax with Form 1040-ES. Not a W-4R case
- Later take cash out of the new Traditional IRA — that would be an other nonperiodic payment (10% default) and a W-4R case

But for a **clean direct rollover to a Traditional IRA**, no W-4R, no withholding, no complexity.

---

## Sources cited in this draft

- IRC §401(a)(31) (direct rollover option)
- IRC §402(c) (eligible rollover distribution and direct rollover)
- IRC §3405(c) (20% mandatory withholding on ERDs paid to participant)
- IRC §3405(c)(2) (direct rollover not subject to mandatory withholding)
- IRC §72(t) (early-withdrawal penalty)
- IRS Pub. 575 (Pension and Annuity Income)
- IRS Pub. 590-A (IRA Contributions, including rollovers)
- Form 1099-R instructions (Distribution Code G — direct rollover)
