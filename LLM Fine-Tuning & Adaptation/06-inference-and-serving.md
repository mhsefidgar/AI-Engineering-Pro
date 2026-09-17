# 06 — Inference, Quantization, and Serving

Training is only half of the production problem. The adapted model must be served within latency, throughput, memory, security, and cost constraints.

## Serving path

```text
Client
  ↓
API / gateway
  ↓
Auth + rate limits
  ↓
vLLM / inference server
  ↓
Model + optional adapter
  ↓
GPU
```

## Benchmark dimensions

Measure at realistic concurrency:

- Time to first token
- Inter-token latency
- End-to-end latency
- Tokens/second
- Requests/second
- P50/P95/P99 latency
- GPU utilization
- GPU memory
- Input/output token distribution
- Error/timeout rate

## Quantization

Compare supported 4-bit, 8-bit, and higher-precision configurations where relevant. Measure actual task quality after quantization rather than assuming numerical compression is harmless.

## vLLM

Use vLLM as a serving benchmark candidate because it provides an inference engine designed for high-throughput LLM serving and supports a range of model/adapter/quantization configurations.

The repository should contain:

```text
serving/
├── config.yaml
├── Dockerfile
├── healthcheck.py
├── benchmark.py
└── README.md
```

## Production controls

Implement:

- Request authentication
- Rate limiting
- Input size limits
- Output token limits
- Timeouts
- Cancellation
- Backpressure
- Structured logs
- Metrics
- Model/version identifiers
- Safe rollout and rollback

## Adapter serving

Record the exact base-model revision with every adapter. An adapter is not a complete model artifact by itself; compatibility with the base model and serving runtime must be verified.

## Practical bottleneck: context length

Long contexts increase memory use and latency. Before increasing the context window, determine whether the real issue is retrieval quality, chunking, summarization, or unnecessary context.
