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

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Inference | Running a trained model to produce predictions or generated text. |
| Serving | Making model inference available to applications through a service or API. |
| Quantization | Using lower numerical precision to reduce model memory and potentially improve efficiency. |
| 4-bit / 8-bit | Common low-precision representations that use approximately four or eight bits per quantized value. |
| vLLM | An inference engine designed for efficient, high-throughput LLM serving. |
| Time to first token (TTFT) | Time from request arrival until the first generated token is available. |
| Inter-token latency | Time between successive generated tokens. |
| End-to-end latency | Total time from receiving a request to completing the response. |
| Throughput | Amount of work processed per unit time, such as tokens or requests per second. |
| Concurrency | Number of requests being processed at the same time. |
| P50/P95/P99 | Latency percentiles: the 50th, 95th, and 99th percentile request times. |
| KV cache | Cached attention key/value tensors reused during generation, reducing repeated computation but consuming memory. |
| Batching | Processing multiple requests together to improve hardware utilization. |
| Streaming | Sending generated output incrementally instead of waiting for the complete response. |
| Backpressure | A mechanism that limits incoming work when the service cannot safely process more requests. |
| Rate limiting | Restricting how many requests a client can make within a defined period. |
| Adapter serving | Loading a parameter-efficient adapter alongside a compatible base model during inference. |
| Rollback | Returning service traffic to a previously validated model or configuration. |
| Context window | The maximum amount of token context the model can process for a request. |
