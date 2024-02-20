FROM python:slim-bookworm

# ENV APP_PORT=${APP_PORT}
# ENV MESSAGE=${MESSAGE}

WORKDIR /app

COPY microservice-http/ /app

# Installation des packages Python
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "app.py"]
