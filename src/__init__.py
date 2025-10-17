"""
News Retrieval and Embedding System
Main package initialization
"""

__version__ = "1.0.0"
__author__ = "News Query Team"

from .rss_loader import load_rss_feed, format_news_for_embedding, load_sample_data
from .tokenizer import tokenize_text, count_tokens, should_chunk
from .embeddings import EmbeddingGenerator
from .vector_store import ChromaDBStore
from .langchain_pipeline import NewsRetrievalPipeline
from .utils import create_results_dataframe, display_results

__all__ = [
    'load_rss_feed',
    'load_sample_data',
    'format_news_for_embedding',
    'tokenize_text',
    'count_tokens',
    'should_chunk',
    'EmbeddingGenerator',
    'ChromaDBStore',
    'NewsRetrievalPipeline',
    'create_results_dataframe',
    'display_results'
]
