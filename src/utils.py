"""This module is single thread for analysis generation"""

try:
    from .modules.extract_articles import extract_articles
    from .modules.analysis import analysis
except:
    from modules.extract_articles import extract_articles
    from modules.analysis import analysis


def expose(company_name):
    """Root function which will be exposed"""
    extracted_articles = extract_articles(company_name)

    comparative_analyed_score, sentiment_analyed_articles = analysis(
        extracted_articles)

    return comparative_analyed_score, sentiment_analyed_articles
