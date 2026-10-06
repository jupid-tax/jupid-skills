# Missed RMDs — Form 5329 Part IX

How to compute, report, and (most often) request a waiver for a missed
required minimum distribution.

---

## When an RMD is required

Under IRC §401(a)(9) and §408(a)(6), required minimum distributions begin
in the year the account owner reaches the "applicable age":

- **Age 70½** — owners who reached 70½ before 2020 (pre-SECURE Act)
- **Age 72** — owners who reached 72 in years 2020-2022 (SECURE Act)
- **Age 73** — owners who reach 72 after 2022 and 73 before 2033 (IRC §401(a)(9)(C)(v)(I), SECURE 2.0 §107)
- **Age 75** — owners who reach 74 after December 31, 2032 (IRC §401(a)(9)(C)(v)(II))

Inherited accounts: RMDs apply differently. For deaths after 12/31/2019,
the SECURE Act 10-year rule applies to most non-spouse beneficiaries
(account fully distributed within 10 years); annual RMDs within the 10
years are required for some categories of beneficiaries (per the 2024
final regulations). Pub. 590-B (2025) notes excise tax relief for certain
missed 2024 RMDs under Notice 2024-35; check whether a missed inherited-IRA
RMD falls in a relief year before computing Part IX.

---

## Computing the RMD

```
RMD = (Account balance on December 31 of prior year) ÷ (Distribution period factor)
```

Distribution period factor comes from Pub 590-B Appendix B tables:

- **Uniform Lifetime Table (Table III)** — most owners. Factor at age 73
  is 26.5; factor at age 75 is 24.6; factor at age 80 is 20.2 (Pub. 590-B
  (2025), Appendix B).
- **Joint Life and Last Survivor Table** — used when sole spouse
  beneficiary is more than 10 years younger than the owner
- **Single Life Table** — beneficiaries of inherited accounts

### Example

Owner aged 75 on 12/31. Traditional IRA balance on 12/31 of prior year:
$430,000. Distribution period factor at age 75 (Uniform Lifetime Table):
24.6.

```
RMD = $430,000 ÷ 24.6 = $17,479.67 → $17,480
```

If only $5,000 was distributed during the year, the shortfall (Form 5329
Line 52b − Line 53b, or 52a − 53a if fully corrected in the window) is
$12,480.

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

Lines 52a-55 (2025 Form 5329; the a/b split was already on the 2024 form):

| Line | Field | Source |
|------|-------|--------|
| 52a | RMD from plans whose full shortfall was distributed during the correction window | Computed using the applicable table |
| 52b | RMD from all other plans | Computed using the applicable table |
| 53a / 53b | Amount distributed during the tax year from those plans | Distributions during the year only; not distributions after the RMD deadline or during the correction window |
| 54a | (52a − 53a) × 10% | Reduced rate |
| 54b | (52b − 53b) × 25% | Default rate |
| 55 | 54a + 54b | → Schedule 2 (Form 1040), line 8 |

---

## Three rate paths for Line 55

### Path 1 — 25% (default)

The standard rate post-SECURE 2.0. Was 50% before tax years beginning
after 12/31/2022 (SECURE 2.0 §302).

### Path 2 — 10% (corrected during the correction window)

The rate drops from 25% to 10% under IRC §4974(e), added by SECURE 2.0
§302, if during the correction window the user (1) receives a distribution
of the shortfall from the plan for which the tax was imposed and (2) files
a return reflecting the tax (2025 Instructions for Form 5329, Reduced tax
rate). The correction window ends on the earliest of: the date a deficiency
notice for the tax is mailed, the date the tax is assessed, or the last day
of the second taxable year that begins after the end of the taxable year in
which the tax is imposed.

For calendar-year filers:
- Missed 2024 RMD: window ends no later than 12/31/2026
- Missed 2025 RMD: window ends no later than 12/31/2027

If the user takes the corrective distribution after the window, the rate
stays at 25%.

### Path 3 — 0 (waiver request)

If the missed RMD was due to "reasonable cause" and the user is taking
"reasonable steps to remedy the shortfall," the user can request a
waiver under IRC §4974(d): the shortfall must be due to reasonable error
and the user must be taking reasonable steps to remedy it.

To request (2025 Instructions for Form 5329, "Waiver of tax for reasonable
cause"):
1. Take the missed RMD as soon as possible (the corrective distribution
   itself is part of "remedying the shortfall")
2. Complete Lines 52a/52b and 53a/53b as instructed
3. **Enter "RC" and the shortfall amount to be waived in parentheses on
   the dotted line next to Line 54a and/or 54b.** Subtract it from the
   shortfall and enter the result (at that line's rate) on Line 54a/54b;
   a full waiver leaves 0
4. Complete Line 55 and pay any tax it shows
5. **Attach a statement** to Form 5329 explaining (i) the reasonable
   error and (ii) the steps taken to remedy the shortfall

---

## Waiver request statement template

The statement is short, factual, and labeled clearly. Use the user's own
words for reasonable cause; do not template a reason that isn't true.

```markdown
# Form 5329 Lines 54a/54b — Waiver Request Statement

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
IRC §4974(d). I have entered "RC" and the waived amount next to Line
54a/54b of Form 5329 as the instructions direct.

Filer signature: _______________________
Date: __________
```

---

## Approval rates and what to expect

The IRS does not publish approval rates. The factors that matter:

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

Per the instructions, the IRS reviews the information and decides whether
to grant the waiver; if it is not granted, the IRS notifies the user of the
additional tax owed. No timeline is published.

---

## What if multiple RMDs were missed across multiple accounts

If the user missed RMDs from more than one account, total the RMDs and
distributions on Lines 52a/53a (plans fully corrected in the window) and
52b/53b (all others). The waiver statement should identify each affected
account:

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
