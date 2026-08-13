# Recovery prompt

```text
Recover task <task-id> from durable campaign state.

Use the highest available capability and reasoning effort because recovery must
detect drift, conflicting state, and invalid continuation rather than merely
summarize recent text.

Read, in order:
1. current roster self-binding and required contact slice
2. role memory and event cursor
3. C0 campaign anchor and current C1 lease/scope epoch
4. latest C3 checkpoint
5. relevant post-cursor C2/events
6. only artifacts required for the declared next action

Verify objective, scope, causal edge, mechanism and route class, attempt
predecessor and novelty, failure class, retry/pivot/search-reset state, active
alternatives, open dissent, pending independent reviews, resource ownership,
identity binding, dependencies, required deliveries, evidence refs, and next
action/wake condition.

Classify new messages before applying them. Exclude quarantined evidence. Refresh
role memory and write a recovery checkpoint, then continue only inside the lease.

Do not reconstruct the goal from recent chat, replay the full transcript, or
read the full governance repository unless resolving one named policy conflict.
```
