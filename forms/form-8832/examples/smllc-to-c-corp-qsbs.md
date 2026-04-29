# Example: SMLLC Electing C-Corp for QSBS Strategy

A complete walkthrough of Form 8832 for a single-member LLC pivoting to C-corporation status to position for §1202 Qualified Small Business Stock (QSBS) treatment. This is the canonical "founder approaching priced round" pattern.

## The filer

- **Entity**: Marlowe Labs LLC, a single-member Delaware LLC
- **Owner**: Eli Marlowe (sole member), 100% interest
- **Formation date**: 2024-03-12
- **Tax year**: Calendar year
- **Current classification**: Default disregarded entity (Schedule C filer for 2024 and 2025)
- **Reason for election**: Marlowe Labs is approaching a $2M priced seed round in Q3 2026. The lead investor's term sheet requires C-corporation status. Eli also wants to qualify the equity for §1202 QSBS treatment to position for a future $10M-or-more gain exclusion at exit.
- **Desired effective date**: 2026-08-01 (sixty days before the priced round closes 2026-09-30, giving §1202 holding-period clock a head start on the post-conversion stock)

## Eligibility check (Step 1)

- Domestic eligible entity (Delaware LLC, not a state-law corporation): ✓
- Not on foreign per-se corporation list (irrelevant, domestic): ✓
- Not a trust, estate, REIT, RIC, or other excluded type: ✓
- Prior Form 8832 elections in last 60 months: None (defaulted disregarded since formation): ✓ — this is an initial classification election

Eligible. Proceed.

## Election target (Step 2)

- Line 3: One owner (Eli, 100%) → Yes / No question is **No** (does NOT have more than one owner)
- Available election targets for single-owner: Box 6(a) association OR Box 6(c) disregarded
- Current default: disregarded → no need to elect 6(c) (no-op)
- Desired: C-corporation tax treatment → Box 6(a)

## Effective-date calculation (Step 3)

- Filing date target: 2026-07-15 (mailing date)
- Earliest valid effective date: 2026-07-15 − 75 days = 2026-05-01
- Latest valid effective date: 2026-07-15 + 12 months = 2027-07-15
- Desired effective date: 2026-08-01 → falls within the 75-day-back / 12-month-forward window: ✓

No Part II late-relief needed.

## 60-month rule check (Step 4)

- Line 2a: Has the entity filed an entity classification election within the last 60 months? **No** (no prior election)
- Line 2b: N/A
- Rule does not block: ✓

## §301.7701-3(g) deemed-transaction analysis (Step 11 preview)

The conversion from disregarded entity to association is treated under §301.7701-3(g)(1)(iv) as if Eli contributes the LLC's assets and liabilities to a newly-formed corporation in exchange for stock.

Marlowe Labs' balance sheet on 2026-08-01 (per Eli's books):

| Asset | Tax basis | FMV |
|-------|-----------|-----|
| Cash and bank accounts | $145,000 | $145,000 |
| Software / IP (developed pre-conversion) | $0 | ~$2.5M (per term sheet implied valuation) |
| Equipment | $18,000 | $18,000 |
| Liabilities | ($12,000) | ($12,000) |
| **Net** | **$151,000** | **$2,651,000** |

§351 analysis: Eli is the sole transferor; he receives 100% of the stock immediately after the deemed contribution. Control test (≥80% per §368(c)) is satisfied. §351 applies — no gain recognized on the contribution.

Basis consequences:

- **Eli's basis in stock** (substituted basis under §358): $151,000 (cash $145K + equipment $18K - liabilities $12K)
- **Corporation's basis in assets** (carryover under §362): tax basis carryover (cash $145K, IP $0, equipment $18K)
- **§357(c)** liabilities-in-excess-of-basis rule: liabilities $12K < basis $163K → no §357(c) gain triggered ✓

§1202 QSBS analysis:

- **Qualified small business**: §1202(d)(1) requires aggregate gross assets ≤$50M at all times before issuance and immediately after. Marlowe Labs' $2.65M is well under — qualifies.
- **Stock issuance after election effective date**: §1202 stock holding period starts on the date stock is issued in exchange for cash, services, or property. Stock deemed issued on 2026-08-01 (effective date of election). Eli must hold ≥5 years from 2026-08-01 → eligible for exclusion no earlier than 2031-08-01.
- **Issuance "for property" or "to provide services"**: The §301.7701-3(g) deemed contribution is treated as a §351 exchange; the resulting stock is treated as issued "for property". §1202(c)(1)(B) qualifies. ✓
- **Active business requirement**: Marlowe Labs must be a "qualified trade or business" under §1202(e)(3). Software / IP development is a qualified trade. ✓

CPA recommendation: yes, before mailing. Specific items to confirm:

- §351 control after the priced round: post-money equity tables. If post-round investors take >20%, Eli may not satisfy §368(c) control "immediately after" the deemed transaction unless documented properly. (Note: §1202 stock held by Eli is separately tested from the priced-round stock.)
- §1202 active-business test ongoing — at least 80% of assets must be used in qualified trade.
- Annual valuation tracking to ensure the $50M aggregate gross assets cap isn't breached.

## The completed Form 8832 draft

```markdown
# Form 8832 — DRAFT for Marlowe Labs LLC

## Filing summary
- Entity name: Marlowe Labs LLC
- EIN: 99-1234567
- Election type: Initial classification (Box 1(a))
- Current classification: Default disregarded
- Elected classification: Association (C-corporation)
- Effective date: 08/01/2026
- Filing channel: USPS Certified Mail to Kansas City service center
  (Delaware → Kansas City, MO 64999)
- Late relief requested: No

## Header
Name of eligible entity: Marlowe Labs LLC
EIN: 99-1234567
Address: 1209 Orange Street, Wilmington, DE 19801
Address change: ☐ (not checked — same as prior IRS records)

## Part I — Election Information
1. Type of election:                      ☒ (a) Initial classification
2a. Prior election within last 60 months: ☐ Yes  ☒ No
2b. Was prior election the first?         (skipped — Line 2a = No)
3. More than one owner:                   ☐ Yes  ☒ No
4. (Single individual owner)
   Name: Eli Marlowe
   ID number: ***-**-**** (SSN, redacted in this draft)
5. (Parent corporation)                   N/A
6. Type of entity:
   ☒ (a) Domestic eligible — elect association (C-corp)
   ☐ (b) Domestic eligible — elect partnership
   ☐ (c) Domestic eligible — elect disregarded
   ☐ (d) Foreign eligible — elect association
   ☐ (e) Foreign eligible — elect partnership
   ☐ (f) Foreign eligible — elect disregarded
7. (If foreign) Country of organization:  N/A (domestic)
8. Election effective date:               08/01/2026
9. Contact person: Eli Marlowe
   Phone: 415-555-0142
10. ☐ (Not checked — no §301.9100 attached statement)
11. Consent Statement and Signatures
    [Eli Marlowe, sole member, signs here]
    [Print name: Eli Marlowe]
    [Title: Sole Member]
    [Date: 07/14/2026]

## Part II — Late Election Relief
N/A (effective date within 75-day window)

## Required attachments
- [x] Sole member signature (Line 11) — collected 07/14/2026
- [ ] Part II — not applicable
- [ ] Officer/manager authority documentation — not applicable (sole member signs)

## Validation summary
- Eligibility: pass (domestic SMLLC, no per-se issue, no 60-month block)
- Effective-date window: pass (08/01/2026 within 05/01/2026 to 07/15/2027)
- 60-month rule: not applicable (initial classification, no prior election)
- Consents: complete (sole member)
- Sanity warnings:
  - Box 6(a) C-corp election triggers §301.7701-3(g) deemed contribution
  - $2.5M IP appreciation requires §351 / §358 / §362 review by CPA
  - QSBS holding period clock starts 08/01/2026 (5-year minimum to 08/01/2031)
  - State conformity check: Delaware franchise tax kicks in for C-corp
    (minimum $175 + capital-stock or assumed-par-value calc)

## Filing instructions
Mail to:
  Department of the Treasury
  Internal Revenue Service Center
  Kansas City, MO 64999

Method: USPS Certified Mail with Return Receipt
Postmark deadline: 07/15/2026 (target; any date such that 08/01/2026 effective
                    date is within 75-day window — i.e., postmark by ~10/15/2026
                    at latest)

Expected IRS acknowledgment: 60 days (CP277 acceptance letter)

## Next steps after IRS acceptance
- File Form 1120 for Marlowe Labs Inc. for the short period 08/01/2026–12/31/2026
- File final Schedule C on Eli's 1040 for the period 01/01/2026–07/31/2026
- Update payroll: Eli must transition from owner-draws to W-2 salary post-08/01
- Coordinate priced-round closing with §351 analysis to maintain control test
- File Delaware annual franchise tax return for 2026 (LLC franchise tax for
  pre-conversion period, corp franchise tax for post-conversion period)
- Track aggregate gross assets quarterly to maintain §1202(d) eligibility

## Sources cited in this draft
- IRS Form 8832 (Rev. December 2013)
- 26 CFR §301.7701-3(a) (eligible entity definition)
- 26 CFR §301.7701-3(c)(1)(i)–(iii) (election mechanics, 75-day window)
- 26 CFR §301.7701-3(g)(1)(iv) (deemed contribution on disregarded → association)
- IRC §351 (transfer to corporation in exchange for stock)
- IRC §358 (basis to transferor)
- IRC §362 (basis to corporation)
- IRC §1202 (QSBS exclusion)
- IRC §1202(d) (qualified small business definition)
- IRC §1202(e) (qualified trade or business)
- IRC §1202(c)(1)(B) (issuance for property qualifies)
```

## Why each non-obvious choice

**Why Box 1(a) "Initial classification" rather than 1(b) "Change in current classification"?** Marlowe Labs has only operated under default disregarded classification — no prior Form 8832 has been filed. The first-ever election is "initial classification" per the IRS instructions, even though the entity is two years old and was previously taxed as Schedule C. Default classification is not an "election" for purposes of Line 1.

**Why effective date 2026-08-01 specifically, not the formation date?** Eli wants the §1202 holding-period clock to start as early as possible without retroactivity headaches. 2026-08-01 is two months before the priced-round close (2026-09-30), which gives clean attribution between pre-conversion software development on Schedule C and post-conversion equity issuance to investors. Going earlier would require Part II late relief and a reasonable-cause statement (Eli has none — he's been operating consciously as a disregarded entity).

**Why not file Form 2553 also (S-corp election)?** Eli is raising venture capital. S-corp eligibility caps at 100 shareholders, requires all to be US residents/citizens, and prohibits multiple classes of stock — incompatible with priced-round preferred stock. C-corp is the right vehicle. Additionally, §1202 QSBS treatment requires C-corporation issuance — S-corp stock does not qualify.

**Why mail to Kansas City instead of Ogden?** Delaware is in the eastern routing per the Form 8832 "Where to File" table. Ogden handles western states.

**Why does the 60-month rule not apply here?** This is the first Form 8832 ever filed for the entity. The 60-month rule blocks re-elections within 60 months of a prior 8832 election. There is no prior election — only default classification — so the rule has nothing to lock against.

**What if the priced round falls through and Eli wants to revert to disregarded?** The 60-month rule will block until 2031-08-01. Eli would need to either (a) wait, (b) document a >50% ownership change (hard with sole-member entity unless he sells equity to someone else), or (c) live with C-corp classification and consider an S-corp overlay election if QSBS is no longer the strategy. Once Form 8832 is filed, the door closes for 5 years.

**What should Eli's CPA verify before mailing?**

1. §351 control test post-conversion: confirm Eli holds ≥80% of voting + ≥80% of each class of stock immediately after the deemed contribution
2. §357(c) liabilities-vs-basis: confirmed $12K < $163K, no gain triggered
3. Working capital adequacy: ensure the deemed corporation has sufficient cash to operate post-conversion without owner contributions that could disrupt §351 treatment
4. Delaware franchise tax: corp franchise tax minimum $175 + assumed-par-value calculation; LLC franchise tax was $300 flat — confirm the timing of the changeover
5. §1202 active-business compliance plan for years 1-5: tracking system for aggregate gross assets and use-of-assets tests
