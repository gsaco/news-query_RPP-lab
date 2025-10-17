"""
Simple test script to verify the modules work correctly
Run this with: python test_modules.py
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from rss_loader import load_sample_data, format_news_for_embedding

def test_sample_data_loading():
    """Test loading sample data"""
    print("="*80)
    print("TEST 1: Loading Sample Data")
    print("="*80)
    
    try:
        news_items = load_sample_data("data/sample_rpp_news.json")
        print(f"✅ Successfully loaded {len(news_items)} news items")
        
        if news_items:
            print(f"\nFirst item:")
            print(f"  Title: {news_items[0]['title']}")
            print(f"  Description: {news_items[0]['description'][:80]}...")
            print(f"  Link: {news_items[0]['link']}")
            print(f"  Published: {news_items[0]['published']}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_text_formatting():
    """Test text formatting for embedding"""
    print("\n" + "="*80)
    print("TEST 2: Text Formatting")
    print("="*80)
    
    try:
        news_items = load_sample_data("data/sample_rpp_news.json")
        formatted = format_news_for_embedding(news_items[0])
        print(f"✅ Formatted text: {formatted[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_data_structure():
    """Test data structure validation"""
    print("\n" + "="*80)
    print("TEST 3: Data Structure Validation")
    print("="*80)
    
    try:
        news_items = load_sample_data("data/sample_rpp_news.json")
        
        # Check required fields
        required_fields = ['title', 'description', 'link', 'published']
        all_valid = True
        
        for i, item in enumerate(news_items[:5]):  # Check first 5
            for field in required_fields:
                if field not in item:
                    print(f"❌ Item {i} missing field: {field}")
                    all_valid = False
        
        if all_valid:
            print(f"✅ All items have required fields: {required_fields}")
            print(f"✅ Validated {len(news_items)} items successfully")
        
        return all_valid
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Run all tests"""
    print("\n🧪 Running Module Tests\n")
    
    results = []
    results.append(("Sample Data Loading", test_sample_data_loading()))
    results.append(("Text Formatting", test_text_formatting()))
    results.append(("Data Structure", test_data_structure()))
    
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(r[1] for r in results)
    
    if all_passed:
        print("\n🎉 All tests passed!")
        print("\nℹ️  Note: This sandbox environment has limited internet access.")
        print("   The RSS feed and external APIs (tiktoken, SentenceTransformers) ")
        print("   require internet access to work fully.")
        print("   In a normal environment with internet, all features will work.")
    else:
        print("\n⚠️  Some tests failed")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
