# Distributed Training and AI Serving

## Training parallelism

### Data parallelism

Each worker processes different data while model state is synchronized.

### Tensor parallelism

A model's computation is split across accelerators.

### Pipeline parallelism

Different model stages execute on different devices.

### Sharding

Model/optimizer state can be partitioned across workers to reduce per-device memory.

The right strategy depends on model architecture, batch size, memory, interconnect, and software support.

## Communication matters

Distributed training requires synchronization. If communication is slow, adding GPUs can reduce efficiency rather than improve it.

Measure:

- scaling efficiency
- communication time
- step time
- GPU utilization
- network utilization
- synchronization stalls

## Checkpointing

For expensive jobs, checkpoints are part of reliability engineering.

Record:

```text
model weights
optimizer state
scheduler state
training step
random state where needed
configuration
code revision
data version
```

Store enough metadata to resume or reproduce the run.

## Serving topologies

### Single GPU

Simple and inexpensive when performance requirements fit.

### Multi-GPU single replica

Useful when the model does not fit on one accelerator or latency/throughput requires parallel execution.

### Replicated serving

Multiple replicas improve aggregate capacity and can improve availability, subject to model memory and scheduling constraints.

### Batch inference

Useful when latency is less important than throughput and cost efficiency.

## vLLM-style serving

Use a specialized inference server when it matches the model and workload. Benchmark real prompts and concurrency rather than assuming a generic benchmark transfers to your application.

## Serving capacity experiment

Test at increasing concurrency:

```text
1 → 2 → 4 → 8 → 16 → ...
```

Stop when latency/SLOs or error rates become unacceptable. Record tokens/sec and GPU utilization at each point.

## Senior decision framework

Choose architecture based on:

```text
model fit
+ latency target
+ throughput target
+ concurrency
+ availability
+ cost
+ operational complexity
```

Do not select a distributed architecture merely because the model is large.

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Data parallelism | Replicating model computation while splitting input data across workers. |
| Tensor parallelism | Splitting model computation across multiple accelerators. |
| Pipeline parallelism | Splitting model layers/stages across workers. |
| Sharding | Partitioning model or training state across devices/nodes. |
| Collective communication | Coordinated data exchange among distributed workers. |
| Checkpoint | Saved state that allows training to resume or be analyzed later. |
| Replica | Independent serving instance of a workload. |
| Concurrency | Number of requests/work units being processed at the same time. |
| Throughput | Work completed per unit time. |
| Scaling efficiency | Useful performance gained relative to the ideal increase in resources. |
