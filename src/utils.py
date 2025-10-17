"""
News Retrieval and Embedding System
Utility functions for the complete pipeline
"""
from typing import List, Dict
import pandas as pd


def create_results_dataframe(results: Dict) -> pd.DataFrame:
    """
    Create a pandas DataFrame from ChromaDB query results
    
    Args:
        results: ChromaDB query results dictionary
        
    Returns:
        DataFrame with columns: title, description, link, date_published
    """
    data = []
    
    if 'metadatas' in results and results['metadatas']:
        for metadata in results['metadatas'][0]:  # First query results
            data.append({
                'title': metadata.get('title', ''),
                'description': metadata.get('description', ''),
                'link': metadata.get('link', ''),
                'date_published': metadata.get('published', '')
            })
    
    return pd.DataFrame(data)


def display_results(df: pd.DataFrame, max_rows: int = 10):
    """
    Display results in a formatted way
    
    Args:
        df: Results DataFrame
        max_rows: Maximum number of rows to display
    """
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', 50)
    pd.set_option('display.width', None)
    
    print("\n" + "="*100)
    print(f"QUERY RESULTS ({len(df)} items found)")
    print("="*100)
    print(df.head(max_rows).to_string(index=False))
    print("="*100 + "\n")
    
    return df
