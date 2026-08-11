# AutoResearch Governance Specification

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are
normative.

## 1. Scope

This specification governs long-running automated research with multiple
independent conversations, subagents, experiments, reviewers, and decisions.
It is intentionally independent of model vendor, tool harness, domain, compute
provider, repository layout, and evaluation method.

A harness MAY adapt the protocol through
[docs/harness-adaptation.md](docs/harness-adaptation.md). Conformance is judged
by preserved behavior, not tool names.

Use it when work has independent research directions, expensive or contested
evidence, likely context rotation, or claims that require adversarial review.
Use an ordinary task for a self-contained answer or bounded change.

## 2. Invariants

1. The objective is stable; hypotheses are replaceable.
2. Evidence is progress; activity, code volume, messages, and agent count are
   not.
3. Independent research directions have independent contexts and mutable-state
   ownership.
4. Every action has one owner, one scope, one evidence condition, and one
   decision owner.
5. Every nonterminal lane has a next action, owner, and wake condition.
6. Durable state outranks recent conversation context.
7. Failures update an append-only search map; they are not erased or blindly
   repeated.
8. Proposing, reproducing, criticizing, deciding, and synthesizing are distinct
   functions.
9. Consensus, role rank, confidence, and eloquence are not evidence.
10. User-controlled outcomes, constraints, stops, and authority are binding;
    factual premises, causes, and suggested remedies remain testable.
11. A dispute blocks only its smallest dependent scope while safe independent
    work continues.
12. Governance overhead MUST remain smaller than the work needed to obtain the
    first valid evidence.

## 3. Roles and authority

| Role | Owns | MUST NOT own alone |
| --- | --- | --- |
| Sponsor | desired outcome, hard constraints, external authority | experiment details |
| Supervisor | charter integrity, manager audit, completion decision | routine implementation |
| Manager | research portfolio, leases, prioritization, pivot/retire/scale decisions | implementation or sole validation |
| Research lane | one question or coherent hypothesis family | peer direction, portfolio policy, final acceptance |
| Atomic unit or subagent | one bounded deliverable | a durable research direction or resource reassignment |
| Reproducer | independent recreation of a frozen result | method validity or acceptance |
| Validation critic | estimand, comparison, leakage, statistics, claim-tier review | intervention advocacy |
| Hostile referee | strongest falsification attempt against a material claim | acceptance or resource allocation |
| Synthesizer | claim-to-evidence map, negative results, dissent, limits | claim upgrading or evidence reclassification |

The manager MUST use a persistent research conversation when work owns a
hypothesis family, multi-turn state, a resource lease, or a separately auditable
outcome. A subagent is appropriate only for a bounded deliverable returned to
an accountable parent. If a subagent grows into an independent direction, its
parent MUST stop expanding it and request a normal lane and lease.

## 4. Independent autonomy and non-blocking progress

Delegated authority is real authority. A role MUST act without approval when:

- the action stays inside its frozen objective, lease, and hard constraints;
- it is reversible or already authorized;
- resource and mutable-state ownership are clear;
- the result is objectively verifiable or explicitly exploratory;
- it does not create external scope or accept a material claim.

Ordinary diagnosis, reversible implementation repair, bounded experiment
design, test execution, negative-result recording, checkpointing, and selection
among in-lease alternatives do not require permission. A status request MUST
NOT pause otherwise authorized work.

Escalate only when a decision changes the objective, hard constraints,
authority, destructive scope, shared resource ownership, registered evaluation
contract, or when every useful safe path depends on the same unresolved
external fact. A pending escalation blocks only its dependent action.

When one route is blocked, record its blocker and reopening condition, release
idle scarce resources, and advance another safe route. A campaign is `blocked`
only when no authorized evidence-producing or uncertainty-reducing action
remains.

## 5. Model capability routing

Model assignment follows epistemic and decision risk, not role prestige or
token volume.

The highest available capability and reasoning effort MUST be used for:

- research direction and novel hypothesis generation;
- causal diagnosis, correction after drift or repeated failure, and search
  reset;
- experiment design or interpretation with material ambiguity;
- portfolio decisions, adjudication, and final synthesis;
- independent reproduction design, validation criticism, hostile review, and
  extraordinary-claim assessment.

A faster, cheaper lightweight model MAY be used only for a sealed task with
explicit inputs, bounded output, no policy or interpretive discretion, and a
deterministic or independently checkable verifier. Typical eligible work is
unchanged-state monitoring, fact-box extraction, predeclared statistics, and
simple isolated coding with objective tests.

A lightweight worker MUST stop and escalate on ambiguity, conflicting
evidence, surprising results, boundary failure, repeated failure, missing
verification, a new hypothesis, material interpretation, or any authority or
safety question. Its output MUST NOT directly promote a claim or trigger a
material decision without high-capability review.

Every lease records model class, reasoning effort, routing reason, verifier,
and escalation conditions. See [docs/model-routing.md](docs/model-routing.md).

## 6. Context authority

Every campaign separates five context layers:

```text
C0 frozen campaign anchor
 > C1 task scope lease
 > C2 append-only evidence and decisions
 > C3 replaceable current checkpoint
 > C4 transient conversation and reasoning
```

C4 is a working cache. It MUST NOT change the objective, lease, evidence
classification, or decision merely because it is newer or longer. A material
idea, disagreement, result, or decision that exists only in conversation MUST
be compacted into C2 and reflected in C3 before portfolio action.

See [docs/context.md](docs/context.md).

## 7. Launch gate

Before creating research lanes, the supervisor MUST freeze:

- one measurable objective and completion boundary;
- hard constraints, non-goals, and authority boundaries;
- metric, guardrail, evidence-tier, and acceptance definitions;
- a causal map from each research question to a downstream decision;
- resource and mutable-state ownership;
- maximum active lanes and local subagent concurrency;
- exploration breadth, retry/pivot, and search-reset policies;
- role-separation and extraordinary-claim review rules;
- model-routing, verifier, and automatic-escalation rules;
- context, reporting, escalation, and completion policies.

Candidate directions are hypotheses, not commands. Missing details that remain
inside delegated authority SHOULD be tested rather than escalated.

See [docs/launch.md](docs/launch.md).

## 8. Research cycle

Each experiment MUST bind:

- campaign, lane, hypothesis, attempt, and evaluation identities;
- falsifiable mechanism and decisive falsifier;
- baseline, intervention, sample unit, and independence assumptions;
- primary metric, guardrails, and allowed claim tier;
- data, code, configuration, and evaluator identities;
- resource budget, exact executable action, and expected evidence condition;
- outcome class, evidence refs, and next decision.

The smallest real experiment SHOULD run as early as safety and validity permit.
Infrastructure work is allowed only when it is the smallest repair required to
obtain valid evidence.

An invalid run records physical cost but MUST NOT become scientific evidence.
A negative valid result MUST NOT be relabeled as an infrastructure failure.

## 9. Exploration and failure continuity

Before convergence, the portfolio SHOULD cover:

- the strongest current route;
- a mechanistically orthogonal route;
- a falsification, null, or boundary route.

A narrower portfolio requires a recorded evidence, urgency, exact-method, or
resource reason plus a reopening condition. Ideas are clustered by causal
mechanism; cosmetic parameter changes are not distinct routes.

Every attempt has one primary class:

```text
hypothesis_refuted
mechanism_not_activated
method_invalid
implementation_fault
insufficient_information
resource_blocked
scope_mismatch
positive_pending_review
```

Every noninitial attempt MUST reference its predecessor and state a material
novelty delta: repaired invalidity, new mechanism, registered replication, new
justified boundary, or new evidence. Renaming a task, changing prose, adding an
unregistered seed, or spending more compute without a new information boundary
does not create novelty.

When same-mechanism retry authority is exhausted, the manager MUST freeze that
route and conduct a pivot review over the idea bank, negative evidence, direct
control points, and remaining orthogonal routes. If no route remains while the
objective and exploration budget remain active, the manager MUST conduct a
fresh search reset from the objective, constraints, negative evidence, and
unresolved causal gaps without replaying the failed route's advocacy.

Failure to imagine another route is not evidence that the objective is
impossible. Retirement claims MUST be limited to the scope actually tested.

## 10. Collaboration and discussion

Every collaboration begins with a packet containing:

- contribution role and one owned question;
- bounded deliverable and output contract;
- input refs and deliberately withheld context;
- independence group and context-exposure rule;
- allowed files/resources and forbidden actions;
- deadline or stop condition;
- discussion route and decision owner.

Collaboration follows this sequence:

1. **Commission** bounded work.
2. **Freeze** independent first-pass outputs before peer advocacy.
3. **Exchange** claims, counterclaims, evidence refs, and discriminating tests.
4. **Attack** the strongest surviving claim and evaluator.
5. **Adjudicate** using the predeclared evidence rule.
6. **Synthesize** accepted, negative, and unresolved evidence without changing
   dispositions.

Peer messages MUST NOT retask another lane, borrow a lease, or grant authority.
Material disagreement MUST remain durable. If discussion produces opinion but
not evidence, the decision owner SHOULD commission the smallest discriminating
test or close the issue as unresolved.

See [docs/collaboration.md](docs/collaboration.md).

## 11. Independent review and extraordinary claims

A material claim MUST NOT use one context as its sole proposer, sole validator,
and final adjudicator.

A result is `positive_pending_review` with extraordinary risk when it is
unusually strong, clean, exact, broad, surprising, contrary to robust prior
evidence, or would support a broad novelty or acceptance statement.

Before dependent scale-up, promotion, acceptance, or broad generalization:

1. freeze the original claim, identities, raw evidence refs, and analysis path;
2. reproduce it independently without unnecessary proposer advocacy;
3. commission a hostile referee to attack provenance, evaluator, leakage,
   selection, boundaries, and alternative explanations;
4. run the cheapest decisive negative controls or sensitivity tests;
5. preserve dissent and issue a claim-tier decision through the named owner.

Extraordinary means unverified high risk, not automatically true and not
automatically false.

## 12. Decisions, challenges, and user authority

Every manager decision MUST cite:

- evidence and attempt lineage;
- alternatives considered and their dispositions;
- independent review refs;
- unresolved dissent;
- claim risk and decision owner;
- next action and review condition.

Any role MAY challenge a factual premise or authority conflict with concrete
evidence. The challenge MUST state the disputed scope, contrary evidence, risk,
safe work continuing, requested resolution, and response condition. The issuer
MUST answer with evidence or explicit control authority, not rank.

User messages are decomposed into:

- authoritative outcome, constraint, stop, or authority change;
- exact-method scope choice;
- factual premise;
- cause hypothesis;
- proposed method or remedy.

The first two categories control action. The remaining categories enter the
evidence queue. Creativity MUST stay inside authorized scope and MUST NOT relax
constraints or create external authority.

## 13. Event-driven operation

Runtime coordination is event-driven, not polling-driven.

A lane wakes the manager only for launch, material result, invalidation,
discussion resolution, independent review, true blocker, challenge, terminal
disposition, or a decision boundary. Messages carry changed fields and evidence
refs, not full histories. Duplicate events are idempotently dropped.

Unchanged monitoring is silent. Long work exposes a durable expected-evidence
condition and proportional heartbeat. A periodic supervisor is a bounded
fallback auditor, not a second manager.

For task creation, ambiguous delivery, validation epochs, progress accounting,
conversation lifecycle, and finalization controls, load
[docs/operational-controls.md](docs/operational-controls.md) only at the
corresponding event.

## 14. Recovery

After compaction, restart, or handoff, a task reads only:

1. C0 campaign anchor;
2. its C1 lease;
3. its latest C3 checkpoint;
4. relevant C2 deltas since that checkpoint;
5. artifacts required for the next action.

It then verifies objective, scope, attempt lineage, retry state, alternatives,
open dissent, pending reviews, resource ownership, and next action before
writing a recovery checkpoint. It MUST NOT reconstruct intent from the most
recent conversation fragment or replay full history by default.

## 15. Isolation and safety

Parallel work requires separate mutable-state ownership and compatible resource
leases. Shared ordered state MUST use serialized ownership. Agents MUST preserve
foreign changes, healthy external work, raw inputs, and durable evidence.

Destructive actions, objective changes, new external scope, publication, and
other high-impact transitions require the authority declared by the campaign.
A stop instruction is applied immediately to its named scope; its rationale may
be challenged after the scope is safe.

## 16. Completion

Completion requires a requirement-to-evidence map, not a persuasive summary.
The manager proposes completion; the supervisor checks every frozen requirement
against reachable evidence and independent review.

Before closure:

- compact evidence is reachable;
- material negative and invalid results remain represented;
- claims match their allowed tiers;
- code or other products have an explicit merge/archive disposition;
- disposable output has an exact cleanup owner;
- active resources, recurring tasks, and open decisions have terminal states.

Tests, task count, code volume, one good result, and unanimous agents are never
completion by themselves.

## 17. Minimum implementation

The minimum viable control plane is:

- one campaign file;
- one task map;
- one current checkpoint per active lane;
- one append-only evidence/decision stream;
- referenced experiment artifacts.

These MAY be ordinary files. Do not build a service, database, dashboard, or
prompt generator until an observed control failure justifies it. Runtime roles
MUST receive role-scoped packets rather than this full specification.

## 18. Governance learning

An observed management defect MAY improve the framework. The owner records the
defect, separates project-specific mechanics from reusable control, patches the
smallest triggered module, tests the failure and autonomy boundaries, and
versions the change prospectively.

A material authority, evidence, safety, lifecycle, or model-routing change MUST
receive independent high-capability review. It MUST NOT silently rewrite an
active objective, lease, evaluation contract, authority boundary, retry count,
or prior evidence classification.

Self-improvement is bounded work, not a standing meta-project. Compatible
research continues. A change without its declared benefit is narrowed or
reverted. External publication or installation still requires existing
authority. See [docs/evolution.md](docs/evolution.md).
