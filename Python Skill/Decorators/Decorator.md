# **1️⃣ `@staticmethod`**

Used when a method does not depend on instance state.

### **✅ When used in LLM/RAG?**

* Utility functions

* Prompt formatting helpers

* Embedding preprocessing

class PromptBuilder:

   @staticmethod  
   def format\_prompt(query: str, context: str) \-\> str:  
       return f"""  
       Answer the question based on the context.

       Context:  
       {context}

       Question:  
       {query}  
       """

\# Usage  
prompt \= PromptBuilder.format\_prompt("What is RAG?", "RAG combines retrieval and generation.")  
print(prompt)  
---

# **2️⃣ `@classmethod`**

Used when a method needs access to the class (`cls`) instead of instance.

### **✅ When used?**

* Model factory methods

* Creating LLM instances with configs

* Loading embedding models

class LLMModel:

   def \_\_init\_\_(self, model\_name):  
       self.model\_name \= model\_name

   @classmethod  
   def from\_env(cls):  
       import os  
       return cls(os.getenv("LLM\_MODEL", "gpt-4"))

\# Usage  
llm \= LLMModel.from\_env()  
print(llm.model\_name)  
---

# **3️⃣ `@property`**

Used to access a method like an attribute.

### **✅ When used?**

* Lazy loading embeddings

* Cached vector index access

* Model metadata

class VectorStore:

   def \_\_init\_\_(self):  
       self.\_index \= None

   @property  
   def index(self):  
       if self.\_index is None:  
           print("Loading vector index...")  
           self.\_index \= "FAISS\_INDEX"  
       return self.\_index

store \= VectorStore()  
print(store.index)  
---

# **4️⃣ `@lru_cache` (from `functools`)**

Used to cache expensive function results.

### **✅ VERY common in LLM systems**

* Cache embedding results

* Cache vector search

* Cache prompt templates

from functools import lru\_cache

@lru\_cache(maxsize=128)  
def compute\_embedding(text: str):  
   print("Computing embedding...")  
   return hash(text)

\# First call  
print(compute\_embedding("hello"))

\# Cached  
print(compute\_embedding("hello"))  
---

# **5️⃣ `@dataclass` (from `dataclasses`)**

Used for structured data models.

### **✅ Common in:**

* RAG document schema

* LLM request objects

* API request models

from dataclasses import dataclass

@dataclass  
class Document:  
   id: str  
   content: str  
   metadata: dict

doc \= Document("1", "RAG explanation", {"source": "kb"})  
print(doc)  
---

# **6️⃣ `@abstractmethod` (from `abc`)**

Used for defining LLM interfaces.

### **✅ Used when building:**

* Custom LLM wrappers

* Base retriever classes

* Embedding interfaces

from abc import ABC, abstractmethod

class BaseRetriever(ABC):

   @abstractmethod  
   def retrieve(self, query: str):  
       pass

class SimpleRetriever(BaseRetriever):

   def retrieve(self, query: str):  
       return \["doc1", "doc2"\]

retriever \= SimpleRetriever()  
print(retriever.retrieve("What is RAG?"))  
---

# **7️⃣ `@app.get`, `@app.post` (API decorators)**

Used in APIs like:

* FastAPI

* Flask

These are NOT built-in Python decorators but are extremely common in LLM APIs.

### **Example with FastAPI (LLM endpoint)**

from fastapi import FastAPI

app \= FastAPI()

@app.post("/ask")  
async def ask\_llm(query: str):  
   return {"answer": f"You asked: {query}"}  
---

# **8️⃣ `@asyncio.coroutine` / `async def`**

Modern LLM APIs use async functions.

### **✅ Used when:**

* Calling OpenAI

* Calling vector DB

* Streaming responses

import asyncio

async def call\_llm():  
   await asyncio.sleep(1)  
   return "LLM response"

async def main():  
   response \= await call\_llm()  
   print(response)

asyncio.run(main())  
---

# **9️⃣ Custom Decorators (VERY IMPORTANT in RAG)**

Used for:

* Logging

* Timing

* Retry logic

* Monitoring

### **Example: Logging decorator**

import time

def log\_execution(func):  
   def wrapper(\*args, \*\*kwargs):  
       print(f"Calling {func.\_\_name\_\_}")  
       start \= time.time()  
       result \= func(\*args, \*\*kwargs)  
       print(f"Finished in {time.time() \- start:.2f}s")  
       return result  
   return wrapper

@log\_execution  
def retrieve\_documents(query):  
   time.sleep(1)  
   return \["doc1", "doc2"\]

print(retrieve\_documents("What is RAG?"))  
---

# **🔟 `@wraps` (VERY important for APIs)**

Used when building custom decorators.

from functools import wraps

def secure\_endpoint(func):  
   @wraps(func)  
   def wrapper(\*args, \*\*kwargs):  
       print("Checking authentication...")  
       return func(\*args, \*\*kwargs)  
   return wrapper

@secure\_endpoint  
def protected\_route():  
   return "Secret Data"

print(protected\_route())  
---

# TOP DECORATORS USED IN AI, LLM, AND RAG

# **🚀 Most Important Decorators in Real LLM / RAG Systems**

If you are building:

### **🔹 RAG backend**

* `@lru_cache`

* `@dataclass`

* `@abstractmethod`

* Custom logging decorators

### **🔹 LLM API (FastAPI)**

* `@app.post`

* `@app.get`

* `@wraps`

* `async def`

### **🔹 Production AI Systems**

* Retry decorators

* Caching decorators

* Monitoring decorators

* Rate limiting decorators

