# Fetch Code Challenge: Document Similarity

Created a hacky verion of this Gensim NGram model, which I've used before to POC an NLP initiative -- https://radimrehurek.com/gensim/models/phrases.html

### Explicit Answers
Do you count punctuation or only words?
> I included commas, periods, and apostrophes, as well as words.

Which words should matter in the similarity comparison?
> I excluded common english stop words to cut down on noise, all other words matter.

Do you care about the ordering of words?
> To a degree. For a perfect match of 1.0 order can matter, but if a sufficiently small NGram number is chosen a very high similarity score can be achieved -- will be text dependent.

What metric do you use to assign a numerical value to the similarity?
> A ratio of matching NGrams divided by the number of unique NGrams between both documents, calculate in both directions. If we have 2 documents A and B, then Similarity = Intersection(A,B)/Union(A,B). In this calculation order of the Intersection function matters to defend against the edge case where A is a subset of B.

What type of data structures should be used?  (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.)
> List and list comprehension were primarily used. Dictionaries were used, but in a trivial manner.

### How to run it

##### Locally
```
docker build -t crunchy-similarity-api .
docker run --net=host -d -p 80:80 crunchy-similarity-api

echo '{"doc1": "text", "doc2": "text", "ngram_length": 5}' | curl -H "Content-Type: application/json" -X POST -d @- http://127.0.0.1:8000/compare/ngram/
```

##### From Dockerhub
```
docker pull adockerimage:latest
docker run --net=host -d -p 80:80 adockerimage

echo '{"doc1": "text", "doc2": "text", "ngram_length": 5}' | curl -H "Content-Type: application/json" -X POST -d @- http://127.0.0.1:8000/compare/ngram/
```


### Resources
FastAPI, I have only ever used Flask to build an API, this very good documentation.
https://github.com/tiangolo/fastapi

And the FastAPI Docker resource
https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

Boiler plate NGram code
http://www.albertauyeung.com/post/generating-ngrams-python/

My favorite ETL design pattern
https://refactoring.guru/design-patterns/template-method