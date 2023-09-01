FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /omni/

WORKDIR /omni/

COPY . .

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN adduser -D user
USER user
