"""
RSS Feed Loader Module
Loads and parses RSS feeds from RPP Perú
"""
import feedparser
from datetime import datetime
from typing import List, Dict


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


def format_news_for_embedding(news_item: Dict) -> str:
    """
    Format news item for embedding
    
    Args:
        news_item: Dictionary with news data
        
    Returns:
        Formatted text string
    """
    return f"{news_item['title']}. {news_item['description']}"
