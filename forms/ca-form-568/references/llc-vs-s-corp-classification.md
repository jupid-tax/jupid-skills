# LLC vs. S-Corporation Classification (Form 568 vs. Form 100S)

One of the most common confusions for California LLC owners: when does a California LLC file Form 568, and when does it file Form 100S? The answer turns on **federal tax classification** AND **California's election rules**.

---

## The four federal classifications for an LLC

1. **Disregarded entity** (default for SMLLC) — federal tax owner is the single member; LLC has no separate federal tax existence
2. **Partnership** (default for multi-member LLC) — files federal Form 1065
3. **C-corporation** (electable via federal Form 8832) — files federal Form 1120
4. **S-corporation** (electable via federal Form 2553, after first electing corporation classification on Form 8832 or by default for single-member LLC owner) — files federal Form 1120-S

---

## California treatment by federal classification

| Federal | Default California treatment | California return |
|---------|------------------------------|-------------------|
| Disregarded entity | Disregarded for California (with exceptions) | **Form 568** + owner reports on 540 |
| Partnership | Partnership for California | **Form 568** |
| C-corporation | C-corporation for California | **Form 100** |
| S-corporation | **California must accept federal S-corp election if Form 2553 filed federally** (R&TC §23800(a)) | **Form 100S** |

Critical rule: California **automatically conforms** to a federal S-corp election. The LLC does not need to file a separate California S-corp election form. Once Form 2553 is filed federally, the LLC is an S-corp for California too.

---

## When an LLC files Form 568 (this skill applies)

- **SMLLC, disregarded entity** (no federal Form 8832 or 2553 filed) → Form 568
- **Multi-member LLC, partnership classification** (default for multi-member; no federal Form 8832 or 2553) → Form 568

In both cases:
- $800 annual tax (R&TC §17941)
- LLC fee tier (R&TC §17942)
- Form 568 due 15th day of 3rd month (multi-member) or 4th month (SMLLC) after year-end
- Federal classification reported on Side 1 box H

---

## When an LLC files Form 100S (this skill does NOT apply)

- LLC filed federal Form 2553 → automatically an S-corp for California → **Form 100S**

In this case, the LLC owes:
- **California S-corp tax** (greater of 1.5% of net income OR $800 minimum franchise tax — R&TC §23802 / §23153)
- **NO** §17942 LLC fee (the fee is for partnership-classified LLCs, not S-corps)
- Form 100S due 15th day of 3rd month after year-end (calendar year = March 15)

This is fundamentally different from Form 568. If the user filed federal Form 2553, do not produce Form 568 — redirect to a Form 100S skill (forthcoming).

---

## When an LLC files Form 100 (also outside this skill)

- LLC filed federal Form 8832 to elect C-corp → **Form 100**

Owes:
- 8.84% California corporate tax on net income (or $800 minimum franchise tax, whichever greater)
- No §17942 LLC fee
- Form 100 due 15th day of 4th month after year-end

---

## How to figure out the user's classification

Ask the user, in order:

1. **"Did you file federal Form 8832 to elect to be taxed as a corporation?"**
   - Yes → ask if they then filed Form 2553. If yes, S-corp (Form 100S). If no, C-corp (Form 100).
   - No → continue.
2. **"Did you file federal Form 2553 to elect S-corp status?"** (LLCs can file Form 2553 directly without Form 8832, per IRS revenue procedure 2013-30)
   - Yes → S-corp (Form 100S).
   - No → continue.
3. **"How many members does the LLC have?"**
   - 1 → SMLLC, disregarded → Form 568 (this skill applies)
   - 2+ → multi-member LLC, partnership default → Form 568 (this skill applies)

If the user is unsure whether they filed Form 2553 or 8832, ask them to check their records or pull their federal Form 1120-S filing history. The IRS sends a CP261 confirmation letter when accepting Form 2553; that letter is the definitive proof.

---

## Why owners convert LLC → S-corp election

Common motivations:

1. **Save self-employment tax** — federal S-corp owners take a "reasonable salary" + distributions; only salary is subject to SE tax (15.3%). For high-income LLCs ($100K+ net income), this can save thousands in SE tax.
2. **Avoid the §17942 LLC fee** — California S-corps have a 1.5% net income tax + $800 minimum, but no tiered fee. For very high-income LLCs (>$5M total income), the $11,790 LLC fee disappears in favor of 1.5% × net income (which may be more or less depending on profit margin).

But the conversion has costs:
- Reasonable salary requirement → must run payroll, file Form 941, pay employer-side FICA
- More complex bookkeeping
- Loss of QBI deduction flexibility (sometimes)

**Out of scope**: this skill does not advise on whether to elect S-corp. If the user asks, redirect to a CPA. The decision depends on income level, profit margin, and operational complexity — case-specific.

---

## Edge case: LLC that elected federally but not yet at California level

Historically, California required a separate election to recognize federal S-corp status. **This is no longer true** — under current R&TC §23800(a), California automatically conforms. So an LLC that filed federal Form 2553 is automatically an S-corp for California, even without filing any California-specific form.

**However**: the LLC must still notify the California SOS that its tax classification has changed — failing this can create a mismatch where SOS still thinks the entity is an LLC but FTB taxes it as an S-corp. This isn't fatal but causes friction at audit.

If user filed Form 2553 federally and is now confused which California return to file, the answer is **Form 100S, not Form 568**.

---

## Citation summary

- IRC §7701 / Reg §301.7701-3 — Federal entity classification election
- IRC §1361-§1379 — S-corporation rules
- IRS Form 8832 — Entity Classification Election
- IRS Form 2553 — Election by a Small Business Corporation
- Rev. Proc. 2013-30 — LLCs filing Form 2553 directly without Form 8832
- R&TC §23800(a) — California automatic conformity to federal S-election
- R&TC §17941 — California $800 annual LLC tax
- R&TC §17942 — California LLC fee
- R&TC §23802 — California S-corp tax (1.5% rate, $800 minimum)
- R&TC §23153 — California minimum franchise tax ($800)

For the agent: the deciding question is "did the LLC file federal Form 2553 (or Form 8832 + 2553)?". Anything else and Form 568 is the right return.
