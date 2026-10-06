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

- Nonresident alien individuals + foreign estates (line 54): $201,235 >
  $100,000 ✓ → line 54 "Yes"
- Foreign corporations + foreign partnerships (line 55): $0, below the
  2026 §6039F threshold of $20,573 (Rev. Proc. 2025-32 §4.47); line 55
  "No"

Note: a bequest from a foreign decedent's estate is reported on line 54
("gifts or bequests from a nonresident alien ... or a foreign estate").
The estate of Maria Bianchi is a foreign estate (§7701(a)(31)(A)).

## Currency translation

Spot rate on August 12, 2026: $1.0878/EUR (illustrative; the agent uses
the actual rate for the date).

USD value: €185,000 × $1.0878 = $201,243 (python). (Use the bank's recorded
credit if it differs slightly from the spot rate; document the
discrepancy.)

For consistency, Anna uses the **bank's recorded USD credit of $201,235**
because that's what hit her account. Any small spread between the
published rate and the bank's rate is the bank's currency conversion
spread — already netted out. Document both.

## Which Parts apply

- Part I — No (Anna didn't transfer property to a foreign trust)
- Part II — No (Anna is not a US owner of a foreign trust)
- Part III — No (Anna didn't receive a distribution from a foreign trust)
- **Part IV — Yes** (aggregate gift from foreign individuals/estates >
  $100,000)

Only Part IV is filled.

## Filled draft

```markdown
# Form 3520 (Rev. December 2023) — DRAFT for tax year 2026

## Page 1
A. Initial return: [x]
B. Filer type: Individual
C. Counted on Form 8938: No (Anna does not file Form 8938)
Trigger box checked: Part IV (gifts or bequests from foreign persons)
1a. Name: Anna Romano           1b. TIN: 123-45-6789
1c, 1e–1h. Address: 412 Elm Street, Boston, MA 02116, United States
1d. Spouse's TIN: (blank)
1i. Joint Form 3520: [ ]   1j. 2-month extension: [ ]
1k. Income tax return extension: [ ] (check and enter 4868 if she extends)
2a–4f. (blank — no foreign trust, no decedent filing)

## Part IV — Gifts or bequests from foreign persons
54. More than $100,000 from a nonresident alien or foreign estate: Yes
| (a) Date of gift or bequest | (b) Description of property received | (c) FMV of property received |
|-----------------------------|---------------------------------------|------------------------------|
| 08/12/2026                  | Cash bequest under Italian will (€185,000 wire from estate account) | $201,235 |
Total: $201,235
55. Gifts from foreign corporations / partnerships over $20,573: No
56. Donor acting as nominee or intermediary: No

## Currency translation
Source: Bank of America wire credit on 2026-08-12
Rate: ~$1.0878/EUR (illustrative)
Notes: Bank credit of $201,235 used as the USD value; rate source documented

## Required attachments
- None required for a Part IV-only filing
- Recommended for her records (not filed): copy of the Italian will or the
  notary's estate distribution letter naming Anna, and the wire record

## Mailing address
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math: $201,235 > $100,000 → line 54 required; single bequest over $5,000 listed
- Line 55 below the 2026 threshold → "No"
- Sanity: bequest from a foreign estate, correctly on line 54; no nominee
- Next steps:
  1. Anna prints, signs, and mails to Ogden via USPS Certified Mail with
     Return Receipt by April 15, 2027 (or by October 15, 2027 if she
     extends Form 1040 with Form 4868 and checks line 1k)
  2. Anna does NOT report this on Form 1040 — gifts and inheritances are
     excluded from gross income under IRC §102
  3. Form 8938: the inheritance sits in a U.S. account, so it is not a
     specified foreign financial asset
  4. If the funds had first been deposited to a foreign account in Anna's
     name, FBAR (FinCEN 114) would apply if the aggregate maximum value of
     her foreign accounts exceeded $10,000 at any time during 2026 —
     confirm with Anna

## Sources cited in this draft
- IRS Form 3520 (Rev. December 2023) and Instructions (Rev. December 2025), Part IV, line 54
- Rev. Proc. 2025-32 §4.47 (2026 §6039F threshold $20,573)
- IRC §102 (gifts and inheritances excluded from gross income)
- IRC §6039F (information returns for gifts from foreign persons)
- IRC §7701(a)(31)(A) (foreign estate definition)
```

## Why this is straightforward (when it is)

- Single transaction; clear date; cash; bank-mediated transfer
- Donor was clearly a foreign individual / foreign estate, not an entity
- No relationship between the donor and any US person business
- Anna was not previously involved with any foreign trust
- No FBAR / 8938 trigger because funds moved promptly to a US bank

## Edge cases the agent should flag

- **If funds had stayed in an Italian account in Anna's name**, FBAR
  (FinCEN 114) applies if the aggregate maximum value of her foreign
  accounts exceeded $10,000 at any time during 2026, and Form 8938 may
  apply if her specified foreign financial assets exceed the Form 8938
  thresholds. Ask for the account history.
- **If Anna inherited real estate** (an Italian apartment), the
  reporting is similar — list the property on line 54 by description with
  FMV in USD as of the date of the bequest. Directly held foreign real
  estate is not itself an FBAR or Form 8938 asset; if it is held through
  a foreign entity, the interest in the entity may be.
- **If the will named multiple US beneficiaries**, each US beneficiary
  tests the $100,000 amount on what they personally received and files
  their own Form 3520 if it is exceeded.
- **If the funds came as a series of payments** over months (e.g., the
  Italian estate distributed in three tranches), aggregate the tranches
  for the threshold check; report each tranche over $5,000 as a separate
  line 54 row with its own date and FMV.
- **If gifts also came from other relatives abroad**, aggregate gifts
  from donors who are related to each other (Instructions, Line 54).
