# Example: Reusable Research Request

Use this prompt in Codex, Claude Code, or another agent runtime. The same
GitHub folder is the source for both Codex and Claude Code:

```text
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/irs-evidence-research
```

If the agent can access GitHub, paste this:

```text
Use this skill from GitHub:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/irs-evidence-research

If you can tell whether this session is Codex or Claude Code, use the matching
runtime behavior. If you cannot tell, ask me whether I am using Codex or Claude
Code.

Research my tax question using official IRS sources only:
[QUESTION]
```

If the skill is already installed or loaded, paste this shorter version:

```text
Use the irs-evidence-research skill.

Research this question using official sources only:
[QUESTION]

Facts known:
- Tax year:
- Taxpayer/entity type:
- Form or filing obligation:
- Jurisdiction:
- Facts already confirmed:
- Facts uncertain:

Rules:
- Do not answer from memory.
- Cite every material claim with an official source and pinpoint reference.
- If the official source does not support the conclusion, say "not determined".
- Separate supported conclusions from open facts.
- Do not give personalized tax advice; produce research support for review.
```
