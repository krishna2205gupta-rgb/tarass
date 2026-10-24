---
name: ponytail-audit
description: TARA QA skill for a repository-wide, conservative audit of over-engineering and standard-library/native replacements.
license: MIT
homepage: https://github.com/DietrichGebert/ponytail
---

# Ponytail-style QA audit in TARA

Use this audit after understanding the code's purpose and data flow. Inspect the whole generated Python codebase, not only changed lines.

## Find and rank
- `delete`: dead code, unused flexibility, or speculative functionality; replacement: nothing.
- `stdlib`: hand-written functionality already supplied by Python's standard library; name the exact module/function.
- `native`: code or a dependency duplicating a platform/browser/runtime feature; name the feature.
- `yagni`: an abstraction, factory, configuration option, or layer with only one real use.
- `shrink`: repeated or unnecessarily verbose logic that can be simplified without changing behavior.

## Output
Return evidence-backed findings ranked by expected safe reduction. Each finding must include:
- tag (`delete`, `stdlib`, `native`, `yagni`, or `shrink`)
- repository-relative file path
- what is unnecessarily complex and why
- a concrete suggested replacement
- a compatibility/risk note

If no well-supported finding exists, return an empty list. Never invent findings to fill the report.

## Safety boundaries
This is an audit, not permission to rewrite files automatically. Keep recommendations separate from applied refactors. Never remove input validation, error handling, security controls, data-loss protection, or accessibility. Correctness bugs, security weaknesses, and performance concerns must also be reported through normal QA/security checks. Check runtime/Python-version compatibility and existing tests before recommending standard-library substitutions.

## Reference
This TARA skill follows the publicly documented Ponytail project conventions. Original project: https://github.com/DietrichGebert/ponytail
