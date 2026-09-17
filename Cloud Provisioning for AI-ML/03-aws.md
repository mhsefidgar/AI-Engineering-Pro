# AWS Provisioning for AI/ML

AWS building blocks commonly used for AI/ML include Amazon EKS, Amazon EC2 GPU instances, Amazon S3, Amazon ECR, AWS IAM, Amazon CloudWatch, Amazon VPC, load balancing, and autoscaling/capacity tooling.

## Reference architecture

```text
VPC
├── private subnets
│   ├── EKS control plane / data plane integration
│   ├── CPU node group
│   └── GPU node group
├── public edge
│   └── load balancer
└── VPC endpoints / NAT as required

S3 → datasets / models / checkpoints
ECR → container images
IAM → workload permissions
CloudWatch → logs / metrics
```

## Terraform resources to understand

Learn the AWS provider and EKS modules, then understand the underlying resources rather than blindly copying modules.

Typical categories:

```text
aws_vpc
aws_subnet
aws_route_table
aws_iam_role
aws_s3_bucket
aws_ecr_repository
aws_eks_cluster
aws_eks_node_group
```

For GPU capacity, evaluate managed node groups, Karpenter, or other scheduling/capacity approaches based on workload requirements.

## GPU node-group principles

Keep GPU nodes isolated from general CPU workloads when appropriate.

Use labels and taints such as:

```text
accelerator=gpu
workload=training
```

Then use Kubernetes scheduling rules so only intended workloads consume expensive GPU nodes.

## S3 data layout

A practical structure:

```text
s3://bucket/
  datasets/<dataset-version>/
  models/<model-version>/
  checkpoints/<run-id>/
  evaluations/<run-id>/
  logs/<date>/
```

Do not use mutable `latest` paths as the only reference to production artifacts.

## AWS-specific senior concerns

- Service Quotas and regional GPU capacity
- EBS vs EFS vs S3 semantics
- S3 request/data-transfer patterns
- cross-AZ network charges
- EC2 Spot interruption behavior
- IAM policy scope
- private ECR/S3 access
- CloudWatch cardinality and cost
- Karpenter provisioning behavior
- AMI/driver compatibility
- CUDA/container compatibility

## Capacity decision

If a training job can restart safely from checkpoints, EC2 Spot capacity may be appropriate. If interruption causes unacceptable recovery time or the workload requires guaranteed capacity, use On-Demand capacity or another capacity model appropriate to the availability requirement.

The decision must be based on checkpoint interval, restart time, interruption probability, availability requirements, and cost—not on the word “Spot” alone.

## Primary AWS references

- EKS AI/ML best practices: https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html
- EKS Terraform setup: https://docs.aws.amazon.com/eks/latest/userguide/ml-cluster-setup-tf.html
- Terraform AWS provider best practices: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| EKS | Amazon Elastic Kubernetes Service. |
| EC2 | Amazon Elastic Compute Cloud. |
| S3 | Amazon Simple Storage Service; AWS object storage. |
| ECR | Amazon Elastic Container Registry. |
| IAM | AWS Identity and Access Management. |
| Karpenter | Kubernetes node provisioning and autoscaling technology for AWS environments. |
| EC2 Spot Instances | Spare EC2 capacity offered at a discount and subject to interruption. |
| EBS | Amazon Elastic Block Store; persistent block storage for AWS compute. |
| EFS | Amazon Elastic File System; managed shared file storage. |
| AMI | Amazon Machine Image used to create EC2 instances. |
| Service Quotas | AWS limits on the amount of a service resource that an account can use. |
