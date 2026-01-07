# **🦙 llama-pro**

**llama-pro** is a lightweight meta-package that simplifies LlamaIndex v0.10+ by bundling fragmented readers into easy-to-use groups.

---

## **🚀 Quick Start**

To install the **standard** set of readers (Web, JSON, DB, and Files):

Bash  
pip install "llama-pro\[necessary\] @ git+https://github.com/mhsefidgar/AI-Engineering-Pro.git\#subdirectory=llama-index-readerPro"

To install **everything** (Wikipedia, GitHub, Google Drive, S3, Slack, etc.):

Bash  
pip install "llama-pro\[all\] @ git+https://github.com/mhsefidgar/AI-Engineering-Pro.git\#subdirectory=llama-index-readerPro"

---

## **📦 Bundles Included**

| Shortcut | Includes | Best For |
| :---- | :---- | :---- |
| **necessary** | Web, JSON, DB, Local Files | Most common RAG applications. |
| **all** | Everything in necessary \+ Wiki, GitHub, Google, S3, Notion, Slack | Complex, multi-source enterprise agents. |
| **web** | llama-index-readers-web | Basic web scraping only. |
| **wiki** | llama-index-readers-wikipedia | Knowledge retrieval from Wikipedia. |
| **github** | llama-index-readers-github | Analyzing code repositories and issues. |

---

## **🛠 Usage Examples**

### **Using the "Necessary" Readers (SQL & Web)**

Python  
from llama\_index.readers.database import DatabaseReader  
from llama\_index.readers.web import SimpleWebPageReader

\# Load from a Website  
web\_docs \= SimpleWebPageReader().load\_data(\["https://example.com"\])

\# Load from a Database  
db\_reader \= DatabaseReader(uri="sqlite:///example.db")  
db\_docs \= db\_reader.load\_data(query="SELECT \* FROM table")

### **Using the "All" Readers (Wikipedia & GitHub)**

Python  
from llama\_index.readers.wikipedia import WikipediaReader  
from llama\_index.readers.github import GithubRepositoryReader

\# Load Wiki pages  
wiki\_docs \= WikipediaReader().load\_data(pages=\['Artificial Intelligence'\])

\# Load GitHub Repo  
git\_reader \= GithubRepositoryReader(github\_token="TOK", owner="user", repo="repo")  
git\_docs \= git\_reader.load\_data(branch="main")

---

## **📂 Project Structure**

Plaintext  
llama-index-readerPro/  
├── pyproject.toml    \# Defines 'necessary' and 'all' bundles  
└── README.md         \# Documentation

## **🤝 Support & Conflict Resolution**

This package automatically handles the fsspec version conflict between **Hugging Face Datasets** and **LlamaIndex S3 readers** by pinning fsspec to a stable range (\>=2024.1.0, \<=2025.3.0).

