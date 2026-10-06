# LLC vs. S-Corporation Classification (Form 568 vs. Form 100S)

One of the most common confusions for California LLC owners: when does a California LLC file Form 568, and when does it file Form 100S? The answer turns on **federal tax classification**. California generally treats federal check-the-box elections as California elections and allows no separate state election (2025 Form 568 Booklet, General Information S).

---

## The four federal classifications for an LLC

1. **Disregarded entity** (default for SMLLC) — federal tax owner is the single member; LLC has no separate federal tax existence
2. **Partnership** (default for multi-member LLC) — files federal Form 1065
3. **C-corporation** (electable via federal Form 8832) — files federal Form 1120
4. **S-corporation** (electable via federal Form 2553; an eligible entity that timely elects S status is deemed to have elected corporate classification, Treas. Reg. §301.7701-3(c)(1)(v)(C), so a separate Form 8832 is not needed) — files federal Form 1120-S

---

## California treatment by federal classification

| Federal | Default California treatment | California return |
|---------|------------------------------|-------------------|
| Disregarded entity | Disregarded for California (exception: an SMLLC treated as a corporation for California before 1997 that never changed) | **Form 568** + owner reports on the owner's own return |
| Partnership | Partnership for California | **Form 568** |
| C-corporation | C-corporation for California | **Form 100** |
| S-corporation | A corporation with a valid federal S election is an S corporation for California (R&TC §23801(a)) | **Form 100S** |

Critical rule: California **automatically follows** a federal S election. The LLC does not file a separate California S election. Once the federal Form 2553 election is effective, the LLC is an S corporation for California too, and LLCs classified as S corporations file Form 100S (2025 booklet, General Information A).

---

## When an LLC files Form 568 (this skill applies)

- **SMLLC, disregarded entity** (no federal Form 8832 or 2553 filed) → Form 568
- **Multi-member LLC, partnership classification** (default for multi-member; no federal Form 8832 or 2553) → Form 568

In both cases:
- $800 annual tax (R&TC §17941)
- LLC fee tier (R&TC §17942)
- Form 568 due the 15th day of the 3rd month after year-end (partnership-classified, and SMLLCs owned by pass-through entities) or the 15th day of the 4th month after the close of the owner's taxable year (other SMLLCs) (2025 booklet, General Information E)
- Disregarded status reported in Question U(1); a copy of any federal Form 8832 is attached for the year the election takes effect (2025 booklet, General Information S)

---

## When an LLC files Form 100S (this skill does NOT apply)

- LLC filed federal Form 2553 → automatically an S-corp for California → **Form 100S**

In this case, the LLC owes:
- **California S-corp tax** (greater of 1.5% of net income OR $800 minimum franchise tax — R&TC §23802 / §23153)
- **NO** §17942 LLC fee (the fee is for partnership-classified LLCs, not S-corps)
- Form 100S due 15th day of 3rd month after year-end (calendar year = March 15)

This is fundamentally different from Form 568. If the user filed federal Form 2553, do not produce Form 568. This skill does not draft Form 100S; the federal side is [`../../form-1120-s/SKILL.md`](../../form-1120-s/SKILL.md).

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
2. **"Did you file federal Form 2553 to elect S-corp status?"** (LLCs can file Form 2553 directly without Form 8832, Treas. Reg. §301.7701-3(c)(1)(v)(C))
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

California does not require a separate election to recognize federal S status: under R&TC §23801(a), a corporation with a valid federal S election in effect is an S corporation for California, and under §23801(e) a federal termination terminates the California status too. So an LLC that filed federal Form 2553 is automatically an S corporation for California, even without filing any California-specific form.

If the LLC also filed federal Form 8832, attach a copy to the California return for the year the election takes effect (2025 booklet, General Information S). The LLC remains an LLC with the Secretary of State; the tax classification change is reported to the FTB through the return it files, not through an SOS form.

If user filed Form 2553 federally and is now confused which California return to file, the answer is **Form 100S, not Form 568**.

---

## Citation summary

- IRC §7701 / Reg §301.7701-3 — Federal entity classification election
- IRC §1361-§1379 — S-corporation rules
- IRS Form 8832 — Entity Classification Election
- IRS Form 2553 — Election by a Small Business Corporation
- Treas. Reg. §301.7701-3(c)(1)(v)(C) — a timely S election by an eligible entity is a deemed election to be an association
- Rev. Proc. 2013-30 — relief for late S and entity-classification elections
- R&TC §23801(a), (e) — federal S election and termination apply for California
- 2025 Form 568 Booklet, General Information A and S (check-the-box; no separate California election)
- R&TC §17941 — California $800 annual LLC tax
- R&TC §17942 — California LLC fee
- R&TC §23802 — California S-corp tax (1.5% rate, $800 minimum)
- R&TC §23153 — California minimum franchise tax ($800)

For the agent: the deciding question is "did the LLC file federal Form 2553 (or Form 8832 + 2553)?". Anything else and Form 568 is the right return.
