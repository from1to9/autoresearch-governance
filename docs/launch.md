# Launch and Lifecycle

This guide turns the core specification into a minimal executable campaign.

If the harness has not been mapped yet, first run the bounded
[harness adaptation](harness-adaptation.md). Missing optional automation does
not prevent a manual or event-driven launch.

## 1. Choose a launch mode

| Work shape | Mode |
| --- | --- |
| One answer, diagnosis, or bounded change | ordinary task |
| One durable outcome with one coherent context | one autonomous task |
| Multiple independent directions, contested claims, expensive resources, or likely context rotation | hierarchical campaign |

Hierarchy is a control mechanism, not a default. Start with the smallest mode
that preserves independent evidence and ownership.

## 2. Freeze the campaign

Fill [the campaign template](../templates/campaign.yaml). The supervisor checks:

1. Is the outcome measurable?
2. Does every completion condition point to evidence?
3. Are hard constraints and non-goals explicit?
4. Can each initial research question change a named downstream decision?
5. Are the evaluation method and claim tiers defined before results?
6. Are mutable state and scarce resources owned by one lane at a time?
7. Are route breadth, retry/pivot, and search-reset rules configured?
8. Are independent review and extraordinary-claim triggers configured?
9. Are high-risk roles assigned the highest-capability model and lightweight
   tasks sealed by an objective verifier and escalation rule?
10. Is there one human-facing authority gateway?
11. Can the control plane be maintained without delaying first evidence?
12. Are the participant roster, direct-routing, dependency subscriptions,
    terminal notifications, role memories, and watchdog targets configured?

If a missing answer changes authority or the objective, ask the sponsor one
compact question. Delegate or test ordinary uncertainty.

One consolidated readiness review closes when concrete scientific and safety
faults are resolved. Do not create serial approval gates for reversible,
in-lease work.

## 3. Start the hierarchy

### G0 supervisor

The sponsor starts exactly one supervisor with
[prompts/supervisor.md](../prompts/supervisor.md). The supervisor freezes the
campaign and creates exactly one G1 manager. It owns the human gateway,
functional governance maintenance, G1 audit/repair/replacement, and completion.
Both use the highest available capability and reasoning effort because they
govern objectives, correction,
portfolio choices, and completion.

### G1 manager

The manager receives [prompts/manager.md](../prompts/manager.md), the campaign,
participant roster, task/dependency map, and its role memory. It owns goal
control, leases, routing directory, portfolio, and cross-task arbitration. It is
not a routine message relay. It creates no more active G2 conversations than:

```text
min(
    ready independent questions,
    configured active-lane limit,
    independent resource leases,
    manager supervision capacity
)
```

### G2 role/task conversations

Each G2 receives:

- [prompts/researcher.md](../prompts/researcher.md);
- its verified self-binding and required contact slice;
- its role-memory snapshot;
- one [task lease](../templates/task-lease.yaml);
- one current checkpoint;
- only the contracts and evidence needed for its next experiment.

Distinct lanes MUST have distinct questions or contribution responsibilities and
mutable-state ownership. A lease separates functional role, professional lens,
owned question, deliverable, and decision scope. Related work in one coherent
lane SHOULD reuse its conversation. G2 roles use the highest available capability
and reasoning effort and may invoke subagents only for bounded returned outputs.

### Contributors and reviewers

Bounded contributors receive a collaboration packet, not a campaign transcript.
Product, software, algorithm, data/statistics, mathematics, domain, operations,
safety, or security lenses are assigned only when they produce distinct
mechanisms, risks, evidence, or tests. They are not votes.
Reviewers receive [prompts/reviewer.md](../prompts/reviewer.md), the frozen
claim, evaluation contract, identities, and evidence refs. They do not receive
unnecessary proposer advocacy. Reviewers and hostile referees use the highest
available capability and reasoning effort.

Lightweight workers are launched only for tasks that pass
[the model-routing gate](model-routing.md). Give them
[prompts/lightweight-worker.md](../prompts/lightweight-worker.md), one sealed
packet, one objective verifier, and explicit escalation conditions.

## 4. Form the initial portfolio

Before committing to a favored mechanism, the manager commissions independent
idea cards. It clusters them by mechanism and chooses a portfolio that covers:

- the best-supported route;
- a mechanistically different route;
- a falsification or boundary route.

If only one route is feasible, record why and when alternatives reopen. Agent
count and repeated wording do not increase an idea's evidence weight.

## 5. Run the lifecycle

```text
launch
  -> orient
  -> independently generate routes
  -> freeze validation and experiment cards
  -> execute minimum real experiment
  -> classify result and attempt
  -> discuss only after first-pass freeze
  -> independently reproduce or challenge when due
  -> manager decision
  -> follow up, queue, retire, or rotate
  -> completion audit
```

Every completed lane turn ends with one lifecycle disposition:

| Disposition | Required state |
| --- | --- |
| `reuse` | same lane, one next action/owner and wake condition |
| `queue` | no ready safe action, scarce lease released, wake condition/target recorded |
| `retire` | evidence and reopen condition preserved, resource considered for reallocation |
| `rotate` | context/isolation reason, durable handoff, atomic lease transfer |

An idle conversation is not a retired lane. A nonterminal lane without an action
owner, future wake, pending decision, reopening subscriber, or bounded delivery
repair is governance drift. Before idle, bounded work persists its result and
sends the required terminal event to its commissioner and subscribers.

Creation, ambiguous delivery, validation-scale, and evidence-finalization
events use the corresponding section of
[operational controls](operational-controls.md); ordinary roles do not preload
that whole guide.

## 6. Event-driven management

The manager wakes only for a material management event:

- launch;
- valid result or invalidation;
- material discussion resolution or independent review;
- true blocker or challenge;
- terminal lane disposition;
- overdue declared evidence condition;
- sponsor control message;
- roster, dependency, missing-ownership, or completion-delivery change.

Peers send scoped evidence, dependency, review, discussion, handoff, and
completion events directly. The manager processes a bounded event batch,
persists decisions, verifies the campaign still has a liveness edge, sends
follow-ups once, refreshes its memory, and returns to idle. It does not poll full
child histories.

An optional recurring G0 watchdog uses
[the watchdog prompt](../prompts/watchdog.md) and
[communication/liveness rules](communication-liveness.md). It reads bounded
durable state and wakes the minimum authorized G2, G1, or G0 target set only for
a material liveness, identity, routing, or completion fault.

## 7. Finish

The manager submits a requirement-to-evidence map. The supervisor checks claim
tiers, negative and invalid evidence, review independence, unresolved dissent,
resource state, and artifact reachability.

Completion is rejected when it depends only on activity, one local success,
tests without outcome evidence, agent consensus, or an unreviewed extraordinary
claim.

If execution exposes a governance defect, preserve valid work and open one
bounded [evolution record](evolution.md). The campaign continues on compatible
routes while the smallest affected control is repaired.
