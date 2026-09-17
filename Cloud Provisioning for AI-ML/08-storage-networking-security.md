# Storage, Networking, and Security

## Storage decision table

| Need | Typical choice |
|---|---|
| Durable datasets/models | Object storage |
| Low-latency VM-attached data | Block/local storage |
| Shared POSIX filesystem | Managed shared filesystem |
| Temporary cache | Local ephemeral storage |
| Metadata/transactions | Database |
| Async work | Queue |

The exact service depends on provider and workload.

## Object storage pattern

Use versioned paths and immutable artifacts:

```text
bucket/datasets/v17/...
bucket/models/model-2026-09-17/...
bucket/checkpoints/run-abc/step-10000/...
```

## Network checklist

Measure:

- ingress bandwidth
- egress bandwidth
- node-to-node bandwidth
- cross-zone traffic
- cross-region traffic
- model startup transfer time
- data-loader throughput
- DNS latency
- load-balancer latency

## Security layers

```text
identity
  ↓
network boundary
  ↓
service authorization
  ↓
workload identity
  ↓
secret manager
  ↓
encryption
  ↓
audit logging
```

## Least privilege

A training job should not automatically have permission to delete production datasets.

A serving pod should not automatically have permission to modify Terraform state.

Separate identities by function.

## Kubernetes security

Learn:

- RBAC
- ServiceAccounts
- NetworkPolicy
- admission controls/policy engines
- image provenance/scanning
- Pod Security standards
- secret handling

## AI-specific threat model

Consider:

- model artifact tampering
- malicious container images
- prompt injection
- data poisoning
- training data leakage
- model endpoint abuse
- excessive inference cost
- insecure retrieval sources
- sensitive logs
- credentials in prompts or environment variables

## Medical/regulated workloads

Use the organization's approved controls for PHI/PII, retention, access, audit, encryption, data residency, and incident response. Cloud certification or a managed service feature does not by itself make an application compliant.

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Object storage | Durable storage accessed through an object API rather than a normal filesystem. |
| Block storage | Disk-like storage attached to compute. |
| Ephemeral storage | Storage whose lifecycle is tied to a machine or workload and should not be treated as durable. |
| Egress | Data leaving a network or cloud boundary. |
| RBAC | Role-Based Access Control. |
| NetworkPolicy | Kubernetes mechanism for controlling pod network communication. |
| Least privilege | Giving an identity only the permissions it needs. |
| Workload identity | Cloud identity mechanism assigned to an application workload. |
| Data poisoning | Deliberately or accidentally introducing harmful data into training/evaluation pipelines. |
| Artifact provenance | Evidence of where and how a software/model artifact was produced. |
