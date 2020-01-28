from fastapi import FastAPI
from pydantic import BaseModel

from . import NGramCompare

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__file__)

# TODO: add optional parameters available in BaseDocSimilarity
# TODO: add more logging and more error handling
class DocsIn(BaseModel):
    doc1: str
    doc2: str
    ngram_length: int = 1


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Fetch"}
 

@app.post("/compare/ngram/")
async def calculate_similarity_metric(docs: DocsIn):
    """From a POST request body, return similarity of documents provided"""
    try:
        results = NGramCompare.NGramCompare(
            left_doc = docs.doc1,
            right_doc = docs.doc2,
            ngram_length = docs.ngram_length
            ).compare()
        return {'similarity_score doc1 to doc2': results[0],'similarity_score doc2 to doc1': results[1]}
    except (ZeroDivisionError, ValueError):
        # TODO: read docs and figure out how to return 4XX response
        msg = "NGram length [{0}] is not allowed, must be > 0.".format(docs.ngram_length)
        logger.error(msg)
        return {'Error': msg}
