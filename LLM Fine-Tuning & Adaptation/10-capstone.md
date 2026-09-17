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
