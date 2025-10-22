# News Retrieval and Embedding System - RPP RSS Feed

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A news retrieval system that ingests the latest news from RPP Perú (https://rpp.pe/rss), generates embeddings using SentenceTransformers, and builds a semantic search system using ChromaDB orchestrated with LangChain.

## 🎯 Objective

Ingest the latest news from RPP Perú RSS feed, embed them using SentenceTransformers, and build a retrieval system using ChromaDB orchestrated with LangChain.

## 📁 Project Structure

```
news-query_RPP-lab/
├── src/                          # Source code modules
│   ├── __init__.py
│   ├── rss_loader.py            # RSS feed loading and parsing
│   ├── tokenizer.py             # Tokenization with tiktoken
│   ├── embeddings.py            # Embedding generation
│   ├── vector_store.py          # ChromaDB vector storage
│   ├── langchain_pipeline.py    # LangChain orchestration
│   └── utils.py                 # Utility functions
├── notebooks/                    # Jupyter notebooks
│   └── news_retrieval_system.ipynb
├── data/                         # Data directory
├── outputs/                      # Output CSV files
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Internet connection (for RSS feeds and model downloads)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gsaco/news-query_RPP-lab.git
   cd news-query_RPP-lab
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter notebook**
   ```bash
   jupyter notebook notebooks/news_retrieval_system.ipynb
   ```

### Running in Google Colab

1. Upload the repository to Google Drive or clone it directly in Colab:
   ```python
   !git clone https://github.com/gsaco/news-query_RPP-lab.git
   %cd news-query_RPP-lab
   ```

2. Install dependencies:
   ```python
   !pip install -r requirements.txt
   ```

3. Run the notebook cells sequentially

**Note**: All file paths in the notebook are relative and will work in both local and Colab environments.

## Implementation Steps

### Step 0: Load Data
- Uses `feedparser` to extract 50 latest news items from RPP RSS feed
- Each record includes: `title`, `description`, `link`, `published` (date)

### Step 1: Tokenization
- Tokenizes a sample article using `tiktoken`
- Computes `num_tokens` and decides if chunking is needed
- Analyzes token distribution across all articles

### Step 2: Embedding
- Generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- Creates 384-dimensional embeddings for each article
- Stores embeddings alongside text and metadata

### Step 3: Create or Upsert Chroma Collection
- Uses ChromaDB to store documents, metadata, and embeddings
- Implements a retriever that supports similarity search by keyword or description
- Persistent storage in `chroma_db/` directory

### Step 4: Query Results
- Queries with prompts like "Últimas noticias de economía"
- Displays results in a pandas DataFrame with columns:
  - `title`
  - `description`
  - `link`
  - `date_published`
- Saves results to CSV in `outputs/` directory

### Step 5: Orchestrate with LangChain
- Implements an end-to-end pipeline in LangChain
- Pipeline: Loads RSS → Tokenizes → Embeds → Stores → Retrieves
- Each step is modular (functions or LangChain chains)

## Deliverables

✅ **Jupyter Notebook**: Complete implementation in `notebooks/news_retrieval_system.ipynb`

✅ **requirements.txt**: All required packages with versions

✅ **README.md**: This file with setup instructions

✅ **Organized Repository Structure**: `/src`, `/data`, `/notebooks`, `/outputs`

✅ **Relative File Paths**: No absolute directories, works in any environment

✅ **End-to-End Execution**: Runs without manual intervention

✅ **Google Colab Compatible**: Can be run directly in Colab

## 🛠️ Technical Stack

- **Python** 3.10+
- **feedparser** 6.0.10 - RSS feed parsing
- **tiktoken** 0.5.2 - Tokenization
- **sentence-transformers** 2.7.0 - Text embeddings
- **chromadb** 0.4.18 - Vector database
- **langchain** 0.1.0 - Pipeline orchestration
- **datasets**, **transformers**, **torch** - ML infrastructure
- **pandas**, **matplotlib**, **seaborn**, **scikit-learn** - Data science
- **jupyter** - Interactive notebooks

## Usage Example

```python
# Load RSS feed
news_items = load_rss_feed(url="https://rpp.pe/rss", max_items=50)

# Create pipeline
pipeline = NewsRetrievalPipeline(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    persist_directory="./chroma_db"
)

# Run complete pipeline
results_df = pipeline.run_pipeline(
    news_items=news_items,
    query_text="Últimas noticias de economía",
    k=10
)

# Display results
print(results_df)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- RPP Perú for providing the RSS feed
- Hugging Face for SentenceTransformers models
- ChromaDB and LangChain communities
