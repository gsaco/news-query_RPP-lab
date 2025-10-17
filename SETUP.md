# Setup and Installation Guide

This guide will help you set up the News Retrieval and Embedding System on your local machine.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Internet connection (for downloading dependencies and accessing RSS feeds)
- At least 2GB of free disk space (for models and dependencies)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gsaco/news-query_RPP-lab.git
cd news-query_RPP-lab
```

### 2. Create a Virtual Environment (Recommended)

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- feedparser: RSS feed parsing
- sentence-transformers: Text embeddings
- chromadb: Vector database
- langchain: Pipeline orchestration
- tiktoken: Tokenization
- pandas: Data manipulation
- jupyter: Interactive notebooks
- And their dependencies

**Note:** The installation may take 5-10 minutes depending on your internet connection, as it downloads pre-trained models.

### 4. Verify Installation

Run the test script to verify everything is installed correctly:

```bash
python test_modules.py
```

You should see:
```
🎉 All tests passed!
```

## Running the Jupyter Notebook

### 1. Start Jupyter Notebook

```bash
jupyter notebook
```

This will open your web browser with the Jupyter interface.

### 2. Navigate to the Notebook

- In the Jupyter file browser, navigate to `notebooks/`
- Click on `news_retrieval_system.ipynb`

### 3. Run the Notebook

- Click `Cell` → `Run All` to execute all cells
- Or run cells individually by pressing `Shift + Enter`

## Project Structure Overview

```
news-query_RPP-lab/
├── src/                          # Python modules
│   ├── __init__.py              # Package initialization
│   ├── rss_loader.py            # RSS feed loading
│   ├── tokenizer.py             # Text tokenization
│   ├── embeddings.py            # Embedding generation
│   ├── vector_store.py          # ChromaDB operations
│   ├── langchain_pipeline.py    # LangChain orchestration
│   └── utils.py                 # Utility functions
├── notebooks/                    # Jupyter notebooks
│   └── news_retrieval_system.ipynb
├── data/                         # Data files
│   ├── sample_rpp_news.json     # Sample news data
│   └── README.md                # Data documentation
├── outputs/                      # Generated outputs
├── chroma_db/                    # ChromaDB database (generated)
├── requirements.txt              # Python dependencies
├── test_modules.py              # Test script
├── SETUP.md                     # This file
└── README.md                    # Main documentation
```

## Troubleshooting

### Issue: `ModuleNotFoundError`

**Solution:** Make sure you've activated the virtual environment and installed all requirements:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: ChromaDB persistence errors

**Solution:** Delete the ChromaDB directory and restart:
```bash
rm -rf chroma_db/
```

### Issue: RSS feed timeout

**Possible causes:**
- No internet connection
- RSS feed temporarily unavailable
- Firewall blocking the connection

**Solution:** Use sample data for testing:
```python
from rss_loader import load_sample_data
news_items = load_sample_data("data/sample_rpp_news.json")
```

### Issue: Jupyter kernel crashes

**Solution:** Increase memory allocation or reduce the number of news items processed:
```python
# Instead of 50 items, try fewer
news_items = load_rss_feed(url="https://rpp.pe/rss", max_items=20)
```

### Issue: SentenceTransformers model download fails

**Solution:** The model will be downloaded automatically on first use. Ensure you have:
- Active internet connection
- At least 1GB free disk space
- Access to huggingface.co

## System Requirements

### Minimum Requirements
- CPU: Dual-core processor (2GHz+)
- RAM: 4GB
- Storage: 2GB free space
- Internet: Required for initial setup and live RSS feeds

### Recommended Requirements
- CPU: Quad-core processor (2.5GHz+)
- RAM: 8GB
- Storage: 5GB free space
- Internet: Broadband connection

## Using in Different Environments

### Local Development
Follow the standard installation steps above.

### Google Colab
Upload the notebook and install requirements:
```python
!pip install feedparser sentence-transformers chromadb langchain langchain-community tiktoken pandas
```

### Docker (Optional)
A Dockerfile is not provided but you can create one based on:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
```

## Next Steps

After successful installation:

1. **Explore the Notebook:** Run `notebooks/news_retrieval_system.ipynb` to see the complete pipeline
2. **Try Custom Queries:** Modify queries in the notebook to search for different topics
3. **Experiment with Parameters:** Adjust embedding models, token counts, or result limits
4. **Build Your Own:** Use the modular components to create custom news retrieval applications

## Getting Help

If you encounter issues:
1. Check this troubleshooting guide
2. Review the main [README.md](README.md)
3. Check the sample data format in [data/README.md](data/README.md)
4. Open an issue on GitHub with:
   - Your operating system
   - Python version (`python --version`)
   - Full error message
   - Steps to reproduce

## License

This project is licensed under the MIT License - see LICENSE file.
