FROM python:3.8-alpine
ENV PYTHONBUFFERED 1

RUN apk update \
    && apk add postgresql-dev 

RUN mkdir /final_ss

WORKDIR /final_ss

COPY requirements.txt /final_ss/

RUN python -m pip install -r requirements.txt

COPY . /final_ss/
