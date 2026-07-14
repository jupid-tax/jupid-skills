# Validation and limits

## Existing prompt-pack evidence

The source prompt pack was tested as a three-step workflow:

1. partial file to missing/unclear/reviewer-question list;
2. approved gap list to client-ready request;
3. final missing-item list to follow-up schedule.

The independent review reached `FINAL VERDICT: PASS` after:

- replacing proof language with controlled smoke-test language;
- distinguishing real OS source material from synthetic client facts;
- tightening wording around platform tax forms;
- adding a second S-Corporation owner/payroll scenario.

This remains a controlled validation, not evidence that the prompts are reliable for every client or entity type.

## Agent-package checks

Each agent must:

- have valid YAML frontmatter;
- use a lowercase hyphenated identifier;
- state specific trigger conditions and a `When to invoke` section;
- operate read-only;
- separate facts, assumptions, unclear items, and professional-review questions;
- refuse final tax, accounting, filing, or approval decisions;
- produce a structured output another human can review quickly.

## Release boundary

Before sending this pack externally, Slava should approve:

- the exact GitHub URL;
- whether the recipient gets the whole pack or only the requested resource;
- the accompanying LinkedIn message.

No connection request or message is automated by this repository package.
