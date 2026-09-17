# Hands-On Labs and Rules of Thumb

This chapter turns the preceding infrastructure concepts into repeatable engineering exercises. The objective is not to memorize cloud SKU names. It is to learn how to form a hypothesis, measure a bottleneck, change one variable, and verify the result.

> **Rule of thumb:** never scale a resource because it is the resource you happen to be looking at. First identify the constraint that is preventing useful work.

## Lab 1 — Write a workload specification

Pick one real workload: LLM inference, embedding generation, RAG, fine-tuning, or batch inference.

Record:

```text
model:
parameter_count:
quantization/precision:
context_length:
input_tokens_p50/p95:
output_tokens_p50/p95:
requests_per_second:
concurrency:
TTFT target:
end_to_end_latency target:
availability target:
budget:
data size:
security requirements:
```

### Deliverable

Produce low/base/high scenarios. Do not choose a VM yet.

### Rule of thumb

**Requirements first, instance type second.** If a requirement cannot be measured, mark it as an assumption.

---

## Lab 2 — Prove whether GPU memory is the constraint

Estimate model-weight memory:

```text
weights ≈ parameters × bytes_per_parameter
```

Then add the runtime components that apply to your workload:

```text
peak_VRAM ≈ weights
          + KV_cache
          + activations
          + temporary_buffers
          + framework/runtime_overhead
```

For training, include gradients and optimizer state.

### Experiment

Run the smallest representative workload and capture:

- peak VRAM
- GPU utilization
- tokens/sec or samples/sec
- batch size
- sequence length
- OOM events

### Rule of thumb

**VRAM capacity and GPU compute are different bottlenecks.** A GPU can have spare compute while running out of memory, or have abundant VRAM while being compute-bound.

---

## Lab 3 — Find the inference knee point

Run the same model at increasing concurrency:

```text
1 → 2 → 4 → 8 → 16 → 32 → ...
```

Record:

| Concurrency | RPS | TTFT | P95 latency | tokens/sec | GPU util | VRAM | Errors |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 4 | | | | | | | |
| 8 | | | | | | | |
| 16 | | | | | | | |

Plot where throughput stops increasing proportionally while latency continues increasing.

That region is the **capacity knee**: additional concurrency is creating queueing rather than useful throughput.

### Rule of thumb

Do not autoscale solely on GPU utilization. A 90% GPU can be healthy if throughput and latency are good; a 40% GPU can still be unhealthy if requests are blocked elsewhere.

---

## Lab 4 — Detect a CPU/data-loader bottleneck

Run an inference or training job while measuring CPU utilization, GPU utilization, data-loader throughput, and step/request time.

### Hypothesis

If GPU utilization repeatedly drops while CPU workers are saturated or data arrival is irregular, investigate preprocessing and input delivery before adding GPUs.

### Try

1. Increase data-loader workers.
2. Add local caching where appropriate.
3. Change serialization/compression.
4. Measure again.

### Rule of thumb

**A GPU waiting for data is paid-for idle capacity.** Measure the producer side of the pipeline, not only the accelerator.

---

## Lab 5 — Measure storage throughput

Separate **capacity** from **throughput**.

A dataset may fit on a disk and still fail to feed the GPUs quickly enough.

Measure:

```text
GB/s read
IOPS
average I/O latency
small-file rate
concurrent readers
cache hit rate
```

Estimate the required read rate:

```text
required_read_rate ≈ bytes_consumed_per_step × steps_per_second
```

### Rule of thumb

For AI training, ask **"Can the storage feed all workers fast enough?"**, not just **"How many TB do I need?"**

---

## Lab 6 — Measure network as a bottleneck

For a transfer of `D` bytes that must complete in `T` seconds:

```text
minimum_bandwidth ≈ D / T
```

Then account for contention and protocol overhead.

Measure separately:

- node-to-node bandwidth
- object-store download rate
- cross-zone traffic
- cross-region traffic
- model image/artifact pull time

### Rule of thumb

**Convert bits to bytes explicitly.** A network advertised in Gb/s is not the same unit as storage throughput reported in GB/s.

---

## Lab 7 — Compare one GPU vs multiple GPUs

Benchmark the same workload at 1, 2, 4, and 8 GPUs where available.

Calculate:

```text
speedup(N) = throughput(N) / throughput(1)
parallel_efficiency(N) = speedup(N) / N
```

Record communication time and synchronization stalls.

### Interpretation

If 8 GPUs deliver 5× the throughput of one GPU:

```text
parallel_efficiency = 5 / 8 = 62.5%
```

Investigate communication, input pipelines, imbalance, and synchronization before buying more accelerators.

### Rule of thumb

**More GPUs are useful only when the workload can convert them into useful work.**

---

## Lab 8 — Test Kubernetes GPU scheduling

Create separate CPU and GPU node pools. Label GPU nodes and use taints/tolerations where isolation is required.

Example concepts:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

Then verify:

```bash
kubectl get nodes --show-labels
kubectl describe node <gpu-node>
kubectl get pods -o wide
kubectl describe pod <pod>
```

### Failure injection

Submit a GPU workload when no compatible GPU capacity exists. Observe the pod's scheduling events.

### Rule of thumb

**If an expensive resource is not explicitly requested and constrained, assume it can eventually be consumed accidentally.**

---

## Lab 9 — Terraform change-safety exercise

For a representative infrastructure change:

```text
terraform fmt
terraform validate
terraform plan
review
terraform apply
```

Then deliberately introduce a configuration change that would replace a production-like resource and inspect the plan before applying it.

### Questions

- What resource is being replaced?
- What data could be lost?
- What is the blast radius?
- Can the change be rolled back?
- Is state stored remotely and protected?

### Rule of thumb

**Never approve a Terraform change you cannot explain resource-by-resource.**

---

## Lab 10 — Build a cost-per-success metric

Track:

```text
compute
storage
network
managed services
observability
failed/retried work
```

Then calculate:

```text
cost_per_successful_task = total_cost / successful_tasks
```

For inference, also track:

```text
cost_per_1M_input_tokens
cost_per_1M_output_tokens
cost_per_successful_request
```

### Rule of thumb

**Cost per VM-hour is an infrastructure metric; cost per successful outcome is an engineering metric.**

---

## Lab 11 — Reliability game day

Pick a deployed workload and simulate:

- GPU node loss
- pod eviction
- image-pull failure
- insufficient GPU capacity
- object-storage access failure
- network saturation
- OOM
- failed model rollout
- failed Terraform apply
- runaway autoscaling

For each failure record:

```text
failure → detection → impact → recovery → data loss? → rollback → prevention
```

### Rule of thumb

A recovery procedure is not production-ready until somebody has exercised it.

---

## Lab 12 — Create a bottleneck report

For each experiment write:

```text
Workload:
Hypothesis:
Baseline:
Observed bottleneck:
Evidence:
Change:
Result:
Regression risk:
Cost impact:
Decision:
```

### Example

```text
Hypothesis: GPU utilization is low because object storage cannot feed workers.
Evidence: GPU utilization falls during input stalls; local-cache test removes stalls.
Change: add local dataset cache.
Result: step time decreases while GPU utilization rises.
Decision: improve data locality before adding GPUs.
```

This format turns infrastructure tuning into an auditable engineering process.

---

# Practical Rules of Thumb

These are heuristics, not universal limits. Validate them against the actual workload.

| Situation | Starting heuristic |
|---|---|
| Choosing compute | Size from measured workload requirements, not SKU familiarity. |
| GPU sizing | Check VRAM fit before comparing raw GPU compute. |
| LLM inference | Benchmark realistic input/output token distributions and concurrency. |
| Latency | Track P50, P95, and P99 rather than averages alone. |
| Autoscaling | Scale on a signal correlated with demand/saturation, not a convenient metric. |
| Storage | Size both capacity and sustained/random throughput. |
| Networking | Calculate required transfer rate before assuming the network is sufficient. |
| Distributed training | Measure communication and synchronization overhead. |
| Kubernetes GPUs | Use explicit GPU requests plus intentional node isolation. |
| Production headroom | Reserve capacity for variability; determine the amount with load testing. |
| Spot/interruptible compute | Use when checkpoint/restart economics tolerate interruption. |
| Terraform | Keep state protected and review plans before apply. |
| Security | Prefer short-lived workload identities over embedded credentials. |
| Cost | Measure useful work per dollar, not only resource price. |
| Reliability | Test failure and recovery paths before depending on them. |

# Bottleneck Decision Tree

```text
Is the workload meeting its SLO?
        │
      yes ──► measure cost and utilization
        │
       no
        │
        ▼
Is the request waiting in a queue?
   │                 │
  yes                no
   │                 │
   ▼                 ▼
capacity/scaling   Is model compute saturated?
                         │
                    ┌────┴────┐
                   yes       no
                    │         │
                    ▼         ▼
                GPU/CPU    Is VRAM full?
                compute      │
                         ┌───┴───┐
                        yes     no
                         │       │
                         ▼       ▼
                    memory/   Check storage,
                    batching  network, CPU,
                              scheduling,
                              dependencies
```

# Recommended evidence to collect

Every benchmark should preserve:

- model and model revision
- container image digest
- CUDA/driver/runtime versions where relevant
- dataset version
- prompt/token distribution
- concurrency
- batch size
- hardware type
- region/zone
- Kubernetes/Terraform version or commit
- benchmark timestamp
- workload configuration
- raw measurements

This prevents a benchmark from becoming an unexplained number in a spreadsheet.

# Further reading

- Kubernetes GPU scheduling: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
- Terraform documentation: https://developer.hashicorp.com/terraform/docs
- AWS EKS AI/ML best practices: https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html
- Google Cloud GKE GPU documentation: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus
- Azure AKS GPU architecture: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-gpu/gpu-aks
