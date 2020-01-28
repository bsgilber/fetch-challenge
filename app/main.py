from fastapi import FastAPI
from pydantic import BaseModel

from . import NGramCompare


# TODO: add optional parameters
class DocsIn(BaseModel):
    doc1: str
    doc2: str
    ngram_length: int


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Fetch"}
 

@app.post("/compare/ngram/")
async def calculate_similarity_metric(docs: DocsIn):
    results = NGramCompare.NGramCompare(
    	left_doc = docs.doc1,
    	right_doc = docs.doc2,
    	ngram_length = docs.ngram_length
    	).compare()
    return {'similarity_score doc1 to doc2': results[0],'similarity_score doc2 to doc1': results[1]}
