# Contributing

Contributions should make the protocol more portable, testable, or
context-efficient.

## Principles

- Keep domain facts, hostnames, credentials, private paths, and live task IDs
  out of the repository.
- Put universal decision rules in `GOVERNANCE.md`.
- Put operational detail in the relevant `docs/` guide.
- Keep prompts role-scoped and short; do not copy the full specification into
  runtime prompts.
- Add fields to templates only when they change authority, evidence lineage,
  recovery, or a downstream decision.
- Avoid fixed agent counts, compute budgets, thresholds, or vendor-specific
  APIs in normative rules.

Run validation before submitting changes:

```bash
python3 scripts/validate.py
```
