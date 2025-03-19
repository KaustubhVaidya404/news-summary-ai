"""This module provides API"""

from typing import Union

from fastapi import FastAPI

from .utils import expose


app = FastAPI()


@app.get("/v1/company")
def get_data(q: Union[str, None] = None):
    """GET request which accepts company name and returns response"""
    try:
        score, articles, summary = expose(q)
        return {
            "company": q,
            "score": score,
            "count": len(articles),
            "summary": summary,
            "articles": articles
        }
    except:
        return {"msg": "Please wait while we fix the error"}
