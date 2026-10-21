# AutoResearch Governance Specification

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are
normative. Current human directives apply within system and runtime requirements;
this specification and historical records grant no additional authority.

## 1. Scope

Use this protocol for long-running research with independent directions,
contested evidence, costly resources, or likely context rotation. Use an ordinary
task for a self-contained answer or bounded change. The protocol is independent
of domain, vendor, harness, compute provider, storage and evaluation method.
[Harness adaptation](docs/harness-adaptation.md) preserves behavior, not tool names.

## 2. Invariants

- The authorized objective and constraints control action; hypotheses remain
  replaceable. Confidence, repetition, rank and consensus are not evidence.
- Each action has a coherent owner, scope and completion condition. Independent
  work has separate mutable-state ownership and appropriate context separation.
- Durable evidence and decisions survive context loss. New explicit human
  instructions supersede older controls; recent conversation alone cannot
  silently rewrite accepted evidence or an active evaluation contract.
- Preserve valid work, raw inputs, healthy jobs, foreign changes and accepted
  evidence. A dispute blocks only its smallest dependent scope.
- Nonterminal work has an owner/action, future wake, pending decision, reopening
  event or bounded delivery repair. A manager need not remain active to watch it.
- Validation and traceability serve the outcome; completeness of proof is not
  an independent objective.

### Proportionate design and sufficient verification

Use the simplest sound design. Add or retain defensive machinery only for a
current requirement or a concrete material failure it prevents. Its benefit MUST
justify complexity, cost and interruption. Speculative uncertainty is not a
reason to add guards, fallbacks, wrappers, schemas or governance.

Validate at meaningful trust boundaries and trust established internal contracts.
Reuse adequate evidence. Hash equality, exhaustive provenance and repeated
consistency checks are not default execution prerequisites. Put a necessary
check at its owning boundary; do not propagate it through every layer.

Judge compatibility by what remains correct and usable. Accept authorized change
and recompute only what a relevant semantic change invalidates. Metadata drift,
incomplete history or missing auxiliary evidence alone MUST NOT force a restart,
new approval or broader validation. Stop only the operation that violates an
actual correctness, authority or safety requirement; continue independent work.

Prefer removing unnecessary mechanisms to adding exceptions. Preserve real
business/security constraints, resource cleanup and meaningful errors. Follow
existing error conventions rather than hiding broken contracts behind fabricated
defaults. Once the smallest sufficient check passes and no material issue remains,
finish. Reopen only for evidence that can change the result or next action. Do
not create another approval process or proof ledger to enforce this principle.

## 3. Roles and authority

G0, G1 and G2 name governance responsibilities, not a required number of new chats.
Use the smallest arrangement that preserves necessary ownership and independence.

| Role | Responsibility |
| --- | --- |
| Sponsor | Outcome, hard constraints and external authority |
| G0 supervisor | Human gateway, charter, manager repair and completion |
| G1 manager | Acceptance, dependencies, portfolio, resource leases and decisions |
| G2 executor or reviewer | One coherent research, implementation, validation, operations or synthesis task |

Keep implementation, independent validation, training/research, deployment and
management responsibilities clear. Reuse a suitable conversation. Creation,
messages and subagents require authority under the current harness; a role chart
or incoming peer request does not supply it. A bounded subagent returns one
artifact; independent long-lived work needs an explicitly owned durable task.

Assign a professional lens only when it changes mechanisms, risks, evidence or
tests. Titles and head count are not votes. A bounded adjudicator may decide its
predeclared dispute; it cannot assume portfolio or sponsor authority.

## 4. Autonomy and non-blocking progress

Executors MUST complete authorized work and resolve routine reversible choices
without reassurance or repeated permission requests. Status questions do not
pause that work. Prepare the concrete reviewable result before requesting an
approval that is actually needed.

Escalate a material missing decision or action outside authority: changed
objective, hard constraint, destructive/external scope, resource ownership or
evaluation contract. State the rule and concrete conflict. Block only the
dependent action. A campaign is blocked only when no useful authorized path
remains; release idle scarce resources and advance safe alternatives.

## 5. Model capability routing

Use the highest available capability and reasoning effort for research direction,
causal diagnosis, ambiguous experiment design/interpretation, portfolio decisions,
independent criticism, extraordinary claims and final synthesis. Follow explicit
user choices and runtime availability; a model label is not evidence of validity.

Lightweight models are for sealed tasks with explicit inputs, bounded outputs,
no material interpretive discretion and an objective verifier. They escalate
ambiguity, conflicts, new hypotheses, repeated failures or authority questions.
Record the routing reason and verifier in the existing lease; do not let an
unchecked lightweight result promote a material claim.
See [model routing](docs/model-routing.md).

## 6. Context authority

Keep a stable campaign anchor (C0), task lease (C1), evidence/decisions (C2),
replaceable checkpoint (C3) and transient conversation (C4). C4 is working context,
not a substitute for the first four. Record material findings and decisions
before dependent action. One compact role snapshot indexes current scope, event
cursor, findings, dependencies and next action; it is not a transcript.
Read only context needed for the next decision. See [context](docs/context.md).

## 7. Launch

Before research compute, define the outcome, hard constraints, acceptance and
claim boundaries, causal questions, resources, mutable-state owners and relevant
review/retry rules. Give each role its lease, current checkpoint and necessary
references. Resolve details inside delegated authority by testing or judgment.

Use existing records and [launch guidance](docs/launch.md); template fields may
be nonapplicable. Do not create a service, dashboard or approval chain to launch
an ordinary task. Hierarchy and recurrence are optional mechanisms.

## 8. Research cycle

Bind the falsifiable mechanism, baseline/intervention, sample unit, metrics and
guardrails, relevant input/code/config/evaluator identities, budget, outcome and
next decision in one experiment card. Run the smallest complete outcome-bearing
experiment once ready. Infrastructure is justified only when it enables valid
work. Tests and review support the experiment; they do not replace its outcome.

Invalid runs retain their cost but cannot support scientific claims. Negative
valid results MUST NOT be relabeled as infrastructure failures. Diagnose the
first failed boundary and repair the smallest cause.

## 9. Exploration and failure continuity

Cover the leading, mechanistically orthogonal and falsification/boundary routes
before convergence, or record a scope/resource/evidence reason and reopening
condition for a narrower portfolio. Group ideas by mechanism, not wording.

Classify attempts as hypothesis refuted, mechanism not activated, method invalid,
implementation fault, insufficient information, resource blocked, scope mismatch
or positive pending review. Noninitial attempts identify their predecessor and
material novelty: repaired invalidity, new mechanism, registered replication,
justified boundary or new evidence. More compute and renamed tasks alone do not
justify repeating a failed route.

When retry authority is exhausted, pivot using negative evidence and alternatives.
If the objective/budget remain active but no route remains, reset the search from
the objective and unresolved causal gaps. One failed implementation or inability
to imagine another route does not prove the objective impossible.

## 10. Collaboration and delivery

Commission one concrete action/dependency with its artifact/revision, scope,
deliverable, decision owner and return path. Omit history, broadcasts and repeated
constraints. Freeze independent first passes before peer advocacy, then exchange
evidence and resolve material disagreements with the cheapest discriminating test.

Executors own implementation, checks, observation, recovery and authorized
delivery. When independent review is required, the executor freezes the artifact
and requests the authorized reviewer directly. They resolve findings and complete
delivery, then notify management once. Deployment consumes accepted delivery under
its own authority. Peers cannot retask one another or expand leases.

A management handoff is complete when receipt, deliverable and return path are
clear. The manager MUST end that turn. Receipt confirms delivery, not execution.
Resume on final delivery, a blocker requiring a management decision, or an explicit
user status/intervention request. Do not watch task status or output artifacts,
wait on execution, or create substitute monitors after handoff. Explicitly
requested monitoring stays with its assigned executor and cadence.
See [communication and liveness](docs/communication-liveness.md).

## 11. Independent review and extraordinary claims

One context MUST NOT be the sole proposer, validator and final adjudicator of a
material claim. Review is proportionate to the affected decision and uses frozen
artifacts. Further rounds need new material evidence and a decision they can change.

Unusually strong, broad, clean or surprising claims remain positive pending review.
Before dependent acceptance or scale-up, freeze the claim and evidence, obtain
independent reproduction and hostile criticism, run cheap decisive controls, and
preserve dissent in the claim-tier decision. Extraordinary means high unverified
risk, not automatically true or false. See [collaboration](docs/collaboration.md).

## 12. Decisions and human control

A material decision cites supporting evidence, alternatives, relevant review,
unresolved dissent, owner and next action. Match the record to the decision;
ordinary reversible choices do not need a new decision dossier.

Apply explicit human outcomes, constraints, stops and exact-method choices.
Test factual premises, causal explanations and suggested remedies as hypotheses.
Explain errors and uncertainty plainly without delaying authorized work. A
challenge names contrary evidence and its affected scope; rank is not an answer.

## 13. Event-driven operation

Send one useful material delta to declared recipients through an authorized
route. Verify the destination and reconcile ambiguous creation/delivery before
retrying. Do not duplicate built-in result delivery or acknowledge duplicates.

Unchanged monitoring is silent. An optional authorized watchdog repairs missing
ownership or delivery; it is not a second manager or observer of healthy work.
The recurring prompt contains a stable task-record pointer, action/trigger,
authority and terminal condition. Current progress belongs in that record.
See [operational controls](docs/operational-controls.md) only when needed.

## 14. Recovery

Read current instructions, own binding/lease, compact checkpoint, relevant
post-cursor events and next-action artifacts. Do not replay full history or infer
intent from the last fragment. Reconcile a real conflict at its owning source.
Preserve valid stages and compatible partial work; native continuation is preferred
to starting over. Verify consumption and new progress at the relevant boundary.

## 15. Isolation and safety

Concurrent writers need separate mutable-state ownership; shared ordered state
needs serialized ownership. Preserve foreign work and accepted evidence. Existing
authority governs publication, destructive actions and process control separately.
Apply a stop immediately to its named scope. Stopping a monitor does not stop
computation unless that action was also authorized.

## 16. Completion

Match the requested outcome to sufficient reachable evidence and required review.
Separate accepted implementation, delivered revision, deployment, actual runtime
adoption, recovery/progress, performance and domain outcome. One stage, passing
tests or a successful exit is not evidence for every later boundary.

State supported claims, limitations, remaining work and next owner. Give products,
resources and recurring tasks their authorized disposition; cleanup is not an
automatic consequence of completion. Do not rerun accepted work for a new SHA or
to improve a report when behavior and its evidence remain valid.

## 17. Minimum implementation

An existing task record can hold campaign scope, participant bindings, leases,
checkpoint, evidence/decisions and artifact references. Separate files only when
ownership or recovery needs them. Templates are aids, not required bureaucracy.
Runtime prompts point to canonical rules rather than copying the whole manual.

## 18. Governance learning

Improve the smallest canonical rule for a current requirement, observed defect
or concrete simplification. Generalize the mechanism before publishing it: remove
project identities, runtime facts and accidental thresholds. Material authority,
evidence, safety, lifecycle or model-routing changes receive independent review;
editorial equivalents use mechanical checks. Apply changes prospectively without
silently rewriting active contracts or historical evidence. Compatible work
continues. Close or narrow a repair that does not provide its expected benefit.
See [governance evolution](docs/evolution.md).
