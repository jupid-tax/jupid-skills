# Jupid Skills

Open-source agent skills for accounting, taxes, and finance — used inside [Jupid](https://jupid.com), our AI accountant for solopreneurs and small businesses.

Each skill is a self-contained operating manual that teaches an AI agent how to handle one form, one calculation, or one workflow. Skills are written for [Claude Code](https://claude.com/claude-code), the [Anthropic Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), and any other agent runtime that loads markdown skill packages.

## Skills available

| Skill | Topic |
|-------|-------|
| [schedule-c](./schedule-c/) | IRS Schedule C (Form 1040) — Profit or Loss From Business |

More skills are in progress.

## Using a skill

### With Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r jupid-skills/schedule-c ~/.claude/skills/
```

Then in any Claude Code session, ask the kind of question the skill is built for:

```
> Help me fill out Schedule C for my freelance business
```

Claude will detect the trigger phrases declared in the skill's frontmatter and engage.

### With the Anthropic Agent SDK

Load the skill's `SKILL.md` into your system prompt; load reference and example files on demand based on what the user's situation needs.

```python
from anthropic import Anthropic
from pathlib import Path

skill = Path("jupid-skills/schedule-c/SKILL.md").read_text()
references = {
    p.stem: p.read_text()
    for p in Path("jupid-skills/schedule-c/references").glob("*.md")
}
```

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
