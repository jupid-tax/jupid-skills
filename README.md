# Jupid Skills

Open-source agent skills for accounting, taxes, and finance — used inside [Jupid](https://jupid.com), our AI accountant for solopreneurs and small businesses.

Each skill is a self-contained operating manual that teaches an AI agent how to handle one form, one calculation, or one workflow. Skills are written for [Claude Code](https://claude.com/claude-code), the [Anthropic Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), and any other agent runtime that loads markdown skill packages.

## Repo layout

```
jupid-skills/
├── forms/           # IRS / state forms — fill-out skills
│   └── schedule-c/
├── calculators/     # (planned) tax & finance calculators
└── workflows/       # Multi-step accounting and tax research flows
```

## Skills available

| Skill | Topic |
|-------|-------|
| [forms/schedule-c](./forms/schedule-c/) | IRS Schedule C (Form 1040) — Profit or Loss From Business |
| [workflows/irs-evidence-research](./workflows/irs-evidence-research/) | IRS-only, citation-gated tax research workflow |
| [workflows/linkedin-post-analytics-coach](./workflows/linkedin-post-analytics-coach/) | LinkedIn post analytics review and next-post coaching workflow |
| [workflows/spreadsheet-logic-builder](./workflows/spreadsheet-logic-builder/) | Deterministic spreadsheet logic, reconciliation, and automation workflow |

More skills are in progress.

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

For repeated use, install the folder locally using the platform-specific
instructions below. The GitHub link stays the same for both platforms.

### With Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r jupid-skills/forms/schedule-c ~/.claude/skills/
cp -r jupid-skills/workflows/irs-evidence-research ~/.claude/skills/
cp -r jupid-skills/workflows/linkedin-post-analytics-coach ~/.claude/skills/
cp -r jupid-skills/workflows/spreadsheet-logic-builder ~/.claude/skills/
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
```

Then ask Codex:

```
Use the irs-evidence-research skill. Research this question using official sources only: ...
Use the linkedin-post-analytics-coach skill. Analyze my LinkedIn post analytics export and recommend the next experiment.
Use the spreadsheet-logic-builder skill. Build deterministic spreadsheet logic for this reconciliation workflow.
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
