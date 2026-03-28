def save_to_csv(articles):
    import pandas as pd
    from datetime import datetime
    import os

    if not articles:
        print("No articles to save.")
        return

    # Remove raw field
    clean_articles = [
        {k: v for k, v in article.items() if k != "raw"}
        for article in articles
    ]

    df = pd.DataFrame(clean_articles)
    df.drop_duplicates(subset=["title"], inplace=True)

    os.makedirs("data", exist_ok=True)

    file_name = f"data/news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(file_name, index=False)
    print(f"Saved {len(df)} articles")