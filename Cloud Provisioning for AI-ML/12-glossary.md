# AI/ML Cloud Infrastructure Glossary

A practical glossary for engineers moving from notebooks and model APIs to production infrastructure.

## Workload and performance

| Term | Practical definition | What to measure |
|---|---|---|
| **Workload** | The actual pattern of computation, data movement, requests, and reliability requirements the platform must support. | RPS, tokens, batch size, concurrency, runtime |
| **SLO** | A measurable target for service behavior, such as latency or availability. | P95 latency, availability |
| **Throughput** | Useful work completed per unit time. | tokens/s, requests/s, samples/s |
| **Latency** | Time required for an operation or request. | P50/P95/P99 |
| **Concurrency** | Number of operations simultaneously in progress. | requests in flight |
| **Queue depth** | Number of jobs or requests waiting for capacity. | queued work over time |
| **Saturation** | A resource is near the point where additional demand mostly produces waiting rather than useful work. | utilization + queueing + latency |
| **Capacity knee** | The operating region where adding concurrency produces sharply worse latency with little additional throughput. | throughput/latency curve |
| **Headroom** | Deliberately unused capacity reserved for variability, failures, and bursts. | peak utilization vs available capacity |
| **Scaling efficiency** | Useful performance gained relative to the ideal performance increase from additional resources. | measured speedup / ideal speedup |

## LLM serving

| Term | Practical definition | Rule of thumb |
|---|---|---|
| **TTFT** | Time to First Token: delay from request acceptance until the first generated token is available. | Track separately from total response latency. |
| **Inter-token latency** | Time between generated tokens during streaming. | A useful indicator of generation smoothness. |
| **Prefill** | Processing the input prompt/context before autoregressive generation. | Long prompts can make prefill a major latency component. |
| **Decode** | Autoregressive generation of output tokens after prefill. | Often sensitive to KV-cache and memory bandwidth. |
| **KV cache** | Stored attention key/value tensors reused during generation. | Context length and concurrency can make KV memory a first-order constraint. |
| **Continuous batching** | Dynamically combining work from different requests during model execution. | Benchmark at realistic concurrency; batching changes throughput/latency trade-offs. |
| **Tokens/sec** | Rate of token processing or generation. | Define whether the metric means input, output, or aggregate tokens. |
| **Model server** | Runtime service that loads a model and handles inference requests. | Benchmark the actual server/configuration, not only the GPU specification. |

## GPU and memory

| Term | Practical definition | Common failure mode |
|---|---|---|
| **VRAM** | GPU-attached memory used by weights, KV cache, activations, buffers, and runtime state. | OOM despite apparently low GPU compute utilization. |
| **Memory bandwidth** | Rate at which data can be moved to/from GPU memory. | GPU compute units appear underutilized while memory movement limits throughput. |
| **FLOPS / TFLOPS** | Floating-point operations per second; a theoretical compute capability metric. | Comparing GPUs using TFLOPS alone and ignoring memory/interconnect/workload behavior. |
| **OOM** | Out Of Memory condition. | Batch size, context length, KV cache, or runtime buffers exceed available memory. |
| **Quantization** | Representing model values with lower numerical precision to reduce memory and/or improve efficiency. | Quality/performance changes must be benchmarked for the actual model. |
| **Activation** | Intermediate neural-network values produced during computation. | Long sequences and large batches can increase memory pressure. |
| **Memory fragmentation** | Free memory exists but cannot be allocated in the required contiguous/compatible pattern. | Theoretical memory calculation says the model fits, but runtime allocation fails. |

## Distributed training

| Term | Practical definition | Rule of thumb |
|---|---|---|
| **Data parallelism** | Multiple workers process different input batches while synchronizing model state. | Communication overhead grows with synchronization requirements. |
| **Tensor parallelism** | A model's tensor operations are partitioned across accelerators. | Interconnect bandwidth and latency matter. |
| **Pipeline parallelism** | Different model stages/layers execute on different devices. | Pipeline bubbles and load imbalance can reduce utilization. |
| **Sharding** | Model/training state is partitioned across workers. | Reduces per-device memory but adds communication complexity. |
| **Collective communication** | Coordinated communication such as all-reduce among distributed workers. | Measure communication time rather than assuming linear scaling. |
| **Scaling efficiency** | Ratio between achieved speedup and ideal speedup. | More GPUs are not automatically more throughput. |
| **Checkpoint** | Persistent saved training state used for recovery or analysis. | Checkpoint interval should be evaluated against restart time and interruption risk. |

## Storage

| Term | Practical definition | What to ask |
|---|---|---|
| **Object storage** | Durable storage accessed through an object API, typically used for datasets and artifacts. | How fast can workers read the data? |
| **Block storage** | Disk-like storage attached to compute. | IOPS, throughput, latency, durability |
| **Ephemeral storage** | Storage whose lifetime is tied to a machine or workload. | What happens when the node disappears? |
| **Shared filesystem** | Filesystem accessible by multiple workers. | Concurrent-read/write behavior and throughput |
| **IOPS** | Input/output operations per second. | Important for many-small-file workloads. |
| **Storage throughput** | Amount of data read/written per unit time. | GB/s or MB/s |
| **Data locality** | How close data is to the compute processing it. | Moving data repeatedly can become a bottleneck and cost driver. |

## Networking

| Term | Practical definition | Rule of thumb |
|---|---|---|
| **Bandwidth** | Maximum/observed data transfer rate. | Calculate required bandwidth from data volume and deadline. |
| **Network latency** | Time required for data to travel between endpoints. | Important for distributed synchronization and request paths. |
| **North-south traffic** | Traffic entering or leaving a platform/network boundary. | Commonly associated with users, APIs, and external services. |
| **East-west traffic** | Traffic between internal services/nodes. | Important for distributed training and microservice architectures. |
| **Egress** | Data leaving a cloud/network boundary. | Large cross-region or internet transfers can become expensive. |
| **Cross-zone traffic** | Traffic crossing availability/failure zones. | Account for both performance and provider-specific pricing. |
| **Interconnect** | High-speed communication path between accelerators/nodes. | Critical for distributed training and model parallelism. |

## Kubernetes

| Term | Practical definition | Rule of thumb |
|---|---|---|
| **Pod** | Kubernetes' smallest deployable workload unit. | Treat pod lifecycle as disposable. |
| **Node** | Worker machine running pods. | Separate expensive GPU capacity from general workloads when useful. |
| **Node pool** | Group of nodes managed with common configuration/scaling behavior. | Separate GPU types or workload classes when scheduling needs differ. |
| **Resource request** | Resource amount used by Kubernetes scheduling decisions. | Base requests on measurements. |
| **Resource limit** | Maximum resource consumption configured for a container/resource type. | Understand the resource-specific semantics before setting it. |
| **Taint** | Node property that prevents ordinary scheduling unless tolerated. | Useful for protecting dedicated GPU nodes. |
| **Toleration** | Pod declaration allowing it to run on a tainted node. | Pair with labels/affinity for intentional placement. |
| **Affinity** | Scheduling rules based on node/pod attributes. | Use when placement materially affects performance or isolation. |
| **Readiness probe** | Check determining whether a pod should receive traffic. | A loaded process can be alive but not ready. |
| **Liveness probe** | Check used to determine whether a container should be restarted. | Do not restart simply because model loading is slow. |
| **Startup probe** | Check allowing slow-starting applications time to initialize. | Useful for large model loading. |
| **HPA** | Horizontal Pod Autoscaler; adjusts replica count based on metrics. | Choose metrics that correlate with demand/capacity. |
| **PDB** | PodDisruptionBudget; limits voluntary disruptions to selected pods. | It does not prevent all failures or involuntary disruptions. |

## Infrastructure as code

| Term | Practical definition | Rule of thumb |
|---|---|---|
| **Terraform provider** | Plugin implementing resource/data-source behavior for a platform. | Pin and review provider versions. |
| **Terraform resource** | Infrastructure object Terraform manages. | Understand lifecycle and replacement behavior. |
| **Terraform module** | Reusable package of infrastructure configuration. | Expose meaningful inputs instead of every provider argument. |
| **Terraform state** | Persistent record Terraform uses to map configuration to real infrastructure. | Protect it like sensitive infrastructure data. |
| **Drift** | Difference between Terraform's recorded/intended state and actual infrastructure. | Detect it rather than assuming state equals reality. |
| **Plan** | Proposed infrastructure changes calculated before apply. | Read it before approving. |
| **Blast radius** | Scope of resources that can be affected by a change or failure. | Keep modules and state boundaries understandable. |
| **Immutable artifact** | Artifact identified by a version/digest rather than a mutable alias. | Prefer model/container digests for reproducibility. |

## Cloud architecture

| Term | Practical definition |
|---|---|
| **Region** | Geographic cloud location containing infrastructure. |
| **Availability zone** | Separate failure domain within a region. |
| **VPC/VNet** | Provider network boundary for IP connectivity and routing. |
| **Subnet** | Address range within a cloud network. |
| **Load balancer** | Component distributing traffic across healthy backends. |
| **Private endpoint** | Private connectivity mechanism to a managed service without requiring public network paths. |
| **NAT** | Network Address Translation; commonly allows private resources to initiate outbound connections without public IPs. |
| **Workload identity** | Mechanism allowing an application workload to obtain cloud permissions without embedding long-lived credentials. |
| **Managed service** | Provider-operated service that removes some infrastructure operations from the customer. |
| **Failure domain** | Components expected to share a common failure cause. |

## Security

| Term | Practical definition |
|---|---|
| **Least privilege** | Granting only the permissions required for a task. |
| **RBAC** | Role-Based Access Control: permissions assigned through roles. |
| **NetworkPolicy** | Kubernetes policy controlling network communication between workloads. |
| **Secret manager** | Managed system for storing and retrieving sensitive credentials/configuration. |
| **Artifact provenance** | Evidence describing where and how an artifact was produced. |
| **Image digest** | Content-addressed identifier for a container image. |
| **Data poisoning** | Malicious or harmful data introduced into a training/evaluation pipeline. |
| **Prompt injection** | Input designed to manipulate an AI system into violating intended instructions or boundaries. |
| **Blast radius** | Scope of impact if an identity, resource, or change is compromised. |

## Observability and FinOps

| Term | Practical definition | Useful signal |
|---|---|---|
| **Metric** | Numeric measurement recorded over time. | GPU utilization, latency, tokens/sec |
| **Log** | Timestamped event/message describing system behavior. | errors, startup events, scheduling failures |
| **Trace** | End-to-end record of work across components. | request → gateway → model server → tools |
| **Cardinality** | Number of unique values in a telemetry dimension. | High-cardinality labels can increase telemetry cost. |
| **P50/P95/P99** | Percentiles describing typical and tail behavior. | Tail latency is often more useful than average latency for SLOs. |
| **FinOps** | Practice of connecting cloud spending with engineering and business decisions. | cost per workload/outcome |
| **Idle capacity** | Allocated compute that produces little useful work. | GPU-hours vs successful work |
| **Cost per successful task** | Total relevant cost divided by successful outcomes. | Useful for AI/agent workloads where retries and failures matter. |

## Agentic AI infrastructure

| Term | Practical definition | Rule of thumb |
|---|---|---|
| **Agent loop** | Repeated cycle of reasoning, tool selection, execution, observation, and further reasoning. | Bound both iterations and resource consumption. |
| **Tool call** | Structured request from a model to an external capability. | Trace every call and its result. |
| **Tool latency** | Time spent executing an external tool/API. | Do not attribute all agent latency to the LLM. |
| **Sequential dependency** | Operation that cannot begin until another operation produces required information. | Represent dependencies explicitly. |
| **Parallel execution** | Independent operations executed concurrently. | Parallelize only when dependencies and side effects permit it. |
| **Capability gating** | Exposing only tools that are valid/allowed for the current state. | Reduce irrelevant tool choices and accidental calls. |
| **No-progress detection** | Detecting that another iteration is unlikely to produce new useful information. | Combine semantic stopping with a hard iteration budget. |
| **Redundant call** | Tool invocation that repeats equivalent work without adding useful information. | Track normalized tool+argument fingerprints. |
| **Context window** | Amount of input/output context a model can process in one request. | Context is a resource; keep it relevant. |
| **Context transfer** | Moving information from one agent/component to another. | Large handoffs can become a latency/token bottleneck. |

## Senior engineering vocabulary

When reviewing an AI/ML infrastructure design, ask in this order:

```text
Requirement
   ↓
Workload model
   ↓
Resource constraint
   ↓
Measured bottleneck
   ↓
Architecture change
   ↓
Benchmark
   ↓
Cost / reliability impact
   ↓
Automation
```

Useful questions:

- What is the limiting resource?
- What measurement proves it?
- Is the bottleneck compute, memory, storage, network, scheduling, queueing, or application logic?
- What happens at P95/P99 workload conditions?
- What happens when one failure domain disappears?
- What is the recovery time?
- What is the cost per useful outcome?
- Can the change be reproduced from code?
- Can the previous version be restored?

> **Engineering rule:** if you cannot name the bottleneck and show the measurement that supports the claim, you have a hypothesis—not yet a diagnosis.
