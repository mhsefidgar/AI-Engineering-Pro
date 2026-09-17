# LLM Fine-Tuning & Adaptation — Master Plan

## Objective

Build a portfolio-quality, production-oriented learning path that demonstrates the capabilities expected from an AI/ML Engineer specializing in LLM fine-tuning and adaptation for high-stakes domain applications.

The plan deliberately treats fine-tuning as one tool in a larger adaptation decision. Every project should answer: **Why this adaptation method, why this data, how do we know it works, and how do we operate it safely?**

## Terminology convention

Use canonical ML/LLM terminology and define it once before using it as shorthand. Prefer **adapter** over the ambiguous spelling “adaptor” throughout this section. Use **evaluation set** or **golden evaluation set** when referring to a controlled reference set, and define the exact unit when discussing cost or success metrics.

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
- Model/adapter versioning
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
- Unit cost per explicitly defined unit of work

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
Model/adapter registry
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

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Baseline | A reference system used to measure whether a new approach actually improves the task. |
| Problem framing | Clearly defining the task, users, constraints, risks, and measurable success criteria before implementation. |
| RAG | Retrieval-Augmented Generation; retrieves external information and supplies it to the model as context. |
| SFT | Supervised Fine-Tuning; training a model on examples of desired behavior. |
| LoRA | Low-Rank Adaptation; a parameter-efficient method that learns small adapter updates instead of updating all model weights. |
| QLoRA | LoRA combined with low-bit loading of the base model to reduce training memory. |
| Continued pretraining | Further language-model pretraining on domain text rather than task-specific instruction/output examples. |
| DPO | Direct Preference Optimization; trains from preferred vs. rejected responses to optimize behavior. |
| GRPO | Group Relative Policy Optimization; a policy-optimization approach that compares candidate outputs using a reward signal. |
| RLHF | Reinforcement Learning from Human Feedback; a family of methods using human preferences to guide model behavior. |
| Adapter | A parameter-efficient set of learned weights applied to a compatible base model. |
| Latency | How long the system takes to respond to a request or produce tokens. |
| Throughput | How much work the system can process over a unit of time, such as tokens or requests per second. |
| Context length | The amount of input/output token context a model or serving system can handle for a request. |
| Data provenance | A record of where data came from, how it was transformed, and which version was used. |
| Data leakage | Information from evaluation/test data unintentionally influencing training or model selection. |
| Model registry | A controlled place to store and promote versioned model or adapter artifacts. |
| Drift | A meaningful change in production data or behavior compared with the development/validation distribution. |
| CI/CD | Automated processes for integrating code, testing it, building artifacts, and delivering deployments. |
| PHI | Protected Health Information under applicable U.S. HIPAA rules. |
| Human oversight | Defined points where qualified people review, approve, override, or escalate model behavior. |
