FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .