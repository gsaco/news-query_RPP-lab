# Sample Data

This directory contains sample news data for testing and demonstration purposes.

## Files

### `sample_rpp_news.json`
Sample news articles in the format returned by the RPP RSS feed. Contains 20 news items covering various topics:
- Economy
- Sports
- Politics
- Technology
- Education

**Note:** The sample data uses dates from October 2023. These are for testing purposes only and do not reflect current news. In production, use the live RSS feed which provides current, real-time news.

## Usage

When internet access is unavailable, you can use the sample data instead of fetching from the live RSS feed:

```python
from rss_loader import load_sample_data

# Load sample data
news_items = load_sample_data("data/sample_rpp_news.json")
```

## Data Format

Each news item contains:
- `title`: Article headline
- `description`: Brief article summary
- `link`: URL to full article
- `published`: Publication date in RFC 822 format

## Note

This is sample data for testing purposes. In production, use the live RSS feed:

```python
from rss_loader import load_rss_feed

# Load from live RSS feed (requires internet)
news_items = load_rss_feed("https://rpp.pe/rss", max_items=50)
```
