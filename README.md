# News Retrieval and Embedding System - RPP RSS Feed

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive news retrieval system that ingests the latest news from RPP Perú (https://rpp.pe/rss), generates embeddings using SentenceTransformers, and builds a semantic search system using ChromaDB orchestrated with LangChain.

## 🎯 Project Overview

This project implements a complete pipeline for:
- 📡 Loading RSS feeds from RPP Perú
- 🔤 Tokenizing articles using tiktoken
- 🧮 Generating embeddings with SentenceTransformers
- 💾 Storing in ChromaDB vector database
- 🔍 Semantic similarity search
- 🔗 End-to-end orchestration with LangChain

## 📁 Project Structure

```
news-query_RPP-lab/
├── src/                          # Source code modules
│   ├── rss_loader.py            # RSS feed loading and parsing
│   ├── tokenizer.py             # Tokenization with tiktoken
│   ├── embeddings.py            # Embedding generation
│   ├── vector_store.py          # ChromaDB vector storage
│   ├── langchain_pipeline.py    # LangChain orchestration
│   └── utils.py                 # Utility functions
├── notebooks/                    # Jupyter notebooks
│   └── news_retrieval_system.ipynb
├── data/                         # Data directory (generated)
├── outputs/                      # Output files (generated)
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git
- Internet connection (for RSS feeds and model downloads)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gsaco/news-query_RPP-lab.git
   cd news-query_RPP-lab
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python test_modules.py
   ```

For detailed setup instructions, see [SETUP.md](SETUP.md).

### Quick Start

**Run the example script:**
```bash
python example_usage.py
```

**Run the Jupyter notebook:**
```bash
jupyter notebook notebooks/news_retrieval_system.ipynb
```

## 📚 Features

### Step 0: RSS Feed Loading
- Fetches latest 50 news items from https://rpp.pe/rss
- Extracts: title, description, link, and published date
- Using `feedparser` library

### Step 1: Tokenization
- Tokenizes articles using `tiktoken`
- Computes token counts
- Determines if chunking is needed based on model context limits
- Provides statistics on token distribution

### Step 2: Embedding Generation
- Uses `sentence-transformers/all-MiniLM-L6-v2` model
- Generates 384-dimensional embeddings
- Batch processing for efficiency

### Step 3: ChromaDB Storage
- Creates and manages ChromaDB collections
- Supports upsert operations
- Stores documents, embeddings, and metadata
- Persistent storage for future queries

### Step 4: Query & Retrieval
- Semantic similarity search
- Keyword-based queries (e.g., "Últimas noticias de economía")
- Results displayed in pandas DataFrame
- Columns: `title | description | link | date_published`

### Step 5: LangChain Orchestration
- End-to-end pipeline: Load → Tokenize → Embed → Store → Retrieve
- Modular architecture
- Easy to extend and customize

## 💡 Usage Examples

### Query for Economic News
```python
query = "Últimas noticias de economía"
results = chroma_store.query(query_texts=[query], n_results=10)
df_results = create_results_dataframe(results)
```

### Query for Sports News
```python
query = "Noticias de deportes y fútbol"
results = chroma_store.query(query_texts=[query], n_results=10)
```

### Complete LangChain Pipeline
```python
pipeline = NewsRetrievalPipeline()
results_df = pipeline.run_pipeline(
    news_items=news_items,
    query_text="Noticias sobre tecnología",
    k=10
)
```

## 📊 Output

The system generates:
- **CSV files** with query results in `outputs/` directory
- **ChromaDB database** in `chroma_db/` directory (persisted)
- **DataFrames** with columns: `title`, `description`, `link`, `date_published`

## 🛠️ Technical Stack

- **feedparser** (6.0.10): RSS feed parsing
- **sentence-transformers** (2.2.2): Text embeddings
- **chromadb** (0.4.18): Vector database
- **langchain** (0.1.0): Pipeline orchestration
- **tiktoken** (0.5.2): Tokenization
- **pandas** (2.1.4): Data manipulation
- **jupyter**: Interactive notebooks

## 📝 Module Documentation

### `rss_loader.py`
- `load_rss_feed(url, max_items)`: Load RSS feed data
- `format_news_for_embedding(news_item)`: Format news for embedding

### `tokenizer.py`
- `tokenize_text(text, model)`: Tokenize text
- `count_tokens(text, model)`: Count tokens
- `should_chunk(text, max_tokens)`: Check if chunking needed

### `embeddings.py`
- `EmbeddingGenerator`: Class for generating embeddings
- `embed_text(text)`: Generate single embedding
- `embed_texts(texts)`: Batch embedding generation

### `vector_store.py`
- `ChromaDBStore`: ChromaDB wrapper class
- `add_documents()`: Add documents to collection
- `upsert_documents()`: Update or insert documents
- `query()`: Search similar documents

### `langchain_pipeline.py`
- `NewsRetrievalPipeline`: Complete pipeline orchestration
- `load_and_process()`: Load and process documents
- `create_vectorstore()`: Create vector store
- `query()`: Query and return DataFrame
- `run_pipeline()`: Run complete pipeline

## 🎓 Educational Value

This project demonstrates:
- Working with RSS feeds
- Text tokenization and analysis
- Embedding generation for semantic search
- Vector database operations
- LangChain integration patterns
- Modular code organization
- Best practices in ML pipelines

## 🔧 Troubleshooting

**Issue**: Module import errors
```bash
# Make sure you're in the project root
cd news-query_RPP-lab
# Install requirements again
pip install -r requirements.txt
```

**Issue**: ChromaDB persistence errors
```bash
# Delete the ChromaDB directory and rerun
rm -rf chroma_db/
```

**Issue**: RSS feed loading timeout
```bash
# Check internet connection
# RPP RSS feed may be temporarily unavailable
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- RPP Perú for providing the RSS feed
- Hugging Face for SentenceTransformers models
- ChromaDB team for the vector database
- LangChain community

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Built with ❤️ for learning and experimentation**
