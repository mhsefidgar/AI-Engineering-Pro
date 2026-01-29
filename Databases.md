### **📊 AI Vector Database Comparison — Performance & Features (2025–2026)**

| Database / Tool | Retrieval System / Index | Quantization | Hybrid Search | Scale | p95 Latency (typical) | Throughput (QPS) | Strength / Notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **FAISS** | HNSW, IVF, PQ/OPQ | PQ, OPQ, SQ | ❌ | In‑memory | \~10–20 ms (in‑memory) | \~20k‑50k (local) | Fastest raw vector search; no DB features; requires custom wrapper. |
| **Milvus** | HNSW, IVF, DiskANN | PQ, SQ | ✔️ (via Brute filters) | Very high (distributed) | \~25–80 ms | \~10k‑20k | Enterprise scale, highly configurable, stronger for very large data. |
| **Qdrant** | HNSW | SQ, PQ & binary | ✔️ | High | \~30–40 ms (vector) | \~8k‑15k | Rust‑based, excellent speed & filtering; efficient quantization support. |
| **Weaviate** | HNSW | PQ & scalar | ✔️ (BM25 \+ vector) | High | \~50–70 ms | \~3k‑8k | Hybrid search \+ GraphQL schemas; strong metadata \+ semantic. |
| **Pinecone** | Proprietary ANN (HNSW‑like) | Managed / opaque | ✔️ | Very high (managed) | \~40–80 ms | \~5k‑10k | Fully managed cloud, easy setup but vendor lock‑in. |
| **Redis Vector Search** | HNSW | Basic | ✔️ | High (in‑memory) | \<1 ms avg. | \~8k | Ultra‑low latency (in‑memory), good for small/real‑time. |
| **pgvector (PostgreSQL)** | HNSW / IVF (extension) | Limited | ✔️ | Moderate | \~10–45 ms | \~3k–5k | SQL ecosystem integration; slower at scale. |
| **Chroma** | HNSW (embedded) | Basic | Partial | Moderate | \~50–100 ms | lower | Easy local/dev setup, not for massive scale. |

---

### **📌 How to Interpret These Metrics**

**🧠 Retrieval System / Index**

* Most vector databases rely on **ANN algorithms** like **HNSW** (graph‑based) or **IVF** for efficient high‑dimensional search.

* Tools that leverage multiple indexing types (e.g., Milvus) offer greater flexibility for tuning speed vs accuracy.

**📉 Latency (p95)**

* Lower p95 latency means faster responses under load. FAISS in pure in‑memory scenarios is typically fastest.

* Managed services and hybrid search workflows like Pinecone and Weaviate trade some speed for ease and features.

**📊 Throughput (QPS)**

* Throughput depends on hardware, parallelism, and indexing type.

* Qdrant often leads in raw throughput among open‑source options, while Milvus can scale high with distributed setups.

**🔁 Hybrid Search**

* Means combining semantic vector similarity with traditional filtering or keyword search (e.g., **BM25 \+ vectors**): available in Weaviate, Pinecone, Milvus (via SDKs), Redis, pgvector, etc.

**💾 Scalability**

* **FAISS** excels in speed but does *not* provide persistence/DB features.

* **Milvus** is built for massive enterprises (billions+ vectors) with sharding and cluster capabilities.

---

### **🧩 When to Choose What**

| Use Case | Recommended Database |
| ----- | ----- |
| **Ultra low‑latency vector search (in‑memory)** | FAISS, Redis |
| **Hybrid semantic \+ keyword \+ filters** | Weaviate, Pinecone, Redis, pgvector |
| **Massive scale (100M+ vectors)** | Milvus, Pinecone (managed) |
| **High throughput / cost‑efficient self‑hosted** | Qdrant |
| **SQL‑centric teams** | pgvector |
| **Quick proto / embedded dev** | Chroma |

---

### **🧠 Tips for Benchmarking Your Use Case**

1. **Dataset Size & Dimensionality** – Benchmarks vary widely with vector count and embedding dimension (e.g., 768 vs 1536). Always test with your actual data distribution.

2. **Latency vs Recall Trade‑off** – Quantization speeds up search but can slightly lower recall — tune according to how much accuracy matters vs speed.

3. **Filtering Complexity** – If heavy metadata filters are needed (e.g., boolean \+ geo \+ ranges), Qdrant and Weaviate are strong choices. 

