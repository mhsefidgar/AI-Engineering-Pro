# LLM Fine-Tuning & Adaptation — Master Plan

## Objective

Build a portfolio-quality, production-oriented learning path that demonstrates the capabilities expected from an AI/ML Engineer specializing in LLM fine-tuning and adaptation for high-stakes domain applications.

The plan deliberately treats fine-tuning as one tool in a larger adaptation decision. Every project should answer: **Why this adaptation method, why this data, how do we know it works, and how do we operate it safely?**

## Phase 0 — Baseline and problem framing

1. Define the task and success criteria.
2. Establish a prompting-only baseline.
3. Establish a RAG baseline when external/domain knowledge is required.
4. Define latency, cost, context-length, privacy, and deployment constraints.
5. Define an evaluation set before training.

Deliverable: `01-baseline-and-adaptation-decision.md`.

## Phase 1 — Data engineering

1. Identify data sources and ownership.
2. Define a schema for instruction/input/output examples.
3. Normalize clinical terminology and document formats.
4. Remove duplicates and near-duplicates.
5. Detect leakage between train/validation/test.
6. Apply appropriate de-identification/privacy controls.
7. Create deterministic train/validation/test manifests.
8. Version data and record provenance.
9. Build automated data-quality checks.

Deliverable: reproducible data pipeline plus a data card.

## Phase 2 — Supervised fine-tuning

1. Select a compatible open-weight model.
2. Start with a small representative dataset.
3. Implement SFT with Hugging Face Transformers/TRL.
4. Track loss, validation behavior, throughput, memory, and checkpoints.
5. Compare full fine-tuning feasibility with parameter-efficient adaptation.
6. Add reproducibility metadata: model revision, tokenizer, dataset revision, seed, hyperparameters, hardware, and software versions.

Deliverable: first reproducible SFT experiment.

## Phase 3 — LoRA / QLoRA

1. Explain low-rank adapters and where they are injected.
2. Select target modules appropriate to the architecture.
3. Tune rank, alpha, dropout, learning rate, batch size, gradient accumulation, and sequence length.
4. Use 4-bit quantization for memory-constrained QLoRA experiments where appropriate.
5. Measure quality against GPU memory, training time, and inference cost.
6. Save adapters separately from the base model.
7. Test adapter merge/unmerge behavior and serving compatibility.

Deliverable: LoRA/QLoRA benchmark and adapter artifact.

## Phase 4 — Evaluation and benchmarking

Evaluate at four levels:

### Task quality
- Exact/structured-match metrics where applicable
- Precision, recall, F1, AUROC/AUPRC where applicable
- ROUGE/BERTScore or equivalent only when appropriate to the task
- Extraction validity and schema adherence

### Generative quality
- Factuality
- Hallucination rate
- Instruction following
- Completeness
- Citation/evidence correctness for grounded tasks

### Robustness and safety
- Distribution shift
- Ambiguous inputs
- Long inputs
- Adversarial/prompt-injection-like inputs
- Refusal and uncertainty behavior
- Bias/fairness slices

### Human/domain evaluation
- Blind review by qualified domain experts where required
- Inter-rater agreement
- Error taxonomy
- Severity-weighted error analysis

Deliverable: evaluation report with a fixed benchmark set and regression thresholds.

## Phase 5 — Preference optimization

Study in this order:

1. SFT as the behavioral foundation.
2. DPO for preference-pair optimization.
3. GRPO and related policy-optimization methods when the task and reward structure justify them.
4. RLHF concepts: reward models, preference collection, policy optimization, and operational complexity.

Do not introduce RL-style optimization merely because it is available. Demonstrate a concrete failure mode that preference optimization addresses.

Deliverable: one controlled comparison showing whether preference optimization changes a measurable target.

## Phase 6 — Inference optimization

1. Export the trained artifact.
2. Test standard Transformers inference.
3. Serve with vLLM where appropriate.
4. Benchmark latency, throughput, concurrency, GPU memory, and token utilization.
5. Evaluate quantization and KV-cache effects.
6. Test batching and streaming.
7. Establish timeout, cancellation, retry, and overload behavior.

Deliverable: reproducible inference benchmark and deployment configuration.

## Phase 7 — MLOps

Implement:

- Git-based code versioning
- Dataset versioning
- Model/adaptor versioning
- Experiment tracking with MLflow or Weights & Biases
- Automated tests
- CI pipeline
- Container image
- Reproducible training job
- Model registry/promotion process
- Deployment configuration
- Monitoring and alerting
- Rollback procedure

Deliverable: training-to-serving pipeline.

## Phase 8 — Production monitoring

Track:

- Request volume
- Input/output token counts
- Latency percentiles
- GPU utilization/memory
- Error and timeout rates
- Model/version distribution
- Task-quality samples
- Data distribution drift
- Output safety/quality signals
- Human feedback
- Cost per request/task

Create explicit thresholds and escalation procedures.

## Phase 9 — Medical/regulated AI controls

For synthetic/de-identified demonstrations, document the controls that would be required in a real environment:

- PHI/PII handling
- Access control
- Encryption
- Data minimization
- Audit logging
- Retention/deletion
- Vendor/data-processing review
- Human oversight
- Model card and risk documentation
- Clinical validation boundaries

The repository must not contain real patient data.

## Phase 10 — Capstone

Build:

```text
Synthetic / de-identified clinical data
          ↓
Data validation + privacy checks
          ↓
Task dataset + fixed evaluation set
          ↓
Prompt/RAG baseline
          ↓
SFT baseline
          ↓
LoRA / QLoRA
          ↓
Evaluation + error analysis
          ↓
Model/adaptor registry
          ↓
vLLM serving
          ↓
API + monitoring
          ↓
Human/domain feedback
          ↓
Controlled retraining
```

The final report must explain not only the best-performing configuration, but also its failure modes, resource requirements, and operational boundaries.

## Suggested folder structure

```text
LLM Fine-Tuning & Adaptation/
├── 00-PLAN.md
├── 01-baseline-and-adaptation-decision.md
├── 02-data-engineering-and-privacy.md
├── 03-sft-fundamentals.md
├── 04-lora-qlora.md
├── 05-evaluation-and-benchmarking.md
├── 06-preference-optimization.md
├── 07-inference-and-serving.md
├── 08-mlops-and-monitoring.md
├── 09-medical-ai-responsible-engineering.md
├── 10-bottlenecks-and-troubleshooting.md
├── 11-capstone.md
├── references.md
└── labs/
    ├── 01_data_quality/
    ├── 02_sft/
    ├── 03_lora/
    ├── 04_qlora/
    ├── 05_evaluation/
    ├── 06_preference_optimization/
    ├── 07_vllm/
    └── 08_mlops/
```

## Definition of done

A candidate completing this path should be able to explain and demonstrate:

- When **not** to fine-tune
- How to prepare a reliable domain dataset
- How SFT differs from continued pretraining and preference optimization
- How LoRA/QLoRA reduce adaptation cost
- How quantization changes memory and numerical behavior
- How to design a leakage-resistant evaluation set
- How to diagnose overfitting and catastrophic forgetting
- How to benchmark quality/cost/latency trade-offs
- How to serve and monitor the resulting model
- How to handle sensitive clinical data safely
- How to communicate uncertainty and limitations to domain experts
