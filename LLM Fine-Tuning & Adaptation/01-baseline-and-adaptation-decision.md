# 01 — Baseline and Adaptation Decision

Fine-tuning should be a measured engineering decision, not the default response to poor model quality.

## Decision tree

```text
Is the problem primarily missing/up-to-date knowledge?
 ├─ Yes → RAG / tool use / better retrieval
 └─ No
     ↓
Is the problem behavior, format, style, task procedure, or domain-specific mapping?
 ├─ Yes → SFT / LoRA candidate
 └─ No
     ↓
Is there a large domain corpus and a need to change language/domain representation?
 ├─ Yes → consider continued/domain-adaptive pretraining
 └─ No
     ↓
Do we have reliable preference data and a measurable behavioral target?
 ├─ Yes → consider DPO/GRPO/RL-style optimization
 └─ No → improve task definition/data/evaluation first
```

## Baselines to build first

### Baseline A — Prompting

Record the exact system prompt, model identifier/revision, decoding parameters, input template, and output schema.

### Baseline B — RAG

For knowledge-intensive tasks, compare against retrieval before training the model. The retrieval system should itself be evaluated for recall, relevance, freshness, and source attribution.

### Baseline C — Smaller/cheaper model

A domain model is not automatically better if a smaller model plus retrieval or deterministic post-processing satisfies the task.

## Adaptation matrix

| Need | Candidate approach | Main risk |
|---|---|---|
| Current external knowledge | RAG | Retrieval failure |
| Stable output format | Structured prompting / constrained decoding / SFT | Brittle formatting |
| Domain task behavior | SFT + LoRA | Overfitting |
| Domain vocabulary/knowledge in weights | Continued pretraining | Forgetting / contamination |
| Preference alignment | DPO / related methods | Preference-data quality |
| Reasoning/reward optimization | GRPO/RL-style methods | Reward hacking / complexity |
| Low-memory adaptation | QLoRA | Quantization/training compatibility |

## Experiment contract

Every experiment should declare:

```yaml
experiment_id: unique-id
base_model: exact-model-id-and-revision
task: task-name
dataset: exact-version
method: prompting|rag|sft|lora|qlora|dpo|grpo
seed: 0
max_seq_length: 2048
learning_rate: null
train_examples: null
eval_examples: null
hardware: null
software_versions: null
primary_metric: null
safety_metrics: []
latency_target_ms: null
cost_target: null
```

## Practical bottleneck: weak problem definition

If the target is not measurable, training can optimize a number while making the real system worse. Define a small, high-quality evaluation set before spending GPU time.

## Practical bottleneck: confusing knowledge with behavior

Fine-tuning can teach patterns and behaviors, but it is not a substitute for a reliable source-of-truth retrieval system when information changes frequently. For clinical systems, separate the model's learned behavior from evidence retrieval and establish explicit provenance.

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Baseline | A reference system used to measure whether a new approach improves the task. |
| Prompting | Giving instructions and context to a model without changing its trained parameters. |
| RAG | Retrieval-Augmented Generation; retrieves relevant external information and provides it to the model as context. |
| SFT | Supervised Fine-Tuning; trains on examples of desired behavior. |
| Continued pretraining | Further pretraining on domain text to adapt the model's language/domain representation. |
| DPO | Direct Preference Optimization; learns from preferred and rejected responses. |
| GRPO | Group Relative Policy Optimization; optimizes outputs using relative reward signals across groups of candidates. |
| Deterministic post-processing | Rule-based processing applied after model generation, such as schema validation or formatting. |
| Decoding parameters | Generation settings such as temperature, top-p, and maximum output tokens. |
| Provenance | Information showing where data or evidence came from and how it was used. |
| Adaptation | Any method used to make a base model better suited to a task, domain, or workflow. |
| Overfitting | When a model learns training examples too specifically and performs worse on unseen data. |
| Reward hacking | Optimizing the measured reward in an unintended way rather than achieving the real objective. |
| Experiment contract | A structured record of the exact configuration needed to reproduce and compare an experiment. |
