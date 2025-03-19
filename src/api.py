"""This module provides API"""

from typing import Union

from fastapi import FastAPI

from .utils import expose


app = FastAPI()


@app.get("/v1/company")
def get_data(q: Union[str, None] = None):
    """GET request which accepts company name and returns response"""
    try:
        score, articles = expose(q)
        return {
            "status": 200,
            "score": score,
            "count": len(articles),
            "articles": articles,
        }
    except e:
        return {"status": 500, "msg": "Please wait while we fix the error"}
