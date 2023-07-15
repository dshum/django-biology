FROM python:3.11.2-slim

# Install dependencies
RUN apt-get update && apt-get install -y gettext

ADD requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir

ADD ./src /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000