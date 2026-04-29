# Example: Freelancer with SE Tax + Additional Medicare Tax

A complete walkthrough of Schedule 2 for a high-earning freelance consultant who owes both SE tax (Line 4) and Additional Medicare Tax (Line 11). This is the canonical pattern for a successful sole proprietor whose business income crosses the $200K threshold.

## The filer

- **Name**: Priya Shah
- **Filing status**: Single
- **Business**: Independent management consulting (sole proprietor, single-member LLC)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered

### Schedule C results

- Gross receipts: $312,000
- Total expenses: $48,000
- Net profit (Schedule C Line 31): **$264,000**

### Schedule SE computation

- Net SE earnings (Schedule C Line 31 × 92.35%): $264,000 × 0.9235 = $243,804
- 2025 SS wage base: $176,100 (SSA Oct 2024 announcement)
- SS portion: 12.4% × min($243,804, $176,100) = 12.4% × $176,100 = $21,836
- Medicare portion: 2.9% × $243,804 = $7,070
- **Schedule SE Line 12: $28,906**

→ **Schedule 2 Line 4 = $28,906**

Half of SE tax ($14,453) deducts on Schedule 1 Line 15.

### Additional Medicare Tax analysis

Priya's only earned income is SE — no W-2 wages. She has no spouse.

- SE earnings (Form 8959 source): $243,804
- Filing-status threshold: $200,000 (single)
- SE earnings above threshold: $243,804 − $200,000 = $43,804
- Additional Medicare Tax: 0.9% × $43,804 = **$394**

Note: Form 8959 has a unique structure for SE filers. Line 8 = SE earnings from Schedule SE. Line 9 = threshold. Line 10 = wages threshold reduction (zero for Priya since she had no W-2 wages). Line 11 = Line 9 − Line 10 = $200,000. Line 12 = Line 8 − Line 11 = $43,804. Line 13 = 0.9% × Line 12 = $394.

→ **Schedule 2 Line 11 = $394**

No employer withholding to reconcile (no W-2 wages); the full $394 is owed at filing.

### NIIT analysis

Priya has small investment income:

- Brokerage interest: $1,800
- Dividends: $2,200
- Total: $4,000

But IRC §1411(c)(2) excludes income from active trades or businesses. Priya's consulting income is *active*, so her $264,000 Schedule C net profit is NOT investment income. Only the $4,000 brokerage income is.

- MAGI ≈ $250,000 (AGI after half-SE-tax adjustment)
- Threshold (single): $200,000
- MAGI excess: $50,000
- NII: $4,000
- NIIT base = lesser of $4,000 or $50,000 = $4,000
- NIIT = 3.8% × $4,000 = **$152**

→ **Schedule 2 Line 12 = $152**

### Other Schedule 2 lines

- No AMT (no ISO, no large state-tax issue, regular tax exceeds tentative minimum tax)
- No 1095-A (private health insurance, no marketplace)
- No early IRA distributions
- No household employees
- No first-time homebuyer credit
- All Lines 1, 2, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 20 = $0

## The completed Schedule 2 draft

```markdown
# Schedule 2 (Form 1040) — DRAFT for tax year 2025

## Header
Name(s) shown on Form 1040: Priya Shah
Your social security number: XXX-XX-XXXX

## Part I — Tax
 1.  Alternative minimum tax. Attach Form 6251:           $0
 2.  Excess advance premium tax credit repayment.
     Attach Form 8962:                                    $0
 3.  Add lines 1 and 2. Enter here and on Form 1040,
     1040-SR, or 1040-NR, line 17:                        $0

## Part II — Other Taxes
 4.  Self-employment tax. Attach Schedule SE:             $28,906
 5.  Social security and Medicare tax on unreported
     tip income. Attach Form 4137:                        $0
 6.  Uncollected social security and Medicare tax on
     wages. Attach Form 8919:                             $0
 7.  Total additional social security and Medicare tax.
     Add lines 5 and 6:                                   $0
 8.  Additional tax on IRAs or other tax-favored accounts.
     Attach Form 5329 if required:                        $0
 9.  Household employment taxes. Attach Schedule H:       $0
10.  Repayment of first-time homebuyer credit:            $0
11.  Additional Medicare Tax. Attach Form 8959:           $394
12.  Net investment income tax. Attach Form 8960:         $152
13.  Section 965 net tax liability:                       $0
14.  Interest on installment income (residential lots
     and timeshares):                                     $0
15.  Interest on deferred tax on installment sales
     > $150,000:                                          $0
16.  Recapture of low-income housing credit:              $0
17.  Other additional taxes:                              $0
18.  Total Other Additional Taxes (17a–17z):              $0
19.  Reserved for future use:                             —
20.  Section 965 installment from Form 965-A:             $0
21.  Add lines 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
     and 18. Enter here and on Form 1040, 1040-SR, or
     1040-NR, line 23:                                    $29,452

## Form 1040 routing
Form 1040 Line 17 (from Schedule 2 Line 3):               $0
Form 1040 Line 23 (from Schedule 2 Line 21):              $29,452

## Required upstream forms attached
- [x] Schedule SE (Line 4 = $28,906)
- [x] Form 8959 (Line 11 = $394)
- [x] Form 8960 (Line 12 = $152)

## Validation summary
- Math:
  - Line 3 = $0 + $0 = $0 ✓
  - Line 7 = $0 + $0 = $0 ✓
  - Line 21 = $28,906 + $0 + $0 + $0 + $0 + $394 + $152 + $0 + $0 + $0 + $0 + $0 = $29,452 ✓
- Cross-form: Schedule SE, 8959, 8960 attached
- Sanity:
  - SE tax $28,906 on $243,804 SE earnings = 11.86% effective (capped SS portion + uncapped Medicare) — within expected range
  - Additional Medicare Tax $394 on $43,804 excess SE earnings at 0.9% — exact match
  - NIIT $152 on $4,000 NII at 3.8% — exact match
  - Half-of-SE-tax adjustment ($14,453) confirmed on Schedule 1 Line 15
  - Active business income correctly excluded from NIIT (IRC §1411(c)(2))

## Sources cited in this draft
- IRS Form 1040 Schedule 2, Rev. 2025
- IRC §1401 (SE tax rate)
- IRC §164(f) (half-of-SE-tax deduction)
- IRC §1411 (NIIT) and §1411(c)(2) (active business exclusion)
- IRC §3101(b)(2) and §1401(b)(2) (Additional Medicare Tax)
- Rev. Proc. 2024-40 (2025 inflation adjustments)
- SSA Fact Sheet (2025 SS wage base $176,100)
- Schedule SE Instructions (i1040sse), 2025 revision
- Form 8959 Instructions (i8959), 2025 revision
- Form 8960 Instructions (i8960), 2025 revision
```

## Why each non-obvious choice

**Why isn't Priya's consulting income subject to NIIT?** IRC §1411(c)(2) explicitly excludes income derived in the *ordinary course* of a trade or business that is not a passive activity. Priya is the sole proprietor and materially participates — her consulting income is active. Only her $4,000 brokerage income is NII.

**Why does Priya's Form 8959 have only an SE component, no W-2 component?** Priya has no W-2 wages. Form 8959 Part I (wages) = 0; Part II (SE earnings) does the calculation. Priya's filing-status threshold is fully available against SE earnings (no reduction from W-2 wages).

**Why didn't Priya's quarterly estimated tax payments show up on Schedule 2?** Estimated tax payments are *credits* against tax, not additional taxes. They go on Form 1040 Line 26 (estimated tax payments). Schedule 2 reports only liabilities.

**Why didn't AMT trigger?** Priya doesn't have ISOs, has limited Schedule A SALT add-back (single, no high state tax), and no other major preferences. Her tentative minimum tax was lower than her regular tax. She still ran Form 6251 to confirm.

**Why is half of SE tax deductible above-the-line, not on Schedule 2?** The half-SE-tax adjustment is an *income* adjustment under IRC §164(f), not an *expense* on Schedule C. It reduces AGI on Schedule 1 Line 15. Schedule 2 reports the full SE tax owed (Line 4 = $28,906); the deduction for half is a separate AGI-side mechanism.

## What if Priya were audited?

Her audit defense would be:

1. Schedule C with bank-statement-traced gross receipts ($312,000)
2. Bookkeeping export with categorized expenses ($48,000) and receipts retained
3. Schedule SE worksheet showing 92.35% × $264,000 = $243,804
4. Form 8959 worksheet showing the SE-only computation path
5. Form 8960 worksheet showing the active-business exclusion under §1411(c)(2)
6. 1099-INT and 1099-DIV from her brokerage substantiating the $4,000 NII
7. Quarterly Form 1040-ES payment confirmations
