# Example — Offshore Trust Distribution (Default Method, Throwback)

End-to-end Form 3520 for a US beneficiary receiving a distribution from
a foreign non-grantor trust that does NOT provide a Beneficiary
Statement. Part III + Schedule C (default method) + Form 4970.

## Filer profile

- **Name**: Sarah Patel (US citizen)
- **SSN**: 345-67-8901 (illustrative)
- **Address**: 1840 Madison Avenue, New York, NY 10029
- **Filing status**: Single
- **Tax year**: 2026 (calendar year)

## Background

Sarah is the US-citizen beneficiary of a Cayman Islands trust established
in 2015 by her late father (UK citizen, never a US resident). The trust:

- Was established in Cayman Islands under Cayman law
- Has discretionary distribution provisions (trustees decide who gets
  what, when)
- Has Sarah's siblings (UK and Singapore residents) and Sarah herself as
  beneficiaries
- Is administered by Cayman Trust Company Ltd.
- Has accumulated approximately $4,200,000 of undistributed income since
  2015 (per the trust's available accounting)

Sarah has been a beneficiary since 2015. She received NO distributions
prior to 2024.

## §679 status — N/A

Sarah's father set up the trust; he was not a US person. §679 applies
only when a **US person** transfers property to a foreign trust that has
a US beneficiary. Sarah did not transfer property to this trust; her
father did, and he was not a US person.

Therefore Sarah is NOT a US owner of this trust. The trust is a **foreign
non-grantor trust** as to Sarah. She has no Part II obligation, only
Part III when she receives a distribution.

## Distribution history

- 2023: $0 received from trust
- 2024: $40,000 cash distribution from trust to Sarah
- 2025: $80,000 cash distribution
- 2026: **$500,000 cash distribution** received on August 30, 2026

Sarah filed Form 3520 Part III for 2024 ($40,000) and 2025 ($80,000).
The trust did not provide a Beneficiary Statement in those years either.

For the smaller 2024 and 2025 distributions, Sarah's tax preparer
applied default method but the excess distribution calculation produced
small amounts because the prior-year averages were either zero or modest.

The 2026 $500,000 is a different scale and the default method math gets
ugly.

## Beneficiary Statement availability

Sarah has asked Cayman Trust Company Ltd. for a Foreign Nongrantor Trust
Beneficiary Statement for 2026. The trustee responded that they do not
prepare such statements and that doing so would "violate the trust's
confidentiality obligations under Cayman law."

The trustee's position is wrong on US tax grounds (the IRS does not
honor foreign confidentiality clauses) but Sarah has no practical way to
compel a Beneficiary Statement. She is forced into the default method.

## Default method calculation (Schedule C of Part III)

### Step 1 — Current distribution

$500,000 received 2026-08-30. Already in USD; no currency conversion
needed (Cayman Trust Company sent USD wire).

### Step 2 — Prior 3-year average

Years 2023, 2024, 2025:

- 2023: $0
- 2024: $40,000
- 2025: $80,000
- Sum: $120,000
- Average: $40,000

### Step 3 — Excess distribution

Excess = $500,000 − (1.25 × $40,000) = $500,000 − $50,000 = **$450,000**

### Step 4 — Allocate excess across throwback years

Trust was created in 2015 and Sarah has been a US beneficiary the entire
time. Throwback years are 2015 through 2025 = **11 years**.

Per-year deemed accumulation distribution: $450,000 ÷ 11 ≈ **$40,909/year**

### Step 5 — Compute throwback tax (Form 4970)

Sarah's highest marginal tax rate in any of the 3 immediately preceding
years (2023, 2024, 2025) was 32% (in 2024 when she had a high-income
year with bonuses).

Using simplified method: **Throwback tax = 32% × $450,000 = $144,000**

(The formal year-by-year recomputation under §667(b) would require
reconstructing Sarah's 2015-2025 returns and adding the per-year deemed
amount to each. The simplified method using highest recent marginal
rate is allowed by Form 4970 instructions and is what most practitioners
use when full reconstruction isn't feasible.)

### Step 6 — Compute §668(a) interest charge

The interest charge is roughly: per-year tax × underpayment rate ×
(years from throwback year to current year).

Approximating with a uniform 5% underpayment rate (current AFR
underpayment rates are at https://www.irs.gov/payments/quarterly-interest-rates):

For each of the 11 throwback years (2015-2025), the per-year tax of
~$13,090 ($144,000 / 11) accrues interest from that year to 2026.

| Throwback year | Years to 2026 | Per-year tax | Interest |
|----------------|---------------|--------------|----------|
| 2015           | 11            | $13,090      | $7,200   |
| 2016           | 10            | $13,090      | $6,545   |
| 2017           | 9             | $13,090      | $5,890   |
| 2018           | 8             | $13,090      | $5,236   |
| 2019           | 7             | $13,090      | $4,581   |
| 2020           | 6             | $13,090      | $3,927   |
| 2021           | 5             | $13,090      | $3,272   |
| 2022           | 4             | $13,090      | $2,618   |
| 2023           | 3             | $13,090      | $1,963   |
| 2024           | 2             | $13,090      | $1,309   |
| 2025           | 1             | $13,090      | $654     |
| **Total**      |               | $144,000     | **$43,195** |

(These figures use simple interest at 5% and are illustrative; the actual
Form 3520 instructions and Form 4970 instructions specify the exact
compounding method, which uses the IRS quarterly underpayment rates
applied per the §668 formula. The skill's deliverable should use the
form's worksheet and not the simple approximation here.)

### Step 7 — Total additional US tax in 2026

- Throwback tax (added on Form 1040 via Form 4970): **$144,000**
- §668(a) interest charge (added on Form 1040 Schedule 2): **$43,195**
- **Total additional tax**: $187,195

Effective rate on the $500,000 distribution: 37.4%. Sarah's regular tax
on her other 2026 income is unchanged (the throwback tax is in addition
to her normal tax on her wages, etc.).

If Sarah had obtained a Beneficiary Statement showing that the
distribution was 80% long-term capital gains (taxed at 20%) and 20%
qualified dividends (15%), the actual-method tax would have been roughly
$500,000 × 0.19 = $95,000 — a savings of $92,195. The skill flags this
and recommends Sarah escalate the Beneficiary Statement request for
future years (perhaps via UK or Cayman counsel; a US tax practitioner
familiar with Cayman trusts may have leverage).

## Filled draft

```markdown
# Form 3520 — DRAFT for tax year 2026

## Filer identification
Name: Sarah Patel
Identifying number: 345-67-8901
Address: 1840 Madison Avenue, New York, NY 10029
Filing status: Single
Country of citizenship: USA
Initial: No (3rd Form 3520 for this trust; first was 2024)

## Parts being filed
- [ ] Part I
- [ ] Part II
- [x] Part III — Distribution from foreign trust
- [ ] Part IV

## Part III — Distribution

Foreign trust name: [Father's name] Family Settlement
Trust country: Cayman Islands
Trust governing law: Cayman Islands
Trust EIN (US): None (trust has no US EIN; uses Cayman registration)
Trust type: **Non-grantor trust** (settlor was non-US person; no
              §679 applicable)
Trustee: Cayman Trust Company Ltd., P.O. Box XXXX, Grand Cayman KY1-XXXX

Beneficiary Statement provided for 2026: No
Method used: **Default method (Schedule C)**

Distribution detail:
| Line | Date       | Type | Description                | FMV (USD) |
|------|------------|------|----------------------------|-----------|
| 28a  | 2026-08-30 | Cash | Wire from Cayman Trust Co. | $500,000  |
| 29   | Total                                       | $500,000  |

## Schedule C — Default method calculation

| Line | Item                                       | Amount     |
|------|--------------------------------------------|------------|
|      | Current year distribution                  | $500,000   |
|      | Prior 3-year distributions:                |            |
|      |   2023                                     | $0         |
|      |   2024                                     | $40,000    |
|      |   2025                                     | $80,000    |
|      |   Sum                                      | $120,000   |
|      |   Average (÷ 3)                            | $40,000    |
|      | 1.25 × Average                             | $50,000    |
|      | Excess distribution                        | $450,000   |
|      | Throwback years (2015-2025)                | 11         |
|      | Per-year deemed amount                     | $40,909    |
|      | Highest recent marginal rate (simplified)  | 32%        |
|      | Throwback tax (Form 4970)                  | $144,000   |
|      | §668(a) interest charge (worksheet)        | $43,195    |
|      | Total additional 2026 tax                  | $187,195   |

## Currency translation
Source: Wire received in USD; no conversion needed
Notes: Trust corpus is denominated and administered in USD by Cayman
trustee; no FX adjustment required for this distribution

## Required attachments
- [ ] Form 4970 — attached to Form 1040, NOT to Form 3520; reflects
      throwback tax of $144,000 added to Schedule 2 of Form 1040
- [ ] Statement re: Beneficiary Statement request — Sarah's
      correspondence with Cayman Trust Company Ltd. showing 2026
      Beneficiary Statement was requested and refused (supports
      reasonable cause if IRS questions default method)
- [ ] Trust accounting (any portion provided by trustee) — kept with
      Sarah's records, not necessarily filed

## Mailing address (for Form 3520)
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math: prior 3-year sum $120,000 / 3 = $40,000 ✓
- Math: excess $500,000 − $50,000 = $450,000 ✓
- Math: per-year $450,000 / 11 = $40,909 ✓
- Math: throwback tax $450,000 × 32% = $144,000 ✓
- Math: §668(a) interest worksheet result reconciled with
        approximation (verify exact figure using Form 3520 Schedule C
        worksheet and quarterly interest rates)
- Sanity: Default method generated $187,195 additional tax on
        $500,000 (37.4% effective). Recommend Sarah escalate
        Beneficiary Statement request for 2027 and beyond to avoid
        recurrence.
- Sanity: Throwback period spans 11 years; if Sarah was not a US
        person for any portion (e.g., became citizen later), the
        throwback period may be shorter. CONFIRM Sarah was a US
        person for 2015-2025 throughout.
- Cross-form: Form 4970 must be attached to Form 1040; the $144,000
        flows to Schedule 2 line 17z (or wherever Form 4970
        instructions direct for current revision). §668 interest
        charge of $43,195 also goes on Schedule 2 with notation
        "§668 interest".
- Next steps:
  1. Sarah signs Form 3520 in blue ink
  2. Mail Form 3520 to Ogden by April 15, 2027 (or October 15, 2027 if
     Form 4868 extension filed)
  3. File Form 1040 with attached Form 4970 and Schedule 2 entries
  4. Pay the $187,195 additional tax (or apply withholding/estimated
     payments if available)
  5. For 2027 onward: Sarah should engage an international tax
     practitioner to push Cayman Trust Company for a Beneficiary
     Statement, OR explore alternative reporting positions (e.g., trust
     accountings reconstructed to support an actual-method calculation)

## Sources cited in this draft
- IRS Form 3520 (latest revision)
- IRS Instructions for Form 3520 (latest revision)
- IRS Form 4970 (Tax on Accumulation Distribution of Trusts)
- IRS Instructions for Form 4970
- IRC §665 (definitions, including UNI)
- IRC §667 (treatment of amounts deemed distributed by trust in prior
  years; throwback rules)
- IRC §668 (interest charge on accumulation distributions)
- IRC §6048 (information returns for foreign trusts)
- IRC §6677 (penalties for late/incomplete filing)
- IRS quarterly underpayment interest rate publications
```

## Why this case is painful

- The default method is structurally punitive
- Sarah has no leverage with the Cayman trustee
- The trust likely accumulated mostly capital gains income that would
  have been taxed at 20% under actual method, but default method taxes
  at 32% ordinary rate plus interest charge
- The interest charge runs from 2015 (when the trust first started
  accumulating) — 11 years of compounding
- Future distributions will face the same default method until a
  Beneficiary Statement is obtained

## Mitigation strategies (out of scope for this skill, redirect to a CPA)

- Negotiate with the trustee for a Beneficiary Statement (sometimes
  successful when escalated to senior trust officers or via legal
  counsel)
- Request a US tax accounting reconstruction from the trustee — even
  partial accountings can support an actual-method position
- Consider whether the trust could be restructured (e.g., decanted into
  a new trust with a cooperative US-aware trustee) — this is a
  practitioner-level project
- For Sarah personally: avoid taking large distributions in a single
  year if the default method applies; spread distributions across
  multiple years to keep the 3-year average closer to the current-year
  amount and reduce the "excess"

## What would simplify this case

- A Beneficiary Statement → actual method, likely much lower tax
- A trustee willing to file Form 3520-A on the trust's behalf (the trust
  is non-grantor, so 3520-A doesn't strictly apply, but a Beneficiary
  Statement modeled on the 3520-A page 4 information would substitute)
- Sarah being a UK or Singapore tax resident instead of US — the entire
  problem disappears outside the US tax net
