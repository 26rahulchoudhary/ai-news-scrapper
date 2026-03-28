from datetime import timedelta

FEEDS = [
    # Startups + AI
    "https://techcrunch.com/feed/",

    # ⚡ Fast tech news
    "https://www.theverge.com/rss/index.xml",
    "https://www.engadget.com/rss.xml",
    "https://feeds.arstechnica.com/arstechnica/index",

    # Deep tech + AI insights
    "https://www.technologyreview.com/feed/",

    # AI-focused
    "https://www.marktechpost.com/feed/",
    "https://aibusiness.com/rss.xml",

    # Developer + trends
    "https://news.ycombinator.com/rss",

    # Research (cutting edge)
    "https://rss.arxiv.org/rss/cs.AI",

    # Aggregated AI news
    "https://news.google.com/rss/search?q=artificial+intelligence",
]

KEYWORDS = [
    # Core AI
    "ai", "artificial intelligence", "machine learning", "deep learning",

    # LLM / GenAI
    "llm", "large language model", "generative ai",
    "chatgpt", "gpt", "claude", "gemini", "copilot",

    # Tools / Dev
    "api", "open source ai", "rag", "vector database",
    "hugging face", "langchain", "fine-tuning",

    # Industry
    "ai startup", "funding", "automation", "enterprise ai",

    # Research
    "benchmark", "sota", "research", "arxiv",

    # Hot topics
    "ai safety", "deepfake", "regulation",
]

AI_KEYWORDS = [
    "ai", "artificial intelligence", "machine learning",
    "llm", "generative ai", "deep learning"
]
TECH_KEYWORDS = [
    "python", "javascript", "react", "node", "django",
    "fastapi", "nextjs", "pytorch", "tensorflow"
]

DATE_LIMIT_DAYS = 1