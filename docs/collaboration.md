# Collaboration, Discussion, and Review

Multiple agents create value only when they contribute independent information.
This guide prevents parallel work from collapsing into duplicated effort,
groupthink, or a vote.

## Contribution roles

| Role | Question it answers | Output |
| --- | --- | --- |
| Lead investigator | Can this mechanism work? | experiments, evidence, recommendation |
| Idea scout | What distinct mechanisms are plausible? | deduplicated idea cards |
| Alternative explorer | What does an orthogonal route show? | bounded result and reopen condition |
| Reproducer | Does the frozen result recur? | independent result and deviations |
| Validation critic | Is the method allowed to support the claim? | method disposition |
| Hostile referee | What would make the strongest claim wrong? | falsifications and unresolved risks |
| Synthesizer | What has actually been established? | claim-to-evidence map and limits |

These are contribution roles, not authority levels. Team size follows
uncertainty, independence, resources, and review risk. Do not create agents to
manufacture confidence.

## Commissioning packet

Before work starts, freeze:

- contribution role;
- one owned question;
- bounded deliverable;
- input refs;
- context exposure: full lease, evidence only, or blind to favored route;
- deliberately withheld context and reason;
- independence group;
- mutable-state ownership;
- forbidden actions;
- output contract;
- model class, routing reason, and verifier;
- automatic escalation conditions;
- stop or due condition;
- discussion route;
- decision owner.

Independence never permits hiding safety rules, constraints, estimands, or
inputs required for reproducibility. Blindness removes advocacy and anchoring,
not the evidence contract.

## Discussion protocol

### 1. Independent first pass

Idea scouts, alternative explorers, reproducers, and reviewers freeze their
initial output before reading peer advocacy whenever possible. This preserves
real diversity and makes later convergence auditable.

### 2. Structured exchange

Open one bounded discussion record containing:

- one disputed question;
- frozen position refs;
- claims and counterclaims;
- evidence refs;
- the smallest discriminating test;
- unresolved dissent;
- adjudicator and close condition.

Participants may question evidence. They may not retask peers, change leases,
or turn direct messages into authority.

### 3. Adversarial pass

A fresh reviewer attacks the strongest surviving claim and the evaluator. The
review seeks decisive counterexamples, leakage, alternative explanations,
boundary failures, and unjustified generalization.

### 4. Adjudication

The named manager or supervisor maps evidence to a predeclared decision. It may
disagree with every contributor. It may not substitute rank, confidence,
consensus, or user enthusiasm for missing evidence.

### 5. Synthesis

The synthesizer reports accepted, negative, invalid, and unresolved evidence.
It cannot change dispositions, strengthen claim tiers, or omit material dissent.

Use [templates/discussion.yaml](../templates/discussion.yaml).

## Failure-aware collaboration

Negative exploration maps the search space. Preserve:

- the exact mechanism tested;
- whether it activated;
- whether the method was valid;
- the evidence boundary;
- why it was retired;
- what evidence would reopen it.

Repeated work is allowed only for a named repair, registered replication, new
mechanism, new justified boundary, or new evidence. A new agent or conversation
does not itself create novelty.

When retries are exhausted, the manager conducts a pivot review. If the search
space appears empty but the objective remains authorized, it commissions a
fresh search-reset group using the objective, constraints, negative evidence,
and unresolved causal gaps while withholding the failed route's advocacy.

## Extraordinary claims

Treat a result as extraordinary when it is implausibly strong, unexpectedly
clean, unusually broad, contrary to robust prior evidence, or likely to support
a broad novelty statement.

Required separation:

```text
proposer -> independent reproducer -> hostile referee -> decision owner
                                              -> synthesizer after decision
```

The proposer may answer objections but cannot close them. Failed reproduction
or unresolved decisive objections narrow or quarantine the claim.

## Challenges

Any role may submit a challenge with:

- disputed action;
- contradicted factual premise or authority conflict;
- evidence refs;
- risk if executed;
- safe work continuing;
- requested resolution: withdraw, revise, test, reaffirm with evidence, or
  escalate;
- response condition.

A challenge is not a veto over unrelated work and does not grant new authority.
An explicit stop is applied first; its rationale may be challenged afterward.

## Decision rule

Every material decision names:

- the owner;
- evidence used;
- alternatives considered;
- review independence;
- dissent;
- claim tier;
- next action and next review condition.

The number of agents on each side is deliberately absent.

## Non-blocking review contract

A review has one owner, disputed scope, evidence packet, due or wake condition,
and close rule. It blocks only the claim or costly action that depends on it.
Exploration, negative-result preservation, and unrelated safe lanes continue.

A reviewer either identifies a concrete material fault, requests the smallest
discriminating evidence, narrows the claim, or closes. Review does not remain
open merely because more criticism is imaginable, and it is not a routine
approval gate for reversible in-lease work.

## Model assignment

Lead research, correction, reproduction design, validation criticism, hostile
review, adjudication, and synthesis require the highest available capability
and reasoning effort. A lightweight contributor may only monitor declared
fields, extract referenced facts, compute preregistered statistics, or implement
a small sealed change with objective tests. See
[model routing](model-routing.md).
