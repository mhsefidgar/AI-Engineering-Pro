# RAG General Considerations 
## **1\. Indexing Pipeline (The "Write" Path)**

In production, indexing is an asynchronous, event-driven process. You cannot simply "upload a PDF"; you must ensure the data is searchable and secure.

* **Extraction & Cleaning:** Use robust parsers (like **Unstructured** or **LlamaParse**) to handle messy PDFs, tables, and headers.  
* **Chunking Strategy:** \* **Semantic Chunking:** Break text based on meaning (using **sentence embeddings**) rather than fixed character counts.  
  * **Contextual Prepending:** Prepend the document title or a summary to every chunk so the retriever knows the "global" context of a single paragraph.  
* **Metadata Enrichment:** Tag chunks with user\_id, permissions, timestamp, and document\_type. This is critical for **filtering** (e.g., "only search my private files").  
* **Storage:** Use a production-grade vector database (e.g., Pinecone, Weaviate, or Qdrant) with an **HNSW index** for sub-second search speeds.

---

## **2\. Retrieval & Ranking (The "Read" Path)**

Semantic search alone is often insufficient for production. You need a multi-stage "Funnel" approach.

* **Hybrid Search:** Combine **Dense Retrieval** (semantic similarity via embeddings) with **Sparse Retrieval** (keyword matching via BM25). This ensures you find both concepts and specific names/jargon.  
* **Ranking (The Reranker):** Initial retrieval might return 50 chunks. Passing all 50 to an LLM is expensive and noisy.  
  * Use a **Cross-Encoder reranker** (like BGE-Reranker or Cohere Rerank) to score the top 50 and narrow them down to the 5 most relevant.  
* **Query Transformation:** If a user asks a vague question, use a small LLM to "rewrite" the query into a better search term before hitting the database.

---

## **3\. Relevance Iteration (The "Optimization" Loop)**

Production RAG is never "done." You iterate by adjusting "knobs" based on data.

* **The "Long Context" Problem:** LLMs often ignore the middle of a long prompt ("Lost in the Middle"). If your relevance is low, try decreasing chunk size or moving the most relevant chunks to the top of the prompt.  
* **Prompt Versioning:** Treat your prompts like code. Use tools like LangSmith or Weights & Biases to track which version of a prompt produces better answers.  
* **Domain-Specific Embeddings:** If your data is highly technical (medical, legal), consider fine-tuning your embedding model or using a "Query-to-Document" adapter.

---

## **4\. Evaluation (The "Feedback" Path)**

You cannot ship what you cannot measure. Use the **RAG Triad** to evaluate performance without needing thousands of human labels.

| Metric | What it measures | How to fix if low |
| :---- | :---- | :---- |
| **Context Relevance** | Is the retrieved info actually useful for the question? | Improve your chunking or reranker. |
| **Groundedness** | Is the LLM's answer derived *only* from the context? | Tighten the system prompt to prevent hallucination. |
| **Answer Relevance** | Does the answer actually address the user's intent? | Improve the generation prompt or model choice. |

**Pro Tip:** Use **LLM-as-a-Judge** (using GPT-4o or Claude 3.5 Sonnet) to automatically score these metrics on a daily "Golden Dataset" of your top 100 most important questions.

