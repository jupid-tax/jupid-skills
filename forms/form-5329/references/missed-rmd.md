# Missed RMDs — Form 5329 Part IX

How to compute, report, and (most often) request a waiver for a missed
required minimum distribution.

---

## When an RMD is required

Under IRC §401(a)(9) and §408(a)(6), required minimum distributions begin
in the year the account owner reaches the "applicable age":

- **Age 70½** — owners who reached 70½ before 2020 (pre-SECURE Act)
- **Age 72** — owners who reached 72 in years 2020-2022 (SECURE Act)
- **Age 73** — owners who reach 73 in 2023-2032 (SECURE 2.0 §107)
- **Age 75** — owners who reach 73 in 2033 or later

Inherited accounts: RMDs apply differently. For deaths after 12/31/2019,
the SECURE Act 10-year rule applies to most non-spouse beneficiaries
(account fully distributed within 10 years); annual RMDs within the 10
years are required for some categories of beneficiaries (per the 2024
final regulations).

---

## Computing the RMD

```
RMD = (Account balance on December 31 of prior year) ÷ (Distribution period factor)
```

Distribution period factor comes from Pub 590-B Appendix B tables:

- **Uniform Lifetime Table** — most owners. Factor at age 73 is 26.5;
  factor at age 75 is 24.6; factor at age 80 is 20.2 (verify against
  current Pub 590-B since the IRS updated the tables effective 2022).
- **Joint Life and Last Survivor Table** — used when sole spouse
  beneficiary is more than 10 years younger than the owner
- **Single Life Table** — beneficiaries of inherited accounts

### Example

Owner aged 75 on 12/31. Traditional IRA balance on 12/31 of prior year:
$430,000. Distribution period factor at age 75 (Uniform Lifetime Table):
24.6.

```
RMD = $430,000 ÷ 24.6 = $17,479
```

If only $5,000 was distributed during the year, the shortfall (Form 5329
Line 54) is $12,479.

### Aggregation rules

- **IRA RMDs may be aggregated** across all the user's IRAs. Take the
  total RMD from any one or any combination.
- **403(b) RMDs may be aggregated** across multiple 403(b) accounts.
- **401(k) and other qualified plans** — RMD must come from each plan
  separately; no aggregation.
- **Inherited IRAs** — RMDs may be aggregated across inherited IRAs from
  the *same* decedent only.

A user with a 401(k), a traditional IRA, and an inherited IRA from a
parent must take three separate RMDs (one from each "bucket").

---

## Reporting on Form 5329 Part IX

Lines 52-55:

| Line | Field | Source |
|------|-------|--------|
| 52 | Required minimum distribution | Computed using the applicable table |
| 53 | Amount actually distributed | Sum of distributions during the year (any portion of the RMD that *was* taken) |
| 54 | Shortfall | Line 52 − Line 53 |
| 55 | Additional tax | 25% × Line 54, OR 10% (SECURE 2.0), OR 0 (waiver) |

---

## Three rate paths for Line 55

### Path 1 — 25% (default)

The standard rate post-SECURE 2.0. Was 50% before tax years beginning
after 12/31/2022 (SECURE 2.0 §302).

### Path 2 — 10% (SECURE 2.0 corrected within 2 years)

If the user takes the missed amount within 2 years of the end of the year
it should have been taken (and before the IRS issues a deficiency notice
for the missed RMD), the rate drops from 25% to 10% under IRC §4974(e),
added by SECURE 2.0 §302.

The 2-year window:
- For a missed 2024 RMD, corrective distribution must be taken by
  12/31/2026 to qualify for 10%
- For a missed 2025 RMD, corrective distribution must be taken by
  12/31/2027 to qualify for 10%

If the user takes the corrective distribution after the 2-year window,
the rate stays at 25%.

### Path 3 — 0 (waiver request)

If the missed RMD was due to "reasonable cause" and the user is taking
"reasonable steps to remedy the shortfall," the user can request a
waiver under IRC §4974(d). The IRS approves these liberally in practice
when reasonable cause is documented.

To request:
1. Take the missed RMD as soon as possible (the corrective distribution
   itself is part of "remedying the shortfall")
2. Compute Line 54 (the shortfall)
3. **Write 0 on Line 55** (not the 25% or 10% calculation)
4. **Attach a statement** to Form 5329 explaining (i) the reasonable
   cause and (ii) the corrective steps

Some practitioners write "RC" (reasonable cause) next to Line 54 on the
form. The instructions don't require this but it flags the waiver to the
IRS reviewer.

---

## Waiver request statement template

The statement is short, factual, and labeled clearly. Use the user's own
words for reasonable cause; do not template a reason that isn't true.

```markdown
# Form 5329 Line 54 — Waiver Request Statement

Filer: <full legal name>
SSN: <SSN>
Tax Year: YYYY

## Account information

Account: <Custodian name + account type, e.g., "Fidelity Inherited
Traditional IRA, account #XXXX-XXXX">
Decedent (if inherited): <decedent name + DOD>
Required minimum distribution for YYYY: $X,XXX
Distribution actually taken in YYYY: $X,XXX
Shortfall: $X,XXX

## Reasonable cause

[2-4 sentences explaining the cause. Examples of accepted causes:

- "I inherited this IRA from my parent who died on [date]. As a non-spouse
  beneficiary I was unaware of the year-of-death RMD requirement. I
  learned of it on [date] when I consulted with [advisor name]."

- "Due to a [serious illness / family emergency / other life event] from
  [date] to [date], I missed the deadline to take my RMD."

- "My account custodian's automated RMD program failed to distribute the
  required amount due to [system error / address change / other]. I
  discovered this when reviewing my year-end statements in [month YYYY]."

- "I turned 73 in YYYY and was uncertain whether the new RMD age
  applied to me. I consulted with [advisor] in [month YYYY] and at that
  point requested the missed distribution."]

## Steps to remedy

I have taken / will take the following corrective actions:

1. On [date], I requested the missed distribution amount of $X,XXX from
   [custodian]. The distribution was processed on [date].
2. I have set up [automatic RMD distributions / calendar reminders /
   advisor oversight] to ensure timely RMDs in future years.
3. [Any additional remedial steps.]

## Request

I respectfully request that the IRS waive the additional tax under
IRC §4974(d). I have entered $0 on Line 55 of Form 5329 pending review of
this waiver request.

Filer signature: _______________________
Date: __________
```

---

## Approval rates and what to expect

The IRS approves the vast majority of well-documented waiver requests.
The factors that drive approval:

1. **The missed amount has been distributed** (or will be soon) — the
   "remedy" prong of §4974(d). A waiver request without corrective
   distribution is much weaker.

2. **The cause is one a reasonable person would experience** — illness,
   death of family member, custodian error, recently inherited account,
   misunderstanding of the new age threshold. "I forgot" is *not* generally
   accepted.

3. **The statement is specific and dated** — vague language hurts.
   "Sometime last year" → bad. "I learned of the requirement on March 14,
   2025, when reviewing the account with my CPA" → good.

4. **Documentation is referenced** (not necessarily attached) — "supported
   by Dr. Smith's letter dated [date]" or "as shown in custodian
   correspondence dated [date]".

The IRS typically responds within 60-180 days with either silent approval
(no notice = approved; the original 0 on Line 55 stands) or a CP letter
requesting more information or denying the waiver.

---

## What if multiple RMDs were missed across multiple accounts

If the user missed RMDs from more than one account, sum the shortfalls
into Line 54. The waiver statement should identify each affected account:

```markdown
## Account information

Total shortfall: $X,XXX across the following accounts:

| Account | Required | Actual | Shortfall |
|---------|----------|--------|-----------|
| Fidelity Traditional IRA #XXXX | $5,200 | $0 | $5,200 |
| Vanguard Inherited IRA #YYYY | $3,400 | $1,000 | $2,400 |
| Schwab 403(b) #ZZZZ | $4,800 | $4,800 | $0 |
| **Total** | **$13,400** | **$5,800** | **$7,600** |
```

---

## Coordination with the corrective distribution itself

When the user takes the corrective distribution to remedy the missed RMD,
that distribution is reported on a 1099-R for the year it's actually
taken (not the year it should have been taken). The user reports it as
ordinary income on Form 1040 Lines 4a/4b or 5a/5b in the year of
distribution.

The fact that it was "for" a prior year's RMD doesn't change its tax
treatment in the actual year of receipt — it's still ordinary income then.

---

## Edge case: first-year RMD with April 1 deadline

A user reaching age 73 has the option to delay the *first* year's RMD to
April 1 of the following year (the "required beginning date" rule).
Taking advantage of this means two RMDs in the second year — the delayed
first-year RMD plus the second-year RMD — both taxable in the second
year.

This is a planning choice, not a missed RMD. Don't file Part IX for a
first-year delay properly elected and taken by April 1.

Where Part IX *does* apply: the user delayed the first-year RMD past
April 1 of the year after turning 73 — that's a missed RMD.
