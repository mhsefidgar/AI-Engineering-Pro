# 08 — Practical Bottlenecks and Troubleshooting

## 1. GPU out-of-memory

Symptoms:

- CUDA OOM
- Training fails after a few steps
- Evaluation fits but training does not

Debug order:

1. Measure sequence-length distribution.
2. Reduce micro-batch size.
3. Reduce maximum sequence length.
4. Use gradient accumulation to preserve effective batch size.
5. Enable activation/gradient checkpointing where supported.
6. Reduce model size or use a quantized base.
7. Inspect unexpected tensors retained by the training loop.

## 2. Training is extremely slow

Check:

- GPU utilization
- CPU data-loader utilization
- Storage throughput
- Tokenization bottleneck
- Padding inefficiency
- Sequence packing
- Gradient accumulation
- Network access to model/data artifacts

Do not optimize GPU kernels before proving the GPU is the bottleneck.

## 3. Validation loss rises

Likely causes:

- Overfitting
- Dataset too small
- Label noise
- Distribution mismatch
- Learning rate too high
- Excessive epochs

Run an error analysis before simply changing hyperparameters.

## 4. Fine-tuned model becomes worse at general tasks

Possible causes include catastrophic forgetting, excessive update magnitude, narrow training data, or evaluation mismatch.

Mitigations to investigate:

- Lower learning rate
- Fewer epochs
- Better data diversity
- Parameter-efficient adaptation
- Mixed/general-domain examples where justified
- Retain a broad regression suite

## 5. Model follows format but loses factuality

Formatting success is not task success. Evaluate factual correctness separately from schema validity.

## 6. Model hallucinates clinical details

Do not attempt to solve every hallucination problem with more fine-tuning. Determine whether the missing capability is:

- Retrieval
- Source attribution
- Input completeness
- Uncertainty handling
- Output validation
- Deterministic post-processing
- Human review

## 7. RAG and fine-tuning are confused

RAG is primarily an information-access architecture; fine-tuning changes model parameters/adapters. They can be combined.

Example:

```text
Fine-tuned model
      +
RAG retrieval
      +
structured output validation
      ↓
application
```

## 8. Data leakage

Symptoms:

- Suspiciously high evaluation scores
- Memorized benchmark examples
- Near-identical train/test records

Use exact and near-duplicate detection, group-aware splits, and an untouched evaluation set.

## 9. Quantization changes quality

Measure quality before and after quantization. Investigate which task slices regress; aggregate averages can hide important failures.

## 10. Serving mismatch

Common causes:

- Different chat template
- Different tokenizer
- Different base model revision
- Adapter not loaded
- Incorrect quantization
- Different generation parameters

Always run a golden inference test through the same serving stack used in production.

## 11. Cost unexpectedly increases

Check:

- Output length
- Context length
- Retries
- Duplicate requests
- Concurrency strategy
- GPU under-utilization
- Model size
- Logging/storage volume

Cost optimization should be measured as cost per successful task, not only cost per token.

## 12. Evaluation score improves but users complain

Possible explanations:

- Benchmark does not represent production
- Human preferences differ from automated metric
- Critical errors are rare but severe
- Latency worsened
- Output became harder to use
- Model became overconfident

Add production-like slices and domain-expert review.

## Production incident checklist

```text
[ ] Identify model/version
[ ] Freeze relevant logs/artifacts
[ ] Reproduce on golden case
[ ] Check serving/runtime change
[ ] Check data distribution change
[ ] Check retrieval if applicable
[ ] Check latency/GPU metrics
[ ] Compare against previous model
[ ] Roll back if required
[ ] Classify root cause
[ ] Add regression test
[ ] Document corrective action
```

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| GPU OOM | GPU out-of-memory: the workload requires more GPU memory than is available. |
| Micro-batch | The number of examples processed by one device before gradients are accumulated or an update occurs. |
| Gradient accumulation | Combining gradients from several micro-batches before an optimizer update. |
| Activation checkpointing | Trading extra computation for lower memory by recomputing saved intermediate activations. |
| Tokenization | Converting text into the token IDs consumed by a language model. |
| Padding | Adding placeholder tokens so examples in a batch have compatible lengths. |
| Sequence packing | Combining multiple shorter training sequences into fuller sequences to reduce wasted padding. |
| Overfitting | Learning training patterns too specifically and losing performance on unseen data. |
| Learning rate | A training hyperparameter controlling the size of parameter updates. |
| Catastrophic forgetting | Loss of previously useful capabilities after narrow adaptation. |
| Factuality | Whether generated statements are supported by the available information. |
| Hallucination | Unsupported or fabricated generated information. |
| Source attribution | Identifying the source of evidence used to support an output. |
| Output validation | Checking generated output against rules, schemas, constraints, or other correctness checks. |
| RAG | Retrieval-Augmented Generation; retrieves external information to provide context to the model. |
| Data leakage | Unintended information flow from held-out evaluation data into training or model selection. |
| Quantization regression | A quality or behavior degradation caused by changing the model's numerical precision. |
| Serving mismatch | A difference between training/evaluation and production inference configuration that changes model behavior. |
| Root cause | The underlying reason a failure occurred, rather than only its visible symptom. |
| Golden case | A fixed, trusted test example used to quickly verify expected model behavior. |
| Cost per successful task | Operational cost measured against successfully completed tasks rather than raw tokens alone. |
