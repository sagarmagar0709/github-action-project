#1 2Simple Python App..
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask

CMD ["python", "app.py"]

