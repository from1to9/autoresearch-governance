# Model Capability Routing

Use model capability where an error can redirect the research program. Use a
lightweight model where correctness is sealed by the task and its verifier.

## Default classes

| Class | Default work | Required reasoning |
| --- | --- | --- |
| `high` | research, hypothesis generation, causal diagnosis, correction, experiment design and interpretation, portfolio decisions, synthesis | highest available |
| `adversarial_high` | independent review, reproduction design, hostile criticism, extraordinary-claim assessment | highest available |
| `lightweight` | monitoring, fact-box extraction, predeclared statistics, simple sealed coding | low or medium, optimized for speed and cost |

`High` and `adversarial_high` may use the same underlying model. The separate
label records independence and purpose; it does not imply a hierarchy between
agents.

G0/G1 supervision, G2 research, correction/recovery, adjudication, validation
criticism, hostile review, and material synthesis default to the strongest model
at its highest supported reasoning effort, regardless of professional lens.

## Lightweight eligibility gate

A task is eligible only when every answer is yes:

1. Are inputs complete, immutable, and explicitly referenced?
2. Is the output bounded by a schema, patch scope, or named fields?
3. Is correctness deterministically testable or independently checkable?
4. Does the worker lack discretion to change objectives, hypotheses, metrics,
   claim tiers, resources, or authority?
5. Can failure stop locally without contaminating evidence or shared state?
6. Are ambiguity and anomaly escalation conditions explicit?

If any answer is no, route the work to `high`.

## Eligible lightweight patterns

- **Monitoring:** read declared fields, compare them with fixed thresholds,
  emit only changed state, and never infer cause.
- **Fact box:** extract exact facts and provenance into a fixed schema; do not
  reconcile conflicts or form conclusions.
- **Statistics:** execute preregistered calculations over frozen inputs; do not
  choose tests after seeing results or interpret material findings.
- **Simple coding:** edit an isolated, explicitly bounded surface with objective
  tests; exclude security, safety, irreversible migration, architecture, and
  ambiguous product behavior.

A monitor that only compares sealed fields may be lightweight. A watchdog that
diagnoses drift, selects a wake target, repairs identity/routing, or recommends
manager replacement is correction work and therefore `high`.

## Mandatory escalation

A lightweight worker stops, preserves its partial output, and emits
`needs_high_capability` when it encounters:

- ambiguous instructions or more than one reasonable interpretation;
- missing, inconsistent, or conflicting evidence;
- an unexpected or unusually strong result;
- verifier failure, uncovered behavior, or scope boundary pressure;
- repeated failure after one ordinary repair;
- a need to invent a hypothesis, choose a method, explain a cause, or recommend
  a decision;
- safety, authority, destructive-action, or external-scope uncertainty.

Escalation is a successful disposition, not worker failure. The receiving
high-capability role gets the sealed packet, partial artifact, verifier output,
and the exact uncertainty—not the full worker transcript.

## Review boundary

Lightweight output may update mechanical state when its verifier passes. It may
not directly:

- accept or reject a research claim;
- change a metric, guardrail, or evaluation method;
- retire a route or allocate research resources;
- resolve dissent or an extraordinary claim;
- declare campaign completion.

A high-capability decision owner reviews any lightweight output used at a
material decision boundary.

## Recording assignment

Each task lease or collaboration packet records:

```yaml
model_assignment:
  class: high | adversarial_high | lightweight
  reasoning_effort: highest_available | low | medium
  routing_reason: <why this class is safe>
  objective_verifier: <test, schema, or reviewer>
  escalate_on:
    - <condition>
```

Do not pin vendor-specific model names in the governance core. The launcher maps
these capability classes to currently available models and records that mapping
in the campaign anchor so later recovery can reproduce the assignment. A
harness adapter that cannot provide separate tiers uses the strongest available
model for all material work; it never silently substitutes a cheaper model.
