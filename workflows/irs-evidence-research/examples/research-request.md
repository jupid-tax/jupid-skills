# Example: Reusable Research Request

Use this prompt in Codex, Claude Code, or another agent runtime after installing
or loading the `irs-evidence-research` skill.

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

