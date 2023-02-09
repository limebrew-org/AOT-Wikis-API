FROM python:3.9.0

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .