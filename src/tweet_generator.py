import random

def generate_tweet(article):
    summary = article["summary"]

    hooks = [
        "Big news in AI:",
        "AI is evolving fast:",
        "This just happened in tech:",
        "Interesting AI update:",
        "Worth paying attention:"
    ]

    endings = [
        "This could be huge.",
        "Game changer?",
        "What do you think?",
        "The future is here.",
        "This is just a beginning."
    ]
    hashtags = "#AI #Tech #MachineLearning"

    hook = random.choice(hooks)
    ending = random.choice(endings)
    hashtag = random.choice(hashtags)

    def trim_tweet(text, max_len=500):
        if len(text) <= max_len:
            return text

        trimmed = text[:max_len]

        # cut at last full word
        return trimmed.rsplit(" ", 1)[0] + "..."

    tweet = f"{hook}\n\n{summary}\n\n{ending}\n\n{hashtag}"

    # Twitter limit safety (~280 chars)
    return trim_tweet(tweet)