FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app

RUN pip install fastapi

COPY . .