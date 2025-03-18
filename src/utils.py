
from .modules.extract_articles import extract_articles

from .modules.analysis import sentiment_analysis
from .modules.analysis import comparative_analysis


def expose(company_name):
    """Root function which will be exposed"""
    extracted_articles = extract_articles(company_name)

    sentiment_analyed_articles = sentiment_analysis(extracted_articles)

    comparative_analyed_score = comparative_analysis(sentiment_analyed_articles)

    return comparative_analyed_score, sentiment_analyed_articles
