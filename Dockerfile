FROM python:slim-bookworm

ENV APP_PORT=9999
ENV MESSAGE="testMsg"

WORKDIR /app

COPY microservice-http/ /app

# Installation des packages Python
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "app.py"]
