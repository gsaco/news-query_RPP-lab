"""
RSS Feed Loader Module
Loads and parses RSS feeds from RPP Perú
"""
import feedparser
import json
import os
from datetime import datetime
from typing import List, Dict, Optional


def load_rss_feed(url: str = "https://rpp.pe/rss", max_items: int = 50) -> List[Dict]:
    """
    Load RSS feed from RPP Perú
    
    Args:
        url: RSS feed URL
        max_items: Maximum number of items to retrieve
        
    Returns:
        List of dictionaries with news data
    """
    feed = feedparser.parse(url)
    
    news_items = []
    for entry in feed.entries[:max_items]:
        item = {
            'title': entry.get('title', ''),
            'description': entry.get('description', ''),
            'link': entry.get('link', ''),
            'published': entry.get('published', '')
        }
        news_items.append(item)
    
    return news_items


def load_sample_data(json_path: str = "data/sample_rpp_news.json") -> List[Dict]:
    """
    Load sample RSS data from a JSON file (for testing when internet is unavailable)
    
    Args:
        json_path: Path to JSON file with sample news data
        
    Returns:
        List of dictionaries with news data
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Sample data file not found: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        news_items = json.load(f)
    
    return news_items


def format_news_for_embedding(news_item: Dict) -> str:
    """
    Format news item for embedding
    
    Args:
        news_item: Dictionary with news data
        
    Returns:
        Formatted text string
    """
    return f"{news_item['title']}. {news_item['description']}"
