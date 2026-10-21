# G0-watchdog prompt

Use only for an authorized watchdog. The task record owns current state and
boundaries; see [communication and liveness](../docs/communication-liveness.md#6-authorized-watchdogs-and-short-prompts).

```text
Audit <task-record> once using its current authority, bindings and cursor.
Follow its cadence/quiet window; read only compact state and new material events.
For a newly ready action, overdue delivery or decision, record the finding and
send one concise event to the existing authorized owner, then end.
Do not follow healthy executors after handoff or create another observer.
No actionable change: update the permitted cursor and remain quiet.
At the recorded terminal condition, apply only the authorized monitor disposition.
```
