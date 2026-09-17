# Production Checklists

## Architecture

- [ ] Workload type documented
- [ ] Model/version documented
- [ ] Resource sizing evidence exists
- [ ] Low/base/high demand scenarios calculated
- [ ] Availability requirement documented
- [ ] SLOs documented
- [ ] Failure domains identified
- [ ] Cost model documented

## Terraform

- [ ] Remote state configured
- [ ] State access restricted
- [ ] Provider versions managed
- [ ] Modules reviewed
- [ ] Plan reviewed in CI
- [ ] Production apply protected
- [ ] Secrets excluded from source
- [ ] Drift detection process defined
- [ ] Rollback/recovery plan exists

## Kubernetes

- [ ] CPU/RAM/GPU requests set
- [ ] GPU node pools isolated where appropriate
- [ ] Taints/tolerations reviewed
- [ ] Probes configured
- [ ] PDB configured where appropriate
- [ ] Autoscaling tested
- [ ] Pod security reviewed
- [ ] Network policies reviewed

## AI serving

- [ ] Model artifact immutable/versioned
- [ ] Container image pinned
- [ ] CUDA/driver/runtime compatibility tested
- [ ] TTFT measured
- [ ] P95/P99 latency measured
- [ ] Throughput measured
- [ ] Concurrency limits configured
- [ ] Request/token limits configured
- [ ] Timeouts configured
- [ ] Backpressure configured
- [ ] Rollback tested

## Security

- [ ] Workload identity used
- [ ] Least privilege enforced
- [ ] Secrets manager integrated
- [ ] Private networking used where required
- [ ] Encryption configured
- [ ] Audit logging enabled
- [ ] Images/dependencies scanned
- [ ] Sensitive logs reviewed

## Cost

- [ ] GPU idle utilization measured
- [ ] Autoscaling tested
- [ ] Interruptible capacity evaluated
- [ ] Storage lifecycle policy defined
- [ ] Egress reviewed
- [ ] Budget alerts configured
- [ ] Cost per successful task calculated

## Incident response

When a system fails, capture:

```text
what changed?
what failed?
which resources were saturated?
which pods/nodes were affected?
what did users experience?
what was the rollback?
what prevented automatic recovery?
what permanent fix is required?
```

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| SLO | Target for service reliability/performance. |
| PDB | Policy limiting voluntary pod disruption. |
| Backpressure | Mechanism preventing overloaded systems from accepting unlimited work. |
| Rollback | Returning to a previously known-good version. |
| Blast radius | Scope of impact from a failure/change. |
| Immutable artifact | Artifact whose contents are not changed after publication. |
