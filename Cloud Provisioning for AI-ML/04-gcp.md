# GCP Provisioning for AI/ML

GCP building blocks commonly used for AI/ML include Google Kubernetes Engine (GKE), Compute Engine GPU VMs, Cloud Storage, Artifact Registry, IAM, Workload Identity Federation for GKE, Cloud Monitoring, and managed networking.

## Reference architecture

```text
VPC
├── private GKE nodes
│   ├── CPU node pool
│   └── GPU node pool
├── load balancing
└── private service connectivity

Cloud Storage → datasets / models / checkpoints
Artifact Registry → images
IAM + Workload Identity Federation → permissions
Cloud Monitoring → telemetry
```

## GKE GPU principles

GPU workloads should request the GPU resource explicitly and be scheduled onto compatible node pools.

Keep accelerator node pools separated when different GPU types or workload priorities exist.

## Terraform categories

Typical resources/modules cover:

```text
VPC
subnets
firewall rules
GKE cluster
node pools
GPU nodes
Cloud Storage buckets
Artifact Registry
service accounts / Workload Identity Federation
monitoring dependencies
```

Understand what the module creates, what it owns, and how state is managed before using it in production.

## Storage design

Cloud Storage should usually be the durable artifact/data layer. Local disks can provide faster temporary access but should not be assumed durable unless explicitly designed that way.

## GCP-specific senior concerns

- Cloud quotas and regional/zone accelerator availability
- GKE GPU node pools
- Workload Identity Federation for GKE
- Autopilot vs Standard suitability for the workload
- Persistent Disk vs Local SSD vs other ephemeral storage
- Spot VM interruption
- network egress
- private GKE design
- Cloud Monitoring cost and cardinality
- GPU driver/runtime compatibility

## Primary GCP references

- GKE GPUs: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus
- GKE GPU concepts: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus
- Google Cloud Terraform best practices: https://docs.cloud.google.com/docs/terraform/best-practices/working-with-resources

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| GKE | Google Kubernetes Engine. |
| Compute Engine | Google Cloud virtual machine compute service. |
| Cloud Storage | Google Cloud object storage. |
| Artifact Registry | Google Cloud service for container and package artifacts. |
| Workload Identity Federation for GKE | Google Cloud mechanism for securely associating Kubernetes workloads with IAM identities without long-lived service-account keys. |
| Spot VM | Interruptible Compute Engine VM capacity designed for lower-cost workloads. |
| Quota | Cloud-enforced limit on the amount of a resource or service that can be consumed. |
| Standard GKE | GKE mode providing direct control over nodes and node pools. |
