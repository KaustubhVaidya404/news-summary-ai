"""This module perform sentiment analysis and comparative sentiment analysis"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download("vader_lexicon")


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
        [article for article in articles if article["sentiment"]["compound"] > 0.05]
    )
    negative_count = len(
        [article for article in articles if article["sentiment"]["compound"] < -0.05]
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


def analysis(extracted_articles):
    sentiment_analyed_articles = sentiment_analysis(extracted_articles)

    comparative_analyed_score = comparative_analysis(
        sentiment_analyed_articles)

    return comparative_analyed_score, sentiment_analyed_articles
