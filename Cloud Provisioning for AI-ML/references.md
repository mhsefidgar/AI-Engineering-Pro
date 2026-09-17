# Primary References

Use primary documentation for implementation details because cloud APIs, GPU availability, Kubernetes integrations, and provider recommendations change over time.

## AWS

- EKS AI/ML best practices: https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html
- EKS Terraform setup for ML clusters: https://docs.aws.amazon.com/eks/latest/userguide/ml-cluster-setup-tf.html
- AWS Terraform provider best practices: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html
- EKS documentation: https://docs.aws.amazon.com/eks/
- EC2 documentation: https://docs.aws.amazon.com/ec2/
- S3 documentation: https://docs.aws.amazon.com/s3/
- IAM documentation: https://docs.aws.amazon.com/iam/

## GCP

- GKE GPUs: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus
- GKE GPU concepts: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus
- Terraform best practices: https://docs.cloud.google.com/docs/terraform/best-practices/working-with-resources
- GKE documentation: https://cloud.google.com/kubernetes-engine/docs
- Compute Engine documentation: https://cloud.google.com/compute/docs
- Cloud Storage documentation: https://cloud.google.com/storage/docs
- IAM documentation: https://cloud.google.com/iam/docs

## Azure

- AKS GPU architecture: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-gpu/gpu-aks
- AKS best practices: https://learn.microsoft.com/en-us/azure/aks/best-practices
- AKS documentation: https://learn.microsoft.com/en-us/azure/aks/
- Azure VMs documentation: https://learn.microsoft.com/en-us/azure/virtual-machines/
- Blob Storage documentation: https://learn.microsoft.com/en-us/azure/storage/blobs/
- Managed identities: https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/

## Infrastructure / Kubernetes

- Terraform: https://developer.hashicorp.com/terraform/docs
- Terraform language: https://developer.hashicorp.com/terraform/language
- Helm: https://helm.sh/docs/
- Kubernetes GPU scheduling: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
- Kubernetes resource management: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Kubernetes scheduling: https://kubernetes.io/docs/concepts/scheduling-eviction/

## AI serving

- vLLM documentation: https://docs.vllm.ai/

## How to use these references

For each production implementation, record:

```text
provider
service
region/zone
resource/SKU
provider documentation URL
Terraform provider/module version
container image version
CUDA/driver/runtime versions
model revision
benchmark date
```

Cloud sizing should be revalidated when model architecture, software stack, accelerator generation, workload shape, or traffic changes.

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Primary source | Documentation maintained by the organization that provides or owns the technology. |
| SKU | Provider-specific identifier for a resource configuration/product. |
| Accelerator generation | Hardware generation of a GPU or other ML accelerator. |
| Runtime | Software environment that executes the workload. |
| Version pinning | Explicitly selecting versions instead of relying on moving defaults. |
| Reproducibility | Ability to recreate a result or environment from recorded inputs and configuration. |
