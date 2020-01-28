FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

WORKDIR /app

RUN pip install fastapi

COPY . .