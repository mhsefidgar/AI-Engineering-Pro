# Observability and Cost for AI/ML Infrastructure

## Four-layer observability

### Infrastructure

Monitor:

- CPU
- RAM
- GPU utilization
- GPU memory
- disk throughput/latency
- network throughput
- node health

### Kubernetes

Monitor:

- pod pending time
- scheduling failures
- restarts
- evictions
- node pressure
- queue depth
- autoscaler activity

### Model serving

Monitor:

- requests/sec
- input/output tokens
- TTFT
- inter-token latency
- end-to-end latency
- P50/P95/P99
- errors/timeouts
- batch size
- KV-cache utilization

### Business/task layer

Monitor:

- successful task rate
- quality metrics
- safety failures
- cost per successful task
- customer-visible latency

## Cost equation

A practical monthly estimate is:

```text
monthly_cost = compute
             + storage
             + database/search
             + network
             + observability
             + managed services
             + failed/retried work
```

Then divide by useful output:

```text
cost_per_successful_task = monthly_cost / successful_tasks
```

## Idle GPU problem

GPU utilization is not the same as useful model throughput.

A GPU can show activity while the system is bottlenecked by CPU preprocessing, storage, network, synchronization, or application-level queues.

Always correlate GPU utilization with tokens/sec, latency, and successful work.

## Autoscaling

Scale on signals that represent demand or saturation.

For inference, useful signals may include queue depth, concurrency, request rate, tokens/sec, or latency.

For training, autoscaling is usually less about request demand and more about scheduling queued jobs and controlling capacity.

## Cost controls

Use:

- automatic scale-down
- idle-resource detection
- interruptible capacity where appropriate
- resource requests based on measurements
- lifecycle policies for artifacts/logs
- budget alerts
- environment quotas
- maximum replica/job limits

## Senior FinOps review

Ask:

- What percentage of GPU hours produce useful work?
- What causes idle time?
- How much cost comes from failed runs?
- How much data crosses zones/regions?
- Which resources are permanently allocated but rarely used?
- What happens to cost if demand doubles?
- What is the cost of the SLO we chose?

## Terms & Phrases Explained

| Term | Meaning |
|---|---|
| Observability | Ability to understand system behavior from metrics, logs, traces, and events. |
| Saturation | A resource is approaching or exceeding its useful capacity. |
| Queue depth | Number of work items waiting to be processed. |
| Token throughput | Number of generated/processed tokens per unit time. |
| P50 | Median measurement. |
| P95 | Value below which 95% of measurements fall. |
| P99 | Value below which 99% of measurements fall. |
| FinOps | Cloud financial management integrated with engineering decisions. |
| Idle capacity | Allocated resources doing little or no useful work. |
| SLO | Service Level Objective; measurable target for reliability/performance. |
