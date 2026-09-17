# Resource Sizing for AI/ML Workloads

The central skill is turning a workload into measurable resource requirements. Cloud instance selection comes after this step.

## 1. Start with the workload

Record:

```text
model = architecture + parameter count + context length
precision = training/inference precision
workload = training | fine-tuning | batch inference | online inference
micro_batch_size = per-device batch size
gradient_accumulation_steps = optimizer-update accumulation
concurrency = simultaneous requests/work units
SLOs = latency + throughput + availability targets
```

## 2. Model-weight memory: first estimate

A simple first-order estimate is:

```text
weight_memory ≈ parameter_count × bytes_per_parameter
```

Useful planning values:

| Representation | Approx. bytes/value |
|---|---:|
| FP32 | 4 |
| BF16/FP16 | 2 |
| INT8 | 1 |
| INT4 | 0.5 |

Real deployments need additional memory for runtime metadata, buffers, activations, KV cache, fragmentation, and framework overhead.

## 3. Training memory

For full fine-tuning, model weights are only one part of memory. Also account for gradients, optimizer states, activations, temporary buffers, and framework overhead.

For Adam-style optimization, a rough mental model is:

```text
training_memory ≈ weights + gradients + optimizer_states + activations + overhead
```

Do not use one universal multiplier as a production sizing rule. Precision, optimizer implementation, sharding, sequence length, batch size, checkpointing, and framework behavior change the result.

For LoRA/QLoRA, trainable optimizer state is much smaller, but the base model, activations, temporary tensors, and quantization/runtime overhead still matter.

## 4. GPU count

Start with memory feasibility:

```text
required_GPU_count ≥ total_peak_memory / usable_GPU_memory
```

Then validate compute and communication requirements.

If a model fits on one GPU but is too slow, multiple GPUs may improve throughput. If it exceeds the memory capacity of one GPU, determine whether tensor parallelism, FSDP/sharding, quantization, offloading, or a smaller model is appropriate.

## 5. Leave headroom

Never size a production GPU to exactly the theoretical minimum.

Use measured peak utilization and reserve headroom for:

- memory fragmentation
- request variability
- longer prompts
- larger batches
- software upgrades
- temporary buffers
- traffic spikes

A practical initial target is often to avoid sustained operation at the absolute hardware ceiling. The correct percentage is workload-specific and should be validated through load testing.

## 6. Sequence length is expensive

Longer context can increase activation memory during training and KV-cache usage during inference.

Therefore benchmark at realistic percentiles, not only an average prompt length.

Track:

```text
P50 input tokens
P95 input tokens
P99 input tokens
P50 output tokens
P95 output tokens
P99 output tokens
```

## 7. Inference capacity

For online inference, capacity is driven by:

```text
traffic
× input tokens
× output tokens
× concurrency
× target latency
```

Measure:

- time to first token (TTFT)
- inter-token latency
- end-to-end latency
- tokens/sec
- requests/sec
- concurrency
- GPU utilization
- GPU memory utilization
- queue depth

Do not estimate production capacity from a single interactive test.

## 8. Storage sizing

Separate capacity from throughput.

```text
capacity = datasets + model weights + checkpoints + logs + artifacts + headroom
```

But a 10 TB disk can still be too slow if training needs high sustained throughput.

For training, ask:

- How many GB must be read per minute?
- How many workers read simultaneously?
- Are files many small objects or a few large objects?
- Can data be cached locally?
- How often are checkpoints written?

## 9. Network sizing

For distributed training and large model startup, network can dominate.

A rough lower bound for transferring `D` bytes in `T` seconds is:

```text
required_bandwidth ≈ D / T
```

Convert units carefully: cloud networking is commonly advertised in bits/sec while storage throughput is commonly reported in bytes/sec.

Account for protocol overhead, contention, cross-zone traffic, and real utilization.

## 10. CPU and RAM

GPU workloads still need CPU and system RAM for:

- tokenization
- data loading
- preprocessing
- decompression
- request handling
- batching
- serialization
- networking
- model loading

A GPU that spends time waiting for CPU/data pipelines is expensive idle capacity.

## 11. Scaling efficiency

For distributed training:

```text
scaling_efficiency = measured_speedup / ideal_speedup
```

Equivalent practical form:

```text
parallel_efficiency ≈ measured_speedup / GPU_count
```

Example: if 8 GPUs produce only 5× the throughput of one GPU, measured scaling efficiency is 5/8 = 62.5%. Adding more GPUs may have diminishing returns unless the bottleneck changes.

## 12. Cost model

A first-order compute estimate:

```text
compute_cost ≈ hourly_resource_cost × runtime_hours
```

Total workload cost should include:

```text
compute
+ storage
+ network
+ managed services
+ observability
+ failed/retried work
+ idle capacity
```

For production, calculate cost per successful inference request or completed training job, not only cost per VM-hour.

## 13. Scenario planning

Always create at least three scenarios:

| Scenario | Purpose |
|---|---|
| Low | expected minimum demand |
| Base | normal production demand |
| High | realistic peak or growth case |

For each, calculate resources, latency/throughput expectation, and cost.

## 14. Senior-engineer heuristic

When uncertain, optimize in this order:

1. Verify the workload requirement.
2. Measure the smallest representative system.
3. Find the actual bottleneck.
4. Change one resource dimension.
5. Benchmark again.
6. Record the result.
7. Automate the winning configuration.

Do not solve an unmeasured bottleneck by automatically adding GPUs.

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| VRAM | Memory physically available on a GPU. |
| Activation | Intermediate values created while a neural network processes data. |
| KV cache | Stored attention key/value tensors reused during autoregressive generation. |
| Throughput | Amount of work completed per unit time. |
| Latency | Time required to complete a request or operation. |
| TTFT | Time to first token; how quickly streaming generation starts. |
| P95/P99 | Percentile latency values describing the slower tail of requests. |
| Headroom | Deliberate unused capacity kept for variability and safety. |
| Bottleneck | Resource or operation limiting overall performance. |
| Scaling efficiency | Measured speedup divided by ideal speedup for the added resources. |
| IOPS | Input/output operations per second. |
| Bandwidth | Amount of data transferred per unit time. |
| Capacity planning | Estimating resources required for expected workloads. |
