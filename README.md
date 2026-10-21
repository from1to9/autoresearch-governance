# AutoResearch Governance

A compact, platform-agnostic governance protocol for long-running,
evidence-producing research performed by multiple AI conversations and
subagents.

It is designed for research programs that need more than one line of attack,
must survive context compaction, and cannot treat confidence, consensus, or
activity as evidence.

For ordinary bounded work, use an ordinary task. This protocol adds only the
ownership, independence and continuity that the requested outcome needs. Prefer
the simplest sound design, reuse sufficient evidence and stop checking once the
result is established. Do not build a governance project around routine work.

## Core loop

```text
freeze objective
    -> explore independent routes
    -> commission bounded work
    -> run real experiments
    -> freeze positions before discussion
    -> reproduce and challenge claims
    -> decide from evidence
    -> checkpoint, finish, or repair an observed governance defect
```

The protocol separates:

- goals and authority from factual hypotheses;
- persistent research conversations from bounded subagents;
- proposing, reproducing, criticizing, deciding, and synthesizing;
- durable state from disposable conversation context;
- failed hypotheses from invalid experiments;
- useful persistence from unchanged retries.

## Five-minute start

1. Read [GOVERNANCE.md](GOVERNANCE.md).
2. If needed, let a high-capability agent map and install the smallest local
   adapter with [docs/harness-adaptation.md](docs/harness-adaptation.md).
3. Choose a launch mode with [docs/launch.md](docs/launch.md).
4. Record the scope and evidence boundary, using
   [templates/campaign.yaml](templates/campaign.yaml) where useful.
5. Reuse authorized roles and bind required participants through
   [the roster](templates/participant-roster.yaml). Use
   [the supervisor prompt](prompts/supervisor.md) when that responsibility is needed.
6. Give every runtime role only its prompt, self-binding/contact slice, role
   memory, lease, current checkpoint, and referenced evidence.

Do not paste this entire repository into every agent. The launcher and an
exceptional auditor may read the full specification. Runtime roles use the
smallest packet that completely defines their action.

## Context-loading guide

| Role | Load | Do not load by default |
| --- | --- | --- |
| Sponsor or launcher | core spec, launch guide, campaign template | experiment logs |
| G0 supervisor | own memory, frozen campaign, verified G1 binding, manager snapshot | child transcripts |
| G0 watchdog | short prompt, task-record pointer, cursor and new triggered events | full roster and transcripts |
| G1 manager | own memory, campaign, roster/task/dependency maps, compact checkpoints | child reasoning and raw logs |
| G2 role/task | own binding/contact slice and memory, task lease, checkpoint, one experiment card | unrelated roster and peer histories |
| Reviewer or referee | reviewer prompt, frozen claim, evaluation contract, evidence refs | proposer advocacy and portfolio history |
| Recovering task | recovery prompt, self-binding, role memory, durable C0-C3 and event deltas | full conversation replay |

## Repository map

- [GOVERNANCE.md](GOVERNANCE.md) — normative, compact core.
- [docs/launch.md](docs/launch.md) — launch modes, gates, and lifecycle.
- [docs/context.md](docs/context.md) — C0-C4 state model and recovery.
- [docs/communication-liveness.md](docs/communication-liveness.md) — verified
  participant identity, direct routing, completion delivery, watchdog wakeups,
  and role-owned memory.
- [docs/collaboration.md](docs/collaboration.md) — roles, discussion, dissent,
  review, and decision separation.
- [docs/model-routing.md](docs/model-routing.md) — high-capability versus
  lightweight model assignment and automatic escalation.
- [docs/operational-controls.md](docs/operational-controls.md) — event-loaded
  field controls for identity, delivery, validation, progress, and closure.
- [docs/harness-adaptation.md](docs/harness-adaptation.md) — behavior-level
  mapping and autonomous installation for Codex or another agent harness.
- [docs/evolution.md](docs/evolution.md) — evidence-triggered self-learning,
  prospective migration, evaluation, and rollback.
- [prompts/](prompts/) — role-scoped runtime prompts.
- [templates/](templates/) — minimal durable records.
- [examples/minimal-campaign.md](examples/minimal-campaign.md) — a small,
  domain-neutral example.
- [scripts/validate.py](scripts/validate.py) — dependency-free repository
  validation.

## Scope of reusable guidance

Keep project mechanics in their repository and current host/run state in local
records. Promote a lesson here only when its mechanism transfers across domains,
work units, storage systems and harnesses. Maintain one canonical rule with short
pointers. Recurring prompts reference task state instead of accumulating history.

## Reference implementation status

The protocol has been tested in Codex for role-scoped context, multiple
conversations and subagents, direct role communication, independent review,
durable recovery, repository editing, and automated validation. The repository
validator also runs in GitHub Actions. This is reference compatibility evidence,
not certification of every Codex release or of other harnesses.

For another harness, give a high-capability agent the
[adaptation guide](docs/harness-adaptation.md). It may autonomously install the
smallest reversible adapter inside already authorized local or repository
scope, run the conformance scenarios, and record any weaker guarantees. It
must not invent missing independence, persistence, or idempotence.

## What this is not

This repository is not an agent framework, scheduler, database, benchmark, or
claim that more agents are always better. It defines decision and evidence
boundaries that can be implemented with ordinary conversations, files, version
control, and the orchestration tools already available.

## License

[MIT](LICENSE)
