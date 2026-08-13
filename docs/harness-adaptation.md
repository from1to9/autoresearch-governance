# Harness Adaptation

The protocol is behavioral. A harness is conformant when it preserves
authority, independence, evidence lineage, recovery, and non-blocking progress;
it does not need the same tool names or product architecture as the reference
environment.

## Reference status

This repository has been tested in Codex as a reference implementation for
role-scoped prompts, multiple conversations and subagents, durable checkpoints,
direct role communication, independent review, local repository changes, and
automated validation. This is compatibility evidence, not certification of
every Codex release or guarantee that another harness provides equivalent
isolation.

Other harnesses may have a high-capability agent adapt and install the protocol
inside the user-authorized local or repository scope. The adapter agent should
read this guide, the core specification, launch guide, and validator; it should
not paste all documentation into runtime roles.

If the source is not already attached or checked out, a read-only download of
the public repository is sufficient. Do not request a credential merely to read
public artifacts. Record the source version and the authorized installation
target before changing local configuration or project files.

## Capability map

Map these logical operations to available primitives:

| Governance operation | Required behavior |
| --- | --- |
| create or reuse task | stable creation key, one owner, task-list read-back |
| participant directory | stable logical IDs, verified transport read-back, versioned roster |
| send follow-up | resolve current logical recipient; bind destination, scope, content, and idempotence |
| read result | bounded task read or durable result artifact |
| wait | event, callback, or declared manual wake; no busy polling |
| direct peer event | scoped send without mandatory manager relay; authority unchanged |
| completion notification | terminal event reaches commissioner, decision owner, and subscribers |
| liveness audit | detect missing owner/wake/delivery and wake minimum G2/G1/G0 target |
| independent lane | distinct context plus mutable-state and resource ownership |
| bounded subagent | one deliverable returned to an accountable parent |
| durable state | repository or artifact records outside transient conversation |
| checkpoint and recover | reload self-binding, role memory, C0/C1/C3, event deltas, then minimum artifacts |
| model class | strongest available for material judgment; lightweight only behind a verifier |
| review separation | proposer is not sole reproducer, critic, and adjudicator |
| external action | explicit authority boundary and read-back after mutation |

Record the actual mapping and adapter version in the campaign anchor. Keep
vendor-specific tool names in the adapter, never in the governance core.

## Autonomous installation procedure

The adapter agent uses the highest available capability and reasoning effort
because this work interprets authority and failure semantics.

1. Inventory native task, subagent, participant-directory, direct-messaging,
   persistence, event/wake, model, workspace, and verification primitives.
2. Select only the core, triggered guides, prompts, templates, and validator
   required by the target workflow.
3. Mark each logical operation as native, emulated, manual, or unavailable.
4. Choose the smallest adapter: instructions and templates first; a script only
   when a real mechanical gap exists; a new service only after repeated measured
   failure proves it necessary.
5. Install only inside declared repository or local configuration scope.
6. Preserve unrelated configuration and user work.
7. Compile role-scoped packets and map current model classes.
8. Run the conformance scenarios below.
9. Record source version, supported behavior, limitations, validation evidence,
   and rollback.
10. Begin with the smallest real campaign; do not wait for optional automation.

The adapter agent does not need approval for reversible, in-scope local edits,
configuration additions, or validation that the user has already authorized.
It stops before credentials, external publication, destructive replacement,
paid resource expansion, new external integrations, or a material scope change
unless those actions are explicitly authorized.

## Graceful degradation

| Missing primitive | Adaptation |
| --- | --- |
| scheduler or recurring task | use event wakes or a bounded manual liveness audit |
| subagents | run bounded contributions sequentially under one accountable lane |
| separate conversations | freeze independent first passes before exposure and label that context independence is not guaranteed |
| durable task IDs | maintain stable local logical IDs, verified binding epochs, and a roster |
| destination read-back | forbid automatic resend; require manual reconciliation |
| direct task messaging | persist peer events and use narrow manual or parent-assisted delivery without changing decision authority |
| resource leases | serialize mutable work and record ownership explicitly |
| model tiers | use the strongest available model for every material and adversarial role |
| cheap model | use the strongest model; lightweight routing is optional, not required |
| artifact store | use versioned repository files or another reachable immutable record |
| event API | persist compact events and wake declared recipients through the narrowest route |

An emulation must state what independence, idempotence, or durability it cannot
prove. Missing capability narrows claims; it must not be hidden by renaming a
prompt or agent.

## Conformance scenarios

An adapter is ready when it demonstrates, at proportionate scale:

1. two independent routes freeze first-pass outputs before seeing each other;
2. a bounded subagent cannot change its parent's lease or portfolio decision;
3. an ambiguous create is reconciled without starting duplicate work;
4. an ambiguous delivery is read back and never blindly sent a third time;
5. context recovery succeeds from self-binding, role memory, C0-C3, and event
   deltas without transcript replay;
6. a blocked lane releases or retains resources explicitly while another safe
   route continues;
7. a lightweight worker escalates an anomaly without interpreting it;
8. an extraordinary result is reproduced and attacked in a distinct context;
9. a sponsor stop affects its named scope immediately;
10. completion fails when required evidence or review lineage is unreachable;
11. a stale or wrong destination binding is rejected before execution and then
    repaired through roster read-back;
12. a bounded task notifies declared dependents without requiring G1 relay;
13. an all-idle nonterminal state wakes the minimum authorized G2/G1/G0 set;
14. professional lenses create distinct tests without becoming persona votes.

Also run [the repository validator](../scripts/validate.py) after installation
when the adapter copies or modifies these artifacts.

## Minimal installation prompt

```text
Adapt AutoResearch Governance to this harness.

Source artifact: <public repository URL or attached directory>.
Installation target: <authorized repository or local configuration scope>.

Use the highest available capability and reasoning effort. Work autonomously
inside the already authorized local or repository scope. Inspect native task,
subagent, participant-directory, direct-messaging, persistence, event/wake,
model, workspace, and verification primitives. Map them to
docs/harness-adaptation.md and docs/communication-liveness.md, install the smallest
reversible adapter, preserve unrelated state, and run its conformance scenarios.

Do not invent a service for a prompt-level problem. Do not request credentials,
publish externally, make destructive replacements, or expand scope without
authority. Record limitations honestly; if true independent contexts are
unavailable, freeze first passes and label the weaker independence claim.

Return the capability map, files or settings changed, validation evidence,
limitations, rollback, and the smallest campaign-ready next action.
```

For Codex-specific model and prompting behavior, prefer current
[official OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)
over frozen vendor details in this repository.
