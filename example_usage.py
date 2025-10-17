"""
Example: Basic News Retrieval System Usage

This script demonstrates how to use the news retrieval system modules.

Note: This example uses sample data. In a real environment with internet access,
replace load_sample_data with load_rss_feed to fetch live data.
"""

import sys
import os
sys.path.insert(0, 'src')

from rss_loader import load_sample_data, format_news_for_embedding
import pandas as pd


def main():
    print("="*80)
    print("NEWS RETRIEVAL SYSTEM - BASIC EXAMPLE")
    print("="*80)
    
    # Step 1: Load news data
    print("\n📡 Step 1: Loading news data...")
    news_items = load_sample_data("data/sample_rpp_news.json")
    print(f"✅ Loaded {len(news_items)} news items")
    
    # Step 2: Display as DataFrame
    print("\n📊 Step 2: Converting to DataFrame...")
    df = pd.DataFrame(news_items)
    print(f"✅ Created DataFrame with shape: {df.shape}")
    
    # Step 3: Show sample news
    print("\n📰 Step 3: Sample News Items")
    print("-" * 80)
    for i, item in enumerate(news_items[:3], 1):
        print(f"\n{i}. {item['title']}")
        print(f"   📅 {item['published']}")
        print(f"   📝 {item['description'][:100]}...")
        print(f"   🔗 {item['link']}")
    
    # Step 4: Format for embedding
    print("\n📝 Step 4: Formatting for embedding...")
    formatted_texts = [format_news_for_embedding(item) for item in news_items[:3]]
    print("✅ Sample formatted text:")
    print(f"   {formatted_texts[0][:100]}...")
    
    # Step 5: Simple keyword filtering (without embeddings)
    print("\n🔍 Step 5: Simple keyword search (example: 'economía')...")
    keyword = "economía"
    filtered = [item for item in news_items 
                if keyword.lower() in item['title'].lower() 
                or keyword.lower() in item['description'].lower()]
    
    print(f"✅ Found {len(filtered)} items containing '{keyword}':")
    for item in filtered[:3]:
        print(f"   • {item['title']}")
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total news items: {len(news_items)}")
    print(f"Unique topics covered: Economy, Sports, Politics, Technology, etc.")
    print(f"\nℹ️  For full functionality including:")
    print("   • Semantic embeddings with SentenceTransformers")
    print("   • Vector storage with ChromaDB")
    print("   • LangChain orchestration")
    print("   • Similarity-based search")
    print("\n   Run the Jupyter notebook: notebooks/news_retrieval_system.ipynb")
    print("="*80)


if __name__ == "__main__":
    main()
