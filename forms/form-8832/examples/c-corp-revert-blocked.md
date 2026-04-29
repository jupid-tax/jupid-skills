# Example: Reverting C-Corp Election Blocked by 60-Month Rule

A complete walkthrough showing how the 60-month limitation in 26 CFR §301.7701-3(c)(1)(iv) blocks an attempted reversal — and what the agent should produce instead of a filed Form 8832. This example is the canonical "we tried to undo a prior election" pattern.

The key lesson: the 60-month rule is unforgiving, and the right response is often **not to file**. The skill must surface the block before the user mails a form that will be rejected.

## The filer

- **Entity**: Lattice Goods LLC, a California multi-member LLC (3 members)
- **Members**: Aria Patel (50%), Jordan Reyes (30%), Marina Volkov (20%)
- **Formation date**: 2022-05-04
- **Tax year**: Calendar year
- **Prior election**: On **2024-01-01**, Lattice Goods filed Form 8832 electing C-corporation classification (Box 6(a)). This was a "change in current classification" — the LLC's default was partnership, and the filing changed to C-corp. Effective 2024-01-01.
- **Current classification**: C-corporation since 2024-01-01
- **Reason for desired reversion**: The C-corp election was driven by a planned strategic-investor round that fell through in late 2024. The members have been operating as a C-corp for two tax years (2024 and 2025), filing Form 1120, and have accumulated $180K of after-tax retained earnings inside the corporation. They now want to revert to partnership classification (Box 6(b)) effective **2026-01-01** to:
  - Eliminate the double tax layer (corporate 21% + dividend 15-20% on distributions)
  - Pass the next round of profits through to members on a current basis
  - Simplify accounting (Form 1065 K-1s vs. Form 1120 + W-2 + 1099-DIV)
- **Desired effective date**: 2026-01-01

## 60-month rule check (Step 4 — this is the blocker)

- Prior Form 8832 effective date: **2024-01-01**
- Earliest valid new effective date under the 60-month rule: 2024-01-01 + 60 months = **2029-01-01**
- Desired new effective date: 2026-01-01
- **2026-01-01 is 36 months after the prior effective date — well within the 60-month lock**

The prior election (2024-01-01) was a "change in current classification" — Box 1(b) was checked, Line 2b was N/A (it was the entity's first election, but the entity was not "newly-formed" at the time of the election; it had operated as a default partnership for 20 months before electing).

Wait — **was Line 2b "Yes" on the 2024 filing?** This is worth checking. §301.7701-3(c)(1)(iv) excludes "an election made by an existing entity to change its classification" — meaning the rule only applies when there was a *change*. An initial classification of a newly-formed entity does NOT trigger the 60-month lock. But Lattice Goods was 20 months old when it elected — it was an "existing entity" changing from default partnership to C-corp. That's a change. The 60-month rule applies.

If the 2024 filing was incorrectly marked as Line 2b "Yes" (newly-formed) when it should have been "No" (existing entity changing), the rule still applies based on the actual facts — not the form's representation. The IRS looks at substance.

## Exception analysis

### Exception 1 — More than 50% ownership change

Has more than 50% of the ownership interest changed since 2024-01-01?

| Member | 2024-01-01 stake | 2026-04-29 stake |
|--------|-------------------|--------------------|
| Aria Patel | 50% | 50% |
| Jordan Reyes | 30% | 30% |
| Marina Volkov | 20% | 20% |

No ownership changes. The 50% exception does not apply.

### Exception 2 — Initial classification by newly-formed entity

The 2024 election was not made on the date of formation — it was made 20 months after formation. Line 2b would correctly be marked "No" on a fresh Form 8832. Initial-classification exception does not apply.

**No exception is available. The 60-month rule blocks.**

## What the agent should produce

Instead of a filed Form 8832, the agent produces a **block-and-explain output**: the analysis above, the date the entity becomes eligible to re-elect, and a list of intermediate options. The Form 8832 draft is NOT generated — generating a draft would imply readiness to file, which is not the case.

```markdown
# Form 8832 — BLOCKED for Lattice Goods LLC

## Status: NOT FILED

Reason: 26 CFR §301.7701-3(c)(1)(iv) — 60-month limitation

## Analysis

### Prior election

Lattice Goods LLC filed Form 8832 effective 01/01/2024 electing
classification as an association (C-corporation). The filing was a
"Change in current classification" (Line 1(b)) because the entity
was an existing multi-member LLC defaulted to partnership prior to
the election.

### Requested new election

The members request to revert to partnership classification (Line 6(b))
effective 01/01/2026.

### 60-month limitation

26 CFR §301.7701-3(c)(1)(iv): "If an eligible entity makes an election
under paragraph (c)(1)(i) of this section to change its classification
(other than an election made by an existing entity to change its
classification as of the effective date of this section), the entity
cannot change its classification by election again during the sixty
months succeeding the effective date of the election."

The 2024 election locks Lattice Goods until 01/01/2029.

### Exceptions considered

1. **>50% ownership change since 01/01/2024**: NO. Ownership remained
   stable (50% / 30% / 20%) throughout the lock period. The 50% exception
   does not apply.

2. **Prior election was an initial classification by a newly-formed entity
   (Line 2b "Yes")**: NO. The 2024 election occurred 20 months after
   formation and was a "change" from the default partnership classification.
   The newly-formed-entity exception does not apply.

No exception applies. The election is blocked.

## Earliest valid new effective date

**01/01/2029** (5 years after the 2024-01-01 effective date)

Form 8832 may be pre-filed up to 12 months in advance per 26 CFR
§301.7701-3(c)(1)(iii). The members can submit a new Form 8832 as early
as **01/01/2028** with effective date 01/01/2029.

## Options for the members

### Option A — Wait until 01/01/2029 (cleanest)

Continue operating as a C-corporation for 2026, 2027, and 2028. File
Form 8832 in early 2028 with effective date 01/01/2029. Distribute
accumulated earnings as dividends or reinvest them. Plan the deemed-
liquidation tax consequences of the future reversion in advance with
a CPA.

Cost: 3 more years of double taxation on profits not retained in the
corporation. Estimated tax cost depends on annual profits and
distribution policy.

### Option B — File Form 2553 to elect S-corporation status

The 60-month rule under §301.7701-3 is an **entity classification** rule.
Once classified as an association (C-corp), the entity is a corporation.
The S-corp election is a separate procedure under IRC §1362 with its
own eligibility test — not blocked by §301.7701-3(c)(1)(iv).

Eligibility check for Lattice Goods:
- ☑ Domestic entity classified as a corporation
- ☑ ≤100 shareholders
- ☑ All shareholders are individuals who are US citizens or residents
  (verify: are all 3 members US persons?)
- ☑ One class of stock (verify: does the operating agreement provide
  for any preferred / non-voting / liquidation-preference distinctions?)
- ☑ All shareholders consent

If eligibility is satisfied, file Form 2553 with effective date 01/01/2026.
Deadline: 03/15/2026 (75th day after the start of the desired tax year).
Late relief available under Rev. Proc. 2013-30 if missed.

Pros:
- Eliminates double tax on operating profits
- Members report income via K-1 (similar simplicity to partnership)
- Available immediately (not blocked by 60-month rule)

Cons:
- §1374 built-in gains tax: any gain on assets held at the time of S
  election is subject to a 21% corporate-level tax if recognized within
  5 years. Lattice Goods' assets must be valued at 01/01/2026 to track
  built-in gain.
- §1375 passive investment income limit: if earnings & profits exist
  from the C-corp years (likely yes — $180K accumulated) and passive
  investment income exceeds 25% of gross receipts for 3 consecutive
  years, the S election can be terminated.
- Distribution of pre-S-election E&P is taxed as a dividend; only
  post-S-election Accumulated Adjustment Account (AAA) flows tax-free.
- Loss of certain corporate-level deductions (e.g., §1202 QSBS not
  available for S-corp shares).

Recommendation: this is often the right move for an entity caught
by the 60-month rule. Consult a CPA to model the §1374 BIG tax
exposure on the entity's specific asset mix.

### Option C — Document a >50% ownership change and re-file

If the members are willing to restructure ownership such that more than
50% of the interests have genuinely changed hands since 01/01/2024,
the IRS may waive the 60-month rule. This would require:
- An actual transfer of >50% of capital and profits interests to a new
  member or members
- Documentation (purchase agreement, capital account adjustment, IRS
  Schedule K-1 showing the new ownership)
- Attached statement on Form 8832 explaining the change and citing
  §301.7701-3(c)(1)(iv) waiver

This option is rarely worth pursuing as a workaround — the IRS may
challenge the ownership change as a sham if it appears engineered solely
to escape the 60-month rule.

### Option D — Live with the C-corp classification

If retained earnings are productive (re-investing in growth, paying
modest dividends, planning toward an exit), C-corp is not a bad outcome.
The 21% federal corporate rate is competitive. The members can take W-2
salaries (deductible by corp) plus modest dividends. Full reversion may
not be the right answer — Option B (S-corp) often is.

## Filing instructions

**DO NOT MAIL FORM 8832 AT THIS TIME.**

The IRS will reject (CP278 — 60-month limitation). Mailing the form:
- Wastes filing effort
- Generates a rejection notice that complicates the entity's IRS file
- Does not preserve the desired effective date (rejection means no
  election; the entity stays C-corp)

Instead:
- Decide between Option A, B, C, or D above
- If Option A: tickle a reminder for 01/01/2028 to begin the new Form
  8832 process
- If Option B: prepare Form 2553 with deadline 03/15/2026
- If Option C: engage counsel; this is not a self-serve path
- If Option D: no action needed

## Sources cited in this analysis

- 26 CFR §301.7701-3(c)(1)(iv) — 60-month limitation
- 26 CFR §301.7701-3(c)(1)(iii) — pre-filing window (12 months in advance)
- IRC §1361 — S-corporation eligibility
- IRC §1362 — S-corporation election procedures
- IRC §1374 — built-in gains tax on former C-corp converting to S-corp
- IRC §1375 — passive investment income tax for S-corp with C-corp E&P
- Rev. Proc. 2013-30 — late S-corp election relief
- IRS Form 2553 (S-corp election)
```

## Why each non-obvious choice

**Why not even draft a Form 8832 to mail?** The 60-month rule is a substantive bar — not a procedural one. Mailing the form will result in CP278 rejection, which complicates the entity's IRS file with no benefit. The right output is a block-and-explain memorandum that the user can review and act on.

**Why is the S-corp election (Form 2553) not blocked?** The 60-month rule in §301.7701-3 governs **entity classification** under the check-the-box regulations. S-corp status is not an entity classification — it's a Subchapter S election under IRC §1362 layered on top of corporate classification. Two separate rules. The corporation can be locked-in classified as an association *and* still elect Subchapter S treatment.

**Why does the 60-month rule still apply if the original Form 8832 was incorrectly marked Line 2b "Yes"?** The IRS looks at substance over form. If the entity was 20 months old at the time of the prior election, it was an "existing entity" — not a "newly-formed entity". Marking 2b "Yes" on the prior form does not change the underlying facts; the 60-month clock still ticks.

**Why is Option A ("wait") presented as cleanest?** Cleanest = no IRS scrutiny, no §1374 BIG tracking, no ownership engineering. The cost is real (3 more years of C-corp double taxation), but for an entity with predictable retained earnings policy and an eventual exit horizon, waiting is often the right answer.

**Why is Option B (S-corp) usually the practical recommendation?** S-corp avoids the lock-in entirely while delivering the pass-through outcome the members want. The §1374 BIG tax is a real cost but it's bounded (only 21% on built-in gain, only on assets sold within 5 years). The §1375 passive income trap is only relevant if the entity has significant passive investment income — for an operating business it usually isn't. S-corp gets most of the benefit of partnership reversion without waiting until 2029.

**What should the agent do if the user insists on filing Form 8832 anyway?** Refuse to mail. Surface the rejection certainty. Document the user's decision. If the user wants to file unilaterally despite the warning, the user can mail the form themselves — but the agent does not assist in a known-wrong filing. This is a judgment-heavy boundary in the skill: a skill that helps the user file a doomed form is worse than a skill that blocks.
