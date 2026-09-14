# AI Engineering Pro

> A practical AI engineering laboratory for building, understanding, and experimenting with modern LLM, agentic, RAG, multimodal, backend, database, and Python systems.

[![AI Engineering](https://img.shields.io/badge/AI%20Engineering-LLM%20%7C%20Agents%20%7C%20RAG-blue)](https://github.com/mhsefidgar/AI-Engineering-Pro)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Workflows-0F172A)](https://www.langchain.com/langgraph)
[![RAG](https://img.shields.io/badge/RAG-Practical%20Patterns-7C3AED)](https://github.com/mhsefidgar/AI-Engineering-Pro/tree/main/Practical%20RAG)

## About

**AI Engineering Pro** is a hands-on collection of experiments, tutorials, reference implementations, and practical notebooks focused on turning AI concepts into working engineering systems.

The repository is designed around one idea:

> **Learn the model, understand the system, then engineer the workflow.**

Instead of focusing only on model APIs, the projects explore the surrounding engineering layers that make AI applications useful: orchestration, retrieval, embeddings, vector search, multimodal representations, databases, backend services, cost optimization, tool use, and production-oriented Python practices.

It is both a **learning lab** and a **technical reference library** for engineers who want to move from isolated LLM experiments toward complete AI applications.

## What you will find here

| Area | What it covers |
|---|---|
| **Agents** | Agent patterns, tool use, orchestration, and autonomous workflows |
| **LangGraph** | Stateful graphs, tool-enabled agents, routing, and workflow design |
| **RAG** | Retrieval-augmented generation, semantic search, embeddings, and vector retrieval |
| **Multimodal AI** | Text + image embeddings and multimodal database querying |
| **LLM Engineering** | OpenAI integrations, LangChain components, prompts, tools, and application patterns |
| **Cost Optimization** | Token/time budgeting and efficiency patterns for agentic AI systems |
| **Databases** | PostgreSQL, vector databases, multimodal retrieval, and database integration |
| **Backend Engineering** | Python backend concepts, APIs, decorators, and service-oriented patterns |
| **Python** | Practical Python engineering patterns and reusable implementation notes |
| **Recommendation Systems** | Video recommendation and applied retrieval/ranking ideas |

## Repository map

```text
AI-Engineering-Pro/
│
├── Agents/                         # Agentic AI experiments and patterns
├── LangGraphBasics/                # LangGraph tutorials, tools, and workflows
├── Practical RAG/                  # Retrieval and semantic-search projects
├── RAG/                            # RAG-focused experiments
├── MultimodelDatabaseAIQuery/      # Multimodal embeddings + database queries
├── Cost minimization/              # Token/time/cost optimization for agents
├── Databases/                      # Database-focused AI engineering work
├── BackEnd Programming/            # Backend and API engineering
├── Python Skill/                   # Python engineering reference material
├── Video Recommendation System/    # Recommendation-system experiments
└── llama-index-readerPro/          # LlamaIndex + GitHub repository reading
```

## Featured engineering themes

### 1. Agentic AI and workflow orchestration

The repository explores how an LLM becomes part of a larger system rather than remaining a single prompt-response call. The LangGraph material includes graph-based workflows, state, tools, routing, and model/tool integration.

Example concepts include:

- State-driven agent workflows
- Tool calling
- Conditional routing
- Graph execution
- Agent/tool separation
- LLM-powered decision loops
- OpenAI model integration through LangChain

### 2. Practical RAG

The RAG material focuses on the engineering pipeline behind retrieval-augmented generation:

```text
Documents
   ↓
Chunking / preprocessing
   ↓
Embeddings
   ↓
Vector index / database
   ↓
Semantic retrieval
   ↓
Relevant context
   ↓
LLM generation
```

The repository includes practical work with LangChain, Hugging Face embeddings, FAISS, semantic search, and related retrieval tooling.

### 3. Multimodal AI

The multimodal work extends retrieval beyond text. It includes experiments using CLIP-style representations to create embeddings from text and images and connect those representations with database-backed querying.

```text
Text ───────┐
            ├──► Multimodal Embedding ───► Vector Search ───► Query
Image ──────┘
```

### 4. Cost-aware agent engineering

Agentic systems can become expensive when every step consumes tokens and latency. The cost-minimization material explores token and time budgeting so agent workflows can be designed with explicit resource constraints.

Key questions:

- How many model calls does a workflow really need?
- Where can context be reduced?
- When should retrieval happen?
- How can latency and token usage be bounded?
- Which steps should be deterministic instead of LLM-driven?

### 5. AI + databases

Modern AI applications depend heavily on data infrastructure. This repository connects AI concepts with practical database engineering, including PostgreSQL, vector retrieval, multimodal querying, and database-backed application patterns.

### 6. Python and backend engineering

AI applications still need reliable software engineering underneath them. The repository includes Python-focused material covering reusable patterns, decorators, backend concepts, APIs, and implementation practices that support production-oriented AI systems.

## Technology landscape

```text
                 ┌─────────────────────┐
                 │     AI Applications │
                 └──────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          Agents           RAG        Multimodal AI
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                  LangChain / LangGraph
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
           LLMs         Embeddings       Tools
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                Vector Search / Databases
                            │
                            ▼
                 Python / Backend Systems
```

Technologies represented across the repository include:

- Python
- LangChain
- LangGraph
- OpenAI APIs and models
- Hugging Face
- FAISS
- LlamaIndex
- PostgreSQL
- Vector databases
- FastAPI concepts
- Jupyter notebooks
- CLIP / multimodal embeddings

## Learning paths

### Path A — Start with LLM applications

1. Python Skill
2. LangGraphBasics
3. Agents
4. Practical RAG
5. RAG

### Path B — Become a RAG engineer

1. Embeddings fundamentals
2. Semantic search
3. FAISS
4. Practical RAG
5. Vector databases
6. Multimodal retrieval

### Path C — Build agentic systems

1. LangGraph fundamentals
2. Tools and tool calling
3. Agent workflows
4. Conditional routing
5. Cost and latency budgeting
6. Backend integration

### Path D — Explore multimodal AI

1. Embeddings
2. CLIP representations
3. Text/image retrieval
4. Multimodal database querying
5. Application integration

## Engineering principles

This repository is intentionally broader than a collection of API examples. The projects encourage several engineering habits:

- **Understand the data flow**, not just the model call.
- **Separate orchestration from business logic.**
- **Use retrieval to ground generation when appropriate.**
- **Treat tokens, latency, and infrastructure as engineering resources.**
- **Choose deterministic code where deterministic behavior is valuable.**
- **Keep AI components composable and testable.**
- **Connect AI prototypes to real data and backend systems.**
- **Prefer small, understandable experiments before assembling larger systems.**

## Why this repository is useful

AI engineering sits at the intersection of several disciplines:

```text
          Machine Learning
                 │
                 ▼
       ┌───────────────────┐
       │   AI Engineering  │
       └───────────────────┘
        ▲       ▲       ▲
        │       │       │
     Software  Data   Systems
    Engineering      Engineering
```

A successful AI application rarely depends on the model alone. It depends on how models interact with retrieval, data, tools, state, APIs, databases, cost controls, and application logic.

This repository brings those layers together as a practical engineering playground.

## Getting started

Clone the repository:

```bash
git clone https://github.com/mhsefidgar/AI-Engineering-Pro.git
cd AI-Engineering-Pro
```

Most projects are organized as notebooks or focused examples. Open the relevant directory and follow the notebook or project-specific setup instructions.

For notebook-based experiments, a typical environment can be created with Python and Jupyter:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip jupyter
jupyter notebook
```

Individual notebooks may require additional dependencies. Install the packages specified by the notebook before running it.

## Project philosophy

**From notebooks to systems.**

The goal is not simply to demonstrate that an LLM can answer a question. The goal is to understand what it takes to build an AI system that can retrieve the right information, use tools, maintain state, interact with databases, control cost, and fit into a real software architecture.

That makes this repository useful for:

- AI engineers
- ML engineers
- Backend engineers moving into AI
- Developers learning agentic workflows
- Engineers studying RAG architectures
- Students building practical AI projects
- Researchers prototyping AI application ideas

## Related project

For a deeper example of an end-to-end AI-driven engineering system, see the author's quantitative trading research project:

**[Multi-Agent Quantitative Trading Research](https://github.com/mhsefidgar/Multi-Agent-Quantitative-Trading-Research)**

It applies multi-agent research, backtesting, deterministic risk controls, execution boundaries, persistence, observability, and deployment-oriented architecture to quantitative trading research.

## Repository status

This repository is an evolving engineering notebook and reference collection. Examples may have different levels of completeness, dependency requirements, and production readiness. Always check the individual project or notebook before treating an example as production-ready.

## Contributing

Ideas, improvements, corrections, and new examples are welcome. When adding material, prefer focused examples with clear explanations, reproducible steps, and explicit dependencies.

## License

See the repository's license and individual project files for applicable licensing information.

---

<p align="center">
  <strong>AI Engineering Pro</strong><br/>
  Build agents. Ground them with retrieval. Connect them to data. Engineer the system.
</p>
