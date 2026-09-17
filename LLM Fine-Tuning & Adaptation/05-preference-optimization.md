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

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Preference optimization | Training that makes a model favor outputs judged better according to preferences or rewards. |
| Preference pair | One prompt with a preferred (`chosen`) response and a less-preferred (`rejected`) response. |
| DPO | Direct Preference Optimization; a method for learning from preference pairs without the full classic RLHF loop. |
| GRPO | Group Relative Policy Optimization; uses relative rewards among groups of candidate outputs. |
| RLHF | Reinforcement Learning from Human Feedback; uses human preference information to guide model behavior. |
| Reward | A numerical signal representing how desirable an output is according to a defined objective. |
| Reward function | The procedure that converts an output into a reward value. |
| Reward model | A model trained to predict human preference or quality and provide a reward signal. |
| Policy | In reinforcement learning, the model's behavior rule for generating actions; here, token/output generation. |
| Policy optimization | Updating the model so its generated outputs receive higher rewards under the chosen objective. |
| Reward hacking | Finding unintended ways to increase the measured reward without achieving the real goal. |
| Preference-label noise | Inconsistency or error in human preference judgments. |
| Mode collapse | A reduction in output diversity where the model produces overly similar responses. |
| Over-optimization | Improving the training objective while degrading broader quality, safety, or generalization. |
| Behavioral gap | A specific, measurable behavior that the current model fails to achieve reliably. |
| Anti-hacking check | An independent test designed to detect whether a reward can be increased through undesirable shortcuts. |
