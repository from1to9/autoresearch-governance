# Launch and Lifecycle

This guide turns the core specification into a minimal executable campaign.

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

If a missing answer changes authority or the objective, ask the sponsor one
compact question. Delegate or test ordinary uncertainty.

## 3. Start the hierarchy

### Supervisor

The sponsor starts exactly one supervisor with
[prompts/supervisor.md](../prompts/supervisor.md). The supervisor freezes the
campaign and creates exactly one manager. Both use the highest available
capability and reasoning effort because they govern objectives, correction,
portfolio choices, and completion.

### Manager

The manager receives [prompts/manager.md](../prompts/manager.md), the campaign,
and the task map. It creates no more active research lanes than:

```text
min(
    ready independent questions,
    configured active-lane limit,
    independent resource leases,
    manager supervision capacity
)
```

### Research lanes

Each lane receives:

- [prompts/researcher.md](../prompts/researcher.md);
- one [task lease](../templates/task-lease.yaml);
- one current checkpoint;
- only the contracts and evidence needed for its next experiment.

Distinct lanes MUST have distinct questions and mutable-state ownership. Related
work in one coherent lane SHOULD reuse its conversation. Research lanes use the
highest available capability and reasoning effort.

### Contributors and reviewers

Bounded contributors receive a collaboration packet, not a campaign transcript.
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
| `reuse` | same lane, one next action and wake condition |
| `queue` | no ready safe action, scarce lease released, wake condition recorded |
| `retire` | evidence and reopen condition preserved, resource considered for reallocation |
| `rotate` | context/isolation reason, durable handoff, atomic lease transfer |

An idle conversation is not a retired lane. A nonterminal lane without a next
owner is governance drift.

## 6. Event-driven management

The manager wakes only for a material event:

- launch;
- valid result or invalidation;
- material discussion resolution or independent review;
- true blocker or challenge;
- terminal lane disposition;
- overdue declared evidence condition;
- sponsor control message.

It processes a bounded event batch, persists decisions, sends follow-ups once,
and returns to idle. It does not poll full child histories.

## 7. Finish

The manager submits a requirement-to-evidence map. The supervisor checks claim
tiers, negative and invalid evidence, review independence, unresolved dissent,
resource state, and artifact reachability.

Completion is rejected when it depends only on activity, one local success,
tests without outcome evidence, agent consensus, or an unreviewed extraordinary
claim.
