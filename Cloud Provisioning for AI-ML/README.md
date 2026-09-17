# Cloud Provisioning for AI/ML Engineering

A practical, cloud-neutral guide to provisioning infrastructure for AI/ML workloads on **AWS, GCP, and Azure**. It is written for juniors who need the concepts explained clearly and for senior engineers who need the trade-offs, sizing heuristics, failure modes, production decision framework, and hands-on diagnostics.

The goal is not to memorize instance names. The goal is to translate an ML workload into **CPU, RAM, GPU/accelerator, VRAM, storage, network, Kubernetes, security, observability, and cost requirements**, then provision those resources reproducibly with Terraform and Helm.

## The engineering loop

```text
workload requirement
        ↓
baseline measurement
        ↓
resource constraint
        ↓
measured bottleneck
        ↓
one hypothesis
        ↓
one change
        ↓
benchmark
        ↓
performance + cost + reliability
        ↓
automation
```

> **Rule of thumb:** adding capacity is an intervention, not a diagnosis.

## What an AI/ML engineer should know

- Cloud primitives: regions, zones, VPC/VNet, subnets, routing, IAM, object storage, block storage, load balancers
- Compute: CPU, RAM, GPU, accelerator topology, GPU memory, NUMA, local NVMe, ephemeral disks
- AI workloads: training, fine-tuning, batch inference, online inference, embeddings, RAG, vector search
- Kubernetes: nodes, pods, requests/limits, taints/tolerations, affinity, node pools, GPU scheduling, autoscaling
- Infrastructure as Code: Terraform state, modules, variables, outputs, providers, plan/apply, remote state, drift
- Packaging: Helm charts, values, releases, secrets, ConfigMaps, probes, resources
- Distributed systems: data/tensor/pipeline parallelism, sharding, collective communication, checkpointing
- Storage: object storage vs block storage vs shared filesystem; dataset/model/checkpoint lifecycle
- Networking: bandwidth, latency, egress, load balancing, private endpoints, DNS, service discovery
- Security: least privilege, workload identity, secrets, encryption, private networking, image supply chain
- Observability: GPU utilization, VRAM, CPU/RAM, queue depth, latency, throughput, errors, cost per successful task
- FinOps: capacity planning, utilization, autoscaling, interruptible capacity, reservations/commitments, idle-resource detection
- Reliability: failure domains, multi-zone design, retries, checkpointing, rollback, disaster recovery

## Recommended learning path

```text
01. Workload → resource requirements
        ↓
02. Cloud primitives and architecture
        ↓
03. GPU/CPU sizing and capacity planning
        ↓
04. Terraform foundations and state
        ↓
05. AWS / GCP / Azure implementations
        ↓
06. Kubernetes + GPU node pools
        ↓
07. Helm deployment patterns
        ↓
08. Storage + networking + security
        ↓
09. Observability + autoscaling + cost
        ↓
10. Distributed training + inference
        ↓
11. Hands-on labs + rules of thumb
        ↓
12. Practical glossary
```

## Hands-on labs

Start with [`11-hands-on-labs.md`](./11-hands-on-labs.md).

The labs turn the concepts into measurable exercises:

- workload specification
- VRAM feasibility
- inference capacity and capacity-knee testing
- CPU/data-loader bottleneck detection
- storage throughput measurement
- network sizing
- multi-GPU scaling efficiency
- Kubernetes GPU scheduling
- Terraform change safety
- cost per successful task
- reliability game days
- bottleneck reports

Each lab follows:

```text
hypothesis → evidence → controlled change → benchmark → decision
```

## Practical terminology

Use [`12-glossary.md`](./12-glossary.md) as a field reference. Definitions are intentionally tied to engineering decisions rather than only giving dictionary descriptions.

Important terms include:

- VRAM, KV cache, prefill, decode
- TTFT, inter-token latency, throughput, concurrency
- saturation, capacity knee, headroom, scaling efficiency
- IOPS, data locality, east-west/north-south traffic, egress
- workload identity, blast radius, drift, immutable artifact
- Kubernetes requests/limits, probes, taints/tolerations
- collective communication, sharding, checkpointing
- agent loop, tool call, capability gating, no-progress detection
- cost per successful task and idle capacity

## Provider mapping

| Abstraction | AWS | GCP | Azure |
|---|---|---|---|
| Virtual network | VPC | VPC | VNet |
| Kubernetes | EKS | GKE | AKS |
| Object storage | S3 | Cloud Storage | Blob Storage |
| Container registry | ECR | Artifact Registry | ACR |
| Identity | IAM / workload identity patterns | IAM / Workload Identity | Entra ID / Managed Identity |
| Monitoring | CloudWatch | Cloud Monitoring | Azure Monitor |
| GPU compute | EC2 GPU families | Compute Engine GPU VMs | Azure GPU VM families |

The abstraction should remain stable while the provider implementation changes.

## Evidence-driven sizing

For each production-like benchmark, preserve:

```text
model revision
container image digest
runtime/driver versions
hardware
region/zone
dataset version
input/output token distribution
batch size
concurrency
configuration revision
benchmark timestamp
raw measurements
```

This makes performance claims reproducible instead of turning them into unexplained numbers.

## Senior review checklist

Before approving an AI/ML infrastructure design, ask:

- What requirement determines capacity?
- What assumption determines GPU count?
- Is the constraint compute, VRAM, storage, network, CPU, queueing, or scheduling?
- What evidence identifies the bottleneck?
- What happens at P95/P99 workload conditions?
- What happens when a node or zone fails?
- How quickly can the workload recover?
- What is the cost at low/base/high utilization?
- Are expensive resources protected from accidental consumption?
- Are identities short-lived and least-privileged?
- Are artifacts immutable and traceable to source/configuration?
- Can infrastructure and application versions be rolled back independently?

## Primary references

- [Kubernetes GPU scheduling](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
- [AWS EKS AI/ML best practices](https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html)
- [Google Cloud GKE GPU documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus)
- [Azure AKS GPU architecture](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-gpu/gpu-aks)

## Files in this section

- `00-PLAN.md` — learning and implementation plan
- `01-resource-sizing.md` — sizing formulas and heuristics
- `02-cloud-architecture.md` — common architecture and cloud primitives
- `03-aws.md` — AWS/EKS/S3/EC2/IAM/Karpenter patterns
- `04-gcp.md` — GCP/GKE/Cloud Storage/IAM and GPU patterns
- `05-azure.md` — Azure/AKS/Blob Storage/Managed Identity patterns
- `06-terraform.md` — Terraform structure, modules, state, CI/CD and examples
- `07-kubernetes-and-helm.md` — GPU scheduling, Helm, autoscaling and workload patterns
- `08-storage-networking-security.md` — data plane, network, secrets, identity and security
- `09-observability-and-cost.md` — metrics, tracing, GPU monitoring, SLOs and FinOps
- `10-distributed-training-and-serving.md` — multi-GPU/multi-node training and inference
- `11-hands-on-labs.md` — hands-on experiments and rules of thumb
- `12-glossary.md` — practical AI/ML cloud infrastructure terminology
