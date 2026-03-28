import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def extract_key_sentences(text, max_sentences=3):
    sentences = sent_tokenize(text)

    if len(sentences) <= max_sentences:
        return sentences

    return sentences[:max_sentences]  # simple approach (can upgrade later)