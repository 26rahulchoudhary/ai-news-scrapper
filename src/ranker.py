from datetime import datetime
from src.config import KEYWORDS

# Source priority
SOURCE_PRIORITY = {
    "TechCrunch": 5,
    "MIT Technology Review": 5,
    "MarkTechPost": 4,
    "The Verge": 3,
    "Engadget": 3,
    "Ars Technica": 4
}

def keyword_score(text):
    text = text.lower()
    return sum(1 for k in KEYWORDS if k in text)


def source_score(source):
    return SOURCE_PRIORITY.get(source, 1)


def recency_score(published):
    try:
        dt = datetime.strptime(published[:25], "%a, %d %b %Y %H:%M:%S")
        hours_old = (datetime.now() - dt).total_seconds() / 3600

        if hours_old < 6:
            return 5
        elif hours_old < 24:
            return 3
        else:
            return 1
    except:
        return 1


def length_score(summary):
    length = len(summary.split())
    if length > 50:
        return 3
    elif length > 20:
        return 2
    return 1


def rank_articles(articles):
    for article in articles:
        text = article["title"] + " " + article["summary"]

        score = (
            keyword_score(text) * 2 +
            source_score(article["source"]) * 2 +
            recency_score(article["published"]) +
            length_score(article["summary"])
        )

        article["score"] = score

    # Sort descending
    return sorted(articles, key=lambda x: x["score"], reverse=True)