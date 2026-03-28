from newspaper import Article

def extract_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()

        return {
            "text": article.text,
            "title": article.title
        }
    except Exception as e:
        print(f"Error fetching article: {url}")
        return {"text": "", "title": ""}