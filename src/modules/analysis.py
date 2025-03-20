"""This module perform sentiment analysis and comparative sentiment analysis"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import heapq


nltk.download("vader_lexicon")
nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')


def sentiment_analysis(extracted_articles):
    """Function returns sentiment analysis scrore"""
    analyzer = SentimentIntensityAnalyzer()

    articles = extracted_articles

    for article in articles:
        sentence = article["title"] + article["summary"]
        sentiment = analyzer.polarity_scores(sentence)
        article.update({"sentiment": sentiment})

    return articles


def comparative_analysis(sentiment_analyzed):
    """Function returns comparative sentiment analysis score"""
    articles = sentiment_analyzed

    total_articles = len(articles)
    positive_count = len(
        [article for article in articles
         if article["sentiment"]["compound"] > 0.05]
    )
    negative_count = len(
        [article for article in articles
         if article["sentiment"]["compound"] < -0.05]
    )
    neutral_count = total_articles - positive_count - negative_count

    positive_percentage = (positive_count / total_articles) * 100
    negative_percentage = (negative_count / total_articles) * 100
    neutral_percentage = (neutral_count / total_articles) * 100

    return {
        "positive": positive_percentage,
        "negative": negative_percentage,
        "neutral": neutral_percentage,
    }


def summary_generation(combined_all_summary):
    """Function returns overall summary of the articles"""
    articles_summary = combined_all_summary
    summary_data = "".join(article["summary"] for article in articles_summary)
    sentences = sent_tokenize(summary_data)

    word_freq = defaultdict(int)
    for word in word_tokenize(summary_data):
        if word.isalpha():
            word_freq[word.lower()] += 1

    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] /= max_freq

    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word.lower() in word_freq:
                sentence_scores[sentence] += word_freq[word.lower()]

    num_sentences = 2
    summary_sentences = heapq.nlargest(
        num_sentences, sentence_scores, key=sentence_scores.get)
    overall_summary = "".join(summary_sentences)
    return overall_summary


def analysis(extracted_articles):
    """Function returns sentement, comparative sentiment and overall summary"""
    sentiment_analyed_articles = sentiment_analysis(extracted_articles)

    comparative_analyed_score = comparative_analysis(
        sentiment_analyed_articles)

    overall_summary = (
        summary_generation(sentiment_analyed_articles)
    )

    return (
        comparative_analyed_score,
        sentiment_analyed_articles,
        overall_summary
    )
