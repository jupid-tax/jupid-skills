#!/usr/bin/env python3
"""Generate a blank spreadsheet automation rule spec."""

from __future__ import annotations


SPEC = """# Spreadsheet Automation Rule Spec

## Job
Build deterministic logic to:

## Tool Target
- [ ] Excel desktop
- [ ] Excel Online
- [ ] Google Sheets
- [ ] Local Python script
- [ ] Other:

## Source A
Sheet/file name:
Columns:
Approximate row count:
Key fields:

## Source B
Sheet/file name:
Columns:
Approximate row count:
Key fields:

## Matching / Transformation Rules
Exact match fields:
Fuzzy match fields:
Date tolerance:
Amount tolerance:
One-to-one / many-to-one / many-to-many:
Tie-breakers:
Ignore rules:
Priority order:

## Normalization
Whitespace:
Case:
Punctuation:
Vendor/customer aliases:
Date format:
Amount format:

## Desired Outputs
- [ ] Matched rows
- [ ] Unmatched Source A
- [ ] Unmatched Source B
- [ ] Ambiguous matches
- [ ] Duplicate candidates
- [ ] Exception report
- [ ] Clean export
- [ ] Audit log

## Verification Checks
Source row counts:
Output row counts:
Total amount tie-out:
Known correct examples:
Known exception examples:
Reviewer signoff:

## Privacy Constraint
- [ ] Work from headers only
- [ ] Work from fake/anonymized sample rows
- [ ] Inspect local workbook
- [ ] Other:

## Open Questions
-
"""


def main() -> int:
    print(SPEC)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

