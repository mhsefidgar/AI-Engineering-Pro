# Kubernetes and Helm for AI/ML

## GPU scheduling

A GPU workload should declare its resource requirement instead of relying on a node's default configuration.

Conceptually:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

The exact device plugin/operator setup depends on the platform and current Kubernetes ecosystem.

## Node isolation

Use labels, taints, tolerations, and affinity when you need to isolate:

- GPU training
- GPU inference
- CPU preprocessing
- system workloads
- high-priority workloads

## Requests and limits

Requests influence scheduling. Limits constrain resource consumption depending on the resource and configuration.

Do not blindly copy CPU/RAM requests. Profile the workload.

For namespace-level aggregate controls, use the canonical Kubernetes `ResourceQuota` resource. Use `LimitRange` when you need namespace-level defaults or per-container/per-pod constraints.

Example:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: gpu-quota
  namespace: ml-training
spec:
  hard:
    requests.cpu: "32"
    requests.memory: "128Gi"
    requests.nvidia.com/gpu: "4"
```

## Helm chart structure

```text
chart/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    configmap.yaml
    serviceaccount.yaml
    hpa.yaml
    pdb.yaml
```

Use `values.yaml` for environment-specific configuration and keep secrets out of source control.

## Probes

Use:

- startup probes for slow model loading
- readiness probes for traffic eligibility
- liveness probes only when restart behavior is genuinely correct

A model server can be alive while not ready to accept production traffic.

## Autoscaling

CPU-based autoscaling may be insufficient for LLM serving.

Consider workload-specific signals such as:

- queue depth
- requests in flight
- tokens/sec
- GPU utilization
- latency

Scale using signals that correlate with user demand and service capacity.

## Job scheduling

Training should often use Jobs or a specialized batch/distributed scheduler rather than a long-running Deployment.

For queues of expensive jobs, learn priority, `ResourceQuota`, and fair-scheduling mechanisms.

## Helm upgrade safety

Before changing a production model server:

```text
render → validate → deploy to staging → smoke test → load test → rollout → monitor → rollback if needed
```

## Primary references

- Kubernetes GPU scheduling: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
- Kubernetes ResourceQuota: https://kubernetes.io/docs/concepts/policy/resource-quotas/
- Kubernetes LimitRange: https://kubernetes.io/docs/concepts/policy/limit-range/
- Helm: https://helm.sh/docs/

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Kubernetes | Container orchestration platform. |
| Pod | Smallest deployable Kubernetes unit. |
| Deployment | Kubernetes controller for maintaining a set of replicated pods. |
| Job | Kubernetes workload intended to run to completion. |
| ResourceQuota | Kubernetes namespace-level policy that limits aggregate resource consumption and/or object counts. |
| LimitRange | Kubernetes policy that sets default or minimum/maximum resource constraints within a namespace. |
| Taint | Node property that repels workloads unless they tolerate it. |
| Toleration | Pod rule allowing scheduling onto a tainted node. |
| Affinity | Scheduling preference/constraint based on node or pod attributes. |
| Probe | Kubernetes health check. |
| Readiness | Whether a pod should receive traffic. |
| Liveness | Whether Kubernetes considers a container healthy enough to keep running. |
| Helm | Kubernetes package manager and templating system. |
| HPA | Horizontal Pod Autoscaler. |
| PDB | PodDisruptionBudget; limits voluntary disruption of selected pods. |
