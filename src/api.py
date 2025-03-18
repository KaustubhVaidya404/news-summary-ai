from typing import Union
from fastapi import FastAPI
from .utils import expose

app = FastAPI()


@app.get("/v1/company")
def get_data(q: Union[str, None] = None):
    score, articles = expose(q)
    return {"score": score, "articles": articles}
