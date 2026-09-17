# 10 — End-to-End Capstone

## Project

Build a domain-specific LLM adaptation service using synthetic/de-identified data. The system should demonstrate the complete lifecycle expected from an AI/ML Engineer.

## Target task

Choose one:

- Document summarization
- Structured information extraction
- Classification
- Terminology normalization
- Evidence-grounded question answering

Start with one task; add a second only after the first has a stable evaluation suite.

## Architecture

```text
                 ┌─────────────────────┐
                 │ Synthetic / safe data│
                 └──────────┬──────────┘
                            ↓
                    Data validation
                            ↓
                 ┌──────────┴──────────┐
                 ↓                     ↓
             Train set             Eval set
                 ↓                     │
          SFT / LoRA / QLoRA           │
                 ↓                     │
             Model adapter             │
                 └──────────┬──────────┘
                            ↓
                     Benchmark suite
                            ↓
                    Model registry
                            ↓
                      vLLM serving
                            ↓
                         API
                            ↓
                Monitoring + feedback
```

## Required experiments

### Experiment 1 — Prompt baseline

Measure quality, latency, and cost.

### Experiment 2 — RAG baseline

If the task requires external knowledge, establish retrieval quality and grounded generation.

### Experiment 3 — SFT

Train the smallest practical model first.

### Experiment 4 — LoRA

Compare quality and resource requirements with SFT.

### Experiment 5 — QLoRA

Compare memory and throughput under constrained GPU resources.

### Experiment 6 — Preference optimization

Only if a clear preference signal exists. Compare DPO or another justified method against the SFT/LoRA baseline.

### Experiment 7 — Serving

Serve the selected artifact and benchmark realistic concurrency.

## Deliverables

```text
README.md
architecture.md
data-card.md
model-card.md
evaluation-report.md
benchmark-report.md
risk-register.md
experiments/
training/
evaluation/
serving/
monitoring/
```

## Hiring-signal questions the project should answer

- Why did you fine-tune instead of using RAG?
- Why LoRA/QLoRA instead of full fine-tuning?
- How did you prevent leakage?
- How did you choose the evaluation set?
- Which errors matter most?
- How much GPU memory did training require?
- What was the throughput/latency trade-off?
- How does quantization affect quality?
- How do you detect drift?
- What triggers retraining?
- How do you roll back a bad model?
- How do you keep sensitive data out of logs and artifacts?
- How do domain experts participate in validation?

## Final success criteria

The capstone is complete when the repository can reproduce the data-to-model-to-serving pipeline from versioned configuration, produce a benchmark report, expose the model through a controlled inference service, and explain known limitations and failure modes.

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Capstone | A final project that combines the concepts learned across the preceding sections into one end-to-end system. |
| Domain-specific | Designed for a particular field, workflow, vocabulary, or task rather than general-purpose use. |
| Evidence-grounded QA | Question answering where the response is expected to be supported by retrieved or provided evidence. |
| Structured information extraction | Turning unstructured text into defined fields or records, often using a schema. |
| Architecture | The components of the system and how data flows between them. |
| Train set | Data used to update model parameters during training. |
| Eval set | Held-out examples used to measure model behavior during development or final evaluation. |
| Benchmark suite | A fixed collection of tests covering quality, safety, robustness, latency, and/or cost. |
| Model registry | A controlled system for storing and promoting versioned model or adapter artifacts. |
| API | Application Programming Interface; a defined way for software systems to communicate with the model service. |
| Concurrency | Multiple requests being processed at the same time. |
| RAG | Retrieval-Augmented Generation; retrieves external information and supplies it as context to the model. |
| Resource requirement | Hardware, memory, storage, time, or other infrastructure needed to run a workload. |
| Risk register | A maintained list of identified risks, their impact, controls, owners, and status. |
| Rollback | Returning production to a previously validated model or configuration. |
| Retraining trigger | A predefined condition that starts investigation or a new model-training cycle. |
| Versioned configuration | A saved, identifiable configuration whose exact values can be reproduced later. |
| End-to-end | Covering the complete workflow from input/data through processing, serving, and monitoring. |
