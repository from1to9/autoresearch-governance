# Operational Controls

This guide preserves field lessons that matter during long campaigns without
forcing every runtime role to read them. Load only the section triggered by the
current event: identity, task creation, ambiguous delivery, launch readiness,
validation, stalled progress, context rotation, resource conflict, or closure.

## 1. State and evidence boundaries

Keep three layers distinct:

| Layer | Contains | Excludes |
| --- | --- | --- |
| Portable governance | rules, schemas, role prompts, adapters | live task IDs, credentials, machine paths, current results |
| Campaign state | anchors, leases, checkpoints, cursors, task map | raw evidence presented as fact without refs |
| Evidence | immutable inputs, manifests, outcomes, analyses, archives | unbound conclusions |

Use an existing repository, artifact store, and task system before inventing a
parallel database or scheduler. Logical records may share one file when their
identities and append-only lineage remain clear.

Every campaign-specific number names its source: statistical design, resource
capacity, safety constraint, economic contract, or sponsor instruction. A
convenient number from another campaign is not a default.

## 2. Goal, experiment, and diagnostic lineage

The campaign anchor binds a versioned goal model:

```yaml
goal_model:
  version: <monotonic-version>
  hash: <canonical-hash>
  root_goal_id: <stable-id>
  root_outcome: <measurable-outcome>
  completion_edges:
    - <requirement-to-evidence-edge>
  semantic_anchors:
    - <compact-term-or-relationship>
  subgoals:
    - subgoal_id: <stable-id>
      parent_id: <id>
      question: <falsifiable-question>
      causal_edge_to_parent: <edge>
      downstream_decision: <decision>
      forbidden_substitutes:
        - <nearby-non-answer>
      diagnostic_budget: <envelope>
```

Each experiment card binds the exact goal-model hash, parent question, causal
edge, downstream decision, forbidden substitutes, predecessor, and evaluation
identity. If diagnostics can displace outcome work, also bind:

```yaml
diagnostic_chain_id: <stable-id-or-none>
diagnostic_sequence: <monotonic-or-none>
counts_toward_streak: <true-or-false>
integration_due: <condition-or-none>
```

A local metric, parameter, component, or failure remains a diagnostic; it does
not become a new objective. Outcome-bearing diagnostics count toward the
declared streak even when negative or underpowered. Pre-outcome infrastructure
or invalid-method failures neither count nor reset it.

At the diagnostic limit, integrate findings into an outcome-bearing comparison,
retire the exact path, or obtain an authorized goal-model change. Relabeling a
nearby detail does not reset the limit. Schema changes are prospective and do
not invalidate a healthy frozen campaign merely for documentation consistency.

Semantic anchors are a low-cost compaction checksum. Their disappearance can
trigger review, but keyword presence never proves alignment; the causal edge
and downstream decision are authoritative.

## 3. Single-writer task creation

Conversation or task creation is a small transaction:

```yaml
creation_key: <campaign/lane/scope-epoch/role>
creation_owner: <supervisor-or-manager>
creation_state: reserved | pending | ambiguous | bound | contained
creation_request_ref: <ref-or-none>
authoritative_task_id: <id-or-none>
duplicate_task_ids:
  - <id>
```

The owner:

1. reserves one stable key;
2. enumerates compatible existing tasks and reuses a match;
3. otherwise issues exactly one create operation;
4. treats a timeout, queued response, request ID, or transport error as
   `pending` or `ambiguous`, not proof that creation failed;
5. reconciles through destination or task-list read-back before any retry;
6. binds one authoritative task before sending executable work or a lease;
7. contains duplicates before any of them begin work.

A completed turn, failed hypothesis, released resource, or missing
acknowledgement is not permission to create a replacement. A new task needs a
terminal prior transaction plus a new scope epoch or recorded rotation gate.

## 4. Idempotent delivery

Before sending a material instruction, freeze:

```yaml
instruction_id: <stable-id>
destination_task_id: <id>
scope_epoch: <version>
content_hash: <canonical-hash>
dispatch_owner: <one-role>
delivery_state: pending | ambiguous | observed | superseded
supersedes: <instruction-id-or-none>
```

An ambiguous send requires destination read-back for the same instruction ID,
hash, and scope. If policy permits one retry after absence is shown, resend the
identical tuple. Never send a blind third copy. Receivers apply the first tuple
once and silently drop duplicates.

One dispatch owner prevents a supervisor, manager, and researcher from
mirroring the same correction. Urgent containment changes urgency, not
idempotence.

## 5. Readiness without approval loops

One bounded prelaunch review covers:

- causal question and control/intervention identity;
- estimand, sample unit, comparison, and important edge cases;
- outcome fields, evidence writer, capacity, and resume behavior;
- executable path, resource safety, and smallest decisive falsifier.

Resolve concrete findings together, run focused verification, and launch. Do
not reopen the same gate through serial reviewers unless new evidence
contradicts the approved design. Scientific comparability comes before hashes,
wrappers, display fields, optional metadata, or defensive branches.

Within its lease, a research lane autonomously repairs reversible experiment
code, configuration, imports, persistence, identity/accounting, tests, and
ordinary local infrastructure. A validation-invalid run is quarantined and its
physical cost recorded; it does not enter scientific sample size or consume a
hypothesis retry. Repairing the cause and obtaining the first valid result is
required progress.

After readiness, the next action starts real validation or returns one
evidence-backed architecture, data, resource, or authority blocker. More cards,
audits, tests, or defensive code without outcome evidence are governance
no-progress.

## 6. Post-launch continuity

Do not interrupt healthy expensive work for reconstructible audit debt:

| Finding | Default action |
| --- | --- |
| Optional field, timestamp, label, descriptive hash, duplicate transport message, or reconstructible encoding defect | continue the atomic run; preserve output; backfill at a safe boundary |
| Result-writer failure with recoverable authoritative outcomes and execution identity | preserve the boundary and reconstruct; do not repeat compute |
| Missing unrecoverable primary outcome or denominator, wrong method or input, leakage, corrupted evidence, unsafe resource state, or intervention not applied | fail closed for affected evidence; repair; rerun only invalid scope |

Code, configuration, branch, runtime source, or evaluator changes open an
evidence epoch. They do not by themselves stop unrelated healthy research.
Incompatible epochs remain unpooled; only the affected batch starts fresh.

## 7. Statistical scale and validation

An execution batch is a recoverable cost unit, not automatically an independent
replicate, inferential look, or total sample cap. Repeated events within one
correlated subject, family, parent, or time block are not independent because a
runner reports many rows.

Before efficacy conclusions or confirmation-scale allocation, freeze the
relevant fields:

```yaml
validation_id: <id>
validation_epoch: <version>
claim_and_tier: <claim-boundary>
estimand: <quantity>
independent_unit_and_correlation: <definition>
compute_or_coverage_unit: <definition>
eligibility_denominators_and_missingness: <definitions>
provenance_freshness_and_leakage: <checks>
minimum_effect_of_interest: <effect>
error_power_and_sidedness: <values>
planned_independent_observations: <count>
sequential_looks_and_spending: <policy>
maximum_cumulative_compute: <envelope>
baseline_intervention_evaluator_identity: <refs>
negative_or_placebo_controls:
  - <control>
invalidation_conditions:
  - <condition>
result_class_to_decision:
  <class>: <decision>
```

At an early semantic or feasibility screen, nonapplicable fields may state the
promotion condition that will require them. Do not build a power framework for
a no-effect screen; do not make an efficacy claim without the required design.

A fresh high-capability validation critic returns one of:

```text
valid_for_claim
valid_for_narrower_claim
screen_only
method_revision_required
invalid_for_claim
unresolved
```

A material method change increments the validation epoch. Prior evidence is
quarantined until a bridge proves comparability. Invalid validation blocks the
affected claim and dependent scale-up, not unrelated routes.

## 8. Progress and intervention

Classify work exactly once:

```text
experiment_result
replication_result
portfolio_decision
enabling_fix
audit_only
blocked
```

Only the first three are evidence progress. Credit an enabling fix only when it
is linked to the experiment it unblocked. Useful portfolio signals include
valid results, replicated results, decisions changed, primary and guardrail
effects, compute per valid result, invalid or duplicate compute, governance
budget, time since evidence, unowned idle time, and free resources while ready
work exists.

An expected experiment window containing only plans, validators, tests,
reports, or governance changes triggers intervention. A finished lane with
ready safe work but no next owner is also no-progress.

| Level | Trigger | Smallest response |
| --- | --- | --- |
| I0 observe | aligned and producing evidence | wait for the declared event |
| I1 correct | small drift or incomplete report | restate boundary and next evidence |
| I2 constrain | excess enabling work or unowned ready lane | freeze extra machinery; run linked experiment |
| I3 reallocate | repeated drift, duplication, poor marginal compute | pause, retire, reassign, or gated rotation |
| I4 restructure | manager cannot preserve objective or portfolio quality | replace manager from frozen state |

Intervention does not grant destructive, external, or scope-expanding
authority.

## 9. Conversation lifecycle and human gateway

Transport `idle` means only that a turn ended. Every nonterminal lane records:

```yaml
research_state: active | awaiting_manager | queued | blocked | retired
disposition: reuse | queue | retire | rotate
resource_lease_state: assigned | released | transferring
next_owner: <role-or-none-terminal>
next_action: <one-action-or-none>
decision_due: <event-or-condition>
predecessor_task_id: <id-or-none>
successor_task_id: <id-or-none>
rotation_reason: <gate-or-none>
```

Reuse is the default for a coherent recoverable lane. Rotate only for a true
independence, isolation, failed-recovery, repeated-drift, or incompatible-phase
gate. Transfer one lease atomically after successor acknowledgement; do not
replay the predecessor transcript.

Exactly one management role is the human gateway:

| Class | Meaning | Handling |
| --- | --- | --- |
| H0 autonomous | charter or lease determines action | decide and continue |
| H1 deferred | input may improve a later choice | batch it; continue |
| H2 scoped | one action needs external authority or value judgment | pause that action only |
| H3 campaign critical | all useful paths depend on one external decision and guessing is unsafe | present one compact decision packet |

H3 requires evidence that the decision lies outside active leases, affects
every useful path, cannot be reduced safely first, and guessing or delay creates
material risk. Silence is not approval, but it is also not a reason to stop H0
work.

## 10. Resources, evidence, cleanup, and reports

Parallel lanes require separate mutable-state ownership. Share immutable inputs
and compatible identity-bound caches through their existing locking contract.
Persist code, input, configuration, evaluator, resource, concurrency, cache,
and owner identity with results. Never infer a fixed research role from a
resource name.

Finalization is a state machine:

```text
running -> result_frozen -> reachable
        -> merged_or_archived -> cleaned
```

Preserve raw inputs, durable evidence, active resume state, foreign changes,
and unmerged work. Clean only exact resolved targets after reachability,
ownership, process/lock, and merge/archive checks. Recurring campaign tasks are
resources and need an explicit retained or removed disposition.

A management report contains objective status, primary and guardrail effects,
uncertainty, valid and invalid work, failure cost, route and retry state,
reviews and dissent, resource changes, human-decision scope, safe work
continuing, next actions, and next report condition. A no-result period says so
and names cost, failure class, corrective decision, and next evidence condition.
Do not concatenate child logs.

## 11. Failure repair index

| Observed failure | Repair |
| --- | --- |
| unchanged state is polled | restore event/cursor reads and silence no-change events |
| ambiguous create duplicates tasks | bind one creation key and contain duplicate leases |
| ambiguous instruction is resent | read destination; retry one identical tuple only after absence |
| invalid evidence repeats | quarantine affected claims and repair the smallest method boundary |
| review becomes an approval loop | require one concrete material fault or close it |
| challenge becomes a stalling tactic | require new evidence and close duplicate objections by lineage |
| completed lane becomes unowned | choose reuse, queue, retire, or gated rotation |
| one blocker stops the campaign | narrow the blocked scope and advance safe alternatives |
| governance becomes the project | reduce to anchor, leases, checkpoints, decisions, and evidence refs |
| context drifts after correction | rotate from a compact checkpoint instead of replaying history |

Activate these controls after the named event or a material risk. They are not
a checklist that every ordinary experiment must complete.
