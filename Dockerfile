FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
COPY requirements-dev.txt /code/

RUN python -m pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/
