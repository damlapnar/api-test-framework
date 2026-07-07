FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BASE_URL=https://dummyjson.com
ENV PYTHONPATH=/app

CMD ["pytest", "-v", "--html=reports/report.html", "--self-contained-html", "-m", "smoke"]
