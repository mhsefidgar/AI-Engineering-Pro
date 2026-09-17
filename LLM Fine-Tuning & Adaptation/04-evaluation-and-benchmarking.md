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
 metrics/tests     human evaluation    adversarial slices
```

## Build a golden evaluation set

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

Do not rely on one overlap metric. Combine automated measures with factuality, completeness, omission, contradiction, and human evaluation.

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
Human evaluation metric:
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

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Evaluation | Measuring how well a model or system performs against predefined criteria. |
| Benchmark | A repeatable dataset and protocol used to compare systems. |
| Golden evaluation set | A carefully reviewed, versioned evaluation set treated as a controlled reference. |
| Precision | Of the items predicted positive, the fraction that are actually positive. |
| Recall | Of the relevant positive items, the fraction the system successfully finds. |
| F1 | The harmonic mean of precision and recall. |
| AUROC | Area under the receiver operating characteristic curve; summarizes ranking performance across thresholds. |
| AUPRC | Area under the precision-recall curve; often informative for imbalanced classification tasks. |
| Calibration | How closely predicted confidence corresponds to actual correctness or event frequency. |
| Factuality | Whether generated content is supported by the input or reliable evidence. |
| Hallucination | Generated information that is unsupported, fabricated, or inconsistent with available evidence. |
| Groundedness | How well an answer is supported by retrieved or provided evidence. |
| Recall@k | Whether a relevant item appears among the top k retrieved results. |
| MRR | Mean Reciprocal Rank; rewards relevant results appearing near the top of a ranked list. |
| NDCG | Normalized Discounted Cumulative Gain; evaluates ranking quality while weighting higher-ranked results more heavily. |
| Error taxonomy | A defined set of categories used to classify failures consistently. |
| Regression test | A test that checks whether a change unintentionally breaks previously working behavior. |
| Distribution shift | A meaningful difference between development/evaluation data and the data encountered later. |
| Adversarial case | An input intentionally designed to expose weaknesses or unsafe behavior. |
| Inter-rater agreement | A measure of how consistently multiple human reviewers judge the same examples. |
| Severity-weighted error | Error analysis that considers the impact of an error, not just how often it occurs. |
