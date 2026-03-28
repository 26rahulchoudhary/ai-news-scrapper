# 🚀 AI News Scraper & Twitter Content Engine

A modular Python-based pipeline that scrapes AI & tech news, filters high-quality articles, extracts meaningful insights, ranks them, and generates engaging tweets.

---

## 📌 Project Overview

This project is designed to:

* 📰 Scrape latest AI & tech news from trusted sources
* 🧠 Filter relevant content using keyword logic
* 📖 Extract full article content (fallback supported)
* ✂️ Summarize articles using NLP
* 📊 Rank articles based on quality signals
* 🐦 Generate engaging & opinion-based tweets

---

## 🏗️ Project Structure

```
ai-news-scraper/
│
├── data/                  # Output CSV files
├── src/
│   ├── scraper.py        # Fetch RSS feeds
│   ├── filter.py         # Keyword filtering logic
│   ├── article_extractor.py
│   ├── nlp.py            # Text processing & summarization
│   ├── ranker.py         # Article ranking logic
│   ├── tweet_generator.py
│   ├── engagement.py     # Engagement tweet generation
│   ├── utils.py          # Helpers (HTML cleaning)
│   └── config.py         # Configurations
│
├── main.py               # Entry point
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-news-scraper.git
cd ai-news-scraper
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🔄 Pipeline Flow

```
RSS Feeds → Filter → Extract → Summarize → Rank → Generate Tweets → Save CSV
```

---

## 🧠 Features

### ✅ Smart Filtering

* AI keyword-based filtering
* Avoids irrelevant tech/tutorial noise

### ✅ Article Extraction

* Uses `newspaper3k` / fallback methods
* Handles blocked or partial content

### ✅ NLP Summarization

* Extracts key sentences
* Keeps content concise and tweet-ready

### ✅ Ranking System

Articles are scored based on:

* Keyword relevance
* Source quality
* Recency
* Content richness

### ✅ Tweet Generation

* Hook-based tweets
* Smart truncation (no broken words)
* Optional engagement tweets (questions, comparisons)

---

## 📊 Output Example

| title                     | tweet                | source     |
| ------------------------- | -------------------- | ---------- |
| AI startup raises funding | 🚀 Big news in AI... | TechCrunch |

---

## 🔥 Advanced Features (WIP)

* 🧠 AI-based tweet generation (LLM)
* 🧵 Thread generation
* 📈 Viral scoring system
* 🤖 Auto-posting to Twitter API
* ⏰ Scheduled execution (cron jobs)

---

## 💡 Key Learnings

This project demonstrates:

* Web scraping best practices
* NLP pipeline design
* Data filtering & ranking strategies
* Content generation for social media

---

## ⚠️ Notes

* Some websites may block scraping
* RSS summaries may be incomplete
* Full article extraction may fail → fallback used

---

## 🚀 Future Roadmap

* Replace keyword filtering with LLM classification
* Add semantic search / embeddings
* Build dashboard for analytics
* Deploy as a microservice

---

## 🤝 Contributing

Feel free to fork and improve the project!

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Rahul Choudhary

---

🔥 Built with the goal of turning news into actionable, engaging content.
