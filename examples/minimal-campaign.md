# Minimal campaign example

This synthetic example shows the protocol without depending on a particular
agent platform or research domain.

## Objective

Reduce the median runtime of a deterministic solver by at least 20% while
preserving exact output equivalence and keeping peak memory within the existing
guardrail.

## Initial route slate

| Route | Mechanism | Falsifier |
| --- | --- | --- |
| Leading | cache repeated intermediate results | cache hit rate stays low or runtime does not improve |
| Orthogonal | change data layout to reduce allocation | allocation falls but runtime does not |
| Falsification | rerun the baseline under matched warm-up and I/O isolation | apparent gain disappears under a fair baseline |

The three idea cards are frozen independently before the manager shares the
favored caching explanation.

## Lane leases

- Lane A owns caching experiments and one isolated workspace.
- Lane B owns data-layout experiments and another workspace.
- Reviewer C owns matched-baseline validation and no implementation authority.

Each lane reports only material events and artifact refs.

The supervisor, manager, research lanes, reproducer, and hostile referee use the
highest-capability model at its highest reasoning effort. A lightweight worker
only collects fixed runtime fields and executes the preregistered summary
statistics; its schema validator must pass, and any anomaly escalates to the
manager without interpretation.

## Failure continuity

The first caching attempt fails because keys are unstable. It is classified
`implementation_fault`, does not enter scientific evidence, and is repaired.
The second attempt activates the cache but improves runtime by only 3%. It is
classified `hypothesis_refuted` for the registered effect boundary. A third
attempt that merely increases cache size is rejected because it has no material
novelty.

The manager preserves the negative result, releases that lane's resource, and
continues the orthogonal route rather than terminating the objective or
restarting caching under a new conversation.

## Discussion and review

The data-layout lane reports a 27% improvement. Before discussion:

1. the lane freezes its result;
2. an independent reproducer freezes a 25% result;
3. a hostile referee finds that one input family regresses by 8%;
4. the original investigator answers with boundary evidence;
5. the manager adjudicates the claim as valid only for the eligible input
   family and commissions a targeted guardrail repair.

The synthesizer reports both the improvement and the unresolved generalization
limit. It does not rewrite the result as a universal 27% gain.

## Context recovery

After compaction, the data-layout lane reads only:

- campaign hash and objective;
- its current lease;
- its latest checkpoint;
- the result, reproduction, referee, and manager-decision records;
- artifacts required for the guardrail repair.

It does not replay the brainstorming or full discussion transcript.

## Governance learning

The first review cycle repeatedly asks the data-layout lane for approval-only
messages even though its lease already authorizes reversible tests. The manager
preserves the ongoing experiment, records the symptom and wasted review time,
and opens one bounded governance defect. The smallest change removes the
redundant acknowledgement step and adds a scenario proving that in-lease work
continues while a review is open.

An independent reviewer checks that the change does not weaken claim review or
expand external authority. The next cycle closes faster without changing
evidence quality, so the prospective rule is retained. If that signal had not
improved, the change would have been reverted.
