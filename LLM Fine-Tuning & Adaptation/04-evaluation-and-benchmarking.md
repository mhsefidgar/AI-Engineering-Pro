# 04 — Evaluation and Benchmarking

A fine-tuning project is incomplete without a fixed evaluation protocol.

## Evaluation stack

```text
                 Overall evaluation
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
   Task quality     Generative       Safety/robustness
       │              quality              │
       ▼                ▼                  ▼
 metrics/tests     human review       adversarial slices
```

## Build a golden set

Create a versioned evaluation set that is:

- Representative of the intended workload
- Independent from training data
- Diverse across task types and difficulty
- Explicit about expected output structure
- Reviewed for ambiguous or invalid examples

For clinical work, include domain-expert review and severity categories for errors.

## Metrics by task

### Classification

- Precision
- Recall
- F1
- AUROC/AUPRC when appropriate
- Confusion matrix
- Calibration

### Information extraction

- Entity-level precision/recall/F1
- Exact structured-output validity
- Field-level accuracy
- Critical-field error rate

### Summarization

Do not rely on one overlap metric. Combine automated measures with factuality, completeness, omission, contradiction, and human review.

### Semantic search / RAG

Evaluate retrieval separately from generation:

- Recall@k
- Precision@k
- MRR/NDCG where applicable
- Evidence relevance
- Answer groundedness

## Error taxonomy

Every failed example should be classified, for example:

```text
WRONG_FACT
MISSING_INFORMATION
UNSUPPORTED_CLAIM
WRONG_FORMAT
INSTRUCTION_FAILURE
RETRIEVAL_FAILURE
AMBIGUITY
SAFETY_FAILURE
```

Track both frequency and severity.

## Regression testing

A new model should not be accepted because its aggregate score improved if a critical safety or domain metric regressed.

Maintain:

```text
benchmark-v1
benchmark-v2
critical-cases
adversarial-cases
latency-suite
```

## Human evaluation

Use blind comparisons where practical. Define the rubric before reviewing outputs. Capture disagreement rather than silently averaging it away.

For domain experts, collect structured judgments and maintain an error taxonomy that feeds the next data iteration.

## Robustness slices

Include:

- Short vs long inputs
- Easy vs difficult cases
- Missing fields
- Contradictory information
- Rare terminology
- Distribution shift
- Noisy formatting
- Out-of-domain requests
- Prompt injection/tool misuse scenarios where relevant

## Benchmark report template

```text
Model:
Base revision:
Adapter:
Dataset revision:
Evaluation revision:

Task metric:
Safety metric:
Robustness metric:
Human score:
P95 latency:
Tokens/request:
GPU memory:
Cost/request:

Top failure modes:
1.
2.
3.

Critical regressions:

Decision rationale:
```

The purpose of evaluation is not to produce one leaderboard number. It is to establish evidence that the adapted system satisfies its intended operating requirements.
