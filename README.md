# Jupid Skills

Open-source agent skills for accounting, taxes, and finance — used inside [Jupid](https://jupid.com), our AI accountant for solopreneurs and small businesses.

Each skill is a self-contained operating manual that teaches an AI agent how to handle one form, one calculation, or one workflow. Skills are written for [Claude Code](https://claude.com/claude-code), the [Anthropic Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), and any other agent runtime that loads markdown skill packages.

## 54 skills available

The repository currently contains:

- **50 form skills** covering individual, business, payroll, information-return, international, and state filings;
- **4 workflow skills** for tax research, spreadsheet logic, document cleanup, and LinkedIn analytics.

Every form skill includes a `SKILL.md`, filing guidance, form-specific references, and worked examples.

## Repository layout

```
jupid-skills/
├── forms/           # 50 IRS and state form skills
│   ├── form-1040/
│   ├── form-1099-nec/
│   ├── schedule-c/
│   └── ...
└── workflows/       # 4 multi-step accounting and research workflows
```

## Form skills (50)

Browse the complete [`forms/` directory](./forms/) or open a skill directly below.

| Skill | Form or schedule |
|-------|------------------|
| [ca-form-568](./forms/ca-form-568/) | California Form 568 — Limited Liability Company Return of Income |
| [form-1040](./forms/form-1040/) | Form 1040 — U.S. Individual Income Tax Return |
| [form-1040-es](./forms/form-1040-es/) | Form 1040-ES — Estimated Tax for Individuals |
| [form-1095-a](./forms/form-1095-a/) | Form 1095-A — Health Insurance Marketplace Statement |
| [form-1099-c](./forms/form-1099-c/) | Form 1099-C — Cancellation of Debt |
| [form-1099-k](./forms/form-1099-k/) | Form 1099-K — Payment Card and Third Party Network Transactions |
| [form-1099-misc](./forms/form-1099-misc/) | Form 1099-MISC — Miscellaneous Information |
| [form-1099-nec](./forms/form-1099-nec/) | Form 1099-NEC — Nonemployee Compensation |
| [form-1099-q](./forms/form-1099-q/) | Form 1099-Q — Qualified Education Program Distributions |
| [form-1099-sa](./forms/form-1099-sa/) | Form 1099-SA — HSA/MSA Distributions |
| [form-1116](./forms/form-1116/) | Form 1116 — Foreign Tax Credit |
| [form-2210](./forms/form-2210/) | Form 2210 — Underpayment of Estimated Tax by Individuals |
| [form-2290](./forms/form-2290/) | Form 2290 — Heavy Highway Vehicle Use Tax Return |
| [form-2553](./forms/form-2553/) | Form 2553 — Election by a Small Business Corporation |
| [form-2555](./forms/form-2555/) | Form 2555 — Foreign Earned Income |
| [form-3115](./forms/form-3115/) | Form 3115 — Application for Change in Accounting Method |
| [form-3520](./forms/form-3520/) | Form 3520 — Foreign Trusts and Foreign Gifts |
| [form-4506-t](./forms/form-4506-t/) | Form 4506-T — Request for Transcript of Tax Return |
| [form-4562](./forms/form-4562/) | Form 4562 — Depreciation and Amortization |
| [form-4684](./forms/form-4684/) | Form 4684 — Casualties and Thefts |
| [form-4797](./forms/form-4797/) | Form 4797 — Sales of Business Property |
| [form-5329](./forms/form-5329/) | Form 5329 — Additional Taxes on Qualified Plans |
| [form-5472](./forms/form-5472/) | Form 5472 — Foreign-Owned U.S. Corporation Information Return |
| [form-5498](./forms/form-5498/) | Form 5498 — IRA Contribution Information |
| [form-5498-sa](./forms/form-5498-sa/) | Form 5498-SA — HSA/MSA Information |
| [form-5500](./forms/form-5500/) | Form 5500 — Employee Benefit Plan Annual Return |
| [form-720](./forms/form-720/) | Form 720 — Quarterly Federal Excise Tax Return |
| [form-8300](./forms/form-8300/) | Form 8300 — Cash Payments Over $10,000 |
| [form-8824](./forms/form-8824/) | Form 8824 — Like-Kind Exchanges |
| [form-8832](./forms/form-8832/) | Form 8832 — Entity Classification Election |
| [form-8889](./forms/form-8889/) | Form 8889 — Health Savings Accounts |
| [form-8919](./forms/form-8919/) | Form 8919 — Uncollected Social Security and Medicare Tax |
| [form-8949](./forms/form-8949/) | Form 8949 — Sales and Other Dispositions of Capital Assets |
| [form-8959](./forms/form-8959/) | Form 8959 — Additional Medicare Tax |
| [form-8962](./forms/form-8962/) | Form 8962 — Premium Tax Credit |
| [form-8995](./forms/form-8995/) | Form 8995 — Qualified Business Income Deduction, Simplified |
| [form-8995-a](./forms/form-8995-a/) | Form 8995-A — Qualified Business Income Deduction |
| [form-941](./forms/form-941/) | Form 941 — Employer's Quarterly Federal Tax Return |
| [form-982](./forms/form-982/) | Form 982 — Discharge of Indebtedness Tax Attributes |
| [form-w-4r](./forms/form-w-4r/) | Form W-4R — Withholding on Nonperiodic Payments |
| [form-w4](./forms/form-w4/) | Form W-4 — Employee's Withholding Certificate |
| [form-w7](./forms/form-w7/) | Form W-7 — ITIN Application |
| [form-w9](./forms/form-w9/) | Form W-9 — Taxpayer Identification Number and Certification |
| [schedule-1](./forms/schedule-1/) | Schedule 1 — Additional Income and Adjustments to Income |
| [schedule-2](./forms/schedule-2/) | Schedule 2 — Additional Taxes |
| [schedule-8812](./forms/schedule-8812/) | Schedule 8812 — Credits for Qualifying Children and Dependents |
| [schedule-a](./forms/schedule-a/) | Schedule A — Itemized Deductions |
| [schedule-c](./forms/schedule-c/) | Schedule C — Profit or Loss From Business |
| [schedule-d](./forms/schedule-d/) | Schedule D — Capital Gains and Losses |
| [schedule-se](./forms/schedule-se/) | Schedule SE — Self-Employment Tax |

## Workflow skills (4)

| Skill | Topic |
|-------|-------|
| [workflows/irs-evidence-research](./workflows/irs-evidence-research/) | IRS-only, citation-gated tax research workflow |
| [workflows/linkedin-post-analytics-coach](./workflows/linkedin-post-analytics-coach/) | LinkedIn post analytics review and next-post coaching workflow |
| [workflows/spreadsheet-logic-builder](./workflows/spreadsheet-logic-builder/) | Deterministic spreadsheet logic, reconciliation, and automation workflow |
| [workflows/cleanup-documents](./workflows/cleanup-documents/) | Read a messy document folder, sort invoices/receipts/statements into folders, build an index |

## Using a skill

### Fastest path

Open Codex or Claude Code and paste:

```text
Use this skill from GitHub:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/irs-evidence-research

If you can tell whether this session is Codex or Claude Code, use the matching
runtime behavior. If you cannot tell, ask me whether I am using Codex or Claude
Code.

Research my tax question using official IRS sources only:
[write your question here]
```

For LinkedIn post analytics coaching, paste:

```text
Use this skill from GitHub:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/linkedin-post-analytics-coach

Analyze my LinkedIn post and analytics export. Tell me what worked, what did
not work, and what exact experiment I should run in the next post.
```

For accountant spreadsheet automation, paste:

```text
Use this skill from GitHub:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/spreadsheet-logic-builder

Help me build deterministic spreadsheet logic for this accounting workflow.
Ask for the missing rules first, then produce the rule spec, formulas/macro/script,
verification checks, and local run instructions.
```

For cleaning up a messy folder of documents, paste:

```text
Use this skill from GitHub:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/cleanup-documents

Clean up my documents folder: [path]. Propose a folder structure first and
confirm it with me before moving anything. At the end, ask me whether I want
a spreadsheet index of everything you filed.
```

For repeated use, install the folder locally using the platform-specific
instructions below. The GitHub link stays the same for both platforms.

### With Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r jupid-skills/forms/schedule-c ~/.claude/skills/
cp -r jupid-skills/workflows/irs-evidence-research ~/.claude/skills/
cp -r jupid-skills/workflows/linkedin-post-analytics-coach ~/.claude/skills/
cp -r jupid-skills/workflows/spreadsheet-logic-builder ~/.claude/skills/
cp -r jupid-skills/workflows/cleanup-documents ~/.claude/skills/
```

Then in any Claude Code session, ask the kind of question the skill is built for:

```
> Help me fill out Schedule C for my freelance business
> Use official IRS sources only to research whether this filing requirement applies
```

Claude will detect the trigger phrases declared in the skill's frontmatter and engage.

### With the Anthropic Agent SDK

Load the skill's `SKILL.md` into your system prompt; load reference and example files on demand based on what the user's situation needs.

```python
from anthropic import Anthropic
from pathlib import Path

skill = Path("jupid-skills/workflows/irs-evidence-research/SKILL.md").read_text()
references = {
    p.stem: p.read_text()
    for p in Path("jupid-skills/workflows/irs-evidence-research/references").glob("*.md")
}
```

### With Codex

Copy the skill folder into a Codex skill directory, or load the skill files in a
repo-level `AGENTS.md` workflow. For local installation:

```bash
mkdir -p ~/.codex/skills
cp -r jupid-skills/workflows/irs-evidence-research ~/.codex/skills/
cp -r jupid-skills/workflows/linkedin-post-analytics-coach ~/.codex/skills/
cp -r jupid-skills/workflows/spreadsheet-logic-builder ~/.codex/skills/
cp -r jupid-skills/workflows/cleanup-documents ~/.codex/skills/
```

Then ask Codex:

```
Use the irs-evidence-research skill. Research this question using official sources only: ...
Use the linkedin-post-analytics-coach skill. Analyze my LinkedIn post analytics export and recommend the next experiment.
Use the spreadsheet-logic-builder skill. Build deterministic spreadsheet logic for this reconciliation workflow.
Use the cleanup-documents skill. Organize the documents in [folder] — propose the folder structure first.
```

### With browser automation

Form skills include a `filing.md` reference that gives an agent step-by-step instructions to actually file the completed form via the browser — IRS Free File Fillable Forms, paper assembly + mailing addresses, or third-party tax software. See [`forms/schedule-c/filing.md`](./forms/schedule-c/filing.md) for the canonical pattern.

### With other agent runtimes

Each skill is plain markdown with optional reference and example folders. Any runtime that supports tool / file context can use them.

## Quality standards

Every skill in this repo holds to four rules:

1. **Cite every number.** No invented thresholds, rates, or limits. Every value links to an IRS form, publication, IRC section, or Revenue Procedure.
2. **Year-aware.** Numbers that change annually (mileage rate, Section 179 limit, SS wage base) are flagged as year-dependent with a pointer to the canonical IRS page.
3. **Edge-case honest.** When a rule depends on facts the agent doesn't have, the skill tells the agent to ask, not guess.
4. **Audit-grade output.** A CPA should be able to read the agent's deliverable without having to re-derive the math.

## License

MIT — see [LICENSE](./LICENSE).

## Disclaimer

The skills in this repository encode procedural guidance based on publicly available IRS forms and publications. They are not tax advice and do not establish a CPA-client relationship. Tax law is complex and individual circumstances vary; always consult a licensed tax professional for advice specific to your situation.
