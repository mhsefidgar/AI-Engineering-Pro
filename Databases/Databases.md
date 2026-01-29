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


### **🧠 Vector Quantization Techniques Explained**

| Technique | Full Name | How It Works | Use Case / Strength | Limitations / Trade-offs |
| ----- | ----- | ----- | ----- | ----- |
| **PQ** | Product Quantization | Splits a high-dimensional vector into smaller sub-vectors, then quantizes each sub-vector into a codebook (cluster centers). Distance between vectors is approximated via precomputed distances between codewords. | Reduces memory drastically; fast approximate search. Ideal for billion-scale datasets. | Approximation can reduce recall slightly; requires proper choice of sub-vector splits. |
| **OPQ** | Optimized Product Quantization | Adds a **rotation matrix** to vectors before PQ. Rotates the vector space to reduce quantization error, then applies PQ. | Higher accuracy than PQ at similar compression. Often used when recall matters. | Slightly more computational overhead; needs training for rotation matrix. |
| **SQ** | Scalar Quantization | Each vector dimension is quantized individually to discrete levels (e.g., 8-bit or 16-bit). | Simple, very fast; reduces storage per dimension. | Less efficient than PQ/OPQ for very high-dimensional vectors; accuracy loss can be higher. |
| **Binary / LSH** | Locality Sensitive Hashing / Binary Quantization | Maps vectors to binary codes via hashing or projection. Distance approximated by Hamming distance. | Extremely fast, memory-light; useful for embedded or real-time systems. | Often lower recall; less precise for very similar vectors. |
| **IVF (Inverted File \+ PQ)** | Inverted File Index | Vectors are clustered into “cells” (coarse quantization). PQ or OPQ is applied **within each cell**. | Reduces number of distance computations drastically; efficient for large datasets. | Needs careful tuning of \#clusters; extra complexity in training. |

---

### **🔹 Visual Intuition**

1. **PQ**: “Cut the vector into pieces, compress each piece.”

2. **OPQ**: “Rotate the space, then do PQ — reduces distortion.”

3. **SQ**: “Each dimension gets its own bucket/step.”

4. **IVF+PQ**: “Group similar vectors, then compress each group.”

   ---

   ### **⚡ When They’re Used in Databases**

| Database | Supported Quantization Techniques | Notes |
| ----- | ----- | ----- |
| **FAISS** | PQ, OPQ, SQ, IVF+PQ | Highly flexible; can mix IVF \+ PQ/OPQ. |
| **Milvus** | PQ, SQ, OPQ, IVF+PQ | Supports hybrid ANN indexes with quantization. |
| **Weaviate** | PQ | Mostly for HNSW compressed vectors. |
| **Qdrant** | PQ, Binary, SQ | Optimized for memory vs speed. |
| **Pinecone** | Provider-managed | Abstracted; they handle compression internally. |



