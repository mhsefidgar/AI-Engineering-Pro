# Terraform for AI/ML Infrastructure

Terraform should make infrastructure reproducible, reviewable, and replaceable. It should not become a giant file containing every resource in the platform.

## Suggested repository structure

```text
terraform/
  modules/
    network/
    object-storage/
    container-registry/
    kubernetes-cluster/
    gpu-node-pool/
    observability/
  environments/
    dev/
    staging/
    prod/
```

Cloud-specific implementations can live under provider-specific directories when abstractions stop being useful.

## State

Treat Terraform state as sensitive infrastructure data.

Production practices:

- remote backend
- locking where supported
- encrypted state
- restricted access
- separate state for appropriate blast-radius boundaries
- automated plan review
- controlled apply
- state backup/recovery strategy

Never commit local state or secret-bearing state to a public repository.

## Module design

A good module should expose business-relevant inputs rather than every provider argument.

Example:

```hcl
module "gpu_pool" {
  source = "../../modules/gpu-node-pool"

  cluster_name = var.cluster_name
  gpu_type     = var.gpu_type
  min_size     = 0
  max_size     = var.max_gpu_nodes
  labels = {
    accelerator = "gpu"
  }
}
```

The module should document assumptions, supported combinations, outputs, security implications, and upgrade behavior.

## Variables

Avoid hard-coding:

- region
- environment
- project/account/subscription IDs
- GPU SKU
- node counts
- CIDRs
- bucket names
- image tags

Prefer typed variables with validation.

## Terraform CI/CD

A production pipeline commonly looks like:

```text
format → validate → lint → security scan → plan → review → apply
```

For production, require approval before apply and record the exact commit that produced the infrastructure change.

## Drift

Infrastructure can change outside Terraform. Detect and reconcile drift rather than assuming state equals reality.

## Secrets

Do not pass long-lived secrets through Git, Terraform variables, or Helm values when a workload identity/secret manager integration is available.

## Import and migration

Learn how to bring existing resources under management carefully. Before importing, understand ownership and whether Terraform should control every attribute.

## Senior Terraform review

Ask:

- What is the module's blast radius?
- Can this change replace a production resource?
- What happens to state if apply fails halfway?
- Are dependencies explicit?
- Is the resource immutable or mutable?
- Are provider versions pinned appropriately?
- Is the plan deterministic enough to review?
- Can dev/staging/prod drift unintentionally?
- Does the module hide an important security setting?

## Primary reference

Terraform documentation: https://developer.hashicorp.com/terraform/docs

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Provider | Terraform plugin that knows how to manage a platform such as AWS, GCP, or Azure. |
| Resource | A managed infrastructure object. |
| Module | Reusable collection of Terraform resources and configuration. |
| State | Terraform's record of managed infrastructure and relationships. |
| Drift | Difference between Terraform's intended state and actual infrastructure. |
| Plan | Preview of proposed infrastructure changes. |
| Apply | Operation that makes approved Terraform changes. |
| Blast radius | Scope of resources potentially affected by a change. |
| Backend | Mechanism used to store Terraform state. |
