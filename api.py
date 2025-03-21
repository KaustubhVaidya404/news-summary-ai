"""This module provides API"""

from typing import Union

from fastapi import FastAPI

from utils import expose

from modules.text_to_speech import text_to_speech_file

import asyncio

app = FastAPI()


@app.get("/v1/company")
async def get_data(q: Union[str, None] = None, sentiment_type: Union[str, None] = None):
    """GET request which accepts company name and returns response"""
    try:
        score, articles, summary = expose(q)
        audio_path = await text_to_speech_file(summary)
        if sentiment_type is None:
            return {
                "company": q,
                "score": score,
                "count": len(articles),
                "summary": summary,
                "articles": articles,
                "audio_path": audio_path
            }
        else:
            if sentiment_type == "positive":
                filtered_articles = [
                    article for article in articles
                    if article["sentiment"]["pos"] > 0
                ]
            elif sentiment_type == "negative":
                filtered_articles = [
                    article for article in articles
                    if article["sentiment"]["neg"] > 0
                ]
            elif sentiment_type == "neutral":
                filtered_articles = [
                    article for article in articles
                    if article["sentiment"]["neu"] > 0
                ]
            else:
                return {
                    "msg": (
                        f"Invalid sentiment_type: {sentiment_type}. "
                        "Please use 'positive', 'negative', or 'neutral'."
                    )
                }

            return {
                "company": q,
                "score": score,
                "count": len(filtered_articles),
                "summary": summary,
                "articles": filtered_articles,
                "audio_path": audio_path
            }
    except Exception as e:
        return {"msg": f"An error occurred: {str(e)}"}
