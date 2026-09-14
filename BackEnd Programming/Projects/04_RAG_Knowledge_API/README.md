# Project 04 — Multi-tenant RAG Knowledge API

Build a document ingestion and question-answering backend.

## Core workflow

```text
upload -> validate -> queue -> parse/chunk -> embed -> index
question -> retrieve -> rerank/filter -> generate -> cite
```

## Requirements

- tenant isolation;
- document/version metadata;
- asynchronous ingestion;
- vector retrieval;
- citations;
- configurable retrieval and context budgets;
- deletion propagation;
- duplicate detection;
- authentication/authorization;
- usage and cost tracking;
- observability;
- evaluation dataset;
- API and integration tests.

## Evaluation

Create at least 30 representative questions. Track retrieval recall, source relevance, citation coverage, answer quality, latency, token usage, and cost.

## Failure drills

Deleted source, stale index, empty retrieval, embedding outage, provider timeout, poisoned document, prompt injection, cross-tenant retrieval, and oversized context.

## Stretch goals

Add hybrid search, reranking, streaming answers, feedback capture, and offline regression evaluation in CI.