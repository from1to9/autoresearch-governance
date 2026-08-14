# Governance Evolution

The framework may learn from management defects encountered during real
projects. Evolution is triggered repair, not continuous self-expansion.

## Trigger

A change needs observed evidence that at least one of these occurred:

- valid work was blocked by unnecessary approval or repeated review;
- objective, lease, evidence, retry, or decision state drifted;
- task creation, messaging, compute, or ownership duplicated;
- evidence became invalid, unreachable, or misclassified;
- a role repeatedly loaded irrelevant context or missed required context;
- a stale participant binding misrouted work, a required completion event was
  lost, or all roles became idle without a liveness edge;
- a recurring failure has a smaller testable control;
- a simplification can measurably reduce latency, context, or overhead while
  preserving authority and evidence validity.

Preference, speculative completeness, or the ability to add an abstraction is
not enough.

## Defect record

Create one compact append-only record:

```yaml
defect_id: <stable-id>
observed_symptom: <what-happened>
affected_decision_or_evidence: <scope>
evidence_refs:
  - <reachable-ref>
classification: project_specific | candidate_universal | uncertain
root_cause_hypothesis: <falsifiable-cause>
minimal_change: <smallest-rule-schema-prompt-or-adapter-change>
affected_modules:
  - <module>
active_campaign_compatibility: compatible | migration_required | unsafe
migration_plan: <prospective-version-or-explicit-rebind>
rollback_condition: <observable-condition>
expected_context_or_overhead_effect: <direction-and-measure>
evaluator_and_tests:
  - <check>
change_owner: <role>
independent_reviewer: <role-or-none-with-reason>
decision_ref: <pending-or-ref>
```

Project mechanisms stay local. Only a generalized control may be promoted here,
after removing domain assumptions, runtime identities, paths, credentials, and
current results.

## Learning loop

1. Preserve the failing event, valid work, and affected evidence.
2. Separate a project defect from a reusable governance defect.
3. State the smallest falsifiable root-cause hypothesis.
4. Patch the smallest triggered module, prompt, template, or harness adapter.
5. Reproduce the defect and test autonomy, evidence, privacy, context, and
   active-lease boundaries.
6. Obtain independent high-capability review for a material authority,
   evidence, safety, lifecycle, or model-routing change.
7. Version prospectively and migrate only explicitly affected active state.
8. Monitor the declared benefit and rollback condition at ordinary events.
9. Retain, narrow, or revert based on evidence; record the decision and limits.
10. Upstream a generalized lesson only when external publication is authorized.

An author cannot solely approve a material governance change. Editorial fixes
with objectively equivalent semantics may use mechanical review.

## Authority and continuity

An agent may autonomously improve governance when repository writes are inside
its declared scope and the repair is reversible, testable, and compatible with
active leases. It must not silently change:

- objectives, constraints, non-goals, or completion boundaries;
- task scope, resource ownership, or external authority;
- metrics, estimands, evidence tiers, or acceptance rules;
- prior evidence classes, retry counts, or decision lineage;
- publication, destructive-action, or human-gateway boundaries.

A required safety or evidence-validity correction blocks only the minimum
dependent scope. Compatible experiments, analysis, preservation, and other
lanes continue. A migration binds old and new versions explicitly; it does not
reinterpret history in place.

Self-improvement grants no external authority. A framework may draft a reusable
lesson, but publishing it, installing it elsewhere, or mutating another system
requires existing authorization.

## Evolution budget and evaluation

Each evolution item has one owner, a time or work budget, a close condition,
and an expected benefit. Track only relevant signals:

- time to first valid evidence;
- approval requests inside delegated leases;
- blocked-scope breadth and unowned idle time;
- duplicate creation, delivery, or compute incidents;
- invalid or unreachable evidence;
- context actually loaded by each role;
- material review closure time;
- valid evidence or decisions per unit of governance overhead.

If a change does not improve its declared signal, creates more failures than it
prevents, or delays first evidence, narrow or revert it. Do not build a
self-modifying service, new database, or standing review board unless repeated
measured failures justify that exact mechanism.

## Regression scenarios

Exercise scenarios affected by the change, including:

1. reversible in-lease work proceeds without an approval request;
2. one blocked lane does not stop unrelated work;
3. independent first passes remain independent before discussion;
4. extraordinary results receive reproduction and hostile review;
5. ambiguous create or send does not duplicate work;
6. recovery loads compact durable state rather than full history;
7. lightweight work escalates judgment;
8. active campaigns retain frozen semantics after a prospective update;
9. project-specific experience stays local;
10. a no-benefit change reaches rollback and closes.
11. a wrong task/conversation binding is rejected and repaired before execution;
12. a completed small task notifies its declared dependents without G1 relay;
13. all-idle nonterminal state wakes the minimum authorized G2/G1/G0 set;
14. each durable role recovers from its own memory and event cursor;
15. functional roles and professional lenses produce distinct tests without
    exceeding decision scope or becoming votes.
16. an overdue required reply wakes its declared manager, coordination group,
    or functional inquiry owner to ask directly, while unrelated work continues;
17. one unanswered inquiry routes the smallest affected edge to G1, and G0 is
    woken only if G1 itself is silent or needs repair.
18. when material review is triggered, it closes and the smallest complete
    outcome-bearing run starts before any review without new evidence;
19. hash-only or reconstructible metadata debt warns or backfills without
    blocking work whose canonical semantic identity and provenance are intact;
20. defensive machinery without an observed active-path failure and affected
    result is removed or deferred rather than expanding the mainline.

Repository validation proves structural consistency, not operational benefit.
Retaining a material change also requires evidence tied to its defect record.
