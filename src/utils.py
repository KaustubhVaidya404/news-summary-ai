from bs4 import BeautifulSoup
import requests

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



nltk.download('vader_lexicon')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def extract_articles(company_name):
    """Function to extract the articles from times of india website"""

    url = f"https://timesofindia.indiatimes.com/topic/{company_name}/news"

    try:
        result = requests.get(url, headers=headers)

        soup = BeautifulSoup(result.text, 'html.parser')

        data = soup.find_all('div', class_='VXBf7')
        if data:
            articles = []
            for div in data:

                title = div.find('div', class_='fHv_i').get_text(strip=True) if div.find('div', class_='fHv_i') else "No title"
                date = div.find('div', class_='ZxBIG').get_text(strip=True) if div.find('div', class_='ZxBIG') else "No date"
                summary = div.find('p', class_='oxXSK').get_text(strip=True) if div.find('p', class_='oxXSK') else "No summary"

                article = {
                    'title': title,
                    'date': date,
                    'summary': summary
                }
                articles.append(article)
            return articles
        else:
            return "No data found."
    except(e):
        return f"Failed to fetch page. Status code: {result.status_code} {e}"


def sentiment_analysis(extracted_articles):
    """Function to perform sentiment analysis"""
    analyzer = SentimentIntensityAnalyzer()

    articles = extracted_articles

    for article in articles:
        sentence = article['title'] + article['summary']
        sentiment = analyzer.polarity_scores(sentence)
        article.update({'sentiment': sentiment})

    return articles


def comparative_analysis(sentiment_analyed):
    """Function to perform comparative sentiment analysis"""
    articles = sentiment_analyed

    total_articles = len(articles)
    positive_count = len([article for article in articles if article['sentiment']['compound'] > 0.05])
    negative_count = len([article for article in articles if article['sentiment']['compound'] < -0.05])
    neutral_count = total_articles - positive_count - negative_count

    positive_percentage = (positive_count / total_articles) * 100
    negative_percentage = (negative_count / total_articles) * 100
    neutral_percentage = (neutral_count / total_articles) * 100

    return {"positive": positive_percentage, "negative": negative_percentage, "neutral": neutral_percentage}


def expose(company_name):
    """Root function which will be exposed"""
    extracted_articles = extract_articles(company_name)

    sentiment_analyed_articles = sentiment_analysis(extracted_articles)

    comparative_analyed_score = comparative_analysis(sentiment_analyed_articles)

    return comparative_analyed_score, sentiment_analyed_articles
