# Cloud Provisioning for AI/ML — Master Plan

## Goal

Build the ability to design, provision, operate, and troubleshoot AI/ML infrastructure on AWS, GCP, and Azure without treating cloud resources as a collection of instance names.

The engineer should be able to start with a model and workload and finish with reproducible infrastructure, a cost estimate, an operational plan, and a documented set of trade-offs.

## Phase 0 — Workload framing

Learn to classify workloads:

- offline training
- SFT / LoRA / QLoRA
- distributed pretraining or continued pretraining
- batch inference
- online LLM inference
- embeddings
- RAG retrieval
- data processing / ETL
- evaluation workloads
- agent workloads

Output: a one-page workload specification containing model, data, latency, throughput, availability, security, and budget requirements.

## Phase 1 — Resource mathematics

Learn:

- parameter memory estimates
- optimizer-state memory
- gradient and activation memory
- KV-cache memory
- effective batch size
- sequence-length effects
- GPU count estimation
- storage capacity and throughput
- network bandwidth
- CPU/RAM ratios
- headroom and failure capacity

Output: a sizing worksheet with low/base/high scenarios.

## Phase 2 — Cloud primitives

Understand the equivalent concepts across providers:

| Concept | AWS | GCP | Azure |
|---|---|---|---|
| Network | VPC | VPC | VNet |
| Kubernetes | EKS | GKE | AKS |
| Object storage | S3 | Cloud Storage | Blob Storage |
| Identity | IAM | IAM / Workload Identity | Entra ID / Managed Identity |
| Container registry | ECR | Artifact Registry | Azure Container Registry |
| Monitoring | CloudWatch | Cloud Monitoring | Azure Monitor |
| Secrets | Secrets Manager | Secret Manager | Key Vault |
| GPU VM | EC2 GPU families | Compute Engine GPU VMs | Azure GPU VM families |

The goal is to understand the abstraction before memorizing product names.

## Phase 3 — Terraform

Learn:

- providers
- resources
- data sources
- variables
- outputs
- modules
- locals
- dependency graphs
- remote state
- locking
- workspaces vs separate state
- import and state migration
- plan/apply/destroy
- drift detection
- policy checks
- secrets handling
- CI/CD for Terraform

Output: reusable modules for network, cluster, object storage, identity, registry, and GPU node pools.

## Phase 4 — Kubernetes + Helm

Learn:

- Deployments
- Jobs and CronJobs
- Services
- Ingress/Gateway
- ConfigMaps and Secrets
- resource requests/limits
- GPU resource requests
- node selectors
- taints/tolerations
- affinity/anti-affinity
- PodDisruptionBudgets
- probes
- HPA/KEDA
- cluster autoscaling
- priority classes
- topology spread
- Helm values and releases

Output: a Helm chart for an AI service and a GPU batch job.

## Phase 5 — AWS

Study:

- VPC and private subnets
- EKS
- EC2 GPU instances
- S3
- ECR
- IAM
- IRSA / pod identity patterns
- Karpenter or managed node groups
- CloudWatch
- EBS / EFS where appropriate
- load balancing
- private endpoints
- Spot capacity

Output: Terraform-managed EKS environment with CPU and GPU node pools.

## Phase 6 — GCP

Study:

- VPC and subnet architecture
- GKE
- Compute Engine GPU VMs
- Cloud Storage
- Artifact Registry
- IAM and Workload Identity
- autoscaling
- Cloud Monitoring
- persistent disks / Filestore where appropriate
- private cluster networking
- Spot VMs

Output: equivalent GKE deployment using the same application contract.

## Phase 7 — Azure

Study:

- VNet and subnets
- AKS
- Azure GPU VM families
- Blob Storage
- Azure Container Registry
- Entra ID / Managed Identity
- autoscaling
- Azure Monitor
- managed disks / Azure Files where appropriate
- private endpoints
- Spot VMs

Output: equivalent AKS deployment using the same application contract.

## Phase 8 — Storage and data plane

Learn to choose between:

- object storage
- block storage
- shared filesystem
- local NVMe / ephemeral storage
- databases
- caches
- queues

For every choice document capacity, IOPS, throughput, latency, durability, availability, cost, and failure behavior.

## Phase 9 — Networking

Learn:

- ingress vs egress
- east-west vs north-south traffic
- DNS
- load balancing
- private endpoints
- NAT
- service discovery
- security groups / firewall rules
- Kubernetes NetworkPolicy
- cross-zone traffic
- cross-region traffic
- cloud egress costs

AI-specific concern: large model and dataset transfers can make network throughput a first-order bottleneck.

## Phase 10 — Security

Minimum production topics:

- least privilege
- short-lived credentials
- workload identity
- encryption at rest and in transit
- private networking
- secrets management
- image scanning
- signed images
- dependency scanning
- audit logging
- Kubernetes RBAC
- network policies
- backup and restore
- separation of environments

For medical/regulated workloads, add data classification, PHI controls, retention, access review, audit requirements, and organization-specific compliance controls.

## Phase 11 — Observability

Instrument at four layers:

1. Infrastructure — CPU, RAM, disk, network, GPU
2. Kubernetes — pod health, scheduling, restarts, queue depth
3. Model server — tokens/sec, TTFT, latency percentiles, batch size, KV cache
4. Business/task — success rate, quality, cost per successful task

Always preserve model version, container image, configuration version, and infrastructure version with measurements.

## Phase 12 — Cost engineering

Learn to separate:

- fixed capacity
- variable compute
- storage
- network
- managed service costs
- observability costs
- idle capacity
- failed-job cost
- engineering/operational cost

Use measured utilization before choosing reservations/commitments or interruptible capacity.

## Phase 13 — Distributed training

Understand:

- data parallelism
- tensor parallelism
- pipeline parallelism
- FSDP / sharding concepts
- NCCL / collective communication
- checkpoint frequency
- interconnect bandwidth
- node failure recovery
- elastic jobs

Senior rule: adding GPUs does not guarantee linear speedup. Measure communication overhead and scaling efficiency.

## Phase 14 — Production inference

Compare:

- single VM
- Kubernetes deployment
- vLLM-style model server
- multi-GPU serving
- autoscaled replicas
- asynchronous batch inference

Measure TTFT, inter-token latency, end-to-end latency, throughput, concurrency, GPU utilization, VRAM, and cost.

## Phase 15 — Reliability and operations

Practice:

- zone failure
- GPU node loss
- pod eviction
- image pull failure
- insufficient GPU capacity
- object-store outage
- network saturation
- OOM
- bad model rollout
- bad Terraform change
- failed Helm upgrade
- runaway autoscaling
- unexpected cloud bill

Every production service should have rollback and recovery procedures.

## Definition of done

An AI/ML engineer completing this section should be able to:

- translate model requirements into resources
- estimate GPU/VRAM/storage/network requirements
- explain the estimate and its uncertainty
- build the environment with Terraform
- deploy the workload with Helm/Kubernetes
- secure identities and secrets
- instrument the system
- benchmark it
- calculate cost
- identify bottlenecks
- scale it
- recover from common failures
- explain AWS/GCP/Azure trade-offs
- review another engineer's infrastructure pull request

## Senior review questions

Before approving infrastructure, ask:

- What assumption drives the GPU count?
- What happens when demand doubles?
- What happens when one node disappears?
- What is the largest object transferred during startup?
- Are GPUs starved by storage or network throughput?
- Is VRAM the bottleneck or compute?
- What percentage of capacity is idle?
- Can this workload tolerate interruption?
- How is the model version tied to the deployment?
- How do we roll back infrastructure and application independently?
- What is the blast radius of this Terraform module?
- What is the monthly cost at 25%, 50%, and 100% utilization?
- Which metric tells us that adding capacity is actually helping?
