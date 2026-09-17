# Cloud Architecture for AI/ML

## The common architecture

A production AI platform commonly looks like:

```text
Users / CI
    ↓
DNS / Load Balancer / API Gateway
    ↓
Kubernetes or managed compute
    ↓
Model server / API / workers
    ├── object storage
    ├── vector database / search
    ├── relational database
    ├── cache
    └── queue

Observability spans every layer.
Identity and network controls surround every layer.
```

## Region and zone

A region is a geographic cloud area. A zone is an isolated failure domain within a region.

Use multiple zones when availability requirements justify the additional cost and complexity.

For GPU workloads, also verify that the required accelerator capacity is actually available in the selected zones.

## VPC/VNet

Treat the network as a security and performance boundary.

Typical layout:

```text
Internet
   ↓
Public load balancer
   ↓
Private application subnets
   ↓
Private data services
```

GPU nodes usually do not need public IP addresses.

## Identity

Prefer workload identity over long-lived cloud credentials stored in pods or VM environment variables.

The application should receive only the permissions it needs:

```text
model server → read model artifact
training job → read dataset + write checkpoint
API → read configuration
observability → write metrics/logs
```

## Compute selection

Select compute based on:

- accelerator type
- GPU memory
- GPU count
- CPU cores
- system RAM
- local storage
- network bandwidth
- interconnect characteristics
- availability
- price

Do not compare GPU models using TFLOPS alone. Memory capacity, memory bandwidth, interconnect, software support, and actual workload benchmarks matter.

## Managed services vs Kubernetes

Use managed services when they reduce operational burden without preventing required controls.

Use Kubernetes when you need:

- heterogeneous workloads
- scheduling controls
- GPU node pools
- standardized deployment patterns
- custom operators/controllers
- portability across clouds

Kubernetes is not automatically the cheapest or simplest option for every ML workload.

## AI platform layers

### Data layer

Object storage is generally the durable source for datasets, models, and checkpoints.

### Compute layer

Use CPU and GPU pools separated by workload class.

### Orchestration layer

Kubernetes, batch systems, Ray, or managed ML platforms can schedule workloads.

### Serving layer

Use a model server such as vLLM or another workload-appropriate server.

### MLOps layer

Track datasets, experiments, model artifacts, deployment versions, metrics, and approvals.

## Environment separation

At minimum distinguish:

```text
dev → staging → production
```

Use separate accounts/projects/subscriptions when the organization and risk profile justify strong isolation.

## Senior design principle

Standardize the interface, not necessarily the infrastructure.

For example, every cloud implementation can expose:

```text
make deploy
make benchmark
make destroy
```

while the underlying Terraform modules use EKS, GKE, or AKS.

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Region | Geographic cloud location containing cloud infrastructure. |
| Availability zone | Isolated infrastructure failure domain inside a region. |
| VPC/VNet | Provider network boundary for private IP networking. |
| Subnet | IP address range within a cloud network. |
| North-south traffic | Traffic entering or leaving the platform. |
| East-west traffic | Traffic between services or nodes inside the platform. |
| Workload identity | Mechanism allowing workloads to obtain cloud permissions without embedded long-lived credentials. |
| Managed service | Cloud service where the provider operates substantial infrastructure for you. |
| Failure domain | Set of components likely to fail together. |
| Blast radius | Scope of systems affected by a failure or change. |
