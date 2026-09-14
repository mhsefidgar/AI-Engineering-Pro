# AI Backend Engineering

AI features become backend engineering problems as soon as they need authentication, persistence, concurrency, reliability, and observability.

## Topics

- LLM API integration
- Streaming responses
- Request validation
- Token and cost tracking
- Rate limiting
- Background AI jobs and queues
- Embeddings and vector retrieval
- RAG service architecture
- AI response caching
- Prompt/version management
- Model/provider fallbacks
- Production AI observability

## Reference architecture

```text
Client
  -> FastAPI / Express
  -> auth + validation
  -> AI service
     -> cache
     -> queue for long jobs
     -> LLM provider
     -> retrieval/vector store
     -> FastMCP tools when tool interoperability is useful
  -> structured response/stream
```

Keep provider-specific code behind an adapter so the application can test and replace providers without rewriting business logic.