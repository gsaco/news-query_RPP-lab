"""
Tokenization Module
Handles tokenization using tiktoken
"""
import tiktoken
from typing import List


def tokenize_text(text: str, model: str = "gpt-3.5-turbo") -> List[int]:
    """
    Tokenize text using tiktoken
    
    Args:
        text: Input text to tokenize
        model: Model name for encoding (default: gpt-3.5-turbo)
        
    Returns:
        List of token IDs
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return tokens


def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    Count number of tokens in text
    
    Args:
        text: Input text
        model: Model name for encoding
        
    Returns:
        Number of tokens
    """
    tokens = tokenize_text(text, model)
    return len(tokens)


def should_chunk(text: str, max_tokens: int = 8192, model: str = "gpt-3.5-turbo") -> bool:
    """
    Determine if text needs to be chunked based on token count
    
    Args:
        text: Input text
        max_tokens: Maximum allowed tokens
        model: Model name for encoding
        
    Returns:
        True if chunking is needed, False otherwise
    """
    num_tokens = count_tokens(text, model)
    return num_tokens > max_tokens
