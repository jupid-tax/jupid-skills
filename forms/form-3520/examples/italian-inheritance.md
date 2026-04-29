# Example — Italian Cash Inheritance ($200,000)

End-to-end Form 3520 for a US citizen who received a cash inheritance
from a foreign individual in Italy. Part IV only.

## Filer profile

- **Name**: Anna Romano (US citizen)
- **SSN**: 123-45-6789 (illustrative)
- **Address**: 412 Elm Street, Boston, MA 02116
- **Filing status**: Single
- **Tax year**: 2026 (calendar year)

## The transaction

Anna's maternal grandmother, Maria Bianchi (Italian citizen, lifelong
resident of Bologna, Italy), passed away in May 2026. Under her Italian
will, Anna inherited €185,000 in cash from her grandmother's estate.

The funds were wired from the Italian estate's bank account
(Intesa Sanpaolo, Bologna) to Anna's US Bank of America checking
account on **August 12, 2026**. The wire amount was €185,000. Bank of
America credited Anna's account with **$201,235** at the spot exchange
rate of $1.0878/EUR on the receipt date (illustrative rate).

There were no other foreign gifts received by Anna during 2026.

## Threshold check

- Foreign individuals + foreign estates: aggregate $201,235 > $100,000 ✓
  → Part IV reporting required for this category
- Foreign corporations + foreign partnerships: $0; below threshold; no
  reporting needed

Note: an inheritance from a foreign individual's estate is treated as a
gift from a foreign individual for §6039F purposes. The estate of Maria
Bianchi is a "foreign estate" under §7701(a)(31)(A); it falls in the
$100,000 bucket together with foreign individual donors.

## Currency translation

Spot rate on August 12, 2026: $1.0878/EUR (Federal Reserve H.10 release,
illustrative).

USD value: €185,000 × $1.0878 = $201,243. (Use the bank's recorded
credit if it differs slightly from the spot rate; document the
discrepancy.)

For consistency, Anna uses the **bank's recorded USD credit of $201,235**
because that's what hit her account. Any small spread between the
Federal Reserve rate and the bank's rate is the bank's currency
conversion fee — already netted out.

## Which Parts apply

- Part I — No (Anna didn't transfer property to a foreign trust)
- Part II — No (Anna is not a US owner of a foreign trust)
- Part III — No (Anna didn't receive a distribution from a foreign trust)
- **Part IV — Yes** (aggregate gift from foreign individuals/estates >
  $100,000)

Only Part IV is filled.

## Filled draft

```markdown
# Form 3520 — DRAFT for tax year 2026

## Filer identification
Name: Anna Romano
Identifying number: 123-45-6789
Address: 412 Elm Street, Boston, MA 02116
Filing status: Single
Country of citizenship: USA
Initial: Yes

## Parts being filed
- [ ] Part I
- [ ] Part II
- [ ] Part III
- [x] Part IV — Receipt of gift from foreign person

## Part IV — Gifts/Bequests
Aggregate from foreign individuals + foreign estates: $201,235
Threshold: $100,000 (statutory; IRC §6039F(c)(1)(B))
Aggregate from foreign corporations + foreign partnerships: $0
Threshold: $19,570 for 2025 (Rev. Proc. 2024-40); 2026 figure verified
against Form 3520 instructions

| Donor name      | Type            | Country | Date       | Description    | FMV (USD) |
|-----------------|-----------------|---------|------------|----------------|-----------|
| Estate of Maria | Foreign estate  | Italy   | 2026-08-12 | Cash bequest   | $201,235  |
|  Bianchi        |                 |         |            | by will        |           |

Donor address: c/o Studio Notarile Rossi, Via Indipendenza 12,
40121 Bologna, Italy
Relationship to filer: Maternal grandmother (decedent)

Line 56 attestations:
- Donor related to filer: Yes (grandparent)
- Donor is a CFC or PFIC: N/A (donor is a foreign estate, not a corp)

## Currency translation
Source: Bank of America wire credit conversion on 2026-08-12
Rate: ~$1.0878/EUR (cross-checked against Federal Reserve H.10 release)
Notes: Bank credit of $201,235 used as authoritative USD value

## Required attachments
- [ ] None required for Part IV-only filing
- [ ] Recommended: copy of Italian will or notarized estate distribution
      letter, showing Anna as a named beneficiary (kept with user's
      records, not necessarily filed)

## Mailing address
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math: aggregate $201,235 correctly compared against $100,000 threshold
- Sanity: gift is from an estate (foreign decedent's estate), correctly
  bucketed with foreign individuals; no anti-abuse flags
- Next steps:
  1. Anna prints, signs in blue ink, mails to Ogden via USPS Certified
     Mail with Return Receipt by April 15, 2027 (or October 15, 2027 if
     she extends Form 1040 via Form 4868)
  2. Anna does NOT report this on Form 1040 — gifts and inheritances are
     excluded from gross income under IRC §102
  3. Anna does NOT file Form 8938 unless the inherited funds are in a
     foreign financial account at year-end (after wire to US, they're
     not foreign anymore)
  4. If the funds had been left in the Italian bank account in Anna's
     name during 2026, FBAR (FinCEN 114) would apply for any month-end
     balance > $10,000 — confirm with Anna

## Sources cited in this draft
- IRS Form 3520 (latest revision)
- IRS Instructions for Form 3520 (latest revision)
- IRC §102 (gifts and inheritances excluded from gross income)
- IRC §6039F (information returns for gifts from foreign persons)
- IRC §6677 (penalties for failure to file)
- IRC §7701(a)(31)(A) (foreign estate definition)
- Federal Reserve H.10 daily exchange rate report
```

## Why this is straightforward (when it is)

- Single transaction; clear date; cash; bank-mediated transfer
- Donor was clearly a foreign individual / foreign estate, not an entity
- No relationship between the donor and any US person business
- Anna was not previously involved with any foreign trust
- No FBAR / 8938 trigger because funds moved promptly to a US bank

## Edge cases the agent should flag

- **If funds had stayed in Italy** for any month-end during 2026,
  FBAR (FinCEN 114) reporting applies for the month of receipt and
  any subsequent months until the funds are removed from foreign
  account. Form 8938 may also apply if the year-end balance exceeds
  the §6038D threshold.
- **If Anna inherited real estate** (an Italian apartment), the
  reporting is similar — list the property by description with FMV in
  USD as of the date of bequest. Also: the Italian apartment may
  trigger ongoing FBAR if held in a foreign trust/Fideicomiso, or
  ongoing 8938 if it's held through a foreign entity.
- **If the will named multiple US beneficiaries**, each US beneficiary
  files their own Form 3520 for their share. Each is independently
  subject to the $100,000 threshold.
- **If the funds came as a series of payments** over months (e.g., the
  Italian estate distributed in three tranches), aggregate the tranches
  for the threshold check; report each tranche as a separate line in
  the Part IV table with its own date and FMV.
