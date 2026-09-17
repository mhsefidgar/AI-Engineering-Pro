# Hands-on Labs

These labs are intentionally progressive. Use the same application contract across AWS, GCP, and Azure so the learner sees what is cloud-specific and what is a general engineering principle.

## Lab 1 — Size a model

Given a model, context length, precision, batch/concurrency, and target throughput:

- estimate memory
- identify likely bottleneck
- propose GPU count
- calculate storage
- estimate network needs
- create low/base/high scenarios

Deliverable: `sizing.md`.

## Lab 2 — Terraform local structure

Build reusable modules for:

- network
- object storage
- container registry
- Kubernetes cluster
- node pool

Do not provision production resources yet.

Deliverable: validated Terraform modules.

## Lab 3 — AWS

Provision a minimal EKS environment with CPU and GPU capacity, then deploy a sample workload.

Measure:

- provisioning time
- node startup time
- GPU availability
- pod scheduling time
- workload startup time
- cost

Destroy everything afterward.

## Lab 4 — GCP

Repeat the same contract on GKE.

Compare:

- Terraform structure
- identity
- GPU scheduling
- storage
- startup time
- capacity constraints
- cost model

## Lab 5 — Azure

Repeat the same contract on AKS.

Document provider-specific differences instead of forcing identical Terraform code.

## Lab 6 — Helm model server

Create a Helm chart for an inference service with:

- Deployment
- Service
- readiness/startup probes
- CPU/RAM/GPU requests
- ConfigMap
- ServiceAccount
- optional autoscaling

## Lab 7 — Load test

Run a controlled concurrency sweep and record:

```text
concurrency
requests/sec
tokens/sec
TTFT
P50
P95
P99
GPU utilization
VRAM
errors
cost estimate
```

Create a graph and identify the saturation point.

## Lab 8 — GPU bottleneck investigation

Create an artificial bottleneck in one layer:

- CPU preprocessing
- storage
- network
- GPU memory
- GPU compute

Use metrics to identify the bottleneck before changing infrastructure.

## Lab 9 — Interruptible training

Run a checkpointed training job using interruptible capacity where the provider supports it.

Simulate interruption and measure recovery time.

## Lab 10 — Failure drill

Practice:

- kill a GPU pod
- remove a GPU node
- break an image tag
- deploy a bad Helm value
- apply a bad Terraform change in a sandbox

Document detection, impact, rollback, and permanent fix.

## Lab 11 — Cost optimization

Compare:

```text
always-on
vs
scheduled
vs
autoscaled
vs
interruptible
```

Use measured workload utilization to explain the difference.

## Lab 12 — Senior architecture review

Write a two-page design for a production LLM platform and defend:

- GPU choice
- node count
- network design
- storage design
- Terraform boundaries
- Helm strategy
- security model
- observability
- scaling strategy
- failure recovery
- cost model

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Load test | Controlled test that measures behavior under concurrent workload. |
| Saturation point | Load level where additional demand causes unacceptable performance or errors. |
| Failure drill | Deliberate exercise that tests whether a system detects and recovers from failure. |
| Recovery time | Time required to restore acceptable service after a failure. |
| Sandbox | Isolated environment intended for experimentation rather than production. |
