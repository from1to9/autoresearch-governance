# Context Control

Conversation context is a working cache. Durable records preserve authority,
evidence, and recovery.

## C0-C4 model

| Layer | Contents | Mutation rule |
| --- | --- | --- |
| C0 campaign anchor | objective, completion, constraints, metrics, authority, policies | supervisor-authorized version only |
| C1 task lease | function/lens, question, decision scope, resources, dependencies, allowed actions | parent-issued scope epoch |
| C2 evidence and decisions | attempts, results, reviews, discussions, participant events, challenges, decisions | append-only |
| C3 checkpoint | current experiment, alternatives, blockers, communication cursor, next action, context health | replaceable, reconstructable |
| C4 conversation | messages, reasoning, command output, suggestions | transient, non-authoritative |

Precedence is authority-aware:

```text
authorized objective or constraint change
  > C0
  > applicable C1
  > current authoritative artifacts
  > C2
  > C3
  > C4
```

This does not make higher roles factually infallible. Contrary evidence creates
a scoped challenge; it does not grant the challenger broader authority.

## Minimal durable layout

An implementation may use ordinary files:

```text
campaign/
├── campaign.yaml
├── participant-roster.yaml
├── task-map.yaml
├── decisions.jsonl
├── evidence.jsonl
├── events.jsonl
├── deliveries.jsonl
├── participants/
│   └── <participant-id>/
│       └── role-memory.yaml
└── lanes/
    └── <lane-id>/
        ├── lease.yaml
        ├── checkpoint.yaml
        └── artifacts.json
```

Several logical records may share one file. Do not create a database merely to
match this diagram.

## What belongs in C2

Persist only material lineage:

- idea cards and route dispositions;
- experiment cards and results;
- attempt predecessor, novelty, class, and reopening condition;
- validation epochs and reviewer dispositions;
- frozen independent positions and material discussion;
- challenges and responses;
- manager and sponsor decisions;
- participant-binding changes and material message/completion events;
- human authority changes;
- completion and archive decisions.

Raw logs and reasoning remain behind artifact refs unless required to reproduce
a disputed result.

## What belongs in C3

The checkpoint is the current working set:

- campaign and lease hashes;
- owned question and causal edge;
- current hypothesis, mechanism family, route class, and attempt;
- latest valid evidence and quarantined evidence;
- remaining retry authority and search-reset state;
- active alternatives and retired-route reopening conditions;
- open discussion, dissent, and pending independent reviews;
- resource ownership and expected evidence condition;
- next action, owner, and wake condition;
- event cursor, required completion deliveries, and dependency subscriptions;
- a Boolean context-health vector.

Do not compress health into one score. Preserve which invariant failed.

## Message hygiene

- Send deltas and artifact refs, not repeated charters or full histories.
- Resolve logical recipients from the current roster and let scoped peers send
  directly to declared recipients/subscribers.
- Send only on material events.
- Drop duplicate events without receipt-only replies.
- Keep raw logs and large diffs in artifacts.
- A manager reads a bounded evidence sample and management deltas, not every
  child transcript or routine peer message.
- A reviewer receives a frozen review packet, not the researcher's advocacy.
- A status request does not pause authorized work.
- Evidence or safety may exceed a soft message budget once; the next message
  returns to a compact delta.

## Checkpoint events

A research lane checkpoints:

- when accepting a lease;
- before an experiment;
- after a result, invalidation, or attempt classification;
- after freezing an independent first pass;
- after a material discussion or review;
- after a direct dependency/contact change or terminal notification;
- before a pivot or manager decision;
- after compaction or recovery;
- before handoff, retirement, or rotation.

The lane also refreshes its role memory at those material boundaries and before
ending a nonterminal turn. The manager refreshes its own memory/checkpoint after
roster/dependency, portfolio, allocation, pivot, claim-tier, discussion, review,
escalation, and completion decisions.

## Recovery

Use [prompts/recovery.md](../prompts/recovery.md).

After compaction, restart, or handoff:

1. Verify the participant's current roster self-binding and contact slice.
2. Read its role memory and event cursor.
3. Verify C0 identity and C1 scope epoch.
4. Read the latest C3 checkpoint.
5. Read relevant C2/events after the cursor.
6. Resolve only artifacts needed for the next action.
7. Recompute context health and write role memory plus a recovery checkpoint.

Do not begin with the full transcript. Open older context only to resolve a
named evidence conflict.

## Rotation

Rotate a conversation only when:

- an independent outcome must run concurrently;
- a resource, security, or mutable-state boundary requires isolation;
- bounded C0-C3 recovery cannot restore the lease and decision lineage;
- drift repeats after a specific correction;
- a phase is materially incompatible with the existing context.

A completed turn, failed hypothesis, large transcript, or desire for a fresh
prompt is not sufficient by itself. Rotation preserves predecessor/successor
IDs and transfers one lease atomically.

## Context budget rule

Runtime roles load only:

```text
role prompt
+ current roster self-binding and contact slice
+ role memory and event cursor
+ current lease or review packet
+ current checkpoint
+ relevant C2 deltas
+ minimum evidence refs
```

If governance artifacts delay first valid evidence, reduce to the self-binding
and contact slice, role memory, campaign, lease, checkpoint, relevant event
deltas, and next-action artifacts.

Task creation keys, idempotent delivery records, validation epochs, and atomic
lease transfer are event-specific state defined in
[operational controls](operational-controls.md). Load those sections only when
the event occurs.

Roster, direct-routing, terminal-notification, watchdog, and role-memory details
live in [communication and liveness](communication-liveness.md).
