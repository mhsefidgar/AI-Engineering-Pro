# Azure Provisioning for AI/ML

Azure building blocks commonly used for AI/ML include Azure Kubernetes Service (AKS), GPU VM scale sets/node pools, Azure Blob Storage, Azure Container Registry (ACR), Microsoft Entra ID, Azure Managed Identity, Azure Monitor, VNets, and private endpoints.

## Reference architecture

```text
VNet
├── private AKS subnets
│   ├── CPU node pool
│   └── GPU node pool
├── ingress/load balancing
└── private endpoints

Blob Storage → datasets / models / checkpoints
ACR → images
Entra ID + Managed Identity → permissions
Azure Monitor → telemetry
```

## AKS GPU principles

Use dedicated GPU node pools when GPU workloads need different scaling, security, or scheduling behavior from CPU workloads.

Use Kubernetes labels, taints, tolerations, affinity, and resource requests to keep scheduling intentional.

## Terraform categories

Common resource categories include:

```text
VNet
subnets
network security
AKS
node pools
GPU VM scale sets
storage accounts / containers
ACR
managed identities
monitoring
private endpoints
```

## Azure-specific senior concerns

- GPU VM SKU quotas and regional availability
- AKS node-pool design
- Managed Identity scope
- private cluster/private endpoints
- Blob access patterns
- Managed Disks vs Azure Files or other shared storage
- Spot VM interruption
- Azure Monitor cost
- GPU driver/CUDA/container compatibility
- network egress

## Primary Azure references

- AKS GPU architecture: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-gpu/gpu-aks
- AKS best practices: https://learn.microsoft.com/en-us/azure/aks/best-practices

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| AKS | Azure Kubernetes Service. |
| VNet | Azure virtual network. |
| Blob Storage | Azure object storage. |
| ACR | Azure Container Registry. |
| Microsoft Entra ID | Microsoft's cloud identity and access platform. |
| Managed Identity | Azure identity mechanism that avoids storing application credentials. |
| VM scale set | Group of Azure VMs managed as a scalable unit. |
| Spot VM | Interruptible Azure VM capacity for suitable workloads. |
| VM SKU quota | Azure limit on the amount of a VM family or SKU that can be allocated in a subscription/region. |
