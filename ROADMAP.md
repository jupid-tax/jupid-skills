# Roadmap

Skills we plan to add, prioritized by search-volume + audience-fit research from `jupid-tax/OS`. The full ranked list of 192 candidate IRS forms is at [content-outputs/irs-forms-top50.md](https://github.com/jupid-tax/OS/blob/main/content-outputs/irs-forms-top50.md) in the parent repo.

## Top 20 next skills

Each line: `form` — `audience` — short rationale.

| # | Form | Audience | Status | Notes |
|---|------|----------|--------|-------|
| 1 | Schedule C (Form 1040) | Sole prop / freelancer / SMLLC | ✓ Shipped | The reference skill. |
| 2 | Schedule SE (Form 1040) | Self-employment tax | Planned | 92.35% × profit × 15.3%. Tightly couples with Schedule C. |
| 3 | Form 1040 | All individuals | Planned | The umbrella return; pulls from many skills. |
| 4 | W-9 | Independent contractors | Planned | High volume, low complexity — quick win. |
| 5 | Schedule 1 (Form 1040) | Adjustments + business income | Planned | Where Schedule C profit lands. |
| 6 | Form 8829 | Home office (regular method) | Planned | Pairs with Schedule C Line 30. |
| 7 | Form 4562 | Depreciation + Section 179 | Planned | Pairs with Schedule C Line 13. |
| 8 | Form 1099-NEC (filing as payer) | Anyone who paid contractors $600+ | Planned | Distinct from receiving a 1099. |
| 9 | Form 1099-K (interpreting) | Marketplace + payment processor sellers | Planned | Especially after the threshold change. |
| 10 | Form 1040-ES | Quarterly estimated tax | Planned | Self-employed with no W-2 withholding. |
| 11 | Form 2553 | LLC / sole prop electing S-corp status | Planned | Procedural with timing rules. |
| 12 | Form 8995 / 8995-A | QBI deduction | Planned | High value, complex eligibility. |
| 13 | Form 8889 | HSA contributions and distributions | Planned | Highest-score form by audience-fit/SV. |
| 14 | Form 941 | Quarterly payroll tax | Planned | Only if you have W-2 employees. |
| 15 | Form 940 | Annual FUTA | Planned | Pairs with 941. |
| 16 | Form 8949 + Schedule D | Capital gains / crypto / stock sales | Planned | Heavy demand from 1099-B holders. |
| 17 | Schedule A | Itemized deductions | Planned | Decision logic vs. standard deduction. |
| 18 | Form 1065 + K-1 | Multi-member LLC / partnership | Planned | Most complex on this list. |
| 19 | Form 1120-S + K-1 | S-corporation | Planned | Pairs with 2553. |
| 20 | Form 4868 / 7004 | Extensions | Planned | Procedural, time-sensitive. |

## Process

A skill enters this list only after it passes a research gate:

1. **Demand check** — combined search volume (SpyFu + Ahrefs) ≥ 1,000/month for the bare form name, OR a clear bottleneck for the parent skill (e.g., Schedule SE is required to use Schedule C correctly even if its standalone SV were lower)
2. **Audience-fit check** — primary user is solo / freelance / single-member LLC / S-corp owner. Forms that mostly serve corporations or trusts go to a separate roadmap.
3. **Source availability** — official IRS form, instructions, and the most recent IRS publication on the topic must all be available and current.

## Status legend

- `✓ Shipped` — merged to `main`, has examples, has been reviewed against IRS sources at the date in `last_verified`
- `Planned` — committed; assigned to a maintainer
- `Drafting` — PR open, in active review
- `Backlog` — research done, no maintainer assigned yet
