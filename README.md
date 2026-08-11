# AutoResearch Governance

A compact, platform-agnostic governance protocol for long-running,
evidence-producing research performed by multiple AI conversations and
subagents.

It is designed for research programs that need more than one line of attack,
must survive context compaction, and cannot treat confidence, consensus, or
activity as evidence.

## Core loop

```text
freeze objective
    -> explore independent routes
    -> commission bounded work
    -> run real experiments
    -> freeze positions before discussion
    -> reproduce and challenge claims
    -> decide from evidence
    -> checkpoint or finish
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
2. Choose a launch mode with [docs/launch.md](docs/launch.md).
3. Fill [templates/campaign.yaml](templates/campaign.yaml).
4. Start the supervisor with [prompts/supervisor.md](prompts/supervisor.md).
5. Give every runtime role only its prompt, lease, current checkpoint, and
   referenced evidence.

Do not paste this entire repository into every agent. The launcher and an
exceptional auditor may read the full specification. Runtime roles use the
smallest packet that completely defines their action.

## Context-loading guide

| Role | Load | Do not load by default |
| --- | --- | --- |
| Sponsor or launcher | core spec, launch guide, campaign template | experiment logs |
| Supervisor | frozen campaign, manager snapshot, material decisions | child transcripts |
| Manager | manager prompt, campaign, task map, compact checkpoints | child reasoning and raw logs |
| Research lane | researcher prompt, task lease, current checkpoint, one experiment card | peer histories and full governance |
| Reviewer or referee | reviewer prompt, frozen claim, evaluation contract, evidence refs | proposer advocacy and portfolio history |
| Recovering task | recovery prompt and durable C0-C3 state | full conversation replay |

## Repository map

- [GOVERNANCE.md](GOVERNANCE.md) — normative, compact core.
- [docs/launch.md](docs/launch.md) — launch modes, gates, and lifecycle.
- [docs/context.md](docs/context.md) — C0-C4 state model and recovery.
- [docs/collaboration.md](docs/collaboration.md) — roles, discussion, dissent,
  review, and decision separation.
- [docs/model-routing.md](docs/model-routing.md) — high-capability versus
  lightweight model assignment and automatic escalation.
- [prompts/](prompts/) — role-scoped runtime prompts.
- [templates/](templates/) — minimal durable records.
- [examples/minimal-campaign.md](examples/minimal-campaign.md) — a small,
  domain-neutral example.
- [scripts/validate.py](scripts/validate.py) — dependency-free repository
  validation.

## What this is not

This repository is not an agent framework, scheduler, database, benchmark, or
claim that more agents are always better. It defines decision and evidence
boundaries that can be implemented with ordinary conversations, files, version
control, and the orchestration tools already available.

## License

[MIT](LICENSE)
