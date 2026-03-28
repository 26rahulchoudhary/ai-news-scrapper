import feedparser
from src.config import FEEDS
from src.utils import clean_html

def fetch_articles():
    articles = []

    for url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            clean_summary = clean_html(entry.get("summary", ""))

            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", ""),
                "summary": clean_summary,
                "source": feed.feed.get("title", ""),
                "raw": entry
            })

    return articles