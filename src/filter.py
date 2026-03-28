from datetime import datetime, timedelta
from src.config import KEYWORDS, DATE_LIMIT_DAYS, TECH_KEYWORDS, AI_KEYWORDS

def is_relevant(text):
    text = text.lower()

    ai_matches = sum(1 for k in AI_KEYWORDS if k in text)
    tech_matches = sum(1 for k in TECH_KEYWORDS if k in text)

    # Must have AI relevance
    if ai_matches == 0:
        return False

    # Bonus if tech present
    return ai_matches >= 1 or tech_matches >= 2


def is_recent(entry):
    if not entry.get("published_parsed"):
        return False  # skip if no date

    published_date = datetime(*entry.published_parsed[:6])
    cutoff_date = datetime.now() - timedelta(days=DATE_LIMIT_DAYS)

    return published_date >= cutoff_date


def filter_articles(raw_entries):
    filtered = []

    for entry in raw_entries:
        content = entry["title"] + " " + entry["summary"]

        if is_relevant(content) and is_recent(entry["raw"]):
            filtered.append(entry)

    return filtered