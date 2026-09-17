# 07 — MLOps, Monitoring, and Continuous Improvement

## Lifecycle

```text
Data version
   ↓
Experiment
   ↓
Evaluation
   ↓
Model/adaptor registry
   ↓
Staging
   ↓
Automated validation
   ↓
Production
   ↓
Monitoring
   ↓
Feedback / drift
   ↓
New dataset version
```

## Experiment tracking

Record:

- Git commit
- Dataset version
- Model revision
- Training configuration
- Hardware
- Runtime/package versions
- Metrics
- Evaluation artifacts
- Checkpoint/adaptor location

MLflow or Weights & Biases can provide the experiment-tracking layer; the repository should keep the experiment schema portable enough to migrate tools.

## CI/CD gates

Before deployment:

1. Unit tests
2. Data validation tests
3. Training/configuration smoke test
4. Evaluation regression test
5. Safety/critical-case test
6. Container build
7. Serving smoke test
8. Load/latency test

## Monitoring

### Infrastructure

- CPU/GPU utilization
- GPU memory
- Request rate
- Queue depth
- Latency percentiles
- Errors/timeouts

### Model behavior

- Task-quality samples
- Structured-output validity
- Abstention/refusal behavior
- Hallucination/factuality signals where measurable
- Drift in input distributions
- Drift in output distributions

### Cost

- Input tokens
- Output tokens
- GPU seconds
- Cost per request/task
- Cost by model/version

## Drift

Monitor changes in the workload, not only raw feature statistics. A clinically relevant change in document type or task distribution can be more important than a generic embedding-distance alert.

Drift should trigger investigation, not automatic retraining by default.

## Feedback loop

```text
Production errors
      ↓
Error taxonomy
      ↓
Root-cause analysis
      ↓
Data correction / retrieval correction / prompt correction / model correction
      ↓
New experiment
      ↓
Fixed benchmark
      ↓
Controlled deployment
```

## Rollback

Every deployment must identify:

- Previous model/adaptor version
- Container image
- Configuration
- Dataset/evaluation revision
- Rollback command/procedure

Do not make a model artifact immutable only in theory; test the rollback path.
