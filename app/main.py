from fastapi import FastAPI
from pydantic import BaseModel

from NGramCompare import NGramCompare


# TODO: add optional parameters
class DocsIn(BaseModel):
    doc1: str
    doc2: str
    ngram_length: int


app = FastAPI()


@app.post("/compare/ngram/")
async def calculate_similarity_metric(docs: DocsIn):
    return {'similarity_score': NGramCompare(docs.doc1, docs.doc2, docs.ngram_length).compare()}
