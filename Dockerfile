# syntax=docker/dockerfile:1.4
# FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
# RUN --mount=type=cache,target=/root/.cache/pip \
        # pip install -r requirements.txt
RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]