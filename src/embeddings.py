"""
Embedding Module
Handles text embedding using SentenceTransformers
"""
from sentence_transformers import SentenceTransformer
from typing import List, Union
import numpy as np


class EmbeddingGenerator:
    """Generate embeddings using SentenceTransformers"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize embedding generator
        
        Args:
            model_name: Name of the SentenceTransformer model
        """
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text
        
        Args:
            text: Input text
            
        Returns:
            Embedding vector as numpy array
        """
        embedding = self.model.encode(text)
        return embedding
    
    def embed_texts(self, texts: List[str]) -> List[np.ndarray]:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of input texts
            
        Returns:
            List of embedding vectors
        """
        embeddings = self.model.encode(texts)
        return embeddings
