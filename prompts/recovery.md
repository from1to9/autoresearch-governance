# Recovery prompt

```text
Recover task <task-id> from durable campaign state.

Use the highest available capability and reasoning effort because recovery must
detect drift, conflicting state, and invalid continuation rather than merely
summarize recent text.

Read, in order:
1. C0 campaign anchor
2. current C1 task lease and scope epoch
3. latest C3 checkpoint
4. relevant C2 decisions, attempts, reviews, discussions, and challenges after
   that checkpoint
5. only artifacts required for the declared next action

Verify objective, scope, causal edge, mechanism and route class, attempt
predecessor and novelty, failure class, retry/pivot/search-reset state, active
alternatives, open dissent, pending independent reviews, resource ownership,
evidence refs, and next action.

Classify new messages before applying them. Exclude quarantined evidence. Write
a recovery checkpoint, then continue only inside the lease.

Do not reconstruct the goal from recent chat, replay the full transcript, or
read the full governance repository unless resolving one named policy conflict.
```
