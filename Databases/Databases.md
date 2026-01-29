### **🌐 AI Databases Mega Table — Vector \+ Graph**

| Database / Tool | Retrieval System / Index | Quantization / Compression | Vector Support | Graph Support | Hybrid Search | Scale | p95 Latency (typical) | Throughput (QPS) | Strength / Notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **FAISS** | HNSW, IVF, PQ / OPQ | PQ, OPQ, IVF | ✅ | ❌ | ❌ | In-memory | \~10–20 ms | \~20k–50k | Fastest raw vector search; no DB features; requires custom wrapper |
| **Milvus** | HNSW, IVF, DiskANN | PQ, SQ, IVF+PQ | ✅ | ❌ | ✔️ (metadata filters) | Very high (distributed) | \~25–80 ms | \~10k–20k | Enterprise-scale; highly configurable; supports massive datasets |
| **Qdrant** | HNSW | PQ, SQ, Binary | ✅ | ❌ | ✔️ | High | \~30–40 ms | \~8k–15k | Rust-based; memory efficient; supports filtering |
| **Weaviate** | HNSW | PQ, Scalar | ✅ | ✅ (class-based graph) | ✔️ (vector \+ metadata \+ semantic) | High | \~50–70 ms | \~3k–8k | Hybrid vector \+ graph \+ semantic search; built-in embeddings and GraphQL |
| **Pinecone** | Proprietary ANN | Managed / opaque | ✅ | ❌ | ✔️ | Very high (managed) | \~40–80 ms | \~5k–10k | Fully managed cloud service; zero-ops but vendor-locked |
| **Redis Vector Search** | HNSW | Basic (float → lower-bit) | ✅ | Partial (via RedisGraph module) | ✔️ | High (in-memory) | \<1 ms | \~8k | Ultra-low latency; supports simple graph \+ vector queries |
| **pgvector (PostgreSQL)** | HNSW / IVF (extension) | Limited | ✅ | ❌ | ✔️ (via SQL filters) | Moderate | \~10–45 ms | \~3k–5k | SQL ecosystem integration; simpler hybrid queries; slower at scale |
| **Chroma** | HNSW (embedded) | Basic / lightweight | ✅ | ❌ | Partial | Moderate | \~50–100 ms | Lower | Easy local/dev setup; not suitable for massive datasets |
| **Neo4j** | Graph traversal / pattern matching | N/A | ❌ | ✅ | Partial (via plugin or custom ANN) | High | \~50–150 ms | \~1k–5k | Mature graph DB; excellent for relationships, recommendations, fraud detection |
| **TigerGraph** | GSQL / parallel graph traversal | N/A | Partial (vector extensions) | ✅ | Partial (vector analytics via extensions) | Very high | \~50–100 ms | \~1k–10k | Real-time enterprise recommendations; massively parallel graph processing |
| **ArangoDB** | AQL / traversal | N/A | Partial (via Foxx or extensions) | ✅ | Partial | Moderate | \~50–120 ms | \~500–3k | Multi-model flexibility: document \+ graph \+ vector |
| **OrientDB** | SQL \+ graph traversal | N/A | ❌ | ✅ | Partial | Moderate | \~80–150 ms | \~500–2k | Multi-model (graph \+ document); lightweight graph analytics |
| **JanusGraph** | Gremlin traversal | N/A | Partial (via Lucene / Elasticsearch / FAISS) | ✅ | Partial | Very high | \~50–150 ms | \~1k–5k | Big data graph analytics; integrates with scalable storage backends |
| **RedisGraph** | Cypher-like traversal | N/A | Partial (via RedisVector) | ✅ | Partial | High (in-memory) | \<1 ms | \~5k–8k | Fast in-memory graph \+ vector hybrid; limited persistence |

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



