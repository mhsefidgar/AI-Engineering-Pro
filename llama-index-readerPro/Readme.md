# 🦙 llama-index-readerPro

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![LlamaIndex](https://img.shields.io/badge/Powered%20by-LlamaIndex-blue.svg)](https://www.llamaindex.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**llama-pro** is a lightweight "meta-package" that solves the LlamaIndex v0.10+ dependency fragmentation. Instead of hunting for individual data readers, you can install everything you need—from Databases to GitHub and Wikipedia—with a single, clean command.

---

## 🚀 Quick Start

The fastest way to install **llama-pro** with all connectors included:

```bash
pip install "llama-pro[all] @ git+https://github.com/mhsefidgar/AI-Engineering-Pro.git#subdirectory=llama-index-readerPro"

```


The fastest way to install **llama-pro** with necessary connectors included:

```bash
pip install "llama-pro[necessary] @ git+https://github.com/mhsefidgar/AI-Engineering-Pro.git#subdirectory=llama-index-readerPro"
```

---

## 📦 Bundles Included

You can choose to install only what you need to keep your environment lean:

| Shortcut | Description | Install Command |
| --- | --- | --- |
| **`all`** | **The Full Suite** (Web, DB, Wiki, GitHub, etc.) | `pip install "llama-pro[all] @ git+..."` |
| **`web`** | Web Scrapers & HTML Readers | `pip install "llama-pro[web] @ git+..."` |
| **`db`** | SQL & Database Connectors | `pip install "llama-pro[db] @ git+..."` |
| **`wiki`** | Wikipedia Knowledge Ingestion | `pip install "llama-pro[wiki] @ git+..."` |
| **`github`** | Repo, Issue, and PR Readers | `pip install "llama-pro[github] @ git+..."` |

---

## 🛠 Usage Example

After installing, you can use the readers directly without worrying about missing dependencies.

### Ingesting Wikipedia & Web Data

```python
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.readers.web import SimpleWebPageReader

# Load a Wikipedia page
wiki_docs = WikipediaReader().load_data(pages=['Artificial Intelligence'])

# Load a website
web_docs = SimpleWebPageReader(html_to_text=True).load_data(
    ["[https://example.com](https://example.com)"]
)

```

### Ingesting from GitHub

```python
from llama_index.readers.github import GithubRepositoryReader

reader = GithubRepositoryReader(
    github_token="your_token_here",
    owner="run-llama",
    repo="llama_index"
)
documents = reader.load_data(branch="main")

```

---

## 📂 Project Structure

```text
llama-index-readerPro/
├── pyproject.toml    # The magic file that bundles the readers
└── README.md         # You are here!

```



## 🤝 Contributing


Found a reader that should be in the `all` bundle?



1. Open an issue.
2. Or submit a PR updating the `pyproject.toml` file.

---



Created by [mhsefidgar](https://github.com/mhsefidgar)


```



---

### Pro Tip for your Repo:
I included **badges** at the top. They don't just look "wonderful"; they tell other developers that your project is built with Python and uses the MIT license. 








**Would you like me to help you set up a "Tests" section in the README to show how to verify all these readers are working correctly?**

```
