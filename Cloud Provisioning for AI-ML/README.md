# Cloud Provisioning for AI/ML Engineering

A practical, cloud-neutral guide to provisioning infrastructure for AI/ML workloads on **AWS, GCP, and Azure**. It is written for juniors who need the concepts explained clearly and for senior engineers who need the trade-offs, sizing heuristics, IaC patterns, failure modes, and production decision framework.

The goal is not to memorize instance names. The goal is to learn how to translate an ML workload into **CPU, RAM, GPU/accelerator, VRAM, storage, network, Kubernetes, security, observability, and cost requirements**, then provision those resources reproducibly with Terraform and Helm.

## What an AI/ML engineer should know

- Cloud primitives: regions, zones, VPC/VNet, subnets, routing, IAM, object storage, block storage, load balancers
- Compute: CPU, RAM, GPU, accelerator topology, GPU memory, NUMA, local NVMe, ephemeral disks
- AI workloads: training, fine-tuning, batch inference, online inference, embeddings, RAG, vector search
- Kubernetes: nodes, pods, requests/limits, taints/tolerations, affinity, node pools, GPU scheduling, autoscaling
- Infrastructure as Code: Terraform state, modules, variables, outputs, providers, plan/apply, remote state, drift
- Packaging: Helm charts, values, releases, secrets, ConfigMaps, probes, resources
- Distributed systems: data parallelism, tensor parallelism, pipeline parallelism, collective communication, checkpointing
- Storage: object storage vs block storage vs shared filesystem; dataset/model/checkpoint lifecycle
- Networking: bandwidth, latency, egress, load balancing, private endpoints, DNS, service discovery
- Security: least privilege, workload identity, secrets, encryption, private networking, image supply chain
- Observability: GPU utilization, VRAM, CPU/RAM, queue depth, latency, throughput, errors, cost per successful task
- FinOps: capacity planning, utilization, autoscaling, Spot/preemptible capacity, reservations/commitments, idle resource detection
- Reliability: multi-zone design, failure domains, retries, checkpointing, rollback, disaster recovery

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
11. Production architecture and failure drills
```

## Senior-engineer rule of thumb

Start from the workload, not the cloud product.

```text
workload
  → model/data size
  → memory requirement
  → compute requirement
  → GPU/accelerator requirement
  → parallelism requirement
  → storage IOPS/throughput
  → network bandwidth/latency
  → availability/SLO
  → security/compliance
  → cost envelope
  → cloud resources
```

Then validate every assumption with a small benchmark. A sizing formula is a starting hypothesis, not a substitute for profiling.

## Core resource-sizing questions

Before provisioning, answer:

1. What is the workload: training, fine-tuning, batch inference, online inference, RAG, embedding, or data processing?
2. What model architecture and parameter count are involved?
3. What precision is used: FP32, BF16, FP16, FP8, INT8, INT4?
4. How much GPU VRAM is required during the real workload, including activations and KV cache?
5. Does the workload fit on one GPU/node? If not, what parallelism strategy is required?
6. How many concurrent jobs or requests are expected?
7. What throughput and latency targets matter?
8. What dataset size and checkpoint size must be stored?
9. What storage throughput is required to keep GPUs fed?
10. How much east-west and north-south network traffic exists?
11. What failures are acceptable, and how quickly must the system recover?
12. Which data is sensitive and which services must remain private?
13. What is the maximum monthly/hourly cost?
14. Which capacity can be interruptible and which must be reliable?

## Reference implementation philosophy

Use **Terraform for infrastructure** and **Helm/Kubernetes manifests for workloads**. Keep application images immutable and keep environment-specific configuration outside the image.

```text
Terraform
  ├── network
  ├── IAM / workload identity
  ├── object storage
  ├── Kubernetes cluster
  ├── node pools / GPU capacity
  ├── databases / queues / registries
  └── observability dependencies

Helm
  ├── model server
  ├── training job / Ray / Kueue
  ├── API
  ├── worker
  ├── Prometheus / Grafana integrations
  └── policies / probes / autoscaling
```

## Primary references

- AWS EKS AI/ML best practices: https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html
- AWS EKS with Terraform for AI/ML: https://docs.aws.amazon.com/eks/latest/userguide/ml-cluster-setup-tf.html
- AWS Terraform provider best practices: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html
- GKE GPU workloads: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus
- GKE GPU concepts: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus
- Google Cloud Terraform best practices: https://docs.cloud.google.com/docs/terraform/best-practices/working-with-resources
- Azure AKS GPU architecture: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-gpu/gpu-aks
- Azure AKS best practices: https://learn.microsoft.com/en-us/azure/aks/best-practices
- Terraform: https://developer.hashicorp.com/terraform/docs
- Helm: https://helm.sh/docs/
- Kubernetes GPU scheduling: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/

## Files in this section

- `00-PLAN.md` — complete learning and implementation plan
- `01-resource-sizing.md` — practical sizing formulas and senior-engineer heuristics
- `02-cloud-architecture.md` — common architecture and cloud primitives
- `03-aws.md` — AWS/EKS/S3/EC2/IAM/Karpenter patterns
- `04-gcp.md` — GCP/GKE/Cloud Storage/IAM and GPU patterns
- `05-azure.md` — Azure/AKS/Blob Storage/Managed Identity patterns
- `06-terraform.md` — Terraform structure, modules, state, CI/CD and examples
- `07-kubernetes-and-helm.md` — GPU scheduling, Helm, autoscaling and workload patterns
- `08-storage-networking-security.md` — data plane, network, secrets, identity and security
- `09-observability-and-cost.md` — metrics, tracing, GPU monitoring, SLOs and FinOps
- `10-distributed-training-and-serving.md` — multi-GPU/multi-node training and inference
- `11-production-checklists.md` — readiness and incident checklists
- `12-labs.md` — hands-on exercises from laptop to production-style cluster
- `references.md` — primary documentation and terminology

## Safety boundary

Do not put cloud credentials, API keys, private datasets, patient records, PHI, proprietary model weights, Terraform state containing secrets, or production secrets in this public repository. Examples should use placeholders and synthetic data.

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Provisioning | Creating and configuring cloud infrastructure. |
| IaC | Infrastructure as Code; describing infrastructure in version-controlled files instead of clicking through consoles. |
| GPU | Specialized accelerator used heavily for ML computation. |
| VRAM | GPU memory available to the workload. |
| Node | A machine in a Kubernetes cluster. |
| Pod | The Kubernetes unit that runs one or more tightly coupled containers. |
| Node pool | A group of similar Kubernetes nodes, often separated by workload type. |
| Terraform | An infrastructure-as-code tool that manages resources through providers. |
| Helm | A Kubernetes package manager that templates and installs applications. |
| SLO | Service Level Objective; a measurable reliability or performance target. |
| FinOps | The practice of managing cloud cost together with engineering and business decisions. |
