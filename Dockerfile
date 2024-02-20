FROM python:slim-bookworm

WORKDIR /app

COPY microservice-http/ /app

# Installation des packages Python
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "app.py"]
