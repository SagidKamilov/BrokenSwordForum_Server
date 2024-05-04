FROM python:3.11.1-slim

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .

RUN alembic revision --autogenerate -m "initial migration"
RUN alembic upgrade head
