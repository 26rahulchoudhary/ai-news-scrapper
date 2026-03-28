from src.scraper import fetch_articles
from src.filter import filter_articles
from src.article_extractor import extract_article
from src.nlp_processing import extract_key_sentences
from src.storage import save_to_csv
from src.tweet_generator import generate_tweet
from src.ranker import rank_articles

def main():
    print("Fetching articles...")
    articles = fetch_articles()

    print("Filtering...")
    filtered = filter_articles(articles)
    filtered = filtered[:10]

    enriched_articles = []

    for article in filtered:
        print(f"Processing: {article['title']}")

        data = extract_article(article["link"])
        full_text = data["text"]

        if not full_text:
            # fallback to summary
            key_sentences = [article["summary"]]
        else:
            key_sentences = extract_key_sentences(full_text)

        tweet = generate_tweet({
            "title": article["title"],
            "summary": " ".join(key_sentences)
        })

        summary_text = " ".join(key_sentences)

        enriched_articles.append({
            "title": article["title"],
            "link": article["link"],
            "summary": summary_text,
            "tweet": tweet,
            "published": article["published"],
            "source": article["source"]
        })

    ranked = rank_articles(enriched_articles)
    top_articles = ranked[:10]

    print("\nTop Tweets:\n")

    for i, article in enumerate(top_articles, 1):
        print(f"Tweet {i}:\n{article['tweet']}\n")

    save_to_csv(top_articles)

if __name__ == "__main__":
    main()