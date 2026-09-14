# RAG Backend Lab

Build a retrieval API rather than a notebook-only RAG demo.

## Architecture

```text
POST /v1/answers
  -> authenticate
  -> validate question
  -> retrieve top-k chunks
  -> rerank/filter
  -> assemble bounded context
  -> LLM generation
  -> citations + usage metadata
```

## Data pipeline

1. Ingest documents.
2. Normalize and chunk them.
3. Generate embeddings.
4. Store vectors plus document metadata.
5. Retrieve candidates.
6. Apply metadata filters and optional reranking.
7. Generate an answer with citations.

## Hands-on requirements

- tenant/user isolation;
- document versioning;
- chunk IDs and source metadata;
- configurable `top_k`;
- context/token budget;
- citation references;
- ingestion job queue;
- duplicate-document handling;
- deletion propagation;
- retrieval and generation metrics.

## Evaluation

Create a small golden dataset of questions, expected source documents, and answer requirements. Measure retrieval recall/precision and answer faithfulness separately.

## Failure drills

Test empty retrieval, stale embeddings, deleted documents, embedding-provider outage, model timeout, and oversized context.