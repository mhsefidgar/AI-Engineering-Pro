# 05 — Preference Optimization: DPO, GRPO, and RLHF

## Why preference optimization?

SFT teaches the model to imitate examples. Preference optimization is useful when the target is better expressed as a preference between candidate responses or as a reward signal.

## DPO

Direct Preference Optimization trains on preference pairs without requiring a separately deployed reward-model/policy optimization loop in the same way as classic RLHF.

A preference record is conceptually:

```json
{
  "prompt": "...",
  "chosen": "preferred response",
  "rejected": "less preferred response"
}
```

The critical bottleneck is preference-data quality. If reviewers disagree or the rubric is inconsistent, optimization can amplify noise.

## GRPO

Group Relative Policy Optimization and related methods are useful when a task has a measurable reward structure and candidate outputs can be compared within groups. The reward design becomes a major engineering component.

Before using GRPO, define:

- Reward function
- Reward scale
- Validity constraints
- Anti-hacking checks
- Evaluation set independent of reward optimization

## RLHF

Classic RLHF generally involves preference collection, a reward model, and policy optimization. It introduces more moving parts and operational complexity than SFT or DPO.

## Practical progression

```text
SFT
 ↓
Identify a measurable behavioral gap
 ↓
Collect high-quality preference data
 ↓
DPO experiment
 ↓
If a reward structure genuinely exists:
GRPO / RL-style experiment
 ↓
Safety + regression evaluation
```

## Failure modes

- Reward hacking
- Preference-label noise
- Over-optimization
- Reduced factuality while preference score rises
- Mode collapse or reduced diversity
- Benchmark overfitting
- Unintended style changes

The evaluation suite must contain independent quality and safety metrics so that preference optimization cannot define its own success criteria.
