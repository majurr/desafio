FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get clean

RUN python3 -m pip install -U pip
RUN python3 -m pip install poetry
RUN poetry config virtualenvs.create false

COPY ./poetry.lock pyproject.toml /app/
RUN poetry install

COPY . /app
